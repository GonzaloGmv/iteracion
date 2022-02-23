from tabulate import tabulate
diccionario = ['avion','tren','auto','camion']
orden = sorted(diccionario)

indice1 = orden.index(diccionario[0])
indice2 = orden.index(diccionario[1])
indice3 = orden.index(diccionario[2])
indice4 = orden.index(diccionario[3])

posterior1 = indice1 + 2
posterior2 = indice2 + 2
posterior3 = indice3 + 2
posterior4 = indice4 + 2

tabla = [[diccionario[0], indice1, posterior1], [diccionario[1], indice2, posterior2], [diccionario[2], indice3, posterior3], [diccionario[3], indice4, posterior4]]

print(tabulate(tabla, headers=["Diccionario", "anterior", "siguiente"]))

resultado = []
letra = input("Escriba la letra que desea:")
if diccionario[0][0] == letra:
  resultado.append(diccionario[0])
if diccionario[1][0] == letra:
  resultado.append(diccionario[1])
if diccionario[2][0] == letra:
  resultado.append(diccionario[2])
if diccionario[3][0] == letra:
  resultado.append(diccionario[3])
print(resultado)