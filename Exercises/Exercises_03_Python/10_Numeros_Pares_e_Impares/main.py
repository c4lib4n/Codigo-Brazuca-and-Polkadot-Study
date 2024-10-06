"""Atividade 10: Números Pares e Ímpares
Solicitação: Escreva um programa que peça ao usuário um número inteiro e informe se ele é
par ou ímpar.
Lógica: A paridade de um número pode ser determinada pelo resto da divisão do número por
2. Se o resto for 0, o número é par; se for 1, é ímpar."""


numero = int(input("Type a number "))

if numero % 2 == 0:
    print(numero, " is even")
else:
    print(numero, " is odd")


