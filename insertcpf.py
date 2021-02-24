import json

def lerarquivo():

    with open("cpfsfile.json") as arquivo:
        jsonlist = json.load(arquivo)

        return jsonlist


def gravallistanoarquivo(lista):

    with open("cpfsfile.josn","w") as arquivo:

        listacpfs = json.dumps(lista)
        arquivo.write(listacpfs)

def main():

    lista = lerarquivo()
    cpf = input("Digite o CFP:\n")
    lista.append(cpf)
    gravallistanoarquivo(lista)



































