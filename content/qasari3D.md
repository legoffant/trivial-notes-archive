Title: QASARI3D
Date: 2022-11-10 14:29
Category:Entrepreneurship
Tags:libfive
Authors: Anthony Le Goff
Summary:

A tout Empire, il faut des outils de construction. On doit pouvoir modéliser, simuler et valider l'allocation des ressources pour créer un objet réel, de n'importe quel complexité.

Je reviens sur cette note que j'ai écrite: [Rendre accessible la création](https://legoffant.github.io/rendre-accessible-la-creation.html)

Ou je commence à parler de mes idées de logiciel de conception industrielle open source. Comme je disais la CAO est le caniveau des logiciels propriétaires. Des truands comme Dassault Systèmes.

Ce que je veux intégrer [Obligatoire]:

* La collaboration sur les ensembles et pièces tels que Git pour le code
* La génération procédurale en prémisse à nanites.
* Prototypage rapide et le G-Code
* Conception architecturale basé sur openBIM
* Supercalculateur pour de la CFD, FEA etc avec du calcul distribué
* Intelligence artificielle CLI
* Blockchain pour la paternité d'une invention dans des registres.
* Kernel Geometric Modeling

D'autres Plugins seront possible d'être ajouté par la communauté tels que de la PLM, CFAO. En faite il faut créer une "carte mère" avec des API, gestion de Plugins. Un sorte de CLI dans un terminal avec l'assistance d'une intelligence artificielle pour créer un projet et définir les contraintes, module à utiliser.

Je cherche donc des solutions. Ou il va falloir le programme qui fera office de carte mère ou l'on va interfacer des modules et gérer le projet. En ce moment je regardais le "geometric kernel modeling". J'ai laissé tombé Open Cascade, il est ancien et puis appartient à Cap Gemini, petit rappel que ces rats ne veulent pas me payer.

J'ai trouvé ce projet Open Source qui intègre des innovations, codé en C++11. Nommé LibFive. Il utilise également le langage de programmation Guile Scheme.

```
git clone https://github.com/libfive/libfive
```

Cela pourrait être une première base de travail. Il me faut des programmeurs et ingénieurs en C++, il y a quelques mathématiques sur le kernel de niveau ingénieur. Voir comment on peut intégrer la génération procédurale en natif.

Comment s'appel le projet: `QASARI3D`

Qui va créer le logiciel? Alpharatz Consulting, l'ESN que je veux créer sera en charge du développement, maintenance et de la formation. On va sur un business model basé sur Rapid7.