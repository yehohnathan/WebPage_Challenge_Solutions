def get_password(password: str, movements: str):
    # Convertir password en una lista
    password = list(password)
    # Indice del password
    i_pw = 0
    for i in range(len(movements)):
        if movements[i] == 'U':
            if password[i_pw] != '9':
                password[i_pw] = str(int(password[i_pw]) + 1)
            else:
                password[i_pw] = '0'
        elif movements[i] == 'D':
            if password[i_pw] != '0':
                password[i_pw] = str(int(password[i_pw]) - 1)
            else:
                password[i_pw] = '9'
        elif movements[i] == 'R':
            if (i_pw + 1) < (len(password)):
                i_pw += 1
            else:
                i_pw = 0
        elif movements[i] == 'L':
            i_pw -= 1

    return ''.join(password)


get_password('000', 'URURDRDRD')
