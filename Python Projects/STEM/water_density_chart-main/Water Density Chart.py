import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

data = pd.read_csv("Water Density.csv")

x=float(input('Enter temperature in centigrade(must be between 0.0 and 30.9 C): '))
f=int(round(x,1)*10)

ser =data.iloc[f]

print(ser)

data.plot(kind='scatter',x='Temp(C)',y='Water_Density')
plt.show()