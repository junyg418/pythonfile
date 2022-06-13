#줌 하기 귀찮은 내가 만든 프로그램 - 1-5
#1-6 예외처리(40번 줄) 및 버그 수정(class_time에서 10의 자리수 인식못하는 버그)
import datetime, time, webbrowser
import win32api, win32con, win32gui

from typing import Text

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

kakao_opentalk_name = ''
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
hours = {9:[15,25],10:[5,15],11:[5,15],12:[5,15],14:[0,10],15:[0,15],16:[5,15]}
class_time = { 'class_1':[] ,'class_2':[],'class_3':[],'class_4':[],'class_5':[],'class_6':[],'class_7':[] }



subject = ['','링크였던것']
#문학 1,문학a 2,수학 3,확통 4,영어 5,물리 6, 화학 7,지구 8,생물 9,중국 10,일본 11,체육 12,미술 13,음악 14

today_time = ''
treeHit = 0

while treeHit == 0:

    today_time = input("""              오늘은 몇교시
숫자로 기입해주세요.
>""")

    
    if (today_time.isdigit()):
        if 0<=int(today_time):
            treeHit == 1
        today_time = int(today_time)
        treeHit = 1
        print('있다 1 없다 0')    
        for w_time in range(today_time):
            w_time += 1
            class_time['class_{}'.format(w_time)] = input('{}교시 :'.format(w_time))
            


        
    else:
        print('잘못 입력했습니다.')

print(class_time)
a = True
while True:
    now = datetime.datetime.now()
    for key, value in hours.items():
        if now.hour== key\
            and value[0] <= now.minute <= value[1]:
            print('지금은 {}교시 수업중입니다.'.format(list(hours.keys()).index(key)+1))
            webbrowser.get(chrome_path).open(subject[int(class_time['class_{}'.format(list(hours.keys()).index(key)+1)])-1])
            
            kakao_opentalk_name = '이름이였던것'

            
            
            
            
            
            time.sleep(1800)
            a =True
        else:
            if a: 
                    print('''수업이 끝났거나 대기중입니다. 
    수업이 끝나셨다면 ctrl + c 를 눌러주시면 작동이 멈춥니다.''')
                    a = False   