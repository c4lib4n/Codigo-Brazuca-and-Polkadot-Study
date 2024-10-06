"""Atividade 18: Contagem de Palavras
Solicitação: Desenvolva um programa que conte quantas palavras há em uma frase fornecida
pelo usuário.
Lógica: O programa deve dividir a frase em palavras usando espaços como delimitadores e
contar quantas palavras resultaram dessa divisão."""


frase = str(input("Digite uma frase: "))

contagem = len(frase.split())

print(contagem)

