import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio
import time
import datetime

 # Obtenha a hora atual
now = datetime.datetime.now()

# URL da página de vagas
url = 'https://www.itajaionline.com.br/vagas'

# Conectando ao Telegram
bot = Bot(token='5639063615:AAFN7ghKtIeWS5LkQor3UrnCYoXxsBF51xo')

sent_jobs = []

while True:
    # Fazendo a solicitação HTTP
    response = requests.get(url)

     # Analisando o HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando as novas publicações
    new_posts = soup.find_all(class_='collection-item')

    # Enviando os links das novas publicações para o canal
    for post in new_posts:
     link = post.find('a')['href']

     # encontrando horario da publicacao
     time_element = post.find(class_='white-text')
     time_text = time_element.text

   # encontrando o link dentro do elemento job-item
    if link not in sent_jobs:
        asyncio.run(bot.send_message(chat_id='-869312583', text=time_text + "\n" + link))
        sent_jobs.append(link)
        print("Encontrou uma vaga e esta enviando para o grupo do Telegram.")
    else:

        print("Nao encontrou nenhuma vaga nova.")

        # Defina a mensagem de acordo com a hora atual
    if now.hour < 12:
      message = "Bom dia! Aqui esta a chave pix para quem quiser contribuir com o projeto: CPF: 106.906.949-38"
    elif now.hour < 18:
      message = "Boa tarde! Aqui esta a chave pix para quem quiser contribuir com o projeto: CPF: 106.906.949-38"
    else:
      message = "Boa noite! Aqui esta a chave pix para quem quiser contribuir com o projeto: CPF: 106.906.949-38"

     #Espera alguns minutos antes de fazer outra requisição
    time.sleep(60 * 5) # 5 minutos