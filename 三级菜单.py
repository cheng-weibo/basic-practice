menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                '优酷': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                'WAT': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


def func(dic):
    while True:
        for index in dic:
            print(index)
        choice = input('请输入选项，输入q返回上一层，输入e退出：').strip()
        if choice == 'q':
            break
        elif choice == 'e':
            exit()
        else:
            dic1 = dic.get(choice)
            if not dic1:
                print('输入错误，请重新输入')
            else:
                func(dic1)


if __name__ == '__main__':
    func(menu)

'''  # 第一次的low方法
while 1:
    for city in menu:
        print(city)
    city = input('请输入选项，输入e退出：').strip()
    if city == 'q':
        break
    elif city == 'e':
        exit()
    else:
        city_values = menu.get(city)
        if not city_values:
            print('输入错误，请重新输入')
            continue
        else:
            while 1:
                for area in city_values:
                    print('\t', area)
                area = input('\t请输入选项，输入q返回上一层，输入e退出：').strip()
                if area == 'q':
                    break
                elif area == 'e':
                    exit()
                else:

                    # area_values = menu[city].get(area)
                    area_values = city_values.get(area)
                    if not area_values:
                        print('\t输入错误，请重新输入：')
                        continue
                    else:
                        while 1:
                            for i in area_values:
                                print('\t\t', i)

                            building = input('\t\t请输入选项，输入q返回上一层，输入e退出：').strip()
                            if building == 'q':
                                break
                            elif building == 'e':
                                exit()
                            else:
                                # building = menu[city][area].get(building)
                                building = area_values.get(building)
                                # 这里怎么优化
                                if not building:
                                    print('\t\t输入错误，请重新输入：')
                                    continue
                                else:
                                    while 1:
                                        for i in building:
                                            print('\t\t\t', i)

                                        retn = input('\t\t\t输入q返回上一层，输入e退出：').strip()
                                        if retn == 'q':
                                            break
                                        elif retn == 'e':
                                            exit()
                                        else:
                                            retn = input('\t\t\t输入错误，请重新输入')
'''
