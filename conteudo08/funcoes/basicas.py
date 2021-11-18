#FUNÇÕES BÁSICAS DO PROJETO
import os
import time

def espera(tempo):
    time.sleep(tempo)

def limparTela():
    #time.sleep(1)    
    os.system("cls")

def changeColor(cor):
    if cor == "branco":
        os.system("color 7")
    elif cor == "verde":
        os.system("color 2")
    elif cor == "vermelho":
        os.system("color 4")
    else:
        os.system("color 7")

def teste():
    print("teste")