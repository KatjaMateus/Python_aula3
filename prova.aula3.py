alunos = {1234  : "Diana Soares", 3456 : "João Gomes", 2345 : "Marcos Saraiva"}

while True:
    escolha = int(input("""
        Escolha uma opção:
        1 = visualizar alunos
        2 = adicionar alunos
        3 = remover alunos
        4 = sair
                    
      """))
    if escolha == 1:    
        print(alunos)
    elif escolha == 2:
        while True:    
            matricula=int(input("Digite número de matrícula: "))
            if matricula == 0:
                break        
            nome=str(input("Digite o nome do aluno: "))
            alunos.update([[matricula, nome]])
        print(alunos)      
    elif escolha == 3:
        print(alunos)
        deletar = int(input("Digite o número de matrícula do aluno a ser removido: "))
        del alunos[deletar]
        print(f"A matrícula {deletar} foi removido com sucesso")       
    elif escolha == 4:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")
