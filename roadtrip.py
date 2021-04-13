
def roadtrip(arr):
    n = len(arr)
    pen = [[(200-arr[y]-arr[x])*(200-arr[y]-arr[x]) for x in range(n)] for y in range(n)]

    finalPath = []
    penalty = 0

    for i in range(n-1,0,-1):
        print(pen[i])
        temp_pen = pen[i][i]
        temp_num = 0
        for j in range(i,1,-1):
            if temp_pen > pen[i][j]:
                temp_pen = pen[i][j]
                temp_num = j
        finalPath.append(temp_num)
        penalty += pen[i][j]
        i = temp_num
        print(finalPath)
        print(penalty)

    # dist = [0] * n
    # last = [0] * n
    #
    # for i in range(0, n):
    #     dist[i] = pen[i][i]
    #     last[i] = 0
    #     for j in range(0, i):
    #         if pen[i][j] < dist[i]:
    #             dist[i] = pen[i][j]
    #             last[i] = j
    # print(dist)
    # print(last)
    # finalPath = []
    # penalty = 0


    return dist[n-1], penalty, finalPath





test_arr = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
result = roadtrip(test_arr)
print(result[0])
print(result[1])
print(result[2])
