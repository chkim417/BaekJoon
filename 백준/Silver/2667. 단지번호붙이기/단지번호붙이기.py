from collections import deque
N = int(input())
vilage = []
answer= []
for i in range(N):
    a= input()
    vilage.append(list(map(int,a)))

def BFS(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    dx= [-1,1, 0, 0]
    dy= [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if-1<nx<N and -1<ny<N:
                if graph[nx][ny] ==1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count+=1
    return count

for i in range(N):
    for j in range(N):
        if vilage[i][j]==1:
            answer.append(BFS(vilage, i, j))

answer.sort()
l = len(answer)
print(l)
for i in range(l):
    print(answer[i])








