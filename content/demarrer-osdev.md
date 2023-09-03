Title:Base pour démarrer un système d'exploitation en assembleur
Date: 2023-09-03 16:32
Category:Inclassable
Tags:asm
Authors: Anthony Le Goff
Summary:

On va montrer le code de base commenté pour démarrer un système d'exploitation, je n'affiche pas les instructions "Hello World". juste booter le segment en mémoire et être "Ready" pour écrire quelques choses. 

Noter le bien, le processeur ne comprends que le langage d'assemblage spécifique au constructeur. Le Kernel Linux pour le créer il faut d'abord booter en assembleur qui invoque après le langage C. 

Ce que vous avez besoin:

* Un compilateur en assembleur `Nasm`
* Un émulateur via `Qemu`
* Créer un `Makefile` pour automatiser les tâches

```bash
$ sudo pacman -S base-devel nasm qemu-full
```

Créer un dossier de developpement disont `osdev`
```bash
$ mdkir osdev
$ cd osdev
$ mkdir src
$ mkdir build
```

On va créer notre fichier principal en asm
```asm
$ nvim src/main.asm

[org 0x7C00] ; initialisation des segment secteur boot
[bits 16] ; on travail en 16 bits, processeur Intel 8086

main:
	 hlt

.halt:
	jmp .halt


; --- NOP Jusqu'à 510 ---
	times 510-($-$$) db 0
	dw 0xAA55
```

Puis on va automatiser la compilation avec un Makefile
```makefile
$ nvim Makefile

ASM=nasm

SRC_DIR=src
BUILD_DIR=build

$(BUILD_DIR)/main_floppy.img: $(BUILD_DIR)/main.bin 
	cp $(BUILD_DIR)/main.bin $(BUILD_DIR)/main_floppy.img
	truncate -s 1440k $(BUILD_DIR)/main_floppy.img 

$(BUILD_DIR)/main.bin: $(SRC_DIR)/main.asm 
	$(ASM) $(SRC_DIR)/main.asm -f bin -o $(BUILD_DIR)/main.bin
```

Pour lancer la compilation on tape la commande `make` qui va générer notre binaire et copier dans un format .img

Puis on lance dans le terminal shell la virtualisation via `Qemu` qui devrait ouvrir une fenètre confirmant le fonctionnement du code
```bash
$ qemu-system-i386 -fda build/main_floppy.img
```
