
def roadtrip(arr):
    n = len(arr)
    size = 0
    last = [n] * n

    i = 0
    for j in range(i, n-1):
        d = arr[j] - arr[i]
        pen = (200-d)*(200-d)
        if j == n:
            last[j] = i
            i = j
            break
        else:
            nextd = arr[j + 1] - arr[i]
            nextpen = (200-nextd)*(200-nextd)
            if pen < nextpen:
                size += 1
                last[j] = i
                i = j

    path = size*[]
    cur = i
    total = 0
    for j in range(0, size):
        path[size-j] = cur
        total += (200 - (arr[last[cur]] - arr[cur])) * (200 - (arr[last[cur]] - arr[cur]))
        cur = last[cur]
    return total, path





test_arr = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
result = roadtrip(test_arr)
print(result[0])
print(result[1])
