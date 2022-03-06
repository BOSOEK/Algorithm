# 1303 전쟁-전투 104ms
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

def bfs(i, j, std):
    Q = deque()
    Q.append((i, j))
    graph[i][j] = 'v'
    count = 0
    
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] != 'v' and graph[nx][ny] == std:
                    graph[nx][ny] = 'v'
                    Q.append((nx, ny))
                    count += 1
    return count + 1

white, blue = 0, 0
        
for i in range(m):
    for j in range(n):
        if graph[i][j] != 'v':
            if graph[i][j] == 'W':
                white += bfs(i, j, 'W')**2
            else:
                blue += bfs(i, j, 'B')**2
                
print(white, blue)