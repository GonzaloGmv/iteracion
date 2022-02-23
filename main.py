from ejercicio12 import cuadradosperfectos
from ejercicio9 import ejercicio9
from ejercicio8 import descomposicion
from ejercicio11 import ejercicio11

ejercicio = input("Escriba el numero del ejercicio que quiere que se ejecute: ")

if ejercicio == '12':
  cuadradosperfectos(int(input("introduzca un numero entero: ")))
elif ejercicio == '9':
  ejercicio9() 
elif ejercicio == '8':
  descomposicion() 
elif ejercicio == '11':
  ejercicio11() 