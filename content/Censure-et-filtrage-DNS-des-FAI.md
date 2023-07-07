Title:Censure et filtrage DNS des FAI
Date: 2023-07-07 00:12
Category:Linux
Tags:dns
Authors: Anthony Le Goff
Summary:

La censure d'internet, un vaste programme. Nos politiques n'arrêtent pas de peter des cables, entre les sites de terrorisme, de pédopornographie, d'activiste et de librairie pirate interdite en open access (Sci-Hub) : toujours la même méthode, le filtrage DNS des FAI. Car techniquement c'est très compliquer de censurer internet, pour le pecnot moyen changer ces DNS est déja trop complexe.  

La dernière lubie des politiques est de censurer la pornographie en France en fixant une moyenne d'âge et de ficher la population qui regarde du porno. Et puis avec les émeutes ont veut couper les réseaux sociaux. Bah voyons.  

Il y a plusieurs méthodes pour contourner la censure d'internet:  

*   Proxy  
*   Changement de DNS (FAI)  
*   VPN    
*   TOR  
    

Donc ici j'explique la manière simple de changer les DNS en plus que votre traffic internet sera accélérer de + 28% en utilisant Cloudflare.  

```text
1.0.0.1 is about 10 times faster than 1.1.1.1 - 3 vs. 40 ms  
```

Cloudflare chiffre ces données transitant sur ces DNS. support DNS-over-HTTPS, DNS-over-TLS, DNSSEC, and DoS attack protection. Cloudflare logs l'adresse IP 25h sur ces serveurs.  

### Comment procéder  

Procédure pour changer ces DNS sous GNU/Linux (Arch) est d'éditer le fichier `/etc/resolv.conf`.  
```text
$ sudo nano /etc/resolv.conf  

nameserver 1.0.0.1  
nameserver 1.1.1.1  
```

Pour rendre permanent et éviter qu'un programme ré-écrit la configuration (Network Manager)  
```
$ sudo chattr +i /etc/resolv.conf  
```

Il faut redémarrer le PC pour prendre en compte la configuration ou redémarrer le service réseau avec `systemctl` (si vous utilisez `NetworkManager.service`).  

Pour vérifier les changements installer l'outil `dig`  
```text
$ sudo pacman -S dnsutils  

$ dig https://google.fr  

; <<>> DiG 9.18.15 <<>> https://www.google.fr  
;; global options: +cmd  
;; Got answer:  
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 57157  
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:  
; EDNS: version: 0, flags:; udp: 1232  
;; QUESTION SECTION:  
;https://www.google.fr.        IN    A

;; AUTHORITY SECTION:  
google.fr.        60    IN    SOA    ns1.google.com. dns-admin.google.com. 545619271 900 900 1800 60

;; Query time: 26 msec  
;; SERVER: 1.0.0.1#53(1.0.0.1) (UDP)  
;; WHEN: Thu Jul 06 23:47:21 CEST 2023  
;; MSG SIZE  rcvd: 110
```

L'indicateur `SERVER` présente le DNS 1.0.0.1 comme passerelle.

**INCONVENIENT**: Certaines Box Internet n'accepte que le DNS du FAI pour l'accès sur le réseau local. Ce qui complique la configuration du réseau local et son accès (box, serveur, imprimante).

**SOLUTION** Utiliser la fonction [protection par DNS via HTTPS](Configurer les niveaux de la protection par DNS via HTTPS dans Firefox) en utilisant Cloudflare dans le navigateur tel que Firefox au lieu d'éditer `/etc/resolv.conf` pour aller sur internet, et donc permet de garder l'accès au réseau local.

Vous pouvez vérifier que vous utilisez les DNS de Cloudflare sur le site [https://www.dnsleaktest.com](https://www.dnsleaktest.com)

Si vous voulez gérer au mieux le DNS en local il faut ajouter un routeur comme AP derrière la Box internet qui va paramêtrer le DNS. Cela fonctionne généralement en mode DMZ (Zone démilitarisée).

### Adresse IP

L'outil `dig` permet également de récupérer votre IPv4 public en particulier si vous êtes derrière un VPN.

```text
$ dig +short txt ch whoami.cloudflare @1.0.0.1
"176.180.233.XXX"
```
