from itertools import combinations
import math
C = combinations



T = int(input())
for t in range(T):
    N = int(input())
    allX = 0
    allY = 0
    coordinateList = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        coordinateList.append(tmp)
        allX += tmp[0]
        allY += tmp[1]

    chooseStartCoordinate = list(C(coordinateList, N // 2))
    minAbsVectorSquared = -1
    for i in range(len(chooseStartCoordinate)//2):
        allMinusX2 = 0
        allMinusY2 = 0
        for j in chooseStartCoordinate[i]:
            allMinusX2 += j[0]
            allMinusY2 += j[1]
        allPlusX2 = allX - allMinusX2
        allPlusY2 = allY - allMinusY2
        VectorSquared = (allPlusX2-allMinusX2)**2+(allPlusY2-allMinusY2)**2
        if VectorSquared < minAbsVectorSquared or minAbsVectorSquared == -1:
            minAbsVectorSquared = VectorSquared


    print(math.sqrt(minAbsVectorSquared))




