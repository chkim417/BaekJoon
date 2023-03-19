from math import comb

a,b,c=map(int,input().split())
if(c == 0):
    combi =comb(a+b-2, a-1)
    print(combi)
else:
    mogs_before, nameoji_before = divmod(c-1, max(a,b))
    mogs_after,nameoji_after =a-1-mogs_before,b-1-nameoji_before
    answer = comb(mogs_before+nameoji_before,mogs_before)*comb(nameoji_after+mogs_after, nameoji_after)
    print(answer)




