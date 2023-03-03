a= [1, 2, 3]
b= [3, 2, 1]
lst = list(map(int,input().split()))
lst_sort = sorted(lst)
lst_sort_reverse = sorted(lst, reverse = True)

if (lst !=lst_sort)and(lst !=lst_sort_reverse):
    print('mixed')
elif lst== lst_sort:
    print('ascending')
else:
    print('descending')
    
