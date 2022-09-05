Title: ARCH LINUX INSTALL: BTRFS - CHIFFREMENT - UEFI - XFCE - Timeshift
Date: 2022-09-04 14:49
Category:Linux
Tags:arch, xfce, luks, btrfs
Authors: Anthony Le Goff
Summary:

by Trivial

Mise à jours en 2022 de mon installation d'Arch Linux avec quelques nouveautés en particulier la prise en charge de snapshot avec BTRFS. 

nota:  désactiver dans le bios le secure boot pour booter en USB.
Vérifier le démarrage UEFI.

### pre-check configuration 

Charger le clavier français en tapant "loqdkeys fr"
```
loadkeys fr
```

Verifier boot mode
```
ls /sys/firmware/efi/efivars    (Si le répertoire existe, l'ordinateur supporte l'efi)
```

### Connexion au réseau

Vérifier le nom du reseau et si celui-ci est up
```
ip addr show
```

vérifier la connexion internet
```
ping -c 2 google.com
```

Connexion au wifi
```
iwctl
```
affichage du prompt [IWD]#
```
[iwd]# device list
[iwd]# station device scan
[iwd]# station device get-networks
[iwd]# station device connect SSID
```

### Check les disques

Vérifier le nom de votre disque dur ou SSD
```
lsblk
```

### Partitionnement

Destruction des données sécurisées du disque
```
shred -v -n 1 /dev/sda
```

Utilitaire de partitionnement
```
gdisk /dev/sda
```
Créer une nouvelle table de partition GPT

Mise en place de la table de partition:
```
/dev/sda1 EFI ef00 512MB
/dev/sda2 Linux 8300
```

Formatage de la partition EFI
```
mkfs.fat -F32 /dev/sda1
```

### Chiffrement 
```
cryptsetup --cipher aes-xts-plain64 --hash sha512 --use-random --verify-passphrase luksFormat /dev/sda2
```

Ouverture du container chiffré:
```
cryptsetup luksOpen /dev/sda2 root
```

Formater la partition root
```
mkfs.btrfs /dev/mapper/root
```

Monter les partitions:
```
mount /dev/mapper/root /mnt
cd /mnt
```

Créer les subvolumes
```
btrfs subvolume create @
btrfs subvolume create @home
btrfs subvolume create @snapshots
```

Démonter la partition
```
umount /mnt
```

Remonter le subvolume @
```
mount -o noatime,space_cache=v2,compress=zstd,ssd,discard=async,subvol=@ /dev/mapper/root /mnt
```

Créer les dossiers boot et home
```
mkdir /mnt/{boot,home,.snapshots}
mkdir /mnt/boot/efi
```

Monter le subvolume @home
```
mount -o noatime,space_cache=v2,compress=zstd,ssd,discard=async,subvol=@home /dev/mapper/root /mnt/home
```

Monter le subvolume @snapshots
```
mount -o noatime,space_cache=v2,compress=zstd,ssd,discard=async,subvol=@snapshots /dev/mapper/root /mnt/.snapshots
```

Monter la partition EFI
```
mount /dev/sda1 /mnt/boot/efi
```


### Système de base
```
pacstrap /mnt base linux linux-firmware btrfs-progs git vim intel-ucode ntp
```

Générer fstab
```
genfstab -L -p /mnt >> /mnt/etc/fstab
```

Chrooter l'environnement
```
arch-chroot /mnt
```

Editer mkinitcpio
```
vim /etc/mkinitcpio.conf
	Hooks=(base udev autodetect keyboard keymap consolefont modconf block encrypt filesystems btrfs fsck)
```

Générer initramfs
```
mkinitcpio -p linux
```

Nom de la machine
```
vim /etc/hostname
```
Configuration de local paramétrage des langues
```
vim /etc/locale.gen
en_US.UTF-8 UTF-8
fr_FR.UTF-8 UTF-8
```
Génération du fichier
```
locale-gen
```
Configuration des langues par defaut
```
vim /etc/locale.conf
LANG="fr_FR.UTF-8"
LC_COLLATE="fr_FR.UTF-8"
```
Exporter le langage actuel pour création dans initramfs
```
export LANG=fr_FR.UTF-8
```
Console, fonts, clavier azerty
```
vim /etc/vconsole.conf
KEYMAP=fr-pc
FONT=
FONT_MAP=
```

Assigne le fuseau horaire
```
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime 
```

Active la synchronisation par serveur NTP
```
timedatectl set-ntp true
```

```
hwclock --systohc
```

Mot de passe super-administrateur root
```
passwd
```

Installation de paquets supplémentaires:
```
pacman - S grub efibootmgr networkmanager network-manager-applet dialog wpa_supplicant reflector base-devel linux-headers avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils inetutils dnsutils cups hplip alsa-utils pipewire pipewire-alsa pipewire-pulse pipeware-jack pavucontrol bash-completion openssh rsync acpi acpi_call tlp ipset ufw sof-firmware nss-mdns acpid ntfs-3g terminus-font nano man-db man-pages zip p7zip unzip tar htop tmux wget pciutils lshw syslog-ng
```

Driver carte graphique, openGL, touchpad
```
pacman -S xf86-video-intel mesa xf86-input-libinput
```

Installation de QEMU/KVM pour la virtualisation
```
pacman -S virt-manager qemu qemu-arch-extra edk2-ovmf bridge-utils dnsmasq vde2 openbsd-netcat
```

### Configuration de GRUB

Modification du fichier de configuration grub, appel de la partition root chiffrée
```
vim /etc/default/grub
GRUB_CMDLINE_LINUX="cryptdevice=/dev/sda2:root root=/dev/mapper/root rootflags=subvol=@ rw quiet"

GRUB_ENABLE_CRYPTODISK=y
```

```
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
```

```
grub-mkconfig -o /boot/grub/grub.cfg
```

### Activer les services systemD

```
systemctl enable NetworkManager
systemctl enable cups.service
systemctl enable sshd
systemctl enable avahi-daemon
systemctl enable tlp
systemctl enable reflector.timer
systemctl enable libvirtd
systemctl enable acpid
systemctl enable ufw
```

### Créer un utilisateur

```
useradd -m trivial
passwd trivial
```

```
usermod -aG libvirt trivial
```

Ajout dans sudoers de l'utilisateur
```
echo "trivial ALL=(ALL) ALL" >> /etc/sudoers.d/trivial
```

Démonter et reboot
```
exit
umount -R /mnt
reboot
```

### Post-installation

Check ip adresse
```
ip a
```

Connexion au wifi via Networkmanager TUI
```
nmtui
```

Synchronisation repository MAJ
```
sudo pacman -Sy
```

Installation AUR Helper
```
mkdir sources 
cd sources 
git clone https://aur.archlinux.org/yay.git 
cd yay 
makepkg -si 
```

Installation de timeshift et zramd
```
yay -S timeshift-bin timeshift-autosnap zramd
```

```
sudo systemctl enable zramd.service
```

Vérification que la swap est active:
```
lsblk
```

Configuration de reflector
```
reflector --verbose --country 'France' -a 6 -p https --sort rate --save /etc/pacman.d/mirrorlist
```

```
sudo pacman -Syy
```

### Installation du bureau XFCE4

```
sudo pacman -S xorg xfce4 xfce4-goodies lightdm-gtk-greeter-settings gtk-xfce-engine
```

Activer le gestionnaire de démarrage
```
sudo systemctl enable lightdm
```

Editer le fichier de configuration ligthdm
```
sudo nano /etc/lightdm/lightdm.conf
# edit a la ligne
greeter-session = lightdm-gtk-greeter
```

Configuration de xinitrc
```
echo "exec startxfce4" > ~/.xinitrc
```

Installation de fonts
```
sudo pacman -S ttf-ms-fonts ttf-dejavu ttf-bitstream-vera adobe-source-han-sans-otc-fonts noto-fonts noto-fonts-emoji ttf-liberation ttf-droid tex-gyre-fonts
```

NOTA: Pour activer la prise en charge Pinyin, utiliser fcitx.

**Codec Multimédia**

Nous allons installer l’ensemble des greffons gstreamer qui est le framework utilisé par de nombreux environnements de bureau pour gérer le multimedia.
```
sudo pacman -S gst-plugins-{base,good,bad,ugly} gst-libav
```

Installation de navigateurs web
```
sudo pacman -S firefox chromium
```

```
reboot
```

### Configuration des applications

Changer de terminal en utilisant Guake via la touche F12
```
sudo pacman -S guake
```
Pour que Guake démarre au démarrage de l'environnement XFCE:
```
cp /usr/share/applications/guake.desktop /etc/xdg/autostart/
```

#### Configuration de Oh-my-Zsh 

Install Zsh
```bash
$ yay -S zsh oh-my-zsh-git
```

Mettre zsh shell par default
```bash
$ chsh -l
$ chsh -s /usr/bin/zsh
```

Install et activer le thème powerlevel10k
```bash
$ yay -S --noconfirm zsh-theme-powerlevel10k-git
$ echo 'source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```

Install nerd fond hack
```bash
yay -S nerd-fonts-hack
```

Fichier de configuration ~/.zshrc
```bash
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation.
ZSH=/usr/share/oh-my-zsh/

export DEFAULT_USER="anth"
export TERM="xterm-256color"
export ZSH=/usr/share/oh-my-zsh
export ZSH_POWER_LEVEL_THEME=/usr/share/zsh-theme-powerlevel10k

source $ZSH_POWER_LEVEL_THEME/powerlevel10k.zsh-theme

plugins=(archlinux 
	bundler 
	docker 
	jsontools 
	vscode web-search 
	tig 
	gitfast 
	colored-man-pages
	colorize 
	command-not-found 
	cp 
	dirhistory 
	sudo
	zsh-syntax-highlighting
	zsh-autosuggestions) 
# /!\ zsh-syntax-highlighting and then zsh-autosuggestions must be at the end

source $ZSH/oh-my-zsh.sh

# Uncomment the following line to disable bi-weekly auto-update checks.
DISABLE_AUTO_UPDATE="true"

ZSH_CACHE_DIR=$HOME/.cache/oh-my-zsh
if [[ ! -d $ZSH_CACHE_DIR ]]; then
  mkdir $ZSH_CACHE_DIR
fi

source $ZSH/oh-my-zsh.sh
```

Cloner les repos de zsh-syntax-highlighting et zsh-autosuggestions

Dossier de travail: /usr/share/oh-my-zsh/customs/plugins

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git zsh-syntax-highlighting
```
redémarrer zsh

#### Outil de recherche et lanceur Sinapse basé sur Zeitgeist

Installation de synapse + configuration sur le raccourci superL
```
sudo pacman -S synapse
```

#### Application pour développeur et designer

```
sudo pacman -S keepass gimp vlc filezilla inkscape qbittorrent weechat cmus gcalculator baobab neovim discord veracrypt kazam yt-dlp calibre zim neofetch freemind
```

Documentation des langages
```
yay -S zeal
```

Installation des outils de développeurs C/C++, Clang, Python
```
sudo pacman -S llvm clang python python-pip virtualenv nodejs
```

Installation de Jedi autocompletion pour python
```
pip install jedi
```

Editeur de texte VSCodium
```
yay - S vscodium-bin
```

Installation de Java Eclipse
```
sudo pacman -S jdk-openjdk
yay -S eclipse-java
```

**Configuration de Neovim**

Installation du gestionnaire de plugin "vim-plug" cf: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


init.vim
```
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
```
curl -O https :// blackarch .org/strap.sh
sha1sum strap.sh # doit etre egal a d062038042c5f141755ea39dbd615e6ff9e23121
sudo chmod +x strap.sh
sudo ./ strap.sh
```

```
sudo pacman -S blackman
```

Installation des outils basics
```
sudo blackman -i nmap impacket whireshark tcpdump ruby hashcat john proxychains-ng exploitdb httpie metasploit armitage bind-tools radare2 sqlmap wpscan xclip beef set ufonet
```

Configuration WordLists
```
mkdir -p /usr/share/wordlists
wget -q https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz -O /usr/share/wordlists/rockyou.txt.tar.gz
wget -q https://github.com/danielmiessler/SecLists/raw/master/Discovery/Web-Content/common.txt -O /usr/share/wordlists/common.txt
```

#### Outils pour écrivain et chercheur
```
sudo pacman -S ghostwriter wkhtmltopdf pandoc libreoffice-still libreoffice-still-fr hunspell hunspell-fr texmaker manuskript
```

Extension Grammalecte et gestion de bibliographie
```
yay -S zotero libreoffice-extension-grammalecte-fr
```

#### Calcul numérique et scientifique (remplace Matlab)

```
python -m pip install jupyter scipy numpy matplotlib pandas ipython
```

Calcul Formel
```
sudo pacman -S sagemath
```

### Sauvegarde

Installation du client SAMBA pour thunar
```
sudo pacman -S smbclient gvfs-smb
```
Redémarrer le PC pour prendre en compte la découverte du réseau local.

Ensuite rechercher votre serveur dans thunar en tapant:
```
smb://192.168.X.X
```

Pour cela modifier en fonction d'IP de votre serveur.

Pour mettre en place les sauvegardes, le plus simple est d'utiliser deja-dup qui est une interface graphique de duplicity. La sauvegarde est chiffré et incrémental sur une période d'une semaine. Il existe d'autre méthode de sauvegarde tel que avec Borg-backup ou bien rync.
```
sudo pacman -S deja-dup
```

### Par-feu ufw

Activation des logs (très utile pour la suite) :
```
sudo ufw logging on
```

Rejet par défaut des connexions entrantes :
```
sudo ufw default deny incoming
```

Autorisation des connexions sortantes :
```
sudo ufw default allow outgoing
```

Recherchement des règles du pare-feu pour finir :
```
sudo ufw reload
```

### Services Cloud

Vous trouverez plusieurs services de cloud gratuit tels que qcloud, Google drive, Dropbox. Nous allons installer MEGA qui est plus sécurisé ques les autres offres de cloud, le service de l'entrepreneur Kim Dotcom a évolué sur les principes d'anonymat et de vie privée sur les données qui sont stocké sur son serveur depuis l'affaire de megaupload.

Editer le fichier de configuration de pacman pour ajouter le repository officiel de MEGA
```
sudo nano /etc/pacman.conf
```
Ajoutez ces lignes:
```
###Repository oficial MEGA###
 
[DEB_Arch_Extra]
SigLevel = Optional TrustAll
Server = https://mega.nz/linux/MEGAsync/Arch_Extra/$arch
```

Mettre à jour pacman
```
sudo pacman -Sy
```

Installation du logiciel et de l'intégration avec Thunar
```
sudo pacman -S megasync thunar-megasync
```

### Service VPN Proton

Configurer un VPN. Installer le metapackage sur AUR:
```
yay -S protonvpn
```

CLI (Command Line Interface)

Login:
```
protonvpn-cli login <your_protonmail>
```

Connect to the VPN:
```
protonvpn-cli connect
```

Pour créer un compte protonVPN: [https://protonvpn.com/free-vpn/linux/](https://protonvpn.com/free-vpn/linux/)

Pour voir le status de la connexion:
```
protonvpn-cli status
```

Vérifier que votre adresse IP pointe sur le VPN: [https://www.whatismyip.com/fr/](https://www.whatismyip.com/fr/)