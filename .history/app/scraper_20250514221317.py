import requests

# from bs4 import BeautifulSoup
# import pandas as pd

url = "http://vitibrasil.cnpuv.embrapa.br/"  # Atribuindo url à uma variavel
response = requests.get(url)  # Requisição GET na url

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    html_content = response.text  # Armazenando o conteúdo HTML
    print("Página obtida com sucesso!")
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
