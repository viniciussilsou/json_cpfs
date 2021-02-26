from insertcpf import inserircpf,excluircpf,selecionarfuncao

def cadastrodecpsf():

    funcao = selecionarfuncao()

    if funcao == 'C':
        inserircpf()
    elif funcao == 'E':
        excluircpf()
    else:
        print("Função Inválida !")

cadastrodecpsf()