"""Atividade 8: Criando Funções
Exemplo: Definindo e chamando uma função
def saudacao(nome):
print("Olá,", nome + "!")
saudacao("Maria") # Chama a função saudacao com o argumento "Maria"
Atividade Prática:
Escreva uma função que receba um número e retorne se ele é par ou ímpar."""

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("Numero e par!")
else:
    print("Numero e Impar!")



