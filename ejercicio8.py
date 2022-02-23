def descomposicion(): 
  from tabulate import tabulate
  separador = str(input("¿Que separador quieres usar?: "))
  cadena = str(input("¿Que texto deseas analizar?: "))
  cade = cadena.split(separador)
  lista = []
  for i in range(0, len(cade)):
    lista.append(list(cade[i: i+1]))
  tabla = lista
  encabezado = ["nº", "cadena"]
  print(tabulate.tabulate(tabla, encabezado, tablafmt = "fancy_grid", showindex = True))