import csv

def compras_por_pais(pais):
    total_compras = 0
    with open('SalesJan2009.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[7] == pais:
                total_compras += 1
    return total_compras

pais = 'united kingdom'
print(f'Compras realizadas en {pais}: {compras_por_pais(pais)}')

##Ejercicio 2

def compras_por_medio_pago(medio_pago):
    total_compras = 0
    with open('SalesJan2009.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[3] == medio_pago:
                total_compras += 1
    return total_compras

medio_pago = 'visa'
print(f'Compras realizadas con {medio_pago}: {compras_por_medio_pago(medio_pago)}')
