t = int(input())

for _ in range(t):
    stock_count= int(input())
    stock_list=list(map(int,input().split()))
    action=[-1 for _ in range(stock_count)] # -1:null 0: buy 1: sell
    marked=-1
    sum=0
    points=[]
    for i in range(1,stock_count-1):
        if stock_list[i-1]<stock_list[i] and stock_list[i]>stock_list[i+1]:
            points.append([i,stock_list[i]])
    points.append([0,stock_list[0]])
    points.append([stock_count-1,stock_list[-1]])
    points.sort(key=lambda x:x[1], reverse=True)
    for point in points:
        if marked>point[0]:
            continue
        else:
            for idx in range(marked+1, point[0]):
                if point[1]> stock_list[idx]:
                    sum+= point[1]-stock_list[idx]
                    marked=point[0]
    print(sum)






