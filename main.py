import random
def generator_password(count):
    az = 'abcdefghijklmnopqrstuvwxyz'
    azupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    znak = '!@#$%^&*'
    list1 = az + azupper + number + znak
    for i in range(1, count + 1):
        print(i, ')', *random.sample(list1, 16), sep='')
#kolvo = int(input('введите кол во паролей , длина пароля = 16 символов'))
#print()
generator_password(10)
