"""Atividade 6: Somatório com While
Exemplo: Usando um laço while para somar números
soma = 0
contador = 1
while contador <= 5:
soma += contador
contador += 1
print("A soma dos números de 1 a 5 é:", soma)
Atividade Prática:
Crie um programa que pergunte ao usuário por números até que ele digite zero e
então mostre a soma dos números digitados.
"""

numero = int(input("Digite um numero ou zero para sair: "))
soma =0

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um numero ou zero para sair: "))

print("A soma dos numeros digitados", soma)