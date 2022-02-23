import tabulate
def descomposicion(): 
  separador = str(input("¿Que separador quieres usar?: "))
  cadena = str(input("¿Que texto deseas analizar?: "))
  cade = cadena.split(separador)
  lista = []
  for i in range(0, len(cade)):
    