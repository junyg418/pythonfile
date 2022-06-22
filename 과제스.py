# import time
# while True:
#     약물단위 = input('뭐시기 중 하나입력:')
#     약물이름 = input('약물이름 입력:')
#     if 약물단위 == 'ample':
#         약물의총량 = int(input('약물의총량(cc):'))
#         처방난양 = float(input('처방난양(ample):'))
#         if 처방난양 >1:
#             print('처방난양의 범위가 초과되었음.')
#             time.sleep(1.5)
#             continue
#         else:
#             ample약물주입량 = 약물의총량 * 처방난양
#             print(f'd양물의 총주입량={약물이름},{ample약물주입량}cc')
#             break
#     elif 약물단위 == 'vial':
#         약물의총량 = int(input('약물의총량(cc):'))
#         처방난양 = float(input('처방난양(vial):'))
#         if 처방난양 > 1:
#             print('처방난양의 범위가 초과되었음.')
#             time.sleep(1.5)
#             continue
#         else:
#             vial약물의주입량 = 약물의총량 * 처방난양
#             print(f'약물의총주입량{약물이름}{vial약물의주입량}')
#             break
#     else:
#         print('약물의 이름이 잘못되어있습니다.')
#         time.sleep(1.5)
#-------------------------------------------------------------------------------------
# def sum_All(*values):
#     output=[]
#     for value in values:
#         for idx, i in enumerate(value):
#             try:
#                 output[idx] += i
#             except:
#                 output.append(i)            
#     return output

# b = sum_All([1,2,3],[4,5,6])

# print('b :', b)
#-------------------------------------------------------------------------------------

# # for val in ['a','b','c','d','e']:
#     df.loc[df[val]%3==0, val] = 'X'