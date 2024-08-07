playlist = ["Odiosa natureza humana", "Bom e quando faz mal", "Bixo do Mato", "Ouro de tolo"]

for i in range(len(playlist)):
    print(f"Musica {i +1}: {playlist[i]}")
playlist.append("Outra musica")
print("Playlist depois de adicionada a musica: ", playlist)
playlist.remove("Odiosa natureza humana")
print("Playlist depois de removida a musica: ", playlist)
print("kkkkk")