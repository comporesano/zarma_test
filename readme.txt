Добрый день, просим пройти Тестовое задание для кандидата на позицию программиста Python

1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API и получает данные. Например, используйте публичное API https://jsonplaceholder.typicode.com/posts. Сохраните полученные данные в формате JSON в файл.

Мой скрипт:

# Для решения данного таска был выбран публичный API мировых университетов по заданной стране(кроме Russia почему-то не работает:c).


import requests
import json
import os


GLOBAL_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data(url: str, params) -> dict | str:
    try:
        return requests.get(url=url, params=params).json()
    except requests.ConnectionError as ce:
        return f'Connection error: {str(ce)}'
    except requests.Timeout as te:
        return f'Timeout error: {str(te)}'


def dump_to_json(filename: str, data: dict) -> None:
    try:
        with open(file=os.path.join(GLOBAL_PATH, filename), mode='w', encoding='utf-8') as jf:
            json.dump(obj=data, fp=jf, ensure_ascii=False, indent=4)
    except OSError as ose:
        print(f'Unexpected error: {str(ose)}')


def main() -> None:
    data = {}
    URL = 'http://universities.hipolabs.com/search'
    params = {
        'country': input('Print country(Example: Germany) - ') 
    }
    data = get_data(url=URL, params=params)
    dump_to_json(filename='test.json', data=data)


if __name__ == '__main__':
    main()

Типовой вывод(Содержимое файла test.json):

[
    {
        "alpha_two_code": "NG",
        "web_pages": [
            "http://www.aaua.edu.ng/"
        ],
        "country": "Nigeria",
        "domains": [
            "aaua.edu.ng"
        ],
        "name": "Adekunle Ajasin University",
        "state-province": null
    },
    {
        "alpha_two_code": "NG",
        "web_pages": [
            "http://www.aauekpoma.edu.ng/"
        ],
        "country": "Nigeria",
        "domains": [
            "aauekpoma.edu.ng"
        ],
        "name": "Ambrose Alli University",
        "state-province": null
    },
    {
        "alpha_two_code": "NG",
        "web_pages": [.....................

2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

Содержимое базы данных test.sqlite представлено в csv:
id, name, age
1, Alice, 25
2, Bob, 30
3, Charlie, 35
4, David, 40
5, Eve, 45

Мой скрипт:

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

Типовой вывод скрипта:

romandev@devstat:~/zarma_test$ python3 2nd\ TASK/main.py 
Persons with age > 30
Name: Charlie Age: 35
Name: David Age: 40
Name: Eve Age: 45

3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников. Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name). Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount). Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.

Содержимое файла test.csv:

product_id,product_name
1,Samsung Galaxy Z Fold 6
2,Iphone 15 Pro
3,Samsung Galaxy S 24
4,One Plus Nord CE 5G
5,Ipad Air 5
6,Iphone 14 Plus

Содержимое файла test.json:

{
    "sales": [
        {
            "sale_id": 11,
            "product_id": 2,
            "amount": 1
        },
        {
            "sale_id": 12,
            "product_id": 3,
            "amount": 2
        },
        {
            "sale_id": 13,
            "product_id": 5,
            "amount": 20
        },
        {
            "sale_id": 14,
            "product_id": 1,
            "amount": 1
        },
        {
            "sale_id": 15,
            "product_id": 4,
            "amount": 2
        },
        {
            "sale_id": 16,
            "product_id": 4,
            "amount": 6
        },
        {
            "sale_id": 17,
            "product_id": 2,
            "amount": 1
        }
    ]
}

Мой скрипт:



import csv
import json
import os


GLOBAL_PATH = os.path.dirname(os.path.abspath(__file__))


def import_from_csv(csv_filename: str) -> list[dict[str, str]]:
    complete_filename = os.path.join(GLOBAL_PATH, csv_filename)
    with open(file=complete_filename, mode='r', encoding='utf-8') as cf:
        csv_reader = csv.DictReader(cf)
    
        return [{'product_id': el['product_id'], 'product_name': el['product_name']} for el in csv_reader]


def import_from_json(json_filename: str) -> dict[str, list]:
    complete_filename = os.path.join(GLOBAL_PATH, json_filename)
    with open(file=complete_filename, mode='r', encoding='utf-8') as jf:
        return json.load(fp=jf)
    

def get_prod_name(csv_data: list[dict[str, str]], prod_id: int) -> str:
    return [el['product_name'] for el in csv_data if int(el['product_id']) == prod_id][0]


def print_table(data: dict) -> None:
    max_name_len = len(max(data)) + 3
    max_amount_len = max([data[key]['amount'] for key in data]) + 3
    max_sales_len = max([len(data[key]['sales_ids']) for key in data]) + 3
    headers = ''
    headers += f'{"NAME OF PRODUCT":<{max_name_len}}'
    headers += f'{"AMOUNT":<{max_amount_len}}'
    headers += f'{"SALES IDS":<{max_sales_len}}'
    headers += '\n'
    complete_string = ''
    for prod_name in data:
        amount = data[prod_name]['amount']
        sales_ids = ' '.join([str(el) for el in data[prod_name]['sales_ids']])
        pattern_string = ''
        pattern_string += f'{f"{prod_name}":<{max_name_len}}'
        pattern_string += f'{f"{amount}":<{max_amount_len}}'
        pattern_string += f'{f"{sales_ids}":<{max_sales_len}}\n'
        complete_string += pattern_string
    headers += complete_string
    print(headers)
    

def join_data(csv_data: list[dict[str, str]], json_data: dict[str, list]) -> dict:
    result_dict = {}
    
    for el in json_data['sales']:
        prod_id = el['product_id']
        prod_name = get_prod_name(csv_data=csv_data, prod_id=prod_id)
        if not prod_name in result_dict:
            result_dict[prod_name] = {'amount': 0, 'sales_ids': []}
        result_dict[prod_name]['amount'] += el['amount']
        result_dict[prod_name]['sales_ids'].append(el['sale_id'])
    return result_dict


def main() -> None:
    csv_data = import_from_csv(csv_filename='test.csv')
    json_data = import_from_json(json_filename='test.json')
    data = join_data(csv_data=csv_data, json_data=json_data)
    print_table(data)
    
    
if __name__ == '__main__':
    main()

Типовой вывод

romandev@devstat:~/zarma_test$ python3 3rd\ TASK/main.py 
NAME OF PRODUCT           AMOUNT                 SALES IDS
Iphone 15 Pro             2                      11 17
Samsung Galaxy S 24       2                      12   
Ipad Air 5                20                     13   
Samsung Galaxy Z Fold 6   1                      14   
One Plus Nord CE 5G       8                      15 16

4. Оптимизация скрипта
Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.

Исходный скрипт

numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
squares.append(number ** 2)

Я оптимизировал скрипт с помощью list comprehension:

# Старый скрипт
def old_script() -> None:
    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)

# Оптимизированный скрипт
def optimized() -> None:
    sqrd_nums = [num ** 2 for num in range(1, 1000001)]

Почему он оптимизированнее:

1. Читабельнее
2. Уменьшение количества операций
3. И по тестам оптимизированый скрипт не намного но быстрее выполняется

Результаты тестов:

romandev@devstat:~/zarma_test$ python3 4th\ TASK/main.py
Old: 0.8519232010003179 Optimized: 0.6963128869992943
Old: 0.8036980130000302 Optimized: 0.6959065760001977
Old: 0.8401430450003318 Optimized: 0.7194874839997283
Old: 0.7684027499999502 Optimized: 0.7231102690002444
Old: 0.876647531999879 Optimized: 0.7800761290000082