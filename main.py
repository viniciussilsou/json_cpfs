from insertcpf import inserircpf,excluircpf,selecionarfuncao,buscarcpf

def cadastrodecpsf():

    funcao = selecionarfuncao()

    if funcao == 'C':
        inserircpf()

    elif funcao == 'E':
        excluircpf()

    elif funcao == 'B':
        buscarcpf()

    else:
        print("Função Inválida !")

cadastrodecpsf()

repetir = input("EXECUTAR NOVAMENTE ? S/N")
if repetir == "S":
    cadastrodecpsf()
else:
    print("FIM")
