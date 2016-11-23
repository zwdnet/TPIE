# -*- coding:utf-8 -*-
# 列出货品清单，接受用户输入，计算总价，用户付款后输出找零。用人民币做了。

# 货物清单
goodList = {1: 100,
            2: 50,
            3: 320,
            4: 5,
            5: 1035}


def displayGood():
    s = """------------欢迎光临------------
           货物清单
           01        1元
           02        5角
           03        3元2角
           04        5分
           05        10元3角5分
           """
    print(s)


def inputData():
    data = []
    num = 0
    amount = 0
    while True:
        try:
            num = int(input("请输入购买的品种和数量(格式： 货物编号）结束输入请输 -1:"))
            amount = int(input("请输入购买的品种和数量(格式： 数量）结束输入请输 -1:"))
        except ValueError:
            print("输入的不是整数，退出！")
            return None
        if num == -1 and amount == -1:
            break
        data.append((num, amount))
    return data


def calculator(runlist, data):
    result = 0
    for i, j in data:
        result += j * runlist[i]
    return result


def FindCharge(shouldpay, realpay):
    sub = realpay - shouldpay
    Yuan = sub // 100
    Jiao = sub % 100 // 10
    Fen = sub % 100 % 10
    return Yuan, Jiao, Fen


if __name__ == "__main__":
    displayGood()
    information = inputData()
    result = calculator(goodList, information)
    yuan = result // 100
    jiao = result % 100 // 10
    fen = result % 100 % 10
    print("您一共需要付%d元%d角%d分" % (yuan, jiao, fen))
    print("请输入您要付的钱：")
    try:
        inputYuan = int(input("元"))
        inputJiao = int(input("角"))
        inputFen = int(input("分"))
    except ValueError:
        print("输入错误，程序结束")
        exit(1)
    total = 100*inputYuan + 10*inputJiao + inputFen
    if total < result:
        print("你付的钱小于应付总额，交易失败！")
    elif total == result:
        print("成交，再见！")
    else:
        # 找零
        charge = FindCharge(result, total)
        print("一共要找您%d元%d角%d分，慢走" % (charge[0], charge[1], charge[2]))
