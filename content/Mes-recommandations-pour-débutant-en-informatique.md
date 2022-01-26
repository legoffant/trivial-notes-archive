Title: Mes recommandations pour débuter en informatique
Date: 2022-01-24 12:12
Modified: 2022-01-24 12:12
Category: Linux
Tags: linux, raspberry pi, distribution
Authors: Anthony Le Goff
Summary: 

Quand on veut débuter en informatique il faut parler GNU/Linux, on peut ce poser la question mais qui utilise le système d'exploitation? Es-ce réservé à une élite de geek ou de nerd ? Rapide tour d'horizon:  

*   **Google**. L'entreprise avait développé une version interne pour ces employées Goobuntu, qui est devenu depuis gLinux. La raison est simple chez Google, Windows n'est pas utilisé car a des problèmes de sécurité. Egalement les outils Windows sont trop lourds et peu flexibles.
*   **NASA**. L'organisation utilise depuis très longtemps GNU/Linux dans ces supercalculateurs. Les ordinateurs de l'ISS sont également sous Debian et le rover Perseverance a une distribution Linux embarqué.
*   **Gendarmerie française** est un utilisateur de Gendbuntu, une version d'ubuntu. Cela fait plus de 72 000 PCs qui ont migré depuis Windows XP vers GNU/Linux. 
*   **US Departement of Defense (DoD)**. Pour ce connecter à un réseau fiable, le DoD a développer un système de système d'exploitation que l'on peut transporter depuis une clé USB pour ce connecter au réseau du DoD même dans un hotel à base de GNU/Linux.
*   **CERN** a plus de 3000 PCs qui fonctionnent sous Scientific Linux développé par le Fermi Lab, DESY, ETH Zurich. L'analyse massive de donnée est une tâche simplifiée.

En réalité on retrouve parmis les utilisateurs de GNU/Linux des développeurs, ingénieurs, militaires, chercheurs, scientifiques: On a tous les outils à la disposition. On peut également parler de certains journalistes que cela soit pour la protection de l'information et des sources ou Julian Assange utilise Debian.

Car il faut avouer c'est la croix et la bannière quand vous voulez chiffrer un disque dur sous Windows alors que cela est proposé en natif sous GNU/Linux à l'installation. Le respect de la vie privée est un droit.

C'est egalement parler un même langage à base de l'héritage UNIX et des hackers. Même si la ligne de commande n'est plus obligatoire, son utilisation du shell ou terminal optimise le flux de travail. Les utilisateurs de GNU/Linux tous des hackers? Il y a dans l'esprit un peu de ça. GNU/Linux est une projection de la pensée Hacker en particulier le partage de l'information et son ouverture.

On peut reprocher aux utilisateurs de GNU/Linux parfois de ne pas faire assez de pédagogie et garder une forme d'entre-soi. Ce qui fait le système d'exploitation a du mal à se diffuser, ce n'est pas un produit véritablement commercial auprès de l'utilisateur final. Si c'est gratuit il y a un loup ? Pourquoi des gens travail bénévolement sur son développement.

Là ou le lobbying de la communauté fait le plus surface est à travers les libertés numériques accessible à tous. GNU/Linux doit être un choix militant, vous n'etes pas anti-système pour autant ou crypto-anarchiste. Vous êtes le système informatique à sa racine même. Tous les supercalculateurs du top 500 sont sous GNU/Linux ainsi que que le 96,3% selon Alexa du top un million de serveur sont sur GNU/Linux. Vous pouvez donc déployer vos connaissances pour créer un site web et l'administrer voir en faire du profit. Cela peut-être une simple page d'un portofolio personnel. Tout est facilité.

Le cas Raspberry Pi sortie en février 2012. J'étais à la fac de science à l'époque. Les utilisateurs de GNU/Linux dans ma promotion ont tous acheté un, j'ai participé à la vague. La promesse était pour les hackers de pouvoir détourner son utilisation pour éffectuer toutes sortes de tâches en électronique des systèmes embarqués. Mais c'est surtout un outil essentiel pour apprendre l'informatique à moindre coût. Windows n'a pas réussi à percer, GNU/Linux avait le leadership.

GNU/Linux est avant tout un choix de société à travers ces valeurs en refusant l'emprise des monopoles informatiques, la liberté de créer et diffuser le savoir, l'ouverture du code source. Une société qui facilite les STEM (Sciences, Technique, Ingénierie, Mathématiques) avec des outils accessibles pour aider au développement.

Quand on est nouveau dans le milieu voila quelques sites pour s'informer et acquérir la connaissance nécessaire:

*   [GoFOSS](https://gofoss.net/fr/) les libertés numériques pour tou.tes
*   L'[April](https://april.org/) promouvoir et défendre le logiciel libre
*   [Framasoft](https://framasoft.org/fr/) réseau d'éducation populaire au logiciel libre
*   [La quadrature du net](https://www.laquadrature.net/) association de défense des droits et libertés sur internet
*   [Electronic Frontier Foundation](https://www.eff.org/fr) est une ONG de défense des libertés sur internet
*   [Free Software Foundation](https://www.fsf.org/?set_language=fr) promouvoit les libertés informatiques

  

Si Ubuntu est la distribution de choix pour démarrer sous GNU/Linux, j'ai tendance à promouvoir l'utilisation de système basé sur Arch Linux tel que Manjaro plus facile d'accès. J'utilise sur mon ordinateur personnel Manjaro sans chiffrement du disque dur, et sur mon ordinateur de travail Arch Linux avec chiffrement du disque dur. Manjaro est plus stable, il y a moins de risque de faire planter le système sur une mise à jour. De plus tout peu ce faire avec une interface graphique. Seul la maintenance avancée est en ligne de commande. Beaucoup de Hackers utilisent Arch Linux car ils maitrisent mieux le système ou Gentoo pour utilisateur averti. On va dire que le novice ira vers les outils de Kali Linux car l'accès est facile.

Switcher vers GNU/Linux demande quelques compétences en particulier il faudra approfondir des notions en BIOS et UEFI pour démarrer sur une clé USB avec le système GNU/Linux. Rare sont les ordinateurs vendu en natif sous GNU/Linux. Je connais en clavier AZERTY [Starbook pour 900€.](https://starlabs.systems/pages/starbook) Mais ce n'est pas raisonnable pour débuter il vaut mieux acheter soit un Raspberry Pi ou un PC à 400€-600€ tel que des Lenovo Thinkpad reconditionnés. Avoir un PC dédié ou l'on peut ré-installer en cas d'erreur est plus sur. Acheter pour ces enfants un MacBook pro pour apprendre l'informatique sert à rien. Les meilleurs développeurs sont sous GNU/Linux.

Retenez:

1.  Récupérer le fichier .iso du système d'exploitation GNU/Linux sur le website, ici je choisi le bureau [GNOME sous Manjaro](https://manjaro.org/downloads/official/gnome/).
2.  Télécharger rufus sous Windows pour [créer un USB Bootable](https://lecrabeinfo.net/creer-cle-usb-installation-bootable-live-cd-linux-ubuntu-debian.html) du système d'exploitation.
3.  Vérifier que dans votre BIOS vous êtes en UEFI et que la priorité au démarrage des médias tel que la clé USB soit prioritaire. 
4.  Installer le système avec le lien dans le système, souvent sur le bureau. Vous trouverez un résumé en français dans le [guide de l'utilisateur Manjaro](https://free.nchc.org.tw/osdn//storage/g/m/ma/manjaro/Manjaro-User-Guide-French.pdf).
5.  Prenez du café ou thé, pour les plus nerveux de la Red Bull durant l'installation.

  

Question intéressante: _Je veux apprendre à coder à mes enfants pour qu'ils ont une culture informatique, je fais quoi?_

Raspberry Pi est une solution dans un premier temps, c'est un outil dédié à l'éducation à moindre frais en informatique, les outils sont installé en natif tel que Scratch ou un interpréteur Python. Il faudra toujours acheté un écran et clavier mais on peut faire de la récupération du matériel pour s'en tirer pour moins de cent cinquante euros en cherchant du reconditionné ou de l'occasion sur le bon coin. Je dirais à partir de 6 ans. En même temps que l'on apprend le langage, on peut utiliser Scratch.

C'est comme je le dis un choix de société, la plupart des utilisateurs sous Windows sont des consommateurs, alors que sous Linux, ils produisent du code, sécurise, utilise des logiciels scientifiques ou de productivité. Il faut viser cette dimension pour ne pas subir la mondialisation sans être des acteurs. Ils ne subissent plus l'informatique. Je considère les utilisateurs de GNU/Linux plus averti des enjeux car ils sont plus à l'aise avec les outils.

Enfin rejoignez un groupe d'utilisateur de GNU/Linux dans votre région pour partager votre expérience et trouver de l'aide. Dans le jargon on appel cela un GUL listé à [cette adresse du site de l'Aful](https://aful.org/gul/).
