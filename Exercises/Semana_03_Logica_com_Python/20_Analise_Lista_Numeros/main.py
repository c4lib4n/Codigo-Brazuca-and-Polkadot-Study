"""Atividade 20: Análise de Lista de Números
Solicitação: Escreva um programa que peça ao usuário uma lista de números e, ao final, exiba o
maior, o menor, e a média dos números inseridos.
Lógica: O programa deve permitir que o usuário insira vários números, armazenando-os em
uma lista. Após a entrada de todos os números, o programa deve calcular e exibir o maior, o
menor e a média dos valores."""

numeros = []
numero = int(input("Digite os numeros ou digite 0 para sair: "))



contador = 0
while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite os numeros ou digite 0 para sair: "))
    contador += 1

maior = 0
soma = 0
menor = maior

for i in range(len(numeros)):
    soma += numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    else:
        menor = numeros[i]


media = 0;
media = soma / contador

print(contador)
print("Maior numero: ", maior, " Menor numero: ", menor, " Media: ", media)



