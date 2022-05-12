import random
m = int(input("m = "))
n = int(input("n = "))
min_limit = -1000+14#int(input("min_limit = "))
max_limit = -250#int(input("max_limit = "))
while min_limit > max_limit:
    print("Введите мин и макс значения правильно: ")
    min_limit = int(input("min_limit = "))
    max_limit = int(input("max_limit = "))
Matrix = [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
print("Matrix: ")
for i in range(m):
    print(Matrix[i])