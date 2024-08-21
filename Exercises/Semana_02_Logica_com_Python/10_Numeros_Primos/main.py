"""Atividade 10: Números Primos
Exemplo: Verificando se um número é primo
def eh_primo(numero):
if numero <= 1:
return False
for i in range(2, int(numero ** 0.5) + 1):
if numero % i == 0:
Professor: Rodrigo Moreira
return False
return True
print(eh_primo(7)) # Retorna True, pois 7 é primo
Atividade Prática:
Crie um programa que encontre e imprima todos os números primos em um intervalo
definido pelo usuário"""

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        return True


inicio = int(input("Digite o inicio do intervalo: "))
final = int(input("Digite o final do intervalo: "))

print("Os numeros primos entre ", inicio, " e ", final, " sao: ")
for numero in range(inicio, final + 1):
    if(eh_primo(numero)):
        print(numero)

