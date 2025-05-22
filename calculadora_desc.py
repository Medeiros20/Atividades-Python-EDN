# Calculadora de Desconto

produto = "Camisa"
preco_original = 50.0
porcentagem_desconto = 20 / 100

# Calculando o valor com desconto
preco_final = preco_original * (1 - porcentagem_desconto)

#Saida com as informações do produto, valor valor original, desconto e valor final
print(f"A {produto}, com o preço originalmente de R${preco_original:.2f}, ficou por R${preco_final:.2f} após aplicar o desconto de {porcentagem_desconto*100:.0f}%.")
