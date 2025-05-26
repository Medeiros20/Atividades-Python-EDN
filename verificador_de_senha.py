#VERIFICAOR DE SENHA

while True:
    print("Bem vindo ao verificador de Senha")
    #criei essa validação para deixar o SAIR livre mas acabei deixando o sair como uma opção para encerrar o programa
    validacao = input("Deseja continuar? (Sim/Não) ")
    
    if validacao.lower() != "sim":
        print("Programa encerrado...")
        break

    elif validacao.lower() == "sim":
        senha = input("\nCaso dejese sair digite 'sair'\nDigite a sua senha: ")
        
        if senha.lower() == "sair":
            print("Programa encerrado...\n")
            break
        #VERIFICA O TAMANHO DA SENHA
        elif len(senha) < 8:
            print("Senha Fraca! A senha deve conter mais de 8 caracteries\n")
            continue
        #VERIFICA SE TEM NUMERO, ESSA PARTE TIVE QUE PESQUISAR PQ NÃO SABIA KKKKKKKKKKK
        elif not any(char.isdigit() for char in senha):
            print("Senha Fraca! A senha deve conter pelo menos 1 numero\n")
            continue
        else:
            print("Senha Forte!\n")
            break