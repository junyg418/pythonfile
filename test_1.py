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
