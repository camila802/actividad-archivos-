import csv

def compras_por_pais(pais):
    total_compras = 0
    with open('files/SalesJan2009.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[7] == pais:
                total_compras += 1
    return total_compras

pais = 'United Kingdom'
print(f'Compras realizadas en {pais}: {compras_por_pais(pais)}')

