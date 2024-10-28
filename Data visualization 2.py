import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('C:\Arquivos\Documentos\Courses\EA50\Coding\data.csv')

plt.plot(df['TIME (year.decimal fraction)'], df['Greenland mass (Gt)'])
plt.plot(df['TIME (year.decimal fraction)'], df['Antarctica mass (Gt)'])
plt.xlabel('Year')
plt.ylabel('Anomalies')
plt.title('Land Ice Mass')
plt.show()