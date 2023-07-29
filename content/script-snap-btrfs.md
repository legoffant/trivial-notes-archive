Title:Automatiser les snasphots btrfs avec un script shell et cron
Date: 2023-07-29 06:57
Category:Linux
Tags:programmation, informatique
Authors: Anthony Le Goff
Summary:

Les sysAdmins automatisent toutes les tâches pour la maintenance des serveurs et ordinateurs. Généralement il faut savoir faire du scripting avec des paramêtres systèmes. Donc on code en [Bash qui est scripting shell](https://linux.goffinet.org/administration/scripts-shell/) voir en Python grâce au [module os](https://pythonforge.com/module-os-systeme-dexploitation/). Les plus anciens et puristes utilisent Perl. Il existe parfois des programmes avec une interface graphique comme Timeshift. Mais malheureusement pour moi, celui-ci ne détecte pas mes partitions en btrfs surement car j'utilise une surcouche de volume logique LVM dans mon schéma de partitionnement disque.

[btrfs](https://fr.wikipedia.org/wiki/Btrfs) c'est quoi? C'est un système de fichier. Sous Linux on utilise ext4 et Windows utilise ntfs. btrfs est la nouvelle génération avec la particularité de pouvoir faire des snaphots, c'est à dire des instantanés du système pour la sauvegarde, mais égalemement la somme de contrôle ou la compréssion des données en zstd. Mais il existe également ZFS en particularité sur les serveurs et NAS.

**On va donc automatiser nos sauvegardes de DATA tous les jours en utilisant un script shell et un plannificateur de tâche cron en cas de plantage du système.**

### On commence par vérifier nos subvolumes btrfs
```bash
$ sudo btrfs subvolume list /

ID 256 gen 7527 top level 5 path @
ID 257 gen 7528 top level 5 path @home
ID 258 gen 9 top level 5 path @_snapshot
ID 259 gen 17 top level 256 path var/lib/portables
ID 260 gen 18 top level 256 path var/lib/machines
```

### On va créer notre dossier de scripts utilisateurs et le script bash
```bash
$ mkdir ~/scripts
$ mkdir ~/scripts/logs
$ touch ~/scripts/logs/snap-logs

$ nvim btrfs-snapshot-backup.sh

#! /usr/bin/bash

# Dossier pour sauvegarder snapshot
SNAPDIR=/@_snapshot
export SNAPDIR

# Supprimer toutes les snapshots présentent sur le disque
sudo btrfs subvolume delete $SNAPDIR/home_*

# Prendre une snapshot
sudo btrfs subvolume snapshot -r /@home $SNAPDIR/home_$(date +%Y%m%d)

# Check si la snapshot a bien été créer, sinon exit et report
if [ $? -ne 0 ]
then
echo "Erreur pour créer la snapshot home_$(date +%Y%m%d)" >> ~/scripts/logs/snap-logs
exit 1
fi
```

### Rendre executable le script bash
```bash
$ chmod u+x ~/scripts/btrfs-snapshot-backup.sh
```
### On utilise un plannificateur de tâche "Cron" pour lancer le script tous les jours à 11:22
```bash
$ sudo crontab -e
$ sudo nvim /etc/crontab

22 11 * * * trivial /home/trivial/scripts/btrfs-snapshot-backup.sh
```

### Ajoute les droits admins sur les scripts dans sudoers
```bash
$ sudo EDITOR=nvim visudo

trivial ALL=(ALL) NOPASSWD:	 /home/trivial/scripts/*
```

### activation du service daemon au démarrage du système
```
$ sudo systemctl enable crond.service
$ sudo systemctl reload crond.service
```

NOTA: améliorer le script, on peut définir une sauvegarde des snaphots et supprimer les plus anciennes de plus d'une semaine.