import csv

def escrever_csv(nome_arquivo, dados):
    colunas = ["Nome", "Idade", "Cidade",]

    with open(nome_arquivo, mode = "w", newline = '', encoding = "utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)

        escritor.writeheader()
        escritor.writerows(dados)

        print(f"Arquivo {nome_arquivo} criado com sucesso!")

dados_pessoas = [
    {'Nome': 'Luciana', 'Idade': 30, "Cidade": "São Bernardo do Campo"}, # Vírgula adicionada após o dicionário
    {'Nome': 'João', 'Idade': 19, "Cidade": "Castanhal"},              # Vírgula adicionada após o dicionário
    {'Nome': 'Gabriella', 'Idade': 20, "Cidade": "Belém"}              # Sem vírgula após o último dicionário
]

escrever_csv("aula_07/pessoas.csv", dados_pessoas)