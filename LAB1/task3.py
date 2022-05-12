import math
import random
from time import time

def selectionSort(array):
    t = time()
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i + 1, len(array)):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    print('Selection sorting time is: ', time() - t)
    return array

def insertionSort(array):
    t = time()
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    print('Insertion sorting time is: ', time() - t)
    return array

def bubbleSort(array):
    t = time()
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    print('Bubble sorting time is: ', time() - t)
    return array

def shellSort(array):
    t = time()
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    print('Shell sorting time is: ', time() - t)
    return array

def quickSort(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)
def heapSort(array):
    t = time()
    n = len(array)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] # свап
        heapify(array, i, 0)
    print('Heap sorting time is: ', time() - t)
    return array


array = [random.randint(-500, 499) for i in range(1000)]
array0 = array.copy()
array1 = array.copy()
array2 = array.copy()
array3 = array.copy()
array5 = array.copy()
array6 = array.copy()

print('Selection array: ', selectionSort(array0))
print('Insertion array: ', insertionSort(array1))
print('Bubble array: ', bubbleSort(array2))
print('Shells array: ', shellSort(array3))
print('Quick array: ', quickSort(array5))
print('Heap array: ', heapSort(array6))

t = time()
array.sort()
print("default sorting time is: ", time() - t)
print("default array: ", array)
