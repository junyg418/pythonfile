caseN = input()

def check(number):
    if len(number)//2 == 0: #짝수
        for i in range(int(len(number)/2)):
            if number[i] == number[-i-1]:
                continue
            else:
                return False
    else: #홀수
        for i in range(int(len(number))//2):
            if number[i] == number[-1-i]:
                continue
            else:
                return False
    return True

sum = 0
for i in range(int(caseN)):
    a,b = input().split(" ")
    c = a + b
    if check(c):
        sum += 1

print(sum)