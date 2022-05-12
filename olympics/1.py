list = list(map(int, input("введите стороны треугольника: ").split()))
list.sort(reverse=True)
P = -1
while P == -1:
    a = list[0]
    b = list[1]
    c = list[2]
    n = len(list)
    if a + b > c and b + c > a and a + c > b:
        P = a + b + c
        print("Треугольник существует\n" + "Периметр треугольника: ", P, "cm")
    else:
        print("Треугольник не существует")
        P = 0
    if P == 0 and n > 3:
        P = -1
        list.pop(0)
        print(list)




