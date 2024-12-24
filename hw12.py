import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('/content/drive/MyDrive/ColabNotebooks/Mall_Customer.csv')

#Задание 1
female_income = df[df['genre'] == 'Female']['Annual Income'].mean()
print('female_income:', fincome)

#Задание 2
p = df['Annual Income (k$)'].median()
highm = df[(df['genre'] == 'Male') and (df['Annual Income (k$)'] > p)]
highw = highm = df[(df['genre'] == 'Female') and (df['Annual Income (k$)'] > p)]
print('Кол-во мужчин:', highm, 'Кол-во женщин:', highw)

#Задание 3
df_men = df[df['genre'] == 'Male']
plt.figure(figuresize = (7, 5))
plt.scatter(df_men['Age'], df_men['Annual Income'], color = 'blue', alpha = 1.3) 
plt.title('Доход от возраста')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.grid()
plt.show()

#Задание 4
gr = df.groupby(['Genre', 'Annual Income'])['Spending Score'].mean().unstack()
gr.plot(kind='bar', figsize=(10, 6), color=['blue', 'pink'])
plt.figure(figuresize = (13, 10))
plt.title('Расход от дохода')
plt.xlabel('Доходы')
plt.ylabel('Расходы')
plt.legend(title = 'Ламинат')
plt.grid()
plt.show()
