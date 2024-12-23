import re
from functools import *
#Задание 1
n = input()
while n != '':
    if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', n):
        print('Частный автомобиль')
    elif re.fullmatch(r'[А-Я]\d{4,5}', n):
        print('Такси')
    else:
        print('Нет номера')
    n = input()
#Задание 3
a = 'Уважаемые! Если вы к 09:00 не вернете чемодан, то уже в 09:00:01 я за себя не отвечаю.'
a = a.split()
b = list(filter(lambda x: re.search(r'\b(0[0-9]│1[0-9]│2[0-4])[:](0[0-9]│[0-9]{2}\b', b), a))
a = reduce(lambda x, y: x + ' ' + y, a)
for i in b:
    a = a.replace(i,'(TBD)',1)
print(a)

#Задание 4
a = 'Владимир устроился на работу в одно очень важное место.'
b = re.findall((r'\b[А-Я][А-Я]*[А-Я]\b', a))
print(b)
