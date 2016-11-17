# -*- coding:utf-8 -*-
"""分数的四则运算"""


# 用户输入处理
# 返回值 第一个分数的分子 、分母、运算符、 第二个分数的分子、分母
def InputFraction():
    first = input("输入第一个分数:")
    operator = input("输入运算符（+ - * /:)")
    second = input("输入第二个分数:")
    # 判断输入的是否有/，即是否是分数
    if '/' not in first or '/' not in second:
        return None
    no1 = first.split("/")
    no2 = second.split("/")
    num1 = []
    num2 = []
    # 判断输入是否合法，若合法
    for i in no1:
        try:
            x = int(i)
            num1.append(x)
        except ValueError:
            return None
    for j in no2:
        try:
            x = int(j)
            num2.append(x)
        except ValueError:
            return None
    if operator not in ["+", "-", "*", "/"]:
        return None
    return num1[0], num1[1], operator, num2[0], num2[1]


# 通分
def common(Num):
    # 处理分子
    Num[0] = Num[0]*Num[4]
    Num[3] = Num[3]*Num[1]
    # 处理分母
    temp1 = Num[1]
    temp4 = Num[4]
    Num[1] = temp1*temp4
    Num[4] = temp1*temp4
    return Num


# 找两个数的最大公约数
def HCF(a, b):
    m = max(a, b)
    n = min(a, b)
    r = m % n
    if r == 0:
        return n
    comm = 1
    while r != 0:
        temp = n // r
        comm = r
        r = n % r
        n = temp
    return comm


# 约分
def reduction(Num):
    commNum = HCF(Num[0], Num[1])
    if commNum != 1:
        Num[0] = Num[0]/commNum
        Num[1] = Num[1]/commNum
    # 处理负数
    if Num[0] < 0 and Num[1] < 0:
        Num = [abs(x) for x in Num]
    if Num[0] > 0 and Num[1] < 0:
        Num[0] = -1*Num[0]
        Num[1] = abs(Num[1])
    return Num

# 加法
def Add(Num):
    # 先通分，不按数学上的分母乘以最简公分母了，直接互相乘就行了，因为最后还要约分的。
    res = common(Num)
    resNum = [res[0]+res[3], res[1]]
    # 再对结果约分
    resNum = reduction(resNum)
    return resNum


# 减法
def Sub(Num):
    res = common(Num)
    resNum = [res[0]-res[3], res[1]]
    # 再对结果约分
    resNum = reduction(resNum)
    return resNum


# 乘法
def Mul(Num):
    return None


# 除法
def div(Num):
    return None


# 主函数
if __name__ == "__main__":
    inputResult = InputFraction()
    if inputResult == None:
        print("输入错误，程序结束.")
        exit(1)
        # 接下来可以进行数据处理和运算啦
    result = []
    if inputResult[2] == "+":
        result = Add(list(inputResult))
    elif inputResult[2] == "-":
        result = Sub(list(inputResult))
    elif inputResult[2] == "*":
        result = Mul(list(inputResult))
    elif inputResult[2] == "/":
        result = div(list(inputResult))
    print("计算结果为:%d/%d" % (result[0], result[1]))