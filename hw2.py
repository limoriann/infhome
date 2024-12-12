#Задание 1
a, b = map(float, input().split())
if b != 0:
	print(a/b)
else:
	print('Нельзя делить на ноль')

#Задание 2
s = float(input())
if s > 20:
	print('Сумма покупки:', round(s*0.65, 2), '\nРазмер скидки составляет 35%')
else:
	print('Сумма покупки:', round(s, 2), '\nСкидка не применена')

#Задание 3
a = range(1, 13)
b = int(input())
list = [' ', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

if b not in a:
	print('Ошибка. Введите другое число')
else:
	if b < 3 or b == 12:
		print('Зима', list[b])
	elif  2 < b < 6 :
		print('Весна', list[b])
	elif 5 < b < 9 :
		print('Лето', list[b])
	else:
		print('Осень', list[b])

	
