import pandas as pd

# lee el archivo CSV
df = pd.read_csv("covid-19-peru-camas-uci.csv")

# muestra las primeras filas
print(df.head())
