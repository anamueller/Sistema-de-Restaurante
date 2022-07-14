#cria um dicionario para cada categoria e adiciona os itens, depois cria um dicionario com os outros dicionarios de cada categoria

def criando_dics_cardapio(lista_de_categoria, cardapiodic):
    from criar_itens_categoria import adicionar_itens #função que adiciona os itens
    y = 0 #começa na primeira categoria digitada
    b = 0 #para criar o loop
    c = 0 #para adicionar os dicionarios ao cardapio
    while b < len(lista_de_categoria):
        indice = lista_de_categoria[y] #categoria que será utilizada na função
        indicedic = {} #criando o dicionario da categoria
        wish = ''
        m = 1 #key do dicionario
        while wish != 'terminado':
            print("\nVamos adicionar itens a categoria:", lista_de_categoria[y])
            ni = input("Digite o nome do item: ")
            p = input("Digite o preço do item: ")
            adicionar_itens(indicedic, indice, ni, p, m)
            m = m + 1 #proxima key do mesmo dicionario
            wish = input("\nDeseja adicionar mais itens? Se sim digite 'sim', se ja tiver terminado digite 'terminado'. ")
            cardapiodic[y] = indicedic
            newkey = indice
            oldkey = y
            cardapiodic[newkey]=cardapiodic.pop(oldkey)   
        b = b + 1 #continuar o loop até todas as categorias tiverem algum item
        y = y + 1 #para ir para a próxima categoria
    print("\nAqui está seu cardápio terminado. Caso encontre algum erro e queira editar espere até o final que te daremos essa opção.")
    for key, value in cardapiodic.items():
        print(key, '--')
        for subject, score in value.items():
            print(subject, ' : ', score)
    return cardapiodic
        
        
#criando uma nova categoria do cardapio, ex:bebidas
#nomecat = nome da categoria 
#ni = nome do item a ser adicionado na categoria, ex: coca cola
#p = preço do item

def adicionar_itens(indicedic, indice, ni, p, m):
    indicedic[m]= ni + " " + p
    print("O\n item adicionado na categoria", indice, "foi")
    print(indicedic[m])
    
#criando um dicionario com todos os clientes

def criar_cliente(x, nomecliente, endereço, clientesdic):
    clientesdic[x]= nomecliente + ", " + endereço
    return clientesdic

#criando um novo pedido
#ncardapio = número da comida ou bebida no cardápio
#ncliente = nome do cliente
#entregue = se o pedido já foi entregue ou não

def criar_pedido(x, ncardapio, ncliente, entregue, pedidodic):
    if entregue == 'nao':
        entregue1 = 'não entregue'
    if entregue == 'sim':
        entregue1 = 'foi entregue'
    pedidodic[x]= ncliente + " :" + ncardapio + ", " + entregue1
    return(pedidodic)
#fazer com que quando digitar o ncardápio apareça o nome da comida/bebida e não o número 

def dicionario_do_restaurante(nome_restaurantedic, cardapiodic, clientesdic, pedidodic):
    nome_restaurantedic['Cardápio'] = cardapiodic
    nome_restaurantedic['Clientes'] = clientesdic
    nome_restaurantedic['Pedidos'] = pedidodic
    return nome_restaurantedic