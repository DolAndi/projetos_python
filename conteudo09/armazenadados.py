import os
# verificando se o arquivo existe [ini]
try:
    arquivo = open("banco.imed","r")
except:
    arquivo = open("banco.imed","w")
    arquivo.close()
# verificando se o arquivo existe [fim]

while True:
    os.system("cls")
    print("(1) - Inserir novo aluno")
    print("(2) - Ler alunos")
    print("(0) - Sair")
    opcao = input()
    if opcao == "1":
        arquivo = open("banco.imed","r")
        dados = arquivo.read()
        arquivo.close()
        nome = input("Nome: ")
        email = input("E-mail: ")
        dados = dados + nome + "->"+ email + "\n"
        arquivo = open("banco.imed","w")
        arquivo.write(dados)
        arquivo.close()
        print("Dados Salvos!")
        input()
    elif opcao == "2":
        arquivo = open("banco.imed","r")
        dados = arquivo.read()
        arquivo.close()
        print("Lista de Dados Cadatrados: ")
        print(dados)
        input()
    elif opcao == "0":
        break
    else:
        print('opção inválida')

print("Volte Sempre!")