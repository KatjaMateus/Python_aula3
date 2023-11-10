#Dado o conjunto Linguagens com a seguinte estrutura {"Python", "Javascript", "Java", "PHP", "C++", "C#"}
#faça um programa que cheque a linguagem "TypeScript" existe nesse conjunto, e mostre na tela de acordo
# depois faça uma cópia desse conjunto, e mostre na tela os dois conjuntos, o original e a copia

linguagens = {"Python", "Javascript", "Java", "PHP", "C++", "C#"}

print("TypeScritp" in linguagens)

linguagens2=linguagens.copy()
print(linguagens)
print(linguagens2)
