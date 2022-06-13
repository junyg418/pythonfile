#줌 하기 귀찮은 내가 만든 프로그램 -1
import datetime
from urllib import request
now = datetime.datetime.now()

class_time = { 'class_1':[] ,'class_2':[],'class_3':[],'class_4':[],'class_5':[],'class_6':[],'class_7':[] }


문학=korean = '국어링크'#국어
문학a=korean_a = '문학링크' #문학 a
수학=math = '수학링크'          #수학
확통=hacktong = '확통링크'      #확통
영어=english = '영어링크'       #영어   
물리=muli = '물리링크'          #물리
화학=atom = '화학링크'          #화학
지구=eirth = '지구링크'         #지구과학
생물=sengmul = ''                                                                        #생물(공백)
중국=china = '중국어링크' #중국어
일본=japen = ''                                                                          #일본어
체육=health = '체육링크'        #체육
미술=art = '미술링크'   #미술
음악=music = ''                                                                          #음악

#문학,문학a,수학,확통,영어,물리,화학,지구,생물,중국,일본,체육,미술,음악

today_time = ''

while True:

        today_time = input(""""              오늘은 몇교시
        1) 6교시
        2) 7교시
        >>>""")


        if today_time == '1':
                print('      6교시 선택')
                print('오늘의 시간표를 입력하세요')
                print('#문학,문학a,수학,확통,영어,물리,화학,지구,생물,중국,일본,체육,미술,음악 과 같이 기입해주세요.')
                class_time['class_1'] = input('1교시:')
                class_time['class_2'] = input('2교시:')
                class_time['class_3'] = input('3교시:')
                class_time['class_4'] = input('4교시:')
                class_time['class_5'] = input('5교시:')
                class_time['class_6'] = input('6교시:')                    
                
                break

        elif today_time == '2':
            print('7교시 선택')
            break
            class_time = class_time[:]
                

        else:
            print('제대로 써라 휴먼.')
    
        
        