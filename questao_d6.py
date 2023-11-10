#Dado o dicionário Moto com a seguinte estrutura {"Marca": "Honda", "Modelo": "Bros", "Cilindradas": 160}
#faça um programa que imprima a cor da moto, caso não tenha cor, deixe a cor padrão como preta
#depois "zere" todos os valores desse objeto


moto = {"Marca": "Honda", "Modelo": "Bros", "Cilindradas": 160}


if "Cor" in moto:
    print(moto["Cor"])
else:
     moto["Cor"]= "preto"
     print(moto)

print(dict.fromkeys(moto))