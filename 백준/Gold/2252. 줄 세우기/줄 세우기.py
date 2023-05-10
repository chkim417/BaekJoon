from collections import deque
a, b = map(int,input().split())
pointedCnt = [0 for i in range(a)]
pointedLst =[[] for i in range(a)]
for i in range(b):
    n, nn = map(int,input().split())
    pointedCnt[nn-1]+=1
    pointedLst[n-1].append(nn) # 가리키는 노드들 넣기

answer = [] #답 넣는 곳
xxxxx = [] #각 위상정렬의 시작노드 넣는 곳
for i in range(a):
    if pointedCnt[i] ==0:
        xxxxx.append(i+1) # 위상정렬 시작 노드 넣기
dq = deque()

while xxxxx:
    start = xxxxx.pop()
    dq.append(start)

    while dq: #위상 정렬 시작노드 하나 끝까지 돌리기
        node =dq.popleft()
        answer.append(node)
        for x in pointedLst[node-1]:
            pointedCnt[x-1] -=1
            if pointedCnt[x-1] == 0:
                dq.append(x)
for i in answer:
    if i ==answer[-1]:
        print(i)
    else:
        print(i, end=' ')
        


    



    

    

    
    