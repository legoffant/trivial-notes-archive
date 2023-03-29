Title:Parlons du protocole internet Gemini
Date: 2023-03-29 01:58
Category:Inclassable
Tags:Gemini
Authors: Anthony Le Goff
Summary:

Il y a des initiatives de créer un nouveau protocole internet pour remplacer http car le web est devenu lourdingue, on a créé tout un tas de service à travers des couches applicatives qui ont complexifié les websites et donc créé des failles de sécurité et des problèmes de chargement des pages.  

J'y avais moi même pensée comme solution technique de ce blog en passant par un générateur de site statique via Pelican par sécurité pour être à l'abri des attaques informatiques et faire l'économie d'une base de donnée. La question est donc faut t-il un retour au minimalisme pour sécuriser internet? Less is More. On doit retourner à l'essentiel passer par le terminal tel que des modes dégradés dans la sureté des systèmes d'information. On peut même imaginer lire des pages internet et les modifier en temps réel avec Vim ou Emacs réduisant le workflow entre client et serveur tel que [Elpher](https://github.com/emacsmirror/elpher).  

En réalité l'internet de demain n'aura rien à voir avec l'usine à gaz que l'on connait, les services seront isolé dans des protocoles en fonction des tâches. Nous allons vers la containerisation d'internet. Il est clair que face à la cyberguerre, nous devons trouver des solutions pour rendre sur l'échange d'information, la liberté d'expression et la mise en place de service pour la plupart vers une décentralisation de la finance mais également des outils de production et des bases de données pour éviter les monopoles. Car les hackers ciblent l'accès à ces services pour saboter ou accéder à de l'information protégée pour en tirer un profit, les secrets sa rapporte du fric. Réduire la surface d'attaque est le futur créneau des experts en cyberdéfense: et il y a qu'un seul moyen en passant par le minimalisme du code source ouvert sur les outils des systèmes d'information et l'isolation des services en rendant obscure par le chiffrement les communication. Le minimalisme est de chercher la solution technique la plus réductible qui soit, c'est à dire que l'on fait de l'économie sur une fonction. Ce qui devrait être la mentalité recherché à tout ingénieur.  

Parlons donc du protocole Gemini sorti en 2019 début de réponse comme riposte. Il est dans la continuité de Gopher qui est obsolète. Inventé par Solderpunk, avec le soutien notable de Drew DeVault, illustre hacker minimaliste connu pour [le gestionnaire de fenêtres Sway](https://swaywm.org/) sous GNU/Linux pour Wayland. Le protocole n'est pas extensible pour éviter l'utilisation d'outil de pistage. Le but est de consulter des pages internet. L'HTML a été abandonné, il n'y a pas de CSS et encore moins de Javascript remplacé par du Markdown épuré du Gemtext. J'ai toujours trouvé que les développeurs front-end étaient des idiots proche de l'autisme pour rendre intéractif un website, en chipotant sur des détails à la con comme la couleur et l'effet sur un bouton... augmentant l'utilisation de ressource. Mais c'est un autre débat sur les interfaces et l'UX Design.

Les utilisateurs se sont plaind que l'on ne peut pas échanger des fichiers ou des messages. Le créateur ce défend en utilisant d'autres protocoles pour cela comme Git ou Rsync. Ce n'est pas un protocole pour publier. On peut noter également que des fonctions comme LaTeX ou la cotation de ligne de code ne soit pas possible rendant limité la création de document technique et scientifique.  

Alors qui utilise Gemini?  

L'intérêt est de diffuser du contenu, on retrouve des philosophes, des poètes, des hacktivistes qui partage des idées voir des écrivains amateurs. Le Gemtext reste un protocole basé sur l'hyperlien pour naviguer dans les pages. On peut s'étonner que les crypto-terroristes n'ont pas encore investi le protocole pour revendiquer et diffuser leur doctrine et que cela reste un débat d'idée. Un site Gemini s'appelle "une capsule" et en 2022 il existe 2200 capsules, soit un taux d'adoption en 3 ans intéressant par des "early adopter" technophile. Cela fait penser à un club d'Ham Radio version internet.  

Il faut quelques connaissances en administration de système pour créer une capsule Gemini qui n'est pas à la portée de tous et faire souvent de l'auto-hébergement sur serveur car il y a peu de service d'hébergement, plutôt bancale ou l'on ne sait pas si votre capsule sera toujours en ligne le lendemain. L'hébergeur [un bon café](https://gemini.yesterweb.org/proxy/unbon.cafe/) francophone est une solution. Un protocole internet est évaluable sur sa persistance de la distribution de l'information et sa capacité à la relier et donc sa facilité à héberger dans le temps du contenu. Cela simplifie également le traitement de l'information pour des utilisations en intelligence artificielle et Data Mining, plus le langage est complexe plus il y a un risque d'erreur de bruit parasite et vous devez appliquer des filtres pour extraire de l'information de pattern comme le Regex. L'intérêt est que vos écrits perdurent dans le temps tout en étant indexable. Quand j'ai choisi comme hébergeur Github Pages pour ce blog je savais que le service offrait de la persistance, que même si je mourrais mes écrits vont rester. Si vous perdez votre site car vous payez plus le nom de domaine ou l'hébergeur c'est du gachis que doit résoudre internet et les archivistes.  

L'idée d'un protocole simple, plus sûre et respectueux de la vie privée a du sens, même si Gemini adopte une posture extreme, imaginé un internet sans cookies, pistages et publicités ou le protocole est en natif chiffré et les capsules avec un certificat auto-signé est loin d'être une mauvaise idée. Sa simplicité permet d'utiliser des clients légers pour la navigation et réduire la consommation de ressource.  

Pour accéder à Gemini on passe par des clients (dans un terminal CLI) tel que [Amfora](https://github.com/makew0rld/amfora) que vous pouvez installer sur Arch Linux:  

```
pacman -S amfora  
```

On peut noter des services d'aggregation de contenu ou l'on peut s'abonner à des "FEEDS" tel que CAPCOM car Gemini reste essentiellement un outil de blogging et que l'on peut retrouver des "directory" pour la curation de contenu tel que medusae.space catégorisé par topic.  

Ressources:  

*   Bortzmeyer figure de la culture libriste travaillant à l'AFNIC avait écrit un billet de blog sur le protocole: [https://www.bortzmeyer.org/gemini.html](https://www.bortzmeyer.org/gemini.html)  
    
*   Gemini Quickstart [https://geminiquickst.art/](https://geminiquickst.art/)  
    
*   (Github) Awesome Gemini [https://github.com/kr1sp1n/awesome-gemini](https://github.com/kr1sp1n/awesome-gemini)