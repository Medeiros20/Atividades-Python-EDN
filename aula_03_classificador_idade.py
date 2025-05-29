#CLASSIFICADOR DE IDADE!
#RECEBE UM VALOR PARA IDADE
idade = int(input("Digite a sua idade: "))

#CLASSIFICA A IDADE
if idade >= 0 and idade <= 12:
    print("Você é uma criança")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto")
else:
    print("Você é idoso")
