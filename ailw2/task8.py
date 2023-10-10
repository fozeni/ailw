spisok = []
while True:
    a = int(input("введите число (для окончания введите 0) \n"))
    if a == 0:
        break
    else:
        spisok.append(a)
delete = int(input("введите число для удаления"))
for i in spisok:
    if i == delete:
        del spisok[i]
print(spisok)