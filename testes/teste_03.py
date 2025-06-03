#open("caminho", "W")

# R - leitura
# W - escrita
# A - incremento
# W - escrita
# X - cria
# R+ - ler e escreve

arquivo = open("testes/linguagem.txt", "r")

#verifica se o arquivo pode ser lido
print(arquivo.readable())
#lê o arquivo e o print mostra o arquivo 
print(arquivo.read(),"\n")
#lê linha por linha
print(arquivo.readline())
#fecha o arquivo
arquivo.close()