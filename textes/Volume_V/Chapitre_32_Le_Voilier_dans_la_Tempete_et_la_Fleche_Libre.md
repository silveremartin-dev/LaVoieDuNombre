# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 32 : Le Voilier dans la Tempête et la Flèche Libre

> *« Un point est une ancre qui retient le navire au fond de l'eau. Une coordonnée cartésienne dit où tu es. Mais le marin qui affronte la houle n'a que faire de son ancrage : il a besoin de savoir où le vent le pousse, à quelle vitesse, et comment deux courants qui s'affrontent fusionnent en un seul élan. Pour libérer le mouvement du sol, il a fallu inventer la flèche volante : le Vecteur. »*

---

### Ce que tu vas découvrir

- Pourquoi le repère cartésien ne suffisait plus aux physiciens et comment **Hermann Grassmann** a libéré le déplacement de son point d'attache en 1844.
- Le triplet fondamental qui définit un **vecteur** : direction, sens, norme — et la notation fléchée $\vec{u}$ ou $\vec{AB}$.
- La **relation de Chasles** ($\vec{AB} + \vec{BC} = \vec{AC}$) comprise comme un relais de navigateurs ou de coursiers, et la règle du parallélogramme.
- La multiplication d'un vecteur par un nombre réel (scalaire) et la notion de **vecteurs colinéaires**.
- Comment traduire la géométrie en calcul algébrique dans un repère $(O\,; \vec{i}, \vec{j})$ : coordonnées de vecteurs, formule du milieu, formule de la distance.
- Le juge de paix de l'alignement et du parallélisme : le **déterminant** $xy' - yx' = 0$.

---

### 1. Le problème : la barque dans le courant du grand fleuve

Tu te tiens à la barre d'une barque de pêcheurs sur les eaux d'un fleuve large de cinq cents mètres. Sur la rive opposée, droit devant toi au Nord, se dresse l'embarcadère où t'attendent tes compagnons.

Tu empoignes les deux rames. Tu tires sur le bois de toutes tes forces musculaires : ta proue pointe droit vers le **Nord**, et ton effort te propulse dans l'eau à la vitesse constante de **$3\text{ km/h}$**. Tu calcules mentalement que dans dix minutes, tu auras accosté au ponton.

Mais le fleuve n'est pas un étang endormi. Un fort courant s'écoule d'Ouest en **Est** à la vitesse de **$4\text{ km/h}$**.

Regarde la scène depuis la berge :

```
                                  C (Point d'atterrissage réel)
                                 ▲
                               / │
                 Trajectoire /   │
                   réelle   /     │  Courant des rames (Nord : 3 km/h)
                          /       │
                        /         │
                       o──────────┴► B
                       A    Courant du fleuve (Est : 4 km/h)
```

Que subit ton embarcation ?
1. Tes bras t'entraînent vers le Nord : en une heure, sans courant, tu parcourrais $3\text{ km}$ vers le Nord.
2. L'eau sous ta coque t'emporte vers l'Est : en une heure, sans ramer, tu dériverais de $4\text{ km}$ vers l'Est.

Les deux actions s'exercent **en même temps**. Au bout d'une heure imaginaire où les deux mouvements se combineraient, tu ne serais ni au Nord, ni à l'Est, mais au point $C$. Quelle distance as-tu franchie par rapport au fond du fleuve ?

Le triangle formé par le déplacement vers l'Est ($4\text{ km}$), le déplacement vers le Nord ($3\text{ km}$) et la trajectoire réelle est un triangle rectangle. Le théorème de Pythagore donne la distance parcourue :
$$d = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ km}.$$

Ta vitesse réelle par rapport aux rives est de **$5\text{ km/h}$**, orientée en biais vers le Nord-Est !

Ce problème révèle une insuffisance fondamentale des nombres ordinaires :
- Un nombre seul ($5\text{ km/h}$) dit **combien**, mais il ne dit pas **vers où**.
- Une coordonnée de point $A(x_A, y_A)$ dit **où l'on est**, mais elle est clouée au système d'axes que l'on a dessiné sur la carte. Si la barque rame de la même manière cent kilomètres plus en aval, le phénomène physique est rigoureusement identique, bien que les coordonnées de départ et d'arrivée soient complètement changées.

Il fallait inventer un objet mathématique nouveau : une **flèche autonome**, que l'on peut transporter partout sans la déformer, et qui encode à la fois une inclinaison, une orientation et une grandeur.

---

### 2. Libérer la flèche : la naissance du vecteur

#### 2.1 La rupture de Grassmann (1844)

Pendant deux siècles après René Descartes (1637), la géométrie analytique fonctionnait en attachant chaque point à une origine fixe $O(0, 0)$. Pour étudier le déplacement d'un oiseau ou le souffle d'une tempête, on devait manipuler les coordonnées du point de départ $A$, puis celles du point d'arrivée $B$, et faire des soustractions.

En 1844, un professeur de lycée allemand méconnu de ses contemporains, **Hermann Günther Grassmann**, publie un ouvrage visionnaire : *Die Lineale Ausdehnungslehre* (La Théorie de l'Extension Linéaire). Grassmann pose une idée révolutionnaire :
> « Le point est une prison. Ce qui importe en physique, ce n'est pas le lieu où commence l'action, c'est l'action elle-même : le transport pur. »

Cette entité géométrique prend le nom de **vecteur**, du latin *vehere* (« transporter », « charrier » — qui a aussi donné « véhicule »).

#### 2.2 Les trois caractéristiques d'un vecteur

> **📐 Définition — Vecteur.**
> Un vecteur non nul $\vec{u}$ est défini par trois données inséparables :
> 1. **Sa direction :** la droite qui le porte (ou toute droite qui lui est parallèle). Cela indique la ligne sur laquelle s'effectue le mouvement (par exemple la droite Nord-Sud, l'axe horizontal, une pente à $30^\circ$).
> 2. **Son sens :** l'orientation du parcours sur cette droite, indiquée par la pointe de la flèche (par exemple vers le Nord plutôt que vers le Sud, de gauche à droite).
> 3. **Sa norme :** la longueur du segment fléché, notée $\|\vec{u}\|$. Elle représente l'intensité physique (une vitesse en $\text{km/h}$, une force en newtons, un déplacement en mètres).

```
          Sens (la flèche pointe vers le haut)
             ▲
            /
           /   Norme ||u|| (la longueur de la flèche)
          /
         /
        o  Direction (la droite imaginaire en pointillés qui porte la flèche)
       . 
      .
```

**Notation expliquée.**
- On surmonte la lettre d'une flèche vers la droite : $\vec{u}$, $\vec{v}$, $\vec{w}$. On lit à voix haute : « le vecteur u », « le vecteur v ».
- Lorsque le vecteur représente le déplacement allant explicitement d'un point $A$ à un point $B$, on écrit $\vec{AB}$, lu « vecteur AB ». Ici, $A$ est **l'origine** (ou point d'application) du représentant, et $B$ en est **l'extrémité**.
- La **norme** s'écrit avec une double barre : $\|\vec{u}\|$ ou $\|\vec{AB}\|$. On lit « norme de u » ou « norme de AB ». On a toujours $\|\vec{AB}\| = AB$ (la longueur géométrique usuelle). On utilise une double barre pour ne pas confondre avec la valeur absolue $|x|$ d'un nombre réel.

> **⚠️ Attention, piège ! Ne confonds jamais direction et sens !**
> Dans le langage courant, on dit souvent « je vais dans la direction de Paris ». En mathématiques, c'est une faute de vocabulaire :
> - La **direction**, c'est la ligne de chemin de fer reliant Paris à Lyon.
> - Le **sens**, c'est d'aller de Paris vers Lyon, ou de Lyon vers Paris.
> Deux automobilistes qui se croisent à contre-sens sur une même ligne droite ont la **même direction**, mais des **sens opposés**.

#### 2.3 Le vecteur nul et les représentants

Que se passe-t-il si un voyageur ne bouge pas d'un millimètre ?
Son point de départ $A$ et son point d'arrivée $A$ sont confondus. Le déplacement associé est le **vecteur nul**, noté $\vec{0}$ (un zéro surmonté d'une flèche) :
$$\vec{AA} = \vec{BB} = \vec{0}.$$
Le vecteur nul a une norme égale à zéro : $\|\vec{0}\| = 0$. Il n'a pas de direction ni de sens privilégié (on dit qu'il a toutes les directions possibles).

> **💡 Le savais-tu ? Un vecteur est une infinité de flèches à la fois !**
> Un vecteur $\vec{u}$ n'est pas « collé » en un point précis du papier. C'est une classe de déplacements.
> Si dix oiseaux volent de conserve en formation serrée, tous vers le Sud à $40\text{ km/h}$, chaque oiseau trace sa propre flèche dans le ciel. Toutes ces flèches ont la même direction, le même sens et la même longueur. On dit qu'elles sont des **représentants** d'un seul et même vecteur $\vec{u}$.

```
   Oiseau 1            Oiseau 2            Oiseau 3
     A                   C                   E
     o                   o                   o
      \                   \                   \
       \   u = AB          \   u = CD          \   u = EF
        \                   \                   \
         ▼                   ▼                   ▼
         B                   D                   F
         
             AB = CD = EF = même vecteur libre u !
```

#### 2.4 Égalité vectorielle et parallélogramme

Quand peut-on affirmer que deux flèches $\vec{AB}$ et $\vec{CD}$ représentent le même vecteur ?

> **📐 Théorème fondamental — Égalité vectorielle.**
> Soient quatre points du plan $A$, $B$, $C$, $D$.
> $$\vec{AB} = \vec{CD} \iff \text{le quadrilatère } ABDC \text{ est un parallélogramme (éventuellement aplati)}.$$

> **⚠️ Attention, piège ! L'ordre des sommets.**
> Regarde avec une immense vigilance l'ordre des lettres : $\vec{AB} = \vec{CD}$ équivaut à ce que $AB\mathbf{DC}$ soit un parallélogramme, et **non pas** $ABCD$ !
> Pour aller de $A$ à $B$, on effectue le même glissement que pour aller de $C$ à $D$. Les segments $[AD]$ et $[BC]$ ont donc le même milieu : les diagonales se coupent en leur milieu.

```
       A o────────────────────► B
         │                    │
         │                    │
         │                    │
       C o────────────────────► D
       
      Le vecteur AB va de A vers B.
      Le vecteur CD va de C vers D.
      Le quadrilatère tracé en suivant le contour est A-B-D-C !
```

---

### 3. Les opérations sur les vecteurs

#### 3.1 La relation de Chasles : le relais des coursiers

Comment additionner deux déplacements successifs ?
Imagine un message royal porté par des cavaliers d'estafette :
- Un premier cavalier part du relais $A$ et galope jusqu'au relais $B$ : déplacement $\vec{AB}$.
- Au relais $B$, il tend la sacoche de cuir à un second cavalier qui part immédiatement vers la citadelle $C$ : déplacement $\vec{BC}$.

Quel est le bilan global pour la lettre royale ? Elle est partie de $A$ et elle se trouve en $C$.

> **📐 Théorème (Relation de Chasles, 1837) —**
> Pour tous points $A$, $B$, $C$ du plan :
> $$\vec{AB} + \vec{BC} = \vec{AC}.$$

<div align="center">
<svg width="440" height="210" viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8" />
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#b91c1c" />
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#15803d" />
    </marker>
  </defs>
  <rect width="440" height="210" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
  
  <!-- Relais A vers B -->
  <line x1="50" y1="160" x2="210" y2="130" stroke="#1d4ed8" stroke-width="3" marker-end="url(#arr-blue)"/>
  <text x="125" y="165" fill="#1d4ed8" font-family="sans-serif" font-weight="bold" font-size="13">u = AB (1er relais)</text>
  <circle cx="50" cy="160" r="4" fill="#0f172a"/>
  <text x="35" y="175" font-family="sans-serif" font-weight="bold" font-size="12">A</text>

  <!-- Relais B vers C -->
  <line x1="210" y1="130" x2="370" y2="40" stroke="#b91c1c" stroke-width="3" marker-end="url(#arr-red)"/>
  <text x="310" y="105" fill="#b91c1c" font-family="sans-serif" font-weight="bold" font-size="13">v = BC (2e relais)</text>
  <circle cx="210" cy="130" r="4" fill="#0f172a"/>
  <text x="210" y="150" font-family="sans-serif" font-weight="bold" font-size="12">B</text>

  <!-- Bilan direct A vers C -->
  <line x1="50" y1="160" x2="365" y2="43" stroke="#15803d" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arr-green)"/>
  <text x="160" y="75" fill="#15803d" font-family="sans-serif" font-weight="bold" font-size="14">AC = u + v (Bilan global de Chasles)</text>
  <circle cx="370" cy="40" r="4" fill="#0f172a"/>
  <text x="380" y="45" font-family="sans-serif" font-weight="bold" font-size="12">C</text>
  
  <text x="220" y="198" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Relation de Chasles : le point relais B disparaît pour ne laisser que le trajet direct A → C</text>
</svg>
</div>

```
                        C
                       ▲
                      /
            v = BC   /
                    /
        u = AB     /     w = u + v = AC (Bilan global)
                  /
   A o──────────► B
```

**Origine historique.**
Cette relation porte le nom du géomètre français **Michel Chasles** (1793-1880), professeur à la Sorbonne et à Polytechnique, qui a unifié la géométrie projective et les mesures algébriques de segments orientés.

> **💡 Le savais-tu ? Le piège de l'addition des longueurs.**
> $\vec{AB} + \vec{BC} = \vec{AC}$ est une égalité de **vecteurs**. Elle n'implique **jamais** que $AB + BC = AC$ pour les longueurs ordinaires, sauf si les trois points sont alignés dans l'ordre $A, B, C$ !
> En général, dans un triangle non aplati, l'inégalité triangulaire (chapitre 9) impose :
> $$AC < AB + BC.$$
> Le chemin en ligne droite est strictement plus court que le détour par $B$. La norme de la somme est inférieure ou égale à la somme des normes : $\|\vec{u} + \vec{v}\| \le \|\vec{u}\| + \|\vec{v}\|$.

#### 3.2 L'opposé d'un vecteur et la soustraction

Si l'on parcourt le chemin dans l'autre sens, de $B$ vers $A$, le vecteur obtenu a la même direction, la même norme, mais un **sens contraire**. C'est le vecteur **opposé**, noté $-\vec{AB}$ :
$$-\vec{AB} = \vec{BA}.$$

En appliquant la relation de Chasles :
$$\vec{AB} + \vec{BA} = \vec{AA} = \vec{0}.$$

Pour soustraire un vecteur $\vec{v}$, on ajoute son opposé :
$$\vec{u} - \vec{v} = \vec{u} + (-\vec{v}).$$

#### 3.3 La règle du parallélogramme (forces concourantes)

Que faire si deux vecteurs partent du même point initial $A$, comme deux remorqueurs tirant sur un même cargo ?
Soit $\vec{u} = \vec{AB}$ et $\vec{v} = \vec{AC}$.
Pour appliquer Chasles, il suffit de placer au bout de $B$ un représentant de $\vec{v}$ : on construit le point $D$ tel que $\vec{BD} = \vec{AC}$.
Alors :
$$\vec{AB} + \vec{AC} = \vec{AB} + \vec{BD} = \vec{AD}.$$
Le quadrilatère $ABDC$ est un parallélogramme, et le vecteur somme $\vec{AD}$ correspond à sa diagonale principale.

```
       C o....................► D
        ▲                    ▲
         \                  /
      v   \                / v
           \              /
            o────────────► B
            A      u
```

#### 3.4 Multiplication d'un vecteur par un scalaire

En physique et en géométrie, un nombre réel est souvent appelé un **scalaire** (du latin *scala*, échelle), car il sert à changer l'échelle d'une grandeur sans changer sa nature.

> **📐 Définition — Produit d'un vecteur par un réel.**
> Soit $\vec{u}$ un vecteur et $k \in \mathbb{R}$ un nombre réel. Le vecteur $k\vec{u}$ est défini par :
> 1. Si $k = 0$ ou $\vec{u} = \vec{0}$, alors $k\vec{u} = \vec{0}$.
> 2. Si $k \neq 0$ et $\vec{u} \neq \vec{0}$ :
>    - $k\vec{u}$ a la **même direction** que $\vec{u}$ ;
>    - $k\vec{u}$ a le **même sens** que $\vec{u}$ si $k > 0$, et le **sens opposé** si $k < 0$ ;
>    - sa norme est $\|k\vec{u}\| = |k| \times \|\vec{u}\|$.

```
       -2u                -u         0        u          2u         3u
   ◄────────────    ◄──────      o      ──────►    ──────────►  ──────────────►
```

> **📐 Propriétés algébriques —** Pour tous vecteurs $\vec{u}, \vec{v}$ et tous réels $k, k'$ :
> - $(k + k')\vec{u} = k\vec{u} + k'\vec{u}$ (distributivité par rapport aux scalaires) ;
> - $k(\vec{u} + \vec{v}) = k\vec{u} + k\vec{v}$ (distributivité par rapport aux vecteurs) ;
> - $k(k'\vec{u}) = (kk')\vec{u}$ ;
> - $1\vec{u} = \vec{u}$ et $(-1)\vec{u} = -\vec{u}$.

#### 3.5 Caractérisation vectorielle du milieu

Soit un segment $[AB]$. Le milieu $I$ de $[AB]$ peut s'exprimer de trois manières vectorielles équivalentes :
1. $\vec{AI} = \vec{IB}$ (même direction, même sens, même demi-longueur) ;
2. $\vec{IA} + \vec{IB} = \vec{0}$ ($I$ est le centre d'équilibre entre $A$ et $B$) ;
3. Pour tout point $M$ du plan : $\vec{MA} + \vec{MB} = 2\vec{MI}$.

> **✍️ Démonstration — Identité du milieu.**
> D'après Chasles : $\vec{MA} = \vec{MI} + \vec{IA}$ et $\vec{MB} = \vec{MI} + \vec{IB}$.
> En sommant terme à terme :
> $$\vec{MA} + \vec{MB} = (\vec{MI} + \vec{IA}) + (\vec{MI} + \vec{IB}) = 2\vec{MI} + (\vec{IA} + \vec{IB}).$$
> Comme $I$ est le milieu de $[AB]$, on a $\vec{IA} + \vec{IB} = \vec{0}$. Donc :
> $$\vec{MA} + \vec{MB} = 2\vec{MI}. \quad \blacksquare$$

---

### 4. Les vecteurs dans un repère cartésien

#### 4.1 La base $(\vec{i}, \vec{j})$ et les coordonnées d'un vecteur

Munissons le plan d'une origine $O$ et de deux vecteurs non colinéaires $\vec{i}$ et $\vec{j}$. Le triplet $(O\,; \vec{i}, \vec{j})$ forme un **repère du plan**. Si les directions de $\vec{i}$ et $\vec{j}$ sont perpendiculaires et que $\|\vec{i}\| = \|\vec{j}\| = 1$, on dit que le repère est **orthonormé**.

> **📐 Théorème et Définition — Coordonnées d'un vecteur.**
> Pour tout vecteur $\vec{u}$ du plan, il existe un **unique** couple de réels $(x\,; y)$ tel que :
> $$\vec{u} = x\vec{i} + y\vec{j}.$$
> On écrit $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ ou $\vec{u}(x\,; y)$.
> $x$ est **l'abscisse** du vecteur et $y$ est son **ordonnée**.

```
                         y ▲
                           │             u = x i + y j
                       y ──┼ - - - - - - o 
                           │             ▲
                           │           / │
                           │       u /   │ y j
                           │       /     │
                           │     /       │
                       O ──┼────o────────┼────────► x
                           │   i        x
```

#### 4.2 Les formules fondamentales des coordonnées

Soient deux points $A(x_A\,; y_A)$ et $B(x_B\,; y_B)$, et deux vecteurs $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$.

> **📐 Formules clés à maîtriser absolument —**
> 1. **Vecteur reliant deux points (« Arrivée moins Départ ») :**
>    $$\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix}$$
> 2. **Somme de vecteurs :**
>    $$\vec{u} + \vec{v}\begin{pmatrix} x + x' \\ y + y' \end{pmatrix}$$
> 3. **Multiplication par un scalaire :**
>    $$k\vec{u}\begin{pmatrix} kx \\ ky \end{pmatrix}$$
> 4. **Coordonnées du milieu $I$ de $[AB]$ :**
>    $$x_I = \frac{x_A + x_B}{2}, \quad y_I = \frac{y_A + y_B}{2}$$
> 5. **Norme d'un vecteur (dans un repère orthonormé uniquement !) :**
>    $$\|\vec{u}\| = \sqrt{x^2 + y^2}$$
>    et la distance entre deux points :
>    $$AB = \|\vec{AB}\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}.$$

> **✍️ Démonstration — Coordonnées de $\vec{AB}$.**
> Par définition des coordonnées des points, $\vec{OA} = x_A\vec{i} + y_A\vec{j}$ et $\vec{OB} = x_B\vec{i} + y_B\vec{j}$.
> Selon la relation de Chasles :
> $$\vec{AB} = \vec{AO} + \vec{OB} = -\vec{OA} + \vec{OB} = \vec{OB} - \vec{OA}.$$
> En substituant :
> $$\vec{AB} = (x_B\vec{i} + y_B\vec{j}) - (x_A\vec{i} + y_A\vec{j}) = (x_B - x_A)\vec{i} + (y_B - y_A)\vec{j}.$$
> Les coordonnées de $\vec{AB}$ sont donc bien $(x_B - x_A \,;\, y_B - y_A)$. $\blacksquare$

---

### 5. Colinéarité et déterminant : l'art de viser droit

#### 5.1 Définition de la colinéarité

Deux flèches peuvent avoir des tailles différentes et des sens opposés : si elles sont portées par des droites parallèles, elles ont la **même direction**. En mathématiques, on dit qu'elles sont **colinéaires** (du latin *cum*, ensemble, et *linea*, ligne : « sur une même ligne »).

> **📐 Définition — Vecteurs colinéaires.**
> Deux vecteurs $\vec{u}$ et $\vec{v}$ sont dits **colinéaires** si l'un est le produit de l'autre par un nombre réel :
> $$\text{il existe } k \in \mathbb{R} \text{ tel que } \vec{u} = k\vec{v} \quad \text{ou} \quad \vec{v} = k\vec{u}.$$
> Par convention, le vecteur nul $\vec{0}$ est colinéaire à **tous** les vecteurs du plan (car $\vec{0} = 0 \times \vec{u}$).

#### 5.2 Le déterminant de deux vecteurs

Comment tester instantanément si deux vecteurs $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ sont colinéaires, sans chercher $k$ au hasard ?

> **📐 Définition et Théorème — Déterminant dans le plan.**
> Le **déterminant** des vecteurs $\vec{u}$ et $\vec{v}$ dans une base orthonormée est le nombre réel noté $\det(\vec{u}, \vec{v})$ calculé par la règle du produit en croix :
> $$\det(\vec{u}, \vec{v}) = \begin{vmatrix} x & x' \\ y & y' \end{vmatrix} = x y' - y x'.$$
> **Critère fondamental :**
> $$\vec{u} \text{ et } \vec{v} \text{ sont colinéaires} \iff \det(\vec{u}, \vec{v}) = 0 \iff x y' - y x' = 0.$$

> **✍️ Démonstration — Condition de colinéarité.**
> - **Sens direct ($\implies$) :** Supposons $\vec{u}$ et $\vec{v}$ colinéaires. Si $\vec{v} = \vec{0}$, alors $x' = y' = 0$, donc $xy' - yx' = x(0) - y(0) = 0$.
>   Si $\vec{v} \neq \vec{0}$, il existe $k \in \mathbb{R}$ tel que $\vec{u} = k\vec{v}$, ce qui signifie $x = kx'$ et $y = ky'$.
>   Calculons la différence croisée :
>   $$xy' - yx' = (kx')y' - (ky')x' = k x' y' - k y' x' = 0.$$
>
> - **Sens réciproque ($\impliedby$) :** Supposons $xy' - yx' = 0$.
>   Si $\vec{v} = \vec{0}$, $\vec{u}$ et $\vec{v}$ sont colinéaires par définition.
>   Supposons $\vec{v} \neq \vec{0}$. L'une au moins de ses coordonnées est non nulle. Supposons par exemple $x' \neq 0$.
>   Posons $k = \frac{x}{x'}$, de sorte que $x = kx'$.
>   L'égalité $xy' - yx' = 0$ donne alors :
>   $$(kx')y' - yx' = 0 \iff x'(ky' - y) = 0.$$
>   Comme $x' \neq 0$, il vient nécessairement $ky' - y = 0$, soit $y = ky'$.
>   On a donc à la fois $x = kx'$ et $y = ky'$, ce qui s'écrit $\vec{u} = k\vec{v}$. Les vecteurs sont donc bien colinéaires. $\blacksquare$

> **💡 Interprétation géométrique : l'aire du parallélogramme.**
> La valeur absolue du déterminant $|\det(\vec{u}, \vec{v})|$ est exactement égale à l'**aire du parallélogramme** formé par les deux vecteurs $\vec{u}$ et $\vec{v}$ !
> Si les vecteurs sont colinéaires, le parallélogramme est aplati : son aire est nulle, d'où $\det(\vec{u}, \vec{v}) = 0$.

#### 5.3 Les deux grandes applications géométriques

Grâce au déterminant, les problèmes d'alignement et de parallélisme se transforment en une simple vérification de calcul algébrique :

1. **Parallélisme de droites :**
   Deux droites $(AB)$ et $(CD)$ sont parallèles si et seulement si leurs vecteurs directeurs $\vec{AB}$ et $\vec{CD}$ sont colinéaires :
   $$(AB) \parallel (CD) \iff \det(\vec{AB}, \vec{CD}) = 0.$$

2. **Alignement de trois points :**
   Trois points distincts $A$, $B$, $C$ sont alignés si et seulement si les vecteurs $\vec{AB}$ et $\vec{AC}$ ont la même direction :
   $$A, B, C \text{ sont alignés} \iff \vec{AB} \text{ et } \vec{AC} \text{ sont colinéaires} \iff \det(\vec{AB}, \vec{AC}) = 0.$$

---

### 6. Exemples résolus détaillés

> **Exemple résolu 1 — Simplifier une expression vectorielle avec Chasles.**
> Simplifier au maximum le vecteur :
> $$\vec{W} = \vec{AB} - \vec{CB} + \vec{CD} - \vec{AD}.$$
>
> **Méthode pas à pas :**
> 1. Remplacer les soustractions par l'addition de l'opposé :
>    $$-\vec{CB} = \vec{BC} \quad \text{et} \quad -\vec{AD} = \vec{DA}.$$
> 2. Réécrire l'expression :
>    $$\vec{W} = \vec{AB} + \vec{BC} + \vec{CD} + \vec{DA}.$$
> 3. Enchaîner les termes consécutifs grâce à la relation de Chasles :
>    $$\vec{AB} + \vec{BC} = \vec{AC},$$
>    $$\vec{AC} + \vec{CD} = \vec{AD},$$
>    $$\vec{AD} + \vec{DA} = \vec{AA} = \vec{0}.$$
> **Conclusion :** $\vec{W} = \vec{0}$.

> **Exemple résolu 2 — Calculs de coordonnées et de distances.**
> Dans un repère orthonormé $(O\,; \vec{i}, \vec{j})$, on donne $A(-3\,; 2)$, $B(1\,; 5)$ et $C(4\,; 1)$.
> 1. Déterminer les coordonnées de $\vec{AB}$ et la longueur exacte $AB$.
> 2. Déterminer les coordonnées du point $D$ tel que $ABCD$ soit un parallélogramme.
>
> **Solution :**
> 1. Coordonnées de $\vec{AB}$ :
>    $$\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix} = \begin{pmatrix} 1 - (-3) \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}.$$
>    Norme de $\vec{AB}$ (distance $AB$) :
>    $$AB = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5.$$
> 2. Attention : $ABCD$ est un parallélogramme si et seulement si $\vec{AB} = \vec{DC}$ (ou $\vec{AD} = \vec{BC}$).
>    Notons $(x_D\,; y_D)$ les coordonnées de $D$.
>    $$\vec{DC}\begin{pmatrix} x_C - x_D \\ y_C - y_D \end{pmatrix} = \begin{pmatrix} 4 - x_D \\ 1 - y_D \end{pmatrix}.$$
>    L'égalité $\vec{AB} = \vec{DC}$ se traduit par le système :
>    $$\begin{cases} 4 - x_D = 4 \implies x_D = 0 \\ 1 - y_D = 3 \implies y_D = 1 - 3 = -2 \end{cases}$$
>    Le point cherché est donc $D(0\,; -2)$.
>    *(Vérification par les milieux : le milieu de $[AC]$ est $\left(\frac{-3+4}{2}\,;\,\frac{2+1}{2}\right) = (0{,}5\,;\,1{,}5)$ ; le milieu de $[BD]$ est $\left(\frac{1+0}{2}\,;\,\frac{5+(-2)}{2}\right) = (0{,}5\,;\,1{,}5)$. Les diagonales se coupent bien en leur milieu !)*

> **Exemple résolu 3 — Tester l'alignement de trois points avec le déterminant.**
> On considère les points $E(-2\,; -3)$, $F(2\,; 3)$ et $G(6\,; 9)$. Sont-ils alignés ?
>
> **Solution :**
> Calculons les coordonnées des vecteurs $\vec{EF}$ et $\vec{EG}$ :
> $$\vec{EF}\begin{pmatrix} 2 - (-2) \\ 3 - (-3) \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}, \quad \vec{EG}\begin{pmatrix} 6 - (-2) \\ 9 - (-3) \end{pmatrix} = \begin{pmatrix} 8 \\ 12 \end{pmatrix}.$$
> Calculons le déterminant :
> $$\det(\vec{EF}, \vec{EG}) = \begin{vmatrix} 4 & 8 \\ 6 & 12 \end{vmatrix} = 4 \times 12 - 6 \times 8 = 48 - 48 = 0.$$
> Le déterminant est nul, donc les vecteurs $\vec{EF}$ et $\vec{EG}$ sont colinéaires.
> Comme ils partagent le point commun $E$, les points $E$, $F$ et $G$ sont alignés.

> **Exemple résolu 4 — Déterminer un paramètre pour obtenir le parallélisme.**
> Soient les vecteurs $\vec{u}\begin{pmatrix} 2m - 1 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 5 \\ m + 2 \end{pmatrix}$ où $m$ est un réel inconnu.
> Pour quelles valeurs de $m$ ces vecteurs sont-ils colinéaires ?
>
> **Solution :**
> $\vec{u}$ et $\vec{v}$ sont colinéaires si et seulement si $\det(\vec{u}, \vec{v}) = 0$ :
> $$(2m - 1)(m + 2) - 3 \times 5 = 0.$$
> Développons :
> $$2m^2 + 4m - m - 2 - 15 = 0 \iff 2m^2 + 3m - 17 = 0.$$
> C'est une équation du second degré. Son discriminant est :
> $$\Delta = 3^2 - 4 \times 2 \times (-17) = 9 + 136 = 145 > 0.$$
> Il existe deux valeurs réelles distinctes :
> $$m_1 = \frac{-3 - \sqrt{145}}{4} \quad \text{et} \quad m_2 = \frac{-3 + \sqrt{145}}{4}.$$

> **Exemple résolu 5 — Décomposition vectorielle géométrique pure.**
> Soit un triangle $ABC$. On place les points $P$ et $Q$ définis par $\vec{AP} = \frac{1}{3}\vec{AB}$ et $\vec{AQ} = \frac{1}{3}\vec{AC}$.
> Démontrer sans repère que $(PQ) \parallel (BC)$.
>
> **Solution :**
> Exprimons le vecteur $\vec{PQ}$ en fonction de $\vec{AB}$ et $\vec{AC}$ en utilisant Chasles :
> $$\vec{PQ} = \vec{PA} + \vec{AQ} = -\vec{AP} + \vec{AQ} = -\frac{1}{3}\vec{AB} + \frac{1}{3}\vec{AC} = \frac{1}{3}(-\vec{AB} + \vec{AC}) = \frac{1}{3}(\vec{BA} + \vec{AC}).$$
> D'après Chasles, $\vec{BA} + \vec{AC} = \vec{BC}$.
> D'où :
> $$\vec{PQ} = \frac{1}{3}\vec{BC}.$$
> Le vecteur $\vec{PQ}$ est le produit du vecteur $\vec{BC}$ par le scalaire $\frac{1}{3}$.
> Les vecteurs $\vec{PQ}$ et $\vec{BC}$ sont donc colinéaires, ce qui prouve que les droites $(PQ)$ et $(BC)$ sont strictement parallèles.
> *(Remarque : nous venons de redémontrer vectoriellement le théorème de Thalès !)*

> **Exemple résolu 6 — Le centre de gravité d'un triangle.**
> Soit un triangle $ABC$. Soit $G$ le point défini par l'égalité :
> $$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}.$$
> 1. Soit $A'$ le milieu de $[BC]$. Exprimer $\vec{GB} + \vec{GC}$ en fonction de $\vec{GA'}$.
> 2. En déduire que $G$ appartient à la médiane $(AA')$ et préciser sa position sur le segment.
>
> **Solution :**
> 1. D'après l'identité du milieu démontrée au §3.5, comme $A'$ est le milieu de $[BC]$, on a :
>    $$\vec{GB} + \vec{GC} = 2\vec{GA'}.$$
> 2. Remplaçons dans la relation de départ :
>    $$\vec{GA} + 2\vec{GA'} = \vec{0} \iff \vec{GA} = -2\vec{GA'} \iff -\vec{AG} = -2\vec{GA'} \iff \vec{AG} = 2\vec{GA'}.$$
>    Insérons $G$ dans le membre de droite via Chasles : $\vec{AA'} = \vec{AG} + \vec{GA'} = \vec{AG} + \frac{1}{2}\vec{AG} = \frac{3}{2}\vec{AG}$.
>    On en déduit :
>    $$\vec{AG} = \frac{2}{3}\vec{AA'}.$$
>    Les vecteurs $\vec{AG}$ et $\vec{AA'}$ sont colinéaires : le point $G$ est donc situé sur la droite médiane $(AA')$, aux deux tiers de la longueur en partant du sommet $A$. $G$ est le **centre de gravité** (isobarycentre) du triangle $ABC$.

---

### 7. En informatique : tester la colinéarité en Python

Voici un script Python qui prend les coordonnées de deux vecteurs et teste leur colinéarité à l'aide du déterminant :

```python
def determinant(ux, uy, vx, vy):
    """Calcule le déterminant de deux vecteurs u(ux, uy) et v(vx, vy)."""
    return ux * vy - uy * vx

def sont_colineaires(ux, uy, vx, vy, tolerance=1e-9):
    """Vérifie si deux vecteurs sont colinéaires à une précision donnée."""
    det = determinant(ux, uy, vx, vy)
    return abs(det) < tolerance

# Test avec u(4, 6) et v(6, 9)
print("u et v colinéaires ?", sont_colineaires(4, 6, 6, 9))  # Affiche True

# Test avec u(3, -1) et v(2, 5)
print("u et v colinéaires ?", sont_colineaires(3, -1, 2, 5))  # Affiche False
```

---

### Ce qu'il faut retenir

1. **Vecteur :** entité géométrique caractérisée par une **direction** (droite support), un **sens** (flèche) et une **norme** (longueur $\|\vec{u}\|$).
2. **Égalité vectorielle :** $\vec{AB} = \vec{CD} \iff ABDC$ est un parallélogramme.
3. **Relation de Chasles :** $\vec{AB} + \vec{BC} = \vec{AC}$. Pour soustraire : $\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$ avec $-\vec{AB} = \vec{BA}$.
4. **Milieu $I$ de $[AB]$ :** $\vec{AI} = \vec{IB} \iff \vec{IA} + \vec{IB} = \vec{0} \iff \vec{MA} + \vec{MB} = 2\vec{MI}$.
5. **Coordonnées :**
   - $\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix}$
   - Milieu : $I\left(\frac{x_A+x_B}{2} \,;\, \frac{y_A+y_B}{2}\right)$
   - Norme : $\|\vec{u}\| = \sqrt{x^2+y^2}$ et $AB = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2}$ (en repère orthonormé).
6. **Colinéarité et Déterminant :**
   - $\vec{u}$ et $\vec{v}$ colinéaires $\iff \vec{u} = k\vec{v}$ (ou l'un nul) $\iff \det(\vec{u}, \vec{v}) = xy' - yx' = 0$.
   - Droites parallèles : $(AB) \parallel (CD) \iff \det(\vec{AB}, \vec{CD}) = 0$.
   - Points alignés : $A, B, C$ alignés $\iff \det(\vec{AB}, \vec{AC}) = 0$.

---

### Exercices

#### Exercices d'application directe (★)

1. Soit un parallélogramme $MNOP$. Citer trois paires de vecteurs égaux.
2. Simplifier l'expression $\vec{u} = \vec{RS} + \vec{ST} + \vec{TR}$.
3. Simplifier l'expression $\vec{v} = \vec{AB} - \vec{AC} + \vec{BC}$.
4. Soit un vecteur $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$. Calculer sa norme $\|\vec{u}\|$.
5. On donne $A(2\,; -5)$ et $B(-1\,; 7)$. Calculer les coordonnées du vecteur $\vec{AB}$.
6. Avec les mêmes points $A$ et $B$, calculer les coordonnées du milieu $K$ de $[AB]$.
7. Calculer la distance exacte $AB$.
8. Les vecteurs $\vec{u}\begin{pmatrix} 6 \\ -4 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -9 \\ 6 \end{pmatrix}$ sont-ils colinéaires ?
9. Les vecteurs $\vec{w}\begin{pmatrix} 5 \\ 3 \end{pmatrix}$ et $\vec{z}\begin{pmatrix} 7 \\ 4 \end{pmatrix}$ sont-ils colinéaires ?
10. Trouver le réel $y$ pour que $\vec{a}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ et $\vec{b}\begin{pmatrix} 10 \\ y \end{pmatrix}$ soient colinéaires.

#### Exercices d'entraînement et de réflexion (★★)

11. Soient $A(1\,; 2)$, $B(4\,; 6)$ et $C(-2\,; -2)$. Les points $A$, $B$ et $C$ sont-ils alignés ?
12. Soient quatre points $K(-1\,; 1)$, $L(3\,; 3)$, $M(5\,; 1)$ et $N(1\,; -1)$.
    a) Calculer les coordonnées de $\vec{KL}$ et $\vec{NM}$.
    b) Quelle est la nature précise du quadrilatère $KLMN$ ?
13. Reprendre les points $K, L, M, N$ de l'exercice 12. Calculer les longueurs $KL$ et $LM$. Le quadrilatère est-il un losange ? Un rectangle ?
14. Soit un triangle $ABC$. Construire (ou exprimer) les points $M$ et $N$ définis par :
    $$\vec{AM} = \vec{AB} + 2\vec{AC} \quad \text{et} \quad \vec{AN} = 2\vec{AB} + \vec{AC}.$$
    Exprimer le vecteur $\vec{MN}$ en fonction de $\vec{AB}$ et $\vec{AC}$.
15. Soient les points $A(-2\,; 3)$, $B(4\,; 1)$ et $C(2\,; 5)$.
    Déterminer les coordonnées du point $E$ tel que $\vec{AE} = 2\vec{AB} - 3\vec{BC}$.
16. Soit un triangle quelconque $ABC$. Soit $D$ le symétrique de $A$ par rapport à $B$, et $E$ le symétrique de $B$ par rapport à $C$. Exprimer $\vec{DE}$ en fonction de $\vec{AB}$ et $\vec{BC}$.
17. Pour quelle valeur du réel $x$ les points $P(x\,; 3)$, $Q(2\,; -1)$ et $R(6\,; 7)$ sont-ils alignés ?
18. On donne $\vec{u}\begin{pmatrix} 2 \\ -1 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$. Déterminer les réels $\alpha$ et $\beta$ tels que le vecteur $\vec{w}\begin{pmatrix} 7 \\ 0 \end{pmatrix}$ s'écrive $\vec{w} = \alpha\vec{u} + \beta\vec{v}$.

#### Exercices d'approfondissement et défis (★★★)

19. **Le théorème des milieux vectoriel.**
    Soit $ABC$ un triangle. Soit $I$ le milieu de $[AB]$ et $J$ le milieu de $[AC]$.
    Démontrer par le calcul vectoriel que $\vec{IJ} = \frac{1}{2}\vec{BC}$. En déduire la position relative des droites $(IJ)$ et $(BC)$ ainsi que le rapport de leurs longueurs.
20. **Le quadrilatère de Varignon.**
    Soit un quadrilatère quelconque $ABCD$. On note $I, J, K, L$ les milieux respectifs des côtés $[AB], [BC], [CD], [DA]$.
    a) Exprimer $\vec{IJ}$ et $\vec{LK}$ en fonction des vecteurs des sommets.
    b) En déduire que $IJKL$ est toujours un parallélogramme.
21. **Concours des trois médianes.**
    Soit $ABC$ un triangle. On note $A', B', C'$ les milieux respectifs de $[BC], [CA], [AB]$.
    Soit $G$ le point vérifiant $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$.
    a) Démontrer que pour tout point $M$ du plan : $\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$.
    b) En déduire que $G$ appartient à chacune des trois médianes $(AA')$, $(BB')$ et $(CC')$, et préciser le point de concours.
22. **Trajectoire et dérive d'un avion.**
    Un avion vole avec un cap vers le Nord à une vitesse propre de $600\text{ km/h}$ par rapport à l'air. Un vent violent souffle du Nord-Ouest vers le Sud-Est (à $45^\circ$ par rapport aux axes cardinaux) à la vitesse de $100\sqrt{2}\text{ km/h}$.
    On choisit un repère orthonormé où l'axe des abscisses pointe vers l'Est et l'axe des ordonnées vers le Nord.
    a) Déterminer les composantes du vecteur vitesse propre $\vec{v}_a$ de l'avion.
    b) Déterminer les composantes du vecteur vent $\vec{v}_w$.
    c) Calculer le vecteur vitesse sol $\vec{v}_s = \vec{v}_a + \vec{v}_w$.
    d) En déduire la vitesse réelle de l'avion par rapport au sol et la déviation angulaire de sa trajectoire.

---

### Solutions

1. Dans le parallélogramme $MNOP$ : $\vec{MN} = \vec{PO}$, $\vec{NO} = \vec{MP}$, $\vec{NM} = \vec{OP}$.
2. $\vec{RS} + \vec{ST} + \vec{TR} = \vec{RT} + \vec{TR} = \vec{RR} = \vec{0}$.
3. $\vec{v} = \vec{AB} + \vec{CA} + \vec{BC} = (\vec{CA} + \vec{AB}) + \vec{BC} = \vec{CB} + \vec{BC} = \vec{0}$.
4. $\|\vec{u}\| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
5. $\vec{AB}\begin{pmatrix} -1 - 2 \\ 7 - (-5) \end{pmatrix} = \begin{pmatrix} -3 \\ 12 \end{pmatrix}$.
6. $x_K = \frac{2 + (-1)}{2} = \frac{1}{2} = 0{,}5$ et $y_K = \frac{-5 + 7}{2} = \frac{2}{2} = 1$. Donc $K(0{,}5\,; 1)$.
7. $AB = \sqrt{(-3)^2 + 12^2} = \sqrt{9 + 144} = \sqrt{153} = 3\sqrt{17}$.
8. $\det(\vec{u}, \vec{v}) = 6 \times 6 - (-4) \times (-9) = 36 - 36 = 0$. Oui, ils sont colinéaires (on remarque aussi $\vec{v} = -1{,}5\vec{u}$).
9. $\det(\vec{w}, \vec{z}) = 5 \times 4 - 3 \times 7 = 20 - 21 = -1 \neq 0$. Non, ils ne sont pas colinéaires.
10. $\det(\vec{a}, \vec{b}) = 4y - (-6) \times 10 = 4y + 60 = 0 \iff 4y = -60 \iff y = -15$.
11. $\vec{AB}\begin{pmatrix} 4 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ et $\vec{AC}\begin{pmatrix} -2 - 1 \\ -2 - 2 \end{pmatrix} = \begin{pmatrix} -3 \\ -4 \end{pmatrix}$.
    On remarque immédiatement $\vec{AC} = -1\vec{AB}$ (ou $\det = 3(-4) - 4(-3) = -12 + 12 = 0$). Les vecteurs sont colinéaires et ont le point $A$ en commun, donc $A, B, C$ sont alignés.
12. a) $\vec{KL}\begin{pmatrix} 3 - (-1) \\ 3 - 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$ et $\vec{NM}\begin{pmatrix} 5 - 1 \\ 1 - (-1) \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$.
    b) Puisque $\vec{KL} = \vec{NM}$, le quadrilatère $KLMN$ est un parallélogramme.
13. Longueur $KL = \sqrt{4^2 + 2^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$.
    Calculons $\vec{LM}\begin{pmatrix} 5 - 3 \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix}$.
    Longueur $LM = \sqrt{2^2 + (-2)^2} = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}$.
    Comme $KL \neq LM$, les côtés consécutifs ne sont pas de même longueur : ce n'est pas un losange.
    Vérifions si les côtés sont perpendiculaires : $KM^2$ avec $\vec{KM}\begin{pmatrix} 5 - (-1) \\ 1 - 1 \end{pmatrix} = \begin{pmatrix} 6 \\ 0 \end{pmatrix} \implies KM^2 = 36$.
    Or $KL^2 + LM^2 = 20 + 8 = 28 \neq 36$. Le triangle $KLM$ n'est pas rectangle, donc $KLMN$ n'est pas un rectangle. C'est un parallélogramme quelconque.
14. Par Chasles : $\vec{MN} = \vec{MA} + \vec{AN} = -\vec{AM} + \vec{AN}$.
    En remplaçant : $\vec{MN} = -(\vec{AB} + 2\vec{AC}) + (2\vec{AB} + \vec{AC}) = -\vec{AB} - 2\vec{AC} + 2\vec{AB} + \vec{AC} = \vec{AB} - \vec{AC} = \vec{CB}$.
15. $\vec{AB}\begin{pmatrix} 4 - (-2) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -2 \end{pmatrix}$ et $\vec{BC}\begin{pmatrix} 2 - 4 \\ 5 - 1 \end{pmatrix} = \begin{pmatrix} -2 \\ 4 \end{pmatrix}$.
    Alors $\vec{AE} = 2\vec{AB} - 3\vec{BC} = 2\begin{pmatrix} 6 \\ -2 \end{pmatrix} - 3\begin{pmatrix} -2 \\ 4 \end{pmatrix} = \begin{pmatrix} 12 + 6 \\ -4 - 12 \end{pmatrix} = \begin{pmatrix} 18 \\ -16 \end{pmatrix}$.
    Comme $A$ a pour coordonnées $(-2\,; 3)$, on a :
    $x_E = x_A + 18 = -2 + 18 = 16$ et $y_E = y_A - 16 = 3 - 16 = -13$. Donc $E(16\,; -13)$.
16. $D$ symétrique de $A$ par rapport à $B \implies \vec{BD} = \vec{AB}$.
    $E$ symétrique de $B$ par rapport à $C \implies \vec{BE} = 2\vec{BC}$.
    Par Chasles : $\vec{DE} = \vec{DB} + \vec{BE} = -\vec{BD} + \vec{BE} = -\vec{AB} + 2\vec{BC}$.
17. $\vec{QR}\begin{pmatrix} 6 - 2 \\ 7 - (-1) \end{pmatrix} = \begin{pmatrix} 4 \\ 8 \end{pmatrix}$.
    $\vec{QP}\begin{pmatrix} x - 2 \\ 3 - (-1) \end{pmatrix} = \begin{pmatrix} x - 2 \\ 4 \end{pmatrix}$.
    $P, Q, R$ alignés $\iff \det(\vec{QR}, \vec{QP}) = 0 \iff 4 \times 4 - 8(x - 2) = 0 \iff 16 - 8x + 16 = 0 \iff 8x = 32 \iff x = 4$.
18. L'égalité $\vec{w} = \alpha\vec{u} + \beta\vec{v}$ donne le système :
    $$\begin{cases} 2\alpha + \beta = 7 \\ -\alpha + 3\beta = 0 \end{cases}$$
    De la seconde équation, $\alpha = 3\beta$. En injectant dans la première : $2(3\beta) + \beta = 7 \iff 7\beta = 7 \iff \beta = 1$.
    D'où $\alpha = 3 \times 1 = 3$. Solution : $\alpha = 3, \beta = 1$.
19. $I$ milieu de $[AB] \implies \vec{AI} = \frac{1}{2}\vec{AB}$, donc $\vec{IA} = -\frac{1}{2}\vec{AB}$.
    $J$ milieu de $[AC] \implies \vec{AJ} = \frac{1}{2}\vec{AC}$.
    Par Chasles : $\vec{IJ} = \vec{IA} + \vec{AJ} = -\frac{1}{2}\vec{AB} + \frac{1}{2}\vec{AC} = \frac{1}{2}(\vec{BA} + \vec{AC}) = \frac{1}{2}\vec{BC}$.
    Puisque $\vec{IJ} = \frac{1}{2}\vec{BC}$, les vecteurs sont colinéaires, donc les droites $(IJ)$ et $(BC)$ sont parallèles. En prenant les normes, $IJ = \frac{1}{2}BC$.
20. a) Dans le triangle $ABC$, par le théorème des milieux vectoriel (ex. 19), $\vec{IJ} = \frac{1}{2}\vec{AC}$.
    Dans le triangle $ADC$, $L$ est le milieu de $[AD]$ et $K$ le milieu de $[CD]$. Donc $\vec{LK} = \frac{1}{2}\vec{AC}$.
    b) On constate que $\vec{IJ} = \vec{LK}$. Un quadrilatère dont deux côtés opposés forment des vecteurs égaux est un parallélogramme. Donc $IJKL$ est toujours un parallélogramme.
21. a) Soit $M$ un point quelconque. Par Chasles : $\vec{MA} + \vec{MB} + \vec{MC} = (\vec{MG} + \vec{GA}) + (\vec{MG} + \vec{GB}) + (\vec{MG} + \vec{GC}) = 3\vec{MG} + (\vec{GA} + \vec{GB} + \vec{GC}) = 3\vec{MG} + \vec{0} = 3\vec{MG}$.
    b) Choisissons $M = A'$ (milieu de $[BC]$). Alors $\vec{A'A} + \vec{A'B} + \vec{A'C} = 3\vec{A'G}$.
    Comme $A'$ est le milieu de $[BC]$, $\vec{A'B} + \vec{A'C} = \vec{0}$.
    L'égalité devient $\vec{A'A} = 3\vec{A'G}$, ou encore $\vec{AG} = \frac{2}{3}\vec{AA'}$.
    Le point $G$ est donc situé sur la médiane $(AA')$, aux deux tiers à partir du sommet. En choisissant $M = B'$ puis $M = C'$, on obtient de même $\vec{BG} = \frac{2}{3}\vec{BB'}$ et $\vec{CG} = \frac{2}{3}\vec{CC'}$. Le point $G$ est donc le point d'intersection unique des trois médianes.
22. a) L'avion vole plein Nord ($x = 0$) à $600\text{ km/h}$ : $\vec{v}_a\begin{pmatrix} 0 \\ 600 \end{pmatrix}$.
    b) Le vent vient du Nord-Ouest et souffle vers le Sud-Est (angle $-45^\circ$, donc composante $x$ positive vers l'Est, composante $y$ négative vers le Sud).
    Sa vitesse est $100\sqrt{2}$. Comme $\cos(45^\circ) = \sin(45^\circ) = \frac{\sqrt{2}}{2}$, on a :
    $v_{wx} = 100\sqrt{2} \times \frac{\sqrt{2}}{2} = 100$, et $v_{wy} = -100$.
    Donc $\vec{v}_w\begin{pmatrix} 100 \\ -100 \end{pmatrix}$.
    c) Vitesse sol : $\vec{v}_s = \vec{v}_a + \vec{v}_w = \begin{pmatrix} 0 + 100 \\ 600 - 100 \end{pmatrix} = \begin{pmatrix} 100 \\ 500 \end{pmatrix}$.
    d) Vitesse réelle de l'avion : $\|\vec{v}_s\| = \sqrt{100^2 + 500^2} = \sqrt{10000 + 250000} = \sqrt{260000} \approx 509{,}9\text{ km/h}$.
    Déviation angulaire $\theta$ vers l'Est : $\tan\theta = \frac{100}{500} = 0{,}2 \implies \theta \approx 11{,}3^\circ$. L'avion est dévié de plus de $11^\circ$ vers la droite et a perdu près de $90\text{ km/h}$ par rapport au sol !

---

### La question qui ouvre la suite

Nous avons appris à faire glisser des flèches libres dans tout le plan et à repérer si deux flèches pointent dans la même direction grâce au déterminant. Mais que se passe-t-il si l'on plante un piquet en un point $A$ et qu'on laisse une flèche $\vec{u}$ indiquer une trajectoire infinie ? On obtient une **droite**.

Comment caractériser l'ensemble de tous les points alignés le long de cette ligne de mire ? Comment relier l'équation d'une droite à ses vecteurs directeurs, et comment déterminer le point exact où deux trajectoires se croisent ? C'est ce que nous allons découvrir dans **La Ligne de Mire**.
