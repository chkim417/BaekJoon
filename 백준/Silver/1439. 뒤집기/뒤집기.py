x = input()
zeroCnt = 0
oneCnt = 0
last = -1
for i in x:
    i = int(i)
    if last != i:
        if i == 0:
            zeroCnt += 1
        else:
            oneCnt += 1
        last = i
print(min(zeroCnt, oneCnt))
