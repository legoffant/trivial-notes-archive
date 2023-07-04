Title:Le monde ultra fermé de l'élite des hackers: Le Reverse Engineering sous Linux
Date: 2023-07-04 21:25
Category:Linux
Tags:reverse engineering
Authors: Anthony Le Goff
Summary:

Très loin des scripts kiddies, totalement à l'opposer des outils qui suffit de maîtriser en quelques clics, le monde très obscure du Reverse Engineering de binaire. Avec les célèbres "[Obfuscation](https://code-garage.fr/blog/quest-ce-que-lobfuscation-de-code-et-a-quoi-ca-sert/)" dans le langage C. Bienvenue chez les fous et paranos de la sécurité informatique.  

Pour ce lancer dans le reverse engineering il faut des connaissances en langage C/C++ et en assembleur x86-64. Connaître des principes sur la construction de binaire et les compilateurs. Le principe est de faire de l'analyse lexicale, pré-traitement ( préprocesseur ), de l'analyse sémantique et syntaxique au plus proche du langage machine sachant que les ordinateurs utilisent pour le calcul la base hexadécimale.  

Les retro-ingénieurs sont utilisés dans tous domaine ou l'on a pas les plans de conception d'un produit tel qu'en mécanique et l'espionnage industriel ou sur le code source des programmes propriétaires. On appel souvent des crackers. C'est également le domaine de l'analyse de malware(Virus, Trojans, Botnet....) par rétro-conception pour apprendre à les créer, les améliorer ou s'en prévenir. Un domaine émergeant est la génétique sur l'ADN et les algorithmes. C'est de la retro-conception que de retrouver des fonctions de l'ADN ou de la mémoire des ancêtres enregistrée sur le support de stockage de l'information.  

Généralement les vulnérabilités 0-Days sont reportés par des retro-ingénieurs, ou des Kernel Hackers sous Linux. Tel que l'entreprise qui avait fait un peu de bruit à une époque sur l'espionnage et la vente de faille à la NSA: [Vupen](https://fr.wikipedia.org/wiki/Vupen)  

Les failles 0-Days peuvent ce négocier à des millions de dollars pour leur report et exploitation (ie: [The rise of millionaire zero-day exploit markets](https://securityaffairs.com/124690/cyber-crime/zero-day-exploit-markets.html))  

Par malchance, ce monde de l'élite des hackers est encore plus ultra-fermé en France car il n'y a pas de ressource d'apprentissage disponible en français. Vous ne trouverez aucune littérature francophone et éditeur avec des experts sur le sujet, et rare sont les formations académiques faisant une introduction dans leurs cours. C'est un monde d'autodidacte anglophone.  

Clairement, ce lancer dans la retro-ingénierie sous Linux, vous allez manger du ELF.  

J'ai sélectionner les meilleurs livres sur le sujet pour apprendre en autodidacte sur mon repo Git en PDF.  

Cela inclus:  

*   Practical reverse engineering, x86, x64, ARM, Windows Kernel, Reversing Tools, and Obfuscation  
    
*   Reversing: Secrets of Reverse Engineering  
    
*   Mastering Reverse Engineering  
    
*   Compilers: Principles, Techniques, and Tools (dragon book)  
    
*   The Linux programming interface  
    
*   Practical Malware Analysis, The Hands-On Guide to Dissecting Malicious Software  
    
*   The Shellcoder's Handbook: Discovering and Exploiting Security Holes  
    
*   Practical Binary Analysis, Build Your Own Linux Tools for Binary Instrumentation, Analysis, and Disassembly  
    
*   Hacking: The Art of Exploitation, 2nd Edition  
    
```
$ git clone https://github.com/legoffant/reverseengineering.git  
```

Je recommande par lire "Hacking: The Art of Exploitation" c'est une bonne introduction.