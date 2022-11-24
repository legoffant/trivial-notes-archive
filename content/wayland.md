Title: Début de migration sur Wayland
Date: 2022-11-24 01:34
Category:Linux
Tags:wayland, sway
Authors: Anthony Le Goff
Summary:

Je m'intéresse toujours à upgrade ma configuration un peu vieillissante d'Arch linux. Je m'attaque à Wayland. J'essaye de prototyper dans une machine virtuelle sous QEMU/KVM, j'ai quelques erreurs, j'arrive à avoir un bureau, un curseur de souris, mais je ne peux pas cliquer, faire de clique droit ni utiliser les raccourcis clavier. C'est embêtant. la VM ne prend en charge, j'essaye de configurer sans succès.

Configuration en test:

```
OS: Arch Linux
Shell: Zsh
Wayland compositor: Sway
Bar: Waybar
Launcher: Wofi
Terminal: Alacritty
Prompt: Oh-My-Zsh
File Manager: Ranger
```

Sous virt-manager il faut configurer "Display" sous `QXL` au lieu de `virtio` pour la VM. 

### Lancer une installation archlinux

Puis dans le terminal configurer rapidement avec le script d'installation minimal sans environnement de bureau:

```
archinstall
```

### Post-install

Après un restart installer les paquets nécessaires:

```
sudo pacman -S sway alacritty waybar wofi ranger xorg-xwayland xorg-xlsclients qt5-wayland glfw-wayland polkit-qt5
```

Copiez le fichier de configuration de Sway:

```
mkdir ~/.config
cd ~/.config
mkdir sway
cd sway
cp /etc/sway/config .
```

Installer nano et vim si nécessaire pour éditer le fichier de configuration

Pour rendre visible le curseur de souris:

```
export WLR_NO_HARDWARE_CURSORS=1
```

Pour lancer le windows manager Sway:

```
sway
```

Une fois sur l'écran en GUI normalement on devrait accéder aux touches claviers, et là je coince un peu, j'ai tenté de configurer le clavier en français sans succès. Normalement en lançant `super+enter` on lance un terminal. La touche `super` est la touche Windows. Et j'ai l'impression que le clavier ne transfert pas mes commandes quand je suis sur Sway. 

### Sécurité

Wayland isole les applications en GUI, ainsi il est plus sécurisé que le serveur X.org.

### Programmation

Sway et Wayland utilise Qt, il est donc possible de développer des applications en C++.

### En phase de test

Il est possible que j'utilise mon second Thinkpad pour tester le déploiement de Wayland jusqu'à obtenir une machine de production stable remplaçant ma configuration. J'ai peu de fichier important, je peux très bien relancer une installation. Le seul hic serait la compatibilité du vpn Proton. J'ai un petit doute. 