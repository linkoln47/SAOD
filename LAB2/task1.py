import random
from time import time

def binary_search_iterative(array, element):
    print(array)
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
def FibonacciSearch(lys):
    print(lys)
    val = int(input("Введите элемент: "))
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(lys)-1))
        if lys[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif lys[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val:
        return index+1
    return -1
def InterpolationSearch(lys):
    print(lys)
    val = int(input("Введите элемент: "))
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1
class BinarySearchTree:

    def __init__(self):
      self.root = None
      self.size = 0

    def length(self):
      return self.size

    def __len__(self):
      return self.size

    def __iter__(self):
      return self.root.__iter__()
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


array = [random.randint(0, 31) for i in range(15)]
print(array)
array = sorted(array)

answer = input("Бинарное поиск. Хотите найти элемент?(да\нет): ")
match answer:
    case "да":
        p = -1
    case "нет":
        p = 0
answer = ""

while p == -1:
    print(array)
    element = int(input("Введите элемент: "))
    print("Searching for {}".format(element))
    t = time()
    print("Index of {}: {}".format(element, binary_search_iterative(array, element)))
    print('binary_search time is: ', time() - t)
    answer = input("убрать/добавить/не менять элементы?: ")
    match answer:
        case "убрать":
            k = int(input("введите номер элемента: "))
            array.pop(k)
        case "добавить":
            q = int(input("введите число, которое хотите добавить: "))
            array.append(q)
            array = sorted(array)
        case "не менять":
            p = 0
element = 0


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
u = int(input("Бинарное дерево. Введите число для поиска: "))
t = time()
print(root.findval(u))
print('binary_tree time is: ', time() - t)

answer = input("Поиск Фибоначи. Хотите найти элемент?(да\нет): ")
match answer:
    case "да":
        p = -1
    case "нет":
        p = 0
answer = ""

while p == -1:
    t = time()
    print(FibonacciSearch(array))
    print('Fibonacci Search time is: ', time() - t)
    answer = input("убрать/добавить/не менять элементы?: ")
    match answer:
        case "убрать":
            k = int(input("введите номер элемента: "))
            array.pop(k)
        case "добавить":
            q = int(input("введите число, которое хотите добавить: "))
            array.append(q)
            array = sorted(array)
        case "не менять":
            p = 0
p = 0
val = 0

answer = input("Интерполяционный поиск. Хотите найти элемент?(да\нет): ")
match answer:
    case "да":
        p = -1
    case "нет":
        p = 0
answer = ""

while p == -1:
    t = time()
    print(InterpolationSearch(array))
    print('Fibonacci Search time is: ', time() - t)
    answer = input("убрать/добавить/не менять элементы?: ")
    match answer:
        case "убрать":
            k = int(input("введите номер элемента: "))
            array.pop(k)
        case "добавить":
            q = int(input("введите число, которое хотите добавить: "))
            array.append(q)
            array = sorted(array)
        case "не менять":
            p = 0
p = 0
val = 0

v = int(input("Дефолтный поиск. Введите элемент: "))
t = time()
print(array.index(v))
print('default Search time is: ', time() - t)