directions = [
    [-2, -1], [-2, 1],
    [-1, -2], [-1, 2],
    [1, -2], [1, 2],
    [2, -1], [2, 1]
]


def str_to_int_list(coords: str):
    letter, num = list(coords)
    letter = ord(letter) - ord('A') + 1
    num = int(num)
    return [letter, num]


def int_to_str(letter: int, num: int):
    return chr(letter + ord('A') - 1) + str(num)


def list_of_steps(coords: str):
    letter, num = str_to_int_list(coords)
    res = []
    for i in directions:
        if 0 < letter + i[0] < 9 and 0 < num + i[1] < 9:
            res.append(int_to_str(letter + i[0], num + i[1]))
    return res


print(*list_of_steps(input()))
