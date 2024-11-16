#Programa que lê duas notas de um aluno, apresenta a média e parabeniza-o se ele for aprovado (média mínima para aprovação é 6.0).

nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
media = (nota1+nota2) /2

print("A média é ", media)
if media >= 6.0:
  print("Parabéns você foi aprovado!")