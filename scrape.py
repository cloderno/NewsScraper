from bs4 import BeautifulSoup
import requests
import dateparser
from datetime import datetime

# Инициализация скрейпера
def init_scraper(url):
    request = requests.get(url)
    html = request.content

    return BeautifulSoup(html, 'html.parser')


# Функция позволяет сделать массив данных
def scrape_news(array):
    for item in array:  
        soup = init_scraper(item['RESOURCE_URL'])

        news_objects = []
        current_id = 0

        for obj in soup.find_all(class_=item['top_tag']):
            current_id += 1

            news_objects.append({
                "id": current_id,
                "res_id": item['top_tag'],
                "link": str(obj.get('href')),
                "title": str(obj.find(class_=item['title_cut']).get_text()),
                "content": str(obj.find(class_=item['bottom_tag']).get_text()),
                "nd_date": dateparser.parse(obj.find(class_=item['date_cut']).get('datetime')).timestamp(), 
                "s_date": dateparser.parse(str(datetime.now())).timestamp(),
                "not_date": 122
            })


        return news_objects
