"""Atividade 7: Trabalhando com Listas
Exemplo: Manipulando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva") # Adiciona uma fruta à lista
for fruta in frutas:
print("Fruta:", fruta)
Atividade Prática:
Crie uma lista de compras que permita ao usuário adicionar itens e, em seguida,
imprimir a lista completa."""

lista_de_compras = []

while True:
    item = input("\nDigite um item para adicionar a lista ou 'sair' para fechar: ")
    if item.lower() == "sair":
        break
    lista_de_compras.append(item)

    print("\nLista de Compras: ")
    for item in lista_de_compras:
        print(item)



