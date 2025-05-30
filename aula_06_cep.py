import requests

def cep():
    cep = input("Digite o seu CEP (apenas numeros): ").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP invalido verifique-se de digitar 8 numeros!")
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado")
        else:
            logradouro = dados.get("logradouro", "N/A")
            bairro = dados.get("bairro","N/A")
            cidade = dados.get("cidade","N/A")
            estado = dados.get("uf","N/A")

            print("Dados do cep:")
            print(f"logradouro do cep: {logradouro}")
            print(f"bairro do cep: {bairro}")
            print(f"Cidade do cep: {cidade}")
            print(f"estado do cep: {estado}")
    else:
        print("Erro ao acessar a API!")

cep()
