import json


dados = {
    "Noma": "Ana",
    "Idade": 28,
    "cidade": "São paulo"
}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)
