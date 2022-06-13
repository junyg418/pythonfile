pblist = []
pbnum = 2

def checknum(num):
    index = 1
    while index <= num:
        if num % index: 
            pass
        else: #나머지가 0일때 
            if index == 1:
                pass
            elif index != num:
                return False
            else:
                return True   
        index += 1 


while pbnum != 10000:
    if checknum(pbnum):
        # print('y')
        # print(pbnum, end=' ')
        pblist.append(pbnum)
    #     print(pblist)
    # print(pbnum)
    pbnum += 1
print(pblist)

