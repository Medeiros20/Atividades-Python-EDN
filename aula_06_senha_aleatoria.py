import random
import string

#Função para gerar a senha
def gerador_de_senha(tamanho):
    #define os caracteries q podem ser usados, uncluido A-Z,a-z,0-9, e caracteries especiais
    caracteres = string.ascii_letters + string.digits + "" + string.punctuation

    #escolhe os caracteries aleatorios e junta todos esses caracteres
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Informe a quantidade de caracteres da senha: "))
    if tamanho <= 0:
        print("Por favor informe um numero maior que zero")
    else:
        senha = gerador_de_senha(tamanho)
        print(f"Senha gerada {senha}")

except:
    print("informe uma valor inteiro valido!")
