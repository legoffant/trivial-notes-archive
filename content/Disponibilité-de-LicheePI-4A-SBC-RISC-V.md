Title:Disponibilité de LicheePI 4A SBC RISC-V
Date: 2023-07-10 06:01
Category:Linux
Tags:riscv, sbc
Authors: Anthony Le Goff
Summary:

La nouvelle carte de prototypage électronique sous RISC-V est disponible à la vente dans le commerce sur internet. Je suis très intéressé par en acheter une mais, voila qu'il y a de nouveaux problèmes qui m'empêche de basculer.  

Tout d'abord je cherche à utiliser une machine en production pour le travail sous RISC-V qui soit économe en énergie. Il faut au minimum 4 coeurs de processeur + 16GB RAM + 128GB disque interne.  

De ce fait la carte de Sipeed LicheePI 4A est une très bonne candidate sur le plan hardware et le processeur TH1520 avec GPU Imagination. Elle vient concurrencé Raspberry Pi, et l'une des premières cartes avec 16GB de RAM. Pour rappel le [Raspberry Pi 4 8GB est à 95€](https://www.kubii.com/fr/cartes-raspberry-pi/2955-raspberry-pi-4-modele-b-8gb-3272496309050.html).  

Elle est vendu en [plusieurs modèle sur AliExpress](https://fr.aliexpress.com/item/1005005532736080.html?aff_fcid=74f1cc167ecc4249a5ffefeb997a0eb1-1688960372367-09310-_DEFc0c9&tt=CPS_NORMAL&aff_fsk=_DEFc0c9&aff_platform=shareComponent-detail&sk=_DEFc0c9&aff_trace_key=74f1cc167ecc4249a5ffefeb997a0eb1-1688960372367-09310-_DEFc0c9&terminal_id=084e0e86dabf447d917ef70399d0e0bc&afSmartRedirect=y):  

*   8GB RAM + 64GB eMMC 154,76€+ 9€ frais de livraison  
    
*   16GB RAM + 128GB eMMC 205,20€+ 90€ frais de livraison  
    

  

J'étais intéressé par la version 16GB RAM. Mais clairement 90€ de frais de livraison, ils sont en plein délire, personne n’achètera. C'est de l'électronique, pas un animal vivant.... De plus il n'y a pas en vente d'adaptateur secteur pour l'Europe. Seulement US. Encore une erreur marketing, c'est chiant de chercher des composants et acheter à part dans d'autres boutiques. Les bundle.... C'est pas fait pour les chiens.  

De plus le support en système d'exploitation sous Linux est limité à:  

*   Debian  
    
*   openWRT  
    
*   Fedora  
    

Avec un [pure player sous Gentoo](https://wiki.gentoo.org/wiki/User:Dlan/RISC-V/TH1520) via le wiki. Mais rien sous Arch Linux? Encore un nouveau délire. Sur internet, aucune requête pour porter l'OS. Le néant. J'avais l'intention de basculer sous hyprland en production, bah sa attendra. Je reste sur Thinkpad (i7, 16GB RAM, 256GB SSD) + OS Custom ArchLinux + repo BlackArch XFCE plus stable pour la production.