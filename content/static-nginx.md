Title:Note d'installation sécurisée d'un site statique Nginx
Date: 2023-07-08 11:23
Category:Linux
Tags:nginx
Authors: Anthony Le Goff
Summary:

Ma propre configuration pour déployer un site statique tel que [https://qasari.net](https://qasari.net)

Configuration:

* OS: Debian 11
* Auto-update security
* Web server: Nginx
* par-feu: ufw
* securité: fail2ban, rkhunter, clé RSA SSH Only-Login, logwatch
* SSL Enable avec Let's Encrypt auto-renew
* Template: Simple.css


Create a static website on Nginx:

* [https://jgefroh.medium.com/a-guide-to-using-nginx-for-static-websites-d96a9d034940](https://jgefroh.medium.com/a-guide-to-using-nginx-for-static-websites-d96a9d034940)

Proteger son serveur VPS:

* [https://www.remipoignon.fr/securiser-son-serveur-linux/](https://www.remipoignon.fr/securiser-son-serveur-linux/)

Static site template:

* Simple.css [https://github.com/kevquirk/simple.css](https://github.com/kevquirk/simple.css)

Liste pour utiliser un générateur de site statique (blog, docs, etc...):

* [https://jamstack.org/generators/](https://jamstack.org/generators/)

Partage de fichier à la racine (index) du web server comme repository:

* Apaxy: [https://oupala.github.io/apaxy/](https://oupala.github.io/apaxy/)
* h5ai: [https://larsjung.de/h5ai/](https://larsjung.de/h5ai/)
* Directory Lister: [https://www.directorylister.com/](https://www.directorylister.com/)

NOTA: Hacker web design style Brutalist:

* What Is Brutalism in Web Design? [https://elementor.com/blog/brutalism-in-web-design/](https://elementor.com/blog/brutalism-in-web-design/)

--------------------
**LIST COMMAND ON SERVER** 

Install editor text & bash completion:
```
$ apt install sudo nano vim bash-completion
```

Configure the hostname:
```text
$ nano /etc/hosts

127.0.0.1       localhost.qasari.net   localhost
37.187.181.111  qasari.net     qasari
```

The following lines are desirable for IPv6 capable hosts
```text
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

Edit hostname:
```
$ nano /etc/hostname

qasari
```

```
$ reboot now
```

Check if hostname is correct:
```
$ hostname
$ hostname -f
```

Update debian installation:
```text
$ nano /etc/apt/sources.list 

# enable contrib non-free

deb http://deb.debian.org/debian bullseye main contrib non-free
deb-src http://deb.debian.org/debian bullseye main contrib non-free

deb http://deb.debian.org/debian-security bullseye/updates main contrib non-free
deb-src http://deb.debian.org/debian-security bullseye/updates main contrib non-free

deb http://deb.debian.org/debian bullseye-updates main contrib non-free
deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free
```

```
$ sudo apt-get update && apt-get upgrade
```

Synchro the system clock:
```
$ apt install ntp
$ timedatectl set-ntp true
```

Ajout d'une utilisateur:
```
$ sudo adduser toto
$ sudo usermod -a -G sudo toto
$ su toto
$ passwd
```

Enlever un utilisateur:
```
$ sudo deluser debian
```

**IMPORTANT NOTE DE SECURITY**

Utiliser un clé SSH sur pour l'authentification sur le serveur: [https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-debian-11](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-debian-11)

Generate paire de clé RSA 4046
```
$ ssh-keygen -b 4096
```
copy la clé public sur le serveur distant
```text
$ ssh-copy-id toto@37.187.181.111
```

Configuration de SSH:
```text
$ nano /etc/ssh/sshd_config

port 2382
PermitRootLogin no
PasswordAuthentication no
```

```
$ reboot now
```

On ce reconnecte via la clé SSH
```text
$ ssh -p 2382 toto@37.187.181.111
```

Configurer le firewall:

setup ufw:

* [https://linuxconfig.org/ubuntu-20-04-open-http-port-80-and-https-port-443-with-ufw](https://linuxconfig.org/ubuntu-20-04-open-http-port-80-and-https-port-443-with-ufw)

```
$ sudo apt install ufw

$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing

$ sudo ufw allow 2380
$ sudo ufw allow http
$ sudo ufw allow https

$ sudo ufw enable
$ sudo ufw status
```

Configurer fail2ban:
```
$ sudo apt install fail2ban
```

```
$ sudo cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local
$ sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

```text
$ sudo nano /etc/fail2ban/jail.local

[sshd]
enabled = true
port = 2382
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
findtime = 300
bantime = 3600
ignoreip = 127.0.0.1
destemail = test@gmail.com
```


Depuis une dernière version de fail2ban, pour recevoir les mails de notification, il faut indiquer votre mail dans les fichiers :
```
	/etc/fail2ban/action.d/sendmail-common.conf
	/etc/fail2ban/action.d/mail.conf
	/etc/fail2ban/action.d/mail-whois.conf
```

```
$ sudo systemctl enable fail2ban
$ sudo systemctl start fail2ban
```

```
$ sudo fail2ban-client status
```

Configure Rkhunter:
```
$ sudo apt install rkhunter
```

```text
$ sudo nano /etc/default/rkhunter

# Pour effectuer une vérification chaque jour
CRON_DAILY_RUN="yes"
REPORT_EMAIL="test@gmail.com"
```

Open /etc/rkhunter.conf. Uncomment (remove the # to the left) and change the following three variables:
```text
MIRRORS_MODE=1 ---> MIRRORS_MODE=0

UPDATE_MIRRORS=0 ---> UPDATE_MIRRORS=1

WEB_CMD="/bin/false" ---> WEB_CMD=""
```

Confirm config file:
```
sudo rkhunter -C
```

Update database:
```
$ sudo rkhunter --update
```
Check the local system:
```
$ sudo rkhunter --check
```

Configure logwatch:
```
$ sudo apt install logwatch
$ nano /usr/share/logwatch/default.conf/logwatch.conf
MailTo = test@gmail.com
```

```
$ sudo logwatch status
```

test manuellement:
```
$ sudo logwatch --detail Low --mailto email@address --service http --range today
```

Configurer les mises à jours de sécurité automatique:
```
$ sudo apt install unattended-upgrades
```

```
$ sudo systemctl enable unattended-upgrades
$ sudo systemctl start unattended-upgrades
```

Configuration file:
```
$ sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

In our example, remove // from the “security” line if it’s there, "origin=Debian,codename=${distro_codename},label=Debian-Security";

Enabling automatic upgrades:
```text
$ sudo nano /etc/apt/apt.conf.d/20auto-upgrades

APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
APT::Periodic::AutocleanInterval "7";
```

Testing the configuration:

```
$ sudo unattended-upgrades --dry-run --debug
```
Installer Nginx:
```
$ sudo apt install nginx
$ mkdir /var/www/qasari.net
```

Transférer vos fichiers local vers le serveur:
```text
$  scp -P 2382 -r ~/qasari.net/* toto@37.187.181.111:/var/www/qasari.net
```

Ne pas oublier de changer le détenteur du groupe:
```
$ sudo chown -R $USER:$USER /var/www
```


Configure Nginx to serve the website
```text

$ sudo nano /etc/nginx/sites-available/qasari.net
server {
	listen 80 default_server;
	listen [::]:80 default_server;  

	root /var/www/qasari.net;  
	index index.html;  
	
	server_name qasari.net www.qasari.net;  
	location / {
		try_files $uri $uri/ =404;
		}
}

```
Link site enable:
```
$ ln -s /etc/nginx/sites-available/qasari.net /etc/nginx/sites-enabled/qasari.net
```

```
$ sudo systemctl restart nginx
```


Configuration SSL avec let's encrypt:
```
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python3-certbot-nginx
$ sudo certbot --nginx certonly
```

Enable auto-renewal for certificates:
```text

$ sudo crontab -e

17 7 * * * certbot renew --post-hook "systemctl reload nginx"
```

Tell Nginx use SSL for website inside server conf file:

```text
server {
   listen 443 default_server;
   listen [::]:443 default_server;
   #... all other content


   # ...previous content here
   ssl on;
   ssl_certificate /etc/letsencrypt/live/qasari.net/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/qasari.net/privkey.pem;
}
```

Restart web server et reboot:
```
$ sudo systemctl restart nginx
$ reboot now
```
