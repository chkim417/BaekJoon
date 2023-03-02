x = int(input())
lst = []

lst = list(map(int,input().split()))
m = max(lst)
sum_lst = sum(lst)

answer = sum_lst/m*100/x
print(answer)

