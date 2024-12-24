import pandas as pd
import matplotlib.pyplot as plt

#Задание 1
tb1 = pd.DataFrame({
    'number':[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'R':[252, 252, 254, 208, 187, 153, 252, 253, 249, 248, 219],
    'G':[234, 232, 229, 188, 163, 135, 232, 231, 218, 213, 178],
    'B':[118, 95, 0, 254, 13, 48, 93, 36, 0, 0, 22]})

 print(tb1)
#Задание 3
 b = tb1['B'].value_counts()
 plt.bar(b.index, b.values)
 plt.grid()
 plt.xlabel('B')
 plt.ylabel('Частота')
#Задание 2
 uni_1 = tb1['R'][~tb1['R'].isin(tb1['B'])]
 uni_2 = tb1['B'][~tb1['B'].isin(tb1['R'])]
 uni_all = pd.concat([uni_1, uni_2])
 print(uni_all)


#Задание 4
tb2 = pd.DataFrame({
    'number':[1, 141, 189, 134, 194, 105, 106, 107, 765, 109, 110],
    'R':[946, 252, 198, 208, 187, 153, 387, 253, 249, 984, 219],
    'G':[234, 789, 229, 345, 163, 135, 982, 231, 654, 213, 612],
    'B':[22, 95, 99, 254, 0, 48, 11, 36, 0, 0, 22]})

# cc = pd.concat([tb1, tb2])
tbm = tb1.merge(tb2, how='left', left_on='number', right_on='number')
tbm = tbm.set_index('number')
print(tbm)
tbm[['B_x', 'G_x']].plot()
plt.grid()
plt.ylabel('Code')
plt.show()
