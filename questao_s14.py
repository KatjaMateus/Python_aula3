#Dado o conjunto Objetos com a seguinte estrutura {"Relógio", "Garrafa", "Mouse", "Monitor"}
#faça um programa que remova o objeto "Garrafa" do conjunto depois mostre como o conjunto ficou
#na tela, depois limpe o conjunto, e mostre o conjunto vazio na tela

objetos = {"Relógio", "Garrafa", "Mouse", "Monitor"}
objetos.remove("Garrafa")
print(objetos)
objetos.clear()
print(objetos)