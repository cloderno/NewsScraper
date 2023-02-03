from bs4 import BeautifulSoup
import requests
import dateparser
from datetime import datetime

# Инициализация скрейпера
def init_scraper(url):
    request = requests.get(url)
    html = request.content

    return BeautifulSoup(html, 'html.parser')

def empty_data(empty_item):
    if empty_item:
        empty_item = str(empty_item[0].text)
    else:
        empty_item = 'NO DATA'
    
    return empty_item

def empty_link(empty_link):
    pass

# Функция позволяет сделать массив данных
def scrape_news(array):

    # for i in array: 
    #     print(i['RESOURCE_URL'])
    news_objects = []
        
    for item in array: 
        soup = init_scraper(item['RESOURCE_URL'])

        for obj in soup.select(item['top_tag']): #top_tag

            title = obj.select(item['title_cut'])
            title_checked = empty_data(empty_item=title)

            content = obj.select(item['bottom_tag'])
            content_checked = empty_data(empty_item=content)

            date_cut = obj.select(item['date_cut'])
            nd_date = 0
            if date_cut:
                nd_date = dateparser.parse(date_cut[0].get('datetime')).timestamp()

            news_objects.append({
                "res_id": item['top_tag'],
                "link": obj.get('href'),
                "title": title_checked, #title_cut
                "content": content_checked, #bottom_tag
                "nd_date": nd_date, #date_cut
                "s_date": dateparser.parse(str(datetime.now())).timestamp(),
                "not_date": 122
            })

    print(news_objects)
    return news_objects
