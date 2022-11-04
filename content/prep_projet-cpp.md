Title: Préparation de projet avancée en C++
Date: 2022-11-04 03:30
Category:C/C++
Tags:projet, doxygen, cmake, spaceinvaders
Authors: Anthony Le Goff
Summary:


Ceci est un How-to pour créer un projet C++ et le faire dans les règles de l'art. On va utiliser les outils standards de la communauté FLOSS (Free Libre Open Source Software). Car j'éduque dans ce sens à l'ingénierie logicielle tout en apprenant des méthodes pour moi même. J'apprends et je partage les meilleurs pratiques dans mes recherches sur internet.

**Consigne du challenge:**

* Créer un jeu-video de 1978: SPACE INVADERS avec SFML en programmation orienté-objet.
* Adapter ce jeu avec l'OpenGL.

Vous allez me dire qu'es-ce que [SFML](https://www.sfml-dev.org/index-fr.php), c'est une librairie multimédias pour interfacer avec les composants du PC pour avoir de l’interactivité pour créer des applications de jeux-videos entre autre. La partie [OpenGL](https://www.opengl.org/) est le standard que l'on utilise pour de la haute performance graphique.

on aurait très bien pus s'arrêter là, mais on va développer notre projet avec des standards de l'ingénierie logicielle en gestion de projet pour prendre des bonnes habitudes. Je veux que vous soyez opérationnel en C++, alors on reprend les bases:

**Les outils**

* Editeur de texte: [Neovim](http://neovim.io/)
* Compilateur: [g++](https://gcc.gnu.org/)
* Documentation: [Doxygen](https://www.doxygen.nl/)
* Gérer la compilation du projet: [cmake](https://cmake.org/)
* Contrôle de version: [Git](https://git-scm.com/)
* Système d'exploitation: [Arch Linux](https://archlinux.org/)

Pour apprendre à coder en C++ on peut s'appuyer sur ces livres:

* Introduction to programming with C++ for Engineers
* Modern C++ for absolute beginners
* C++ Primer

Des sites références pour nous aider dans notre apprentissage:

* [Zeste du Savoir - Moderne C++](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/)
* [Learncpp](https://www.learncpp.com/)
* [Hackingcpp](https://hackingcpp.com/)

Ce que l'on va construire pour notre projet, un template avec une arborescence root "spaceinvaders":

```
.git
.gitignore
build/
docs/CMakeLists.txt , Doxyfile.in
src/CmakeLists.txt , *.cpp, *.hpp
CMakeLists.txt
README.md
LICENCE
```

**Paquets prérequis en particulier quelques librairies externes C++ utiles pour les développeurs et ingénieurs:**

```
sudo pacman -S base-devel neovim llvm clang git mesa glfw-x11 boost cmake doxygen eigen qt6-base sfml sdl2
```

* base-devel pour les outils de compilation GCC
* neovim votre éditeur de texte
* [llvm](https://llvm.org/) compilateur infrastructure
* clang C language family Frontend for LLVM
* git controle de version
* mesa open-source implementation of OpenGL
* [glfw-x11](https://www.glfw.org/) Free open source openGL portable framework
* [boost](https://www.boost.org/) Free portable C++ source library (dev headers)
* cmake cross-platform open-source make system
* doxygen Documentation system for C++
* [eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) C++ template lib for vector, matrix, linear algebra
* [sdl2](https://www.libsdl.org/) A library low-level access to a video framebuffer, audio output, mouse, keyboard
* [qt6-base](https://www.qt.io/product/qt6) A cross-platform application and UI Framework
* sfml A simple, fast, cross-platform, objet-oriented multimedia API

**Créer votre dossier** `sources` dans /home ou vous allez y mettre vos projets
```
$ mkdir ~/sources
```

### 1. Configurer Git

Nous allons d'abord configurer Git pour les nouveaux venus et apprendre le contrôle de version. Vous trouverez sur internet [des tutoriels](https://www.youtube.com/watch?v=lhiSnzrvG48) pour gérer votre code.

Dans un terminal >

**Votre identité**
```
$ git config --global user.name "Anthony Le Goff"
$ git config --global user.mail triviality-lga@protonmail.com
```

**Votre éditeur de texte**
```
$ git config --global core.editor nvim
```

**Votre nom de branche par défaut**
```
$ git config --global init.defaultBranch main
```

**Vérifier les paramètres**
```
$ git config --List
```

### 2. Générer des clés publiques SSH

Si vous le savez pas encore, l'authentification sous Github utilise maintenant SSH par défaut, il faut donc générer une paire de clé et l'ajouter dans Github pour ce connecter au dépôt distant.

```
$ cd ~/.ssh
$ ssh-keygen -o
```

Suivez la procédure et créer un mot de passe

Enfin pour récupérer la valeur de la clé publique généré à copiez sur Github:
```
cat ~/.ssh/id_rsa.pub
```

Copiez la clé sur un notepad en attendant.

### 3. Copiez la clé publique sur son compte Github

Créer un compte Github, si ce n'est déjà fait. Allez dans `settings/ssh and GPG keys/new SSH Key`. Collez la clé publique et valider.

### 4. Créer un repository

* Cliquez sur + en haut à droite puis "new repository".
* Dans repository name tapez: `spaceinvaders`. 
* Cochez: Add a README File
* Choisir add .gitignore template C++
* Choose a licence: GNU General Public Licence v3.0

Cliquez sur "Create repository" puis sur le bouton vert Code/ssh et copiez la ligne:
```
git@github.com:<monPseudo>/spaceinvaders.git
```

### 5. Cloner votre repository en local

Dans un terminal, allez dans votre dossier de travail projet `sources`:
```
cd ~/sources
```

puis cloner le repo git:
```
git clone git@github.com:<monPseudo>/spaceinvaders.git
```

Vous avez maintenant un nouveau dossier "spaceinvaders" avec quelques fichiers copiez depuis le dépôt distant Github.

### 6. Ignorer le dossier build sur le repo distant

Editer dans votre projet `spaceinvaders`:
```
nvim .gitignore
```

* Ajoutez au début `**/build/`
* Sauvegarder et quittez neovim


### 7. Configurer (Neo)Vim pour C++

Petit rappel pour les débutants. Pour ce familiariser avec Vim, lancer la commande dans un terminal `vimtutor`. Vous pouvez également apprendre à configurer Vim qui est un peu différent de Neovim avec le livre: [Vim pour les humains](https://vimebook.com/fr) en libre accès.

Une fois que vous êtes prêt avec Vim, apprenez de ces deux vidéos pour la suite:

1. [Setting up (Neo)vim for C++: A IDE like experience with coc!](https://www.youtube.com/watch?v=ViHgyApE9zM)
2. [Setting up (Neo)vim for C++: IDE like Files, CMake and GTest integrations!](https://www.youtube.com/watch?v=Y_UubM5eYAM)

N'oubliez pas de créer votre config file dans `~/.config/nvim/init.vim`

Mon propre init.vim pour information:
```bash
" Neovim configuration file init.vim
" author: Anthony J.R Le Goff 
" date: 16th april 2022

:set number
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4
":set mouse=a

call plug#begin() 

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'scrooloose/nerdtree'
Plug 'scrooloose/syntastic'
Plug 'vim-airline/vim-airline'
Plug 'tomasr/molokai'
Plug 'raimondi/delimitmate'
Plug 'kien/ctrlp.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'majutsushi/tagbar'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

set encoding=UTF-8

call plug#end()

:set statusline+=%#warningmsg#
:set statusline+=%{SyntasticStatuslineFlag()}
:set statusline+=%*

:let g:syntastic_always_populate_loc_list = 1
:let g:syntastic_auto_loc_list = 1
:let g:syntastic_check_on_open = 1
:let g:syntastic_check_on_wq = 0

nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

nmap <C-r> :TagbarToggle<CR>
nmap <C-p> :CtrlP<CR>

:colorscheme molokai

let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="~"

" air-line
let g:airline_powerline_fonts = 1


" :CocInstall coc-python
" :CocInstall coc-clangd
" :CocInstall coc-java
```

### 8. Cmake + Doxygen

Pour vous familiarisez avec Cmake quelques ressources disponibles pour mieux comprendre les fichiers de configurations:

* (Video) [Simplified Cmake Tutorial](https://www.youtube.com/watch?v=mKZ-i-UfGgQ&t=25s)
* [Cours de Supelec sur Cmake](http://sirien.metz.supelec.fr/depot/SIR/TutorielCMake/index.html)

Nos fichiers de configurations pour notre projet:

spaceinvaders/CMakeLists.txt
```
cmake_minimum_required ( VERSION 3.10 )
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
project(spaceinvaders version 1.0)
add_subdirectory(src)
add_subdirectory(docs)
```

spaceinvaders/src/CMakeLists.txt
```
# Dependance de librairie externe
find_package(SFML 2 REQUIRED network audio graphics window system)

add_executable(mainDemo main.cpp)
target_compile_options(mainDemo PUBLIC -Wall -Wextra)

# On install le binaire
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/mainDemo
	DESTINATION bin
	RENAME ${CMAKE_PROJECT_NAME}-mainDemo)
	
# On construit le binaire avec SFML
target_include_directories(mainDemo PUBLIC ${SFML_INCLUDE_DIR})
target_link_librairies(mainDemo PUBLIC ${SFML_LIBRARIES} ${SFML_DEPENDENCIES})

# Librairie dynamique headers

add_library(mainDemo
	SHARED
	main.cpp)

install(TARGETS mainDemo
	DESTINATION lib)
	
File(
	GLOB
	headers
	*.hpp
)
```

**Préparation de la documentation**

On utilise le programme Doxygen pour générer le fichier de configuration dans le dossier `spaceinvaders/docs/`:
```
$ cd ~/sources/spaceinvaders
$ mkdir docs
$ cd docs
$ doxygen -g Doxyfile.in
```

On édite le fichier avec neovim pour le configurer avec cmake:
```
	  PROJECT_NAME           = ${CMAKE_PROJECT_NAME}
	  OUTPUT_DIRECTORY       = ${CMAKE_BINARY_DIR}/docs/
	  INPUT                  = ${CMAKE_SOURCE_DIR}/src
	  EXTRACT_ALL            = YES
```

spaceinvaders/docs/CMakeLists.txt
```
find_package(Doxygen)
if(NOT DOXYGEN_FOUND)
    message("Doxygen not found, I will not generate/install the documentation")
else()
   configure_file(Doxyfile.in Doxyfile)

   set(DOXYGEN_INPUT ${CMAKE_BINARY_DIR}/docs/Doxyfile)
   set(DOXYGEN_OUTPUT ${APIDOC_DIR}/html/index.html)

   add_custom_target(doc ALL
     COMMAND ${CMAKE_COMMAND} -E echo_append "Building API Documentation..."
     COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_INPUT} > /dev/null
     COMMAND ${CMAKE_COMMAND} -E echo "Done."
     )

  install(DIRECTORY ${CMAKE_BINARY_DIR}/docs/html 
          DESTINATION share/doc/${CMAKE_PROJECT_NAME})

endif()
```

Pour la documentation, dans `docs` est généré un `index.html` avec les commentaires du code au format Doxygen depuis les fichiers sources. On peut ensuite envoyer sur un site online tels que [https://codedocs.xyz/](https://codedocs.xyz/) à partir de repository Github. Enfin renseignez-vous sur l'utilisation de Sphinx/breathe pour générer de la documentation également.

### 9. Compilation et installation

```
$ cd ~/sources/spaceinvaders
$ mkdir build
$ cd build
$ cmake ..
$ make
$ ./src/mainDemo
$ make install
```

### 10. Commiter votre code

Vous allez faire vos premiers commits de votre code. Il va falloir suivre des fichiers. Créer un `main.cpp` et `class.hpp` basics dans `src/` pour appeler une classe et faire un "hello world" pour tester si tout fonctionne.

**Suivi et Commit du code**

Dans votre dossier projet root `spaceinvaders` lancez les commandes:
```
$ git add . && git commit -m "commit init"
```

Pusher votre code sur Github
```
$ git push origin main
```

### 11. Pour aller plus loin

* Test unitaire avec [GTest](https://google.github.io/googletest/primer.html)
* Créer une archive `tar.gz`
* utilisez CPack/PkgBuild comme générateur de paquet pour Arch Linux

### Conclusion

Voila vous savez presque tout pour bien démarrer un projet avancée en C++ en développant un Space Invaders grâce à la librairie SFML en utilisant tous les outils nécessaire à une bonne organisation du projet. N'oubliez pas de commenter votre code! Après un mois on oublie souvent pourquoi on a créé une fonction, un algorithme ou une classe, donc soyez prévoyant en particulier sur des longs projets ou quand plusieurs personnes ce joint à vous pour du social coding. 