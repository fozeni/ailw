b = []
count = 0

while True:
    a = int(input("введите числа \n"))
    if a == 0:
        break
    else:
        b.append(a)

c = input("ввдеите элемент \n")
for i in b:
    if str(i) == c:
        count += 1
print(count)