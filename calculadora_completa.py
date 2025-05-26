#CALCULADORA DAS 4 OPERAÇÕES
print("--CALCULADORA DAS QUATROS OPERAÇÕES--")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha qual operação você deseja realizar: "))

if op == 1:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um número: "))
    soma = numero1 + numero2
    print(f"{numero1:.2f} + {numero2:.2f} = {soma:.2f}")

elif op == 2:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um número: "))
    sub = numero1 - numero2
    print(f"{numero1:.2f} - {numero2:.2f} = {sub:.2f}")

elif op == 3:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um número: "))
    mult = numero1 * numero2
    print(f"{numero1:.2f} x {numero2:.2f} = {mult:.2f}")

elif op == 4:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um número: "))
    if numero2 != 0:
        div = numero1/numero2
        print(f"{numero1:.2f} / {numero2:.2f} = {div:.2f}")
    else:
        print("ERRO, divisão por zero não é permitida!")

else:
    print("Opção Invalida")

