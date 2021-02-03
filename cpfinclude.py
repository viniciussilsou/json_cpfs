import json

def addcpfs():

    #abrir arquivo Json para escrita
    datacpfs = open("cpfs.json","w")

    #inserir chave/valor arquivo json de cpfs

    print("___________CADASTRO DE CPFS___________\n")
    cpf = input("Insira CPF:\n")
    tampletejson = {'cpf':'{}'.format(cpf)}
    datacpfs.write(str(tampletejson))






addcpfs()









