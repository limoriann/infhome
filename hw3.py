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