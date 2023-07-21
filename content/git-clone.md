Title:Archiviste et Git clone
Date: 2023-07-21 17:41
Category:Inclassable
Tags:git
Authors: Anthony Le Goff
Summary:

Dans les méthodes de développement moderne en informatique ce que l'on appel le workflow on utilise l'outil Git créé par Linus Torvalds à l'initiative du noyau Linux. Son but est la collaboration sur le code et un outil de contrôle de version.

Vous trouverez tous les détails de son utilisation et la documentation française sur le site: [https://git-scm.com/book/fr/v2](https://git-scm.com/book/fr/v2) et le PDF "[Git Magique](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/book.pdf)" sur les commandes de base.

Il existe des plateformes d'hébergement du code tel que Github (qui a été racheté par Microsoft) avec 70 millions d'utilisateurs dans le monde. On trouve également Gitlab, BitBucket, mais encore Gitee en Chine. 

Vous trouverez [un guide complet sur Github sur ce lien](https://www.pierre-giraud.com/git-github-apprendre-cours/)

Aucun ingénieur ou développeur un peu sérieux n'utilise pas l'open source et Git, c'est un standard. Cela permet de travailler en local sur le code sur le repository et de mettre à jour sur le dépôt distant sur un serveur partagé les changements.

Ainsi mon blog utilise Git car c'est un site statique sous Pelican (python) dans le workflow et est déployé gratuitement sur [github pages](https://pages.github.com/). Donc on peut normalement modifier et collaborer sur mon blog, cela m'est arrivé une fois qu'un type, un indien demande une modification sur un article.

L'avantage c'est que je travail sur une copie locale sur mon ordinateur avant de modifier sur l'hébergeur distant et "commit" le code. J'écris en markdown généralement avec [Mousepad](https://doc.ubuntu-fr.org/mousepad) ou [Neovim](https://github.com/neovim/neovim/wiki).

### Installation de Git

Pour cela il faut configurer Git l'installer, sur Arch Linux & Manjaro:
```bash
$ sudo pacman -S git
```

Verification de l'installation:
```bash
$ git --version
git version 2.41.0
```

Puis suivre la documentation pour mettre à jour vos informations personnels. Git est attaché à un compte mail pour savoir qui modifie le code (pas de vérification requise).

On configure:
```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Puis on choisi l'éditeur de texte par défaut:
```bash
$ git config --global core.editor vim
```

Et on modifie la branche principale:
```bash
$ git config --global init.defaultBranch main
```

### Archivage

On peut utiliser les dépôts distants tel que sur Github pour archiver de la documentation, du code etc... Il y a pas de limite théorique en GB. Pour récupérer le code il faut utiliser la commande `git clone` et récupérer le lien du dépôt Github. Par exemple pour fork mon blog et récupérer tous les articles originaux en markdown dans la branche source et dossier `content/` ainsi que les PDF dans `images/` , les fichiers en HTML dans la branche main, il suffit de chercher mon pseudo sur Github `legoffant` et la liste des repository du compte dont `legoffant.github.io`. On y trouve un lien en vert `<> Code` avec le dépôt en HTTPS. Il y a aussi un lien en SSH avec authentification avec des clés de chiffrement.

```bash
$ mkdir ~/sources
$ cd ~/sources
$ git clone https://github.com/legoffant/legoffant.github.io.git
```

Pour mettre à jour le dépot localement sur votre ordinateur, si mon site subit des modifications (pull request):

```bash
$ cd ~/sources/legoffant.github.io
$ git pull
```

C'est rudimentaire Git, mais très utile, généralement une fois adopté, on ne peu plus s'en passer pour développer et suivre les changements sur le code.