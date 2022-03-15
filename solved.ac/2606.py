# 2606 바이러스 32396KB 92ms
from collections import deque

num = int(input())

check = [0] * (num+1)

li = []

net = int(input())
for i in range(net):
    a, b = input().split()
    li.append([int(a), int(b)])

queue = deque()
queue.append(1)

while queue:
    #print(queue)
    #print(check)
    #print('===========')
    n = queue.popleft()
    for i in li:
        if i[0] == n and check[i[1]] == 0 : 
            check[i[1]] = 1
            queue.append(i[1])
        if i[1] == n and check[i[0]] == 0 :
            check[i[0]] = 1
            queue.append(i[0])

check[1] = 0
cnt = 0
for i in check:
    if i == 1: cnt+=1

print(cnt)
