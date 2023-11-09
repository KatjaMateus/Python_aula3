# Dado o dicionário Carro com a seguinte estrutura: {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"},
# faça um programa que cheque se existe uma chave chamada "Cor" no dicionário, se existir, mude a cor dela para "preto" se ela não existir delete a chave ano.

carro = {"Marca": "Ford", 
         "Modelo": "Ka", 
         "Ano": 2020, 
         "Cor": "Cinza"
         }

if "Cor" in carro:
         carro["Cor"] = "preto"
else:
         del carro["Ano"]
    print(carro)
