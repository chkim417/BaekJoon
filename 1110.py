n = int(input())
n_first = n
cycle = 0
new = -1
while  (n_first != new):
    if new == -1:
        new = n
    new = (new//10 + (new%10))%10 +(new%10)*10
    cycle += 1



print(cycle)
"""
                    다른 사람 코드랑 비교해 봤는데 이게 더 빠름.
                    나와 다르게 각 자리수를 변수지정후 저장하는 방법을 씀
                    변수 지정해서 계산하는 게 더 빠른가봄
A = int(input())

cycle = 0
num = A

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = c + (b * 10)

    cycle = cycle + 1

    if (num == A):
        break

print(cycle)
"""