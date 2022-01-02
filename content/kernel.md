Title: [MASTER PLAN] Devenir un kernel hacker
Date: 2022-01-02 21:25
Modified: 2022-01-02 21:25
Category: C/C++
Tags: C, kernel
Authors: Anthony Le Goff
Summary: 

Dans la série *from scratch* comment contribuer à la communauté du logiciel libre en ce formant à moindre frais en autodidacte par internet et quelques bouquins.
Je vais vous présenter un métier très recherché depuis que les systèmes embarqués sous Linux ont fait leur apparition en particulier tel que Android. C'est une expertise demandé par les plus grandes entreprises dont Google, IBM, Intel. Je parle du kernel hacker. Il n'y a aucune formation en France à ce que je sache pour en devenir. La meilleure voie est encore de choisir des métiers de l'ingénierie des systèmes embarqués. Sachez que c'est l'élite du domaine car le noyau est le coeur du système d'exploitation.

*Cela consiste en quoi?*

A terme c'est d'être un ingénieur capable de maintenir le code source du noyau linux et de trouver et corriger des vulnérabilités tels que des failles 0days.

Le noyau consiste à une interface entre le matériel de l'ordinateur et ces processus, on retrouve en particulier la gestion:

* de la mémoire : suivi des contenus stockés, de leur emplacement et de l'espace mémoire utilisé
* des processus : identification des processus susceptibles de solliciter le processeur, à quel moment et pour quelle durée
* Pilote des périphériques : médiateur/interprète entre le matériel et les processus
* Gestionnaire des appels système et de la sécurité : réception des demandes de service envoyées par les processus


Si votre intention est de devenir en autodidacte un kernel hacker il va falloir des bases en compétence qui sont tout à fait possible d'acquérir en dehors des institutions. Cela reste un métier de passionné, de contributeur à la communauté du logiciel libre ou l'on apprend tous les jours un peu plus. Connaitre le noyau permet également de créer son propre système d'exploitation d'ordinateur.

##[COEUR DE LA PROGRAMMATION SYSTEME]

En premier, il est nécessaire d'apprendre le langage C. Celui-ci est le langage principal du noyau et des systèmes d'exploitations en particulier basé sur Linux. Le langage de bas-niveau proche de la machine est majoritairement défini par le C et l'assembleur en petite proportion. Il vous faudra choisir un compileur et c'est l'occasion d'utiliser GCC "GNU compiler collection" sous Linux pour produire du logiciel libre avec un éditeur de texte tels que VS Code ou Vim. Plus tard il sera possible d'apprendre à utiliser Make pour automatiser la tâche de compilation du code pour des projets volumineux.

Une fois que les bases du langage C sont acquises, éssayer de développer des jeux tels que Space Invaders, Pong ou encore s'initier aux automates cellulaires avec le jeu de la vie de Conway. Il sera possible d'apprendre en même temps Git pour le contrôle de version en créant un repository sur Github du projet. Git est une compétence essentiel pour tout travail de collaboration sur du code open source dont le noyau inventé par Linus Torvalds.

Quelques livres pour démarrer:

* Le C en 20 heures, Schang & Berthomier
* Programmer en C pour les Nuls, grand format, 3e éd, Gookin
* Le langage C - 2e éd - Norme ANSI, Kernighan & Ritchie

>Pour aller plus loin, il est possible d'explorer d'autres langages de programmation système tels que Rust, Nim et Zig.

##[ALGORITHME ET STRUCTURE DE DONNEE]

Il faudra maitriser l'algorithmique pour résoudre des problèmes et savoir organiser les données grâce aux structures de données. Connaitre ces principes est un gain de temps et de mémoire pour résoudre des problèmes.

Il est possible de trouver des ressources sur le web pour ce former tels que:

* Algorithmique pour l'apprenti programmeur - Zeste de Savoir [PDF]
* Algorithmes Et Structures De Donnees - Cours Et Exercices Corrigés En Langage C - Divay
* Langage C : Structure de Données et d' Algorithmes en C, Udemy
* Algorithmique, Structures de données et langage C, Enjalbert [PDF]

##[RESEAUX]

Un ordinateur n'a pas de sens à fonctionner seul, les protocoles réseaux ont été développé en même temps que les ordinateurs et c'est directement implémenté dans le noyau. La plupart des hackers ont des solides compétences en protocole et réseau que cela soit pour maitriser internet tel que le TCP/IP. Et cela se développe de plus en plus avec l'internet des objets.

* Réseaux informatiques - Notions fondamentales (8e édition) - (Protocoles, Architectures, Réseaux sans fil, Virtualisation, Sécurité, IPv6...), Dordoigne
* Les réseaux informatiques par la pratique, Launay
* Tout sur les réseaux et Internet - 5e éd, Lemainque & Pillou
* Linux - 4e éd - Programmation système et réseau - Cours et exercices corrigés: Programmation système et réseau, Delacroix

##[SYSTEME D'EXPLOITATION]

Une fois que l'on a de bonne base de programmation système, on doit apprendre les concepts des systèmes d'exploitation sous Linux. Apprendre à utiliser une distribution comme Arch Linux ou l'on construit soit même son propre système d'exploitation permet d'acquérir des compétences vitales dans le domaine.

* Introduction aux systèmes d'exploitation - Cours et exercices en GNU/Linux, Boucheneb & Torres-Moreno
* LINUX - Maîtrisez l'administration du système (6e édition), Rohaut
* UNIX, pour aller plus loin dans la ligne de commande, Lozano [PDF]

##[LINUX KERNEL]

Pour la littérature sur le noyau Linux, tout est en anglais. Il n'y a pas d'article de référence en français. Il est important de développer à ce stade ces compétences pour pouvoir maitriser et entrée de la communauté du logiciel libre à l'internationnal. Le projet du noyau Linux inclus des développeurs du monde entier dont le langage de référence, celui d'internet est l'anglais. On retrouve sur internet toute la documentation du noyau à l'adresse "The Linux Kernel documentation". 

* Linux Kernel Development, third edition - R.Love
* Linux Device Drivers, J.Corbet
* A Beginner’s Guide to Linux Kernel Development (LFD103), The Linux Foundation

##[CHALLENGE DE PROGRAMMATION]

Il ne faut pas négliger l'entrainement à la résolution de problème. En tant que Kernel Hacker chaques jours sont lot de problème à résoudre avec le moins d'effort. Il faut développer des automatismes et entrainer le cerveau à travers des exemples et cas pratique. Les challenges de programmation permettent de progresser en algorithme et structure de donnée. Quelques sites de références:

* Codewars
* CodinGame
