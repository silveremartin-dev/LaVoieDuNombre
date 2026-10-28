#set page(
  paper: "a4",
  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 [
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[LA VOIE DU NOMBRE — Guide de l'Accompagnateur],
        text(size: 8.5pt, fill: rgb("#64748b"), font: "Liberation Sans")[Fondations Didactiques & Clés Pratiques]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    let page-num = counter(page).get().first()
    [
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      #v(2pt)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#94a3b8"), font: "Liberation Sans")[Une Pédagogie Constructive & Incarnée],
        text(size: 8.5pt, fill: rgb("#1e293b"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      )
    ]
  }
)

#set text(
  font: ("Linux Libertine", "Times New Roman", "Georgia"),
  size: 9.5pt,
  lang: "fr"
)

#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 1.3em
)

// Palette éditoriale Oliver Byrne
#let c-blue = rgb("#1d4ed8")
#let c-red = rgb("#b91c1c")
#let c-amber = rgb("#d97706")
#let c-dark = rgb("#0f172a")
#let c-green = rgb("#15803d")
#let c-purple = rgb("#7e22ce")

// Blocs didactiques
#let principe(title, body) = block(
  fill: rgb("#f0f9ff"),
  stroke: (left: 4pt + c-blue),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-blue, size: 9pt)[🏛️ PRINCIPE ÉPISTÉMOLOGIQUE : #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

#let alerte(title, body) = block(
  fill: rgb("#fef2f2"),
  stroke: (left: 4pt + c-red),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-red, size: 9pt)[⚠️ VIGILANCE DIDACTIQUE : #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

#let atelier(title, body) = block(
  fill: rgb("#fefce8"),
  stroke: (left: 4pt + c-amber),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-amber, size: 9pt)[🛠️ GESTE DIDACTIQUE & ATELIER : #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

// ==========================================
// COUVERTURE DU GUIDE DE L'ACCOMPAGNATEUR
// ==========================================
#align(center)[
  #v(1.5cm)
  #text(size: 11pt, weight: "bold", fill: c-blue, tracking: 3pt)[MANUEL D'INGÉNIERIE PÉDAGOGIQUE POUR PARENTS ET ENSEIGNANTS]
  #v(0.6cm)
  #text(size: 26pt, weight: "bold", fill: c-dark)[LA VOIE DU NOMBRE]
  #v(0.2cm)
  #text(size: 18pt, weight: "bold", fill: c-purple)[Le Guide de l'Accompagnateur]
  #v(0.2cm)
  #text(size: 11pt, style: "italic", fill: rgb("#475569"))[Fondations Didactiques, Épistémologiques et Clés Pratiques (Du Premier Caillou au Baccalauréat)]
  #v(0.8cm)
  #line(length: 45%, stroke: 2pt + c-amber)
  #v(1cm)
]

#block(
  fill: rgb("#f8fafc"),
  inset: 14pt,
  radius: 6pt,
  stroke: 1pt + rgb("#e2e8f0"),
  [
    #align(center)[
      #text(size: 10pt, style: "italic", fill: rgb("#334155"))[
        « On n'enseigne pas les mathématiques en les versant comme une eau tiède dans un récipient passif. L'enfant ne comprend que ce qu'il a d'abord éprouvé par ses muscles, construit de ses mains, et réinventé pour surmonter une résistance réelle du monde. Mais l'adulte veille à ce que l'outil ne devienne pas une cage, et que le geste s'élève en pure lumière logique. »
      ]
    ]
  ]
)

#v(0.8cm)
#outline(title: [Sommaire Général du Guide], indent: 1.5em, depth: 2)
#pagebreak()

= PARTIE I — LE MOTEUR ÉPISTÉMOLOGIQUE : LES QUATRE PILIERS SCIENTIFIQUES

Pourquoi la collection *La Voie du Nombre* refuse-t-elle le cours magistral classique ? Ce guide dévoile les quatre piliers théoriques qui en régissent la progression.

== 1. Jean Piaget : Stades et Réversibilité Opératoire
Le cerveau humain ne saute pas les étapes de son développement psychomoteur. Plaquer une formule abstraite (stade formel) sur un enfant encore au stade opératoire concret provoque une sidération cognitive.
- *6 - 8 ans (Volume I) :* Manipulation d'objets réels (cailloux, boîtes d'œufs, balance, chocolat).
- *8 - 10 ans (Volume II) :* Conservation de la substance (découpe de galettes, fractions, trous de sable).
- *10 - 14 ans (Volumes III & IV) :* Transition formelle, expériences de pensée, inconnue $x$ comme sac masqué.
- *14 - 18 ans (Volumes V & VI) :* Opérations formelles, flèches libres (vecteurs), machines $f(x)$, complexes $i$, flux continus.

#principe([La Réversibilité Opératoire])[
Un concept n'est solide que si l'apprenant comprend que l'opération inverse restaure exactement l'état initial : l'addition s'éclaire par la soustraction, la multiplication par la division, et la dérivée par l'intégrale.
]

== 2. George Lakoff & Rafael Núñez : Les Métaphores Incarnées
Tous les concepts mathématiques sont forgés par notre perception sensorimotrice :
- *La collection d'objets (Volumes I & II) :* le nombre est un tas de cailloux, l'addition est un empilement.
- *Le déplacement sur un sentier (Volumes II à VI) :* le nombre est un pas de marche. Avancer vers l'Est $= +$, reculer vers l'Ouest $= -$. Se tourner vers l'Ouest ($-1$) et reculer ($-1$) propulse vers l'Est ($+1$) : le cauchemar de $(-1) times (-1) = +1$ s'évanouit d'un seul geste moteur.
- *La machine d'atelier (Volumes V & VI) :* la fonction $f$ est un automate qui transforme une matière première $x$ en produit fini $f(x)$.
- *La loupe infinie (Volume VI) :* toute courbe lisse grossie au microscope devient droite (la Terre ronde semble plate sous la semelle).

== 3. Oliver Byrne (1847) : La Sémiotique Chromatique
Remplacer les lettres abstraites par des couleurs fonctionnelles permet au cortex visuel de valider la preuve en un vingtième de seconde :
- *Bleu Royal (\#1d4ed8) :* L'Action positive, l'Horizontal, l'abscisse $x$, le premier vecteur.
- *Rouge Vermillon (\#b91c1c) :* La Contrainte, la Verticale $y$, la réaction, le diviseur.
- *Jaune Doré (\#d97706) :* Le Produit, l'Aire intérieure, l'Énergie, le reste, le double produit.
- *Vert Émeraude (\#15803d) :* La Validation, le résultat final, la tangente, la somme de Chasles.
- *Noir Profond (\#0f172a) :* Le Squelette de référence, les axes neutres, la grille.

== 4. Guy Brousseau & Gaston Bachelard : L'Obstacle et la Rupture
Une notion nouvelle n'arrive jamais par décret : elle naît de la faillite de l'outil précédent.
L'apprentissage est une succession de crises constructives : l'addition répétée échoue sous l'orage $arrow.r$ naissance de la multiplication ; les entiers échouent à partager 2 poissons entre 4 $arrow.r$ naissance des fractions ; la droite réelle échoue sur $x^2 = -1$ $arrow.r$ naissance du nombre complexe $i$.

#pagebreak()

= PARTIE II — L'AUDIT CRITIQUE INDÉPENDANT : LES TROIS VIGILANCES MAJEURES

Le comité d'évaluation externe en didactique a dégagé trois vigilances absolues pour l'accompagnateur :

== 1. Le Dépassement de l'Obstacle Métaphorique (Bachelard vs Lakoff)
La métaphore corporelle est indispensable pour amorcer l'intuition, mais elle devient un carcan si on ne sait pas s'en libérer :
- *La limite du rectangle :* la multiplication comme surface rectangulaire ($4 times 6 = 24$) s'effondre pour $(-3) times (-5) = +15$ (une aire négative n'existe pas dans le monde sensible). L'accompagnateur doit expliquer que la règle des signes est imposée par la *cohérence algébrique de la distributivité*.
- *La limite du skieur :* la pente de ski suppose une courbe lisse. Elle ne dit rien des points anguleux ($|x|$ en 0) ou des fonctions oscillantes. L'accompagnateur doit guider l'élève du geste physique vers la définition rigoureuse des limites.

== 2. La Mémoire de Travail et les Gammes d'Automatismes
La mémoire de travail ne retient que 4 à 7 éléments (loi de Miller, Sweller).
- Si un lycéen doit réfléchir à $7 times 8 = 56$ au milieu d'un calcul d'intégrale, son cerveau sature et décroche.
- L'accompagnateur veillera donc à ce que les *Fiches de Gammes du Praticien* soient pratiquées avec assiduité : opérations posées, tables, identités remarquables et dérivées usuelles doivent devenir des réflexes médullaires.

== 3. Le Primat du Visuel en Géométrie (Registres de Duval)
L'intelligence géométrique naît de la conversion permanente entre le tracé graphique et la formule algébrique. L'accompagnateur fera toujours tracer les figures avant de poser les équations.

#pagebreak()

= PARTIE III — LA CONDUITE DE L'ATELIER ET LA DOCTRINE DES CAS LIMITES

#alerte([La Règle d'Or des Cas Limites : L'Enclos Isolé])[
Pour ne jamais déstabiliser l'élève dans la phase d'acquisition d'un geste nouveau, les cas pathologiques ($4 times 0$, division par zéro, exposant zéro, vecteur nul) ne doivent *jamais* être introduits dans la première leçon.
Ils sont toujours explorés dans un second temps, dans un espace dédié baptisé *Le Laboratoire des Cas Limites*, comme une énigme d'ingénieur.
]

== 1. Volume I (6 - 8 ans) : La Main, la Balance et le Mur de Briques
- *Opérations posées :* Utiliser la boîte à deux colonnes (Unités/Dizaines). Ne jamais parler de « retenue » sans montrer l'échange physique de 10 petits cailloux contre 1 bouchon.
- *Multiplication posée :* Insister sur le zéro rouge de décalage à l'étage des dizaines ($146 times 23$).
- *Cas limite de zéro :* Montrer que $4 times 0 = 0$ par l'aplatissement du rectangle (zéro est un élément absorbant).

== 2. Volume II (8 - 10 ans) : Le Marché et la Potence de Division
- *La Potence :* Faire mémoriser le cycle rythmé *D-M-S-A* (Diviser, Multiplier, Soustraire, Abaisser).
- *Diviseur à deux chiffres ($7 thin 845 div 23$) :* Enseigner le réflexe du répertoire des multiples au brouillon ($23 times 1, 23 times 2, 23 times 3...$).
- *Le piège du zéro au quotient ($615 div 3 = 205$) :* Marteler que dès qu'on abaisse un chiffre, on DOIT poser un chiffre au quotient.
- *Division par zéro :* Montrer pourquoi $0 div 5 = 0$, mais $5 div 0$ est rigoureusement impossible ($0 times q = 5$ n'a aucune solution).

== 3. Volume IV (12 - 15 ans) : Identités et Inéquations
- *Identités remarquables :* Faire dessiner le grand carré découpé pour conjurer l'oubli du double produit $2 a b$.
- *Inéquations :* Montrer que multiplier par un négatif inverse le sens ($<$ devient $>$) par symétrie autour de zéro.

== 4. Volumes V & VI (15 - 18 ans) : Vecteurs, Flux et Intégrales
- *Produit scalaire :* Montrer la force efficace : la corde du cheval tirant la péniche.
- *Nombres complexes :* Présenter $i$ comme un opérateur géométrique de quart de tour ($90^circle$).
- *Intégrale :* Dériver c'est trancher au scalpel le tonneau de Kepler ; intégrer c'est recoudre au fil d'or.

#pagebreak()

= PARTIE IV — LE PONT AVEC LE PROGRAMME OFFICIEL ET LES EXAMENS

Pour décrocher la mention Très Bien au Baccalauréat, l'accompagnateur veillera au respect strict des liturgies d'examen :
1. *Récurrence (Terminale) :* Initialisation claire, formulation rituelle de l'hypothèse de récurrence pour un entier fixé $n$, conclusion solennelle.
2. *Théorème des Valeurs Intermédiaires (TVI) :* Vérifier les 3 conditions : fonction continue, strictement monotone, valeur cible encadrée.
3. *Rédaction vectorielle :* Flèches obligatoires ($arrow(u), arrow(A B)$), distinction nette entre direction (droite) et sens (orientation).

= BIBLIOGRAPHIE PATRIMONIALE DE RÉFÉRENCE

1. *Gaston Bachelard*, La Formation de l'esprit scientifique (1938).
2. *Guy Brousseau*, Théorie des situations didactiques en mathématiques (1998).
3. *Oliver Byrne*, The First Six Books of the Elements of Euclid (Londres, 1847).
4. *Michel Chasles*, Aperçu historique sur l'origine et le développement des méthodes en géométrie (1837).
5. *Raymond Duval*, Sémiosis et pensée humaine (1995).
6. *George Lakoff & Rafael Núñez*, Where Mathematics Comes From (2000).
7. *Jean Piaget*, L'Épistémologie génétique (1970).
8. *Simon Stevin*, De Thiende / La Disme (Leyde, 1585).
9. *Al-Khwarizmi*, Abrégé du calcul par la restauration et la comparaison (Bagdad, v. 820).
