n, m = map(int, input().split())

def a(x):
    if x == 0:
        return 0
    else:
        return x//5 + a(x//5)
def b(x):
    if x == 0:
        return 0
    else:
        return x//2 + b(x//2)


ans = min(a(n)-a(n-m)-a(m), b(n)-b(n-m)-b(m))

print(ans)

"""
                        각 팩토리얼의 2와 5의 갯수를 구할 때 2, 2의제곱, 2의세제곱 등으로 나누고 더할 때 무한와일문 이용
                        ex) 14면 14/2 = 7,2가 하나 있는 수의 갯수 = 7, 그리고 base에 arg(2)를 곱해 4로 만들고
                        다시 14/4 = 3 , 즉 2가 두개 이상 있는 수의 갯수 = 3....
                        계속 가다가 base가 num보다 커지면 stop.
                        총 2의 갯수, 즉 모든 2를 카운트한 수를 cnt에 저장 후 counters 리스트에 저장
                        갓벽 ㄷㄷ....
import sys

n, r = map(int,sys.stdin.readline().rstrip().split())
counters = []

for num in [n, r, n-r] : # 1부터 n/r/n-r까지의 숫자에 대해 2의 개수와 5의 개수를 카운트
    for arg in [2, 5] :
        base = arg
        cnt = 0
        while True :
            cnt += num // base
            base *= arg
            if base > num : break
        counters.append(cnt)

fives = counters[1] - counters[3] - counters[5]
twos = counters[0] - counters[2] - counters[4]
print(max(0,min(fives,twos)))
"""