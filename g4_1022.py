

r1, c1, r2, c2 = map(int, input().split())

#행과 열의 값 중애서 더 큰 값으로 공식에 대입


def getSwirl(x, y):
    if abs(x)>=abs(y):
        return 4*(x**2) +abs(x-y)+1
    else:
        return 4*(y**2) +abs(y-x)+1






for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(getSwirl(i, j))
