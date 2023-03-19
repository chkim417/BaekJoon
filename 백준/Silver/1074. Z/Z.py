N, r, c = map(int, input().split())
sector= -1
answer = 0
for i in range(1, N+1):
    std = 2**(N-i)
    if r<std:
        if c<std:
            sector = 0
        else:
            c = c-std
            sector = 1
    else:
        r = r-std
        if c<std:
            sector = 2
        else:
            sector = 3
            c = c-std
    answer +=(2**(2*N-2*i))*sector
    
print(answer)