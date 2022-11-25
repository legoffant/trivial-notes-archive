Title: Futur machine de production Arch
Date: 2022-11-25 15:45
Category:Linux
Tags:arch, env
Authors: Anthony Le Goff
Summary:

Mise à jour de ma machine de production, je partage les meilleurs outils à l'éducation numérique open-source. Pour faire partie de l'élite des développeurs et ingénieurs sous GNU/Linux suivez le Guide et on commence très tôt,faîte un club d'informatique et entraidez-vous, cela vous côutera 250€ à investir dans un PC ThinkPad reconditionné sur BackMarket pour devenir des rockstars en informatique, petit rappel [Linux Pas à Pas](https://legoffant.github.io/linux-pas-a-pas.html) en prélude et les [60 notions essentielles en informatique](https://legoffant.github.io/60-notions-essentielles-en-codage-informatique.html).


*Nota:*

**ERRATUM**

Arch Linux

Archinstall plante un peu chez moi, et le script créé de l'opacité dans l'installation dans le sens que l'on ne contrôle pas, on ne peut pas définir des paramètres avancé de chiffrement. Il vaut mieux faire l'installation manuel. Ou l'on sait quel algorithme de chiffrement on utilise.

Sway et Wayland n'est pas encore assez stable pour de la machine de production, en particulier j'ai des soucis d'intégration avec Wofi/Tofi pour le dmenu. Le successeur de i3 n'est pas encore au point pour intégrer les composants sans passer des heures à paramêtrer. Il manque également de la documentation. Pas très user-friendly.

### Nouveau Projet basé sur Qt

Exigences systèmes:

* Robuste
* Minimaliste


Mon projet de machine de production Linux est à jour. Dans cette liste les éléments open-source pour une productivité efficace. Elle a la particularité d'utiliser peu de ressource, avec des programmes minimalistes qui permet de faire tourner sur des vieux PC à 250€ en reconditionné pour 4GO ram. L'environnement LXQt ne prenant que 340mo en RAM. La machine est orienté pour la programmation en C/C++, Python, Ruby, Java et bash. Qt permet de développer des applications GUI en C++.

C'est une configuration Arch Linux facile à installer, j'ai recherché la simplicité et la robustesse dans un cadre minimaliste. Dans mon projet j'éduque aux outils de travail des développeurs et ingénieurs pour la jeunesse, la reconversion et les projets de start-up ou je défini du matériel de production stable en intégrant quelques innovations.


**CONSIDERER CELA COMME UN STANDARD COMME BASE DE TRAVAIL**

Vous devez connaître tous ces outils, je ferai plus tard un supplément pour la recherche en cybersécurité.


Stack:

* OS: [Arch Linux](https://archlinux.org/)
* Chiffrement: [dmcrypt-LUKS](https://fr.wikipedia.org/wiki/Dm-crypt)
* Bootloader: [systemd-boot](https://systemd.network/systemd-boot.html)
* Système de fichier: [BTRFS](https://fr.wikipedia.org/wiki/Btrfs)
* Shell: [Zsh](https://zsh.sourceforge.io/)
* Environnement: [LXQt](https://lxqt-project.org/)
* Windows Manager: [Open Box](http://openbox.org/wiki/Main_Page)
* Terminal: [QTerminal](https://github.com/lxqt/qterminal)
* Prompt: [Oh-My-Zsh](https://ohmyz.sh/)
* File Manager: [Ranger](https://ranger.github.io/) (term)
* Launcher: [Synapse](https://archlinux.org/packages/community/x86_64/synapse/)
* Virtualisation: [Virt-Manager QEMU/KVM](https://virt-manager.org/)
* Lecteur audio: [CMUS](https://cmus.github.io/) (term)
* Lecteur video: [Vlc](https://www.videolan.org/vlc/)
* IRC: [Weechat](https://weechat.org/) (term)
* Editeur de texte: [Neovim](http://neovim.io/) (term)
* Contrôle de version: [Git](https://git-scm.com/) (term)
* Notepad: [Leafpad](https://archlinux.org/packages/extra/x86_64/leafpad/)
* Calculatrice: [Galculator](https://archlinux.org/packages/community/x86_64/galculator/)
* P2P Torrent: [Qbittorrent](https://www.qbittorrent.org/)
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
* Editeur LaTex: [Texmaker](https://www.xm1math.net/texmaker/)
* Office: [Cryptpad](https://cryptpad.fr/)