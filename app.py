from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_news():
    url = 'https://futebolms.com.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = []
    for item in soup.find_all('div', class_='news-item'):  # Exemplo, ajuste conforme o HTML real
        title = item.find('h2').text
        link = item.find('a')['href']
        date = item.find('time')['datetime']  # Exemplo, ajuste conforme o HTML real
        news_list.append({'title': title, 'link': link, 'date': date})

    return news_list

@app.route('/api/news', methods=['GET'])
def get_news():
    news = fetch_news()
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
