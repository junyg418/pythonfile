print('                       계정 만들기')
lee = input('          성:')
jun = input('        이름:')
id_reg = input('      아이디:')
ps_reg = input('    비밀번호:');ps_regc = input('비밀번호 확인:')
if ps_reg == ps_regc:
   print('{} {}님 환영합니다!'.format(jun, lee))
   acc[id_reg] = [ps_reg, lee + jun]




