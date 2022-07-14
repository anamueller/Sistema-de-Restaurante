username = input("Username:")#anamueller
password = input("Password:")#elisinha72
      
import csv
from criação import criar_cliente, criar_pedido, criando_dics_cardapio, adicionar_itens, dicionario_do_restaurante
from arquivo import criar_arquivo, criar_arquivo_nomes
from imprimir_dados import imprimir_dados, imprimir_dicionario_do_restaurante
from edições import editar_cardapio, editar_clientes, editar_pedidos

if username != 'anamueller' or password != 'elisinha72':
  print("Usuário ou senha invalida. Tente novamente")
if username == 'anamueller' and password == 'elisinha72':
  inicio = input("\nDeseja criar um restaurante novo ou editar um restaurante já existente?(Para criar digite 'criar' para editar digite 'editar': ")
  while inicio == 'criar': #loop para quando terminar o restaurante voltar a tela de editar
    print("\nPara começar a criar o seu restaurante vamos dar um nome a ele.")
    nome_restaurante = input("Digite o nome do seu restaurante: ")
    #criar_arquivo_nomes(restaurantescriados, nome_restaurante)
    #consertar a criação do arquivo, ou conseguindo fazer uma lista q se cria uma vez só, ou copiando para o arquivo sem deletar oq ja estava escrito no arquivo
    desejo = ''
    cardapiodic = {}
    print("\nVamos criar o cardápio do seu restaurante.")
    while desejo != 'nao': #primeiro passo, criar o cardápio do restaurante
      categoria = input("Digite o nome das categorias que você deseja criar, separadas por um espaço:")
      lista_de_categoria = categoria.split()
      print("\nAs categorias digitadas foram as seguintes:\n", lista_de_categoria)
      criando_dics_cardapio(lista_de_categoria, cardapiodic) #função que cria um dicionario com cada categoria e adiciona os itens
      desejo = 'nao'
    if desejo == 'nao': #cardápio terminado, segundo passo criar os clientes
      desejo2 = ''
      x = 1
      clientesdic ={}
      print("\nAgora que seu cardápio está criado vamos adicionar os seus clientes.")
      while desejo2 != 'nao': #criando os clientes
        nomecliente = input("\nDigite o nome do cliente: ") 
        endereço = str(input("Digite o endereço do cliente: "))
        desejo2 = input("\nDeseja adicionar mais clientes? Se sim digite sim, caso já tenha terminado digite não.\n")
        criar_cliente(x, nomecliente, endereço, clientesdic)
        x = x + 1
    if desejo2 == 'nao': #clientes terminados, último passo criar os pedidos
      desejo3 = ''
      pedidodic = {}
      x = 1
      print("\nAqui está sua lista de clientes. Caso encontre algum erro e queira editar espere até o final que te daremos essa opção.")
      for key, value in clientesdic.items():
        print(key, ' : ', value)
      print("\nVamos criar os pedidos do seu restaurante agora.")
      while desejo3 != 'nao': #criando os pedidos
        for key, value in cardapiodic.items():
          print(key, '--')
          for subject, score in value.items():
            print(subject, ' : ', score)
        ncardapio = input("\nDigite o código do item do cardapio que será adicionado ao pedido\n")
        for key, value in clientesdic.items():
          print(key, ' : ', value)
        ncliente =  input("\nDigite o nome do cliente: ")
        entregue = input("Digite se o pedido foi entregue(sim ou não): ")
        criar_pedido(x, ncardapio, ncliente, entregue, pedidodic)
        x = x + 1
        desejo3 = input("\nDeseja adicionar mais pedidos? Se sim digite sim, caso já tenha terminado digite não.\n")
    if desejo3 == 'nao':
      print("\nPronto seu restaurante está montado! Todas as informações foram salvas em um arquivo com o nome do seu restaurante.\n")
      inicio = 'terminado'
  if inicio == 'terminado':
    print("Agora você pode fazer alguma alteração caso seja necessário. Aqui estão todas as informações do seu restaurante, deseja editar alguma? Se sim, digite editar, se não precisa fazer nenhuma alteração digite 'finalizado'.\n")
    imprimir_dados(nome_restaurante, cardapiodic, clientesdic, pedidodic)
    nome_restaurantedic = {}
    dicionario_do_restaurante(nome_restaurantedic, cardapiodic, clientesdic, pedidodic)
    inicio2 = input('\n')
  if inicio2 == 'editar':
    print("\nO que você deseja editar do Restaurante", nome_restaurante, "?\n")
    while inicio != 'finalizado':
      imprimir_dados(nome_restaurante, cardapiodic, clientesdic, pedidodic)
      print("\nOpção 1: Cardápio\nOpção 2: Clientes\nOpção 3: Pedidos\n")
      edicao_desejada = int(input()) #escolherá entre o Cardápio, clientes, e pedidos
      while edicao_desejada == 1:
        print("\nVocê escolheu editar o Cardápio.")
        editar_cardapio(cardapiodic, lista_de_categoria)
        edit = int(input("\nDeseja fazer mais alguma alteração ao Cardápio?\nOpção 1: sim\nOpção 2: não\n"))
        if edit == 2:
          edicao_desejada = 0
        if edit == 1:
          edicao_desejada = 1
      while edicao_desejada == 2:
        print("\nVocê escolheu editar a Lista de Clientes.")
        editar_clientes(clientesdic)
        edit2 = int(input("\nDeseja fazer mais alguma edição a Lista de Clientes?\nOpção 1: não\nOpção 2: sim\n"))
        if edit2 == 1:
          edicao_desejada = 0
        if edit2 == 2:
          edicao_desejada = 2
      while edicao_desejada == 3:
        print("\nVocê escolheu editar a Lista de Pedidos.")
        editar_pedidos(pedidodic, cardapiodic, clientesdic)   
        edicao = input("\nDeseja fazer mais alguma edição a lista de Pedidos?\nOpção 1: sim\nOpção 2: não\n")
        if edicao == '1':
          edicao_desejada = 3
        if edicao == '2':
          edicao_desejada = 7
      inicio2 = input("Deseja alterar algo novamente? Se sim digite sim, se não digite finalizado.\n")     
  if inicio2 == 'finalizado':
    print("Parabéns seu restaurante está totalmente pronto. Compartilhe o arquivo com seus amigos :)")
    criar_arquivo(nome_restaurante, cardapiodic, clientesdic, pedidodic)    
      
    
  
  #quando conseguir fazer funcionar a lista de restaurates criados:
  #if inicio == 'editar':
 # print('\nQual restaurante você deseja editar? Digite o nome do restaurante.')
  #  with open('restaurantescriados.csv', 'r') as arquivo:
   #   reader = csv.reader(arquivo)
    #  for row in reader:
     #   print(row)
    #nome_restaurante = input()
    #decisao = ''
    #while decisao != 'finalizado':
     # print("O que você deseja editar do Restaurante", nome_restaurante)
      #imprimir_dicionario_do_restaurante(nome_restaurantedic, nome_restaurante)
      #escolha = input()