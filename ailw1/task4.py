a = int(input('a \n'))
b = int(input('a \n'))
 
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print(a + b)