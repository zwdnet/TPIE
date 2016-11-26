# -*- coding:utf-8 -*-
# 验证信用卡卡号是否有效，使用Luhn算法
# http://credit.u51.com/post/80114.html


def InputCardNumber():
    number = input("请输入卡号(16位)：")
    if len(number) != 16:
        print("输入错误！")
        return None
    for n in number:
        if len(n) != 1:
            print("输入错误！")
            return None
    cardnumber = []
    for n in number:
        cardnumber.append(int(n))
    return cardnumber


def check(datanumber):
    # 将卡号逆序
    tempnumber = [i for i in reversed(datanumber)]
    # 取出偶数位数的数字乘以2
    evenNumber = [2*x for x in tempnumber[1::2]]
    # 取出奇数位数的数字
    oddNumber = [x for x in tempnumber[0::2]]
    print(evenNumber)
    # 处理大于10的数字
    j = 0
    for i in evenNumber:
        if i >= 10:
            a = i // 10
            b = i % 10
            evenNumber[j] = a+b
        j += 1
    print(evenNumber)
    # 将数字相加
    total = sum(evenNumber) + sum(oddNumber)
    print(total)
    # 将结果以10取模，如果结果为0，则卡号有效，否则无效
    return total % 10 == 0


def testCompany(number):
    # 根据规则判断卡号 依据 https://cnzhx.net/blog/meaning-of-credit-card-number/
    result = ""
    if number[0] == 4:
        result = "Visa"
    elif number[0] == 5 and number[1] in [1,2,3,4,5]:
        result = "Mastercard"
    elif number[0:3] == [6,0,1,1] or number[0:2] == [6,4,4] or number[0:1] == [6,5]:
        result = "Discover"
    elif number[0:1] == [3,4] or number[0:1] == [3,7]:
        result = "Amex"
    else:
        result = "Others"
    return result


if __name__ == "__main__":
    number = InputCardNumber()
    # testnumber = [5,2,0,4,4,0,8,0,8,6,5,6,6,4,9,2]
    # print(testnumber)
    if check(number):
        print("输入的卡号为有效的卡号。")
        print("卡号所属机构为：%s" % testCompany(number))
    else:
        print("输入的为无效卡号")
