import json

def inputcpf():

    cpf = input("Digite CPF:\n")
    return cpf

def convertecpf(cpf):
    
    cpf = int(cpf)
    return cpf
    
def addcpftolist(cpfdata):

    cpfs = []
    cpfs.append(cpfdata)
    return cpfs

def gravarlista(lista):

    jsonfile = open("cpfsfile.josn","w")
    datalist = json.dumps(lista)
    jsonfile.write(datalist)
    jsonfile.close()

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

    while func == "A":

        cpf = inputcpf()
        cpf = convertecpf(cpf)
        cpfs = addcpftolist(cpf)
        gravarlista(cpfs)
        print("CPF {} GRAVADO !".format(cpfs))
        func = selectfunction()

    else:
        print("Função Inválida ! Digite novamente:\n")
        func = selectfunction()






















