"""Atividade 16: Inversão de String
Solicitação: Crie um programa que peça uma string ao usuário e a exiba invertida.
Lógica: O programa precisa pegar a string fornecida pelo usuário e inverter a ordem dos
caracteres, podendo usar slicing ou um loop para construir a string invertida."""

frase = input("Digite uma frase: ")

fraseInvertida = ""

for letra in frase:
    fraseInvertida = letra + fraseInvertida

print("Palavra/Frase invertida: ", fraseInvertida)

