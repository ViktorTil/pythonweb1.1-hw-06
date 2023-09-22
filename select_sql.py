#Программа SQL-запросов по паттерну : [python3 select_sql.py query_number.sql]
import sqlite3
import sys
from pprint import pprint


def read_query(query):
    # читаем файл со скриптом для создания БД
    with open(query, 'r') as f:
        sql = f.read()
    return sql

def execute_query(sql: str) -> list:
    with sqlite3.connect('studies.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    try:
        sql = sys.argv[1]
        pprint(execute_query(read_query(sql)))
    except IndexError:
        print(f"Please enter sql-query in console")
    except FileNotFoundError:
        print(f"No such sql-query: {sql}")   


    