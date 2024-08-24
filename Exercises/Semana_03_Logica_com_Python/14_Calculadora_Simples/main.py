"""Atividade 14: Calculadora Simples
Solicitação: Crie um programa que funcione como uma calculadora simples, pedindo ao
usuário dois números e a operação que deseja realizar.
Lógica: O programa deve pedir dois números e um operador (+, -, *, /). Dependendo do
operador fornecido, o programa deve executar a operação correspondente e exibir o resultado"""

numero1 = float(input("Digite o primeiro numero a ser calculado: "))
numero2 = float(input("Digite o segundo numero a ser calculado: "))
operacao = input("Qual operacao deseja efetuar? ")

if operacao == "+":
    print("A soma dos numeros:", numero1, "+", numero2, "=", numero1 + numero2)
elif operacao == "-":
    print("A diminuicao dos numeros:", numero1, "-", numero2, "=", numero1 - numero2)
elif operacao == "*":
    print("A multiplicacao dos numeros:", numero1, "*", numero2, "=", numero1 * numero2)
else:
    print("A divisao dos numeros:", numero1, "/", numero2, "=", numero1 / numero2)

