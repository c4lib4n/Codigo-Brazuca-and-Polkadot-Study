"""Atividade 15: Soma dos N primeiros Números
Solicitação: Escreva um programa que peça ao usuário um número n e calcule a soma dos
primeiros n números naturais.
Lógica: A soma dos primeiros n números naturais pode ser encontrada usando a fórmula da
soma de uma progressão aritmética ou iterando de 1 até n e acumulando a soma."""

numero = int(input("Digite um numero natural: "))
soma = 0

for i in range(1, numero+1):
    soma += i


print("A soma dos primeiros numeros naturais de ", numero, " sao ", soma)

