import math
a = int(input('a \n'))
b = int(input("b \n"))
c = int(input("c \n"))
p = (a+b+c)/2
if a < b+c or b < a+c or c < b+a:
    s = math.sqrt(p * (p-a)*(p-b)*(p-c))
else:
    print('неравенство не выполняется!')
print(s)