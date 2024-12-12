#Задание 1
a = int(input())
s=0
if a > 100:
	print('Введите другое число')
else:
	for i in range(1, a+1):
		s+=i**3
	print(s)
#Задание 2
x = [ ]
for i in range(1, 10):
	y = [ ]
	for j in range(1, 10):
		y.append(str(i*j)+(3 - len(str(i*j)))*' ')
	x.append(y)
for i in range(9):
	print(*x[i], end = '\n\n')
	
	
