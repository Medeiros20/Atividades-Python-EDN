#CONVERSOR
valor_reais = 100.0
taxa_dolar = 5.20
taxa_euro = 6.15

#Calcula o valor convertido em dolar
valor_dolar = valor_reais * taxa_dolar
#Calcula o valor convertido em euro
valor_euro = valor_reais * taxa_euro

#Mostra ao usuario a taxa do dolar
print(f"O valor da taxa de dolar está: {taxa_dolar:.2f}")

#Mostra ao usuario a taxa do euro
print(f"O valor da taxa de euro está: {taxa_euro:.2f}")

#Calcula a conversão de reais para dolar
print(f"O valor de {valor_reais:2f} reais convertidos em dolar é de: {valor_dolar:.2f}")

##Calcula a conversão de reais para euro
print(f"O valor {valor_reais:2f} reais convertido em euro é de: {valor_euro:.2f}")