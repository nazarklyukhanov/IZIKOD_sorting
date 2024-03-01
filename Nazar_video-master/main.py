import time
from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from data_gen import read_db


# Компаратор который сравнивает в следующем порядке:
# 1) все что начинаются с букв (неважно какой регистр)
# 2) если первая буква совпадает то смотрим на вторую и тд
# 3) далее сортируем по юникоду (если начинается со специального символа)
def comparator(x, y):
    if x[0].isalpha() and y[0].isalpha():
        return x.lower() < y.lower()
    elif x[0].isalpha() and not y[0].isalpha():
        return True
    elif not x[0].isalpha() and y[0].isalpha():
        return False
    else:
        return x < y


if __name__ == '__main__':
    # Генерируем данные при необходимости
    # gen_data(10000)

    # Считываем данные из бд
    data = read_db()

    # Сортируем массивы с помощью трёх алгоритмов
    start = time.time()
    quick_sort(data.copy(), comparator)
    print("Quick sort:", time.time() - start)

    start = time.time()
    merge_sort(data.copy(), comparator)
    print("Merge sort:", time.time() - start)

    # start = time.time()
    # bubble_sort(data.copy(), comparator)
    # print("Bubble sort:", time.time() - start)
    print(quick_sort(data[:500], comparator))


    '''
    Output:
    Quick sort: 0.035240888595581055
    Merge sort: 0.029958248138427734
    Bubble sort: 7.7840728759765625
    '''
