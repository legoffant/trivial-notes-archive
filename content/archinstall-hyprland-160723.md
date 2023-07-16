Title:Arch Install Linux Zen Kernel + LUKS2 + LVM + BTRFS + systemd-boot + hyprland + Fish shell
Date: 2023-07-16 10:36
Category:Linux
Tags:arch install
Authors: Anthony Le Goff
Summary:

Mise à jours en 07/2023 de mon installation d'Arch Linux avec quelques nouveautés en particulier la prise en charge de snapshot avec BTRFS, modification container luks2, ajout kernel linux-zen, bureau hyprland.

Voila sur quoi je travail sur ma nouvelle installation d'Arch Linux en mode dev dans une VM sous Proxmox, avant de déployer sur mon thinkpad Helix. Tout fonctionne pour l'instant jusqu'à l'installation du bureau hyprland.

Ce qui est une grosse mise à jour de ma machine de production actuel > [code l'ancienne config sous LUKS + LVM + EXT4 + GRUB + XFCE + Zsh](https://gist.github.com/legoffant/8a7503430d2663549f982ea7f97622f3)

Inclus:

* Editeur de texte Neovim avec l'autocompletion,ctags du code en C/C++ et Python
* Shell Fish
* Synchro Cloud MEGA
* VPN Proton
* L'aide à l'écriture Manuskript
* Second cerveau Obsidian
* VScodium
* Calcul numérique avec les notebook Jupyter en Python
* Calcul Formel Sagemath
* Recherche en vulnérabilité et le repo Blackarch
* Interpréteur Ruby Pry via RVM
* Launcher fzf
* Machine virtuelle KVM et Virt-manager
* Gestion du par-feu ufw
* Navigateur Firefox
* Gestion de bibliothèque ebook avec calibre et bibliographie avec Zotero
* Editeur LaTex texmaker
* Editeur markdown Ghostwriter


**Pour qui c'est destiné?**

* Les hackers
* Ingénieurs et dévéloppeurs informatique
* Chercheurs
* Ecrivains

**Peut-on faire du jeu-video?**

Installer Steam est possible, ou Minecraft, vous serez limité en ressource graphique.

```
yay -S minecraft-launcher
```

**Stack:**

* OS: [Arch Linux](https://archlinux.org/)
* Chiffrement: [dmcrypt-LUKS](https://fr.wikipedia.org/wiki/Dm-crypt)
* Bootloader: [systemd-boot](https://systemd.network/systemd-boot.html)
* Système de fichier: [BTRFS](https://fr.wikipedia.org/wiki/Btrfs)
* Shell: [Fish](https://fishshell.com/)
* Windows Manager: [hyprland](https://hyprland.org/)
* Terminal: [Kitty](https://sw.kovidgoyal.net/kitty/)
* Prompt: [Starship.rs](https://starship.rs/)
* File Manager: [Broot](https://dystroy.org/broot/) (term)
* Launcher: [fzf](https://archlinux.org/packages/community/x86_64/synapse/) (term)
* Navigation rapide directory: [z](https://github.com/rupa/z) (term) 
* Historique intelligent: [mcFly](https://github.com/cantino/mcfly) (term)
* Corriger et fixer des erreurs, typos de la commande précédente: [thefuck](https://github.com/nvbn/thefuck) (term)
* Moderne replacement pour ls: [exa](https://github.com/ogham/exa) (term)
* cat clone avec coloration syntaxique et git integration : [bat](https://github.com/sharkdp/bat) (term)
* Disque monitoring: [duf](https://github.com/muesli/duf) (term)
* Outil de téléchargement supportant HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink: [aria2](https://aria2.github.io/) (term)
* Recherche récursive dans le directory à base de pattern de regex: [ripgrep](https://github.com/BurntSushi/ripgrep) (term)
* grep-like optimisé pour la recherche dans le code source: [ack3](https://github.com/beyondgrep/ack3) (term)
* Interactive monitoring des ressources, gestion des processus: [htop](https://htop.dev/) (term)
* Rapide et facile, outil de partage de fichier: [transfer.sh](https://transfer.sh/) (term)
* Virtualisation: [Virt-Manager QEMU/KVM](https://virt-manager.org/)
* Lecteur audio: [CMUS](https://cmus.github.io/) (term)
* Lecteur video: [Vlc](https://www.videolan.org/vlc/)
* Spotify TUI client: [spotify-tui](https://github.com/Rigellute/spotify-tui) (term) 
* Recherche et regarder des vidéos sur Youtube: [ytfzf](https://github.com/pystardust/ytfzf) (term)
* Télécharger de l'audio et des vidéos sur Youtube + d'autres sites: [yt-dlp](https://github.com/yt-dlp/yt-dlp) (term)
* Simple iptv player avec fuzzy finder: [IPTV](https://github.com/shahin8r/iptv) (term)
* Utilitaire pour rechercher et télécharger des liens torrents: [tordl](https://github.com/X0R0X/cli-torrent-dl) (term)
* IRC: [Weechat](https://weechat.org/) (term)
* Editeur de texte: [Neovim](http://neovim.io/) (term)
* Contrôle de version: [Git](https://git-scm.com/) (term)
* Commande Git TUI: [lazygit](https://github.com/jesseduffield/lazygit) (term)
* Extension ligne de commande Git intégrant Github: [hub](https://hub.github.com/) (term)
* Interface de monitoring de container Docker: [ctop](https://github.com/bcicen/ctop) (term) 
* Management des containers Dockers et services: [dockly](https://github.com/lirantal/dockly) (term) 
* HTTP Client pour les API: [HTTPie](https://github.com/httpie/httpie) (term) 
* Rapide prise de note: [terminal velocity](https://vhp.github.io/terminal_velocity/) (term)
* SSH + VPN connexion: [xiringuito](https://github.com/ivanilves/xiringuito) (term)
* User-friendly détails et statistiques de sockets TUI: [neoss](https://github.com/PabloLec/neoss) (term)
* Analyseur de packet réseau: [wireshark-cli](https://archlinux.org/packages/?name=wireshark-cli) (term)
* Force TCP connection avec un proxy utilisant TOR, SOCK, HTTP: [proxychains](https://github.com/haad/proxychains) (term)
* Outil de diagnostique réseau: [mtr](https://github.com/traviscross/mtr) (term)
* TUI Client pour Network Manager pour configurer le réseau: [nmtui](https://wiki.archlinux.org/title/NetworkManager) (term)
* Notepad: [Mousepad](https://archlinux.org/packages/extra/x86_64/mousepad/)
* Calculatrice: [Galculator](https://archlinux.org/packages/community/x86_64/galculator/)
* P2P Torrent: [Deluge](https://deluge-torrent.org/)
* Navigateur internet: [Firefox](https://www.mozilla.org/fr/firefox/new/)
* Documentation langage: [Zeal](https://zealdocs.org/)
* Gestionnaire de mot de passe: [Keepass](https://keepass.info/)
* Client Serveur FTP: [Filezilla](https://filezilla-project.org/)
* Carte Mentale: [Freemind](https://freemind.fr.softonic.com/)
* Editeur d'image: [Gimp](https://www.gimp.org/)
* EDI Java: [Eclipse](https://www.eclipse.org/downloads/packages/release/kepler/sr1/eclipse-ide-java-developers)
* Compilateur: [GCC](https://gcc.gnu.org/)
* Interpréteur Ruby: [IRB](https://github.com/ruby/irb)
* Notebook Python: [Jupyter](https://jupyter.org/)
* Container chiffré: [Veracrypt](https://www.veracrypt.fr/code/VeraCrypt/)
* Outil d'écrivain: [Manuskript](https://www.theologeek.ch/manuskript/)
* Calcul formel: [SageMath](https://www.sagemath.org/fr/)
* Par-feu: [Gufw](http://gufw.org/)
* Sauvegarde: [Deja-dup](https://apps.gnome.org/fr/app/org.gnome.DejaDup/)
* Cloud: [MEGA](https://mega.nz/)
* VPN: [Proton](https://protonvpn.com/)
* Gestion bibliographique: [Zotéro](https://www.zotero.org/)
* Base de connaissance: [Obsidian](https://obsidian.md/)
* Wiki local: [Zim](https://www.zim-wiki.org/index.html)
* Editeur LaTex: [Texmaker](https://www.xm1math.net/texmaker/)
* Office: [Cryptpad](https://cryptpad.fr/)
* Flowchart & Diagram: [draw.io](https://www.draw.io/index.html)
* Documentation langage en ligne: [https://devdocs.io/](https://devdocs.io/)
* Social Bookmarking: [Pearltrees](https://www.pearltrees.com/)
* Explication détaillée d'une ligne de commande: [explainshell](https://www.explainshell.com/) 
* Construit, test et debug des expressions régulières: [Regex101](https://regex101.com/) 
* Gestion communautaire de man pages: [tldr](https://tldr.sh/) (term)
* Réponse instantannée à propos du code: [howdoi](https://github.com/gleitz/howdoi) (term) 
* Construction communautaire de docs et cheatsheet, tous langages et frameworks: [wat](https://github.com/dthree/wat) 
* Outil interactif cheatsheet [navi](https://github.com/denisidoro/navi) 
* Recherche dans stack overflow quand une erreur ou une exception est levé dans le code à la compilation: [rebound](https://github.com/shobrook/rebound)
* Utiliser chatGPT via l'API d'OpenAI: [chatGPT-cli](https://github.com/0xacx/chatGPT-shell-cli) & [gpt-cli](https://github.com/kharvd/gpt-cli) (term)
* Surveiller le marché des cryptomonnaies: [cointop](https://github.com/cointop-sh/cointop) (term) 
* Maths calculateur, calcul symbolique, matrice, équation: [Qalculate](https://github.com/Qalculate/libqalculate) (term)
* Sauvegarde chiffrée à distance (cloud service, NAS, etc): [rclone](https://rclone.org/) (term)
* Enregistrement de session terminal: [asciinema](https://asciinema.org/) (term) 
* Un terminal façon Matrix: [cmatrix](https://github.com/matriex/cmatrix) (term)
* Generateur de bannière ASCII Art: [figlet](http://www.figlet.org/) (term) 
* Information sur le système: [neofetch](https://github.com/dylanaraps/neofetch) (term)
* Recherche les informations de l'architecture du CPU: [cpufetch](https://github.com/Dr-Noob/cpufetch) (term)
* Partage de terminal: [duckly](https://duckly.com/)
* Encodage de gifs: [gifski](https://gif.ski/)


Listes d'applications spécifique à la recherche de vulnérabilité:

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
* DDoS service outils: [ufonet](https://ufonet.03c8.net/)
* Traffic capture implementation d'attaque de type man-in-the-middle: [ettercap](https://www.ettercap-project.org/index.html)
* Web Application Attack and Audit Framework: [w3af](http://w3af.org/)
* Vulnerability Assessment Scanner: [openvas](https://www.openvas.org/)
* Command and control server et agent post-exploitation HTTP/2 [Merlin](https://github.com/Ne0nd0g/merlin)


---

nota:  désactiver dans le bios le secure boot pour booter en USB.
Vérifier le démarrage UEFI.

### pre-check configuration 

Charger le clavier français en tapant "loqdkeys fr"
```bash
$ loadkeys fr
```

Verifier boot mode
```bash
$ ls /sys/firmware/efi/efivars    (Si le répertoire existe, l'ordinateur supporte l'efi)
```

### Connexion au réseau

Vérifier le nom du reseau et si celui-ci est up
```bash
$ ip addr show
```

vérifier la connexion internet
```bash
$ ping -c 2 google.com
```

Connexion au wifi
```bash
$ iwctl
```
affichage du prompt [IWD]#
```text
[iwd]# device list
[iwd]# station device scan
[iwd]# station device get-networks
[iwd]# station device connect SSID
```

MAJ
```bash
$ sudo mount -o rw,remount /
$ reflector --verbose --country 'France' -l 50 -p https --sort rate --save /etc/pacman.d/mirrorlist
$ pacman -Syu
```

### Check les disques

Vérifier le nom de votre disque dur ou SSD (ie sda ou NVME)
```bash
lsblk
```

### Partitionnement

Destruction des données sécurisées du disque
```bash
$ shred -v -n 1 /dev/sda
```

Utilitaire de partitionnement
```bash
$ gdisk /dev/sda
```

Commande gdisk:

1. o (écrire table de partition GPT)
2. n (nouvelle partition), default, 512MB, ef00
3. n (nouvelle partition), default, default, 8300
4. w (écrire et quitter)

Mise en place de la table de partition:
```text
/dev/sda1 EFI ef00 512MB
/dev/sda2 Linux 8300
```

Formatage de la partition EFI
```bash
$ mkfs.vfat -F32 -n BOOT /dev/sda1
```

### Chiffrement 
```bash
$ cryptsetup --type luks2 --cipher aes-xts-plain64 --key-size 512 --pbkdf argon2id --use-random --verify-passphrase luksFormat /dev/sda2
```

Ouverture du container chiffré:
```bash
$ cryptsetup luksOpen /dev/sda2 cryptlvm
```

### Systèmes de fichiers

```bash
# Initialize un groupe physique de volume LVM
$ pvcreate --dataalignment 4M /dev/mapper/cryptlvm

# Initialise un groupe virtuel attaché au groupe physique
$ vgcreate vg /dev/mapper/cryptlvm

# Initialise une partition nommée 'arch' dans le volume group 'vg'
$ lvcreate -l +100%FREE vg -n arch

# Affiche les volumes logiques créés
$ lvdisplay
```

Formater la partition root
```bash
$ mkfs.btrfs -KL ARCH /dev/mapper/vg-arch
```

Monter les partitions:
```bash
$ mount /dev/mapper/vg-arch /mnt
```

Créer les subvolumes
```bash
$ btrfs subvolume create /mnt/@
$ btrfs subvolume create /mnt/@home
$ btrfs subvolume create /mnt/@_snapshot
$ brtfs subvolume list /mnt
```

Démonter la partition
```bash
$ cd /
$ umount /mnt
```

Remonter le subvolume @
```bash
$ mount -o noatime,space_cache=v2,compress=zstd,ssd,subvol=@ /dev/mapper/vg-arch /mnt
```

Créer les dossiers boot et home
```bash
$ mkdir -p /mnt/{home,_snapshot}
$ lsblk -l
```

Monter le subvolume @home
```bash
$ mount -o noatime,space_cache=v2,compress=zstd,ssd,subvol=@home /dev/mapper/vg-arch /mnt/home
```

Monter le subvolume @_snapshot
```bash
$ mount -o noatime,space_cache=v2,compress=zstd,ssd,subvol=@_snapshot /dev/mapper/vg-arch /mnt/_snapshot
```

Créer et Monter la partition EFI
```bash
$ mkdir -p /mnt/boot
$ mount /dev/sda1 /mnt/boot
```


### Système de base
```bash
$ pacstrap /mnt base base-devel linux-zen linux-firmware btrfs-progs sudo git linux-tools lvm2 cryptsetup vim intel-ucode fwupd
```

Générer fstab
```bash
$ genfstab -L -p /mnt >> /mnt/etc/fstab
```

Chrooter l'environnement
```bash
$ arch-chroot /mnt
```

Nom de la machine
```bash
$ echo archbox > /etc/hostname
```

Edit `/etc/hosts`:

```text
127.0.0.1		localhost
::1					localhost
127.0.1.1		archbox.localdomain	archbox
```


Configuration de local paramétrage des langues
```bash
$ vim /etc/locale.gen
en_US.UTF-8 UTF-8
fr_FR.UTF-8 UTF-8
```
Génération du fichier
```bash
$ locale-gen
```
Configuration des langues par defaut
```bash
$ vim /etc/locale.conf
LANG="fr_FR.UTF-8"
LC_COLLATE="fr_FR.UTF-8"
```
Exporter le langage actuel pour création dans initramfs
```bash
$ export LANG=fr_FR.UTF-8
```
Console, fonts, clavier azerty
```bash
$ vim /etc/vconsole.conf
KEYMAP=fr-pc
FONT=
FONT_MAP=
```

Assigne le fuseau horaire
```bash
$ ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime 
```


```bash
$ hwclock --systohc
```

Editer mkinitcpio
```bash
$ vim /etc/mkinitcpio.conf
```

```text	
	HOOKS=(base systemd autodetect keyboard sd-vconsole modconf block sd-encrypt sd-lvm2 btrfs filesystems)
	Si VM virtIO MODULES=(virtio virtio_blk virtio_pci virtio_net)
```

Générer initramfs
```bash
$ mkinitcpio -p linux-zen
```

Mot de passe super-administrateur root
```bash
$ passwd
```

Installation de paquets supplémentaires:
```bash
$ pacman - S networkmanager network-manager-applet dialog wpa_supplicant reflector linux-zen-headers avahi xdg-user-dirs xdg-utils gvfs nfs-utils inetutils dnsutils cups hplip bash-completion openssh rsync acpi acpi_call tlp ipset ufw sof-firmware nss-mdns acpid ntfs-3g terminus-font nano man-db man-pages zip p7zip unzip tar htop tmux wget pciutils lshw syslog-ng ntp 
```

Configuration de NTP:
```bash
$ vim /etc/ntp.conf
```

```text
server 0.fr.pool.ntp.org iburst
server 1.fr.pool.ntp.org iburst
server 2.fr.pool.ntp.org iburst
server 3.fr.pool.ntp.org iburst
```

Driver carte graphique, openGL, touchpad
```bash
$ pacman -S xf86-video-intel xf86-input-libinput mesa
```

Installation de QEMU/KVM pour la virtualisation
```bash
$ pacman -S virt-manager qemu qemu-arch-extra edk2-ovmf bridge-utils dnsmasq vde2 openbsd-netcat
```

### Configuration de systemd-boot

```bash
$ bootctl --esp=/boot install
```

Configuration générale du chargeur

```bash
$ vim /boot/loader/loader.conf
```

```text
default arch.conf
editor no
timeout 4
console-mode max
```

Récupérez le champs UUID= de la partition LUKS

```bash
$ blkid | grep /dev/sda2
```

Configuration d’une entrée du menu de démarrage.

```bash
$ vim /boot/loader/entries/arch.conf
```

```text
title Arch Linux
linux /vmlinuz-linux-zen
initrd <cpu>-ucode.img
initrd /initramfs-linux-zen.img
options rd.luks.uuid=<UUID> root=/dev/mapper/vg-arch rootflags=subvol=@ rw
```

### Activer les services systemD

```bash
$ systemctl enable NetworkManager
$ systemctl enable cups
$ systemctl enable sshd
$ systemctl enable avahi-daemon
$ systemctl enable tlp
$ systemctl enable reflector.timer
$ systemctl enable libvirtd
$ systemctl enable acpid
$ systemctl enable ufw
$ systemctl enable syslog-ng@default
$ systemctl enable ntpd
```

### Créer un utilisateur

```bash
$ useradd -mG storage,wheel,power -s /bin/bash trivial
$ passwd trivial
```

```bash
$ usermod -aG libvirt trivial
```

Ajout dans sudoers de l'utilisateur
```bash
$ echo "trivial ALL=(ALL) ALL" >> /etc/sudoers.d/trivial
```

Démonter et reboot
```bash
$ exit
$ umount -R /mnt
$ reboot
```

### Post-installation

Check ip adresse
```bash
$ ip a
```

Connexion au wifi/ethernet via Networkmanager TUI
```bash
$ nmtui
```

Synchronisation repository MAJ + reflector

Activer multilib et communauty:
```bash
$ sudo vim /etc/pacman.conf
```

```text
[community]
Include = /etc/pacman.d/mirrorlist

[multilib]
Include = /etc/pacman.d/mirrorlist
```

```bash
$ sudo reflector --verbose --country 'France' -l 50 -p https --sort rate --save /etc/pacman.d/mirrorlist

$ sudo pacman -Syu
```

Installation AUR Helper
```bash
$ mkdir sources 
$ cd sources 
$ git clone https://aur.archlinux.org/yay.git 
$ cd yay 
$ makepkg -si 
```

Installation de timeshift et zramd
```bash
$ yay -S timeshift-bin zramd
```

```bash
$ sudo systemctl enable zramd.service
$ sudo systemctl start zramd.service
```

Vérification que la swap est active:
```bash
$ lsblk -l
```


### Configuration de hyprland 

Post-installation:

Prérequis avoir `base-devel`, `git` et `wget`

Listing des packages et dépendances:
```bash
$ yay -S hyprland waybar-hyprland eww-wayland mako swaybg \
         kitty fish starship z fzf mclfy neovim broot \
         pipewire wireplumber \
         cliphist grimblast-git ffmpeg wf-recorder viewnior \
         polkit-kde-agent xdg-desktop-portal-hyprland-git \
         qt5-wayland qt6-wayland \
         wlogout swaylock-effects ly \
         webcord weechat fractal \
         cmus spotify-tui vlc ytfzf-git mpv haxor-news \
         cmatrix neofetch \
         ripgrep exa bat duf thefuck aria2 ack transfer.sh \
         lazygit hub ctop dockly httpie \
         xiringuito neoss mtr \
         howdoi tldr navi rebound \
         python python-pip python-virtualenv \
         firefox obsidian mousepad \
         adobe-source-han-sans-otc-fonts ttf-droid ttf-dejavu noto-fonts noto-fonts-emoji nerd-fonts-meta \
         gtk-cyberpunk-neon-theme-git \
         fcitx-im \
         udiskie \
         cointop libqalculate rclone asciinema figlet cpufetch gifski \
```

Installation de youtube-dl:
```bash
$ pip install yt-dlp
```

Installation de terminal velocity
```bash
$ pip install terminal_velocity

```

Installation IPTV:
```bash
$ sudo wget https://raw.githubusercontent.com/shahin8r/iptv/master/iptv -qO /usr/local/bin/iptv && sudo chmod +x /usr/local/bin/iptv

### Run playlist:

$ iptv https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8
```

Configurer Tordl:
```bash
$ git clone https://github.com/X0R0X/cli-torrent-dl.git
$ cd ~/cli-torrent-dl
$ ./setup.sh

# configurer client torrent (deluge)
$ nano ~/.config/torrentdl/config.json

```
Autostart authentification agent:
```bash
$ exec-once=/usr/lib/polkit-kde-authentication-agent-1
```

Activer le service au démarrage ly:
```bash
$ sudo systemctl enable ly.service
```

Configurer fish comme shell par défault:
```bash
$ echo /bin/fish | sudo tee -a /etc/shells
$ chsh -s /bin/fish
```

Editer fichier de configuration:
```bash
$ nvim ~/.config/hypr/hyprland.conf
```

Lancer automatiquement le montage USB, etc:
```text
exec-once = udiskie &
```
Clavier configuration ajouter:
```text
device:nom-clavier {
    kb_layout=fr,us
}
```

Commande pour switcher entre les claviers:
```bash
$ hyprctl switchxkblayout nom-clavier fr
```


NOTA: Pour activer la prise en charge Pinyin, utiliser fcitx.

**Codec Multimédia**

Nous allons installer l’ensemble des greffons gstreamer qui est le framework utilisé par de nombreux environnements de bureau pour gérer le multimedia.
```bash
$ sudo pacman -S gst-plugins-{base,good,bad,ugly} gst-libav
```

Extension essentiel sur Firefox:

* DuckDuckGo Privacy Essentials
* Smart HTTPS
* Disconnect
* U-Block Origin
* Privacy Badger

```
$ reboot
```

### Configuration des applications

#### Application pour développeur et designer

```bash
$ sudo pacman -S keepass gimp vlc filezilla inkscape deluge deluge-gtk galculator veracrypt kazam calibre
```

Embedded (microcontroller, AVR, etc...) - Pour utiliser Arduino et PlatformIO, installer et configurer:

* arduino-cli
* arduino-ide-bin (AUR)
* platformio (AUR)


Documentation des langages
```bash
$ yay -S zeal
```
NOTA: Problème de lenteur de compilation de qt5-webkit

Installation des outils de développeurs C/C++, Clang, Ruby
```bash
$ sudo pacman -S llvm clang nodejs npm ctags
```
RVM Ruby
```bash
$ sudo gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

$ \curl -sSL https://get.rvm.io | bash -s stable --ruby --gems=pry

### Verifier l'installation dans le terminal 
$ source /etc/profile.d/rvm.sh

### Install Gems
$ gem install <gems>

### Integration avec fish

$ curl -L --create-dirs -o ~/.config/fish/functions/rvm.fish https://raw.github.com/lunks/fish-nuggets/master/functions/rvm.fish

$ echo "rvm default" >> ~/.config/fish/config.fish

```

Install Wat, outil communautaire documentation:
```bash
$ npm install -g wat
```


Installation de Jedi autocompletion pour python
```bash
$ pip install jedi
```

Editeur de texte VSCodium
```bash
$ yay - S vscodium-bin
```

Installation de Java Eclipse
```bash
$ sudo pacman -S jdk-openjdk
$ yay -S eclipse-java
```

Outil de mind mapping (java)
```bash
$ yay -S freemind
```

**Configuration de Neovim**

Installation du gestionnaire de plugin "vim-plug" cf: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
```bash
$ sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


init.vim
```text
" Neovim configuration file init.vim
" author: Anthony J.R Le Goff legoff.ant@gmail.com
" date: 16th april 2022

:set number
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4
":set mouse=a

call plug#begin() 

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'scrooloose/nerdtree'
Plug 'scrooloose/syntastic'
Plug 'vim-airline/vim-airline'
Plug 'tomasr/molokai'
Plug 'raimondi/delimitmate'
Plug 'kien/ctrlp.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'majutsushi/tagbar'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

set encoding=UTF-8

call plug#end()

:set statusline+=%#warningmsg#
:set statusline+=%{SyntasticStatuslineFlag()}
:set statusline+=%*

:let g:syntastic_always_populate_loc_list = 1
:let g:syntastic_auto_loc_list = 1
:let g:syntastic_check_on_open = 1
:let g:syntastic_check_on_wq = 0

nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

nmap <C-r> :TagbarToggle<CR>
nmap <C-p> :CtrlP<CR>

:colorscheme molokai

let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="~"

" air-line
let g:airline_powerline_fonts = 1


" :CocInstall coc-python
" :CocInstall coc-clangd
```

#### Outils de Hacking, pentesting, bug bounty, CTF

Installation de dépot BlackArch >> [https://blackarch.org/](https://blackarch.org/)

```bash
$ curl -O https://blackarch.org/strap.sh
$ curl https://blackarch.org/checksums/strap
$ sha1sum strap.sh # doit etre egal a 5ea40d49ecd14c2e024deecf90605426db97ea0c (valeur du fichier strap)
$ sudo chmod +x strap.sh
$ sudo ./strap.sh
```

Mise à jour des paquets:
```bash
sudo pacman -Syyu
```

Vous pouvez installer tous les outils Blackarch via cette commande (recommandé):
```bash
$ sudo pacman -S blackarch
```
SINON Installer les outils un par un:

Installation des outils basics
```bash
$ sudo pacman -S nmap impacket wireshark-qt tcpdump hashcat john proxychains-ng exploitdb httpie metasploit armitage bind-tools radare2 sqlmap wpscan xclip beef set ufonet ettercap w3af merlin-server

```
L'installation d'OpenVAS est un peu plus complexe, voir la page: [https://wiki.archlinux.org/title/OpenVAS](https://wiki.archlinux.org/title/OpenVAS)

Configuration WordLists
```bash
$ mkdir -p /usr/share/wordlists
$ wget -q https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz -O /usr/share/wordlists/rockyou.txt.tar.gz
$ wget -q https://github.com/danielmiessler/SecLists/raw/master/Discovery/Web-Content/common.txt -O /usr/share/wordlists/common.txt
```

#### Outils pour écrivain et chercheur
```bash
$ sudo pacman -S ghostwriter pdfjs pandoc texmaker manuskript libreoffice-still libreoffice-still-fr hunspell hunspell-fr
```

Extension Grammalecte et gestion de bibliographie
```bash
$ yay -S zotero libreoffice-extension-grammalecte-fr
```

#### Calcul numérique et scientifique (remplace Matlab)

```bash
$ python -m pip install jupyter scipy numpy matplotlib pandas ipython
```

Calcul Formel
```bash
$ sudo pacman -S sagemath
```

### Sauvegarde

#### Installation du client SAMBA

```bash
$ sudo pacman -S smbclient gvfs-smb
```
Redémarrer le PC pour prendre en compte la découverte du réseau local.

GUI: Ensuite rechercher votre serveur dans thunar en tapant:
```text
smb://192.168.X.X
```

Terminal: Monter le serveur SMB:

List SMB shares folders
```bash
$ smbclient -L //myServerIpAdress
```

Créer le point de montage:

```bash
sudo mkdir -p /media/NAS
```

Commande de montage
```bash
$  mount -t smbfs -W workgroup //user:password@IPSERVER/shares /media/NAS
```

OU

```bash
$ gio mount smb://<server>/<share>
```

Autres méthodes [8 ways to mount smbfs samba file system in linux](https://www.linuxnix.com/8-ways-to-mount-smbfs-samba-file-system-in-linux/)

Penser à éditer `fstab' pour ajouter le serveur SMB en permanence. Ex:
```bash
$ vim /etc/fstab
//192.168.0.1/share1 /media/NAS smbfs rw,user,username=trivial,password=xylBJRS8 0 0
```

```bash
$  sudo mount -a
```

Pour mettre en place les sauvegardes, le plus simple est d'utiliser deja-dup qui est une interface graphique de duplicity. La sauvegarde est chiffré et incrémental sur une période d'une semaine. Il existe d'autre méthode de sauvegarde tel que avec Borg-backup ou bien rync.
```bash
$ sudo pacman -S deja-dup
```

### Par-feu ufw

Activation des logs (très utile pour la suite) :
```bash
$ sudo ufw logging on
```

Rejet par défaut des connexions entrantes :
```bash
$ sudo ufw default deny incoming
```

Autorisation des connexions sortantes :
```bash
$ sudo ufw default allow outgoing
```

Recherchement des règles du pare-feu pour finir :
```bash
$ sudo ufw reload
```

### Services Cloud

Vous trouverez plusieurs services de cloud gratuit tels que qcloud, Google drive, Dropbox. Nous allons installer MEGA qui est plus sécurisé ques les autres offres de cloud, le service de l'entrepreneur Kim Dotcom a évolué sur les principes d'anonymat et de vie privée sur les données qui sont stocké sur son serveur depuis l'affaire de megaupload.

Aller sur le site [https://mega.io/desktop](https://mega.io/desktop)

Sélectionner Arch Linux et télécharger l'application.

Pour installer sélectionner le package via:
```bash
$ sudo pacman -U <package>
```

### Service VPN Proton

Configurer un VPN. Installer le metapackage sur AUR:
```bash
$ yay -S protonvpn
```

CLI (Command Line Interface)

Login:
```bash
$ protonvpn-cli login <your_protonmail>
```

Connect to the VPN:
```bash
$ protonvpn-cli connect
```

Pour créer un compte protonVPN: [https://protonvpn.com/free-vpn/linux/](https://protonvpn.com/free-vpn/linux/)

Pour voir le status de la connexion:
```bash
$ protonvpn-cli status
```

Vérifier que votre adresse IP pointe sur le VPN: [https://www.whatismyip.com/fr/](https://www.whatismyip.com/fr/)