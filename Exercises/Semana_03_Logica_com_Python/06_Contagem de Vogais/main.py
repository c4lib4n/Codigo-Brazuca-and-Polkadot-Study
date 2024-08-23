"""Atividade 6: Contagem de Vogais
Solicitação: Crie um programa que peça uma frase ao usuário e conte quantas vogais (a, e, i, o,
u) ela contém.
Lógica: O programa deve percorrer cada letra da frase e verificar se é uma vogal. Você pode
fazer isso usando um loop e uma condição para verificar se a letra pertence ao conjunto de
vogais."""

def conta_vogais(string):
    string = string
    result = 0
    vogais = 'aeiouAEIOU'
    for i in vogais:
        if i in string:
            result += 1
    return result

frase = input("Digite uma frase: ")

print("A frase: ", frase, " contem: ", conta_vogais(frase), " vogais!" )

