Title:Apprendre le C++ sous MCU Arduino UNO R3
Date: 2023-06-28 21:17
Category:C/C++
Tags:Arduino
Authors: Anthony Le Goff
Summary:


Arduino utilise un langage épuré à base de C. Il y a très peu de fonction et donc plus facile pour l'apprentissage. Durant un certain temps il fallait utiliser le logiciel Arduino IDE 1.0 qui était très limité pour programmer la carte de prototype électronique. Après  c'est simplifié, suffit d'installer le logiciel et tout marche, ainsi que le port série vers UNO. C'est la version pour les grands débutants et les newbies. Je rappel le lien utile pour apprendre Arduino UNO en libre accès [Arduino : premiers pas en informatique embarquée \[PDF\]](https://eskimon.fr/extra/ebooks/arduino-premiers-pas-en-informatique-embarquee.pdf)  

On va passer à la méthode professionnel chez les développeurs et ingénieurs en systèmes embarqués et microcontrôleurs MCU en utilisant le workflow:  

*   **PlatformIO** is a cross-platform, cross-architecture, multiple framework, professional tool for embedded systems engineers and for software developers who write applications for embedded products.  
    
*   **(Neo)Vim** is a free and open-source, screen-based text editor program for use both from a command-line interface. Et donc d'utiliser des plugins tels que CoC (auto-completion), fugitive (integration de Git) etc.  
    
*   **Picocom** monitor the serial interface  
    

Ce qui permet une plus grande souplesse d'utilisation et de programmer en C++ avec des librairies customs via un éditeur de texte pour professionnel tel que Vim dans un terminal.  

### Installer PlatformIO CLI sur un environnement GNU/Linux (Arch Linux) en utilisant virtualenv en Python:  

```
$ sudo pacman -S python python-pip  
$ python -m pip install --user virtualenv
```
  

Puis installer le package platformio dans un dossier en activant l'environnement virtuel:  

```
$ mkdir -p ~/local
$ cd ~/local   
$ python -m venv platformio   
$ source platformio/bin/activate   
$ pip install platformio
```

NOTA: pour désactiver virtualenv: `$ deactivate`

Cela veut dire que les commandes de platformIO CLI sont disponible dans l'environnement virtuel dans le chemin PATH : `~/local/platformio/bin/pio`

### Rechercher le nom de la carte Arduino UNO R3:  
```
(platformio) $ platformio boards | grep uno
        uno                   atmega328p     16Mhz     31Kb    2Kb    Arduino Uno
```

### Créer un projet  

En l’occurrence on va appeler le projet 'blink' pour faire clignoter une LED sur Arduino pour vérifier que tout fonctionne.
```
$ mkdir ~/project/Blink
$ cd ~/project/Blink
$ pio project init --board uno --ide vim
```

générera un sous-dossier vide et un fichier projet (`platformio.ini`). Le format de `platformio.ini` est [fichier INI](https://en.wikipedia.org/wiki/INI_file).  

### Recherchez les noms des ports série:  

L'Arduino doit communiquer via une interface. Le micrologiciel intégré est téléchargé via le port série. La valeur par défaut est `/dev/ttyUSB0`, donc si vous connectez Arduino, la mise à jour échouera si elle est laissée telle quelle car le nom du port est différent. Par conséquent, il est nécessaire de vérifier le nom du port série et de le spécifier dans `platformio.ini`  

De plus il faut verifier les droits sur le port série, souvent on a pas les privilèges d'accès en écriture. Il faut ajouter l'utilisateur au groupe `uucp` sous Arch Linux(voir wiki Arduino):

```
$ sudo usermod -aG uucp username
```

Lister les ports de série:  
```
(platformio)$ platformio serialports list
        :   #réduction
        /dev/ttyACM0
        ----------
        Hardware ID: USB VID:PID=1a86:7523
        Description: QinHeng Electronics USB2.0-Serial
```

Dans cette exemple on utilise `/dev/ttyACM0` et donc il faut modifier `platformio.ini` avec Vim au paramêtre [upload_port](https://docs.platformio.org/en/latest/projectconf/sections/env/options/upload/upload_port.html)`  

### Ecrire la source

Le clignotement habituel de la LED et l'affichage en série. Mettez la source dans `./src`.  

```cpp

$ vim src/blink.cpp  


#include <Arduino.h>

void setup() {  
    pinMode( LED\_BUILTIN, OUTPUT );  
    Serial.begin(9600);  
}  
   
void loop() {  
    Serial.println("Hello Arduino");

    digitalWrite( LED\_BUILTIN, HIGH );    
    delay(333);                        
   
    digitalWrite( LED\_BUILTIN, LOW );    
    delay(333);                        
}  
```

Dans le programme, il faut utiliser le header `Arduino.h` pour utiliser les librairies et fonctions de la carte. En C++ on utilise le mot clé void. Egalement j'utilise un print pour avoir un retour d'affichage de fonctionnement sur le monitoring du port série.  

### Essayer de compiler:  

La commande va télécharger le programme et flasher la carte UNO:  

```
$ pio run --target=upload
```

Normalement la LED built-in devrait clignoter si tout fonctionne.

### Vim Quickfix Mode  

Pour intégrer avec Vim's quickfix mode un simple makefile suffit:  

```makefile

    .PHONY: all
    all: build
    
    
    .PHONY: build
    build:
        pio run
    
    .PHONY: upload
    upload:
        pio run --target=upload
```

Ensuite vous pouvez automatiser la compilation en lançant la commande dans Vim `:make`

### Monitoring du port de série  

On va installer picocom pour le monitoring: 

```
$ sudo pacman -S picocom  
```

la commande pour monitorer  

```
$ picocom --baud 9600 --echo --noreset /dev/ttyUSB0
```

Qui devrait normalement retourner en affichage le print:

```
Hello Arduino
```
 
Plus d'information sur la doc officiel:` [https://docs.platformio.org/en/latest/index.html](https://docs.platformio.org/en/latest/index.html)