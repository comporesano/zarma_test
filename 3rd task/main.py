# 3. Объединение данных из разных источников
# Напишите скрипт на Python, который объединяет данные из двух источников. 
# Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name). 
# Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount). 
# Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.


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