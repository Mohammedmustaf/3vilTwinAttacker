from os import path,popen
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[91m'
ENDC = '\033[0m'
# phpcli
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

def check_dependencies():
    print("[+] checking dependencies...")
    print"============================="
    ettercap = popen("which ettercap").read().split("\n")
    sslstrip = popen("which sslstrip").read().split("\n")
    xterm = popen("which xterm").read().split("\n")
    dhcpd = popen("which dhcpd").read().split("\n")
    lista = [dhcpd[0], "/usr/sbin/airbase-ng", ettercap[0], sslstrip[0],xterm[0]]
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
    print("=============================\n")