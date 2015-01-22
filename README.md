# 3vilTiwnAttacker
this tool create an rogue Wi-Fi access point , purporting to provide wireless Internet services, but snooping on the traffic.
<img  src="https://dl.dropboxusercontent.com/u/97321327/evil/evil.png"> 
------------------------------------------------------
<h5>Video Demo: Link</h5>
<h3>Software dependencies:</h3>
------------------------------------------------------
<ul>
<li>recommended to use Kali linux</li>
<li>ettercap</li>
<li>sslstrip</li>
<li>airbase-ng include in aircrack-ng</li>
<li>dhpcd</li>
</ul>
<h5>[install dhpcd in  Ubuntu]</h5>
~#sudo apt-get install isc-dhcp-server<br>
<h5>[install dhpcd in Kali linux]</h5>
<p>~# echo "deb http://ftp.de.debian.org/debian wheezy main " >> /etc/apt/sources.list</p>
<p>~# apt-get update && apt-get install isc-dhcp-server</p>
------------------------------------------------------
<h4>Tools Options:</h4>
<img src="https://dl.dropboxusercontent.com/u/97321327/evil/evil2.png"> 
<p><b>Etter.dns:</b> edit etter.dns to loading module dns spoof.</p>
<p><b>Dns Spoof: start dns spoof attack in interface ath0 fake AP.</b></p>
<p><b>Ettercap:</b> start ettercap attack in host connected AP fake Capturing login credentials.</p>
<p><b>Sslstrip:</b> the sslstrip listen the traffic on port 10000. </p>
<p><b>Driftnet:</b> the driftnet sniffs and decodes any JPEG TCP sessions, then displays in  an window.</p>
-------------------------------------------------------
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
