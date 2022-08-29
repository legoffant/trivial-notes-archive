Title: Créer un site web statique sécurisé sous Nginx
Date: 2022-08-28 01:07
Category:Linux
Tags:sysadmin, ingénierie, nginx
Authors: Anthony Le Goff
Summary:

Mon retour d'expérience pour créer un site web simple avec une page statique. Je vais expliquer la construction en moins de 3 heures de [https://qasari.net](https://qasari.net) en apprenant à gérer son propre serveur chez un hébergeur.

### Configuration de base

* Hébergeur: [OVH](https://www.ovhcloud.com/fr/) 
* Type de serveur: VPS(Virtual Private Server) - 1vcore, 2 Go, 40 Go SSD
* OS configuré: Linux Debian 11

Nota: Nom de domaine qasari.net également chez OVH fournisseur français.

Vous pouvez choisir un autre hébergeur tel que Ionos ou infomaniak en Suisse. De l'auto-hébergement sur un Raspberry Pi est possible.

### Première connexion au VPS

Vous allez recevoir à votre achat de VPS via email les identifiants pour une connexion à distance via SSH. Vous avez besoin de l'adresse IPv4 et de l'identifiant avec un mot de passe provisoire.

Depuis un terminal(natif sous UNIX-like) connecter vous au serveur:
```
ssh root@23.2.34.7
```

Dans cette exemple on ce connecte en root sur l'IP 23.2.34.7. Votre mot de passe sera demandé une fois la connexion établie. L'identifiant, ici root peu changer.

Bien maintenant installons le serveur. Une fois sur le serveur votre prompt change avec le nom de celui-ci et un message d'accueil, le MOTD.

### Installation du serveur

Vérifier et installer que vous avez un éditeur de texte ainsi que la completion pour bash:
```
$ apt install nano vim bash-completion
```

Configurer l'hosts réseau en fonction de votre nom de domaine:
```
$ nano /etc/hosts

127.0.0.1       localhost.qasari.net   localhost
37.187.181.161  qasari.net     qasari

# Ligne désirée si en configuration IPv6
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

Changer le nom du serveur:
```
$ nano /etc/hostname

qasari
```

Relancer le serveur pour que la configuration prenne effet puis reconnecter vous en ssh:
```
$ reboot
```

Vérifier si le nom du serveur est correct:
```
$ hostname
$ hostname -f
```

Mettre à jour le système avec les sources des paquets. Ajoutez contrib non-free:
```
$ nano /etc/apt/sources.list 

deb http://deb.debian.org/debian bullseye main contrib non-free
deb-src http://deb.debian.org/debian bullseye main contrib non-free

deb http://deb.debian.org/debian-security bullseye/updates main contrib non-free
deb-src http://deb.debian.org/debian-security bullseye/updates main contrib non-free

deb http://deb.debian.org/debian bullseye-updates main contrib non-free
deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free
```

Mise à jour du système:
```
sudo apt-get update && apt-get upgrade
```

