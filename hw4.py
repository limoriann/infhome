a = int(input())
s=0
if a > 100:
	print('Введите другое число')
else:
	for i in range(1, a+1):
		s+=i**2
	print(s)