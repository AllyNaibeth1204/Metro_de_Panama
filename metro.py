import pandas as pd
path = 'C:\Users\ALISOM\Desktop\Proyecto_SIC_Metro\demanda-de-usuarios-2023-linea-1.csv'
data = pd.read_csv(path, encoding = "latin1")
data.head()