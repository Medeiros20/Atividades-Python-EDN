import requests
from datetime import datetime

def consulta_cotacao():
    moeda = input("Digite o codigo da moeda (ex: USD, EUR, GBR): ").upper().strip()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            chave = f"{moeda}BRL"
            if chave not in dados:
                print("Codigo de moeda inavlido!")

                return
            
            cotacao = dados[chave]
            valor_atual = float(cotacao.get('bid','N/A'))
            valor_max = float(cotacao.get('high','N/A'))
            valor_min = float(cotacao.get('low','N/A'))
            data_hora = datetime.fromtimestamp(int(cotacao['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')
            
            print(f"\nCotação de {moeda} para BRL:")
            print(f"Valor atual: R$ {valor_atual:.2f}")
            print(f"Valor máximo: R$ {valor_max:.2f}")
            print(f"Valor mínimo: R$ {valor_min:.2f}")
            print(f"Última atualização: {data_hora:}")

        else:
            print("Erro ao consultar a cotação! ")
    except ValueError:
        print("Erro ao processar a solicitação")

consulta_cotacao()
