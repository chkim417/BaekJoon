a, b = map(int,input().split())
if a==b:
    print(a)
    exit()
cnt=b-a+2
for i in range(b, a-1, -1):
    for j in range(2,i):
        if i%j !=0:
            cnt+=1
print(cnt)