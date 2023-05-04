t = int(input())

lst =list(map(int,input().split()))
lst.sort()
if t%2==0:
    print(lst[t//2-1])
else:
    print(lst[t//2])