Title:Devenir un hacker en 2022
Date: 2022-03-13 17:19
Category:Inclassable
Tags:guide, hacker
Authors: Anthony Le Goff
Summary:


Temps de lecture: 11min

Dans ce topic je vais éssayer de mettre en perspective la carrière de hacker dans mon programme de rendre accessible l'informatique aux plus jeune dans des zones défavorisés tel que la ruralité d'ou je suis d'origine, c'est surement la compétence de ce siècle qu'il faut apprendre à maitriser à travers la révolution de l'informatique. Le savoir nécessaire étant distribué sur internet à travers des ressources en libre accès, selon la culture des hackers et la libre circulation de l'information, chacun ont la possibilité d'acquérir des compétences dans le domaine à moindre coût.  

  

## Un mot sur le matériel  

Démarrer en sécurité informatique ne nécessite pas de dépenser des sommes importantes. Pour donner un ordre d'idée un ordinateur reconditionné à 400-600€ d'entrée de gamme suffit à la tâche. Préférez des ordinateurs robustes et qui ont fait leur preuve sur la compatibilité matériel sous GNU/Linux tel que Lenovo Thinkpad. Si vous avez de l'argent à dépenser pensez à la série Dell XPS.  

Préparer en avance une stratégie de sauvegarde de vos données, en éxecutant des tâches périodique que vous aller apprendre à plannifier sur votre ordinateur, dépensez dans un NAS Synology à 200€ est un maigre investissement face au risque de corruption des données. On n'est pas à l'abri d'un crash du système ou de la malveillance.  

Pour vous former à moindre coût utilisez Raspberry Pi et faite de la récup de matériel en montant votre propre serveur. Ce mini-ordinateur de la taille d'une carte de crédit permet de s'initier à l'informatique, la communauté et les ressources sont légion sur le web.  

Regarder du côté du matériel libre pour apprendre la programmation et l'électronique tels que sur Arduino ou encore ESP32.  

## Pour bien commencer  

### **Qu'es-ce que le hacking?**  

_"Le hacking consiste à identifier les vulnérabilités et failles dans un système et gagner un accès à des données"_  

Un hacker acquiert un accès non autorisé à des données sur sa cible alors que l'ethical hacking à la permission officielle d'opérer. Dans ce sens on essaye de prévenir une intrusion sur le système qui donnerait lieu à de l'espionnage, du vol de donnée pour la revente sur les marchés noirs ou la concurrence. A la base il y a une volonté de détourner l'utilisation initiale d'un système pour en tirer profit ou simple curiosité. Il n'y a pas de tabou que cela soit dans le but de faire de l'argent, et certains hackers sont millionnaire que cela soit acquérit légalement, je pense au business des failles 0-Days ou des Bug Bounty.  

### **Tous Gray Hat Hacker**  

A partir du moment que l'on suit le mouvement de la libre circulation de l'information, on transit régulièrement entre l'action légale et illégale, car l'information est protégée, sa rareté est source de valeur pour négocier sa diffusion et son partage. L'histoire nous à montré à travers certaine pénétration sur des réseaux sécurisés d'entreprise ou militaire que le secret source de pouvoir entre quelques individus se trouve un jour exposé, la question qui décidez vous à cet instant d'enrichir. Tout acte de hacking est une lutte de pouvoir, pour protéger et solidifier des acquis et business. Au delà du choix que l'on fait c'est interféré dans un projet qui a comme conséquence de redistribuer ou transférer une part de la richesse informationnelle et donc egalement financière.  

### **La communauté**  

Dans [une brêve histoire des hackers](https://www.larevuedesressources.org/une-breve-histoire-des-hackers-eric-steven-raymond,2329.html), on relate l'origine du mouvement et de la communauté principalement autour des systèmes UNIX. C'est pour le développement du système d'exploitation (OS) que fut créé le langage C par Dennis Ritchie en 1972, qui est un pape dans le milieu du hacking, une figure très respecté. Mais on trouve également l'origine plus ancienne autour du développement du langage LISP et les travaux en intelligence artificielle de John McCarcthy en 1958. Les puristes utilisent Emacs codé en LISP comme éditeur de texte face à Vi (et Vim) de l'héritage d'UNIX dans [une guerre sainte](https://blog.desdelinux.net/fr/vim-et-emacs-pas-de-nouvelles-sur-le-front/) interminable des logiciels libres. Des projets plus avancés tels que [Cyc](https://cyc.com/) ont une base en LISP. La communauté ce structure autour du symbole du "Planeur" ou "Glider" en anglais qui est une référence à un schéma mathématique du nom du "[jeu de la vie de Conway](https://korben.info/le-glider-dou-vient-ce-symbole-de-la-culture-hacker.html)" développé par ce mathématicien. Au delà de ça, c'est la reconnaissance des pionniers de l'informatique en particulier de John von Neumann sur ces travaux sur [les automates cellulaires](https://fr.wikichali.com/524906-self-replicating-machine-LGVDVQ). La communauté des hackers fonctionnent comme une machine auto-réplicante sociale dans le processus de diffusion du savoir pour la copie et amélioration des systèmes vers plus d'automatisation et d'autonomie après une phase d'apprentissage d'ou le déploiement massif du Machine Learning (ML) et la recherche sur les réseaux de neurones, le succès de l'imprimante 3D "RepRaps" est plus parlant. Ces fondements ont donné lieux aux libertés informatiques après le développement du projet GNU de Richard Stallman guru du [logiciel libre](https://www.gnu.org/philosophy/free-sw.fr.html) qui travaillait auparavant au laboratoire d'intelligence artificielle du MIT. Après la diffusion des UNIX propriétaires et les contraintes sur l'étude des systèmes dans des licences commerciales, les hackers dans une contre-culture ont décidé de ce réapproprier la machine en particulier l'ordinateur et son système d'exploitation avec des outils de développement, tel que des compilateurs comme GCC autorisé pour la redistribution sans contrainte et son amélioration permettant de créer des programmes dans une attitude progressiste et équitable. Le noyau Linux est devenu l'un des fondements de regroupement de la communauté à travers son idéologie de développement et ces outils. Mais également des niches plus radical tel que des UNIX libres comme FreeBSD ou encore les programmeurs ce regroupant sous la philosophie du langage Perl. D'autres communautés plus largement sur internet pour utilisateur averti et expérimenté adhèrent à Arch Linux et sa devise "KISS, Keep It simple stupid" ou encore à Gentoo qui sont des distributions Linux adapté sur mesure pour l'utilisateur jusqu'à l'ajout de fonctionnalité et outil de hacking tel que BlackArch ou Pentoo. Il y a une idéologie et courant de pensée au sein même des hackers et débats qui se réclame de la tradition au delà de branche plus radicale autrefois réservé à des barbus qui se diffusent de plus en plus en matière d'inclusivité. Ainsi la culture underground jusqu'au cipherpunk est fortement axé sur le développement de GNU/Linux. En France un noyau dur se regroupe autour de l'hacktivisme et "La Quadrature du Net" ainsi que Framasoft et ces outils. Des forums tels que [Hackademics](https://hackademics.fr/) sont plus ouvert sur l'ethical hacking voir les représentants de [Zenk Security](https://www.zenk-security.com/) actif dans la diffusion du savoir. Une branche de la communauté des hackers se réfère souvent egalement au crypto-anarchisme dans l'utilisation de la cryptographie pour protéger les communications et garantir les libertés d'échanges en particulier l'anonymat recherché par les hackers. Le [manifeste crypto-anarchiste](https://bitcoin.fr/the-crypto-anarchist-manifesto/) a depuis lors été édité par Timothy C. May. Il va s'en dire que des individus qui échappent à la surveillance de masse des états sont surveillés par la NSA qui qualifie les lecteurs de Linux Journal d'extremiste, de ne pas hésiter à [troller le FBI](https://www.youtube.com/watch?v=Nn3O8XD1z0w) tel que l'affirme le célèbre hacker Kevin Mitnick. La communauté du renseignement se nourrit des hackers et n'est pas à négliger dans les différentes parties prenantes qui parfois collaborent tel que la DGSI en France, ex DST et la célèbre [affaire du Chaos Computer Club France](https://fr.wikipedia.org/wiki/Chaos_Computer_Club_France). Les dérives actuels du "big business" de la cybersécurité voit apparaitre comme des champignons toutes sortent de groupe qui défendent d'être une autorité en hacking grâce à des formations diplomantes bullshits à travers des écoles privées hors de prix qui sont lié par des contrats commerciaux d'exclusivité bien loin de la tradition des hackers qui luttent contre ce système depuis les UNIX propriétaire et l'avenement des licences logiciels pour s'accaparer le pouvoir. On tombe dans l'amateurisme et la caricature de la profession. Si un hacker vous dit qu'il faut apprendre MATHLAB à des fins de calcul numérique, c'est qu'il vous prend pour un con. Face à cette génération de dégénérer l'éducation est primordiale pour laver des cerveaux malades du système commercial de l'ordre des marchands. La plupart des hackers sont autodidacte et les formations diplomantes reconnus sont en libre accès sur internet tels que [CS50 de Harvard](https://pll.harvard.edu/course/cs50-introduction-computer-science?delta=0) en informatique généraliste. D'autres manières d'appréhender le hacking et plus largement le milieu des pirates est de s'initier au [Serious Gaming](https://fr.wikipedia.org/wiki/Jeu_s%C3%A9rieux) tel que les carrières sur EVE Online dans un sandbox de communauté plus confidentielle dans l'apprentissage du vocabulaire jusqu'à experimenté des "War Room" dans des groupes et entreprises diverses. Ainsi des mots comme RECON, BlackOps, bounty, n'auront aucun secret pour vous, ni leur métaphore. Il faut acquérir beaucoup de connaissance avant de faire ces armes dans des opérations d'infiltration et espionnage pour des tests d'intrusion pour être reconnu par la communauté. En fonction de vos actions vous appartiendrez à différentes souverainetés et façonnerez votre idéologie.  

## Un état d'esprit  

Je ne vais pas reprendre ce qui a déjà été dit et largement validé dans le milieu par [les écrits de Eric S. Raymond](http://www.secuser.com/dossiers/devenir_hacker.htm) sur la mentalité des hackers, à retenir:  

*   Les hackers résolvent des problèmes, construisent des choses et croient à la liberté et à l'entraide volontaire.  
    
*   Le monde est plein de problèmes fascinants qui n'attendent que d'être résolus  
    
*   Personne ne devrait jamais avoir à résoudre le même problème deux fois.  
    
*   La routine et l'ennui sont inacceptables.  
    
*   Les autoritaristes se nourrissent de censure et de secrets. Et ils se méfient de l'entraide mutuelle et du partage d'informations. Ils n'apprécient la "coopération" que quand ils peuvent la contrôler. Donc, pour vous comporter comme un hacker, vous devez développer une hostilité instinctive vis-à-vis de la censure, du secret et de l'usage de la force ou de la ruse pour dominer des adultes responsables. Et vous devez vous tenir prêt à agir conformément à cette conviction.  
    

## Méthodologie d'une attaque  

Des méthodes ont été développé pour la maitrîse des tests d'intrusion (Pentesting) à travers le [PTES](http://www.pentest-standard.org/index.php/Main_Page) (The penetration testing execution standard) qui rassemble les bases pour imiter une attaque de hacker sur des machines. Je vais parler d'une autre méthologie plus intéressante à travers la chaine de cybercriminalité ([Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)) dans le cadre des APTs ([Advanced Persistent Threat](https://fr.wikipedia.org/wiki/Advanced_Persistent_Threat)) développé par Lockheed Martin. Cet industriel de l'armement au coeur du célèbre centre de R&D [Skunkworks](https://fr.wikipedia.org/wiki/Skunk_Works) fait de la recherche en cyberdéfense face aux menaces de ces secrets industriels qui attirent les cybercriminels. En France nos industriels de l'armement tel que Dassault font une politique de l'autruche ne jouant pas le jeux d'enrichir le modelisation des attaques et coopérer avec la communauté par retour d'expérience pour éviter que cela ne se reproduise, tel que le scandale du hacker ASTRA. Cela donne une image de branguignol surtout que l'on n'a jamais plus entendu parler de cet hacker devenu une légende renforçant son aura. Les APTs sont également développé en France tel que Animal Farm opéré par la DGSE et son logiciel malveillant BABAR. La chaîne de cybercriminalité permet de comprendre et de combattre les ransomwares, les failles de sécurité et les menaces persistantes avancées (APT). Depuis sa création, la « Cyber Kill Chain » a continué d'évoluer pour mieux prédire et identifier les menaces internes, l'ingénierie sociale, les ransomwares avancés et les attaques innovantes. Elle est constitué de [plusieurs phases](https://fr.linkedin.com/pulse/cyberattack-kill-chain-ou-la-chaine-de-destruction-ignace-yao):  

*   1\. Reconnaissance  
    
*   2\. Armement et choix du code malveillant  
    
*   3\. Livraison du "colis"  
    
*   4\. Exploitation et installation  
    
*   5\. Commande et contrôle  
    
*   6\. Mouvement Latéral & Pivotement  
    
*   7.Exécution de l'action prévue  
    

  

## Maitriser l'ingénierie sociale  

Souvent qualifiée de « hacking de l’esprit humain », l’ingénierie sociale est l’Art de la manipulation. Une attaque réussie permettra de pousser la victime à révéler des informations sensibles qui auraient été difficiles, voire impossibles, à recueillir par le biais d’une attaque purement technique. Plus vous persister dans une attaque, plus il y a un risque de pousser à l'erreur humaine faisant par effet de boule de neige adopter des comportements psychologiques comme effet de levier. Vous allez devenir dangereux par cette faculté et attirer l'attention en fonction de la sophistication de la maitrise de la compétence. Etudier quelques livres pour comprendre les mécanismes tels que:  

*   Influence et Manipulation de Cialdini  
    
*   Gouverner par le chaos, ingénierie sociale et mondialisation  
    

Ayez quelques bases également en séduction moderne(la french touch) à travers la PNL(programmation neuro-linguistique) pour obtenir ce que vous voulez de l'esprit humain à travers une communication assertive permettant de vaincre des résistances et exploiter des failles humaines. Le diable s'habille en Prada. Etudier le livre sur les origines de la PNL:  

*   Les secrets de la communication de R. Bandler et J. Grinder  
    

  

Vous ne regarderez plus jamais comme auparavent les politiques et les emails de SCAM pour venir en aide à une fille cancéreuse au Bénin en transférant de l'argent par Western Union en fonction de votre empathie. L'ingénierie sociale est intraitable et souvent fait tomber les masques des personnes, de leur relation aux autres ou pullule autres singe, renard, cloporte, parasite et prédateur.  

Ne vous arrêtez pas d'apprendre en étudiant le verbe et le langage en communication qui faciliteront votre apprentissage dans des domaines connexes de la psychologie et la linguistique pour l'étude de l'intelligence artificielle ou des compilateurs.  

## La programmation est l'épanouissement des hackers  

Savoir coder c'est commencer à comprendre un monde d'abstraction technologique qui est gouverné par l'informatique. Cela affûte l'esprit à la résolution de problème qui fait de vous une véritable valeur marchande. Vous allez comprendre comment fonctionne un ordinateur à travers des programmes qui sont des interfaces de communication entre humain et machine. Le code n'est qu'un outil et qui fait loi. Pour plus d'information plonger vous dans [la théorie des langages](https://www.lrde.epita.fr/~akim/thl/lecture-notes/theorie-des-langages-1.pdf) et apprenez l'apport de figure comme Alan Turing sur la discipline. La plupart des hackers le diront, il faut commencer par apprendre le langage C pour la programmation système. La plupart des langages modernes sont des dérivés du C. Il permet de gérer la mémoire manuellement et optimiser les ressources processeurs. Par la suite apprenez un langage de scripting tel que Python. Vous allez avoir de bonnes bases en programmation en suivant ces deux livres en libre accès:  

*   [Le C en 20 heures, Eric Berthomier](https://framabook.org/docs/c20h/C20H_integrale_creative-commons-by-sa.pdf)  
    
*   [Apprendre à programmer avec Python 3, Gerard Swinnen](https://inforef.be/swi/download/apprendre_python3_5.pdf)  
    

Le monde informatique n'est rien sans les algorithmes et les structures des données. C'est un sujet plus difficile à aborder mais nécessaire, commencer doucement à travers ce livre de Zeste Du Savoir:  

*   [Algorithmique pour l'apprenti programmeur](https://zestedesavoir.com/tutoriels/621/algorithmique-pour-lapprenti-programmeur/)  
    

Il faut savoir qu'il vous faudra au moins 300 heures de programmation pour commencer à maitriser des bases solides. C'est un marathon que l'apprentissage de la programmation, ne vous cramer pas les ailes, vous allez apprendre de vos erreurs, parfois abandonner. Lancer vous dans des projets, construiser des petits programmes, apprenez en faisant des jeux tel que Pong, Snake ou Space Invader c'est formateur et ludique. [Contribuer à des projets open source](https://opensource.guide/fr/) en apprenant le social coding avec des outils comme Git. Vous n'allez pas écrire du jours au lendemain vos propres outils de hacking ou faire de la recherche en vulnérabilité sur un logiciel, cela prend du temps, cela demande des sacrifices, des nuits blanches à ce documenter et lire des manuels.  

MEMO: Liste des langages à apprendre  

1.  Bash/Shell  
    
2.  Python
3.  C / C++
4.  LISP
5.  Perl  
    
6.  Java  
    

## Topics annexes  

Il vous faudra egalement explorer d'autres sujet en lien avec le hacking tel que:  

*   Internet et les réseaux  
    
*   Cryptographie  
    
*   Analyse de malware  
    
*   La retro-ingénierie  
    
*   Langage et compilateur  
    
*   Sciences des données et calcul numérique  
    

  

## Hacker 101 - Configuration initiale  

*   Trouver du matériel dédié  
    
*   Choisir un système d'exploitation ( Arch Linux) et lire [le manuel](https://wiki.archlinux.fr/) customiser l'installation pour chiffrer vos partitions avec dm-crypt/LUKS  
    
*   Installe gratuitement un VPN (sous GNOME) avec protonVPN et télécharger Tor  
    
*   Naviguer en sécurité sur internet avec [LibreWolf](https://librewolf.net/)  
    
*   Explorer les solutions de [GoFOSS](https://gofoss.net/fr/)  
    
*   Changer pour un service mail anonyme chiffré avec protonmail.  
    
*   Accéder au [darknet](https://darknet-tor.com/acceder-darknet-tor.php) et explorer le web profond à travers [les liens .onion](https://haxf4rall.com/2017/11/12/deep-web-onion-links/)  
    
*   Rejoignez des [forums](https://haxf4rall.com/2019/04/30/top-10-hacker-forums-on-darknet-and-clearnet/) ou serveur Discord sur le hacking, tel que hackacademics  
    
*   Intéragisser sur twitter pour construire un réseau d'apprentissage #infosec  
    
*   Regarder des [films et séries](https://www.cinetrafic.fr/top/serie/hacker) sur les hackers  
    
*   Lisez l'origine du mot cyberespace dans Neuromancien de W.Gibson qui inspira Matrix.  
    
*   Installer le repository BlackArch pour acceder aux outils de hacking, [un listing](https://haxf4rall.com/2019/05/03/hacking-tools-list/)  
    
*   Apprenez à cloner des dépôts sur Github et récupérer [des ressources, livres, programmes](https://github.com/legoffant/learnprogramming)  
    
*   Chercher [des tutorials sur le hacking](https://www.youtube.com/results?search_query=hacking+tutorial) avec youtube  
    
*   Customizer votre terminal avec [Oh-My-Zsh](https://ohmyz.sh/) et système d'exploitation, partager votre configuration unique sur redddit/UNIX Porn et Deviant Art.  
    
*   Passer en mode [terminal](http://linuxcommand.org/) le plus souvent possible  
    
*   Construisez votre propre [virtual lab](https://www.hackingloops.com/kvm-virt-manager/) avec KVM en faisant de la virtualisation  
    
*   Ecrivez vos propres exploit et utiliser [exploit-db](https://www.exploit-db.com/) ainsi que [shodan](https://www.shodan.io/)  
    
*   Maitriser Metasploit  
    
*   Participer à des [CTF(capture the flag)](https://trailofbits.github.io/ctf/)  
    
*   Explorer [Root Me](https://www.root-me.org/) la plateforme d'apprentissage dédié au hacking en français  
    
*   Apprenez l'anglais car la documentation en informatique n'est pas souvent traduite.  
    

## Un mot sur les certifications  

Vous pouvez valider des certificats sur vos connaissances à travers le LPIC et le CEH qui sont reconnu en France, rappelez-vous que les diplomes c'est du verni dans le milieu des hackers. Les certifications permettent d'ouvrir des portes en montrant que vous maitriser le sujet et que vous êtes compétents. Mais noté que Les anglophones sont très porté sur les certifications si vous décidez de bouger à l'internationnal. Le principe de rétribution est basé sur la réputation, car la construction de la confiance en entreprise construit les contrats des clients qui peuvent exposer des vulnérabilités des données. Si le contrat n'est pas respecté, manque de respect, on escalade en conflit quand les parties sont dans un rapport de force plus qu'à co-construire et s'enrichir mutuellement. Mais si vous voulez faire carrière dans la cybersécurité une expérience d'administrateur système est avantageuse et plus gratifiant que les certifications.  

## Encore plus de bouquins  

Quelques-un des meilleurs livres pour débuter le hacking de la littérature anglaise, vous les trouverez en accès libre sur mon repository [Github:legoffant](https://github.com/legoffant/learnprogramming/tree/master/Cybersecurity).  

*   Hacking - The art of exploitation, Erickson  
    
*   Penetration Testing A Hands On Introduction To Hacking, Weidman  
    
*   The Hacker playbook series (1 - 3)  
    
*   RTFM: Red field team manual  
    
*   Linux for hackers, Occupytheweb  
    

  

  

 BIBLIO:
 

[https://haxf4rall.com/become-a-hacker/](https://haxf4rall.com/become-a-hacker/)  

[https://codescracker.com/computer-tricks/how-to-become-a-hacker.htm](https://codescracker.com/computer-tricks/how-to-become-a-hacker.htm)  

[http://vadeker.net/articles/hacker-howto.html](http://vadeker.net/articles/hacker-howto.html)
