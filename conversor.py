# CONVERSOR
valor_reais = 100.0
taxa_dolar = 5.20
taxa_euro = 6.15

# Calcula o valor convertido em dólar
valor_dolar = valor_reais / taxa_dolar
# Calcula o valor convertido em euro
valor_euro = valor_reais / taxa_euro

# Mostra ao usuário a taxa do dólar
print(f"O valor da taxa de dólar está: {taxa_dolar:.2f}")

# Mostra ao usuário a taxa do euro
print(f"O valor da taxa de euro está: {taxa_euro:.2f}")

# Mostra a conversão de reais para dólar
print(f"O valor de {valor_reais:.2f} reais convertidos em dólar é: {valor_dolar:.2f}")

# Mostra a conversão de reais para euro
print(f"O valor de {valor_reais:.2f} reais convertidos em euro é: {valor_euro:.2f}")
