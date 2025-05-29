# função para calcular a idade em dias
def calculo_idade_em_dias(ano_nascimento, fez_aniversario):
    ano_atual = 2025
    idade_anos = ano_atual - ano_nascimento
    if not fez_aniversario:
        idade_anos -= 1
    idade_dias = idade_anos * 365
    return idade_dias

# função principal
def main():
    try:
        ano = int(input("Digite o seu ano de nascimento: "))
        if ano > 2025:
            print("Você veio do FUTURO? Digite um ano válido!")
            return

        resposta = input("Você já fez aniversário este ano? (sim/não): ").strip().lower()

        if resposta == "sim":
            fez_aniversario = True
        elif resposta != "sim":
            fez_aniversario = False
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")
            return

        idade_dias = calculo_idade_em_dias(ano, fez_aniversario)
        print(f"Você tem aproximadamente {idade_dias} dias de vida.")

    except ValueError:
        print("Você veio do FUTURO! Digite um ano válido.")

main()
