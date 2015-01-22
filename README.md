# 3vilTiwnAttacker
This tool create an rogue Wi-Fi access point , purporting to provide wireless Internet services, but snooping on the traffic.

---

## Video Demo

[![Video Demo](http://img.youtube.com/vi/Jrb43KVPIJw/0.jpg)](http://www.youtube.com/watch?v=Jrb43KVPIJw)

---

### Software dependencies:

* Recommended to use Kali linux.
* Ettercap.
* Sslstrip.
* Airbase-ng include in aircrack-ng.
* DHCP.

#### [install DHCP in  Debian-based]

##### Ubuntu

```sh
$ sudo apt-get install isc-dhcp-server
```

##### Kali linux

```sh
$ echo "deb http://ftp.de.debian.org/debian wheezy main " >> /etc/apt/sources.list
$ apt-get update && apt-get install isc-dhcp-server
```

#### [install DHCP in  redhat-based]

##### Fedora

```sh
$ sudo yum install dhcp
```
---

### Tools Options:

![Tools Options](https://dl.dropboxusercontent.com/u/97321327/evil/evil2.png)

**Etter.dns:** Edit etter.dns to loading module dns spoof.


**Dns Spoof:** Start dns spoof attack in interface ath0 fake AP.


**Ettercap:** Start ettercap attack in host connected AP fake Capturing login credentials.


**Sslstrip:** The sslstrip listen the traffic on port 10000.


**Driftnet:** The driftnet sniffs and decodes any JPEG TCP sessions, then displays in  an window.


---

The MIT License (MIT)

Copyright (c) 2014 P0cL4bs Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
