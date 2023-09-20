Title:Outils de cyberdefense et "blue team"
Date: 2023-09-20 21:51
Category:Inclassable
Tags:cyber, hacking
Authors: Anthony Le Goff
Summary:

Comme je le rappel je suis spécialisé en cyberdéfense dans le hacking. Qu'es-ce que l'on entend par ce défendre des hackers? Il y a plusieurs "team" de hackers:

* Red Team = offensif
* Purple Team = en soutiens du processus (supervision)
* Blue Team = défensif

En l'occurence je joue le rôle de la "blue team" que l'on retrouve au sein des entreprises dans le centre d'opérations de sécurité (SOC). Les méthodes sont les suivantes:

* L'examen et l'analyse des données des logs.
* L'utilisation d'une plateforme de gestion des informations et des événements de sécurité (SIEM) pour la visibilité et la détection des intrusions en direct et pour le triage des alarmes en temps réel.
* Collecter de nouvelles informations sur les menaces et hiérarchisation des actions appropriées en fonction des risques.
* Analyser le trafic et les flux de données.
* Des analyses de vulnérabilité du réseau.
* Audits de DNS.

La "Blue Team" est là pour établir une stratégie et mesure de sécurité autour des actifs clés de l'organisation. La "Blue Team" doit se tenir au courant des nouvelles technologies permettant d’améliorer la sécurité et donc faire une veille sur internet. Egalement c'est un plus pour mieux ce défendre, être capable de prévenir l'attaque et de les simuler. 

Quelques outils essentiels de la "Blue Team"

Fondamentale en réseau, il faut connaitre:

* **ping** pour savoir si un paquet transit vers un site
* **ip** pour manager les outils du réseau
* **traceroute** qui détermine le chemin emprunté par un paquet pour aller de la machine locale à un réseau IP
* **nslookup** Associe adresse IP et DNS. Il permet d'interroger les serveurs DNS pour obtenir des informations
* **netstat** Affiche les informations réseaux, table de routage et des stats.
* **ssh** permet de ce connecter à distance sur un serveur.

### Nmap

Commençons par un outil essentiel pour auditer le réseau et avoir une carte de celui-ci à travers Nmap. Vous pouvez ainsi scanner tous votre réseau local via la commande:
```bash
$ nmap -sS 192.168.1.0/24
```

### OpenVAS

C'est un scanner de vulnérabilité open source, fork de Nessus.

Le résultat du scan fournira :

* la liste des vulnérabilités par niveaux de criticité,
* une description des vulnérabilités,
* et surtout la méthode ou un lien pour corriger le problème

### Monitoring avec OSSEC

OSSEC est un HIDS "host based intrusion detection system". Il a pour objectif de détecter un comportement anormal sur une machine. Il collecte les informations qui lui sont envoyées par les équipements, il utilise les signatures ou le comportement pour détecter une anomalie. Un agent est installé sur chacune des machines.

### Détection wifi avec Kismet

Kismet est un détecteur wifi, mais également sniffer et IDS.

### Wireshark analyse de paquet

Il est utilisé dans le dépannage et l'analyse de réseaux informatiques, le développement de protocoles, l'éducation et la rétro-ingénierie.

### Logs avec syslog-ng

Pour gérer les logs, on utilise un outil basé sur le web en auto-héberger qui peut faire office de SIEM via [Graylog](https://graylog.org/). C'est une solution open source qui implémente syslog.

### Par-feu

Les par-feux les plus utilisés sont ufw, iptables et pfsense, chacun à ces particularités et parfois sont difficile à aborder et les règles complexes. 

### Honeypot avec T-Pot

Le honeypot le plus complet du marché, adresse: [https://github.security.telekom.com/](https://github.security.telekom.com/) développé par Deutsche Telekom AG.

### Analyse de malware avec Yara

Apparu en 2007, YARA est un framework qui a été mis au jour par Victor Manuel Alvarez pour identifier un malware et le classer dans un groupe de famille partageant les mêmes caractéristiques.