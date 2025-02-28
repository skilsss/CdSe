import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

boxes=np.load('./box.npy')
coord=np.load('./coord.npy')
energy=np.load('./energy.npy')

np.savetxt('./box.txt',boxes,fmt='%s',newline='\n')
np.savetxt('./coord.txt',coord,fmt='%s',newline='\n')
np.savetxt('./energy.txt',energy,fmt='%s',newline='\n')

type_map_raw='../type_map.raw'
type_raw='../type.raw'
box_txt='./box.txt'
coord_txt='./coord.txt'
coord_xyz='./coord.xyz'
with open(type_raw,'r') as f:
    element_id=f.read()
    element_id=element_id.strip().split('\n')
    atom_number=len(element_id)
with open(box_txt,'r') as f:
    box=f.read()
    box=box.strip().split('\n')
with open(type_map_raw,'r') as f:
    element_type=f.read()
    element_type=element_type.strip().split('\n')
with open(coord_txt,'r') as f:
    struc=f.readlines()
print('atom number:',atom_number)
with open(coord_xyz,'w') as f:
    for i,s in enumerate(struc):
        f.write(f'{atom_number}\n')
        f.write(f'Lattice=\"{box[i]}\"\n')
        s=s.strip().split()
        for k,j in enumerate(element_id):
            f.write(f'{element_type[int(j)]} {s[3*k]} {s[3*k+1]} {s[3*k+2]}\n')

with open(r'./energy.txt','r') as f:
    all_line=f.read()
    total_enenrgy=all_line.strip().split('\n')
    for i in range(len(total_enenrgy)):
        total_enenrgy[i]=float(total_enenrgy[i])/atom_number
with open('./energy-per-atom.txt','a') as f:
    for i in total_enenrgy:
        f.write(f'{str(i)}\n')

print('over')