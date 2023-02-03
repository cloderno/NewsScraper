import datetime
import db
import json
from scrape import scrape_news

class Resource:
    # populate db and get resources info from resources.json
    def populate_db(self):
        conn = db.create_connection()
        cursor = conn.cursor()

        # Добавление в базу
        add_to_database = f'''
        INSERT INTO resources (RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut) 
        SELECT '{self.RESOURCE_NAME}', '{self.RESOURCE_URL}', '{self.top_tag}', '{self.bottom_tag}', '{self.title_cut}', '{self.date_cut}'
        FROM DUAL
        WHERE NOT EXISTS (
            SELECT * FROM resources WHERE RESOURCE_URL = '{self.RESOURCE_URL}' AND top_tag = '{self.top_tag}' AND bottom_tag = '{self.bottom_tag}'
        ) 
        '''

        cursor.execute(add_to_database)
        conn.commit()

        cursor.close()
        conn.close()
        
    # Получаем данные из JSON и сохраняем их
    def from_json(file_path):
        with open(file_path, "r") as file:
            items_data = json.load(file)

        items = []

        for obj in items_data:
            RESOURCE_NAME = obj['RESOURCE_NAME']
            RESOURCE_URL = obj['RESOURCE_URL']
            top_tag = obj['top_tag']
            bottom_tag = obj['bottom_tag']
            title_cut = obj['title_cut']
            date_cut = obj['date_cut']

            current_item = Resource(RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut)
            items.append(current_item)

        for item in items:
            item.populate_db()


    def __init__(self, RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut):
        self.RESOURCE_NAME = RESOURCE_NAME
        self.RESOURCE_URL = RESOURCE_URL
        self.top_tag = top_tag
        self.bottom_tag = bottom_tag
        self.title_cut = title_cut
        self.date_cut = date_cut

class Items:
    def populate_db():
        resources_tag_array = db.get_resources()
        # print(arr[0]['RESOURCE_URL'])

        scraped_array = scrape_news(resources_tag_array)

        conn = db.create_connection()
        cursor = conn.cursor()

        for obj in scraped_array: 
            add_to_database = f'''
            INSERT INTO `items` (id, res_id, link, title, content, nd_date, s_date)
            SELECT '{obj['id']}', '{int(33)}', '{obj['link']}', '{obj['title']}', '{obj['content']}' ,'{obj['nd_date']}', '{obj['s_date']}'
            FROM DUAL
            WHERE NOT EXISTS (
                SELECT * FROM items WHERE nd_date = '{obj['nd_date']}'
            )'''

            cursor.execute(add_to_database)

        conn.commit()

        cursor.close()
        conn.close()

    def __init__(self, RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut):
        self.res_id = RESOURCE_NAME
        self.link = RESOURCE_URL
        self.title = top_tag
        self.content = bottom_tag
        self.nd_date = title_cut
        self.s_date = date_cut
        self.not_date = date_cut

# class Item:
#     def __init__(self, RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut):
#         self.RESOURCE_NAME = RESOURCE_NAME
#         self.RESOURCE_URL = RESOURCE_URL
#         self.top_tag = top_tag
#         self.bottom_tag = bottom_tag
#         self.title_cut = title_cut
#         self.date_cut = date_cut

#     def create_item(self, connection):
#         cursor = connection.cursor()
#         table = """
#         CREATE TABLE IF NOT EXISTS items (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             RESOURCE_NAME VARCHAR(255),
#             RESOURCE_URL VARCHAR(255),
#             top_tag VARCHAR(255),
#             bottom_tag VARCHAR(255),
#             title_cut VARCHAR(255),
#             date_cut VARCHAR(255)
#         );
#         """
#         cursor.execute(table)

#         insert_query = "REPLACE INTO items (RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (self.RESOURCE_NAME, self.RESOURCE_URL, self.top_tag, self.bottom_tag, self.title_cut, self.date_cut)

#         cursor.execute(insert_query, values)
#         connection.commit()
#         cursor.close()
