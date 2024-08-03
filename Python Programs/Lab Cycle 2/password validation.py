def valid_password(psw):
    while True:
        if len(psw) < 7:
            print('Password is not valid')
        elif not any(i.isupper() for i in psw):
            print('Password is not valid')
        elif not any(i.islower() for i in psw):
            print('Password is not valid')
        elif not any(i.isdigit() for i in psw):
            print('Password is not valid')
        else:
            print('Password is valid.')
            break

        psw = input('Enter Password: ')

password = input('Enter Password: ')
valid_password(password)
    

    
