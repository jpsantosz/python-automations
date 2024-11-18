# Fazer uma request em uma página web usando python
import requests 
# Utilizar a bublioteca datetime para manipular dados do tempo atual
import datetime 
# Biblioteca de tradução para obter a versão traduzida dos dados extraídos da api
from translate import Translator

translator = Translator(to_lang="pt")

chave_api = '*******************************'

url_api = 'https://api.openweathermap.org/data/2.5/weather'

# Configura o nome da cidade a qual desejamos extrair os dados
cidade = "Rio de Janeiro"

# Define o URL onde serão obtidos os dados
request_url = f'{url_api}?appid={chave_api}&q={cidade}'

response = requests.get(request_url)

# Caso a resposta da api esteja "ok" obtemos um JSON dos dados do clima em formato de dict

if response.status_code == 200:
    data = response.json()
    clima = data['weather'][0]['description']
    temperatura = round(data['main']['temp'] - 273.15, 2)
    por_do_sol = datetime.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

    clima_traduzido = translator.translate(clima)

    print("Cidade: ", cidade)
    print('Resumo do tempo: ', clima_traduzido)
    print(f'Temperatura: {temperatura} Celsius')
    print('Por do sol: ', por_do_sol)
else:
    print("ops, algo parece estar errado!")