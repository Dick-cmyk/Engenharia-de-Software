#A variável número nunca é atualizada, então a condição nunca deixará de ser  verdadeira.

soma = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
  soma += int(input("Digite um número(0 para sair): "))
print("A soma é:", soma)