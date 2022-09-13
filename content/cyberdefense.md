Title: Ma start-up cyberdefense
Date: 2022-09-13 19:48
Category:Entrepreneurship
Tags:Ressources, Linux, cyberdefense
Authors: Anthony Le Goff
Summary:

# Ma start-up Cyberdéfense

En 2013, avant l'affaire Snowden, je me suis lancé en tant que consultant indépendant sans réseau dans le milieu à 24 ans pour devenir expert en cyberdefense. Je suis un cipherpunk, c'est à dire je fais la promotion de l'utilisation de la cryptographie pour la défense de la vie privée, contre le vol de donnée, le secret industriel, la protection des sources. Je recherchais à être une aide au dirigeant plus particulièrement.

Je vais donc expliquer ici quelques principes de cyberdéfense, on va construire un sous-marin pour naviguer en furtif, qui sont ma valeur ajouté sur le marché du travail. Mes recherches sont utiles dans l'armement, l'industrie, le journalisme mais egalement dans l'hacktivisme, la cybercriminalité, le terrorisme ou les réseaux mafieux. Il ne faut pas ce voilé la face. 

0. Installer un système d'exploitation en vérifiant l'[intégrité de l'image ISO](https://linuxhint.com/md5_sha1_sha256_checksum_iso/) tel qu'il est possible sous Linux grâce à l'empreinte checksums MD5, sha1, sha256

1. Ne faites confiance qu'à Linux car le code source est ouvert et donc auditable. Les Etats et la sécurité intérieur pour des besoins d'enquête et de fichage de la population ont des portes dérobées dans les produits Microsoft Windows et Appel macOS qui sont des sources propriétaires. Le code malveillant peu y être injecté. Il y a une volonté de rendre vulnérable le système. Le noyau Linux a été plusieurs fois approché par la NSA pour intégré une porte dérobée, ils rêvent complètement. 

2. Préférer des systèmes minimalistes comme Arch Linux, Gentoo, ou vous installer/compiler depuis les sources vous même les paquets nécessaires. Eviter d'installer quelque chose que vous ne comprenez pas. 

3. [Chiffrer votre disque dur](https://wiki.archlinux.org/title/Data-at-rest_encryption). Je m'attarde pas sur l'etat de l'art et les discussions s'il faut chiffrer /boot /tmp et la /swap. Cela enflamme souvent internet en fonction des failles et vulnérabilités.

4. Utiliser des dépôts logiciels avec une signature PGP qui permet d'avoir des sources de confiance. Chiffrer votre connexion internet en HTTPS pour récupérer les mirroirs des repository. Cela évite les attaques APT mais egalement l'installation de keylogger ou de trojan. J'utilise Arch Linux et le gestionnaire de paquet [pacman/signing](https://wiki.archlinux.org/title/Pacman/Package_signing) qui gère en natif. [Reflector](https://wiki.archlinux.org/title/Reflector) force la connexions en HTTPS vers les sources. 

5. Installer un par-feu tel que `ufw` et son interface graphique `gufw` Apprenez à configurer des règles

6. Vérifier les logs dans `/var/log` et installer `syslog-ng`

7. Installer un analyseur de rootkit `rkhunter`

8. Monitorer le système pour analyser des programmes ou script qui utilise du CPU, mémoire ou du réseau avec `htop` `iostat` `ss`

9. Faite de la sécurité par l'obscurité en créant des containers avec [Veracrypt](https://www.veracrypt.fr/en/Home.html) pour déposer vos documents TOP secret

10. Politique de gestion de mot de passe avec `Keepass`, permet de générer des mots de passe fort

11. Installer un VPN gratuit comme protonVPN, utiliser le service mail sécurisé.

12. Utiliser des services cloud sécurisés tel que MEGA.

13. Augmenter votre vie privée avec le navigateur [librewolf](https://librewolf.net/), un fork de Firefox voir utilisé tor browser.

14. Soyez furtif sur internet derrière des noeuds tor et plusieurs proxy avec `proxychains` pour vos activités sensible. Vérifier que la connexion à un site est en HTTPS en particulier les banques et utiliser un VPN si nécessaire.

15. Faite une veille des vulnérabilités et CVE. Via [https://www.cert.ssi.gouv.fr/](https://www.cert.ssi.gouv.fr/)

16. Mettez à jour votre système, préférez la rolling release comme Arch Linux qui publie les mises à jours de paquet en continue sur son site. Dès qu'un paquet est patcher pour une vulnérabilité faite la commande: `sudo pacman -Syu`

17. Sauvegarder incrémentalement votre système. Configurer des snapshots avec un système de fichier BTRFS. Prévoyer un NAS (Synology) pour vos sauvegardes local sur le serveur samba synchronisé dans le cloud à distance grâce à la fonction hyperbackup de Synology. Redondance de la sécurité pour assurer une sureté de fonctionnement. Utiliser l'utilitaire `deja-dup` de duplicity qui est simple pour chiffrer ces sauvegardes. Il existe d'autres programmes plus complexe comme Borg Backup ou Bacula.

19. Automatiser la ré-installation si le système est compromis avec des scripts et sauvegarder vos fichier [dotfiles](https://www.freecodecamp.org/news/dotfiles-what-is-a-dot-file-and-how-to-create-it-in-mac-and-linux/) tels que .zshrc , .vimrc , .gitconfig

20. Garder une clé de System Rescue tel que l'image d'Arch Linux. Booter sur la clé puis: Ouvrir le container chiffré LUKS, Monter les disques, chrooter l'environnement et faite la réparation nécessaire.

Tout cette procédure, je forme à la cyberdefense, c'est des années d'utilisation, de test et d'expérience des meilleurs pratiques. Ce qui est maintenant avant-gardiste, le cipherpunk sera la norme après que la cyberguerre aura détruit le système actuel, depuis Snowden cela a empiré, tous les états veulent leurs hackers sponsorisés pour voler des données, c'est un foutoir infernal et c'est politique. La cyber-armée est une vaste fumisterie. Nos futurs générations apprendrons à créer leur propre système et le customiser, nous sommes des pionniers, des visionnaires pour d'autre. Le coup fatal sera portée par l'internet quantique, on attend avec impatience que les politiques acceptent d'abandonner la surveillance pour rendre inviolable les communications. Let's Encrypt est l'une des initiatives post-Snowden de chiffrer les connexions HTTPS gratuitement avec des certificat, aucun gouvernement n'a soutenu l'initiative, nos politiques sont déconnecté de la problématique, ainsi que l'élite pensante tel que le corps des Mines, étant un ancien mineur, on ne forme pas à Linux en école d'ingénieur. La plupart des experts en cyberdefense sont complètement à l'ouest recommandant toujours plus de logiciel propriétaire payant pour faire des fonctions de sécurité. Le déni complet car c'est un gros business la cybersécurité: Si le code source n'est pas ouvert, et qu'il faut une licence, c'est de la merde pour faire du profit.Je ne suis pas seul, il y a les cipherpunks, la communauté Arch Linux, la Quadrature du Net. 

Je suis joignable dans 'contact' en utilisant protonmail en cas d'information sensible qui demande de la discrétion.

Je finirais l'article cette article par les outils d'hardening sous Linux pour éviter de compromettre un système. voir un IDS comme Snort que vous devez connaitre en cyberdefense.

* Bastille Linux [http://bastille-linux.sourceforge.net/](http://bastille-linux.sourceforge.net/)
* Lynis [https://cisofy.com/lynis/](https://cisofy.com/lynis/)
* nixarmor [https://github.com/emirozer/nixarmor](https://github.com/emirozer/nixarmor)
* Linux server hardening guide [https://github.com/imthenachoman/How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)

### Si vous voulez installer Arch Linux

Utilisez ma configuration, documenter vous pour apprendre, c'est en faisant que vous allez retenir les notions et lignes de commandes ainsi que l'utilité.

[https://legoffant.github.io/arch-linux-install-btrfs-chiffrement-uefi-xfce-timeshift.html](https://legoffant.github.io/arch-linux-install-btrfs-chiffrement-uefi-xfce-timeshift.html)

Ne dites pas que vous ne saviez pas! Des solutions techniques existent, mais c'est tout une culture underground à l'heure actuel. 

NOTA: Je n'ai pas parler de secure boot, signature du bootloader, mais je potasse.