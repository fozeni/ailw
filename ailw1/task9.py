def zamena(a):
    after=""
    for c in a:
        if c=='а':
            c='о'
            after += c
        elif c == 'о':
            c = 'а'
            after+= c
        else:
            after += c
            continue

    return(after)
print(zamena(input()))