import time
import datetime

alarm = {}

while treeHit == 0:
    print('''      시간을 입력해주세요.''')
    int(set_hour) = input('시간\n>')
    int(set_minute) = input('시간\n>')
    if 0<= set_hour <=24\
        and 0<= set_minute <=24:
            treeHit==1
            alarm[set_hour] = set_minute
            if 0<=set_hour <=12:
                am = '오전'
            elif 13<= set_hour <= 24:
                am = '오후'
            print('설정하신 알람은')
            print('{} {}시 {}분 입니다.'.format(am,set_hour,set_minute))
    else:
        print('다시 입력해주세요.')

while True:
    datetime.datetime.now()
    