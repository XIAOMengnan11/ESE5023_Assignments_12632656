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
        #print (new_row)  #这一行可以打印完整版的三角

        row = new_row

    return row


a= Pascal_triangle(100)
b= Pascal_triangle(200)

print(a)
print(b)