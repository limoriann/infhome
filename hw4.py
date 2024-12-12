#Задание 1 
import re
t = input()
p = t.replace('н','!')
c = len(max(re.findall(r'н', t)))
print( 'Новая строка:', p, '\n Количество букв:',c)

#Задание 2
import re
t  = input()
p = re.findall(r'\((.+?)\)', t)
print(p)

#Задание 3
import re
t = input().lower()
p = re.findall(r'\bа\w+я\b', t)
print(p)
