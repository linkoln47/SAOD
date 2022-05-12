def solve(n, k, x, y, a, graph):
    a.add(x)
    a.add(y)
    stack = [(x, 0)]
    parent = (n + 1) * [-1]
    y_height = None
    while stack:
        node, height = stack.pop()
        if node == y:
            y_height = height
        for child in graph[node]:
            if child != parent[node]:
                parent[child] = node
                stack.append((child, height + 1))
    lst = list(a)
    edge_ct = 0
    for node in lst:
        if node != x and parent[node] not in a:
            a.add(parent[node])
            lst.append(parent[node])
        if node != x:
            edge_ct += 2
    return edge_ct - y_height


t = int(input())
for case in range(t):
    input()
    n, k = map(int, input().split())
    x, y = map(int, input().split())
    a = set(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(solve(n, k, x, y, a, graph))
