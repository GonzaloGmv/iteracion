from math imprt sqrt
def cuadradosperfectos(n): 
  r=[]
  s=[]
  for i in range(n+1):
    s.append(i)
  for t in s:
    if sqrt(t) in s:
      r.append(t)
  print("los cuadrados perfectos son: " .format(n))
  for x in r:
    print(x)
if __name__==__main__:
  n=int(input("introduzca un numero entero: "))