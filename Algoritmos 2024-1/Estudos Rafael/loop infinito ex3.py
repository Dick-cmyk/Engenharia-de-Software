#A instrução break encerra o loop imediatamente 
#O bloco else não é executado se o loop for interrompido com break.

contador = 1
while contador <= 5:
  if contador == 3:
    print ("Saindo do loop.")
    break
  print (contador)
  contador += 1 
else:
  print("Loop concluído naturalmente.")