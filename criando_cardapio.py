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
        
        
