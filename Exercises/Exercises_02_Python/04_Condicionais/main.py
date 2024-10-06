"""Atividade 4: Estruturas Condicionais
Exemplo: Usando condições para tomar decisões
idade = int(input("Qual é a sua idade? "))
if idade >= 18:
print("Você é maior de idade.")
else:
print("Você é menor de idade.")
Atividade Prática:
Escreva um programa que peça a temperatura atual e diga se está quente (acima de
30°C), frio (abaixo de 15°C) ou agradável (entre 15°C e 30°C).
"""


temperatura = float(input("Temperatura atual: "))
if temperatura > 30:
    print("Esta calor")
elif temperatura < 15:
    print("Esta frio")
else:
    print("Esta agradavel")

