import sqlite3

def create_db():
    # читаем файл со скриптом для создания БД
    with open('create_table.sql', 'r') as f:
        sql = f.read()

    # создаем соединение с БД (если файла с БД нет, он будет создан)
    with sqlite3.connect('studies.db') as con:
        cur = con.cursor()
        # выполняем скрипт из файла, который создаст таблицы в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
    
    