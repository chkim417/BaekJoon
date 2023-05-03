lst = []
for i in range(9):
    lst.append(int(input()))
summ = sum(lst)

lst_2 =[]
for i in range(9):
   if summ - lst[i]<=100:
      continue
   else:
      for j in range(i+1,9):
         if summ- lst[i] - lst[j] ==100:
            lst[i] = -1
            lst[j] = -1
for i in lst:
   if i>0:
      print(i)


                
                