a = int(input())

for i in range(0, a):
    for j in range(0, a):
        if(a-i-j >=2):
            print(' ', end='')
        elif(j == a-1):
            print('*')
        else:
            print('*', end='')
    
        
        