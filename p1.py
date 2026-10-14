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