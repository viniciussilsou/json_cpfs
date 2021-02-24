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

def addcpftolist(cpf):

    with open("cpfsfile.josn") as cpfsfile:

        listline = json.loads(cpfsfile)
        listline.append(cpf)

        return listline

def gravarlistajsonfile(lista):

    with open("cpfsfile.josn") as jsonfile:

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

    while func == "A":

            cpf = inputcpf()
            cpf = convertecpf(cpf)
            #cpfs = addcpftolist(cpf)
            open("cpfsfile.josn","r")
            cpfs = addcpftolist(cpf)
            gravarlistajsonfile(cpfs)
            print("CPF {} GRAVADO !".format(cpfs))
            func = selectfunction()

    else:
        print("Função Inválida ! Digite novamente:\n")
        func = selectfunction()






















