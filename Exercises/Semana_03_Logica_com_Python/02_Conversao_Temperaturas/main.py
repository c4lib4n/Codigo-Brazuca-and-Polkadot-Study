"""Atividade 2: Conversão de Temperaturas
Solicitação: Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit
e Kelvin.
Lógica: A conversão de temperaturas segue fórmulas matemáticas específicas. Para converter
de Celsius para Fahrenheit, você deve usar a fórmula (C * 9/5) + 32. Para converter de Celsius
para Kelvin, a fórmula é C + 273.15. O programa deve pedir a temperatura em Celsius e realizar
as conversões"""


celsius = int(input("Digite uma temperatura em Celsius: "))

print("Temperatura em Fahrenheit: ", (celsius * 9/5) + 32 )
print("\nTempratura em Kelvin: ", (celsius + 273.15))

