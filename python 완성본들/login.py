import time
acc = {'admin':['admin','admin']}

acc_conplite = 0
reg_complite =0

while True:
    acc_have = input('''        계정이 존재합니까?

    1) 예
    2) 아니오
      >''')


    if acc_have == '1':
            
            while True:
                print('                       로그인')                               #로그인 화면
                id_rg = input('      아이디:')
                ps_rg = input('    비밀번호:')

                if ps_rg == acc[id_rg][0]:
                        time.sleep(1.3)
                        print()
                        print('{}님 환영합니다!'.format(acc[id_rg][1]))                                 #로그인으로 연산
                        print()
                        time.sleep(1.3)
                        acc_conplite = 1
                        break
                        
                

                else:
                    time.sleep(0.5)
                    print('아이디 또는 비밀번호가 잘못됬습니다.')
                    print()

    elif acc_have == '2':
        
        while True:
            print('        회원가입 하시겠습니까?')
            reg_do = input('    1) 예\n    2) 아니오\n       >')            #회원가입 질문
            time.sleep(0.5)
            
            
            if reg_do == '1':
                while True:
                    print('                       회원가입')
                    lee = input('           성:')
                    jun = input('         이름:')
                    
                    print('아이디와 비밀번호는 4글자 이상으로 작성해주세요.')
                    while True:
                        id_reg = input('      아이디:')
                        if len(id_reg) >= 4:
                            id_reg.lower()
                            id_reg.strip()
                            break
                        
                        else:
                            time.sleep(0.3)
                            print()
                            print('아이디를 다시 입력해주십시오.')
                            time.sleep(1)
                            
                    while True:
                        ps_reg = input('     비밀번호:');ps_regc = input('비밀번호 확인:')
                        if len(ps_reg) >= 4\
                            and ps_reg==ps_regc:
                            time.sleep(1.5)
                            print()
                            print('{} {}님 환영합니다!'.format(jun, lee))
                            print()
                            time.sleep(1.2)
                            nick = lee + jun
                            acc[id_reg] = [ps_reg, nick]
                            reg_complite = 1

                            break
                        else:                    
                            time.sleep(1)
                            print()
                            print('비밀번호를 다시 입력해주세요')
                            time.sleep(1)

                    
                        

                  


                        
            elif reg_do == '2':
                break
                                        
            else:
                print("제대로 써라 휴먼.")      #회원가입 하시겠습니까 오류

        if reg_complite == 1:
            break

    else:
        time.sleep(0.5)
        print()
        print("    잘못 입력하셨습니다.")
        print()
        time.sleep(0.5)

    if acc_conplite==1 :
        break
