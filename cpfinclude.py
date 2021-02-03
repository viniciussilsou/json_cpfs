import json

def addcpfs():
    #abrindo arquivo json
    datacpfs = open("cpfs.json", "w")

    #tamplate do objeto cpf
    tampletecpfsjson = {}
    #atribuindo valor a variavel cpf
    cpf = input("Digite CPF:\n")
    #definindo chave/valor ao objeto json colocando a variavel cpf como "valor"
    tampletecpfsjson['cpf'] = cpf
    json_cpfdata = json.dumps(tampletecpfsjson)
    datacpfs.write(json_cpfdata)


addcpfs()








