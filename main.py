from insertcpf import inserircpf,excluircpf,selecionarfuncao,buscarcpf

def cadastrodecpsf():

    funcao = selecionarfuncao()
    cpf = input("Digite CPF:\n")

    if funcao == 'C':
        inserircpf(cpf)

    elif funcao == 'E':
        excluircpf(cpf)

    elif funcao == 'B':
        buscarcpf(cpf)

    else:
        print("Função Invalida !\n")
        cadastrodecpsf()

cadastrodecpsf()



