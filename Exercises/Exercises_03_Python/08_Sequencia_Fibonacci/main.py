"""Atividade 8: Sequência de Fibonacci
Solicitação: Escreva um programa que mostre os primeiros n números da sequência de
Fibonacci, onde n é informado pelo usuário.
Lógica: A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos
dois anteriores. O programa deve gerar a sequência até o enésimo termo solicitado pelo
usuário."""


numero = int(input("Ate qual numero voce deseja ver da sequencia de fibonace? "))

num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= numero:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
