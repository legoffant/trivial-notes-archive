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
```
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
```
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

**INCONVENIENT**: Certaines Box Internet n'accepte que le DNS du FAI pour l'accès sur le réseau local.