# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 40 : La Colonie de Bactéries

> *« Dans le monde inerte des pierres, la vitesse dépend d'une force extérieure qu'on applique. Dans le monde ardent du vivant, la force naît du nombre : chaque cellule est son propre moteur. Plus la colonie grandit, plus elle explose vite. La nature a choisi une unique courbe pour chanter la prolifération de la vie : la fonction exponentielle. »*

---

### Ce que tu vas découvrir

- Le secret biologique de la prolifération : pourquoi la vitesse de croissance d'une population est proportionnelle à son effectif.
- La naissance d'une équation révolutionnaire : $f' = f$ avec $f(0) = 1$.
- La **méthode d'Euler** : comment tracer la courbe pas à pas le long de ses propres tangentes, avec un script **Python**.
- La grande démonstration du programme : pourquoi $\exp(x)$ ne s'annule jamais et pourquoi cette fonction est **unique**.
- La transformation magique de l'addition en multiplication : la preuve de $\exp(x+y) = \exp(x)\exp(y)$.
- Le nombre universel d'Euler : $e \approx 2{,}71828$, et la notation $e^x$.
- L'étude complète de la fonction : dérivée, stricte positivité, croissance explosive, limites et asymptotes.
- La dérivée des fonctions composées : $(e^{u(x)})' = u'(x)e^{u(x)}$.
- Comment résoudre équations et inéquations avec $e^x$.

---

### 1. Le problème : la boîte de Pétri et l'horloge biologique

Regarde à travers l'oculaire d'un microscope dans un laboratoire de biologie.
Dans une boîte de Pétri remplie de gélose nutritive, le chercheur dépose à midi ($t = 0$) une unique bactérie *Escherichia coli*.

Cette bactérie se nourrit. Au bout de vingt minutes, elle s'allonge et se scinde en deux : il y a 2 bactéries.
Vingt minutes plus tard, chacune se divise à son tour : il y a 4 bactéries.
Puis 8, puis 16, 32, 64, 128, 256...

```
Temps t (h) :  0      1      2      3       ...   10
Bactéries   :  1      8     64    512       ...   1 000 000 000
```

Observe attentivement ce qui distingue cette croissance de toutes celles que nous avons étudiées jusqu'ici :

- Pour une voiture sur l'autoroute à vitesse constante, la distance augmente de 100 km chaque heure, quelle que soit la distance déjà parcourue. La dérivée est constante.
- Pour une pierre qui tombe en chute libre, la vitesse augmente de $9{,}8\text{ m/s}$ chaque seconde sous l'action de la gravité : l'accélération est constante, la position suit un polynôme du second degré ($x^2$).
- Mais pour la colonie de bactéries, **les nouveaux venus sont eux-mêmes de futures usines à naissances** !
  - Quand la colonie compte 10 bactéries, il y a 10 naissances potentielles par génération. La pente est faible.
  - Quand la colonie compte un million d'individus, il y a **un million de divisions cellulaires simultanées** ! La vitesse de prolifération devient titanesque.

En notant $N(t)$ le nombre d'individus à l'instant $t$, la vitesse de croissance instantanée (la dérivée $N'(t)$) n'est pas constante : elle est **directement proportionnelle au nombre d'individus déjà présents** :

$$N'(t) = k \cdot N(t).$$

En choisissant judicieusement l'unité de temps pour que $k = 1$, et en partant d'un individu unique à l'instant $t = 0$, nous faisons face au défi le plus fascinant posé au calcul différentiel :

> **L'Énigme fondamentale :**
> Existe-t-il une fonction mathématique $f$, définie et dérivable sur $\mathbb{R}$, qui est **rigoureusement égale à sa propre dérivée** à chaque instant, et qui vaut 1 à l'origine ?
>
> $$\begin{cases} f'(x) = f(x) \quad \text{pour tout } x \in \mathbb{R} \\ f(0) = 1 \end{cases}$$

C'est une fonction dont la pente du ski sous la semelle en chaque point est exactement égale à son altitude ! Plus elle monte haut, plus la pente devient raide ; plus la pente est raide, plus elle s'élève vite vers le ciel.

---

### 2. La méthode d'Euler : construire la courbe à petits pas

Avant de prouver théoriquement qu'une telle fonction existe, comment pouvons-nous dessiner son allure et calculer ses valeurs approchées ?
Au XVIIIᵉ siècle, le génie suisse **Leonhard Euler** imagine une méthode numérique révolutionnaire : avancer pas à pas le long de la tangente.

#### 2.1 Le principe géométrique

Rappelle-toi du chapitre précédent : au voisinage d'un point $x_0$, la courbe se confond presque avec sa tangente :
$$f(x_0 + h) \approx f(x_0) + h \cdot f'(x_0).$$

Mais ici, notre fonction a un pouvoir magique : **sa dérivée est égale à sa valeur** ($f'(x_0) = f(x_0)$) !
La formule d'approximation devient prodigieusement simple :

$$f(x_0 + h) \approx f(x_0) + h \cdot f(x_0) = (1 + h) \cdot f(x_0).$$

Chaque pas en avant de largeur $h$ revient simplement à **multiplier l'altitude précédente par $(1 + h)$** !

```
    Altitude
        ▲                                     . - * M₂(2h ; (1+h)² f(0))
        │                               . - '   /
        │                         . - * M₁(h ; (1+h) f(0))
        │                   . - '   /
        │             . - * M₀(0 ; 1)
        │       . - '
      1 ┼──────*
        │
      0 └──────┴──────────┴──────────┴──────────► x
               0          h          2h
```

#### 2.2 Calcul manuel avec un pas $h = 0{,}2$
Partons de $x_0 = 0$ et $y_0 = 1$ avec un pas $h = 0{,}2$ :
- En $x_1 = 0{,}2$ : $y_1 = y_0 \times (1 + 0{,}2) = 1 \times 1{,}2 = 1{,}2$.
- En $x_2 = 0{,}4$ : $y_2 = y_1 \times 1{,}2 = 1{,}2 \times 1{,}2 = 1{,}44$.
- En $x_3 = 0{,}6$ : $y_3 = 1{,}44 \times 1{,}2 = 1{,}728$.
- En $x_4 = 0{,}8$ : $y_4 = 1{,}728 \times 1{,}2 = 2{,}0736$.
- En $x_5 = 1{,}0$ : $y_5 = 2{,}0736 \times 1{,}2 \approx 2{,}488$.

En 5 pas, nous atteignons $x = 1$, et notre approximation donne $f(1) \approx 2{,}488$.
Si l'on prend un pas dix fois plus petit ($h = 0{,}02$), on effectue 50 multiplications par $1{,}02$, et l'on trouve $(1{,}02)^{50} \approx 2{,}691$.
Avec $h = 0{,}001$ (1000 pas), on obtient $(1{,}001)^{1000} \approx 2{,}7169$.
La courbe existe bel et bien sous nos yeux !

#### 2.3 L'algorithme Python officiel

Voici le script Python exigé par le programme de Première Spécialité pour simuler la méthode d'Euler :

```python
def methode_euler(n_pas):
    h = 1.0 / n_pas  # largeur du pas pour aller de 0 à 1
    x = 0.0
    y = 1.0
    for _ in range(n_pas):
        y = y + h * y  # équivalent à y = y * (1 + h)
        x = x + h
    return y

# Testons avec un découpage de plus en plus fin :
for n in [10, 100, 1000, 10000]:
    print(f"Pour n = {n:5d} pas : f(1) ≈ {methode_euler(n):.6f}")
```

Exécution :
```
Pour n =    10 pas : f(1) ≈ 2.593742
Pour n =   100 pas : f(1) ≈ 2.704814
Pour n =  1000 pas : f(1) ≈ 2.716924
Pour n = 10000 pas : f(1) ≈ 2.718146
```

Les décimales se stabilisent vers un nombre mystérieux : **$2{,}71828\dots$**

---

### 3. Théorème d'existence et démonstration d'unicité

> **📐 Théorème fondamental (admis pour l'existence, démontré pour l'unicité)**
> Il existe une **unique** fonction $f$ dérivable sur $\mathbb{R}$ telle que :
>
> $$\begin{cases} f'(x) = f(x) \quad \text{pour tout } x \in \mathbb{R} \\ f(0) = 1 \end{cases}$$
>
> Cette fonction est appelée la **fonction exponentielle**, notée $\exp$.

La démonstration de l'unicité est une merveille d'ingéniosité mathématique au programme du lycée. Elle repose sur un lemme capital : la fonction ne peut jamais s'évanouir à zéro.

#### 3.1 Lemme : la fonction ne s'annule jamais

> **✍️ Démonstration — Non-annulation de $f$**
> Soit $f$ une fonction dérivable sur $\mathbb{R}$ vérifiant $f' = f$ et $f(0) = 1$.
> Considérons la fonction auxiliaire $g$ définie sur $\mathbb{R}$ par :
> $$g(x) = f(x) \times f(-x).$$
> Dérivons la fonction $g$ à l'aide de la formule du produit $(uv)' = u'v + uv'$ :
> La dérivée de $f(-x)$ est $-f'(-x)$ (dérivée de fonction composée).
> $$g'(x) = f'(x) \cdot f(-x) + f(x) \cdot \big(-f'(-x)\big) = f'(x)f(-x) - f(x)f'(-x).$$
> Mais par hypothèse, $f' = f$ partout, donc $f'(x) = f(x)$ et $f'(-x) = f(-x)$ ! Remplaçons :
> $$g'(x) = f(x)f(-x) - f(x)f(-x) = 0.$$
> La dérivée de $g$ est **identiquement nulle sur $\mathbb{R}$**.
> Une fonction dont la dérivée est nulle partout est **constante** !
> Donc pour tout réel $x$ :
> $$g(x) = g(0) = f(0) \times f(-0) = 1 \times 1 = 1.$$
> Ainsi, pour tout $x \in \mathbb{R}$ :
> $$\boxed{f(x) \times f(-x) = 1}$$
>
> Si un produit de deux nombres vaut 1, aucun des deux ne peut être égal à zéro !
> Par conséquent, **pour tout réel $x$, $f(x) \neq 0$**. $\blacksquare$

#### 3.2 Preuve de l'unicité

> **✍️ Démonstration — Unicité de la fonction exponentielle**
> Supposons qu'il existe deux fonctions $f_1$ et $f_2$ vérifiant toutes deux les conditions :
> $f'_1 = f_1$ avec $f_1(0) = 1$, et $f'_2 = f_2$ avec $f_2(0) = 1$.
> Puisque $f_1$ ne s'annule jamais sur $\mathbb{R}$ d'après le lemme ci-dessus, nous avons le droit absolu de considérer la fonction quotient :
> $$\phi(x) = \frac{f_2(x)}{f_1(x)}.$$
> Dérivons ce quotient grâce à la règle $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ :
> $$\phi'(x) = \frac{f'_2(x)f_1(x) - f_2(x)f'_1(x)}{(f_1(x))^2}.$$
> Comme $f'_2 = f_2$ et $f'_1 = f_1$ :
> $$\phi'(x) = \frac{f_2(x)f_1(x) - f_2(x)f_1(x)}{(f_1(x))^2} = \frac{0}{(f_1(x))^2} = 0.$$
> La dérivée de $\phi$ est identiquement nulle sur $\mathbb{R}$, donc $\phi$ est constante.
> Or en $x = 0$ :
> $$\phi(0) = \frac{f_2(0)}{f_1(0)} = \frac{1}{1} = 1.$$
> Donc pour tout $x \in \mathbb{R}$, $\phi(x) = 1$, ce qui signifie que :
> $$f_2(x) = f_1(x).$$
> Il ne peut donc exister qu'une seule et unique fonction vérifiant ce problème ! $\blacksquare$

---

### 4. La propriété fondamentale : transformer l'addition en multiplication

C'est la propriété reine qui fait de l'exponentielle la fonction la plus puissante des sciences :

> **📐 Théorème fondamental — Relation fonctionnelle**
> Pour tous réels $x$ et $y$ :
>
> $$\boxed{\exp(x + y) = \exp(x) \times \exp(y)}$$

> **✍️ Démonstration exigible au Bac**
> Fixons un nombre réel $y$ quelconque, et considérons la fonction d'une seule variable $x$ définie par :
> $$h(x) = \frac{\exp(x + y)}{\exp(x)}.$$
> (Le quotient est légitime puisque le dénominateur $\exp(x)$ ne s'annule jamais).
> Dérivons $h$ par rapport à $x$ :
> Le numérateur $u(x) = \exp(x + y)$ a pour dérivée $u'(x) = 1 \cdot \exp'(x+y) = \exp(x+y)$.
> Le dénominateur $v(x) = \exp(x)$ a pour dérivée $v'(x) = \exp(x)$.
> Calculons la dérivée du quotient :
> $$h'(x) = \frac{\exp(x+y)\exp(x) - \exp(x+y)\exp(x)}{(\exp(x))^2} = 0.$$
> La fonction $h$ est donc constante sur $\mathbb{R}$.
> Sa valeur pour tout $x$ est égale à sa valeur en $x = 0$ :
> $$h(0) = \frac{\exp(0 + y)}{\exp(0)} = \frac{\exp(y)}{1} = \exp(y).$$
> Ainsi, pour tout $x \in \mathbb{R}$ :
> $$\frac{\exp(x + y)}{\exp(x)} = \exp(y) \iff \exp(x + y) = \exp(x) \times \exp(y). \quad \blacksquare$$

#### 4.1 Propriétés algébriques dérivées

De cette formule découlent instantanément toutes les règles familières des puissances :

> **📐 Propriétés algébriques** — Pour tous réels $x, y$ et tout entier relatif $n$ :
> 1. $\exp(-x) = \frac{1}{\exp(x)}$
> 2. $\exp(x - y) = \frac{\exp(x)}{\exp(y)}$
> 3. $\exp(n \cdot x) = \big(\exp(x)\big)^n$

> **✍️ Démonstrations rapides**
> 1. D'après le lemme : $\exp(x) \times \exp(-x) = \exp(x - x) = \exp(0) = 1 \implies \exp(-x) = \frac{1}{\exp(x)}$.
> 2. $\exp(x - y) = \exp(x + (-y)) = \exp(x) \times \exp(-y) = \exp(x) \times \frac{1}{\exp(y)} = \frac{\exp(x)}{\exp(y)}$.
> 3. Par récurrence immédiate pour $n \in \mathbb{N}$ : $\exp(2x) = \exp(x+x) = (\exp(x))^2$, etc. $\blacksquare$

---

### 5. La notation d'Euler et le nombre $e$

Regarde la ressemblance stupéfiante entre les propriétés de $\exp$ et celles des puissances de collège :
- $a^{x+y} = a^x \times a^y$
- $a^{-x} = \frac{1}{a^x}$
- $a^{nx} = (a^x)^n$

Cette coïncidence totale pousse **Leonhard Euler** en 1728 à poser une notation audacieuse.
Posons le nombre $e$ comme l'image de 1 par la fonction exponentielle :

$$e = \exp(1) \approx 2{,}718281828459\dots$$

Alors, pour tout entier $n$, $\exp(n) = (\exp(1))^n = e^n$.
Euler généralise cette écriture à tous les nombres réels $x$ :

> **📐 Notation d'Euler**
> Pour tout nombre réel $x$, on note :
>
> $$\boxed{\exp(x) = e^x}$$
>
> On prononce indifféremment « exponentielle de $x$ » ou « **e exposant x** ».
> Les règles d'écriture s'alignent sur les puissances :
> $$e^0 = 1, \quad e^1 = e, \quad e^{x+y} = e^x \cdot e^y, \quad e^{-x} = \frac{1}{e^x}, \quad e^{x-y} = \frac{e^x}{e^y}, \quad (e^x)^n = e^{nx}.$$

---

### 6. Étude complète de la fonction exponentielle

#### 6.1 Signe et stricte positivité
Nous avons déjà prouvé que $e^x \neq 0$ pour tout $x$.
De plus, $e^x = e^{x/2 + x/2} = \left(e^{x/2}\right)^2$.
Or un carré est toujours positif ou nul. Comme il ne peut pas valoir 0, il est **strictement positif** !

> **📐 Théorème — Stricte positivité**
> Pour tout nombre réel $x$ :
>
> $$\boxed{e^x > 0}$$
>
> La courbe représentative de l'exponentielle est **entièrement située au-dessus de l'axe des abscisses**. Elle ne traverse jamais la ligne zéro.

#### 6.2 Sens de variation
La dérivée de la fonction exponentielle est elle-même :
$$(e^x)' = e^x.$$
Comme $e^x > 0$ pour tout $x \in \mathbb{R}$, **la dérivée est strictement positive sur tout $\mathbb{R}$**.

> **📐 Théorème — Stricte croissance**
> La fonction exponentielle est **strictement croissante** sur $\mathbb{R}$.
> Par conséquent :
> - $e^a = e^b \iff a = b$
> - $e^a < e^b \iff a < b$

#### 6.3 Limites aux infinis et asymptotes
- Quand $x \to +\infty$ : $e^x$ explose vers l'infini avec une rapidité vertigineuse :
  $$\lim_{x \to +\infty} e^x = +\infty.$$
- Quand $x \to -\infty$ : posons $X = -x$. Quand $x \to -\infty$, $X \to +\infty$.
  $$e^x = e^{-X} = \frac{1}{e^X} \xrightarrow[X \to +\infty]{} 0^+.$$
  $$\lim_{x \to -\infty} e^x = 0.$$

> **📐 Propriété géométrique — Asymptote horizontale**
> La droite d'équation $y = 0$ (l'axe des abscisses) est une **asymptote horizontale** à la courbe de l'exponentielle en $-\infty$.

#### 6.4 Tableau de variations et tracé de la courbe

| $x$ | $-\infty$ | | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $(e^x)' = e^x$ | | $+$ | $1$ | $+$ | $e$ | $+$ | |
| $e^x$ | $0$ | $\nearrow$ | $1$ | $\nearrow$ | $e \approx 2{,}718$ | $\nearrow$ | $+\infty$ |

Tangente en $0$ ($a = 0$) :
$y = e^0(x - 0) + e^0 \iff \boxed{y = x + 1}$.

```
      y
      ▲                                         /  e^x
   4  │                                       /
   3  │                                     .'  (1 ; e ≈ 2,72)
      │                                   .*
   2  │                             . - * │
   1  │                      . - *'       │
      │                . - *'│            │
   0  ┴─────────*──────┴─────┴────────────┴─────► x
     -3        -2     -1     0            1
   (Asymptote y = 0 en -∞)
```

La courbe est entièrement située au-dessus de sa tangente en 0 :
$$\text{Pour tout } x \in \mathbb{R}, \quad \boxed{e^x \ge x + 1}$$

---

### 7. Dérivée de la composée $e^{u(x)}$

Dans les applications concrètes (radioactivité, épidémies, électronique), l'exposant n'est presque jamais un simple $x$, mais une fonction du temps : $e^{-3t}$, $e^{-x^2/2}$, etc.

> **📐 Théorème — Dérivée de $e^u$**
> Si $u$ est une fonction dérivable sur un intervalle $I$, alors la fonction $f(x) = e^{u(x)}$ est dérivable sur $I$, et :
>
> $$\boxed{\big(e^{u(x)}\big)' = u'(x) \cdot e^{u(x)}}$$

> **⚠️ Attention, piège ! — N'oublie jamais $u'(x)$**
> La dérivée de $e^{5x}$ n'est pas $e^{5x}$ !
> Ici $u(x) = 5x \implies u'(x) = 5$.
> Donc $(e^{5x})' = 5e^{5x}$.
> De même : $(e^{-x})' = -e^{-x}$, et $(e^{x^2})' = 2x e^{x^2}$.

---

### Exemples résolus pas à pas

> **✅ Exemple résolu 1 — Simplification d'expressions exponentielles**
> Simplifier au maximum les expressions suivantes :
> 1. $A = \frac{e^3 \times e^{-5}}{(e^2)^3}$
> 2. $B = \frac{e^{2x+1} \times e^{-x+3}}{e^{x-2}}$
> 3. $C = (e^x + e^{-x})^2 - (e^x - e^{-x})^2$
>
> **Solution détaillée :**
> 1. $A = \frac{e^{3 + (-5)}}{e^{2 \times 3}} = \frac{e^{-2}}{e^6} = e^{-2 - 6} = e^{-8} = \frac{1}{e^8}$.
> 2. $B = \frac{e^{(2x+1) + (-x+3)}}{e^{x-2}} = \frac{e^{x+4}}{e^{x-2}} = e^{(x+4) - (x-2)} = e^{x + 4 - x + 2} = e^6$.
> 3. Identité remarquable $(u+v)^2 - (u-v)^2 = 4uv$ :
>    $C = 4 \times e^x \times e^{-x} = 4 \times e^{x - x} = 4 \times e^0 = 4 \times 1 = 4$.

> **✅ Exemple résolu 2 — Résolution d'équations avec exponentielles**
> Résoudre dans $\mathbb{R}$ :
> 1. $e^{3x - 1} = e^{x + 5}$
> 2. $e^{x^2 - 4} = 1$
> 3. $e^{2x} - 3e^x + 2 = 0$
>
> **Solution détaillée :**
> 1. Par stricte croissance : $e^a = e^b \iff a = b$.
>    $$3x - 1 = x + 5 \iff 2x = 6 \iff x = 3. \quad S = \{3\}.$$
> 2. Rappelons que $1 = e^0$ :
>    $$e^{x^2 - 4} = e^0 \iff x^2 - 4 = 0 \iff (x - 2)(x + 2) = 0. \quad S = \{-2; 2\}.$$
> 3. On remarque que $e^{2x} = (e^x)^2$. Posons le changement de variable $X = e^x$ (avec $X > 0$).
>    L'équation devient :
>    $$X^2 - 3X + 2 = 0.$$
>    Racines évidentes : $X_1 = 1$ et $X_2 = 2$ (car $1 - 3 + 2 = 0$).
>    Revenons à $x$ :
>    - $e^x = 1 \iff x = 0$.
>    - $e^x = 2 \iff x = \ln(2)$ (nous verrons le logarithme en Terminale, retenons que c'est une unique valeur réelle $\approx 0{,}693$).
>    $$S = \{0; \ln 2\}.$$

> **✅ Exemple résolu 3 — Résolution d'inéquations**
> Résoudre dans $\mathbb{R}$ :
> 1. $e^{4x - 7} \le 1$
> 2. $\frac{e^x - 3}{e^x + 2} > 0$
>
> **Solution détaillée :**
> 1. $e^{4x - 7} \le e^0 \iff 4x - 7 \le 0 \iff 4x \le 7 \iff x \le \frac{7}{4}$.
>    $$S = \left]-\infty; \frac{7}{4}\right].$$
> 2. Pour tout réel $x$, $e^x > 0$, donc le dénominateur $e^x + 2 > 2 > 0$ est strictement positif !
>    Le signe de la fraction est donc uniquement celui du numérateur :
>    $$e^x - 3 > 0 \iff e^x > 3 \iff x > \ln 3. \quad S = ]\ln 3; +\infty[.$$

> **✅ Exemple résolu 4 — Dérivation de fonctions composées**
> Dériver les fonctions suivantes :
> 1. $f(x) = (2x - 3)e^{-x}$
> 2. $g(x) = e^{-x^2 + 4x}$
> 3. $h(x) = \frac{e^x}{x+1}$ pour $x \neq -1$
>
> **Solution détaillée :**
> 1. Forme $u \cdot v$ avec $u(x) = 2x - 3 \implies u'(x) = 2$, et $v(x) = e^{-x} \implies v'(x) = -e^{-x}$.
>    $$f'(x) = u'v + uv' = 2e^{-x} + (2x - 3)(-e^{-x}) = [2 - (2x - 3)]e^{-x} = (5 - 2x)e^{-x}.$$
> 2. Forme $e^u$ avec $u(x) = -x^2 + 4x \implies u'(x) = -2x + 4$.
>    $$g'(x) = u'(x)e^{u(x)} = (-2x + 4)e^{-x^2 + 4x}.$$
> 3. Forme $\frac{u}{v}$ :
>    $$h'(x) = \frac{(e^x)'(x+1) - e^x(x+1)'}{(x+1)^2} = \frac{e^x(x+1) - e^x(1)}{(x+1)^2} = \frac{e^x(x + 1 - 1)}{(x+1)^2} = \frac{x e^x}{(x+1)^2}.$$

> **✅ Exemple résolu 5 — Étude complète d'une fonction avec exponentielle**
> Soit $f(x) = (x - 1)e^x$ définie sur $\mathbb{R}$.
> Dresser son tableau de variations complet et préciser l'équation de la tangente en 0.
>
> **Solution détaillée :**
> 1. Dérivée : Règle du produit avec $u(x) = x - 1 \implies u'(x) = 1$ et $v(x) = e^x \implies v'(x) = e^x$.
>    $$f'(x) = 1 \cdot e^x + (x - 1)e^x = (1 + x - 1)e^x = x e^x.$$
> 2. Signe de $f'(x)$ :
>    Comme $e^x > 0$ pour tout réel $x$, le signe de $f'(x)$ est **strictement identique au signe de $x$** !
>    - $f'(x) < 0$ pour $x < 0$ ;
>    - $f'(0) = 0$ ;
>    - $f'(x) > 0$ pour $x > 0$.
> 3. Variations :
>    $f$ est strictement décroissante sur $]-\infty; 0]$ et strictement croissante sur $[0; +\infty[$.
>    Elle admet un minimum absolu en $x = 0$, qui vaut $f(0) = (0 - 1)e^0 = -1$.
> 4. Tangente en 0 :
>    $f(0) = -1$ et $f'(0) = 0 \cdot e^0 = 0$.
>    La tangente est horizontale d'équation : $\boxed{y = -1}$.

> **✅ Exemple résolu 6 — Modélisation concrète : la décharge d'un condensateur**
> Dans un circuit électrique, la tension aux bornes d'un condensateur qui se décharge à travers une résistance est modélisée par $U(t) = 12 e^{-0{,}5 t}$ où $t$ est le temps en secondes et $U$ en volts.
> 1. Quelle est la tension initiale à $t = 0$ ?
> 2. Au bout de combien de temps la tension est-elle divisée par 2 ?
> 3. Calculer la vitesse de chute de tension à l'instant $t = 0$.
>
> **Solution détaillée :**
> 1. $U(0) = 12 e^0 = 12 \times 1 = 12$ V.
> 2. On cherche $t$ tel que $U(t) = 6$ V :
>    $$12 e^{-0{,}5 t} = 6 \iff e^{-0{,}5 t} = 0{,}5 = \frac{1}{2} \iff e^{0{,}5 t} = 2.$$
>    Comme $0{,}5 = \frac{1}{2}$, cela donne $t \approx 2 \times 0{,}693 \approx 1{,}39$ seconde.
> 3. Vitesse de décharge : c'est la dérivée $U'(t)$.
>    $$U'(t) = 12 \times (-0{,}5) e^{-0{,}5 t} = -6 e^{-0{,}5 t}.$$
>    À $t = 0$, $U'(0) = -6 e^0 = -6\text{ V/s}$.
>    La tension chute initialement à une vitesse de 6 volts par seconde.

---

### Ce qu'il faut retenir

1. **Définition de l'exponentielle :**
   - Unique fonction vérifiant $f' = f$ et $f(0) = 1$.
   - Notée $\exp(x)$ ou $e^x$, avec $e = \exp(1) \approx 2{,}71828$.

2. **Propriété fondamentale (morphisme addition $\to$ multiplication) :**
   - $e^{a+b} = e^a \cdot e^b$
   - $e^{-a} = \frac{1}{e^a}$
   - $e^{a-b} = \frac{e^a}{e^b}$
   - $(e^a)^n = e^{na}$

3. **Propriétés analytiques :**
   - Strictement positive : $e^x > 0$ sur $\mathbb{R}$.
   - Strictement croissante sur $\mathbb{R}$ : $e^a < e^b \iff a < b$.
   - Limites : $\lim_{x \to -\infty} e^x = 0$ (axe $y = 0$ asymptote) et $\lim_{x \to +\infty} e^x = +\infty$.
   - Dérivée usuelle : $(e^x)' = e^x$.
   - Dérivée d'une composée : $\big(e^{u(x)}\big)' = u'(x) e^{u(x)}$.
   - Tangente en 0 : $y = x + 1$, avec $e^x \ge x + 1$ pour tout réel $x$.

---

### Exercices

#### Niveau ★ (Calculs d'expressions, équations élémentaires)

1. Écrire sous la forme d'une seule puissance de $e$ : $A = e^4 \times e^{-7}$, $B = \frac{e^8}{e^3}$, $C = (e^{-2})^5$.
2. Dériver la fonction $f(x) = 3e^x - 4x + 1$.
3. Dériver $g(x) = e^{4x - 1}$.
4. Dériver $h(x) = e^{-3x}$.
5. Résoudre dans $\mathbb{R}$ l'équation $e^{2x - 3} = e^5$.
6. Résoudre dans $\mathbb{R}$ l'inéquation $e^{3x+1} > e^{x-5}$.
7. Déterminer l'équation de la tangente à la courbe de $f(x) = e^x$ au point d'abscisse $a = 1$.
8. Calculer $f'(x)$ pour $f(x) = x^2 e^x$.

#### Niveau ★★ (Études de fonctions et variations)

9. Résoudre dans $\mathbb{R}$ l'équation $e^{2x} - 4e^x + 3 = 0$ à l'aide d'un changement de variable.
10. Dresser le tableau de variations complet de la fonction $f(x) = (2x - 1)e^x$ sur $\mathbb{R}$.
11. Soit la fonction « cloche de Gauss » $f(x) = e^{-x^2}$.
    a) Calculer $f'(x)$.
    b) Dresser le tableau de variations de $f$ et déterminer son maximum absolu.
12. Résoudre l'inéquation $e^{2x} - e^x \le 0$.
13. On considère la fonction $f(x) = \frac{e^x - 1}{e^x + 1}$.
    a) Démontrer que $f$ est impaire ($f(-x) = -f(x)$).
    b) Calculer $f'(x)$ et montrer que $f$ est strictement croissante sur $\mathbb{R}$.
14. Soit la fonction $g(x) = e^{2x} - 2x$.
    a) Étudier les variations de $g$ sur $\mathbb{R}$.
    b) En déduire que pour tout réel $x$, $e^{2x} \ge 2x + 1 > 2x$.
15. Déterminer les abscisses des points de la courbe de $f(x) = e^{x^2 - 3x}$ où la tangente est horizontale.
16. Un bol de soupe chaude est posé dans une cuisine à 20°C. Sa température en degrés Celsius après $t$ minutes est modélisée par $T(t) = 20 + 60e^{-0{,}05 t}$.
    a) Quelle est la température de la soupe au moment où on la sert ($t = 0$) ?
    b) Quelle sera la température au bout de 20 minutes ? (Donnée : $e^{-1} \approx 0{,}368$)
    c) Vers quelle température la soupe tend-elle quand $t \to +\infty$ ?

#### Niveau ★★★ (Problèmes et défis Bac)

17. **Démonstration de l'inégalité $e^x \ge x + 1$ :**
    Soit la fonction $\varphi(x) = e^x - x - 1$ définie sur $\mathbb{R}$.
    a) Étudier les variations de $\varphi$ et dresser son tableau de variations.
    b) En déduire son minimum et conclure que la courbe de l'exponentielle est toujours située au-dessus de sa tangente en 0.
18. **Intersection de courbes et position relative :**
    Soient les fonctions $f(x) = e^x$ et $g(x) = e^{-x}$.
    a) Déterminer les coordonnées du point d'intersection de leurs deux courbes.
    b) Montrer que leurs tangentes en ce point sont perpendiculaires !
19. **La chaînette (cosinus hyperbolique) :**
    Un câble électrique suspendu entre deux pylônes prend la forme d'une courbe appelée la « chaînette », d'équation $f(x) = \frac{e^x + e^{-x}}{2}$.
    a) Montrer que $f$ est une fonction paire.
    b) Calculer $f'(x)$ et étudier les variations de $f$.
    c) Prouver que pour tout réel $x$, $(f(x))^2 - (f'(x))^2 = 1$.
20. **Algorithme d'Euler et comparaison :**
    Écrire un programme Python qui compare à l'abscisse $x = 1$ la valeur approchée obtenue par la méthode d'Euler avec 100 pas et la valeur exacte donnée par `math.exp(1)`. Calculer l'erreur relative en pourcentage.
21. **Famille de fonctions et point fixe :**
    Pour tout réel $k > 0$, on définit la fonction $f_k(x) = k e^{kx}$.
    Montrer que toutes les courbes $\mathcal{C}_k$ passent par un même point fixe si l'on effectue une translation, et déterminer les coordonnées du point où la tangente à $\mathcal{C}_k$ a pour pente $k^2$.

---

### Solutions

**1.** $A = e^{4 - 7} = e^{-3} = \frac{1}{e^3}$. $B = e^{8 - 3} = e^5$. $C = e^{-2 \times 5} = e^{-10}$.

**2.** $f'(x) = 3e^x - 4$.

**3.** Forme $e^u$ avec $u = 4x-1 \implies u'=4$. $g'(x) = 4e^{4x-1}$.

**4.** Forme $e^u$ avec $u = -3x \implies u'=-3$. $h'(x) = -3e^{-3x}$.

**5.** $e^{2x-3} = e^5 \iff 2x - 3 = 5 \iff 2x = 8 \iff x = 4$. $S = \{4\}$.

**6.** $e^{3x+1} > e^{x-5} \iff 3x + 1 > x - 5 \iff 2x > -6 \iff x > -3$. $S = ]-3; +\infty[$.

**7.** En $a = 1$ : $f(1) = e^1 = e$, $f'(1) = e$.
Tangente : $y = f'(1)(x - 1) + f(1) = e(x - 1) + e = ex - e + e = ex$.
La tangente en 1 passe par l'origine : $y = ex$.

**8.** Règle du produit : $u = x^2 \implies u'=2x$ ; $v = e^x \implies v'=e^x$.
$f'(x) = 2x e^x + x^2 e^x = (x^2 + 2x)e^x = x(x+2)e^x$.

**9.** En posant $X = e^x > 0$, l'équation devient $X^2 - 4X + 3 = 0$.
$\Delta = 16 - 12 = 4 = 2^2$.
$X_1 = \frac{4 - 2}{2} = 1$ et $X_2 = \frac{4 + 2}{2} = 3$.
- $e^x = 1 \iff x = 0$.
- $e^x = 3 \iff x = \ln 3 \approx 1{,}0986$.
$S = \{0; \ln 3\}$.

**10.** $f'(x) = 2e^x + (2x - 1)e^x = (2 + 2x - 1)e^x = (2x + 1)e^x$.
Comme $e^x > 0$, le signe de $f'(x)$ est celui de $2x + 1$ :
- $f'(x) < 0$ sur $]-\infty; -0{,}5[$ ($f$ décroissante) ;
- $f'(-0{,}5) = 0$ ;
- $f'(x) > 0$ sur $]-0{,}5; +\infty[$ ($f$ croissante).
Minimum absolu en $x = -0{,}5$ : $f(-0{,}5) = (2(-0{,}5) - 1)e^{-0{,}5} = -2e^{-0{,}5} = -\frac{2}{\sqrt{e}} \approx -1{,}213$.

**11.**
a) $u(x) = -x^2 \implies u'(x) = -2x$. Donc $f'(x) = -2x e^{-x^2}$.
b) Comme $e^{-x^2} > 0$, le signe de $f'(x)$ est l'opposé de celui de $x$ :
Pour $x < 0$, $f'(x) > 0$ (croissante) ; pour $x > 0$, $f'(x) < 0$ (décroissante).
$f$ admet un maximum absolu en $x = 0$, qui vaut $f(0) = e^0 = 1$.

**12.** Factorisons par $e^x$ : $e^{2x} - e^x = e^x(e^x - 1) \le 0$.
Comme $e^x > 0$ toujours, cela équivaut à $e^x - 1 \le 0 \iff e^x \le 1 = e^0 \iff x \le 0$.
$S = ]-\infty; 0]$.

**13.**
a) $f(-x) = \frac{e^{-x} - 1}{e^{-x} + 1} = \frac{\frac{1}{e^x} - 1}{\frac{1}{e^x} + 1} = \frac{\frac{1 - e^x}{e^x}}{\frac{1 + e^x}{e^x}} = \frac{-(e^x - 1)}{e^x + 1} = -f(x)$. La fonction est impaire.
b) Formule du quotient :
$f'(x) = \frac{e^x(e^x+1) - (e^x-1)e^x}{(e^x+1)^2} = \frac{e^{2x} + e^x - e^{2x} + e^x}{(e^x+1)^2} = \frac{2e^x}{(e^x+1)^2}$.
Le numérateur est strictement positif ($2e^x > 0$) et le dénominateur est un carré non nul ($> 0$).
Donc $f'(x) > 0$ sur $\mathbb{R}$ : $f$ est strictement croissante.

**14.**
a) $g'(x) = 2e^{2x} - 2 = 2(e^{2x} - 1)$.
$g'(x) > 0 \iff e^{2x} > 1 \iff 2x > 0 \iff x > 0$.
$g$ décroît sur $]-\infty; 0]$ et croît sur $[0; +\infty[$.
Minimum absolu en $0$ : $g(0) = e^0 - 0 = 1$.
b) Comme le minimum vaut 1, on a pour tout $x \in \mathbb{R}$ : $g(x) \ge 1 \iff e^{2x} - 2x \ge 1 \iff e^{2x} \ge 2x + 1$.
Comme $2x + 1 > 2x$, on en déduit immédiatement $e^{2x} > 2x$.

**15.** $f'(x) = (2x - 3)e^{x^2 - 3x}$.
Tangente horizontale $\iff f'(x) = 0 \iff 2x - 3 = 0 \iff x = \frac{3}{2} = 1{,}5$.

**16.**
a) $T(0) = 20 + 60e^0 = 20 + 60 = 80^\circ$C.
b) $T(20) = 20 + 60e^{-0{,}05 \times 20} = 20 + 60e^{-1} \approx 20 + 60 \times 0{,}368 = 20 + 22{,}08 = 42{,}08^\circ$C.
c) Quand $t \to +\infty$, $-0{,}05t \to -\infty$, donc $e^{-0{,}05t} \to 0$.
$\lim_{t \to +\infty} T(t) = 20 + 0 = 20^\circ$C (la température ambiante de la pièce).

**17.**
a) $\varphi'(x) = e^x - 1$.
- $\varphi'(x) < 0$ pour $x < 0$ ($\varphi$ décroissante) ;
- $\varphi'(0) = 0$ ;
- $\varphi'(x) > 0$ pour $x > 0$ ($\varphi$ croissante).
b) $\varphi$ atteint son minimum absolu en $x = 0$, qui vaut $\varphi(0) = e^0 - 0 - 1 = 1 - 1 = 0$.
Par conséquent, pour tout $x \in \mathbb{R}$, $\varphi(x) \ge 0 \iff e^x - x - 1 \ge 0 \iff e^x \ge x + 1$.
La courbe $\mathcal{C}_{\exp}$ est donc toujours au-dessus de sa tangente en 0.

**18.**
a) $e^x = e^{-x} \iff e^x = \frac{1}{e^x} \iff (e^x)^2 = 1 \iff e^{2x} = 1 \iff 2x = 0 \iff x = 0$.
Ordonnée : $y = e^0 = 1$. L'intersection est le point $A(0; 1)$.
b) Tangente à $f$ en 0 : coefficient directeur $f'(0) = e^0 = 1$.
Tangente à $g$ en 0 : $g'(x) = -e^{-x} \implies g'(0) = -e^0 = -1$.
Le produit de leurs pentes vaut $m_1 \times m_2 = 1 \times (-1) = -1$.
D'après la propriété d'orthogonalité des droites, les deux tangentes sont rigoureusement perpendiculaires !

**19.**
a) $f(-x) = \frac{e^{-x} + e^{-(-x)}}{2} = \frac{e^{-x} + e^x}{2} = f(x)$. La fonction est paire.
b) $f'(x) = \frac{e^x - e^{-x}}{2}$.
$f'(x) > 0 \iff e^x - e^{-x} > 0 \iff e^x > e^{-x} \iff x > -x \iff 2x > 0 \iff x > 0$.
La fonction décroît sur $]-\infty; 0]$ et croît sur $[0; +\infty[$. Minimum en $0$ valant $f(0) = 1$.
c) $(f(x))^2 - (f'(x))^2 = \left(\frac{e^x + e^{-x}}{2}\right)^2 - \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \frac{4}{4} = 1$.
(C'est l'équivalent hyperbolique de la relation trigonométrique $\cos^2 x + \sin^2 x = 1$ !).

**20.**
```python
import math


def euler_comparaison(n=100):
  h = 1.0 / n
  y = 1.0
  for _ in range(n):
    y = y * (1 + h)
  exact = math.exp(1)
  erreur = abs(y - exact) / exact * 100
  print(f"Euler (n={n}) : {y:.6f}")
  print(f"Exact : {exact:.6f}")
  print(f"Erreur relative : {erreur:.3f}%")


euler_comparaison(100)
# Donne une erreur relative d'environ 0.49% seulement !
```

**21.** En $x = 0$, $f_k(0) = k e^0 = k$.
Dérivée : $f'_k(x) = k \cdot (k e^{kx}) = k^2 e^{kx}$.
La pente vaut $k^2$ si et seulement si $k^2 e^{kx} = k^2 \iff e^{kx} = 1 \iff kx = 0 \iff x = 0$ (car $k > 0$).
Pour toutes les fonctions de la famille, c'est systématiquement au point d'abscisse $x = 0$ que la pente de la tangente vaut $k^2$.

---

### La question qui ouvre la suite

L'exponentielle nous a permis de modéliser des populations qui se multiplient selon des lois mathématiques pures et parfaites.
Mais lorsque le biologiste compte ses bactéries dans la boîte de Pétri, ou lorsque le statisticien interroge un échantillon de mille citoyens dans la rue, les mesures ne tombent jamais sur une courbe lisse : elles oscillent, elles s'éparpillent, elles fluctuent au hasard.
Comment résumer un nuage de mesures éparpillées par deux nombres maîtres : le centre de gravité (**la moyenne**) et la largeur de dispersion (**l'écart-type**) ? C'est ce que nous allons découvrir au chapitre suivant avec **le sondeur et l'écart-type**.
