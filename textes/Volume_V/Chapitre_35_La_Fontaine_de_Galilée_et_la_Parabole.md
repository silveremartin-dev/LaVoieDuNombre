# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 35 : La Fontaine de Galilée et la Parabole

> *« Regarde l'eau jaillir de la vasque de marbre : elle s'élance avec fougue, semble hésiter un instant au sommet de son arche lumineuse, puis retombe en courbure gracieuse dans le bassin. Ce dessin parfait que la pesanteur trace dans l'air n'est pas un arc de cercle : c'est une parabole. Depuis les savants de Babylone et de Bagdad jusqu'à Galilée, l'art du second degré est la clé maîtresse qui ouvre la trajectoire des mondes. »*

---

### Ce que tu vas découvrir

- Pourquoi la trajectoire d'un jet d'eau ou d'un projectile soumis à la pesanteur forme obligatoirement une **parabole**.
- La métamorphose de l'expression : passer de la **forme développée** $ax^2 + bx + c$ à la **forme canonique** $a(x - \alpha)^2 + \beta$ grâce à la complétion du carré d'Al-Khwarizmi.
- Le **sommet** $S(\alpha\,; \beta)$ et l'axe de symétrie d'une parabole.
- Le mystère dévoilé du **discriminant** $\Delta = b^2 - 4ac$ : la démonstration pas à pas qui explique pourquoi il tranche entre 0, 1 ou 2 racines.
- La **forme factorisée** et la règle d'or du **signe du trinôme** (« du signe de $a$ à l'extérieur des racines »).
- Les formules de **Viète** reliant les racines à leur somme $S = -\frac{b}{a}$ et à leur produit $P = \frac{c}{a}$.

---

### 1. Le problème : Galilée et le jet d'eau des jardins Médicis

À Florence, au début de l'été 1608, **Galileo Galilei** se promène dans les jardins de la villa Médicis. Son regard est attiré par une fontaine monumentale. Un ajutage de cuivre incline un jet d'eau à quarante-cinq degrés : un mince filet cristallin jaillit, monte vers le ciel, s'arrondit à son zénith puis plonge dans le bassin.

À cette époque, les traités d'artillerie hérités de la physique d'Aristote prétendaient qu'un boulet de canon avançait en ligne droite sous l'effet de l'explosion, s'arrêtait net en l'air une fois l'élan épuisé, puis tombait verticalement vers le sol !

Galilée sait que cette vision est absurde. Il décompose le mouvement de chaque gouttelette d'eau en deux actions simultanées et indépendantes :
1. **À l'horizontale ($x$) :** Aucun obstacle ne freine l'eau (en négligeant le frottement de l'air). La goutte avance à vitesse constante $v_0$ :
   $$x(t) = v_0 \times t.$$
2. **À la verticale ($y$) :** La Terre attire la gouttelette vers le bas avec une accélération constante $g$. D'après la loi de la chute des corps découverte par Galilée, l'altitude diminue proportionnellement au **carré du temps écoulé** :
   $$y(t) = -\frac{1}{2}g t^2 + h_0.$$

```
       y ▲               Sommet S
         │                 ╭───╮
         │               ╭╯     ╰╮
         │             ╭╯         ╰╮   Jet d'eau
         │            ╭╯             ╰╮
         │           o                 ╰╮
       h0┼──────────►                    ▼
         O ┼──────────────────────────────┼─────► x
                                         Impact
```

Éliminons le temps $t$ ! De la première équation, nous tirons $t = \frac{x}{v_0}$. En injectant cette valeur dans la seconde équation, l'altitude $y$ en fonction de la distance horizontale $x$ devient :
$$y = -\frac{g}{2 v_0^2} x^2 + h_0.$$

C'est une équation où l'altitude dépend du **carré** de la distance parcourue : une fonction polynôme du **second degré**. La courbe obtenue n'est ni un cercle ni une ellipse : c'est une **parabole**.

Pour calculer la hauteur maximale atteinte par l'eau, ou pour savoir à quelle distance exacte le jet frappera le miroir du bassin ($y = 0$), nous avons besoin de maîtriser l'algèbre des trinômes du second degré.

---

### 2. Le trinôme du second degré et la forme canonique

#### 2.1 Définitions et forme développée

> **📐 Définition — Fonction polynôme du second degré.**
> On appelle **fonction polynôme du second degré** (ou **trinôme du second degré**) toute fonction $f$ définie sur $\mathbb{R}$ par :
> $$f(x) = ax^2 + bx + c$$
> où $a, b, c$ sont des nombres réels fixés, avec **$a \neq 0$**.
> Cette écriture est appelée la **forme développée** du trinôme.

- Le terme $a$ est le coefficient de degré 2 (il est obligatoire que $a \neq 0$, sinon l'expression deviendrait affine $bx + c$).
- Le terme $b$ est le coefficient de degré 1.
- Le terme $c$ est le terme constant (l'ordonnée à l'origine, car $f(0) = c$).

#### 2.2 La complétion du carré : l'héritage d'Al-Khwarizmi

Comment trouver le sommet d'une parabole sans tâtonner ?
L'idée géniale remonte au mathématicien persan **Al-Khwarizmi** (vers 820 à Bagdad) : il s'agit de reconstituer géométriquement un carré parfait pour que la variable $x$ n'apparaisse plus qu'**une seule fois** dans toute l'expression !

> **📐 Théorème fondamental — La forme canonique.**
> Tout trinôme $f(x) = ax^2 + bx + c$ ($a \neq 0$) peut s'écrire de manière unique sous la **forme canonique** :
> $$\boxed{f(x) = a(x - \alpha)^2 + \beta}$$
> avec :
> $$\alpha = -\frac{b}{2a} \quad \text{et} \quad \beta = f(\alpha) = -\frac{b^2 - 4ac}{4a}.$$

> **✍️ Démonstration (exigible) — Mise sous forme canonique.**
> Partons de la forme développée :
> $$f(x) = ax^2 + bx + c.$$
> 1. Factorisons le coefficient $a \neq 0$ dans les deux premiers termes :
>    $$f(x) = a\left[ x^2 + \frac{b}{a}x \right] + c.$$
> 2. Regardons l'expression entre crochets : $x^2 + \frac{b}{a}x$ ressemble au début du développement d'une identité remarquable $(x + d)^2 = x^2 + 2dx + d^2$.
>    Pour que le double produit $2dx$ soit égal à $\frac{b}{a}x$, il faut choisir $d = \frac{b}{2a}$.
>    On a alors :
>    $$\left(x + \frac{b}{2a}\right)^2 = x^2 + 2\left(\frac{b}{2a}\right)x + \left(\frac{b}{2a}\right)^2 = x^2 + \frac{b}{a}x + \frac{b^2}{4a^2}.$$
>    On en déduit que :
>    $$x^2 + \frac{b}{a}x = \left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2}.$$
> 3. Remplaçons cette égalité dans l'expression de $f(x)$ :
>    $$f(x) = a\left[ \left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} \right] + c.$$
> 4. Développons le crochet par $a$ :
>    $$f(x) = a\left(x + \frac{b}{2a}\right)^2 - a \times \frac{b^2}{4a^2} + c = a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a} + \frac{4ac}{4a}.$$
> 5. Regroupons les deux derniers termes au même dénominateur $4a$ :
>    $$f(x) = a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a}.$$
> En posant $\alpha = -\frac{b}{2a}$ et $\beta = -\frac{b^2 - 4ac}{4a}$, on obtient la forme canonique :
> $$f(x) = a(x - \alpha)^2 + \beta. \quad \blacksquare$$

---

### 3. Géométrie de la parabole : sommet et axe de symétrie

Grâce à la forme canonique $f(x) = a(x - \alpha)^2 + \beta$, les propriétés géométriques de la courbe deviennent transparentes :
Puisqu'un carré est toujours positif ou nul :
$$(x - \alpha)^2 \ge 0 \quad \text{pour tout } x \in \mathbb{R},$$
avec égalité si et seulement si $x = \alpha$.

Deux cas se présentent selon le signe de $a$ :

```
             CAS a > 0                                CAS a < 0
      (Branches vers le HAUT)                  (Branches vers le BAS)
             y ▲                                      y ▲
           \   │   /                                    │      Sommet S(α, β)
            \  │  /                                     │        ╭───╮
             \ │ /                                    β ┼───────╭╯   ╰╮
              \│/                                       │      ╭╯     ╰╮
             β ┼───o Sommet S(α, β)                     │     ╭╯       ╰╮
               │   │                                    │    /           \
             O ┼───┼───────► x                        O ┼───┼─────────────► x
                   α                                        α
```

1. **Si $a > 0$ :**
   $a(x - \alpha)^2 \ge 0$, donc $f(x) \ge \beta$.
   La fonction admet un **minimum absolu** égal à $\beta$, atteint en $x = \alpha$.
   La parabole a ses **branches tournées vers le haut** (forme de cuvette).
   $f$ est strictement décroissante sur $]-\infty\,; \alpha]$ et strictement croissante sur $[\alpha\,; +\infty[$.

2. **Si $a < 0$ :**
   $a(x - \alpha)^2 \le 0$, donc $f(x) \le \beta$.
   La fonction admet un **maximum absolu** égal à $\beta$, atteint en $x = \alpha$.
   La parabole a ses **branches tournées vers le bas** (forme de colline).
   $f$ est strictement croissante sur $]-\infty\,; \alpha]$ et strictement décroissante sur $[\alpha\,; +\infty[$.

> **📐 Propriétés fondamentales de la parabole —**
> - Le **sommet** de la parabole est le point $S(\alpha\,; \beta)$ avec $\alpha = -\frac{b}{2a}$ et $\beta = f(\alpha)$.
> - La droite verticale d'équation $x = \alpha$ est l'**axe de symétrie** de la parabole.

---

### 4. L'équation du second degré et le discriminant $\Delta$

Résoudre l'équation $ax^2 + bx + c = 0$ revient géométriquement à chercher les points où la parabole traverse l'axe des abscisses ($y = 0$).

#### 4.1 La naissance du discriminant

Reprenons l'étape 3 de la mise sous forme canonique :
$$a\left[ \left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a^2} \right] = 0.$$
Puisque $a \neq 0$, cette équation équivaut à :
$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}.$$

Le membre de gauche est un carré : il est toujours positif ou nul.
Le dénominateur du membre de droite, $4a^2 = (2a)^2$, est strictement positif.
Tout dépend donc exclusivement du signe du numérateur :
$$\Delta = b^2 - 4ac.$$

> **📐 Définition — Discriminant.**
> Le nombre réel $\Delta = b^2 - 4ac$ est appelé le **discriminant** du trinôme $ax^2 + bx + c$.
> La lettre grecque $\Delta$ (« delta » majuscule) a été choisie par les mathématiciens du XIXᵉ siècle car elle est l'initiale de *discriminare* en latin, qui signifie « séparer », « distinguer ». Il discrimine les cas possibles.

#### 4.2 Les trois cas fondamentaux

> **📐 Théorème fondamental — Résolution de $ax^2 + bx + c = 0$.**
> 
> 1. **Si $\Delta < 0$ :**
>    Le membre de droite $\frac{\Delta}{4a^2}$ est strictement négatif. Or un carré réel ne peut jamais être négatif.
>    L'équation n'a **aucune solution réelle** ($S = \varnothing$).
>    La parabole ne touche jamais l'axe des abscisses.
> 
> 2. **Si $\Delta = 0$ :**
>    L'équation devient $\left(x + \frac{b}{2a}\right)^2 = 0$, d'où $x + \frac{b}{2a} = 0$.
>    L'équation admet **une unique solution réelle** (appelée racine double) :
>    $$x_0 = -\frac{b}{2a}.$$
>    Le sommet de la parabole repose exactement sur l'axe des abscisses (la droite est tangente à la courbe).
> 
> 3. **Si $\Delta > 0$ :**
>    Le nombre $\Delta$ admet une racine carrée réelle $\sqrt{\Delta} > 0$.
>    L'égalité devient :
>    $$\left(x + \frac{b}{2a}\right)^2 - \left(\frac{\sqrt{\Delta}}{2a}\right)^2 = 0.$$
>    Par identité remarquable $A^2 - B^2 = (A - B)(A + B)$ :
>    $$\left(x + \frac{b}{2a} - \frac{\sqrt{\Delta}}{2a}\right)\left(x + \frac{b}{2a} + \frac{\sqrt{\Delta}}{2a}\right) = 0.$$
>    D'après la règle du produit nul, l'équation admet **deux solutions réelles distinctes** :
>    $$\boxed{x_1 = \frac{-b - \sqrt{\Delta}}{2a}} \quad \text{et} \quad \boxed{x_2 = \frac{-b + \sqrt{\Delta}}{2a}}.$$
>    La parabole coupe l'axe des abscisses en deux points distincts d'abscisses $x_1$ et $x_2$.

---

### 5. Forme factorisée et signe du trinôme

#### 5.1 La forme factorisée

Connaissant les racines d'un trinôme, on peut l'écrire sous forme d'un produit de facteurs du premier degré :

> **📐 Théorème — Forme factorisée.**
> - Si $\Delta > 0$ : $f(x) = a(x - x_1)(x - x_2)$.
> - Si $\Delta = 0$ : $f(x) = a(x - x_0)^2$.
> - Si $\Delta < 0$ : $f(x)$ ne peut pas se factoriser en produit de facteurs du premier degré dans $\mathbb{R}$.

> **⚠️ Attention, piège ! Ne jamais oublier le facteur $a$ !**
> C'est l'erreur la plus fréquente : écrire $(x - x_1)(x - x_2)$ en oubliant de multiplier par le coefficient $a$ devant.
> Par exemple, $2x^2 - 6x + 4 = 0$ a pour racines $1$ et $2$. Sa forme factorisée est $2(x - 1)(x - 2)$, et non pas $(x - 1)(x - 2)$ (qui donnerait $x^2 - 3x + 2$).

#### 5.2 Le signe du trinôme

> **📐 Règle d'or — Signe de $ax^2 + bx + c$.**
> 
> 1. **Si $\Delta < 0$ :**
>    Le trinôme ne s'annule jamais. Il est **toujours du signe de $a$** sur tout $\mathbb{R}$.
> 
> 2. **Si $\Delta = 0$ :**
>    Le trinôme s'annule en $x_0 = -\frac{b}{2a}$ et est **du signe de $a$ partout ailleurs**.
> 
> 3. **Si $\Delta > 0$ :** (en supposant $x_1 < x_2$)
>    Le trinôme est :
>    - **du signe de $a$ à l'extérieur des racines** (pour $x < x_1$ et pour $x > x_2$) ;
>    - **du signe opposé de $a$ (signe de $-a$) entre les racines** (pour $x_1 < x < x_2$).

> **Tableau de signes récapitulatif pour $\Delta > 0$ :**
>
> | $x$ | $-\infty$ | | $x_1$ | | $x_2$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | Signe de $ax^2+bx+c$ | | **signe de $a$** | $0$ | **signe de $-a$** | $0$ | **signe de $a$** | |

**Intuition géométrique éclatante :**
Si $a > 0$, la parabole a les bras levés vers le ciel. Pour descendre sous l'axe des abscisses, elle doit plonger entre les deux racines : la cuvette est sous l'axe (négative) uniquement *entre* $x_1$ et $x_2$. Partout ailleurs, elle est au-dessus (positive) !

---

### 6. Les relations de Viète : somme et produit des racines

En 1591, le juriste et conseiller secret d'Henri IV, **François Viète**, découvre des liens fascinants reliant directement les coefficients d'un polynôme à ses racines, sans passer par le calcul de $\Delta$.

> **📐 Théorème (Formules de Viète) —**
> Si le trinôme $ax^2 + bx + c$ admet deux racines réelles $x_1$ et $x_2$ (éventuellement confondues), alors :
> $$\boxed{S = x_1 + x_2 = -\frac{b}{a}} \quad \text{et} \quad \boxed{P = x_1 \times x_2 = \frac{c}{a}}.$$

> **✍️ Démonstration —**
> Développons la forme factorisée $a(x - x_1)(x - x_2)$ :
> $$a(x - x_1)(x - x_2) = a\left[ x^2 - (x_1 + x_2)x + x_1 x_2 \right] = ax^2 - a(x_1 + x_2)x + a(x_1 x_2).$$
> Par identification avec la forme développée $ax^2 + bx + c$ :
> $$-a(x_1 + x_2) = b \implies x_1 + x_2 = -\frac{b}{a},$$
> $$a(x_1 x_2) = c \implies x_1 x_2 = \frac{c}{a}. \quad \blacksquare$$

#### 6.1 Trouver deux nombres connaissant leur somme et leur produit

Deux nombres $u$ et $v$ ont pour somme $S$ et pour produit $P$ si et seulement s'ils sont les solutions de l'équation :
$$\boxed{X^2 - SX + P = 0}$$

#### 6.2 L'art de repérer les racines évidentes

Avant de te précipiter sur le discriminant, cherche toujours s'il existe une **racine évidente** :
- **Si $a + b + c = 0$**, alors $x_1 = 1$ est racine évidente. La seconde racine vaut alors immédiatement $x_2 = \frac{c}{a}$.
- **Si $a - b + c = 0$**, alors $x_1 = -1$ est racine évidente. La seconde racine vaut $x_2 = -\frac{c}{a}$.
- **Si $c = 0$**, alors $x_1 = 0$ est racine évidente, et $x_2 = -\frac{b}{a}$.

---

### 7. Exemples résolus détaillés

> **Exemple résolu 1 — Mise sous forme canonique pratique.**
> Mettre sous forme canonique le trinôme $P(x) = 2x^2 - 8x + 11$.
> En déduire le sommet de la parabole et son extremum.
>
> **Solution :**
> 1. Factorisons le coefficient $a = 2$ sur les termes en $x$ :
>    $$P(x) = 2(x^2 - 4x) + 11.$$
> 2. Complétons le carré : $x^2 - 4x = (x - 2)^2 - 4$.
> 3. Remplaçons :
>    $$P(x) = 2\left[(x - 2)^2 - 4\right] + 11 = 2(x - 2)^2 - 8 + 11 = 2(x - 2)^2 + 3.$$
> **Conclusion :**
> La forme canonique est $\boxed{P(x) = 2(x - 2)^2 + 3}$.
> Ici $\alpha = 2$ et $\beta = 3$.
> Le sommet de la parabole est le point $S(2\,; 3)$.
> Comme $a = 2 > 0$, la fonction admet un **minimum absolu valant $3$**, atteint en $x = 2$.
> (Remarque : comme son minimum est $3 > 0$, la parabole ne descend jamais sous 0, donc $P(x) = 0$ n'a aucune solution réelle).

> **Exemple résolu 2 — Résolution d'équations avec le discriminant.**
> Résoudre dans $\mathbb{R}$ les trois équations suivantes :
> a) $3x^2 - 5x - 2 = 0$ \quad b) $4x^2 - 12x + 9 = 0$ \quad c) $2x^2 + 3x + 5 = 0$
>
> **Solution pas à pas :**
> a) $a = 3, b = -5, c = -2$.
>    $$\Delta = b^2 - 4ac = (-5)^2 - 4(3)(-2) = 25 + 24 = 49.$$
>    Comme $\Delta = 49 > 0$, il y a deux solutions réelles distinctes ($\sqrt{\Delta} = 7$) :
>    $$x_1 = \frac{-(-5) - 7}{2(3)} = \frac{5 - 7}{6} = \frac{-2}{6} = -\frac{1}{3},$$
>    $$x_2 = \frac{-(-5) + 7}{2(3)} = \frac{5 + 7}{6} = \frac{12}{6} = 2.$$
>    $S = \left\{-\frac{1}{3} \,;\, 2\right\}$. Forme factorisée : $3\left(x + \frac{1}{3}\right)(x - 2) = (3x + 1)(x - 2)$.
>
> b) $a = 4, b = -12, c = 9$.
>    $$\Delta = (-12)^2 - 4(4)(9) = 144 - 144 = 0.$$
>    Comme $\Delta = 0$, il y a une unique racine double :
>    $$x_0 = -\frac{b}{2a} = -\frac{-12}{2(4)} = \frac{12}{8} = \frac{3}{2}.$$
>    $S = \left\{\frac{3}{2}\right\}$. Forme factorisée : $4\left(x - \frac{3}{2}\right)^2 = (2x - 3)^2$.
>
> c) $a = 2, b = 3, c = 5$.
>    $$\Delta = 3^2 - 4(2)(5) = 9 - 40 = -31 < 0.$$
>    Comme $\Delta < 0$, l'équation n'a aucune solution réelle : $S = \varnothing$.

> **Exemple résolu 3 — Résolution d'une inéquation du second degré.**
> Résoudre dans $\mathbb{R}$ l'inéquation :
> $$-2x^2 + 7x - 3 \ge 0.$$
>
> **Solution :**
> 1. Cherchons d'abord les racines du trinôme :
>    $$\Delta = 7^2 - 4(-2)(-3) = 49 - 24 = 25 > 0 \implies \sqrt{\Delta} = 5.$$
>    $$x_1 = \frac{-7 - 5}{2(-2)} = \frac{-12}{-4} = 3, \quad x_2 = \frac{-7 + 5}{2(-2)} = \frac{-2}{-4} = \frac{1}{2}.$$
> 2. Appliquons la règle du signe du trinôme :
>    Ici, $a = -2 < 0$.
>    Le trinôme est du signe de $a$ (donc négatif) à l'extérieur des racines, et du signe opposé (donc positif) entre les racines.
> 3. Tableau de signes :
>
> | $x$ | $-\infty$ | | $\frac{1}{2}$ | | $3$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $-2x^2+7x-3$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
>
> On veut que l'expression soit $\ge 0$.
> L'ensemble des solutions est donc l'intervalle fermé : $\boxed{S = \left[\frac{1}{2}\,; 3\right]}$.

> **Exemple résolu 4 — Utilisation des racines évidentes et de Viète.**
> Résoudre mentalement l'équation $15x^2 - 2x - 17 = 0$.
>
> **Solution :**
> Testons la somme des coefficients :
> $a = 15, b = -2, c = -17$.
> Calculons $a - b + c = 15 - (-2) + (-17) = 15 + 2 - 17 = 0$.
> D'après le §6.2, $x_1 = -1$ est une racine évidente !
> Le produit des racines est $P = x_1 x_2 = \frac{c}{a} = -\frac{17}{15}$.
> Puisque $x_1 = -1$, on a $(-1) \times x_2 = -\frac{17}{15} \implies x_2 = \frac{17}{15}$.
> Les solutions sont donc instantanément $\boxed{S = \left\{-1 \,;\, \frac{17}{15}\right\}}$, sans poser aucun calcul de discriminant !

> **Exemple résolu 5 — Trouver deux dimensions à partir du périmètre et de l'aire.**
> Un terrain rectangulaire a un demi-périmètre de $29\text{ mètres}$ et une superficie de $198\text{ m}^2$.
> Quelles sont les dimensions de ce terrain ?
>
> **Solution :**
> Soient $L$ et $\ell$ la longueur et la largeur.
> On connaît leur somme $S = L + \ell = 29$ et leur produit $P = L \times \ell = 198$.
> D'après le théorème de Viète, $L$ et $\ell$ sont les solutions de l'équation :
> $$X^2 - 29X + 198 = 0.$$
> Calculons le discriminant :
> $$\Delta = (-29)^2 - 4(1)(198) = 841 - 792 = 49 > 0.$$
> $\sqrt{\Delta} = 7$.
> Les solutions sont :
> $$X_1 = \frac{29 - 7}{2} = \frac{22}{2} = 11, \quad X_2 = \frac{29 + 7}{2} = \frac{36}{2} = 18.$$
> Les dimensions du terrain sont donc de **$18\text{ mètres}$ sur $11\text{ mètres}$**.
> *(Vérification : demi-périmètre $18 + 11 = 29\text{ m}$ ; aire $18 \times 11 = 198\text{ m}^2$).*

> **Exemple résolu 6 — Équation bicarrée se ramenant au second degré.**
> Résoudre dans $\mathbb{R}$ l'équation :
> $$x^4 - 5x^2 - 36 = 0.$$
>
> **Solution :**
> Cette équation est de degré 4, mais elle ne contient que des puissances paires ($x^4 = (x^2)^2$).
> Faisons le **changement de variable** : posons $X = x^2$ (avec la contrainte indispensable $X \ge 0$).
> L'équation devient une équation du second degré en $X$ :
> $$X^2 - 5X - 36 = 0.$$
> Calculons le discriminant :
> $$\Delta = (-5)^2 - 4(1)(-36) = 25 + 144 = 169 = 13^2.$$
> Les racines en $X$ sont :
> $$X_1 = \frac{5 - 13}{2} = \frac{-8}{2} = -4, \quad X_2 = \frac{5 + 13}{2} = \frac{18}{2} = 9.$$
> Revenons maintenant à la variable d'origine $x$ :
> - Pour $X_1 = -4$ : l'équation $x^2 = -4$ n'a aucune solution réelle car un carré est positif.
> - Pour $X_2 = 9$ : l'équation $x^2 = 9$ donne immédiatement $x = -3$ ou $x = 3$.
> L'ensemble des solutions réelles de l'équation de départ est $\boxed{S = \{-3\,; 3\}}$.

---

### 8. En informatique : le résolveur de second degré en Python

Voici un script Python qui implémente l'algorithme complet d'analyse d'un trinôme :

```python
import math

def analyser_trinome(a, b, c):
    """Analyse complète du trinôme a*x^2 + b*x + c."""
    if a == 0:
        return "Erreur : ce n'est pas un trinôme du second degré (a = 0)."
    
    # 1. Sommet de la parabole
    alpha = -b / (2 * a)
    beta = a * alpha**2 + b * alpha + c
    print(f"Sommet S: ({alpha:.3f}, {beta:.3f})")
    print(f"Orientation : branches tournées vers le {'HAUT' if a > 0 else 'BAS'}")
    
    # 2. Discriminant
    delta = b**2 - 4 * a * c
    print(f"Discriminant Delta = {delta}")
    
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Deux racines distinctes : x1 = {x1:.3f} et x2 = {x2:.3f}")
        print(f"Forme factorisée : {a} * (x - {x1:.3f}) * (x - {x2:.3f})")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Une racine double : x0 = {x0:.3f}")
        print(f"Forme factorisée : {a} * (x - {x0:.3f})^2")
    else:
        print("Aucune racine réelle.")
        print("Pas de factorisation dans R.")

# Exemple d'appel : 2x^2 - 7x + 3
analyser_trinome(2, -7, 3)
```

---

### Ce qu'il faut retenir

1. **Forme développée :** $f(x) = ax^2 + bx + c$ ($a \neq 0$).
2. **Forme canonique :** $f(x) = a(x - \alpha)^2 + \beta$ avec :
   $$\alpha = -\frac{b}{2a} \quad \text{et} \quad \beta = f(\alpha) = -\frac{\Delta}{4a}.$$
   - Sommet de la parabole : $S(\alpha\,; \beta)$.
   - Axe de symétrie : $x = \alpha$.
   - Branches vers le haut si $a > 0$ (minimum $\beta$), vers le bas si $a < 0$ (maximum $\beta$).
3. **Discriminant $\Delta = b^2 - 4ac$ :**
   - $\Delta > 0$ : 2 racines distinctes $x_1 = \frac{-b-\sqrt{\Delta}}{2a}$ et $x_2 = \frac{-b+\sqrt{\Delta}}{2a}$.
   - $\Delta = 0$ : 1 racine double $x_0 = -\frac{b}{2a}$.
   - $\Delta < 0$ : 0 racine réelle.
4. **Forme factorisée :**
   - Si $\Delta > 0$ : $a(x - x_1)(x - x_2)$.
   - Si $\Delta = 0$ : $a(x - x_0)^2$.
5. **Signe du trinôme :**
   - Toujours du signe de $a$, **sauf entre les racines** (si $\Delta > 0$) où il est du signe de $-a$.
6. **Relations de Viète :**
   $$S = x_1 + x_2 = -\frac{b}{a}, \quad P = x_1 x_2 = \frac{c}{a}, \quad X^2 - SX + P = 0.$$

---

### Exercices

#### Exercices d'application directe (★)

1. Calculer le discriminant $\Delta$ du trinôme $f(x) = x^2 - 6x + 8$.
2. Calculer le discriminant $\Delta$ du trinôme $g(x) = 2x^2 + 4x + 5$.
3. Déterminer les coordonnées du sommet $S$ de la parabole d'équation $y = 3(x - 4)^2 + 7$.
4. Déterminer les coordonnées du sommet $S$ de la parabole d'équation $y = -2x^2 + 8x - 3$.
5. Résoudre dans $\mathbb{R}$ l'équation $x^2 - 9x + 20 = 0$.
6. Résoudre dans $\mathbb{R}$ l'équation $x^2 + 2x + 1 = 0$.
7. Résoudre dans $\mathbb{R}$ l'équation $3x^2 + x + 2 = 0$.
8. Donner la forme factorisée de $2x^2 - 10x + 12$.
9. Donner le tableau de signes du trinôme $P(x) = x^2 - 4x - 5$.
10. Trouver mentalement les racines de $2x^2 + 3x - 5 = 0$ à l'aide des racines évidentes.

#### Exercices d'entraînement et de réflexion (★★)

11. Mettre sous forme canonique les trinômes :
    a) $f(x) = x^2 - 10x + 21$ \quad b) $g(x) = -3x^2 + 12x - 7$
12. Résoudre dans $\mathbb{R}$ les inéquations :
    a) $x^2 - 5x + 6 \le 0$ \quad b) $-x^2 + 2x + 8 > 0$ \quad c) $2x^2 - 3x + 5 > 0$
13. Trouver deux nombres réels connaissant leur somme $S = 13$ et leur produit $P = 40$.
14. Pour quelles valeurs du paramètre réel $m$ l'équation $x^2 + (m + 1)x + 4 = 0$ admet-elle une racine double ?
15. Résoudre l'équation rationnelle : $\frac{2x - 1}{x + 1} = \frac{x + 2}{x - 1}$.
16. Résoudre dans $\mathbb{R}$ l'équation bicarrée : $x^4 - 13x^2 + 36 = 0$.
17. Une balle de tennis est frappée à une hauteur de $1\text{ mètre}$. Sa trajectoire est donnée par $h(x) = -0{,}05x^2 + 0{,}8x + 1$, où $x$ est la distance horizontale parcourue en mètres et $h(x)$ la hauteur en mètres.
    a) Quelle est la hauteur maximale atteinte par la balle ?
    b) À quelle distance horizontale la balle retombe-t-elle au sol ($h(x) = 0$) ?
18. Déterminer les points d'intersection entre la parabole d'équation $y = x^2 - 3x + 2$ et la droite d'équation $y = 2x - 4$.

#### Exercices d'approfondissement et défis (★★★)

19. **La formule du discriminant réduit $\Delta'$.**
    Lorsque le coefficient $b$ est pair, on peut poser $b = 2b'$.
    a) Démontrer que $\Delta = 4(b'^2 - ac)$.
    b) En posant $\Delta' = b'^2 - ac$, démontrer que les racines s'écrivent simplement $x = \frac{-b' \pm \sqrt{\Delta'}}{a}$.
    c) Utiliser cette formule allégée pour résoudre $x^2 - 14x + 45 = 0$ et $5x^2 - 6x - 8 = 0$.
20. **Position relative de deux paraboles.**
    On considère les paraboles $\mathcal{P}_1 : y = x^2 - 4x + 3$ et $\mathcal{P}_2 : y = -x^2 + 2x + 11$.
    a) Déterminer les abscisses des points d'intersection de ces deux courbes.
    b) Étudier le signe de la différence et en déduire sur quel intervalle $\mathcal{P}_1$ est située au-dessous de $\mathcal{P}_2$.
21. **Optimisation d'un maître nageur.**
    Un maître-nageur délimite une zone de baignade rectangulaire le long d'une plage rectiligne à l'aide d'une ligne de bouées de $160\text{ mètres}$ de long (le côté plage n'est pas balisé).
    Quelles doivent être les dimensions de la zone pour que la surface de baignade soit la plus grande possible ?
22. **La boîte sans couvercle de Tartaglia.**
    Dans une plaque de carton carrée de $30\text{ cm}$ de côté, on découpe quatre petits carrés identiques de côté $x$ aux quatre coins, puis on relève les bords pour former une boîte rectangulaire sans couvercle.
    a) Quelles sont les valeurs possibles pour $x$ ?
    b) Exprimer le volume $V(x)$ de la boîte en fonction de $x$.
    c) Développer l'expression et chercher pour quelle valeur entière de $x$ le volume semble maximal en testant $x = 1, 2, 3, 4, 5, 6$.

---

### Solutions

1. $\Delta = (-6)^2 - 4(1)(8) = 36 - 32 = 4$.
2. $\Delta = 4^2 - 4(2)(5) = 16 - 40 = -24$.
3. L'équation est déjà sous forme canonique : le sommet est directement $S(4\,; 7)$.
4. $\alpha = -\frac{b}{2a} = -\frac{8}{2(-2)} = 2$. $\beta = -2(2)^2 + 8(2) - 3 = -8 + 16 - 3 = 5$. Donc $S(2\,; 5)$.
5. $\Delta = (-9)^2 - 4(1)(20) = 81 - 80 = 1$. $x_1 = \frac{9 - 1}{2} = 4, x_2 = \frac{9 + 1}{2} = 5$. $S = \{4\,; 5\}$.
6. Identité remarquable : $(x + 1)^2 = 0 \implies x_0 = -1$. $S = \{-1\}$.
7. $\Delta = 1^2 - 4(3)(2) = 1 - 24 = -23 < 0$. Aucune solution réelle : $S = \varnothing$.
8. Racines de $2x^2 - 10x + 12 = 0$ : $\Delta = 100 - 96 = 4$. $x_1 = 2, x_2 = 3$. Forme factorisée : $2(x - 2)(x - 3)$.
9. Racines de $x^2 - 4x - 5$ : $a - b + c = 1 - (-4) - 5 = 0 \implies x_1 = -1$ et $x_2 = 5$.
   Comme $a = 1 > 0$, le trinôme est négatif entre $-1$ et $5$, et positif à l'extérieur :
   positif sur $]-\infty\,; -1[ \cup ]5\,; +\infty[$, nul en $-1$ et $5$, négatif sur $]-1\,; 5[$.
10. $a + b + c = 2 + 3 - 5 = 0 \implies x_1 = 1$.
    Produit $P = \frac{c}{a} = -\frac{5}{2}$, donc $x_2 = -\frac{5}{2} = -2{,}5$. $S = \left\{-\frac{5}{2} \,;\, 1\right\}$.
11. a) $x^2 - 10x + 21 = (x - 5)^2 - 25 + 21 = (x - 5)^2 - 4$.
    b) $-3x^2 + 12x - 7 = -3(x^2 - 4x) - 7 = -3[(x - 2)^2 - 4] - 7 = -3(x - 2)^2 + 12 - 7 = -3(x - 2)^2 + 5$.
12. a) Racines : $2$ et $3$. $a = 1 > 0$. Négatif entre les racines : $S = [2\,; 3]$.
    b) $-x^2 + 2x + 8 = 0 \implies \Delta = 4 - 4(-1)(8) = 36$. Racines : $x_1 = \frac{-2 - 6}{-2} = 4, x_2 = \frac{-2 + 6}{-2} = -2$.
       $a = -1 < 0$, donc positif entre les racines : $S = ]-2\,; 4[$.
    c) $\Delta = 9 - 4(2)(5) = -31 < 0$. Comme $a = 2 > 0$, le trinôme est strictement positif pour tout $x \in \mathbb{R}$ : $S = \mathbb{R}$.
13. Équation $X^2 - 13X + 40 = 0$. $\Delta = 169 - 160 = 9$.
    $X_1 = \frac{13 - 3}{2} = 5, X_2 = \frac{13 + 3}{2} = 8$. Les nombres sont $5$ et $8$.
14. Racine double $\iff \Delta = 0$.
    $\Delta = (m + 1)^2 - 4(1)(4) = (m + 1)^2 - 16 = 0 \iff (m + 1)^2 = 16 \iff m + 1 = 4$ ou $m + 1 = -4$.
    Donc $m = 3$ ou $m = -5$.
15. Valeurs interdites : $x \neq -1$ et $x \neq 1$.
    Produit en croix : $(2x - 1)(x - 1) = (x + 2)(x + 1)$.
    $2x^2 - 3x + 1 = x^2 + 3x + 2 \iff x^2 - 6x - 1 = 0$.
    $\Delta = 36 - 4(1)(-1) = 40$. $x = \frac{6 \pm 2\sqrt{10}}{2} = 3 \pm \sqrt{10}$.
    Comme ces deux nombres sont distincts de $1$ et $-1$, $S = \{3 - \sqrt{10} \,;\, 3 + \sqrt{10}\}$.
16. Posons $X = x^2 \ge 0$. $X^2 - 13X + 36 = 0$.
    $\Delta = 169 - 144 = 25$. $X_1 = \frac{13 - 5}{2} = 4, X_2 = \frac{13 + 5}{2} = 9$.
    $x^2 = 4 \implies x = \pm 2$ ; $x^2 = 9 \implies x = \pm 3$. $S = \{-3\,; -2\,; 2\,; 3\}$.
17. a) Sommet : $\alpha = -\frac{0{,}8}{2(-0{,}05)} = \frac{0{,}8}{0{,}1} = 8\text{ mètres}$.
       Hauteur maximale : $\beta = h(8) = -0{,}05(64) + 0{,}8(8) + 1 = -3{,}2 + 6{,}4 + 1 = 4{,}2\text{ mètres}$.
    b) $h(x) = 0 \iff -0{,}05x^2 + 0{,}8x + 1 = 0$. Multiplions par $-20$ : $x^2 - 16x - 20 = 0$.
       $\Delta = 256 + 80 = 336$. $\sqrt{336} \approx 18{,}33$.
       $x = \frac{16 + 18{,}33}{2} \approx 17{,}17\text{ mètres}$ (l'autre racine est négative). La balle retombe à environ $17{,}17\text{ m}$.
18. $x^2 - 3x + 2 = 2x - 4 \iff x^2 - 5x + 6 = 0 \iff (x - 2)(x - 3) = 0$.
    Abscisses : $x = 2$ et $x = 3$.
    Ordonnées : pour $x = 2$, $y = 2(2) - 4 = 0$ ; pour $x = 3$, $y = 2(3) - 4 = 2$.
    Points d'intersection : $A(2\,; 0)$ et $B(3\,; 2)$.
19. a) $\Delta = (2b')^2 - 4ac = 4b'^2 - 4ac = 4(b'^2 - ac)$.
    b) $\sqrt{\Delta} = 2\sqrt{b'^2 - ac} = 2\sqrt{\Delta'}$.
       $x = \frac{-2b' \pm 2\sqrt{\Delta'}}{2a} = \frac{-b' \pm \sqrt{\Delta'}}{a}$.
    c) Pour $x^2 - 14x + 45 = 0$ : $b' = -7$, $\Delta' = 49 - 45 = 4$. $x = 7 \pm 2 \implies S = \{5\,; 9\}$.
       Pour $5x^2 - 6x - 8 = 0$ : $b' = -3$, $\Delta' = 9 - 5(-8) = 49$. $x = \frac{3 \pm 7}{5} \implies S = \{-0{,}8 \,;\, 2\}$.
20. a) $x^2 - 4x + 3 = -x^2 + 2x + 11 \iff 2x^2 - 6x - 8 = 0 \iff x^2 - 3x - 4 = 0$.
       Racines évidentes ($a - b + c = 1 - (-3) - 4 = 0$) : $x_1 = -1$ et $x_2 = 4$.
    b) $\mathcal{P}_1$ est au-dessous de $\mathcal{P}_2 \iff \mathcal{P}_1 - \mathcal{P}_2 \le 0 \iff 2(x + 1)(x - 4) \le 0$.
       Comme le coefficient $2 > 0$, l'expression est négative entre les racines : sur $[-1\,; 4]$.
21. Soit $x$ la largeur des deux côtés perpendiculaires à la plage. La longueur est $160 - 2x$.
    Aire : $A(x) = x(160 - 2x) = -2x^2 + 160x$.
    C'est un trinôme avec $a = -2 < 0$. Son maximum est atteint au sommet :
    $x = -\frac{160}{2(-2)} = 40\text{ mètres}$.
    La longueur est alors $160 - 2(40) = 80\text{ mètres}$.
    Dimensions optimales : $40\text{ m} \times 80\text{ m}$ (aire maximale : $3200\text{ m}^2$).
22. a) $x > 0$ et $2x < 30 \iff x < 15$. Donc $x \in ]0\,; 15[$.
    b) La base est un carré de côté $30 - 2x$ et la hauteur est $x$.
       $V(x) = x(30 - 2x)^2 = x(900 - 120x + 4x^2) = 4x^3 - 120x^2 + 900x$.
    c) Calculons pour quelques valeurs :
       $V(1) = 1(28)^2 = 784\text{ cm}^3$ ;
       $V(3) = 3(24)^2 = 1728\text{ cm}^3$ ;
       $V(5) = 5(20)^2 = 2000\text{ cm}^3$ ;
       $V(6) = 6(18)^2 = 1944\text{ cm}^3$.
       Le volume semble maximal pour $x = 5\text{ cm}$, atteignant $2000\text{ cm}^3$ (soit 2 litres !).

---

### La question qui ouvre la suite

Le second degré nous a appris à prédire l'arche continue d'un jet d'eau dans l'espace. Mais dans le monde réel, tous les phénomènes ne s'écoulent pas comme un fleuve continu :
- Un compte bancaire produit des intérêts à chaque fin de mois ;
- Une colonie de bactéries double à chaque heure ;
- Un escalier se gravit marche par marche, $0, 1, 2, 3\dots$

Comment étudier une quantité qui progresse par bonds successifs dans le temps ? Comment calculer la somme de mille marches sans s'épuiser ? C'est ce que nous allons découvrir dans **Les Marches de l'Escalier et le Prêt de l'Usurier**.
