# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 27 : Le Découpage des Terres et la Boîte du Potier

> *« Une formule apprise par cœur sans être vue est comme une graine stérile. Mais prends une paire de ciseaux, coupe un triangle, recolle les morceaux de l'autre côté : le rectangle apparaît, et la formule devient une évidence. »*

---

### Ce que tu vas découvrir

- Pourquoi **tout triangle est la moitié d'un rectangle**, et comment les ciseaux suffisent à retrouver les aires du parallélogramme, du trapèze et même du disque.
- Comment passer du **plat** (les aires, en m²) au **plein** (les volumes, en m³), et pourquoi on multiplie par 100 dans un cas et par 1 000 dans l'autre.
- Le mystère du **« divisé par 3 »** des pyramides et des cônes, et le trésor dont Archimède était le plus fier : le volume de la **boule**.
- Ce qu'on voit quand on **tranche** un solide avec un couteau bien droit : les **sections**.
- Les pièges qui font perdre des points au brevet : rayon ou diamètre ? hauteur ou côté penché ? cm³ ou litres ?

---

### 1. Le problème : la querelle des deux fermiers et la commande du potier

Dans la vallée de la Meuse, au XIIIᵉ siècle, le grand intendant du comte dresse le registre des terres pour prélever la juste part de blé. Deux fermiers voisins se présentent devant lui.

* Le fermier **Martin** possède un champ **rectangulaire** de 20 mètres de large sur 30 mètres de long. L'intendant calcule sans hésiter :
  $$20 \times 30 = 600 \text{ mètres carrés.}$$
  C'est un quadrillage de 600 petits carrés de terre d'un mètre sur un mètre (tu te souviens du mur de briques du Chapitre 5 ?).
* Mais le fermier **Thomas** possède un champ en forme de **triangle étiré et pointu**. Le côté qui longe le ruisseau mesure 40 mètres, et la distance entre ce ruisseau et la pointe du pré, mesurée bien perpendiculairement, est de 30 mètres.

Les arpenteurs se disputent : *« Comment compter des carrés entiers dans un champ en pointe ? Les bords en biais coupent les carreaux en morceaux impossibles à mesurer ! »*

Un jeune compagnon bâtisseur s'approche avec une feuille de parchemin et une paire de ciseaux : *« Rangez vos cordes, messieurs. Il n'y a pas besoin de couper les brins d'herbe en miettes : il suffit d'inviter un frère jumeau à la table. »*

Le même jour, à l'autre bout du village, le **potier** reçoit une commande étrange : le meunier veut trois récipients qui contiennent **exactement autant de grain** l'un que l'autre — une jarre cylindrique, un entonnoir en forme de cône et un bol en demi-boule. Le potier sait mesurer la longueur avec une corde, la surface avec des carreaux… mais comment mesurer **ce qu'il y a dedans** ?

Ces deux problèmes — mesurer une surface tordue, mesurer un intérieur — vont nous occuper tout le chapitre. Tu verras qu'ils reposent sur la même idée : **découper, déplacer, recoller**, sans rien perdre ni rien ajouter.

---

### 2. Qu'est-ce qu'une aire ? Unités et conversions

#### 2.1 L'idée intuitive

L'**aire** d'une figure, c'est la quantité de « peinture » qu'il faut pour la recouvrir, ou le nombre de carreaux-unités qu'on peut y poser. Deux figures de formes très différentes peuvent avoir la même aire : il suffit qu'on puisse découper l'une et réassembler ses morceaux pour obtenir l'autre.

> **📐 Définition —** On choisit une unité d'aire : par exemple le **carré de 1 cm de côté**. L'**aire** d'une figure est le nombre de ces carrés-unités (et de morceaux de carrés) qu'il faut pour la recouvrir exactement, sans trou ni chevauchement.

**La notation cm².** On écrit $1 \text{ cm}^2$ et on lit « un **centimètre carré** ». Le petit 2 en haut n'est pas décoratif : il rappelle qu'on a multiplié **deux** longueurs (une largeur en cm et une longueur en cm). C'est la même petite puissance que dans $5^2 = 5 \times 5$ (Chapitre 18). D'ailleurs, l'aire d'un carré de côté $c$ s'écrit $c^2$ : voilà pourquoi on dit « $c$ **au carré** » !

**Périmètre ou aire ?** Le **périmètre** est la longueur de la clôture (on fait le tour, en cm) ; l'**aire** est la surface de la pelouse (on remplit, en cm²). Un rectangle de $1 \times 9$ et un carré de $3 \times 3$ ont la même aire (9 cm²) mais pas le même périmètre (20 cm et 12 cm).

#### 2.2 Les conversions d'aires : le piège du « fois 100 »

Un mètre, c'est 10 décimètres. Mais un **mètre carré**, combien de décimètres carrés ? Dessine-le : un carré de 1 m de côté, c'est un carré de 10 dm de côté, donc il contient $10 \times 10 = 100$ petits carrés de 1 dm de côté.

```
  1 m = 10 dm
  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤      10 lignes de 10 carreaux
  │  ...  100 carreaux de 1 dm² │      = 100 dm²
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
  └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
```

$$1 \text{ m}^2 = 100 \text{ dm}^2 = 10\,000 \text{ cm}^2 = 1\,000\,000 \text{ mm}^2.$$

Dans le tableau de conversion des aires, **chaque unité occupe deux colonnes** :

| km² | | hm² (ha) | | dam² (a) | | m² | | dm² | | cm² | | mm² | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | 3 | 5 | 0 | 0 | 0 | | |

Ici on lit : $3{,}5 \text{ m}^2 = 350 \text{ dm}^2 = 35\,000 \text{ cm}^2$.

> **💡 Le savais-tu ?** Les agriculteurs utilisent l'**are** (a), qui vaut $1 \text{ dam}^2 = 100 \text{ m}^2$ (un carré de 10 m de côté), et l'**hectare** (ha), qui vaut $1 \text{ hm}^2 = 10\,000 \text{ m}^2$ (un carré de 100 m de côté, à peu près un terrain et demi de football). Le mot « are » vient du latin *area*, « surface libre », qui a aussi donné le mot « aire » !

> **⚠️ Attention, piège !** $1 \text{ m}^2 \neq 100 \text{ cm}^2$. Puisque $1 \text{ m} = 100 \text{ cm}$, on a $1 \text{ m}^2 = 100 \text{ cm} \times 100 \text{ cm} = 10\,000 \text{ cm}^2$. Quand on convertit des aires, on multiplie (ou divise) par 100 **à chaque changement d'unité**, pas par 10.

---

### 3. Le coup de ciseaux : tout triangle est un demi-rectangle

#### 3.1 Base et hauteur : bien nommer les choses

Avant de couper, il faut apprendre deux mots précis.

> **📐 Définition —** Dans un triangle, on choisit un côté qu'on appelle la **base**. La **hauteur relative à cette base** est le segment issu du sommet opposé et **perpendiculaire** à la droite qui porte la base. Sa longueur est aussi appelée « hauteur ».

```
              C
             /|\
            / | \
           /  |h \
          /   |   \
         /____|____\
        A     H     B
        <---- b ---->
   [CH] est la hauteur relative à la base [AB] ; (CH) ⊥ (AB)
```

Le symbole $\perp$ se lit « est perpendiculaire à ». Le petit carré qu'on dessine au pied $H$ de la hauteur rappelle qu'il y a un angle droit.

Un triangle a **trois** côtés, donc **trois** hauteurs, une pour chaque base possible. On peut choisir celle qu'on veut, à condition de toujours associer une base **avec sa propre hauteur**.

#### 3.2 La preuve du frère jumeau

Reprenons le champ de Thomas : base $b = 40$ m, hauteur $h = 30$ m.

1. On découpe un **deuxième triangle identique**, de couleur différente.
2. On fait faire à ce jumeau un **demi-tour** (une symétrie centrale de centre le milieu d'un côté, comme au Chapitre 26).
3. On le colle contre le premier : ensemble, ils forment un **parallélogramme** de base $b$ et de hauteur $h$.
4. Et un parallélogramme, on va le voir juste après, a la même aire qu'un **rectangle** $b \times h$.

Plus simple encore, quand le pied $H$ de la hauteur tombe à l'intérieur de la base : la hauteur coupe le triangle en deux triangles rectangles. Chacun est la moitié d'un petit rectangle (coupé par sa diagonale). Les deux petits rectangles réunis forment le grand rectangle $b \times h$, et le triangle en occupe exactement la moitié.

```
   ┌─────────┬─────────┐
   │ ╲  (1') │ (2')  ╱ │      Les morceaux (1) et (2) forment le triangle.
   │   ╲     │     ╱   │      Les morceaux (1') et (2') sont leurs jumeaux.
   │ (1) ╲   │   ╱ (2) │      (1) = (1') et (2) = (2')
   │       ╲ │ ╱       │      donc triangle = moitié du rectangle.
   └─────────┴─────────┘
   A         H         B
```

> **📐 Formule — Aire du triangle**
> $$\mathcal{A}_{\text{triangle}} = \frac{\text{base} \times \text{hauteur}}{2} = \frac{b \times h}{2}$$

La lettre $\mathcal{A}$ (un A « calligraphié ») est souvent utilisée pour désigner une aire, pour ne pas la confondre avec le point $A$.

Pour le champ de Thomas : $\mathcal{A} = \dfrac{40 \times 30}{2} = \dfrac{1200}{2} = 600 \text{ m}^2$. Les deux fermiers, aux champs si différents, ont **exactement la même surface** de terre : ils paieront le même impôt, au grain de blé près.

#### 3.3 Aux limites : quand la hauteur tombe dehors

> **⚠️ Attention, piège !** Dans un triangle **obtus** (avec un angle de plus de 90°), la hauteur relative à certaines bases tombe **à l'extérieur** du triangle, sur le **prolongement** de la base. La formule reste vraie, mais la preuve change !

```
                          C
                        / |
                      /   |
                    /     | h
                  /    .  |
                /   .     |
              / .         |
             A--------B . . H
             <--- b -->
```

> **✍️ Démonstration —** Le pied $H$ est sur le prolongement de $[AB]$, au-delà de $B$. Le grand triangle rectangle $AHC$ contient notre triangle $ABC$ **plus** le petit triangle rectangle $BHC$. Donc :
> $$\mathcal{A}_{ABC} = \mathcal{A}_{AHC} - \mathcal{A}_{BHC} = \frac{AH \times h}{2} - \frac{BH \times h}{2} = \frac{(AH - BH) \times h}{2} = \frac{AB \times h}{2}.$$
> La formule « base × hauteur ÷ 2 » est donc vraie pour **tous** les triangles.

> **💡 Le savais-tu ?** Tous les triangles qui ont la même base $[AB]$ et dont le sommet $C$ glisse sur une droite parallèle à $(AB)$ ont **la même aire**, puisque la hauteur ne change pas ! Même un triangle très aplati et très penché. C'est le « triangle qui glisse » d'Euclide (Livre I des *Éléments*, proposition 37).

---

### 4. Le parallélogramme et le trapèze déshabillés

#### 4.1 Le parallélogramme : le champ penché

Prends un rectangle de carton et pousse son côté du haut : il se penche et devient un parallélogramme. Perd-il de la matière ? Coupe le petit triangle qui dépasse d'un côté et recolle-le dans le creux de l'autre côté : **le rectangle réapparaît**, avec la même base et la même hauteur.

```
        ________________                 ________________
       /|              /                |              |
      / |             /      ════>      |              | h
     /  | h          /                  |              |
    /___|___________/                   |______________|
    <------ b ----->                    <------ b ----->
   On coupe le triangle de gauche et on le recolle à droite.
```

> **📐 Formule — Aire du parallélogramme**
> $$\mathcal{A}_{\text{parallélogramme}} = b \times h$$
> où $h$ est la distance entre les deux côtés parallèles de longueur $b$ (mesurée **perpendiculairement**).

> **⚠️ Attention, piège !** Ne multiplie **jamais** la base par le côté penché ! Un parallélogramme de côtés 10 cm et 6 cm peut avoir une aire de 60 cm² (s'il est droit, c'est un rectangle), de 30 cm² (s'il est très penché), et même presque 0 si on l'écrase. Le côté penché ne change pas, mais la hauteur, si.

#### 4.2 Le trapèze : la jupe évasée

Un **trapèze** est un quadrilatère qui a deux côtés parallèles, appelés **bases** : la grande base $B$ et la petite base $b$. La **hauteur** $h$ est la distance entre ces deux bases.

Prends deux trapèzes jumeaux. Retourne l'un la tête en bas et colle-le contre l'autre : tu obtiens un **parallélogramme** dont la base vaut $B + b$ et la hauteur $h$.

```
      b                B                   B + b
   ______  _________________       ________________________
  /      \ \               /      /      /                /
 /        \ \             /  ═>  /      /                / h
/__________\ \___________/      /______/________________/
      B             b               B + b
```

> **📐 Formule — Aire du trapèze**
> $$\mathcal{A}_{\text{trapèze}} = \frac{(B + b) \times h}{2}$$

On peut aussi le voir comme $\dfrac{B+b}{2} \times h$ : c'est un rectangle dont la largeur est la **moyenne** des deux bases.

> **💡 Le savais-tu ?** Les cas limites sont rassurants. Si $b = B$, le trapèze est un parallélogramme et on retrouve $\dfrac{2B \times h}{2} = B \times h$. Si $b = 0$, la petite base s'écrase en un point, le trapèze devient un triangle, et on retrouve $\dfrac{B \times h}{2}$. Une bonne formule se vérifie toujours sur ses cas extrêmes !

---

### 5. La pizza d'Archimède : l'aire du disque

Tu as rencontré le nombre $\pi$ au Chapitre 16 : c'est le nombre de fois que le diamètre « rentre » dans le tour du cercle, $\pi \approx 3{,}14159$. Le périmètre d'un cercle de rayon $R$ vaut donc $2\pi R$. Mais la **surface** du disque ?

Au IIIᵉ siècle avant notre ère, **Archimède de Syracuse** imagine de découper le disque comme une pizza, en un grand nombre de parts fines qui partent du centre. Chaque part a pour longueur le rayon $R$. Il range ces parts **tête-bêche**, une pointe en haut, une pointe en bas :

```
    ____  ____  ____  ____  ____  ____  ____  ____
    \  /\ \  /\ \  /\ \  /\ \  /\ \  /\ \  /\ \  /\
     \/  \ \/  \ \/  \ \/  \ \/  \ \/  \ \/  \ \/  \   hauteur ≈ R
          ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾
    |<----------- demi-périmètre = π R ----------->|
```

La forme obtenue ressemble à un **rectangle qui ondule** :
* sa hauteur est le rayon $R$ ;
* sa longueur est **la moitié du tour** de la pizza (l'autre moitié du croûton est en bas), soit $\dfrac{2\pi R}{2} = \pi R$.

Plus les parts sont fines, plus les ondulations s'aplatissent : à la limite, c'est un vrai rectangle.

> **📐 Formule — Aire du disque de rayon $R$**
> $$\mathcal{A}_{\text{disque}} = \pi R \times R = \pi R^2$$
> On lit « pi R deux » ou « pi R au carré ». Attention : c'est $\pi \times (R \times R)$, le carré ne porte que sur $R$.

> **⚠️ Attention, piège !** Deux erreurs classiques :
> 1. Utiliser le **diamètre** au lieu du rayon. Pour un disque de diamètre 10 cm, $R = 5$ cm et $\mathcal{A} = 25\pi \approx 78{,}5$ cm², et non $100\pi$ !
> 2. Confondre $2\pi R$ (le **périmètre**, une longueur en cm) et $\pi R^2$ (l'**aire**, en cm²). Astuce : l'aire contient un « carré », comme son unité cm².

> **🔍 L'histoire vraie —** Archimède ne connaissait pas la valeur exacte de $\pi$ (personne ne la connaît : ses décimales ne s'arrêtent jamais !). Il a prouvé que l'aire du disque est égale à celle d'un triangle rectangle dont un côté de l'angle droit est le rayon et l'autre le périmètre du cercle : $\dfrac{2\pi R \times R}{2} = \pi R^2$. Et il a encadré $\pi$ entre $3 + \frac{10}{71}$ et $3 + \frac{1}{7}$ en utilisant des polygones à 96 côtés.

---

### 6. Exemples résolus sur les aires

**Exemple résolu 1 — Le jardin en trapèze.**
Un jardin a la forme d'un trapèze : la clôture du fond mesure 16 m, celle de devant 10 m, et les deux clôtures parallèles sont distantes de 8 m. Quelle est son aire ? Combien de sachets de gazon faut-il si un sachet couvre 25 m² ?

*Solution.* $\mathcal{A} = \dfrac{(16 + 10) \times 8}{2} = \dfrac{26 \times 8}{2} = \dfrac{208}{2} = 104 \text{ m}^2$.
$104 \div 25 = 4{,}16$ : 4 sachets ne suffisent pas, il en faut **5**. (On arrondit toujours **au-dessus** quand il s'agit de couvrir !)

**Exemple résolu 2 — La hauteur cachée du triangle rectangle.**
Un triangle $ABC$ est rectangle en $A$ avec $AB = 6$ cm, $AC = 8$ cm, $BC = 10$ cm. Calcule la longueur de la hauteur issue de $A$.

*Solution.* Dans un triangle rectangle, les deux côtés de l'angle droit sont **chacun la hauteur de l'autre**. Donc avec la base $[AB]$ et la hauteur $[AC]$ :
$$\mathcal{A} = \frac{6 \times 8}{2} = 24 \text{ cm}^2.$$
Mais on peut aussi prendre la base $[BC]$ et la hauteur inconnue $h$ issue de $A$ : $\mathcal{A} = \dfrac{10 \times h}{2} = 5h$.
Les deux calculs donnent la même aire, donc $5h = 24$ et $h = 4{,}8$ cm. On a calculé une longueur grâce à une aire, sans aucune mesure !

**Exemple résolu 3 — La figure composée.**
Une fenêtre a la forme d'un rectangle de 120 cm de large et 150 cm de haut, surmonté d'un demi-disque de diamètre 120 cm. Quelle est l'aire de la vitre, arrondie au cm² ?

*Solution.* On **découpe** la figure en morceaux simples.
* Rectangle : $120 \times 150 = 18\,000$ cm².
* Demi-disque : rayon $R = 60$ cm, aire $\dfrac{\pi \times 60^2}{2} = \dfrac{3600\pi}{2} = 1800\pi \approx 5654{,}87$ cm².
* Total : $18\,000 + 1800\pi \approx 23\,655$ cm², soit environ $2{,}37$ m².

**Exemple résolu 4 — La couronne et la piste.**
Un bassin circulaire de rayon 6 m est entouré d'une allée de 2 m de large. Quelle est l'aire de l'allée ?

*Solution.* L'allée est une **couronne** : le grand disque (rayon $6 + 2 = 8$ m) moins le petit disque (rayon 6 m).
$$\mathcal{A} = \pi \times 8^2 - \pi \times 6^2 = 64\pi - 36\pi = 28\pi \approx 87{,}96 \text{ m}^2.$$

> **⚠️ Attention, piège !** On ne peut pas soustraire les rayons d'abord : $\pi \times (8 - 6)^2 = 4\pi$ est faux ! On soustrait les **aires**, pas les longueurs.

**Exemple résolu 5 — Une conversion pour le notaire.**
Un terrain rectangulaire mesure 85 m sur 64 m. Exprime son aire en m², en ares et en hectares.

*Solution.* $85 \times 64 = 5440$ m². Comme $1 \text{ a} = 100 \text{ m}^2$ : $5440 \text{ m}^2 = 54{,}4$ a. Comme $1 \text{ ha} = 100$ a : $54{,}4 \text{ a} = 0{,}544$ ha.

---

