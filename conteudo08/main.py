from funcoes.basicas import limparTela, changeColor, espera
from funcoes.cripto import decriptografar, criptografar
from funcoes.sound import emitirSom
# FRONT-END *******************************************************************************

for i in range(10, 0, -1):
    limparTela()
    print(i)
    emitirSom(100)
    espera(0.5)


while True:
    changeColor("branco")
    limparTela()
    emitirSom(100)
    print("Seja Bem-Vindo ao Sistema de Criptografia!")
    print("(1) - Criptografar")
    print("(2) - Decriptograr")
    print("(0) - Sair")
    opcao = input("Opçao: ")
    if opcao == "1":
        changeColor("verde")
        limparTela()
        print("Informe o texto a ser criptografado:")
        texto = input()
        print(criptografar(texto))
        emitirSom(100)
    elif opcao == "2":
        changeColor("vermelho")
        limparTela()
        print("Informe o texto a ser decriptografado:")
        cripto = input()
        print(decriptografar(cripto))
        emitirSom(100)
    elif opcao == "0":
        break
    else:
        print('Opção Inválida')
    input("press enter to continue")

print("Volte Sempre! :)")
