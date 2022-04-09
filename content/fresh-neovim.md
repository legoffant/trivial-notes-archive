Title:﻿ Fresh Neovim
Date: 2022-04-09 15:04
Category:Linux
Tags: neovim
Authors: Anthony Le Goff
Summary:

﻿Fresh Neovim  

Je viens de passer un peu de temps à revoir mon éditeur de texte, j'ai essayé un peu VScode mais je reste attaché à Vim, au départ c'est un peu rude l'apprentissage qui est un éditeur de texte modal, il faut un certain temps pour le maitriser. 

En 2014, un fork de Vim nommé Neovim est apparu, et une extension particulière a attiré mon attention dans les servers de langage pour l'auto-completion nommé CoC. Je cherchais un moyen de mettre à jour ma config un peu vieillissante sous Vim pour utiliser des plugins innovants. Alors J'ai switcher sur Neovim, et je lui donne sa chance.

Je ne suis pas déçu du résultat, après quelques configuration je retrouve mes habitudes sous Vim mais avec CoC au lieu de YouCompleteMe.

Pour ceux qui on raté un wagon, récapitulation de la base de connaissance pour démarrer sous Vim:

1\. Lancer `vimtutor` pour apprendre dans un terminal

2\. Suivez le livre "[Vim pour les humains](https://vimebook.com/fr)" en accès libre pour ce familliariser

Ainsi passer de Vim à Neovim se fera sans souci. Une vidéo pour [configurer from scratch Neovim](https://www.youtube.com/watch?v=JWReY93Vl6g&ab_channel=NeuralNine). J'utilise clangd pour du C/C++. Il a fallut que je configure les flags pour qu'il accepte le c++17.

Créer le fichier `~/.config/clangd/config.yaml`  

config.yaml
```
CompileFlags:  
  Add: [-Wall, -Wextra, -std=c++20]
```
