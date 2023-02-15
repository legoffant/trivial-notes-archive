Title:Memento d'autodidacte en informatique
Date: 2023-02-15 06:52
Category:Linux
Tags:debuter
Authors: Anthony Le Goff
Summary:

La méthode pour apprendre la programmation dans les règles de l'art et prendre des bonnes habitudes selon les professionnels de l'informatique est de commencer par la langage C avec les outils associés. C'est old school mais cela permet de ce familiariser avec le terminal et la ligne de commande. Il faut fuir les EDI (Environnement de development intégré). On utilise des outils qui consomme très peu de ressource processeur et en mémoire, prenez l'habitude du minimalisme d'ou la priorité de passer par le terminal.  

Bien sur la ligne de commande, c'est complètement has been sous Windows MS-DOS, il faut un environnement qui a été conçu pour à partir d'UNIX. Il n'y a pas d'outil d'édition de code sous Windows en ligne de commande en natif, ce n'est pas fait pour ça. Powershell est une surcouche qui n'intègre pas des outils de développement, juste du scripting. Il faut passer par des interfaces graphiques(GUI) ou EDI. Ce qui est à proscrire.  

Pourquoi les utilisateurs GNU/Linux vont sur Arch Linux: pour le minimalisme et la customisation, c'est presque une religion de nerd, un programmeur professionnel passe sa majeur partie du temps à utiliser le terminal et la ligne de commande, c'est un problème d'abstraction et de productivité, on automatise les tâches en ligne de commande par du scripting. On passe par des standards, et tel que le démontre [ce sondage sur l'environnement de développement des programmeurs en langage C](https://www.jetbrains.com/lp/devecosystem-2021/c/): Le compilateur est GCC. C'est à dire du logiciel libre qui s'utilise dans un terminal en ligne de commande en natif sous GNU/Linux. Il y a tous les outils en natif sous GNU/Linux pour développer en langage C dont:  

*   Vim - Editeur de texte  
    
*   GCC - Compilateur  
    
*   Make - Automatisation de build  
    

Il reste à intégrer d'autres outils dans le workflow, toujours dans un terminal pour être à jour:  

*   Git - Control de version  
    
*   Tmux - Terminal Multiplexer  
    
*   GDB - Debugger  
    

L'utilisation de Git et de Make dans Vim est très simple qui permet de gagner en productivité. On fait tous au clavier pour naviguer, il y a très peu de clic de la souris à contrario avec des éditeurs comme VSCode. Cela demande un peu de temps pour apprendre Vim, mais cela en vaut la peine car c'est un couteau-suisse, vous pouvez passer à Neovim une fois familiarisé. Le livre en libre accès [Vim pour les humains](https://vimebook.com/fr) est parfait pour les débutants. Il faut également faire le tutorial Vim dans un terminal en lançant la commande: vimtutor.  

Pour bien utiliser la gestion de fichier et dossier ainsi que la navigation dans le système de fichier vous devez connaître la base des commandes dans un terminal UNIX tel que ls, cd, pwd, touch, mkdir. La plupart des programmeurs customisent le shell avec des outils tels que [oh-My-Zsh](https://ohmyz.sh/).  

Le langage C est partout, à la base des systèmes d'exploitation et de la programmation système en passant par le kernel Linux. C'est le langage maître ou dérive les autres à l'origine. Il est relativement proche de la machine en particulier dans la gestion de la mémoire et les pointeurs. Vous ne pouvez pas être un informaticien averti sans connaître les pointeurs ou l'allocation dynamique de mémoire. L'informatique ce n'est pas faire du web(HTML, CSS, Javascript) . Des langages essayent de le remplacer tel que Rust plus safe sur la gestion de la mémoire, mais ce n'est pas demain la veille qu'on ne manipulera plus des pointeurs.  

Les livres essentiels à ce procurer pour tous développeur C:  

*   Débutant: Le C en 20 heures [en libre accès](https://archives.framabook.org/le-c-en-20-heures-2/index.html), Framabook, Berthomier & Schang  
    
*   Intermédiaire: Learn C The hard Way, Zed A. Shaw  
    
*   Experimenté: The ANSI C Programming Language, K&R  
    

C'est à travers la communauté FOSS que l'on s'épanouit en informatique, ou il est possible d'étudier le code source des systèmes et le modifier et customiser selon ces besoins, ne tombez pas dans le piège d'apprendre l'informatique dans des systèmes fermés et propriétaires tels que Microsoft ou Apple qui contraint l'utilisateur, on vous prends pour des enfants ou il faut vous tenir la main, ou l'on occulte le fonctionnement de l'ordinateur à travers des interfaces graphiques, ce n'est pas la solution.