# VOLUME VI — L'Âge du Flux et de la Vitesse (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 50 : Le Tonneau Rempli de Tranches d'Eau

> *« Si la dérivée est le scalpel qui découpe le temps en instants minuscules pour en extraire la vitesse, l'intégrale est l'aiguille d'or qui recoud toutes les miettes ensemble pour reconstituer le grand voyage de l'espace. Rien ne se perd, tout se cumule dans la mémoire de la courbe. »*

---

### Ce que tu vas découvrir

- Comment l'astronome **Johannes Kepler**, scandalisé par un marchand de vin lors de son propre mariage en 1615, a inventé la méthode des tranches infiniment fines pour mesurer des volumes courbes.
- La notion **d'intégrale définie** $\int_a^b f(t)\,dt$ : des sommes de rectangles de Riemann à l'aire exacte sous une courbe.
- L'origine et la signification du grand symbole étiré $\int$ inventé par Leibniz en 1675.
- Le **Théorème Fondamental de l'Analyse** et sa démonstration rigoureuse : pourquoi et comment l'intégration est **l'opération inverse** exacte de la dérivation.
- La recherche des **primitives** : tableau des formes usuelles et maîtrise des composées ($u'u^n$, $\dfrac{u'}{u}$, $u'e^u$, etc.).
- Les propriétés indispensables de l'intégrale : **linéarité**, **relation de Chasles**, **positivité**, **aire entre deux courbes** et **valeur moyenne**.
- La technique reine du calcul intégral : **l'intégration par parties** (IPP), issue de la règle du produit de dérivation.
- L'implémentation numérique en **Python** de la méthode des rectangles.

---

### 1. Le problème : Kepler, le marchand de vin et la jauge truquée

#### 1.1 Le mariage de Linz (1615)

À l'automne **1615**, dans la ville de Linz au bord du Danube, le célèbre astronome **Johannes Kepler** — l'homme qui a percé les lois du mouvement des planètes autour du Soleil — prépare le banquet de son second mariage. Pour régaler ses invités, il achète plusieurs gros tonneaux de vin d'Autriche.

Lorsque le marchand livre les fûts au ventre rebondi, il sort de sa poche une simple tige de fer graduée appelée une **jauge**. Il plonge la tige en biais par la bonde (l'ouverture située au sommet du renflement du tonneau) jusqu'au fond de la douve la plus éloignée, retire la baguette mouillée, lit la graduation et annonce la contenance en litres et le prix à payer.

Kepler est stupéfait :
> *« Comment peux-tu mesurer le volume d'un corps aux parois renflées avec une simple ligne droite en diagonale ? Si le tonneau a des flancs très bombés ou des flancs presque cylindriques, ta baguette plonge à la même profondeur, mais le volume de vin n'est pas du tout le même ! Tu vends de l'air ou tu me voles ! »*

Le marchand hausse les épaules : les négociants ont toujours fait ainsi. Kepler s'enferme alors dans son cabinet d'étude. Pendant des semaines, il suspend ses calculs astronomiques pour résoudre l'énigme des fûts.

Sa trouvaille, publiée dans son traité *Nova Stereometria Doliorum Vinariorum* (« Nouvelle stéréométrie des tonneaux de vin », 1615), est d'une simplicité éblouissante :
Pour mesurer un volume aux parois courbes, **il faut le découper par la pensée en une multitude de rondelles plates infiniment fines**, calculer le volume de chaque rondelle (qui est presque un cylindre plat parfait), puis **additionner toutes ces rondelles** du fond jusqu'au sommet !

```
                 Tonneau découpé en tranches fines :
         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
        (    │   │   │   │   │   │   │   │    )
       (     │   │   │   │   │   │   │   │     )  Chaque tranche est un disque
      (      │   │   │   │   │   │   │   │      ) d'épaisseur infime dt
       (     │   │   │   │   │   │   │   │     )
        (    │   │   │   │   │   │   │   │    )
         └───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

#### 1.2 Le compteur de vitesse et l'odomètre brisé

Revenons à une situation de notre temps.
Imagine que tu conduises une voiture dans le désert. Ton compteur kilométrique (l'odomètre) est cassé : il affiche $0\text{ km}$ en permanence. En revanche, ton compteur de vitesse fonctionne parfaitement et un enregistreur trace en continu la courbe de ta vitesse $v(t)$ en kilomètres par heure au fil du temps $t$.

Comment retrouver la distance exacte parcourue entre le départ à $t = a$ et l'arrivée à $t = b$ ?

1. **Cas d'une vitesse constante :** Si tu roules à une vitesse constante de $90\text{ km/h}$ pendant $2\text{ heures}$, la distance est :
   $$\text{Distance} = \text{Vitesse} \times \text{Durée} = 90 \times 2 = 180\text{ kilomètres}.$$
   Graphiquement, dans un repère où le temps est en abscisse et la vitesse en ordonnée, cette distance est **l'aire du rectangle** de base $[0\,; 2]$ et de hauteur $90$ !

```
   Vitesse v(t)
       ▲
    90 ┼─────────────────────────┐
       │                         │   Aire du rectangle
       │   Distance = 90 × 2     │   = 180 km
       │        = 180            │
     0 └─────────────────────────┴──────► Temps t
       0                         2h
```

2. **Cas d'une vitesse variable :** Dans la réalité, la vitesse varie constamment : accélérations, ralentissements, arrêts. La courbe $v(t)$ ondule.
   Pour calculer la distance, découpons le temps en minuscules intervalles de durée $\Delta t$. Pendant une fraction de seconde $\Delta t$, la vitesse $v(t)$ n'a quasiment pas le temps de changer : elle est presque constante.
   La petite distance franchie pendant cet intervalle est donc l'aire d'un rectangle minuscule de largeur $\Delta t$ et de hauteur $v(t)$ :
   $$\Delta d \approx v(t) \times \Delta t.$$
   La distance totale est la somme de tous ces millions de petits rectangles. Et quand la largeur $\Delta t$ devient infinitésimale (on la note alors $dt$), la somme des aires des rectangles devient **l'aire exacte sous la courbe de la vitesse** !

---

### 2. De la somme de rectangles à l'intégrale définie

#### 2.1 Les sommes de Riemann

Soit $f$ une fonction continue et positive sur un intervalle $[a\,; b]$ (avec $a < b$).
On souhaite mesurer l'aire du domaine délimité par :
- la courbe représentative $\mathcal{C}_f$ ;
- l'axe des abscisses ;
- les droites verticales d'équations $x = a$ et $x = b$.

Ce domaine est appelé le **trapèze curviligne** ou le domaine sous la courbe.

```
       y ▲                    Courbe y = f(t)
         │                     ..---*---..
         │                   / | | | | | | \
         │                 /   | | | | | |   \   Chaque bande a
         │               /     | | | | | |     \ une largeur Δt
         │             /       | | | | | |       \ et une hauteur f(t)
       0 └────────────┴────────┴─┴─┴─┴─┴─┴────────┴──────► t
                      a                           b
```

Pour approcher cette aire, découpons le segment $[a\,; b]$ en $n$ sous-intervalles égaux de largeur $\Delta x = \dfrac{b - a}{n}$ à l'aide des points de subdivision :
$$x_k = a + k \dfrac{b - a}{n} \quad (k = 0, 1, 2, \dots, n).$$

Sur chaque sous-intervalle $[x_k\,; x_{k+1}]$, on construit un rectangle de hauteur $f(x_k)$ (méthode des rectangles à gauche).
La somme des aires de ces $n$ rectangles forme la **somme de Riemann à gauche** :
$$S_n = \sum_{k=0}^{n-1} f(x_k) \times \Delta x = \sum_{k=0}^{n-1} f\left(a + k\dfrac{b-a}{n}\right) \dfrac{b-a}{n}.$$

Lorsque le nombre de rectangles $n$ tend vers l'infini ($n \to +\infty$), la largeur de chaque tranche devient infiniment mince ($\Delta x \to 0$), les escaliers épousent la courbe sans laisser le moindre interstice, et la somme $S_n$ converge vers un nombre réel unique : **l'intégrale de $f$ de $a$ à $b$**.

#### 2.2 La notation de Leibniz : $\int_a^b f(t)\,dt$

> **🔍 L'histoire vraie — Le 29 octobre 1675 à Paris :**
> C'est le philosophe et mathématicien **Gottfried Wilhelm Leibniz** qui introduit pour la première fois le symbole $\int$.
> Leibniz se demande : *« Que faisons-nous ? Nous calculons une Somme d'une infinité de tranches infiniment minces. »*
> Il prend alors l'initiale du mot latin **Summa** (la somme) : la lettre **S**.
> Avec sa plume d'oie, il l'étire vers le haut et vers le bas pour lui donner la grâce d'un S élancé : $\int$.
> Et pour désigner la largeur infiniment petite d'une tranche, il note $dt$ (la différentielle de $t$).

Quand tu lis la formule :
$$\int_a^b f(t) \, dt$$
voici ce qu'elle te dit en langage parlé :
- $\int$ : « Fais la somme continue… »
- des bornes $a$ (point de départ) à $b$ (point d'arrivée) ;
- des rectangles de hauteur $f(t)$ ;
- et de largeur infinitésimale $dt$.

> **Remarque sur la variable muette :**
> La lettre $t$ sous le symbole intégrale est une **variable muette** : elle ne sert qu'à parcourir l'intervalle entre $a$ et $b$. On peut la remplacer par n'importe quelle autre lettre sans changer la valeur du résultat :
> $$\int_a^b f(t)\,dt = \int_a^b f(x)\,dx = \int_a^b f(u)\,du.$$

#### 2.3 Algorithme Python : la méthode des rectangles

Voici le script Python officiel permettant d'approcher l'intégrale d'une fonction continue par la méthode des rectangles :

```python
def integrale_rectangles(f, a, b, n):
    """
    Calcule une approximation de l'intégrale de f entre a et b
    par la méthode des rectangles au point médian.
    """
    largeur = (b - a) / n
    somme = 0.0
    for k in range(n):
        # Point milieu du k-ième sous-intervalle
        x_milieu = a + (k + 0.5) * largeur
        somme += f(x_milieu)
    return somme * largeur

# Testons sur f(x) = x^2 entre 0 et 3 (l'aire exacte vaut 9)
def carre(x):
    return x**2

print("Approximation avec 10 rectangles   :", integrale_rectangles(carre, 0, 3, 10))
print("Approximation avec 100 rectangles  :", integrale_rectangles(carre, 0, 3, 100))
print("Approximation avec 1000 rectangles :", integrale_rectangles(carre, 0, 3, 1000))
# Avec 1000 rectangles, on obtient 8.9999988... soit quasiment 9 !
```

---

### 3. Le Théorème Fondamental de l'Analyse : le pont miraculeux

Calculer des sommes de millions de rectangles à la main serait un calvaire infini. C'est ici qu'intervient le plus grand chef-d'œuvre de l'histoire des mathématiques, découvert indépendamment par **Isaac Newton** et **Gottfried Wilhelm Leibniz** entre 1666 et 1675.

#### 3.1 La fonction d'accumulation d'aire

Soit $f$ une fonction continue et positive sur un intervalle $[a\,; b]$.
Fixons la borne inférieure $a$ et laissons la borne supérieure varier comme une variable libre $x \in [a\,; b]$.
Définissons la fonction $A$, dite **fonction d'accumulation** :
$$A(x) = \int_a^x f(t) \, dt.$$

$A(x)$ représente **l'aire balayée sous la courbe entre $a$ et $x$**.
Que vaut le taux de variation de cette aire lorsque la borne supérieure avance d'un tout petit pas $h > 0$ ?

```
       y ▲                        y = f(t)
         │                        ..---*---..
         │                      /      |   | \
         │                    /        | h |   \   Tranche ajoutée de largeur h :
         │                  /          |   |     \ son aire est A(x+h) - A(x) ≈ f(x) × h !
         │                /   Aire     |   |       \
       0 └───────────────┴──── A(x) ───┴───┴────────┴──────► t
                         a             x  x+h        b
```

Quand on passe de $x$ à $x+h$, l'aire augmente de la fine tranche comprise entre $x$ et $x+h$ :
$$\Delta A = A(x+h) - A(x) = \int_x^{x+h} f(t) \, dt.$$
Cette tranche a une largeur $h$ et sa hauteur est quasiment constante, égale à $f(x)$ (car $f$ est continue).
Son aire est donc approximativement :
$$A(x+h) - A(x) \approx f(x) \times h \iff \dfrac{A(x+h) - A(x)}{h} \approx f(x).$$
Quand $h$ tend vers 0, le taux de variation de l'aire devient **exactement la hauteur de la courbe $f(x)$** !

> **La dérivée de la fonction aire est la fonction de départ :**
> $$A'(x) = f(x).$$

#### 3.2 Démonstration rigoureuse du Théorème Fondamental

> **📐 Théorème Fondamental de l'Analyse (exigible) —**
> Soit $f$ une fonction continue sur un intervalle $I$ et soit $a \in I$.
> La fonction $A$ définie sur $I$ par :
> $$A(x) = \int_a^x f(t) \, dt$$
> est dérivable sur $I$, et pour tout $x \in I$ :
> $$A'(x) = f(x).$$

> **✍️ Démonstration —**
> Soit $x \in I$ et soit $h > 0$ tel que $x + h \in I$.
> D'après la relation de Chasles pour l'intégrale :
> $$A(x+h) - A(x) = \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt = \int_x^{x+h} f(t)\,dt.$$
> Puisque $f$ est continue sur l'intervalle fermé $[x\,; x+h]$, le théorème des bornes atteintes garantit que $f$ admet un minimum $m_h$ et un maximum $M_h$ sur $[x\,; x+h]$ :
> $$\text{Pour tout } t \in [x\,; x+h] : \quad m_h \leq f(t) \leq M_h.$$
> En intégrant cet encadrement sur $[x\,; x+h]$ de longueur $h$ :
> $$\int_x^{x+h} m_h \, dt \leq \int_x^{x+h} f(t) \, dt \leq \int_x^{x+h} M_h \, dt \iff m_h \times h \leq A(x+h) - A(x) \leq M_h \times h.$$
> En divisant par $h > 0$ :
> $$m_h \leq \dfrac{A(x+h) - A(x)}{h} \leq M_h.$$
> Or, comme la fonction $f$ est continue en $x$, lorsque $h \to 0^+$, l'intervalle $[x\,; x+h]$ se rétracte sur le point $x$.
> Le minimum $m_h$ et le maximum $M_h$ convergent tous deux vers $f(x)$ :
> $$\lim_{h \to 0^+} m_h = f(x) \quad \text{et} \quad \lim_{h \to 0^+} M_h = f(x).$$
> D'après le **théorème des gendarmes** :
> $$\lim_{h \to 0^+} \dfrac{A(x+h) - A(x)}{h} = f(x).$$
> Un raisonnement parfaitement identique pour $h < 0$ donne $\lim\limits_{h \to 0^-} \dfrac{A(x+h) - A(x)}{h} = f(x)$.
> On conclut que $A$ est dérivable en $x$ et que $A'(x) = f(x)$. $\blacksquare$

---

### 4. Primitives et calcul effectif des intégrales

#### 4.1 Qu'est-ce qu'une primitive ?

> **📐 Définition —**
> Soit $f$ une fonction continue sur un intervalle $I$.
> On appelle **primitive** de $f$ sur $I$ toute fonction $F$ dérivable sur $I$ telle que :
> $$\text{Pour tout } x \in I : \quad F'(x) = f(x).$$

> **Propriété fondamentale des primitives —**
> Si $F$ est une primitive de $f$ sur un intervalle $I$, alors :
> 1. Pour toute constante réelle $C$, la fonction $x \mapsto F(x) + C$ est aussi une primitive de $f$ (car la dérivée d'une constante est nulle : $(F+C)' = F' + 0 = f$).
> 2. Réciproquement, toute autre primitive $G$ de $f$ sur $I$ ne diffère de $F$ que d'une constante : il existe $C \in \mathbb{R}$ tel que $G(x) = F(x) + C$.
> 3. Pour tout point $(x_0\,; y_0)$ avec $x_0 \in I$, il existe **une unique** primitive de $f$ prenant la valeur $y_0$ en $x_0$.

#### 4.2 La formule d'évaluation de l'intégrale

Grâce au théorème fondamental, le calcul d'une intégrale ne demande aucun rectangle :

> **📐 Théorème (Calcul de l'intégrale par une primitive) —**
> Soit $f$ une fonction continue sur $[a\,; b]$, et soit $F$ une primitive quelconque de $f$ sur $[a\,; b]$. Alors :
> $$\int_a^b f(t) \, dt = [F(t)]_a^b = F(b) - F(a).$$

> **✍️ Démonstration —**
> Posons $A(x) = \int_a^x f(t)\,dt$. D'après le théorème fondamental, $A$ est une primitive de $f$ sur $[a\,; b]$.
> Comme $F$ est une autre primitive de $f$, il existe une constante $C \in \mathbb{R}$ telle que pour tout $x \in [a\,; b]$ :
> $$A(x) = F(x) + C.$$
> Déterminons la valeur de $C$ en évaluant en $x = a$ :
> $$A(a) = \int_a^a f(t)\,dt = 0 \implies F(a) + C = 0 \iff C = -F(a).$$
> Ainsi pour tout $x \in [a\,; b]$ :
> $$A(x) = F(x) - F(a).$$
> En prenant $x = b$, on obtient immédiatement :
> $$\int_a^b f(t)\,dt = A(b) = F(b) - F(a).$$
> Remarquons que si l'on avait choisi une autre primitive $G(x) = F(x) + K$, la constante $K$ s'éliminerait par soustraction :
> $$G(b) - G(a) = (F(b) + K) - (F(a) + K) = F(b) - F(a).$$
> Le résultat ne dépend donc absolument pas de la constante choisie ! $\blacksquare$

#### 4.3 Tableau des primitives usuelles

Ce tableau est le miroir exact du tableau des dérivées, lu à l'envers :

| Fonction $f(x)$ | Une primitive $F(x)$ | Intervalle de validité |
|---|---|---|
| $0$ | $k$ (constante) | $\mathbb{R}$ |
| $a$ (constante) | $ax$ | $\mathbb{R}$ |
| $x$ | $\dfrac{x^2}{2}$ | $\mathbb{R}$ |
| $x^n \quad (n \in \mathbb{N})$ | $\dfrac{x^{n+1}}{n+1}$ | $\mathbb{R}$ |
| $x^\alpha \quad (\alpha \in \mathbb{R}, \alpha \neq -1)$ | $\dfrac{x^{\alpha+1}}{\alpha+1}$ | $]0\,; +\infty[$ |
| $\dfrac{1}{x^2} = x^{-2}$ | $-\dfrac{1}{x}$ | $]-\infty\,; 0[$ ou $]0\,; +\infty[$ |
| $\dfrac{1}{\sqrt{x}} = x^{-1/2}$ | $2\sqrt{x}$ | $]0\,; +\infty[$ |
| $\dfrac{1}{x}$ | $\ln|x|$ | $]-\infty\,; 0[$ ou $]0\,; +\infty[$ |
| $e^x$ | $e^x$ | $\mathbb{R}$ |
| $e^{kx} \quad (k \neq 0)$ | $\dfrac{1}{k} e^{kx}$ | $\mathbb{R}$ |
| $\cos x$ | $\sin x$ | $\mathbb{R}$ |
| $\sin x$ | $-\cos x$ | $\mathbb{R}$ |

#### 4.4 Primitives de fonctions composées

Reconnaître une dérivée de fonction composée est la compétence centrale du calcul intégral :

| Forme de la fonction | Une primitive | Condition sur $u$ |
|---|---|---|
| $u'(x) \times \big(u(x)\big)^n \quad (n \in \mathbb{Z}, n \neq -1)$ | $\dfrac{\big(u(x)\big)^{n+1}}{n+1}$ | Si $n < -1$, $u(x) \neq 0$ |
| $\dfrac{u'(x)}{u(x)}$ | $\ln|u(x)|$ | $u(x) \neq 0$ |
| $u'(x) \, e^{u(x)}$ | $e^{u(x)}$ | Aucune |
| $\dfrac{u'(x)}{\sqrt{u(x)}}$ | $2\sqrt{u(x)}$ | $u(x) > 0$ |
| $u'(x) \cos(u(x))$ | $\sin(u(x))$ | Aucune |
| $u'(x) \sin(u(x))$ | $-\cos(u(x))$ | Aucune |

> **Exemple résolu 1 — Primitives directes.**
> 1. $f_1(x) = 3x^4 - 2x^2 + 5 \implies F_1(x) = 3\left(\dfrac{x^5}{5}\right) - 2\left(\dfrac{x^3}{3}\right) + 5x = \dfrac{3}{5}x^5 - \dfrac{2}{3}x^3 + 5x$.
> 2. $f_2(x) = \dfrac{3}{x} + e^{-2x}$ sur $]0\,;+\infty[ \implies F_2(x) = 3\ln x - \dfrac{1}{2}e^{-2x}$.

> **Exemple résolu 2 — Reconnaissance de formes composées.**
> 1. $f(x) = (2x + 1)(x^2 + x + 4)^3$.
>    Posons $u(x) = x^2 + x + 4$. Alors $u'(x) = 2x + 1$.
>    L'expression est exactement de la forme $u' u^3$.
>    Une primitive est donc :
>    $$F(x) = \dfrac{u^4}{4} = \dfrac{(x^2 + x + 4)^4}{4}.$$
>
> 2. $g(x) = \dfrac{2x}{x^2 + 3}$.
>    Posons $u(x) = x^2 + 3$. Alors $u'(x) = 2x$.
>    C'est de la forme $\dfrac{u'}{u}$ avec $u(x) > 0$.
>    Une primitive est $G(x) = \ln(x^2 + 3)$.
>
> 3. $h(x) = \dfrac{x}{x^2 + 1}$.
>    Remarquons que la dérivée de $x^2 + 1$ est $2x$, or nous n'avons que $x$.
>    On force le coefficient 2 en multipliant et divisant par 2 :
>    $$h(x) = \dfrac{1}{2} \times \dfrac{2x}{x^2 + 1} = \dfrac{1}{2} \dfrac{u'}{u} \implies H(x) = \dfrac{1}{2} \ln(x^2 + 1).$$
>
> 4. $k(x) = x e^{-x^2}$.
>    La dérivée de $-x^2$ est $-2x$. Écrivons :
>    $$k(x) = -\dfrac{1}{2} \times (-2x) e^{-x^2} = -\dfrac{1}{2} u' e^u \implies K(x) = -\dfrac{1}{2} e^{-x^2}.$$

---

### 5. Propriétés algébriques de l'intégrale

Ces propriétés sont valables pour toutes fonctions continues sur l'intervalle considéré.

#### 5.1 Linéarité

> **📐 Propriété de linéarité —** Pour tous réels $\alpha, \beta$ et fonctions continues $f, g$ :
> $$\int_a^b \big(\alpha f(t) + \beta g(t)\big) \, dt = \alpha \int_a^b f(t) \, dt + \beta \int_a^b g(t) \, dt.$$

#### 5.2 Relation de Chasles

> **📐 Relation de Chasles —** Pour tous réels $a, b, c$ d'un intervalle où $f$ est continue :
> $$\int_a^c f(t) \, dt + \int_c^b f(t) \, dt = \int_a^b f(t) \, dt.$$
> En particulier :
> - $\int_a^a f(t) \, dt = 0$ (un segment sans largeur a une aire nulle) ;
> - $\int_b^a f(t) \, dt = -\int_a^b f(t) \, dt$ (inverser les bornes change le signe).

#### 5.3 Positivité et conservation de l'ordre

> **📐 Positivité —** Soient $a \leq b$ deux réels.
> - Si pour tout $t \in [a\,; b]$, $f(t) \geq 0$, alors $\int_a^b f(t) \, dt \geq 0$.
> - Si pour tout $t \in [a\,; b]$, $f(t) \leq g(t)$, alors $\int_a^b f(t) \, dt \leq \int_a^b g(t) \, dt$.
> - Inégalité triangulaire : $\left| \int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)| \, dt$.

> **⚠️ Attention, piège ! — L'ordre des bornes compte !**
> La propriété « $f \geq 0 \implies \int_a^b f(t)\,dt \geq 0$ » exige impérativement que **$a \leq b$**.
> Si les bornes sont à l'envers ($a > b$), l'intégrale d'une fonction positive est **négative** !

#### 5.4 Aire entre deux courbes

Soient $f$ et $g$ deux fonctions continues sur $[a\,; b]$ telles que pour tout $x \in [a\,; b]$, **$f(x) \geq g(x)$** (la courbe de $f$ est située au-dessus de celle de $g$).
L'aire $\mathcal{A}$ de la surface délimitée par les deux courbes entre les droites $x = a$ et $x = b$ est égale à l'aire sous $f$ diminuée de l'aire sous $g$ :

$$\mathcal{A} = \int_a^b \big(f(x) - g(x)\big) \, dx.$$

```
       y ▲               ..---*---.. y = f(x) (au-dessus)
         │             / : : : : : : \
         │           / : : Aire  : : : \
         │          ( : : :  A  : : : : )
         │           \ : : : : : : : : /
         │             '--.......---'   y = g(x) (en dessous)
       0 └───────────┴─────────────────┴──────► x
                     a                 b
```

#### 5.5 Valeur moyenne d'une fonction

Comment définir la température moyenne de la journée si la température $T(t)$ varie continûment d'heure en heure ? On ne peut pas additionner une infinité de températures pour diviser par l'infini !
On utilise la **valeur moyenne intégrale** :

> **📐 Définition — Valeur moyenne :**
> Soit $f$ une fonction continue sur $[a\,; b]$ avec $a < b$.
> La **valeur moyenne** de $f$ sur $[a\,; b]$, notée $\mu$ (ou $\overline{f}$), est le nombre réel :
> $$\mu = \dfrac{1}{b - a} \int_a^b f(t) \, dt.$$

**Interprétation géométrique :** $\mu$ est la hauteur d'un rectangle de même base $[a\,; b]$ qui aurait **exactement la même aire** que le domaine sous la courbe ondulée de $f$ :
$$\text{Aire}(f) = \mu \times (b - a).$$

---

### 6. L'Intégration par Parties (IPP) : la technique maîtresse

Quand une fonction à intégrer est un produit de deux fonctions (par exemple $x e^x$ ou $x \cos x$), et qu'elle n'est pas de la forme $u' e^u$, aucune formule de primitive directe ne s'applique.
On utilise alors **l'intégration par parties**, qui est la transposition intégrale de la dérivée d'un produit.

#### 6.1 Théorème et démonstration

> **📐 Théorème d'Intégration par Parties (exigible) —**
> Soient $u$ et $v$ deux fonctions dérivables sur $[a\,; b]$, telles que leurs dérivées $u'$ et $v'$ soient continues sur $[a\,; b]$. Alors :
> $$\int_a^b u'(t) v(t) \, dt = \Big[ u(t) v(t) \Big]_a^b - \int_a^b u(t) v'(t) \, dt.$$

> **✍️ Démonstration —**
> D'après la formule de dérivation d'un produit, pour tout $t \in [a\,; b]$ :
> $$(uv)'(t) = u'(t) v(t) + u(t) v'(t).$$
> En isolant le terme $u'(t) v(t)$ :
> $$u'(t) v(t) = (uv)'(t) - u(t) v'(t).$$
> Intégrons cette égalité entre $a$ et $b$ à l'aide de la linéarité :
> $$\int_a^b u'(t) v(t) \, dt = \int_a^b (uv)'(t) \, dt - \int_a^b u(t) v'(t) \, dt.$$
> Or, une primitive de $(uv)'$ est tout simplement le produit $uv$ !
> D'où :
> $$\int_a^b (uv)'(t) \, dt = \Big[ u(t) v(t) \Big]_a^b = u(b)v(b) - u(a)v(a).$$
> En remplaçant, on obtient exactement la formule :
> $$\int_a^b u'(t) v(t) \, dt = \Big[ u(t) v(t) \Big]_a^b - \int_a^b u(t) v'(t) \, dt.$$
> $\blacksquare$

#### 6.2 Stratégie : qui choisir pour $u'$ et qui pour $v$ ?

Le but d'une intégration par parties est de remplacer le calcul d'une intégrale difficile par celui d'une intégrale **plus simple**.
Pour cela, on choisit en général pour **$v(t)$** la fonction qui **se simplifie par dérivation** (les polynômes perdent un degré en étant dérivés !).

> **🧭 La règle heuristique ALPES pour le choix de $v(x)$ (celle que l'on dérive) :**
> On choisit comme fonction $v(x)$ la première fonction rencontrée dans l'ordre de cette liste :
> 1. **A** : Fonctions circulaires réciproques (Arcsin, Arccos, Arctan)
> 2. **L** : **Logarithmes** ($\ln x$)
> 3. **P** : **Polynômes** ($x, x^2, x^3, \dots$)
> 4. **E** : **Exponentielles** ($e^x, e^{2x}, \dots$)
> 5. **S** : **Sinus / Cosinus** ($\sin x, \cos x$)

> **Exemple résolu 3 — Calcul de $\int_0^1 x e^x \, dx$.**
> On a un produit d'un polynôme $x$ et d'une exponentielle $e^x$.
> D'après la règle ALPES, le polynôme $x$ vient avant l'exponentielle, donc on pose :
> - $v(x) = x \implies v'(x) = 1$ (le degré baisse !)
> - $u'(x) = e^x \implies u(x) = e^x$
>
> Les fonctions $u$ et $v$ sont dérivables et leurs dérivées sont continues sur $[0\,; 1]$.
> Par intégration par parties :
> $$\int_0^1 x e^x \, dx = \Big[ x e^x \Big]_0^1 - \int_0^1 1 \times e^x \, dx.$$
> Calculons le crochet : $[x e^x]_0^1 = 1 e^1 - 0 e^0 = e$.
> L'intégrale restante est immédiate : $\int_0^1 e^x \, dx = [e^x]_0^1 = e^1 - e^0 = e - 1$.
> Donc :
> $$\int_0^1 x e^x \, dx = e - (e - 1) = \mathbf{1}.$$

> **Exemple résolu 4 — L'astuce géniale pour intégrer $\ln x$.**
> Quelle est une primitive de la fonction $\ln x$ sur $]0\,; +\infty[$ ?
> On ne voit pas de produit ? Qu'à cela ne tienne : écrivons $\ln x = 1 \times \ln x$ !
> Posons :
> - $v(x) = \ln x \implies v'(x) = \dfrac{1}{x}$ (le logarithme disparaît !)
> - $u'(x) = 1 \implies u(x) = x$
>
> Alors :
> $$\int \ln x \, dx = x \ln x - \int x \times \dfrac{1}{x} \, dx = x \ln x - \int 1 \, dx = x \ln x - x + C.$$
>
> > **Formule mémorable — Une primitive de $\ln x$ est :**
> > $$F(x) = x \ln x - x.$$
> Vérification immédiate par dérivation :
> $(x \ln x - x)' = 1 \times \ln x + x \times \dfrac{1}{x} - 1 = \ln x + 1 - 1 = \ln x$. Imparable ! ✔

---

### Ce qu'il faut retenir

#### 1. L'intégrale définie
- $\int_a^b f(t)\,dt$ représente l'aire algébrique délimitée par la courbe de $f$, l'axe des abscisses et les droites $x=a$ et $x=b$.
- L'unité d'aire (u.a.) est l'aire du rectangle formé par les vecteurs de base $\|\vec{i}\| \times \|\vec{j}\|$.

#### 2. Théorème fondamental de l'analyse
- Si $f$ est continue sur $I$ et $a \in I$, la fonction $A(x) = \int_a^x f(t)\,dt$ est dérivable sur $I$ et **$A'(x) = f(x)$**.
- Pour toute primitive $F$ de $f$ sur $[a\,; b]$ :
  $$\int_a^b f(t) \, dt = [F(t)]_a^b = F(b) - F(a).$$

#### 3. Tableau des primitives incontournables
- $x^n \to \dfrac{x^{n+1}}{n+1} \quad (n \neq -1)$
- $\dfrac{1}{x} \to \ln|x|$
- $e^{ax} \to \dfrac{1}{a} e^{ax}$
- $\cos(ax) \to \dfrac{1}{a} \sin(ax)$ et $\sin(ax) \to -\dfrac{1}{a} \cos(ax)$
- $u' u^n \to \dfrac{u^{n+1}}{n+1}$
- $\dfrac{u'}{u} \to \ln|u|$
- $u' e^u \to e^u$

#### 4. Propriétés clés
- Linéarité : $\int (\alpha f + \beta g) = \alpha \int f + \beta \int g$.
- Chasles : $\int_a^c f + \int_c^b f = \int_a^b f$.
- Positivité : si $a \leq b$ et $f \geq 0$, alors $\int_a^b f \geq 0$.
- Aire entre deux courbes : $\mathcal{A} = \int_a^b (f(x) - g(x))\,dx$ si $f \geq g$.
- Valeur moyenne : $\mu = \dfrac{1}{b - a} \int_a^b f(t)\,dt$.

#### 5. Intégration par parties
$$\int_a^b u' v = [uv]_a^b - \int_a^b u v'.$$

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 50.1 —** Calculs de primitives élémentaires.
Déterminer une primitive pour chacune des fonctions suivantes sur l'intervalle indiqué :
1. $f_1(x) = 4x^3 - 6x^2 + 2x - 7$ sur $\mathbb{R}$
2. $f_2(x) = \dfrac{5}{x^2} - \dfrac{2}{\sqrt{x}}$ sur $]0\,;+\infty[$
3. $f_3(x) = e^{3x} - 2e^{-x}$ sur $\mathbb{R}$
4. $f_4(x) = 3\cos(2x) + \sin(4x)$ sur $\mathbb{R}$
5. $f_5(x) = \dfrac{4}{x}$ sur $]0\,;+\infty[$

**Exercice 50.2 —** Primitive vérifiant une condition initiale.
1. Déterminer la primitive $F$ de la fonction $f(x) = 3x^2 - 4x + 1$ telle que $F(1) = 5$.
2. Déterminer la primitive $G$ de la fonction $g(x) = e^{2x}$ telle que $G(0) = 2$.

**Exercice 50.3 —** Calculs d'intégrales directes.
Calculer la valeur exacte des intégrales suivantes :
1. $I_1 = \int_1^3 (3x^2 - 2x + 1) \, dx$
2. $I_2 = \int_0^2 e^{3x} \, dx$
3. $I_3 = \int_1^e \dfrac{1}{x} \, dx$
4. $I_4 = \int_0^{\pi/2} \cos x \, dx$
5. $I_5 = \int_0^1 (2x + 1)^3 \, dx$

**Exercice 50.4 —** Reconnaissance de composées $u'u^n$ et $u'e^u$.
Calculer les intégrales suivantes :
1. $J_1 = \int_0^1 2x(x^2 + 1)^4 \, dx$
2. $J_2 = \int_0^2 3x^2 e^{x^3} \, dx$
3. $J_3 = \int_1^2 \dfrac{2x + 3}{x^2 + 3x + 1} \, dx$
4. $J_4 = \int_0^{\pi/4} \cos x \sin^3 x \, dx$

**Exercice 50.5 —** Relation de Chasles et symétrie.
Soit $f$ une fonction continue sur $[-a\,; a]$ avec $a > 0$.
1. Rappeler pourquoi $\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$ si $f$ est paire.
2. Rappeler pourquoi $\int_{-a}^a f(x)\,dx = 0$ si $f$ est impaire.
3. En déduire instantanément sans aucun calcul de primitive la valeur de :
   $$K = \int_{-2}^2 (x^7 - 3x^3 + \sin x) \, dx.$$

**Exercice 50.6 —** Valeur moyenne.
Calculer la valeur moyenne de la fonction $f(x) = x^2$ sur l'intervalle $[0\,; 3]$. Interpréter graphiquement.

**Exercice 50.7 —** Aire géométrique simple.
Calculer l'aire du domaine situé sous la parabole $y = 4 - x^2$ et au-dessus de l'axe des abscisses.

---

#### Niveau ★★ (Réflexion et Baccalauréat)

**Exercice 50.8 —** Intégration par parties simple.
Calculer par intégration par parties les intégrales suivantes :
1. $A_1 = \int_0^{\pi} x \sin x \, dx$
2. $A_2 = \int_1^e x \ln x \, dx$
3. $A_3 = \int_0^1 (2x + 1) e^{-x} \, dx$

**Exercice 50.9 —** Intégration par parties répétée.
Calculer $B = \int_0^1 x^2 e^x \, dx$ en effectuant deux intégrations par parties successives.

**Exercice 50.10 —** Aire entre deux courbes.
On considère les deux paraboles d'équations :
$$y = f(x) = -x^2 + 4x \quad \text{et} \quad y = g(x) = x^2 - 2x.$$
1. Déterminer les abscisses des points d'intersection des deux courbes.
2. Étudier la position relative des deux courbes sur l'intervalle délimité par ces intersections.
3. Calculer l'aire du domaine délimité par ces deux courbes.

**Exercice 50.11 —** Fonction définie par une intégrale.
Soit $F$ la fonction définie sur $]0\,;+\infty[$ par :
$$F(x) = \int_1^x \dfrac{e^t}{t} \, dt.$$
1. Déterminer la valeur de $F(1)$.
2. Justifier que $F$ est dérivable sur $]0\,;+\infty[$ et donner l'expression de $F'(x)$.
3. En déduire le sens de variations de $F$ sur $]0\,;+\infty[$.
4. Démontrer que pour tout $t \geq 1$, $\dfrac{e^t}{t} \geq e$. En déduire que pour tout $x \geq 1$ :
   $$F(x) \geq e(x - 1).$$
5. En déduire la limite de $F(x)$ lorsque $x \to +\infty$.

**Exercice 50.12 —** Suite d'intégrales (Type Bac).
Pour tout entier naturel $n$, on pose :
$$I_n = \int_0^1 x^n e^{-x} \, dx.$$
1. Calculer $I_0$.
2. À l'aide d'une intégration par parties, établir pour tout $n \in \mathbb{N}$ la relation de récurrence :
   $$I_{n+1} = (n + 1) I_n - \dfrac{1}{e}.$$
3. En déduire les valeurs exactes de $I_1$ et $I_2$.
4. Démontrer que pour tout $n \in \mathbb{N}$, $I_n \geq 0$.
5. Démontrer que la suite $(I_n)$ est décroissante.
6. Démontrer que pour tout $x \in [0\,; 1]$, $x^n e^{-1} \leq x^n e^{-x} \leq x^n$. En déduire un encadrement de $I_n$ et déterminer sa limite quand $n \to +\infty$.

**Exercice 50.13 —** Le tonneau de vin de Kepler revisité.
On modélise un tonneau de longueur $2L = 1\text{ mètre}$ (entre $x = -0{,}5$ et $x = 0{,}5$) par la rotation d'un arc de parabole autour de l'axe des abscisses.
Le rayon du tonneau à l'abscisse $x$ est donné par :
$$R(x) = R_0 - k x^2$$
avec $R_0 = 0{,}4\text{ m}$ (rayon au centre/à la bonde) et le rayon aux extrémités vaut $R(0{,}5) = 0{,}3\text{ m}$.
1. Déterminer la constante $k$.
2. Rappeler que le volume d'une tranche de tonneau d'épaisseur $dx$ est le volume d'un cylindre de rayon $R(x)$ : $dV = \pi [R(x)]^2 \, dx$.
3. Exprimer le volume total du tonneau sous la forme d'une intégrale :
   $$V = \int_{-0{,}5}^{0{,}5} \pi [R(x)]^2 \, dx.$$
4. Calculer la valeur exacte de ce volume en litres. Comparer avec le volume d'un cylindre de même rayon moyen.

**Exercice 50.14 —** Décomposition en éléments simples.
Soit $f(x) = \dfrac{1}{x^2 - 1}$ définie sur $]1\,;+\infty[$.
1. Trouver deux réels $a$ et $b$ tels que pour tout $x > 1$ :
   $$\dfrac{1}{x^2 - 1} = \dfrac{a}{x - 1} + \dfrac{b}{x + 1}.$$
2. En déduire une primitive de $f$ sur $]1\,;+\infty[$.
3. Calculer l'intégrale $I = \int_2^3 \dfrac{1}{x^2 - 1} \, dx$.

**Exercice 50.15 —** Encadrement d'aire et vitesse d'une fusée.
Une fusée est lancée verticalement. Son accélération est modélisée par $a(t) = \dfrac{400}{(t + 10)^2}$ pour $t \in [0\,; 30]$ (en $\text{m}\cdot\text{s}^{-2}$).
Au décollage ($t = 0$), sa vitesse initiale est $v(0) = 0$.
1. Exprimer la vitesse $v(t)$ à chaque instant en intégrant l'accélération.
2. Calculer la vitesse atteinte à $t = 30\text{ secondes}$.
3. Exprimer la hauteur $h(t)$ franchie par la fusée en intégrant la vitesse. Calculer l'altitude à $t = 30\text{ s}$.

**Exercice 50.16 —** Inégalité de Cauchy-Schwarz pour les intégrales.
Soient $f$ et $g$ deux fonctions continues sur $[a\,; b]$.
1. Pour tout réel $\lambda$, développer l'intégrale $\int_a^b \big(f(t) + \lambda g(t)\big)^2 \, dt \geq 0$.
2. En considérant le polynôme du second degré en $\lambda$ obtenu, démontrer la célèbre **inégalité de Cauchy-Schwarz** :
   $$\left( \int_a^b f(t) g(t) \, dt \right)^2 \leq \left( \int_a^b (f(t))^2 \, dt \right) \left( \int_a^b (g(t))^2 \, dt \right).$$

---

#### Niveau ★★★ (Approfondissement et Défis)

**Exercice 50.17 —** Les intégrales de Wallis.
Pour tout entier naturel $n$, on pose :
$$W_n = \int_0^{\pi/2} \sin^n x \, dx.$$
1. Calculer $W_0$ et $W_1$.
2. En écrivant $\sin^{n+1} x = \sin x \times \sin^n x$, établir par intégration par parties pour tout $n \geq 1$ :
   $$W_{n+1} = \dfrac{n}{n+1} W_{n-1}.$$
3. En déduire les expressions de $W_{2p}$ et $W_{2p+1}$ à l'aide de factorielles.
4. Démontrer que la suite $(W_n)$ est décroissante et strictement positive.
5. Établir que $\lim\limits_{n \to +\infty} \dfrac{W_{n+1}}{W_n} = 1$, et en déduire la célèbre **formule du produit infini de John Wallis (1655)** pour $\pi$ :
   $$\dfrac{\pi}{2} = \lim_{p \to +\infty} \prod_{k=1}^p \dfrac{4k^2}{4k^2 - 1} = \dfrac{2}{1} \times \dfrac{2}{3} \times \dfrac{4}{3} \times \dfrac{4}{5} \times \dfrac{6}{5} \times \dfrac{6}{7} \times \dots$$

**Exercice 50.18 —** Intégrale de Gauss et coordonnées polaires (introduction).
On pose $I = \int_0^{+\infty} e^{-x^2} \, dx$.
1. Justifier la convergence de cette intégrale par comparaison avec $e^{-x}$ pour $x \geq 1$.
2. On admet que $I^2 = \int_0^{+\infty} \int_0^{+\infty} e^{-(x^2+y^2)} \, dx \, dy$.
   En passant en coordonnées polaires ($x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$), montrer que :
   $$I^2 = \int_0^{\pi/2} d\theta \times \int_0^{+\infty} r e^{-r^2} \, dr.$$
3. Calculer exactement cette dernière intégrale et en déduire la valeur historique :
   $$\int_{-\infty}^{+\infty} e^{-x^2} \, dx = \sqrt{\pi}.$$

**Exercice 50.19 —** Formule d'Euler-Maclaurin et somme des cubes.
Soit $f$ une fonction de classe $C^1$ sur $[0\,; n]$.
1. Démontrer que $\int_0^1 (t - 1/2) f'(t) \, dt = \dfrac{f(0) + f(1)}{2} - \int_0^1 f(t) \, dt$.
2. Généraliser pour relier la somme discrète $\sum_{k=0}^n f(k)$ à l'intégrale $\int_0^n f(t)\,dt$.

**Exercice 50.20 —** Théorème de la moyenne et point intermédiaire.
Soit $f$ continue sur $[a\,; b]$. Démontrer qu'il existe $c \in \; ]a\,; b[$ tel que :
$$\int_a^b f(t) \, dt = f(c)(b - a).$$
*(C'est le Théorème de la Moyenne, équivalent du théorème des accroissements finis appliqué à la primitive).*

---

### Solutions

#### Solutions du Niveau ★

**Solution 50.1 :**
1. $F_1(x) = 4\left(\dfrac{x^4}{4}\right) - 6\left(\dfrac{x^3}{3}\right) + 2\left(\dfrac{x^2}{2}\right) - 7x = x^4 - 2x^3 + x^2 - 7x$.
2. $f_2(x) = 5x^{-2} - 2x^{-1/2} \implies F_2(x) = 5\left(-\dfrac{1}{x}\right) - 2(2\sqrt{x}) = -\dfrac{5}{x} - 4\sqrt{x}$.
3. $F_3(x) = \dfrac{1}{3}e^{3x} + 2e^{-x}$.
4. $F_4(x) = 3\left(\dfrac{1}{2}\sin(2x)\right) - \dfrac{1}{4}\cos(4x) = \dfrac{3}{2}\sin(2x) - \dfrac{1}{4}\cos(4x)$.
5. $F_5(x) = 4\ln x$.

**Solution 50.2 :**
1. Les primitives de $f$ sont $F(x) = x^3 - 2x^2 + x + C$.
   Condition : $F(1) = 1 - 2 + 1 + C = C = 5$. Donc $F(x) = x^3 - 2x^2 + x + 5$.
2. Les primitives de $g$ sont $G(x) = \dfrac{1}{2}e^{2x} + C$.
   Condition : $G(0) = \dfrac{1}{2} + C = 2 \implies C = \dfrac{3}{2}$. Donc $G(x) = \dfrac{1}{2}e^{2x} + \dfrac{3}{2}$.

**Solution 50.3 :**
1. $I_1 = [x^3 - x^2 + x]_1^3 = (27 - 9 + 3) - (1 - 1 + 1) = 21 - 1 = 20$.
2. $I_2 = \left[ \dfrac{1}{3}e^{3x} \right]_0^2 = \dfrac{1}{3}e^6 - \dfrac{1}{3}e^0 = \dfrac{e^6 - 1}{3}$.
3. $I_3 = [\ln x]_1^e = \ln e - \ln 1 = 1 - 0 = 1$.
4. $I_4 = [\sin x]_0^{\pi/2} = \sin(\pi/2) - \sin 0 = 1 - 0 = 1$.
5. Posons $u = 2x+1 \implies u' = 2$. $I_5 = \dfrac{1}{2} \int_0^1 2(2x+1)^3 \, dx = \dfrac{1}{2} \left[ \dfrac{(2x+1)^4}{4} \right]_0^1 = \dfrac{1}{8}(3^4 - 1^4) = \dfrac{81 - 1}{8} = \dfrac{80}{8} = 10$.

**Solution 50.4 :**
1. Forme $u' u^4$ avec $u(x) = x^2 + 1$ : $J_1 = \left[ \dfrac{(x^2+1)^5}{5} \right]_0^1 = \dfrac{2^5}{5} - \dfrac{1^5}{5} = \dfrac{31}{5}$.
2. Forme $u' e^u$ avec $u(x) = x^3$ : $J_2 = [e^{x^3}]_0^2 = e^{2^3} - e^0 = e^8 - 1$.
3. Forme $\dfrac{u'}{u}$ avec $u(x) = x^2 + 3x + 1 > 0$ :
   $J_3 = [\ln(x^2 + 3x + 1)]_1^2 = \ln(4 + 6 + 1) - \ln(1 + 3 + 1) = \ln 11 - \ln 5 = \ln\left(\dfrac{11}{5}\right)$.
4. Forme $u' u^3$ avec $u(x) = \sin x$ :
   $J_4 = \left[ \dfrac{\sin^4 x}{4} \right]_0^{\pi/4} = \dfrac{(\sqrt{2}/2)^4}{4} - 0 = \dfrac{1/4}{4} = \dfrac{1}{16}$.

**Solution 50.5 :**
1. $\int_{-a}^a f = \int_{-a}^0 f + \int_0^a f$. Par changement de variable $u = -x$, si $f$ est paire, $\int_{-a}^0 f(x)\,dx = \int_0^a f(u)\,du$, d'où le résultat $2\int_0^a f$.
2. Si $f$ est impaire, $\int_{-a}^0 f(x)\,dx = -\int_0^a f(u)\,du$, la somme vaut 0.
3. La fonction $x \mapsto x^7 - 3x^3 + \sin x$ est une somme de fonctions impaires, elle est donc impaire. L'intervalle $[-2\,; 2]$ étant symétrique par rapport à 0, l'intégrale est **strictement nulle : $K = 0$**.

**Solution 50.6 :**
$\mu = \dfrac{1}{3 - 0} \int_0^3 x^2 \, dx = \dfrac{1}{3} \left[ \dfrac{x^3}{3} \right]_0^3 = \dfrac{1}{3} \times \dfrac{27}{3} = \dfrac{1}{3} \times 9 = 3$.
Interprétation : le rectangle de largeur 3 et de hauteur $\mu = 3$ a une aire de $3 \times 3 = 9$, exactement égale à l'aire sous la parabole.

**Solution 50.7 :**
La parabole coupe l'axe des abscisses quand $4 - x^2 = 0 \iff x = -2$ ou $x = 2$.
Sur $[-2\,; 2]$, la fonction est positive et paire.
$\mathcal{A} = \int_{-2}^2 (4 - x^2) \, dx = 2 \int_0^2 (4 - x^2) \, dx = 2 \left[ 4x - \dfrac{x^3}{3} \right]_0^2 = 2 \left( 8 - \dfrac{8}{3} \right) = 2 \times \dfrac{16}{3} = \dfrac{32}{3} \approx 10{,}67$ u.a.

---

#### Solutions du Niveau ★★

**Solution 50.8 :**
1. $A_1 = \int_0^\pi x \sin x \, dx$.
   Posons $u'(x) = \sin x \implies u(x) = -\cos x$ et $v(x) = x \implies v'(x) = 1$.
   $A_1 = [-x \cos x]_0^\pi - \int_0^\pi (-\cos x) \times 1 \, dx = (-\pi \cos \pi - 0) + \int_0^\pi \cos x \, dx = \pi(1) + [\sin x]_0^\pi = \pi + 0 = \pi$.
2. $A_2 = \int_1^e x \ln x \, dx$.
   Posons $v(x) = \ln x \implies v'(x) = \dfrac{1}{x}$ et $u'(x) = x \implies u(x) = \dfrac{x^2}{2}$.
   $A_2 = \left[ \dfrac{x^2}{2} \ln x \right]_1^e - \int_1^e \dfrac{x^2}{2} \times \dfrac{1}{x} \, dx = \left( \dfrac{e^2}{2}(1) - 0 \right) - \dfrac{1}{2} \int_1^e x \, dx = \dfrac{e^2}{2} - \dfrac{1}{2} \left[ \dfrac{x^2}{2} \right]_1^e = \dfrac{e^2}{2} - \dfrac{e^2 - 1}{4} = \dfrac{e^2 + 1}{4}$.
3. $A_3 = \int_0^1 (2x + 1) e^{-x} \, dx$.
   Posons $v(x) = 2x+1 \implies v'(x) = 2$ et $u'(x) = e^{-x} \implies u(x) = -e^{-x}$.
   $A_3 = [-(2x+1)e^{-x}]_0^1 - \int_0^1 (-e^{-x}) \times 2 \, dx = (-3e^{-1} - (-1)) + 2 \int_0^1 e^{-x} \, dx = 1 - 3e^{-1} + 2[-e^{-x}]_0^1 = 1 - 3e^{-1} + 2(-e^{-1} + 1) = 3 - 5e^{-1} = 3 - \dfrac{5}{e}$.

**Solution 50.9 :**
Première IPP pour $B = \int_0^1 x^2 e^x \, dx$ :
$v(x) = x^2 \implies v'(x) = 2x$, $u'(x) = e^x \implies u(x) = e^x$.
$B = [x^2 e^x]_0^1 - 2 \int_0^1 x e^x \, dx = (e - 0) - 2 \int_0^1 x e^x \, dx$.
Or nous avons déjà calculé à l'exemple résolu 3 que $\int_0^1 x e^x \, dx = 1$ !
Donc $B = e - 2(1) = e - 2$.

**Solution 50.10 :**
1. $f(x) = g(x) \iff -x^2 + 4x = x^2 - 2x \iff 2x^2 - 6x = 0 \iff 2x(x - 3) = 0$.
   Les points d'intersection ont pour abscisses $x = 0$ et $x = 3$.
2. Étudions le signe de $f(x) - g(x) = 6x - 2x^2 = 2x(3 - x)$.
   Pour tout $x \in [0\,; 3]$, $2x \geq 0$ et $3 - x \geq 0$, donc $f(x) - g(x) \geq 0 \iff f(x) \geq g(x)$.
   La parabole de $f$ est située au-dessus de celle de $g$ sur $[0\,; 3]$.
3. $\mathcal{A} = \int_0^3 (f(x) - g(x)) \, dx = \int_0^3 (6x - 2x^2) \, dx = \left[ 3x^2 - \dfrac{2x^3}{3} \right]_0^3 = (3 \times 9 - \dfrac{2 \times 27}{3}) - 0 = 27 - 18 = 9$ unités d'aire.

**Solution 50.11 :**
1. $F(1) = \int_1^1 \dfrac{e^t}{t} \, dt = 0$.
2. La fonction $t \mapsto \dfrac{e^t}{t}$ est continue sur $]0\,;+\infty[$. D'après le théorème fondamental de l'analyse, $F$ est sa primitive qui s'annule en 1.
   Donc $F$ est dérivable sur $]0\,;+\infty[$ et $F'(x) = \dfrac{e^x}{x}$.
3. Pour tout $x > 0$, $e^x > 0$ et $x > 0$, donc $F'(x) > 0$. $F$ est strictement croissante sur $]0\,;+\infty[$.
4. Soit la fonction $\varphi(t) = \dfrac{e^t}{t}$ sur $[1\,; +\infty[$. $\varphi'(t) = \dfrac{e^t(t-1)}{t^2} \geq 0$ pour $t \geq 1$.
   Son minimum est en $t = 1$ et vaut $\varphi(1) = e$.
   Donc pour tout $t \geq 1$, $\dfrac{e^t}{t} \geq e$.
   En intégrant cette inégalité entre $1$ et $x$ (avec $x \geq 1$) :
   $F(x) = \int_1^x \dfrac{e^t}{t} \, dt \geq \int_1^x e \, dt = e(x - 1)$.
5. Comme $\lim\limits_{x \to +\infty} e(x - 1) = +\infty$, le théorème de comparaison donne $\lim\limits_{x \to +\infty} F(x) = +\infty$.

**Solution 50.12 :**
1. $I_0 = \int_0^1 e^{-x} \, dx = [-e^{-x}]_0^1 = -e^{-1} - (-1) = 1 - \dfrac{1}{e}$.
2. IPP sur $I_{n+1} = \int_0^1 x^{n+1} e^{-x} \, dx$ :
   $v(x) = x^{n+1} \implies v'(x) = (n+1)x^n$ et $u'(x) = e^{-x} \implies u(x) = -e^{-x}$.
   $I_{n+1} = [-x^{n+1} e^{-x}]_0^1 - \int_0^1 - (n+1)x^n e^{-x} \, dx = \left(-1 e^{-1} - 0\right) + (n+1) \int_0^1 x^n e^{-x} \, dx = -\dfrac{1}{e} + (n+1)I_n$.
3. $I_1 = 1 \times I_0 - \dfrac{1}{e} = 1 - \dfrac{1}{e} - \dfrac{1}{e} = 1 - \dfrac{2}{e}$.
   $I_2 = 2 I_1 - \dfrac{1}{e} = 2\left(1 - \dfrac{2}{e}\right) - \dfrac{1}{e} = 2 - \dfrac{5}{e}$.
4. Pour tout $x \in [0\,; 1]$, $x^n \geq 0$ et $e^{-x} > 0$, donc la fonction intégrée est positive. Les bornes étant dans l'ordre $0 \leq 1$, $I_n \geq 0$.
5. $I_{n+1} - I_n = \int_0^1 (x^{n+1} - x^n)e^{-x} \, dx = \int_0^1 x^n(x - 1)e^{-x} \, dx$.
   Pour tout $x \in [0\,; 1]$, $x - 1 \leq 0$ et les autres facteurs sont positifs, donc l'intégrande est négative. Ainsi $I_{n+1} - I_n \leq 0$ : la suite est décroissante.
6. Pour $x \in [0\,; 1]$, on a $-1 \leq -x \leq 0 \implies e^{-1} \leq e^{-x} \leq 1$.
   En multipliant par $x^n \geq 0$ : $x^n e^{-1} \leq x^n e^{-x} \leq x^n$.
   En intégrant sur $[0\,; 1]$ :
   $e^{-1} \left[ \dfrac{x^{n+1}}{n+1} \right]_0^1 \leq I_n \leq \left[ \dfrac{x^{n+1}}{n+1} \right]_0^1 \iff \dfrac{1}{e(n+1)} \leq I_n \leq \dfrac{1}{n+1}$.
   Comme $\lim\limits_{n \to +\infty} \dfrac{1}{n+1} = 0$, le théorème des gendarmes donne $\lim\limits_{n \to +\infty} I_n = 0$.

**Solution 50.13 :**
1. $R(0{,}5) = 0{,}4 - k(0{,}5)^2 = 0{,}3 \iff 0{,}4 - 0{,}25k = 0{,}3 \iff 0{,}25k = 0{,}1 \iff k = 0{,}4$.
   Donc $R(x) = 0{,}4 - 0{,}4 x^2 = 0{,}4(1 - x^2)$.
2. Chaque tranche circulaire d'épaisseur $dx$ a une surface de $\pi R(x)^2$, donc son volume est $dV = \pi R(x)^2 dx$.
3. $V = \int_{-0{,}5}^{0{,}5} \pi [R(x)]^2 \, dx$.
4. Par parité : $V = 2\pi \int_0^{0{,}5} 0{,}16(1 - x^2)^2 \, dx = 0{,}32\pi \int_0^{0{,}5} (1 - 2x^2 + x^4) \, dx$.
   Calculons la primitive : $\left[ x - \dfrac{2}{3}x^3 + \dfrac{x^5}{5} \right]_0^{0{,}5} = 0{,}5 - \dfrac{2}{3}(0{,}125) + \dfrac{0{,}03125}{5} = 0{,}5 - \dfrac{0{,}25}{3} + 0{,}00625 = 0{,}5 - 0{,}08333 + 0{,}00625 = 0{,}42292\text{ m}^3$.
   $V = 0{,}32\pi \times 0{,}42292 \approx 0{,}425\text{ m}^3 = 425\text{ litres}$.
   Un cylindre parfait de rayon intermédiaire $0{,}35\text{ m}$ aurait un volume de $\pi (0{,}35)^2 \times 1 \approx 0{,}385\text{ m}^3 = 385\text{ litres}$. Le ventre bombé du tonneau apporte donc 40 litres supplémentaires !

**Solution 50.14 :**
1. $\dfrac{a}{x-1} + \dfrac{b}{x+1} = \dfrac{a(x+1) + b(x-1)}{(x-1)(x+1)} = \dfrac{(a+b)x + (a-b)}{x^2 - 1}$.
   Par identification : $a + b = 0$ et $a - b = 1$, d'où $a = \dfrac{1}{2}$ et $b = -\dfrac{1}{2}$.
   Ainsi $\dfrac{1}{x^2 - 1} = \dfrac{1}{2(x-1)} - \dfrac{1}{2(x+1)}$.
2. Une primitive sur $]1\,;+\infty[$ est $F(x) = \dfrac{1}{2}\ln(x-1) - \dfrac{1}{2}\ln(x+1) = \dfrac{1}{2}\ln\left(\dfrac{x-1}{x+1}\right)$.
3. $I = [F(x)]_2^3 = \dfrac{1}{2}\ln\left(\dfrac{2}{4}\right) - \dfrac{1}{2}\ln\left(\dfrac{1}{3}\right) = \dfrac{1}{2}\left(\ln(1/2) - \ln(1/3)\right) = \dfrac{1}{2}\ln\left(\dfrac{3}{2}\right)$.

**Solution 50.15 :**
1. $a(t) = 400(t+10)^{-2}$. Une primitive est $-400(t+10)^{-1} = -\dfrac{400}{t+10}$.
   $v(t) = -\dfrac{400}{t+10} + C$.
   Condition initiale : $v(0) = -\dfrac{400}{10} + C = 0 \implies C = 40$.
   Donc $v(t) = 40 - \dfrac{400}{t+10}$.
2. À $t = 30\text{ s}$ : $v(30) = 40 - \dfrac{400}{40} = 40 - 10 = 30\text{ m}\cdot\text{s}^{-1}$ ($108\text{ km/h}$).
3. L'altitude est $h(t) = \int_0^t v(u)\,du = [40u - 400\ln(u+10)]_0^t = 40t - 400\ln(t+10) + 400\ln 10 = 40t - 400\ln\left(1 + \dfrac{t}{10}\right)$.
   À $t = 30\text{ s}$ : $h(30) = 40(30) - 400\ln(1 + 3) = 1200 - 400\ln 4 \approx 1200 - 400(1{,}386) \approx 1200 - 554{,}5 = 645{,}5\text{ mètres}$.

**Solution 50.16 :**
1. Développons le carré : $(f(t) + \lambda g(t))^2 = (f(t))^2 + 2\lambda f(t)g(t) + \lambda^2 (g(t))^2$.
   Par positivité de l'intégrale d'une fonction positive :
   $P(\lambda) = \lambda^2 \left(\int_a^b g^2\right) + 2\lambda \left(\int_a^b fg\right) + \left(\int_a^b f^2\right) \geq 0$.
2. Ce trinôme du second degré en $\lambda$ est toujours positif ou nul. Son discriminant réduit $\Delta'$ est donc nécessairement négatif ou nul :
   $\Delta' = \left(\int_a^b fg\right)^2 - \left(\int_a^b g^2\right)\left(\int_a^b f^2\right) \leq 0$.
   D'où $\left(\int_a^b fg\right)^2 \leq \left(\int_a^b f^2\right)\left(\int_a^b g^2\right)$.

---

#### Solutions du Niveau ★★★

**Solution 50.17 :**
1. $W_0 = \int_0^{\pi/2} 1 \, dx = \dfrac{\pi}{2}$.
   $W_1 = \int_0^{\pi/2} \sin x \, dx = [-\cos x]_0^{\pi/2} = 0 - (-1) = 1$.
2. $W_{n+1} = \int_0^{\pi/2} \sin x \times \sin^n x \, dx$.
   IPP : $u'(x) = \sin x \implies u(x) = -\cos x$, et $v(x) = \sin^n x \implies v'(x) = n \cos x \sin^{n-1} x$.
   $W_{n+1} = [-\cos x \sin^n x]_0^{\pi/2} + n \int_0^{\pi/2} \cos^2 x \sin^{n-1} x \, dx$.
   Le crochet s'annule aux deux bornes. Remplaçons $\cos^2 x$ par $1 - \sin^2 x$ :
   $W_{n+1} = n \int_0^{\pi/2} (1 - \sin^2 x)\sin^{n-1} x \, dx = n W_{n-1} - n W_{n+1}$.
   $(n+1) W_{n+1} = n W_{n-1} \iff W_{n+1} = \dfrac{n}{n+1} W_{n-1}$.
3. Par récurrence immédiate :
   $W_{2p} = \dfrac{2p-1}{2p} \times \dfrac{2p-3}{2p-2} \times \dots \times \dfrac{1}{2} \times \dfrac{\pi}{2} = \dfrac{(2p)!}{2^{2p} (p!)^2} \dfrac{\pi}{2}$.
   $W_{2p+1} = \dfrac{2p}{2p+1} \times \dfrac{2p-2}{2p-1} \times \dots \times \dfrac{2}{3} \times 1 = \dfrac{2^{2p} (p!)^2}{(2p+1)!}$.
4. Pour $x \in [0\,; \pi/2]$, $0 \leq \sin x \leq 1 \implies 0 \leq \sin^{n+1} x \leq \sin^n x$. En intégrant, $0 < W_{n+1} \leq W_n$.
5. De la décroissance, $W_{n+1} \leq W_n \leq W_{n-1}$. En divisant par $W_{n+1}$ :
   $1 \leq \dfrac{W_n}{W_{n+1}} \leq \dfrac{W_{n-1}}{W_{n+1}} = \dfrac{n+1}{n} = 1 + \dfrac{1}{n}$.
   Par les gendarmes, $\lim\limits_{n \to +\infty} \dfrac{W_{n+1}}{W_n} = 1$.
   En formant le rapport $\dfrac{W_{2p+1}}{W_{2p}}$, on obtient exactement le produit infini de Wallis tendant vers $\dfrac{2}{\pi}$.

**Solution 50.18 :**
1. Pour $x \geq 1$, $x^2 \geq x \implies -x^2 \leq -x \implies e^{-x^2} \leq e^{-x}$.
   Comme $\int_1^{+\infty} e^{-x}\,dx = e^{-1}$ est finie, l'intégrale converge.
2. Le changement de variables polaires remplace le quadrant $x \geq 0, y \geq 0$ par $\theta \in [0\,; \pi/2]$ et $r \in [0\,; +\infty[$.
3. $\int_0^{+\infty} r e^{-r^2} \, dr = \left[ -\dfrac{1}{2}e^{-r^2} \right]_0^{+\infty} = 0 - \left(-\dfrac{1}{2}\right) = \dfrac{1}{2}$.
   Ainsi $I^2 = \dfrac{\pi}{2} \times \dfrac{1}{2} = \dfrac{\pi}{4} \implies I = \dfrac{\sqrt{\pi}}{2}$.
   Par parité sur $\mathbb{R}$ : $\int_{-\infty}^{+\infty} e^{-x^2} \, dx = 2I = \sqrt{\pi}$.

**Solution 50.19 :**
1. IPP avec $u'(t) = 1 \implies u(t) = t - 1/2$ et $v(t) = f(t) \implies v'(t) = f'(t)$ :
   $\int_0^1 (t - 1/2) f'(t) \, dt = [(t - 1/2) f(t)]_0^1 - \int_0^1 1 \times f(t) \, dt = \left(\dfrac{1}{2} f(1) - \left(-\dfrac{1}{2} f(0)\right)\right) - \int_0^1 f(t) \, dt = \dfrac{f(0)+f(1)}{2} - \int_0^1 f(t) \, dt$.
2. En sommant cette relation sur les intervalles $[k\,; k+1]$ pour $k = 0, \dots, n-1$, on obtient la formule sommatoire d'Euler-Maclaurin, qui permet d'évaluer les sommes discrètes avec une précision extraordinaire.

**Solution 50.20 :**
Soit $F(x) = \int_a^x f(t)\,dt$. $F$ est continue sur $[a\,; b]$ et dérivable sur $]a\,; b[$.
D'après le Théorème des Accroissements Finis (TAF), il existe $c \in \; ]a\,; b[$ tel que :
$$\dfrac{F(b) - F(a)}{b - a} = F'(c).$$
Or $F(b) - F(a) = \int_a^b f(t)\,dt$ et $F'(c) = f(c)$.
On a donc bien : $\int_a^b f(t)\,dt = f(c)(b - a)$.

---

### La question qui ouvre la suite

Nous savons désormais calculer l'aire sous une courbe lorsque la formule de la fonction est connue. Mais que se passe-t-il dans la vraie vie, quand nous ne connaissons pas la formule de la fonction, mais seulement **la relation entre la fonction et sa propre dérivée** ?

Quand une tasse de thé chaud est posée sur la table, la vitesse à laquelle elle refroidit est proportionnelle à la différence entre sa température et celle de la pièce.
Comment trouver l'équation complète de la température au fil du temps à partir de cette simple loi physique ?

C'est l'entrée dans le royaume des **équations différentielles** : rendez-vous au chapitre 51 avec **la tasse de thé qui refroidit**.
