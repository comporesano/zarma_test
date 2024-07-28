# 2. Обработка данных с использованием SQL
# Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. 
# Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

# БД лежит в папке скрипта, имя файла - test.sqlite


import sqlite3
import os


GLOBAL_PATH = os.path.dirname(os.path.abspath(__file__))


def establish_connection(db_name: str) -> sqlite3.Connection | str:
    try:
        return sqlite3.connect(os.path.join(GLOBAL_PATH, db_name))
    except sqlite3.Error as e:
        return f'Unexpected error: {str(e)}'
    
    
def execute_request(connection: sqlite3.Connection, request_body: str) -> list:
    cursor = connection.cursor()
    try:
        cursor.execute(request_body)
    except sqlite3.Error as e:
        print(f'Error during request execution: {str(e)}')
    return cursor.fetchall()


def main() -> None:
    connection = establish_connection(db_name='test.sqlite')
    data = execute_request(connection=connection, 
                           request_body='SELECT name, age FROM users WHERE age > 30')
    print('Persons with age > 30')
    for target in data:
        print(f'Name: {target[0]} Age: {target[1]}')


if __name__ == '__main__':
    main()
