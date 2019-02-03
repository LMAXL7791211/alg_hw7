#  2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


from random import random


def merge_sort(array_for_separate):
    if len(array_for_separate) > 1:
        separator = len(array_for_separate) // 2
        arr_left, arr_right = array_for_separate[:separator], array_for_separate[separator:]
        arr_left = merge_sort(arr_left)
        arr_right = merge_sort(arr_right)
        return merge(arr_left, arr_right, [])
    else:
        return array_for_separate


def merge(a1, a2, sorted_array):
    if min(len(a1), len(a2)) == 0:
        sorted_array = sorted_array + a1 + a2
        return sorted_array
    else:
        if a1[0] < a2[0]:
            sorted_array.append(a1[0])
            a1.pop(0)
        else:
            sorted_array.append(a2[0])
            a2.pop(0)
        return merge(a1, a2, sorted_array)


LIST_LEN = 17
ROUNDS = 5
MAX_RANDOM = 50

for _ in range(ROUNDS):
    for_sort = [random() * MAX_RANDOM for _ in range(LIST_LEN)]
    print('\nArray for sorting:')
    print(', '.join(['{0:.2f}'.format(el) for el in for_sort]))
    for_sort = merge_sort(for_sort)
    print('Sorted array:')
    print(', '.join(['{0:.2f}'.format(el) for el in for_sort]))
