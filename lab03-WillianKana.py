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
#print(clientes["active"].describe())

"""
    3. Implemente un método que imprima las tres operaciones de tendencia central de la tabla Pagos (Payment)
"""

#query03 = 'select * from payment'
#pagos03 = (pd.read_sql(query03, cnx))["amount"]
#print(f"Media:\n{pagos03.mean()}\n")
#print(f"Mediana:\n{pagos03.median()}\n")
#print(f"Moda:\n{pagos03.mode()}\n")

"""
    4. Implemente un método que imprima las tres operaciones de tendencia central de la tabla Película (Film)
        únicamente del campo Costo de reemplazo (Replacement_cost)
"""

#query04 = 'select replacement_cost from film'
#peliculas = (pd.read_sql(query04, cnx))
#print(f"Media:\n{peliculas.mean()}\n")
#print(f"Mediana:\n{peliculas.median()}\n")
#print(f"Moda:\n{peliculas.mode()}\n")

"""
    5. Implemente un método que imprima las tres operaciones de tendencia central de la tabla Pagos (Payment)
        únicamente del campo Cantidad (amount) de los clientes de Perú.
"""

query05 = '''select * from payment
inner join customer on payment.customer_id = customer.customer_id
inner join address on customer.address_id = address.address_id
inner join city on address.city_id = city.city_id
inner join country on city.country_id = country.country_id
where country.country = 'Peru';'''
pagos05 = (pd.read_sql(query05, cnx))["amount"]
print(f"Media:\n{pagos05.mean()}\n")
print(f"Mediana:\n{pagos05.median()}\n")
print(f"Moda:\n{pagos05.mode()}\n")
