def pen(source, destination):
    return (200 - (destination-source)) * (200 - (destination-source))

def roadtrip(arr):
    n = len(arr)
    cost = [0] * n
    last = [0] * n
    for i in range(1, n):
        cost[i] = pen(arr[last[i]], arr[i]) + cost[last[i]]
        for j in range(0, i):
            penalty = pen(arr[j], arr[i]) + cost[j]
            if penalty < cost[i]:
                cost[i] = penalty
                last[i] = j

    finalPath = [n-1]
    while finalPath[-1]!= 0:
        finalPath.append(last[finalPath[-1]])
    finalPath.reverse()
    return cost[-1], finalPath

# test_arr = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
test_arr = [0, 195, 212, 370, 450, 530, 670, 700, 800, 920, 970, 1085, 1130, 1220, 1350, 1440, 1600]

result = roadtrip(test_arr)
print()
print(result)


    # pen = [[(200 - arr[y] - arr[x]) * (200 - arr[y] - arr[x]) for x in range(n)] for y in range(n)]
    # print(pen)
    # for i in range(n-1,0,-1):
    #     temp_pen = pen[i][i]
    #     temp_num = i
    #     for j in range(i,1,-1):
    #         if temp_pen > pen[i][j]:
    #             temp_pen = pen[i][j]
    #             temp_num += j
    #     finalPath.append(temp_num)
    #     penalty += pen[i][j]
    #     i = temp_num

    # dist = [0] * n
    # last = [0] * n
    #

    # print(dist)
    # print(last)
    # finalPath = []
    # penalty = 0


    # return dist[n-1], penalty, finalPath






