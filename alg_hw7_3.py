#  3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#  в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
#  Задачу можно решить без сортировки исходного массива.
#  Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        #assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


m = int(input('введите m для определения длины массива 2m + 1 -->'))
for_search = [random.randint(-100, 100) for _ in range(2 * m + 1)]
#  for_search = [10, 63, 90, 53, -75, 100, 17, -32, 38, -48, -8, 49, 100, -76, 42, -15, 39, 9, -15, -92, 79]
median = quickselect_median(for_search)
print('Медиана массива:')
print(for_search)
print(f'равна {median}')
print(f'проверка, отсортированный массив:\n{sorted(for_search)}')
print(f'медиана = {sorted(for_search)[int(len(for_search)//2)]}')
