"""Atividade 13: Soma de Números Pares
Solicitação: Escreva um programa que calcule a soma de todos os números pares entre 1 e
100.
Lógica: Para somar todos os números pares entre 1 e 100, o programa deve iterar por esses
números, verificando se cada um é par (divisível por 2) e, se for, adicioná-lo a uma soma
acumulada"""

par = 0
for i in range(1, 101):
    if i % 2 == 0:
        print("numero: ", i)
        par += i

print("Soma dos numeros pares! ", par)

