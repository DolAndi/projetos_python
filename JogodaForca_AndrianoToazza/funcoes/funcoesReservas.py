import random

#def carregaPalavraSecreta():
#    palavras = []
#    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
#        for linha in arquivo:
#            linha = linha.strip()
#            palavras.append(linha)
#
#    numero = random.randrange(0, len(palavras))
#    palavra_secreta = palavras[numero].upper()
#    return palavra_secreta

#def inicializarLetrasCertas(palavra):
#    return ["_" for letra in palavra]

#def pedeChute():
#    chute = input("Qual letra? ")
#    chute = chute.strip().upper()
#    return chute

#def ChuteCorreto(chute, letras_acertadas, palavra_secreta):
#    index = 0
#   for letra in palavra_secreta:
#        if (chute == letra):
#            letras_acertadas[index] = letra
#        index += 1