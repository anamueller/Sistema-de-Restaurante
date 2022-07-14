#funções para editar cada parte do restaurante
#mais pra frente poder adicionar categorias 
    #para adicionar categoria pegar o tamanho do dic cardapio e adicionar 1 será onde a categoria
    #sera adicionada, criar um loop que fara um novo dicionario dessa categoria, depois adicionar
    #o dicionario da categoria nova ao dicinoario do cardapio

def editar_cardapio(cardapiodic, lista_de_categoria):
    for key, value in cardapiodic.items():
         print(key, '--')
         for subject, score in value.items():
            print(subject, ' : ', score)
    print("\nDeseja adicionar um item ao Cardápio ou editar algum item já existente?\nOpção 1: Adicionar item\nOpção 2: Editar um item")
    wish3 = input()
    while wish3 == '1':
        print("\nA qual categoria você deseja adicionar um item? Aqui estão as categorias existentes no seu Cardápio, digite a categoria que deseja.")
        print(lista_de_categoria)
        cat_escolha = input("\n")
        if cat_escolha in lista_de_categoria:
            x = len(cardapiodic[cat_escolha])
            y = x + 1
            novo_item_nome = input("\nDigite o nome do item:")
            novo_item_preco = input("Digite o preço do item:")
            cardapiodic[cat_escolha][y] = novo_item_nome + " " + novo_item_preco
            wishy = input("\nDeseja fazer mais alguma adição ao Cardápio(digite sim)? Caso tenha terminado digite 'nao'")
            if wishy == 'nao':
                wish3 = '10'
            if wishy == 'sim':
                wish3 = '1'
    while wish3 == '2':
        print("Em qual categoria está o tem que você deseja editar? Aqui estão as categorias existentes no seu Cardápio, digite a categoria que deseja.")
        print(lista_de_categoria)
        cat_escolha = input()
        if cat_escolha in lista_de_categoria:
            print("Aqui estão os itens dessa categoria, qual item você deseja editar? Digite o número.")
            for key, value in cardapiodic[cat_escolha].items():
                print(key, ' : ', value)
            item_escolha = int(input())
            nome_novo = input("Digite o novo nome do item:")
            novo_preco = input("Digite o novo preço do item:")
            cardapiodic[cat_escolha][item_escolha] = nome_novo + " " + novo_preco
            wishyy = input("Deseja fazer mais alguma edição ao Cardápio(digite sim)? Caso tenha terminado digite 'nao'")
            if wishyy == 'nao':
                wish3 = '57'
            if wishyy == 'sim':
                wish3 = '2'
            
def editar_clientes(clientesdic):
    for key, value in clientesdic.items():
        print(key, ' : ', value)
    print("\nDeseja adicionar um cliente ou editar um já existente?\nOpção 1: adicionar\nOpção 2: editar\n")
    wish4 = input()
    while wish4 == '1':
       x = len(clientesdic)
       y = x + 1
       cliente_novo = input("\nDigite o nome do cliente:")
       endereço_novo = input("Digite o endereço do cliente:")
       clientesdic[y] = cliente_novo + ", " + endereço_novo
       wishh = input("Deseja fazer mais alguma adição a Lista de Clientes(digite sim)? Caso tenha terminado digite 'nao'.\n")
       if wishh == 'nao':
            wish4 = '60'
       if wishh == 'sim':
           wish4 = '1'
    while wish4 == '2': #nao está editando está adicionando
        for key, value in clientesdic.items():
            print(key, ' : ', value)
        cliente_editado = int(input("Qual cliente você deseja editar? Digite o número."))
        nome_editado = input("Digite o novo nome:")
        endereço_editado = input("Digite o novo endereço:")
        clientesdic[cliente_editado] = nome_editado + ", " + endereço_editado   
        wiish = input("Deseja fazer mais alguma edição a Lista de Clientes(digite sim)? Caso tenha terminado digite 'nao'.")    
        if wiish == 'sim':
            wish4 = '2'
        if wiish == 'nao':
            wish4 = '30'
        
def editar_pedidos(pedidodic, cardapiodic, clientesdic):
    from criarpedido import criar_pedido
    for key, value in pedidodic.items():
        print(key, ' : ', value)
    print("Deseja adicionar um pedido ou editar um já existente?\nOpção 1: adicionar\nOpção 2: editar")
    wish5 = input()
    while wish5 == '1':
        y = len(pedidodic)
        x = y + 1
        for key, value in cardapiodic.items():
            print(key, '--')
            for subject, score in value.items():
                print(subject, ' : ', score)
        ncardapio = input("Digite o código do item do cardapio que será adicionado ao pedido:")
        for key, value in clientesdic.items():
              print(key, ' : ', value)
        ncliente =  input("Digite o nome do cliente: ")
        entregue = input("Digite se o pedido foi entregue(sim ou não): ")
        criar_pedido(x, ncardapio, ncliente, entregue, pedidodic)
        wosh = input("Deseja fazer mais alguma adição a Lista de Pedidos(digite sim)? Caso tenha terminado digite 'nao'.")
        if wosh == 'sim':
            wish5 = '1'
        if wosh == 'nao':
            wish5 = '100'
    while wish5 == '2':
        for key, value in pedidodic.items():
            print(key, ' : ', value)
        x = int(input("\nQual pedido você deseja editar? Digite o número.\n"))
        ncardapio = input("\nDigite o novo código do item do cardapio que será adicionado ao pedido:")
        for key, value in clientesdic.items():
              print(key, ' : ', value)
        ncliente =  input("Digite o novo nome do cliente: ")
        entregue = input("Digite se o pedido foi entregue(sim ou não): ")
        criar_pedido(x, ncardapio, ncliente, entregue, pedidodic)
        woosh = input("Deseja fazer mais alguma edição a Lista de Pedidos(digite sim)? Caso tenha terminado digite 'nao'.\n")
        if woosh == 'sim':
            wish5 = '2'
        if woosh == 'nao':
            wish5 = '190'