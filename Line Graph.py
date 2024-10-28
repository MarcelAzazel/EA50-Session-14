from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('C:\Arquivos\Documentos\Courses\EA50\Coding\data.csv')

plt.plot(df['TIME (year.decimal fraction)'], df['Greenland mass (Gt)'], label='Greenland mass')
plt.plot(df['TIME (year.decimal fraction)'], df['Antarctica mass (Gt)'], label='Antarctica mass')
plt.xlabel('Year')
plt.ylabel('Anomalies')
plt.title('Land Ice Mass')
plt.legend()
plt.show()
