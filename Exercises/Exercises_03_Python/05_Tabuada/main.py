"""Atividade 5: Tabuada
Solicitação: Escreva um programa que exiba a tabuada de um número fornecido pelo usuário.
Lógica: Para gerar a tabuada de um número, você deve multiplicar o número por cada valor de
1 a 10. O programa deve iterar de 1 a 10, multiplicando o número fornecido e exibindo os
resultados."""

numero = int(input("Digite um numero para saber a tabuada: "))
i = 1
while i <= 10:
    tabuada = numero * i
    print(i, " * ", numero, " = ", tabuada)
    i += 1

