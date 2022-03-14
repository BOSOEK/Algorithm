# 1012번 유기농 배추 32444KB, 360ms
from collections import deque

T = int(input())

answer = []

def solve(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        if x+1 < len(graph) and graph[x+1][y] == 1:
            queue.append((x+1, y))
            graph[x+1][y] = 0
        if x > 0 and graph[x-1][y] == 1:
            queue.append((x-1, y))
            graph[x-1][y] = 0
        if y+1 < len(graph[0]) and graph[x][y+1] == 1:
            queue.append((x, y+1))
            graph[x][y+1] = 0
        if y > 0 and graph[x][y-1] == 1:
            queue.append((x, y-1))
            graph[x][y-1] = 0

for l in range(T):
    m, n, k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    bug = 0

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                bug += 1
                solve(graph, x, y)
    print(bug)
