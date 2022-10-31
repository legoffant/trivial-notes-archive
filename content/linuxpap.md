Title: Linux pas à pas
Date: 2022-10-31 06:53
Category:Linux
Tags:Linux
Authors: Anthony Le Goff
Summary:

Basculer sous GNU/Linux est souvent pas idéologie, quand on commence à comprendre l'intérêt du code source ouvert et du logiciel libre dans l'infrastructure informatique. Défendre les libertés numériques devraient être une nécessité. Là ou il y a de l'expertise informatique, il y a GNU/Linux.

Faire ce basculement nécessite du matériel dédié, qui est conforme aux standards des drivers, dont le risque de non comptabilité est négligeable car certaines firmes ont fait des alliances avec des groupes commerciaux sous GNU/Linux. C'est le Cas de IBM avec Red Hat ainsi que la section ordinateur Lenovo dont les Thinkpads sont réputés dans l'industrie.

Commencez sérieusement sous Linux, achetez un Thinkpad reconditionné aux alentours de 300€, que vous n'aurez pas peur de casser. On trouve des offres intéressantes sur [BackMarket](https://www.backmarket.fr/fr-fr/search?q=thinkpad). Ou si vous voulez sérieusement apprendre l'informatique à vos adolescents, l'achat d'un vieux Thinkpad fait largement l'affaire. Il n'y a pas d'âge pour s'y mettre et ce n'est pas qu'un truc de geek et de barbu. On peut faire des choses très "kawaii". Aujourd'hui le Rover Persévérance de la NASA fonctionne sous GNU/Linux, c'est privilégié dans les systèmes complexes.

Notez bien, que les environnements de développement sont optimisé sous GNU/Linux pour les programmeurs et ingénieurs. La base, c'est que l'on est des fainéants et sur GNU/Linux ont peu tout automatiser mais également personnaliser selon ces besoins. 26% des développeurs du sondage de Stack Overflow admettent êtres sous GNU/Linux.

NOTA: 

> Pour votre apprentissage, créer un profil de social bookmarking sur Pearltrees ou vous allez sauvegarder toutes les pages internets et notion à apprendre au fur à mesure.

### Choisir une image ISO Live USB

On commence à apprendre doucement, on va utiliser des images ISO du système d'exploitation que l'on va installer sur le disque dur de l'ordinateur. Vous devez commencer à Googler sur internet comment accéder au BIOS / UEFI de votre ordinateur, en tapant le modèle. Il va être nécessaire de faire une manipulation, tel que désactiver le "secure boot" et "booter" sur une clé USB avec l'image ISO.

Entre temps, choisissez un logiciel pour graver l'image ISO du système d'exploitation sur une clé USB tels que:

* [Ventoy](https://www.ventoy.net/en/index.html)
* [Etcher](https://etcherpc.com/)
* [Rufus](http://rufus.ie/fr/)

Nous allons graver une image de la distribution [Xubuntu](https://xubuntu.org/download/) qui est une version alléger d'Ubuntu avec le bureau XFCE. Nous allons tout le temps utiliser ce bureau. Car il est facile à utiliser, léger et simple à installer, voir à customiser. Ainsi il fonctionne très bien sur des vieux ordinateurs. Il a l'avantage d'être une "Ubuntu" et donc le support associé en particulier la documentation. Suivez la procédure d'installation. Si vous êtes perdu il est temps d'aller sur la [documentation du wiki-fr](https://doc.ubuntu-fr.org/)

* N'oubliez pas de parcourir le [guide de débutant](https://doc.ubuntu-fr.org/debutant) pour la prise en main
* Suivez votre premier cours en ligne en [reprenant le contrôle sous GNU/Linux](https://openclassrooms.com/fr/courses/7170491-initiez-vous-a-linux?archived-source=43538)
* Cours De la Linux Foundation [Introduction à Linux](https://training.linuxfoundation.org/training/introduction-to-linux/)

### Vos premiers programmes informatiques

Nota: 
> Installer https://zealdocs.org/ pour avoir la documentation hors ligne des langages informatiques

Vous allez apprendre à développer, et bien le faire. Pour cela il existe des méthodes d'outils pour le développement de logiciel libre. Nous allons donc poser les bases de la doctrine de votre futur workflow:

> Vim + GCC + Makefile + Git

Nous allons commencer par apprendre le langage C qui est utilisé pour coder le noyau Linux et le système d'exploitation, certains bureaux comme KDE sont codés en C++ à aborder également car c'est le langage de la robotique.

La base est de connaître l'utilisation d'un compilateur tels que GCC avec un éditeur de texte comme Vim dans un terminal. 

* Pour vous lancez dans l'apprentissage de Vim, essayez la commande `vimtutor` dans un terminal ainsi que le livre [Vim pour les humains](https://vimebook.com/fr). Adoptez Vim va améliorer votre workflow.
* Pour créer vos premiers programmes suivez le livre [Le langage C en 20h](https://archives.framabook.org/docs/c20h/C20H_integrale_creative-commons-by-sa.pdf)
* [Introduction à Makefile](https://gl.developpez.com/tutoriel/outil/makefile/) , comment automatiser les liens avec les bibliothèques à la compilation.
* [Tutorial contrôle de version avec Git & Github](https://www.pierre-giraud.com/git-github-apprendre-cours/) + Github [Handbook](https://docs.github.com/en). Versionner son code est une bonne habitude à prendre dès le départ, que cela soit pour corriger des erreurs, suivre les modifications et faire du social coding.

#### La prise en main de la POO (Programmation orientée-objet)

L'apprentissage du C++ est difficile vous allez ramer, vous êtes prévenu, cela prend du temps. Mais c'est un bagage important. Le compilateur est g++ s'utilise comme GCC. A la base le C++ est du langage C avec classe, même si aujourd'hui le langage à bien changé. Comme le C, c'est un langage privilégié pour des instructions bas niveaux proche de la machine et de la mémoire.

* Tutorial https://www.learncpp.com/
* Ressources C++ https://hackingcpp.com/
* [La programmation en C++ Moderne](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/)
* [Learn C++ Programming for Beginners – Free 31-Hour Course](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/)
* Livre C++ Primer


#### Quelques bases en algorithmes et structures de données

Lisez: [Algorithmique pour l'apprenti programmeur](https://zestedesavoir.com/tutoriels/621/algorithmique-pour-lapprenti-programmeur/)

Vous devriez maintenant vous lancez dans des petits projets sur Github tels que faire un "jeu de la vie de Conway" voir un Space Invaders en C++. C'est en faisant des projets que vous allez apprendre. Apprendre à apprendre est une compétence essentielle.

### Lancer vous dans le LPIC

Pour une maîtrise des compétences sous GNU/Linux, rien de tel que le passage de la [certification LPIC](https://www.lpi.org/fr/our-certifications/summary-of-certifications) qui n'est pas trop cher. Ainsi trouvez-vous le livre(pirater-le s'il faut):

* Préparation à la certification LPIC-1 Linux 101 et 102

Vous allez comme ça valider des bases:

* Package Manager
* Shell Scripting
* Gestion des disques
* Automatisation des tâches
* Sauvegardes
* Sécurité
* Gestion des utilisateurs et privilèges 
* Réseaux TCP/IP, SSH, DNS
* Monitoring

Cela fera de vous un administrateur système "sysAdmin" prêt pour une utilisation avancée du système d'exploitation. 

Pour allez plus loin:

* Linux Administration [https://linux.goffinet.org/](https://linux.goffinet.org/)
* [Pour aller plus loins avec la ligne de commande UNIX](https://archives.framabook.org/docs/Pour_aller_plus_loin_avec_la_ligne_de_commande/Pour_aller_plus_loin_avec_la_ligne_de_commande_art-libre.pdf)
* Langage de scripting: le Python dont le [livre de Gerard Swinnen](https://inforef.be/swi/download/apprendre_python3_5.pdf) comme base d'apprentissage

### Utilisation avancée: Arch Linux

Pour connaitre tout le système en profondeur et recherchez une distribution sur mesure, passons à Arch Linux. Pour les plus fous d'entre vous il y a "Linux From Scratch".

Maintenant nous passons au niveau supérieur, nous allons supprimer et sauvegarder notre système Xubuntu d'apprentissage pour l'utilisation professionnel à travers Arch Linux qui est plus sécurisé(signature des paquets entre autre), minimaliste et customisable. Ainsi il y a l'avantage de AUR pour les paquets.

Sauvegarder sur une clé USB de 64GB vos documents fichiers depuis /home, cela devrait suffire.

#### Virtualisation avec KVM

Vous pouvez d'abord vous entraînez dans une machine virtuelle sous Linux avec KVM. Suivez ce [tutorial](https://phoenixnap.com/kb/ubuntu-install-kvm) pour installer sous Ubuntu.

Visitez le wiki Arch Linux en français pour débuter l'installation: [https://wiki.archlinux.fr/Accueil](https://wiki.archlinux.fr/Accueil). N'hésitez pas à aller sur le chat IRC via le client Weechat, ou j'y suis personnellement sous le pseudo: Trivial régulièrement pour toutes aides.  

Apprenez les lignes de commandes et leur utilité pour configurer le système. Regardez des vidéos sur Youtube sur l'installation comme guide complet: [https://www.youtube.com/watch?v=DPLnBPM4DhI&t=3747s](https://www.youtube.com/watch?v=DPLnBPM4DhI&t=3747s)

Une fois que vous avez pris vos marques, on démarre l'installation sur l'ordinateur. Vous avez le droit à l'erreur, c'est même conseillé.

#### Installation Arch Linux 

Sur votre ordinateur personnel, tel qu'un Thinkpad, pour une utilisation avancée je recommande:

* Système de fichier BTRFS
* Chiffrement dm-crypt/LUKS
* LVM
* ZRAM
* Bureau: XFCE ou i3, Open Box. Minimaliste "Less is more"

Vérifier toujours la signature PGP de l'image ISO en cas de corruption. Utilisez l'utilitaire en ligne de commande `dd` pour graver sur le media USB depuis Linux. Cette clé USB sera votre méthode de secours pour accéder au système en cas de plantage sévère. 

Vous trouverez [ma configuration et installation d'Arch Linux](https://gist.github.com/legoffant/0a90e1067e3130711bf3f728a8a4a356), n'installez que ce que vous comprenez, recherchez à quoi sert un paquet spécifique.
Liste des [outils pour désigners et développeurs sous Arch Linux](https://gist.github.com/legoffant/f4a05f7b3e246f6495a184072c3aee9c)

ENFIN BIENVENUE DANS LA COMMUNAUTE, "I Use Arch BTW"

N'hésitez pas à vous renseignez tels que sur:

* La programmation système
* Webdev
* Datascience
* Bug Bounty
* Reverse-engineering

Les sujets ne manque pas, en devenant un "archer" vous êtes administrateur système dans la voie de devenir un ingénieur système Linux. Et cela est un parcours ouvert aux autodidactes.