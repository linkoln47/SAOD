ans = 1000 * 1000 * 1000

n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    cur = 0
    x = a[i]
    y = a[i + 1]
    if x < y:
        x, y = y, x
    cnt = min(x-y, int((x+1)/2))
    cur += cnt
    x -= 2*cnt
    y -= cnt
    if x > 0 and y > 0:
        cur += (x + y + 2) / 3
    ans = min(ans, cur)

for i in range(n-2):
    cur = 0
    x = a[i]
    y = a[i + 2]
    if x < y:
        x, y = y, x
    cnt = (x - y + 1) / 2
    cur += cnt
    cur += y
    ans = min(ans, cur)

a.sort()
ans = int(min(ans, int((a[0]+1)/2 + (a[1]+1)/2)))
print(ans)
