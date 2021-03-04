from insertcpf import inserircpf,excluircpf,selecionarfuncao,buscarcpf

def cadastrodecpsf():

    funcao = selecionarfuncao()
    cpf = input("Digite CPF:\n")

    if funcao == 'C' or 'c':
        inserircpf(cpf)

    elif funcao == 'E' or 'e':
        excluircpf(cpf)

    elif funcao == 'B' or 'b':
        buscarcpf(cpf)

    else:
        print("Função Invalida !\n")
        cadastrodecpsf()

cadastrodecpsf()



