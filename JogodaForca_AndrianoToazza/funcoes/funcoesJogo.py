
import getpass
import netrc
import os
import time
import random

def espera(tempo):
    time.sleep(tempo)

def limparTela():
    os.system('cls')
    print("\n" *10)

def desintegrar(string):
    CPalavra = list()
    for c in string:
        CPalavra.append(c.upper())
    print(CPalavra)
