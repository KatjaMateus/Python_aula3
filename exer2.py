
lista_notas = []
maior = 0
menor = 10
soma = 0
for i in range(4):
    nota = float(input("Digite a nota do aluno: "))
    lista_notas.append(nota)   
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma += nota
media = soma / 4

if media >= 6.0:
    situacao = "aprovado"
else:
    situacao = "reprovado"

aluno = {"nome":str(input("Digite o nome do aluno: ")), 
         "notas":lista_notas, 
         "maior nota":maior, 
         "menor nota":menor,
         "media":media,
         "situação":situacao
         }
print(aluno)