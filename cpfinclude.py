import json

def addcpfs():

    #abrir arquivo Json para escrita
    datacpfs = open("cpfs.json","w")
    tampletejson = {'cpf':''}
    datacpfs.write(str(tampletejson))

#######################################################
    print("___________CADASTRO DE CPFS___________\n")
    cpf = input("Insira CPF:\n")
#######################################################
    #adicionar cpf ao valor da chave




addcpfs()









