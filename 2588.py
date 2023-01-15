num1 = int(input())
num2 = int(input())
num2_100 = (num2 - num2%100)//100
num2_10 = (num2%100-num2%10)//10
num2_1 = num2%10
print(num1*num2_1, num1*num2_10, num1*num2_100, num1*num2, sep='\n')


