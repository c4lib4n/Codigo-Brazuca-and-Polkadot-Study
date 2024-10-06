"""Atividade 9: Ordenação de Números
Solicitação: Crie um programa que leia três números diferentes e os imprima em ordem
crescente.
Lógica: O programa precisa comparar os três números e ordená-los do menor para o maior.
Isso pode ser feito usando condições if-else para comparar cada par de números."""

primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
terceiro_numero = float(input("Digite o terceiro numero:"))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]
numeros.sort()

print(numeros)