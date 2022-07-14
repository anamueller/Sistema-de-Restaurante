#criando um dicionario com todos os clientes

def criar_cliente(x, nomecliente, endereço, clientesdic):
    clientesdic[x]= nomecliente + ", " + endereço
    return clientesdic