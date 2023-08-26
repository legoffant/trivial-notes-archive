Title:Créer un blog avec un générateur de site statique
Date: 2023-08-26 05:19
Category:Inclassable
Tags:blog
Authors: Anthony Le Goff
Summary:

Vous pourriez avoir une passion pour l'écriture et commencer un blog mais également comme journal ou aide mémoire de votre apprentissage de l'informatique avec du code. C'est également un moyen de créer une communauté pour de l'intelligence collective et transférer de la connaissance.

On va s'intéresser à la création de blog pour développeur comme sur "Trivial Notes" qui utilise Pelican + Github Pages. Tout d'abord c'est quoi un générateur de site statique? C'est un framework écrit dans un langage qui automatise la création de page html + css pour un site sans gestion de base de donnée. Il ne fait que afficher des pages. Pour avoir quelques fonctions extra tel que le formatage pour le code on écrit en [markdown](https://www.markdowntutorial.com/fr/) qui va convertir en html.

### 1. Choisir un générateur de site statique

Il y en a quelques un, et le choix ce fait en fonction du langage de programmation et vos connaissances permettant de gérer les fichiers de configuration: [https://jamstack.org/generators/](https://jamstack.org/generators/)

Dans notre exemple nous allons utiliser [Jekyll](https://jekyllrb.com/) en Ruby.

### 2. Déploiement chez un hébergeur web

Votre site doit être chez un hébergeur (host). Vous pouvez vous même configurer un simple web serveur avec juste Nginx qui va afficher les pages html que vous pusher via une commande scp en utilisant ssh. Donc installer un VPS. Mais cela n'est pas gratuit vous pouvez utilisez avec interface en français:

* [OVH 1 vcore, 2go ram, 20 GO SSD 4,20€/mois](https://www.ovhcloud.com/fr/vps/)
* [Hostinger 1 vcore, 4go ram, 50 GO NVMe 4,99€/mois](https://www.hostinger.fr/vps)
* [Infomaniak 4 vcore, 12go ram, 250 GO HDD 24,99€/mois (overkill...)](https://www.infomaniak.com/fr/hebergement/vps-cloud/tarifs)

Maintenant vous pouvez automatiser la gestion du serveur web pour déployer le blog via des hébergeurs gratuits conçus pour les sites statiques. Listing:

* [Netlify](https://www.netlify.com/)
* [Vercel](https://vercel.com/)
* [Cloudflare pages](https://pages.cloudflare.com/)
* [Firebase by Google](https://firebase.google.com/)
* [DigitalOcean app platform](https://www.digitalocean.com/products/app-platform)
* [Surge](https://surge.sh/)
* [Statically](https://statically.io/)
* [Render](https://render.com/)
* [Gitlab Pages](https://about.gitlab.com/stages-devops-lifecycle/pages/)
* [Github Pages](https://pages.github.com/)

Dans notre exemple nous allons déployer sur Gitlab Pages. On va fuir Microsoft et Github, si c'était à refaire j'aurai transféré sur Gitlab.

### 3. Etape par étape

A. Nous devons installer les pré-requis sur notre ordinateur en local tel que Git et un environnement Ruby. Sous GNU/Linux dans un terminal:

```bash
$ sudo pacman -S git base-devel tar gzip diffutils curl
```

En utilisant un packet manager en Ruby RVM
```bash
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys \
  409B6B1796C275462A1703113804BB82D39DC0E3 \
  7D2BAF1CF37B13E2069D6956105BD0E739499BDB

$ \curl -sSL https://get.rvm.io | bash -s stable --auto-dotfiles

$ source ~/.rvm/scripts/rvm

$ rvm list known

$ rvm pkg install openssl

$ rvm install ruby --with-openssl-dir=$HOME/.rvm/usr

$ ruby -v
```

Modifier `zshrc` pour ajouter le PATH des gems en fonction de votre version ruby
```
export PATH=$PATH':/home/trivial/.local/share/gem/ruby/3.0.0/bin'
source ~/.rvm/scripts/rvm
```

Installer bundler
```bash
$ gem install bundler
```

B. Nous devons créer un compte sur Gitlab avec un nom de "user" et générer un nouveau repository. [Tutoriel Gitlab](https://github.com/SocialGouv/tutoriel-gitlab)

```bash
$ git clone git@gitlab.test.com/user/monblog.git blog
$ cd blog
$ git checkout --orphan documentation 
$ rm -rf *
```
On initialise GemFile avec bundle pour installer Jekyll
```bash
$ bundle init
$ sudo bundle add jekyll

$ sudo jekyll new . --force
$ sudo bundle update
$ sudo chown -R $USER ~/blog
$ git add . && git commit -m "install Jekyll website"
$ git push origin documentation
```

On récupère le projet et on initialise une branche `documentation`. `--orphan` indique à Git qu'il doit créer cette branche sans tenir compte de l'historique du projet. La branche repart de zéro comme s'il s'agissait d'un deuxième projet complètement différent dans le même repository.

On demande à Jekyll de nous faire la structure sur laquelle on va travailler et on pousse le tout sur GitLab.

Il nous faut maintenant dire à GitLab qui y a du CI sur ce projet. Comme notre projet n'a aucune spécificité particulière (création d'une branche de zéro) nous allons pouvoir utiliser le template par défaut de GitLab :

* cliquez sur "Overview" > "Set CI project"
* dans la dropdown de template sélectionnez "Jekyll"
* Vous pouvez commiter en sélectionnant "documentation" dans target branch

Si vous allez dans l'onglet "Pipelines" de votre projet vous devriez maintenant voir qu'un nouveau (premier ?) pipeline a été crée et lancé par GitLab. Il contient un job de test et un job de build pour votre version actuelle du site.

Le job de build s'appelle `pages` et contient un artéfact (votre site buildé). C'est cet artéfact que GitLab va automatiquement déployer.

Une fois fini, si vous allez sur l'adresse du site statique que vous venez de générer vous pourrez voir le site par défaut de Jekyll avec un article de bienvenue autogénéré.

Si vous rencontrez des problèmes avec la génération des URL c'est peut-être parce que Jekyll pense être à la racine d'un nom de domaine alors qu'il est dans le dossier dédié au projet. Dans `_config.yml` il faut rajouter une entrée `baseurl: ""` avec pour valeur le endpoint de votre site. Pour un site disponible a l'adresse `https://gitlab.test.io/user/projectname/` ce sera `/user/projectname`.

A partir de là vous passez la plupart de votre temps dans le dossier `_posts` pour créer vos articles de blog:

```bash
$ rm -rf _posts/*
$ vim _posts/2032-08-26-hello-world
```

Pour servir en local le serveur avec option d'auto-refresh de pages:
```bash
bundle exec jekyll serve --livereload
```

Adresse: http://localhost:4000

Si vous devez faire la commande de build en manuel
```bash
bundle exec jekyll build
```


Pour plus d'information pour customiser Jekyll, lire la doc et en particulier [sur les themes](https://jekyllrb.com/docs/themes/). Vous pourriez avoir besoin d'un nom de domaine perso pour votre blog. Comme fournisseur de nom de domaine choisissez [name.com](https://www.name.com/)