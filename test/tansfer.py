import dpdata
import numpy as np
import math
import os
os.chdir('YourTestData/')
data = dpdata.LabeledSystem('OUTCAR', fmt = 'vasp/outcar')           #通过改变文件名可以将其中不同原子数的OUTCAR文件转化为dpdate数据
data.to_deepmd_npy('test_data')
print(f'-- the training data contains {len(data)} frames.')
