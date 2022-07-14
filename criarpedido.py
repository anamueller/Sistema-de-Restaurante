#criando um novo pedido
#ncardapio = número da comida ou bebida no cardápio
#ncliente = nome do cliente
#entregue = se o pedido já foi entregue ou não

def criar_pedido(x, ncardapio, ncliente, entregue, pedidodic):
    if entregue == 'nao':
        entregue1 = 'não entregue'
    if entregue == 'sim':
        entregue1 = 'foi entregue'
    pedidodic[x]= ncliente + ":" + ncardapio + ";" + entregue1
    return(pedidodic)
#fazer com que quando digitar o ncardápio apareça o nome da comida/bebida e não o número 