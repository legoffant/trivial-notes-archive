Title:Comment créer un site web
Date: 2023-09-15 11:05
Category:Inclassable
Tags:site
Authors: Anthony Le Goff
Summary:

Comment créer un site web

Parlons un peu du web, créer un site n'est pas bien difficile, il y a des plateformes spécialisés pour les gros noobs tel que Wix. Tout dépend des fonctions que l'on recherche à avoir sur un site. 

Comment apprendre à créer un site? La plupart des hébergeurs proposent une solution tout-en-un d'hébergement mutualisé de site pour généralement 5€-7€ / mois. 

Pourquoi avoir son propre site?

* Projet personnel (landing pages, CV, Portfolio, e-influence & personal branding)
* Entreprise (fournir des services)
* E-Commerce (vente de produits)

Si vous voulez-vous mettre à votre compte, avoir une stratégie de diffusion de vos services est utile, tout en automatisant la facturation ou la vente de produit pour augmenter vos ventes.

Les hébergements web vendu par OVH sont en particulier l'offre ["hebergement web perso" à 3,95€/mois](https://www.ovhcloud.com/fr/web-hosting/personal-offer/). C'est très bien pour les débutants. Cela donne accès à:

* Installation de CMS en un clic
* 100GO disques
* Un nom de domaine
* FTP

Utilise PHP et généralement mySQL en base de donnée. Généralement si vous voulez juste faire du web dev (HTML + CSS + Javascript) c'est suffisant.

### Serveur VPS

L'offre standard largement plébiscité est le serveur VPS chez les hébergeurs. A quoi cela sert? Une meilleure maitrise du serveur. On vous loue un serveur avec juste un système d'exploitation, généralement sous GNU/Linux. C'est de l'administration système vous gérer la stack serveur, et vous devez installer vous mêmes des produits tels que le serveur web (apache, nginx), php + mySQL. Ce que l'on appel la stack oldschool LAMP. 

Chez OVH il y a [l'offre Kimsufi à petit prix à 4,20€/mois](https://www.kimsufi.com/fr/vps/).

### CMS

Quels sont les CMS pour gérer son site les plus plesbiscités? 50% des sites sont sur Wordpress. Il y a également Joomla et Drupal. C'est les trois leaders sur le marché basé sur une couche PHP. Avec Wordpress vous pouvez créer un blog (overkill), un site d'e-commerce avec des plugins, un site d'entreprise, etc...

### Les stacks serveurs

Dans le développement web ils existent des leaders pour fabriquer des sites sur mesure de A à Z. A travers des stacks et frameworks tel que:

* LAMP (Linux Apache MySQL PHP)
* MERN (MongoDB Express React.Js Node)
* Django
* RoR (Ruby On Rails)

### Les pages statiques

Si vous voulez juste créer une landing page autant utiliser juste HTML+CSS. Une fois que vous avez un serveur web disponible (apache, nginx). Pas la peine de sortir l'artillerie lourde. Pour créer [https://kor51.org](https://www.kimsufi.com/fr/vps/), j'ai juste utilisé un générateur de site statique Hugo + Thème Console que j'ai pushé via SFTP et Filezilla sur un hébergement web chez OVH. 

### Les blogs et générateurs de site statique

On peut créer un blog ou un site personnel avec un site statique, j'avais expliquer la procédure avec Jekyll et les particularités du milieu, dont on peut trouver des hébergeurs gratuits comme Github Pages. Mais généralement c'est des développeurs qui utilisent cette méthode. 

Les générateurs de site statique réputés:

* Jekyll (ruby)
* Gatsby (JS React)
* Pelican (Python)
* Hugo (go)

