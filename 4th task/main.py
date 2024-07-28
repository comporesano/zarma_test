# 4. Оптимизация скрипта
# Дан следующий скрипт на Python для обработки списка чисел. 
# Оптимизируйте его для повышения производительности.

# Исходный скрипт

# numbers = [i for i in range(1, 1000001)]
# squares = []
# for number in numbers:
#   squares.append(number ** 2)


# Оптимизированный скрипт
sqrd_nums = [num ** 2 for num in range(1, 1000001)]


if __name__ == '__main__':
    print(sqrd_nums)