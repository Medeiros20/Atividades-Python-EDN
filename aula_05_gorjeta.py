#Calculo da gorjeta

#função para calcular a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_da_gorjeta):
    gorjeta = valor_conta * (porcentagem_da_gorjeta / 100)
    return gorjeta

#função principal
def main():
    try:
        valor_conta = float(input("Digite o valor da conta: "))
        porcentagem = input("Digite a porcentagem de gorjeta (ex. 10 ou 10%): ")
        #remove a porcentagem (%) caso o usuario digite
        porcentagem = porcentagem.replace("%", "")

        #converte a porcentagem pra float apos tirar o %
        porcentagem = float(porcentagem)

        valor_da_gorjeta = calcular_gorjeta(valor_conta, porcentagem)

        print(f"O valor da compra foi: {valor_conta:.2f}")
        print(f"O valor da gorgeta para uma porcentagem de {porcentagem} % é: {valor_da_gorjeta:.2f}")
        print(f"O valor a pagar é: {valor_conta + valor_da_gorjeta:.2f}")
    except:
        print("Erro! insira apenas numeros validos")

main()