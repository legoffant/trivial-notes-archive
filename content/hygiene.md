Title: Un peu d'hygiène informatique
Date: 2022-11-8 10:24
Category:Entrepreneurship
Tags:securité, chiffrement, mot de passe
Authors: Anthony Le Goff
Summary:

Voila que vous commencer à vous demander comment protéger les individus dans les communications ou business en particulier si vous faites des choses un peu illégal par la loi tels qu'ouvrir un commerce de vente d'arme sur le darknet.

Déjà, il est sain d'être parano, c'est une protection nécessaire à toute réussite d'entreprise.

Vous devez **anticiper la perquisition**. L'échec est possible. Ce que vous devez faire pour tous processus de commerce en règle général:

* Protéger les fonds
* Protéger les clients
* Protéger les outils de production, que vous continuer à vendre même absent: votre revenu passif

Sinon on a affaire à des amateurs et si votre réseau tombe avec vous en allant en prison, vous allez vous faire des ennemis et nuire à votre réputation: Vous ne se seriez pas quelqu'un de fiable, et la confiance est parfois long à construire. C'est le Ba-Ba du commerce.

Le scénario simple: Vous avez un porte-feuille de cryptomonnaie sur votre ordinateur, des bitcoins, admettons 50 000€ en bitcoin dans la trésorerie qui vous servent à acheter des armes sur le darknet pour les revendre localement.

Vous devez protéger vos traces contre le footprinting, et être le plus discret possible. En vous connectant via un VPN à Tor, entrée en communication sur des messageries chiffré mais en plus votre historique internet vous dénoncerais à la police de vos activités, il faut donc protéger l'ordinateur:

* Politique de mot de passe
* Chiffrement du disque dur 

Vos bitcoins aussi doivent être protégé. Admettons vous mourrez d'une crise cardiaque, c'est balo. Qui récupère votre ordinateur? Il va ce connecter, entrée sur la session fouillé un peu et découvrir votre porte-feuille? Bel héritage. Scénario 2 vous avez un mot de passe de session. Ah! Ok mais n'importe quel idiot utilisant un live CD sous Linux accédera aux fichiers du disque dur local si celui-ci n'est pas chiffré.

Comme dirait certain, rien à cacher, la devise des gens qui n'ont aucun commerce.

Non on fait pas les choses comme ça. 

Vous pourriez avoir plein de raison de protéger votre PC, tels que si vous faites des recherches sensibles ou des investigations journalistique, ou tout simplement écrire un livre et protéger la publication ou votre journal intime.

Les données c'est le pouvoir, le renseignement l'outil du Prince: avoir les bonnes informations, analyser et filtrer au bon moment.

*Politique de mot de passe*:

* Il vous faut un mot de passe fort de 16 caractères pour le chiffrement de votre disque dur, capable de résister à des attaques tels que le brute force et par dictionnaire.
* Un mot de passe de session
* Un protocole de mots de passe dynamique pour vos sites internet


Comment créer un mot de passe facile à retenir?

Exemple: vous apprenez par coeur un poème, vous prenez les 2 premiers caractères de chaques mots, vous y ajoutez du l33t. Cela est votre mot de pasee de session.

Puis les mots de passes dynamique des sites internet:

A votre mot de passe de session vous ajoutez les 2 premières ou dernières lettres du nom du site dans l'URL.

Voila comment vos mots de passe change sur chaque site, en applicant ce protocole.

*Chiffrement du disque dur*

Windows n'a pas cette fonction en natif, car le système de monsieur tous le monde est vulnérable pour faciliter les enquètes et investigations d'organisme comme le FBI ou Interpol. Les naîfs

Sous Linux, à l'installation de tous les systèmes on peut demander à chiffrer le disque. Pour une utilisation plus pointu de dm-crypt/LUKS passer sous Arch Linux.

**ON NOTE JAMAIS UN MOT DE PASSE SUR UN BOUT DE PAPIER! VOUS AVEZ UNE MEMOIRE**

RETENEZ: L'important est de créer des silos pour protéger les biens et les personnes à travers une boite noire, la sécurité par l'obscurité implique des protocoles de chiffrement qui agit comme filtre. D'utiliser des intermédiaires pour communiquer qui vous représente.

Un dernier mot sur VeraCrypt. Pour vos donnez les plus sensibles vous pouvez utiliser l'utilitaire et cacher sous un nom anodin des données, en créant des container.

INCEPTION: Votre OS chiffré créé Un machine virtuelle sous KVM/VirtualBox chiffré qui contient un container veraCrypt est une méthode qui rendra fou les enquêtes. 

Soyez vicieux. Aucune pitié pour profiter du système.