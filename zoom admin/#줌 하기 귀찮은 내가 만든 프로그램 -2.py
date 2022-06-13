#줌 하기 귀찮은 내가 만든 프로그램 -2
from selenium import webdriver
from selenium.webdriver.common.key import Keys
from selenium.webdriver.common.action_chains import Action_Chains

driver = webdriver.Chrom()

import time


from datetime import datetime
now_time = datetime.now().strftime("%H:%M")

korean = '국어링크'#국어
korean_a = '문학링크' #문학 a
math = '수학링크'          #수학
hacktong = '확통링크'      #확통
english = '영어링크'       #영어   
muli = '물리링크'          #물리
atom = '화학링크'          #화학
eirth = '지구링크'         #지구과학
sengmul = ''                                                                        #생물(공백)
china = '중국어링크' #중국어
japen = ''                                                                          #일본어
health = '체육링크'        #체육
art = '미술링크'   #미술
music = ''                                                                          #음악


class_time = { 'class_1':['9:15'] ,'class_2':['10:05'],'class_3':['11:05'],'class_4':['12:05'],'class_5':['2:00'],'class_6':['3:00'],'class_7':['4:15'] }




today_time = ''

while True:

        today_time = input(""""              오늘은 몇교시
        1) 6교시
        2) 7교시
        >>>""")


        if today_time == '1':
                print('             6교시 선택')
                print('오늘의 시간표를 입력하세요')
                class_time['class_1'] = input('1교시:')
                class_time['class_2'] = input('2교시:')
                class_time['class_3'] = input('3교시:')
                class_time['class_4'] = input('4교시:')
                class_time['class_5'] = input('5교시:')
                class_time['class_6'] = input('6교시:')                    
                print()
                print(now_time)
                if class_time['class_1'][0] == now_time:
                    driver.get(class_time['class_1'][1])



               
               
               
               
               
                break

        elif today_time == '2':
            print('7교시 선택')
            break
            class_time = class_time[:]
                

        else:
            print('제대로 써라 휴먼.')
    
        
        