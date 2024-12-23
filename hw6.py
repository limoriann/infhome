#Задание 5
from array import array
from random import *
a =  []
matrix = [[random.randint(-10, 10) for i in range(10)] for i in range(10)]
for i in range(len(matrix)):
    a.append(sum(matrix[i]))

#Задание 6
from random import *
a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        c = randint(1, 10)
for i in range (c):
    print(i)
print()
for j in (c): 
    minimum = min(j)
    j = [(1 if minimum % 2 else 0)if g == minimum else g for g in j]
    print(*j)
