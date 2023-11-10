lista = {"nome":str(input("Digite seu nome: ")),
         "sobrenome":str(input("Digite seu sobrenome: ")), 
         "idade":int(input("Digite sua idade: ")),
         "email":str(input("Digite seu email: "))
        }

print(lista.items())
for chave, valor in lista.items():
    print(f"{n1}{chave} - {valor}")