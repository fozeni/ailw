a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i//2)
    else:
        b.append(i)
print(b)