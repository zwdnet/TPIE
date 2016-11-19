# -*- coding:utf-8 -*-


def bin2dec(string_num):
    # 二进制转十进制
    return str(int(string_num, 2))

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'), ord('A')+6)]


def dec2bin(string_num):
    # 十进制转二进制
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])


if __name__ == "__main__":
    print("输入数字:")
    num = input()
    print("你输入的是十进制（十）还是二进制（二）？")
    s = input()
    if s == "十":
        res = dec2bin(num)
    elif s == "二":
        res = bin2dec(num)
    else:
        print("输入错误!")
        exit(1)
    print(res)