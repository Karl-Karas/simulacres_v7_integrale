Ce projet consiste à compiler les règles de Simulacres v7 et d'y joindre les
nombreuses extensions et options qui ont été publiées au cours du temps, afin
de constituer un document complet permettant de disposer de toute la gamme.

On pourra citer, entre autres :

- les règles Sangdragon (du HS11)
- le bestiaire de Sangdragon (du HS11, sans les spécificités de Malienda)
- les points de vie et armures localisées (du HS10)
- les pouvoirs psioniques (du HS10)
- les super pouvoirs (du HS10)
- le Bien, le Mal et la Nature
- la voie du guerrier
- la voie du moine
- les immortels, les inhumains
- les règles de déplacement et de poursuite
- le bestiaire fantastique du HS14
- ...

Techniquement
-------------

Le projet utilise le format RestructuredText
(https://docutils.sourceforge.io/rst.html) et l'outil rst2latex
(https://docutils.sourceforge.io/docs/user/latex.html) pour produire un pdf
complet imprimable, avec une feuille de style personnalisée.

Les polices de caractères sont Linux Libertine
(https://sourceforge.net/projects/linuxlibertine/), ainsi que celle de
Simulacres proprement dite (en téléchargement libre sur
https://www.facebook.com/groups/Simulacres/)

Pour compiler ::

 rst2latex  --new-class-functions \
            --table-style=booktabs \ 
            --stylesheet=sim_styles.sty \ 
            --documentclass=extarticle \
            --documentoptions=a4paper,twocolumn,9pt,twoside \
            --language=fr \
            simulacres_v7.rst > simulacres_v7.tex

 ../bin/float_img.py simulacres_v7.tex

 pdflatex simulacres_v7.tex

Attention
---------

Simulacres™ est une marque déposée par Pierre Rosenthal, toute utilisation est
soumise à l’autorisation de Pierre Rosenthal (roliste@wanadoo.fr).

En ce qui concerne le jeu de rôle Simulacres©™ :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Son utilisation gratuite dans le cadre associatif, gratuit ou privé est autorisé.

Des auteurs amateurs ou des associations peuvent donc utiliser tout ou partie
des règles (y compris les symboles, mais pas les illustrations), les univers,
conseils et scénarios étant exclus.

Ceci autorise la création de jeux, univers et scénarios utilisant tout ou
partie de Simulacres à titre gratuit.

Seule obligation : mentionner que le système Simulacres™ est une marque déposée
de Pierre Rosenthal et soumis aux copyrights ©.

Pour toute exploitation commerciale, veuillez contacter Pierre Rosenthal
(roliste@wanadoo.fr)

Ce projet vise à la constitution d'une compilation de textes pour faciliter le
travail de gestion du jeu à Simulacres v7. Il ne s'agit que de matériel
officiel, mais remis en forme dont Pierre Rosenthal ne peut garantir la
fiabilité.

TODO
----

- ajouter les références de pages pour les sorts identiques à ceux d'autres
  listes
- nice to have: passer la plupart des field lists en definition lists (plus
  propre dans la source, même rendu final)

DONE
----

- ré-écrire l'introduction
- règles Sangdragon de base + personnage joueur
- règles Sangdragon de campagne
- les intervenants
- la magie (hors liste de sorts) 
- définir les références de pages automatiquement en rst : sur base de trois
  rôles (LaTeX et rst) : label, ref et pageref
- ajouter les points de vie et armures localisées (HS10)
- ajouter les erratums et les composantes de sorts (LPC19)
- ajouter la Voie du Guerrier (LPC 24)
- ajouter Nuisance et Nature (LPC 17)
- ajouter les pouvoirs psy (HS10)
- ajouter les immortels, les inhumain, la voie du moine (LPC 25)
- ajouter les règles de poursuite de véhicules + dégâts et blindage (HS10)
- ajouter les animaux de monte (LPC 15)
- ajouter les supers pouvoirs (HS10)
- ajouter le bestiaire du HS14
- ajouter le bestiaire du HS11
- ajouter lamies et autres du LPC16
- ajouter l'origine des personnages med-fan (LPC 18)
- ajouter toutes les listes des sortilèges dans le grimoire (HS11)
- ajout de la fiche de perso pour les règles de base (HS10)
- ajout de la fiche de perso pour les règles de campagne (HS11)
- ajout de la fiche de perso pour les règles de PV localisé (HS10)
- ajout de la fiche de perso pour les magiciens (HS11)
- ajout de la fiche de perso pour les magiciens hermétiques (HS10)
- refaire tous les tableaux et figures diverses
- ajouter une annexe avec les tableaux pour l'écran de MJ



