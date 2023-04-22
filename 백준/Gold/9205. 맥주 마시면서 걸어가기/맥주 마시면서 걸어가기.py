from collections import deque



def bfs():
    q = deque()
    q.append([startX, startY])
    while q:
        x, y = q.popleft()
        if abs(x - endX) + abs(y - endY) <= 1000:
            print("happy")
            return
        for i in range(conviniCnt):
            if not visited[i]:
                new_x, new_y = convinis[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return

for t in range(int(input())):
    conviniCnt = int(input())
    convinis = []
    startX, startY = map(int,input().split())
    for _ in range(conviniCnt):
        convinis.append(list(map(int,input().split())))
    endX, endY = map(int,input().split())
    visited = [0 for i in range(conviniCnt)]
    bfs()


    