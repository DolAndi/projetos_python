listaNotas = [6.0, 7.0, 5.0, 8.0]

i = 0
soma = 0

while i <len(listaNotas):
    print("Nota:", listaNotas[i])
    soma = soma + listaNotas[i]
    i = i + 1

print("Media: ", soma/len(listaNotas))
