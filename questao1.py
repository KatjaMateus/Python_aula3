#Dado O Dicionário pessoa com a seguinte estrutura: {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True},
#faça um programa que imprima na tela quantas chaves existem nesse dicionário, e quais os nomes de cada uma dela

pessoa = {"nome" : "Abel", "idade" : 28, "altura" : 1.79, "habilitacao" : True}


print(f"O dicionario possui {len(pessoa)} chaves")

lista_chaves = list(pessoa)

for chave in pessoa:
    print(chave)
