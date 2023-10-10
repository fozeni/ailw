b = []
while True:
    a = int(input("введите число (для окончания введите 0) \n"))
    if a == 0:
        break
    else:
        b.append(a)

otr = []
pol = []

for i in b:
    if i <= 0:
        otr.append(i)
    else:
        pol.append(i)
print(otr,pol)