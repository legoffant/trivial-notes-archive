Title:Méthodologie pour sécuriser son ordinateur
Date: 2023-04-06 09:28
Category:Linux
Tags:securité
Authors: Anthony Le Goff
Summary:


On arrive à la fin d'un âge avec la prolifération des attaques informatiques ou l'utilisateur n'était qu'un consommateur ou celui-ci doit maintenant reprendre le contrôle de sa machine. Pour ce protéger, il n'y a pas beaucoup de méthode à appliquer à part celle-ci:  

```
A armes égales, et donc une militarisation du cyberespace.  
```

Vous ne pouvez pas protéger de l'information et votre organisation, car beaucoup d'entreprise font faillite après une attaque informatique, et être productif sur votre poste de travail sans penser comme un hacker. Même si les hackers le savent très bien la faille est principalement humaine et l'ingénierie sociale reste l'art de duper son adversaire pour l'exploiter. C'est aussi vaincre par votre niveau de connaissance des pratiques de sécurité sur les systèmes et le renseignement sur le terrain tel que la veille.  

On voit qu'au niveau de la prolifération des méthodologies d'attaques, les hackers cybercriminels recherchent à monnayer des secrets. Entrée sur des bases de donnée, récupérer des informations de clients, mot de passe, d'informations bancaires, des portes-feuilles de cryptomonnaies. Les infostealers sont par exemple en pleine expansion. On est loin des APT (Advanced Persistant Threat) tel que le célèbre Stuxnet pour endommager des structures qui reste rare tel que sur les SCADA dans l'industrie pour rendre inopérant une cible. La technique également qui fait parler d'elle le ransomware pour faire chanter les organisations de payer une rançon en bloquant l'accès à ces documents numériques, sous peine de destruction depuis l'épidemie de l'attaque Wannacry (2017) et la vulnérabilité Eternal Blue. Internet à basculé après l'attaque par botnet Mirai (2016) ciblant l'internet des objets. Microsoft a vu tout son système d'authentification mis à l'épreuve avec Mimikatz (2012).  

Présentons donc une méthodologie pour ce protéger des hackers et éduquer au numérique, ce que l'on apprend pas à l'école, nos politiques veulent surveiller la population, que le flic puisse enquêté sur votre ordinateur pour trouver vos photos pedopornographiques, ou vos activités illégales, ils sont totalement obsédés par l'accès aux systèmes informatiques par les services de renseignement.  

### Ne faite confiance qu'à l'open source  

La règle est de rendre le code source ouvert pour auditer permettant sa maintenance et son amélioration. Un système propriétaire permet d'intégrer des backdoors pour espionner qui est une atteinte à la vie privée, ainsi que de la télémetrie pour exploiter vos données. Les gouvernements favorisent l'utilisation des systèmes propriétaires pour cette raison sur l'ingénierie logiciel. Donc oublié MacOS et Windows, passé à GNU/Linux. La NSA a tenté de backdoorer le noyau Linux, sans succès.  

### Réduire la surface d'attaque  

N'allez pas vers des systèmes qui sont infecté par des virus et malwares, + 96% des malwares sont sur Windows. Linux n'est touché qu'à hauteur de 1% par les ransomwares. Ce qui est mainstream est plus vulnérable. Le système d'exploitation le plus sécurisé au monde est un UNIX libre: openBSD. Préférer le minimalisme, n'installer que le strict nécessaire sur le système tel que des distributions sur mesure comme Arch Linux ou Gentoo. Linux est vulnérable, et Debian en 20 ans à générer un nombre important de CVE qui sont patché régulièrement, un code open source permet à n'importe qui de chercher des vulnérabilités. Alléger votre bootloader et activer le secure boot de l'UEFI pour empêcher au démarrage du code inconnu comme l'attaque ["Evil Maid"](https://www.schneier.com/blog/archives/2009/10/evil_maid_attac.html). Réduiser votre utilisation d'application avec une interface graphique GUI et utiliser des serveurs d'affichage plus sur tel que Wayland. Vous serez plus productif et sécurisé en utilisant le terminal en CLI.  

### Le chiffrement  

Le système doit être protégé par le chiffrement avec des outils tel que dm-crypt/ LUKS pour protéger vos documents sensibles et information de connexion, voir de porte-feuille de cryptomonnaie. La connexion réseau doit également être chiffré via SSL et TLS en forçant HTTPS, pour éviter des attaques de type MITM, souvent le VPN est préconisé. Quand vous chercher à à vous connecter à des mirrors et repository sous Arch Linux en utilisant reflector forçé la connexion HTTPS. Préconiser l'utilisation de clé de chiffrement pour vous connecter en remote sur un serveur distant. Vous devez savoir utiliser GPG mais également de créer des containers Veracrypt en applicant la sécurité par l'obscurité. Ayez des notions sur le hashage, les mots de passe ne doivent pas exister en clair dans une base de donnée.  

### Contrôle d'accès  

Les programmes malveillants cherchent à escalader les privilèges pour prendre le contrôle de la machine. Le système doit protéger les actions de modification tel que le compte administrateur avec un mot de passe comme root sous Linux. Ainsi vous devez avoir des mots de passe différent en fonction du niveau de privilège sur le système en cas de compromission:  

*   1 mot de passe pour la partition chiffrée + 16 caractères  
    
*   1 mot de passe pour le compte administrateur root + 12 caractères  
    
*   1 mot de passe sur chaques sites webs différents et dynamique + 8 caractères  
    

Vous devez utiliser un gestionnaire de mot de passe comme Keepass et garder la base de donnée en local sur votre machine. Ne jamais faire confiance au cloud et un tiers-parti en intermédiaire ou les données sont stocké à distance. Votre mot de passe doit être résistant à des attaques par dictionnaire et brute force.  

### Utilisez un gestionnaire de paquet  

Vous devez avoir une source de confiance pour les logiciels sur des dépots distants que vous installez et vérifiez qu'ils ne sont pas corrompu tel que la signature GPG du mainteneur. D'ou l'utilisation de GNU/Linux, comme pacman, rpm, apt, emerge, etc.  

### Auditer le système  

Les vulnérabilités CVE sont régulièrement mise à jours, la dernière en date "Dirty Pipe" sur le noyau Linux à fait parler d'elle, vous devez auditer le système avec des outils tel que Lynis et appliquer des contres-mesures d' "hardening" en particulier sur le noyau Linux comme AppArmor, SELinux, Grsecurity et LKRG. Il faut faire une recherche de rootkit régulièrement avec chkrootkit mais également de malware, il y en a sur Linux en utilisant Yara avec des règles prédifinis comme le repo ["Protections Artifacts"](https://github.com/elastic/protections-artifacts) d'Elastic Security.  

### Rolling Release pour mettre à jours le système  

Patcher le système dès que les paquets logiciels sont disponible en intégrant la rolling release. C'est la particularité des distributions GNU/Linux basé sur Arch Linux, tel que Manjaro, Archcraft, etc.  

### Monitoring  

Vous pouvez détecter des comportements anormaux sur votre système en faisant du monitoring sur les ressources en particulier les processus et l'outil htop, mais également sur le réseau car les programmes malveillants cherchent à communiquer avec l'extérieur pour extraire de l'information et l'utilisation de port (ssh, samba, http, etc) et l'outil ss ou netstat. Il est possible d'analyser les paquets avec l'outil tcpdump.  

### Logs  

Un programme malveillant doit être furtif et les hackers effacer leur trace sur la cible. Pourtant ils peuvent laisser des empreintes sur les accès sur le système en vérifiant les logs. Windows n'a toujours pas compris ça et Linux intègre un système de logs avancé tel que sur les services avec systemd et journalctl voir l'outil syslog-ng.  

### Sauvegarde et restauration  

De nos jours les systèmes les plus avancés intègrent un système de sauvegarde automatisé périodique en cas de compromission. La technique utilisé en particulier est les snapshots qu'il est possible de créer avec des systèmes de fichier comme BTRFS et des outils comme Snapper + snap-pac sur Arch Linux pour sauvegarder à chaque mise à jour en cas que vous casser le système pour le restaurer. Il faut coupler à une sauvegarde de l'environnement utilisateur tels que les .dotfiles et les documents en utilisant des outils pour chiffrer des sauvegardes dans le cloud ou sur un NAS. Il y a Duplicity, Borg, Bacula mais également Rsync ou Rclone. En règle général il faut une sauvegarde locale + distante. En cas de perquisition ou de vol à votre domicile, vos données doivent être disponible à distance.  

### Conclusion  

En terme de pratique de sécurité sur les ordinateurs, Windows c'est le moyen-âge et MacOS par son caractère propriétaire n'est pas une source de confiance pour l'audit du code. Quand on connait rien à l'informatique et que l'on ne veut pas trop s'en occuper, je conseil le chromebook qui est un Gentoo allegé mais vous êtes dépendant des GAFAM comme Google et ces services. Les pratiques de cybersécurité sont un héritage des administrateurs systèmes de serveur et donc l'utilisation de GNU/Linux sur le marché quand on cherche à maintenir une disponibilité de l'outil de production et des services.