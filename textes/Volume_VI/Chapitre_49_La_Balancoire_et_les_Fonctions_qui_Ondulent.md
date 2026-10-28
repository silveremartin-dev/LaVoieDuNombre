# VOLUME VI — L'Âge du Flux et de la Vitesse (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 49 : La Balançoire et les Fonctions qui Ondulent

> *« Le mouvement pendulaire m'a révélé que le temps n'est pas une ligne droite qui s'enfuit, mais une respiration qui revient. »*
> — Inspiré des observations de Galileo Galilei (1583)

---

### Ce que tu vas découvrir

- Pourquoi le va-et-vient d'une balançoire ou d'un pendule n'est rien d'autre que **l'ombre d'un point qui tourne en rond à vitesse constante**.
- La géométrie du **cercle trigonométrique** et comment le **radian** devient l'unique unité naturelle d'angle pour faire du calcul différentiel.
- Les propriétés de symétrie indispensables : **parité**, **imparité**, **périodicité $2\pi$**, et les formules d'addition et de duplication.
- La dérivation des fonctions sinus et cosinus : la démonstration géométrique fondamentale de $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$, pourquoi $(\sin)' = \cos$ et $(\cos)' = -\sin$.
- Le mystère du quart de tour : pourquoi la dérivée avance de $\dfrac{\pi}{2}$ par rapport à la fonction.
- La dérivation des fonctions composées du type $t \mapsto \cos(\omega t + \varphi)$ et l'équation différentielle de l'oscillateur harmonique $y'' + \omega^2 y = 0$.
- L'étude complète des variations, des tangentes et de la convexité des courbes sinusoïdales.
- Les applications concrètes : ondes sonores, courant alternatif à $50\text{ Hz}$, marées et sismologie.

---

### 1. Le problème : le lustre de Pise et l'ombre du cercle

#### 1.1 L'intuition de Galilée

En **1583**, un jeune étudiant en médecine de dix-neuf ans nommé **Galileo Galilei** (Galilée) assiste à un office dans la cathédrale de Pise. Son regard s'égare vers la voûte. Un sacristain vient d'allumer un grand lustre suspendu à une chaîne immense, et en le lâchant, lui a imprimé un mouvement de balancier régulier.

Galilée remarque une chose extraordinaire : que l'amplitude du balancement soit grande au début, ou minuscule lorsqu'il commence à ralentir à cause des frottements de l'air, **la durée d'un aller-retour semble exactement la même**. 

N'ayant pas de montre — les montres mécaniques de précision n'existent pas encore —, Galilée prend son propre pouls à son poignet. Il compte les battements : 4 battements pour un grand balancement, 4 battements pour un moyen, 4 battements pour un tout petit. C'est la découverte de **l'isochronisme des petites oscillations du pendule**.

Ce phénomène est universel : une balançoire d'enfant au parc, une corde de violon pincée, l'eau qui clapote dans une baie fermée, les électrons dans une antenne radio, tous obéissent à ce même rythme fondamental de va-et-vient.

```
                  Point d'attache
                       │
                       │ \  θ
                       │  \
                       │   \ L
                       │    \
                       │     ●  Masse m
                       │    /
                 ←─────┼───►  Va-et-vient horizontal
```

#### 1.2 Du cercle à la vague : la projection lumineuse

Comment représenter mathématiquement ce mouvement d'aller-retour ?
Imaginons une expérience visuelle très simple :
1. Une grande roue verticale tourne à vitesse constante dans une pièce sombre. Un petit voyant lumineux $M$ est fixé sur son bord extérieur.
2. Une source de lumière éclaire la roue horizontalement et projette l'ombre du voyant $M$ sur un mur vertical situé derrière.

Que fait l'ombre sur le mur ?
- Lorsque le voyant monte en haut de la roue, son ombre monte jusqu'au sommet du mur, ralentit, s'arrête un instant infinitésimal, puis redescend.
- Au milieu de la course, l'ombre fonce à sa vitesse maximale.
- En bas, elle ralentit, s'arrête et repart vers le haut.

L'ombre sur le mur effectue **exactement le mouvement d'un pendule ou d'une balançoire** !
Si l'on fait défiler un rouleau de papier verticalement à vitesse constante derrière le mur, le voyant trace une onde parfaite : **une sinusoïde**.

```
          Roue qui tourne                             Onde tracée sur le papier
               ▲ y                                               y ▲
           . ─── .                                                 │     _--_
        .    M    .          ─── Projection ───►                  1 ┼   /    \
       /     │     \                                               │  /      \
      │      │      │                                            0 ┼─*────────*────*──► t
       \     │     /                                               │           \  /
        .    O    .                                               -1 ┼            --
           . ─── .                                                 │  0    π   2π
```

Le mouvement rectiligne oscillatoire n'est rien d'autre que **la projection d'un mouvement circulaire uniforme**. Pour comprendre la balançoire, il faut donc maîtriser le cercle.

---

### 2. Le cercle trigonométrique et les symétries fondamentales

#### 2.1 Le radian : la mesure naturelle de l'arc

Au collège, tu as appris à mesurer les angles en degrés ($360^\circ$ pour un tour complet). Ce choix de 360 est hérité des astronomes babyloniens de l'Antiquité, qui aimaient le nombre 360 car il est divisible par 2, 3, 4, 5, 6, 8, 9, 10, 12, etc., et proche des 365 jours de l'année.

Mais en mathématiques supérieures et en physique, le degré est un choix arbitraire et catastrophique : si l'on dérivait en degrés, des facteurs parasites comme $\dfrac{\pi}{180}$ viendraient polluer toutes les formules de dérivation !

L'unité naturelle, c'est le **radian** :

> **📐 Définition du radian —**
> Dans le plan muni d'un repère orthonormé $(O; \vec{i}, \vec{j})$, le **cercle trigonométrique** $\mathcal{C}$ est le cercle de centre l'origine $O(0\,;0)$ et de rayon $R = 1$, orienté dans le **sens direct** (sens inverse des aiguilles d'une montre, dit sens anti-horaire).
> La mesure d'un angle en **radians** est égale à la **longueur de l'arc** intercepté par cet angle sur le cercle trigonométrique de rayon 1.

Puisque le périmètre complet d'un cercle de rayon 1 est $2\pi R = 2\pi$, un tour complet de $360^\circ$ correspond à un angle de **$2\pi$ radians**.

| Degrés | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|---|---|---|---|---|---|---|---|---|
| **Radians** | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

#### 2.2 Enroulement de la droite réelle et coordonnées

Imaginons une droite numérique graduée tangente au cercle trigonométrique au point $I(1\,;0)$. Enroulons cette droite infinie autour du cercle :
- Les nombres réels positifs s'enroulent dans le sens direct (vers le haut) ;
- Les nombres réels négatifs s'enroulent dans le sens indirect (vers le bas).

À chaque réel $x \in \mathbb{R}$ correspond un unique point $M$ du cercle trigonométrique.

> **📐 Définition des fonctions cosinus et sinus —**
> Pour tout nombre réel $x$, on note $M$ le point du cercle trigonométrique associé à $x$ par l'enroulement de la droite réelle.
> - Le **cosinus** de $x$, noté $\cos x$, est **l'abscisse** du point $M$.
> - Le **sinus** de $x$, noté $\sin x$, est **l'ordonnée** du point $M$.
>
> $$M(x) = \big(\cos x \, ; \, \sin x\big).$$

```
                        y ▲
                          │  (0, 1)
                          │   . + .
                     M' . │ .       . M(x) = (cos x, sin x)
                       \  │          /
                        \ │  sin x  / |
                         \│        /  |
        ──────────────────┼───────*───┼────────► x
               (-1, 0)    │ O   cos x (1, 0)
                          │
                          │   . - .
                          │  (0, -1)
```

#### 2.3 Conséquences immédiates et valeurs remarquables

1. **Bornes absolues :** Puisque le cercle est de rayon 1, les coordonnées de tout point $M$ sont comprises entre $-1$ et $1$ :
   $$\text{Pour tout } x \in \mathbb{R} : \quad -1 \leq \cos x \leq 1 \quad \text{et} \quad -1 \leq \sin x \leq 1.$$

2. **Équation du cercle (Pythagore) :** Le triangle rectangle formé par les projections de $M$ a pour côtés de l'angle droit $|\cos x|$ et $|\sin x|$, et pour hypoténuse le rayon $OM = 1$. Le théorème de Pythagore donne :
   $$\cos^2 x + \sin^2 x = 1.$$
   *(Rappel de notation : $\cos^2 x$ signifie $(\cos x)^2$).*

3. **Tableau des valeurs remarquables (à connaître par cœur) :**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| **$\cos x$** | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ |
| **$\sin x$** | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ |

> **💡 Astuce mnémotechnique pour la ligne du sinus :**
> Remarque la suite des racines : $\sin 0 = \dfrac{\sqrt{0}}{2} = 0$, $\sin\dfrac{\pi}{6} = \dfrac{\sqrt{1}}{2} = \dfrac{1}{2}$, $\sin\dfrac{\pi}{4} = \dfrac{\sqrt{2}}{2}$, $\sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2}$, $\sin\dfrac{\pi}{2} = \dfrac{\sqrt{4}}{2} = 1$. Les numérateurs montent de $\sqrt{0}$ à $\sqrt{4}$, tandis que pour le cosinus ils descendent en sens inverse !

#### 2.4 Périodicité et parité : la force des symétries

Faire un tour complet supplémentaire sur le cercle revient à ajouter $2\pi$ à la longueur enroulée : le point $M$ revient exactement au même endroit.

> **📐 Périodicité —**
> Les fonctions cosinus et sinus sont **périodiques de période $2\pi$** (ou $2\pi$-périodiques). Pour tout réel $x$ et tout entier relatif $k \in \mathbb{Z}$ :
> $$\cos(x + 2k\pi) = \cos x \quad \text{et} \quad \sin(x + 2k\pi) = \sin x.$$

Examinons maintenant les symétries géométriques sur le cercle :
- Les points associés à $x$ et $-x$ sont symétriques par rapport à **l'axe des abscisses $(Ox)$**. Ils ont donc la même abscisse et des ordonnées opposées.

> **📐 Parité —**
> - La fonction cosinus est **paire** : $\cos(-x) = \cos x$. Sa courbe représentative dans un repère orthogonal est symétrique par rapport à **l'axe des ordonnées $(Oy)$**.
> - La fonction sinus est **impaire** : $\sin(-x) = -\sin x$. Sa courbe représentative est symétrique par rapport à **l'origine $O(0\,;0)$**.

#### 2.5 Formules d'angles associés (les reflets du cercle)

En faisant tourner le point $M(x)$ par un demi-tour ($+\pi$) ou par symétrie par rapport aux axes, on obtient les relations fondamentales :

| Transformation | Angle | Cosinus | Sinus | Interprétation |
|---|---|---|---|---|
| Demi-tour | $x + \pi$ | $-\cos x$ | $-\sin x$ | Symétrie centrale par rapport à $O$ |
| Angle supplémentaire | $\pi - x$ | $-\cos x$ | $\sin x$ | Symétrie par rapport à l'axe vertical $(Oy)$ |
| Quart de tour | $x + \dfrac{\pi}{2}$ | $-\sin x$ | $\cos x$ | Rotation de $+90^\circ$ |
| Angle complémentaire | $\dfrac{\pi}{2} - x$ | $\sin x$ | $\cos x$ | Symétrie par rapport à la bissectrice $y = x$ |

> **💡 Le savais-tu ? Le mot "cosinus" :**
> Le préfixe *co-* vient du latin *complementi* : le **cosinus** d'un angle est simplement le **sinus du complémentaire** ($\cos x = \sin(\frac{\pi}{2}-x)$).

#### 2.6 Formules d'addition et de duplication

Ces formules permettent d'exprimer les fonctions d'une somme en fonction des composantes :

> **📐 Formules d'addition —** Pour tous réels $a$ et $b$ :
> $$\cos(a + b) = \cos a \cos b - \sin a \sin b$$
> $$\cos(a - b) = \cos a \cos b + \sin a \sin b$$
> $$\sin(a + b) = \sin a \cos b + \cos a \sin b$$
> $$\sin(a - b) = \sin a \cos b - \cos a \sin b$$

> **📐 Formules de duplication —** En posant $a = b = x$ :
> $$\sin(2x) = 2 \sin x \cos x$$
> $$\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$$

> **Exemple résolu 1 — Calcul exact de $\cos\left(\dfrac{\pi}{12}\right)$.**
> Remarquons que $\dfrac{\pi}{12} = \dfrac{\pi}{3} - \dfrac{\pi}{4}$.
> En appliquant la formule d'addition du cosinus :
> $$\cos\left(\dfrac{\pi}{12}\right) = \cos\left(\dfrac{\pi}{3} - \dfrac{\pi}{4}\right) = \cos\dfrac{\pi}{3}\cos\dfrac{\pi}{4} + \sin\dfrac{\pi}{3}\sin\dfrac{\pi}{4}.$$
> Remplaçons par les valeurs remarquables :
> $$\cos\left(\dfrac{\pi}{12}\right) = \left(\dfrac{1}{2}\right)\left(\dfrac{\sqrt{2}}{2}\right) + \left(\dfrac{\sqrt{3}}{2}\right)\left(\dfrac{\sqrt{2}}{2}\right) = \dfrac{\sqrt{2} + \sqrt{6}}{4}.$$

---

### 3. La dérivation du sinus et du cosinus : le virage à angle droit

Pour calculer la vitesse d'une balançoire ou l'accélération d'un oscillateur, nous devons dériver les fonctions sinus et cosinus. Mais avant cela, une question vertigineuse se pose : **quelle est la dérivée de $\sin x$ en $x = 0$ ?**

#### 3.1 La limite fondamentale $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$

Le taux d'accroissement de la fonction sinus en 0 s'écrit :
$$\tau(x) = \dfrac{\sin x - \sin 0}{x - 0} = \dfrac{\sin x}{x}.$$
Quand $x$ tend vers 0, nous faisons face à une forme indéterminée « $\dfrac{0}{0}$ ». Levons cette indétermination par un argument géométrique éclatant.

> **📐 Lemme fondamental (encadrement trigonométrique) —**
> Pour tout réel $x \in \left]0\,; \dfrac{\pi}{2}\right[$ :
> $$\sin x \leq x \leq \tan x \quad \left(\text{où } \tan x = \dfrac{\sin x}{\cos x}\right).$$

> **✍️ Démonstration géométrique (exigible) —**
> Considérons sur le cercle trigonométrique de centre $O$ et de rayon 1 :
> - le point $A(1\,;0)$ ;
> - le point $M(\cos x\,; \sin x)$ associé à l'angle $x \in \left]0\,; \dfrac{\pi}{2}\right[$ ;
> - le point $T(1\,; \tan x)$, intersection de la demi-droite $[OM)$ avec la tangente verticale au cercle en $A$.
>
> Comparons les aires de trois surfaces géométriques imbriquées les unes dans les autres :
> 1. Le **triangle intérieur** $OAM$ : sa base est $OA = 1$, sa hauteur est l'ordonnée de $M$, soit $\sin x$.
>    $$\text{Aire}(OAM) = \dfrac{\text{base} \times \text{hauteur}}{2} = \dfrac{1 \times \sin x}{2} = \dfrac{\sin x}{2}.$$
> 2. Le **secteur angulaire** $OAM$ (la portion de disque de rayon 1 d'angle au centre $x$) :
>    Puisque l'aire d'un disque complet de rayon 1 est $\pi \times 1^2 = \pi$ pour un angle de $2\pi$, l'aire d'un secteur d'angle $x$ radians est proportionnelle :
>    $$\text{Aire}(\text{secteur } OAM) = \dfrac{x}{2\pi} \times \pi = \dfrac{x}{2}.$$
> 3. Le **triangle extérieur** $OAT$ : sa base est $OA = 1$, sa hauteur est $AT = \tan x$.
>    $$\text{Aire}(OAT) = \dfrac{\text{base} \times \text{hauteur}}{2} = \dfrac{1 \times \tan x}{2} = \dfrac{\tan x}{2}.$$
>
> Puisque le triangle $OAM$ est strictement contenu dans le secteur angulaire $OAM$, lui-même strictement contenu dans le triangle $OAT$ :
> $$\text{Aire}(OAM) \leq \text{Aire}(\text{secteur } OAM) \leq \text{Aire}(OAT) \iff \dfrac{\sin x}{2} \leq \dfrac{x}{2} \leq \dfrac{\tan x}{2}.$$
> En multipliant par 2 :
> $$\sin x \leq x \leq \tan x.$$
> $\blacksquare$

```
                   T (1, tan x)
                   ▲
                   │\
                   │ \
                   │  \   M (cos x, sin x)
                   │   *
                   │  /│\
                   │ / │ \
                   │/  │  \
                   ┼───*───┼──►
                   O  cos  A (1, 0)
```

> **📐 Théorème — Limite remarquable en 0 :**
> $$\lim_{x \to 0} \dfrac{\sin x}{x} = 1.$$

> **✍️ Démonstration —**
> Pour tout $x \in \left]0\,; \dfrac{\pi}{2}\right[$, on a $\sin x > 0$. Divisons l'encadrement $\sin x \leq x \leq \dfrac{\sin x}{\cos x}$ par $\sin x$ :
> $$1 \leq \dfrac{x}{\sin x} \leq \dfrac{1}{\cos x}.$$
> En passant aux inverses (les termes étant strictement positifs) :
> $$\cos x \leq \dfrac{\sin x}{x} \leq 1.$$
> Cette inégalité est également vraie pour $x \in \left]-\dfrac{\pi}{2}\,; 0\right[$, car $\cos(-x) = \cos x$ et $\dfrac{\sin(-x)}{-x} = \dfrac{-\sin x}{-x} = \dfrac{\sin x}{x}$.
> Or, par continuité du cosinus en 0, $\lim\limits_{x \to 0} \cos x = \cos 0 = 1$.
> D'après le **théorème des gendarmes** :
> $$\lim_{x \to 0} \dfrac{\sin x}{x} = 1.$$
> $\blacksquare$

> **Corollaire fondamental — Limite de $\dfrac{1 - \cos x}{x^2}$ en 0 :**
> $$\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2} \quad \text{et par conséquent} \quad \lim_{x \to 0} \dfrac{\cos x - 1}{x} = 0.$$
>
> *Démonstration :*
> Utilisons la formule de duplication $\cos(2u) = 1 - 2\sin^2 u$ avec $u = \dfrac{x}{2}$, d'où $1 - \cos x = 2\sin^2\left(\dfrac{x}{2}\right)$.
> Alors :
> $$\dfrac{1 - \cos x}{x^2} = \dfrac{2 \sin^2(x/2)}{x^2} = \dfrac{2}{4} \times \left(\dfrac{\sin(x/2)}{x/2}\right)^2 = \dfrac{1}{2} \left(\dfrac{\sin(x/2)}{x/2}\right)^2.$$
> Quand $x \to 0$, $u = \dfrac{x}{2} \to 0$, donc $\dfrac{\sin(x/2)}{x/2} \to 1$.
> Par produit de limites : $\lim\limits_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2} \times 1^2 = \dfrac{1}{2}$.
> De plus, $\dfrac{\cos x - 1}{x} = -x \times \dfrac{1 - \cos x}{x^2} \to 0 \times \dfrac{1}{2} = 0$. $\blacksquare$

#### 3.2 Le calcul des dérivées de sinus et cosinus

> **📐 Théorème (Démonstrations exigibles au baccalauréat) —**
> Les fonctions $\sin$ et $\cos$ sont dérivables sur $\mathbb{R}$, et pour tout réel $x$ :
> $$\sin'(x) = \cos x \quad \text{et} \quad \cos'(x) = -\sin x.$$

> **✍️ Démonstration pour $\sin'(x)$ —**
> Soit $x \in \mathbb{R}$ fixé et soit $h \neq 0$. Formons le taux d'accroissement de la fonction sinus entre $x$ et $x+h$ :
> $$\tau(h) = \dfrac{\sin(x+h) - \sin x}{h}.$$
> D'après la formule d'addition : $\sin(x+h) = \sin x \cos h + \cos x \sin h$.
> Donc :
> $$\tau(h) = \dfrac{\sin x \cos h + \cos x \sin h - \sin x}{h} = \sin x \left(\dfrac{\cos h - 1}{h}\right) + \cos x \left(\dfrac{\sin h}{h}\right).$$
> Lorsque $h \to 0$ :
> - $\lim\limits_{h \to 0} \dfrac{\cos h - 1}{h} = 0$ ;
> - $\lim\limits_{h \to 0} \dfrac{\sin h}{h} = 1$.
>
> On en déduit :
> $$\lim_{h \to 0} \tau(h) = \sin x \times 0 + \cos x \times 1 = \cos x.$$
> La fonction sinus est donc dérivable en tout réel $x$, et $\sin'(x) = \cos x$. $\blacksquare$

> **✍️ Démonstration pour $\cos'(x)$ —**
> On utilise la formule d'addition pour le cosinus :
> $$\dfrac{\cos(x+h) - \cos x}{h} = \dfrac{\cos x \cos h - \sin x \sin h - \cos x}{h} = \cos x \left(\dfrac{\cos h - 1}{h}\right) - \sin x \left(\dfrac{\sin h}{h}\right).$$
> Par passage à la limite quand $h \to 0$ :
> $$\lim_{h \to 0} \dfrac{\cos(x+h) - \cos x}{h} = \cos x \times 0 - \sin x \times 1 = -\sin x.$$
> La fonction cosinus est donc dérivable sur $\mathbb{R}$, et $\cos'(x) = -\sin x$. $\blacksquare$

#### 3.3 Le mystère du quart de tour : la vision cinématique

Pourquoi la dérivée de sinus est-elle cosinus, et la dérivée de cosinus est-elle **moins** sinus ?
Regarde ce qui se passe lorsqu'on ajoute un quart de tour, c'est-à-dire un angle de $+\dfrac{\pi}{2}$ :
- $\sin\left(x + \dfrac{\pi}{2}\right) = \cos x$ ;
- $\cos\left(x + \dfrac{\pi}{2}\right) = -\sin x$.

> **Dériver une sinusoïde, c'est lui faire faire un quart de tour en avance de phase !**

En physique cinématique, si un point parcourt le cercle trigonométrique dans le sens direct avec une position $\vec{OM}(t) = \cos t \, \vec{i} + \sin t \, \vec{j}$, son vecteur vitesse instantanée $\vec{v}(t) = \dfrac{d\vec{OM}}{dt}$ est :
$$\vec{v}(t) = -\sin t \, \vec{i} + \cos t \, \vec{j}.$$
Or le produit scalaire $\vec{OM}(t) \cdot \vec{v}(t) = \cos t(-\sin t) + \sin t(\cos t) = 0$ !
Le vecteur vitesse est **strictement perpendiculaire** au rayon : il est orienté tangentiellement dans le sens de rotation, soit exactement $90^\circ$ en avant.

```
                      y ▲
                        │        vitesse v (perpendiculaire à OM)
                        │         ▲
                        │        /
                        │       * M (cos t, sin t)
                        │      /
                        │     / rayon OM
                        │    /
        ────────────────┼───*────────────► x
                        │  O
```

#### 3.4 Dérivées de fonctions composées

D'après le théorème de dérivation des composées $(f \circ u)' = u' \times (f' \circ u)$ :

> **📐 Formules de composition —** Soit $u$ une fonction dérivable sur un intervalle $I$ :
> 1. $\big(\sin(u(x))\big)' = u'(x) \cos(u(x))$
> 2. $\big(\cos(u(x))\big)' = -u'(x) \sin(u(x))$
>
> En particulier, pour les pulsations harmoniques $u(t) = \omega t + \varphi$ avec $\omega, \varphi \in \mathbb{R}$ :
> $$\big(\sin(\omega t + \varphi)\big)' = \omega \cos(\omega t + \varphi)$$
> $$\big(\cos(\omega t + \varphi)\big)' = -\omega \sin(\omega t + \varphi)$$

> **Exemple résolu 2 — Calculs de dérivées composées.**
> 1. $f_1(x) = \sin(3x - \pi) \implies f'_1(x) = 3 \cos(3x - \pi)$.
> 2. $f_2(x) = \cos(x^2 + 1) \implies f'_2(x) = -(2x) \sin(x^2 + 1) = -2x \sin(x^2 + 1)$.
> 3. $f_3(x) = \sin^3(x) = (\sin x)^3 \implies f'_3(x) = 3(\sin x)^2 \times (\sin x)' = 3\sin^2 x \cos x$.
> 4. $f_4(x) = e^{-x} \cos(2x) \implies$ règle du produit $(uv)' = u'v + uv'$ :
>    $$f'_4(x) = (-e^{-x})\cos(2x) + e^{-x}(-2\sin(2x)) = -e^{-x}\big(\cos(2x) + 2\sin(2x)\big).$$

#### 3.5 Dérivée seconde et l'équation de l'oscillateur harmonique

Calculons la dérivée seconde de la fonction $f(t) = \cos(\omega t)$ :
- $f'(t) = -\omega \sin(\omega t)$ ;
- $f''(t) = -\omega \times \big(\omega \cos(\omega t)\big) = -\omega^2 \cos(\omega t) = -\omega^2 f(t)$.

En passant tout du même côté :
$$f''(t) + \omega^2 f(t) = 0.$$

> **💡 Découverte magistrale —**
> Les fonctions sinusoïdales sont les **uniques solutions** de l'équation différentielle du second ordre :
> $$y'' + \omega^2 y = 0.$$
> C'est l'équation maîtresse de toute la physique classique : celle du ressort (loi de Hooke $m a = -k x$), du circuit électrique bobine-condensateur (oscillateur LC), du son, de la lumière et des ondes électromagnétiques !

---

### 4. Étude complète des fonctions sinus et cosinus

Puisque les fonctions sinus et cosinus sont périodiques de période $2\pi$, il suffit de les étudier sur un intervalle de longueur $2\pi$, par exemple $[-\pi\,; \pi]$.
De plus, grâce à la parité :
- Pour le cosinus (fonction paire) : on étudie sur $[0\,; \pi]$, puis on complète par symétrie axiale par rapport à $(Oy)$ sur $[-\pi\,; \pi]$.
- Pour le sinus (fonction impaire) : on étudie sur $[0\,; \pi]$, puis on complète par symétrie centrale par rapport à l'origine $O$ sur $[-\pi\,; \pi]$.

Enfin, on reproduit le motif à l'infini vers la gauche et vers la droite par translations successives de vecteur $2\pi \vec{i}$.

#### 4.1 Étude de la fonction cosinus

Sur l'intervalle $[0\,; \pi]$ :
- $\cos'(x) = -\sin x$.
- Pour tout $x \in \; ]0\,; \pi[$, $\sin x > 0$, donc $\cos'(x) < 0$.
- La fonction cosinus est donc **strictement décroissante** sur $[0\,; \pi]$.
- $\cos 0 = 1$, $\cos\left(\dfrac{\pi}{2}\right) = 0$, et $\cos \pi = -1$.

Tableau de variations sur $[-\pi\,; \pi]$ :

```
    x    │ -π                0                π
─────────┼───────────────────────────────────────
  cos'(x)│        +          0        -
─────────┼───────────────────┼───────────────────
         │                   1
  cos(x) │                 ↗   ↘
         │ -1                         -1
```

**Tangentes et concavité :**
- En $x = 0$, $\cos'(0) = 0$ : la courbe admet une **tangente horizontale** au sommet $(0\,;1)$.
- En $x = \pi$, $\cos'(\pi) = 0$ : **tangente horizontale** au creux $(\pi\,;-1)$.
- Dérivée seconde : $\cos''(x) = -\cos x$.
  Sur $\left[0\,; \dfrac{\pi}{2}\right]$, $\cos x \geq 0 \implies \cos''(x) \leq 0$ : la fonction est **concave**.
  Sur $\left[\dfrac{\pi}{2}\,; \pi\right]$, $\cos x \leq 0 \implies \cos''(x) \geq 0$ : la fonction est **convexe**.
  Le point d'inflexion se situe en $x = \dfrac{\pi}{2}$, là où la courbe traverse l'axe des abscisses avec une pente de $-1$.

#### 4.2 Étude de la fonction sinus

Sur l'intervalle $[0\,; \pi]$ :
- $\sin'(x) = \cos x$.
- Sur $\left[0\,; \dfrac{\pi}{2}\right[$, $\cos x > 0$ : $\sin$ est **strictement croissante**.
- En $x = \dfrac{\pi}{2}$, $\cos\left(\dfrac{\pi}{2}\right) = 0$ : tangente horizontale au point $\left(\dfrac{\pi}{2}\,; 1\right)$.
- Sur $\left]\dfrac{\pi}{2}\,; \pi\right]$, $\cos x < 0$ : $\sin$ est **strictement décroissante**.

Tableau de variations sur $[-\pi\,; \pi]$ :

```
    x    │ -π        -π/2         0         π/2         π
─────────┼─────────────────────────────────────────────────
  sin'(x)│     -       0     +    1    +     0     -
─────────┼─────────────────────────────────────────────────
         │                   0              1
  sin(x) │                 ↗   ↘          ↗   ↘
         │ 0             -1         0              0
```

**Tangentes remarquables :**
- En $x = 0$, $\sin'(0) = 1$ et $\sin 0 = 0$. La tangente à l'origine est la droite d'équation :
  $$y = x.$$
  Pour $x \approx 0$, l'approximation affine donne **$\sin x \approx x$**. C'est la célèbre approximation des petits angles utilisée par tous les physiciens !

```
              y ▲                     _---_ (π/2 ; 1)
                │                  _-'     '-_
              1 ┼                -'           '-
                │              /                 \  y = sin(x)
              0 ┼────────────*─────────────────────*────────► x
                │          0/ ¦                   π
             -1 ┼          /  ¦
                │        /    ¦
                │       / y = x (tangente en 0)
```

---

### 5. Résolution d'équations et inéquations trigonométriques

#### 5.1 Les équations fondamentales

> **🧭 Méthode — Résolution de $\cos x = \cos \alpha$ :**
> Deux points du cercle trigonométrique ont la même abscisse si et seulement si leurs angles sont égaux ou opposés, à un nombre entier de tours près :
> $$\cos x = \cos \alpha \iff x = \alpha + 2k\pi \quad \text{ou} \quad x = -\alpha + 2k\pi \quad (k \in \mathbb{Z}).$$

> **🧭 Méthode — Résolution de $\sin x = \sin \alpha$ :**
> Deux points du cercle trigonométrique ont la même ordonnée si et seulement si leurs angles sont égaux ou supplémentaires ($\pi - \alpha$), à un nombre entier de tours près :
> $$\sin x = \sin \alpha \iff x = \alpha + 2k\pi \quad \text{ou} \quad x = \pi - \alpha + 2k\pi \quad (k \in \mathbb{Z}).$$

> **Exemple résolu 3 — Résolution sur un intervalle donné.**
> Résoudre l'équation $\cos(2x) = \dfrac{1}{2}$ sur l'intervalle $[0\,; 2\pi]$.
> - On sait que $\dfrac{1}{2} = \cos\left(\dfrac{\pi}{3}\right)$.
> - L'équation équivaut à :
>   $$2x = \dfrac{\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{6} + k\pi$$
>   ou
>   $$2x = -\dfrac{\pi}{3} + 2k\pi \iff x = -\dfrac{\pi}{6} + k\pi \quad (k \in \mathbb{Z}).$$
> - Sélectionnons les valeurs qui tombent dans l'intervalle $[0\,; 2\pi]$ :
>   - Pour la première série $x = \dfrac{\pi}{6} + k\pi$ :
>     - $k = 0 \implies x_1 = \dfrac{\pi}{6} \in [0\,; 2\pi]$ ;
>     - $k = 1 \implies x_2 = \dfrac{\pi}{6} + \pi = \dfrac{7\pi}{6} \in [0\,; 2\pi]$ ;
>     - $k = 2 \implies x = \dfrac{13\pi}{6} > 2\pi$ (hors intervalle).
>   - Pour la seconde série $x = -\dfrac{\pi}{6} + k\pi$ :
>     - $k = 0 \implies x = -\dfrac{\pi}{6} < 0$ (hors intervalle) ;
>     - $k = 1 \implies x_3 = -\dfrac{\pi}{6} + \pi = \dfrac{5\pi}{6} \in [0\,; 2\pi]$ ;
>     - $k = 2 \implies x_4 = -\dfrac{\pi}{6} + 2\pi = \dfrac{11\pi}{6} \in [0\,; 2\pi]$.
> - Conclusion : $\mathcal{S} = \left\{ \dfrac{\pi}{6} \; ; \; \dfrac{5\pi}{6} \; ; \; \dfrac{7\pi}{6} \; ; \; \dfrac{11\pi}{6} \right\}$.

#### 5.2 Équations avec changement de variable

> **Exemple résolu 4 — Équation du second degré.**
> Résoudre sur $[0\,; 2\pi[$ l'équation $2\sin^2 x - 3\sin x + 1 = 0$.
> Posons $X = \sin x$. L'équation devient un trinôme du second degré :
> $$2X^2 - 3X + 1 = 0.$$
> $\Delta = (-3)^2 - 4(2)(1) = 9 - 8 = 1$.
> Les racines en $X$ sont $X_1 = \dfrac{3 - 1}{4} = \dfrac{1}{2}$ et $X_2 = \dfrac{3 + 1}{4} = 1$.
> 
> Revenons à $\sin x$ :
> 1. $\sin x = 1 \iff x = \dfrac{\pi}{2}$.
> 2. $\sin x = \dfrac{1}{2} = \sin\left(\dfrac{\pi}{6}\right) \iff x = \dfrac{\pi}{6}$ ou $x = \pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}$.
>
> Les solutions dans $[0\,; 2\pi[$ sont : $\mathcal{S} = \left\{ \dfrac{\pi}{6} \; ; \; \dfrac{\pi}{2} \; ; \; \dfrac{5\pi}{6} \right\}$.

#### 5.3 Inéquations trigonométriques

Pour résoudre une inéquation du type $\cos x \geq c$ ou $\sin x < c$, on lit directement l'ensemble des solutions sur le cercle trigonométrique en traçant la droite frontière verticale ($x = c$) ou horizontale ($y = c$).

> **Exemple résolu 5 — Inéquation sur $[-\pi\,; \pi]$.**
> Résoudre sur $[-\pi\,; \pi]$ l'inéquation $\sin x \geq -\dfrac{\sqrt{2}}{2}$.
> Traçons la droite horizontale d'ordonnée $y = -\dfrac{\sqrt{2}}{2}$.
> Elle coupe le cercle aux angles $-\dfrac{\pi}{4}$ et $-\dfrac{3\pi}{4}$.
> La zone où l'ordonnée est supérieure ou égale à $-\dfrac{\sqrt{2}}{2}$ correspond à l'arc supérieur.
> En parcourant l'intervalle de $-\pi$ à $\pi$ :
> - de $-\pi$ à $-\dfrac{3\pi}{4}$ : $\sin x \geq -\dfrac{\sqrt{2}}{2}$ ;
> - de $-\dfrac{3\pi}{4}$ à $-\dfrac{\pi}{4}$ : $\sin x < -\dfrac{\sqrt{2}}{2}$ ;
> - de $-\dfrac{\pi}{4}$ à $\pi$ : $\sin x \geq -\dfrac{\sqrt{2}}{2}$.
>
> L'ensemble des solutions est :
> $$\mathcal{S} = \left[ -\pi \; ; \; -\dfrac{3\pi}{4} \right] \cup \left[ -\dfrac{\pi}{4} \; ; \; \pi \right].$$

---

### 6. Le monde des signaux et des ondes : modélisations concrètes

Une oscillation physique réelle ne fait pas toujours un aller-retour en $2\pi$ secondes, et son amplitude n'est pas forcément égale à 1 mètre. On utilise la forme générale d'un **signal sinusoïdal** :

$$s(t) = A \cos(\omega t + \varphi)$$

où :
- **$A > 0$** est **l'amplitude** (la valeur maximale atteinte par le signal) ;
- **$\omega > 0$** est la **pulsation** (en radians par seconde, $\text{rad}\cdot\text{s}^{-1}$) ;
- **$T = \dfrac{2\pi}{\omega}$** est la **période** temporelle (durée d'un cycle complet en secondes) ;
- **$f = \dfrac{1}{T} = \dfrac{\omega}{2\pi}$** est la **fréquence** (nombre de cycles par seconde, en Hertz $\text{Hz}$) ;
- **$\varphi$** est la **phase à l'origine** (le déphasage au temps $t = 0$).

#### 6.1 Le courant alternatif du réseau électrique

Dans les prises de courant européennes, la tension électrique est une onde sinusoïdale de fréquence $f = 50\text{ Hz}$.
La pulsation est $\omega = 2\pi f = 2\pi \times 50 = 100\pi \approx 314{,}16\text{ rad}\cdot\text{s}^{-1}$.
La période d'oscillation est $T = \dfrac{1}{50} = 0{,}02\text{ s} = 20\text{ millisecondes}$.
La tension efficace de $230\text{ V}$ correspond à une amplitude maximale de crête $U_{\max} = 230 \sqrt{2} \approx 325\text{ V}$ :
$$u(t) = 325 \cos(100\pi t).$$

#### 6.2 Les notes de musique et l'acoustique

Le son pur produit par un diapason est une variation de pression de l'air de forme purement sinusoïdale.
Le « *La 440* » de référence des musiciens correspond à 440 vibrations complètes par seconde ($f = 440\text{ Hz}$).
La longueur d'onde dans l'air (à la vitesse du son $c \approx 340\text{ m}\cdot\text{s}^{-1}$) est :
$$\lambda = \dfrac{c}{f} = \dfrac{340}{440} \approx 0{,}77\text{ m}.$$

> **💻 Simulation Python — Échantillonnage d'une sinusoïde :**
> ```python
> import math
>
> def signal_sinusoidal(amplitude, frequence, duree, nb_points):
>     omega = 2 * math.pi * frequence
>     pas = duree / nb_points
>     points = []
>     for i in range(nb_points):
>         t = i * pas
>         valeur = amplitude * math.sin(omega * t)
>         points.append((round(t, 4), round(valeur, 3)))
>     return points
>
> # Générons un signal de 50 Hz pendant 0.02 seconde (1 période complète)
> ech = signal_sinusoidal(amplitude=325, frequence=50, duree=0.02, nb_points=5)
> print("Points échantillonnés :", ech)
> ```

---

### Ce qu'il faut retenir

#### 1. Le cercle trigonométrique et les symétries
- Le radian mesure la longueur d'arc : $180^\circ = \pi\text{ rad}$.
- Coordonnées : $M(x) = (\cos x\,; \sin x)$, d'où $\cos^2 x + \sin^2 x = 1$ et $-1 \leq \cos x, \sin x \leq 1$.
- Périodicité : $\cos(x+2\pi) = \cos x$ et $\sin(x+2\pi) = \sin x$.
- Parité : $\cos(-x) = \cos x$ (cosinus est paire) ; $\sin(-x) = -\sin x$ (sinus est impaire).
- Formules d'angles associés : $\cos\left(\dfrac{\pi}{2}-x\right) = \sin x$ et $\sin\left(\dfrac{\pi}{2}-x\right) = \cos x$.

#### 2. Dérivation fondamentale
- Limite remarquable à l'origine : $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$ et $\lim\limits_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$.
- Dérivées des fonctions usuelles :
  $$(\sin x)' = \cos x \quad \text{et} \quad (\cos x)' = -\sin x.$$
- Dérivées des fonctions composées :
  $$\big(\sin(u)\big)' = u' \cos(u) \quad \text{et} \quad \big(\cos(u)\big)' = -u' \sin(u).$$
- En particulier : $\big(\cos(\omega t + \varphi)\big)' = -\omega \sin(\omega t + \varphi)$.
- Dérivée seconde : $(\sin)''(x) = -\sin x$ et $(\cos)''(x) = -\cos x$.
- Équation différentielle de l'oscillateur harmonique : $y'' + \omega^2 y = 0$.

#### 3. Allure des courbes et tangentes
- Tangente à l'origine de $\sin$ : $y = x$. Pour $x$ proche de 0, $\sin x \approx x$.
- Tangente au sommet de $\cos$ en 0 : $y = 1$ (tangente horizontale).
- Période $T = \dfrac{2\pi}{\omega}$ et fréquence $f = \dfrac{1}{T}$.

#### 4. Résolution des équations trigonométriques
- $\cos x = \cos \alpha \iff x = \alpha + 2k\pi$ ou $x = -\alpha + 2k\pi$.
- $\sin x = \sin \alpha \iff x = \alpha + 2k\pi$ ou $x = \pi - \alpha + 2k\pi$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 49.1 —** Conversions et valeurs exactes.
1. Convertir en radians les angles suivants : $15^\circ$, $75^\circ$, $150^\circ$, $315^\circ$.
2. Donner sans calculatrice les valeurs exactes de :
   $A = \cos\left(\dfrac{2\pi}{3}\right)$, $\quad B = \sin\left(-\dfrac{\pi}{4}\right)$, $\quad C = \cos\left(\dfrac{7\pi}{6}\right)$, $\quad D = \sin\left(\dfrac{5\pi}{2}\right)$.

**Exercice 49.2 —** Simplification d'expressions trigonométriques.
Simplifier pour tout réel $x$ :
1. $E(x) = \cos(x + \pi) + \sin\left(x + \dfrac{\pi}{2}\right)$
2. $F(x) = \sin(\pi - x) - \cos\left(\dfrac{\pi}{2} - x\right)$
3. $G(x) = \cos(-x) + \cos(\pi - x) + \sin(-x) + \sin(\pi + x)$
4. $H(x) = (\cos x + \sin x)^2 + (\cos x - \sin x)^2$

**Exercice 49.3 —** Calculs de dérivées directes.
Dériver sur $\mathbb{R}$ les fonctions suivantes :
1. $f_1(x) = 3\sin x - 2\cos x$
2. $f_2(x) = x \sin x$
3. $f_3(x) = \dfrac{\cos x}{x^2 + 1}$
4. $f_4(x) = \sin(5x - 2)$
5. $f_5(x) = \cos(4x^2)$

**Exercice 49.4 —** Équations élémentaires dans $\mathbb{R}$.
Résoudre dans $\mathbb{R}$ :
1. $\cos x = \dfrac{\sqrt{3}}{2}$
2. $\sin x = -\dfrac{1}{2}$
3. $\cos(3x) = 0$
4. $\sin(2x) = 1$

**Exercice 49.5 —** Équations sur un intervalle restreint.
1. Résoudre $\cos x = -\dfrac{\sqrt{2}}{2}$ sur l'intervalle $[0\,; 2\pi]$.
2. Résoudre $\sin(2x) = \dfrac{\sqrt{3}}{2}$ sur l'intervalle $[-\pi\,; \pi]$.

**Exercice 49.6 —** Inéquations immédiates.
Résoudre sur $[-\pi\,; \pi]$ :
1. $\cos x > 0$
2. $\sin x \leq \dfrac{1}{2}$

**Exercice 49.7 —** Calcul de limites trigonométriques.
Déterminer :
1. $\lim\limits_{x \to 0} \dfrac{\sin(3x)}{x}$
2. $\lim\limits_{x \to 0} \dfrac{\tan x}{x}$
3. $\lim\limits_{x \to +\infty} \dfrac{\cos x}{x}$ (utiliser le théorème des gendarmes)

---

#### Niveau ★★ (Réflexion et Baccalauréat)

**Exercice 49.8 —** Équation du second degré en cosinus.
Résoudre sur $[0\,; 2\pi[$ l'équation :
$$2\cos^2 x + \cos x - 1 = 0.$$

**Exercice 49.9 —** Étude d'une fonction oscillante amortie.
Soit $f$ la fonction définie sur $[0\,; +\infty[$ par $f(t) = e^{-t} \sin t$.
1. Déterminer la limite de $f$ en $+\infty$.
2. Calculer $f'(t)$ et montrer que $f'(t) = \sqrt{2} e^{-t} \cos\left(t + \dfrac{\pi}{4}\right)$.
3. Dresser le tableau de variations de $f$ sur l'intervalle $[0\,; 2\pi]$.
4. Tracer l'allure de la courbe en faisant apparaître les courbes enveloppes $y = e^{-t}$ et $y = -e^{-t}$.

**Exercice 49.10 —** Étude complète d'une fonction trigonométrique classique.
Soit $f$ la fonction définie sur $\mathbb{R}$ par :
$$f(x) = \cos(2x) + 2\cos x.$$
1. Montrer que $f$ est $2\pi$-périodique et paire. En déduire que l'on peut limiter l'étude à l'intervalle $[0\,; \pi]$.
2. Calculer $f'(x)$ et montrer que $f'(x) = -2\sin x (2\cos x + 1)$.
3. Étudier le signe de $f'(x)$ sur $[0\,; \pi]$ et dresser le tableau de variations de $f$ sur cet intervalle.
4. Préciser les extremums de $f$ sur $[0\,; \pi]$.

**Exercice 49.11 —** Tangentes et approximation locale.
Soit $g(x) = \dfrac{\sin x}{2 + \cos x}$ définie sur $\mathbb{R}$.
1. Justifier que le dénominateur ne s'annule jamais sur $\mathbb{R}$.
2. Démontrer que la fonction $g$ est impaire.
3. Calculer $g'(x)$ et montrer que $g'(x) = \dfrac{2\cos x + 1}{(2 + \cos x)^2}$.
4. Déterminer l'équation de la tangente $T$ à la courbe de $g$ à l'origine $(0\,;0)$.

**Exercice 49.12 —** Formules d'addition et calculs d'angles.
1. Démontrer que pour tous réels $a$ et $b$ :
   $$\cos(a+b)\cos(a-b) = \cos^2 a - \sin^2 b.$$
2. Résoudre dans $\mathbb{R}$ l'équation $\cos(3x) = \sin(2x)$ en utilisant $\sin(u) = \cos\left(\dfrac{\pi}{2} - u\right)$.

**Exercice 49.13 —** Convexité et points d'inflexion.
Soit $f(x) = \sin^2 x$ définie sur $[0\,; \pi]$.
1. Exprimer $f(x)$ à l'aide de $\cos(2x)$.
2. Calculer $f'(x)$ puis $f''(x)$.
3. Déterminer les intervalles sur lesquels $f$ est convexe, puis concave.
4. Préciser les coordonnées des points d'inflexion sur $[0\,; \pi]$.

**Exercice 49.14 —** Modélisation d'une marée océanique.
Dans un port breton, la hauteur de la mer $H(t)$ (en mètres) est modélisée en fonction du temps $t$ (en heures écoulées depuis minuit) par :
$$H(t) = 6 + 4 \cos\left(\dfrac{\pi}{6} t - \dfrac{\pi}{3}\right).$$
1. Quelle est la période de la marée ?
2. Quelle est la hauteur d'eau à marée haute (pleine mer) ? À marée basse (basse mer) ?
3. À quelle heure de la matinée (pour $t \in [0\,; 12]$) la marée haute est-elle atteinte ?
4. Un chalutier ne peut entrer dans le port que si la hauteur d'eau dépasse $8\text{ mètres}$. Sur quels créneaux horaires de la matinée le chalutier peut-il naviguer en toute sécurité ?

**Exercice 49.15 —** Limites de formes indéterminées avec trigonométrie.
Déterminer en justifiant :
1. $\lim\limits_{x \to 0} \dfrac{1 - \cos(2x)}{x \sin x}$
2. $\lim\limits_{x \to \pi/2} \dfrac{\cos x}{x - \dfrac{\pi}{2}}$
3. $\lim\limits_{x \to 0} \dfrac{\sqrt{1 + \sin x} - \sqrt{1 - \sin x}}{x}$

---

#### Niveau ★★★ (Approfondissement et Défis)

**Exercice 49.16 —** La formule de Machin et le calcul de $\pi$.
On définit la fonction tangente par $\tan x = \dfrac{\sin x}{\cos x}$ pour $x \in \left]-\dfrac{\pi}{2}\,; \dfrac{\pi}{2}\right[$.
1. Montrer que $\tan(a+b) = \dfrac{\tan a + \tan b}{1 - \tan a \tan b}$.
2. Soit $\alpha$ tel que $\tan \alpha = \dfrac{1}{5}$. Calculer $\tan(2\alpha)$ puis $\tan(4\alpha)$.
3. En déduire la remarquable relation de John Machin (1706) :
   $$\dfrac{\pi}{4} = 4 \arctan\left(\dfrac{1}{5}\right) - \arctan\left(\dfrac{1}{239}\right).$$
   *(Cette formule a permis de calculer les 100 premières décimales de $\pi$ à la main !)*

**Exercice 49.17 —** Somme trigonométrique de Dirichlet.
Pour $n \in \mathbb{N}^*$ et $x \in \mathbb{R} \setminus 2\pi\mathbb{Z}$, on pose :
$$S_n(x) = \dfrac{1}{2} + \sum_{k=1}^n \cos(kx) = \dfrac{1}{2} + \cos x + \cos(2x) + \dots + \cos(nx).$$
1. Démontrer la relation trigonométrique : $2\sin\left(\dfrac{x}{2}\right)\cos(kx) = \sin\left(\left(k+\dfrac{1}{2}\right)x\right) - \sin\left(\left(k-\dfrac{1}{2}\right)x\right)$.
2. En multipliant $S_n(x)$ par $2\sin\left(\dfrac{x}{2}\right)$, obtenir par somme télescopique :
   $$S_n(x) = \dfrac{\sin\left(\left(n+\dfrac{1}{2}\right)x\right)}{2\sin\left(\dfrac{x}{2}\right)}.$$
   *(Ce noyau de Dirichlet est au cœur de la théorie des séries de Fourier).*

**Exercice 49.18 —** Inégalité de Jordan et encadrement fin.
1. Démontrer que la fonction $f(x) = \dfrac{\sin x}{x}$ est strictement décroissante sur $\left]0\,; \dfrac{\pi}{2}\right]$.
2. En déduire la célèbre **inégalité de Jordan** :
   $$\text{Pour tout } x \in \left[0\,; \dfrac{\pi}{2}\right] : \quad \dfrac{2}{\pi} x \leq \sin x \leq x.$$
3. Interpréter graphiquement cette inégalité à l'aide de la corde et de la tangente.

**Exercice 49.19 —** Système oscillant couplé et déphasage.
On considère deux signaux $s_1(t) = 3\cos(\omega t)$ et $s_2(t) = 4\sin(\omega t)$.
On forme la somme $S(t) = s_1(t) + s_2(t)$.
1. Montrer qu'il existe une amplitude $A > 0$ et un angle de phase $\varphi \in [0\,; 2\pi[$ tels que :
   $$S(t) = A \cos(\omega t - \varphi).$$
2. Calculer exactement $A$ et donner une valeur approchée de $\varphi$.
3. Généralisation : Montrer que toute combinaison linéaire $a\cos(\omega t) + b\sin(\omega t)$ peut s'écrire sous la forme $R\cos(\omega t - \theta)$ avec $R = \sqrt{a^2 + b^2}$.

**Exercice 49.20 —** Absence de limite en l'infini.
Démontrer rigoureusement à l'aide de suites que la fonction $x \mapsto \cos x$ n'admet **aucune limite** lorsque $x \to +\infty$.

---

### Solutions

#### Solutions du Niveau ★

**Solution 49.1 :**
1. Formule de conversion : $\theta_{\text{rad}} = \theta_{\text{deg}} \times \dfrac{\pi}{180}$.
   - $15^\circ = 15 \times \dfrac{\pi}{180} = \dfrac{\pi}{12}\text{ rad}$.
   - $75^\circ = 75 \times \dfrac{\pi}{180} = \dfrac{5\pi}{12}\text{ rad}$.
   - $150^\circ = 150 \times \dfrac{\pi}{180} = \dfrac{5\pi}{6}\text{ rad}$.
   - $315^\circ = 315 \times \dfrac{\pi}{180} = \dfrac{7\pi}{4}\text{ rad}$.
2. Valeurs exactes :
   - $A = \cos\left(\pi - \dfrac{\pi}{3}\right) = -\cos\left(\dfrac{\pi}{3}\right) = -\dfrac{1}{2}$.
   - $B = \sin\left(-\dfrac{\pi}{4}\right) = -\sin\left(\dfrac{\pi}{4}\right) = -\dfrac{\sqrt{2}}{2}$.
   - $C = \cos\left(\pi + \dfrac{\pi}{6}\right) = -\cos\left(\dfrac{\pi}{6}\right) = -\dfrac{\sqrt{3}}{2}$.
   - $D = \sin\left(2\pi + \dfrac{\pi}{2}\right) = \sin\left(\dfrac{\pi}{2}\right) = 1$.

**Solution 49.2 :**
1. $E(x) = -\cos x + \cos x = 0$.
2. $F(x) = \sin x - \sin x = 0$.
3. $G(x) = \cos x - \cos x - \sin x - \sin x = -2\sin x$.
4. Développons : $(\cos^2 x + 2\sin x \cos x + \sin^2 x) + (\cos^2 x - 2\sin x \cos x + \sin^2 x) = 2(\cos^2 x + \sin^2 x) = 2 \times 1 = 2$.

**Solution 49.3 :**
1. $f'_1(x) = 3\cos x - 2(-\sin x) = 3\cos x + 2\sin x$.
2. Produit $(uv)' = u'v + uv'$ : $f'_2(x) = 1 \times \sin x + x \cos x = \sin x + x \cos x$.
3. Quotient $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$ :
   $f'_3(x) = \dfrac{(-\sin x)(x^2+1) - \cos x(2x)}{(x^2+1)^2} = \dfrac{-(x^2+1)\sin x - 2x\cos x}{(x^2+1)^2}$.
4. Dérivée composée : $f'_4(x) = 5\cos(5x - 2)$.
5. Dérivée composée : $u(x) = 4x^2 \implies u'(x) = 8x$, donc $f'_5(x) = -8x \sin(4x^2)$.

**Solution 49.4 :**
1. $\cos x = \dfrac{\sqrt{3}}{2} = \cos\left(\dfrac{\pi}{6}\right) \iff x = \dfrac{\pi}{6} + 2k\pi$ ou $x = -\dfrac{\pi}{6} + 2k\pi$ ($k \in \mathbb{Z}$).
2. $\sin x = -\dfrac{1}{2} = \sin\left(-\dfrac{\pi}{6}\right) \iff x = -\dfrac{\pi}{6} + 2k\pi$ ou $x = \pi - \left(-\dfrac{\pi}{6}\right) + 2k\pi = \dfrac{7\pi}{6} + 2k\pi$ ($k \in \mathbb{Z}$).
3. $\cos(3x) = 0 = \cos\left(\dfrac{\pi}{2}\right) \iff 3x = \dfrac{\pi}{2} + k\pi \iff x = \dfrac{\pi}{6} + \dfrac{k\pi}{3}$ ($k \in \mathbb{Z}$).
4. $\sin(2x) = 1 = \sin\left(\dfrac{\pi}{2}\right) \iff 2x = \dfrac{\pi}{2} + 2k\pi \iff x = \dfrac{\pi}{4} + k\pi$ ($k \in \mathbb{Z}$).

**Solution 49.5 :**
1. $\cos x = -\dfrac{\sqrt{2}}{2} = \cos\left(\dfrac{3\pi}{4}\right)$.
   Les solutions dans $\mathbb{R}$ sont $x = \dfrac{3\pi}{4} + 2k\pi$ et $x = -\dfrac{3\pi}{4} + 2k\pi$.
   Dans $[0\,; 2\pi]$ : pour $k=0$, $x_1 = \dfrac{3\pi}{4}$ ; pour $k=1$ dans la seconde, $x_2 = 2\pi - \dfrac{3\pi}{4} = \dfrac{5\pi}{4}$.
   $\mathcal{S} = \left\{\dfrac{3\pi}{4} \; ; \; \dfrac{5\pi}{4}\right\}$.
2. $\sin(2x) = \dfrac{\sqrt{3}}{2} = \sin\left(\dfrac{\pi}{3}\right)$.
   Donc $2x = \dfrac{\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{6} + k\pi$ ou $2x = \dfrac{2\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{3} + k\pi$.
   Dans $[-\pi\,; \pi]$ :
   - $x = \dfrac{\pi}{6} + k\pi$ donne pour $k = 0 : \dfrac{\pi}{6}$ et pour $k = -1 : -\dfrac{5\pi}{6}$.
   - $x = \dfrac{\pi}{3} + k\pi$ donne pour $k = 0 : \dfrac{\pi}{3}$ et pour $k = -1 : -\dfrac{2\pi}{3}$.
   $\mathcal{S} = \left\{ -\dfrac{5\pi}{6} \; ; \; -\dfrac{2\pi}{3} \; ; \; \dfrac{\pi}{6} \; ; \; \dfrac{\pi}{3} \right\}$.

**Solution 49.6 :**
1. $\cos x > 0$ sur $[-\pi\,; \pi]$ : correspond aux abscisses strictement positives du cercle, soit $\mathcal{S} = \left]-\dfrac{\pi}{2} \; ; \; \dfrac{\pi}{2}\right[$.
2. $\sin x \leq \dfrac{1}{2}$ sur $[-\pi\,; \pi]$ : la droite $y = 1/2$ coupe en $-\dfrac{7\pi}{6}$ (qui vaut $\dfrac{5\pi}{6}$) et $\dfrac{\pi}{6}$.
   Sur $[-\pi\,; \pi]$, l'ordonnée est inférieure ou égale à $1/2$ sur $\left[-\pi \; ; \; \dfrac{\pi}{6}\right] \cup \left[\dfrac{5\pi}{6} \; ; \; \pi\right]$.

**Solution 49.7 :**
1. Posons $u = 3x$. Quand $x \to 0$, $u \to 0$.
   $\dfrac{\sin(3x)}{x} = 3 \times \dfrac{\sin u}{u}$. Comme $\lim\limits_{u \to 0} \dfrac{\sin u}{u} = 1$, la limite vaut $3 \times 1 = 3$.
2. $\dfrac{\tan x}{x} = \dfrac{\sin x}{x \cos x} = \dfrac{\sin x}{x} \times \dfrac{1}{\cos x}$.
   Or $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$ et $\lim\limits_{x \to 0} \cos x = 1$. La limite vaut $1 \times 1 = 1$.
3. Pour tout réel $x > 0$, $-1 \leq \cos x \leq 1 \iff -\dfrac{1}{x} \leq \dfrac{\cos x}{x} \leq \dfrac{1}{x}$.
   Comme $\lim\limits_{x \to +\infty} -\dfrac{1}{x} = \lim\limits_{x \to +\infty} \dfrac{1}{x} = 0$, d'après le théorème des gendarmes, $\lim\limits_{x \to +\infty} \dfrac{\cos x}{x} = 0$.

---

#### Solutions du Niveau ★★

**Solution 49.8 :**
Posons $X = \cos x$. L'équation devient $2X^2 + X - 1 = 0$.
$\Delta = 1^2 - 4(2)(-1) = 9 = 3^2$.
$X_1 = \dfrac{-1 - 3}{4} = -1$ et $X_2 = \dfrac{-1 + 3}{4} = \dfrac{1}{2}$.
- $\cos x = -1 \iff x = \pi$ sur $[0\,; 2\pi[$.
- $\cos x = \dfrac{1}{2} = \cos\left(\dfrac{\pi}{3}\right) \iff x = \dfrac{\pi}{3}$ ou $x = 2\pi - \dfrac{\pi}{3} = \dfrac{5\pi}{3}$.
$\mathcal{S} = \left\{ \dfrac{\pi}{3} \; ; \; \pi \; ; \; \dfrac{5\pi}{3} \right\}$.

**Solution 49.9 :**
1. Pour tout $t \geq 0$, $-1 \leq \sin t \leq 1 \iff -e^{-t} \leq e^{-t} \sin t \leq e^{-t}$.
   Comme $\lim\limits_{t \to +\infty} e^{-t} = 0$, le théorème des gendarmes implique $\lim\limits_{t \to +\infty} f(t) = 0$.
2. Dérivée du produit : $f'(t) = -e^{-t}\sin t + e^{-t}\cos t = e^{-t}(\cos t - \sin t)$.
   Or $\cos t - \sin t = \sqrt{2}\left(\dfrac{\sqrt{2}}{2}\cos t - \dfrac{\sqrt{2}}{2}\sin t\right) = \sqrt{2}\left(\cos t \cos\dfrac{\pi}{4} - \sin t \sin\dfrac{\pi}{4}\right) = \sqrt{2}\cos\left(t + \dfrac{\pi}{4}\right)$.
   Donc $f'(t) = \sqrt{2} e^{-t} \cos\left(t + \dfrac{\pi}{4}\right)$.
3. Sur $[0\,; 2\pi]$, $e^{-t} > 0$, donc $f'(t)$ s'annule quand $\cos\left(t + \dfrac{\pi}{4}\right) = 0$ :
   $t + \dfrac{\pi}{4} = \dfrac{\pi}{2} \iff t_1 = \dfrac{\pi}{4}$, et $t + \dfrac{\pi}{4} = \dfrac{3\pi}{2} \iff t_2 = \dfrac{5\pi}{4}$.
   - Sur $\left[0\,; \dfrac{\pi}{4}\right]$, $f'(t) \geq 0$ : $f$ croît de $0$ à $f(\pi/4) = \dfrac{\sqrt{2}}{2} e^{-\pi/4} \approx 0{,}322$.
   - Sur $\left[\dfrac{\pi}{4}\,; \dfrac{5\pi}{4}\right]$, $f'(t) \leq 0$ : $f$ décroît jusqu'à $f(5\pi/4) = -\dfrac{\sqrt{2}}{2} e^{-5\pi/4} \approx -0{,}014$.
   - Sur $\left[\dfrac{5\pi}{4}\,; 2\pi\right]$, $f'(t) \geq 0$ : $f$ remonte jusqu'à $f(2\pi) = 0$.
4. L'oscillation sinusoïdale est pincée entre les deux courbes exponentielles amorties $y = e^{-t}$ et $y = -e^{-t}$, touchant alternativement ces enveloppes aux crêtes et creux déphasés.

**Solution 49.10 :**
1. $f(x+2\pi) = \cos(2x+4\pi) + 2\cos(x+2\pi) = \cos(2x) + 2\cos x = f(x)$ : $f$ est $2\pi$-périodique.
   $f(-x) = \cos(-2x) + 2\cos(-x) = \cos(2x) + 2\cos x = f(x)$ : $f$ est paire.
   On peut donc restreindre l'étude à un demi-intervalle de période : $[0\,; \pi]$.
2. $f'(x) = -2\sin(2x) - 2\sin x$.
   Comme $\sin(2x) = 2\sin x \cos x$, on a :
   $f'(x) = -2(2\sin x \cos x) - 2\sin x = -2\sin x(2\cos x + 1)$.
3. Sur $]0\,; \pi[$, $\sin x > 0$, donc le signe de $f'(x)$ est l'opposé de celui de $2\cos x + 1$ :
   - $2\cos x + 1 = 0 \iff \cos x = -\dfrac{1}{2} \iff x = \dfrac{2\pi}{3}$.
   - Pour $x \in \left[0\,; \dfrac{2\pi}{3}\right[$, $\cos x > -1/2 \implies 2\cos x + 1 > 0 \implies f'(x) < 0$.
   - Pour $x \in \left]\dfrac{2\pi}{3}\,; \pi\right]$, $\cos x < -1/2 \implies 2\cos x + 1 < 0 \implies f'(x) > 0$.
   $f$ est donc strictement décroissante sur $\left[0\,; \dfrac{2\pi}{3}\right]$, puis strictement croissante sur $\left[\dfrac{2\pi}{3}\,; \pi\right]$.
4. - Maximum en $x = 0$ : $f(0) = \cos 0 + 2\cos 0 = 1 + 2 = 3$.
   - Minimum absolu en $x = \dfrac{2\pi}{3}$ : $f\left(\dfrac{2\pi}{3}\right) = \cos\left(\dfrac{4\pi}{3}\right) + 2\cos\left(\dfrac{2\pi}{3}\right) = -\dfrac{1}{2} + 2\left(-\dfrac{1}{2}\right) = -\dfrac{3}{2}$.
   - En $x = \pi$ : $f(\pi) = \cos(2\pi) + 2\cos(\pi) = 1 - 2 = -1$ (maximum relatif).

**Solution 49.11 :**
1. Pour tout $x \in \mathbb{R}$, $\cos x \geq -1$, donc $2 + \cos x \geq 2 - 1 = 1 > 0$. Le dénominateur ne s'annule jamais.
2. $g(-x) = \dfrac{\sin(-x)}{2 + \cos(-x)} = \dfrac{-\sin x}{2 + \cos x} = -g(x)$. La fonction $g$ est impaire.
3. Formule du quotient :
   $g'(x) = \dfrac{\cos x(2+\cos x) - \sin x(-\sin x)}{(2+\cos x)^2} = \dfrac{2\cos x + \cos^2 x + \sin^2 x}{(2+\cos x)^2} = \dfrac{2\cos x + 1}{(2+\cos x)^2}$.
4. En $x = 0$ : $g(0) = 0$ et $g'(0) = \dfrac{2(1)+1}{(2+1)^2} = \dfrac{3}{9} = \dfrac{1}{3}$.
   L'équation de la tangente $T$ à l'origine est : $y = \dfrac{1}{3}x$.

**Solution 49.12 :**
1. $\cos(a+b)\cos(a-b) = (\cos a \cos b - \sin a \sin b)(\cos a \cos b + \sin a \sin b) = \cos^2 a \cos^2 b - \sin^2 a \sin^2 b$.
   Remplaçons $\cos^2 b$ par $1 - \sin^2 b$ et $\sin^2 a$ par $1 - \cos^2 a$ :
   $= \cos^2 a(1 - \sin^2 b) - (1 - \cos^2 a)\sin^2 b = \cos^2 a - \cos^2 a \sin^2 b - \sin^2 b + \cos^2 a \sin^2 b = \cos^2 a - \sin^2 b$.
2. $\cos(3x) = \sin(2x) \iff \cos(3x) = \cos\left(\dfrac{\pi}{2} - 2x\right)$.
   Cela donne deux séries :
   - $3x = \dfrac{\pi}{2} - 2x + 2k\pi \iff 5x = \dfrac{\pi}{2} + 2k\pi \iff x = \dfrac{\pi}{10} + \dfrac{2k\pi}{5}$ ($k \in \mathbb{Z}$).
   - $3x = -\left(\dfrac{\pi}{2} - 2x\right) + 2k\pi \iff 3x = -\dfrac{\pi}{2} + 2x + 2k\pi \iff x = -\dfrac{\pi}{2} + 2k\pi$ ($k \in \mathbb{Z}$).

**Solution 49.13 :**
1. Puisque $\cos(2x) = 1 - 2\sin^2 x$, on a $f(x) = \sin^2 x = \dfrac{1 - \cos(2x)}{2} = \dfrac{1}{2} - \dfrac{1}{2}\cos(2x)$.
2. $f'(x) = -\dfrac{1}{2}(-2\sin(2x)) = \sin(2x)$.
   $f''(x) = 2\cos(2x)$.
3. Le signe de $f''(x)$ dépend de $\cos(2x)$ sur $[0\,; \pi]$ :
   - $2x \in [0\,; \pi/2] \iff x \in [0\,; \pi/4]$ : $\cos(2x) \geq 0 \implies f''(x) \geq 0$, $f$ est **convexe**.
   - $2x \in [\pi/2\,; 3\pi/2] \iff x \in [\pi/4\,; 3\pi/4]$ : $\cos(2x) \leq 0 \implies f''(x) \leq 0$, $f$ est **concave**.
   - $2x \in [3\pi/2\,; 2\pi] \iff x \in [3\pi/4\,; \pi]$ : $\cos(2x) \geq 0 \implies f''(x) \geq 0$, $f$ est **convexe**.
4. $f''(x)$ s'annule en changeant de signe en $x = \dfrac{\pi}{4}$ et $x = \dfrac{3\pi}{4}$.
   Les points d'inflexion sont $I_1\left(\dfrac{\pi}{4}\,; \dfrac{1}{2}\right)$ et $I_2\left(\dfrac{3\pi}{4}\,; \dfrac{1}{2}\right)$.

**Solution 49.14 :**
1. La pulsation est $\omega = \dfrac{\pi}{6}$. La période est $T = \dfrac{2\pi}{\omega} = \dfrac{2\pi}{\pi/6} = 12\text{ heures}$.
2. Le cosinus varie entre $-1$ et $1$.
   - Hauteur maximale (pleine mer) : $H_{\max} = 6 + 4(1) = 10\text{ mètres}$.
   - Hauteur minimale (basse mer) : $H_{\min} = 6 + 4(-1) = 2\text{ mètres}$.
3. Marée haute atteinte quand le cosinus vaut $1$ :
   $\dfrac{\pi}{6}t - \dfrac{\pi}{3} = 0 \iff \dfrac{\pi}{6}t = \dfrac{\pi}{3} \iff t = 2$.
   La marée haute a lieu à **2h du matin** (puis à $2 + 12 = 14\text{h}$, soit 14h de l'après-midi).
4. $H(t) \geq 8 \iff 6 + 4\cos\left(\dfrac{\pi}{6}t - \dfrac{\pi}{3}\right) \geq 8 \iff \cos\left(\dfrac{\pi}{6}t - \dfrac{\pi}{3}\right) \geq \dfrac{1}{2}$.
   Or $\cos \theta \geq \dfrac{1}{2} \iff -\dfrac{\pi}{3} \leq \theta \leq \dfrac{\pi}{3}$ (modulo $2\pi$).
   Ici : $-\dfrac{\pi}{3} \leq \dfrac{\pi}{6}t - \dfrac{\pi}{3} \leq \dfrac{\pi}{3} \iff 0 \leq \dfrac{\pi}{6}t \leq \dfrac{2\pi}{3} \iff 0 \leq t \leq 4$.
   Le chalutier peut naviguer en sécurité **entre minuit et 4h du matin** (puis entre 12h et 16h).

**Solution 49.15 :**
1. $1 - \cos(2x) = 2\sin^2 x$. L'expression s'écrit $\dfrac{2\sin^2 x}{x \sin x} = 2 \dfrac{\sin x}{x}$.
   Quand $x \to 0$, cela tend vers $2 \times 1 = 2$.
2. Posons $h = x - \dfrac{\pi}{2} \to 0$, donc $x = \dfrac{\pi}{2} + h$.
   Le quotient devient $\dfrac{\cos(\pi/2 + h)}{h} = \dfrac{-\sin h}{h} = -\dfrac{\sin h}{h}$.
   Comme $\lim\limits_{h \to 0} \dfrac{\sin h}{h} = 1$, la limite vaut $-1$.
3. Expression conjuguée :
   $\dfrac{\sqrt{1+\sin x} - \sqrt{1-\sin x}}{x} = \dfrac{(1+\sin x) - (1-\sin x)}{x(\sqrt{1+\sin x} + \sqrt{1-\sin x})} = \dfrac{2\sin x}{x(\sqrt{1+\sin x} + \sqrt{1-\sin x})} = \dfrac{\sin x}{x} \times \dfrac{2}{\sqrt{1+\sin x} + \sqrt{1-\sin x}}$.
   Quand $x \to 0$, $\dfrac{\sin x}{x} \to 1$ et le second facteur tend vers $\dfrac{2}{\sqrt{1} + \sqrt{1}} = 1$. La limite est donc $1$.

---

#### Solutions du Niveau ★★★

**Solution 49.16 :**
1. $\tan(a+b) = \dfrac{\sin(a+b)}{\cos(a+b)} = \dfrac{\sin a \cos b + \cos a \sin b}{\cos a \cos b - \sin a \sin b}$.
   En divisant numérateur et dénominateur par le produit $\cos a \cos b$ (supposé non nul), on obtient immédiatement $\tan(a+b) = \dfrac{\tan a + \tan b}{1 - \tan a \tan b}$.
2. Avec $\tan \alpha = \dfrac{1}{5}$ :
   $\tan(2\alpha) = \dfrac{2(1/5)}{1 - (1/5)^2} = \dfrac{2/5}{24/25} = \dfrac{2}{5} \times \dfrac{25}{24} = \dfrac{5}{12}$.
   Puis :
   $\tan(4\alpha) = \dfrac{2(5/12)}{1 - (5/12)^2} = \dfrac{5/6}{119/144} = \dfrac{5}{6} \times \dfrac{144}{119} = \dfrac{120}{119}$.
3. Calculons $\tan\left(4\alpha - \dfrac{\pi}{4}\right)$ :
   Comme $\tan\left(\dfrac{\pi}{4}\right) = 1$, on a :
   $\tan\left(4\alpha - \dfrac{\pi}{4}\right) = \dfrac{\tan(4\alpha) - 1}{1 + \tan(4\alpha)} = \dfrac{\frac{120}{119} - 1}{1 + \frac{120}{119}} = \dfrac{1/119}{239/119} = \dfrac{1}{239}$.
   En prenant la bijection réciproque arctangente :
   $4\alpha - \dfrac{\pi}{4} = \arctan\left(\dfrac{1}{239}\right) \iff \dfrac{\pi}{4} = 4\arctan\left(\dfrac{1}{5}\right) - \arctan\left(\dfrac{1}{239}\right)$.

**Solution 49.17 :**
1. Développons le membre de droite :
   $\sin\left(kx + \dfrac{x}{2}\right) - \sin\left(kx - \dfrac{x}{2}\right) = \left[\sin(kx)\cos\dfrac{x}{2} + \cos(kx)\sin\dfrac{x}{2}\right] - \left[\sin(kx)\cos\dfrac{x}{2} - \cos(kx)\sin\dfrac{x}{2}\right] = 2\cos(kx)\sin\dfrac{x}{2}$.
2. Multiplions $S_n(x)$ par $2\sin\left(\dfrac{x}{2}\right)$ :
   $2\sin\left(\dfrac{x}{2}\right)S_n(x) = \sin\left(\dfrac{x}{2}\right) + \sum_{k=1}^n 2\sin\left(\dfrac{x}{2}\right)\cos(kx)$.
   En injectant la relation précédente :
   $= \sin\left(\dfrac{x}{2}\right) + \sum_{k=1}^n \left[\sin\left(\left(k+\dfrac{1}{2}\right)x\right) - \sin\left(\left(k-\dfrac{1}{2}\right)x\right)\right]$.
   Cette somme est télescopique : tous les termes intermédiaires s'annulent sauf le premier $-\sin\left(\dfrac{x}{2}\right)$ (qui compense exactement le premier terme extérieur) et le dernier $\sin\left(\left(n+\dfrac{1}{2}\right)x\right)$.
   Il reste donc : $2\sin\left(\dfrac{x}{2}\right)S_n(x) = \sin\left(\left(n+\dfrac{1}{2}\right)x\right)$.
   Puisque $x \notin 2\pi\mathbb{Z}$, $\sin\left(\dfrac{x}{2}\right) \neq 0$, d'où la formule du noyau de Dirichlet.

**Solution 49.18 :**
1. Pour $x \in \left]0\,; \dfrac{\pi}{2}\right]$, $f'(x) = \dfrac{x\cos x - \sin x}{x^2} = \dfrac{\cos x(x - \tan x)}{x^2}$.
   Or d'après le lemme fondamental de la section 3.1, pour tout $x \in \left]0\,; \dfrac{\pi}{2}\right[$, on a $x < \tan x \iff x - \tan x < 0$.
   Comme $\cos x > 0$ et $x^2 > 0$, $f'(x) < 0$. La fonction $f$ est strictement décroissante.
2. Pour tout $x \in \left]0\,; \dfrac{\pi}{2}\right]$ :
   $f\left(\dfrac{\pi}{2}\right) \leq f(x) \leq \lim_{t \to 0^+} f(t) \iff \dfrac{\sin(\pi/2)}{\pi/2} \leq \dfrac{\sin x}{x} \leq 1 \iff \dfrac{2}{\pi} \leq \dfrac{\sin x}{x} \leq 1$.
   En multipliant par $x > 0$ : $\dfrac{2}{\pi} x \leq \sin x \leq x$. Cette relation est encore vraie en 0.
3. Graphiquement sur $\left[0\,; \dfrac{\pi}{2}\right]$, la courbe de sinus est coincée entre sa tangente à l'origine ($y = x$) et la corde joignant $(0\,;0)$ à $\left(\dfrac{\pi}{2}\,; 1\right)$ d'équation $y = \dfrac{2}{\pi}x$.

**Solution 49.19 :**
1. $S(t) = 3\cos(\omega t) + 4\sin(\omega t)$.
   Factorisons par $\sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$ :
   $S(t) = 5\left(\dfrac{3}{5}\cos(\omega t) + \dfrac{4}{5}\sin(\omega t)\right)$.
   Puisque $\left(\dfrac{3}{5}\right)^2 + \left(\dfrac{4}{5}\right)^2 = \dfrac{9}{25} + \dfrac{16}{25} = 1$, il existe un unique angle $\varphi \in [0\,; 2\pi[$ tel que $\cos \varphi = \dfrac{3}{5}$ et $\sin \varphi = \dfrac{4}{5}$.
   Alors $S(t) = 5(\cos(\omega t)\cos \varphi + \sin(\omega t)\sin \varphi) = 5\cos(\omega t - \varphi)$.
2. L'amplitude est $A = 5$.
   $\tan \varphi = \dfrac{4/5}{3/5} = \dfrac{4}{3} \implies \varphi = \arctan\left(\dfrac{4}{3}\right) \approx 0{,}927\text{ rad} \approx 53{,}1^\circ$.
3. Dans le cas général, posons $R = \sqrt{a^2 + b^2} > 0$. On a $\left(\dfrac{a}{R}\right)^2 + \left(\dfrac{b}{R}\right)^2 = 1$.
   Il existe $\theta$ tel que $\cos \theta = \dfrac{a}{R}$ et $\sin \theta = \dfrac{b}{R}$.
   Alors $a\cos(\omega t) + b\sin(\omega t) = R\big(\cos(\omega t)\cos \theta + \sin(\omega t)\sin \theta\big) = R\cos(\omega t - \theta)$.

**Solution 49.20 :**
Supposons par l'absurde que la fonction cosinus admette une limite finie ou infinie $L$ en $+\infty$.
D'après la caractérisation séquentielle de la limite, pour toute suite $(u_n)$ tendant vers $+\infty$, la suite $\big(\cos(u_n)\big)$ devrait converger vers $L$.
Considérons la suite $u_n = 2n\pi$. Quand $n \to +\infty$, $u_n \to +\infty$.
Or pour tout $n$, $\cos(u_n) = \cos(2n\pi) = 1$, donc la suite $\big(\cos(u_n)\big)$ est constante égale à 1 et tend vers 1.
Considérons maintenant la suite $v_n = \pi + 2n\pi$. Quand $n \to +\infty$, $v_n \to +\infty$.
Or pour tout $n$, $\cos(v_n) = \cos(\pi + 2n\pi) = -1$, donc la suite $\big(\cos(v_n)\big)$ converge vers $-1$.
Puisque les deux limites $1$ et $-1$ sont distinctes, cela contredit l'unicité de la limite.
La fonction cosinus n'admet donc aucune limite en $+\infty$.

---

### La question qui ouvre la suite

Nous avons appris à mesurer la pente, le taux de variation et la vitesse d'une courbe en chacun de ses points : c'est le calcul différentiel. Mais que se passe-t-il si l'on cherche à faire le chemin inverse ?
Si l'on connaît la vitesse d'une fusée à chaque seconde, comment calculer la distance totale parcourue ? Si l'on connaît le profil d'un tonneau ou la forme ondulée d'une colline, comment calculer exactement son volume et son aire ?

Comment additionner une infinité de lamelles infiniment fines pour reconstituer un tout ?

Rendez-vous au chapitre 50 avec **le tonneau rempli de tranches d'eau** et la découverte du calcul intégral.
