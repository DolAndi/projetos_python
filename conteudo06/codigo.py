deposito = 100
print("A Quantidade de Litros em deposito:", deposito)

while deposito > 0:
    abastecimento = int(input("Qtd. Litros: "))
    if deposito - abastecimento < 0:
        print("Não temos essa quantidade em estoque.")
    else:
        deposito = deposito - abastecimento
    print("A Quantidade de Litros em deposito:", deposito)


