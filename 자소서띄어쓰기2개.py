import sys
sys.stdin = open('test.txt', encoding='UTF-8')
data = sys.stdin.readlines()
for index, dat in enumerate(data):
    for idx, st in enumerate(dat):
        if dat[idx-1] == ' ' and st == ' ':
            print(dat[idx+1:idx+3])