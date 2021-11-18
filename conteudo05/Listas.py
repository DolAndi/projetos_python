#array
# todo index começa no valor 0

#             0      1         2       3
fruteira = ["Uva", "Maça", "Banana", "Pera"]  #[] é sempre uma lista

fruta = input("Informe o nome da Fruta: ")
fruteira.append(fruta) #append é a função para add

print(fruteira[0]) #printando a uva
print("Lista:", fruteira)
print("Melancia está na lista:", "Melancia" in fruteira)
print("Maça está na lista:", "Maça" in fruteira)


# para gerar listas automaticas list(range(0,5))
numeros = list(range(0, 4))
print(numeros)

#len = lenght  -> mostra o tamanho da lista, no caso: 4
print("Tamanho da lista: ",len(fruteira))