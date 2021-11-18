
listaNotas = []

for nota in range(0,4):
    nota = float(input("Digite uma nota: "))
    listaNotas.append(nota)

i = 0
soma = 0

while i <len(listaNotas):
    print("Nota:", listaNotas[i])
    soma = soma + listaNotas[i]
    i = i + 1

print("Media: ", soma/len(listaNotas))