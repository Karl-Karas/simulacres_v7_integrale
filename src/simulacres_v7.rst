.. _simulacres_v7:

.. compile with:
.. rst2latex --new-class-functions \
..           --stylesheet=sim_styles.sty \
..           --documentclass=extarticle \
..           --documentoptions=a4paper,twocolumn,9pt,twoside \
..           --language=fr \
..             simulacres_v7.txt > simulacres_v7.tex && \
.. ../bin/float_img.py simulacres_v7.tex && \
.. pdflatex simulacres_v7.tex

.. include:: common_subs.txt

.. raw:: latex

    \begin{titlepage}
        \begin{center}
            \includegraphics[width=0.9\textwidth]{images/simulacres_logo_big.png}

            \vspace{2cm}
            Version 7

            1994 - 1997

            \vspace{1cm}
            {\Huge\textbf{Pierre Rosenthal}}


            \vspace{2cm}
            La compilation de \textbf{Karl Karas} - version 1.0

            \vspace{6cm}

            \begin{minipage}{12cm}
            \footnotesize
                Simulacres™ est une marque déposée par Pierre Rosenthal, toute
                utilisation est soumise à l’autorisation de Pierre Rosenthal
                (roliste@wanadoo.fr).
                
                \vspace{5mm}
                \textbf{En ce qui concerne le jeu de rôle Simulacres©™ :}
                
                Son utilisation gratuite dans le cadre associatif, gratuit ou
                privé est autorisé.
                
                Des auteurs amateurs ou des associations peuvent donc utiliser
                tout ou partie des règles (y compris les symboles, mais pas les
                illustrations), les univers, conseils et scénarios étant
                exclus.
                
                Ceci autorise la création de jeux, univers et scénarios
                utilisant tout ou partie de Simulacres à titre gratuit.
                
                Seule obligation : mentionner que le système Simulacres™ est
                une marque déposée de Pierre Rosenthal et soumis aux copyrights
                ©.
                
                Pour toute exploitation commerciale, veuillez contacter Pierre
                Rosenthal (roliste@wanadoo.fr)
            \end{minipage}
        \end{center}
    \end{titlepage}
    \thispagestyle{empty}
    
.. =============================================
.. :red:`Simulacres, le Jeu de Rôle Élémentaire`
.. =============================================

.. class:: Huge

    **Note de l'éditeur**

Ce projet de compilation de l'intégrale de Simulacres v7 est né de ma pratique
continue du jeu depuis sa sortie en 1994. Étudiant sans le sou à l'époque, le
hors-série de Casus Belli avait un prix abordable pour moi et a été ma porte
d'entrée dans le jeu de rôle. Je ne l'ai plus quitté depuis. Malgré quelques
infidélités au cours du temps, il reste mon jeu principal, que ce soit pour
faire de l'initiation ou pour une campagne qui dure depuis plus de 15 ans.

Cependant, pour ceux qui n'ont pas (encore) suivi Pierre Rosenthal avec la v8
et qui pratiquent toujours Simulacres v7, l'utilisation des textes de référence
devient petit à petit problématique : les suppléments de Casus Belli ont pris
de l'âge, les couvertures se déchirent, les reliures se défont et, parfois, les
feuilles s'envolent. Pour avoir l'ensemble des règles de base, il faut de plus
manipuler 2 hors-séries : le 10 (Simulacres) et le 11 (SangDragon).

En outre, si on souhaite utiliser certaines des règles optionnelles parues dans
les différents Petits Capharnaüms, il faut alors utiliser des copies ou
manipuler encore d'autres numéros de Casus. Bien entendu, les fichiers pdf
permettent de consulter les textes sans avoir recourt à leur support physique
d'antan, mais ce n'est tout de même pas la même chose.

Enfin, par la nature de sa publication originale, Simulacres v7 ne s'insère pas
facilement dans une bibliothèque (réelle) de rôliste et, pour mon jeu
principal, je trouve cela dommage.

C'est pour toutes ces raisons que je souhaitais disposer d'une version complète
et cohérente, imprimable et reliable, que je pourrais emporter sans craindre de
l'abîmer et qui pourrait se tenir aux côtés de mes autres jeux de rôle. Cette
compilation représente l'aboutissement de mon effort pour arriver à cet
objectif. Puisque Pierre nous permet d'utiliser ses textes, si ce travail peut
servir à d'autres vieux passionnés, je pense que ça vaut la peine de le mettre
à disposition du plus grand nombre.

En conclusion, je tiens à remercier ici **Pierre Rosenthal**, non seulement
d'avoir imaginé et publié Simulacres, mais aussi et peut-être surtout d'en
avoir fait un système abordable et ouvert qui a préfiguré, plus d'une décennie
à l'avance, tout le mouvement des licences ouvertes en jeux de rôle.

|s|

**Karl Karas**

.. raw:: latex

    \clearpage
    \newpage
    \setcounter{page}{1}

.. class:: center 

 .. class:: red

  **Simulacres est un jeu de rôle généraliste, contenant tout ce qui est
  nécessaire pour faire jouer dans n’importe quel univers. Nous vous proposons
  ici le corpus de règles publié dans divers hors-séries de Casus Belli, ainsi
  que dans plusieurs rubriques du Petit Capharnaüm. Si vous désirez découvrir
  les univers ou les scénarios publiés pour Simulacres, il vous faudra vous
  procurer ces publications.**

.. image:: images/L.png
    :width: 1.5cm
    :align: left

es règles de Simulacres sont présentées dans les chapitres suivants. Elles
proviennent principalement du hors-série 11 de Casus Belli nommé « |s|
SangDragon |s| ». Les autres sources de cette compilation sont le hors-série
10, présentant la première publication de la version 7 du jeu, ainsi que le
contenu des Petits Capharnaüms numéros 15, 16, 17, 18, 19, 24 et 25. L'objectif
de ce document étant de proposer une compilation, les éditions ont été limitées
au strict minimum, il reste donc certaines incohérences mineures entre les
différentes parties du texte.

Pour vous laisser le choix du degré de complexité des règles que nous avons
suivi la même présentation que celle du hors-série 10 : d’abord savoir comment
fonctionne le personnage et comment le créer avec les **règles de base** ; puis
la découverte des **mécanismes du jeu** (p. :pageref:`base`) ; et enfin comment
effectivement créer un personnage avec les **règles de campagne**, et toutes
les adaptations nécessaires (p. :pageref:`campagne-start`).  Les **règles de
magie** (p. :pageref:`magie`) n’auront à être connues que du meneur de jeu et
des joueurs dont le personnage est magicien. On présente ensuite les **règles
optionnelles** (p. :pageref:`regles-optionnelles-generales`), ainsi que
certaines **règles spécifiques** (p. :pageref:`regles-specifiques`).

En fin de volume, vous trouverez des aides de jeux (p.
:pageref:`aides-de-jeu`), dont les tableaux récapitulatifs de l'Écran de jeu,
le bestiaire complet de Simulacres, comprenant celui publié dans le hors-série
14 de Casus Belli (p.  :pageref:`bestiaire`), et finalement la liste complète
des sorts (p.  :pageref:`grimoire-start`).

.. include:: personnage_joueur.rst
.. include:: mecanismes_de_jeu.rst
.. include:: intervenants.rst
.. include:: regles_de_campagne.rst
.. include:: magie.rst
.. include:: regles_optionnelles.rst
.. include:: regles_specifiques.rst
.. include:: aides_de_jeu.rst
.. include:: bestiaire.rst
.. include:: grimoire.rst

