Title: Mon top 23 d'application de recherche en vulnérabilité informatique
Date: 2022-11-28 08:04
Category:Linux
Tags: hacking, blackarch
Authors: Anthony Le Goff
Summary:

Prétendre à devenir un hacker vous devez connaître une base d'outils et savoir les utiliser par la suite. Mon TOP 23 personnel:


* Exploration réseau et audit de sécurité: [nmap](https://nmap.org/)
* Collection de classe Python pour travailler avec les protocoles réseaux: [impacket](https://www.secureauth.com/labs/open-source-tools/impacket/)
* Outil d'analyse de protocoles réseaux: [wireshark](https://www.wireshark.org/)
* Capturer et analyser les packets sur le réseau: [tcpdump](https://www.tcpdump.org/)
* Outil de récupération de mot de passe: [hashcat](https://hashcat.net/hashcat/)
* Sécurité audit de mot de passe: [john](https://www.openwall.com/john/)
* Surfer anonymement via TOR ou un serveur proxy: [proxychains-ng](https://proxychains.sourceforge.net/)
* Base de donnée d'exploits [exploitdb](https://www.exploit-db.com/)
* Client HTTP CLI [httpie](https://httpie.io/)
* Framework d'audit de sécurité, développement d'exploits: [metasploit](https://www.metasploit.com/)
* Front-end GUI pour metasploit, aide à l'utilisation [armitage](https://www.offensive-security.com/metasploit-unleashed/armitage/)
* Bind outil d'administration DNS: [bind-tools]()
* Framework de retro-ingénierie et analyse de fichier binaire r2: [radare2](https://rada.re/n/radare2.html)
* Automatisation détection et exploitation injection SQL: [sqlmap](https://sqlmap.org/)
* Wordpress security scanner: [wpscan](https://wpscan.com/)
* Outil de copy/coller clipboard en CLI: [xclip]()
* Navigateur exploitation framework: [beef](https://beefproject.com/)
* Outils d'ingénierie sociale: [set](https://github.com/trustedsec/social-engineer-toolkit)
* DDoS service botnet outils: [ufonet](https://ufonet.03c8.net/)
* Traffic capture implementation d'attaque de type man-in-the-middle: [ettercap](https://www.ettercap-project.org/index.html)
* Web Application Attack and Audit Framework: [w3af](http://w3af.org/)
* Vulnerability Assessment Scanner: [openvas](https://www.openvas.org/)
* Command and control server et agent post-exploitation HTTP/2: [Merlin](https://github.com/Ne0nd0g/merlin)

### Installation Arch

Installation de dépot BlackArch >> [https://blackarch.org/](https://blackarch.org/)
```
curl -O https://blackarch.org/strap.sh
sha1sum strap.sh # doit etre egal a d062038042c5f141755ea39dbd615e6ff9e23121
sudo chmod +x strap.sh
sudo ./ strap.sh
```

```
sudo pacman -S blackman
```

Installation des outils basics
```
sudo blackman -i nmap impacket whireshark tcpdump ruby hashcat john proxychains-ng exploitdb httpie metasploit armitage bind-tools radare2 sqlmap wpscan xclip beef set ufonet openvas ettercap w3af merlin-server
```
