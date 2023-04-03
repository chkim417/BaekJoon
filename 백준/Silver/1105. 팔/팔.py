a, b = map(int,input().split())

strA, strB = str(a), str(b)

if len(strA) != len(strB):
    print(0)
else:
    count=0
    for i in range(len(strA)):
        if strA[i] == strB[i]:
            if strA[i] =='8':
                count+=1
        elif strA[i]<strB[i]:
            break

    print(count)


