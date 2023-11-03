# Faça um programa que pede para o usuário inserir o nome de um aluno e a nota desse mesmo aluno e adicione ele em uma lista até o usuário escrever no lugar do nome a palvra "fim"
# então mostre na tela o nome do aluno que obteve a melhor nota

lista_alunos = []

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    lista_alunos.append([nome, nota])

    if nome == "fim":
        break

maior = 0
maior_nome = ""
for aluno in lista_alunos:
    if aluno[1] > maior:
        maior = aluno[1]
        maior_nome = aluno[0]
print(f"A maior nota foi {maior} do aluno {maior_nome}")