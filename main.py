import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

Data = pd.read_csv("Full.csv", delimiter=";", encoding='latin-1')

Data[['Day','Month','Year']] = Data.Datum.str.split(".",expand=True,)

grouped = Data.groupby(Data.Year)
df2022 = grouped.get_group("2022")
df2021 = grouped.get_group("2021")
df2020 = grouped.get_group("2020")


Take = df2021.groupby(df2021.Month)
df_21_Okt = Take.get_group("10")

#find unique points values
points = df2021.Month.unique()
points.sort()

print(points)
print(len(points))

y = len(points)
z = 0
num_rows = []

while z < y:
    df_Zw = df2021.apply(lambda x: True
    if x['Month'] == points[z] else False, axis=1)
    num_rows.append(len(df_Zw[df_Zw == True].index))
    z = z+1

print(num_rows)


average = sum(num_rows)/len(num_rows)


#normal distribution

mu = average
variance = np.var(num_rows)
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()



plt.plot(points, num_rows)
plt.show()



Data[['Anlegedatum','Anlegeuhrzeit']] = Data.Angelegtam.str.split(" ",expand=True,)
df_2 = Data.sort_values(by='Anlegeuhrzeit', ascending=True)
df_2[['Stunde', 'Minuten']] = df_2.Anlegeuhrzeit.str.split(":", expand=True)

Uhrzeiten = df_2.Stunde.unique()
a = len(Uhrzeiten)
c = 0
num_rows2 = []

while c < a:
    df_Zwi = df_2.apply(lambda x: True
    if x['Stunde'] == Uhrzeiten[c] else False, axis=1)
    num_rows2.append(len(df_Zwi[df_Zwi == True].index))
    c = c+1

plt.plot(Uhrzeiten, num_rows2)
plt.show()




