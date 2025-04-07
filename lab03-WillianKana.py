from sqlalchemy import create_engine
import pandas as pd

cnx = create_engine('mysql+pymysql://root:root@localhost:3306/sakila').connect()

"""
    1. Importe la base de datos sakila y procese la data mediante un DataFrame
"""
#query01 = 'select * from payment'
#pagos = pd.read_sql(query01, cnx)
#print(pagos)

"""
    2. Implemente un método que liste la tabla cliente (Customer) e imprima estadísticas del mismo. 
"""
#query02 = 'select * from customer'
#clientes = pd.read_sql(query02, cnx)
#print(clientes.describe())

"""
    3. Implemente un método que imprima las tres operaciones de tendencia central de la tabla Pagos (Payment)
"""

query03 = 'select * from payment'
pagos03 = pd.read_sql(query03, cnx)
print(f"Media:\n{pagos03.mean()}\n")
print(f"Mediana:\n{pagos03.median()}\n")
print(f"Moda:\n{pagos03.mode()}\n")