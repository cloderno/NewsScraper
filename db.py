import mysql.connector
import json

# Подключение к бд
def create_connection():
    return mysql.connector.connect(
        database="mysql",
        host="127.0.0.1",
        user="root",
        password="root"
    )

# Создание таблиц
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Создание таблицы при отсутствии
    resources = f'''
    CREATE TABLE IF NOT EXISTS resources (
        id INT AUTO_INCREMENT PRIMARY KEY,
        RESOURCE_NAME VARCHAR(255),
        RESOURCE_URL VARCHAR(255),
        top_tag VARCHAR(255),
        bottom_tag VARCHAR(255),
        title_cut VARCHAR(255),
        date_cut VARCHAR(255)
    );
    '''
    
    items = f'''
    CREATE TABLE IF NOT EXISTS items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        res_id INT NOT NULL, 
        link VARCHAR(255), 
        title TEXT NOT NULL, 
        content TEXT NOT NULL, 
        nd_date FLOAT, 
        s_date FLOAT 
    );
    '''

    queries = [resources, items]

    for query in queries:
        cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()

# Получение ресурсов
def get_resources():
    arr = []

    conn = create_connection()
    cursor = conn.cursor()

    # Получение ссылок из таблицы
    table = 'SELECT * FROM resources'
    cursor.execute(table)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    for row in result:
        arr.append({"id": row[0], "RESOURCE_NAME":row[1],"RESOURCE_URL":row[2],"top_tag":row[3], "bottom_tag":row[4],"title_cut":row[5],"date_cut":row[6]})


    return arr
