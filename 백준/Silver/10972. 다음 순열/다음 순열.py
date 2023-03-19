t = int(input())
combi = list(map(int, input().split()))

for i in range(t-1, 0, -1):
    if combi[i-1] < combi[i]:
        for j in range(t-1, 0, -1):
            if combi[i-1] < combi[j]:
                combi[i-1], combi[j] = combi[j], combi[i-1]
                combi = combi[:i] + sorted(combi[i:])
                print(*combi)
                exit()
print(-1)
