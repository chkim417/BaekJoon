from math import pow
from math import ceil


# 1 121 12321 1234321 123454321 과 같은 구조를 기준으로 추가로 더해서 구조가 완성이 된다.
T = int(input())

for i in range(T):
    start, finish = map(int, input().split())
    distance = finish - start
    squared = 1
    while True:
        if pow(squared, 2) < distance:
            squared += 1
        else:
            break
    surplus = distance - pow(squared, 2)
    extra = ceil(surplus/squared)
    result = 2*squared - 1 + extra
    print(result)

