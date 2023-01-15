s = int(input())
def a(n):
    if n == 0:
        return 0
    else:
        return n//5 + a(n//5)

print(a(s))


