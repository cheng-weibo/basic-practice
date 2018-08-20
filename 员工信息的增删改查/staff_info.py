"""
    支持以下类似的语句：
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT"
    find * from staff_table where enroll_date like "2013"

    add staff_table Alex Li,25,134435344,IT,2015‐10‐29
    del from staff_table where id=3 / age=250

    UPDATE staff_table SET dept = "Market" WHERE dept = "IT"
    UPDATE staff_table SET age = 25 WHERE name = "Alex Li"
"""


def read_file():
    """处理文件最后的空行"""
    with open('staff_info.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    while 1:
        if content[-1] == '\n':
            del content[-1]
        elif not content[-1].endswith('\n'):
            content[-1] += '\n'
        else:
            break
    return content


def file2list(content):
    """
    文件转成二维数组，并转置
    """
    lst = []
    for line in content:  # 把文件的每一行内容都转换成列表
        line = line.strip()
        lst.append(line.split(','))
    return zip(*lst)    # 文件按列存成列表


def produce_id(info_dict):
    """
    设置添加员工时的ID
    """
    for p in range(int(info_dict['id'][-1])+1, 10000):
        yield str(p)


def file2dict(content):
    """
    读取文件，转成字典
    """

    r_info_list = file2list(content)
    info_list = list(r_info_list)

    k = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    info_dict = {}
    for i in range(len(k)):  # 文件内容存成字典，k[i]为键，每一列为一个值
        info_dict[k[i]] = list(info_list[i])

    return info_dict, k


def find_staff(sql, info_dict, count, content):
    """
    查找
    """
    res = sql.replace('find ', '')
    res = res.replace(' from staff_table where ', '.')

    left, right = res.split('.')  # left: 'name, age'   right: 'age > 22'
    left = left.split(',')  # left-->['name', 'age']
    a, b, c = right.split(' ')

    if left == ['*']:
        for index, i in enumerate(info_dict[a]):
            if b == 'like' and eval(c) in i or eval(c) == i:
                count += 1
                print(content[index].strip())

    elif b == '>':
        if left == ['*']:
            left = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
        for index, i in enumerate(info_dict[a]):  # age_list
            if int(i) > int(c):  # xx > 22
                count += 1
                left_ = ''
                for x in left:
                    left_ += (info_dict[x][index] + ',')
                print(left_)
    return "\033[33m查到%s条记录\033[0m" % count


def add_staff(sql, info_dict, k):
    res = sql.replace('add staff_table ', '')
    res = res.split(',')
    if res[2] in info_dict['phone']:
        print('手机号不能重复')

    else:
        p_id = produce_id(info_dict)
        res.insert(0, next(p_id))
        for i in range(len(k)):
            info_dict[k[i]].append(res[i])
        return "\033[33m添加1条记录\033[0m"


def del_staff(sql, info_dict, k):
    res = sql.replace('del from staff_table where ', '')
    a, c = res.split('=')
    count = info_dict[a].count(c)
    while c in info_dict[a]:
        for index, i in enumerate(info_dict[a]):  # 找删除项的索引
            if int(c) == int(i):
                for item in range(len(k)):
                    del info_dict[k[item]][index]
    return "\033[33m删除%s条记录\033[0m" % count


def update_staff(sql, info_dict, count):
    res = sql.replace('UPDATE staff_table SET ', '')
    res = res.replace(' WHERE ', '.')
    left, right = res.split('.')

    k1, v1 = left.split('=')
    k1, v1 = k1.strip(), v1.strip()
    k2, v2 = right.split('=')
    k2, v2 = k2.strip(), v2.strip()

    x = info_dict[k2]

    for i in range(len(x)):
        if x[i] == str(eval(v2)):
            count += 1
            if k1 == k2:
                x[i] = str(eval(v1))
            else:
                info_dict[k1][i] = str(eval(v1))
    return "\033[33m更新%s条记录\033[0m" % count


def write_file(info_dict):
    """处理完成，写入文件"""
    end_list = []
    for i in info_dict:
        end_list.append(info_dict[i])
    w_list = zip(*end_list)
    with open('staff_info.txt', 'w', encoding='utf-8') as f:
        for i in w_list:
            col = ','.join(i)
            f.write(col + '\n')


def main():

    while True:
        content = read_file()
        info_dict, k = file2dict(content)
        try:
            count = 0
            sql = input('请输入命令，q退出>>:').strip()
            if sql == 'q':
                break

            def staff_handle():
                if sql.startswith('find'):
                    return find_staff(sql, info_dict, count, content)
                if sql.startswith('add'):
                    return add_staff(sql, info_dict, k)
                if sql.startswith('del'):
                    return del_staff(sql, info_dict, k)
                if sql.startswith('UPDATE'):
                    return update_staff(sql, info_dict, count)
            msg = staff_handle()
            if msg:
                print(msg)
            else:
                print('输入有误，请重新输入...')
        except:
            print("请输入规范的查询语句")

        write_file(info_dict)


if __name__ == '__main__':
    main()
