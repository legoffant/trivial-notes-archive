Title:Le monde enchanté de la customisation (ricing) sous Linux 
Date: 2023-04-02 06:32
Category:Linux
Tags:custom, arch
Authors: Anthony Le Goff
Summary:

Je suis un partisan que l'outil informatique doit être un espace pour les créatifs qui veulent faire de l'art numérique ou coder leur propre outils. Des systèmes d'exploitations comme Windows ou MacOS ne sont pas customisable, par leur nature fermé de prendre l'utilisateur pour des arriérés et voler leur travail, l'environnement est prédéfini par les ingénieurs et ne laisse aucune possibilité d'accès au code source par leur nature propriétaire. Ce qui fait que le pecnot moyen n'a pas son mot à dire s'il trouve une fonction débile et voudrait l'améliorer.  

De ce fait on aurait besoin d'accès aux fichiers de configuration de l'environnement utilisateur, ce que l'on appel .dotfiles et l'utilisateur pourrait les modifier en trackant les changements via du control de version avec Git et les partager avec la communauté.  

Il faut donc un contrôle sur sa machine et comprendre comment est assembler les différents composants du système d'exploitation, que cela soit dans des buts de customisation tels qu'en cyberdefense et blue team, optimisation de la productivité et art numérique.  

Par sa nature GNU/Linux est le choix principal mais une distribution sort du lot pour fabriquer un système sur mesure: Arch Linux. La communauté à largement dépasser Gentoo dans les distributions minimal et simpliste.  

Le temple de la customisation auparavant dans les années 2000-10 était le site de [deviant-art](https://www.deviantart.com/). Puis est arrivé Reddit et [r/unixporn](https://www.reddit.com/r/unixporn/) qui permet de suivre l'état de l'art des "ricing" ou +50% des utilisateurs sont sous Arch Linux.  

Généralement la communauté est des programmeurs et codeurs en optimisant leur utilisation du terminal pour la productivité, réduire l'utilisation de la souris et utiliser des raccourcis clavier pour gérer leur environnement avec des [Tiling Windows Manager](https://fr.wikipedia.org/wiki/Gestionnaire_de_fen%C3%AAtres_par_pavage). Ils finissent à poster egalement des memes sur [r/linuxmasterrace](https://www.reddit.com/r/linuxmasterrace/wiki/index/) et crier sur les toits "I Use Arch BTW".  

Dans cette optique je vais vous présenter ma configuration nommé "broutage de chaton" pour p0wn à tout les coups et humilier votre entourage par votre maîtrise de l'informatique en invoquant "Pedobear" en mode fanatique.  

![mineur](images/mineur.jpg)

### Prérequis  

Il faudra faire l'installation d'Arch Linux en manuel sans l'utilisation du script archinstall en intégrant:  

*   Chiffrement: dm-crypt / LUKS  
    
*   Système de fichier pour les snapshots du système: BTRFS  
    
*   UEFI Secure Boot (signé)  
    
*   swap zram  
    

Je conseil l'utilisation du combo [arch-secure-boot](https://github.com/maximbaz/arch-secure-boot) + [snap-pac](https://github.com/wesbarnett/snap-pac) dans les bonnes pratiques de sécurité du système et de restauration. Si vous n'utilisez pas le secure boot, autant utiliser un bootloader léger tel que systemd-boot.  

### Affichage Server  

il est nécessaire pour démarrer une interface utilisateur graphique GUI. L'ancien se nomme X.org et commence à être dépasser dans l'optique nous allons utiliser son successeur: Wayland qui se veut plus facile à développer et extensif avec une facilité à maintenir et plus sur.  

### Affichage Driver  

Normalement vous n'aurez pas besoin d'intégrer des drivers spécifiques avec Intel et AMD car ceci est pris en charge par [Kernel Mode Setting KMS](https://wiki.archlinux.org/title/Kernel_mode_setting). Seulement NVIDIA qui reste propriétaire nécessite la configuration en manuel. NVIDIA et Linux toujours un peu en guerre.

![nvidia](images/nvidia-linus.jpg)

### Compositor  

Le compositor est un élément essentiel qui permet l'affichage de fenêtre mais également la transparence et les animations, pour Wayland nous utilisons un Tiling Windows Manager: [hyprland](https://hyprland.org/). Il faudra utiliser une barre d'état tel que Waybar et ces extensions comme Eww pour les Widgets.  

### Gestionnaire d'affichage  

Nous allons utiliser une configuration minimaliste qui gère Wayland. Pour cela on utilise un TUI (Terminal UI) en utilisant [Ly](https://github.com/fairyglade/ly). Celui-ci gère votre authentification sur le système et lancement de l'environnement. Vous pouvez également utiliser [Lemurs](https://github.com/coastalwhite/lemurs).  

### Terminal Emulateur  

La tendance est à l'utilisation de [Kitty](https://sw.kovidgoyal.net/kitty/) qui est léger et rapide propulsé par le GPU. Il intègre en natif un gestionnaire de fenêtre ou l'on peut créer des tabs et splitter le terminal ce qui fait que l'on peut ce passer de tmux comme multiplexer. Vous pouvez le customiser avec le gestionnaire de plugins [Kittens](https://sw.kovidgoyal.net/kitty/kittens_intro/#kittens).  

\> Shell  

L'utilisation du shell [fish](https://fishshell.com/) est conseillé car il intègre en natif des fonctions tels que  

*   autosuggestions en ligne basées sur l'historique ;
*   complément de tabulation utilisant les données des pages de manuel ;  
    
*   mise en évidence de la syntaxe ;
*   support intuitif des caractères génériques ;
*   configuration basée sur le Web ;
*   une saine écriture de scripts.  
    
*   Un gestionnaire de plugins: [fisher](https://github.com/jorgebucaran/fisher)  
    

  

\> Prompt  

L'invité de commande du shell peut-être customisé pour intégrer des informations tels que les branches sur Git, version logiciel, runtime, icones et symboles, etc. Nous allons utiliser [starship.rs](https://starship.rs/) et vous pouvez explorer les [presets](https://starship.rs/presets/).  

\> Autres outils en ligne de commande  

*   [duf](https://github.com/muesli/duf) Free disque usage  
    
*   [ripgrep](https://github.com/BurntSushi/ripgrep) Recherche récursive de pattern de Regex dans un dossier  
    
*   [bat](https://github.com/sharkdp/bat) cat clone avec coloration syntaxique et Git intégration  
    
*   [tldr](https://tldr.sh) Terminal companion améliorant les man pages avec example de ligne de commande  
    
*   [cmus](https://github.com/cmus/cmus) CLI audio player  
    
*   [yt-dlp](https://github.com/yt-dlp/yt-dlp) Outil de téléchargement de video sur Youtube, etc.  
    
*   [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli) Utiliser chatGPT via l'API d'OpenAi  

*   [ufw](https://wiki.archlinux.org/title/Uncomplicated_Firewall) Uncomplicated Firewall

*   [ssh](https://wiki.archlinux.org/title/Secure_Shell) Secure Shell est un protocole réseau chiffré pour ce connecter à distance sur un serveur. Voir scp et sftp
    

NOTA: pour partager un fichier / Pastebin utilisez la commande:  

```
$ cat FILE | curl -F 'sprunge=<-' http://sprunge.us`
```

### Apps Launcher  

Nous faisons tout dans un terminal sans utiliser un menu pour lancer des applications. Pour cela nous allons utiliser un outil de recherche de fichier et de binaire "fuzzy finder" tel que [fzf](https://github.com/junegunn/fzf) comme extension du shell.  

### Information système  

Pour gérer les processus et visualiser l'utilisation des ressources [htop](https://htop.dev/) reste un outil simple en CLI. Pour visualiser la configuration de l'environnement: [neofetch](https://github.com/dylanaraps/neofetch)  

### Gestionnaire de fichier  

Pour gérer ces fichiers et dossiers en CLI on utilise une extension de l'outil tree qui ce nomme [broot](https://dystroy.org/broot/).  

### Editeur de fichier  

On optimise l'utilisation du terminal pour éditer du texte et du code en particulier pour du travail à distance sur un serveur en administrateur mais également en utilisant peu de ressource système sur la charge CPU / RAM. La tendance est l'utilisation du successeur de Vim nommé [Neovim](https://neovim.io/) parmi les développeurs. On peut transformer [Neovim](https://neovim.io/) en EDI en intégrant des plugins tels que:  

*   CoC  
    
*   Telescope  
    
*   Barbar  
    
*   Vim-fugitive  
    
*   NerdTree  
    
*   Vim-surround  
    
*   Tagbar  
    
*   Delimitmate  
    
*   Vim-airline  
    
*   Vim-devicons  
    
*   Vim-ai  
    

### Fonts  

On note l'utilisation de:  

*   adobe-source-han-sans-otc-fonts (sinogramme asiatique et l'utilisation de [fcitx](https://github.com/fcitx/fcitx))  
    
*   noto-fonts  
    
*   noto-fonts-emoji  
    
*   Nerd-fonts  
    

IRC  

Client IRC pour tchater en CLI: [weechat](https://weechat.org/). D'autres se tournerons vers Matrix et Discord considéré comme plus moderne même si la communauté FOSS et les hackers sont toujours sur IRC.  

### Themes et Icones  

Il existe des classiques tels que Catppuccin, Gruvbox ou encore Neon aux effets cyberpunk. Un repo de la communauté sur hyprland est disponible sur Github: [theme-repo](https://github.com/hyprland-community/theme-repo)  

### AUR Helper  

Pour l'utilisation de AUR, les paquets logiciels de la communauté, j'ai ma préférence pour [yay](https://github.com/Jguer/yay) qui a remplacé le projet obsolète de yaourt en complément de pacman.  

### Cloud distant et sauvegarde  

Vous pouvez utiliser l'outil [rclone](https://rclone.org/) en CLI qui permet d'accéder à un cloud distant (AWS S3, GDrive, NAS, etc) et de faire des sauvegardes chiffrés. Même si vous faites des snapshots du système, ayez une sauvegarde locale et à distance en particulier vos documents /home. D'autres options sont possible tel que le traditionnel Rsync mais aussi Borg ou Duplicity.  

References:  

*   dotfiles [https://wiki.archlinux.org/title/Dotfiles](https://wiki.archlinux.org/title/Dotfiles)  
    
*   Configuration for Arch Linux, Hyprland, kitty, kakoune, zsh and more + scripted installation guide [https://github.com/maximbaz/dotfiles](https://github.com/maximbaz/dotfiles)  
    
*   My journey of ricing Arch Linux [https://peterpf.dev/posts/ricing-arch-linux/](https://peterpf.dev/posts/ricing-arch-linux/)  
    
*   Awesome hyprland [https://github.com/hyprland-community/awesome-hyprland](https://github.com/hyprland-community/awesome-hyprland)  
    
*   Curation d'outils fish [awsm.fish](https://github.com/jorgebucaran/awsm.fish)