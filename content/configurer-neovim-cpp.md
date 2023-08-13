Title:Configurer (Neo)Vim comme IDE en langage C/C++
Date: 2023-08-13 08:45
Category:Linux
Tags:vim, coc
Authors: Anthony Le Goff
Summary:

On peut très bien apprendre à coder dans un terminal shell avec un simple éditeur de texte comme `Vim` et utiliser le compilateur. C-a-d Ouvrir un terminal sous Linux:

```cpp
$ vim hello.cpp

// Premier programme en C++ 

#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
```

On compile en manuel, normalement gcc est intégré en natif dans le système Linux:
```bash
$ g++ hello.cpp -o hello
```

On lance le fichier binaire:
```bash
$ ./hello
```

Output:
```text
Hello World!"
```

Voila, pour apprendre à utiliser Vim plus en détail, l'éditeur de texte pour les professionnels de l'informatique:

[L’éditeur de texte VI](https://linux.goffinet.org/administration/traitement-du-texte/editeur-de-texte-vi/)

> Ce chapitre est un incontournable de la maîtrise d’un système Linux. Dans 99,99 % des cas, l’éditeur VI est présent sur votre système. Pourquoi s’en passer ?

Egalement le livre numérique [PDF] gratuit "[Vim pour les humains](https://vimebook.com/fr)" est une très bonne ressource pour apprendre Vim.

### Transformer Vim en IDE (environnement de développement intégré)

Vim est un peu lite, c'est du brute de décoffrage mais il est customisable et extensible. Pour avoir des fonctions supplémentaires et d'automatisation:

* Recherche dans le code
* Navigation dans les fichiers
* Controle de version Git
* Refactoring
* Coloration syntaxique
* Code complétion
* Assistance avec une IA
* ctags
* Intégration de makefile / cmake
* Intégration du debugger
* multi-fenetrage / tabs
* snippet
* CI/CD
* test unitaire

etc...

On va donc apprendre à configurer le fork de Vim: `Neovim` avec [Coc](https://github.com/neoclide/coc.nvim). Qui a plus de fonctionnalité pour du code en C/C++.

Prérequis sur le système:

```bash
$ sudo pacman -S clang ctags neovim nodejs npm gdb
```

Vérifier l'installation
```bash
$ clangd --version

clangd version 15.0.7
Features: linux
Platform: x86_64-pc-linux-gnu
```

### Introduction à Neovim

lancer le tutorial dans un terminal `vimtutor`

Vidéo explicative pour configurer Neovim:

* [Setting up (Neo)vim for C++: An IDE like experience with coc!](https://www.youtube.com/watch?v=ViHgyApE9zM)
* [Setting up (Neo)vim for C++ Part 2: IDE like Files, CMake and GTest integrations!](https://www.youtube.com/watch?v=Y_UubM5eYAM&t=2s)

### Configuration de Neovim

Installation du gestionnaire de plugin "vim-plug" cf: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)

```bash
$ sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

Création du fichier `init.vim` dans `~/.config/nvim/`

```text
" Neovim configuration file init.vim
" author: Anthony J.R Le Goff legoff.ant@gmail.com
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
Plug 'madox2/vim-ai'

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


```

Sauvegarder le fichier, quitter et relancer `nvim` puis lancer la commande:
```bash
:PlugInstall
```

Après cela vous aller pouvoir installer via le serveur de langage le code completion pour C/C++ avec Coc:
```bash
:CocInstall coc-clangd
```

#### Intégration de C++23 dans clangd

Créer le fichier `~/.config/clangd/config.yaml`

config.yaml
```text
CompileFlags:  
  Add: [-Wall, -Wextra, -std=c++23]
```

#### Utiliser le debugger sur un programme

Télécharger et lancer le plugin:
```bash
:packadd termdebug
:Termdebug
```
