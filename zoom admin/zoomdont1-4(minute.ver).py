'''
줌 하기 귀찮은 내가 만든 프로그램 - 1-3.practice
1-3ver 을 약 7~8시간을 작동시켜놓으면 7~8동안 계속 시간을 새로고침함
-수업이 시작되면 30분동안 프로그램을 정지시킴으로서 연산을 줄여 최적화 시킴
'''
import datetime

import time
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


hours = {9:[15,25],10:[5,15],11:[5,15],17:[5,15],26:[0,10],27:[0,15],29:[5,15]}
class_time = { 'class_1':[] ,'class_2':[],'class_3':[],'class_4':[],'class_5':[],'class_6':[],'class_7':[] }

subject = [
'국어링크',#국어 1
'문학a링크', #문학 a 2
'수학링크',          #수학 3
'확통링크',      #확통 4
'영어링크',       #영어 5  
'물리링크',          #물리 6
'화학링크',          #화학 7
'지구과학링크',         #지구과학 8
'',                                                                        #생물(공백) 9
'중국어링크', #중국어 10
'',                                                                          #일본어 11
'체육링크',        #체육 12
'미술링크',   #미술 13
'',                                                                          #음악 14
]

#문학 1,문학a 2,수학 3,확통 4,영어 5,물리 6, 화학 7,지구 8,생물 9,중국 10,일본 11,체육 12,미술 13,음악 14

today_time = ''
treeHit = 0

while treeHit == 0:

    today_time = input(""""              오늘은 몇교시
        숫자로 기입해주세요.
        >>>""")

    
    if '1' <=today_time <='7':
        treeHit = 1
        today_time = int(today_time)
        print('# 1.문학, 2.문학a, 3.수학, 4.확통, 5.영어, 6.물리, 7.화학, 8.지구, 9.생물, 10.중국, 11.일본, 12.체육, 13.미술, 14.음악')    
        for w_time in range(today_time):
            w_time += 1
            class_time['class_{}'.format(w_time)] = input('{}교시 >>'.format(w_time))
            


        
    else:
        print('잘못 입력했습니다.')
#readline.clear_history()
print(class_time)
a = True

while True:
    now = datetime.datetime.now()
    
    for key, value in hours.items():
        if now.minute== key\
            and value[0] <= now.second <= value[1]:

            webbrowser.get(chrome_path).open(subject[int(class_time['class_{}'.format(list(hours.keys()).index(key)+1)][0])-1])
            print('지금은 {}교시 수업중입니다.'.format(list(hours.keys()).index(key)+1))
            time.sleep(30)
           
            a =True
    else:
        if a: 
                print('''수업이 끝났거나 대기중입니다. 
수업이 끝나셨다면 ctrl + c 를 눌러주시면 작동이 멈춥니다.''')
                a = False   