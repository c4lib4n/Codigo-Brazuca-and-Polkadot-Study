"""Atividade 17: Verificação de Número Perfeito
Solicitação: Escreva um programa que verifique se um número dado é um número perfeito.
Lógica: Um número perfeito é um número que é igual à soma dos seus divisores próprios
(excluindo ele mesmo). O programa deve encontrar todos os divisores de um número e somá-
los para verificar essa condição."""


numero = int(input("Digite um numero: "))

somaDivisao = 0
for i in range(1, numero):
    if numero % i == 0:
        somaDivisao += i

if somaDivisao == numero:
    print("\nNumero perfeito!")
else:
    print("Nao é um numero perfeito!")
