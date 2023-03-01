words = input().upper()  # 어차피 출력값은 대문자니까 첨부터 대문자로 받자
char = list(set(words))  # words에 있는 알파벳의 중복값을 없애주고 char라는 리스트애 담아줌

lst = [ ]  #각 알파벳당 중복수를 담을 리스트
for x in char:
    cnt = words.count(x)  #처음 인풋받은 워즈에서 x 개수를 세어서 cnt에 넣어줌
    lst.append(cnt)   # 리스트에 cnt 추가

if lst.count(max(lst)) >1:  #최대빈도 알파벳이 여러개면 물음표 출력
    print('?')
else:
    max_idx = lst.index(max(lst))  #하나이면 그 알파벳을 출력
    print(char[max_idx])