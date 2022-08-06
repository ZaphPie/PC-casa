"""
PANDAS: filtrado

El método where() se usa para verificar una o más condiciones y devolver el resultado. De forma predeterminada, las filas que no cumplen la condición se rellenan con el valor NaN. 
EJM:
#filter = df['estado'] == "en uso"
#df_enuso = df.where(filter)
#print(df_enuso)
"""
"""
PANDAS: estadísticas
-Agrupar datos en base a los valores de una columna
#grouped_data =df.grouphy('estado')
-Resumen descriptivo
print(grouped_data.describe())
otras funciones: count();sum();mean();std();min()max()
Agrupar datos y filtrar columna
#minsa = df.groupby('estado')['minsa']
#print(minsa.describe())
"""
"""
PANDAS:gráficos
-Pandas permite visualizar el resumen de los datos mediante gráficos usando la librería matplotlib.

#import matplotlib.pyplot as plt

#minsa_resume = df.groupby('estado')['minsa'].sum()
#minsa_resume.plot(kind='bar')
"""