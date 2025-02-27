import dpdata
import numpy as np
import math
import os
os.chdir('/YourAllStructureDataFile')
data = dpdata.LabeledSystem('OUTCAR', fmt = 'vasp/outcar')           #通过改变文件名可以将其中不同原子数的OUTCAR文件转化为dpdate数据
data_number = len(data)
print(f'# the data contains {data_number} frames.')
index_validation = np.random.choice(data_number, size=math.ceil(data_number*0.05), replace=False) # 选择第一性原理数据的5%做为验证集（validation_data）
data_validation = data.sub_system(index_validation)
data_validation.to_deepmd_npy('validation_data') # 建立对应的验证集文件夹。
print(f"--> the validation data contains {len(data_validation)} frames.")
index_training = list(set(range(data_number))-set(index_validation)) # 除验证集外的数据作为训练集
data_training = data.sub_system(index_training)
data_training.to_deepmd_npy('training_data') # 建立对应的训练集文件夹。 
print(f'-- the training data contains {len(data_training)} frames.')
