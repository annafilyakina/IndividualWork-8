def perevod(n, osn):
    number = ''
    while n > 0:
        number = str(n % osn) + number
        n = n//osn
    return number


try:
    n = int(input("введите число "))
    osn = int(input('введите систему счисления '))
except ValueError:
    print('неверные данные')
else:
    if osn == 2 or osn == 8:
        print(n, '=>', perevod(n, osn))
    else:
        print('доступные системы счисления:2 и 8 -> попробуйте еще раз')
