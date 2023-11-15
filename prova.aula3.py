alunado = {1234  : "Diana Soares", 3456 : "João Gomes", 2345 : "Marcos Saraiva"}

while True:    
    matricula=int(input("Digite número de matrícula: "))
    if matricula == 0000:
        break        
    nome=str(input("Digite o nome do aluno: "))
    alunado.update([[matricula, nome]])
print(alunado)

deletar = int(input("Digite o número de matrícula a ser deletado: "))
del alunado[deletar]
print(alunado)
