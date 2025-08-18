import random
dado=0
contador=0
puntaje=0
while contador<10 and puntaje<38:
  dado=random.randint(1,6)
  print(dado)
  puntaje=puntaje+dado
  contador=contador+1
print("El puntaje total es: " + str(puntaje))
if puntaje >=38:
  print("Ganaste")
else:
  print("Perdiste")