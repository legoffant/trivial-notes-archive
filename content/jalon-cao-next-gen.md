Title:Jalon logiciel de CAO Next-Gen
Date: 2023-08-13 20:38
Category:Linux
Tags:c++, logiciel, ingénierie, open source
Authors: Anthony Le Goff
Summary:

Alors voila, j'avance sur mon grand projet d'ingénierie logicielle ou je compte créer le logiciel de CAO next-gen open source sous GNU/Linux. Le nom provisoir est *Qasari3D*. Ce projet va bien m'occuper 10 à 15 ans. C'est du long terme.

L'intérêt est de rabattre les cartes sur le marché, rendre accessible la conception, et faire hurler Dassault Systemes qui m'a bien casser les couilles avec ces sbires à L'école des Mines. Il y a des joueurs. Chiche?

Voila les grands principes et exigence du logiciel:

* Intégration de la conception communautaire via une refonte de Git pour les plans de pièces et éléments.
* Conception architecturale et le paradigme openBIM voir une amélioration du format STEP.
* Rendu 3D basé sur les moteurs de jeux-vidéos en utilisant un Geometric kernel open source.
* Langage de scripting (lua, python? A voir)
* Interface et modulaire, extensible. La communauté doit pouvoir créer des modules
* Intègre le calcul parallèle et distribué pour les HPC pour des opérations lourdes (éléments finis, CFD, etc...) Voir le projet BOINC.
* Ce lance en ligne de commande avec une assistance par une intelligence articielle. Puis choix des modules et définition du projet à créer. Si on travail en plan2D, ou rendu 3D etc... 
* Base de donnée mondiale de pièce et élément standardisé pour des bibliothèques.
* Automatise l'invention par le machine Learning et la méthode TRIZ.
* En natif le logiciel fait de la génération procédurale au niveau des algorithmes et intègre les automates cellulaires et la conception de nanites.

Rappel: [article schématique qui résume l'idée](https://legoffant.github.io/qasari3d.html)

Autant dire que c'est pour fabriquer des grands ensembles, des vaisseaux spatiaux de dizaines de kilometres, des structures pour de la terraformation, industrie lourde, naval, nucléaire et militaire. La fin des haricots.

Jalon d'apprentissage:

* [Les bases du C++ et Linux](https://legoffant.github.io/jalon-apprentissage-c.html)
* [Configurer et apprendre Neovim](https://legoffant.github.io/configurer-neovim-comme-ide-en-langage-cc.html)
* [Environnement et écosystème C++](https://legoffant.github.io/c-eco-systeme.html)
* [Démarrer un projet avec Cmake](https://legoffant.github.io/preparation-de-projet-avancee-en-c.html)

Bac à sable: *savoir et apprendre à programmer un Space Invader via SFML et un Game Engine(Pikuma tuto) en C++ (obligatoire)*.

En attente pour le projet: On démarre véritablement avec l'assistance de **GPT-5** via le plugin Neovim "vim-ai". Donc je recherche des ingénieurs logicielles pour le projet, sachez que Dassault et sa mafia va vous hair, mais c'est pas grave, je suis un peu sado-masochiste sur les bords depuis la mort de Serge Dalai - Lama Dassault. Egalement des ingénieurs mécaniques qui sont les utilisateurs et donc des exigences sur les interfaces.

Je n'ai pas encore totalement défini chez qui je vais héberger le code source. Mais je pense que je vais choisir une organisation "non-profit" basé à Berlin, Allemagne: [https://codeberg.org/](https://codeberg.org/)

Je vais bouder Microsoft et Github.

MAJ: Repo dispo du projet sur Codeberg: [https://codeberg.org/legoffant/qasari](https://codeberg.org/legoffant/qasari)

En cours d'initialisation, en particulier la documentation.