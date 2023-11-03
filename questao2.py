#Dado o Dicionário Animal com a seguinte estrutura: {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": 1, "Adestrado": "Sim"},
#faça um programa que cheque se o cachorro tem mais de 2 anos de idade, se tiver, crie uma nova chave chamada "Vacinado" e atribua o valor de
#verdadeiro, caso contrário, mude o valor da chave "Adestrado" para "Não"

Animal = {"Especie": "Cachorro",
           "Raça": "Pinscher",
            "Idade": int(input("Digite a idade do cachorro: ")), 
            "Adestrado": "Sim"
            }

if Animal ["Idade"] > 2:
    Animal ["Vacinado"] = True  #procurar dentro de dicionario coloque []
else:
    Animal ["Adestrado"] = False

print(Animal)