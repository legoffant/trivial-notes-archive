Title:Lichee Pi 4A Desktop RISC-V
Date: 2022-12-30 00:58
Category:Inclassable
Tags:risc-v
Authors: Anthony Le Goff
Summary:

Je suis à la recherche de configurer un PC de bureau Next-Gen Low Cost et basse consommation d'énergie. Je m'interesse à des mini-PC voir nano-ordinateur pour le développement. J'attendais qu'un processeur correcte sorte en [RISC-V](https://fr.wikipedia.org/wiki/RISC-V) l'architecture open source. Et voila que cela bouge dans le milieu. Il faut savoir que c'est le début de la guerre des semi-conducteurs ou la Chine à misé sur l'architecture Open Source RISC-V pour faire en particulier concurrence à ARM (ce que l'on retrouve sur les Raspberry Pi). [Sipeed](https://www.sipeed.com/), une marque chinoise à sortie une [SBC](https://fr.wikipedia.org/wiki/Ordinateur_%C3%A0_carte_unique) pour concurrencer Raspberry Pi. Les caractéristiques sont très intéressante, utilisant en particulier le processeur TH1520 qui a été développé par la plateforme Alibaba Cloud:  

> Un exemple de la performance de la plateforme Wujian 600 est reflété dans le développement et le prototypage du TH1520, un SoC de haute performance par T-head. **Le TH1520 fait preuve d’une vitesse et d’une efficacité énergétique exceptionnelles dans un dispositif informatique d’intelligence artificielle embarqué.** Il est sur un CPU Xuantie C910 à quatre cœurs pouvant atteindre 2,5 GHz, 4 TOPs de NPU, 64 bits 4266MT sur DDR  

La carte [Sipeed Lichee Pi 4A](https://sipeed.com/licheepi4a) peut avoir 16GB de RAM et jusqu'à 128GB d'eMMC en stockage interne. Pour une somme estimé à 140$.  

Question OS il sera en natif sous Debian. Sipeed travail déjà avec la communauté Ubuntu et on peut espérer que la communauté Arch Linux développe sa propre solution, en tout cas je suis partant pour donner un coup de main, et en plus je pourrais peut-être avoir une carte Lichee Pi A 4A gratuitement pour le développement.  

J'ai donc fait mon petit configurateur et devis pour préparer un PC desktop sur la carte et sa conso énergétique, en intégrant un RAID 1 SSD pour mes documents ainsi qu'un nouvel écran full HD reconditionné (j'ai un écran qui a 12 ans en DVI) Je m'en sors pour **un total de 393€**:  

\------------------------------  

PC de Bureau RISC-V  

\------------------------------  

Lichee Pi 4A LM4A

*   RISC-V 1,8Ghz x4 TH1520  
    
*   16 GB RAM  
    
*   \+ 32 GB eMMC (/root)  
    
*   GPU Imagination  
    
*   NPU 4TOPS@INT8 1GHz  
    
*   Wifi / bluetooth  
    
*   Ethernet x2  
    
*   USB 3.0 x4  
    

  

\=140$

  

5V x 700mA = 3,5W

\--------------------

Chez LDLC

  

2 x SSD Crucial BX500

*   SATA 6GB/s  
    
*   480GO (/home)  
    

  

\=90€

  

ICY BOX IB-123CL-U3

*   2 baies 2,5"  
    
*   Clonage disque  
    

  

\=56€

  

2 x 2W = 4W

\---------------------

Chez Backmarket

  

Écran 21" LED FHD Dell P2217H  

*   1920 x 1080  
    
*   LED  
    
*   1x HDMI  
    

  

\=107€

  

18W

  

TOTAL = 393€

Conso estimé: 26W