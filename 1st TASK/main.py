# 1. Подключение к API и получение данных
# Напишите скрипт на Python, который подключается к API и получает данные. 
# Например, используйте публичное API https://jsonplaceholder.typicode.com/posts. 
# Сохраните полученные данные в формате JSON в файл.

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
