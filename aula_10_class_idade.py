def classificador_de_idade(idade):
    # Tarefa 1 - Classificador de Idade
    print("Tarefa 1 - Classificador de Idade")

    idade = int(input("Digite a sua idade: "))

    # Análise
    if idade < 13:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

print(classificador_de_idade())
