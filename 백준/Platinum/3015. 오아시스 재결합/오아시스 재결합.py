import sys
input = sys.stdin.readline
t = int(input())
lst=[]
sum=0
for _ in range(t):       
    inputt =int(input())
    cnt = 1

    while lst and lst[-1][0] <= inputt:
        h, cnt = lst.pop()
        sum += cnt
        if h == inputt:
            cnt+=1
        elif h<inputt:
            cnt = 1
    if lst:
        sum+=1
    lst.append((inputt,cnt))
print(sum)



    

