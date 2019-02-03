#  1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#  заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#  Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


from random import randint
from timeit import timeit


def descending_bubblesort(array):
    counter = 0
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
                counter += 1
    return array, counter


def descending_bubblesort_flag(array):
    counter = 0
    flag = True
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
                counter += 1
                flag = False
        if flag:
            break
    return array, counter


def descending_bubblesort_upgr(array):
    counter = 0
    for i in range(len(array)-1):
        local_max_idx = array.index(max(array[i+1:]), i + 1)
        if array[local_max_idx] > array[i]:
            array[i], array[local_max_idx] = array[local_max_idx], array[i]
            counter += 1
    return array, counter


LIST_LEN = 1000
ROUNDS = 1

for _ in range(ROUNDS):
    for_sort = [randint(-100, 100) for _ in range(LIST_LEN)]
    for_sort_copy = for_sort.copy()
    for_sort_copy2 = for_sort.copy()
#    for_sort = [63, 90, 53, -75, 100, 17, -32, 38, -48, -8, 49, 100, -76, 42, -15, 39, 9, -15, -92, 79]
    print(f'\nArray for sorting:\n{for_sort}')
    #  print(f'Checking by function sorted(): {sorted(for_sort, reverse=True)}')
    for_sort, total_changes = descending_bubblesort(for_sort)
    print(f'Sorted array:\n{for_sort}\nTotal changes = {total_changes}')
    for_sort_copy, total_changes = descending_bubblesort_upgr(for_sort_copy)
    print(f'Sorted array, upgraded version:\n{for_sort_copy}'
          f'\nTotal changes = {total_changes}')
    for_sort_copy2, total_changes = descending_bubblesort_flag(for_sort_copy2)
    print(f'Sorted array, upgraded with flag:\n{for_sort_copy2}'
          f'\nTotal changes = {total_changes}')

print("Время выполнения базового алгоритма:")
print(timeit("descending_bubblesort(for_sort)", setup="from __main__ import descending_bubblesort, for_sort", number=1000))
print("Время выполнения усовершенствованного алгоритма:")
print(timeit("descending_bubblesort_upgr(for_sort_copy)", setup="from __main__ import descending_bubblesort_upgr, for_sort_copy", number=1000))
print("Время выполнения алгоритма с флагом:")
print(timeit("descending_bubblesort_flag(for_sort_copy2)", setup="from __main__ import descending_bubblesort_flag, for_sort_copy2", number=1000))

"""
Для 10 элементов в списке результаты timeit с параметрами по умолчанию:

Время выполнения базового алгоритма:
12.483591117
Время выполнения усовершенствованного алгоритма:
9.191956505999999
Время выполнения алгоритма с флагом:
2.4173380490000014

Для 1000 элементов в списке результаты timeit с параметрами number = 1000:

Время выполнения базового алгоритма:
79.55114852999999
Время выполнения усовершенствованного алгоритма:
19.515205465000008
Время выполнения алгоритма с флагом:
0.1313771279999969
"""