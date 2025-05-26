#REGISTRO DE NOTAS
notas = []

while True:
    print("Bem vindo ao Sistema de notas")
    resposta = input("\nCaso deseje sair digite 'Fim'\nQual a nota do aluno: ")
    
    #VERIFICA SE A RESPOSTA É FIM
    if resposta.lower() == "fim":
        print("Sistema encerrado!")
        break

    elif resposta.lower() != "fim":
        #TRANSFORMA O QUE O USUARIO DIGITOU EM FLOAT
        nota = float(resposta)
        if nota >= 0 and nota <= 10:
            #ADICIONA A NOTA DIGITA NA LISTA 
            notas.append(nota)
        else:
            print("Nota Invalida! digite um valor de 0 a 10")
    else:
        print("Entrada inválida! Digite um número ou 'fim'.")

if notas:
    #CALCULA A MEDIA DA DA LSITA, SOMA AS NOTAS DIGITADAS E DEPOS DIVIDE PELA QUANTIDADE DE NOTAS
    media = sum(notas) / len(notas)
    print(f"A media das notas dos alunos é {media:.2f}")
else:
    print("Nenhuma nota registrada!")