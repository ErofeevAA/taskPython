def is_prime(n: int):
    if n < 2:
        return False
    tmp = 2
    while n % tmp != 0:
        tmp += 1
    return tmp == n


def check_pin(pin: str):
    pin = pin.split('-')
    if is_prime(int(pin[0])) is not True:
        return "Некорректен"
    if pin[1] != pin[1][::-1]:
        return "Некорректен"
    part3 = int(pin[2])
    for i in range(1, 3):
        if i == part3:
            return "Корректен"
    i = 2
    while i < part3:
        i *= i
        if i == part3:
            return "Корректен"
    return "Некорректен"


print(check_pin(input()))
