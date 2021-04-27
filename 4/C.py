print(sum(map(lambda x: x * x, filter(lambda x: x % 9 == 0, [i for i in range(20, 100)]))))
# checking
print(sum(i * i for i in range(27, 100, 9)))
