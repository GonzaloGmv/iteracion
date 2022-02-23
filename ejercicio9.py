def ejercicio9():
  from tabulate import tabulate
  diccionario = ['avion','tren','auto','camion']
  orden = sorted(diccionario)
  
  indice1 = orden.index(diccionario[0])
  indice2 = orden.index(diccionario[1])
  indice3 = orden.index(diccionario[2])
  indice4 = orden.index(diccionario[3])
  
  if indice1 != 0:
      anterior1 = diccionario.index(orden[indice1 - 1]) + 1
  else:
      anterior1 = "..."
  if indice2 != 0:
      anterior2 = diccionario.index(orden[indice2 - 1]) + 1
  else:
      anterior2 = "..."
  if indice3 != 0:
      anterior3 = diccionario.index(orden[indice3 - 1]) + 1
  else:
      anterior3 = "..."
  if indice4 != 0:
      anterior4 = diccionario.index(orden[indice4 - 1]) + 1
  else:
      anterior4 = "..."
    
  
  if indice1 != 3:
      posterior1 = diccionario.index(orden[indice1 + 1]) + 1
  else:
      posterior1 = "..."
  if indice2 != 3:
      posterior2 = diccionario.index(orden[indice2 + 1]) + 1
  else:
      posterior2 = "..."
  if indice3 != 3:
      posterior3 = diccionario.index(orden[indice3 + 1]) + 1
  else:
      posterior3 = "..."
  if indice4 != 3:
      posterior4 = diccionario.index(orden[indice4 + 1]) + 1
  else:
      posterior4 = "..."
  
  tabla = [[diccionario[0], anterior1, posterior1], [diccionario[1], anterior2, posterior2], [diccionario[2], anterior3, posterior3], [diccionario[3], anterior4, posterior4]]
  
  print(tabulate(tabla, headers=["Diccionario", "anterior", "siguiente"]))
  
  #9.1
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
  
  #9.3
  diccionario.append(input("Escriba una nueva palabra: "))
  orden = sorted(diccionario)
  
  indice1 = orden.index(diccionario[0])
  indice2 = orden.index(diccionario[1])
  indice3 = orden.index(diccionario[2])
  indice4 = orden.index(diccionario[3])
  indice5 = orden.index(diccionario[4])
  
  if indice1 != 0:
      anterior1 = diccionario.index(orden[indice1 - 1]) + 1
  else:
      anterior1 = "..."
  if indice2 != 0:
      anterior2 = diccionario.index(orden[indice2 - 1]) + 1
  else:
      anterior2 = "..."
  if indice3 != 0:
      anterior3 = diccionario.index(orden[indice3 - 1]) + 1
  else:
      anterior3 = "..."
  if indice4 != 0:
      anterior4 = diccionario.index(orden[indice4 - 1]) + 1
  else:
      anterior4 = "..."
  if indice5 != 0:
      anterior5 = diccionario.index(orden[indice5 - 1]) + 1
  else:
      anterior5 = "..."
    
  
  if indice1 != 4:
      posterior1 = diccionario.index(orden[indice1 + 1]) + 1
  else:
      posterior1 = "..."
  if indice2 != 4:
      posterior2 = diccionario.index(orden[indice2 + 1]) + 1
  else:
      posterior2 = "..."
  if indice3 != 4:
      posterior3 = diccionario.index(orden[indice3 + 1]) + 1
  else:
      posterior3 = "..."
  if indice4 != 4:
      posterior4 = diccionario.index(orden[indice4 + 1]) + 1
  else:
      posterior4 = "..."
  if indice5 != 4:
      posterior5 = diccionario.index(orden[indice5 + 1]) + 1
  else:
      posterior5 = "..."
  
  tabla = [[diccionario[0], anterior1, posterior1], [diccionario[1], anterior2, posterior2], [diccionario[2], anterior3, posterior3], [diccionario[3], anterior4, posterior4], [diccionario[4], anterior5, posterior5]]
  
  print(tabulate(tabla, headers=["Diccionario", "anterior", "siguiente"]))
  
  #9.4
  diccionario.remove(input("Escriba la palabra que desea eliminar: "))
  orden = sorted(diccionario)
  
  indice1 = orden.index(diccionario[0])
  indice2 = orden.index(diccionario[1])
  indice3 = orden.index(diccionario[2])
  indice4 = orden.index(diccionario[3])
  
  if indice1 != 0:
      anterior1 = diccionario.index(orden[indice1 - 1]) + 1
  else:
      anterior1 = "..."
  if indice2 != 0:
      anterior2 = diccionario.index(orden[indice2 - 1]) + 1
  else:
      anterior2 = "..."
  if indice3 != 0:
      anterior3 = diccionario.index(orden[indice3 - 1]) + 1
  else:
      anterior3 = "..."
  if indice4 != 0:
      anterior4 = diccionario.index(orden[indice4 - 1]) + 1
  else:
      anterior4 = "..."
    
  
  if indice1 != 3:
      posterior1 = diccionario.index(orden[indice1 + 1]) + 1
  else:
      posterior1 = "..."
  if indice2 != 3:
      posterior2 = diccionario.index(orden[indice2 + 1]) + 1
  else:
      posterior2 = "..."
  if indice3 != 3:
      posterior3 = diccionario.index(orden[indice3 + 1]) + 1
  else:
      posterior3 = "..."
  if indice4 != 3:
      posterior4 = diccionario.index(orden[indice4 + 1]) + 1
  else:
      posterior4 = "..."
  
  tabla = [[diccionario[0], anterior1, posterior1], [diccionario[1], anterior2, posterior2], [diccionario[2], anterior3, posterior3], [diccionario[3], anterior4, posterior4]]
  
  print(tabulate(tabla, headers=["Diccionario", "anterior", "siguiente"]))