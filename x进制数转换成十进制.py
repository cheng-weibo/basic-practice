x = '0b100000100'  # 2/8/16进制的数，带前缀0b, 0o, 0x,切必须是字符串形式
# x = bin(260)   # return '0b100000100'


def transfer_conversion(num):
    lst = []

    for i in num:  # 字符串转换成列表，倒序
        lst.insert(0, i)
    lst.pop()
    flag = lst.pop()
    # 判断传入数字的进制
    if flag == 'x':
        conversion = 16
    elif flag == 'b':
        conversion = 2
    else:
        conversion = 8

    # 计算十进制开始
    index_, result = 0, 0
    for i in lst:
        if conversion == 16:
            hex_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            if i in hex_16:
                i = hex_16.index(i)
        result += int(i) * conversion ** index_
        index_ += 1

    return result


print('>>>: ', transfer_conversion(x))
