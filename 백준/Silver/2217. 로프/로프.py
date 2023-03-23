t = int(input())
ropes = []
max_weight=[]
for _ in range(t):
    ropes.append(int(input()))
ropes.sort(reverse=True)
for i  in range(len(ropes)):
    max_weight.append(ropes[i]*(i+1))
print(max(max_weight))
