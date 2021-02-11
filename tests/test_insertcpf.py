from insertcpf import convertecpf, addcpftolist


def test_convertecpf():
    cpf = "377464645"
    cpf_convertido = convertecpf(cpf)

    assert isinstance(cpf_convertido, int)
    #assert cpf_convertido == "377464645"

def test_verificalista():

    cpf= 35353535535
    cpfslist = addcpftolist(cpf)

    assert len(cpfslist) != 0