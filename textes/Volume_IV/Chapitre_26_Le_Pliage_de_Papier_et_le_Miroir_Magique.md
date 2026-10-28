# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 26 : Le Pliage de Papier et le Miroir Magique

> *« Regarde une goutte d'eau qui tombe dans un lac, les ailes d'un papillon qui s'ouvrent au soleil ou le visage de ton ami : la nature ne choisit jamais ses formes au hasard. Elle construit dans le miroir de la symétrie, car ce qui est symétrique partage la force, équilibre les masses et résiste à la tempête. »*

---

### Ce que tu vas découvrir

- Le secret des bâtisseurs médiévaux : pourquoi l'asymétrie détruit les ponts et comment la **médiatrice** et la **bissectrice** créent l'harmonie.
- La grande famille des transformations géométriques :
  - La **symétrie axiale** : le pliage de la feuille et le reflet du miroir.
  - La **symétrie centrale** : le demi-tour parfait autour d'un pivot.
  - La **translation** : le glissement rectiligne sans la moindre rotation.
  - La **rotation** : le tourbillon d'un angle donné autour d'un centre.
  - L'**homothétie** : la caméra zoom qui rétrécit ou agrandit le monde d'un rapport $k$.
- Les trésors que ces transformations **conservent** : longueurs, angles, parallélisme et aires.
- La distinction cruciale entre **triangles égaux** (superposables) et **triangles semblables** (de même silhouette).
- L'art fascinant des **frises et des pavages** : des arabesques de l'Alhambra de Grenade aux métamorphoses impossibles de Maurits Cornelis Escher.

---

### 1. Le problème : le pont qui s'écroule et la dispute du puits

Au XIIᵉ siècle, dans une vallée encaissée d'Auvergne, les habitants décident de construire un grand pont de pierre au-dessus d'une gorge tumultueuse. Le maître maçon est pressé : il taille des claveaux inégaux et monte une arche légèrement penchée vers la droite, plus pesante d'un côté que de l'autre. L'arche est pittoresque, mais bancale.

Quelques mois plus tard survient la première crue d'automne. Le torrent rugit, le vent s'engouffre dans la faille. Le côté le plus massif tire sur le flanc le plus mince. Une fissure serpentine apparaît dans la voûte... et dans un vacarme assourdissant de roches broyées, **le pont s'effondre dans le gouffre** !

```
              Arche penchée (instable)               Arche symétrique (éternelle)
                     /\                                     /¯¯\
                    /  \___                                /    \
                   /       \                              /      \
               ───┴─────────┴───                      ───┴────────┴───
               Forces déséquilibrées                  Forces partagées
```

Le vieux maître bâtisseur réunit ses apprentis autour de sa table à dessin :
*« Gravez ceci dans votre mémoire : la pierre pardonne les aspérités de surface, mais elle ne pardonne jamais l'asymétrie. Quand une arche ne possède pas son axe miroir, le poids du ciel s'abat sur un seul pied, et la ruine est certaine. »*

Quelques lieues plus loin, une autre querelle agite deux villages voisins, Arras et Béthune, séparés par six kilomètres de lande herbeuse. Le comte décide de creuser un grand puits en pierre dans la plaine pour abreuver bêtes et gens.

Aussitôt, la discorde éclate :
*« Creusez le puits tout près de notre clocher ! »* exigent les gens d'Arras.
*« Hors de question ! »* répliquent ceux de Béthune. *« Ce serait du favoritisme ! Nous voulons que la marche soit rigoureusement égale pour chaque village ! »*

Un enfant propose : *« Creusons le puits pile au milieu du sentier qui relie les deux villages ! »*
C'est une bonne idée : à 3 kilomètres d'Arras et 3 kilomètres de Béthune, l'endroit est juste.
Mais le géomètre de la commanderie s'avance et trace un grand sillon dans la terre avec une pique :
*« Il n'y a pas un seul emplacement possible : il y a une infinité de places pour le puits ! »*

```
                           Axe de la Médiatrice (d)
                                     ▲
                                     │  Puits possible 1 (Équidistant !)
                                     ●
                                   / │ \
                                 /   │   \
                               /     │     \
         Village A o───────────┼─────o─────┼───────────o Village B
        (Arras)                │  Milieu   │           (Béthune)
                               \     │     /
                                 \   │   /
                                   \ │ /
                                     ●  Puits possible 2 (Équidistant !)
                                     │
```

Cette ligne droite perpendiculaire qui coupe le chemin en son milieu possède une propriété magique : **chaque point de cette droite est situé à une distance strictement égale du village A et du village B**. 
Cette ligne d'équité parfaite s'appelle **la médiatrice**.

Pour maîtriser l'architecture, l'art et les machines, nous devons comprendre les lois qui régissent les mouvements du plan : les **transformations géométriques**.

---

### 2. Les deux miroirs : Symétrie axiale et Symétrie centrale

Une **transformation géométrique** est une opération qui déplace chaque point du plan vers une nouvelle position selon une consigne précise. Le point de départ s'appelle le point initial $M$, et le point d'arrivée s'appelle son **image** $M'$.

#### 2.1 La symétrie axiale : le pliage le long d'une droite

Prends une feuille de papier, dépose une goutte d'encre fraîche sur la gauche, plie la feuille en deux le long d'un trait droit $(d)$ et appuie fermement. En rouvrant, la tache s'est imprimée de l'autre côté.

> **📐 Définition — Symétrie axiale (par rapport à une droite $(d)$).**
> - L'image d'un point $M$ situé en dehors de $(d)$ est le point $M'$ tel que la droite $(d)$ soit la **médiatrice** du segment $[M M']$.
>   Cela signifie que $(d)$ est perpendiculaire à $[M M']$ et le coupe en son milieu.
> - Si un point $M$ est situé directement sur la droite $(d)$, son image est lui-même : $M' = M$ (on dit que $M$ est un **point invariant**).

```
                      M ●
                         \
                          \  (d) Axe de symétrie
                           \  │
                            \ │
                             \┼─ Angle droit
                              │\  Distance = Distance
                              │ \
                              │  \
                                  ● M'
```

*Effet miroir :* La symétrie axiale inverse l'orientation ! Ta main droite devient une main gauche dans le miroir. Si un triangle tourne dans le sens des aiguilles d'une montre ($A \to B \to C$), son image par symétrie axiale tournera dans le sens inverse.

#### 2.2 La symétrie centrale : le demi-tour autour d'un pivot

Imagine maintenant que tu plantes une punaise sur ta feuille au point $O$, et que tu fasses tourner ton calque d'un **demi-tour exact ($180^\circ$)**.

> **📐 Définition — Symétrie centrale (par rapport à un centre $O$).**
> L'image d'un point $M$ par la symétrie centrale de centre $O$ est le point $M'$ tel que **le point $O$ soit le milieu du segment $[M M']$**.

```
                M ●───────────────o───────────────● M'
                         OM   =   O   =   OM'
```

*Propriété essentielle :*
Une symétrie centrale transforme n'importe quelle droite $(d)$ en une droite $(d')$ qui lui est **strictement parallèle** ! Elle n'inverse pas le sens d'orientation (une boucle horaire reste horaire après un demi-tour).

---

### 3. Les deux mouvements rigides : Translation et Rotation

#### 3.1 La translation : le glissement parfait

Imagine un tiroir que l'on tire, ou un train qui file sur des rails parfaitement droits. Chaque point de l'objet avance de la même distance, dans la même direction, et dans le même sens.

> **📐 Définition — Translation.**
> Une **translation** fait glisser une figure d'un point $A$ vers un point $B$.
> L'image de n'importe quel point $M$ est le point $M'$ tel que :
> 1. Les droites $(A B)$ et $(M M')$ sont **parallèles** (même direction).
> 2. On va de $M$ vers $M'$ dans le **même sens** que de $A$ vers $B$.
> 3. La longueur $M M' = A B$ (même distance).
> 
> *En un mot :* Le quadrilatère $A B M' M$ est un **parallélogramme** (éventuellement aplati).

```
                 A ●────────────────────────────>● B
                          (Vecteur de glissement)
                 
                 M ●────────────────────────────>● M'
```

Dans une translation, la figure glisse sans tourner d'un quart de poil. C'est le mouvement typique des pas d'un promeneur dans le sable.

#### 3.2 La rotation : le tourbillon contrôlé

Pense à l'aiguille d'une horloge, à une pale d'éolienne, ou aux nacelles d'une grande roue de fête foraine.

> **📐 Définition — Rotation.**
> Une **rotation** est définie par trois éléments inséparables :
> 1. Un point fixe appelé le **centre de rotation** $O$.
> 2. Un **angle** de rotation $\alpha$ (en degrés).
> 3. Un **sens de rotation** :
>    - soit le **sens horaire** (sens des aiguilles d'une montre) ;
>    - soit le **sens antihoraire** (sens trigonométrique, inverse des aiguilles).
> 
> L'image d'un point $M$ par la rotation de centre $O$ et d'angle $\alpha$ est le point $M'$ tel que :
> - $O M = O M'$ (le point reste sur le même cercle de rayon $O M$) ;
> - L'angle $\widehat{M O M'} = \alpha$.

```
                              M' ●
                                /
                               /   Angle α
                              / ∡ 
                             /     \
                            /       \
                        O  ●─────────● M
                             OM = OM'
```

*Remarque éclatante :* Une rotation d'angle $180^\circ$ n'est rien d'autre qu'une **symétrie centrale** !

---

### 4. L'effet de zoom : l'Homothétie

Toutes les transformations précédentes (symétries, translation, rotation) déplaçaient les figures sans jamais modifier leur gabarit. On les appelle des **isométries** (du grec *isos*, égal, et *metron*, mesure).

L'**homothétie** (du grec *homoios*, semblable, et *thesis*, disposition) est d'une nature différente : c'est un **effet de zoom optique**. Elle agrandit ou rétrécit la figure à partir d'un centre projecteur.

#### 4.1 Définition et rapport $k$

> **📐 Définition — Homothétie.**
> Une homothétie est définie par :
> 1. Un point fixe appelé le **centre** $O$.
> 2. Un nombre non nul appelé le **rapport** $k$.
> 
> L'image d'un point $M$ est le point $M'$ situé sur la droite $(O M)$ tel que :
> - La distance $O M' = |k| \times O M$.
> - **Si $k > 0$ :** le point $M'$ se trouve sur la demi-droite $[O M)$ (du même côté de $O$ que $M$).
> - **Si $k < 0$ :** le point $M'$ se trouve de l'autre côté de $O$ (sur la demi-droite opposée). Cela produit un zoom combiné à un demi-tour !

```
     k > 0 (Zoom avant k = 2) :
     O ●──────────────● M ────────────────────────────● M'
            OM                     OM' = 2 × OM
     
     k < 0 (Inversion k = -1,5) :
     M' ●─────────────────────────● O ──────────────● M
          OM' = 1,5 × OM
```

#### 4.2 Les effets d'échelle du rapport $k$
- Si $|k| > 1$ : c'est un **agrandissement**.
- Si $0 < |k| < 1$ : c'est une **réduction**.
- Si $k = 1$ : la figure ne bouge pas (homothétie identité).
- Si $k = -1$ : l'homothétie est identique à la **symétrie centrale de centre $O$** !

#### 4.3 L'effet ravageur sur les aires et les volumes

C'est l'un des pièges les plus récurrents du brevet et du lycée :
- Quand on applique une homothétie de rapport $k$, **toutes les longueurs sont multipliées par $|k|$**.
- **Mais l'aire d'une surface est multipliée par $k^2$ !**
- **Et le volume d'un solide est multiplié par $|k|^3$ !**

*Exemple frappant :* Si tu agrandis une maquette d'un rapport $k = 3$ :
- Sa hauteur est multipliée par 3.
- La peinture pour peindre sa façade est multipliée par $3^2 = 9$.
- Son poids de métal est multiplié par $3^3 = 27$ !

---

### 5. Ce que les transformations conservent : le code génétique des formes

| Transformation | Longueurs | Angles | Parallélisme | Alignement | Aires | Orientation |
|---|---|---|---|---|---|---|
| **Symétrie axiale** | Conservées | Conservés | Conservé | Conservé | Conservée | **Inversée** (miroir) |
| **Symétrie centrale** | Conservées | Conservés | Conservé | Conservé | Conservée | Conservée |
| **Translation** | Conservées | Conservés | Conservé | Conservé | Conservée | Conservée |
| **Rotation** | Conservées | Conservés | Conservé | Conservé | Conservée | Conservée |
| **Homothétie (rapport $k$)** | $\times |k|$ | **Conservés** | Conservé | Conservé | $\times k^2$ | Conservée si $k>0$ |

Retiens ce principe fondamental : **toutes les transformations du collège conservent scrupuleusement la mesure des angles, le parallélisme et l'alignement des points**.

---

### 6. Triangles égaux et Triangles semblables

#### 6.1 Les triangles égaux (isométriques) : des clones parfaits

Deux triangles sont dits **égaux** (ou isométriques) lorsqu'ils sont parfaitement **superposables**, par glissement, rotation ou retournement miroir. Leurs côtés homologues ont rigoureusement la même longueur et leurs angles correspondants ont la même mesure.

Pour prouver que deux triangles sont égaux, pas besoin de mesurer les 6 éléments (3 côtés et 3 angles) ! Trois suffisent, selon **les trois cas d'égalité** :

1. **Cas C-C-C (Côté-Côté-Côté) :**
   Les trois côtés de l'un sont respectivement égaux aux trois côtés de l'autre.
2. **Cas C-A-C (Côté-Angle-Côté) :**
   Deux côtés de l'un sont égaux à deux côtés de l'autre, et **l'angle compris entre ces deux côtés** a la même mesure.
3. **Cas A-C-A (Angle-Côté-Angle) :**
   Un côté de l'un est égal à un côté de l'autre, et **les deux angles adjacents à ce côté** ont les mêmes mesures.

```
       Cas C-A-C :
             /|                                  /|
          b / |                               b / |
           /  | a                              /  | a
          /__θ|                               /__θ|
            c                                   c
```

#### 6.2 Les triangles semblables : la même silhouette à une échelle différente

Deux triangles sont dits **semblables** lorsqu'ils ont exactement **la même forme**, mais pas nécessairement la même taille. L'un est un agrandissement ou une réduction de l'autre.

> **📐 Définition — Triangles semblables.**
> Deux triangles sont semblables si :
> - Leurs **angles sont deux à deux de même mesure** ;
> - **OU** les longueurs de leurs côtés sont **deux à deux proportionnelles** :
>   $$\frac{A'B'}{AB} = \frac{B'C'}{BC} = \frac{A'C'}{AC} = k.$$

*Théorème d'économie :*
Puisque la somme des angles d'un triangle vaut toujours $180^\circ$ (Chapitre 15), dès que **deux angles d'un triangle sont égaux à deux angles d'un autre triangle**, le troisième est obligatoirement égal, et **les deux triangles sont immédiatement semblables** !

---

### 7. Les droites de justice : Médiatrice et Bissectrice

Ces deux droites remarquables sont fondées sur la symétrie axiale :

#### 7.1 La médiatrice d'un segment
- **Définition :** C'est la droite perpendiculaire au segment en son milieu.
- **Propriété caractéristique :** Un point appartient à la médiatrice d'un segment $[AB]$ si et seulement si il est à égale distance des deux extrémités :
  $$M \in \text{Médiatrice de } [AB] \iff MA = MB.$$
- **Le cercle circonscrit :** Les médiatrices des trois côtés d'un triangle se coupent en un point unique, le **centre du cercle circonscrit**, qui passe par les trois sommets du triangle.

#### 7.2 La bissectrice d'un angle
- **Définition :** C'est la demi-droite qui partage un angle en deux angles adjacents de même mesure. C'est l'**axe de symétrie** de l'angle.
- **Propriété caractéristique :** Tout point de la bissectrice est situé à égale distance des deux côtés de l'angle.
- **Le cercle inscrit :** Les bissectrices des trois angles d'un triangle se coupent au **centre du cercle inscrit**, qui touche tangentiellement les trois côtés du triangle à l'intérieur.

---

### 8. L'art des frises, des pavages et le génie d'Escher

Quand la géométrie des transformations rencontre l'art, le résultat touche au sublime.

#### 8.1 Qu'est-ce qu'un pavage ?
Un **pavage** est un recouvrement complet du plan par des formes géométriques jointives, sans laisser le moindre interstice vide et sans qu'aucune forme ne chevauche sa voisine.
- Une **frise** est un pavage dans une seule direction (une bande linéaire décorative le long d'un mur). Elle utilise principalement des translations répétées d'un même pas horizontal, parfois combinées à des symétries axiales ou des demi-tours.
- Un **pavage du plan** s'étend dans les deux dimensions à l'infini.

#### 8.2 Les mosaïques de l'Alhambra de Grenade
Au XIVᵉ siècle, les artistes mauvaises de l'Alhambra, soumis à l'interdiction religieuse de représenter des figures vivantes, ont exploré les mathématiques des symétries avec une virtuosité stupéfiante.
Les mathématiciens ont démontré des siècles plus tard qu'il n'existe rigoureusement que **17 types de pavages périodiques possibles dans tout le plan** (les 17 groupes de papier peint). Les artisans de Grenade les avaient **tous découverts empiriquement** sur les faïences (*azulejos*) de leur palais !

#### 8.3 Les métamorphoses de Maurits Cornelis Escher
En 1936, l'artiste néerlandais M. C. Escher visite l'Alhambra et est bouleversé par ces mosaïques. Il consacre ensuite sa vie à remplacer les polygones abstraits par des créatures vivantes : oiseaux, poissons, salamandres, anges et démons.

Comment fabrique-t-il un lézard qui s'emboîte parfaitement avec ses frères ?
1. Il part d'un carré ou d'un parallélogramme qui pave naturellement le plan.
2. Il découpe un morceau sur le bord gauche et le **translate** sur le bord droit.
3. Il découpe un morceau sur le bord inférieur et lui fait subir une **rotation** de $90^\circ$ pour former la patte supérieure.
Puisque la matière retirée d'un côté est exactement restituée de l'autre, la surface de la figure reste inchangée et les motifs s'imbriquent à l'infini avec une perfection absolue !

```
              ┌───┐                  ┌───┐
     Découpe  │   │  Translation     │   │ ───► Recolle
     à gauche └───┘                  └───┘      à droite
        \_____/                         \_____/
```

---

### 9. Exemples résolus pas à pas

#### Exemple 1 : Image par rotation
Soit un triangle équilatéral $ABC$ de sens direct (sens antihoraire). On désigne par $O$ le centre du cercle circonscrit à ce triangle.
1. Quelle est l'image du point $A$ par la rotation de centre $O$ et d'angle $120^\circ$ dans le sens antihoraire ?
2. Quelle est l'image du segment $[AB]$ par cette rotation ?

**Résolution détaillée :**
1. Dans un triangle équilatéral, le centre $O$ partage le tour complet de $360^\circ$ en trois angles au centre égaux :
   $$\widehat{AOB} = \widehat{BOC} = \widehat{COA} = \frac{360^\circ}{3} = 120^\circ.$$
   De plus, par définition du cercle circonscrit, $OA = OB = OC$.
   La rotation de centre $O$ et d'angle $120^\circ$ antihoraire envoie donc le point $A$ sur le point $B$, et le point $B$ sur le point $C$.
   L'image de $A$ est donc $B$.
2. Une rotation conserve les segments. L'image de $A$ étant $B$, et l'image de $B$ étant $C$, l'image du segment $[AB]$ est le segment $[BC]$.

---

#### Exemple 2 : Calcul avec une homothétie et ses effets d'aire
Un trapèze d'aire $12 \text{ cm}^2$ subit une homothétie de rapport $k = -2{,}5$.
1. Quelle est la nature de la figure obtenue ?
2. L'orientation est-elle inversée ?
3. Quelle est l'aire du trapèze agrandi ?

**Résolution détaillée :**
1. L'homothétie conserve la nature des figures et le parallélisme : l'image d'un trapèze est un **trapèze**.
2. Le rapport $k = -2{,}5$ est négatif : la figure subit donc un demi-tour ($180^\circ$) par rapport au centre de l'homothétie, mais elle conserve son orientation globale (contrairement à une symétrie axiale).
3. L'aire est multipliée par $k^2$ :
   $$\text{Aire}' = k^2 \times \text{Aire} = (-2{,}5)^2 \times 12 = 6{,}25 \times 12 = 75 \text{ cm}^2.$$
   L'aire du nouveau trapèze est de $75 \text{ cm}^2$.

---

#### Exemple 3 : Démontrer que deux triangles sont semblables
Dans un cercle de centre $O$, on trace deux diamètres distincts $[AB]$ et $[CD]$.
Démontrer que les triangles $AOC$ et $BOD$ sont égaux, puis qu'ils sont semblables.

**Résolution détaillée :**
1. Les points $A, B$ et $C, D$ étant les extrémités de deux diamètres passant par $O$, le point $O$ est le milieu commun de $[AB]$ et de $[CD]$.
2. Par conséquent :
   - La symétrie centrale de centre $O$ transforme le point $A$ en $B$ (car $O$ milieu de $[AB]$).
   - Elle transforme le point $C$ en $D$ (car $O$ milieu de $[CD]$).
3. L'image du triangle $AOC$ par la symétrie centrale de centre $O$ est donc le triangle $BOD$.
4. Puisque la symétrie centrale est une isométrie (elle conserve scrupuleusement les longueurs des côtés et les angles), **les triangles $AOC$ et $BOD$ sont égaux**.
5. Deux triangles égaux ayant leurs côtés de même longueur ($k = 1$), ils sont en particulier **semblables** de rapport $1$.

---

#### Exemple 4 : Utiliser les triangles semblables pour calculer une longueur inaccessible
Deux mâts verticaux $[AB]$ et $[DE]$ sont plantés sur un sol plat horizontal.
Le mât $[AB]$ mesure 2 mètres de haut. À une certaine heure, son ombre au sol mesure 3,5 mètres.
Au même instant, l'ombre du grand mât $[DE]$ mesure 14 mètres.
Calculer la hauteur du grand mât $[DE]$.

**Résolution détaillée :**
1. Les rayons du soleil étant considérés comme parallèles entre eux au même instant, les angles formés par les rayons avec le sol horizontal sont identiques.
2. Les deux mâts étant verticaux, ils forment tous deux un angle droit avec le sol ($90^\circ$).
3. Les triangles rectangles formés par les mâts et leurs ombres possèdent donc deux angles de même mesure : ils sont **semblables**.
4. Leurs côtés homologues sont donc proportionnels :
   $$\frac{\text{Hauteur grand mât } DE}{\text{Hauteur petit mât } AB} = \frac{\text{Ombre grande}}{\text{Ombre petite}}.$$
   $$\frac{DE}{2} = \frac{14}{3{,}5}.$$
5. On calcule le coefficient d'agrandissement :
   $$k = \frac{14}{3{,}5} = 4.$$
6. La hauteur du mât est donc :
   $$DE = 2 \times 4 = 8 \text{ mètres}.$$

---

#### Exemple 5 : Construction de la médiatrice au compas seul
Expliquer et justifier la méthode classique pour tracer la médiatrice d'un segment $[AB]$ à l'aide d'une règle non graduée et d'un compas.

**Résolution détaillée :**
1. On écarte le compas d'un rayon $R$ strictement supérieur à la moitié de $AB$ ($R > \frac{AB}{2}$).
2. En piquant en $A$, on trace deux arcs de cercle, l'un au-dessus, l'autre en dessous de $[AB]$.
3. Sans changer l'écartement du compas, on pique en $B$ et on coupe les arcs précédents en deux points $P$ et $Q$.
4. On trace la droite $(PQ)$ à la règle.
5. **Justification rigoureuse :**
   - Par construction, $PA = PB = R$ : le point $P$ est équidistant de $A$ et de $B$, donc $P$ appartient à la médiatrice de $[AB]$.
   - De même, $QA = QB = R$ : le point $Q$ est équidistant de $A$ et de $B$, donc $Q$ appartient aussi à la médiatrice de $[AB]$.
   - Deux points distincts définissant une unique droite, la droite $(PQ)$ est très exactement la médiatrice du segment $[AB]$.

---

### Ce qu'il faut retenir

1. **Les 5 transformations géométriques :**
   - **Symétrie axiale :** pliage par rapport à une droite $(d)$ (médiatrice). Inverse l'orientation.
   - **Symétrie centrale :** demi-tour de $180^\circ$ autour d'un centre $O$ (milieu).
   - **Translation :** glissement sans tourner selon une direction, un sens et une longueur (parallélogramme).
   - **Rotation :** pivotement d'un angle $\alpha$ autour d'un centre $O$ dans un sens donné.
   - **Homothétie :** zoom d'un rapport $k$ à partir d'un centre $O$ ($OM' = |k| \times OM$).
2. **Conservations :**
   - Toutes les transformations conservent les angles, l'alignement et le parallélisme.
   - Les quatre premières (isométries) conservent les distances et les aires.
   - L'homothétie multiplie les longueurs par $|k|$ et les aires par $k^2$.
3. **Triangles égaux :**
   Triangles superposables. Côtés de même longueur deux à deux et angles de même mesure deux à deux (cas CCC, CAC, ACA).
4. **Triangles semblables :**
   Triangles de même forme : angles deux à deux égaux et côtés deux à deux proportionnels. Deux angles égaux suffisent à garantir qu'ils sont semblables.
5. **Médiatrice et Bissectrice :**
   - Médiatrice : perpendiculaire au milieu d'un segment, équidistante des extrémités, centre du cercle circonscrit.
   - Bissectrice : partage un angle en deux parts égales, équidistante des côtés, centre du cercle inscrit.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 26.1** Identifier les transformations :
Associer chaque situation de la vie courante à la transformation géométrique correspondante :
1. Une cabine de grande roue en mouvement.
2. Le reflet d'un arbre dans l'eau calme d'un lac.
3. Un train sur une voie rectiligne.
4. L'image projetée sur l'écran d'un cinéma par rapport à la pellicule du projecteur.
5. Une carte à jouer (la reine de cœur) posée sur la table avec son double tête-bêche.

**Exercice 26.2** Propriétés d'une symétrie axiale :
Soit un segment $[AB]$ de longueur 6 cm et un angle $\widehat{BAC} = 45^\circ$.
On applique une symétrie axiale d'axe $(d)$. On note $A', B', C'$ les images respectives de $A, B, C$.
1. Quelle est la longueur du segment $[A'B']$ ? Justifier.
2. Quelle est la mesure de l'angle $\widehat{B'A'C'}$ ? Justifier.

**Exercice 26.3** Translation et parallélogramme :
Soit $M'$ l'image de $M$ par la translation qui transforme $A$ en $B$.
1. Quelle est la nature exacte du quadrilatère $ABM'M$ ?
2. Si $AB = 7 \text{ cm}$, que vaut la distance $MM'$ ?

**Exercice 26.4** Calculs avec l'homothétie :
Un triangle $ABC$ a un périmètre de 18 cm et une aire de $14 \text{ cm}^2$.
On applique une homothétie de rapport $k = 3$.
1. Quel est le périmètre du triangle agrandi ?
2. Quelle est l'aire du triangle agrandi ?

**Exercice 26.5** Reconnaître des triangles égaux :
Dans un triangle $ABC$, on a $AB = 5 \text{ cm}$, $AC = 7 \text{ cm}$ et $\widehat{BAC} = 40^\circ$.
Dans un triangle $DEF$, on a $DE = 5 \text{ cm}$, $DF = 7 \text{ cm}$ et $\widehat{EDF} = 40^\circ$.
Les triangles $ABC$ et $DEF$ sont-ils égaux ? Quel critère permet de l'affirmer ?

---

#### Niveau ★★ : Réflexion et enchaînements

**Exercice 26.6** Composition de symétries :
Soit deux droites sécantes $(d_1)$ et $(d_2)$ perpendiculaires en un point $O$.
On applique à une figure la symétrie axiale d'axe $(d_1)$, puis à la figure obtenue la symétrie axiale d'axe $(d_2)$.
Démontrer que l'enchaînement de ces deux symétries axiales équivaut à une seule transformation géométrique simple que l'on précisera.

**Exercice 26.7** Triangles semblables et calcul d'angle :
Soit un triangle $ABC$ tel que $\widehat{A} = 65^\circ$ et $\widehat{B} = 45^\circ$.
Soit un triangle $RST$ tel que $\widehat{R} = 65^\circ$ et $\widehat{T} = 70^\circ$.
Les triangles $ABC$ et $RST$ sont-ils semblables ? Justifier avec soin.

**Exercice 26.8** Le problème de l'arbre et du miroir :
Pour mesurer la hauteur d'un arbre inaccessible, Arthur dépose un petit miroir plat sur le sol horizontal au point $M$, à 12 mètres du pied de l'arbre $P$.
Il recule ensuite de 2 mètres jusqu'au point $A$, où il aperçoit dans le miroir le sommet $S$ de l'arbre.
Les yeux d'Arthur sont situés à 1,60 mètre du sol.
La loi de l'optique stipule que l'angle d'incidence est égal à l'angle de réflexion : $\widehat{SMA} = \widehat{PMS}$.
1. Justifier que les triangles formés par Arthur et par l'arbre sont semblables.
2. Calculer la hauteur de l'arbre.

**Exercice 26.9** Homothétie négative :
Sur une droite graduée, le centre de l'homothétie $O$ a pour abscisse 0. Le point $A$ a pour abscisse 3.
Le rapport de l'homothétie est $k = -2$.
1. Quelle est l'abscisse de l'image $A'$ ?
2. Où se situe le point $O$ par rapport au segment $[AA']$ ?

**Exercice 26.10** Le secret de la médiatrice :
Soit un cercle de centre $O$ et une corde $[AB]$ qui ne passe pas par $O$.
1. Démontrer que le point $O$ appartient à la médiatrice du segment $[AB]$.
2. En déduire que la droite qui passe par le centre d'un cercle et qui coupe une corde perpendiculairement passe obligatoirement par le milieu de cette corde.

**Exercice 26.11** Frise par translation :
Une frise est construite à partir d'un motif de base de largeur 4 cm.
On applique successivement une translation de vecteur horizontal de 4 cm vers la droite.
1. Combien de motifs complets composent une frise de 1,20 m de long ?
2. Si le motif de base a une aire de $15 \text{ cm}^2$, quelle est l'aire totale de la frise peinte ?

---

#### Niveau ★★★ : Défis et recherche

**Exercice 26.12** Le billard mathématique :
Sur une table de billard rectangulaire sans poches, une bille blanche est située au point $A$ et une bille rouge au point $B$.
Le joueur doit frapper la bille $A$ pour qu'elle rebondisse sur la bande supérieure $(d)$ avant d'aller heurter la bille $B$.
1. En utilisant le symétrique $B'$ du point $B$ par rapport à la droite $(d)$, déterminer géométriquement l'endroit exact $P$ de la bande que la bille $A$ doit viser.
2. Démontrer que ce point $P$ est celui qui minimise la longueur totale du trajet $AP + PB$ (trajet le plus court possible).

**Exercice 26.13** Triangles semblables imbriqués dans un triangle rectangle :
Soit un triangle $ABC$ rectangle en $A$. Soit $H$ le pied de la hauteur issue de $A$ sur l'hypoténuse $[BC]$.
1. Démontrer que les trois triangles $ABC$, $HBA$ et $HAC$ sont tous semblables entre eux.
2. En écrivant les rapports de proportionnalité des côtés entre $HBA$ et $HAC$, démontrer la célèbre relation :
   $$AH^2 = HB \times HC.$$
3. Application numérique : si $HB = 4 \text{ cm}$ et $HC = 9 \text{ cm}$, calculer la hauteur $AH$.

**Exercice 26.14** Le paradoxe de l'échiquier d'Ozanam (perte d'aire) :
On découpe un carré de $8 \times 8 = 64$ carreaux en quatre pièces polygonales (deux triangles rectangles de côtés de l'angle droit 3 et 8, et deux trapèzes de bases 5 et 3 et de hauteur 5).
En réassemblant ces quatre pièces, on semble former un rectangle de dimensions $5 \times 13 = 65$ carreaux !
D'où vient ce carreau magique apparu de nulle part ($65 - 64 = 1$) ?
*Indication : calculer les pentes des hypoténuses des pièces avec les triangles semblables.*

---

### Solutions

#### Niveau ★

**Solution 26.1**
1. Cabine de grande roue : **Translation circulaire** (la cabine reste toujours verticale sans tourner sur elle-même).
2. Reflet d'arbre dans l'eau : **Symétrie axiale** (d'axe la surface de l'eau).
3. Train sur voie rectiligne : **Translation**.
4. Projecteur de cinéma : **Homothétie** (agrandissement de centre l'objectif).
5. Reine de cœur tête-bêche : **Symétrie centrale** (demi-tour autour du centre de la carte).

**Solution 26.2**
1. $A'B' = 6 \text{ cm}$. En effet, la symétrie axiale est une isométrie : elle conserve scrupuleusement les longueurs.
2. $\widehat{B'A'C'} = 45^\circ$. La symétrie axiale conserve également la mesure des angles.

**Solution 26.3**
1. Par définition de la translation transformant $A$ en $B$, le quadrilatère $ABM'M$ est un **parallélogramme**.
2. Dans un parallélogramme, les côtés opposés ont la même longueur. Donc $MM' = AB = 7 \text{ cm}$.

**Solution 26.4**
1. Les longueurs sont multipliées par $k = 3$. Le nouveau périmètre est :
   $$\text{Périmètre}' = 3 \times 18 = 54 \text{ cm}.$$
2. Les aires sont multipliées par $k^2 = 3^2 = 9$. La nouvelle aire est :
   $$\text{Aire}' = 9 \times 14 = 126 \text{ cm}^2.$$

**Solution 26.5**
Oui, les triangles $ABC$ et $DEF$ sont égaux. 
Le critère appliqué est le cas **C-A-C (Côté-Angle-Côté)** : ils possèdent deux côtés de même longueur ($5 \text{ cm}$ et $7 \text{ cm}$) et l'angle compris entre ces deux côtés a la même mesure ($40^\circ$).

---

#### Niveau ★★

**Solution 26.6**
Soit $M$ un point du plan.
La symétrie axiale par rapport à $(d_1)$ envoie $M$ sur $M_1$, et la symétrie d'axe $(d_2)$ envoie $M_1$ sur $M'$.
Puisque $(d_1) \perp (d_2)$, le triangle formé par les projections montre que $O$ est le milieu du segment $[MM']$ et que l'angle $\widehat{MOM'} = 180^\circ$.
L'enchaînement de deux symétries d'axes perpendiculaires équivaut à **la symétrie centrale de centre $O$** (ou rotation d'angle $180^\circ$ de centre $O$).

**Solution 26.7**
Dans le triangle $ABC$, la somme des angles vaut $180^\circ$ :
$$\widehat{C} = 180^\circ - (65^\circ + 45^\circ) = 180^\circ - 110^\circ = 70^\circ.$$
Les trois angles du triangle $ABC$ mesurent donc $65^\circ, 45^\circ$ et $70^\circ$.
Dans le triangle $RST$ : $\widehat{R} = 65^\circ$, $\widehat{T} = 70^\circ$, donc le troisième angle mesure :
$$\widehat{S} = 180^\circ - (65^\circ + 70^\circ) = 180^\circ - 135^\circ = 45^\circ.$$
Les deux triangles ont leurs trois angles de même mesure deux à deux : **ils sont donc rigoureusement semblables**.

**Solution 26.8**
1. Le triangle Arthur-sol-miroir et le triangle arbre-sol-miroir possèdent chacun un angle droit ($90^\circ$, verticalité) et un angle aigu égal au point de réflexion $M$ ($\widehat{SMA} = \widehat{PMS}$). Ayant deux angles égaux, ils sont **semblables**.
2. Rapport de proportionnalité :
   $$\frac{\text{Hauteur arbre}}{\text{Hauteur yeux Arthur}} = \frac{\text{Distance miroir-arbre}}{\text{Distance miroir-Arthur}}.$$
   $$\frac{h}{1{,}60} = \frac{12}{2} = 6.$$
   $$h = 1{,}60 \times 6 = 9{,}60 \text{ mètres}.$$
   L'arbre mesure 9,60 mètres de haut.

**Solution 26.9**
1. Par définition de l'homothétie de rapport $k = -2$, l'abscisse de $A'$ est :
   $$x_{A'} = k \times x_A = (-2) \times 3 = -6.$$
2. La distance $OA = 3$ et la distance $OA' = |-6| = 6$. Le point $O$ est situé entre $A'$ et $A$, à un tiers de la distance en partant de $A$ (puisque $OA' = 2 \times OA$).

**Solution 26.10**
1. Les points $A$ et $B$ appartiennent au cercle de centre $O$, donc les rayons sont égaux : $OA = OB$.
   Le point $O$ est équidistant de $A$ et de $B$. Par propriété caractéristique de la médiatrice, le point $O$ appartient donc obligatoirement à la médiatrice du segment $[AB]$.
2. La médiatrice d'un segment est la droite unique perpendiculaire à ce segment et passant par son milieu. Puisque le centre $O$ appartient à la médiatrice, toute droite perpendiculaire à $[AB]$ passant par $O$ est la médiatrice elle-même : elle coupe donc nécessairement $[AB]$ en son milieu.

**Solution 26.11**
1. La longueur totale est $1{,}20 \text{ m} = 120 \text{ cm}$.
   Chaque motif mesure 4 cm.
   Nombre de motifs : $\frac{120}{4} = 30$ motifs complets.
2. Aire totale : $30 \times 15 \text{ cm}^2 = 450 \text{ cm}^2$.

---

#### Niveau ★★★

**Solution 26.12**
1. Traçons le point $B'$, symétrique de la bille rouge $B$ par rapport à la droite de la bande $(d)$.
   Pour tout point $M$ de la bande $(d)$, la symétrie axiale garantit que $MB = MB'$.
   La longueur du trajet avec rebond s'écrit donc : $AM + MB = AM + MB'$.
   Or, la ligne la plus courte reliant deux points $A$ et $B'$ est le segment de droite $[AB']$ !
   Le point d'impact optimal $P$ est donc très exactement **l'intersection entre le segment $[AB']$ et la droite de la bande $(d)$**.
2. Par l'inégalité triangulaire, pour tout autre point $M$ de la bande, on a $AM + MB' > AB'$. Le trajet $AP + PB = AP + PB' = AB'$ est donc strictement le plus court possible. C'est le principe de Fermat appliqué à la réflexion !

**Solution 26.13**
1. Dans le triangle $ABC$ rectangle en $A$, l'angle $\widehat{B}$ a pour complémentaire $\widehat{C}$ ($\widehat{B} + \widehat{C} = 90^\circ$).
   Dans le triangle $HBA$ rectangle en $H$, l'angle $\widehat{HAB}$ est le complémentaire de $\widehat{B}$, donc $\widehat{HAB} = \widehat{C}$.
   Les triangles $ABC$, $HBA$ et $HAC$ ont tous les mêmes angles ($90^\circ$, $\widehat{B}$, $\widehat{C}$) : ils sont tous **semblables**.
2. Puisque $HBA$ et $HAC$ sont semblables, les côtés opposés aux angles homologues sont proportionnels :
   - Opposé à $\widehat{B}$ : dans $HBA$, c'est $AH$ ; dans $HAC$, c'est $HC$.
   - Opposé à $\widehat{C}$ : dans $HBA$, c'est $HB$ ; dans $HAC$, c'est $AH$.
   On a donc :
   $$\frac{AH}{HC} = \frac{HB}{AH} \implies AH \times AH = HB \times HC \implies AH^2 = HB \times HC.$$
3. Avec $HB = 4$ et $HC = 9$ :
   $$AH^2 = 4 \times 9 = 36 \implies AH = \sqrt{36} = 6 \text{ cm}.$$

**Solution 26.14**
Ce prétendu paradoxe repose sur une illusion d'optique !
Pour que le rectangle $5 \times 13$ soit parfaitement plein, la grande diagonale du rectangle devrait être un segment de droite unique.
Calculons les pentes des deux pièces qui la bordent :
- Pour le triangle rectangle : pente $= \frac{3}{8} = 0{,}375$.
- Pour le trapèze : pente $= \frac{2}{5} = 0{,}400$.
Les pentes ne sont pas égales ($\frac{3}{8} \neq \frac{2}{5}$) !
Les pièces ne s'emboîtent pas le long d'une ligne droite parfaite : elles laissent au centre un minuscule parallélogramme vide très étiré, invisible à l'œil nu. L'aire de cette fente cachée vaut exactement 1 carreau ($65 - 64 = 1$) !

---

### La question qui ouvre la suite

Regarde l'incroyable voyage que nous venons d'accomplir : nous savons désormais découper des formes, calculer des aires, manipuler des équations, des inégalités et des fonctions. Mais que se passe-t-il lorsque l'on quitte le monde plat de la feuille de papier pour pénétrer dans le relief en trois dimensions de notre univers ? Comment calculer la contenance d'une jarre conique, d'une pyramide de pierre ou de la planète Terre tout entière ?

C'est l'aventure de l'espace, des solides et des sections géométriques qui t'attend dans le chapitre suivant : **Le Découpage des Terres et la Boîte du Potier**.
