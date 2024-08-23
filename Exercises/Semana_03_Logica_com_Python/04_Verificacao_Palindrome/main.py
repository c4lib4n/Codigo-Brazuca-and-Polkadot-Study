"""Atividade 4: Verificação de Palíndromo
Solicitação: Crie um programa que verifique se uma palavra ou frase é um palíndromo.
Lógica: Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás para
frente. O programa deve comparar a string original com sua versão invertida. Se forem iguais, é
um palíndromo; caso contrário, não é."""

frase = input("Digite a palavra ou frase: ")

frase = frase.replace(" ", "").lower()

if frase == frase[::-1]:
    print("E um palindrome")
else:
    print("Nao e um palindrome")



