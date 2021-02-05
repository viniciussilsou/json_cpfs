import json

def jsonopen(arquivo):
   arquivo = open("cpfs.json","w")

   return arquivo



def addcpfs():

    datacpfs = open("cpfs.json", "a")
    cpfs = json.load(datacpfs)
    cpf = int(input("Digite CPF:\n"))
    cpfs.append(cpf)
    cpfinsert = json.dumps(cpfs)
    datacpfs.write(cpfinsert)


addcpfs()








