## Popsims
Ultracool dwarf population simulation routines

## Installation

```pip install popsims```


Notebook example: https://github.com/caganze/popsims/blob/main/examples/ExampleNotebook.ipynb


```python
#imports 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import popsims
from popsims.simulator import Population, pop_mags
from popsims.galaxy import Disk, Halo
from popsims.plot_style import  plot_style

plot_style()

import warnings
warnings.filterwarnings("ignore")
```


```python
#draw masses from a power-law IMF and uniform ages
#obtain temperatures from Baraffe et al.2003 relations
p=Population(evolmodel= 'baraffe2003',
              imf_power= -0.6,
              binary_fraction=0.2,
              age_range=[0.01, 14],
              mass_range=[0.01, 1])
    
evol_params= pd.DataFrame(p.simulate(int(1e5)))
```


```python
#Add absolute magnitudes from a relation on file
mags=pop_mags(evol_params.spt.values, keys=['LSST_Z'], object_type='dwarfs', get_from='spt')
evol_params['abs_LSST_Z']= mags['abs_LSST_Z'].values
```


```python
#define a galaxy density model and draw distances in a given direction
disk= Disk(H=300, L=2600)
tdisk=Disk(H=900, L=3600)
halo= Halo()
model= disk+0.12*tdisk+(1/400)*halo

#pick distances from 0.1pc to 10kpc at l=45 deg and b=0
dists= model.sample_distances(0.1, 10_000,len(evol_params.mass), l=np.pi/4, b=0.0,  dsteps=10_000 )

#compute magnitudes from distances
evol_params['distance']=np.log10(dists)
evol_params['LSST_Z']= evol_params['abs_LSST_Z']+ 5*np.log10(dists/10)
```


```python
#make a magnitude cut (for a magnitude limited survey)
final_df = (evol_params.query('LSST_Z < 30').reset_index(drop=True)[['mass', 'age', 'temperature', 'spt', 'abs_LSST_Z', 'LSST_Z', 'distance']]).dropna()
```


```python
len(final_df)
```




    4266




```python
p.visualize(final_df, keys=['mass', 'temperature', 'spt'])
```


    
![png](./examples/ExampleNotebook_files/ExampleNotebook_6_0.png)
    



```python
#visualize countours in galaxy model
ax=model.plot_countours(log=True, rmax=50_000, zmax=10000, zmin=-10000, npoints=2000)
```


    
![png](./examples/ExampleNotebook_files/ExampleNotebook_7_0.png)
    



```python

```


This code is still being developed, feedback is welcome!