from math import gcd
G = gcd


N = int(input())

ingredient = [None]*N
pairList = []
for i in range(N):
    a, b, c, d = list(map(int, input().split()))
    if ~bool(ingredient[a]) and ~bool(ingredient[b]):
        ingredient[a] = c//G(c,d)
        ingredient[b] = d//G(c,d)
    elif bool(ingredient[a]) and bool(ingredient[b]):
        a = 1










