#preço do produto

nome_produto = input("Qual o nome do produto? ")
preco_unitario = float(input("Qual o preço unitario do produto? "))
qtd_produto = int(input("Qual a quantidade de produtos? "))

valor_total = preco_unitario*qtd_produto

print("O valor total de ", qtd_produto, "unidade (s) de ", nome_produto, " à ", preco_unitario, " reais cada, é de ", valor_total, "reais")