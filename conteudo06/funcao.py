# -------------- back-end (cálculos, base de dados, ....)
def calculaMedia(nota1, nota2):
    media = (nota1+nota2)/2
    return media

def digaOi():
    return "Hello World"


# -------------- front-end (interação com o usuário)
print("Bem-Vindo o Sistema")
resultado = calculaMedia(8, 7)
print("A média do aluno é:", resultado)

print("A média do aluno é:", calculaMedia(6, 9))
print("A média do aluno é:", calculaMedia(nota2=4, nota1=7))

print( digaOi() )
