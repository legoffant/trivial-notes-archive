Title:Ce lancer dans le minage de crypto Monero
Date: 2023-11-29 08:37
Category:Inclassable
Tags:crypto
Authors: Anthony Le Goff
Summary:

Monero fait parti des meilleurs cryptomonnaie à miner car elle est résistante au minage ASIC. Nous allons donc voir comment mettre en place un serveur de minage de cette cryptomonnaie. Sachez qu'il est difficile de faire du profit, il faut des fermes de serveur informatique et investir au moins 10 000 à 20 000 euros avec les meilleurs cartes GPU du marché pour avoir les meilleurs taux de hashage. 

Je vais déployer une machine virtuelle sur Proxmox conçu pour le minage. Sa capacité n'est pas conséquente avec 4 cores de processeur dédié j'atteinds 396 H/s. Ce qui utilise mon processeur un AMD ryzen 5600G à 33% de sa charge.

Pour obtenir des stats sur le Pool de minage que nous allons rejoindre, veuillez vous référez à l'adresse: [https://moneroocean.stream/](https://moneroocean.stream/) et désactiver les adblockers ou anti-scripts. Vous pourrez voir des stats sur votre addresse Monero. Il faudra penser à changer le XMR Threshold à 0,003 dans le setting de votre adresse Monero.

Nous allons utiliser le logiciel [xmrig](https://xmrig.com/) pour miner en CLI développé en C++ sur une machine en Ubuntu Server 22.04. 

### I. Récupérer un wallet et des adresses Monero

Nous allons utiliser le [wallet Feather](https://featherwallet.org/) qui est sur les distributions Linux comme Arch dans les dépots. Vous pouvez le configurer en lançant la commande:
```bash
$ yay -S monero-feather-git
```

Il va installer le réseau Tor dont il a besoin pour utiliser et se synchroniser. Si le Wallet à des problèmes pour synchroniser et à un status "déconnecté", il peut y avoir un problème de permission dans le fichier de configuration de `Tor`. Lançer en manuel alors:
```bash
$ sudo tor
```

Vous trouverez vos adresses Monero dans l'onglet "Receive" que l'on va copier pour la configuration de xmrig.

### II. Installation de xmrig

Pour commencer nous allons utiliser la dernière version LTS d'Ubuntu Server 22.04. Une fois installer dans une machine virtuelle, nous lançons les commandes de mise à jour et d'installation des dépendances ainsi que xmrig.
```bash
$ sudo apt update && sudo apt upgrade
```

On reboot le serveur
```bash
$ sudo reboot now
```

On lance l'installation des dépendances
```bash
$ sudo apt-get install git build-essential cmake automake libtool autoconf
```

On git clone le repo de xmrig dans home de l'user, dans mon cas "Trivial" `~`
```bash
$ git clone https://github.com/xmrig/xmrig.git
```

On créé un dossier `build` et navigue dans les scripts
```bash
$ mkdir xmrig/build && cd xmrig/scripts
```

On lance l'installation des scripts et navigue dans le dossier build après
```bash
$ ./build_deps.sh && cd ../build
```

Installation de xmrig en lançant make
```bash
$ cmake .. -DXMRIG_DEPS=scripts/deps
$ make -j$(nproc)
```

### Fichier de configuration

Vous pouvez créer un fichier de configuration avec le wizard à cette addresse: [https://xmrig.com/wizard](https://xmrig.com/wizard). Puis copiez-collez dans un fichier `config.json` dans le dossier build.

Mon propre fichier de configuration:
```json
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "gulf.moneroocean.stream:10128",
            "user": "monero wallet",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}
```

Dans ce fichier on configure le Pool, l'utilisation du CPU/GPU, l'addresse du wallet, TLS etc... Pour le password "x" signifie sans mot de passe.

### Lancer le programme

Pour lancer le programme, toujours dans le dossier build par la commande:
```bash
$ ./xmrig
```

Nous allons configurer automatiquement le démarrage au boot de la machine virtuelle et en background avec un script bash

Script `startup-xmrig.sh`
```bash
#!/usr/bin/bash

set -m
nohup /trivial/xmrig/build/./xmrig &
```

On le rend executable
```bash
$ sudo chmod +x startup-xmrig.sh
```

Configuration d'une tache cron
```bash
$ crontab -e

@reboot bash /trivial/startup-xmrig.sh
```



