import pandas as pd

PERS=pd.read_csv("APRENDIENDO/PERSONAS-500000.csv")
print(PERS.head(2))
print(PERS.dtypes)
print(PERS.tail(3))

PERS=pd.read_csv("APRENDIENDO/FALLOS.csv")
print(PERS.head(2))
print(PERS.dtypes)
print(PERS.tail(3))