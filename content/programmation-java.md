Title:Démarrer la programmation en Java
Date: 2023-10-18 12:14
Category:Inclassable
Tags:java
Authors: Anthony Le Goff
Summary:

Java reste un très bon langage pour démarrer la programmation, en plus d'être un incontournable sur mobile et Android pour créer des Apps, tout comme Kotlin. Je le trouve personnellement trop verbeux, et j'ai ma préférence pour le C/C++ car je suis plus un ingénieur sur les systèmes embarqués et la robotique. Mais connaitre le Java en particularité sur le marché de l'emploi est non négligeable car la plupart des offres d'emploi (le 3/4) sont en Java pour les entreprises et la maitrise du full-stack avec le framework Spring. 

Alors voici quelques astuces pour débuter en Java sous GNU/Linux tel que Manjaro / Arch. L'installation des prérequis est très simple, cela prends que quelque minutes. On va installer l'EDI Eclipse pour coder

**1#** Procurez-vous le livre d'apprentissage de Java d'OpenClassRooms sur les [anciens PDF](https://openclassrooms.com/fr/old-courses-pdf) à cette addresse: [lien du PDF](http://user.oc-static.com/pdf/10601-apprenez-a-programmer-en-java.pdf). Il y a toutes les instructions nécessaire même pour ceux qui reste sur Windows.

**2#** Installation openJDK, la dernière version, en est à la 21 en 2023.

```bash
$ sudo pacman -S jdk-openjdk
```

Qu'es-ce que cela? Java Developement Kit permet de faire marcher la JVM et d'intégrer les outils de développement en ligne de commande tel que `javac`. Cela permet d'intégrer l'environnement virtuelle pour convertir en bytcode.

**3#** Installer Eclipse qui est dans AUR, le dépot utilisateur, en suivant la page wiki: ["Eclipse"](https://wiki.archlinux.org/title/Eclipse). On installe la version simple et basic pour Java. Il y a même le dark theme maintenant sur l'EDI.

```bash
$ yay -S eclipse-java
```

Vous trouverez la documentation en anglais [sur ce lien](https://help.eclipse.org/2023-09/index.jsp) d'Eclipse.