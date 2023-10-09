a = int(input('a \n'))
_sum = 0
while a > 0:
    digit = a % 10
    _sum = _sum + digit
    a = a // 10
print("Сумма:", _sum)