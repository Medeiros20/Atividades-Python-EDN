#CONVERSOR DE TEMPERATURA
temp = float(input("Digite o valor da temperatura: "))

#lower tranforma todos as carateres em minusculas para fazer a comparação do if
origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").lower()
destino = input("Digite a unidade para converter (Celsius, Fahrenheit, Kelvin): ").lower()

# Converte para Celsius
if origem == 'celsius':
    c = temp
elif origem == 'fahrenheit':
    c = (temp - 32) * 5 / 9
elif origem == 'kelvin':
    c = temp - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Converte de Celsius para destino
if destino == 'celsius':
    resultado = c
elif destino == 'fahrenheit':
    resultado = (c * 9 / 5) + 32
elif destino == 'kelvin':
    resultado = c + 273.15
else:
    print("Unidade destino inválida.")
    exit()

print(f"{temp} {origem.capitalize()} equivale a {resultado:.2f} {destino.capitalize()}.")
