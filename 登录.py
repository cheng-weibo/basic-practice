"""
输入用户名和密码，正确则登录成功，错误则重新输入，错误三次锁定账户
"""

account = [['jack', '123.json'], ['eric', '456'], ['tom', '789']]

while True:
    username_list = []

    for i in account:
        username_list.append(i[0])  # 用于检查用户是否存在

    with open('forbiden.txt', 'a+', encoding='utf-8') as f:
        f.seek(0)
        forbiden_list = f.read()  # 已被锁定的用户

    name = input("请输入用户名(输入q或Q退出):").strip()
    if name == 'q' or name == 'Q':
        exit()

    if name not in username_list:
        print('用户不存在')
        continue
    if name in forbiden_list:
        print('该账户已被锁定')
        continue
    else:
        count = 0
        while count < 3:
            count += 1

            if count > 1:
                passwd = input("密码错误请重新输入密码:").strip()
            else:
                passwd = input("请输入密码:").strip()

            if [name, passwd] in account:
                print('欢迎%s登陆!' % name)
                break

        else:
            with open('forbiden.txt', 'a+', encoding='utf-8') as f:
                f.write(name)
                f.write('\n')
            print('输入密码错误次数过多，账户已被锁定。。。')
    ext = input('退出请输入q或Q，否则登陆其他用户：').strip()
    if ext.lower() == 'q':
        exit()

