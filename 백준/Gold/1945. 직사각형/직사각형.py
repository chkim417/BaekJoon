plus = []
minus = []

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    plus.append(b/c)
    minus.append(d/a)
plus.sort(reverse=True)
minus.sort(reverse=True)
max = -1 # 통과하는 직사각형 개수 최대값
now = 0 # 현재 지나가는 직사각형 개수
last = 0 # 전 기울기 값
buffer = 0 # 예를 들어 마이너스에 1이란 기울기가 3개 들어있으면 이 3개를 모두 지나고 이것의 다음 기울기가 왔을떄 한꺼번에 빼줘야 하므로 이걸 기다려주는 버퍼를 만듦
while plus:
    k = -1 #기울기 담을 변수 초기화
    if plus[-1]<minus[-1]: # 더 낮은 쪽 pop하기
        k = plus.pop()
        now+=1
        if last != k:
            now-= buffer
            buffer=0

    elif plus[-1]>minus[-1]:
        k = minus.pop()
        if last != k:
            now-= buffer
            buffer=1
        else: 
            buffer+=1
    else:                   #기울기 같으면 둘다 pop하기
        k= plus.pop()
        minus.pop()
        now+=1
        if last != k:
            now-= buffer
            buffer=1
        else: 
            buffer+=1
    if max<now:
        max = now

    last = k
print(max)