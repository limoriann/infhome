#Задание 1
a, b = map(float, input().split())
if a == 0 or b == 0:
    print('Делить на ноль нельзя')
else:
    print(round(a/b, 2))
#Задание 2
s = float(input())
if s > 20:
    s = s * 0.65
    print("Сумма:", round(s, 2), "Скидка составила 35%")
else:
    print("Сумма:", round(s, 2), "Скидка составила 0%")

#Задание 3
n = int(input())
if n < 1 or n > 13:
    print('Ошибка')
else:
    mon = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь, 'октябрь, 'ноябрь, 'декабрь']
    if n in [12, 1, 2]:
        print(f'месяц: {mon[n-1]}\n', f'время года: Зима')
    elif n in [3, 4, 5]:
        print(f'месяц: {mon[n-1]}\n', f'время года: Весна')
    elif n in [6, 7, 8]:
        print(f'месяц: {mon[n-1]}\n', f'время года: Лето')
    else:
        print(f'месяц: {mon[n-1]}\n', f'время года: Осень')