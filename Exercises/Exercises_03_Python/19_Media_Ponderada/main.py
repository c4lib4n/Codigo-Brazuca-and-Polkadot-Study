"""Atividade 19: Média Ponderada
Solicitação: Crie um programa que calcule a média ponderada de três notas fornecidas pelo
usuário, considerando os pesos 2, 3 e 5.
Lógica: A média ponderada é calculada multiplicando cada nota pelo seu peso, somando os
resultados, e dividindo pela soma dos pesos. O programa deve receber as notas e aplicar essa
fórmula."""


nota1 = float(input("Dgite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

nota1 = nota1 * 2
nota2 = nota2 * 3
nota3 = nota3 * 5

pesos = 2+3+5

media_ponderada = (nota1 + nota2 + nota3) / (2+3+5)

print("Media ponderada: ", media_ponderada)


