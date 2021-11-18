
while True:
    try:
        nota = int(input("Nota: "))
        print(nota)
        break
    except:
        print("Valor informado incorretamente!")


print("Acabou o programa")