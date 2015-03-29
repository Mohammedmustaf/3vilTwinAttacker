from PyQt4.QtGui import *
from subprocess import Popen, PIPE
from os import popen
from re import search
import getpass
import threading
class frm_privelege(QDialog):
    def __init__(self, parent = None):
        super(frm_privelege, self).__init__(parent)
        self.setWindowTitle("Privilege Authentication")
        self.Main = QVBoxLayout()
        self.frm = QFormLayout()
        self.setGeometry(0, 0, 400, 100)
        self.center()
        self.Qui()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def Qui(self):
        self.user = QComboBox()
        self.user.addItem(getpass.getuser())
        self.btn_cancel = QPushButton("Cancel")
        self.btn_ok = QPushButton("Ok")
        self.Editpassword = QLineEdit()
        #temporary

        self.Editpassword.setEchoMode(QLineEdit.Password)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.function_ok)
        self.btn_ok.setDefault(True)
        self.frm.addRow("Adminstrator:", self.user)
        self.frm.addRow("Password:", self.Editpassword)
        self.grid = QGridLayout()
        self.grid.addWidget(self.btn_cancel, 1,2)
        self.grid.addWidget(self.btn_ok, 1,3)
        self.Main.addLayout(self.frm)
        self.Main.addLayout(self.grid)
        self.setLayout(self.Main)

    def function_ok(self):
        out = self.password_check(self.Editpassword.text())
        if search("1 incorrect password attemp",out):
            QMessageBox.information(self, "Sudo Password check", "[sudo] password for %s: Sorry, try again."%(getpass.getuser()))
            self.show()
            self.Editpassword.clear()
        else:
            self.close()

    def password_check(self,sudo_password):
        self.hide()
        command = self.thread(sudo_password)
        self.close()
        return command
    def thread(self,sudo_password):
        command = 'python functions.py'.split()
        popen("sudo -k")
        sudo_password = self.Editpassword.text()
        p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
        sudo_prompt = p.communicate(str(sudo_password) + '\n')[1]
        return sudo_prompt      
