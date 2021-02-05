import json

def inputcpf():
    cpf = input("Digite CPF:\n")
    return cpf

def addcpftolist(cpfdata):

    cpfs = []
    cpfs.append(cpfdata)

    return cpfs

def loaddatajsonfile():

    newfile = open("venv/cpfsfile.json", "w")

    return newfile

def jsonclose(jsonfile):

    return jsonfile.close()


def jsondumps(data):

    datafile = json.dumps(data)
    return datafile

def selectfunction():

    func = input("DIGITE A FUNÇÃO DESEJADA:\n"
          "A - ADICIONAR NOVO CPF.\n"
          "E - EXCLUIR CPF\n"
          "C - CONSULTAR CPF\n")

    return func

def main():

    func = selectfunction()

    if func == 'A':

        cpf = inputcpf()
        cpfs = addcpftolist(cpf)
        newfile = loaddatajsonfile()
        datafile = jsondumps(cpfs)
        newfile.write(datafile)
        jsonclose(newfile)


    else:
        print("VALOR INVALIDO!\n")
        print(func)

main()



















