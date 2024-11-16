#Um loop dentro de outro loop.
#O loop interno completa todas as suas interações para cada interação do loop externo.

i = 1
while i <= 3:
  j = 1
  while j <= 3:
    print(f"{i} x {j} = {i * j}")
    j += 1 
  i += 1