import json

def lerarquivo():

    with open("cpfsfile.json") as arquivo:
        jsonlist = json.load(arquivo)

        return jsonlist

def gravallistanoarquivo(lista):

    with open("cpfsfile.json","w") as arquivo:

        listacpfs = json.dumps(lista)
        arquivo.write(listacpfs)

def inserircpf():

    lista = lerarquivo()
    cpf = input("Digite o CFP:\n")
    lista.append(cpf)
    gravallistanoarquivo(lista)

def excluircpf():

    lista = lerarquivo()
    cpf = input("Digite o CPF que deseja excluir:\n")
    lista.remove(cpf)
    gravallistanoarquivo(lista)


def selecionarfuncao():

    funcao = input("ESCOLHA UMA OPÇÃO:\n"
          "\n"
          "DIGITE - C - PARA CADASTRAR CPF\n"
          "DIGITE - E - PARA EXCLUIR CPF\n")

    return funcao






































