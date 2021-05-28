def password_level(password: str):
    if len(password) < 6:
        return "Недопустимый пароль"
    flag_up = False
    flag_low = False
    flag_num = False
    for s in password:
        if s.isnumeric():
            flag_num = True
            continue
        if s.islower():
            flag_low = True
            continue
        flag_up = True
    if flag_up == flag_low == flag_num:
        return "Надёжный пароль"
    if (not flag_up and not flag_low) or (not flag_num and not flag_low) or (not flag_num and not flag_up):
        return "Ненадёжный пароль"
    return "Слабый пароль"


print(password_level(input()))
