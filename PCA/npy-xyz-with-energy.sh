#!/bin/bash

# 保存最初的工作目录
initial_dir=$(pwd)

# 创建新的 merged-coord.xyz 和 merged-energy-per-atom.txt 文件
touch merged-coord.xyz
touch merged-energy-per-atom.txt

# 循环遍历 data 文件夹中的每一个文件夹
for folder in data/*/; do
    # 进入 set.000 文件夹
    cd "$folder/set.000" || continue
    
    # 运行 my-npy-xyz.py 脚本生成 coord.xyz 和 energy.txt
    python "$initial_dir/my-npy-xyz_energy_per-atom.py"
    
    # 将生成的 coord.xyz 和 energy.txt 内容追加到 merged-coord.xyz 和 merged-energy.txt 文件中
    cat coord.xyz >> "$initial_dir/merged-coord.xyz"
    cat energy-per-atom.txt >> "$initial_dir/merged-energy-per-atom.txt"
    
    # 返回最初的工作目录
    cd "$initial_dir"
done
