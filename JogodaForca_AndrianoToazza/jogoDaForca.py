import os
import getpass
import netrc
import random

from funcoes.funcoesJogo import limparTela, espera, desintegrar
from funcoes.funcoesCompletas import Vencedor, Perdedor, DesenhoForca
#from funcoes.funcoesReservas import 

Palavra = ""
Copia = ""
Acertos = 0
Tentat = 5
LErros = 0
Id = tam = 0
Acerto = False
Letras = ""
Letra = ""

print("=================================")
print("========= JOGO DA FORCA =========")
print("=================================")
try:
    Palavra = str(input("Digite uma Palavra para Ocultar: ")).upper()
    nomeDesafiante = str(input("Insira o nome do desafiante: ")).upper()
    nomeCompetidor = str(input("Insira o nome do competidor: ")).upper()
    while Palavra.isnumeric():
        print("> Palavra Inválida. Tente Novamente...")
        Palavra = str(input("Digite uma Palavra para Ocultar: ")).upper()
except ValueError:
    print("> Valor Inválido.")

tam = len(Palavra)
limparTela()
print("Sejam bem vindos", nomeDesafiante, "e", nomeCompetidor)
print("Palavra ocultada com Sucesso!")
PalavraCóp = list()
for ele in Palavra:
    PalavraCóp.append(ele.replace(ele, '_'))

while Acertos < tam or Tentat < 5:
    print("\nPalavra é: ", end='')
    for item in PalavraCóp:
        print(f"{item}", end=' ')
    print("\033[m")

    try:
        Letra = str(input("Digite uma Letra: ")).upper()[0]
        Letras += Letra
        while Letra.isnumeric():
            print("Letra Inválida. Tente Novamente...")
            Letra = str(input("Digite uma Letra: ")).upper()[0]
            Letras += Letra
    except ValueError():
        print("Valor Inválido.")

    for c, value in enumerate(Palavra):
        if value == Letra:
            print(f"Letra [{Letra}] encontrada com sucesso.")
            PalavraCóp[c] = Letra
            Acerto = True
            Acertos += 1

    if Acertos == tam:
        Vencedor(Palavra)
        break

    if Acerto == False:
        LErros += 1
        Tentat-=1
        DesenhoForca(LErros)
        print(f"Letra [{Letra}] não encontrada. Tente Novamente...")
        print("Tentativas restantes: [{}].".format(Tentat))

    if Tentat == 0:
        Perdedor(Palavra)
        print("========= FIM ==========")
        print("As tentativas acabaram.")
        print("O desafiante ganhou!")
        break
    Acerto = False

print("=========================================================")
print(f" => Letras Digitadas: [{Letras}]")
print(f" => Total de Letras Digitadas: [{len(Letras)}]")
print(f" => Total de Tentativas com sucesso: [{tam}]")
print(f" => Total de Tentativas Erradas: [{LErros}]")
print("=========================================================")

arquivo = open("historico.txt", "a")
arquivo.write("Palavra: " + Palavra + " -> Participantes: " + nomeDesafiante + " e " + nomeCompetidor + "\n")
