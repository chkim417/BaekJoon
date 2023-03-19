from collections import deque
t = int(input())
jump_lst=[]
for _ in range(t):
    jump_lst.append(list(map(int,input().split())))
able_jump=deque()
able_jump.append([0,0])
cnt = 0
count_list = [[0 for i in range(t)] for i in range(t)]
count_list[0][0]=1
for i in range(t):
    for j in range(t):
        size = jump_lst[i][j]
        if size == 0:
            break
        if (i+size)<t:
            count_list[i+size][j] += count_list[i][j]
        if (j+size)<t:
            count_list[i][j+size] += count_list[i][j]


print(count_list[-1][-1])




    



