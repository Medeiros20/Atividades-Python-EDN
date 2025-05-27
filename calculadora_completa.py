print("--CALCULADORA DAS QUATRO OPERAÇÕES--")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

try:
    op = int(input("Escolha qual operação você deseja realizar: "))

    if op in [1, 2, 3, 4]:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))

        if op == 1:
            resultado = numero1 + numero2
            operador = '+'
        elif op == 2:
            resultado = numero1 - numero2
            operador = '-'
        elif op == 3:
            resultado = numero1 * numero2
            operador = 'x'
        elif op == 4:
            if numero2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida!")
            resultado = numero1 / numero2
            operador = '/'

        print(f"{numero1:.2f} {operador} {numero2:.2f} = {resultado:.2f}")
    else:
        print("Opção inválida. Por favor, escolha entre 1 e 4.")

except ValueError:
    print("Erro: Digite apenas números válidos.")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
