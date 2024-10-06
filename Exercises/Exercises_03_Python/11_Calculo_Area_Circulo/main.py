"""Atividade 11: Cálculo de Área de Círculo
Solicitação: Desenvolva um programa que calcule a área de um círculo a partir do raio
fornecido pelo usuário.
Lógica: A fórmula da área de um círculo é A = πr², onde r é o raio do círculo. O programa deve
pedir o raio, aplicar a fórmula e exibir o resultado."""

raio = float(input("Digite o raio: "))

area = 3.14 * raio ** 2

print("Area do circulo: ", area)

