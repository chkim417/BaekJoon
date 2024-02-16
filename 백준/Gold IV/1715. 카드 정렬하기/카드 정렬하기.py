from queue import PriorityQueue
que = PriorityQueue(100000)
a=int(input())
sum=0
for _ in range(a):
    que.put(int(input()))
if a==1:
    print(0)
    exit()
while True:
    first=que.get()
    second = que.get()
    tmp = first+second
    sum+=tmp
    if que.empty()!= True:
        que.put(tmp)
    else:
        break
print(sum)
