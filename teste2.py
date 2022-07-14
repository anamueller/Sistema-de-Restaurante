dict1 = {
	'ma': 19, 'na':23
}

arq = open('meals.csv', 'w')

for chave in dict1:
	nome = chave
	preco = dict1[chave]
	linha = "{},{}\n".format(nome,preco)
	#print(linha)
	arq.write(linha)

arq.close()
