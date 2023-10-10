a = [1,2,3,3,2,1,2,1]
b = int(input("Элемент: \n"))
for i in a:
    if b == i:
        print(a.index(b))
        break