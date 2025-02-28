import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
t=np.loadtxt(r'YourPCAFile',unpack=True)
PCA1=t[0]
PCA2=t[1]
energy=t[10]
norm = TwoSlopeNorm(vmin=-25.90,vcenter=-25.60,vmax=-25.30)
plt.scatter(-PCA1,-PCA2,c=energy,cmap='RdYlBu',s=6,norm=norm)
cbar=plt.colorbar()
cbar.set_label('energy/atom(ev)')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()
