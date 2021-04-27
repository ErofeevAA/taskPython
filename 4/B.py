def my_simple_map(func, lst: list):
    res = []
    for i in lst:
        res.append(func(i))
    return res


test = [1, 2, 3, 4, 5]
print(*my_simple_map(lambda x: x + 1, test))
