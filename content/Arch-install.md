Title:Introduction à l'extremisme sous GNU/Linux
Date: 2021-05-12 19:40
Category:Linux
Tags:linux, arch, configuration, manjaro
Authors: Anthony Le Goff
Summary:

## A Propos

Toi, tu as entendu parler d'Arch? Cela commence comme ça, c'est un murmure dans la communauté des libristes. On en parle pas trop car c'est limite légendaire que certain utilisateurs de GNU/Linux seraient capable de construire eux-même leur propre système d'exploitation. Mais combien sont-ils? On estime que 5 millions d'archers sont comptabiliser parmis les 90-100 millions d'utilisateurs de GNU/Linux, dont 40 millions sous Ubuntu. Soit environ 4% d'archers. Pourtant c'est l'une des communautés les plus actives avec la devise de la distribution comme principe:
```
KISS: Keep It Simple, Stupid
```

La distribution est construite comme un LEGO. L'utilisateur va construire son système d'exploitation sur mesure selon ces besoins. Elle est adapté aux utiliteurs recherchant à customiser leur environnement. Tout ce paramètre, on apprend les bases comment GNU/Linux fonctionne. Pour toutes personnes voulant apprendre à utiliser en profondeur, tout en connaissant les entrailles du système c'est un passage obligé. On peut dire même que c'est un rituel pour les hackers. Je rappel que les hackers démontent les systèmes informatiques pour comprendre le fonctionnement. On rentre totalement dans la logique. On a un accès simplifier à la création de système d'exploitation à la demande. D'autres se tourneront vers Gentoo ou l'a aussi on construit son système en compilant depuis les sources. On peut-être rassurer que aucun malware ou spyware soit intégrer dans le système. 

Alors qu'es ce qui fait qu'il y a plus d'utilisateurs sur Arch que Gentoo. Principalement la communauté. Le wiki est surement la seconde plus grande source d'information après celui d'Ubuntu. Et il existe sous Arch AUR(Arch User Repository) qui est le dépot de logiciel par les utilisateurs. Ainsi des programmes non disponible dans les dépots officiels sont souvent portée sous AUR. 

Arch est particulièrement adapté pour la mise en place dans un groupe de recherche en innovation radicale à la pointe de la Tech.Le logiciel libre accélère l'innovation par la libre circulation de l'information. On peut compter sur ces hackers utilisant les dépots de [Blackarch](https://www.blackarch.io/) pour assurer la cybersécurité. Encore aujourd'hui dans les branches les plus extremistes il y a un débat de choix de distribution entre Debian "Kali" et Arch "Blackarch" parmis la communauté des hackers. On peut considéré que les archers sont plus en marge avec une connaissance approfondi des systèmes. Cette connaissance leur permet d'avoir des compétences avancés tel que le partitionnement de disque et la protection de donnée en introduisant une sécurité militaire sur un poste de travail. Rien n'empêche un archer de chiffrer ces partitions avec des algorithmes avancés. On peut donc ce poser la question si des archers ne sont pas plus aptes à travailler dans des environnements contraint de recherche et développement ou la protection de l'information est nécessaire.

## Extremisme libertarien

Bill Gates à longtemps consideré les libristes et le logiciel libre comme un groupuscule extremiste faisant allusion à du communisme. Pour l'anecdote de la rupture dans les années 90 de Microsoft et le discours de Richard Stallman. D'ailleurs on n'a jamais vu de milliardaire étant un defenseur des 4 libertés fondamentales du logiciel libre. Certains influenceurs dans le top des penseurs mondiaux on un discours ouvert sur l'open source mais plus limités sur le logiciel libre. Qui en fait un mouvement plus en marge. Le principe de logiciel gratuit pose problème avec la possibilité d'en retirer un revenu et de rémunérer les developpeurs. Quand on parle de business on emploi "open source". Et on retrouve des multinationales d'envergure tel que le [top 35 entreprises "open source"](https://www.datamation.com/open-source/35-top-open-source-companies/).

Le discours libriste se retrouve plus facilement autour de l'économie de l'abondance que de pénurie et de rareté dont participe le capitaliste. La libre circulation de l'information, les libertés de copier et de redistribuer des logiciels est une amorce à l'économie de l'abondance. C'est un véritable mouvement de fond. Un monde post-pénurie est ouvert à nous si nous nous tournons vers le Cosmos. Les astéroides et les exoplanètes nous donnerons des quantités illimités de ressource rendant caduque l'offre de rareté de l'économie actuel.

Ainsi la résistance numérique s'amorce autour de thématique tel que l'économie spatial et le minage d'astéroide aux interfaces homme-machine (IHM) tout droit sorti des vagues du transhumanisme.Le succès de la mise en place et l'accès à la technologie considéré par le transhumanisme sera au moins "open source" ou va accentuer les inégalités.

Tout projet sérieux d'ingénierie passe de nos jours par la mise en place d'un repository sur Github. Les règles ont changé et tout commence par la transformation numérique. Quand on parle d'ingénierie système avec des projets fortement multi-discipline prenant en compte différente partis prenantes. La partie software peut-être développé en amont. Mais la gouvernance est fortement axé sur de la gestion de projet informatique. Github permet de mettre en place des ressources conséquente tel qu'un wiki, tableau de bord et serveur distant de documentation, tout en permettant de facilement contribuer sur le code. La station de travail sous Arch est particulièrement adapté pour les développeurs informatiques en recherche de productivité et de maitrise complète de leur système. 

## La nébuleuse Arch

Croire que Arch est réservé à l'élite des plus nerds d'entre nous est trompeur. Une entrée en matière est possible avec Manjaro. Cette distribution est un "fork" d'Arch Linux utilisant les specificités du gestionnaire de paquet pacman et AUR. L'installation du système se fait pas à pas et est guidé. L'avantage c'est que vous parlerez le même langage que la communauté Arch.

1. [First step on Manjaro](https://manjaro.org/support/firststeps/)
2. [User Guide français](https://chuangtzu.ftp.acc.umu.se/mirror/osdn.net/storage/g/m/ma/manjaro/Manjaro-User-Guide-French.pdf)

Pour les plus motivez ce qui faut savoir sur Arch:

1. [Installation de base](https://wiki.archlinux.fr/installation)
2. [Automatiser l'installation avec le script archfi](https://github.com/MatMoul/archfi)

### Post-installation

Fraichement installé sur votre nouveau système il reste quelques ajustement à faire pour avoir un système plus opérationnel. Beaucoup de manipulation se passe par le terminal ou le shell car c'est plus rapide. Ainsi après une fraîche install faite une mise à jour du système en lançant la commande:
```bash
sudo pacman -Syu
```

Mise à jour des mirroirs de téléchargement des paquets:
```bash
sudo pacman-mirrors -g
```

Par la suite il est nécessaire d'installer quelques outils pour développeurs.En lançant dans un terminal:
```bash
sudo pacman -S base-devel
```

Si vous regardez ce que contient [ce metapackage](https://archlinux.org/groups/x86_64/base-devel/), on peut trouver des utilitaires tels que gcc, le compilateur pour langage C, C++, Go essentiel à l'ingénierie logicielle, mais aussi make pour automatiser les commandes du compilateur sur de plus large projet.

Ainsi que cette commande pour installer Git, Vim, zsh, curl et xterm
```bash
sudo pacman -S git vim zsh curl xterm
```

Installer quelques codecs supplémentaires
```bash
sudo pacman -S exfat-utils fuse-exfat a52dec faac faad2 flac jasper lame libdca libdv gst-libav libmad libmpeg2 libtheora libvorbis libxv wavpack x264 xvidcore flashplugin libdvdcss libdvdread libdvdnav dvd+rw-tools dvdauthor dvgrab
```

Prise en charge d'outils de compression, archivage par le gestionnaire de fichier Nautilus sous Gnome
```bash

sudo pacman -S file-roller seahorse-nautilus nautilus-share zlib p7zip unzip zip zziplib
```

Installer le SDK de kit de developpement Java:
```bash
sudo pacman -S jdk-openjdk
```

Installer des IDE

* VS code, il se nomme codium est libre sans la télémétrie de Microsoft
* Eclipse, IDE complet pour coder en Java
* Code::Blocks, IDE pour C/C++
* Pycharm, IDE pour python

Si cela vous fatigue de jongler entre des IDE pour coder, Vim fait largement l'affaire.
```bash
sudo pacman -S code codeblocks pycharm-community-edition
```

Pour installer Eclipse Java il faut passer par AUR. Pour cela il est nécessaire d'installer un gestionnaire de paquet tel que yay.
Suivez [ce tutoriel sur yay](https://www.tecmint.com/install-yay-aur-helper-in-arch-linux-and-manjaro/)

Puis pour installer Eclipse Java lancer la commande:
```bash
sudo yay -S eclipse-java
```

Quelques outils nécessaires:

* Navigateurs internet chromium
* lecteur video vlc
* Editeur photo Gimp

```bash
sudo pacman -S vlc gimp chromium
```

Je conseille egalement d'installer Zeal de la documentation hors-ligne pour developpeurs logiciels.
```bash
sudo yay -S zeal
```

Il reste quelques customizations à faire tel que d'installer oh-my-zsh pour les power-users de la ligne de commande du shell:

* [Installer oh-my-zsh](https://gist.github.com/legoffant/a3e19432781236564cfe279ef660eb12)

Ce faciliciter la vie en configurant ssh pour Git et Github:

* [Ce connecter à Github via ssh](https://gist.github.com/legoffant/27daf8e664662f5cad19bc069004ae37)

Ce post montre un peu l'étendu de la customization possible de son système d'exploitation par la branche plus extremiste sous linux tel que les archers lors de la post-install.
