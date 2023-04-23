Title:Proxmox HomeLab
Date: 2023-04-23 10:24
Category:Linux
Tags:homelab
Authors: Anthony Le Goff
Summary:

On va parler un peu de serveur. Notre monde fonctionne actuellement sous l'apartheid informatique dans le sens que les utilisateurs Windows et MacOS sous logiciels propriétaires ne connaissent rien en serveur, alors que les libristes, hackers et utilisateurs de Linux sont des experts, c'est dans leur seconde nature. Tout simplement car l'infrastructure d'internet fonctionne entièrement sous le logiciel libre et open source. Le Top 1 million des sites mondiaux fonctionnent sous un serveur web Linux à 96,3% mais également plus de 90% des infrastructures en cloud computing. [Stats Linux](https://truelist.co/blog/linux-statistics/).  

Clairement Windows server est marginal, peu de service et vulnérable, et quand on se lance dans l'apprentissage des serveurs, c'est du pure suicide, certain sont des Microsoft fanboys en particulier pour de l'utilisation avec Azure. De nombreux serveurs ont une stack de base sous Debian LAMP (Linux Apache MySQL PHP), c'est old school mais toujours d'actualité chez les "tradis" pour le développement de services web.  

Débuter sur serveur ne demande pas un grand investissement, il est possible de commencer sur un [Raspberry Pi Zero W à 18€](https://www.kubii.fr/pi-zero-w/1851-raspberry-pi-zero-w-3272496006997.html) fonctionne avec un Debian lite (RaspberryPi OS). Il y a beaucoup de documentation pour les apprenants. [Quelques idées de projets](https://raspberrytips.fr/projets-raspberry-pi-zero-2w/). Personnellement je préfère le modèle [MangoPi MQ Pro à 30€](https://fr.aliexpress.com/item/1005004157984532.html) sur architecture RISC-V en processeur. Windows server ne fonctionne pas sur nano-ordinateur et système embarqué, vous êtes prévenu c'est de la daube, problème de compatibilité matériel, mais également d'utilisation des ressources sur des configurations minimalistes.  

### L'auto-hébergement  

Si vous voulez monter en compétence chez soi sur serveur, vous faites de l'auto-hébergement en particulier dans le cadre pour contrôler vos données que cela soit personnel ou entreprise et déployer des services. Cela demande quelques compétences en réseau informatique et administration système et tester des technologies localement. Un web entrepreneur a raison de monter en compétence sur serveur pour préparer des services d'entreprises et gérer les données localement, en réalité l'entrepreneur est garant des données et donc du patrimoine informationnel de son entreprise et de la gestion du système d'information (SI). Il faut planifier en amont des sauvegardes et possibilités de migration des données et services quand l'entreprise monte en puissance, ce que l'on appel du [scaling](https://www.leslivresblancs.fr/dossier/tout-comprendre-de-la-scalabilite-du-scaling-et-de-la-scale). D'ou que l'on utilise la technologie de virtualisation sur serveur.  

### Proxmox  

L'un des produits open source largement plébiscité est [Proxmox VE](https://www.proxmox.com/en/) pour de la virtualisation sur serveur avec comme hyperviseur KVM et des containers LXC. C'est un standard actuellement dans la construction de Homelab mais également pour des TPE ou associations. L'interface d'administration des machines virtuelles (VM) est intuitive, mais également pour utiliser des technologies comme les snapshots ou le RAID avec le système de fichier ZFS. Proxmox est une distro Linux Debian avec une surcouche de management de VM et d'interface d'administration.  

Le matériel nécessaire est en fonction de ces propres besoins. Vous pouvez commencer sur du pré-construit comme un Intel NUC et seulement 4GB de ram à 150€, voir des Lenovo Thinkcentre en mini-PC. Une VM fait généralement à minima 512Mo de RAM pour un serveur.  

Pour un Homelab performant, il est nécessaire de monter soi-même sa configuration et mettre entre 1000 à 2000€, avec du matériel dédié pour serveur tel qu'un processeur Xeon ou des disques durs pour NAS comme la série Iron Wolf. J'ai ma préférence pour l'utilisation du format mini-ITX en carte-mère et un boitier adapté avec 4 à 6 emplacement de disques durs comme le "[fractal design node 304](https://www.fractal-design.com/products/cases/node/node-304/black/)" qui permet de réduire l'encombrement. Vous trouverez sur [ce guide pour NAS](https://forums.serverbuilds.net/t/guide-nas-killer-4-0-fast-quiet-power-efficient-and-flexible-starting-at-125/667), des configurations matériels détaillées d'Homelab.  

Proxmox permet d'utiliser la technologie PCI Passthrough pour utiliser une carte graphique et déployer une machine virtuelle dédiée à de l'utilisation de GPU intensive comme du Cloud Gaming. Il est possible de ce connecter à distance depuis votre PC sur votre réseau local à une VM de Cloud Gaming avec une environnement isolé et pré-configuré, c'est pratique si votre PC ne permet pas d'utiliser une carte graphique ou installer des produits, jeux. Seulement faudra une configuration matériel puissante que cela soit en processeur, ram et alimentation. Cela me permet d'invoquer une session à distance sous Arch Linux via Remmina en me connectant au serveur.  

La configuration de mon propre serveur Proxmox à titre indicatif:  

```Text

###########################################################
Config Server mini-ITX CPU Ryzen 5  64GO RAM 4x2TO HDD RAID
###########################################################
Par ldlc.com

- Carte mère: ASRock A520M-ITX/ac 119€95
- CPU: AMD Ryzen 5 5500 Wraith Stealth 6 cores (3.6 GHz / 4.2 GHz) 157€96
- Boitier: Fractal Design Node 304 Noir 119€95
- RAM: Corsair Vengeance LPX Series Low Profile 64 Go (2x 32 Go) DDR4 3200 MHz CL16 256€95
- HDD: 4 x Seagate IronWolf 2 To 395€80
- Alimentation: be quiet! Straight Power 11 450W 80PLUS Gold  107€95
- Ventirad: Noctua NH-L9a-AM4 59€
- Cable: 2 x Corsair Câbles SATA Gainés Droits/Coudés 30 cm (coloris bleu) 29€90
- Clavier: Advance GTA 230 (AZERTY Français) 19€94
- GPU: Zotac NVIDIA GTX 1650 OC 4GB 180€ 

total: 1440€
```

### Configuration  

Quand vous devez configurer la première fois le serveur, il faut mettre en place un OS "bare metal" en installant l'iso de Proxmox via USB. Il faut un écran, clavier et souris. On doit choisir les volumes, mettre en place le RAID, les paramètres d'administration et réseau. Qui ne serve qu'une fois, ou en cas de maintenance critique et d'accès réseau à distance coupé. Une fois le serveur configuré, on ce connecte à distance sur le réseau local depuis son PC de travail. [Installer Proxmox et lancer sa première VM](https://www.it-connect.fr/comment-installer-proxmox-ve-7-0-et-creer-sa-premiere-vm/).  

### Services Homelab  

Il est possible de déployer énormément de services ou de les créer. Il y a une pléthore de programme et apps open source pour de l'auto-hébergement. Vous trouverez une [liste Awesome "self-hosted"](https://github.com/awesome-selfhosted/awesome-selfhosted). Dans l'exemple d'une association, il est possible de déployer un ERP pour la comptabilité: Dolibarr + outils de collaboration et de gestion de document: Nextcloud + un site statique (Jekyll en Ruby) + service de mailing list (Sympa) pour la communication.  

Après dans les outils plébiscités on retrouve:  

*   Prometheus  
    
*   Terraform  
    
*   Kubernetes  
    
*   Docker  
    
*   Portainer  
    
*   Plex  
    
*   Ansible  
    
*   Pi-Hole  
    
*   Webmin  
    

Le mieux est de se renseigner sur internet, il y a des articles de blogs et vidéos Youtube sur le type d'utilisation d'un HomeLab avec retour d'expérience. [HomeLab Services Tour Late 2021 - What am I Self-Hosting in my HomeLab?](https://www.youtube.com/watch?v=IE5y2_S8S8U)  

Cela reste très chronophage que d'apprendre avec un HomeLab, et de monter en compétence en [sysAdmin](https://legoffant.github.io/ressources-pour-sysadmin-linux.html). On peut déployer des VMs pour beaucoup de choses, même pour hacker et apprendre sur son propre réseau avec des vulnérabilités.