import json

def addcpfs():

    #abrir arquivo Json para escrita
    #datacpfs = open("cpfs.json","w")

    #inserir chave/valor arquivo json de cpfs

    print("___________CADASTRO DE CPFS___________\n")
    cpf = input("Insira CPF:\n")
    tampletejson = '{"cpf":{}.'
    tampletejson = (tampletejson)
    cpfs = json.loads(tampletejson)
    print(cpfs['cpf'])


addcpfs()









