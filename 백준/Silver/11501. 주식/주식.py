def stock(stock_list, start, end):
    sum = 0
    while start < end:
        point_value = 0
        point = -1
        for i in range(end, start-1, -1):
            if i and stock_list[i] < stock_list[i-1]:
                end -= 1
            else:
                break
        for i in range(end, start-1, -1):
            if point_value < stock_list[i]:
                point_value = stock_list[i]
                point = i
        for i in range(start, point):
            sum += point_value - stock_list[i]
        start = point + 1
    return sum


for _ in range(int(input())):
    n = int(input())
    stock_list = list(map(int,input().split()))
    print(stock(stock_list, 0, n-1))
