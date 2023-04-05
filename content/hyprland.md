Title:Mon bureau hyprland
Date: 2023-04-05 11:08
Category:Linux
Tags:hyprland
Authors: Anthony Le Goff
Summary:

Sous Arch Linux lancer le script `archinstall` et définir:

* Chiffrement dm-crypt / LUKS
* Système de fichier BTRFS
* Bootloader systemd-boot

Post-installation:

Prérequis avoir `base-devel`, `git` et `wget`

Installation AUR helper:
```
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

Listing des packages et dépendances:
```
yay -S hyprland waybar-hyprland eww-wayland mako swaybg \
       kitty fish starship fzf neovim broot \
       pipewire wireplumber \
       cliphist grimblast-git ffmpeg wf-recorder viewnior \
       polkit-kde-agent xdg-desktop-portal-hyprland-git \
       qt5-wayland qt6-wayland \
       wlogout swaylock-effects ly \
       webcord weechat fractal \
       cmus spotify-tui vlc \
       cmatrix neofetch htop \
       ripgrep duf tldr \
       python python-pip \
       firefox obsidian \
       adobe-source-han-sans-otc-fonts noto-fonts noto-fonts-emoji nerd-fonts-git \
       gtk-cyberpunk-neon-theme-git \
       fcitx-im \
       udiskie \
```

Installation de youtube-dl:
```
pip install yt-dlp
```

Autostart authentification agent:
```
exec-once=/usr/lib/polkit-kde-authentication-agent-1
```

Activer le service au démarrage ly:
```
sudo systemctl enable ly.service
```

Configurer fish comme shell par défault:
```
echo /bin/fish | sudo tee -a /etc/shells
chsh -s /bin/fish
```

Editer fichier de configuration:
```
nvim ~/.config/hypr/hyprland.conf
```

Lancer automatiquement le montage USB, etc:
```
exec-once = udiskie &
```
Clavier configuration ajouter:
```
device:nom-clavier {
    kb_layout=fr,us
}
```

Commande pour switcher entre les claviers:
```
hyprctl switchxkblayout nom-clavier fr
```

