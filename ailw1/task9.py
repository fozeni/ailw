def zamena(a):
    after=""
    for c in a:
        if c=='а':
            c='о'
            after += c
        else:
            after+= 'a'
    return(after)
print(zamena('аоаоаоаоаоаоаао'))