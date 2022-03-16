from collections import deque

case = int(input())

for c in range(case):
    queue = deque()
    n, m = map(int, input().split())
    dump = list(map(int, input().split()))
    max = 0
    for j in dump: 
        queue.append(j)
        if j >= max : max = j
    count = 0
    while queue:
        data = queue.popleft()
        if max == data:
            count += 1
            if m == 0:
                print(count)
                break
            else :
                max = 0
                for j in queue:
                    if j >= max: max = j
                if m == 0: m = len(queue)-1
                else: m -= 1
        else :
            queue.append(data)
            if m == 0: m = len(queue)-1
            else: m -= 1
