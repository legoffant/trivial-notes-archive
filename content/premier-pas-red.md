Title:Premier pas en langage Red
Date: 2023-07-28 03:05
Category:Linux
Tags:red
Authors: Anthony Le Goff
Summary:

Voila que j'apprend un nouveau langage, et me suis dit pourquoi pas le Red. Donc j'ai installé les toochains et CLI tools. Cela a été laborieux.... Pas encore au point, problème avec des librairies partagées car cela fonctionne que en 32bits.

Sous Arch:
```
$ yay -S red lib32-gdk-pixbuf2 lib32-gtk3
```
en lançant la commande `red` on obtient un REPL (interpréteur)

Récupérer le toolschain pour compiler des programmes: [Télécharger sur la page](https://www.red-lang.org/p/download.html) puis renommer le fichier en `redc` et faite un chmod u+x pour le rendre executable:
```
$ chmod u+x redc
```

Premier programme "hello World", Neovim ne reconnait pas l'extension, par de coloration syntaxique.
```
$ nvim hello.red

 Red [
     Title: "Simple hello world script"
 ]

 print "Hello World!"
```

On compile:
```
./redc -c hello.red
```

Il va génerer plusieurs fichiers, et le temps de compilation est assez long....

```
-rwxr--r-- 1 trivial trivial   85344 28 juil. 02:56 hello
-rw-r--r-- 1 trivial trivial      73 28 juil. 02:53 hello.red
-rw-r--r-- 1 trivial trivial  332088 28 juil. 02:56 libRedRT-defs.r
-rw-r--r-- 1 trivial trivial     414 28 juil. 02:56 libRedRT-extras.r
-rw-r--r-- 1 trivial trivial   69005 28 juil. 02:56 libRedRT-include.red
-rwxr--r-- 1 trivial trivial 1300352 28 juil. 02:56 libRedRT.so
-rwxr--r-- 1 trivial trivial 1551836 28 juil. 02:54 redc
```

Le binaire fait 85k.

En lance l'executable:
```
./hello
```
J'ai une erreur avec un module GTK, mais ça compile.
```
$ ./hello
Gtk-Message: 03:02:41.047: Failed to load module "xapp-gtk3-module"
Gtk-Message: 03:02:41.049: Failed to load module "xapp-gtk3-module"
Hello World!
```

J'ai trouvé ce site sur l'apprentissage du langage: [Red Language Notebook](https://ungaretti.gitbooks.io/red-language-notebook/content/)



