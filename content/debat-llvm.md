Title:Débat doit-on basculer sur le compilateur LLVM en C/C++?
Date: 2023-09-03 09:05
Category:C/C++
Tags:
Authors: Anthony Le Goff
Summary:

Ma réponse serait **"oui"**. Outre le symbolisme du dragon comme logo, c'est un compilateur plus performant que GCC. Je l'utilise déjà pour Neovim et Coc pour l'auto-complétion avec clangd.

Donc le projet Qasari devrait être codé avec LLVM.

* [GCC vs Clang.LLVM: An In-Depth Comparison of C/C++ Compilers](https://alibabatech.medium.com/gcc-vs-clang-llvm-an-in-depth-comparison-of-c-c-compilers-899ede2be378)
* [LLVM Clang 16 vs. GCC 13 Compiler Performance On Intel Raptor Lake](https://www.phoronix.com/review/gcc13-clang16-raptorlake)

### Installation

```bash
sudo pacman -S llvm
```

### Utilisation

Pour compiler on utilise l'utilitaire en front-end `clang`

hello.cpp
```cpp
#include <iostream>

int main() {

   std::cout << "Hello World!";
   return 0;
}

```

```bash
clang++ hello.cpp -o hello -Wall -Wextra -std=c++23
```
