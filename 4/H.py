def sorted2(data, key=lambda x: -x):
    res = []
    for i in data:
        res.append(sorted(i, key=key))
    res.sort(key=lambda x: x[-1:])
    return res


print(sorted2([[6, 3, 5, 2], [7, 4, 3, 2, 1]]))
