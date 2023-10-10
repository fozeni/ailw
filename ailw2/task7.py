b = []

while True:
    a = int(input("введите число (для окончания введите 0) \n"))
    if a == 0:
        break
    else:
        b.append(a)
num = int(input("ввидите число \n"))
pos = int(input("введите позицию"))
b.append(num[pos])
print(b)
