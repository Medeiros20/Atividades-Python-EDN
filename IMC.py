#CALCULO DO IMC
peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite o a sua altura em metros: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}")
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}")
    print("Peso normal")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f}")
    print("Sobrepeso")
else:
    print(f"Seu IMC é {imc:.2f}")
    print("Obseso")
