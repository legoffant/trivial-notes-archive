Title:Chiffrer ces emails et générer des clés PGP
Date: 2023-09-08 08:28
Category:Inclassable
Tags:mail, pgp
Authors: Anthony Le Goff
Summary:

Tout utilisateur avancée de l'informatique protège son travail avec de la cryptographie et ces communications. C'est le domaine et le monde des cipherpunks. Globalement internet utilise de plus en plus la cryptographie pour:

* Sécuriser les transactions financières
* Protéger l'intégrité des données
* Rendre les communications privées
* Sécuriser l'authentification

Il faut donc avoir quelques notions pour l'utilisateur averti d'un outil essentiel : openPGP qui utilise la méthode [chiffrement asymétrique](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique). Le créateur de PGP(Pretty Good Privacy), 	Philip Zimmermann, a été violamment réprimandé par les gouvernements, à l'origine ceux-ci ne veulent pas que la population est accès la cryptographie. Zimmermann à violé le "Arms Export Control Act" des USA. La cryptologie est une arme de guerre.

Citation de Zimmermann: « If privacy is outlawed, only outlaws will have privacy », soit, en français : « Si la vie privée est mise hors la loi, seuls les hors-la-loi auront une vie privée. »

Comment utiliser PGP et le chiffrement asymétrique? Il faut savoir qu'une clé RSA peut être utilisé que cela soit pour openSSL ou openPGP / GnuPG.

Nous allons l'utiliser pour chiffrer nos messages sur un email et servir d'authentification sécurisé tel que pour maintenir un logiciel et la signature du mainteneur dans les dépôts sous GNU/Linux.

1] Tout d'abord créer un email généraliste ou l'on peut utiliser PGP et intégrer des API. Un compte webmail Gmail est suffisant, ne vous inquietez pas si l'email est sur les serveurs de Google, ils n'ont pas accès aux emails chiffrés. 

2] Utiliser un outil pour générer des clés PGP public et privée. Mettez un mot de passe, taille de la clé 4096 bits, et algorithme RSA. Pas de temps d'expiration tel que sur [https://pgptool.org/](https://pgptool.org/). Récuperez les fichiers, rappel votre clé privée est personnel et ne se partage pas, elle doit être protégée sur une partition chiffrée.

3] Utilisez un outil qui gère la signature PGP pour les emails. Vous pouvez utiliser le client Thunderbird avec Enigmail. Mais egalement un webmail Gmail avec [Mailvelope](https://www.malekal.com/utiliser-pgp-sur-gmail-pour-le-chiffrement-de-mail/).

4] Rendre votre clé public accessible pour authentifier votre signature. Il y a des serveurs généralistes qui collecte les clés, en particulier sur GNU/Linux pour la signature des dépôts. Ainsi transféré votre clé sur le serveur d'Ubuntu en copiant votre clé public. Aller sur [https://keyserver.ubuntu.com/](https://keyserver.ubuntu.com/). Il y a également le serveur du MIT [https://pgp.mit.edu/](https://pgp.mit.edu/) mais également sur [https://keys.openpgp.org/](https://keys.openpgp.org/). Les serveurs sont synchronisés entre eux.

5] Partager le lien de votre clé public pour pouvoir l'utiliser. Comment est formaté un lien public vers une clé PGP?

C'est sous la forme: `nom + mail + signature` exemple pour ma propre clé: [Anthony Le Goff legoff.ant[at]gmail.com 0x6F3B7C4C](https://keyserver.ubuntu.com/pks/lookup?search=0x6F3B7C4C&fingerprint=on&op=index)

Bienvenue dans le monde des cipherpunks.