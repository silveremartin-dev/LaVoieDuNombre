# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 38 : Tirer la Corde et l'Ombre Efficace

> *« Quand tu tires un fardeau avec une corde oblique, tes muscles brûlent, ton front ruisselle de sueur, et pourtant la charge avance à pas de tortue. Pourquoi ? Parce que l'univers ne te récompense pas pour la peine dépensée dans le vide : il ne compte que l'ombre utile de ta force sur le chemin. »*

---

### Ce que tu vas découvrir

- Pourquoi la multiplication usuelle entre deux nombres ne suffit pas quand on veut multiplier **deux flèches** (deux vecteurs).
- Le sens physique du **travail d'une force** et la découverte du **produit scalaire**.
- La géométrie du **projeté orthogonal** : comment faire tomber la lumière d'en haut pour mesurer l'ombre efficace.
- Les quatre visages du produit scalaire : par le **cosinus**, par la **projection**, par les **coordonnées cartésiennes** ($xx' + yy'$), et par les **longueurs seules** (formes de polarisation).
- Le critère absolu d'**orthogonalité** et son application reine : trouver le vecteur normal d'une droite et son équation cartésienne $ax + by + c = 0$.
- Les théorèmes puissants du triangle : la formule d'**Al-Kashi** (Pythagore généralisé) et le **théorème de la médiane**.
- La recherche des **ensembles de points** : caractériser un cercle par le produit scalaire $\vec{MA} \cdot \vec{MB} = 0$.

---

### 1. Le problème : le cheval de halage et la péniche de charbon

Au début du XIXᵉ siècle, au cœur de la Révolution industrielle, le charbon est le sang qui alimente les machines à vapeur. Pour acheminer des milliers de tonnes de houille depuis les mines du Nord jusqu'aux usines de Paris ou de Londres, le réseau fluvial est le moyen le plus économique. De lourdes péniches ventrues, pesant plus de cent tonnes, glissent silencieusement sur les canaux.

Ces péniches n'ont pas encore de moteur. Elles sont remorquées depuis la terre ferme par un puissant cheval de trait ardennais marchant d'un pas lourd sur le chemin de terre qui longe le canal : le **chemin de halage**.

Regarde la scène depuis une passerelle au-dessus de l'eau :

```
                        Chemin de halage
   Cheval  o══════════════════════════════════════════════════════►
            \
             \  Corde de chanvre tendue
              \  Force musculaire F (angle θ)
               \
                \
                 o────────────────────────────────────────────────►
              Péniche       Déplacement d rectiligne le long du canal
```

Le canal est rectiligne. La péniche glisse tout droit le long d'un vecteur de déplacement $\vec{d}$.
Mais le cheval ne peut pas marcher sur l'eau ! Il est contraint d'avancer sur la berge. La longue corde de chanvre fait donc un **angle $\theta$ en biais** par rapport à la direction du canal.

Le cheval bande ses jarrets, son sabot s'enfonce dans la glaise, son poitrail écrase le collier de cuir : il déploie une force considérable $\vec{F}$.
Et pourtant, un jeune apprenti batelier assis sur le gouvernail constate quelque chose de troublant :
*« Le cheval s'épuise, et pourtant le bateau n'avance que très lentement. Pourquoi ? »*

Le marinier expérimenté lui répond :
*« Parce qu'une partie de sa force tire le bateau vers la berge ! Cette partie-là ne fait rien avancer du tout : elle tente seulement d'échouer la péniche dans les roseaux. Je dois constamment lutter contre elle en poussant sur la barre du gouvernail. Seule la partie de la force qui pointe droit devant, parallèlement à l'eau, produit le mouvement utile. »*

```
                 F (effort total déployé)
                ▲
               /│
              / │
             /  │  Composante latérale perdue (tire vers la berge)
            /   │
           /θ   │
          o─────┴────────────────────────────────► Canal (déplacement d)
          |◄─── Ombre efficace ───►|
              ||F|| × cos(θ)
```

Pour mesurer l'énergie réellement transmise au bateau, il ne suffit pas de multiplier la force par la distance. Il faut **extraire l'ombre efficace de la force dans la direction du mouvement**.

---

### 2. Le travail d'une force et la définition géométrique

#### 2.1 Du geste physique au produit scalaire

En physique, lorsqu'un objet subit une force constante $\vec{F}$ lors d'un déplacement rectiligne $\vec{d} = \vec{AB}$, l'énergie mécanique transmise s'appelle le **travail de la force**, noté $W$ (de l'anglais *Work*).

Si la force était parfaitement alignée avec le déplacement ($\theta = 0$), toute la force contribuerait au mouvement : $W = \|\vec{F}\| \times \|\vec{d}\|$.
Mais lorsque la corde est inclinée d'un angle $\theta$, l'ombre efficace de la force vaut $\|\vec{F}\| \cos\theta$. Le travail s'écrit alors :

$$W = \|\vec{F}\| \times \|\vec{d}\| \times \cos\theta.$$

Pour formaliser cette opération mathématique qui combine deux vecteurs $\vec{u}$ et $\vec{v}$ pour fabriquer **un simple nombre réel** (un scalaire, par opposition à un vecteur), les mathématiciens ont forgé un concept universel.

> **📐 Définition — Produit scalaire (par la norme et le cosinus)**
> Soient $\vec{u}$ et $\vec{v}$ deux vecteurs du plan.
> - Si l'un des deux vecteurs est nul ($\vec{u} = \vec{0}$ ou $\vec{v} = \vec{0}$), leur produit scalaire est nul : $\vec{u} \cdot \vec{v} = 0$.
> - Si $\vec{u} \neq \vec{0}$ et $\vec{v} \neq \vec{0}$, on pose $\vec{u} = \vec{OA}$ et $\vec{v} = \vec{OB}$. Le **produit scalaire** de $\vec{u}$ et $\vec{v}$, noté $\vec{u} \cdot \vec{v}$, est le nombre réel défini par :
>
> $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\widehat{AOB}).$$

**Lecture et prononciation :**
$\vec{u} \cdot \vec{v}$ se lit « **$\vec{u}$ scalaire $\vec{v}$** ». Le point médian « $\cdot$ » est réservé à cette opération.

> **🔍 L'histoire vraie — D'où vient le mot « scalaire » ?**
> Le mot vient du latin *scala*, qui signifie « échelle », « degré ». C'est le mathématicien irlandais **William Rowan Hamilton** qui l'introduit en 1843 lorsqu'il invente les quaternions : il appelle « partie scalaire » la partie numérique pure qui se gradue sur une échelle ordinaire de nombres, par opposition à la « partie vectorielle » dotée d'une direction dans l'espace. Le produit scalaire moderne tel qu'on l'écrit avec un point a été popularisé par le physicien américain **Josiah Willard Gibbs** à la fin du XIXᵉ siècle.

#### 2.2 Les trois régimes de la corde

La valeur du produit scalaire dépend de l'angle $\theta$ formé par les deux vecteurs :

1. **Angle aigu ($0 \leqslant \theta < \frac{\pi}{2}$) : produit scalaire strictement positif.**
   $\cos\theta > 0$. La force aide le déplacement : les physiciens parlent de **travail moteur**. L'ombre tombe dans le sens de la marche.
2. **Angle droit ($\theta = \frac{\pi}{2}$, soit $90^\circ$) : produit scalaire nul.**
   $\cos\left(\frac{\pi}{2}\right) = 0$, donc $\vec{u} \cdot \vec{v} = 0$.
   Si le cheval tire à angle droit de la rive, le bateau n'avance pas d'un millimètre dans le canal. Toute son énergie part à tenter de casser la berge.
3. **Angle obtus ($\frac{\pi}{2} < \theta \leqslant \pi$) : produit scalaire strictement négatif.**
   $\cos\theta < 0$. La force s'oppose au déplacement : c'est le rôle des freins ou des frottements de l'eau, que les physiciens nomment **travail résistant**.

```
    θ aigu : u · v > 0            θ = 90° : u · v = 0           θ obtus : u · v < 0
       v                             v                               v
      ▲                             ▲                                 ▲
     /                             │                                   \
    /  θ                          │                                 θ   \
   o───────► u                    o───────► u                    ◄───────o
   Travail moteur                Travail nul                     u   Travail résistant
```

> **⚠️ Attention, piège ! — Scalaire n'est pas vecteur**
> Le produit scalaire de deux vecteurs n'est **jamais un vecteur** ! C'est un **nombre réel** (qui peut être positif, nul ou négatif). Écrire $\vec{u} \cdot \vec{v} = \vec{0}$ avec une flèche sur le zéro est une erreur grossière de notation. On écrit $\vec{u} \cdot \vec{v} = 0$.

---

### 3. Le projeté orthogonal : mesurer l'ombre portée

#### 3.1 Définition par la projection

Au lieu de calculer un cosinus, il est souvent bien plus rapide de faire tomber la perpendiculaire.

> **📐 Propriété — Définition par projection orthogonale**
> Soient $\vec{u} = \vec{OA}$ et $\vec{v} = \vec{OB}$ deux vecteurs non nuls.
> Soit $H$ le projeté orthogonal du point $B$ sur la droite $(OA)$.
>
> $$\vec{u} \cdot \vec{v} = \vec{OA} \cdot \vec{OB} = \vec{OA} \cdot \vec{OH}.$$
>
> En mesures algébriques orientées par l'axe $(OA)$ :
> - Si $\vec{OH}$ et $\vec{OA}$ ont le **même sens** (angle aigu) : $\vec{u} \cdot \vec{v} = OA \times OH$.
> - Si $\vec{OH}$ et $\vec{OA}$ ont des **sens contraires** (angle obtus) : $\vec{u} \cdot \vec{v} = - OA \times OH$.

```
    Cas 1 : Même sens                      Cas 2 : Sens contraires
           B                                            B
          /│                                            │\
         / │                                            │ \
        /  │                                            │  \
       o───┴─────────►                               ───┴───o────────►
       O   H         A                                  H   O        A
       u · v = + OA × OH                                u · v = - OA × OH
```

> **✍️ Démonstration**
> Dans le triangle $OHB$ rectangle en $H$ :
> - Si l'angle $\widehat{AOB}$ est aigu, $\cos(\widehat{AOB}) = \frac{OH}{OB}$, donc $OH = OB \cos(\widehat{AOB})$.
>   Ainsi, $\vec{OA} \cdot \vec{OB} = OA \times OB \cos(\widehat{AOB}) = OA \times OH$.
> - Si l'angle $\widehat{AOB}$ est obtus, le projeté $H$ est situé de l'autre côté de $O$. L'angle adjacent dans le triangle rectangle est $\pi - \widehat{AOB}$.
>   Comme $\cos(\pi - \theta) = -\cos\theta$, on a $OH = OB \cos(\pi - \widehat{AOB}) = -OB \cos(\widehat{AOB})$.
>   Par suite, $OA \times OB \cos(\widehat{AOB}) = -OA \times OH$.
> Dans les deux cas, le résultat correspond exactement à l'expression annoncée. $\blacksquare$

> **💡 Le savais-tu ? — La symétrie du produit scalaire**
> Projeter $B$ sur $(OA)$ donne le même résultat que projeter $A$ sur $(OB)$ !
> En effet, $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta = \|\vec{v}\| \|\vec{u}\| \cos\theta = \vec{v} \cdot \vec{u}$.
> Le produit scalaire est **commutatif**.

#### 3.2 Le carré scalaire

Que se passe-t-il si l'on calcule le produit scalaire d'un vecteur avec lui-même ?
L'angle entre $\vec{u}$ et $\vec{u}$ est nul ($\theta = 0$), et $\cos(0) = 1$.

> **📐 Définition — Carré scalaire**
> Pour tout vecteur $\vec{u}$, on note $\vec{u}^2 = \vec{u} \cdot \vec{u}$. On a :
>
> $$\vec{u}^2 = \|\vec{u}\|^2.$$
>
> Le carré scalaire d'un vecteur est égal au carré de sa norme. C'est un réel **positif ou nul**, et $\vec{u}^2 = 0 \iff \vec{u} = \vec{0}$.
> Pour un segment géométrique $[AB]$, on a $\vec{AB}^2 = AB^2$.

---

### 4. L'expression analytique en repère orthonormé

#### 4.1 La formule $xx' + yy'$

Lorsque le plan est muni d'un repère orthonormé $(O; \vec{i}, \vec{j})$, les vecteurs de base vérifient :
- $\|\vec{i}\| = 1$ et $\|\vec{j}\| = 1$, donc $\vec{i}^2 = 1$ et $\vec{j}^2 = 1$.
- $\vec{i}$ et $\vec{j}$ sont perpendiculaires, donc $\vec{i} \cdot \vec{j} = 0$.

C'est ici que la magie de l'algèbre simplifie tous les calculs géométriques :

> **📐 Théorème — Formule analytique du produit scalaire**
> Dans un repère **orthonormé** $(O; \vec{i}, \vec{j})$, si $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$, alors :
>
> $$\boxed{\vec{u} \cdot \vec{v} = xx' + yy'}$$

> **✍️ Démonstration**
> Par bilinéarité du produit scalaire (développons comme un produit usuel) :
> $$\begin{aligned}
> \vec{u} \cdot \vec{v} &= (x\vec{i} + y\vec{j}) \cdot (x'\vec{i} + y'\vec{j}) \\
> &= xx'(\vec{i} \cdot \vec{i}) + xy'(\vec{i} \cdot \vec{j}) + yx'(\vec{j} \cdot \vec{i}) + yy'(\vec{j} \cdot \vec{j}).
> \end{aligned}$$
> Or $\vec{i} \cdot \vec{i} = 1$, $\vec{j} \cdot \vec{j} = 1$ et $\vec{i} \cdot \vec{j} = \vec{j} \cdot \vec{i} = 0$.
> Les deux termes croisés s'annulent complètement ! Il reste :
> $$\vec{u} \cdot \vec{v} = xx'(1) + 0 + 0 + yy'(1) = xx' + yy'. \quad \blacksquare$$

> **⚠️ Attention, piège ! — Repère impérativement orthonormé**
> La formule $\vec{u} \cdot \vec{v} = xx' + yy'$ est **fausse** si les axes ne sont pas perpendiculaires ou si les unités sur les deux axes sont différentes ! Elle n'est vraie que dans un repère **orthonormé**.

---

### 5. Les formes de polarisation : calculer avec les normes seules

Peut-on connaître le produit scalaire de deux vecteurs sans connaître ni leurs coordonnées, ni l'angle entre eux, mais uniquement la longueur des tiges qui les composent ?
Oui, grâce aux **identités remarquables vectorielles**.

Pour tous vecteurs $\vec{u}$ et $\vec{v}$ :
$$\|\vec{u} + \vec{v}\|^2 = (\vec{u} + \vec{v})^2 = \vec{u}^2 + 2\vec{u}\cdot\vec{v} + \vec{v}^2 = \|\vec{u}\|^2 + 2\vec{u}\cdot\vec{v} + \|\vec{v}\|^2.$$

En isolant le produit scalaire $\vec{u} \cdot \vec{v}$, on obtient la célèbre formule de polarisation :

> **📐 Théorème — Formes de polarisation**
> Pour tous vecteurs $\vec{u}$ et $\vec{v}$ :
>
> 1. $\vec{u} \cdot \vec{v} = \frac{1}{2}\left( \|\vec{u} + \vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2 \right)$
> 2. $\vec{u} \cdot \vec{v} = \frac{1}{2}\left( \|\vec{u}\|^2 + \|\vec{v}\|^2 - \|\vec{u} - \vec{v}\|^2 \right)$
> 3. $\vec{u} \cdot \vec{v} = \frac{1}{4}\left( \|\vec{u} + \vec{v}\|^2 - \|\vec{u} - \vec{v}\|^2 \right)$

Dans un triangle $ABC$ avec $\vec{u} = \vec{AB}$ et $\vec{v} = \vec{AC}$, on remarque que $\vec{u} - \vec{v} = \vec{AB} - \vec{AC} = \vec{CB}$.
La deuxième formule devient :

$$\vec{AB} \cdot \vec{AC} = \frac{1}{2}\left( AB^2 + AC^2 - BC^2 \right).$$

C'est une passerelle directe entre les longueurs des trois côtés d'un triangle et le produit scalaire !

---

### 6. Orthogonalité, vecteur normal et équation de droite

#### 6.1 Le critère d'orthogonalité

> **📐 Théorème fondamental de l'orthogonalité**
> Deux vecteurs $\vec{u}$ et $\vec{v}$ sont orthogonaux si et seulement si :
>
> $$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0.$$
>
> Dans un repère orthonormé avec $\vec{u}(x;y)$ et $\vec{v}(x';y')$ :
>
> $$\vec{u} \perp \vec{v} \iff xx' + yy' = 0.$$

#### 6.2 Vecteur normal à une droite

En Seconde, une droite était caractérisée par un point et un *vecteur directeur* $\vec{u}$ parallèle à la droite.
En Première, le produit scalaire permet une approche bien plus commode : caractériser la droite par une flèche qui lui est **perpendiculaire**.

> **📐 Définition — Vecteur normal**
> Un vecteur non nul $\vec{n}$ est dit **normal** à une droite $(d)$ s'il est orthogonal à tout vecteur directeur de $(d)$.

```
                     ▲ n (vecteur normal)
                     │
                     │
           ──────────┼──────M─────────────────► Droite (d)
                     A      AM ⟂ n
```

Un point $M(x;y)$ appartient à la droite $(d)$ passant par $A(x_A; y_A)$ et de vecteur normal $\vec{n}(a; b)$ si et seulement si :

$$\vec{AM} \cdot \vec{n} = 0 \iff a(x - x_A) + b(y - y_A) = 0 \iff ax + by + (-ax_A - by_A) = 0.$$

En posant $c = -ax_A - by_A$, on retrouve l'équation cartésienne !

> **📐 Théorème — Équation cartésienne et vecteur normal**
> - Dans un repère orthonormé, toute droite ayant pour vecteur normal $\vec{n}\begin{pmatrix} a \\ b \end{pmatrix}$ admet une équation cartésienne de la forme :
>
> $$ax + by + c = 0 \quad (\text{avec } (a; b) \neq (0; 0)).$$
>
> - Réciproquement, toute équation $ax + by + c = 0$ avec $(a;b) \neq (0;0)$ est l'équation d'une droite de vecteur normal $\vec{n}\begin{pmatrix} a \\ b \end{pmatrix}$.

---

### 7. Les deux grands théorèmes métriques du triangle

#### 7.1 Le théorème d'Al-Kashi (loi des cosinus)

Dans un triangle quelconque $ABC$, si l'angle $\widehat{A}$ n'est pas droit, que devient le théorème de Pythagore ?

> **📐 Théorème d'Al-Kashi (ou de Pythagore généralisé)**
> Soit un triangle $ABC$. En notant $a = BC$, $b = AC$, $c = AB$ et $\widehat{A} = \widehat{BAC}$ :
>
> $$a^2 = b^2 + c^2 - 2bc \cos\widehat{A}.$$
>
> De même pour les autres sommets :
> $$b^2 = a^2 + c^2 - 2ac \cos\widehat{B}, \qquad c^2 = a^2 + b^2 - 2ab \cos\widehat{C}.$$

```
                     A
                    / \
                c  /   \  b
                  /  Â  \
                 B───────C
                     a
```

> **✍️ Démonstration géométrique par le produit scalaire**
> Écrivons la relation de Chasles pour le vecteur $\vec{BC}$ :
> $\vec{BC} = \vec{BA} + \vec{AC} = \vec{AC} - \vec{AB}$.
> Élevons au carré scalaire :
> $$BC^2 = \|\vec{BC}\|^2 = \|\vec{AC} - \vec{AB}\|^2 = \|\vec{AC}\|^2 - 2\vec{AC}\cdot\vec{AB} + \|\vec{AB}\|^2.$$
> Or $\|\vec{AC}\| = b$, $\|\vec{AB}\| = c$, et $\vec{AB}\cdot\vec{AC} = AB \times AC \cos\widehat{A} = bc\cos\widehat{A}$.
> On remplace :
> $$a^2 = b^2 + c^2 - 2bc \cos\widehat{A}. \quad \blacksquare$$

Remarque la beauté de la formule : si $\widehat{A} = 90^\circ$, alors $\cos(90^\circ) = 0$, et le terme correctif $-2bc\cos\widehat{A}$ disparaît : on retrouve exactement le théorème de Pythagore $a^2 = b^2 + c^2$ ! Al-Kashi contient Pythagore comme un cas particulier.

> **🔍 L'histoire vraie — Ghiyath al-Din Jamshid al-Kashi**
> Astronome et mathématicien persan du XVᵉ siècle, Al-Kashi travaillait à l'observatoire de Samarcande sous la protection du prince Ulugh Beg. Dans son chef-d'œuvre, *La Clé de l'Arithmétique* (1427), il calcule $\pi$ avec 16 décimales exactes (un record mondial qui tiendra deux siècles) et établit des tables trigonométriques d'une précision inouïe. La formule qui porte aujourd'hui son nom en France permettait aux astronomes de résoudre n'importe quel triangle sans avoir besoin de le découper en triangles rectangles.

#### 7.2 Le théorème de la médiane

Considérons un triangle $ABC$ et désignons par $I$ le **milieu** du segment $[BC]$. Comment relier la longueur de la médiane $AI$ aux longueurs des trois côtés ?

> **📐 Théorème de la médiane**
> Dans tout triangle $ABC$, si $I$ est le milieu du segment $[BC]$, alors :
>
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2.$$

```
                     A
                    /│\
                   / │ \
                c /  │  \ b
                 /   │   \
                B────I────C
                   a/2 a/2
```

> **✍️ Démonstration**
> Exprimons les vecteurs $\vec{AB}$ et $\vec{AC}$ en passant par le milieu $I$ :
> $\vec{AB} = \vec{AI} + \vec{IB}$ et $\vec{AC} = \vec{AI} + \vec{IC}$.
> Élevons au carré scalaire :
> $$AB^2 = \|\vec{AI} + \vec{IB}\|^2 = AI^2 + 2\vec{AI}\cdot\vec{IB} + IB^2,$$
> $$AC^2 = \|\vec{AI} + \vec{IC}\|^2 = AI^2 + 2\vec{AI}\cdot\vec{IC} + IC^2.$$
> Additionnons membre à membre ces deux égalités :
> $$AB^2 + AC^2 = 2AI^2 + 2\vec{AI}\cdot(\vec{IB} + \vec{IC}) + IB^2 + IC^2.$$
> Or $I$ est le milieu de $[BC]$, donc $\vec{IB} + \vec{IC} = \vec{0}$ ! Le terme central s'annule complètement.
> De plus, $IB = IC = \frac{BC}{2}$, donc $IB^2 + IC^2 = \left(\frac{BC}{2}\right)^2 + \left(\frac{BC}{2}\right)^2 = 2\frac{BC^2}{4} = \frac{1}{2}BC^2$.
> Il vient immédiatement :
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2. \quad \blacksquare$$

---

### 8. Ensembles de points et équations de cercles

Le produit scalaire offre une méthode d'une élégance absolue pour trouver la formule algébrique d'un cercle.

#### 8.1 Cercle défini par son centre et son rayon

Un point $M(x;y)$ appartient au cercle $\mathcal{C}$ de centre $\Omega(x_\Omega; y_\Omega)$ et de rayon $R$ si et seulement si la distance $\Omega M$ vaut $R$ :

$$\Omega M^2 = R^2 \iff (x - x_\Omega)^2 + (y - y_\Omega)^2 = R^2.$$

#### 8.2 Cercle défini par un diamètre $[AB]$

Rappelle-toi du collège : un triangle inscrit dans un cercle ayant pour hypoténuse le diamètre est un **triangle rectangle**.
Autrement dit : un point $M$ (distinct de $A$ et $B$) appartient au cercle de diamètre $[AB]$ si et seulement si l'angle $\widehat{AMB}$ est droit, ce qui équivaut vectoriellement à :

$$\vec{MA} \cdot \vec{MB} = 0.$$

(Remarque : si $M = A$ ou $M = B$, l'un des vecteurs est nul, le produit scalaire est encore nul, donc la relation reste vraie en tout point du cercle).

> **📐 Théorème — Équation d'un cercle de diamètre $[AB]$**
> Le cercle de diamètre $[AB]$, avec $A(x_A; y_A)$ et $B(x_B; y_B)$, est l'ensemble des points $M(x;y)$ vérifiant :
>
> $$\vec{MA} \cdot \vec{MB} = 0 \iff (x_A - x)(x_B - x) + (y_A - y)(y_B - y) = 0,$$
> ou encore :
> $$\boxed{(x - x_A)(x - x_B) + (y - y_A)(y - y_B) = 0}$$

---

### Exemples résolus pas à pas

> **✅ Exemple résolu 1 — Calcul de produit scalaire sous plusieurs formes**
> Soit un carré $ABCD$ de côté 4 et de centre $O$.
> Calculer les produits scalaires suivants :
> 1. $\vec{AB} \cdot \vec{AC}$
> 2. $\vec{AB} \cdot \vec{AD}$
> 3. $\vec{AB} \cdot \vec{CD}$
> 4. $\vec{OA} \cdot \vec{OB}$
>
> **Solution détaillée :**
> 1. Par projeté orthogonal : Le projeté orthogonal de $C$ sur la droite $(AB)$ est le point $B$. Donc $\vec{AB} \cdot \vec{AC} = \vec{AB} \cdot \vec{AB} = AB^2 = 4^2 = 16$.
> 2. Par orthogonalité : Dans un carré, $(AB) \perp (AD)$, donc l'angle est droit : $\vec{AB} \cdot \vec{AD} = 0$.
> 3. Vecteurs colinéaires de sens contraires : $\vec{CD} = -\vec{AB}$. Donc $\vec{AB} \cdot \vec{CD} = -AB^2 = -16$.
> 4. Dans un carré, les diagonales se coupent perpendiculairement en leur milieu $O$, donc $(OA) \perp (OB)$. Ainsi, $\vec{OA} \cdot \vec{OB} = 0$.

> **✅ Exemple résolu 2 — Calcul d'un angle avec les coordonnées**
> Dans un repère orthonormé, on donne trois points : $A(1; 2)$, $B(4; 6)$ et $C(-2; 6)$.
> Calculer l'angle $\widehat{BAC}$ au dixième de degré près.
>
> **Solution détaillée :**
> Calculons les coordonnées des vecteurs $\vec{AB}$ et $\vec{AC}$ :
> - $\vec{AB}\begin{pmatrix} 4 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ ;
> - $\vec{AC}\begin{pmatrix} -2 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$.
>
> 1. Produit scalaire analytique :
>    $\vec{AB} \cdot \vec{AC} = xx' + yy' = 3 \times (-3) + 4 \times 4 = -9 + 16 = 7$.
> 2. Calcul des normes :
>    $\|\vec{AB}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
>    $\|\vec{AC}\| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
> 3. Extraction du cosinus :
>    $\vec{AB} \cdot \vec{AC} = \|\vec{AB}\| \times \|\vec{AC}\| \times \cos\widehat{BAC}$,
>    donc $7 = 5 \times 5 \times \cos\widehat{BAC} = 25 \cos\widehat{BAC}$, d'où $\cos\widehat{BAC} = \frac{7}{25} = 0{,}28$.
> 4. À la calculatrice : $\widehat{BAC} = \arccos(0{,}28) \approx 73{,}7^\circ$.

> **✅ Exemple résolu 3 — Équation cartésienne à l'aide d'un vecteur normal**
> Déterminer une équation cartésienne de la droite $(d)$ passant par le point $A(3; -1)$ et perpendiculaire à la droite $(\Delta)$ d'équation $2x - 5y + 7 = 0$.
>
> **Solution détaillée :**
> - La droite $(\Delta)$ a pour vecteur normal $\vec{n_\Delta}\begin{pmatrix} 2 \\ -5 \end{pmatrix}$.
> - Comme $(d)$ est perpendiculaire à $(\Delta)$, un vecteur normal à $(\Delta)$ est un **vecteur directeur** de $(d)$.
>   Donc $\vec{u}_d = \begin{pmatrix} 2 \\ -5 \end{pmatrix}$.
> - Un vecteur normal à $(d)$ doit être orthogonal à $\vec{u}_d$. Le vecteur $\vec{n}_d\begin{pmatrix} 5 \\ 2 \end{pmatrix}$ convient parfaitement car $2 \times 5 + (-5) \times 2 = 10 - 10 = 0$.
> - L'équation de $(d)$ est donc de la forme $5x + 2y + c = 0$.
> - Comme $A(3; -1) \in (d)$, ses coordonnées vérifient l'équation :
>   $5(3) + 2(-1) + c = 0 \iff 15 - 2 + c = 0 \iff 13 + c = 0 \iff c = -13$.
> - L'équation cartésienne de $(d)$ est donc : $\boxed{5x + 2y - 13 = 0}$.

> **✅ Exemple résolu 4 — Calcul de longueur et d'angle par Al-Kashi**
> Un géomètre observe un terrain triangulaire $ABC$. Il mesure $AB = 60$ m, $AC = 100$ m et l'angle $\widehat{BAC} = 60^\circ$.
> 1. Calculer la distance $BC$.
> 2. Calculer l'angle $\widehat{ABC}$ au degré près.
>
> **Solution détaillée :**
> 1. D'après le théorème d'Al-Kashi :
>    $BC^2 = AB^2 + AC^2 - 2 \times AB \times AC \times \cos\widehat{A}$.
>    $BC^2 = 60^2 + 100^2 - 2 \times 60 \times 100 \times \cos(60^\circ)$.
>    Comme $\cos(60^\circ) = \frac{1}{2}$ :
>    $BC^2 = 3600 + 10000 - 12000 \times 0{,}5 = 13600 - 6000 = 7600$.
>    Donc $BC = \sqrt{7600} \approx 87{,}18$ m.
>
> 2. Pour l'angle $\widehat{B}$, appliquons Al-Kashi en isolant $\cos\widehat{B}$ :
>    $AC^2 = AB^2 + BC^2 - 2 \times AB \times BC \times \cos\widehat{B}$,
>    $100^2 = 60^2 + 7600 - 2 \times 60 \times \sqrt{7600} \times \cos\widehat{B}$,
>    $10000 = 3600 + 7600 - 120\sqrt{7600} \cos\widehat{B} = 11200 - 120\sqrt{7600} \cos\widehat{B}$.
>    $120\sqrt{7600} \cos\widehat{B} = 11200 - 10000 = 1200$.
>    $\cos\widehat{B} = \frac{1200}{120\sqrt{7600}} = \frac{10}{\sqrt{7600}} \approx 0{,}1147$.
>    D'où $\widehat{B} = \arccos(0{,}1147) \approx 83^\circ$.

> **✅ Exemple résolu 5 — Équation d'un cercle défini par un diamètre**
> On donne les points $A(-1; 3)$ et $B(5; 1)$.
> 1. Déterminer une équation cartésienne du cercle $\mathcal{C}$ de diamètre $[AB]$.
> 2. Déterminer les coordonnées de son centre $\Omega$ et son rayon $R$, puis vérifier la forme $(x-x_\Omega)^2 + (y-y_\Omega)^2 = R^2$.
>
> **Solution détaillée :**
> 1. $M(x; y) \in \mathcal{C} \iff \vec{MA} \cdot \vec{MB} = 0$.
>    $\vec{MA}\begin{pmatrix} -1 - x \\ 3 - y \end{pmatrix}$ et $\vec{MB}\begin{pmatrix} 5 - x \\ 1 - y \end{pmatrix}$.
>    $\vec{MA} \cdot \vec{MB} = (-1 - x)(5 - x) + (3 - y)(1 - y) = 0$.
>    Développons :
>    $(-5 + x - 5x + x^2) + (3 - 3y - y + y^2) = 0 \iff x^2 - 4x + y^2 - 4y - 2 = 0$.
>
> 2. Centre $\Omega$, milieu de $[AB]$ :
>    $x_\Omega = \frac{-1 + 5}{2} = 2$, et $y_\Omega = \frac{3 + 1}{2} = 2$, donc $\Omega(2; 2)$.
>    Rayon : $AB = \sqrt{(5 - (-1))^2 + (1 - 3)^2} = \sqrt{6^2 + (-2)^2} = \sqrt{36 + 4} = \sqrt{40} = 2\sqrt{10}$.
>    Le rayon est $R = \frac{AB}{2} = \sqrt{10}$, d'où $R^2 = 10$.
>    L'équation réduite est $(x - 2)^2 + (y - 2)^2 = 10$.
>    En développant : $x^2 - 4x + 4 + y^2 - 4y + 4 = 10 \iff x^2 - 4x + y^2 - 4y - 2 = 0$.
>    On retrouve exactement la même équation !

> **✅ Exemple résolu 6 — Utiliser le théorème de la médiane**
> Soit un triangle $ABC$ tel que $AB = 7$, $AC = 9$ et $BC = 8$.
> Calculer la longueur exacte de la médiane issue de $A$.
>
> **Solution détaillée :**
> Soit $I$ le milieu de $[BC]$. La médiane issue de $A$ est le segment $[AI]$.
> D'après le théorème de la médiane :
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2.$$
> On remplace par les valeurs connues :
> $$7^2 + 9^2 = 2AI^2 + \frac{1}{2}(8^2),$$
> $$49 + 81 = 2AI^2 + \frac{1}{2}(64),$$
> $$130 = 2AI^2 + 32.$$
> On isole $AI^2$ :
> $$2AI^2 = 130 - 32 = 98 \implies AI^2 = 49 \implies AI = \sqrt{49} = 7.$$
> La médiane mesure exactement 7.

---

### Ce qu'il faut retenir

1. **Quatre définitions équivalentes du produit scalaire :**
   - Géométrique : $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$.
   - Par projection : $\vec{OA} \cdot \vec{OB} = \pm OA \times OH$ ($H$ projeté orthogonal de $B$ sur $(OA)$).
   - Analytique (repère orthonormé) : $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix} \cdot \vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix} = xx' + yy'$.
   - Polarisation : $\vec{u} \cdot \vec{v} = \frac{1}{2}\left(\|\vec{u}+\vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2\right)$.

2. **Orthogonalité et géométrie vectorielle :**
   - $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0 \iff xx' + yy' = 0$.
   - Une droite de vecteur normal $\vec{n}(a; b)$ a pour équation cartésienne $ax + by + c = 0$.

3. **Formules fondamentales du triangle :**
   - Al-Kashi : $a^2 = b^2 + c^2 - 2bc\cos\widehat{A}$.
   - Médiane : $AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2$ (avec $I$ milieu de $[BC]$).

4. **Cercles :**
   - Centre $\Omega(x_\Omega; y_\Omega)$ et rayon $R$ : $(x - x_\Omega)^2 + (y - y_\Omega)^2 = R^2$.
   - Diamètre $[AB]$ : $\vec{MA} \cdot \vec{MB} = 0 \iff (x - x_A)(x - x_B) + (y - y_A)(y - y_B) = 0$.

---

### Exercices

#### Niveau ★ (Applications directes)

1. Soient deux vecteurs $\vec{u}$ et $\vec{v}$ tels que $\|\vec{u}\| = 5$, $\|\vec{v}\| = 6$ et l'angle entre eux vaut $\frac{\pi}{3}$. Calculer $\vec{u} \cdot \vec{v}$.
2. Dans un repère orthonormé, on donne $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 2 \\ 5 \end{pmatrix}$. Calculer $\vec{u} \cdot \vec{v}$.
3. Les vecteurs $\vec{u}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 9 \\ 6 \end{pmatrix}$ sont-ils orthogonaux ?
4. Déterminer un vecteur normal $\vec{n}$ à la droite d'équation $3x - 7y + 11 = 0$.
5. Donner une équation cartésienne de la droite passant par $A(1; 4)$ et de vecteur normal $\vec{n}\begin{pmatrix} 2 \\ -3 \end{pmatrix}$.
6. Dans un triangle $ABC$, on donne $AB = 5$, $AC = 8$ et $\widehat{A} = 60^\circ$. Calculer la longueur $BC$.
7. Soit un segment $[AB]$ avec $A(2; 1)$ et $B(6; 5)$. Écrire l'équation du cercle de diamètre $[AB]$.
8. Soit un triangle équilatéral $ABC$ de côté $a = 6$. Calculer le produit scalaire $\vec{AB} \cdot \vec{AC}$.

#### Niveau ★★ (Réflexion et géométrie)

9. Soit un rectangle $ABCD$ tel que $AB = 6$ et $BC = 3$. Soit $I$ le milieu de $[AB]$. Calculer $\vec{CA} \cdot \vec{DI}$.
10. Démontrer que dans un losange, les diagonales se coupent à angle droit en utilisant le produit scalaire de $(\vec{u} + \vec{v})$ et $(\vec{u} - \vec{v})$.
11. Dans un repère orthonormé, on considère les points $A(-2; 1)$, $B(2; 3)$ et $C(1; 5)$.
    a) Calculer $\vec{BA} \cdot \vec{BC}$.
    b) En déduire une valeur approchée au degré près de l'angle $\widehat{ABC}$.
12. Déterminer la valeur du réel $k$ pour que les vecteurs $\vec{u}\begin{pmatrix} 2k - 1 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 4 \\ k + 2 \end{pmatrix}$ soient orthogonaux.
13. On considère le triangle $MNP$ avec $MN = 5$, $NP = 7$ et $MP = 8$. Calculer l'angle $\widehat{MNP}$ au dixième de degré.
14. Soit un triangle $ABC$ avec $AB = 6$, $AC = 10$, et la médiane $AI = 6$. Calculer la longueur du côté $BC$.
15. Déterminer l'ensemble des points $M(x; y)$ dont les coordonnées vérifient l'équation :
    $$x^2 + y^2 - 6x + 8y = 0.$$
16. Déterminer la distance du point $A(2; 3)$ à la droite $(d)$ d'équation $4x + 3y - 7 = 0$ en utilisant un vecteur normal.

#### Niveau ★★★ (Problèmes et défis Bac)

17. **Hauteurs d'un triangle concourantes :**
    Soit un triangle $ABC$. Soit $H$ l'intersection des hauteurs issues de $A$ et de $B$.
    a) Exprimer l'appartenance de $H$ aux deux premières hauteurs en termes de produits scalaires.
    b) En déduire que $\vec{CH} \cdot \vec{AB} = 0$, et conclure que les trois hauteurs sont concourantes.
18. **Ensemble de points et ligne de niveau :**
    Soient $A$ et $B$ deux points distincts distants de $AB = 6$ cm. On note $I$ le milieu de $[AB]$.
    Déterminer et représenter l'ensemble des points $M$ du plan vérifiant :
    $$\vec{MA} \cdot \vec{MB} = 7.$$
19. **Optimisation d'un tir de rugby :**
    Un joueur de rugby doit transformer un essai marqué en coin. Soient les poteaux situés en $P_1(0; 2)$ et $P_2(0; -2)$. Le joueur peut reculer perpendiculairement sur la ligne $y = 5$. En quelle abscisse $x > 0$ doit-il placer le ballon pour que l'angle de tir $\widehat{P_1 M P_2}$ soit maximal ?
20. **Formule de Heron démontrée par Al-Kashi :**
    Soit un triangle $ABC$ de côtés $a, b, c$ et de demi-périmètre $p = \frac{a+b+c}{2}$.
    En utilisant l'aire $\mathcal{S} = \frac{1}{2}bc\sin\widehat{A}$ et la formule d'Al-Kashi pour $\cos\widehat{A}$, démontrer la célèbre formule de Héron d'Alexandrie :
    $$\mathcal{S} = \sqrt{p(p-a)(p-b)(p-c)}.$$
21. **Puissance d'un point par rapport à un cercle :**
    Soit un cercle $\mathcal{C}$ de centre $\Omega$ et de rayon $R$, et un point $M$ quelconque du plan. Une droite passant par $M$ coupe le cercle en deux points $A$ et $B$.
    Montrer que le produit scalaire $\vec{MA} \cdot \vec{MB}$ ne dépend pas de la droite choisie et vaut toujours $M\Omega^2 - R^2$.

---

### Solutions

**1.** $\vec{u} \cdot \vec{v} = 5 \times 6 \times \cos\left(\frac{\pi}{3}\right) = 30 \times 0{,}5 = 15$.

**2.** $\vec{u} \cdot \vec{v} = (-3) \times 2 + 4 \times 5 = -6 + 20 = 14$.

**3.** $xx' + yy' = 4 \times 9 + (-6) \times 6 = 36 - 36 = 0$. Oui, les vecteurs sont orthogonaux.

**4.** Le vecteur $\vec{n}\begin{pmatrix} 3 \\ -7 \end{pmatrix}$ est normal à la droite.

**5.** $2(x - 1) - 3(y - 4) = 0 \iff 2x - 3y - 2 + 12 = 0 \iff 2x - 3y + 10 = 0$.

**6.** Al-Kashi : $BC^2 = 5^2 + 8^2 - 2 \times 5 \times 8 \times \cos(60^\circ) = 25 + 64 - 80 \times 0{,}5 = 89 - 40 = 49$. Donc $BC = 7$.

**7.** $(x - 2)(x - 6) + (y - 1)(y - 5) = 0 \iff x^2 - 8x + 12 + y^2 - 6y + 5 = 0 \iff x^2 + y^2 - 8x - 6y + 17 = 0$.

**8.** $\vec{AB} \cdot \vec{AC} = 6 \times 6 \times \cos(60^\circ) = 36 \times 0{,}5 = 18$.

**9.** Plaçons un repère orthonormé d'origine $D$ avec $(DA)$ comme axe des abscisses et $(DC)$ comme axe des ordonnées. $D(0; 0)$, $A(3; 0)$, $B(3; 6)$, $C(0; 6)$. Le milieu $I$ de $[AB]$ a pour coordonnées $(3; 3)$.
Ainsi, $\vec{CA}\begin{pmatrix} 3 - 0 \\ 0 - 6 \end{pmatrix} = \begin{pmatrix} 3 \\ -6 \end{pmatrix}$, et $\vec{DI}\begin{pmatrix} 3 \\ 3 \end{pmatrix}$.
Le produit scalaire vaut : $\vec{CA} \cdot \vec{DI} = 3 \times 3 + (-6) \times 3 = 9 - 18 = -9$.

**10.** Soient $\vec{u}$ et $\vec{v}$ les deux vecteurs formant les côtés adjacents issus d'un sommet d'un losange. Comme tous les côtés d'un losange sont égaux, $\|\vec{u}\| = \|\vec{v}\|$, donc $\|\vec{u}\|^2 - \|\vec{v}\|^2 = 0$.
Les diagonales sont représentées par les vecteurs $\vec{u} + \vec{v}$ et $\vec{u} - \vec{v}$.
Calculons leur produit scalaire grâce à l'identité remarquable vectorielle :
$(\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v}) = \|\vec{u}\|^2 - \|\vec{v}\|^2 = 0$.
Leur produit scalaire étant nul, les diagonales d'un losange sont rigoureusement perpendiculaires.

**11.**
a) $\vec{BA}\begin{pmatrix} -2 - 2 \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} -4 \\ -2 \end{pmatrix}$, et $\vec{BC}\begin{pmatrix} 1 - 2 \\ 5 - 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$.
$\vec{BA} \cdot \vec{BC} = (-4) \times (-1) + (-2) \times 2 = 4 - 4 = 0$.
b) Comme le produit scalaire est nul, les vecteurs sont orthogonaux : $\widehat{ABC} = 90^\circ$ exactement !

**12.** $\vec{u} \perp \vec{v} \iff (2k - 1) \times 4 + 3 \times (k + 2) = 0 \iff 8k - 4 + 3k + 6 = 0 \iff 11k + 2 = 0 \iff k = -\frac{2}{11}$.

**13.** Par Al-Kashi dans $MNP$ : $MP^2 = MN^2 + NP^2 - 2 \times MN \times NP \times \cos\widehat{N}$.
$8^2 = 5^2 + 7^2 - 2 \times 5 \times 7 \times \cos\widehat{N} \iff 64 = 25 + 49 - 70\cos\widehat{N} \iff 64 = 74 - 70\cos\widehat{N}$.
$70\cos\widehat{N} = 10 \iff \cos\widehat{N} = \frac{10}{70} = \frac{1}{7} \approx 0{,}1428$.
Donc $\widehat{MNP} = \arccos\left(\frac{1}{7}\right) \approx 81{,}8^\circ$.

**14.** Théorème de la médiane : $AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2$.
$6^2 + 10^2 = 2(6^2) + \frac{1}{2}BC^2 \iff 36 + 100 = 72 + \frac{1}{2}BC^2 \iff 136 = 72 + \frac{1}{2}BC^2$.
$\frac{1}{2}BC^2 = 64 \iff BC^2 = 128 \implies BC = \sqrt{128} = 8\sqrt{2} \approx 11{,}31$.

**15.** Forme canonique : $(x^2 - 6x) + (y^2 + 8y) = 0 \iff (x - 3)^2 - 9 + (y + 4)^2 - 16 = 0 \iff (x - 3)^2 + (y + 4)^2 = 25$.
Il s'agit du cercle de centre $\Omega(3; -4)$ et de rayon $R = \sqrt{25} = 5$.

**16.** Soit $H$ le projeté orthogonal de $A$ sur $(d)$. La distance de $A$ à $(d)$ est la longueur $AH$.
Le vecteur $\vec{n}\begin{pmatrix} 4 \\ 3 \end{pmatrix}$ est normal à $(d)$, sa norme vaut $\|\vec{n}\| = \sqrt{4^2 + 3^2} = 5$.
Prenons un point quelconque de $(d)$, par exemple $B(1; 1)$ car $4(1) + 3(1) - 7 = 0$.
Le vecteur $\vec{BA} = \begin{pmatrix} 2 - 1 \\ 3 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
La valeur absolue du produit scalaire donne $|\vec{BA} \cdot \vec{n}| = \|\vec{n}\| \times AH$.
Or $\vec{BA} \cdot \vec{n} = 1 \times 4 + 2 \times 3 = 10$.
D'où $10 = 5 \times AH \implies AH = \frac{10}{5} = 2$.
La distance vaut exactement 2.

**17.**
a) $H$ est sur la hauteur issue de $A$, donc $\vec{AH} \perp \vec{BC} \iff \vec{AH} \cdot \vec{BC} = 0$.
$H$ est sur la hauteur issue de $B$, donc $\vec{BH} \perp \vec{AC} \iff \vec{BH} \cdot \vec{AC} = 0$.
b) Calculons $\vec{CH} \cdot \vec{AB}$ :
$\vec{CH} \cdot \vec{AB} = \vec{CH} \cdot (\vec{CB} - \vec{CA}) = \vec{CH} \cdot \vec{CB} - \vec{CH} \cdot \vec{CA}$.
Or $\vec{CH} = \vec{CA} + \vec{AH} = \vec{CB} + \vec{BH}$.
En substituant astucieusement :
$\vec{CH} \cdot \vec{CB} = (\vec{CA} + \vec{AH}) \cdot \vec{CB} = \vec{CA} \cdot \vec{CB} + \vec{AH} \cdot \vec{CB} = \vec{CA} \cdot \vec{CB} + 0$.
De même, $\vec{CH} \cdot \vec{CA} = (\vec{CB} + \vec{BH}) \cdot \vec{CA} = \vec{CB} \cdot \vec{CA} + \vec{BH} \cdot \vec{CA} = \vec{CB} \cdot \vec{CA} + 0$.
Ainsi, $\vec{CH} \cdot \vec{AB} = \vec{CA} \cdot \vec{CB} - \vec{CB} \cdot \vec{CA} = 0$.
Le vecteur $\vec{CH}$ est donc orthogonal à $\vec{AB}$ : la droite $(CH)$ est la troisième hauteur du triangle. Les trois hauteurs passent par le même point $H$ : elles sont concourantes.

**18.** Exprimons $\vec{MA}$ et $\vec{MB}$ en passant par le milieu $I$ de $[AB]$ :
$\vec{MA} \cdot \vec{MB} = (\vec{MI} + \vec{IA}) \cdot (\vec{MI} + \vec{IB})$.
Comme $\vec{IB} = -\vec{IA}$, on a l'identité remarquable :
$\vec{MA} \cdot \vec{MB} = MI^2 - IA^2$.
Comme $AB = 6$, $IA = 3$, donc $IA^2 = 9$.
L'équation devient : $MI^2 - 9 = 7 \iff MI^2 = 16 \iff MI = 4$.
L'ensemble recherché est donc le **cercle de centre $I$ (milieu de $[AB]$) et de rayon $R = 4$ cm**.

**19.** Un point de la ligne de tir est $M(x; 5)$ avec $x > 0$.
$\vec{MP_1}\begin{pmatrix} -x \\ 2 - 5 \end{pmatrix} = \begin{pmatrix} -x \\ -3 \end{pmatrix}$ et $\vec{MP_2}\begin{pmatrix} -x \\ -2 - 5 \end{pmatrix} = \begin{pmatrix} -x \\ -7 \end{pmatrix}$.
Le produit scalaire vaut : $\vec{MP_1} \cdot \vec{MP_2} = (-x)(-x) + (-3)(-7) = x^2 + 21$.
Les normes valent : $\|\vec{MP_1}\| = \sqrt{x^2 + 9}$ et $\|\vec{MP_2}\| = \sqrt{x^2 + 49}$.
Le cosinus de l'angle $\theta = \widehat{P_1 M P_2}$ vérifie $\cos\theta = \frac{x^2 + 21}{\sqrt{(x^2+9)(x^2+49)}}$.
L'angle $\theta$ est aigu et maximal quand $\cos\theta$ est minimal (ou $\tan\theta$ maximal).
En élevant au carré le rapport : $\cos^2\theta = \frac{(x^2+21)^2}{x^4 + 58x^2 + 441} = \frac{x^4 + 42x^2 + 441}{x^4 + 58x^2 + 441} = 1 - \frac{16x^2}{x^4 + 58x^2 + 441} = 1 - \frac{16}{x^2 + 58 + \frac{441}{x^2}}$.
Ce cosinus est minimal lorsque le dénominateur $x^2 + \frac{441}{x^2}$ est minimal.
D'après l'inégalité arithmético-géométrique, la somme de deux nombres de produit constant $x^2 \times \frac{441}{x^2} = 441$ est minimale lorsqu'ils sont égaux :
$x^2 = \frac{441}{x^2} \iff x^4 = 441 \iff x^2 = 21 \iff x = \sqrt{21} \approx 4{,}58$ m.
Le buteur doit poser le ballon à environ 4,58 mètres des poteaux.

**20.**
On sait que l'aire d'un triangle vaut $\mathcal{S} = \frac{1}{2}bc\sin\widehat{A}$.
Donc $4\mathcal{S} = 2bc\sin\widehat{A}$, d'où $16\mathcal{S}^2 = 4b^2 c^2 \sin^2\widehat{A} = 4b^2 c^2 (1 - \cos^2\widehat{A}) = (2bc - 2bc\cos\widehat{A})(2bc + 2bc\cos\widehat{A})$.
D'après Al-Kashi, $2bc\cos\widehat{A} = b^2 + c^2 - a^2$.
Remplaçons :
$2bc - (b^2 + c^2 - a^2) = a^2 - (b - c)^2 = (a - b + c)(a + b - c)$.
$2bc + (b^2 + c^2 - a^2) = (b + c)^2 - a^2 = (b + c - a)(b + c + a)$.
Comme $p = \frac{a+b+c}{2}$, on a $a+b+c = 2p$, $b+c-a = 2(p-a)$, $a+c-b = 2(p-b)$, et $a+b-c = 2(p-c)$.
Le produit devient :
$16\mathcal{S}^2 = 2(p-b) \times 2(p-c) \times 2(p-a) \times 2p = 16 p(p-a)(p-b)(p-c)$.
En divisant par 16 et en prenant la racine carrée, on obtient exactement :
$\mathcal{S} = \sqrt{p(p-a)(p-b)(p-c)}$.

**21.** Soit $A'$ le point diamétralement opposé à $A$ sur le cercle. Alors le triangle $AA'B$ est inscrit dans un demi-cercle, donc l'angle $\widehat{A'BA}$ est droit : $(BA') \perp (BA)$.
Le projeté orthogonal de $A'$ sur la droite $(AB)$ est donc le point $B$.
Par projection orthogonale : $\vec{MA} \cdot \vec{MB} = \vec{MA} \cdot \vec{MA'}$.
Or $\vec{MA} = \vec{M\Omega} + \vec{\Omega A}$ et $\vec{MA'} = \vec{M\Omega} + \vec{\Omega A'}$.
Comme $A$ et $A'$ sont diamétralement opposés, $\vec{\Omega A'} = -\vec{\Omega A}$.
Donc :
$\vec{MA} \cdot \vec{MB} = (\vec{M\Omega} + \vec{\Omega A}) \cdot (\vec{M\Omega} - \vec{\Omega A}) = \|\vec{M\Omega}\|^2 - \|\vec{\Omega A}\|^2 = M\Omega^2 - R^2$.
Cette quantité ne dépend que de la position de $M$ et des paramètres du cercle, et est indépendante de la droite sécante sécante tracée. C'est la **puissance du point $M$ par rapport au cercle $\mathcal{C}$**.

---

### La question qui ouvre la suite

Le produit scalaire nous a permis de mesurer l'inclinaison d'une force par rapport à une droite, et de calculer la pente d'un segment rigide.
Mais que se passe-t-il si la pente n'est plus une ligne droite, mais une **courbe ondulante** comme une colline enneigée où un skieur dévale à toute allure ? Comment mesurer l'inclinaison de la planche sous la semelle en un instant infinitésimal, en un seul point de contact ? C'est la grande aventure de la **dérivation**, qui s'ouvre au chapitre suivant.
