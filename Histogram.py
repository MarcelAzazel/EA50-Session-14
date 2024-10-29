from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('C:\Arquivos\Documentos\Courses\EA50\Coding\Session 14\data.csv')

sorted_df = df.sort_values('TIME (year.decimal fraction)')

years = []
for year in range(int(sorted_df.loc[0, 'TIME (year.decimal fraction)']), int(sorted_df.loc[len(sorted_df['TIME (year.decimal fraction)']) - 1, 'TIME (year.decimal fraction)']) + 1):
    years.append(year)

plt.hist(sorted_df['Greenland mass (Gt)'], 20, range=(-2000, 2000), alpha=0.5, label='Greenland mass')
plt.hist(sorted_df['Antarctica mass (Gt)'], 20, range=(-2000, 2000), alpha=0.5, label='Antarctica mass')
plt.ylabel('Frequency')
plt.xlabel('Anomalies')
plt.title('Measurements each year')
plt.legend()
plt.show()
