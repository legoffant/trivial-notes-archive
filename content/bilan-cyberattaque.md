Title:Bilan cyberattaque 22/07/2023
Date: 2023-07-26 06:44
Category:Inclassable
Tags:cyberattaque
Authors: Anthony Le Goff
Summary:

Je viens de subir une cyberattaque sur mon Laptop Thinkpad. Ce qui a donné la destruction de 150GB de data. L'attaque est relativement sophistiqué car je suis sous Arch Linux (mon Laptop c'est un tank) et que mon réseau local n'a pas de port ouvert sur l'extérieur normalement.... Seulement UPNP actif pour la redirection de port.

Je suis allez signaler sur le forum Arch Linux, dont les utilisateurs étaient sceptique, car c'est très rare qu'un utilisateur d'Arch Linux en individuel sur un réseau local domestique soit attaqué. *J'ai gagné un trophée....* En gros t'es qui toi pour être une cible?

La procédure quand j'ai vu la cyberattaque est la mise en quarantaine de mon serveur NAS et sauvegarde, isoler du réseau local. Puis monitoring et analyses de logs. Et j'ai donc trouver des squatteurs qui ont ouvert des ports. 

J'ai signalé au FAI Bouygues Telecom sur la hotline, qui n'a rien vu d'anormal. Pourtant j'ai une explosion de traffic sur la session... Des billes, et ils s'en foutent des cyberattaques sur des individus sur le réseau domestique. Je l'ai ai incendié par courrier recommandé.

Toutes les infos sur la cyberattaque et les logs sont sur le forum Bouygues: [Cyberattaque en cours sur mon réseau local /home (linux) supprimé [ANOMALIE]](https://www.assistance.bouyguestelecom.fr/s/forum/question/0D5670000Ftx2VtCQI/cyberattaque-en-cours-sur-mon-r%C3%A9seau-local-home-linux-supprim%C3%A9-anomalie)

J'ai donc désactiver la redirection de port UPNP sur le routeur du FAI (qui est de la daube) puis après avoir logger la cyberattaque, nétoyer mon système avec une clean install d'Arch Linux.

Nouvelle config Arch: **systemd-boot + LUKS2 + LVM + BTRFS + Kernel-zen + XFCE + Kitty + Zsh**

J'ai lancer des procédures de détection de malware, audit et rootkit:

* rkhunter clean
* yara
* lynis clean
* arch-audit clean

En cas de compromission et leak de data:

* J'ai également changer mes mots de passe root, chiffrement et site web (en cours)
* Générer de nouvelle clé SSH
* Générer un nouveau porte-feuille de BTC (bitcoin) la clé privée exposé dans /home (l'argent n'a pas bougé)

Renforcer la sécurité en ajoutant un container Veracrypt pour les données sensibles et secrêtes.

Je viens donc de remettre en marche mon blog, procédure:

```text
Quick start recovery:

# Générer une nouvelle pair de clé SSH et transférer sur Github

1. git clone ssh repo/blog
2. changer de branch origin/source
3. supprimer l'ancien venv et sauvegarde pelicanconf.py

Install Pelican:

2. virtualenv .venv
3. source .venv/bin/activate
4. pip install pelican markdown ghp-import
5. pelican-quickstart
6. Copie des themes et plugins

Workflow:

$ git add . && git commit -m "Ajout article blog"
$ make html
$ make devserver
$ git push --all
$ make github
```

Il me reste à faire le tri des datas et analyser malware et rootkit de /home sur mon NAS de la sauvegarde. Pour cela je vais configurer une machine virtuelle sur Proxmox et transférer les datas en cas d'infection et compromission.


