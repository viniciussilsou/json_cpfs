import json

def lerarquivo():

    with open("cpfsfile.json") as arquivo:
        jsonlist = json.load(arquivo)

        return jsonlist


def gravallistanoarquivo(lista):

    with open("cpfsfile.json","w") as arquivo:

        listacpfs = json.dumps(lista)
        arquivo.write(listacpfs)

def main():

    lista = lerarquivo()
    cpf = input("Digite o CFP:\n")
    lista.append(cpf)
    gravallistanoarquivo(lista)


def excluircpf():

    lista = lerarquivo()
    cpf = input("Digite o CPF que deseja excluir:\n")
    indice = lista.index(cpf)
    lista.remove(cpf)

excluircpf()



































