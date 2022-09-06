#줌 하기 귀찮은 내가 만든 프로그램 - 1-5

"""
제작자: 이준영
email : fgh235897@gmail.com
배포 자유이지만 하신다면 메일 보내주시기 바랍니다.
사용해주시는 분들 감사합니다!
"""

import datetime
import time
import webbrowser


# 자신의 시간표대로 수정 필요
# 지정해둬야하는 교시만큼 미리 작성
# 시간은 각 교시의 시작시간으로 작성해야한다.
# 서식 : [  [hour, [min-5,min+5]], ... ]
# 아래 시간은 개발한 이의 시간표의 시간이다.
hours = [[10,[10,20]], [11,[5,15]], [12,[5,15]], [13,[5,15]], [14,[45,55]], [15,[45,55]], [16,[5,15]]]


class_time = { 'class_1':[] ,'class_2':[],'class_3':[],'class_4':[],'class_5':[],'class_6':[],'class_7':[], 'class_8':[]}

# 각 과목에 알맞는 줌 접속 링크로 변경해주세요.
# 만약 없을경우 아무것이나 넣어도 상관 없답니다~!. ex) 점심
subject = [
    '국어링크',
    '수학링크',
    '영어링크',
    '물리링크',
    '화학링크',
    '정보링크',
    '기하링크',
    '음악링크',
    '체육링크',
    '시민링크',
    '사문탐링크',
    '진로링크',
    '점심',
]
# 넣은 과목 순서대로 1부터 시작하여 아래 주석과 같이 과목명을 적어준다면 더욱 편하게 사용하실 수 있습니다.
# 1.문학, 2.미적, 3.영어, 4.물리, 5.화학, 6.정보, 7.기하, 8.음악, 9.체육, 10.시민, 11.사문탐, 12,점심

today_time = ''
treeHit = 0

while True:

    today_time = input("""              오늘은 몇교시
                                    숫자로 기입해주세요. >
                       """)

    
    if (today_time.isdigit()):

        if 0>=int(today_time):
            continue
    
        today_time = int(today_time)

        # 링크를 넣은 과목 순서대로 1부터 시작하여 아래 주석과 같이 과목명을 적어주는것을 강력히 권장합니다.
        # 귀찮으시다면 코드의 순서를 보고 잘... 
        print('과목번호: 1.문학, 2.미적, 3.영어, 4.물리, 5.화학, 6.정보, 7.기하, 8.음악, 9.체육, 10.시민, 11.사문탐, 12,점심')

        for w_time in range(1, today_time+1):
            class_time[f'class_{w_time}'] = input('{}교시 과목번호:'.format(w_time))
        break

    else:
        print('잘못 입력했습니다.')


print(class_time)
waiting = True
while True:
    now = datetime.datetime.now()
    
    for idx, (key, value) in enumerate(hours):
        if now.hour== key:
            if value[0] <= now.minute <= value[1]:

                print(f'지금은 {idx+1}교시 수업중입니다.')
                webbrowser.open(subject[idx])

                # 연산 최적화를 위한 멈춤 
                # default : 3000  -> 50분
                # 수업시간이 짧거나 길다면 조정하시기 바람
                time.sleep(3000) # 기준 sec

                waiting = True

        else:
            if waiting: 
                    print('''수업이 끝났거나 대기중입니다. 
    수업이 끝나셨다면 ctrl + c 를 눌러주시면 작동이 멈춥니다.''')
                    waiting = False