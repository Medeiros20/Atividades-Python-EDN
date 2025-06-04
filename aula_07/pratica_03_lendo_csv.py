
import csv 

dados = [["Nome", "Idade", "Cidade"], ["João", 19, "Castanhal"], ["Gabrielle", 20, "são paulo"], ["Alan", 35, "são paulo"]]

with open ("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)


with open ("dados.csv", mode="r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

    cabecalho = linhas[0].strip()

    nomes = []

    for linha in linhas [1:]:
        nomes.append(linha.strip())
    
print(cabecalho)
        
for nome in nomes:
    print(nome)