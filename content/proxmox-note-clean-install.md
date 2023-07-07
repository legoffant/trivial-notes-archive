Title:Note clean install Proxmox VE 8
Date: 2023-07-07 18:54
Category:Linux
Tags:proxmox
Authors: Anthony Le Goff
Summary:

J'ai relancer l'installation de mon serveur Proxmox pour une clean install et configurer la nouvelle carte graphique. Voila ma prise de note, et configuration de base post-installation.

**Documentation**: 

* The Debian Administrator's Handbook [https://debian-handbook.info/browse/stable/](https://debian-handbook.info/browse/stable/)
*  Proxmox VE Documentation Index  [https://pve.proxmox.com/pve-docs-7/](https://pve.proxmox.com/pve-docs-7/)

Créer une clé USB bootable de Proxmox 8 VE. 
sous linux en CLI:

###INSTALL

check la partition clé USB
```
$ sudo fdisk -l
```

Formatage de la clé USB avec l'iso
```
$ sudo dd if=proxmox-ve_8.0-2.iso of=/dev/sdb bs=4M status=progress && sync
```

BIOS AsRock Configuration:

* *Advanced -> CPU Configuration -> SVM Mode: enabled*
* *Advanced -> AMD CBS -> NBIO Common Options -> IOMMU enabled*

Activer  GPU Passthrough sur  Proxmox 8
[https://asded.gitlab.io/post/2023-07-01-pci-passthrough-proxmox-04/](https://asded.gitlab.io/post/2023-07-01-pci-passthrough-proxmox-04/)

### MISE A JOUR

Desactivation dans mise à jour du depot entreprise et ceph
```text
$ nano /etc/apt/sources.list.d/pve-no-enterprise.list

# not for production use
deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription

$ apt-get update && apt-get dist-upgrade
$ reboot now
```

### CREER UN UTILISATEUR
```
$ useradd -g users -d /home/toto -m -s /bin/bash toto
$ passwd toto
```
Droit sudo
```
$ apt-get install sudo
$ usermod -aG sudo toto
```

### SECURITY 

Les ports ouverts par défauts sont 22(SSH), 111(rpcbind), 3128(squid-http)

Sécuriser SSH
```text
$  nano  /etc/ssh/sshd_config

Port 2222                  # Changer le port par défaut (à retenir!)
PermitRootLogin no         # Ne pas permettre de login en root
AllowUsers toto            # N'autoriser qu'un utilisateur précis

$  /etc/init.d/ssh restart
```

Installation de fail2ban, protection contre les brutes-forces
```text
$ apt install fail2ban
$ sudo systemctl enable fail2ban
$ sudo nano /etc/fail2ban/jail.local
```
Change the variables bantime (the number of seconds the attacker will be blocked for) and maxretry (the number of attempts to enter the login / password) for each individual service.
```text
mta = mail
destemail = test@gmail.com
sender = fail2ban@srv01.com
ignoreip = 127.0.0.1/8 ::1

[sshd]
enabled = true
port = ssh, sftp,2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
findtime = 300
bantime = 3600

[proxmox]
enabled = true
port = https,http,8006
filter = proxmox
logpath = /var/log/daemon.log
maxretry = 5
bantime = 3600
```
Créer le fichier /etc/fail2ban/filter.d/proxmox.conf :
```text
[Definition]
failregex = pvedaemon\[.*authentication failure; rhost=<HOST> user=.* msg=.*
ignoreregex =
```

```
$ sudo systemctl restart fail2ban
```

check status
```
$ fail2ban-client -v status sshd
$ fail2ban-client -v status proxmox
```

Portsentry, une solution pour se protéger des scans de ports: [https://www.geeek.org/portsentry-linux-securite/](https://www.geeek.org/portsentry-linux-securite/)

Rkhunter
```
$ apt-get install rkhunter
```

Indiquer l'adresse de notification et l'execution journaliere
```text
$  nano /etc/default/rkhunter

REPORT_EMAIL="monitoring@test.com"
CRON_DAILY_RUN="yes"
```

En cas de fausses détections positives sur des répertoires ou fichiers existants et sains, éditez /etc/rkhunter.conf pour les ajouter à la liste des éléments autorisés.
Ex:
```
ALLOWHIDDENDIR=/dev/.udev
ALLOWHIDDENDIR=/dev/.static
```

Installer automatiquement les mises à jour de sécurité de Debian
[https://www.noobunbox.net/serveur/securite/installer-automatiquement-les-mises-jour-de-securite-sous-debian](https://www.noobunbox.net/serveur/securite/installer-automatiquement-les-mises-jour-de-securite-sous-debian)

Debsecan – Trouvez les paquets vulnérables CVE de votre distribution Linux
```
$ apt install debsecan
```
Scan et list en detail
```
$ debsecan --suite bookworm --format detail
```
Mettre à jour le système avec les derniers paquets corrigés. Pour cela, commencez par lister les paquets concernés avec le paramètre « –format packages »
```
$ debsecan --suite bookworm --only-fixed --format packages
```

Puis installation avec apt
```
$ apt install $(debsecan --suite buster --only-fixed --format packages)
```

### FIREWALL 

Activer le par-feu intégré à Proxmox VE
[https://artheodoc.files.wordpress.com/2023/03/le_pare-feu_integre_de_proxmox.pdf](https://artheodoc.files.wordpress.com/2023/03/le_pare-feu_integre_de_proxmox.pdf)

### BACKUP

Configurer Rclone vzbackup
[https://github.com/TheRealAlexV/proxmox-vzbackup-rclone](https://github.com/TheRealAlexV/proxmox-vzbackup-rclone)

* Tarification AWS S3 200GO  0,023 USD par Go 4,6$/month
* Tarification GDrive 200GO 2,99 €/month

Object Storage Price Comparison [https://www.qualeed.com/en/qbackup/cloud-storage-comparison/](https://www.qualeed.com/en/qbackup/cloud-storage-comparison/)

**RAPPEL**: Il faut 3 copies de sauvegarde

1. Sur le serveur, snapshot LOCAL
2. Sur un HDD Externe, NAS sur le routeur en USB LOCAL
3. Dans le Cloud, DISTANT

### INSTALL ISO IMAGE

Comment télécharger des images ISO pour créer les VM
[https://unixcop.com/upload-iso-image-proxmox-server/](https://unixcop.com/upload-iso-image-proxmox-server/)

Liste ISO:

* Debian netinstall [https://www.debian.org/CD/netinst/](https://www.debian.org/CD/netinst/)
* Ubuntu server [https://ubuntu.com/download/server](https://ubuntu.com/download/server)
* Arch Linux [https://archlinux.org/download/](https://archlinux.org/download/)
* Gentoo minimal Install [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/)
* Fedora server [https://fedoraproject.org/server/download/](https://fedoraproject.org/server/download/)
* Windows 10 22H2 pro (torrent) [https://1337x.to/search/Windows+10+22H2/1/](https://1337x.to/search/Windows+10+22H2/1/)
* Windows 11 [https://www.microsoft.com/en-us/software-download/windows11?9d47a9e1-e53b-49a1-92ca-a647d62dc410=True](https://www.microsoft.com/en-us/software-download/windows11?9d47a9e1-e53b-49a1-92ca-a647d62dc410=True)
* WinLSD 3.5 (french) [https://archive.org/details/winlsd.3.5](https://archive.org/details/winlsd.3.5)
* Win 7 AIO SP1 [https://gofile.io/d/bXFzYx](https://gofile.io/d/bXFzYx)
* Windows NT 4.0 Server [https://isoriver.com/windows-nt-4-0-iso-download/](https://isoriver.com/windows-nt-4-0-iso-download/)
* Kali net installer [https://www.kali.org/get-kali/#kali-installer-images](https://www.kali.org/get-kali/#kali-installer-images)
* openBSD (high sec server) [https://www.openbsd.org/faq/faq4.html#Download](https://www.openbsd.org/faq/faq4.html#Download)
* TrueNAS CORE [https://www.truenas.com/download-truenas-core/](https://www.truenas.com/download-truenas-core/)
* YunoHost [https://yunohost.org/fr/install/hardware:regular](https://yunohost.org/fr/install/hardware:regular)
* Freedom Box [https://freedombox.org/download/amd64/](https://freedombox.org/download/amd64/)
* FreeBSD 13.1 bootonly [https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.1/](https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.1/)
* macOS collection (torrent) [https://archive.org/download/macos-collection](https://archive.org/download/macos-collection)
* Ubuntu 8.04LTS [https://old-releases.ubuntu.com/releases/8.04.0/](https://old-releases.ubuntu.com/releases/8.04.0/)


### WEB SERVER ALL-IN-ONE

sandstorm.io
```
$ curl https://install.sandstorm.io | bash
```


### CONFIGURER DOCKER

How to Install Docker With Portainer Inside an LXC Container On Proxmox 
[https://apacheiot.org/docker/how-to-install-docker-portainer-lxc-container-proxmox/](https://apacheiot.org/docker/how-to-install-docker-portainer-lxc-container-proxmox/)

### PROVISIONNING

* VM Cloud Gaming 6 coeurs - RAM 16GO - HDD 64GO
* VM server VPS 4 coeurs - RAM 4GO - HDD 32GO à 128GO
* Container - 2 coeurs - RAM 2GO - HDD 32GO
