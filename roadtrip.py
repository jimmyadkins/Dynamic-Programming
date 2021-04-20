def pen(source, destination):
    return (200 - (destination-source)) * (200 - (destination-source))

def roadtrip(arr):
    n = len(arr)

    cost = [0] * n
    last = [0] * n
    for i in range(n-1, 0, -1):
        cost[i] = pen(0, arr[i])
        print(cost)
        print(last)
        for j in range(0, i-1):
            penalty = pen(arr[j], arr[i])
            if penalty < cost[i]:
                cost[i] = penalty
                last[i] = j
        i = last[i]
    print(cost)
    print(last)

    # final_path = []
    # final_path.append(n)
    # final_path.append(last[n])

test_arr = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
result = roadtrip(test_arr)
print()
print()
# print(result[0])
# print(result[1])
# print(result[2])

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






