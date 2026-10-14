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