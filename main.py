from models import Resource, Items
from db import create_table

# Создаем таблицы
create_table()

Resource.from_json("resources2.json")
Items.populate_db()
