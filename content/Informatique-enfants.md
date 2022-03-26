Title:L'informatique pour les Kids
Date: 2022-03-26 14:13
Category:Linux
Tags: matos, linux
Authors: Anthony Le Goff
Summary:

## INTRO

Donner de la liberté sur l'outil informatique à des enfants, c'est le meilleur moyen d'éveiller leur curiosité, mais egalement de les initier aux mathématiques en leur apprenant par le jeu des notions en cryptographie tel que décoder un message secret, mais également en géométrie pour déssiner des formes dans un jeu-video et construire un environnement. Les enfants adorent les mondes imaginaires, il faut leur donner l'opportunité de créer leur propre monde virtuel à partir de connaissance et de technique en informatique.

Comment débuter en informatique de 7 à 77+ ans? Déjà armer vous de patience, et il faudra un peu de matériel dédié qui ne craint pas la destruction, ni l'opportunité de bidouiller et détourner son fonctionnement.

Pour cela acheter un Raspberry Pi, qui est un micro-ordinateur de la taille d'une carte de crédit. C'est un système embarqué qui a été développé pour éduquer à l'informatique à moindre coût et faciliter l'accès également au pays en voie de développement. Pour vous équipez visionner des sites comme Gotronic et Kubii enfin LDLC. Il peu y avoir des ruptures de stock sur certains modèles. Ce que vous avez besoin pour débuter:

*   [Raspberry Pi 4 2GO RAM 52€](https://www.kubii.fr/cartes-raspberry-pi/2771-nouveau-raspberry-pi-4-modele-b-2gb-0765756931175.html) (préféré un modèle avec 4GO)
*   [Alimentation 15W USB-C 8€](https://www.kubii.fr/alimentations/2678-alimentation-officielle-usb-type-c-raspberry-pi-3272496300002.html?search_query=alimentation&results=295)
*   [microSD 64GO 18€](https://www.ldlc.com/fiche/PB00391413.html) (Pour le système d'exploitation et le stockage de fichiers)
*   [Un adaptateur micro HDMI - HDMI 4€](https://www.kubii.fr/cables-adaptateurs-video/2949-adaptateur-officiel-micro-hdmi-vers-hdmi-644824915043.html)
*   [Un clavier  AZERTY retro-éclairé 15€](https://www.ldlc.com/fiche/PB00281752.html)
*   [Un souris USB 10€](https://www.ldlc.com/fiche/PB00152295.html)
*   [Un écran PC avec port HDMI ~140€ en neuf](https://www.ldlc.com/fiche/PB00423452.html)

  

**Vous pouvez donc vous en tirer pour 250€ en neuf**. Le prix d'une tablette. Si vous voulez économiser il est possible de trouver des écrans bon marché sur le bon coin, mais si ce n'est pas un port HDMI prévoyé des adaptateurs VGA/DVI. J'avais personnellement trouvé un écran plat LCD 19" port VGA pour 10€ que j'ai adapté sur ma Raspberry Pi et mon serveur. 

Avec ce matériel, vos enfants vont pouvoir découvrir l'informatique, les composants du micro-ordinateur et son port GPIO pour l'électronique. Pour plus de référence:

*   [Le Guide de débutant Raspberry Pi 4 \[PDF\]](https://www.framboise314.fr/docs/BeginnersGuide-4thEd-FR_v5.pdf) sur le site dédié [framboise314.fr](https://www.framboise314.fr/)

## SYSTEME D'EXPLOITATION

Vous allez devoir installer sur votre carte microSD le système d'exploitation officiel de Raspberry Pi, nommé Raspberry Pi OS (anciennement Raspbian) est un système d’exploitation GNU/Linux basé sur Debian spécialement conçu et optimisé pour la Raspberry Pi. [Suivez cette page pour télécharger.](https://raspberry-pi.fr/telechargements/) Il vous faudra créer une carte SD depuis Windows, Mac, Linux avec l'outil Raspberry Pi Imager [en suivant ce guide](https://raspberry-pi.fr/creer-carte-sd-windows-mac-linux-raspberry-pi-imager/). Ainsi une fois votre OS sur la carte, il reste plus qu'à l'insérer dans le slot microSD du nano-ordinateur. Au démarrage, il vous sera demandé un identifiant qui sont:

ID: pi
Mot de passe: raspberry

Vous allez alors acccéder à Raspberry Pi OS pour plus ample information accéder à [la documentation officielle sur cette page](https://www.raspberrypi.com/documentation/) en anglais (traduisez-là avec Google si nécessaire).

Egalement [25 tips for beginners](https://raspberrytips.com/raspberry-pi-tips-beginners/), des choses à faire après la première installation et jeter un oeil à l'[utilisation possible avec Raspberry Pi](https://www.makeuseof.com/tag/different-uses-raspberry-pi/). Nous allons nous concentrer sur deux aspects:

*   Programmation
*   Serveur Minecraft

## RESSOURCES EDUCATIVES

Donner des accès hors ligne à des ressources pour l'éducation sur votre Raspberry Pi en fonction des intérêts de votre enfants en installant des logiciels(Reportez-vous à la documentation pour l'installation de logiciel avec la commande apt-get). Nous allons nous intéresser à deux projets:

*   [Kolibri](https://learningequality.org/kolibri/) de "learning equality" est une plateforme d'apprentissage regroupant des ressources tels que des cours de Khan Academy.
*   [Kiwix](https://www.kiwix.org/fr/) l'internet hors-ligne qui donne accès à Wikipedia, des TED Talks, projet Gutenberg etc...

Avoir une stratégie hors ligne dans un premier temps peut-être nécessaire avant d'éduquer à internet et filtrer le contenu sensible. Après il est intéressant d'accèder à des ressources tels que [Lumni](https://www.lumni.fr/).

## DANS LE CLOUD

Apprenez à vos enfants à utiliser les outils du cloud computing et rejoignez des projets tels que Disroot et éduquer à la vie privée sur internet contre la suveillance de masse. Le projet est basé sur une non-profit fondation à Amsterdam, qui est maintenu par la communauté et des volontaires. Disroot est une collection d'outils de communication, de partage et d'organisation qui sont ouvert, décentralisé, fédéré et respecte les libertés.

*   Créer un nouvel utilisateur(nouvel email perso): [https://user.disroot.org/pwm/private/login](https://user.disroot.org/pwm/private/login)
*   Les applications: [https://apps.disroot.org/](https://apps.disroot.org/)

Ne manquez pas le projet français [Framasoft](https://framasoft.org/fr/) et ces outils d'éducation populaire.

## PROGRAMMATION

Raspberry Pi OS fourni une liste de logiciel pré-installé dont le logiciel Scratch dès 7 ans pour apprendre la programmation pour les enfants. On retrouve en natif installé un interpréteur Python. Il faudra changer d'éditeur de texte pour apprendre avec Vim(pour casse-cou) et [VSCode](https://code.visualstudio.com/) qui est un standard facile d'utilisation pour Python. [Guide d'installation sur Raspberry Pi](https://code.visualstudio.com/docs/setup/raspberry-pi).

Je recommande ces 4 livres pour les parents et les enfants:

*   [Python pour les Kids: la programmation accessible aux enfants 22€](https://www.amazon.fr/Python-pour-kids-prorammation-accessible/dp/2212140886)
*   [Programmer en s'amusant avec Python pour les Nuls, mégapoche, 3e éd 17€](https://www.amazon.fr/Programmer-samusant-avec-Python-m%C3%A9gapoche/dp/2412056080/ref=asc_df_2412056080/?tag=googshopfr-21&linkCode=df0&hvadid=411535311074&hvpos=&hvnetw=g&hvrand=7585781742632118253&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9055186&hvtargid=pla-932049526250&psc=1&tag=&ref=&adgrpid=92288642049&hvpone=&hvptwo=&hvadid=411535311074&hvpos=&hvnetw=g&hvrand=7585781742632118253&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9055186&hvtargid=pla-932049526250)
*   [Pygame:Initiez-vous au développement de jeux vidéo en Python 29€](https://www.editions-eni.fr/supports-de-cours/livre/pygame-initiez-vous-au-developpement-de-jeux-video-en-python-9782409021688)
*   [A la conquète des Maths avec Python 24€](https://livre.fnac.com/a14028547/Peter-Farrell-A-la-conquete-des-maths-avec-Python)

## MINECRAFT

_Minecraft_ est un jeu qui convie le joueur à laisser libre cours à son imagination. Pour peu que l’on ait de la patience et un esprit créatif, on peut à peu près tout y construire ! _Minecraft_ est un jeu de type bac à sable, c’est à dire qu’il intègre des “outils” pour façonner son propre univers de jeu. Ainsi , le  joueur peut à peu près bâtir tout ce qu’il veut. Il existe différents modes de jeu dans lesquels la partie aventure et la partie créative sont plus ou moins développées. _Minecraft_ n’est pas un jeu réaliste, et ses graphismes à base de cubes ne sont pas sans rappeler les jouets Lego.  

Comme vous l’avez probablement remarqué, Raspberry Pi OS (version Desktop) est livré avec _Minecraft_ installé. Et ce n’est pas (uniquement) pour jouer. Si vous ne le saviez pas, l’objectif principal de la Fondation Raspberry Pi est d’aider les jeunes à apprendre comment programmer. Ils ont livré Minecraft Pi installé pour aider les enfants à atteindre cet objectif tout en s’amusant.  

Pour cela suivez ce livre ou renseigner vous sur internet comment programmer dans Minecraft:

*   [Apprendre à coder en Python avec Minecraft: Dès 10 ans 24€](https://www.amazon.fr/Apprendre-coder-Python-Minecraft-%C3%A9dition/dp/2212677219)
    

## POUR ALLER PLUS LOIN

Il existe des projets pour initier à la robotique et à l'électronique tels que Arduino en complément à l'informatique, c'est des activités connexes qui sont relativement abordable et formateur. Cela permet aux enfants de débrider leur créativité et d'avoir un regard sur la machine tout en la programmant.
