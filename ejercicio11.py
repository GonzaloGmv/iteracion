def ejercicio11():
  numero1 = int(input("Escriba un numero: "))
  numero2 = int(input("Escriba otro numero: "))
  op1 = numero1
  op2 = numero2
  
  if numero1 == numero2:
    print("El mcd es ", numero1)
    
  elif numero1 > numero2:
      while numero1 > op2:
          op2 = op2 + numero2
      resto = op2 - numero1
      restor = op2 - numero2
      resto1 = numero1 - restor
      opR = resto1
      if resto == 0:
          print("El mcd es ", numero2)
      else:
          while True:
              resto1 = opR
              while opR < numero2:
                  opR = opR + resto1
              resto = opR - numero2
              restor = opR - resto1
              resto2 = numero2 - restor
              if resto == 0:
                  print("El mcd es ", resto1)
                  break
              else:
                  numero2 = resto1
                  opR = resto2
                  pass
                
  else:
      while numero2 > op1:
          op1 = op1 + numero1
      resto = op1 - numero2
      restor = op1 - numero1
      resto1 = numero2 - restor
      opR = resto1
      if resto == 0:
          print("El mcd es ", numero1)
      else:
          while True:
              resto1 = opR
              while opR < numero1:
                  opR = opR + resto1
              resto = opR - numero1
              restor = opR - resto1
              resto2 = numero1 - restor
              if resto == 0:
                  print("El mcd es ", resto1)
                  break
              else:
                  numero2 = resto1
                  opR = resto2
                  pass