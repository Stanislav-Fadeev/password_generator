import random
def generator_password(count,dlina1):
    print()
    az = 'abcdefghijklmnopqrstuvwxyz'
    azupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    znak = '!@#$%^&*'
    list1 = az + azupper + number + znak
    for i in range(1, count + 1):
        print(i, ')', *random.sample(list1, dlina1), sep='')
kolvo = int(input('введите кол во паролей'))
dlina=int(input('введите длину пароля'))
generator_password(kolvo,dlina)
