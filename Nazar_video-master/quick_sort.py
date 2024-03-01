'''
Быстрая сортировка, которая работает за O(n log n) в среднем и O(n^2) в худшем случае.

Сначала выбирается опорный элемент, затем массив разбивается на три части:
меньшие опорного, равные опорному и большие опорного.

Затем рекурсивно вызывается функция для меньших и больших элементов.
'''


def quick_sort(arr, comparator=(lambda x, y: x < y)):
    if len(arr) <= 1:
        return arr

    middle = arr[len(arr) // 2] # Выбираем опорный элемент

    less = [x for x in arr if comparator(x, middle)] # Меньшие опорного

    equal = [x for x in arr if x == middle] # Равные опорному

    greater = [x for x in arr if comparator(middle, x)] # Большие опорного

    # Рекурсивно вызываем функцию для меньших и больших элементов
    return quick_sort(less, comparator) + equal + quick_sort(greater, comparator)
