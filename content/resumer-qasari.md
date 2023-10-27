Title:Qasari3D Core choix d'implémentation
Date: 2023-10-27 03:33
Category:Inclassable
Tags:qasari
Authors: Anthony Le Goff
Summary:

Voila un résumer de comment est architecturé la partie "Core" de Qasari à programmer et développer, avec l'implémentation technologique.
Rappel rapide des outils de développement:

* Langage C++
* Compilateur LLVM
* Build manager Cmake
* Documentation Doxigen
* Plateforme UNIX Like
* Editeur de texte (neo)vim

Liste des modules "CORE"

1. **Initialisation du Projet** :
    - Module d'initialisation du projet : Créez un nouveau projet de CAO, configurez les paramètres initiaux, gérez les fichiers de projet et configurez l'environnement de travail.

2. **Gestion des Nanites** :
    - Module de création de nanites : Permet la création, l'édition et l'organisation des nanites, qui servent d'éléments de base pour la modélisation.
    - Module de transformation : Gère les transformations géométriques (translation, rotation, mise à l'échelle) pour les nanites et les objets.
    - Module d'interaction avec les nanites : Pour interagir avec les nanites via une interface utilisateur, y compris la sélection, la modification et la suppression.
    - Module de cotation automatique : Pour générer automatiquement des cotations sur les dessins à l'aide des nanites.
    - Module de loi d'évolution de TRIZ pour gérer l'automatisation des nanites

3. **Scripts Personnalisés en Lua** :
    - Module d'exécution de scripts Lua : Charge, exécute et interagit avec des scripts Lua personnalisés. Fournit une interface pour les scripts Lua pour interagir avec l'ensemble de l'application, y compris le moteur de modélisation et le générateur procédural. Implémentation: LuaBridge comme "Binding C++"
    - Permet d'écrire également en mode console CLI des formes complexes et personnalisés

4. **Interface Utilisateur** :
    - Module d'interface utilisateur : Crée et gère l'interface utilisateur de l'application, y compris les panneaux de dessin, les menus, les boîtes de dialogue et les outils de dessin. Implementation: Dear ImGui
    - Intégration de Lua dans l'interface utilisateur : Permet aux utilisateurs d'utiliser des scripts Lua directement à partir de l'interface utilisateur. 

5. **Gestion des Fichiers** :
    - Module de gestion de fichiers : Gère le chargement, l'enregistrement et la gestion des fichiers de dessins et de projets.
    - Gestion de conversion des .STEP amelioré

6. **Optimisation et Performance** :
    - Module d'optimisation de performance : Veille à ce que l'application fonctionne de manière fluide, même avec des dessins complexes.

7. **Moteur de Modélisation 2D/3D** :
    - Moteur de modélisation : Inclut les composants pour la création, la modification et la visualisation de modèles en 2D et en 3D. Gère les objets, les matériaux, les éclairages, les textures, etc. Implementation: Vulkan + GLFW + GLM (vkvg pour le 2D vectoriel)
    - Intégration de nanites : Permet l'utilisation des nanites comme composants du moteur de modélisation, permettant la création de modèles complexes.
    - Construit comme un moteur de jeu.

8. **Génération Procédurale** :
    - Module de génération procédurale : Permet la création de modèles et de formes géométriques à l'aide d'algorithmes de génération procédurale. Il peut utiliser des scripts personnalisés en Lua pour définir ces algorithmes. Implementation: Boost.Geometry

9. **Kernel Géométrique** :
    - Kernel géométrique : Fournit des fonctionnalités essentielles pour le traitement et la manipulation des données géométriques, y compris des opérations de géométrie de base, de modélisation, et de rendu.
    - Native utilise la generation procédurale basée sur les automates cellulaires. Implémentation: Libfive

10. **Base de Données** :

    - Module de gestion de base de données : Intègre un système de gestion de base de données pour stocker et gérer des projets, des modèles, des scripts, des métadonnées, et d'autres informations pertinentes. Assurez-vous que la base de données est capable de gérer les opérations CRUD (Create, Read, Update, Delete) et de fournir des fonctionnalités de recherche et de requête. Implémentation: SurrealDB pour de la graph database noSQL.

11. **Documentation et Aide** :
     - Module de documentation : Fournit de l'aide et de la documentation aux utilisateurs, y compris des tutoriels pour l'utilisation des nanites, des scripts Lua, de la génération procédurale, et du kernel géométrique. Implémentation: Doxygen + Wiki + CLI

12. **Tests et Débogage** :
     - Module de tests et de débogage : Facilite les tests unitaires, le débogage, et l'assurance qualité de l'ensemble de l'application.

12. **Sauvegarde et Contrôle de Version** :
     - Module de sauvegarde et de contrôle de version : Gère les versions et la sauvegarde des dessins, des projets, et des données générées par la génération procédurale. Implémentation: Perforce Helix Core pour gérer des .STEP amelioré en binaire.

