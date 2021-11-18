g1 = float(input("Qual é a sua nota G1? "))
g2 = float(input('Qual é a sua nota G2? '))
media = (g1 + g2) / 2
print('A nota média dessa pessoa é de {:.1f}'.format(media))

#Condições das notas 
if media < 7:
    print('A sua nota está abaixo da média')
elif media > 7:
    print('A sua nota está cima da média')
elif media == 7:
    print('A sua nota está na média')