
def roadtrip(arr):
    n = len(arr)
    pen = [[(200-arr[y]-arr[x])*(200-arr[y]-arr[x]) for x in range(n)] for y in range(n)]
    path = []
    total = 0
    last = 0
    for i in range(0, n):
        last = 0
        for j in range(0, n):
            if pen[i][j]
    return total, path





test_arr = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
result = roadtrip(test_arr)
print(result[0])
print(result[1])
