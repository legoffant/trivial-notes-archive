Title:﻿De l'informatique embarquée avec Arduino  
Date: 2022-04-01 15:29
Category:C/C++
Tags: Arduino, programmation, langage C
Authors: Anthony Le Goff
Summary:

﻿

C'est le premier article que je fais véritablement sur Arduino. Et je me devais d'en parler pour son apport dans l'éducation à l'électronique aux détournements par des hackers aux ingénieurs. Arduino est un outil qui transforme notre regard sur la technologie et l'usage que nous en faisons.

C'est une excellente plate-forme qui réduit les coûts d'entrée en électronique et programmation, il permet à des personnes qui n'ont pas trop la fibre scolaire de ce plonger dans des domaines qui les intéressent. 

Arduino UNO, la carte de prototypage électronique standard de la gamme est sortie en 2010. Ce qui a permis une petite révolution dans le milieu de l'ingénierie par son introduction pour de l'informatique embarquée mais également en robotique. Son rapport qualité/coût pour prototyper vite en fond un outil qui dépasse le cadre seul de l'éducation. Il fait parti de la mode DIY (Do it Yourself) introduite par des composants tel que la RepRap, une imprimante 3D, né en 2005 qui deviendra l'emblème des hackerspaces. Les « **hackerspaces** » sont des lieux de rencontre et d'expérimentation collective qui rassemblent des personnes qui partagent un intérêt commun (notamment pour l'informatique, la technologie, les sciences et la créativité). qui débute le plus souvent dans un garage on retrouve le trio matériel RepRap, Arduino, Raspeberry Pi. En Bretagne il existe sur Rennes un hackerspace [Breizh-Entropy](https://breizh-entropy.org/) . Le plus connu est C-Base à Berlin. On appel des makers les utilisateurs des hackerspaces et fablabs. Des lieux qui donnent accès à des outils de prototypage rapide et fabrication numérique pour l'invention, [la charte](http://fab.cba.mit.edu/about/charter/) a été édité en 2012 au MIT. Arduino faisant donc parti des composants de prototypage électronique. Alors on va me dire, mais Anthony en 2010 j'étais en école d'ingénieur specialisé dans le prototypage rapide industriel,  la pointe en France dans le domaine, as tu entendu parler de tout ça? NON J'ai découvert plus tard par la communauté des hackers et libristes. Mon directeur d'école snobait l'impression 3D et son éco-système en considérant que cela n'avait pas d'avenir dans l'industrie, en gros bon pour les amateurs(SIC) gros plantage dans la vision d'avenir. Il faut dire qu'il etait très porté sur les brevets et la propriété intellectuelle de ces propres solutions de prototypage rapide qui expiraient et tombaient dans le domaine public.

Arduino introduit la notion de matériel libre (OSHW – _OpenSource Hardware_) par l'utilisation de la license GNU GPL. C'est à dire que les plans de la carte électronique sont ouvert. On peut donc redistribuer les plans pour fabriquer soit même une carte électronique. C'est une extension du logiciel libre au matériel.

Dans ce sens il existe des cartes dérivées d'Arduino UNO sur le marché. Parlons donc affaires, théma la taille du rat, que je suis et tout ça cela coût combien? On peut s'en sortir en achetant chinois pour 10€ la carte "clone" d'Arduino UNO dans les prix les plus bas. Je ne conseil pas forcement, mais si vous avez peur de griller la carte, ou pour faire des achats de groupe cela peut-être intéressant. En réalité les makers sont fidèles à la marque Arduino pour sa qualité, tels que les soudures etc. Petit listing des prix croissant:

*   [Carte UNO R3 chinois Feiyang 10,22€](https://fr.aliexpress.com/item/32831857482.html?spm=a2g0o.detail.1000014.6.5fec43a5mtbkAz&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.274735.0&scm_id=1007.40050.274735.0&scm-url=1007.40050.274735.0&pvid=cefbbf12-c165-40e8-8b65-ad754c54af9a&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.274735.0,pvid:cefbbf12-c165-40e8-8b65-ad754c54af9a,tpp_buckets:668%232846%238114%231999&pdp_ext_f=%257B%2522sku_id%2522%253A%252265339139953%2522%252C%2522sceneId%2522%253A%252230050%2522%257D&pdp_pi=-1%253B7.55%253B-1%253B-1%2540salePrice%253BEUR%253Brecommend-recommend)
*   [Gotronic GT016 UNO R3 10,90€](https://www.gotronic.fr/art-carte-go-tronic-gt016-26125.htm)
*   [Carte DFRduino DFR0216 12,90€](https://www.gotronic.fr/art-carte-dfrduino-dfr0216-20306.htm)
*   [Keyestudio UNOR3 14,61€](https://fr.aliexpress.com/item/4000873964058.html?gatewayAdapt=glo2fra&spm=a2g0o.store_pc_promotion.promoteRecommendProducts_undefined.14)
*   [Carte Joy-It R3DIP 16,90€](https://www.gotronic.fr/art-carte-joy-it-r3dip-25413.htm)
*   [ELEGOO UNO R3 18,99€](https://www.amazon.fr/Elegoo-ATmega328P-ATMEGA16U2-Controller-Microcontr%C3%B4leur/dp/B01N91PVIS/ref=asc_df_B01N91PVIS/?tag=googshopfr-21&linkCode=df0&hvadid=106800305641&hvpos=&hvnetw=g&hvrand=1358551832062616299&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9055186&hvtargid=pla-329356109727&psc=1)
*   [Arduino UNO R3 officiel 19,50€](https://www.gotronic.fr/art-carte-arduino-uno-12420.htm)

Si vous ne savez pas quoi prendre, prenez la carte officielle, sachez que d'autres modèles clones existent, c'est à titre indicatif, pour montrer l'éco-système autour de la carte. Maintenant que vous avez une vague idée à quoi ressemble la carte de prototypage électronique parlons-en.

### Caractéristique de l'Arduino UNO

La carte Arduino est un circuit imprimé conçu pour héberger un microcontrôleur et données accès à des entrées / sorties. Elle comprend aussi quelques autres composants électroniques qui permettent de faire fonctionner le microcontrôleur ou d'étendre les fonctionalités.

Un microcontrôleur est un petit ordinateur, le cerveau du circuit intégré en électronique. C'est une puce en l'occurrence le modèle 8bits ATMEGA328 fabriqué par Atmel. C'est également cela que l'on appel des semi-conducteurs dans l'industrie. Grâce à la puce nous allons pouvoir contrôler nos entrées / sorties et donc les programmer.  

L'Arduino seul ne sert pas à grand chose, il a besoin de sentir des objets du monde réel grâce à une série de capteur et d'agir dessus (actionneur). Il faut penser communication et intéraction avec l'extérieur permettant l'envoi de signaux. Quand on apprend l'exercice de base est de faire clignoter une LED (diode electroluminescente) pour vérifier que tout fonctionne bien. Il faut choisir de positionner la LED sur une sortie de la carte et de programmer un délai pour faire clignoter. C'est la version "Hello World" en électronique.

### Interface de programmation

Arduino est un superbe outil pour apprendre la programmation en langage C qui est le standard quand il s'agit de système embarqué. Il fournit un logiciel pour écrire du code, un [Arduino IDE](https://www.arduino.cc/en/software) et permet de téléverser dans le microcontrôleur et la mémoire flash de 32Kb. On est en environnement contraint avec peu de ressource mémoire, il est impossible de compiler un système d'exploitation avec seulement 32kb ou simplement d'avoir un compilateur sur la carte. Arduino IDE va simplifier la tâche de cross-compilation et traduire en langage machine le code en le téléversant dans le microcontrôleur. On peut également [programmer en C++](https://www.youtube.com/watch?v=_el8cUKFpJo&ab_channel=EricPeronnin) pour ce faire il faut changer d'éditeur de texte pour utiliser des outils comme VScode et plateformIO qui sont plus adapté.

### IoT: Internet des objets

Arduino peut faire office d'objet connecté à internet. Pour ce faire il faut ajouter des fonctions grâces à des shields tels que le wifi ou [ethernet](https://www.gotronic.fr/art-ethernet-shield-2-a000024-23299.htm). Là cela devient intéressant car on va pouvoir intéragir avec un site web et serveur mais egalement analyser des DATAs que l'on va enregistrer et monitorer comme pour faire de la domotique.

### Robotique

Arduino est un objet de choix pour initier à la robotique et apprendre à contrôler la machine. Il vous faudra des capteurs et actionneurs tel qu'un servo-moteur. Cela peut-être très tentant pour les enfants de jouer avec des robots mais également aux ingénieurs, les possibilités sont illimités. C'est tout un univers et vous pourrez trouver des projets Arduino sur internet traitant du sujet de la robotique. Vous n'êtes pas seul d'autres on eu l'idée à travers le monde. OpenClassRoom le site dédié à l'apprentissage de l'informatique aborde le sujet de l'[initiation à la robotique avec Arduino](https://openclassrooms.com/fr/courses/4076871-sinitier-a-la-robotique/4083254-fabriquez-votre-propre-robot-arduino). Pour aller plus loin je recommande des sujets DIY sur les [drônes et Quadcopter](https://create.arduino.cc/projecthub/akarsh98/diy-arduino-based-quadcopter-drone-948153) avec Arduino ou vous pouvez construire certaines pièces en impression 3D.

### Kit de démarrage

Commencer à utiliser une carte Arduino sans composant électronique sert à rien. Il va falloir intéragir avec l'environnement et maitriser les bases de l'électronique tels que l'utilisation de résistance, condensateur et transistor etc... A cela ajoutez des capteurs et actionneurs, il faut compter 50€ + Arduino UNO 20€ pour atteindre environ 70€ d'investissement initial dans un kit de démarrage (starter kit). Il y a plusieurs façon de faire. 

*   [Starter kit officiel Arduino UNO 95€](https://www.gotronic.fr/art-starter-kit-arduino-k020007-en-francais-22949.htm)
*   [Kit d'Apprentissage pour Arduino UNO UCTRONICS 40€](https://www.robotshop.com/eu/fr/kit-apprentissage-avance-pour-arduino-uno-uctronics.html?gclid=CjwKCAjwxZqSBhAHEiwASr9n9OIfVeO9onT3ZQ9V0WAmLilpcwj8HiXzcse9poOyQtLEAUrAhhf_SBoCkswQAvD_BwE) 
*   [ELEGOO Carte Starter Kit de Démarrage 44€](https://www.amazon.fr/Elegoo-D%C3%A9marrage-dUtilisation-D%C3%A9butants-Professionnels/dp/B01JD2Z5XW/ref=asc_df_B01JD2Z5XW/?tag=googshopfr-21&linkCode=df0&hvadid=51048574806&hvpos=&hvnetw=g&hvrand=5674023775678939394&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9055186&hvtargid=pla-273870859096&psc=1)

Il est possible d'acheter les composants électroniques séparement tels que chez Gotronic si vous savez la liste et la référence des produits. Pour cela vous pouvez suivre les recommendations du site Zeste du Savoir qui a édité un livre en libre accès sur l'apprentissage d'Arduino à [cette adresse](https://zestedesavoir.com/tutoriels/686/arduino-premiers-pas-en-informatique-embarquee/). Vous trouverez une [liste d'achat](https://zestedesavoir.com/tutoriels/686/arduino-premiers-pas-en-informatique-embarquee/742_decouverte-de-larduino/3414_presentation-darduino/#4-10777_liste-dachat). Pour plus de détail utilisez mon document personnel de devis chez Gotronic avec quantité et référence produit sur [ce lien](https://docs.google.com/document/d/11zg9CfiQlGsX_OBRPir9_GQxPYS-UZBbgPNnxE33DXI/edit?usp=sharing) totalisant 76€ Arduino UNO inclus pour des composants de qualité et une boite de rangement.

### Suivre un livre

Je vous est recommandé le livre en libre accès pour apprendre Arduino du site zeste du savoir. Il suffit largement pour ce lancer dans l'aventure, si pour autant vous cherchez d'autres références, quelques livres traitant d'Arduino sont disponible sur [ce lien](https://www.axiseo.com/meilleurs-livre-arduino/).
