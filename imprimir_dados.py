#função imprimi todos os dados do restaurante: cardapio, clientes e pedidos

def imprimir_dados(nome_restaurante, cardapiodic, clientesdic, pedidodic):
    print("Restaurante", nome_restaurante)
    print('Cardapio')
    for key, value in cardapiodic.items():
        print(key, '--')
        for subject, score in value.items():
            print(subject, ' : ', score)
    print('\nLista de clientes')
    for key, value in clientesdic.items():
        print(key, ' : ', value)
    print('\nLista de pedidos')
    for key, value in pedidodic.items():
        print(key, ' : ', value)
        
def imprimir_dicionario_do_restaurante(nome_restaurantedic, nome_restaurante):
    print("Restaurante", nome_restaurante)
    for key, value in nome_restaurantedic.items():
        print(key, '--')
        for subject, score in value.items():
            print(subject, ' : ', score)