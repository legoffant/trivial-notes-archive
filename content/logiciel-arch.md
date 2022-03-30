Title:Outils pour designers et développeurs sous Arch Linux
Date: 2022-03-30 20:16
Category:Linux
Tags: Linux, arch, logiciel
Authors: Anthony Le Goff
Summary:


---
Liste d'outils essentiels pour la productivité sous des distributions de type Arch Linux (Inclus Manjaro et Garuda Linux) utilisant le gestionnaire de packet Pacman. L'AUR Helper utilisé est yay.

---
## Navigateurs web

### **Chromium** (Google Chrome)

Le navigateur le plus populaire d'internet, il permet de synchroniser son compte Google sur tous les appareils et d'utiliser les services associés. Ne respecte pas la vie privée, est très intrusif.

Installation dans un terminal: `sudo pacman -S chromium`

* Guide wiki: https://wiki.archlinux.fr/Chromium

### **Mozilla Firefox**

Ce navigateur est installé en standard sur la plupart des distributions GNU/Linux car est un logiciel libre qui fut populaire avant l'arrivée de Chrome.

Installation dans un terminal: `sudo pacman -S firefox`

* Guide wiki: https://wiki.archlinux.fr/Firefox

### **LibreWolf**

LibreWolf, un fork de Firefox axé sur la confidentialité, la sécurité et la liberté. Les avantages liés à l’utilisation de LibreWolf sont nombreux. La plupart de ses fonctionnalités ont été conçues pour garantir votre sécurité et respecter votre vie privée. Dans un premier temps, LibreWolf a désactivé toute la télémétrie. En d’autres termes, aucune donnée de navigation ou de données personnelles ne sera collectée. Il intègre en natif un bloqueur de publicité.

Installation dans un terminal: `sudo yay -S librewolf`

* Guide: https://librewolf.net/installation/arch/

## Music Player

### **MOC Music On Console**

MOC est une lecteur de musique basé sur la ligne de commande dans un terminal. Il permet de lire de la musique dans un dossier. Il est customisable avec des thèmes.

Installation dans un terminal: `sudo pacman -S moc`

* Guide wiki: https://wiki.archlinux.org/title/MOC

## Music streaming

### **Spotify**

Le service de music en streaming Spotify a un logiciel en natif sous GNU/Linux même si l'application web fait très bien le travail. Beaucoup de gens sont plus productif en écoutant de la musique.

Installation dans un terminal: `sudo yay -S spotify`

* Guide wiki: https://wiki.archlinux.org/title/Spotify 

## Lecteur vidéo

### **VLC**

VLC est un logiciel open-source, lecteur multimedia qui accepte la plupart des formats vidéos, DVD, CD.

Installation dans un terminal: `sudo pacman -S vlc`

* Guide : https://www.videolan.org/vlc/download-archlinux.html

## IRC Client

### **WeeChat**

Client IRC pour chatter sur le réseau.

Installation dans un terminal: `sudo pacman -S weechat`

* Guide Wiki: https://wiki.archlinux.org/title/WeeChat


## Service de stockage Cloud

Les services cloud ont permis d'améliorer la portabilité des documents, la collaboration et le partage en synchronisant sur plusieurs appareils à la fois et permettant d'avoir une sauvegarde de ces documents les plus utiles sans avoir besoin d'avoir avec soi une clé USB.

### **Dropbox**

Dropbox est le service de stockage cloud le plus populaire, il permet d'avoir une offre gratuite de 2GB. Il existe un client natif GNU/Linux qui permet de synchroniser ces dossiers avec le serveur de Dropbox.

Installation dans un terminal: `sudo yay -S dropbox`

* Guide wiki: https://wiki.archlinux.org/title/Dropbox

### **MEGA**

MEGA est un service cloud respectant la vie privée ou les documents sont chiffrés sur le serveur. Il existe un client en natif sous GNU/LINUX. Il offre 20GB de stockage gratuit.

Installation dans un terminal: `sudo yay -S megasync`

* Guide: https://www.linuxadictos.com/en/how-to-install-megasync-on-arch-linux-and-derivatives-and-fix-ibcryptopp-so-error.html


## Editeurs d'image

### **Gimp** (Adobe photoshop)

Gimp est le standard en open-source pour l'édition d'image, il y a de nombreuse ressource sur internet pour apprendre à s'en servir. Il permet la création de dessin ou encore l'utilisation de filtre photos dans la palette d'utilisation possible.

Installation dans un terminal: `sudo pacman -S gimp`

* Guide wiki: https://wiki.archlinux.org/title/GIMP

### **Inkscape** (Abobe Illustrator)

Inkscape est un logiciel de dessin vectoriel populaire dans le milieu des graphistes, il permet des retouches et des créations rapides. Etant un logiciel libre, il y a une liste importante de tutorial sur le sujet.

Installation dans un terminal : `sudo pacman -S inkscape`

* Guide wiki: https://wiki.archlinux.org/title/Inkscape

## Logiciel Paint

### **Krita**

Krita est un logiciel de digital painting, vous pouvez créer de l'art digital, des comics ou encore des animations. C'est un outil professionnel utilisé dans les écoles d'art graphique et open source. 

Installation dans un terminal: `sudo pacman -S krita`

* Guide installation: https://docs.krita.org/en/user_manual/getting_started/installation.html

## Application de photographie

### **Shotwell** (GNOME)

Shotwell est un logiciel d'organisation d'images et de visualisation.

Installation dans un terminal: `sudo pacman -S shotwell`

* Guide: http://shotwell-project.org/doc/html/

## Edition vidéo

### **Shotcut**

[Shotcut](https://shotcut.org/) est un logiciel d'édition et création vidéo open-source.

Installation dans un terminal: `sudo pacman -S shotcut`

* Tutorial: https://shotcut.org/tutorials/

## Outils de screenshot et enregistrement d'écran

### **Shutter**

[Shutter](https://shutter-project.org/) est un outil d'édition et de partage de capture d'écran, il est installé en natif sous Ubuntu.

Installation dans un terminal: `sudo pacman -S shutter`

* Guide installation: https://www.makeuseof.com/install-shutter-linux/

### **Kazam**

Kazam est un logiciel capable d'enregistrer votre écran (screen recording). Il vous laissera le choix de faire soit une capture en continu (format vidéo) ou une simple capture d'écran.

Installation dans un terminal: `sudo yay -S kazam`


## Bureautique

### **LibreOffice**

LibreOffice est une suite bureautique libre et gratuite, dérivée du projet OpenOffice.org, créée et gérée par The Document Foundation. N'oubliez pas d'installer le pack de langage, les correcteurs orthographique et grammaticale pour l'outil de texte.

Installation dans un terminal: `sudo pacman -S libreoffice-still`

* Guide wiki: https://wiki.archlinux.fr/LibreOffice

### **Cryptpad**

CryptPad est une solution open source en ligne d'édition collaborative en temps réel et chiffrée.

Site web: https://cryptpad.fr/

### **Ghostwriter**

Un éditeur de Markdown simple, libre et gratuit. Il permet de prévisualiser le document Markdown en HTML. L'aperçu ne se met à jour que lorsque vous arrêtez de taper, ce qui vous permet de continuer à travailler sur un document volumineux sans que l'application ne gèle.

Installation dans un terminal: `sudo pacman -S ghostwriter`

* Documentation: https://wereturtle.github.io/ghostwriter/documentation.html

### **Texmaker**

[Texmaker](https://www.xm1math.net/texmaker/index_fr.html) est un éditeur LaTeX libre et gratuit avec support de l'unicode, correction orthographique, auto-complétion et repliage de code. Il intègre un afficheur pdf intégré avec support pour synctex et affichage en mode continu.

Installation dans un terminal: `sudo pacman -S texmaker`

* Info LaTeX: https://wiki.archlinux.fr/LaTeX

## Outils de téléchargement

### **Youtube-dl**

Youtube-dl est un outil pour télécharger des vidéos et audios depuis plus de 1000 sites dont Youtube ou Dailymotion. Il s'utilise en ligne de commande.

Installation dans un terminal: `sudo pacman -S youtube-dl`

* Guide wiki: https://wiki.archlinux.org/title/Youtube-dl

### **uGet**

[uGet](https://ugetdm.com/) est le premier outil open-source de management de téléchargement depuis internet incluant via HTTP, FTP, Bitorrent. Il permet de reprendre un téléchargement si celui-ci est trop long en particulier pour les connexions internet à bas débit.

Installation dans un terminal: `sudo pacman -S uget`

## IDE et éditeur de texte pour codeur

### **Vim**

Vim est un éditeur de texte, c'est-à-dire un logiciel permettant la manipulation de fichiers texte. Il est directement inspiré de vi, dont il est le clone le plus populaire. Son nom signifie d'ailleurs Vi IMproved, que l'on peut traduire par « VI aMélioré. S'utilise en ligne de commande.

Installation dans un terminal: `sudo pacman -S vim`

### **VSCodium**

[VSCodium](https://vscodium.com/) est un fork de Visual Studio Code de Microsoft sans la télémétrie. S'utilise de la même façon.

Installation dans un terminal: `sudo yay -S vscodium-bin`

### **Eclipse**

Eclipse est un projet, décliné et organisé en un ensemble de sous-projets de développements logiciels, de la fondation Eclipse visant à développer un environnement de production de logiciels libre qui soit extensible, universel et polyvalent, en s'appuyant principalement sur Java.

Installation dans un terminal: `sudo yay -S eclipse-java`

* Guide wiki: https://wiki.archlinux.org/title/Eclipse

### **Code::Blocks**

Code::Blocks est un environnement de développement intégré libre et multiplate-forme.Il est écrit en C++ et utilise la bibliothèque wxWidgets. Code::Blocks est orienté C et C++, mais il supporte d'autres langages comme FORTRAN ou le D. Il nécessite l'installation de Xterm pour fonctionner correctement.

Installation dans un terminal: `sudo pacman -S codeblocks`

Guide wiki: https://wiki.codeblocks.org/index.php/Main_Page

### **PyCharm**

Python IDE pour développeur professionnel.

Installation dans un terminal: `sudo pacman -S pycharm-community-edition`

## PDF et eBook application

### **Calibre**

[Calibre](https://calibre-ebook.com/) est pour les bibliophiles qui collectent des ebooks pour manager et créer ces propres ebooks dans divers formats dont EPUB. Il permet de convertir dans divers formats.

Installation dans un terminal: `sudo pacman -S calibre`

## Notes et To-do list

Dans tout processus d'apprentissage, la prise de note est essentiel car nous ne pouvons pas tout retenir.

### **Zim** 

Zim est un éditeur de texte, inspiré de la forme wiki, pensé pour gérer et organiser une collection de textes interconnectables stockés localement. Chaque page-wiki peut contenir du texte avec un formatage léger, des liens vers d'autres pages, des pièces-jointes et des images.

Installation dans un terminal: `sudo pacman -S zim`

* Guide wiki: https://wiki.archlinux.org/title/Zim

### **Planner**

[Planner](https://useplanner.com/) est une application to-do list pour faire de la GTD(Getting thing done) pour manager des tâches à accomplir.

Installation dans un terminal: `sudo yay -S elementary-planner`

## mots de passe protection et chiffrement de dossiers

### **KeePass**

[KeePass](https://keepass.info/) Password Safe est un gestionnaire de mots de passe publié sous la licence libre GPL v2 ou ultérieure, permettant de sauvegarder un ensemble de mots de passe dans une base de données chiffrée sous la forme d'un seul fichier dont l'extension est.kdb ou *.kdbx selon la version. Il permet egalement de générer des mots de passe fort contre les attaques brutes forces.

Installation dans un terminal: `sudo pacman -S keepass`

* Guide wiki: https://wiki.archlinux.org/title/KeePass

### **VeraCrypt**

VeraCrypt est un logiciel utilitaire sous licence libre utilisé pour le chiffrement à la volée (OTFE). Il est développé par la société française IDRIX2 et permet de créer un disque virtuel chiffré dans un fichier ou une partition. L'ensemble du dispositif de stockage demande une authentification avant de monter le disque virtuel.

Installation dans un terminal: `sudo pacman -S veracrypt`

Guide wiki (fork TrueCrypt): https://wiki.archlinux.org/title/TrueCrypt

## Système maintenance

### **Deja-Dup**

Deja-Dup est un outil de sauvegarde de système minimaliste basé sur Duplicity. Il permet de sauvegarder vers des emplacements distants et de la programmer automatiquement.

Installation dans un terminal: `sudo pacman -S deja-dup`

* Guide d'installation: https://ostechnix.com/how-to-backup-and-restore-files-using-deja-dup-in-linux/

### **Par-feu GUFW**

UFW est un nouvel outil de configuration simplifié en ligne de commande de Netfilter, qui donne une alternative à l'outil iptables. UFW devrait à terme permettre une configuration automatique du pare-feu lors de l'installation de programmes en ayant besoin. Gufw est le front-end GUI.

Installation dans un terminal: `sudo pacman -S gufw`

* Guide wiki: https://wiki.archlinux.org/title/Uncomplicated_Firewall

### **CUPS**

Common Unix Printing System (CUPS) est un système modulaire d'impression numérique pour les systèmes d'exploitation Unix et assimilés. Tout ordinateur qui utilise CUPS peut se comporter comme un serveur d'impression ; il peut accepter des documents envoyés par d'autres machines (ordinateurs clients), les traiter, et les envoyer à l'imprimante qui convient. 

Installation dans un terminal : `sudo pacman -S cups`

* Guide wiki: https://wiki.archlinux.fr/CUPS

### **Neofetch**

C'est un outil en ligne de commande qui permet d'afficher les informations du système, thèmes icones, manager de fenêtre avec un style ASCII pour le logo de la distribution GNU/Linux.

Installation dans un terminal: `sudo pacman -S neofetch`

### **Etcher**

[Etcher](https://www.balena.io/etcher/) est un logiciel de création de live USB, multi-plateforme et open source.

Installation dans un terminal: `sudo yay -S balena-etcher`

## Virtualisation

### **VirtualBox**

VirtualBox (ou VBox) est un produit pour la virtualisation d'un environnement 32 (x86) ou 64 bits (AMD64/Intel64) et il est aussi valable pour le milieu de l'entreprise que pour les particuliers. Il supporte un nombre important de systèmes d'exploitation, propose une interface graphique (Qt / SDL) de même qu'une interface en ligne de commande. 

Installation dans un terminal: `sudo pacman -S virtualbox`

* Guide wiki: https://wiki.archlinux.fr/VirtualBox

### **KVM**

KVM est un hyperviseur de virtualisation, il s'utilise avec QEMU et l'interface graphique de gestion des machines virtuelles Virt-Manager.

Installation dans un terminal: `sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat`

* Guide d'installation: https://computingforgeeks.com/install-kvm-qemu-virt-manager-arch-manjar/

## Contrôle de version

### **Git**

Git est un logiciel de gestion de versions décentralisé. C'est un logiciel libre créé par Linus Torvalds, auteur du noyau Linux, et distribué selon les termes de la licence publique générale GNU version 2. Il est utilisé par plus de douze millions de personnes.

Installation dans un terminal: `sudo pacman -S git`

Guide wiki: https://wiki.archlinux.org/title/Git

## Management de base de donnée SQL

### **Beekeeper Studio**

Beekeeper Studio est un logiciel cross-plateforme d'édition et management de requête SQL. C'est un client pour MySQL, Postgres, SQLite, SQL Server, MariaDB etc.

Installation dans un terminal: `sudo yay -S beekeeper-studio-bin`

* Guide d'installation: https://docs.beekeeperstudio.io/installation/#linux-installation

## Transfert de fichier 

### **FileZilla**

FileZilla Client est un client FTP, FTPS et SFTP, développé sous la licence publique générale GNU.

Installation dans un terminal: `sudo pacman -S filezilla`

* Guide wiki: https://wiki.filezilla-project.org/Main_Page

## RDP (Remote desktop client)

### **Remmina**

Remmina est un client graphique de connexion et de prise de contrôle de bureau multi-protocoles pour les systèmes d'exploitation basés sur le noyau Linux. Il supporte the Remote Desktop Protocol, VNC, NX, XDMCP, SPICE, X2Go and SSH protocols

Installation dans un terminal: `sudo pacman -S remmina`

* Guide d'installation: https://remmina.org/how-to-install-remmina/

## API Client

### **Insomnia**

[Insomnia](https://insomnia.rest/) est un outil open-source de design et client API(Application programming interface) qui facilite l'envoi de requête REST, SOAP, GraphQL, and GRPC.

Installation dans un terminal: `sudo yay -S insomnia-bin`

* Guide docs: https://docs.insomnia.rest/


## Diagramme et flowchart

### **Draw.io**

draw.io est une application de création de diagrammes et schémas sous licence Apache disponible sous Windows, MacOs, Linux, sous forme d'application web et intégrée à des services cloud tels NextCloud ou Google Drive.

Site web: https://app.diagrams.net/

## Mindmapping

### **Freemind**

FreeMind est un logiciel libre qui permet de créer des cartes heuristiques, diagrammes représentant les connexions sémantiques entre différentes idées.

Installation dans un terminal: `sudo pacman -S freemind`

## Container

### **Docker**

Docker est une plateforme logicielle qui permet de construire des applications dans un environnement isolé basé sur des containers.

Installation dans un terminal: `sudo pacman -S docker`

Guide d'installation: https://www.linuxfordevices.com/tutorials/linux/install-docker-on-arch


## Outils Terminal

### **Oh My Zsh**

Oh-My-Zsh est un outil pour manager Zsh qui est un shell tout comme en natif sous GNU/Linux Bash. Utiliser Oh-My-Zsh c'est avoir un terminal plus design, intégrant des outils et l'auto-completion des lignes de commandes.

Site web: https://ohmyz.sh/

* Docs: https://github.com/ohmyzsh/ohmyzsh/wiki

### **Guake terminal**

Guake est un terminal déroulant. Il permet d'obtenir un terminal en appuyant simplement sur la touche F12 (par défaut, configurable). C'est un clone de Yakuake pour Gnome. 

Installation dans un terminal: `sudo pacman -S guake`

* Guide wiki: https://wiki.archlinux.org/title/Guake

### **Tmux**

Tmux est un terminal multiplexer qui permet à un nombre de terminal pouvant être créé, contrôlé et accédé depuis un seul écran.

Installation dans un terminal: `sudo pacman -S tmux`

* Guide d'installation: https://computingforgeeks.com/linux-tmux-cheat-sheet/

### **SSH**

SSH est un protocole permettant d'établir une communication chiffrée, donc sécurisée (on parle parfois de tunnel), sur un réseau informatique (intranet ou Internet) entre une machine locale (le client) et une machine distante (le serveur). La sécurité du chiffrement peut être assurée par différentes méthodes, entre autre par mot de passe ou par un système de clés publique / privée (mieux sécurisé, on parle alors de cryptographie asymétrique). C'est un outil essentiel pour développeurs pour ce connecter à un serveur distant.

Installation dans un terminal: `sudo pacman -S openssh`

* Guide wiki: https://wiki.archlinux.fr/Ssh

## Documentation

Rappelez-vous de lire le manuel. Les distributions de type Arch Linux sont bien documenté via le wiki Arch en anglais et français. Référez-vous aux Man Pages dans un terminal pour documenter la ligne de commande.

Si vous ne comprenez pas une ligne de commande, prenez l'habitude d'utiliser des sites comme https://explainshell.com/ qui va analyser la ligne de commande.

### **DevDocs**

DevDocs API documentation rassemble sur un site web: https://devdocs.io/ les sources des langages, frameworks.

### **Zeal**

Zeal est une application de documentation hors-ligne pour développeurs de logiciel. Les langages sont référencés, API, Frameworks etc...

Installation dans un terminal: `sudo yay -S zeal`

* Guide d'utilisation: https://zealdocs.org/usage.html
