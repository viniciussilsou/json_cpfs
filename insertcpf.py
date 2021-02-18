import json

def inputcpf():

    cpf = input("Digite CPF:\n")
    return cpf

def convertecpf(cpf):
    
    cpf = int(cpf)
    return cpf
    
#def addcpftolist(cpfdata):

#    cpfs = []
 #   cpfs.append(cpfdata)
  #  return cpfs

def readcpf(cpfdata):

    with open("cpfsfile.json") as cpfsfile:
        listline = cpfsfile.readline()
        listline.append(cpfdata)

        return listline

def gravarlista(lista):


    with open("cpfsfile.json") as jsonfile:

        datalist = json.dumps(lista)
        jsonfile.write(datalist)


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
        #cpfs = addcpftolist(cpf)
        cpfs = readcpf(cpf)
        gravarlista(cpfs)
        print("CPF {} GRAVADO !".format(cpfs))
        func = selectfunction()

    else:
        print("Função Inválida ! Digite novamente:\n")
        func = selectfunction()






















