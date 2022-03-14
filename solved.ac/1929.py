
n, m = input().split()

n = int(n)
m = int(m)

def sal(m):
    arr = [True] * (m+1)
    arr[0] = False
    arr[1] = False

    for i in range(2, m+1):
        if arr[i] == True:
            j = 2

            while (i * j) <= m:
                arr[i*j] = False
                j += 1
    return arr

arr = sal(m)
for i in range(len(arr)):
    if i >= n and arr[i] == True:
        print(i)
