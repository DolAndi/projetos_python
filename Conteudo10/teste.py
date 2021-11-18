#              Key    :   value        key :  value          key  :   value
telefonesMarcos = {'Marcos': '99999 9999',
                   'João': '98888 8888', 'Biel': '97777 7777'}

telefonesGabriel = {'Pedrinho': "96666 6666",
                    "Joana": "95555 55555", "Biel": "94444 4444"}
telefonesMarcos.update(telefonesGabriel)

print("########## Contatos:  #######")
for contato in telefonesMarcos:
    print("Name:", contato, "Phone:", telefonesMarcos[contato])
print("#############################")

busca = input("Search: ")
# Marcos
# lower = marcos
# upper = MARCOS
# captalize =  Marcos

for contato in telefonesMarcos:
    if (busca in contato):
        print("Contato Encontrado:", contato, telefonesMarcos[contato])

#print(telefonesMarcos.get(busca, "Nenhum registro encontrado"))
