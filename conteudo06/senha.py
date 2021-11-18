import os
import time
while True:
    os.system("cls")
    usuario = input("Informe o usuário: ")
    senha = input("Informe o senha: ")
    if usuario == "IMED" and senha == "2021":
        break
    else:
        print("Usuário ou Senha Inválidos!")
    time.sleep(3)


print("Bem-Vindo ao Sistema")
