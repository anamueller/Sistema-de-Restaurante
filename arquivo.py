#criando o arquivo com o nome do restaurante
def criar_arquivo(nome_restaurante, cardapiodic, clientesdic, pedidodic):
    arquivo = "{} {}".format(nome_restaurante, '.csv')
    abertura = '                   Dados do restaurante'
    intro = "{} {}\n".format(abertura,nome_restaurante)
    arq = open(arquivo, 'w')
    arq.write(intro)
    arq.write('\n     Cardápio\n')
    for key, value in cardapiodic.items():
        header = "\n{} ---- \n".format(key)
        arq.write(header)
        for subject, score in value.items():
            conteudo = "{}:{}\n".format(subject,score)
            arq.write(conteudo)    
    arq.write('\n     Lista de clientes\n')
    for key, value in clientesdic.items():
        linha = "{}:{}\n".format(key,value)
        arq.write(linha)
    arq.write('\n')
    arq.write('\n     Lista de pedidos\n')
    for key, value in pedidodic.items():
        linha2 = "\n{}:{}\n".format(key, value)
        arq.write(linha2)
    arq.close
    
def criar_arquivo_nomes(restaurantescriados, nome_restaurante):
    arquivo = 'restaurantescriados.csv'
    arq = open(arquivo, 'w')
    i = 0
    numerorestaurante = 1
    print(restaurantescriados)
    while i < len(restaurantescediçõesriados):
        linha = "Restaurante {}: {}".format(numerorestaurante, restaurantescriados[i])
        arq.write(linha)
        arq.write('\n')
        i = i + 1
        numerorestaurante = numerorestaurante + 1