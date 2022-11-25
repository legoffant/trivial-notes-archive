Title: Futur machine de production Arch
Date: 2022-11-25 15:45
Category:Linux
Tags:arch, env
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

**ERRATUM**

Archinstall plante un peu chez moi, et le script créé de l'opacité dans l'installation dans le sens que l'on ne contrôle pas, on ne peut pas définir des paramètres avancé de chiffrement. Il vaut mieux faire l'installation manuel. Ou l'on sait quel algorithme de chiffrement on utilise.

Sway n'est pas encore assez stable pour de la machine de production, en particulier j'ai des soucis d'intégration avec Wofi/Tofi pour le dmenu. Le successeur de i3 n'est pas encore au point pour intégrer les composants sans passer des heures à paramêtrer. Il manque également de la documentation. Pas très user-friendly.

### Nouveau Projet basé sur Qt

Exigences systèmes:

* Robuste
* Minimaliste


On ne réinvente pas la roue on va utiliser LXQt qui sera notre base de projet toujours avec Qt. Comme ça pour les codeurs il est possible de développer des applications GUI en C++, avoir une base de travail commune dans mes projets. Je privilégie les environnements léger et LXQt utilise 350mo de RAM. Idéal pour un vieux Thinkpad avec 4GO de RAM. 

Stack:

* OS: [Arch Linux](https://archlinux.org/)
* Chiffrement: [dmcrypt-LUKS](https://fr.wikipedia.org/wiki/Dm-crypt)
* Bootloader: [systemd-boot](https://systemd.network/systemd-boot.html)
* Système de fichier: [BTRFS](https://fr.wikipedia.org/wiki/Btrfs)
* Shell: [Zsh](https://zsh.sourceforge.io/)
* Environnement: [LXQt](https://lxqt-project.org/)
* Windows Manager: [Open Box](http://openbox.org/wiki/Main_Page)
* Terminal: [Yakuake](https://wiki.archlinux.org/title/Yakuake)
* Prompt: [Oh-My-Zsh](https://ohmyz.sh/)
* File Manager: [Ranger](https://ranger.github.io/)
