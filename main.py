import requests
from config import URL_BASE, API_KEY

nome_cidade = input("Insira o nome da cidade para pesquisar o clima: ")

url_completa = f"{URL_BASE}q={nome_cidade}&appid={API_KEY}"
# print(url_completa)

dados_recebidos = requests.get(url_completa).json()
# print(dados_recebidos)

if dados_recebidos['cod'] != '404':
  # dados da chave 'main' = principal
    principal = dados_recebidos
    # print(principal)
    temperatura_corrente = principal['temp']
    pressao_corrente = principal['pressure']
    humidade_corrente = principal['humidity']

  # dados da chave 'weather'= Clima
    clima = dados_recebidos['weather']
    # print(clima)
    descricao_clima = clima[0]['description']
    # print(descricao_clima)

    #Mostrar os seguintes valores
    print(f"\nTemperatura = {round(temperatura_corrente - 273.15, 1)}Cº.")
    print(f"\nPressãoAtmosférica = {pressao_corrente}hPa.")
    print(f"\nHumidade Corrente = {humidade_corrente}%.")
    print(f"\nDescrição do Clima = {descricao_clima}.")
else:
    print("Cidade não encontrada")
