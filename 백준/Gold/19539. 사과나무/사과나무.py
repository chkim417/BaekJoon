t = int(input())

trees = list(map(int,input().split()))
one = 0
two = 0
for i in trees:
    if i%2 ==0:
        two+=i//2
    else:
        two+= i//2
        one+= 1
if(two<one):
    print("NO")
elif(two==one):
    print("YES")
else:
    a = two-one
    if a%3==0:
        print("YES")
    else:
        print("NO")

