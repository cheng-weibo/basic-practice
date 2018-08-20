"""
如果是新用户--》创建账户，输入工资
else：读取用户信息
需要先创建保存信息的文件，json文件可读性好
"""
import time
import json

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "笔记本", "price": 998},
    {"name": "绿茶", "price": 3},
    {"name": "康师傅", "price": 5},
    {"name": "面包", "price": 666},
]

with open('goods.json', 'a+', encoding='utf-8') as f:
    f.seek(0)
    account = f.read()
    if not account:
        account = {}
    else:
        account = json.loads(account)

my_goods = []   # 保存本次购买的商品

name = input('请输入用户名：').strip()
person = account.get(name)
if person:
    # 老客户
    pwd = input('请输入密码：').strip()
    if pwd == account[name]["pwd"]:
        sear_ch = input('查询历史记录输入1，输入其它开始购物：').strip()
        if sear_ch == '1':
            had_goods = account[name]["record"]

            for index, i in enumerate(had_goods):
                print('-------------第%s次购物-------------' % (index + 1))
                print(i)
                for j in had_goods[i]:
                    print('\t', j)
                print('-----------------------------------')

    else:
        print('密码错误')
        exit()
else:
    # 新客户
    pwd = input('请输入密码：').strip()
    cash = input('请输入工资：').strip()
    if cash.isdigit() and int(cash) >= 0:
        account[name] = {}
        account[name]["pwd"] = pwd
        account[name]["cash"] = cash
        account[name]["record"] = {}  # 用于保存购买记录
    else:
        print('请输入有效的工资')
        exit()

cash = int(account[name]["cash"])
cash_1 = cash
print('\033[31m您的余额为%s元\033[0m' % cash)
while 1:
    for index, i in enumerate(goods):
        print(index, i)

    choice = input('请输入序号选择商品,输入q退出:').strip()
    # 判断输入是否有效
    if choice.isdigit():
        # 判断输入的是否为有效数字
        choice = int(choice)
        if 0 <= choice < len(goods):   # if choice >= 0 and choice < len(goods):

            if cash - goods[choice]["price"] >= 0:
                cash -= goods[choice]["price"]    # cash = cash - goods[choice]["price"]
                my_goods.append(goods[choice])
                print('您已\033[33m购买%s\033[0m，\033[31m余额%s元\033[0m' % (goods[choice]["name"], cash))

            else:
                print('\033[31m余额不足，仅剩%s元\033[0m' % cash)

        else:
            print('输入错误，请输入有效的序号')

    else:
        # 输入不为数字时，是否退出
        if choice == 'q':
            print('本次\033[33m消费%s元\033[0m，\033[31m余额%s元\033[0m' % (cash_1 - cash, cash))

            print('已购商品：')
            for i in my_goods:
                print('\t', i)

            account[name]['cash'] = cash
            # now = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            now = time.strftime('%Y-%m-%d %H:%M')

            # 把本次购买的保存
            account[name]["record"].update({now: my_goods})

            with open('goods.json', 'w', encoding='utf-8') as f:

                f.write(json.dumps(account))  # f.write(str(account))
                #  用json写的才能用json读

            exit()
        else:
            print('输入错误，请输入有效的数字')
            continue



