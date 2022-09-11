Title: Contribuer sur le code
Date: 2022-09-11 13:36
Category:Linux
Tags:ressources, hacker, contribution, git
Authors: Anthony Le Goff
Summary:

La carrière d'un hacker suit souvent le même cadre d'apprentissage. Tout d'abord on cherche à apprendre un langage de programmation. Je conseil de commencer avec le langage C car un héritage de la création d'UNIX. Puis on se familiarise à la ligne de commande. On switch sous Linux par idéologie, mais également pratique pour avoir les outils pour développeurs et chercheur en cybersécurité. On approfondi rapidement les structures de données et les algorithmes. On peut chercher à monter et administrer des systèmes sur mesure tel que sous Arch Linux et Gentoo par sécurité mais également de l'art numérique en customisant son OS. Tout ça dans l'optique de rependre le contrôle sur la machine. Vous n'êtes plus consommateur, mais devenez un créateur. Cette étape, le mindset est importante dans la construction cognitive. Vous allez pouvoir agir à votre manière sur le monde, et le modifier selon vos perspectives. La recherche de vulnérabilité ne vient pas tout de suite dans l'apprentissage. On attribue le hacking trop souvent à l'exploitation de serveur distant, élévation de privilège. Vous pouvez devenir un kernel hacker en devenant spécialiste du noyau Linux et le patcher écrit en C.Il y a environ 5000 kernel développeurs dans le monde mais c'est l'élite et le salaire tourne en moyenne à 9000€/mois. Forcément sans les bases du langages vous ne pourrez pas rechercher des vulnérabilités dans le code. Une autre activité est de casser les licences propriétaires des logiciels ou limitations généralement du C++. Une connaissance du langage, de la retro-ingénierie de binaire est nécessaire. Lancer un botnet de cryptomonnaie et infecter des ordinateurs demande un minimum de code. Pour le langage de scripting tourné vous vers Python est Ruby. Vous pouvez faire de l'argent par vos malwares et revendre sur le darknet, personnellement je ne juge pas, chacun sa manière de contribuer à la communauté. Mais l'une des manières la plus répandu est le social coding tels que sous des plateformes comme Github(Microsoft depuis 2018) avec 76 millions de développeurs et Gitee en Chine avec plus de 5 millions de développeurs, ne négligez pas les chinois par un frein de la langue. Github c'est quoi? A la base il y a un logiciel développé par Linus Torvalds pour les besoins de gestion de version du code du kernel nommé: Git. Maintenir et développer du code de logiciel libre en public sur un repository distant est la norme en passant généralement par Github. Plus généralement c'est la contribution à l'open source dérivé commercial créer par Eric S. Raymond. Utilisez Git demande un peu de temps, mais devient rapidement indispensable au développeur. Un exercice intéressant pour débutant est d'apprendre à coder avec Vim + plugins "Fugitive" un petit jeu vidéo comme Space Invader sur un repo distant Github avec Python et Pygame. Vous trouverez comment utiliser Git + Github sur internet. N'oubliez pas vous êtes évaluez par vos pairs via vos projets que vous partagez, le diplome n'a pas d'importance, mais la qualité du code intéresse les parties prenantes.

Pour démarrer un projet Github ce que je fais:

* Créer le repository sur Github, ajout licence, readme + .gitignore
* Git clone en ssh le repository sur mon ordinateur en local
* Je commit mon code via Vim+fugitive
* Je push sur le repo distant les modifications 

**Liens**

* 1 [Pourquoi contribuer à l'open source](https://opensource.guide/fr/how-to-contribute/)
* 2 [Les bases pour créer un projet Github](https://gamebuino.com/fr/academy/workshop/partagez-votre-projet-sur-github-1/les-bases-1)
* 3 [Apprendre à utiliser Git et GitHub | Cours Complet (2020)](https://www.pierre-giraud.com/git-github-apprendre-cours/)
* 4 [Générer des clés SSH pour Github](https://kinsta.com/fr/blog/generer-cles-ssh-github/)
* 5 [Complément d'information le livre Pro Git](https://git-scm.com/book/fr/v2)