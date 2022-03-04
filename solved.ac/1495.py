n, s, m = map(int, input().split()) 
v = list(map(int, input().split())) 

dp = []
for i in range(n+1):
    line = []
    for j in range(m+1):
        line.append(0)
    dp.append(line)

dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j - v[i] >= 0 :
                dp[i+1][j - v[i]] = 1
            if j + v[i] <= m :
                dp[i+1][j + v[i]] = 1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        print(i)
        break
    if i == 0 and dp[n][i] == 0:
        print(-1)
