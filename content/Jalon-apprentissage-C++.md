Title: Jalon apprentissage C++
Date: 2021-04-13 15:49
Modified: 2021-04-13 15:49
Category: C/C++
Tags: C, C++, programmation
Authors: Anthony Le Goff
Summary: 


﻿J'avance par étape dans mon perfectionnement de l'ingénierie logiciel dans mon parcours d'ingénieur système, la maitrise de GNU/Linux est essentiel dans une logique de connaissance des systèmes embarqués moderne et serveur. A mon sens l'ingénierie système est la voie d'excellence en robotique. Il n'y a pas beaucoup de formation d'ingénieur système en France, j'ai eu l'occasion de m'initier à l'université de Lorraine à la fac de sciences après Mines Nancy dans la formation ISC Ingénierie de Système Complexe. J'étais un peu perdu en programmation, je ne maitrisais pas du tout le C++ pour la robotique. Enfin l'environnement utilisé préconisait à l'université d'utiliser Visual Studio. Les techniques étaient un peu old school, la base de donnée etait Microsoft server. Mais j'ai appréciés la formation pour le peu que j'ai fréquenté couplé à mes projets d'entreprises qui me prenaient du temps.  

Comment donc rattraper mon retard en programmation informatique, en école d'ingénieur nous avons été initié par du VBA(sic encore plus old school, so Microsoft) quand on est libriste on a vite envie de vomir.  

Dans le cadre de mes projets d'entreprises j'ai lancé une veille technologique pour connaitre les standards de l'industrie et ne pas toujours croire se que l'on nous raconte à l'école. Des professeurs sont parfaitement à jours, mais parfois on tombe sur des dinosaures en voie d'extinction. Bref la formation peut nous habituer à de mauvaises habitudes.  

### JALON 1: Mettre en place l'environnement de travail  

J'ai rapidement vérifié quels sont les pratiques de l'éco-système C++. On peut trouver des statistiques sur JetBrain: [https://www.jetbrains.com/lp/devecosystem-2019/cpp/](https://www.jetbrains.com/lp/devecosystem-2019/cpp/)  

Ainsi on découvre la part de marché chez les dev des compileurs:  

1.  GCC 66%  
    
2.  Clang 32%  
    
3.  MSVC(Microsoft) 30%  
    

Egalement quels sont les éditeurs de texte utilisés:  

1.  Visual Studio 27%  
    
2.  CLion 22%  
    
3.  VSCode 18%  
    
4.  Vi/Vim 7%  
    

Les systèmes de Builds:  

1.  CMake 42%  
    
2.  Visual studio project 37%  
    
3.  Makefile 33%  
    

On peut coupler ces statistiques à l'étude des pratiques des développeurs de StackOverFlow et obtenir en complément: [https://insights.stackoverflow.com/survey/](https://insights.stackoverflow.com/survey/)  

Le système d'exploitation des développeurs:  

1.  Microsoft Windows 45,33%  
    
2.  Linux Based 25,32%  
    
3.  MacOS 25,19%  
    

_Que Neovim est l'éditeur de texte le plus aimé_  

Que les développeurs veulent travailler avec les bases de données:  

1.  PostGreSQL 17,99%  
    
2.  MongoDB 17,86%  
    
3.  Redis 12,58%  
    
4.  Elasticsearch 10,52%  
    
5.  MySQL 9,76%  
    

On arrive vite à la conclusion que pour optimiser l'outil de travail sur les pratiques d'ingénierie logiciel il faut ce tourner vers:  

*   Linux  
    
*   GCC  
    
*   Neovim  
    
*   Cmake  
    
*   PostGreSQL & MongoDB  
    

Complémentaire aux besoins:  

*   Git pour le contrôle de version  
    
*   PlatformIO CLI pour la gestion de carte électronique embarquée  
    

  

Donc pour être confortable pour travailler en C/C++ vous devez adopter des pratiques et mettre en place l'environnement. Pour le choix de la distribution sous GNU/Linux j'ai ma préférence d'Arch Linux pour la documentation abondante du wiki de la communauté, la personnalisation, le côté administrateur de système et enfin AUR(Arch Linux User Repository). De plus comme argument Greg K-H mainteneur du noyau Linux a migré son équipe sous Arch Linux. C'est une tendance de bonnes pratiques des professionnels.   

Je recommande donc à mes collaborateurs sur mes projets d'entreprise de s'alligner sur ces pratiques comme requête de recrutement pour harmoniser l'outil de travail. Je recommande un Thinkpad comme PC.  

### JALON 2: Apprendre à programmer en C/C++  

Dans cette partie il faudra tout d'abord atteindre 300h de pratique pour commencer à assimiler soit 8h pendant 6jours/semaines = 192h/mois. Je suis un défenseur que vous n'avez pas à payer 8000€ pour apprendre la programmation. Que les ressources sont en libre accès sur internet.  

Pour débuter initier vous à la programmation par ces cours en libre accès en français:  

*   [Le C en 20h](https://archives.framabook.org/le-c-en-20-heures-2/index.html), Framabook. Vous allez utiliser les outils sous un système GNU/Linux tels que Vim, GCC. Une introduction à la programmation avant d'entamer le C++.  
    
*   [Initiation à la programmation en C++](https://www.coursera.org/learn/initiation-programmation-cpp), EPFL Mooc Coursera.  
    
*   [La programmation en C++ moderne](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/), Zeste du Savoir.  
    

### JALON 3: Algorithmique, structures de donnée  

Vous trouverez des cours de spécialisation en algorithmique et structure de donnée en C++ sur Udemy, mais egalement des ressources sur internet dans la littérature anglaise et plus particulièrement:  

*   Data Structures and Algorithm Analysis in C++ (4th) Mark Allen Weiss (Dispo sur Github)  
    
*   # [](https://github.com/gibsjose/cpp-cheat-sheet/blob/master/Data%20Structures%20and%20Algorithms.md#c-data-structures-and-algorithms-cheat-sheet)
    
    [C++ Data Structures and Algorithms Cheat Sheet](https://github.com/gibsjose/cpp-cheat-sheet/blob/master/Data%20Structures%20and%20Algorithms.md)  
    
*   [Learn DSA](https://www.programiz.com/dsa)  
    

### JALON 4: Design Pattern  

*   [Les patrons de conception en C++](https://refactoring.guru/fr/design-patterns/cpp)  
    
*   [Design Pattern in Modern C++ \[Livre PDF\]](https://www.programmer-books.com/wp-content/uploads/2019/03/Design-Patterns-in-Modern-C.pdf)  
    

### JALON 5: Projet Qasari  

Appliquer la programmation pour évoluer dans le [projet Qasari sur Github](https://github.com/legoffant/qasari). Récupérer les données sur les noyaux de modelisation géométrique. Il y a également des livres sur la création de jeux-vidéos et l'architecture des moteurs de jeux. La c'est les choses sérieuses créer des outils d'environnement virtuel en logiciel libre. L'apprentissage par la création de jeux-vidéos est à privilegier pour acquérir de la pratique et du fun.  

Pourquoi cette approche?  

Besoin de virtualiser la conception, flux d'échanges, maintenance de machines dans un environnement simuler du système solaire pour intégrer l'exploration du système solaire. Il faut voir grand, et préparer le terrain à créer une métropole autour d'un ascenceur spatial pour permettre la gestion d'un spatioport pour l'envoi de sonde et de robot pour le minage, fret de marchandise automatisé.  

C'est un chantier industriel entièrement automatisé à créer, et il faut le logiciel de modélisation pour plannifier la gestion des ressources et sa transformation en produit et service en privilegiant les circuits courts. Un approche modulaire est nécessaire tout en développant un esprit communautaire, associé au logiciel libre.  

Le projet s'inscrit dans l'eco-système de l'industrie minière. Mettre en place un spatioport dans le futur basé sur un ascenceur spatial demande de créer des fondations de 16km de profondeurs. On va devoir optimiser la ressource, l'extraire, la transformer, rendre habitable les soutterains. Cela ce plannifie bien en amont dans le projet, que de valider le choix de la zone d'implémentation riche en ressource minière. Ce genre de projet se plannifie sur 5000 ans de la conception à l'abandon de la structure et son recyclage. Pour avoir une maturité technologique et d'exploitation minière. La première étape est l'environnement simulé et créer les briques facilicitant l'émergence.
