# 4. Оптимизация скрипта
# Дан следующий скрипт на Python для обработки списка чисел. 
# Оптимизируйте его для повышения производительности.

# Исходный скрипт

# numbers = [i for i in range(1, 1000001)]
# squares = []
# for number in numbers:
#   squares.append(number ** 2)

import timeit

# Старый скрипт
def old_script() -> None:
    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)

# Оптимизированный скрипт
def optimized() -> None:
    sqrd_nums = [num ** 2 for num in range(1, 1000001)]


if __name__ == '__main__':
    for _ in range(5):
        print(f'Old: {timeit.timeit("old_script()", setup="from __main__ import old_script", number=1)}', 
              f'Optimized: {timeit.timeit("optimized()", setup="from __main__ import optimized", number=1)}')