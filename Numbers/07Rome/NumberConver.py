# -*- coding:utf-8 -*-
# 阿拉伯数字转换为罗马数字，参考http://blog.csdn.net/menxu_work/article/details/9147209


def Conver(number):
    if number <= 0:
        print("输入数字必须大于0。")
        return None
    numDic = {'I': 1,
              'II': 2,
              'III': 3,
              'IV': 4,
              'V': 5,
              'VI': 6,
              'VII': 7,
              'VIII': 8,
              'IX': 9,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}
    tempNum = number
    RomeNumber = ""
    keyList = ['M', 'D', 'C', 'L', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    for key in keyList:
        if tempNum >= numDic[key]:
            t = tempNum//numDic[key]
            for i in range(t):
                RomeNumber += key
            tempNum = tempNum % numDic[key]
    return RomeNumber


if __name__ == "__main__":
    number = input("请输入大于0的阿拉伯数字，整数：")
    number = int(number)
    Rome = Conver(number)
    if Rome == None:
        print("转换失败")
    else:
        print("相应的罗马数字为：", Rome)
