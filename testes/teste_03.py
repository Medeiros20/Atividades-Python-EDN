#open("caminho", "W")

# R - leitura
# W - escrita
# A - incremento
# W - escrita
# X - cria
# R+ - ler e escreve

arquivo = open("testes/linguagem.txt", "r")

print(arquivo.readable())

print(arquivo.read())

arquivo.close()