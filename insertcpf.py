import json

def inputcpf():

    cpf = input("Digite CPF:\n")
    return cpf

def convertecpf(cpf):
    
    cpf = int(cpf)
    return cpf

def addcpftolist(cpf):

    with open("cpfsfile.josn","w") as cpfsfile:

        listline = json.loads(cpfsfile)
        listline.append(cpf)

        return listline

def gravarlistajsonfile(lista):

    with open("cpfsfile.josn","a+") as jsonfile:

        datalist = json.dumps(lista)
        jsonfile.write(str(datalist))


def selectfunction():

    func = input(
          "\nDIGITE A FUNÇÃO DESEJADA:\n"
          "\n"
          "A - ADICIONAR NOVO CPF\n"
          "E - EXCLUIR CPF\n"
          "C - CONSULTAR CPF\n")

    return func

def main():

    func = selectfunction()

    open("cpfsfile.josn","w")

    if func == "A":

            cpf = inputcpf()
            cpf = convertecpf(cpf)
            #cpfs = addcpftolist(cpf)
            cpfs = addcpftolist(cpf)
            gravarlistajsonfile(cpfs)
            print("CPF {} GRAVADO !".format(cpfs))
            func = selectfunction()

    else:
        print("Função Inválida ! Digite novamente:\n")
        func = selectfunction()






















