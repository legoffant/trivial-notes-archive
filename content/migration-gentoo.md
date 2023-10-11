Title:Migration sur Gentoo
Date: 2023-10-11 20:56
Category:Inclassable
Tags:gentoo
Authors: Anthony Le Goff
Summary:

Je suis en train de préparer ma migration sur Gentoo, j'ai pris ma décision essentiellement pour quitter system-d. Mais également avoir plus de contrôle sur la distribution en compilant à la main. Je vais utiliser Pentoo. Je vais être en phase de test quelques temps pour tout vérifier que j'ai bien mes logiciels, la config visée:

* Gentoo + Pentoo en overlay
* DE: LXQT (j'utilise Qt en C++)
* Terminal: Kitty
* Shell: Zsh
* Init: openrc
* filesystem: BTRFS
* Encrypt: LUKS2
* Bootloader: EFI stub
* Login Manager: Ly

Je vais donc prototyper dans une VM pendant quelques temps, je lis la doc et me renseigne


### Installer et utiliser Gentoo Linux : Guide de démarrage pour les débutants
https://fr.linux-console.net/?p=10803

### Le guide en 20 étapes pour installer Gentoo
https://blog.desdelinux.net/fr/20-%C3%A9tapes-pour-installer-Gentoo/


### Gentoo Handbook AMD64
https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Introduction


### Gentoo with EFIStub, encrypted BTRFS, swap, dracut or genkernel initramfs, open-rc.
https://aj.immo/2021/11/gentoo-with-efistub-encrypted-btrfs/

### LXQT DE
https://wiki.gentoo.org/wiki/LXQt

### EFI Stub
https://wiki.gentoo.org/wiki/EFI_stub

### Configure Ly with Gentoo and openRC
https://www.youtube.com/watch?v=9nspf7yapGY