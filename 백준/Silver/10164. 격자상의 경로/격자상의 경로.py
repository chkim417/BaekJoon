from math import comb

a,b,c=map(int,input().split())
if(c == 0):
    combi =comb(a+b-2, a-1)
    print(combi)
else:
    moving_count_before_point=0
    moving_count_after_point=0
    bigger = max(a, b)
    mogs, nameoji = divmod(c,bigger)
    nameoji -=1
    moving_count_before_point += comb(mogs+nameoji, nameoji)
    mogs,nameoji = divmod(a*b-c,bigger)
    moving_count_after_point += comb(mogs+nameoji, nameoji)
    answer=moving_count_after_point*moving_count_before_point
    print(answer)




