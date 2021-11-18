# w - write
# r - read
# a - append
#            nome do arquivo , modo de operação
'''
arquivo = open("banco.imed", "r")
dados = arquivo.read()
arquivo.close() #boa prática 

nome = input("Informe o nome do aluno: ")
email = input("Informe o e-mail do aluno: ")
dados = dados + nome + " -> " + email + "\n"

arquivo = open ("banco.imed", "w")
arquivo.write(dados)
arquivo.close()


'''
print("Mostrando Histórico de Alunos: ")
arquivo = open("banco.imed", "r")
dados = arquivo.readlines()
for linha in dados:
    print(linha)

arquivo.close() #boa prática 



