from PyQt4.QtGui import *
from PyQt4.QtCore import *
class frm_Update(QDialog):
    def __init__(self, parent = None):
        super(frm_Update, self).__init__(parent)
        self.setWindowTitle("Update Center")
        self.Main = QVBoxLayout()
        self.frm = QFormLayout()
        self.setGeometry(0, 0, 200, 100)
        self.center()
        sshFile="Core/dark_style.css"
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())
        self.Qui_update()
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def Qui_update(self):
        self.setLayout(self.Main)