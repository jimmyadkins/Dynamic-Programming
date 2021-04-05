
def sequence(arr):
    n = len(arr)
    best = 0
    size = [1] * n
    last = [n] * n

    for i in range(0, n):
        for j in range(i, n):
            if arr[j] > arr[i]:
                if size[i] >= size[j]:
                    last[j] = i
                    size[j] = size[i] + 1

                if size[j] > size[best]:
                    best = j

    cur = best
    result = [0] * size[best]
    for i in range(0, size[best]):
        result[i] = arr[cur]
        cur = last[cur]
    result.reverse()
    return size[best], result

test_arr = [2, 22, 32, 35, 66, 59, 79, 64, 48, 96, 7, 39, 18, 15, 45, 89, 3, 81, 26, 26, 31, 55, 10, 91, 70, 61, 12, 87, 13, 31, 27, 58, 71, 75, 32, 63, 98, 77, 92, 43, 66, 32, 11, 65, 1, 80, 14, 99, 29, 91]
result = sequence(test_arr)
print(result[0])
print(result[1])
