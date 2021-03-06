peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

#Condições do IMC
if imc < 17:
    print('Muito abaixo do peso')
    print('O que pode acontecer?\nQueda de cabelo, infertilidade, ausência menstrual')
elif imc < 18.5:
    print('Abaixo do peso')
    print('O que pode acontecer?\nFadiga, stress, ansiedade')
elif imc < 25:
    print('Peso normal')
    print('O que pode acontecer?\nMenor risco de doenças cardíacas e vasculares')
elif imc < 30:
    print('Acima do peso')
    print('O que pode acontecer?\nFadiga, má circulação, varizes')
elif imc < 35:
    print('Obesidade Grau I')
    print('O que pode acontecer?\nDiabetes, angina, infarto, aterosclerose')
elif imc <= 40:
    print('Obesidade Grau II')
    print('O que pode acontecer?\nApneia do sono, falta de ar')
else:
    print('Obesidade Grau III')
    print('O que pode acontecer?\nRefluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC')
