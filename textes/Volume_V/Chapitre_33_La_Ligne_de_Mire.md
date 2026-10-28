# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 33 : La Ligne de Mire

> *« Une droite n'est pas une simple trace d'encre tirée à la règle : c'est un rayon laser infini qui traverse l'univers, une ligne de mire balayée par le regard du guetteur. Pour enfermer cette infinité de points dans une formule algébrique, il suffit de deux nombres : une ancre sur l'axe vertical et une pente d'escalade. Alors, le croisement de deux chemins devient le dénouement d'une équation. »*

---

### Ce que tu vas découvrir

- Comment une droite naît d'un point d'ancrage et d'un **vecteur directeur** qui lui donne son cap.
- L'**équation cartésienne** générale $ax + by + c = 0$, et pourquoi le vecteur $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ en est la boussole.
- L'**équation réduite** $y = mx + p$ : le sens physique du **coefficient directeur** $m$ (la pente) et de l'**ordonnée à l'origine** $p$.
- Le cas particulier des droites verticales d'équation $x = k$.
- Les trois destins de deux droites qui se rencontrent : sécantes en un point unique, strictement parallèles ou confondues.
- La résolution algébrique et graphique des **systèmes de deux équations à deux inconnues** par substitution et par combinaison linéaire.

---

### 1. Le problème : la tour de guet et le navire dans le brouillard

Sur une falaise escarpée dominant l'océan se dresse une tour de guet. La nuit est tombée, un épais brouillard enveloppe la baie et deux navires naviguent à l'aveugle.

Le gardien du phare dispose d'un radar cartésien :
- Le navire marchand *L'Espérance* se trouve actuellement au point de coordonnées $A(2\,; 3)$ et suit un cap rectiligne guidé par le vecteur vitesse $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
- Une frégate de secours *La Vigilante* est signalée au point $B(-1\,; 8)$ et file en ligne droite selon le vecteur $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

```
                 y ▲
                   │           La Vigilante B(-1, 8)
                 8 ┼           o
                   │            \   v(1, -1)
                   │             ▼\
                   │               \
                   │                 \   Point de rencontre ?
                 3 ┼               o───►o──────────────────►
                   │            A(2,3)   \ u(2, 1)
                   │                      \   L'Espérance
                 O ┼───────┼───────┼───────┼────────► x
                  -1       0       2
```

Le commandant du port pose deux questions cruciales :
1. *Ces deux navires risquent-ils d'entrer en collision, c'est-à-dire leurs trajectoires se coupent-elles en un point précis du plan d'eau ?*
2. *Si oui, quelles sont les coordonnées exactes du point de croisement ?*

Pour répondre, le dessin sur papier millimétré a ses limites : avec un crayon mal taillé ou une échelle imprécise, on peut se tromper de plusieurs centaines de mètres. Il nous faut une méthode algébrique infaillible, capable de traduire une ligne infinie en une équation que l'on peut résoudre avec une précision absolue.

---

### 2. Le cap et la trace : le vecteur directeur

#### 2.1 Donner une direction à une droite

Une droite dans le plan est entièrement déterminée par :
- soit **deux points distincts** $A$ et $B$ (par deux points passe une unique droite) ;
- soit **un point d'ancrage** $A$ et **un vecteur non nul** qui lui donne sa direction.

> **📐 Définition — Vecteur directeur.**
> Soit $\mathcal{D}$ une droite du plan. Tout vecteur non nul $\vec{u}$ ayant la même direction que la droite $\mathcal{D}$ est appelé un **vecteur directeur** de $\mathcal{D}$.
> Si $A$ et $B$ sont deux points distincts de $\mathcal{D}$, alors le vecteur $\vec{AB}$ est un vecteur directeur de $\mathcal{D}$.

```
                             D
                           /
                         /  u (vecteur directeur)
                       /──►
                     /
                   o A
                 /
               /
```

> **💡 Le savais-tu ? Une droite a une infinité de vecteurs directeurs !**
> Si $\vec{u}$ est un vecteur directeur de la droite $\mathcal{D}$, alors pour tout nombre réel non nul $k$, le vecteur $k\vec{u}$ a la même direction : il est donc aussi un vecteur directeur de $\mathcal{D}$. Deux fois plus long, trois fois plus court ou orienté en sens contraire, il porte toujours la même droite.

#### 2.2 Caractérisation vectorielle d'une droite

Un point $M(x\,; y)$ appartient à la droite $\mathcal{D}$ passant par $A(x_A\,; y_A)$ et de vecteur directeur $\vec{u}$ si et seulement si le déplacement de $A$ à $M$ se fait le long de ce même cap :
$$M \in \mathcal{D} \iff \vec{AM} \text{ et } \vec{u} \text{ sont colinéaires}.$$

D'après le chapitre précédent, deux vecteurs sont colinéaires si et seulement si leur déterminant est nul :
$$M \in \mathcal{D} \iff \det(\vec{AM}, \vec{u}) = 0.$$

C'est cette condition simple qui engendre toutes les équations de droites !

---

### 3. L'équation cartésienne d'une droite

#### 3.1 La forme générale $ax + by + c = 0$

> **📐 Théorème fondamental — Équation cartésienne.**
> 1. Toute droite $\mathcal{D}$ du plan admet une équation de la forme :
>    $$ax + by + c = 0$$
>    où $a, b, c$ sont des réels avec $(a, b) \neq (0, 0)$ (c'est-à-dire que $a$ et $b$ ne sont pas nuls en même temps).
> 2. Réciproquement, toute équation de la forme $ax + by + c = 0$ avec $(a, b) \neq (0, 0)$ est l'équation d'une droite.
> 3. Le vecteur $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ est un **vecteur directeur** de cette droite.

> **✍️ Démonstration (exigible) — De la colinéarité à l'équation cartésienne.**
> Soit $\mathcal{D}$ la droite passant par $A(x_A\,; y_A)$ et de vecteur directeur $\vec{u}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$ non nul.
> Soit un point quelconque $M(x\,; y)$ du plan.
> Le vecteur $\vec{AM}$ a pour coordonnées :
> $$\vec{AM}\begin{pmatrix} x - x_A \\ y - y_A \end{pmatrix}.$$
> Le point $M$ appartient à $\mathcal{D}$ si et seulement si $\vec{AM}$ et $\vec{u}$ sont colinéaires :
> $$\det(\vec{AM}, \vec{u}) = 0 \iff (x - x_A)u_2 - (y - y_A)u_1 = 0.$$
> En développant :
> $$u_2 x - u_1 y + (-u_2 x_A + u_1 y_A) = 0.$$
> Posons :
> $$a = u_2, \quad b = -u_1, \quad c = -u_2 x_A + u_1 y_A.$$
> Comme $\vec{u} \neq \vec{0}$, le couple $(u_1, u_2) \neq (0, 0)$, donc $(a, b) \neq (0, 0)$.
> L'égalité devient :
> $$ax + by + c = 0.$$
> De plus, le vecteur $\vec{u}$ a pour coordonnées $\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} -b \\ a \end{pmatrix}$. C'est bien un vecteur directeur de la droite. $\blacksquare$

> **⚠️ Attention, piège ! L'équation cartésienne n'est pas unique.**
> Si $2x - 3y + 5 = 0$ est l'équation d'une droite, alors en multipliant chaque terme par $2$, on obtient $4x - 6y + 10 = 0$, qui décrit **exactement la même droite** !
> Deux équations $ax + by + c = 0$ et $a'x + b'y + c' = 0$ représentent la même droite si et seulement si leurs coefficients sont proportionnels : il existe un réel $k \neq 0$ tel que $a' = ka$, $b' = kb$ et $c' = kc$.

---

### 4. L'équation réduite : la pente et l'ordonnée à l'origine

L'équation cartésienne $ax + by + c = 0$ est très générale, mais pour tracer une droite ou comprendre sa pente physique, les mathématiciens préfèrent exprimer $y$ directement en fonction de $x$.

#### 4.1 Deux catégories de droites

Isolons le terme en $y$ dans l'équation cartésienne :
$$by = -ax - c.$$

Deux cas se présentent :

##### Cas 1 : $b \neq 0$ (la droite n'est pas verticale)
On peut diviser par $b$ :
$$y = -\frac{a}{b}x - \frac{c}{b}.$$
En posant $m = -\frac{a}{b}$ et $p = -\frac{c}{b}$, l'équation prend la forme :
$$\boxed{y = mx + p}$$
C'est **l'équation réduite** de la droite.

- **$m$ est le coefficient directeur** (ou la **pente**).
- **$p$ est l'ordonnée à l'origine** : c'est l'altitude à laquelle la droite franchit l'axe vertical $(Oy)$ (pour $x = 0$, on a $y = m(0) + p = p$). Le point de coordonnées $(0\,; p)$ est sur la droite.

```
                    y ▲
                      │            /
                      │          /
                      │        /
                    p ┼──────o             Avance de 1
                      │     /│             Monte de m
                      │    / │ m
                      │   /  │
                      │  o───┴──
                      │  │ 1
                    O ┼──┴────────────► x
```

##### Cas 2 : $b = 0$ (la droite est verticale)
L'équation devient $ax + c = 0$. Puisque $(a, b) \neq (0, 0)$ et $b = 0$, on a obligatoirement $a \neq 0$.
On en déduit :
$$x = -\frac{c}{a} = k.$$
Tous les points de la droite ont la **même abscisse** $k$. La droite est strictement parallèle à l'axe des ordonnées $(Oy)$. Elle n'a pas de pente définie (sa pente est « infinie ») et elle ne peut pas s'écrire sous la forme $y = mx + p$. Son vecteur directeur est vertical, par exemple $\vec{j}\begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

#### 4.2 Le sens géométrique du coefficient directeur $m$

> **📐 Propriété fondamentale — Calcul de la pente.**
> Soient deux points distincts $A(x_A\,; y_A)$ et $B(x_B\,; y_B)$ d'une droite non verticale ($x_A \neq x_B$).
> Le coefficient directeur $m$ est donné par la formule :
> $$m = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x}.$$

**Sens physique :**
$\Delta y$ représente la variation d'altitude (dénivelé) et $\Delta x$ représente l'avancement horizontal.
- Si $m > 0$ : la droite « monte » de gauche à droite. La fonction affine associée est strictement croissante.
- Si $m < 0$ : la droite « descend » de gauche à droite. La fonction affine associée est strictement décroissante.
- Si $m = 0$ : l'équation devient $y = p$. La droite est parfaitement **horizontale**, parallèle à l'axe des abscisses.
- Un vecteur directeur immédiat d'une droite d'équation $y = mx + p$ est $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$. En avançant de $1$ unité en abscisse, on monte de $m$ unités en ordonnée.

---

### 5. Méthodes fondamentales de construction et de détermination

#### 5.1 Tracer une droite à coup sûr

Il existe deux méthodes rapides :
1. **La méthode des deux points :** On choisit deux abscisses simples (souvent $x = 0$ et $x = 1$ ou $x = 2$), on calcule les ordonnées correspondantes, on place les deux points et on les relie à la règle.
2. **La méthode de la pente :** On place le point de départ $(0\,; p)$ sur l'axe des ordonnées. Depuis ce point, on se décale d'une unité vers la droite, puis on monte de $m$ unités (ou descend si $m < 0$). On place le second point et on trace.

#### 5.2 Trouver l'équation d'une droite

- **Cas A : Connaissant deux points $A(x_A\,; y_A)$ et $B(x_B\,; y_B)$ avec $x_A \neq x_B$.**
  1. On calcule $m = \frac{y_B - y_A}{x_B - x_A}$.
  2. L'équation s'écrit $y = mx + p$. Pour trouver $p$, on utilise le fait que $A \in \mathcal{D}$ :
     $$y_A = m x_A + p \implies p = y_A - m x_A.$$

- **Cas B : Connaissant un point $A(x_A\,; y_A)$ et un vecteur directeur $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$.**
  1. L'équation cartésienne s'écrit directement $ax + by + c = 0$.
  2. On remplace $x$ et $y$ par les coordonnées de $A$ pour calculer la constante $c$ :
     $$a x_A + b y_A + c = 0 \implies c = -a x_A - b y_A.$$

---

### 6. Positions relatives de deux droites et systèmes linéaires

Considérons deux droites dans le plan : $\mathcal{D} : ax + by + c = 0$ et $\mathcal{D}' : a'x + b'y + c' = 0$, de vecteurs directeurs respectifs $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ et $\vec{u}'\begin{pmatrix} -b' \\ a' \end{pmatrix}$.

#### 6.1 Les trois configurations possibles

```
   Droites sécantes            Droites strictement parallèles     Droites confondues
          /  /                            /     /                        ///////
         /  /                            /     /                        ///////
        /  X  (un point)                /     /   (aucun point)        /////// (infinité)
       /  /  \                         /     /                        ///////
```

1. **Droites sécantes :** Leurs vecteurs directeurs ne sont pas colinéaires :
   $$\det(\vec{u}, \vec{u}') \neq 0 \iff (-b)(a') - (a)(-b') \neq 0 \iff ab' - a'b \neq 0.$$
   Pour des droites non verticales : $m \neq m'$.
   Elles se coupent en **un point unique**.

2. **Droites strictement parallèles :** Les vecteurs directeurs sont colinéaires ($ab' - a'b = 0$, soit $m = m'$), mais les ordonnées à l'origine sont différentes ($p \neq p'$).
   Leur intersection est vide : $\mathcal{D} \cap \mathcal{D}' = \varnothing$.

3. **Droites confondues :** Les vecteurs directeurs sont colinéaires et les droites ont au moins un point commun (donc $m = m'$ et $p = p'$). Tous leurs points sont communs : $\mathcal{D} = \mathcal{D}'$.

#### 6.2 Résolution d'un système de deux équations à deux inconnues

Chercher l'intersection de deux droites revient à trouver les couples $(x\,; y)$ qui vérifient simultanément les deux équations :
$$\begin{cases} ax + by = e \\ cx + dy = f \end{cases}$$

Il existe deux grandes techniques algébriques :

##### Méthode 1 : La substitution
On isole l'une des inconnues (celle dont le coefficient est le plus simple, idéalement $1$ ou $-1$) dans l'une des équations, puis on remplace son expression dans l'autre équation. On obtient alors une équation à une seule inconnue.

##### Méthode 2 : La combinaison linéaire (élimination)
On multiplie les équations par des nombres judicieusement choisis pour que les coefficients de l'une des inconnues (par exemple $x$) deviennent opposés. En additionnant membre à membre les deux nouvelles équations, l'inconnue $x$ s'élimine !

---

### 7. Exemples résolus détaillés

> **Exemple résolu 1 — Retour au problème du port : collision de navires.**
> Rappel des données :
> - *L'Espérance* part de $A(2\,; 3)$ avec $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
> - *La Vigilante* part de $B(-1\,; 8)$ avec $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
> 1. Déterminer une équation cartésienne de la trajectoire $\mathcal{D}_1$ de *L'Espérance*.
> 2. Déterminer une équation cartésienne de la trajectoire $\mathcal{D}_2$ de *La Vigilante*.
> 3. Déterminer si les trajectoires se croisent et trouver les coordonnées du point d'intersection $I$.
>
> **Solution :**
> 1. Pour $\mathcal{D}_1$, $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ est vecteur directeur. Comme $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$, on peut choisir $a = 1$ et $b = -2$.
>    L'équation est $1x - 2y + c = 0$.
>    $A(2\,; 3) \in \mathcal{D}_1 \implies 2 - 2(3) + c = 0 \implies 2 - 6 + c = 0 \implies c = 4$.
>    Donc $\mathcal{D}_1 : x - 2y + 4 = 0$ (ou sous forme réduite : $y = \frac{1}{2}x + 2$).
>
> 2. Pour $\mathcal{D}_2$, $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ est vecteur directeur. On peut choisir $a = -1$ et $b = -1$, ou plus simplement $\vec{v}\begin{pmatrix} -b \\ a \end{pmatrix} \implies a = 1, b = 1$ (car $\begin{pmatrix} -1 \\ 1 \end{pmatrix} = -\vec{v}$).
>    L'équation est $x + y + c' = 0$.
>    $B(-1\,; 8) \in \mathcal{D}_2 \implies -1 + 8 + c' = 0 \implies 7 + c' = 0 \implies c' = -7$.
>    Donc $\mathcal{D}_2 : x + y - 7 = 0$ (ou sous forme réduite : $y = -x + 7$).
>
> 3. Comparons les pentes : $m_1 = \frac{1}{2}$ et $m_2 = -1$.
>    Puisque $m_1 \neq m_2$, les droites sont sécantes en un point unique $I$.
>    Résolvons le système :
>    $$\begin{cases} y = \frac{1}{2}x + 2 \\ y = -x + 7 \end{cases}$$
>    Par égalité des deux expressions de $y$ :
>    $$\frac{1}{2}x + 2 = -x + 7 \iff \frac{1}{2}x + x = 7 - 2 \iff \frac{3}{2}x = 5 \iff x = \frac{10}{3}.$$
>    Calculons $y$ :
>    $$y = -\frac{10}{3} + 7 = -\frac{10}{3} + \frac{21}{3} = \frac{11}{3}.$$
>    Les trajectoires se croisent au point $I\left(\frac{10}{3} \,;\, \frac{11}{3}\right)$.

> **Exemple résolu 2 — Déterminer l'équation d'une droite passant par deux points.**
> Soient les points $E(-3\,; 5)$ et $F(1\,; -3)$.
> Trouver l'équation réduite de la droite $(EF)$.
>
> **Solution :**
> Vérifions d'abord si la droite est verticale : $x_E = -3$ et $x_F = 1$. Comme $x_E \neq x_F$, elle n'est pas verticale.
> 1. Calcul du coefficient directeur $m$ :
>    $$m = \frac{y_F - y_E}{x_F - x_E} = \frac{-3 - 5}{1 - (-3)} = \frac{-8}{4} = -2.$$
> 2. Calcul de l'ordonnée à l'origine $p$ :
>    L'équation s'écrit $y = -2x + p$.
>    Comme $F(1\,; -3)$ appartient à la droite :
>    $$-3 = -2(1) + p \implies -3 = -2 + p \implies p = -1.$$
> L'équation réduite est donc $\boxed{y = -2x - 1}$.
> *(Vérification avec $E$ : $-2(-3) - 1 = 6 - 1 = 5 = y_E$. Tout concorde !)*

> **Exemple résolu 3 — Résolution d'un système par combinaison linéaire.**
> Résoudre dans $\mathbb{R}^2$ le système suivant :
> $$\begin{cases} 3x + 4y = 11 \quad (L_1) \\ 5x - 2y = 40 \quad (L_2) \end{cases}$$
>
> **Solution :**
> Observons les coefficients de $y$ : $+4$ dans $L_1$ et $-2$ dans $L_2$.
> En multipliant $L_2$ par $2$, le coefficient de $y$ deviendra $-4$, exactement l'opposé de $+4$ !
> Multiplions $L_2$ par $2$ :
> $$2 \times (5x - 2y) = 2 \times 40 \iff 10x - 4y = 80 \quad (L'_2).$$
> Additionnons $L_1$ et $L'_2$ membre à membre :
> $$(3x + 4y) + (10x - 4y) = 11 + 80 \iff 13x = 91 \iff x = \frac{91}{13} = 7.$$
> Remplaçons maintenant $x = 7$ dans $L_1$ :
> $$3(7) + 4y = 11 \iff 21 + 4y = 11 \iff 4y = 11 - 21 = -10 \iff y = -\frac{10}{4} = -2{,}5.$$
> Le système admet pour unique solution le couple $(7\,; -2{,}5)$.
> L'ensemble des solutions est $S = \{(7\,; -2{,}5)\}$.

> **Exemple résolu 4 — Système sans solution ou avec une infinité de solutions.**
> Étudier selon la géométrie les deux systèmes suivants :
> a) $\begin{cases} 2x - 3y = 7 \\ -4x + 6y = 5 \end{cases}$ \quad b) $\begin{cases} x - 2y = 3 \\ 3x - 6y = 9 \end{cases}$
>
> **Solution :**
> a) Multiplions la première équation par $2$ :
> $$4x - 6y = 14.$$
> Additionnons avec la deuxième :
> $$(4x - 6y) + (-4x + 6y) = 14 + 5 \iff 0 = 19.$$
> Cette égalité est impossible ! Géométriquement, les deux droites ont des vecteurs directeurs colinéaires ($\frac{-4}{2} = \frac{6}{-3} = -2$), elles sont strictement parallèles et ne se coupent jamais. Le système n'a **aucune solution** : $S = \varnothing$.
>
> b) Multiplions la première équation par $3$ :
> $$3x - 6y = 9.$$
> C'est exactement la deuxième équation ! Les deux équations décrivent la **même droite**.
> Tout point de cette droite est solution. Le système admet une **infinité de solutions** : tous les couples de la forme $(2y + 3 \,;\, y)$ pour $y \in \mathbb{R}$.

> **Exemple résolu 5 — Déterminer l'équation de la médiatrice d'un segment.**
> On donne $A(1\,; 2)$ et $B(5\,; 4)$.
> Trouver l'équation de la médiatrice $\Delta$ du segment $[AB]$.
>
> **Solution :**
> Rappel : la médiatrice est la droite perpendiculaire à $[AB]$ passant par son milieu $I$.
> 1. Milieu $I$ de $[AB]$ :
>    $$x_I = \frac{1 + 5}{2} = 3, \quad y_I = \frac{2 + 4}{2} = 3 \implies I(3\,; 3).$$
> 2. Propriété géométrique : $M(x\,; y) \in \Delta \iff MA^2 = MB^2$.
>    $$MA^2 = (x - 1)^2 + (y - 2)^2 = x^2 - 2x + 1 + y^2 - 4y + 4 = x^2 + y^2 - 2x - 4y + 5.$$
>    $$MB^2 = (x - 5)^2 + (y - 4)^2 = x^2 - 10x + 25 + y^2 - 8y + 16 = x^2 + y^2 - 10x - 8y + 41.$$
>    L'égalité $MA^2 = MB^2$ donne :
>    $$x^2 + y^2 - 2x - 4y + 5 = x^2 + y^2 - 10x - 8y + 41.$$
>    Les termes quadratiques $x^2$ et $y^2$ s'annulent :
>    $$-2x - 4y + 5 = -10x - 8y + 41 \iff 8x + 4y - 36 = 0.$$
>    En divisant toute l'équation par $4$ :
>    $$\boxed{2x + y - 9 = 0} \quad \text{ou sous forme réduite} \quad \boxed{y = -2x + 9}.$$

> **Exemple résolu 6 — Faisceau de droites dépendant d'un paramètre.**
> Pour tout réel $m$, on considère la droite $\mathcal{D}_m$ d'équation :
> $$(m - 1)x + (2m + 1)y - 5m + 2 = 0.$$
> Démontrer que toutes les droites $\mathcal{D}_m$ passent par un point fixe $K$ dont on déterminera les coordonnées.
>
> **Solution :**
> Réorganisons l'équation en regroupant les termes selon les puissances du paramètre $m$ :
> $$mx - x + 2my + y - 5m + 2 = 0 \iff m(x + 2y - 5) + (-x + y + 2) = 0.$$
> Pour que cette égalité soit vraie **pour toute valeur de $m$**, il faut et il suffit que le coefficient devant $m$ et le terme constant soient nuls simultanément :
> $$\begin{cases} x + 2y - 5 = 0 \\ -x + y + 2 = 0 \end{cases}$$
> Additionnons les deux équations :
> $$(x + 2y - 5) + (-x + y + 2) = 0 \iff 3y - 3 = 0 \iff y = 1.$$
> Remplaçons dans la deuxième équation :
> $$-x + 1 + 2 = 0 \iff x = 3.$$
> Toutes les droites du faisceau passent par le point fixe $K(3\,; 1)$ !

---

### 8. En informatique : résoudre un système $2 \times 2$ en Python

Voici un script Python qui prend les coefficients de deux droites sous forme cartésienne et calcule leur point d'intersection :

```python
def resoudre_systeme(a1, b1, c1, a2, b2, c2):
    """
    Résout le système :
    a1*x + b1*y + c1 = 0
    a2*x + b2*y + c2 = 0
    """
    # Calcul du déterminant principal (a1*b2 - a2*b1)
    det = a1 * b2 - a2 * b1
    
    if abs(det) < 1e-12:
        # Droites parallèles ou confondues
        # Test de proportionnalité avec les constantes
        if abs(a1 * c2 - a2 * c1) < 1e-12 and abs(b1 * c2 - b2 * c1) < 1e-12:
            return "Infinité de solutions (droites confondues)"
        else:
            return "Aucune solution (droites strictement parallèles)"
    else:
        # Règle de Cramer pour trouver x et y
        # Réécriture sous la forme a*x + b*y = -c
        e1, e2 = -c1, -c2
        x = (e1 * b2 - e2 * b1) / det
        y = (a1 * e2 - a2 * e1) / det
        return (x, y)

# Test avec le système de l'Exemple 1 :
# x - 2y + 4 = 0  et  x + y - 7 = 0
solution = resoudre_systeme(1, -2, 4, 1, 1, -7)
print("Point d'intersection :", solution)  # Affiche (3.3333333333333335, 3.6666666666666665)
```

---

### Ce qu'il faut retenir

1. **Vecteur directeur :** tout vecteur $\vec{u}$ non nul parallèle à la droite. Si $A, B \in \mathcal{D}$, $\vec{AB}$ est un vecteur directeur.
2. **Équation cartésienne :** $ax + by + c = 0$ avec $(a, b) \neq (0, 0)$.
   - Vecteur directeur canonique : $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$.
3. **Équation réduite :**
   - Si la droite n'est pas verticale ($b \neq 0$) : $y = mx + p$.
     - $m = -\frac{a}{b} = \frac{y_B - y_A}{x_B - x_A}$ est la **pente** (coefficient directeur).
     - $p$ est l'**ordonnée à l'origine** (point $(0\,; p)$).
     - Vecteur directeur : $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$.
   - Si la droite est verticale ($b = 0$) : $x = k$. Pas de coefficient directeur.
4. **Positions relatives :**
   - Parallèles $\iff m = m'$ (ou $ab' - a'b = 0$).
   - Sécantes $\iff m \neq m'$ (ou $ab' - a'b \neq 0$). Intersection unique par système.
5. **Méthodes de résolution de système :**
   - *Substitution* : isoler une variable dans une ligne et l'injecter dans l'autre.
   - *Combinaison* : multiplier pour annuler une variable par addition.

---

### Exercices

#### Exercices d'application directe (★)

1. Donner un vecteur directeur de la droite d'équation $3x - 5y + 7 = 0$.
2. Donner un vecteur directeur de la droite d'équation réduite $y = -4x + 3$.
3. Déterminer le coefficient directeur et l'ordonnée à l'origine de la droite $2x + 4y - 8 = 0$.
4. Écrire l'équation réduite de la droite passant par le point $P(0\,; -5)$ et de pente $m = 3$.
5. La droite d'équation $x = 4$ admet-elle un coefficient directeur ? Pourquoi ?
6. Les droites d'équations $y = 3x - 2$ et $6x - 2y + 5 = 0$ sont-elles parallèles ?
7. Le point $A(3\,; -1)$ appartient-il à la droite d'équation $2x - 5y - 11 = 0$ ?
8. Déterminer l'abscisse du point de la droite $y = 2x - 6$ dont l'ordonnée vaut $4$.
9. Résoudre le système par substitution : $\begin{cases} y = 2x - 1 \\ 3x + y = 9 \end{cases}$.
10. Résoudre le système par combinaison : $\begin{cases} x + y = 10 \\ x - y = 4 \end{cases}$.

#### Exercices d'entraînement et de réflexion (★★)

11. Déterminer l'équation cartésienne de la droite passant par $A(2\,; -3)$ et de vecteur directeur $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$.
12. Déterminer l'équation réduite de la droite passant par les points $M(-2\,; 7)$ et $N(4\,; 1)$.
13. On donne les points $A(-1\,; 2)$, $B(3\,; 4)$ et $C(2\,; -1)$.
    Déterminer une équation de la droite $\mathcal{D}$ passant par $C$ et parallèle à $(AB)$.
14. Résoudre dans $\mathbb{R}^2$ le système : $\begin{cases} 4x + 3y = 1 \\ 2x - 5y = 7 \end{cases}$.
15. Déterminer les coordonnées du point d'intersection des droites $\mathcal{D}_1 : 3x - 2y + 6 = 0$ et $\mathcal{D}_2 : x + 2y - 2 = 0$.
16. Pour quelle valeur du réel $k$ la droite d'équation $kx + 2y - 5 = 0$ est-elle parallèle à la droite passant par $A(1\,; 1)$ et $B(3\,; 7)$ ?
17. Soit le triangle $ABC$ avec $A(0\,; 4)$, $B(-2\,; 0)$ et $C(4\,; 0)$.
    Déterminer l'équation de la médiane issue de $A$.
18. Déterminer le réel $m$ pour que le système $\begin{cases} mx + 2y = 4 \\ 3x + (m - 1)y = 2 \end{cases}$ n'admette pas de solution unique.

#### Exercices d'approfondissement et défis (★★★)

19. **Intersection des trois hauteurs d'un triangle (orthocentre).**
    Dans un repère orthonormé, on donne $A(0\,; 3)$, $B(-2\,; 0)$ et $C(4\,; 0)$.
    a) Déterminer une équation de la hauteur issue de $A$.
    b) En utilisant le fait que la hauteur issue de $B$ est perpendiculaire à $(AC)$, déterminer son équation.
    c) Calculer les coordonnées de l'orthocentre $H$ du triangle.
20. **Projeté orthogonal d'un point sur une droite.**
    Soit la droite $\mathcal{D} : 2x - y + 1 = 0$ et le point $A(4\,; 4)$.
    a) Déterminer l'équation de la droite $\Delta$ perpendiculaire à $\mathcal{D}$ passant par $A$.
    b) Déterminer les coordonnées du point d'intersection $H$ de $\mathcal{D}$ et $\Delta$.
    c) Calculer la distance $AH$. (Cette distance est la distance minimale du point $A$ à la droite $\mathcal{D}$).
21. **Point de concours de trois droites.**
    On considère les trois droites :
    $\mathcal{D}_1 : 2x - y - 1 = 0$, $\mathcal{D}_2 : x + y - 5 = 0$, et $\mathcal{D}_3 : 3x + ky - 7 = 0$.
    Déterminer la valeur du réel $k$ pour que ces trois droites soient concourantes en un même point.
22. **Problème économique d'offre et de demande.**
    Dans un marché de denrées, la quantité offerte $q_O$ et la quantité demandée $q_D$ (en tonnes) dépendent du prix unitaire $p$ (en euros par kg) selon les lois linéaires suivantes :
    - Offre : $q_O = 2p - 4$ (les producteurs offrent davantage si le prix monte).
    - Demande : $q_D = -3p + 21$ (les acheteurs achètent moins si le prix monte).
    a) Tracer les deux droites dans un repère $(p\,; q)$.
    b) Déterminer par le calcul le prix d'équilibre $p_E$ pour lequel l'offre est égale à la demande.
    c) Quelle est alors la quantité échangée sur le marché à l'équilibre ?

---

### Solutions

1. Pour $ax + by + c = 0$, un vecteur directeur est $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$. Ici $a = 3, b = -5 \implies \vec{u}\begin{pmatrix} 5 \\ 3 \end{pmatrix}$.
2. Pour $y = mx + p$, un vecteur directeur est $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$. Ici $m = -4 \implies \vec{u}\begin{pmatrix} 1 \\ -4 \end{pmatrix}$.
3. $4y = -2x + 8 \iff y = -\frac{2}{4}x + \frac{8}{4} = -\frac{1}{2}x + 2$.
   Coefficient directeur $m = -\frac{1}{2}$, ordonnée à l'origine $p = 2$.
4. $y = 3x - 5$.
5. Non, la droite $x = 4$ est verticale. Sa pente n'est pas définie (dénominateur $\Delta x = 0$ nul).
6. Droite 1 : $m_1 = 3$. Droite 2 : $-2y = -6x - 5 \iff y = 3x + 2{,}5 \implies m_2 = 3$.
   Comme $m_1 = m_2 = 3$ et que les ordonnées à l'origine sont distinctes ($-2 \neq 2{,}5$), les droites sont strictement parallèles.
7. Remplaçons $x = 3$ et $y = -1$ : $2(3) - 5(-1) - 11 = 6 + 5 - 11 = 0$. Oui, $A \in \mathcal{D}$.
8. $4 = 2x - 6 \iff 2x = 10 \iff x = 5$.
9. Remplaçons $y$ dans la deuxième équation : $3x + (2x - 1) = 9 \iff 5x - 1 = 9 \iff 5x = 10 \iff x = 2$.
   Alors $y = 2(2) - 1 = 3$. Solution : $(2\,; 3)$.
10. Additionnons les équations : $(x + y) + (x - y) = 10 + 4 \iff 2x = 14 \iff x = 7$.
    Alors $7 + y = 10 \iff y = 3$. Solution : $(7\,; 3)$.
11. $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix} = \begin{pmatrix} -b \\ a \end{pmatrix} \implies a = 4$ et $b = 3$.
    L'équation est $4x + 3y + c = 0$.
    $A(2\,; -3) \in \mathcal{D} \implies 4(2) + 3(-3) + c = 0 \iff 8 - 9 + c = 0 \iff c = 1$.
    Équation : $4x + 3y + 1 = 0$.
12. $m = \frac{1 - 7}{4 - (-2)} = \frac{-6}{6} = -1$.
    $y = -x + p$. Avec $N(4\,; 1)$ : $1 = -4 + p \implies p = 5$.
    Équation réduite : $y = -x + 5$.
13. Vecteur $\vec{AB}\begin{pmatrix} 3 - (-1) \\ 4 - 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$ ou plus simplement $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
    $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix} \implies a = 1, b = -2$.
    L'équation est $x - 2y + c = 0$.
    $C(2\,; -1) \in \mathcal{D} \implies 2 - 2(-1) + c = 0 \iff 2 + 2 + c = 0 \iff c = -4$.
    Équation : $x - 2y - 4 = 0$ (ou $y = \frac{1}{2}x - 2$).
14. Multiplions la deuxième ligne par $-2$ :
    $-2(2x - 5y) = -2(7) \iff -4x + 10y = -14$.
    Additionnons avec la première : $(4x + 3y) + (-4x + 10y) = 1 - 14 \iff 13y = -13 \iff y = -1$.
    Remplaçons : $2x - 5(-1) = 7 \iff 2x + 5 = 7 \iff 2x = 2 \iff x = 1$.
    Solution : $(1\,; -1)$.
15. Additionnons $\mathcal{D}_1$ et $\mathcal{D}_2$ :
    $(3x - 2y + 6) + (x + 2y - 2) = 0 \iff 4x + 4 = 0 \iff x = -1$.
    Injectons dans $\mathcal{D}_2$ : $-1 + 2y - 2 = 0 \iff 2y = 3 \iff y = 1{,}5$.
    Intersection : $I(-1\,; 1{,}5)$.
16. Pente de $(AB)$ : $m = \frac{7 - 1}{3 - 1} = \frac{6}{2} = 3$.
    Droite $kx + 2y - 5 = 0 \iff 2y = -kx + 5 \iff y = -\frac{k}{2}x + \frac{5}{2}$.
    Sa pente est $-\frac{k}{2}$.
    Parallélisme $\iff -\frac{k}{2} = 3 \iff k = -6$.
17. La médiane issue de $A$ passe par $A(0\,; 4)$ et par le milieu $A'$ de $[BC]$.
    $x_{A'} = \frac{-2 + 4}{2} = 1$ et $y_{A'} = \frac{0 + 0}{2} = 0$, donc $A'(1\,; 0)$.
    Pente $m = \frac{0 - 4}{1 - 0} = -4$. Ordonnée à l'origine (donnée par $A(0\,; 4)$) : $p = 4$.
    Équation : $y = -4x + 4$.
18. Pas de solution unique si le déterminant est nul :
    $m(m - 1) - 2 \times 3 = 0 \iff m^2 - m - 6 = 0$.
    Factorisation : $(m - 3)(m + 2) = 0 \implies m = 3$ ou $m = -2$.
19. a) Le côté $[BC]$ est porté par l'axe des abscisses ($y = 0$). La hauteur issue de $A$ est donc perpendiculaire à l'axe des abscisses : c'est une droite verticale passant par $A(0\,; 3)$, d'équation $x = 0$.
    b) Le vecteur $\vec{AC}\begin{pmatrix} 4 - 0 \\ 0 - 3 \end{pmatrix} = \begin{pmatrix} 4 \\ -3 \end{pmatrix}$.
    Une droite perpendiculaire à $(AC)$ admet $\vec{AC}$ comme vecteur normal, ce qui signifie que son vecteur directeur est $\vec{u}\begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
    Pente de cette hauteur : $m = \frac{4}{3}$.
    Elle passe par $B(-2\,; 0)$ : $y - 0 = \frac{4}{3}(x - (-2)) \implies y = \frac{4}{3}x + \frac{8}{3}$.
    c) L'orthocentre $H$ est l'intersection des deux hauteurs.
    Comme la première hauteur est $x = 0$, on remplace $x = 0$ dans la seconde : $y = \frac{8}{3}$.
    Donc $H\left(0\,; \frac{8}{3}\right)$.
20. a) Vecteur directeur de $\mathcal{D} : 2x - y + 1 = 0$ est $\vec{u}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ (pente $m = 2$).
    La perpendiculaire $\Delta$ a une pente $m' = -\frac{1}{m} = -\frac{1}{2}$.
    Son équation est $y - 4 = -\frac{1}{2}(x - 4) \iff y = -\frac{1}{2}x + 2 + 4 = -\frac{1}{2}x + 6 \iff x + 2y - 12 = 0$.
    b) Intersection de $\mathcal{D}$ et $\Delta$ :
    De $\mathcal{D}$, $y = 2x + 1$. Dans $\Delta$ : $x + 2(2x + 1) - 12 = 0 \iff 5x - 10 = 0 \iff x = 2$.
    Alors $y = 2(2) + 1 = 5$. Le projeté est $H(2\,; 5)$.
    c) $AH = \sqrt{(2 - 4)^2 + (5 - 4)^2} = \sqrt{(-2)^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}$.
21. Trouvons l'intersection $K$ de $\mathcal{D}_1$ et $\mathcal{D}_2$ :
    $\begin{cases} 2x - y = 1 \\ x + y = 5 \end{cases}$
    Somme : $3x = 6 \implies x = 2$. Alors $y = 5 - 2 = 3$. Donc $K(2\,; 3)$.
    Pour que $\mathcal{D}_3$ passe aussi par $K$ :
    $3(2) + k(3) - 7 = 0 \iff 6 + 3k - 7 = 0 \iff 3k = 1 \iff k = \frac{1}{3}$.
22. a) La droite d'offre a une pente positive $2$, la droite de demande a une pente négative $-3$.
    b) À l'équilibre, $q_O = q_D \iff 2p - 4 = -3p + 21 \iff 5p = 25 \iff p_E = 5\text{ €/kg}$.
    c) Quantité échangée : $q_E = 2(5) - 4 = 10 - 4 = 6\text{ tonnes}$ (ou $q_E = -3(5) + 21 = 6\text{ tonnes}$).

---

### La question qui ouvre la suite

Une droite représente le cas le plus docile et le plus simple des mathématiques : une relation où chaque pas en avant produit toujours le même gain régulier. C'est le monde des fonctions affines $x \mapsto mx + p$.

Mais que se passe-t-il lorsque la règle de la machine devient plus complexe ? Quand la machine élève au carré, inverse les nombres ou en extrait la racine ? Comment cartographier les reliefs, les vallées et les sommets des courbes non rectilignes ? C'est ce que nous allons explorer dans **Le Métier Jacquard et la Boîte à Fabriquer**.
