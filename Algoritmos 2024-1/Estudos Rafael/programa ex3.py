"""""""""
Programa que lê duas notas de um aluno, apresenta a média e informa o resultado:
Aprovado: media maior ou igual a 6;
Exame: media maior ou igual a 3 e menor que 6;
Reprovado: nota menor que 3.
"""""""""

nota1 = float(input("Nota1:"))
nota2 = float(input("Nota2:"))
media = (nota1 + nota2) /2
print("A média é", media)
if media >= 6.0:
  print("Aprovado!")
elif media >= 3.0:
  print("Exame!")
else:
  print("Reprovado!")