def zamena(a):
    after=""
    for c in a:
        if a=='а':
            a='о'
        after+=a
    return(after)
print(zamena('аоаоаоаоаоаоаао'))