N = int(input())
meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x:(x[1],x[0]))
cnt=1
a=meetings[0]
if N!=1:
    for i in range(1,N):
        if a[1]>meetings[i][0]:
            continue
        else:
            cnt+=1
            a=meetings[i]
            
print(cnt)


