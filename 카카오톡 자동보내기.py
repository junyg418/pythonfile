'''
설명 주석
    구글에서 가져왔었던 파이썬 자동보내기 코드
    이를 분석하고 zoomdon't 프로젝트에 추가하려 코드를 작성했음
    초기자료
    Update and rename test_2.py to 카카오톡 자동보내기.py
'''

from typing import Text
import win32api, win32con, win32gui, time

kakao_opentalk_name = '***'

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

text = '어머니'
kakao_sendtext(text)
