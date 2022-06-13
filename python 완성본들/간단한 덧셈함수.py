def Quiz(a,b):
    answar = int(input('{} + {} = '.format(a,b)))
    if a + b == answar:
        print('yes')
    else:
        print('no')

Quiz(1,3)