Title:C++ eco-système
Date: 2022-02-15 08:59
Category:C/C++
Tags: outils, communauté, c++
Authors: Anthony Le Goff
Summary:


Ce sujet traite de l'éco-système C++ en allant aux outils à la communauté pour être plus productif dans le travail et devenir un développeur averti.

### Compileurs

![GCC Logo](images/gccegg-65.png)

**GCC g++**  

De facto le standard sous GNU/Linux:   

*   [https://gcc.gnu.org/](https://gcc.gnu.org/)  
    
*   sur Windows WinLibs: [https://winlibs.com/](https://winlibs.com/) et [WSL](https://docs.microsoft.com/fr-fr/windows/wsl/about)

![LLVM Logo](images/LLVM-Logo-Derivative-3.png)

**LLVM clang++**

Un compileur concurrent de GCC qui offre de meilleur performance  

*   [https://llvm.org/](https://llvm.org/)  
    

![Visual C++ Logo](images/visual-logo.png)

**Microsoft visual C++**  

Pour utiliser le C++ moderne il faut installer la dernière version du logiciel

*   [Documentation sur Microsoft C++, C, Assembleur](https://docs.microsoft.com/fr-fr/cpp/?view=msvc-170)
*   [https://visualstudio.microsoft.com/fr/free-developer-offers/](https://visualstudio.microsoft.com/fr/free-developer-offers/)  
    

  

### Compileurs online

Il est possible d'accéder sur internet à des compileurs en ligne

*   [https://godbolt.org/](https://godbolt.org/)  gcc, permet d'avoir une sortie en assembleur  
    
*   [https://coliru.stacked-crooked.com/](https://coliru.stacked-crooked.com/) gcc  
    
*   [https://wandbox.org/](https://wandbox.org/) inclus Boost, clang++, gcc  
    

### Debugging

**gdb**  

*   [https://www.sourceware.org/gdb/](https://www.sourceware.org/gdb/)  
    
*   [Intro to gdb](https://hackingcpp.com/cpp/tools/gdb_intro.html)
*   frontend DDD: [https://www.gnu.org/software/ddd/](https://www.gnu.org/software/ddd/)

**WinDBG**  

*   [Microsoft documentation](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools)  
    

**x64dbg**

*   [https://x64dbg.com/](https://x64dbg.com/) Pour Windows, .DLL, .EXE etc...

### Code Analyseur

**ASAN(Adress SANITIZER)**  

*   [https://clang.llvm.org/docs/AddressSanitizer.html](https://clang.llvm.org/docs/AddressSanitizer.html)  
    
*   [Intro, détection de corruption mémoire](https://hackingcpp.com/cpp/tools/asan.html)

### Stand-alone outils d'analyse

**Valgrind**  

Valgrind est un outil de programmation libre pour déboguer, effectuer du profilage de code et mettre en évidence des fuites mémoires.  

*   [https://valgrind.org/](https://valgrind.org/)  
    
*   [Intro](https://hackingcpp.com/cpp/tools/valgrind.html)
*   [Quick Start](https://valgrind.org/docs/manual/quick-start.html)

### Profiling & Benchmarking

**GNU gprof**  

Gprof est un logiciel GNU Binary Utilities qui permet d'effectuer du profilage de code. Cela permet de détecter dans le code le temps d'éxécution qui demanderait à être ré-écrit.  

*   [https://sourceware.org/binutils/docs/gprof/](https://sourceware.org/binutils/docs/gprof/)  
    
*   [Tutorial](https://www.thegeekstuff.com/2012/08/gprof-tutorial/)

**Valgrind**  

*   cachegrind, callgrind
*   [https://valgrind.org/info/tools.html](https://valgrind.org/info/tools.html)  
    

**Perf**  

perf: Linux profiling with performance counters  

*   [https://perf.wiki.kernel.org/index.php/Main\_Page](https://perf.wiki.kernel.org/index.php/Main_Page)  
    
*   [Tutorial](https://perf.wiki.kernel.org/index.php/Tutorial)

### Documentation  

**Doxygen**  

Outil d'annotation et de création de documentation C++  

*   [https://www.doxygen.nl/index.html](https://www.doxygen.nl/index.html)  
    
*   [Documenter son code avec Doxygen](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/etre-un-developpeur/mais-ou-est-la-doc/#3-documenter-son-code-avec-doxygen)

### Benchmarking librairies / framework

**gperftools**  

Implementation du multi-threading pour malloc() haute performance  

*   [https://github.com/gperftools/gperftools/wiki](https://github.com/gperftools/gperftools/wiki)  
    
*   HEAP checker, CPU profiler

### Build Systems

**GNU Make**  

**Make** est un logiciel qui construit automatiquement des fichiers, souvent exécutables, ou des bibliothèques à partir d'éléments de base tels que du code source. Il utilise des fichiers appelés **makefile** qui spécifient comment construire les fichiers cibles  

S'utilise pour de petit projet, tous les développeurs devraient savoir faire un makefile.

*   [https://www.gnu.org/software/make/](https://www.gnu.org/software/make/)  
    
*   [Cheatsheet](https://devhints.io/makefile)
*   [Manuel](https://www.gnu.org/software/make/manual/make.html)

**CMake**   

_CMake_ est un outil permettant d'automatiser le processus de compilation et d'installation d'un logiciel.  

*   [https://cmake.org/](https://cmake.org/)  
    
*   Standard en C++
*   [A introduction to modern CMake](https://cliutils.gitlab.io/modern-cmake/)
*   [A template CMake project to get you started with C++ and tooling](https://github.com/cpp-best-practices/cpp_starter_project)  
    

### Test Unitaire

**Doctest**  

*   [https://github.com/doctest/doctest](https://github.com/doctest/doctest)  
    
*   [Tutorial](https://github.com/doctest/doctest/blob/master/doc/markdown/tutorial.md)

### Package management

**Conan**  

*   [https://conan.io/](https://conan.io/)  
    
*   Fonctionne avec CMake, MSbuild

### Source code management

**Git**  

*   Le standard dans l'industrie
*   [https://git-scm.com/](https://git-scm.com/)  
    

### Autres liens

*   [A curated list of awesome C++ (or C) frameworks, libraries, resources](https://github.com/fffaraz/awesome-cpp)  
    
*   [Toolchain ressource](https://www.toolchains.net/)

### Langage reference

**cppreference**

*   [https://en.cppreference.com/w/](https://en.cppreference.com/w/)  
    

### Best practices / Core guidelines

*   [https://github.com/cpp-best-practices/cppbestpractices/blob/master/00-Table\_of\_Contents.md](https://github.com/cpp-best-practices/cppbestpractices/blob/master/00-Table_of_Contents.md)  
    
*   [https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md)  
    

### Social Media

**Reddit**  

*   C++ Communauté [https://www.reddit.com/r/cpp/](https://www.reddit.com/r/cpp/)  
    

**#include ＜C++＞**

*   Discord server [https://www.includecpp.org/discord/](https://www.includecpp.org/discord/)  
    

**Developpez.net**  

*   Forum [https://www.developpez.net/forums/f19/c-cpp/cpp/](https://www.developpez.net/forums/f19/c-cpp/cpp/)  
    

### Groupe d'utilisateur

**C++ francophone CPP-FRUG**  

*   [https://www.meetup.com/fr-FR/User-Group-Cpp-Francophone/](https://www.meetup.com/fr-FR/User-Group-Cpp-Francophone/)  
    
*   [http://cppfrug.org/](http://cppfrug.org/)
