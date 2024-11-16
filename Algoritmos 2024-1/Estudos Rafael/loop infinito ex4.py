#A instrução continue pula a interação atual e vai para a próxima interação do loop.

contador = 0
while contador < 5:
  contador += 1 
  if contador == 3:
    continue
  print("Contador:", contador)