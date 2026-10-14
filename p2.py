import numpy as np
import random

#调用random中的randint方法，生成0-50之间的随机整数，定义M1、M2两个矩阵
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))

print(M1)
print(M2)

#第二问，定义矩阵的乘法函数，M1与M2相乘后应为5*5矩阵，M1的每一行都与M2的每一列相乘后再相加
def Matrix_multip(M1, M2):
    result = []  #先用一个空的矩阵进行占位

#创建一个全为0的矩阵
    for i in range(len(M1)): #len指的是获取矩阵的行数
        row = []
        for j in range(len(M2[0])): #获取矩阵的列数
            row.append(0)
        result.append(row)

    # 计算矩阵乘法
    for i in range(len(M1)):  #遍历M1的第一行到第五行，外层循环
        for j in range(len(M2[0])): #内层循环，遍历M2的第一到第五列
            for k in range(len(M2)): #负责累加，将M1和M2的对应元素相乘后再加起来
                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]  #M1的列数等于M2的行数，递加

    return result

M=Matrix_multip(M1, M2)
MM=np.array(M)  #将相乘的结果转换成numpy数组的形式
print(MM)

