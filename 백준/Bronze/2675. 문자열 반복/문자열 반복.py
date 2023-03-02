t = int(input())
for i in range(0, t):
    times, word = input().split()
    lst =list(word)
    str=""
    for k in lst:
        str += k*int(times)

    print(str)

