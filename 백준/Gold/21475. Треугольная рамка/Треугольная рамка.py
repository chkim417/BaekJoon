from math import acos,sqrt,tan
a, b, c, d = map(int,input().split())

angleA = acos((b**2+c**2-a**2)/(2*b*c))
angleHalfA = angleA/2
angleB = acos((c**2+a**2-b**2)/(2*c*a))
angleHalfB = angleB/2
angleC = acos((a**2+b**2-c**2)/(2*a*b))
angleHalfC = angleC/2
aa = d/tan(angleHalfA)
bb=d/tan(angleHalfB)
cc=d/tan(angleHalfC)
angleB = acos((c**2+a**2-b**2)/(2*c*a))
angleHalfB = angleB/2

answer = round((a+b+c-aa-bb-cc)*d,5)
print(answer)
