def sum_list(lst):

    result = []

    def inner(lst1):
        for obj in lst1:
            if isinstance(obj, list):
                inner(obj)
            elif isinstance(obj, int):
                result.append(obj)
            else:
                pass
        return sum(result)
    return inner(lst)


if __name__ == '__main__':
    ls = [1, 1, [1, ['jack', 1]], [1, [1, [1]]]]

    print(sum_list(ls))
