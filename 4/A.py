def get_num_from_console(n: int):
    for j in range(n):
        tmp = input().split()
        yield int(tmp[1]) > 1


all_sum = int(input())

flag_list = []

for i in range(all_sum):
    group_sum = int(input())
    flag_list.append(any(get_num_from_console(group_sum)))

print('ДА' if all(flag_list) else 'НЕТ')
