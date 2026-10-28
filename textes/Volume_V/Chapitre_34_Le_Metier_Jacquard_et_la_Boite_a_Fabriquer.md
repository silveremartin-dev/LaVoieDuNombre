# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 34 : Le Métier Jacquard et la Boîte à Fabriquer

> *« Une fonction n'est pas un dessin figé dans un livre. C'est une usine vivante : tu glisses un morceau de métal brut à l'entrée, les rouages tournent, la règle mécanique s'applique, et une pièce façonnée sort sur le tapis roulant. Les mathématiques modernes sont le grand atelier où ces métamorphoses s'enchaînent. »*

---

### Ce que tu vas découvrir

- Comment l'invention des cartes perforées de **Joseph Marie Jacquard** à Lyon et le génie d'**Ada Lovelace** ont donné naissance au concept moderne de fonction.
- Le vocabulaire fondamental : **antécédent**, **image**, **ensemble de définition** $\mathcal{D}_f$, et la règle absolue de l'unicité de l'image.
- Comment lire et construire une **courbe représentative**, un tableau de valeurs et un **tableau de variations**.
- Les notions de **maximum**, de **minimum** (locaux et globaux) et la **parité** (fonctions paires et impaires, symétries du plan).
- L'étude complète des **cinq fonctions de référence** : carré ($x^2$), inverse ($\frac{1}{x}$), racine carrée ($\sqrt{x}$), cube ($x^3$) et valeur absolue ($|x|$).
- La résolution graphique d'équations $f(x) = k$, $f(x) = g(x)$ et d'inéquations, ainsi que la **composition** d'usines $g \circ f$.

---

### 1. Le problème : les canuts de Lyon et les cartons d'Ada Lovelace

Au tout début du XIXᵉ siècle, sur les pentes raides de la colline de la Croix-Rousse à Lyon, les ateliers des tisseurs de soie — les *canuts* — résonnent du cliquetis assourdissant des navettes de bois.

Pour tisser un tissu de brocart damassé orné de roses rouges et de feuilles d'argent, il fallait deux ouvriers sur chaque métier : le maître tisseur assis devant le peigne, et un tout jeune enfant courbé dans la poussière (le « tireur de lacs ») qui tirait manuellement des cordelettes pour soulever les fils de chaîne un par un. Le travail était exténuant, destructeur pour la vue et la colonne vertébrale, et la moindre distraction de l'enfant créait un nœud irréversible dans l'étoffe précieuse.

En **1801**, un fils d'artisan lyonnais, **Joseph Marie Jacquard**, invente un mécanisme automatique qui va sidérer l'Europe :
Il remplace l'enfant par un ruban sans fin de **cartes de carton perforées** enchaînées les unes aux autres.
- Un trou dans le carton ? Une aiguille passe librement : le crochet s'enclenche, le fil de soie monte.
- Pas de trou ? Le carton plein repousse l'aiguille : le fil de soie reste en bas.

Le métier Jacquard est la première machine programmable de l'Histoire humaine !

```
   [ Carton perforé ] ───► ┌──────────────────────────┐ ───► [ Soie ouvragée ]
        (Entrée x)         │    Le Métier Jacquard    │        (Sortie f(x))
                           │     (Règle mécanique)    │
                           └──────────────────────────┘
```

En **1843**, à Londres, une jeune mathématicienne d'une intuition prodigieuse, **Ada Lovelace** (fille unique du poète Lord Byron), étudie les plans de la « Machine Analytique » à engrenages imaginée par Charles Babbage. Elle fait immédiatement le lien avec les soyeux lyonnais et écrit cette formule célèbre :
> *« La Machine Analytique tisse des motifs algébriques tout comme le métier Jacquard tisse des fleurs et des feuilles. »*

Ada Lovelace rédige alors l'algorithme de calcul des nombres de Bernoulli : elle vient d'écrire le **tout premier programme informatique du monde**.

Ce que Jacquard a réalisé dans le carton et ce qu'Ada Lovelace a formalisé dans l'esprit, c'est l'essence même de ce que les mathématiciens appellent une **Fonction**.

---

### 2. Anatomie d'une fonction : vocabulaire et ensemble de définition

#### 2.1 La boîte noire ($x \mapsto f(x)$)

Oublie pour l'instant les courbes compliquées. Pense à une **machine industrielle inflexible** :

```
             x (Matière brute à l'entrée : ANTÉCÉDENT)
             │
             ▼
      ┌───────────────┐
      │  Machine f    │   Règle : "Prends l'entrée, multiplie par 3,
      │               │            puis soustrais 5"
      └───────────────┘
             │
             ▼
           f(x) = 3x - 5  (Pièce finie à la sortie : IMAGE)
```

> **📐 Définitions fondamentales —**
> 1. Une **fonction** $f$ est un processus mathématique qui, à tout nombre réel $x$ d'un ensemble donné, associe **au plus un** unique nombre réel, noté $f(x)$.
> 2. On note :
>    $$f : x \mapsto f(x)$$
>    On lit à voix haute : « la fonction $f$ qui à $x$ associe $f$ de $x$ ».
> 3. **L'antécédent :** c'est le nombre $x$ introduit au départ.
> 4. **L'image :** c'est le résultat $f(x)$ obtenu à l'arrivée.

> **⚠️ Règle d'or absolue — Unicité de l'image.**
> - Un nombre $x$ a **au maximum une seule image** par une fonction $f$. Si tu enfournes la même farine dans le même four, il ne peut pas sortir deux pains différents en même temps !
> - En revanche, un nombre $y$ peut avoir **aucun, un ou plusieurs antécédents**. Par exemple, pour la machine qui élève au carré ($f(x) = x^2$) :
>   - Le nombre $9$ a deux antécédents : $3$ et $-3$ (car $3^2 = 9$ et $(-9)^2 = 9$).
>   - Le nombre $-4$ n'a aucun antécédent réel (aucun carré réel n'est négatif).

#### 2.2 L'ensemble de définition $\mathcal{D}_f$ : les valeurs interdites

Toutes les machines physiques ont des limites de tolérance : glisse une grosse barre de fer dans un moulin à café en plastique, et le moulin vole en éclats.
En mathématiques, certaines opérations sont formellement prohibées dans l'ensemble des réels.

> **📐 Définition — Ensemble de définition.**
> L'**ensemble de définition** d'une fonction $f$, noté $\mathcal{D}_f$, est l'ensemble de tous les réels $x$ pour lesquels le calcul de $f(x)$ est possible et licite.

Au lycée, deux opérations imposent la recherche d'une **valeur interdite** :
1. **La division par zéro :** Le dénominateur d'une fraction ne peut **jamais** s'annuler.
   $$\frac{A}{B} \text{ existe si et seulement si } B \neq 0.$$
2. **La racine carrée d'un nombre négatif :** La quantité placée sous le radical doit être positive ou nulle.
   $$\sqrt{A} \text{ existe si et seulement si } A \ge 0.$$

---

### 3. Courbe représentative, variations et extremums

#### 3.1 La courbe dans le repère

> **📐 Définition — Courbe représentative.**
> Dans un repère $(O\,; \vec{i}, \vec{j})$, la **courbe représentative** d'une fonction $f$, notée $\mathcal{C}_f$, est l'ensemble de tous les points $M(x\,; y)$ dont l'abscisse $x \in \mathcal{D}_f$ et l'ordonnée est son image $y = f(x)$ :
> $$\mathcal{C}_f = \left\{ M(x\,; f(x)) \mid x \in \mathcal{D}_f \right\}.$$
> L'équation de la courbe est : $y = f(x)$.

Pour vérifier si un point $A(x_A\,; y_A)$ est sur la courbe, on calcule $f(x_A)$. S'il est égal à $y_A$, le point est sur la courbe ; sinon, il ne l'est pas.

#### 3.2 Variations : la lecture du relief

Imagine un randonneur qui marche sur la courbe $\mathcal{C}_f$ de la gauche vers la droite (dans le sens des abscisses croissantes, $x$ augmentant).

```
         y ▲             Sommet (Maximum)
           │                 ▲
           │               /   \
           │              /     \
           │             /       ▼
           │            /         \
           │           ▲           ▼
           │          /             \  Creux (Minimum)
           │         /               ▼
         O ┼────────┼─────────────────┼────────► x
                    a                 b
```

> **📐 Définition — Sens de variation sur un intervalle $I$.**
> Soit $f$ une fonction définie sur un intervalle $I$.
> 1. $f$ est **strictement croissante** sur $I$ si pour tous réels $a$ et $b$ de $I$ :
>    $$a < b \implies f(a) < f(b).$$
>    *(Une fonction croissante conserve l'ordre des inégalités).*
> 2. $f$ est **strictement décroissante** sur $I$ si pour tous réels $a$ et $b$ de $I$ :
>    $$a < b \implies f(a) > f(b).$$
>    *(Une fonction décroissante inverse l'ordre des inégalités).*
> 3. $f$ est **constante** sur $I$ si pour tous $a, b \in I$, $f(a) = f(b)$.
> 4. Une fonction est dite **monotone** sur un intervalle si elle est soit seulement croissante, soit seulement décroissante sur cet intervalle.

#### 3.3 Extremums : sommets et creux

> **📐 Définition — Maximum et Minimum.**
> Soit $f$ une fonction définie sur un ensemble $\mathcal{D}_f$ et soit $x_0 \in \mathcal{D}_f$.
> - $f$ admet un **maximum** en $x_0$ sur $\mathcal{D}_f$, valant $M = f(x_0)$, si pour tout $x \in \mathcal{D}_f$ :
>   $$f(x) \le f(x_0).$$
> - $f$ admet un **minimum** en $x_0$ sur $\mathcal{D}_f$, valant $m = f(x_0)$, si pour tout $x \in \mathcal{D}_f$ :
>   $$f(x) \ge f(x_0).$$
> Un **extremum** désigne indifféremment un maximum ou un minimum.

---

### 4. La parité : la symétrie dans le miroir

#### 4.1 Ensemble centré en zéro

Pour comparer ce qui se passe à droite et à gauche de l'origine, l'ensemble de définition doit être symétrique par rapport à zéro :
$$\forall x \in \mathcal{D}_f, \quad -x \in \mathcal{D}_f.$$
Par exemple, $[-3\,; 3]$ et $\mathbb{R} \setminus \{0\}$ sont centrés en 0 ; en revanche, $[-2\,; 5]$ ne l'est pas (car pour $x = 4$, $-4$ n'est pas dans l'ensemble).

#### 4.2 Fonctions paires et impaires

> **📐 Définition — Parité.**
> 1. Une fonction $f$ est **paire** si pour tout $x \in \mathcal{D}_f$ :
>    $$f(-x) = f(x).$$
>    **Propriété géométrique :** Sa courbe $\mathcal{C}_f$ admet l'**axe des ordonnées $(Oy)$ comme axe de symétrie**.
> 2. Une fonction $f$ est **impaire** si pour tout $x \in \mathcal{D}_f$ :
>    $$f(-x) = -f(x).$$
>    **Propriété géométrique :** Sa courbe $\mathcal{C}_f$ admet l'**origine du repère $O$ comme centre de symétrie**.

```
         FONCTION PAIRE                      FONCTION IMPAIRE
       (Symétrie axiale)                   (Symétrie centrale)
             y ▲                                 y ▲
           \   │   /                               │       /
            \  │  /                                │      /
             \ │ /                                 │     /
       ───────\│/───────► x                ────────┼────o───► x
               O                                 / │
                                                /  │
                                               /   │
```

---

### 5. Les cinq fonctions de référence

Ce sont les cinq briques de base avec lesquelles toutes les machines mathématiques du lycée sont construites.

#### 5.1 La fonction carré : $f(x) = x^2$

- **Ensemble de définition :** $\mathcal{D}_f = \mathbb{R} = ]-\infty\,; +\infty[$.
- **Parité :** Pour tout réel $x$, $(-x)^2 = x^2$. La fonction carré est **paire**.
- **Variations :**
  - Sur $]-\infty\,; 0]$, elle est strictement décroissante : si $a < b \le 0$, alors $a^2 > b^2$.
  - Sur $[0\,; +\infty[$, elle est strictement croissante : si $0 \le a < b$, alors $a^2 < b^2$.
- **Courbe :** C'est une **parabole** tournée vers le haut, dont le sommet est l'origine $O(0\,; 0)$. Son minimum absolu est $0$, atteint en $x = 0$.

> **Tableau de variations de $x \mapsto x^2$ :**
>
> | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
> |---|---|---|---|---|---|
> | Variations de $x^2$ | $+\infty$ | $\searrow$ | $0$ | $\nearrow$ | $+\infty$ |

#### 5.2 La fonction inverse : $f(x) = \frac{1}{x}$

- **Ensemble de définition :** $\mathcal{D}_f = \mathbb{R}^* = \mathbb{R} \setminus \{0\} = ]-\infty\,; 0[ \cup ]0\,; +\infty[$.
- **Parité :** Pour tout $x \neq 0$, $\frac{1}{-x} = -\frac{1}{x}$. La fonction inverse est **impaire**.
- **Variations :**
  - Strictement décroissante sur $]-\infty\,; 0[$.
  - Strictement décroissante sur $]0\,; +\infty[$.
- **Courbe :** C'est une **hyperbole** en deux branches distinctes, symétrique par rapport à $O$. Les axes de coordonnées sont ses **asymptotes**.

> **⚠️ Attention, piège classique !**
> On ne dit **JAMAIS** que la fonction inverse est « décroissante sur $\mathbb{R}^*$ ».
> En effet, prenons $a = -1$ et $b = 1$. On a bien $a < b$, mais $f(a) = \frac{1}{-1} = -1$ et $f(b) = 1$. L'image a augmenté de $-1$ à $+1$ !
> La décroissance est vraie **sur chacun des deux intervalles séparément**, mais pas sur leur réunion.

> **Tableau de variations de $x \mapsto \frac{1}{x}$ :**
>
> | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
> |---|---|---|---|---|---|
> | Variations de $\frac{1}{x}$ | $0$ | $\searrow$ | $-\infty$ $\parallel$ $+\infty$ | $\searrow$ | $0$ |
>
> *(La double barre $\parallel$ indique la valeur interdite en $0$).*

#### 5.3 La fonction racine carrée : $f(x) = \sqrt{x}$

- **Ensemble de définition :** $\mathcal{D}_f = [0\,; +\infty[ = \mathbb{R}_+$.
- **Parité :** Aucun sens (l'ensemble n'est pas centré en 0).
- **Variations :** Strictement croissante sur $[0\,; +\infty[$.
  $$0 \le a < b \implies \sqrt{a} < \sqrt{b}.$$
- **Courbe :** C'est une demi-branche de parabole couchée. Elle démarre en $O(0\,; 0)$ avec une tangente verticale à l'origine.

#### 5.4 La fonction cube : $f(x) = x^3$

- **Ensemble de définition :** $\mathcal{D}_f = \mathbb{R}$.
- **Parité :** $(-x)^3 = (-1)^3 x^3 = -x^3$. La fonction cube est **impaire**.
- **Variations :** Strictement croissante sur tout $\mathbb{R}$.
  $$a < b \implies a^3 < b^3.$$
- **Courbe :** Elle traverse l'origine avec une inflexion horizontale en $O(0\,; 0)$.

#### 5.5 La fonction valeur absolue : $f(x) = |x|$

- **Ensemble de définition :** $\mathcal{D}_f = \mathbb{R}$.
- **Définition explicite :**
  $$|x| = \begin{cases} x & \text{si } x \ge 0 \\ -x & \text{si } x < 0 \end{cases}$$
- **Parité :** $|-x| = |x|$. La fonction est **paire**.
- **Variations :**
  - Strictement décroissante sur $]-\infty\,; 0]$ (pente $-1$).
  - Strictement croissante sur $[0\,; +\infty[$ (pente $+1$).
- **Courbe :** Forme une pointe en **V**, avec deux demi-droites se raccordant à angle droit en $O(0\,; 0)$. Son minimum absolu est $0$.

---

### 6. Résolutions graphiques et composition d'usines

#### 6.1 Résolutions graphiques

1. **Résoudre $f(x) = k$ :**
   On trace la droite horizontale d'équation $y = k$. Les solutions de l'équation sont les **abscisses** des points d'intersection entre la courbe $\mathcal{C}_f$ et la droite horizontale.

2. **Résoudre $f(x) = g(x)$ :**
   Les solutions sont les **abscisses** des points où les deux courbes $\mathcal{C}_f$ et $\mathcal{C}_g$ se coupent.

3. **Résoudre $f(x) \le g(x)$ :**
   Les solutions sont les intervalles de l'axe des abscisses où la courbe $\mathcal{C}_f$ est située **en dessous** de la courbe $\mathcal{C}_g$ (ou la touche).

```
                 y ▲               Droite y = k
                   │  Cf          /
                   │   \    k ───o───────o────► y = k
                   │    \       /│       │
                   │     \_____/ │       │
                 O ┼─────────────┼───────┼────────► x
                                 x1      x2
                         Solutions de f(x) = k : {x1, x2}
```

#### 6.2 L'usine en cascade : la composition $g \circ f$

Quand on place deux machines à la chaîne :

```
             ┌───────────┐           ┌───────────┐
     x ────► │ Machine f │ ── f(x) ─►│ Machine g │ ───► g(f(x))
             └───────────┘           └───────────┘
```

> **📐 Définition — Composée de deux fonctions.**
> Soient deux fonctions $f$ et $g$. La fonction composée de $f$ suivie de $g$, notée $g \circ f$ (lu « g rond f »), est définie par :
> $$(g \circ f)(x) = g(f(x)).$$
> Pour que cette opération soit possible, il faut que $x \in \mathcal{D}_f$ et que le résultat intermédiaire $f(x)$ appartienne à l'ensemble de définition de la seconde machine : $f(x) \in \mathcal{D}_g$.

> **⚠️ Attention, piège ! L'ordre des machines est vital.**
> En général, $g \circ f \neq f \circ g$.
> Si $f(x) = x + 3$ et $g(x) = x^2$ :
> - $(g \circ f)(x) = g(x + 3) = (x + 3)^2 = x^2 + 6x + 9$.
> - $(f \circ g)(x) = f(x^2) = x^2 + 3$.
> Les deux résultats n'ont rien à voir !

---

### 7. Exemples résolus détaillés

> **Exemple résolu 1 — Déterminer des ensembles de définition.**
> Déterminer l'ensemble de définition des fonctions suivantes :
> a) $f(x) = \frac{2x - 1}{x^2 - 9}$ \quad b) $g(x) = \sqrt{3x - 6}$ \quad c) $h(x) = \frac{1}{\sqrt{x} - 2}$
>
> **Solution pas à pas :**
> a) $f(x)$ est définie si et seulement si son dénominateur est non nul :
>    $$x^2 - 9 \neq 0 \iff (x - 3)(x + 3) \neq 0 \iff x \neq 3 \text{ et } x \neq -3.$$
>    Donc $\mathcal{D}_f = \mathbb{R} \setminus \{-3\,; 3\} = ]-\infty\,; -3[ \cup ]-3\,; 3[ \cup ]3\,; +\infty[$.
>
> b) $g(x)$ contient une racine carrée : la quantité sous le radical doit être positive ou nulle :
>    $$3x - 6 \ge 0 \iff 3x \ge 6 \iff x \ge 2.$$
>    Donc $\mathcal{D}_g = [2\,; +\infty[$.
>
> c) Pour $h(x)$, deux conditions doivent être respectées :
>    1. Présence de $\sqrt{x} \implies x \ge 0$.
>    2. Dénominateur non nul : $\sqrt{x} - 2 \neq 0 \iff \sqrt{x} \neq 2 \iff x \neq 4$.
>    On combine les deux : $\mathcal{D}_h = [0\,; 4[ \cup ]4\,; +\infty[$.

> **Exemple résolu 2 — Images et antécédents.**
> Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = 2x^2 - 3x - 5$.
> 1. Calculer l'image de $-2$ et de $\frac{1}{2}$ par $f$.
> 2. Déterminer les antécédents éventuels de $-5$ par $f$.
>
> **Solution :**
> 1. Calcul des images :
>    $$f(-2) = 2(-2)^2 - 3(-2) - 5 = 2(4) + 6 - 5 = 8 + 6 - 5 = 9.$$
>    $$f\left(\frac{1}{2}\right) = 2\left(\frac{1}{4}\right) - 3\left(\frac{1}{2}\right) - 5 = \frac{1}{2} - \frac{3}{2} - 5 = -1 - 5 = -6.$$
> 2. Pour trouver les antécédents de $-5$, on résout l'équation $f(x) = -5$ :
>    $$2x^2 - 3x - 5 = -5 \iff 2x^2 - 3x = 0.$$
>    On factorise par $x$ :
>    $$x(2x - 3) = 0 \iff x = 0 \quad \text{ou} \quad 2x - 3 = 0 \implies x = \frac{3}{2}.$$
>    Le nombre $-5$ admet deux antécédents par $f$ : $0$ et $\frac{3}{2}$.

> **Exemple résolu 3 — Démontrer le sens de variation d'une fonction sans dérivée.**
> Soit $f$ définie sur $]1\,; +\infty[$ par $f(x) = \frac{3}{x - 1}$.
> Démontrer rigoureusement que $f$ est strictement décroissante sur cet intervalle.
>
> **Solution :**
> Soient deux réels quelconques $a$ et $b$ appartenant à $]1\,; +\infty[$ tels que $1 < a < b$.
> Construisons l'expression pas à pas en appliquant les règles sur les inégalités :
> 1. On soustrait $1$ :
>    $$0 < a - 1 < b - 1.$$
> 2. On applique la fonction inverse, qui est strictement décroissante sur $]0\,; +\infty[$ (elle inverse l'ordre des nombres strictement positifs) :
>    $$\frac{1}{a - 1} > \frac{1}{b - 1}.$$
> 3. On multiplie par $3 > 0$ (l'ordre est conservé) :
>    $$\frac{3}{a - 1} > \frac{3}{b - 1} \iff f(a) > f(b).$$
> Conclusion : Nous sommes partis de $a < b$ et nous avons abouti à $f(a) > f(b)$.
> L'ordre a été inversé : la fonction $f$ est **strictement décroissante** sur $]1\,; +\infty[$. $\blacksquare$

> **Exemple résolu 4 — Étude de parité algébrique.**
> Étudier la parité des fonctions suivantes :
> a) $f(x) = \frac{x^4 - 3}{x^2 + 1}$ \quad b) $g(x) = \frac{2x}{x^2 + 4}$ \quad c) $h(x) = x^3 - 2x + 1$
>
> **Solution :**
> a) $\mathcal{D}_f = \mathbb{R}$ car $x^2 + 1 > 0$ ne s'annule jamais. $\mathcal{D}_f$ est centré en 0.
>    $$f(-x) = \frac{(-x)^4 - 3}{(-x)^2 + 1} = \frac{x^4 - 3}{x^2 + 1} = f(x).$$
>    Donc $f$ est **paire**.
>
> b) $\mathcal{D}_g = \mathbb{R}$, centré en 0.
>    $$g(-x) = \frac{2(-x)}{(-x)^2 + 4} = \frac{-2x}{x^2 + 4} = -\frac{2x}{x^2 + 4} = -g(x).$$
>    Donc $g$ est **impaire**.
>
> c) $\mathcal{D}_h = \mathbb{R}$, centré en 0.
>    $$h(-x) = (-x)^3 - 2(-x) + 1 = -x^3 + 2x + 1.$$
>    Comparons :
>    - $h(x) = x^3 - 2x + 1 \neq h(-x)$, donc $h$ n'est pas paire.
>    - $-h(x) = -x^3 + 2x - 1 \neq h(-x)$ (à cause du $+1$ final), donc $h$ n'est pas impaire.
>    Conclusion : la fonction $h$ n'est **ni paire ni impaire**.

> **Exemple résolu 5 — Décomposition et calcul d'une fonction composée.**
> Soient $f(x) = 2x - 5$ et $g(x) = \frac{1}{x}$.
> 1. Déterminer l'expression de $(g \circ f)(x)$ et son ensemble de définition.
> 2. Déterminer l'expression de $(f \circ g)(x)$ et son ensemble de définition.
>
> **Solution :**
> 1. $(g \circ f)(x) = g(f(x)) = g(2x - 5) = \frac{1}{2x - 5}$.
>    Condition d'existence : $2x - 5 \neq 0 \iff x \neq \frac{5}{2}$.
>    Donc $\mathcal{D}_{g \circ f} = \mathbb{R} \setminus \left\{\frac{5}{2}\right\}$.
>
> 2. $(f \circ g)(x) = f(g(x)) = f\left(\frac{1}{x}\right) = 2\left(\frac{1}{x}\right) - 5 = \frac{2}{x} - 5$.
>    Condition d'existence : $x \neq 0$.
>    Donc $\mathcal{D}_{f \circ g} = \mathbb{R}^*$.
>    *(On remarque à nouveau que les deux composées sont totalement différentes).*

> **Exemple résolu 6 — Résolution graphique et encadrement avec les fonctions de référence.**
> Résoudre dans $\mathbb{R}$ :
> a) $x^2 \le 7$ \quad b) $\frac{1}{x} > 2$
>
> **Solution :**
> a) On sait que la fonction carré est décroissante sur $]-\infty\,; 0]$ et croissante sur $[0\,; +\infty[$.
>    L'équation $x^2 = 7$ a deux solutions : $-\sqrt{7}$ et $\sqrt{7}$.
>    La parabole $y = x^2$ est située en dessous de la droite horizontale $y = 7$ pour toutes les abscisses comprises entre ces deux valeurs.
>    Donc l'ensemble des solutions est $\boxed{S = [-\sqrt{7}\,; \sqrt{7}]}$.
>
> b) Traçons mentalement l'hyperbole $y = \frac{1}{x}$ et la droite $y = 2$.
>    - Pour $x \le 0$, $\frac{1}{x} < 0$, donc $\frac{1}{x}$ ne peut jamais être strictement supérieur à 2.
>    - Pour $x > 0$, l'équation $\frac{1}{x} = 2$ donne $x = \frac{1}{2}$.
>    Comme la fonction inverse est strictement décroissante sur $]0\,; +\infty[$, pour avoir une image plus grande que $2$, il faut choisir des abscisses plus petites que $\frac{1}{2}$ (mais strictement positives pour rester au-dessus de 0).
>    Donc l'ensemble des solutions est $\boxed{\left.S = \right]0\,; \frac{1}{2}\left[\right.}$.

---

### 8. En informatique : table de valeurs et recherche de racine en Python

En mathématiques et en sciences, on utilise souvent un script informatique pour calculer automatiquement les images d'une fonction et localiser où elle s'annule :

```python
def f(x):
    """Définition de la fonction f(x) = x**3 - 3*x + 1"""
    return x**3 - 3*x + 1

def table_de_valeurs(debut, fin, pas):
    """Affiche une table de valeurs de la fonction f."""
    print("  x   |  f(x)")
    print("------|--------")
    x = debut
    while x <= fin + 1e-9:
        print(f"{x:5.2f} | {f(x):7.3f}")
        x += pas

# Affichage des valeurs entre -2 et 2 avec un pas de 0.5
table_de_valeurs(-2, 2, 0.5)

# Recherche approchée d'une solution à f(x) = 0 par balayage
def balayage(a, b, pas=0.001):
    x = a
    while x <= b:
        if f(x) * f(x + pas) <= 0:
            return round(x + pas / 2, 3)
        x += pas
    return None

solution = balayage(0, 1)
print(f"\nUne solution approchée dans [0; 1] est x ≈ {solution}")
```

---

### Ce qu'il faut retenir

1. **Fonction :** $x \mapsto f(x)$. À chaque antécédent $x \in \mathcal{D}_f$ correspond **une unique image** $f(x)$. Un nombre peut avoir $0$, $1$ ou plusieurs antécédents.
2. **Ensemble de définition $\mathcal{D}_f$ :**
   - Dénominateur $\neq 0$.
   - Quantité sous une racine carrée $\ge 0$.
3. **Variations :**
   - Croissante : $a < b \implies f(a) \le f(b)$ (conserve l'ordre).
   - Décroissante : $a < b \implies f(a) \ge f(b)$ (inverse l'ordre).
4. **Parité :**
   - Paire : $f(-x) = f(x)$, symétrie par rapport à l'axe des ordonnées $(Oy)$.
   - Impaire : $f(-x) = -f(x)$, symétrie centrale par rapport à l'origine $O$.
5. **Les 5 fonctions de référence :**
   - Carré $x^2$ : $\mathcal{D} = \mathbb{R}$, paire, décroissante sur $\mathbb{R}_-$, croissante sur $\mathbb{R}_+$, sommet $O(0\,; 0)$.
   - Inverse $\frac{1}{x}$ : $\mathcal{D} = \mathbb{R}^*$, impaire, décroissante sur $]-\infty\,; 0[$ et sur $]0\,; +\infty[$.
   - Racine $\sqrt{x}$ : $\mathcal{D} = [0\,; +\infty[$, croissante.
   - Cube $x^3$ : $\mathcal{D} = \mathbb{R}$, impaire, croissante.
   - Valeur absolue $|x|$ : $\mathcal{D} = \mathbb{R}$, paire, en forme de V.
6. **Résolution graphique :** $f(x) = k$ $\iff$ abscisses des points de la courbe à hauteur $k$.

---

### Exercices

#### Exercices d'application directe (★)

1. Soit la fonction $f(x) = x^2 - 4x + 3$. Calculer $f(0)$, $f(1)$, $f(2)$ et $f(-1)$.
2. Donner l'ensemble de définition de la fonction $g(x) = \frac{1}{x - 7}$.
3. Donner l'ensemble de définition de la fonction $h(x) = \sqrt{2x + 8}$.
4. Soit $f(x) = 3x - 5$. Quel est l'antécédent de $10$ par $f$ ?
5. La fonction $f(x) = 5x^4 - 2x^2 + 1$ est-elle paire, impaire ou ni l'un ni l'autre ?
6. La fonction $g(x) = x^3 + 4x$ est-elle paire, impaire ou ni l'un ni l'autre ?
7. Résoudre dans $\mathbb{R}$ l'équation $x^2 = 25$.
8. Résoudre dans $\mathbb{R}$ l'inéquation $x^2 < 16$.
9. Résoudre dans $\mathbb{R}^*$ l'équation $\frac{1}{x} = 5$.
10. Déterminer la valeur de $|-17|$, $|3{,}14|$ et $|5 - 9|$.

#### Exercices d'entraînement et de réflexion (★★)

11. Déterminer l'ensemble de définition des fonctions :
    a) $f(x) = \frac{x + 2}{x^2 - 4x}$ \quad b) $g(x) = \sqrt{10 - 2x}$ \quad c) $h(x) = \frac{\sqrt{x + 3}}{x - 1}$
12. Soit la fonction $f$ définie sur $[-4\,; 4]$ dont le tableau de variations est :
    - Décroissante de $-4$ à $-1$, passant de $5$ à $-3$.
    - Croissante de $-1$ à $2$, passant de $-3$ à $4$.
    - Décroissante de $2$ à $4$, passant de $4$ à $1$.
    a) Quel est le maximum global de $f$ sur $[-4\,; 4]$ ? Pour quelle valeur de $x$ est-il atteint ?
    b) Quel est le minimum global de $f$ ?
    c) Combien de solutions l'équation $f(x) = 0$ admet-elle ?
13. Démontrer sans utiliser la dérivation que la fonction $f(x) = x^2 - 6x + 5$ est strictement croissante sur l'intervalle $[3\,; +\infty[$. *(Indication : écrire $f(x)$ sous la forme $(x - 3)^2 - 4$)*.
14. Résoudre dans $\mathbb{R}$ les inéquations :
    a) $x^2 \ge 9$ \quad b) $\frac{1}{x} \le 3$
15. Étudier la parité de la fonction $f(x) = \frac{x^3}{x^2 + 1}$.
16. On considère $f(x) = \sqrt{x}$ et $g(x) = x + 4$.
    Expliciter les formules de $(g \circ f)(x)$ et de $(f \circ g)(x)$, en précisant leurs domaines de définition.
17. Résoudre l'équation $|2x - 3| = 7$.
18. Résoudre l'inéquation $|x - 5| \le 2$ en l'interprétant comme une distance sur la droite numérique.

#### Exercices d'approfondissement et défis (★★★)

19. **Une fonction ni paire ni impaire décomposée en deux.**
    Soit $f$ une fonction quelconque définie sur $\mathbb{R}$.
    On pose $p(x) = \frac{f(x) + f(-x)}{2}$ et $i(x) = \frac{f(x) - f(-x)}{2}$.
    a) Démontrer que $p$ est paire et que $i$ est impaire.
    b) Démontrer que $f(x) = p(x) + i(x)$.
    c) Appliquer cette décomposition à la fonction $f(x) = 2x^2 - 3x + 4$.
20. **Optimisation d'un enclos rectangulaire.**
    Un éleveur dispose de $40\text{ mètres}$ de grillage pour construire un enclos rectangulaire adossé à un mur de pierre déjà existant (il n'a donc pas besoin de grillage le long du mur).
    On note $x$ la largeur des deux côtés perpendiculaires au mur.
    a) Exprimer la longueur du troisième côté en fonction de $x$.
    b) Pour quelles valeurs de $x$ l'enclos est-il réalisable ?
    c) Exprimer l'aire $A(x)$ de l'enclos en fonction de $x$.
    d) Démontrer que $A(x) = -2(x - 10)^2 + 200$.
    e) En déduire la valeur de $x$ qui rend l'aire maximale et donner cette aire maximale.
21. **Inégalité remarquable arithmético-géométrique.**
    Pour tout réel strictement positif $x > 0$, on pose $f(x) = x + \frac{1}{x}$.
    a) Développer l'expression $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2$.
    b) En déduire que pour tout $x > 0$, $x + \frac{1}{x} \ge 2$.
    c) Pour quelle valeur de $x$ cette inégalité devient-elle une égalité exacte ?
22. **Point fixe d'une fonction.**
    On appelle point fixe d'une fonction $f$ un nombre $x$ tel que $f(x) = x$.
    Déterminer tous les points fixes des fonctions de référence :
    a) $f(x) = x^2$ \quad b) $g(x) = \frac{1}{x}$ \quad c) $h(x) = \sqrt{x}$ \quad d) $k(x) = x^3$.

---

### Solutions

1. $f(0) = 3$. $f(1) = 1 - 4 + 3 = 0$. $f(2) = 4 - 8 + 3 = -1$. $f(-1) = (-1)^2 - 4(-1) + 3 = 1 + 4 + 3 = 8$.
2. Dénominateur non nul : $x - 7 \neq 0 \iff x \neq 7$. Donc $\mathcal{D}_g = \mathbb{R} \setminus \{7\}$.
3. Quantité sous la racine positive ou nulle : $2x + 8 \ge 0 \iff 2x \ge -8 \iff x \ge -4$. Donc $\mathcal{D}_h = [-4\,; +\infty[$.
4. $3x - 5 = 10 \iff 3x = 15 \iff x = 5$. L'antécédent est $5$.
5. $f(-x) = 5(-x)^4 - 2(-x)^2 + 1 = 5x^4 - 2x^2 + 1 = f(x)$. La fonction est paire.
6. $g(-x) = (-x)^3 + 4(-x) = -x^3 - 4x = -(x^3 + 4x) = -g(x)$. La fonction est impaire.
7. $x^2 = 25 \iff x = 5$ ou $x = -5$. $S = \{-5\,; 5\}$.
8. $x^2 < 16 \iff -4 < x < 4$. $S = ]-4\,; 4[$.
9. $\frac{1}{x} = 5 \iff x = \frac{1}{5} = 0{,}2$.
10. $|-17| = 17$ ; $|3{,}14| = 3{,}14$ ; $|5 - 9| = |-4| = 4$.
11. a) $x^2 - 4x = x(x - 4) \neq 0 \implies x \neq 0$ et $x \neq 4$. $\mathcal{D}_f = \mathbb{R} \setminus \{0\,; 4\}$.
    b) $10 - 2x \ge 0 \iff 2x \le 10 \iff x \le 5$. $\mathcal{D}_g = ]-\infty\,; 5]$.
    c) $x + 3 \ge 0 \iff x \ge -3$ et dénominateur $x - 1 \neq 0 \iff x \neq 1$. $\mathcal{D}_h = [-3\,; 1[ \cup ]1\,; +\infty[$.
12. a) Le maximum global est $5$, atteint en $x = -4$.
    b) Le minimum global est $-3$, atteint en $x = -1$.
    c) Sur $[-4\,; -1]$, $f$ passe de $5$ à $-3$, donc coupe $0$ une fois. Sur $[-1\,; 2]$, elle passe de $-3$ à $4$, donc coupe $0$ une deuxième fois. Sur $[2\,; 4]$, les valeurs vont de $4$ à $1$ (toujours positives), donc elle ne coupe pas $0$. L'équation $f(x) = 0$ admet donc exactement $2$ solutions.
13. Forme canonique : $(x - 3)^2 - 4 = x^2 - 6x + 9 - 4 = x^2 - 6x + 5$.
    Soient $3 \le a < b$.
    Alors $0 \le a - 3 < b - 3$.
    Comme la fonction carré est strictement croissante sur $[0\,; +\infty[$, on a $(a - 3)^2 < (b - 3)^2$.
    En retranchant $4$ : $(a - 3)^2 - 4 < (b - 3)^2 - 4 \iff f(a) < f(b)$.
    L'ordre est conservé : $f$ est strictement croissante sur $[3\,; +\infty[$.
14. a) $x^2 \ge 9 \iff x \le -3$ ou $x \ge 3$. $S = ]-\infty\,; -3] \cup [3\,; +\infty[$.
    b) Pour $\frac{1}{x} \le 3$ :
    - Si $x < 0$, $\frac{1}{x} < 0 < 3$, donc tous les réels strictement négatifs sont solutions : $]-\infty\,; 0[$.
    - Si $x > 0$, $\frac{1}{x} \le 3 \iff x \ge \frac{1}{3}$.
    L'ensemble des solutions est $S = ]-\infty\,; 0[ \cup \left[\frac{1}{3}\,; +\infty\right[$.
15. $\mathcal{D}_f = \mathbb{R}$ (car $x^2 + 1 > 0$). Centré en 0.
    $f(-x) = \frac{(-x)^3}{(-x)^2 + 1} = \frac{-x^3}{x^2 + 1} = -f(x)$. La fonction est impaire.
16. $(g \circ f)(x) = g(\sqrt{x}) = \sqrt{x} + 4$, défini sur $[0\,; +\infty[$.
    $(f \circ g)(x) = f(x + 4) = \sqrt{x + 4}$, défini lorsque $x + 4 \ge 0 \iff x \ge -4$, donc sur $[-4\,; +\infty[$.
17. $|2x - 3| = 7 \iff 2x - 3 = 7$ ou $2x - 3 = -7$.
    $2x = 10 \implies x = 5$ ou $2x = -4 \implies x = -2$. $S = \{-2\,; 5\}$.
18. $|x - 5|$ est la distance entre $x$ et $5$. On cherche les réels $x$ dont la distance à $5$ est inférieure ou égale à $2$ : $5 - 2 \le x \le 5 + 2 \iff 3 \le x \le 7$. $S = [3\,; 7]$.
19. a) $p(-x) = \frac{f(-x) + f(-(-x))}{2} = \frac{f(-x) + f(x)}{2} = p(x)$, donc $p$ est paire.
    $i(-x) = \frac{f(-x) - f(-(-x))}{2} = \frac{f(-x) - f(x)}{2} = -\frac{f(x) - f(-x)}{2} = -i(x)$, donc $i$ est impaire.
    b) $p(x) + i(x) = \frac{f(x) + f(-x) + f(x) - f(-x)}{2} = \frac{2f(x)}{2} = f(x)$. Toute fonction est la somme d'une fonction paire et d'une fonction impaire !
    c) Pour $f(x) = 2x^2 - 3x + 4$ :
    $f(-x) = 2x^2 + 3x + 4$.
    $p(x) = \frac{(2x^2 - 3x + 4) + (2x^2 + 3x + 4)}{2} = 2x^2 + 4$ (partie paire).
    $i(x) = \frac{(2x^2 - 3x + 4) - (2x^2 + 3x + 4)}{2} = \frac{-6x}{2} = -3x$ (partie impaire).
20. a) Soit $x$ la largeur des deux côtés perpendiculaires. La longueur restante pour le côté opposé au mur est $40 - 2x$.
    b) Il faut $x > 0$ et $40 - 2x > 0 \iff 2x < 40 \iff x < 20$. Donc $x \in ]0\,; 20[$.
    c) Aire : $A(x) = x(40 - 2x) = 40x - 2x^2$.
    d) Développons : $-2(x - 10)^2 + 200 = -2(x^2 - 20x + 100) + 200 = -2x^2 + 40x - 200 + 200 = 40x - 2x^2 = A(x)$.
    e) Comme $(x - 10)^2 \ge 0$, $-2(x - 10)^2 \le 0$, donc $A(x) \le 200$.
    Le maximum est atteint lorsque le terme au carré s'annule, soit $x - 10 = 0 \iff x = 10\text{ m}$.
    L'aire maximale est de $200\text{ m}^2$ (dimensions : $10\text{ m} \times 20\text{ m}$).
21. a) $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2 = (\sqrt{x})^2 - 2 \times \sqrt{x} \times \frac{1}{\sqrt{x}} + \left(\frac{1}{\sqrt{x}}\right)^2 = x - 2 + \frac{1}{x}$.
    b) Un carré est toujours positif ou nul : $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2 \ge 0 \iff x - 2 + \frac{1}{x} \ge 0 \iff x + \frac{1}{x} \ge 2$.
    c) L'égalité a lieu si et seulement si $\sqrt{x} - \frac{1}{\sqrt{x}} = 0 \iff \sqrt{x} = \frac{1}{\sqrt{x}} \iff (\sqrt{x})^2 = 1 \iff x = 1$.
22. a) $x^2 = x \iff x^2 - x = 0 \iff x(x - 1) = 0 \implies x = 0$ ou $x = 1$.
    b) $\frac{1}{x} = x \iff x^2 = 1 \iff x = 1$ ou $x = -1$.
    c) $\sqrt{x} = x$ pour $x \ge 0 \iff x = x^2 \implies x = 0$ ou $x = 1$.
    d) $x^3 = x \iff x^3 - x = 0 \iff x(x^2 - 1) = 0 \iff x(x - 1)(x + 1) = 0 \implies x = 0, 1 \text{ ou } -1$.

---

### La question qui ouvre la suite

Dans l'exercice de l'éleveur, nous avons rencontré une expression remarquable : $A(x) = -2x^2 + 40x$. Pour trouver son sommet sans tâtonner, nous avons dû ruser en écrivant la fonction sous la forme $-2(x - 10)^2 + 200$.

Cette famille de courbes — les paraboles associées aux trinômes $ax^2 + bx + c$ — régit le vol des obus, le jet des fontaines et les miroirs des télescopes. Comment trouver systématiquement leurs sommets et leurs racines sans faire d'artifice au hasard ? Quel est ce mystérieux nombre $\Delta$ que les géomètres ont découvert ? C'est ce que nous allons explorer dans **La Fontaine de Galilée et la Parabole**.
