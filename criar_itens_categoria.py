#criando uma nova categoria do cardapio, ex:bebidas
#nomecat = nome da categoria 
#ni = nome do item a ser adicionado na categoria, ex: coca cola
#p = preço do item

def adicionar_itens(indicedic, indice, ni, p, m):
    indicedic[m]= ni + " " + p
    print("\nO item adicionado na categoria", indice, "foi")
    print(indicedic[m])