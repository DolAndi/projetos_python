lista1 = [10, 12, 34, 45, 62, 74, 85, 89, 97, 102]
lista2= ["Maria", "Pedro", "Tiago"]
lista3= [11,22,33,44]

#append, insere no final da lista
lista1.append(18)
lista2.append("Teste")

#extend
lista3.extend(lista1)

#insert, precisa informar a posicao
lista1.insert(0,5)

#remove
lista1.remove(34)

#ordena itens da lista
# lista1.sort()

#reverse() inverte a ordem dos elementos na lista
# lista1.reverse()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////

#testes no terminal
print(lista2[0])
print(lista1[1])

print(lista1)
print(lista2)
print(lista3)

#index
print(lista1.index(45))

#count - retorna nº de vezes do valor na lista
print(lista1.count(12))