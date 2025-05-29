#VERIFICA NUMEROS SE INTEIROS SÃO IMPA OU PAR

#AS VARIAVEIS INICIAM COM 0 PARA IR SOMANDO AO LONGO DO ENTRADA
pares = 0
impares = 0

print("Bem-vindo ao classificador de números pares e ímpares!")

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        print("Programa encerrado.")
        break

    #utilizei o try para verificar se pode converter para um numero inteiro
    try:
        numero = int(entrada) 
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: isso não é um número inteiro válido!")

print("\nResumo:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
