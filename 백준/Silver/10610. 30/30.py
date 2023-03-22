x = int(input())
y = list(str(x))

if x%3 !=0 or '0' not in y:
    print(-1)
else:
    y.sort(reverse=True)
    print(''.join(y))


