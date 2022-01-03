Title: Configurer un environnement C/C++
Date: 2022-01-03 22:57
Modified: 2022-01-03 22:57
Category: C/C++
Tags: C, C++
Authors: Anthony Le Goff
Summary: 

### Quelques informations

Ce topic est pour les grands débutants en informatique. Mon but est de rendre accessible à tous les outils pour la programmation des logiciels libres \[1\]. L'esprit hacker est très lié au mouvement. Ayant des projets d'entreprises j'ai des intérêts à vulgariser l'informatique pour former du personnel de tout horizons. Ce qui m'importe est la motivation et la capacité à apprendre continuellement. De l'importance de savoir coder dans notre société pour ne pas être seulement consommateur et subir la technologie. Programmer c'est fun, on peut créer des jeux, des sites web, faire bouger des robots, créer des logiciels. Ce que vous avez besoin est d'un ordinateur et une connexion à internet. Connaitre les bonnes sources d'information. Ce que apporte la programmation:  

*   La tenacité, l'esprit critique, la logique, le défi intellectuel  
    
*   Les salaires les plus rémunéré  
    
*   L'apprentissage en permanence  
    
*   Les compétences essentielles aux entrepreneurs  
    
*   La porte d'entrée à l'ingénierie et la robotique.  
    

Je vais travailler sur les idées reçus. Pour commencer la plupart des outils de développement sont sous Linux à travers l'expansion des logiciels libres. Utiliser Windows pour du développement informatique, c'est ce mettre une balle dans le pieds car trop limité. Si vous aspiré à devenir un virtuose de l'informatique le passage vers Linux est une obligation. Secondement le langage python n'est pas le plus conseillé aux débutants. Personnellement j'utilise trois langages qui sont nécessaire aux systèmes embarqués et donc la programmation de micro-controlleur.  

COMPILER:

*   C, pour la programmation système, noyau et Arduino  
    
*   C++, pour le paradigme orienté-objet  

SCRIPTING:

*   (Bash, langage du shell Linux)
*   Python, standard chez les hackers

Le C/C++ est considéré comme le langage le plus performant utilisé entre autres pour créer des compilateurs, des jeux vidéos, application en robotique et temps réels. On dit que le C++ est une extension du langage C avec classe dans le paradigme orienté-objet. Ainsi Le Rover Curiosity sur Mars fonctionne avec 2,5 millions de lignes de code en C. Parlons également de l'avion de chasse furtif le F-35 qui utilise plus de 8 millions de lignes de code en C/C++. Pourquoi ce succès? C/C++ a une gestion de la mémoire manuel, l'utilisation des pointeurs ou de l'allocation dynamique permet de contrôler au mieux les ressources processeurs et mémoires. Etre à la pointe de la technologie se traduit par l'apprentissage du C/C++ héritage de Denis Ritchie et d'UNIX. Troisième idée reçu, il n'est pas nécessaire de commencer la programmation avec un IDE(integrated development environnement) et ce n'est pas conseillé car cela n'apprend pas les bases pour compiler. Ce que vous avez besoin pour débuter:  

*   Compilateur libre GCC  
    
*   Make\[13\]  
    
*   Git, outil de version contrôle  
    
*   Vim , éditeur de texte dans un terminal
*   Une dose de café ou de thé, voir des cocktails à base de redbull

### WSL (Windows Subsystem for Linux)

Vous débuter en informatique et maintenant vous savez qu'il faut utiliser des logiciels libres, comment je fais cela depuis Windows? Nous allons installer WSL \[5\]

> Le Sous-système Windows pour Linux (WSL, Windows System for Linux) permet aux développeurs d’exécuter un environnement GNU/Linux (et notamment la plupart des utilitaires, applications et outils en ligne de commande) directement sur Windows, sans modification et tout en évitant la surcharge d’une machine virtuelle traditionnelle ou d’une configuration à double démarrage.  

L'installation s'éffectue par cette ligne de commande depuis PowerShell qui va configurer le noyau linux et par défaut choisir la distribution Ubuntu, le redémarrage de l'ordinateur est nécessaire après l'installation de WSL:
```
wsl --install
```
Ensuite nous allons configurer le nom d'utilisateur et le mot de passe sous Ubuntu. Pour cela aller dans le menu démarrer, chercher et lancer l'application "ubuntu". Vous serez inviter à faire les modifications. Quitter l'environnement PowerShell en tapant:  
```
exit
```
### Mettre à jour la distribution ubuntu

Relancer WSL en recherchant "ubuntu" dans le menu démarrer et lancer votre première ligne de commande\[5\] pour mettre à jour la distribution:
```
sudo apt update && sudo apt upgrade
```

### Installer Windows Terminal

> Windows Terminal pouvez exécuter n’importe quelle application avec une interface de ligne de commande. Ses principales fonctionnalités comprennent un affichage multi-onglet, des volets, une prise en charge des caractères Unicode et UTF-8, un moteur de rendu de texte accéléré par GPU, ainsi que la possibilité de créer vos propres thèmes et de personnaliser le texte, les couleurs, les arrière-plans et les touches de raccourci.  

Pour installer Windows Terminal\[7\] puis choisir le profile avec WSL

### Installer l'environnement de développement

Lancer un terminal, nous allons installer les composants nécessaire dans WSL pour notre environnement\[9\] dont le meta-package "build-essential" qui inclus GNU Compiler Collection\[2\], GNU Debugger, Make pour le langage C/C++ ainsi que Git et Vim.  
```
sudo apt install build-essential git vim
```

### Hello World

L'écriture de votre premier programme passe par le traditionnel "Hello World". Nous avons besoin d'un éditeur de texte tel que Vim pour écrire le code source. Ne vous affoler pas pour l'apprentissage de Vim, il y a un ebook disponible à cette adresse\[14\] pour le reste suivez cette procédure\[15\] et plus généralement l'utilisation de GCC\[3\] en ligne de commande, pour compiler votre premier programme en langage C. La compilation d'un programme C++ on change de compilateur en utilisant g++, mais le principe est le même car c'est les mêmes outils.

### Apprendre à coder

Maintenant vous avez tous les outils pour apprendre à coder. Je vous conseil de commencer par le langage C puis connaitre le paradigme orienté-objet à travers le C++. Sachez que le C++ a évolué et il est difficile de trouver de la documentation en français sur ce que l'on appel le C++ moderne. Pour bien commencer à coder, procurer vous les livres pour grand débutant en informatique:

*   Le C en 20 heures - Berthomier, Schang - 2010
*   Le guide du C++ moderne – De débutant à développeur - Benharrats, Vittupier - 2021
    

### Pour aller plus loin 

Pour participer sur des projets open source et savoir gérer son code on utilise Git et Github\[4\]. Cette étape d'apprentissage est nécessaire à tous développeur sans exception. Dans votre apprentissage n'oublié pas de lire la documentation du langage\[8\]. Vous allez utiliser des librairies pour le C\[12\] et C++\[10\] tel que Boost\[11\] qui ajoute des fonctions au langage comme les pointeurs intelligents comme pratique de programmation avancée et moderne.

**Sources bibliographiques:**

\[1\] Introduction aux logiciels libres [https://www.april.org/files/documents/html/intro.html?q=groupes/gnufr/intro.html](https://www.april.org/files/documents/html/intro.html?q=groupes/gnufr/intro.html)  

\[2\] GNU Compiler Collection [https://fr.wikipedia.org/wiki/GNU\_Compiler\_Collection](https://fr.wikipedia.org/wiki/GNU_Compiler_Collection)

\[3\] Première compilation avec GCC [http://perso.univ-lyon1.fr/jean-claude.iehl/Public/educ/gcc.html](http://perso.univ-lyon1.fr/jean-claude.iehl/Public/educ/gcc.html)

\[4\] Gérer du code avec Git & Github [https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github](https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github)

\[5\] Console: Ligne de commande [https://doc.ubuntu-fr.org/tutoriel/console\_ligne\_de\_commande](https://doc.ubuntu-fr.org/tutoriel/console_ligne_de_commande)

\[6\] Documentation pour le sous-système Linux sous Windows [https://docs.microsoft.com/fr-fr/windows/wsl/](https://docs.microsoft.com/fr-fr/windows/wsl/)  

\[7\] Windows Terminal [https://www.microsoft.com/fr-fr/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab#](https://www.microsoft.com/fr-fr/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab#)

\[8\] C/C++ référence documentation [https://en.cppreference.com/w/](https://en.cppreference.com/w/)

\[9\] Hacking cpp, development setup [https://hackingcpp.com/cpp/tools/beginner\_dev\_setup.html](https://hackingcpp.com/cpp/tools/beginner_dev_setup.html)

\[10\] bibliothèques en vue pour la programmation C++ [https://www.lemondeinformatique.fr/actualites/lire-9-bibliotheques-en-vue-pour-la-programmation-en-c-82199.html](https://www.lemondeinformatique.fr/actualites/lire-9-bibliotheques-en-vue-pour-la-programmation-en-c-82199.html)  

[](https://www.it-swarm-fr.com/fr/c%2B%2B/quels-sont-les-avantages-de-lutilisation-des-bibliotheques-c-boost/958398176/)\[11\] Quels sont les avantages de l'utilisation des bibliothèques C ++ Boost?​​​​​​​ [https://www.it-swarm-fr.com/fr/c%2B%2B/quels-sont-les-avantages-de-lutilisation-des-bibliotheques-c-boost/958398176/](https://www.it-swarm-fr.com/fr/c%2B%2B/quels-sont-les-avantages-de-lutilisation-des-bibliotheques-c-boost/958398176/)  

\[12\] List of open source C librairy [https://en.cppreference.com/w/c/links/libs](https://en.cppreference.com/w/c/links/libs)

\[13\] Makefile [https://gl.developpez.com/tutoriel/outil/makefile/](https://gl.developpez.com/tutoriel/outil/makefile/)  

\[14\] Vim pour les humains [https://vimebook.com/fr](https://vimebook.com/fr)

\[15\] Apprendre à programmer en C/C++ [https://legoffant.github.io/apprendre-a-programmer-en-langage-cc.html](https://legoffant.github.io/apprendre-a-programmer-en-langage-cc.html)