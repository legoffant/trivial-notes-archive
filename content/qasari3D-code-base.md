Title:Les premières lignes de code de Qasari3D
Date: 2023-10-27 16:10
Category:Inclassable
Tags:qasari
Authors: Anthony Le Goff
Summary:

Voila de quoi travailler. Il faut bien un départ, et ce code doit être maitriser en C++.

Voici comment je lance les premières briques de Qasari3D avec l'utilisation de chaptGPT. Tout d'abord c'est un framework, avec des modules ou l'on définir une architecture simple logiciel. On va construire autour du framework qui est à la base une interface CLI pour intérragir avec l'utilisateur en CLI.

Ce que l'on va faire:

* Créer la base du framework comme support des modules
* Définir une nanite basic comme template dans un module
* Créer une module d'initialisation de projet
* Intégrer des scripts Lua pour ajouter des fonctionnalités personnalisés

Il va falloir gérer un prompt interactif, le logiciel est minimaliste et doit intégrer et ce complexifier via des modules.

### Framework

Créer un framework en C++ basé sur une interface en ligne de commande (CLI) pour charger des modules est un projet plus complexe que dans le cas de Python, mais cela offre une grande flexibilité. Voici comment vous pourriez approcher la création d'un tel framework en C++ avec une explication détaillée du code :

**Étape 1 : Création de la Structure du Projet**

1. Créez un répertoire pour votre projet. À l'intérieur, organisez vos fichiers et modules. Créez un répertoire appelé "modules" pour stocker les modules.

**Étape 2 : Modules**

2. Chaque module représente une fonctionnalité spécifique que le framework peut effectuer, comme la modélisation, la conversion de fichiers, la visualisation, etc. Chaque module sera implémenté dans un fichier C++ séparé.

**Étape 3 : Fichier Principal (main.cpp)**

3. Créez un fichier C++ principal (par exemple, `main.cpp`) qui servira de point d'entrée pour le framework. Dans ce fichier, vous gérerez le chargement des modules et l'interaction avec l'utilisateur.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <dlfcn.h> // Pour le chargement dynamique des bibliothèques partagées

// Définition de la structure d'un module
struct Module {
    void* handle; // Gestionnaire de la bibliothèque partagée
    void (*run)(); // Pointeur vers la fonction d'exécution du module
};

int main() {
    // Map pour stocker les modules chargés
    std::map<std::string, Module> modules;

    // Boucle d'interaction avec l'utilisateur
    while (true) {
        std::cout << "Entrez le nom du module à charger (ou 'exit' pour quitter) : ";
        std::string moduleName;
        std::cin >> moduleName;

        if (moduleName == "exit") {
            break;
        }

        // Tentative de chargement du module
        void* moduleHandle = dlopen(("modules/lib" + moduleName + ".so").c_str(), RTLD_LAZY);
        if (moduleHandle == nullptr) {
            std::cerr << "Impossible de charger le module." << std::endl;
            continue;
        }

        // Récupération du pointeur vers la fonction run
        void (*run)() = (void (*)())dlsym(moduleHandle, "run");
        if (run == nullptr) {
            std::cerr << "Module invalide." << std::endl;
            dlclose(moduleHandle);
            continue;
        }

        // Stockage du module dans la map
        modules[moduleName] = {moduleHandle, run};

        // Exécution du module
        run();
    }

    // Libération des modules chargés
    for (auto& pair : modules) {
        dlclose(pair.second.handle);
    }

    return 0;
}
```

**Étape 4 : Modules (modules/module_name.cpp)**

4. Chaque module est implémenté dans un fichier C++ séparé (par exemple, `module_name.cpp`). Voici un exemple de module simple :

```cpp
#include <iostream>

extern "C" void run() {
    std::cout << "Exécution du module de test." << std::endl;
}
```

**Étape 5 : Compilation**

5. Compilez le code en utilisant un compilateur C++ (g++ dans cet exemple). Assurez-vous d'inclure l'option `-rdynamic` pour permettre le chargement dynamique des modules.

```bash
g++ -o framework main.cpp -ldl -rdynamic
g++ -shared -o modules/libtest.so modules/test.cpp
```

**Étape 6 : Exécution**

6. Exécutez le framework en tapant `./framework`. Vous pouvez charger des modules en entrant leur nom, par exemple, "test".

**Explication du Code :**

- Le fichier principal (main.cpp) gère le chargement dynamique des modules à l'aide de la fonction `dlopen` et exécute les modules en appelant leur fonction `run`.

- Chaque module est stocké dans une bibliothèque partagée (fichier .so) qui est chargée dynamiquement.

- Les modules sont stockés dans une map où la clé est le nom du module et la valeur est une structure contenant le gestionnaire de bibliothèque partagée et le pointeur vers la fonction `run`.

- Lorsque l'utilisateur entre le nom d'un module, le framework tente de charger ce module à partir du répertoire "modules" et exécute la fonction `run` du module.

- À la fin de l'exécution, les modules sont libérés à l'aide de `dlclose`.

Ce code montre comment créer un framework en C++ avec une CLI pour charger et exécuter des modules dynamiquement. Vous pouvez étendre ce modèle en ajoutant plus de modules et en personnalisant les fonctionnalités de chaque module selon vos besoins.

### Module nanites

Si vous souhaitez créer un framework de CAO basé sur des modules, et que vous souhaitez définir des "nanites" comme des templates de modèles, vous pouvez concevoir un module dédié à la création, la gestion et l'instanciation de ces nanites. Voici comment vous pourriez aborder la création d'un module pour définir des nanites :

**Étape 1 : Création du Module**

Créez un nouveau fichier C++ (par exemple, `nanite_module.cpp`) pour votre module de gestion des nanites.

**Étape 2 : Structure de Nanite**

Définissez une structure ou une classe C++ pour représenter une nanite. Une nanite pourrait avoir des propriétés telles que des dimensions, des caractéristiques géométriques, des matériaux, des relations avec d'autres nanites, etc.

```cpp
struct Nanite {
    // Propriétés de la nanite
    double x, y, z; // Coordonnées
    double width, height, depth; // Dimensions
    // ... d'autres propriétés ...
};
```

**Étape 3 : Gestion des Nanites**

Dans le module, implémentez des fonctions pour créer, modifier, supprimer et lister des nanites. Vous pouvez également fournir des fonctions pour définir des relations entre les nanites si cela fait partie de votre modèle.

```cpp
#include <vector>

std::vector<Nanite> nanites; // Un conteneur pour stocker les nanites

// Fonction pour créer une nouvelle nanite
void createNanite(double x, double y, double z, double width, double height, double depth) {
    Nanite newNanite;
    newNanite.x = x;
    newNanite.y = y;
    newNanite.z = z;
    newNanite.width = width;
    newNanite.height = height;
    newNanite.depth = depth;
    // ... initialisation d'autres propriétés ...
    nanites.push_back(newNanite);
}

// Fonction pour lister toutes les nanites
void listNanites() {
    for (const Nanite& nanite : nanites) {
        // Affichez les propriétés de chaque nanite
        // Vous pouvez personnaliser le format de sortie ici
    }
}

// Autres fonctions pour modifier, supprimer et gérer les nanites
```

**Étape 4 : Module de Compilation**

Compilez le module de gestion des nanites en une bibliothèque partagée (fichier .so) que vous pouvez charger dynamiquement dans votre framework principal.

```bash
g++ -shared -o modules/libnanite_module.so nanite_module.cpp
```

**Étape 5 : Intégration dans le Framework Principal**

Dans votre framework principal (main.cpp), chargez le module de gestion des nanites et utilisez les fonctions du module pour créer, modifier et lister des nanites.

Cette approche vous permet de définir et de gérer des nanites en tant que modèles de base dans votre framework de CAO. Vous pouvez étendre ce modèle pour inclure des fonctionnalités de relations entre les nanites, de génération procédurale, de conception paramétrée, etc., en fonction de vos besoins spécifiques.

### Initialisation de projet

Il est tout à fait possible d'intégrer une invite de commande (CLI) dans votre framework de CAO pour permettre aux utilisateurs d'initialiser différents types de projets avec des nanites. Pour ce faire, vous devrez créer un module spécifique qui gère cette fonctionnalité. Voici comment vous pourriez approcher la création de ce module :

**Étape 1 : Création du Module d'Initialisation de Projets**

Créez un nouveau fichier C++ pour votre module d'initialisation de projets (par exemple, `project_init.cpp`).

**Étape 2 : Structure de Projet**

Définissez une structure de projet qui représente les caractéristiques d'un projet, y compris les types de nanites, les paramètres par défaut, les configurations, etc.

```cpp
struct Project {
    std::string projectName;
    std::vector<Nanite> nanites; // Liste des nanites du projet
    // ... autres propriétés ...
};
```

**Étape 3 : Fonctions d'Initialisation de Projets**

Dans le module, implémentez des fonctions pour créer, configurer et gérer des projets. Par exemple, vous pouvez créer des fonctions pour créer un nouveau projet, ajouter des nanites, configurer des paramètres par défaut, etc.

```cpp
#include <vector>
#include <iostream>

std::vector<Project> projects; // Un conteneur pour stocker les projets

// Fonction pour créer un nouveau projet
void createProject(const std::string& projectName) {
    Project newProject;
    newProject.projectName = projectName;
    // ... initialisation d'autres propriétés ...
    projects.push_back(newProject);
    std::cout << "Projet '" << projectName << "' créé avec succès." << std::endl;
}

// Fonction pour ajouter des nanites à un projet existant
void addNaniteToProject(const std::string& projectName, const Nanite& nanite) {
    for (Project& project : projects) {
        if (project.projectName == projectName) {
            project.nanites.push_back(nanite);
            std::cout << "Nanite ajoutée au projet '" << projectName << "'." << std::endl;
            return;
        }
    }
    std::cerr << "Projet '" << projectName << "' non trouvé." << std::endl;
}
```

**Étape 4 : Module de Compilation**

Compilez le module d'initialisation de projets en une bibliothèque partagée (fichier .so) que vous pourrez charger dynamiquement dans votre framework principal.

```bash
g++ -shared -o modules/libproject_init.so project_init.cpp
```

**Étape 5 : Intégration dans le Framework Principal**

Dans votre framework principal (main.cpp), chargez le module d'initialisation de projets et utilisez les fonctions du module pour créer et gérer des projets.

Avec ce module, les utilisateurs peuvent utiliser l'invite de commande pour créer différents types de projets, ajouter des nanites, configurer des paramètres par défaut, etc. Cette fonctionnalité facilitera la gestion de projets complexes et la personnalisation des modèles en fonction des besoins de l'utilisateur. Vous pouvez également étendre ce module pour inclure des fonctionnalités avancées, telles que des modèles de projet prédéfinis, des configurations personnalisées, etc.

### Intégration de script lua

Intégrer une interface avec des scripts Lua dans votre framework de CAO est une excellente idée, car cela permet aux utilisateurs d'ajouter des fonctionnalités personnalisées en écrivant des scripts Lua sans avoir à recompiler le code source principal. Voici comment vous pourriez intégrer cette fonctionnalité :

**Étape 1 : Intégration de Lua**

1. Intégrez la bibliothèque Lua à votre framework de CAO. Vous pouvez utiliser une bibliothèque C/C++ pour Lua, comme [LuaBridge](https://github.com/vinniefalco/LuaBridge), pour faciliter l'intégration.

**Étape 2 : Configuration de l'Interpréteur Lua**

2. Configurez un interpréteur Lua dans votre framework, qui permettra d'exécuter des scripts Lua. Vous pouvez également créer un environnement Lua pour isoler les scripts.

```cpp
extern "C" {
    #include "lua.h"
    #include "lualib.h"
    #include "lauxlib.h"
}

lua_State* L = luaL_newstate();
luaL_openlibs(L);
```

**Étape 3 : Exposition des Fonctions C/C++ aux Scripts Lua**

3. Exposez les fonctions C/C++ de votre framework aux scripts Lua en utilisant LuaBridge ou une méthode similaire. Cela permet aux scripts Lua d'appeler des fonctions de votre framework.

```cpp
#include "LuaBridge/LuaBridge.h"

// Exemple : Exposer une fonction C++ pour créer un nouveau projet depuis un script Lua
luabridge::getGlobalNamespace(L)
    .beginNamespace("Framework")
        .addFunction("createProject", &createProject)
    .endNamespace();
```

**Étape 4 : Chargement et Exécution des Scripts Lua**

4. Vous pouvez charger et exécuter des scripts Lua depuis un fichier ou même à partir d'une chaîne de caractères. Vous pouvez également gérer des événements de script qui se déclenchent à des moments spécifiques de l'exécution de votre framework.

```cpp
// Charger et exécuter un script Lua depuis un fichier
if (luaL_dofile(L, "script.lua") != 0) {
    std::cerr << "Erreur lors de l'exécution du script Lua : " << lua_tostring(L, -1) << std::endl;
    lua_pop(L, 1); // Supprimer le message d'erreur de la pile Lua
}

// Appel d'une fonction Lua depuis C++
luabridge::LuaRef result = luabridge::getGlobal(L, "myLuaFunction")(arg1, arg2);
```

**Étape 5 : Gestion des Erreurs**

5. Assurez-vous de gérer les erreurs dans les scripts Lua, en capturant les exceptions Lua et en fournissant des informations utiles aux utilisateurs en cas de problème.

**Étape 6 : Intégration de Scripts Lua dans l'Interface Utilisateur**

6. Intégrez une interface utilisateur dans votre framework qui permet aux utilisateurs de charger, éditer et exécuter des scripts Lua. Vous pouvez également ajouter des fonctionnalités telles que la coloration syntaxique pour faciliter l'écriture de scripts.

L'intégration de Lua permet aux utilisateurs de personnaliser leur expérience avec le logiciel de CAO en ajoutant des fonctionnalités spécifiques à leurs besoins. Cela peut être particulièrement utile pour l'automatisation de tâches, la création de scripts de génération procédurale, la définition de nanites personnalisées, etc.