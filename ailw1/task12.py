a = input("add \n")
b = a.split()
b[-1],b[0] = b[0], b[-1]
print(' '.join(b))