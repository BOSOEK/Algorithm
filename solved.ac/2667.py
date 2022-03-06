# 2667 단지번호붙이기 72ms
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))


def dfs(x, y):
    global count
    if x < n-1 and graph[x+1][y] == 1 :
        graph[x][y] = 3
        dfs(x+1, y)
    if x > 0 and graph[x-1][y] == 1 :
        graph[x][y] = 3
        dfs(x-1, y) 
    if y < n-1 and graph[x][y+1] == 1 :
        graph[x][y] = 3
        dfs(x, y+1)
    if y > 0 and graph[x][y-1] == 1 :
        graph[x][y] = 3
        dfs(x, y-1)

    graph[x][y] = 0
    count += 1
    return

num = []
count = 0 


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            num.append(count)
            count = 0

num.sort()
print(len(num))
for i in num:
    print(i)

