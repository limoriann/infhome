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

	
