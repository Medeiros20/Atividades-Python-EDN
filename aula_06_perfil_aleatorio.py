import requests
import time

def gera_perfil():
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario["location"]['country']

        print("Gerando usuario...")
        time.sleep(2)
        print("Perfil de usuario aleatorio: ")
        print(f"Nome: {nome}")
        print(f"Emai: {email}")
        print(f"País: {pais}")

    else:
        print("Erro ao acessar a API")

gera_perfil()