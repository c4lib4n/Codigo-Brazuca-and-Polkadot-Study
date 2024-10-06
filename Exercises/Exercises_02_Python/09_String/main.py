"""Atividade 9: Manipulação de Strings
Exemplo: Manipulando strings
texto = "Python é incrível!"
print(texto.upper()) # Converte para maiúsculas
print(texto.replace("incrível", "poderoso")) # Substitui uma palavra
Atividade Prática:
Escreva um programa que peça uma frase ao usuário e conte quantas vezes uma letra
específica aparece"""


frase = input("Digite uma frase: ")
letra = input("Qual letra deseja contar? ")

quantidade_letras = frase.count(letra)

print("A frase ", frase, " contem ", quantidade_letras, " letras ", letra)
