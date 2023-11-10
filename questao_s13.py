#Dado o conjunto Modulos com a seguinte estrutura {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
#faça um programa que peça ao usuário o nome de um novo módulo e adicione esse módulo dentro desse conjunto

modulos = {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
novo_modulo = str(input("Digite nome de novo módulo: "))
modulos.update({novo_modulo})
print(modulos)