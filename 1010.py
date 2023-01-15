def getCombination(n, m):
    def factorial(a):

        num = 1
        for i in range(1, a+1):
            num*=i
        return num

    return factorial(n)//(factorial(n-m)*factorial(m))



if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        n, m = map(int, input().split())
        print(getCombination(m, n))




