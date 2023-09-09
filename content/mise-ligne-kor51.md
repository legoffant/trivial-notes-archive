Title:Mise en ligne de kor51.org
Date: 2023-09-09 13:09
Category:Inclassable
Tags:kor51
Authors: Anthony Le Goff
Summary:


Voila que le site **"Kor 51"** est up temporairement chez OVH. J'ai utilisé un hébergement web basic: [Hébebergement web perso 3,29€/mois](https://www.ovhcloud.com/fr/web-hosting/), juste pour afficher une page statique HTML, rien de bien compliquée.

Le site est accesible à l'adresse [http://kor51.org](http://kor51.org). 

Le certificat SSL est en cours de validation, et devrait basculer en HTTPS dans la journée.

Alors cela fonctionne comment de créer une simple page web statique en HTML? J'ai utilisé le générateur de site Statique Hugo, puis j'ai transféré par SFTP via Filezilla mes dossiers et fichiers dans "public" sur le dossier racine de l'hébergement web dans `www`, veuillez à tous supprimer avant ce qu'il y a dans le dossier et les liens symboliques. Il faut également configuré et lié le nom de domaine de l'hébergement.

OVH est un bon service car il y a de la documentation, tout est expliqué sur internet, à n'importe qu'elle débutant en informatique.

1] [Premiers pas avec un hébergement web](https://help.ovhcloud.com/csm/fr-web-hosting-getting-started?id=kb_article_view&sysparm_article=KB0052770)

2] [Tutoriel - Utiliser FileZilla avec votre hébergement OVHcloud](https://help.ovhcloud.com/csm/fr-web-hosting-filezilla?id=kb_article_view&sysparm_article=KB0052749)

3] [Tutoriel - Créer sa page web personnelle chez OVHcloud](https://help.ovhcloud.com/csm/fr-hosting-create-web-page?id=kb_article_view&sysparm_article=KB0052525)

Bien sur c'est temporaire, des que mon serveur Proxmox et mon réseau locale est up en auto-hébergé, je transfert le site. Il me faut créer une VM dédié sous Debian et configuré Nginx. Après je dois rendre accessible depuis internet mes services auto-hébergés. J'ai fais une demande d'IP fixe à Free qui fournis le service. 