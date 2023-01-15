n = int(input())
if n == 1:
    trash = input()
    print("A")
elif n == 2:
    first, second = map(int, input().split())
    if first == second:
        print(first)
    else:
        print("A")
else:
    lst = list(map(int, input().split()))
    if (lst[0] == lst[1] ):
        A = 0
    else:
        A = (lst[2] - lst[1]) // (lst[1] - lst[0])

    B = lst[1] - lst[0] * A
    for i in range(n - 1):
        expect = lst[i] * A + B
        if (lst[i + 1] != expect):
            print("B")
            exit()

    print(lst[-1] * A + B)




