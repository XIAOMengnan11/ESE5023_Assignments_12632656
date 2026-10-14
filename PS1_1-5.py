<<<<<<< HEAD
#第一题
import random #使用random模块用来生成随机数

#调用random中的randint方法，生成1-100（不含100）之间的随机整数，a,b,c用于输入
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

print("the random result is:",a,b,c)

#定义函数，使用if-else条件判断语句就可以完成
def Print_values(a, b, c):
    if a > b:  #第一层判断
        if b > c: #嵌套的第二层判断
            print(a,b,c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            if a > c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c, b, a)

Print_values(a,b,c) #调用上述定义的函数方法

print("the result is:",a,b,c)

#第二题
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
                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]

    return result

M=Matrix_multip(M1, M2)
MM=np.array(M)  #将相乘的结果转换成numpy数组的形式
print(MM)

#第三题
def Pascal_triangle(k):
    row = [1] #第一行为1，直接赋值

    for i in range(k - 1): #从第一行循环到第k-1行

        new_row = []  #创建一个新的空列表，进行后续行的存放

        new_row.append(1) #给每一行的第一个数字赋值为1
        j = 0 #j代表行的索引值，从0开始，索引的数跟每一行的相加的次数相等
        for j in range(len(row) - 1): #内嵌的循环，遍历每一行的数字，索引从0开始，减去1；len为获取长度的函数
            a = row[j]
            b = row[j + 1]
            c = a + b
            new_row.append(c)

        new_row.append(1)

        row = new_row

    return row


a= Pascal_triangle(100)
b= Pascal_triangle(200)

print(a)
print(b)

#第四题
def Least_moves(x):
    steps = [0] * (x + 1)  #先使用0来进行占位
    steps[1] = 0  #step[i]表示从1到数字i所需要的步数

#使用列表存储之前的结果，再用for循环逐个计算后面的结果，偶数有两种可能，需要讨论一下，用if
    for i in range(2, x + 1): #得到1的情况为0，从2开始，循环到得到x，range左闭右开
        steps[i] = steps[i - 1] + 1

        if (i%2==0):
            steps[i] = min(steps[i-1]+1,steps[i//2]+1)
    a = steps[x]
    print(a)
    return a

result = Least_moves(100)
print (result)

#第五题
def Print_expression(expression, i, show):  #控制表达式打印的函数
    if show == True:
        print(expression, "=", i)


def Find_expression(i, show=True):  #True表示打印，False表示不打印，这里用bool判断
    digits = "123456789" #以文本形式定义
    count = 0

    for n in range(3 ** 8):  #穷举法，所有情况，从0开始找
        temp = n
        expression = "1" #1的左边不参与计算

        for j in range(1, 9):  #这里的j相当于是digits的索引，1-8，对用数字2-9
            choice = temp % 3  #取余数
            temp = temp // 3   # 取商

            if choice == 0:
                expression = expression + digits[j] #这个代表中间不加+和—
            elif choice == 1:
                expression = expression + "+" + digits[j]
            else:
                expression = expression + "-" + digits[j]

        result = eval(expression) #这个函数可以计算expression表达式

        if result == i: #如果计算结果是我们想找的结果i
            count = count + 1  #循环计数
            Print_expression(expression, i, show)

    a = count
    print(a)
    return count

Find_expression(5)  #执行函数

#第二问，画图
import matplotlib.pyplot as plt

number = range(1,101) #定义横坐标，从1到100，目标数
Total_solutions = []

for i in number:

    count = Find_expression(i, False)

    Total_solutions.append(count)

plt.plot(number, Total_solutions)  #Total_solutions是纵坐标
plt.xlabel("Number")
plt.ylabel("Number of solutions")  #横纵坐标轴的标签
plt.title("Number of suitable")
=======
#第一题
import random #使用random模块用来生成随机数

#调用random中的randint方法，生成1-100（不含100）之间的随机整数，a,b,c用于输入
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

print("the random result is:",a,b,c)

#定义函数，使用if-else条件判断语句就可以完成
def Print_values(a, b, c):
    if a > b:  #第一层判断
        if b > c: #嵌套的第二层判断
            print(a,b,c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            if a > c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c, b, a)

Print_values(a,b,c) #调用上述定义的函数方法

print("the result is:",a,b,c)

#第二题
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
                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]

    return result

M=Matrix_multip(M1, M2)
MM=np.array(M)  #将相乘的结果转换成numpy数组的形式
print(MM)

#第三题
def Pascal_triangle(k):
    row = [1] #第一行为1，直接赋值

    for i in range(k - 1): #从第一行循环到第k-1行

        new_row = []  #创建一个新的空列表，进行后续行的存放

        new_row.append(1) #给每一行的第一个数字赋值为1
        j = 0 #j代表行的索引值，从0开始，索引的数跟每一行的相加的次数相等
        for j in range(len(row) - 1): #内嵌的循环，遍历每一行的数字，索引从0开始，减去1；len为获取长度的函数
            a = row[j]
            b = row[j + 1]
            c = a + b
            new_row.append(c)

        new_row.append(1)

        row = new_row

    return row


a= Pascal_triangle(100)
b= Pascal_triangle(200)

print(a)
print(b)

#第四题
def Least_moves(x):
    steps = [0] * (x + 1)  #先使用0来进行占位
    steps[1] = 0  #step[i]表示从1到数字i所需要的步数

#使用列表存储之前的结果，再用for循环逐个计算后面的结果，偶数有两种可能，需要讨论一下，用if
    for i in range(2, x + 1): #得到1的情况为0，从2开始，循环到得到x，range左闭右开
        steps[i] = steps[i - 1] + 1

        if (i%2==0):
            steps[i] = min(steps[i-1]+1,steps[i//2]+1)
    a = steps[x]
    print(a)
    return a

result = Least_moves(100)
print (result)

#第五题
def Print_expression(expression, i, show):  #控制表达式打印的函数
    if show == True:
        print(expression, "=", i)


def Find_expression(i, show=True):  #True表示打印，False表示不打印，这里用bool判断
    digits = "123456789" #以文本形式定义
    count = 0

    for n in range(3 ** 8):  #穷举法，所有情况，从0开始找
        temp = n
        expression = "1" #1的左边不参与计算

        for j in range(1, 9):  #这里的j相当于是digits的索引，1-8，对用数字2-9
            choice = temp % 3  #取余数
            temp = temp // 3   # 取商

            if choice == 0:
                expression = expression + digits[j] #这个代表中间不加+和—
            elif choice == 1:
                expression = expression + "+" + digits[j]
            else:
                expression = expression + "-" + digits[j]

        result = eval(expression) #这个函数可以计算expression表达式

        if result == i: #如果计算结果是我们想找的结果i
            count = count + 1  #循环计数
            Print_expression(expression, i, show)

    a = count
    print(a)
    return count

Find_expression(5)  #执行函数

#第二问，画图
import matplotlib.pyplot as plt

number = range(1,101) #定义横坐标，从1到100，目标数
Total_solutions = []

for i in number:

    count = Find_expression(i, False)

    Total_solutions.append(count)

plt.plot(number, Total_solutions)  #Total_solutions是纵坐标
plt.xlabel("Number")
plt.ylabel("Number of solutions")  #横纵坐标轴的标签
plt.title("Number of suitable")
>>>>>>> origin/main
plt.show()