#Задание 1
import math
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
o = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
acosz = acos(z1, z2)
if acosy > acosx :
    acosx = acosy
    o = [y1, y2]
if acosz > acosx :
    acosz = acosz
    o = [z1, z2]
print(o)

#Задание 2
def pm(n):
	k = bin(n)[2:]
	if k == k[: :-1]:
		return k
	else:
		return ' '
n = int(input())
result = {}
for i in range(n + 1):
    if pm(i) != ' ':
        result.update({i: pm(i)})
print(f'кол-во палиндромов: {len(result)}, \n {result}')
