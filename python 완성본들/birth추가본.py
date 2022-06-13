print("정보 기입")
print()
name = input('     이름:')
print("          ex)20040418 형식으로 입력해주세요.")
birth = input('태어난 해:')
cord = input('확인 코드:')
if len(birth) == 8:                                                       #birth 연산
  
  bi_y =birth[0:4]
  bi_m = birth[4:6]
  bi_d = birth[6:]

  bi_yi = int(bi_y)
  
  if 1900 < bi_yi <2100:                                                   #년도 계산     
        if cord == "4148":
            if bi_yi == 2007:
              print('{}님은 특별한 "황금 돼지 띠"입니다.'.format(name))

            else:
                bi_yd = bi_yi % 12
                if bi_yd == 0:
                  print('{}님은 "원숭이 띠" 입니다.'.format(name))
                elif bi_yd == 1: 
                      print('{}님은 "닭 띠" 입니다.'.format(name))
                elif bi_yd == 2:
                    print('{}님은 "개 띠" 입니다.'.format(name))
                elif bi_yd == 4:
                    print('{}님은 "쥐 띠" 입니다.'.format(name))
                elif bi_yd == 5:
                    print('{}님은 "소 띠" 입니다.'.format(name))
                elif bi_yd == 6:
                  print('{}님은 "호랑이 띠" 입니다.'.format(name))
                elif bi_yd == 7:
                  print('{}님은 "토끼 띠" 입니다.'.format(name))
                elif bi_yd == 8:
                    print('{}님은 "용 띠" 입니다.'.format(name))
                elif bi_yd == 9:
                  print('{}님은 "말 띠" 입니다.'.format(name))
                elif bi_yd == 10:
                  print('{}님은 "뱀 띠" 입니다.'.format(name))
                elif bi_yd == 11:
                    print('{}님은 "양 띠" 입니다.'.format(name))
                else:
                  print('{}님은 "돼지 띠" 입니다.'.format(name))
        else:
              print("확인 코드가 잘못되었습니다.")
else:
  print('생년월일을 잘못 입력하셨습니다.')  


