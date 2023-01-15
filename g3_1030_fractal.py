"""
    before_List = now_List
        now_List = []
        for beforeTile in before_List:
            for i in range((N - K)//2 + N*beforeTile[0], (N + K)//2 + N*beforeTile[0]):
                print((N + K) // 2 + N * beforeTile[0])
                for j in range((N - K)//2 + N*beforeTile[1], (N + K)//2 + beforeTile[1]):
                    now_List.append([i, j])
                    print(now_List)
        sec = sec-1
"""


if __name__ == '__main__':
    sec, N, K, R_1, R_2, C_1, C_2 = map(int, input().split())
    nowTime = 0
    before_List = []
    while nowTime < sec:
        now_List = []
        for i in range(0, N**nowTime):
            for j in range(0, N**nowTime):
                for k in range((N - K) // 2 + N * i, (N + K) // 2 + N * i):
                    for l in range((N - K) // 2 + N * j, (N + K) // 2 + N * j):
                        now_List.append([k, l])


                if[i, j] in before_List:
                    for k in range(N*i, N*(i+1)):
                        for l in range(N * j, N * (j + 1)):
                            now_List.append([k, l])

        nowTime += 1
        before_List = now_List



    for i in range(R_1, R_2+1):     #출력
        for j in range(C_1, C_2+1):
            print(0, end = "")

            if j == C_2:
                print("\n", end = "")





