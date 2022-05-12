import math

n = int(input())
q = list(map(int, input().split()))
summ = 9876543212345678987654321

for i in range(n - 1):
    a = min(q[i], q[i + 1])
    b = max(q[i], q[i + 1])
    if b > 2 * a:
        summ = min(summ, math.ceil(b / 2))
    else:
        summ = min(summ, math.ceil((a + b) / 3))

for i in range(n - 2):
    a = min(q[i], q[i + 2])
    b = max(q[i], q[i + 2])
    x = a
    x = x + math.ceil((b - a) / 2)
    summ = min(summ, x)

q.sort()
summ = min(summ, math.ceil(q[0] / 2) + math.ceil(q[1] / 2))
print(summ)