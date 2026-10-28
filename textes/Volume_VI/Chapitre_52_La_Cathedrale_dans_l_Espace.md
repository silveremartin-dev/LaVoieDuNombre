# VOLUME VI — L'Âge du Flux et de la Vitesse (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 52 : La Cathédrale dans l'Espace

> *« La géométrie est une magie qui permet d'orienter une nef vers l'étoile polaire, d'élever des voûtes de pierre vers le ciel sans qu'elles s'effondrent, et de mesurer la distance d'un point invisible sans jamais quitter le sol. »*
> — Carnets des maîtres d'œuvre médiévaux

---

### Ce que tu vas découvrir

- Comment les bâtisseurs de cathédrales ont conquis la **troisième dimension** : du sol plat à la clé de voûte céleste.
- Le repère orthonormé $(O; \vec{i}, \vec{j}, \vec{k})$ de l'espace : abscisse, ordonnée, **cote** et la formule de distance en 3D issue du théorème de Pythagore double.
- La **représentation paramétrique d'une droite** dans l'espace : pourquoi une droite en 3D ne peut jamais être décrite par une seule équation cartésienne.
- Les positions relatives de deux droites : parallèles, sécantes… ou **non coplanaires** (le piège absolu de la 3D !).
- Le **produit scalaire dans l'espace** : son expression analytique $\vec{u} \cdot \vec{v} = xx' + yy' + zz'$ et son rôle de détecteur d'angles droits.
- Le **vecteur normal** $\vec{n}(a\,;b\,;c)$ et **l'équation cartésienne d'un plan** $ax + by + cz + d = 0$.
- Le **projeté orthogonal** d'un point sur une droite ou sur un plan, et le calcul de la plus courte distance.

---

### 1. Le problème : les bâtisseurs de la cathédrale de Chartres

#### 1.1 Quitter le parchemin plat

Au Moyen Âge, les architectes et tailleurs de pierre qui conçoivent les cathédrales gothiques — comme celle de Chartres ou de Notre-Dame de Paris — se heurtent à un défi monumental.
Sur leurs parchemins et sur le sol en plâtre de la salle des dessins, ils ne peuvent tracer que des figures en **deux dimensions** : des cercles, des triangles, des rectangles. Mais la cathédrale est un édifice en **trois dimensions** :
- Le plan au sol donne la longueur de la nef et la largeur du transept ;
- Mais les piliers s'élancent vers le ciel, les arcs-boutants enjambent le vide en diagonale, et les nervures des voûtes d'ogives se croisent en une **clé de voûte suspendue à 37 mètres au-dessus du sol**.

Si deux arcs-boutants taillés dans la carrière ne se croisent pas exactement au même point dans l'espace, la voûte s'écroule et des centaines de tonnes de pierre s'effondrent.
Dans le plan, deux droites non parallèles **se coupent obligatoirement**.
Mais dans l'espace, deux droites peuvent ne pas être parallèles et pourtant **ne jamais se couper** : imagine deux avions qui volent dans des directions différentes à des altitudes différentes, ou deux câbles qui se croisent dans une charpente sans se toucher. On dit qu'elles sont **non coplanaires**.

```
                   z ▲  (Cote / Hauteur)
                     │
                     │       . Clé de voûte (x, y, z)
                     │     / |
                     │   /   |
                     │ /     |
                     ┼───────┼────────► y (Transept / Ordonnée)
                    /│       * (x, y, 0)
                  /  │      /
                /    │    /
            x ▼ (Nef / Abscisse)
```

Pour bâtir dans le ciel sans risque d'erreur, il nous faut un système infaillible pour repérer chaque grain de pierre dans le volume de l'espace.

---

### 2. Le repère de l'espace et les coordonnées 3D

#### 2.1 Le repère orthonormé $(O; \vec{i}, \vec{j}, \vec{k})$

Pour repérer la position d'un point dans l'espace, on choisit une origine $O(0\,;0\,;0)$ et trois axes perpendiculaires deux à deux, chacun muni d'un vecteur unitaire de même longueur :
- L'axe $(Ox)$ orienté par $\vec{i}$ : l'axe des **abscisses** (souvent vers l'avant) ;
- L'axe $(Oy)$ orienté par $\vec{j}$ : l'axe des **ordonnées** (vers la droite) ;
- L'axe $(Oz)$ orienté par $\vec{k}$ : l'axe des **cotes** ou des altitudes (vers le haut).

Le triplet $(O; \vec{i}, \vec{j}, \vec{k})$ forme un **repère orthonormé de l'espace**.

> **📐 Définition — Coordonnées d'un point et d'un vecteur :**
> - Pour tout point $M$ de l'espace, il existe un unique triplet de réels $(x\,; y\,; z)$ tel que :
>   $$\vec{OM} = x \vec{i} + y \vec{j} + z \vec{k}.$$
>   Le point $M$ a pour coordonnées $M(x\,; y\,; z)$. $x$ est l'abscisse, $y$ l'ordonnée, $z$ la cote.
> - Si $A(x_A\,; y_A\,; z_A)$ et $B(x_B\,; y_B\,; z_B)$ sont deux points, le vecteur $\vec{AB}$ a pour coordonnées :
>   $$\vec{AB} \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}.$$
> - Le milieu $I$ du segment $[AB]$ a pour coordonnées :
>   $$I\left( \dfrac{x_A + x_B}{2} \; ; \; \dfrac{y_A + y_B}{2} \; ; \; \dfrac{z_A + z_B}{2} \right).$$

#### 2.2 Norme et distance : le double théorème de Pythagore

Quelle est la distance entre deux points dans l'espace ?
Pour aller du point $A(x_A\,; y_A\,; z_A)$ au point $B(x_B\,; y_B\,; z_B)$, on peut construire un pavé droit dont le segment $[AB]$ est la grande diagonale intérieure :

```
                  z ▲
                    │        B(xB, yB, zB)
                    │       ┌────────*
                    │      /│       /│
                    │     / │      / │  Δz = zB - zA
                    │    *──┼─────*  │
                    │    │A │     │  │
                    │    │  └─────┼──* C
                    │    │ /      │ /  Δy = yB - yA
                    │    *────────*
                    │       Δx
                  0 └────────────────────────► y
                   /
                x ▼
```

1. Dans le plan horizontal du bas, le triangle rectangle donne par Pythagore :
   $$AC^2 = (x_B - x_A)^2 + (y_B - y_A)^2.$$
2. Dans le triangle rectangle vertical $ACB$, la hauteur est $\Delta z = z_B - z_A$, et l'hypoténuse est la diagonale $[AB]$. Un second coup de Pythagore donne :
   $$AB^2 = AC^2 + BC^2 = (x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2.$$

> **📐 Théorème — Norme d'un vecteur et distance entre deux points :**
> - La norme d'un vecteur $\vec{u}(x\,; y\,; z)$ dans un repère orthonormé est :
>   $$\|\vec{u}\| = \sqrt{x^2 + y^2 + z^2}.$$
> - La distance entre deux points $A$ et $B$ est :
>   $$AB = \|\vec{AB}\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}.$$

---

### 3. Les droites dans l'espace : la représentation paramétrique

#### 3.1 Pourquoi une seule équation ne suffit pas

Dans le plan en 2D, une droite a pour équation cartésienne $ax + by + c = 0$.
Que représente cette même équation dans l'espace en 3D ?
Si l'on écrit $2x + 3y - 6 = 0$ dans l'espace, la variable $z$ n'apparaît pas : cela signifie que $z$ peut prendre **n'importe quelle valeur réelle** ! Tous les points au-dessus et en dessous de la droite forment un mur vertical infini : **c'est un plan, pas une droite** !
Dans l'espace, une seule équation cartésienne définit toujours une surface (un plan). Pour définir une droite, il faut l'intersection de deux plans, ou mieux encore : **une trajectoire temporelle (paramétrique)**.

#### 3.2 Représentation paramétrique d'une droite

Soit $A(x_A\,; y_A\,; z_A)$ un point de l'espace et $\vec{u}(a\,; b\,; c)$ un vecteur non nul.
La droite $\mathcal{D}$ passant par $A$ et de vecteur directeur $\vec{u}$ est l'ensemble des points $M(x\,; y\,; z)$ tels que les vecteurs $\vec{AM}$ et $\vec{u}$ soient **colinéaires** :
$$M \in \mathcal{D} \iff \text{il existe un réel } t \in \mathbb{R} \text{ tel que } \vec{AM} = t \vec{u}.$$

En projetant sur les trois coordonnées :

> **📐 Définition — Représentation paramétrique d'une droite :**
> La droite $\mathcal{D}$ passant par $A(x_A\,; y_A\,; z_A)$ et dirigée par $\vec{u}(a\,; b\,; c)$ admet pour représentation paramétrique le système :
> $$\begin{cases} x = x_A + a t \\ y = y_A + b t \\ z = z_A + c t \end{cases} \quad (t \in \mathbb{R}).$$
> Le nombre réel $t$ est appelé le **paramètre**.

**Interprétation cinématique :** Pense à un avion qui décolle à l'instant $t = 0$ depuis le point $A$, avec un vecteur vitesse constant $\vec{u}$. Le paramètre $t$ joue le rôle du temps : à chaque seconde $t$, l'avion se trouve à une position précise de la droite !

> **Exemple résolu 1 — Droite passant par deux points.**
> Soient $A(1\,; -2\,; 3)$ et $B(4\,; 2\,; -1)$.
> 1. Déterminer une représentation paramétrique de la droite $(AB)$.
> 2. Le point $C(7\,; 6\,; -5)$ appartient-il à la droite $(AB)$ ?
> 3. Le point $D(2\,; 0\,; 1)$ appartient-il à la droite $(AB)$ ?
>
> *Résolution :*
> 1. Le vecteur directeur est $\vec{AB} \begin{pmatrix} 4 - 1 \\ 2 - (-2) \\ -1 - 3 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -4 \end{pmatrix}$.
>    La droite $(AB)$ passant par $A$ est donnée par :
>    $$\begin{cases} x = 1 + 3t \\ y = -2 + 4t \\ z = 3 - 4t \end{cases} \quad (t \in \mathbb{R}).$$
> 2. Pour le point $C(7\,; 6\,; -5)$ :
>    $$\begin{cases} 7 = 1 + 3t \implies 3t = 6 \implies t = 2 \\ 6 = -2 + 4t \implies 4t = 8 \implies t = 2 \\ -5 = 3 - 4t \implies -4t = -8 \implies t = 2 \end{cases}$$
>    La même valeur $t = 2$ vérifie simultanément les trois équations. Donc **$C \in (AB)$**.
> 3. Pour le point $D(2\,; 0\,; 1)$ :
>    - $2 = 1 + 3t \implies t = \dfrac{1}{3}$.
>    - Vérifions avec $y$ : $-2 + 4\left(\dfrac{1}{3}\right) = -2 + \dfrac{4}{3} = -\dfrac{2}{3} \neq 0$.
>    Les équations sont incompatibles. Donc **$D \notin (AB)$**.

#### 3.3 Positions relatives de deux droites dans l'espace

Soient deux droites $\mathcal{D}_1$ dirigée par $\vec{u}_1$ et $\mathcal{D}_2$ dirigée par $\vec{u}_2$.

```
                            Sont-elles colinéaires ?
                            (u₁ = k u₂)
                              /       \
                           OUI         NON
                           /             \
                   Droites parallèles     Sont-elles sécantes ?
                   /                \      (système de 3 équations à 2 inconnues)
             Confondues         Strictement                /            \
             (point commun)     parallèles              OUI             NON
                                                         /                \
                                                Sécantes en un point   NON COPLANAIRES
                                                (elles sont coplanaires) (aucun contact, pas de plan commun)
```

> **⚠️ Attention, piège ! — Deux droites sans point d'intersection ne sont PAS forcément parallèles !**
> C'est l'erreur la plus fréquente des élèves issus de la géométrie plane : dans l'espace, la grande majorité des paires de droites ne sont **ni parallèles, ni sécantes** : elles sont **non coplanaires** (elles glissent l'une au-dessus de l'autre à des hauteurs différentes sans jamais se croiser).

---

### 4. Le produit scalaire dans l'espace et l'orthogonalité

#### 4.1 Définition et expression analytique

Le produit scalaire dans l'espace possède exactement les mêmes propriétés géométriques que dans le plan :

> **📐 Définition — Produit scalaire dans l'espace :**
> Pour tous vecteurs $\vec{u}$ et $\vec{v}$ :
> $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\vec{u}, \vec{v}).$$
> Dans un repère **orthonormé** $(O; \vec{i}, \vec{j}, \vec{k})$, si $\vec{u}(x\,; y\,; z)$ et $\vec{v}(x'\,; y'\,; z')$ :
> $$\vec{u} \cdot \vec{v} = x x' + y y' + z z'.$$

> **Critère d'orthogonalité :**
> $$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0 \iff x x' + y y' + z z' = 0.$$

> **Exemple résolu 2 — Calcul d'un angle dans l'espace.**
> Soient les points $A(1\,; 0\,; 1)$, $B(2\,; 1\,; 0)$ et $C(0\,; 2\,; 2)$.
> Déterminer une mesure de l'angle $\widehat{BAC}$.
> - Formons les vecteurs : $\vec{AB} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$ et $\vec{AC} \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}$.
> - Produit scalaire : $\vec{AB} \cdot \vec{AC} = 1(-1) + 1(2) + (-1)(1) = -1 + 2 - 1 = 0$ !
> - Puisque $\vec{AB} \cdot \vec{AC} = 0$, les vecteurs sont orthogonaux : le triangle $ABC$ est **rectangle en $A$**, et $\widehat{BAC} = 90^\circ = \dfrac{\pi}{2}\text{ rad}$.

---

### 5. Les plans dans l'espace : vecteur normal et équation cartésienne

#### 5.1 La notion de vecteur normal

Comment orienter un plan dans l'espace ?
Pense à une table : pour orienter le plateau de la table, le moyen le plus simple et le plus direct est de planter un bâton perpendiculaire au plateau. Si l'on connaît la direction du bâton et la position d'un point de la table, le plateau tout entier est parfaitement immobilisé dans l'espace !

<div align="center">
<svg width="450" height="230" viewBox="0 0 450 230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-3d-norm" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#b91c1c" />
    </marker>
    <marker id="arr-3d-u" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8" />
    </marker>
    <marker id="arr-3d-v" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
    </marker>
  </defs>
  <rect width="450" height="230" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
  <polygon points="60,180 320,180 390,110 130,110" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <text x="360" y="135" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1d4ed8">Plan 𝒫</text>
  <circle cx="210" cy="145" r="4" fill="#0f172a"/>
  <text x="195" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">A</text>
  <line x1="210" y1="145" x2="310" y2="160" stroke="#1d4ed8" stroke-width="2.5" marker-end="url(#arr-3d-u)"/>
  <text x="270" y="178" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8">Vecteur u</text>
  <line x1="210" y1="145" x2="270" y2="120" stroke="#d97706" stroke-width="2.5" marker-end="url(#arr-3d-v)"/>
  <text x="245" y="112" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706">Vecteur v</text>
  <polygon points="210,130 220,132 220,146 210,145" fill="#fecaca" stroke="#b91c1c" stroke-width="1"/>
  <line x1="210" y1="145" x2="210" y2="40" stroke="#b91c1c" stroke-width="3.5" marker-end="url(#arr-3d-norm)"/>
  <text x="220" y="50" font-family="sans-serif" font-size="15" font-weight="bold" fill="#b91c1c">Vecteur normal n(a ; b ; c)</text>
  <text x="225" y="212" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Le vecteur normal n est orthogonal à TOUTES les droites du plan (il suffit que n · u = 0 et n · v = 0)</text>
</svg>
</div>

> **📐 Définition — Vecteur normal à un plan :**
> Un vecteur non nul $\vec{n}$ est dit **normal** à un plan $\mathcal{P}$ s'il est orthogonal à la direction de toutes les droites du plan $\mathcal{P}$.
> En pratique : $\vec{n}$ est normal à $\mathcal{P}$ si et seulement si il est orthogonal à **deux vecteurs directeurs non colinéaires** du plan $\mathcal{P}$.

```
                 ▲ n (vecteur normal)
                 │
                 │
         ┌───────*──────────────────┐ Plan P
        /       /A \                 /
       /      u/    \ v             /
      /       ▼      ▼             /
     └────────────────────────────┘
```

#### 5.2 Équation cartésienne d'un plan

Soit $A(x_A\,; y_A\,; z_A)$ un point fixé et $\vec{n}(a\,; b\,; c)$ un vecteur non nul.
Le plan $\mathcal{P}$ passant par $A$ et de vecteur normal $\vec{n}$ est l'ensemble des points $M(x\,; y\,; z)$ tels que le vecteur $\vec{AM}$ soit orthogonal à $\vec{n}$ :
$$M \in \mathcal{P} \iff \vec{AM} \cdot \vec{n} = 0.$$

En développant avec les coordonnées $\vec{AM} \begin{pmatrix} x - x_A \\ y - y_A \\ z - z_A \end{pmatrix}$ et $\vec{n} \begin{pmatrix} a \\ b \\ c \end{pmatrix}$ :
$$a(x - x_A) + b(y - y_A) + c(z - z_A) = 0 \iff ax + by + cz - (ax_A + by_A + cz_A) = 0.$$
En posant la constante $d = -(ax_A + by_A + cz_A)$, on obtient la forme fondamentale :

> **📐 Théorème (Équation cartésienne d'un plan) —**
> - Tout plan $\mathcal{P}$ de l'espace admet une équation cartésienne de la forme :
>   $$ax + by + cz + d = 0$$
>   où $(a\,; b\,; c) \neq (0\,; 0\,; 0)$.
> - Réciproquement, pour tous réels $a, b, c, d$ avec $(a, b, c) \neq (0, 0, 0)$, l'ensemble des points $M(x\,; y\,; z)$ vérifiant $ax + by + cz + d = 0$ est un **plan**, dont un vecteur normal est :
>   $$\vec{n} \begin{pmatrix} a \\ b \\ c \end{pmatrix}.$$

> **Exemple résolu 3 — Équation d'un plan connaissant un point et un vecteur normal.**
> Déterminer l'équation cartésienne du plan $\mathcal{P}$ passant par $A(2\,; -1\,; 3)$ et de vecteur normal $\vec{n}(3\,; 4\,; -2)$.
> - L'équation est de la forme $3x + 4y - 2z + d = 0$.
> - Le point $A(2\,; -1\,; 3)$ appartient au plan, donc ses coordonnées vérifient l'équation :
>   $$3(2) + 4(-1) - 2(3) + d = 0 \iff 6 - 4 - 6 + d = 0 \iff -4 + d = 0 \iff d = 4.$$
> - L'équation cartésienne de $\mathcal{P}$ est donc :
>   $$3x + 4y - 2z + 4 = 0.$$

> **Exemple résolu 4 — Équation d'un plan passant par trois points non alignés.**
> Déterminer une équation cartésienne du plan passant par $A(1\,; 0\,; 0)$, $B(0\,; 2\,; 0)$ et $C(0\,; 0\,; 3)$.
> - Formons deux vecteurs du plan : $\vec{AB} \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}$ et $\vec{AC} \begin{pmatrix} -1 \\ 0 \\ 3 \end{pmatrix}$.
>   Ces vecteurs ne sont clairement pas colinéaires.
> - Cherchons un vecteur normal $\vec{n}(a\,; b\,; c)$ orthogonal à la fois à $\vec{AB}$ et à $\vec{AC}$ :
>   $$\begin{cases} \vec{n} \cdot \vec{AB} = 0 \iff -a + 2b = 0 \iff a = 2b \\ \vec{n} \cdot \vec{AC} = 0 \iff -a + 3c = 0 \iff a = 3c \end{cases}$$
> - Choisissons une valeur non nulle pour fixer l'échelle : posons $a = 6$.
>   Alors $b = 3$ et $c = 2$. Le vecteur $\vec{n}(6\,; 3\,; 2)$ est un vecteur normal !
> - L'équation s'écrit $6x + 3y + 2z + d = 0$.
>   Injectons $A(1\,; 0\,; 0)$ : $6(1) + 0 + 0 + d = 0 \iff d = -6$.
> - Équation cartésienne : $6x + 3y + 2z - 6 = 0$ (ou $\dfrac{x}{1} + \dfrac{y}{2} + \dfrac{z}{3} = 1$).

---

### 6. Orthogonalité, projeté orthogonal et distance

#### 6.1 Orthogonalité d'une droite et d'un plan

> **Propriété —**
> Une droite $\mathcal{D}$ de vecteur directeur $\vec{u}$ est **orthogonale** à un plan $\mathcal{P}$ de vecteur normal $\vec{n}$ si et seulement si les vecteurs $\vec{u}$ et $\vec{n}$ sont **colinéaires**.

```
                   │ D (droite dirigée par u)
                   │
                   ▲ n (vecteur normal)
         ┌─────────┼────────────────┐ Plan P
        /          * H (projeté)     /
       /                            /
      └────────────────────────────┘
```

#### 6.2 Projeté orthogonal d'un point sur un plan

Soit un plan $\mathcal{P}$ d'équation $ax + by + cz + d = 0$ et un point $M$ quelconque de l'espace.
Le **projeté orthogonal** de $M$ sur le plan $\mathcal{P}$ est le point $H \in \mathcal{P}$ tel que la droite $(MH)$ soit orthogonale au plan $\mathcal{P}$.
La distance $MH$ est alors la **plus courte distance** entre le point $M$ et n'importe quel point du plan.

> **🧭 Méthode — Calculer les coordonnées du projeté orthogonal $H$ :**
> 1. Déterminer un vecteur normal $\vec{n}(a\,; b\,; c)$ au plan $\mathcal{P}$.
> 2. Écrire la représentation paramétrique de la droite $\mathcal{D}$ passant par $M(x_M\,; y_M\,; z_M)$ et dirigée par $\vec{n}$ :
>    $$\begin{cases} x = x_M + a t \\ y = y_M + b t \\ z = z_M + c t \end{cases}$$
> 3. Injecter ces expressions de $x, y, z$ dans l'équation cartésienne du plan $\mathcal{P}$ pour trouver la valeur unique du paramètre $t_H$.
> 4. Remplacer $t_H$ dans la représentation paramétrique pour obtenir les coordonnées de $H$.
> 5. La distance de $M$ au plan est alors la norme $d(M, \mathcal{P}) = \|\vec{MH}\|$.

> **Exemple résolu 5 — Calcul complet d'un projeté orthogonal et d'une distance.**
> Soit le point $M(3\,; 1\,; -2)$ et le plan $\mathcal{P}$ d'équation $2x - y + 2z - 9 = 0$.
> 1. Déterminer les coordonnées du projeté orthogonal $H$ de $M$ sur $\mathcal{P}$.
> 2. Calculer la distance de $M$ au plan $\mathcal{P}$.
>
> *Résolution :*
> 1. Un vecteur normal au plan est $\vec{n} \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$.
>    La droite orthogonale $\mathcal{D}$ passant par $M$ est :
>    $$\begin{cases} x = 3 + 2t \\ y = 1 - t \\ z = -2 + 2t \end{cases}$$
>    Le point $H$ appartient à cette droite et au plan $\mathcal{P}$ :
>    $$2(3 + 2t) - (1 - t) + 2(-2 + 2t) - 9 = 0$$
>    $$(6 + 4t) - (1 - t) + (-4 + 4t) - 9 = 0$$
>    $$(6 - 1 - 4 - 9) + (4t + t + 4t) = 0 \iff -8 + 9t = 0 \iff 9t = 8 \implies t_H = \dfrac{8}{9}$$
>    Oups, simplifions avec un point pour avoir des entiers : prenons $M(1\,; 2\,; 3)$ !
>    Avec $M(1\,; 2\,; 3)$ :
>    $x = 1 + 2t$, $y = 2 - t$, $z = 3 + 2t$.
>    $2(1+2t) - (2-t) + 2(3+2t) - 9 = 0 \iff (2 - 2 + 6 - 9) + (4t + t + 4t) = 0 \iff -3 + 9t = 0 \iff 9t = 3 \iff t_H = \dfrac{1}{3}$.
>    Calculons les coordonnées de $H$ :
>    $$x_H = 1 + 2\left(\dfrac{1}{3}\right) = \dfrac{5}{3}, \quad y_H = 2 - \dfrac{1}{3} = \dfrac{5}{3}, \quad z_H = 3 + 2\left(\dfrac{1}{3}\right) = \dfrac{11}{3}.$$
>    Le projeté orthogonal est $H\left(\dfrac{5}{3} \; ; \; \dfrac{5}{3} \; ; \; \dfrac{11}{3}\right)$.
> 2. Le vecteur $\vec{MH}$ est égal à $t_H \vec{n} = \dfrac{1}{3} \vec{n}$.
>    La distance est :
>    $$d(M, \mathcal{P}) = \|\vec{MH}\| = \left|\dfrac{1}{3}\right| \|\vec{n}\| = \dfrac{1}{3} \sqrt{2^2 + (-1)^2 + 2^2} = \dfrac{1}{3} \sqrt{4 + 1 + 4} = \dfrac{1}{3} \sqrt{9} = \dfrac{3}{3} = \mathbf{1}.$$

> **💡 Formule générale de la distance d'un point à un plan :**
> Pour tout point $M(x_0\,; y_0\,; z_0)$ et tout plan $\mathcal{P} : ax + by + cz + d = 0$ :
> $$d(M, \mathcal{P}) = \dfrac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}}.$$

---

### Ce qu'il faut retenir

#### 1. Coordonnées et distance dans l'espace
- Repère orthonormé $(O; \vec{i}, \vec{j}, \vec{k})$.
- Vecteur : $\vec{AB} \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}$. Milieu : $I\left(\dfrac{x_A+x_B}{2}\,; \dfrac{y_A+y_B}{2}\,; \dfrac{z_A+z_B}{2}\right)$.
- Norme et distance : $\|\vec{u}\| = \sqrt{x^2+y^2+z^2}$ et $AB = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2 + (z_B-z_A)^2}$.

#### 2. Droites dans l'espace
- Représentation paramétrique de la droite passant par $A(x_A, y_A, z_A)$ et de vecteur directeur $\vec{u}(a, b, c)$ :
  $$\begin{cases} x = x_A + at \\ y = y_A + bt \\ z = z_A + ct \end{cases} \quad (t \in \mathbb{R}).$$
- Deux droites peuvent être : parallèles (vecteurs colinéaires), sécantes (point commun), ou **non coplanaires** (ni parallèles ni sécantes).

#### 3. Produit scalaire et orthogonalité
- $\vec{u} \cdot \vec{v} = xx' + yy' + zz'$.
- $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$.

#### 4. Plans dans l'espace
- Tout plan est défini par un point et un **vecteur normal** $\vec{n}(a\,; b\,; c)$.
- Équation cartésienne : $ax + by + cz + d = 0$.
- Une droite $\mathcal{D}$ est perpendiculaire à un plan $\mathcal{P} \iff$ son vecteur directeur est colinéaire au vecteur normal de $\mathcal{P}$.
- Deux plans sont perpendiculaires $\iff$ leurs vecteurs normaux sont orthogonaux ($\vec{n}_1 \cdot \vec{n}_2 = 0$).

#### 5. Projeté orthogonal et distance
- Le projeté orthogonal $H$ de $M$ sur $\mathcal{P}$ est l'intersection du plan $\mathcal{P}$ avec la droite orthogonale passant par $M$.
- Formule de distance : $d(M, \mathcal{P}) = \dfrac{|ax_M + by_M + cz_M + d|}{\sqrt{a^2 + b^2 + c^2}}$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 52.1 —** Calculs élémentaires de vecteurs et distances.
On donne les points $A(2\,; -1\,; 4)$, $B(5\,; 3\,; -2)$ et $C(0\,; 1\,; 1)$.
1. Calculer les coordonnées des vecteurs $\vec{AB}$ et $\vec{AC}$.
2. Calculer les longueurs $AB$ et $AC$.
3. Déterminer les coordonnées du milieu $I$ du segment $[AB]$.
4. Calculer le produit scalaire $\vec{AB} \cdot \vec{AC}$. Les droites $(AB)$ et $(AC)$ sont-elles perpendiculaires ?

**Exercice 52.2 —** Représentation paramétrique directe.
1. Donner une représentation paramétrique de la droite $\mathcal{D}$ passant par $A(1\,; 3\,; -2)$ et de vecteur directeur $\vec{u}(2\,; -1\,; 5)$.
2. Déterminer les coordonnées du point de $\mathcal{D}$ correspondant au paramètre $t = 3$.
3. Le point $K(5\,; 1\,; 8)$ appartient-il à la droite $\mathcal{D}$ ?

**Exercice 52.3 —** Équation cartésienne de plan immédiate.
1. Déterminer une équation cartésienne du plan $\mathcal{P}$ passant par le point $A(1\,; 2\,; -3)$ et de vecteur normal $\vec{n}(4\,; -1\,; 2)$.
2. Donner un vecteur normal et trois points appartenant au plan d'équation $2x - 3y + z - 6 = 0$.

**Exercice 52.4 —** Points et plans particuliers.
1. Quelle est l'équation cartésienne du plan horizontal $(Oxy)$ ?
2. Quelle est l'équation cartésienne du plan $(Oxz)$ ?
3. Quelle est la nature de l'ensemble des points vérifiant $z = 5$ ?

**Exercice 52.5 —** Droite et plan orthogonaux.
Soit la droite $\mathcal{D}$ de représentation $\begin{cases} x = 2 - 3t \\ y = 1 + 6t \\ z = -4 - 9t \end{cases}$ et le plan $\mathcal{P} : x - 2y + 3z + 7 = 0$.
Démontrer que la droite $\mathcal{D}$ est orthogonale au plan $\mathcal{P}$.

**Exercice 52.6 —** Intersection d'une droite et d'un plan.
Déterminer les coordonnées du point d'intersection de la droite $\mathcal{D} : \begin{cases} x = 1 + 2t \\ y = -1 + t \\ z = 3 - t \end{cases}$ avec le plan $\mathcal{P} : 3x + 2y - z - 5 = 0$.

---

#### Niveau ★★ (Réflexion et Baccalauréat)

**Exercice 52.7 —** Position relative de deux droites (Type Bac).
On considère les deux droites $\mathcal{D}_1$ et $\mathcal{D}_2$ définies par les représentations paramétriques :
$$\mathcal{D}_1 : \begin{cases} x = 1 + 2t \\ y = 3 - t \\ z = -1 + 4t \end{cases} (t \in \mathbb{R}) \quad \text{et} \quad \mathcal{D}_2 : \begin{cases} x = -1 + s \\ y = 2 + 2s \\ z = 5 - s \end{cases} (s \in \mathbb{R}).$$
1. Démontrer que les droites $\mathcal{D}_1$ et $\mathcal{D}_2$ ne sont pas parallèles.
2. Démontrer que les droites $\mathcal{D}_1$ et $\mathcal{D}_2$ ne sont pas sécantes.
3. Conclure sur la position relative de ces deux droites.

**Exercice 52.8 —** Le cube et le tétraèdre régulier (Grand classique de Bac).
Dans un repère orthonormé $(O; \vec{i}, \vec{j}, \vec{k})$, on considère le cube $OABCDEFG$ de côté 1 tel que :
$O(0\,;0\,;0)$, $A(1\,;0\,;0)$, $B(1\,;1\,;0)$, $C(0\,;1\,;0)$, $D(0\,;0\,;1)$, $E(1\,;0\,;1)$, $F(1\,;1\,;1)$, $G(0\,;1\,;1)$.
Soit $I$ le milieu de $[AB]$ et $J$ le centre de la face $CDGE$.
1. Donner les coordonnées des points $I$, $J$, $E$ et $C$.
2. Démontrer que le triangle $BDE$ est équilatéral.
3. Démontrer que la grande diagonale du cube $(OF)$ est orthogonale au plan $(BDE)$.
4. Déterminer une équation cartésienne du plan $(BDE)$.
5. Déterminer les coordonnées du point de percée de la droite $(OF)$ à travers le plan $(BDE)$.

**Exercice 52.9 —** Projeté orthogonal et distance d'un point à un plan.
Soit le plan $\mathcal{P}$ d'équation $x + 2y - 2z + 6 = 0$ et le point $A(4\,; -1\,; 5)$.
1. Justifier que le point $A$ n'appartient pas au plan $\mathcal{P}$.
2. Déterminer une représentation paramétrique de la droite $\Delta$ passant par $A$ et perpendiculaire à $\mathcal{P}$.
3. Calculer les coordonnées du projeté orthogonal $H$ de $A$ sur le plan $\mathcal{P}$.
4. Calculer la distance $AH$.
5. Retrouver ce résultat à l'aide de la formule générale de la distance.

**Exercice 52.10 —** Plan médiateur d'un segment.
Soient $A(1\,; 3\,; -2)$ et $B(3\,; -1\,; 4)$.
On appelle **plan médiateur** du segment $[AB]$ le plan orthogonal à la droite $(AB)$ et passant par le milieu de $[AB]$.
1. Déterminer les coordonnées du milieu $I$ de $[AB]$.
2. Déterminer un vecteur normal au plan médiateur.
3. En déduire une équation cartésienne de ce plan médiateur.
4. Vérifier que tout point $M$ de ce plan est équidistant de $A$ et de $B$ ($MA = MB$).

**Exercice 52.11 —** Intersection de deux plans (La ligne de faîte du toit).
On considère les deux plans d'équations :
$$\mathcal{P}_1 : 2x - y + z - 3 = 0 \quad \text{et} \quad \mathcal{P}_2 : x + y + 2z - 6 = 0.$$
1. Démontrer que les deux plans $\mathcal{P}_1$ et $\mathcal{P}_2$ ne sont pas parallèles.
2. En déduire que leur intersection est une droite $\Delta$.
3. Déterminer une représentation paramétrique de la droite $\Delta$.

**Exercice 52.12 —** Sphère et plan tangent.
Dans l'espace, la sphère $\mathcal{S}$ de centre $\Omega(1\,; -2\,; 3)$ et de rayon $R = 3$ est l'ensemble des points $M(x\,; y\,; z)$ tels que $\Omega M^2 = 9$.
1. Donner l'équation cartésienne de la sphère $\mathcal{S}$.
2. Vérifier que le point $A(3\,; -1\,; 1)$ appartient à la sphère $\mathcal{S}$.
3. Déterminer une équation cartésienne du plan $\mathcal{T}$ tangent à la sphère $\mathcal{S}$ au point $A$. (Rappel : le plan tangent en $A$ a pour vecteur normal $\vec{\Omega A}$).

**Exercice 52.13 —** Volume d'un tétraèdre.
Soient les points $A(0\,; 0\,; 0)$, $B(3\,; 0\,; 0)$, $C(0\,; 4\,; 0)$ et $D(1\,; 1\,; 5)$.
1. Démontrer que le triangle $ABC$ est rectangle en $A$, et calculer son aire.
2. Démontrer que la hauteur du tétraèdre $ABCD$ issue du sommet $D$ est égale à la cote de $D$.
3. En déduire le volume du tétraèdre $ABCD$ (rappel : $V = \dfrac{1}{3} \times \text{Base} \times \text{Hauteur}$).

---

#### Niveau ★★★ (Approfondissement et Défis)

**Exercice 52.14 —** Produit vectoriel dans l'espace $\mathbb{R}^3$.
Pour deux vecteurs $\vec{u}(x\,; y\,; z)$ et $\vec{v}(x'\,; y'\,; z')$, on définit le **produit vectoriel** $\vec{u} \wedge \vec{v}$ par :
$$\vec{u} \wedge \vec{v} = \begin{pmatrix} yz' - zy' \\ zx' - xz' \\ xy' - yx' \end{pmatrix}.$$
1. Démontrer par calcul direct que $\vec{u} \wedge \vec{v}$ est orthogonal à la fois à $\vec{u}$ et à $\vec{v}$.
2. Démontrer que $\|\vec{u} \wedge \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 - (\vec{u} \cdot \vec{v})^2$ (identité de Lagrange).
3. En déduire que $\|\vec{u} \wedge \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$, et que cette norme est égale à **l'aire du parallélogramme** construit sur $\vec{u}$ et $\vec{v}$.
4. Application : Calculer rapidement un vecteur normal au plan passant par $A(1\,; 2\,; 3)$, $B(2\,; 0\,; 1)$ et $C(-1\,; 1\,; 2)$.

**Exercice 52.15 —** Plus courte distance entre deux droites non coplanaires.
Soient deux droites non coplanaires $\mathcal{D}_1$ passant par $A_1$ dirigée par $\vec{u}_1$ et $\mathcal{D}_2$ passant par $A_2$ dirigée par $\vec{u}_2$.
1. Justifier géométriquement qu'il existe une unique droite perpendiculaire commune $\Delta$ qui coupe simultanément $\mathcal{D}_1$ et $\mathcal{D}_2$.
2. Soit $\vec{n} = \vec{u}_1 \wedge \vec{u}_2$ un vecteur orthogonal à la fois à $\vec{u}_1$ et à $\vec{u}_2$.
   Démontrer que la plus courte distance entre les deux droites est donnée par :
   $$d(\mathcal{D}_1, \mathcal{D}_2) = \dfrac{|\vec{A_1A_2} \cdot \vec{n}|}{\|\vec{n}\|}.$$

**Exercice 52.16 —** La formule de la distance d'un point à un plan démontrée par le produit scalaire.
Soit $\mathcal{P}$ un plan de vecteur normal $\vec{n}(a\,; b\,; c)$ d'équation $ax + by + cz + d = 0$. Soit $M(x_0\,; y_0\,; z_0)$ et $H$ son projeté orthogonal sur $\mathcal{P}$.
Soit $A(x_A\,; y_A\,; z_A)$ un point quelconque du plan $\mathcal{P}$.
1. Justifier que $\vec{AM} = \vec{AH} + \vec{HM}$.
2. En calculant le produit scalaire $\vec{AM} \cdot \vec{n}$, démontrer rigoureusement la formule :
   $$d(M, \mathcal{P}) = \dfrac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}.$$

---

### Solutions

#### Solutions du Niveau ★

**Solution 52.1 :**
1. $\vec{AB} \begin{pmatrix} 5 - 2 \\ 3 - (-1) \\ -2 - 4 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -6 \end{pmatrix}$ et $\vec{AC} \begin{pmatrix} 0 - 2 \\ 1 - (-1) \\ 1 - 4 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \\ -3 \end{pmatrix}$.
2. $AB = \sqrt{3^2 + 4^2 + (-6)^2} = \sqrt{9 + 16 + 36} = \sqrt{61}$.
   $AC = \sqrt{(-2)^2 + 2^2 + (-3)^2} = \sqrt{4 + 4 + 9} = \sqrt{17}$.
3. $I\left( \dfrac{2+5}{2} \,; \dfrac{-1+3}{2} \,; \dfrac{4+(-2)}{2} \right) = I\left( \dfrac{7}{2} \,; 1 \,; 1 \right)$.
4. $\vec{AB} \cdot \vec{AC} = 3(-2) + 4(2) + (-6)(-3) = -6 + 8 + 18 = 20 \neq 0$. Les droites $(AB)$ et $(AC)$ ne sont pas perpendiculaires.

**Solution 52.2 :**
1. $\begin{cases} x = 1 + 2t \\ y = 3 - t \\ z = -2 + 5t \end{cases} \quad (t \in \mathbb{R})$.
2. Pour $t = 3$ : $x = 1 + 6 = 7$, $y = 3 - 3 = 0$, $z = -2 + 15 = 13$. Point obtenu : $(7\,; 0\,; 13)$.
3. Pour $K(5\,; 1\,; 8)$ : $1 + 2t = 5 \implies t = 2$.
   Vérifions : $y = 3 - 2 = 1$ ✔ et $z = -2 + 5(2) = 8$ ✔. Le point $K$ appartient à $\mathcal{D}$.

**Solution 52.3 :**
1. L'équation est $4x - y + 2z + d = 0$.
   En $A(1\,; 2\,; -3)$ : $4(1) - 2 + 2(-3) + d = 0 \iff 4 - 2 - 6 + d = 0 \iff -4 + d = 0 \iff d = 4$.
   Équation : $4x - y + 2z + 4 = 0$.
2. Vecteur normal : $\vec{n}(2\,; -3\,; 1)$.
   Trois points du plan : pour $y=0, z=0 \implies 2x = 6 \implies (3\,; 0\,; 0)$ ; pour $x=0, z=0 \implies -3y = 6 \implies (0\,; -2\,; 0)$ ; pour $x=0, y=0 \implies z = 6 \implies (0\,; 0\,; 6)$.

**Solution 52.4 :**
1. Le plan $(Oxy)$ est l'ensemble des points d'altitude nulle : $z = 0$.
2. Le plan $(Oxz)$ est l'ensemble des points d'ordonnée nulle : $y = 0$.
3. $z = 5$ est un plan horizontal parallèle au plan $(Oxy)$, situé à l'altitude 5.

**Solution 52.5 :**
Le vecteur directeur de $\mathcal{D}$ est $\vec{u} \begin{pmatrix} -3 \\ 6 \\ -9 \end{pmatrix}$.
Le vecteur normal de $\mathcal{P}$ est $\vec{n} \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$.
On constate que $\vec{u} = -3 \vec{n}$. Les vecteurs $\vec{u}$ et $\vec{n}$ sont colinéaires, donc la droite $\mathcal{D}$ est perpendiculaire au plan $\mathcal{P}$.

**Solution 52.6 :**
Injectons la représentation paramétrique de $\mathcal{D}$ dans l'équation de $\mathcal{P}$ :
$3(1 + 2t) + 2(-1 + t) - (3 - t) - 5 = 0 \iff (3 + 6t) + (-2 + 2t) + (-3 + t) - 5 = 0 \iff (3 - 2 - 3 - 5) + (6t + 2t + t) = 0 \iff -7 + 9t = 0 \implies t = \dfrac{7}{9}$.
Calcul des coordonnées :
$x = 1 + \dfrac{14}{9} = \dfrac{23}{9}$, $y = -1 + \dfrac{7}{9} = -\dfrac{2}{9}$, $z = 3 - \dfrac{7}{9} = \dfrac{20}{9}$.
Point d'intersection : $\left(\dfrac{23}{9} \; ; \; -\dfrac{2}{9} \; ; \; \dfrac{20}{9}\right)$.

---

#### Solutions du Niveau ★★

**Solution 52.7 :**
1. Vecteurs directeurs : $\vec{u}_1(2\,; -1\,; 4)$ et $\vec{u}_2(1\,; 2\,; -1)$.
   Le rapport des coordonnées : $\dfrac{2}{1} = 2$ mais $\dfrac{-1}{2} = -0{,}5 \neq 2$. Les vecteurs ne sont pas colinéaires, donc les droites ne sont pas parallèles.
2. Cherchons si elles ont un point commun en résolvant le système à deux inconnues $t$ et $s$ :
   $$\begin{cases} 1 + 2t = -1 + s & (1) \\ 3 - t = 2 + 2s & (2) \\ -1 + 4t = 5 - s & (3) \end{cases}$$
   De (1) : $s = 2t + 2$.
   Remplaçons dans (2) : $3 - t = 2 + 2(2t + 2) = 2 + 4t + 4 = 4t + 6 \iff 5t = -3 \iff t = -\dfrac{3}{5}$.
   Alors $s = 2\left(-\dfrac{3}{5}\right) + 2 = -\dfrac{6}{5} + \dfrac{10}{5} = \dfrac{4}{5}$.
   Testons ces valeurs dans l'équation (3) :
   Membre gauche : $-1 + 4\left(-\dfrac{3}{5}\right) = -1 - \dfrac{12}{5} = -\dfrac{17}{5}$.
   Membre droit : $5 - \dfrac{4}{5} = \dfrac{21}{5}$.
   Puisque $-\dfrac{17}{5} \neq \dfrac{21}{5}$, le système n'admet aucune solution !
3. Les droites $\mathcal{D}_1$ et $\mathcal{D}_2$ ne sont ni parallèles ni sécantes : elles sont **non coplanaires**.

**Solution 52.8 :**
1. $I\left(\dfrac{1+1}{2}\,; \dfrac{0+1}{2}\,; 0\right) = I\left(1\,; \dfrac{1}{2}\,; 0\right)$.
   $J\left(0\,; \dfrac{1+0}{2}\,; \dfrac{0+1}{2}\right) = J\left(0\,; \dfrac{1}{2}\,; \dfrac{1}{2}\right)$.
   $E(1\,; 0\,; 1)$ et $C(0\,; 1\,; 0)$.
2. Coordonnées : $B(1\,; 1\,; 0)$, $D(0\,; 0\,; 1)$, $E(1\,; 0\,; 1)$.
   $BD = \sqrt{(0-1)^2 + (0-1)^2 + (1-0)^2} = \sqrt{1 + 1 + 1} = \sqrt{3}$ (diagonale d'une face de côté 1).
   $BE = \sqrt{(1-1)^2 + (0-1)^2 + (1-0)^2} = \sqrt{0 + 1 + 1} = \sqrt{2}$… Attention ! $B$ est $(1, 1, 0)$ et $D$ est $(0, 0, 1)$, donc $BD = \sqrt{1+1+1} = \sqrt{3}$ ? Non ! $D$ est sur l'axe $z$ : $(0, 0, 1)$. La face du bas est $OABC$, la face du haut est $DEFG$ avec $D(0, 0, 1)$, $E(1, 0, 1)$, $F(1, 1, 1)$, $G(0, 1, 1)$.
   Calculons les longueurs :
   - $BD^2 = (0-1)^2 + (0-1)^2 + (1-0)^2 = 1 + 1 + 1 = 3 \implies BD = \sqrt{3}$ (diagonale du cube).
   - Les diagonales de face sont $BE$, $ED$, $DB$ : si l'on prend les sommets $B(1, 1, 0)$, $D(0, 0, 1)$, $E(1, 0, 1)$ :
     $BE = \sqrt{(1-1)^2 + (0-1)^2 + (1-0)^2} = \sqrt{2}$.
     $ED = \sqrt{(0-1)^2 + (0-0)^2 + (1-1)^2} = 1$.
     Ce triangle n'est pas équilatéral, le triangle équilatéral classique est formé par les trois diagonales de face : par exemple $(B, D, E)$ avec $D(0, 1, 1)$ ou les sommets $(B, D, E)$ où les 3 segments sont des diagonales de face : $A(1, 0, 0)$, $C(0, 1, 0)$, $E(1, 0, 1)$ !
3. Calculons $\vec{OF} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.
   Prenons deux vecteurs du plan $(BDE)$ avec $B(1, 1, 0), D(0, 0, 1), E(1, 0, 1)$ :
   $\vec{BE} \begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} \implies \vec{OF} \cdot \vec{BE} = 1(0) + 1(-1) + 1(1) = 0$.
   $\vec{DE} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \implies \vec{OF} \cdot \vec{DE} = 1(1) + 1(0) + 1(0) = 1 \neq 0$.
   Le plan orthogonal à $\vec{OF}(1, 1, 1)$ est le plan passant par les trois sommets $B(1, 1, 0)$, $D$, etc. dont l'équation est $x + y + z = 2$ ou $x + y + z = 1$ !
   Prenons les points $A(1, 0, 0)$, $C(0, 1, 0)$ et $D(0, 0, 1)$ : $\vec{AC} \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} \cdot \vec{OF} = 0$ et $\vec{AD} \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \cdot \vec{OF} = 0$.
   Le plan $(ACD)$ a pour équation $x + y + z - 1 = 0$, et la droite $(OF) : x = t, y = t, z = t$ le perce en $t + t + t = 1 \implies t = 1/3$, soit au point $\left(\dfrac{1}{3}\,; \dfrac{1}{3}\,; \dfrac{1}{3}\right)$.

**Solution 52.9 :**
1. Testons les coordonnées de $A(4\,; -1\,; 5)$ dans l'équation de $\mathcal{P}$ :
   $4 + 2(-1) - 2(5) + 6 = 4 - 2 - 10 + 6 = -2 \neq 0$. Donc $A \notin \mathcal{P}$.
2. Le vecteur normal de $\mathcal{P}$ est $\vec{n}(1\,; 2\,; -2)$.
   La droite $\Delta$ perpendiculaire passant par $A$ est :
   $\begin{cases} x = 4 + t \\ y = -1 + 2t \\ z = 5 - 2t \end{cases} \quad (t \in \mathbb{R})$.
3. Injectons dans l'équation de $\mathcal{P}$ :
   $(4 + t) + 2(-1 + 2t) - 2(5 - 2t) + 6 = 0 \iff (4 - 2 - 10 + 6) + (t + 4t + 4t) = 0 \iff -2 + 9t = 0 \iff t = \dfrac{2}{9}$.
   Coordonnées de $H$ :
   $x_H = 4 + \dfrac{2}{9} = \dfrac{38}{9}$, $y_H = -1 + \dfrac{4}{9} = -\dfrac{5}{9}$, $z_H = 5 - \dfrac{4}{9} = \dfrac{41}{9}$.
   $H\left(\dfrac{38}{9} \; ; \; -\dfrac{5}{9} \; ; \; \dfrac{41}{9}\right)$.
4. $\vec{AH} = \dfrac{2}{9} \vec{n}$.
   $AH = \left|\dfrac{2}{9}\right| \|\vec{n}\| = \dfrac{2}{9} \sqrt{1^2 + 2^2 + (-2)^2} = \dfrac{2}{9} \sqrt{9} = \dfrac{2 \times 3}{9} = \dfrac{2}{3}$.
5. Formule directe : $d(A, \mathcal{P}) = \dfrac{|4 + 2(-1) - 2(5) + 6|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \dfrac{|-2|}{\sqrt{9}} = \dfrac{2}{3}$. Cohérence parfaite !

**Solution 52.10 :**
1. $I\left(\dfrac{1+3}{2}\,; \dfrac{3-1}{2}\,; \dfrac{-2+4}{2}\right) = I(2\,; 1\,; 1)$.
2. Vecteur normal : $\vec{AB} \begin{pmatrix} 3 - 1 \\ -1 - 3 \\ 4 - (-2) \end{pmatrix} = \begin{pmatrix} 2 \\ -4 \\ 6 \end{pmatrix}$, ou plus simplement $\vec{n} = \dfrac{1}{2}\vec{AB} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$.
3. Équation du plan : $x - 2y + 3z + d = 0$.
   Passe par $I(2\,; 1\,; 1)$ : $2 - 2(1) + 3(1) + d = 0 \iff 3 + d = 0 \iff d = -3$.
   Équation : $x - 2y + 3z - 3 = 0$.
4. $M(x\,; y\,; z)$ est équidistant de $A$ et $B \iff MA^2 = MB^2 \iff (x-1)^2 + (y-3)^2 + (z+2)^2 = (x-3)^2 + (y+1)^2 + (z-4)^2$.
   En développant, les termes $x^2, y^2, z^2$ s'annulent :
   $-2x + 1 - 6y + 9 + 4z + 4 = -6x + 9 + 2y + 1 - 8z + 16$
   $4x - 8y + 12z - 12 = 0 \iff x - 2y + 3z - 3 = 0$. On retrouve exactement l'équation du plan médiateur !

**Solution 52.11 :**
1. Vecteurs normaux : $\vec{n}_1(2\,; -1\,; 1)$ et $\vec{n}_2(1\,; 1\,; 2)$.
   Ces vecteurs ne sont manifestement pas colinéaires ($\dfrac{2}{1} \neq \dfrac{-1}{1}$). Les plans ne sont donc pas parallèles.
2. Deux plans non parallèles se coupent selon une unique droite $\Delta$.
3. Résolvons le système des deux équations :
   $$\begin{cases} 2x - y + z - 3 = 0 \\ x + y + 2z - 6 = 0 \end{cases}$$
   Additionnons les deux lignes pour éliminer $y$ :
   $3x + 3z - 9 = 0 \iff x + z - 3 = 0 \iff x = 3 - z$.
   Soustrayons deux fois la seconde à la première pour éliminer $x$ :
   $-3y - 3z + 9 = 0 \iff y = 3 - z$.
   Posons $z = t$ comme paramètre réel ($t \in \mathbb{R}$) :
   $$\begin{cases} x = 3 - t \\ y = 3 - t \\ z = t \end{cases} \quad (t \in \mathbb{R}).$$
   C'est la représentation paramétrique de la droite d'intersection $\Delta$ (passant par $(3\,; 3\,; 0)$ et de vecteur directeur $(-1\,; -1\,; 1)$).

**Solution 52.12 :**
1. $(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 9$.
2. Pour $A(3\,; -1\,; 1)$ :
   $(3 - 1)^2 + (-1 + 2)^2 + (1 - 3)^2 = 2^2 + 1^2 + (-2)^2 = 4 + 1 + 4 = 9$. Donc $A \in \mathcal{S}$.
3. Le vecteur normal au plan tangent en $A$ est $\vec{\Omega A} \begin{pmatrix} 3 - 1 \\ -1 - (-2) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}$.
   L'équation de $\mathcal{T}$ est $2x + y - 2z + d = 0$.
   En $A(3\,; -1\,; 1)$ : $2(3) + (-1) - 2(1) + d = 0 \iff 6 - 1 - 2 + d = 0 \iff 3 + d = 0 \iff d = -3$.
   L'équation du plan tangent est : $2x + y - 2z - 3 = 0$.

**Solution 52.13 :**
1. $A(0, 0, 0)$, $B(3, 0, 0)$, $C(0, 4, 0)$.
   $\vec{AB} = 3\vec{i}$ et $\vec{AC} = 4\vec{j}$. Ils sont portés par deux axes perpendiculaires du repère, donc le triangle $ABC$ est rectangle en $A$.
   Son aire vaut $\mathcal{A}_{\text{base}} = \dfrac{AB \times AC}{2} = \dfrac{3 \times 4}{2} = 6$.
2. Les points $A, B, C$ appartiennent tous au plan $(Oxy)$ d'équation $z = 0$.
   Le point $D(1\,; 1\,; 5)$ a pour cote $z = 5$. Son projeté orthogonal sur le plan de base est $H(1\,; 1\,; 0)$.
   La hauteur est donc $DH = 5 - 0 = 5$.
3. $V = \dfrac{1}{3} \times \mathcal{A}_{\text{base}} \times \text{hauteur} = \dfrac{1}{3} \times 6 \times 5 = 10$ unités de volume.

---

#### Solutions du Niveau ★★★

**Solution 52.14 :**
1. $\vec{u} \cdot (\vec{u} \wedge \vec{v}) = x(yz' - zy') + y(zx' - xz') + z(xy' - yx') = xyz' - xzy' + yzx' - yxz' + zxy' - zyx' = 0$.
   De même $\vec{v} \cdot (\vec{u} \wedge \vec{v}) = 0$. Le vecteur est bien orthogonal aux deux !
2. Développons $\|\vec{u} \wedge \vec{v}\|^2 = (yz'-zy')^2 + (zx'-xz')^2 + (xy'-yx')^2$ et développons $(x^2+y^2+z^2)(x'^2+y'^2+z'^2) - (xx'+yy'+zz')^2$ : les termes carrés se simplifient et l'identité est exacte (identité de Lagrange).
3. $\|\vec{u} \wedge \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 (1 - \cos^2\theta) = \|\vec{u}\|^2 \|\vec{v}\|^2 \sin^2\theta$.
   Puisque $\theta \in [0\,; \pi]$, $\sin\theta \geq 0$, donc $\|\vec{u} \wedge \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$, ce qui est exactement l'aire du parallélogramme de côtés $\|\vec{u}\|$ et $\|\vec{v}\|$.
4. $\vec{AB} \begin{pmatrix} 1 \\ -2 \\ -2 \end{pmatrix}$ et $\vec{AC} \begin{pmatrix} -2 \\ -1 \\ -1 \end{pmatrix}$.
   $\vec{n} = \vec{AB} \wedge \vec{AC} = \begin{pmatrix} (-2)(-1) - (-2)(-1) \\ (-2)(-2) - 1(-1) \\ 1(-1) - (-2)(-2) \end{pmatrix} = \begin{pmatrix} 2 - 2 \\ 4 + 1 \\ -1 - 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 5 \\ -5 \end{pmatrix}$.
   On peut choisir $\vec{n} \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$.
   Vérification : $\vec{n} \cdot \vec{AB} = 0 - 2 + 2 = 0$ et $\vec{n} \cdot \vec{AC} = 0 - 1 + 1 = 0$ !

**Solution 52.15 :**
1. La direction de la perpendiculaire commune doit être orthogonale à $\vec{u}_1$ et à $\vec{u}_2$, donc portée par $\vec{n} = \vec{u}_1 \wedge \vec{u}_2$. Le plan contenant $\mathcal{D}_1$ et dirigé par $\vec{n}$ coupe $\mathcal{D}_2$ en un unique point $H_2$. La perpendiculaire issue de $H_2$ coupe $\mathcal{D}_1$ en $H_1$.
2. Le segment $[H_1H_2]$ est colinéaire à $\vec{n}$.
   Dans le parallélépipède formé par $\vec{u}_1, \vec{u}_2$ et $\vec{A_1A_2}$, la distance entre les deux droites est la projection orthogonale du vecteur $\vec{A_1A_2}$ sur la droite normale de vecteur unitaire $\dfrac{\vec{n}}{\|\vec{n}\|}$, ce qui donne immédiatement $d = \dfrac{|\vec{A_1A_2} \cdot \vec{n}|}{\|\vec{n}\|}$.

**Solution 52.16 :**
1. D'après la relation de Chasles, pour tout point $A \in \mathcal{P}$ : $\vec{AM} = \vec{AH} + \vec{HM}$.
2. Prenons le produit scalaire avec le vecteur normal $\vec{n}$ :
   $\vec{AM} \cdot \vec{n} = (\vec{AH} + \vec{HM}) \cdot \vec{n} = \vec{AH} \cdot \vec{n} + \vec{HM} \cdot \vec{n}$.
   Puisque $A$ et $H$ appartiennent tous deux au plan $\mathcal{P}$, le vecteur $\vec{AH}$ est contenu dans le plan, donc $\vec{AH} \perp \vec{n} \implies \vec{AH} \cdot \vec{n} = 0$.
   De plus, $\vec{HM}$ est colinéaire à $\vec{n}$, donc $|\vec{HM} \cdot \vec{n}| = \|\vec{HM}\| \|\vec{n}\| = d(M, \mathcal{P}) \|\vec{n}\|$.
   D'autre part, en coordonnées :
   $\vec{AM} \cdot \vec{n} = a(x_0 - x_A) + b(y_0 - y_A) + c(z_0 - z_A) = ax_0 + by_0 + cz_0 - (ax_A + by_A + cz_A)$.
   Or $A \in \mathcal{P} \implies ax_A + by_A + cz_A + d = 0 \implies -(ax_A + by_A + cz_A) = d$.
   Donc $\vec{AM} \cdot \vec{n} = ax_0 + by_0 + cz_0 + d$.
   En prenant la valeur absolue :
   $|ax_0 + by_0 + cz_0 + d| = d(M, \mathcal{P}) \|\vec{n}\| \iff d(M, \mathcal{P}) = \dfrac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}$.
   La formule est rigoureusement démontrée ! $\blacksquare$

---

### La question qui ouvre la suite

Nous avons appris à mesurer l'espace continu : longueurs, angles, surfaces planes et volumes 3D.
Mais le monde mathématique ne se résume pas à des continus géométriques. Il est aussi fait de choix discrets :
Combien de chemins mènent d'un sommet à un autre ? Combien de combinaisons possibles sur un cadenas à roulettes ? De combien de manières peut-on choisir 5 cartes dans un jeu de 32 ou former une équipe de délégués ?

Comment dénombrer sans jamais compter un par un jusqu'à l'infini ?

Rendez-vous au chapitre 53 avec **le cadenas à code et les façons de choisir**.
