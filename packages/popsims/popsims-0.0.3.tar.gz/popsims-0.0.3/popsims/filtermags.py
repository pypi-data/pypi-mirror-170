
################################
#contains absolute magnitude relation generation scripts
#includes copied functions from splat
##############################

from .filterinitialize import *
from .core import DATA_FOLDER
import numpy
from astropy import units as u            # standard units
from astropy import constants as const        # physical constants in SI units
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from scipy.integrate import trapz        # for numerical integration
from scipy.interpolate import interp1d
import copy
import os

# splat functions and constants

VEGAFILE='vega_kurucz.txt'
FILTER_FOLDER=DATA_FOLDER+ '/filters/'

def checkFilter(filt,verbose=True):
    output = False
    f = copy.deepcopy(filt)
    f = f.replace(' ','_').upper()
    for k in list(FILTERS.keys()):
        if f==k.upper() or f.lower() in FILTERS[k]['altnames']:
            output = k
    if output == False and verbose == True: 
        print('\nFilter '+filt+' not currently available for SPLAT')
        filterInfo()
    return output

def checkFilterName(f,verbose=False):
    '''
    Purpose: 
        Checks that an input filter name is one of the available filters, including a check of alternate names
    Required Inputs:
        :param: filter: A string containing the filter name to be checked. This should be one of the names listed in `splat.FILTERS.keys()` or name alternates
        
    Optional Inputs:
        None
    Output:
        A string containing SPLAT's default name for a given filter, or False if that filter is not present
    Example:
    >>> import splat
    >>> print(splat.checkFilterName('2MASS_KS'))
        2MASS_KS
    >>> print(splat.checkFilterName('2mass k'))
        2MASS_KS
    >>> print(splat.checkFilterName('somethingelse'))
        False
    '''
    output = False
    if not isinstance(f,str):
        return output
    for k in list(FILTERS.keys()):
        if f.lower().replace(' ','_').replace('-','_') == k.lower() or f.lower().replace(' ','_') in [x.lower() for x in FILTERS[k]['altname']]:
            output = k
    if verbose==True and output==False:
        print('\nSPLAT does not contain the filter {}'.format(f))
    return output

def filterProfile(filt,**kwargs):
    '''
    :Purpose: Retrieve the filter profile for a SPLAT filter. Returns two arrays: the filter wavelength and filter transmission curve.
    :param filter: String giving the name of one of the predefined filters listed in splat.FILTERS.keys() (required)
    
    :param filterFolder: folder containing the filter transmission files (optional, default = splat.FILTER_FOLDER)
    :Example:
    >>> import splat
    >>> import splat.photometry as spphot
    >>> sp = splat.getSpectrum(shortname='1507-1627')[0]
    >>> sp.fluxCalibrate('2MASS J',14.5)
    >>> spphot.filterMag(sp,'MKO J')
        (14.345894376898123, 0.027596454828421831)
    '''
# keyword parameters
    filterFolder = kwargs.get('filterFolder',FILTER_FOLDER)
    if not os.path.exists(filterFolder):
        filterFolder = FILTER_FOLDER

# check that requested filter is in list
    f0 = checkFilterName(filt, verbose=True)
    if f0 == False: raise ValueError
    filt = f0

# read in filter
    fwave,ftrans = numpy.genfromtxt(os.path.normpath(filterFolder+FILTERS[filt]['file']), comments='#', unpack=True, missing_values = ('NaN','nan'), filling_values = (numpy.nan))
#    print(type(fwave),type(ftrans),isinstance(fwave,numpy.ndarray),isinstance(ftrans,numpy.ndarray),not isinstance(fwave,numpy.ndarray) or not isinstance(ftrans,numpy.ndarray))
    if not isinstance(fwave,numpy.ndarray) or not isinstance(ftrans,numpy.ndarray):
        raise ValueError('\nProblem reading in {}'.format(filterFolder+FILTERS[filt]['file']))
    fwave = fwave[~numpy.isnan(ftrans)]*u.micron
    ftrans = ftrans[~numpy.isnan(ftrans)]
    return fwave,ftrans

def filterMag(wave, flux, noise,  flux_unit, filt,*args,**kwargs):
    '''
    :Purpose: 
    Determine the photometric magnitude of a source based on its
    spectrum. Spectral fluxes are convolved with the filter profile specified by
    the ``filter`` input.  By default this filter is also
    convolved with a model of Vega to extract Vega magnitudes,
    but the user can also specify AB magnitudes, photon flux or energy flux.
    :Required Parameters:
        **filter**: String giving name of filter, which can either be one of the predefined filters listed in splat.FILTERS.keys() or a custom filter name
    :Optional Parameters:
    
        **custom** = None: A 2 x N vector array specifying the wavelengths and transmissions for a custom filter
        **notch** = None: A 2 element array that specifies the lower and upper wavelengths for a notch filter (100% transmission within, 0% transmission without)
        **vega** = True: compute Vega magnitudes (may be set by filter)
        **ab** = False: compute AB magnitudes (may be set by filter)
        **energy** = False: compute energy flux
        **photon** = False: compute photon flux
        **filterFolder** = splat.FILTER_FOLDER: folder containing the filter transmission files
        **vegaFile** = 'vega_kurucz.txt': name of file containing Vega flux file, must be within ``filterFolder``
        **nsamples** = 100: number of samples to use in Monte Carlo error estimation
        **info** = False: List the predefined filter names available
        **verbose** = True: List the predefined filter names available
    :Example:
    >>> import splat
    >>> import splat.photometry as spphot
    >>> sp = splat.getSpectrum(shortname='1507-1627')[0]
    >>> fluxCalibrate('2MASS J',14.5)
    >>> spphot.filterMag(sp,'MKO J')
        (14.345894376898123, 0.027596454828421831)
    '''
# keyword parameters
    filterFolder = kwargs.get('filterFolder',FILTER_FOLDER)
    vegaFile = kwargs.get('vegaFile',VEGAFILE)
    info = kwargs.get('info',False)
    custom = kwargs.get('custom',False)
    notch = kwargs.get('notch',False)
    vega = kwargs.get('vega',True)
    ab = kwargs.get('ab',not vega)
    rsr = kwargs.get('rsr',False)
    nsamples = kwargs.get('nsamples',100)
    verbose = kwargs.get('verbose',False)


# check that requested filter is in list
    if isinstance(custom,bool) and isinstance(notch,bool):
        f0 = checkFilterName(filt,verbose=True)
        if f0 == False: 
            return numpy.nan, numpy.nan
        filt = f0
        
# reset filter calculation methods based on filter design
        if 'ab' in FILTERS[filt]['method']: 
            ab = kwargs.get('ab',True)
            vega = not ab
        if 'vega' in FILTERS[filt]['method']: 
            vega = kwargs.get('vega',True)
            ab = not vega
        rsr = FILTERS[filt]['rsr']

# other possibilities
    photons = kwargs.get('photons',False)
    photons = kwargs.get('photon',photons)
    energy = kwargs.get('energy',False)
    energy = kwargs.get('flux',energy)
    if (photons or energy):
        vega = False
        ab = False
    if photons: energy = False
    if energy: photons = False


# Read in filter
    if isinstance(custom,bool) and isinstance(notch,bool):
        fwave,ftrans = filterProfile(filt,**kwargs)
# notch filter
    elif isinstance(custom,bool) and isinstance(notch,list):
        dn = (notch[1]-notch[0])/1000
        fwave = numpy.arange(notch[0]-5.*dn,notch[1]+5.*dn,dn)
        ftrans = numpy.zeros(len(fwave))
        ftrans[numpy.where(numpy.logical_and(fwave >= notch[0],fwave <= notch[1]))] = 1.
# custom filter
    else:
        fwave,ftrans = custom[0],custom[1]

# units
    if isinstance(fwave,u.quantity.Quantity) == True:
        fwave = fwave.to(u.micron)
    else:
        fwave = fwave*u.micron

# check that spectrum and filter cover the same wavelength ranges
    if numpy.nanmax(fwave) < numpy.nanmin(wave) or numpy.nanmin(fwave) > numpy.nanmax(wave):
        if verbose==True: print('\nWarning: no overlap between spectrum and filter {}'.format(filt))
        return numpy.nan, numpy.nan

    if numpy.nanmin(fwave) < numpy.nanmin(wave) or numpy.nanmax(fwave) > numpy.nanmax(wave):
        if verbose==True: print('\nWarning: spectrum does not span full filter profile for {}'.format(filt))

# interpolate spectrum onto filter wavelength function
    wgood = numpy.where(~numpy.isnan(noise))
    if len(wave[wgood]) > 0:
        d = interp1d(wave[wgood].value,flux[wgood].value,bounds_error=False,fill_value=0.)
        n = interp1d(wave[wgood].value,noise[wgood].value,bounds_error=False,fill_value=0)
# catch for models
    else:
        if verbose==True: print('\nWarning: data values in range of filter {} have no uncertainties'.format(filt))
        d = interp1d(wave.value,flux.value,bounds_error=False,fill_value=0.)
        n = interp1d(wave.value,flux.value*1.e-9,bounds_error=False,fill_value=0.)

    result = []
    if (vega):
# Read in Vega spectrum
        vwave,vflux = numpy.genfromtxt(os.path.normpath(filterFolder+vegaFile), comments='#', unpack=True, \
            missing_values = ('NaN','nan'), filling_values = (numpy.nan))
        vwave = vwave[~numpy.isnan(vflux)]*u.micron
        vflux = vflux[~numpy.isnan(vflux)]*(u.erg/(u.cm**2 * u.s * u.micron))
        vflux.to(flux_unit,equivalencies=u.spectral_density(vwave))
# interpolate Vega onto filter wavelength function
        v = interp1d(vwave.value,vflux.value,bounds_error=False,fill_value=0.)
        if rsr:
            val = -2.5*numpy.log10(trapz(ftrans*fwave.value*d(fwave.value),fwave.value)/trapz(ftrans*fwave.value*v(fwave.value),fwave.value))
        else:
            val = -2.5*numpy.log10(trapz(ftrans*d(fwave.value),fwave.value)/trapz(ftrans*v(fwave.value),fwave.value))
        for i in numpy.arange(nsamples):
#            result.append(-2.5*numpy.log10(trapz(ftrans*numpy.random.normal(d(fwave),n(fwave))*flux_unit,fwave)/trapz(ftrans*v(fwave)*flux_unit,fwave)))
            if rsr:
                result.append(-2.5*numpy.log10(trapz(ftrans*fwave.value*(d(fwave.value)+numpy.random.normal(0,1.)*n(fwave.value)),fwave.value)/trapz(ftrans*fwave.value*v(fwave.value),fwave.value)))
            else:
                result.append(-2.5*numpy.log10(trapz(ftrans*(d(fwave.value)+numpy.random.normal(0,1.)*n(fwave.value)),fwave.value)/trapz(ftrans*v(fwave.value),fwave.value)))
        outunit = 1.

    elif (ab):
        nu = wave.to('Hz',equivalencies=u.spectral())
        fnu = flux.to('Jy',equivalencies=u.spectral_density(wave))
        noisenu = noise.to('Jy',equivalencies=u.spectral_density(wave))
        filtnu = fwave.to('Hz',equivalencies=u.spectral())
        fconst = 3631*u.jansky
        d = interp1d(nu.value,fnu.value,bounds_error=False,fill_value=0.)
        n = interp1d(nu.value,noisenu.value,bounds_error=False,fill_value=0.)
        b = trapz((ftrans/filtnu.value)*fconst.value,filtnu.value)
        val = -2.5*numpy.log10(trapz(ftrans*d(filtnu.value)/filtnu.value,filtnu.value)/b)
        for i in numpy.arange(nsamples):
            a = trapz(ftrans*(d(filtnu.value)+numpy.random.normal(0,1)*n(filtnu.value))/filtnu.value,filtnu.value)
            result.append(-2.5*numpy.log10(a/b))
        outunit = 1.

    elif (energy):
        outunit = u.erg/u.s/u.cm**2
        if rsr:
            a = trapz(ftrans*fwave.value*d(fwave.value),fwave.value)*wave.unit*flux.unit
            b = trapz(ftrans*fwave.value,fwave.value)*wave.unit
            c = trapz(ftrans*fwave.value*fwave.value,fwave.value)*wave.unit*wave.unit
            val = (a/b * c/b).to(outunit).value
        else:
            a = trapz(ftrans*d(fwave.value),fwave.value)*wave.unit*flux.unit
            b = trapz(ftrans,fwave.value)*wave.unit
            c = trapz(ftrans*fwave.value,fwave.value)*wave.unit*wave.unit
            val = (a/b * c/b).to(outunit).value
        for i in numpy.arange(nsamples):
            if rsr:
                result.append((trapz(ftrans*fwave.value*(d(fwave.value)+numpy.random.normal(0,1.)*n(fwave.value)),fwave.value)*wave.unit*flux.unit).to(outunit).value)
            else:
                result.append((trapz(ftrans*(d(fwave.value)+numpy.random.normal(0,1.)*n(fwave.value)),fwave.value)*wave.unit*flux.unit).to(outunit).value)

    elif (photons):
        outunit = 1./u.s/u.cm**2
        convert = const.h.to('erg s')*const.c.to('micron/s')
        val = (trapz(ftrans*fwave.value*convert.value*d(fwave.value),fwave.value)*wave.unit*flux.unit*convert.unit).to(outunit).value
        for i in numpy.arange(nsamples):
            result.append((trapz(ftrans*fwave.value*convert.value*(d(fwave.value)+numpy.random.normal(0,1.)*n(fwave.value)),fwave.value)*wave.unit*flux.unit*convert.unit).to(outunit).value)
    else:
        raise NameError('\nfilterMag not given a correct physical quantity (vega, ab, energy, photons) to compute photometry\n\n')


#    val = numpy.nanmean(result)*outunit
    err = numpy.nanstd(result)
    if len(wave[wgood]) == 0:
        err = 0.
    return val*outunit,err*outunit


def vegaToAB(filt,vegafile=VEGAFILE,filterfolder=FILTER_FOLDER,custom=False,notch=False,rsr=False,**kwargs):

# check that requested filter is in list
    if isinstance(custom,bool) and isinstance(notch,bool):
        f0 = checkFilterName(filt,verbose=True)
        if f0 == False: 
            return numpy.nan, numpy.nan
        filt = f0
        rsr = FILTERS[filt]['rsr']

# Read in filter
    if isinstance(custom,bool) and isinstance(notch,bool):
        fwave,ftrans = filterProfile(filt,**kwargs)
# notch filter
    elif isinstance(custom,bool) and isinstance(notch,list):
        dn = (notch[1]-notch[0])/1000
        fwave = numpy.arange(notch[0]-5.*dn,notch[1]+5.*dn,dn)
        ftrans = numpy.zeros(len(fwave))
        ftrans[numpy.where(numpy.logical_and(fwave >= notch[0],fwave <= notch[1]))] = 1.
# custom filter
    else:
        fwave,ftrans = custom[0],custom[1]


# Read in Vega spectrum
    vwave,vflux = numpy.genfromtxt(os.path.normpath(filterfolder+vegafile), comments='#', unpack=True, \
        missing_values = ('NaN','nan'), filling_values = (numpy.nan))
    vwave = vwave[~numpy.isnan(vflux)]*u.micron
    vflux = vflux[~numpy.isnan(vflux)]*(u.erg/(u.cm**2 * u.s * u.micron))

# trim spectrum
    vflux = vflux[vwave>=numpy.nanmin(fwave)]
    vwave = vwave[vwave>=numpy.nanmin(fwave)]
    vflux = vflux[vwave<=numpy.nanmax(fwave)]
    vwave = vwave[vwave<=numpy.nanmax(fwave)]

# convert to fnu
    nu = vwave.to('Hz',equivalencies=u.spectral())
    fnu = vflux.to('Jy',equivalencies=u.spectral_density(vwave))
    filtnu = fwave.to('Hz',equivalencies=u.spectral())
    fconst = 3631*u.jansky
    d = interp1d(nu.value,fnu.value,bounds_error=False,fill_value=0.)
    b = trapz((ftrans/filtnu.value)*fconst.value,filtnu.value)
    return -2.5*numpy.log10(trapz(ftrans*d(filtnu.value)/filtnu.value,filtnu.value)/b)



def filterInfo(*args,**kwargs):
    '''
    :Purpose: Prints out the current list of filters in the SPLAT reference library.
    '''

    verbose = kwargs.get('verbose',True)

    if len(args) > 0: 
        fname = list(args)
    elif kwargs.get('filter',False) != False: 
        fname = kwargs['filter']
    else: 
        fname = sorted(list(FILTERS.keys()))
    if isinstance(fname,list) == False: 
        fname = [fname]

    output = {}
    for k in fname:
        f = checkFilterName(k)
        if f != False:
            output[f] = {}
            output[f]['description'] = FILTERS[f]['description']
            output[f]['zeropoint'] = FILTERS[f]['zeropoint']
            fwave,ftrans = filterProfile(f,**kwargs)
            try:
                fwave = fwave.to(u.micron)
            except:
                fwave = fwave*u.micron
            fw = fwave[numpy.where(ftrans > 0.01*numpy.nanmax(ftrans))]
            ft = ftrans[numpy.where(ftrans > 0.01*numpy.nanmax(ftrans))]
            fw05 = fwave[numpy.where(ftrans > 0.5*numpy.nanmax(ftrans))]
            output[f]['lambda_mean'] = trapz(ft*fw,fw)/trapz(ft,fw)
            output[f]['lambda_pivot'] = numpy.sqrt(trapz(fw*ft,fw)/trapz(ft/fw,fw))
            output[f]['lambda_central'] = 0.5*(numpy.max(fw)+numpy.min(fw))
            output[f]['lambda_fwhm'] = numpy.max(fw05)-numpy.min(fw05)
            output[f]['lambda_min'] = numpy.min(fw)
            output[f]['lambda_max'] = numpy.max(fw)
            if verbose ==True: 
                print(f.replace('_',' ')+': '+output[f]['zeropoint'])
                print('Zeropoint = {} Jy'.format(output[f]['zeropoint']))
                print('Central wavelength: = {:.3f}'.format(output[f]['lambda_central']))
                print('Mean wavelength: = {:.3f}'.format(output[f]['lambda_mean']))
                print('Pivot point: = {:.3f}'.format(output[f]['lambda_pivot']))
                print('FWHM = {:.3f}'.format(output[f]['lambda_fwhm']))
                print('Wavelength range = {:.3f} to {:.3f}\n'.format(output[f]['lambda_min'],output[f]['lambda_max']))             
        else:
        	if verbose ==True: print('  Filter {} not in SPLAT filter list'.format(k))
    kys = list(output.keys())
    if len(kys) == 1: return output[kys[0]]
    else: return output


def filterProperties(filt,**kwargs):
    '''
    :Purpose: Returns a dictionary containing key parameters for a particular filter.
    :param filter: name of filter, must be one of the specifed filters given by splat.FILTERS.keys()
    :type filter: required
    :param verbose: print out information about filter to screen
    :type verbose: optional, default = True
    :Example:
    >>> import splat
    >>> data = splat.filterProperties('2MASS J')
    Filter 2MASS J: 2MASS J-band
    Zeropoint = 1594.0 Jy
    Pivot point: = 1.252 micron
    FWHM = 0.323 micron
    Wavelength range = 1.066 to 1.442 micron
    >>> data = splat.filterProperties('2MASS X')
    Filter 2MASS X not among the available filters:
      2MASS H: 2MASS H-band
      2MASS J: 2MASS J-band
      2MASS KS: 2MASS Ks-band
      BESSEL I: Bessel I-band
      FOURSTAR H: FOURSTAR H-band
      FOURSTAR H LONG: FOURSTAR H long
      FOURSTAR H SHORT: FOURSTAR H short
      ...
    '''
    filterFolder = kwargs.get('filterFolder',FILTER_FOLDER)
    if not os.path.exists(filterFolder):
        filterFolder = SPLAT_URL+FILTER_FOLDER

# check that requested filter is in list
    filt = checkFilterName(filt)
    if filt == False: return None

    report = {}
    report['name'] = filt
    report['description'] = FILTERS[filt]['description']
    report['zeropoint'] = FILTERS[filt]['zeropoint']
    report['method'] = FILTERS[filt]['method']
    report['rsr'] = FILTERS[filt]['rsr']
    fwave,ftrans = filterProfile(filt,**kwargs)
    try:
        fwave = fwave.to(u.micron)
    except:
        fwave = fwave*u.micron
    fw = fwave[numpy.where(ftrans > 0.01*numpy.nanmax(ftrans))]
    ft = ftrans[numpy.where(ftrans > 0.01*numpy.nanmax(ftrans))]
    fw05 = fwave[numpy.where(ftrans > 0.5*numpy.nanmax(ftrans))]
#        print(trapz(ft,fw))
#        print(trapz(fw*ft,fw))
    report['lambda_mean'] = trapz(ft*fw,fw)/trapz(ft,fw)
    report['lambda_pivot'] = numpy.sqrt(trapz(fw*ft,fw)/trapz(ft/fw,fw))
    report['lambda_central'] = 0.5*(numpy.max(fw)+numpy.min(fw))
    report['lambda_fwhm'] = numpy.max(fw05)-numpy.min(fw05)
    report['lambda_min'] = numpy.min(fw)
    report['lambda_max'] = numpy.max(fw)
    report['wave'] = fwave
    report['transmission'] = ftrans
# report values out
    if kwargs.get('verbose',False):
        print('\nFilter '+filt+': '+report['description'])
        print('Zeropoint = {} Jy'.format(report['zeropoint']))
        print('Pivot point: = {:.3f}'.format(report['lambda_pivot']))
        print('FWHM = {:.3f}'.format(report['lambda_fwhm']))
        print('Wavelength range = {:.3f} to {:.3f}\n'.format(report['lambda_min'],report['lambda_max']))
    return report


def magToFlux(mag,filt,**kwargs):
    '''
    :Purpose: Converts a magnitude into an energy, and vice versa.
    :param mag: magnitude on whatever system is defined for the filter or provided (required)
    :param filter: name of filter, must be one of the specifed filters given by splat.FILTERS.keys() (required)
    :param reverse: convert energy into magnitude instead (optional, default = False)
    :param ab: magnitude is on the AB system (optional, default = filter preference)
    :param vega: magnitude is on the Vega system (optional, default = filter preference)
    :param rsr: magnitude is on the Vega system (optional, default = filter preference)
    :param units: units for energy as an astropy.units variable; if this conversion does not work, the conversion is ignored (optional, default = erg/cm2/s)
    :param verbose: print out information about filter to screen (optional, default = False)
    WARNING: THIS CODE IS ONLY PARTIALLY COMPLETE
    '''

# keyword parameters
    filterFolder = kwargs.get('filterFolder',FILTER_FOLDER)
    if not os.path.exists(filterFolder):
        filterFolder = SPLAT_URL+FILTER_FOLDER
    vegaFile = kwargs.get('vegaFile','vega_kurucz.txt')
    vega = kwargs.get('vega',True)
    ab = kwargs.get('ab',not vega)
    rsr = kwargs.get('rsr',False)
    nsamples = kwargs.get('nsamples',100)
    custom = kwargs.get('custom',False)
    notch = kwargs.get('notch',False)
    base_unit = u.erg/(u.cm**2 * u.s)
    return_unit = kwargs.get('unit',base_unit)
    e_mag = kwargs.get('uncertainty',0.)
    e_mag = kwargs.get('unc',e_mag)
    e_mag = kwargs.get('e_mag',e_mag)
    if not isinstance(mag,u.quantity.Quantity): mag=mag*u.s/u.s
    if not isinstance(e_mag,u.quantity.Quantity): e_mag=e_mag*mag.unit

# check that requested filter is in list
    filt = checkFilterName(filt)
    if filt == False: return numpy.nan, numpy.nan

# reset filter calculation methods based on filter design
    if 'ab' in FILTERS[filt]['method']: 
        ab = kwargs.get('ab',True)
        vega = not ab
    if 'vega' in FILTERS[filt]['method']: 
        vega = kwargs.get('vega',True)
        ab = not vega
    if 'rsr' in FILTERS[filt]['method']: 
        rsr = kwargs.get('rsr',True)


# Read in filter
    if isinstance(custom,bool) and isinstance(notch,bool):
        fwave,ftrans = filterProfile(filt,**kwargs)
# notch filter
    elif isinstance(custom,bool) and isinstance(notch,list):
        dn = (notch[1]-notch[0])/1000
        fwave = numpy.arange(notch[0]-5.*dn,notch[1]+5.*dn,dn)*u.micron
        ftrans = numpy.zeros(len(fwave))
        ftrans[numpy.where(numpy.logical_and(fwave >= notch[0],fwave <= notch[1]))] = 1.
# custom filter
    else:
        fwave,ftrans = custom[0],custom[1]
    if isinstance(fwave,u.quantity.Quantity) == False: fwave=fwave*u.micron
    if isinstance(ftrans,u.quantity.Quantity) == True: ftrans=ftrans.value
    fwave = fwave[~numpy.isnan(ftrans)]
    ftrans = ftrans[~numpy.isnan(ftrans)]

    result = []
    err = 0.
# magnitude -> energy
    if kwargs.get('reverse',False) == False:
        
        if vega == True:
    # Read in Vega spectrum
            vwave,vflux = numpy.genfromtxt(os.path.normpath(filterFolder+vegaFile), comments='#', unpack=True, \
                missing_values = ('NaN','nan'), filling_values = (numpy.nan))
            vwave = vwave[~numpy.isnan(vflux)]*u.micron
            vflux = vflux[~numpy.isnan(vflux)]*(u.erg/(u.cm**2 * u.s * u.micron))
    # interpolate Vega onto filter wavelength function
            v = interp1d(vwave.value,vflux.value,bounds_error=False,fill_value=0.)
            if rsr: fact = trapz(ftrans*fwave.value*v(fwave.value),fwave.value)
            else: fact = trapz(ftrans*v(fwave.value),fwave.value)
            val = 10.**(-0.4*mag.value)*fact*u.erg/(u.cm**2 * u.s)
    # calculate uncertainty        
            if e_mag.value > 0.:
                for i in numpy.arange(nsamples): result.append(10.**(-0.4*(mag.value+numpy.random.normal(0,1.)*e_mag.value))*fact)
                err = (numpy.nanstd(result))*u.erg/(u.cm**2 * u.s)
            else: err = 0.*u.erg/(u.cm**2 * u.s)
        elif ab == True:
            fconst = 3631*u.jansky
            ftrans = (ftrans*fconst).to(u.erg/(u.cm**2 * u.s * u.micron),equivalencies=u.spectral_density(fwave))
            if rsr: fact = trapz(ftrans.value*fwave.value,fwave.value)
            else: fact = trapz(ftrans.value,fwave.value)
            val = (10.**(-0.4*mag.value)*fact)*u.erg/(u.cm**2 * u.s)
    # calculate uncertainty        
            if e_mag.value > 0.:
                for i in numpy.arange(nsamples): result.append(10.**(-0.4*(mag.value+numpy.random.normal(0,1.)*e_mag.value))*fact)
                err = (numpy.nanstd(result))*u.erg/(u.cm**2 * u.s)
            else: err = 0.*u.erg/(u.cm**2 * u.s)
        else:
            raise ValueError('\nmagToFlux needs vega or ab method specified')

# convert to desired energy units
#        try:
        val.to(return_unit)
        err.to(return_unit)
#        except:
#            print('\nWarning: unit {} is not an energy flux unit'.format(return_unit))
        try:
            val.to(base_unit)
            err.to(base_unit)
        except:
            print('\nWarning: cannot convert result to an energy flux unit'.format(base_unit))
            return numpy.nan, numpy.nan
        return val, err

# energy -> magnitude
# THIS NEEDS TO BE COMPLETED
    else:
        print('passed')
        pass
# check that input is an energy flux
#        try:
#            mag.to(base_unit)        
#            e_mag.to(base_unit)        
#        except:
#            raise ValueError('\nInput quantity unit {} is not a flux unit'.format(mag.unit))

