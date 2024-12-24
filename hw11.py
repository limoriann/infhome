import pandas as pd
import numpy as np

df = pd.read_csv('/content/drive/MyDrive/ColabNotebooks/NISPUF17.csv')
# Columns: SEX - пол ребенка
# HAD_CPOX - болел/не болел
# P_NUMVRC - дозы вакцины

 print(df['SEX'].unique())
 print(df['HAD_CPOX'].unique())
 print(df['P_NUMVRC'].unique())

negative_m = len(df['SEX'][df['P_NUMVRC'] > 0].where((df['HAD_CPOX'] == 1) & (df['SEX'] == 1)).dropna())
positive_m = len(df['SEX'][df['P_NUMVRC'] > 0].where((df['HAD_CPOX'] == 2) & (df['SEX'] == 1)).dropna())

negative_w = len(df['SEX'][df['P_NUMVRC'] > 0].where((df['HAD_CPOX'] == 1) & (df['SEX'] == 2)).dropna())
positive_w = len(df['SEX'][df['P_NUMVRC'] > 0].where((df['HAD_CPOX'] == 2) & (df['SEX'] == 2)).dropna())

d = {
     'male': round(float(negative_m/positive_m), 4),
     'female': round(float(negative_w/positive_w), 4)
    }

print(d)
