Title:Thinkpad T480
Date: 2022-07-01 11:53
Category:Inclassable
Tags: notebook, thinkpad
Authors: Anthony Le Goff
Summary:

﻿En cette période de soldes, je suis tombé sur une bonne affaire pour mettre à jour mon matériel informatique. Je cherchais un Lenovo Thinkpad robuste entre autre pour être plus à l'aise avec la virtualisation sous KVM et lancer facilement 2 VMs.  

J'ai donc casser ma tirelire pour 400€ sur un modèle reconditionné de chez Back Market datant de 2018: Un Lenovo thinkpad T480. Pourquoi donc ce choix, plus en détail.

Il faut savoir que Lenovo a un partenariat avec l'entreprise Red Hat Linux, de ce fait les thinkpads en particulier ce modèle a été testé sur différente distribution GNU/Linux et fonctionnant "out of the box" sans prise de tête avec le matériel. C'est le bastion des développeurs. L'équipement lourd pour construire un tank.

J'ai regardé les soldes sur la boutique officiel de Lenovo et le prix le plus bas est à 689€ pour le [Thinkpad E14 G3 AMD](https://www.lenovo.com/fr/fr/laptops/thinkpad/edge-series/ThinkPad-E14-Gen-3-14%E2%80%9D-AMD/p/20Y7004TFR) avec seulement 8GB RAM, je veux 16GB. Ce n'est pas mon budget. Je mets plus cher qu'une tablette neuve, environ 250. Au maximum le double du prix pour un PC portable soit une limite haute de 500-600€ en neuf.

Mon ACER Aspire a 3 ans, tourne sur Manjaro GNOME avec un processeur intel core i3, 8GB RAM, 128GB. Je veux upgrader toute la configuration pour une station de travail plus puissante.

Cela tombe bien pour 400€ j'ai trouvé un thinkpad T480 en reconditionné avec une configuration:

*   Processeur intel core i7 @1,8GHZ
*   16GB RAM
*   SSD 256GO

Du matériel de professionnel au top de la technologie entièrement compatible sous Arch Linux tel que l'article sous le wiki: [https://wiki.archlinux.org/title/Lenovo\_ThinkPad\_T480](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T480)

Pas de mauvaise surprise, il me restera à mettre à jour le BIOS depuis Windows avant d'effacer le disque pour l'install d'Arch. Il y a surement quelques modification à faire dans le BIOS tel que désactiver Secure Boot pour lancer un Live USB, ainsi que vérifier le démarrage en UEFI et non pas en utilisant le BIOS Legacy. Mais c'est du détail.

Voici toutes mes notes pour installer Arch Linux, il y aura surement une modif à faire pour le support de partitionnement pour les disques nvme au lieu de sda. La configuration est valide, je l'ai testé il y a pas longtemps sur un autre PC portable plus léger avec seulement 4GB de ram sous le bureau XFCE. Cela pourrait être amélioré à l'avenir par le support de Wayland et BTRFS. Je préfère la robustesse du serveur X pour XFCE et ext4 en système de fichier, même si j'ai conscience des fonctions du BTRFS en particulier les snapshot. Mais j'ai un NAS qui suffit largement en cas de panne avec des sauvegardes. Je compte changer de thème GTK pour un look cyberpunk avec [Pandora-Arc](https://www.xfce-look.org/p/1352568/).  

Gist notes : [https://gist.github.com/legoffant/8a7503430d2663549f982ea7f97622f3](https://gist.github.com/legoffant/8a7503430d2663549f982ea7f97622f3)
