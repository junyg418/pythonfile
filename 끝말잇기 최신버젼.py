'''
설명 주석
    초기 자료 X
    선물용으로 제작한 코드
    끝말잇기 간단하게 구현함
'''

import time
print('''
            끝말잇기를 시작합니다.
첫 단어를 입력하는 순간부터 3초가 카운트 됩니다.
   시간은 보이지 않으니 빠르게 입력하지 않으면
    시간초과로 게임에서 패배하게 됩니다.
''')
time.sleep(1)
first_word = input('단어를 입력하세요! : ')
start = 0
end = 1
treehit = 1
while end-start<=3:
    try:
        start = time.time()
        print(f'{first_word[-1]}로 시작하는 말')
        back_word = input('입력: ')
        if back_word:
            print('당신은 아무것도 입력하지 않아서 패배ㅐ~')
            treehit = 0
            break
        if back_word[0] == first_word[-1]:
            end = time.time()
            first_word = back_word
            continue
        else:
            print('잘못 입력하셨습니다..!')
            treehit = 0
            break
    except:
        print('오류가 났나봅니다..')
        break
if treehit:
    print('시간초과!...')
