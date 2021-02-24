import json

def lerarquivo():

    with open("cpfsfile.json") as arquivo:
        cpfs = json.load(arquivo)

    return cpfs

def inserircpfnalista(cpf):

    cpfs = []
    cpfs.append(cpf)

    return cpfs


def gravallistanoarquivo(lista):

    with open("cpfsfile.josn","a+") as arquivo:

        listacpfs = json.dumps(lista)
        arquivo.write(listacpfs)




def main():

    cpf = int(input("Digite CPF:"))
    listacpf = inserircpfnalista(cpf)
    gravallistanoarquivo(listacpf)


































