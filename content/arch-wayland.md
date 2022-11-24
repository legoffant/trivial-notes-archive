Title: Futur machine de production Arch
Date: 2022-11-24 18:11
Category:Linux
Tags:arch, wayland
Authors: Anthony Le Goff
Summary:



*Nota:*

Refonte du système d'exploitation et ces composants pour intégrer des innovations et renforcer la sécurité.

### Automatisé avec le script `archinstall`

* OS: [Arch Linux](https://archlinux.org/)
* Chiffrement: [dmcrypt-LUKS](https://fr.wikipedia.org/wiki/Dm-crypt)
* Bootloader: [systemd-boot](https://systemd.network/systemd-boot.html)
* Système de fichier: [BTRFS](https://fr.wikipedia.org/wiki/Btrfs)

### Post-install

* Shell: [Zsh](https://zsh.sourceforge.io/)
* Wayland compositor: [Sway](https://swaywm.org/)
* Bar: [Waybar](https://github.com/Alexays/Waybar)
* Launcher: [Wofi](https://hg.sr.ht/~scoopta/wofi)
* Terminal: [Alacritty](https://alacritty.org/)
* Prompt: [Oh-My-Zsh](https://ohmyz.sh/)
* File Manager: [Ranger](https://ranger.github.io/)
* Notification daemon: [Mako](https://wayland.emersion.fr/mako/)
* Screenshot: [Grim + Slurp](https://wayland.emersion.fr/grim/)


Le but est de simplifier la réinstallation du système en cas de plantage et d'automatiser un peu. Cela pourrait être fait dans un script bash personnalisé. 