'''
설명주석
    전국 동아리 소프트웨어 경진대회 출전 당시
    GUI를 제작하기 위한 PyQt5 모듈 공부 겸
    여러코드를 제작하고 지우고 반복하는 파일로 사용됨
    초기 자료
'''
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

class StartDialog(QtGui.QDialog, QtCore.QObject): 
    new_start_signal = QtCore.pyqtSignal() 
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent) 
        QtCore.QObject.__init__(self) 
        self.setupUi(parent) 
        self.new_button.clicked.connect(self.new_button_clicked) 
        
    def new_button_clicked(self): 
        self.new_start_signal.emit() 

app = QtGui.QApplication(sys.argv) 
start_dialog = StartDialog()



if __name__ == '__main__':
    app.show()
    sys.exit(app.exec_())
