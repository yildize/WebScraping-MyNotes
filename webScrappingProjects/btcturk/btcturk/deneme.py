import pandas as pd
import numpy as np

df = pd.read_csv("prices.csv",  thousands=',')
print(df.dtypes)
print(df.head())
df.iloc[:,-5:] = df.iloc[:,-5:].astype(float)
#print(df.dtypes)