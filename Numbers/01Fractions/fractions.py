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



# 主函数
if __name__ == "__main__":
    inputResult = InputFraction()
    if inputResult == None:
        print("输入错误，程序结束.")
        exit(1)
    # 接下来可以进行数据处理和运算啦
