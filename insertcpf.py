import json

def selecionarfuncao():

    funcao = input("ESCOLHA UMA OPÇÃO:\n"
          "\n"
          "DIGITE - C - PARA CADASTRAR CPF\n"
          "DIGITE - E - PARA EXCLUIR CPF:\n"
          "DIGITE - B - PARA BUSCAR CPF:\n")

    return funcao

def lerarquivo():

    with open("cpfsfile.json") as arquivo:
        jsonlist = json.load(arquivo)

        return jsonlist

def gravallistanoarquivo(lista):

    with open("cpfsfile.json","w") as arquivo:

        listacpfs = json.dumps(lista)
        arquivo.write(listacpfs)

def inserircpf(cpf):

    lista = lerarquivo()
    lista.append(cpf)
    gravallistanoarquivo(lista)
    print("CPF Incluído com sucesso !")

def excluircpf(cpf):

    confirma = input("Confirma a exclusão do CPF {} ? S/N\n".format(cpf))

    if confirma == "S" or 's':
        lista = lerarquivo()
        lista.remove(cpf)
        gravallistanoarquivo(lista)
        print("CPF Deletado com sucesso !")
    else:
        selecionarfuncao()


def buscarcpf(cpf):

    lista = lerarquivo()
    if cpf in lista:
        print("CPF Existe !")

    else:
        print("CPF não existe!")
        incluir = input("Deseja inserir ? S/N\n")

        if incluir == "S":
            inserircpf(cpf)

        elif incluir == "N":
            print("VSF")









































