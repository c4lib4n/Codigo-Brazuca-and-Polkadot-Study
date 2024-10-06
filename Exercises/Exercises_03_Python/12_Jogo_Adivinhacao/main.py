import random

"""Atividade 12: Jogo de Adivinhação
Solicitação: Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o
usuário deve adivinhar qual é o número.
Lógica: O programa deve gerar um número aleatório e permitir que o usuário faça palpites,
dando dicas se o palpite foi maior ou menor que o número secreto, até que o usuário acerte."""


numero = random.randint(1, 100)

tentativa = int(input("Digite um numero para tentar acertar o numero secreto: "))

while tentativa != numero:
    if tentativa > numero:
        print("O numero digitado e maior que o escolhido!")
    else:
        print("O numero digitado e menor que o escolhido")
    tentativa = int(input("Digite outro numero! "))

print("\nParabens voce acertou o numero secreto!! ", numero)

