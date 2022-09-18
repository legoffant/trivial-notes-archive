Title: Open Box environnement minimaliste
Date: 2022-09-18 14:26
Category:Linux
Tags:Openbox, Linux
Authors: Anthony Le Goff
Summary:

J'explore toujours les environnements minimalistes et customisables sous Arch Linux. Voici une configuration sous Open Box qui n'utilise que 500MB de RAM.

Pour installer changer à partir "installation du bureau XFCE4" de mon précedent poste [https://gist.github.com/legoffant/0a90e1067e3130711bf3f728a8a4a356](https://gist.github.com/legoffant/0a90e1067e3130711bf3f728a8a4a356)

Garder la configuration:

* Chiffrement LUKS
* Partionnement BTRFS
* Systemd-boot
* zramd

* Enlever guake terminal remplacer par alacritty.
* Ne pas oublier la configuration du clavier sous Xorg en français

### Installation du serveur X
```
sudo pacman -S xorg-server xorg-xinit xorg-fonts-misc
```

### Installation des composants

* Openbox Windows Manager
* Thunar File Manager
* Alacritty Terminal
* Compton Compositor

```
sudo pacman -S openbox thunar alacritty compton
```

### Configurer Openbox
```
mkdir -p ~/.config/openbox
cp -a /etc/xdg/openbox/ ~/.config/
```

This will copy 4 files into the ~/.config/openbox directory

    rc.xml
    menu.xml
    autostart
    environment

### Plugins pour Openbox

* obconf - The Openbox Configuration Manager, can be used for general configuration.
* lxappearance-obconf - The lxde Openbox Configuration Manager can be used to configure themes and other general customizations
* lxinput - Can be used to configure mouse and keyboard, allows mouse speed and acceleration to be adjusted.
* tint2 - custom taskbar
* MenuMaker - is a powerful tool that creates XML-based menus
* Nitrogen - Fast and lightweight wallpaper browser /setter for X
* Thin - Startup Manager

```
sudo pacman -S obconf menumaker tint2 lxinput lxappearance nitrogen thin
```

Configurer autostart pour que démarre au démarrage:
```
vim ~/.config/openbox/autostart.sh

tint2 &
nitrogen --restaure &
compton -b -c &
exec alacritty
```

Dans ce fichier on démarre la taskbar, le fond d'écran, le compositeur et un terminal

### Générer un menu démarrer

```
mmaker -v OpenBox3
```

### Thèmes et apparences 

Installer des thèmes supplémentaires:
```
sudo pacman -S openbox-themes
```

### Activer le login manager

Créer un script par defaut xinitrc:
```
cp /etc/X11/xinit/xinitrc ~/.xinitrc
```
Editer-le et ajouter:
```
vim ~/.xinitrc

exec openbox-session
```

Activer Slim:
```
sudo systemctl enable slim.service
```

Enfin:
```
reboot
```

### En complément: Trash & drive Management

* gvfs - volumes and have trash control
* udisks2 - Automatic mounting
* udiskie - Removable disk automounter using udisks


