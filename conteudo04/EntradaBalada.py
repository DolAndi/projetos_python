idade = int(input("Informe a sua idade: "))


if idade >= 18:
    print("Você pode entrar e beber.")

elif idade == 16 and 17:
    print("Você pode entrar, porém não pode beber.")

elif idade <= 15:
    print("Você não pode entrar!")

print("Fim do programa.")