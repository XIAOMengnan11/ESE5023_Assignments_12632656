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

Find_expression(50)  #执行函数

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
plt.show()