"""Professor: Rodrigo Moreira
Atividade 3: Operações Matemáticas Simples
Exemplo: Realizando operações matemáticas básicas
a = 5
b = 3
soma = a + b # Soma
produto = a * b # Multiplicação
print("Soma:", soma)
print("Produto:", produto)
Atividade Prática:
Escreva um programa que peça dois números ao usuário e exiba a soma, subtração,
multiplicação e divisão deles.
"""

number1 = input("Digite o primeiro numero: ")
number2 = input("Digite o segundo numero: ")

soma = int(number1) + int(number2)
produto = int(number1) * int(number2)
subtracao = int(number1) - int(number2)
divisao = int(number1) / int(number2)

print("A soma e: ", soma, "A subtracao e: ", subtracao, "A multiplicacao e: ", produto, "A divisao e: ", divisao)

