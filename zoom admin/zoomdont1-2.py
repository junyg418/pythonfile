#줌 하기 귀찮은 내가 만든 프로그램 - 1-2
import datetime

import time
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'



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
        print('#문학 1,문학a 2,수학 3,확통 4,영어 5,물리 6, 화학 7,지구 8,생물 9,중국 10,일본 11,체육 12,미술 13,음악 14')    
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
     
    if now.hour == 9\
        and 20 <= now.minute <=25:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_1'][0])-1])
            print('지금은 1교시 수업중입니다.')
            time.sleep(1800)

    elif now.hour == 10\
        and 5 <=now.minute <= 15\
            and 2<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_2'][0])-1])
            print('지금은 2교시 수업중입니다.')
            time.sleep(1800)
    
    elif now.hour == 11\
        and 5 <=now.minute <= 15\
            and 3<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_3'][0])-1])
            print('지금은 3교시 수업중입니다.')
            time.sleep(1800)

    elif now.hour == 12\
        and 5<= now.minute <= 15\
            and 4<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_4'][0])-1])
            print('지금은 4교시 수업중입니다.')
            time.sleep(1800)

    elif now.hour == 14\
        and 0 <= now.minute <= 5\
            and 5<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_5'][0])-1])
            print('지금은 5교시 수업중입니다.')
            time.sleep(1800)

    elif now.hour == 15\
        and 0<=now.minute <= 5\
            and 6<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_6'][0])-1])
            print('지금은 6교시 수업중입니다.')
            time.sleep(1800)

    elif now.hour == 16\
        and 5 <= now.minute <= 15\
            and 7<=today_time:
            webbrowser.get(chrome_path).open(subject[int(class_time['class_7'][0])-1])
            print('지금은 7교시 수업중입니다.')
            time.sleep(1800)
    
    else:
        if a: 
            print('''수업이 끝났거나 대기중입니다. 
수업이 끝나셨다면 ctrl + c 를 눌러주시면 작동이 멈춥니다.''')
            a = False