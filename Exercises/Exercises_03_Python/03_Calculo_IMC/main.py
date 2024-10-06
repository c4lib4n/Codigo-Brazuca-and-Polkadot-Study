"""Atividade 3: Cálculo de IMC
Solicitação: Escreva um programa que peça o peso e a altura de uma pessoa e calcule seu
Índice de Massa Corporal (IMC).
Lógica: O IMC é calculado dividindo o peso de uma pessoa em quilogramas pelo quadrado da
sua altura em metros. O programa deve receber esses dois valores, aplicar a fórmula IMC =
peso / (altura * altura) e exibir o resultado."""


peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a Altura da pessoa: "))

imc = peso / (altura * altura)

print("IMC: ", imc)

