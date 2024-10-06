"""Atividade 7: Média de Notas
Solicitação: Desenvolva um programa que calcule a média de várias notas inseridas pelo
usuário. O programa deve parar de pedir notas quando o usuário digitar -1.
Lógica: O programa precisa coletar notas até que o usuário insira o valor -1. A cada nova nota,
você deve somá-la a um total acumulado e contar quantas notas foram inseridas. No final,
divida a soma total pelo número de notas para calcular a média."""



media = 0
qdt = 0
while True:
    notas = float(input("Digite uma nota ou -1 para sair: "))
    if notas != -1 and notas > 0:
        media += notas
        qdt += 1
    elif notas == -1:
        break
    else:
        print("Digite uma nota maior que 0")

if qdt > 1:
    print("\nMedia: ", media / qdt)
else:
    print("\nNao a notas!")
