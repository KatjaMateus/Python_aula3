#Dado o dicionário Filme com a seguinte estrutura {"Titulo" : "It a Coisa", "Genero": "Terror", "Duracao": 120, Cartaz: False}
#faça um programa que imprima os valores de todas as chaves, uma por uma, e no final 
#remova a chave "Genero" e caso ela não exista, mostre #uma mensagem de erro informando que a chave não existe

filme = {"Título":"It a Coisa", 
         "Genero":"Terror", 
         "Duração":120, 
         "Cartaz": False
}
print(filme.values())

filme.pop("Genero", "Chave inexistente")
print(filme)