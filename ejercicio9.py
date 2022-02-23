diccionario = ['avion','tren','auto','camion']
palabra1 = diccionario[0]
palabra2 = diccionario[1]
palabra3 = diccionario[2]
palabra4 = diccionario[3]
resultado =[]

letra = input("Escriba la letra que desea:")
if palabra1[0] == letra:
  resultado.append(palabra1)
elif palabra2[0] == letra:
  resultado.append(palabra2)
elif palabra3[0] == letra:
  resultado.append(palabra3)
elif palabra4[0] == letra:
  resultado.append(palabra4)
else:
  resultado.append("No hay palabras que empiecen por esa letra")
print(resultado)
  