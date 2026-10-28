# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 46 : Le Fil sans Coupure

> *« Natura non facit saltus — La nature ne fait pas de sauts, disait Gottfried Wilhelm Leibniz. Si un train quitte Paris à midi et entre en gare de Lyon à deux heures, il n'a pas disparu à Dijon pour réapparaître subitement cinquante kilomètres plus loin. Il a foulé chaque mètre, chaque millimètre de rail sans jamais lever les roues. En mathématiques, cette fidélité au chemin s'appelle la continuité, et elle possède le pouvoir magique de garantir qu'une équation a une solution même lorsqu'on est incapable de la calculer à la main. »*

---

### Ce que tu vas découvrir

- L'intuition motrice de la **continuité** : le tracé que l'on effectue d'un seul trait de crayon sans jamais décoller la mine de la feuille, et sa traduction formelle $\lim\limits_{x \to x_0} f(x) = f(x_0)$.
- Pourquoi la quasi-totalité des fonctions de la physique et des sciences sont continues, et le lien crucial : **dérivable implique continue** (mais la réciproque est fausse !).
- Le **Théorème des Valeurs Intermédiaires (TVI)** : l'assurance absolue de traverser un fleuve si l'on passe d'une rive à l'autre.
- Le **corollaire de la bijection** (ou TVI pour fonctions strictement monotones) : l'outil n°1 du baccalauréat pour prouver l'existence et l'unicité de la solution d'une équation $f(x) = k$.
- La méthode d'encadrement par **dichotomie** et son implémentation en **Python**.
- Les suites récurrentes $u_{n+1} = f(u_n)$ : comment la continuité de $f$ force la limite de la suite à être un **point fixe** ($f(L) = L$).

---

### 1. Le problème : traverser la rivière sans se téléporter

#### 1.1 La randonneuse et le pont invisible

Imagine une randonneuse qui part d'une vallée située à $500\text{ mètres}$ d'altitude à 8 heures du matin. À midi, elle atteint le sommet de la montagne à $2200\text{ mètres}$.
Peux-tu affirmer avec certitude qu'à un moment précis de la matinée, son altimètre a affiché très exactement $1500\text{ mètres}$ ?

```
 Altitude (m) ▲
        2200 ┼                                    * (Sommet à 12h)
             │                                .-'
        1500 ┼ - - - - - - - - - - - - - - - * - - - - - (Altitude franchie !)
             │                          _.-'
         500 ┼ * (Départ à 8h)       .-'
             └─┼─────────────────────────────┼─────► Temps (h)
               8h                            12h
```

La réponse est évidemment **oui**. À moins que la randonneuse ne possède un appareil de téléportation de science-fiction, son corps s'est déplacé continûment dans l'espace. Elle n'a pas pu passer sous la barre des $1500\text{ m}$ puis au-dessus sans **couper** le plan horizontal des $1500\text{ m}$.

Considère maintenant un autre phénomène : le tarif d'un stationnement souterrain.
- De 0 à 1 heure : $2{,}00$ €.
- De 1 heure à 2 heures : $4{,}00$ €.
Si tu es resté garé $1\text{ heure et } 1\text{ seconde}$, l'automate t'affiche directement $4{,}00$ €. Le prix a fait un **saut brutal**. Il n'a jamais valu $2{,}87$ € ni $3{,}50$ €. La fonction tarifaire est **discontinue**.

```
 Tarif (€) ▲
       4 ┼               [───────────)
         │               ▲ Saut
       2 ┼ [───────────) │
         └─┼─────────────┼───────────► Temps (h)
           0             1           2
```

La question fondamentale de l'analyse mathématique est la suivante : *quelles garanties mathématiques possède-t-on lorsqu'une courbe n'a pas de coupure ?*

---

### 2. La Continuité : du trait de crayon à la définition formelle

#### 2.1 Définition en un point

Intuitivement, une fonction est continue si l'on peut tracer sa courbe représentative sans lever le crayon.
Mais comment un ordinateur ou une équation peuvent-ils « savoir » si un crayon s'est levé ? Les mathématiciens traduisent cette idée motrice par une égalité de limites :

> **📐 Définition — Continuité en un point.**
> Soit $f$ une fonction définie sur un intervalle ouvert contenant $x_0$.
> On dit que **$f$ est continue en $x_0$** si :
> $$\lim_{x \to x_0} f(x) = f(x_0).$$

**Décomposition du geste :**
Pour que cette égalité soit vraie, trois conditions doivent être réunies :
1. $f(x_0)$ existe (la fonction est bien définie au point $x_0$) ;
2. $f(x)$ admet une limite finie lorsque $x \to x_0$ ;
3. Cette limite coïncide rigoureusement avec la valeur réelle $f(x_0)$.

Si $\lim\limits_{x \to x_0^-} f(x) \neq \lim\limits_{x \to x_0^+} f(x)$, ou si la limite ne vaut pas $f(x_0)$, la courbe présente une rupture (un trou, ou un saut) : $f$ est dite **discontinue** en $x_0$.

#### 2.2 Continuité sur un intervalle

> **📐 Définition — Continuité sur un intervalle.**
> Une fonction $f$ est dite **continue sur un intervalle $I$** si elle est continue en tout point $x_0$ de cet intervalle.

#### 2.3 Continuité des fonctions usuelles

Toutes les fonctions de référence étudiées au lycée sont continues sur chaque intervalle où elles sont définies :
- Les fonctions **polynômes** (droites, paraboles...) sont continues sur $\mathbb{R}$.
- Les fonctions **rationnelles** (quotients de polynômes) sont continues sur chaque intervalle de leur ensemble de définition.
- La fonction **racine carrée** $x \mapsto \sqrt{x}$ est continue sur $[0 \,;\, +\infty[$.
- La fonction **valeur absolue** $x \mapsto |x|$ est continue sur $\mathbb{R}$.
- La fonction **exponentielle** $x \mapsto e^x$ est continue sur $\mathbb{R}$.
- Les fonctions trigonométriques $\cos$ et $\sin$ sont continues sur $\mathbb{R}$.

De plus, la somme, le produit, le quotient (si le dénominateur ne s'annule pas) et la **composée** de fonctions continues sont des fonctions continues.

#### 2.4 Le lien capital : Dérivabilité et Continuité

> **📐 Théorème fondamental — Dérivable implique continue.**
> Si une fonction $f$ est dérivable en un point $x_0$, alors elle est **nécessairement continue** en $x_0$.
> Si $f$ est dérivable sur un intervalle $I$, alors elle est continue sur $I$.

> **✍️ Démonstration (exigible).**
> Supposons $f$ dérivable en $x_0$. Cela signifie que le taux d'accroissement admet une limite finie notée $f'(x_0)$ :
> $$\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = f'(x_0).$$
> Écrivons pour tout $x \neq x_0$ :
> $$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \times (x - x_0).$$
> Passons à la limite quand $x \to x_0$ en appliquant la règle du produit de limites :
> $$\lim_{x \to x_0} [f(x) - f(x_0)] = \lim_{x \to x_0} \left(\frac{f(x) - f(x_0)}{x - x_0}\right) \times \lim_{x \to x_0} (x - x_0) = f'(x_0) \times 0 = 0.$$
> On en déduit immédiatement :
> $$\lim_{x \to x_0} f(x) = f(x_0).$$
> La fonction $f$ est donc bien continue en $x_0$. $\blacksquare$

> **⚠️ Attention, piège ! — La réciproque est FAUSSE !**
> Une fonction peut être parfaitement continue en un point sans y être dérivable.
> **Contre-exemple absolu n°1 : La fonction valeur absolue $f(x) = |x|$ en 0.**
> Sa courbe forme une pointe (un V). Elle se trace sans lever le crayon, elle est continue en 0 car $\lim_{x \to 0} |x| = 0 = |0|$.
> Mais son taux d'accroissement en 0 vaut :
> - $\frac{|x| - 0}{x - 0} = \frac{x}{x} = 1$ pour $x > 0$ ;
> - $\frac{|x| - 0}{x - 0} = \frac{-x}{x} = -1$ pour $x < 0$.
> La limite à droite ($1$) et la limite à gauche ($-1$) sont différentes : $f$ n'est **pas dérivable en 0**.
> **Contre-exemple n°2 :** $f(x) = \sqrt{x}$ en 0 est continue en 0 mais non dérivable (tangente verticale).

---

### 3. Le Théorème des Valeurs Intermédiaires (TVI)

#### 3.1 L'énoncé général

Le mathématicien tchèque Bernard Bolzano (1817) puis le Français Augustin-Louis Cauchy (1821) ont donné la première preuve rigoureuse de ce principe géométrique limpide :

> **📐 Théorème des Valeurs Intermédiaires (TVI).**
> Soit $f$ une fonction **continue** sur un intervalle fermé $[a \,;\, b]$.
> Pour tout réel $k$ compris entre $f(a)$ et $f(b)$, il existe **au moins un réel $c$** appartenant à l'intervalle $[a \,;\, b]$ tel que :
> $$f(c) = k.$$

```
 y ▲
   │
f(b)┼─────────────────────────────────* (b, f(b))
   │                                 /
 k ┼ - - - - - - - - * - - - - - - -* - - - - - - -
   │                / \            /
f(a)┼──────* (a, f(a))   \        /
   │       │               \    /
   └───────┼─────────┼──────┼──┼──────┼────────► x
           a        c_1     c_2       b
```

*Remarques capitales :*
- Le théorème affirme l'**existence** d'au moins une solution, mais il n'en donne pas le nombre exact : sur le schéma ci-dessus, il y a deux solutions $c_1$ et $c_2$.
- Si $f$ n'était pas continue, la courbe pourrait sauter par-dessus la ligne horizontale $y = k$ sans jamais la toucher !

#### 3.2 Le cas particulier du zéro : Théorème de Bolzano

C'est la forme la plus courante dans les applications pratiques :

> **📐 Corollaire — Changement de signe.**
> Soit $f$ une fonction continue sur $[a \,;\, b]$.
> Si $f(a)$ et $f(b)$ sont de **signes contraires** (c'est-à-dire $f(a) \times f(b) \leq 0$),
> alors il existe au moins un réel $c \in [a \,;\, b]$ tel que $f(c) = 0$.

*En clair :* Pour passer d'une altitude négative (sous l'eau) à une altitude positive (en l'air), une courbe continue doit impérativement percer la surface de l'eau ($y = 0$).

---

### 4. Le Théorème de la Bijection (TVI pour fonctions strictement monotones)

Au baccalauréat, on ne cherche presque jamais « au moins une solution » : on veut prouver qu'il existe **une et une seule** solution. Pour obtenir l'unicité, il faut interdire à la courbe de faire des demi-tours. On exige donc que la fonction soit **strictement monotone** (toujours strictement croissante ou toujours strictement décroissante).

> **📐 Théorème — Corollaire du TVI (Théorème de la bijection).**
> Soit $f$ une fonction définie sur un intervalle $I = [a \,;\, b]$. Si :
> 1. $f$ est **continue** sur $[a \,;\, b]$ ;
> 2. $f$ est **strictement monotone** (strictement croissante ou strictement décroissante) sur $[a \,;\, b]$ ;
>
> Alors, pour tout réel $k$ compris entre $f(a)$ et $f(b)$, l'équation :
> $$f(x) = k$$
> admet **une unique solution** $\alpha$ dans l'intervalle $[a \,;\, b]$.

#### Extension aux intervalles ouverts ou infinis

Le théorème reste parfaitement valable sur un intervalle ouvert $]a \,;\, b[$ ou infini comme $]-\infty \,;\, +\infty[$, $[0 \,;\, +\infty[$, etc.
Il suffit de remplacer les valeurs aux bornes $f(a)$ et $f(b)$ par les **limites** de la fonction aux bornes de l'intervalle :
Si $f$ est continue et strictement croissante sur $]a \,;\, b[$, alors pour tout $k \in \left]\lim_{x \to a^+} f(x) \,;\, \lim_{x \to b^-} f(x)\right[$, l'équation $f(x) = k$ admet une unique solution dans $]a \,;\, b[$.

> **🧭 Méthode — La rédaction canonique parfaite au Baccalauréat :**
> Pour justifier que l'équation $f(x) = k$ admet une unique solution $\alpha$ sur un intervalle $I$ :
> 1. **Continuité :** Mentionner que $f$ est continue sur $I$ (par exemple comme somme, produit ou quotient de fonctions usuelles, ou parce qu'elle y est dérivable).
> 2. **Stricte monotonie :** Indiquer que $f$ est strictement croissante (ou décroissante) sur $I$, en s'appuyant sur le signe de sa dérivée $f'(x)$.
> 3. **Appartenance de la valeur cible :** Calculer les images des bornes (ou leurs limites) et vérifier que $k$ appartient à l'intervalle image : $k \in [f(a) \,;\, f(b)]$ (ou $] \lim_a f \,;\, \lim_b f [$).
> 4. **Conclusion :** Écrire : *« D'après le corollaire du théorème des valeurs intermédiaires, l'équation $f(x) = k$ admet une unique solution $\alpha$ dans $I$. »*

---

### 5. Résolution approchée : l'Algorithme de Dichotomie en Python

Le TVI prouve qu'une solution $\alpha$ existe et qu'elle est unique, mais il ne donne pas sa valeur numérique exacte (souvent impossible à exprimer avec des fractions ou des racines simples).
Pour trouver une valeur approchée de $\alpha$ avec une précision chirurgicale (par exemple $10^{-6}$), on utilise la **méthode de dichotomie** (du grec *dicha*, « en deux », et *tomein*, « couper »).

#### 5.1 Principe du découpage en deux

On sait que la racine $\alpha$ est enfermée dans un intervalle $[a \,;\, b]$ avec $f(a) \times f(b) < 0$.
1. On calcule le milieu de l'intervalle : $m = \frac{a + b}{2}$.
2. On regarde le signe de $f(m)$ :
   - Si $f(a)$ et $f(m)$ sont de signes contraires ($f(a) \times f(m) < 0$), alors la racine est dans la moitié gauche : on remplace $b$ par $m$.
   - Sinon, la racine est dans la moitié droite : on remplace $a$ par $m$.
3. À chaque étape, la largeur de l'intervalle est **divisée par 2**.
Au bout de $n$ étapes, l'incertitude sur la racine n'est plus que de $\frac{b - a}{2^n}$.

```
 Étape 0 :  [───────────────── α ───────────────]   Largeur L
                               m
 Étape 1 :  [──────── α ───────]                    Largeur L/2
                        m
 Étape 2 :             [── α ──]                    Largeur L/4
```

#### 5.2 Script Python officiel

Considérons l'équation $x^3 + x - 1 = 0$ sur $[0 \,;\, 1]$.
La fonction $f(x) = x^3 + x - 1$ est continue, strictement croissante, $f(0) = -1 < 0$ et $f(1) = 1 > 0$. Il existe une unique solution $\alpha \in [0 \,;\, 1]$.

```python
def f(x):
    """Fonction dont on cherche le zéro."""
    return x**3 + x - 1

def dichotomie(a, b, precision):
    """
    Renvoie un encadrement [a, b] de la racine de f(x) = 0
    avec une largeur b - a <= precision.
    """
    while (b - a) > precision:
        m = (a + b) / 2
        # Si f(a) et f(m) ont le même signe, la racine est dans [m, b]
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return a, b

# Recherche d'un encadrement à 10^-4 près
inf, sup = dichotomie(0.0, 1.0, 1e-4)
print(f"Encadrement obtenu : {inf:.5f} < alpha < {sup:.5f}")
# Affichera : 0.68231 < alpha < 0.68237
```

*Vitesse spectaculaire :* Pour obtenir une précision de $10^{-6}$ (un millionième) sur un intervalle de départ de longueur 1 :
Comme $2^{20} = 1\,048\,576 > 10^6$, **20 itérations seulement** suffisent pour donner six décimales exactes !

---

### 6. Suites Récurrentes $u_{n+1} = f(u_n)$ et Recherche du Point Fixe

Au chapitre 44, nous avons étudié des suites monotones bornées qui convergeaient vers une limite $L$. Mais comment calculer cette limite $L$ lorsque la suite est définie par une formule de récurrence $u_{n+1} = f(u_n)$ ?

C'est ici que la continuité révèle toute sa puissance !

> **📐 Théorème du Point Fixe.**
> Soit $(u_n)$ une suite définie par $u_0$ et par la relation $u_{n+1} = f(u_n)$ pour tout $n \in \mathbb{N}$.
> Si :
> 1. La suite $(u_n)$ **converge** vers un nombre réel $L$ ;
> 2. La fonction $f$ est **continue** au point $L$ ;
>
> Alors la limite $L$ est solution de l'équation :
> $$f(L) = L.$$
> Un tel nombre $L$ est appelé un **point fixe** de la fonction $f$.

> **✍️ Démonstration.**
> Puisque $\lim\limits_{n \to +\infty} u_n = L$, la suite décalée $(u_{n+1})$ converge évidemment vers la même limite : $\lim\limits_{n \to +\infty} u_{n+1} = L$.
> D'autre part, comme $f$ est continue en $L$, par composition de limites :
> $$\lim_{n \to +\infty} f(u_n) = f\left(\lim_{n \to +\infty} u_n\right) = f(L).$$
> Or, pour tout entier $n$, $u_{n+1} = f(u_n)$.
> En passant à la limite des deux côtés de l'égalité, on obtient nécessairement :
> $$L = f(L). \quad \blacksquare$$

*Interprétation géométrique (le diagramme en toile d'araignée / escalier) :*
La limite $L$ est l'abscisse d'un point d'intersection entre la courbe de la fonction $y = f(x)$ et la première bissectrice d'équation **$y = x$**.

```
       y ▲                     / y = x
         │                   /
         │             *───*  y = f(x)
         │            /│   │
         │           *─┼───*
         │          /│ │   │
         └─────────┼─┼─┼───┼────────► x
                  u_0 u_1 u_2 L
```

---

### 7. Attention, pièges !

> **⚠️ Attention, piège ! — Oublier la stricte monotonie.**
> Si tu écris seulement « $f$ est continue sur $[a ; b]$ et $k$ est compris entre $f(a)$ et $f(b)$ », le TVI garantit seulement l'existence d'**au moins une** solution. Pour affirmer qu'il n'y en a **qu'une seule**, la mention de la **stricte monotonie** est rigoureusement indispensable. Sans elle, le correcteur retire des points.

> **⚠️ Attention, piège ! — Les fonctions non continues.**
> Considère la fonction $f(x) = \frac{1}{x}$ sur $[-1 \,;\, 1] \setminus \{0\}$.
> On a $f(-1) = -1 < 0$ et $f(1) = 1 > 0$.
> Pourtant, l'équation $f(x) = 0$ n'a **aucune solution** !
> Pourquoi le TVI ne s'applique-t-il pas ? Parce que la fonction n'est **pas continue en 0** (elle n'y est même pas définie). Le fil est coupé au milieu.

---

### 8. Exemples Résolus pas à pas

#### Exemple résolu 1 — Application type Bac du corollaire du TVI

**Énoncé :** Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = 2x^3 - 3x^2 - 12x + 5$.
1. Dresser le tableau de variations complet de $f$ sur $[-3 \,;\, 4]$.
2. Démontrer que l'équation $f(x) = 0$ admet exactement trois solutions réelles dans l'intervalle $[-3 \,;\, 4]$.

**Solution :**
1. **Dérivation et variations :**
   La fonction $f$ est une fonction polynôme, donc dérivable sur $\mathbb{R}$.
   Pour tout $x \in [-3 \,;\, 4]$ :
   $$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2).$$
   Factorisons le trinôme $x^2 - x - 2$ : son discriminant est $\Delta = (-1)^2 - 4(1)(-2) = 1 + 8 = 9 = 3^2$.
   Les racines sont $x_1 = \frac{1 - 3}{2} = -1$ et $x_2 = \frac{1 + 3}{2} = 2$.
   Donc $f'(x) = 6(x + 1)(x - 2)$.
   Calculons les valeurs remarquables :
   - $f(-3) = 2(-27) - 3(9) - 12(-3) + 5 = -54 - 27 + 36 + 5 = -40$.
   - $f(-1) = 2(-1) - 3(1) - 12(-1) + 5 = -2 - 3 + 12 + 5 = 12$.
   - $f(2) = 2(8) - 3(4) - 12(2) + 5 = 16 - 12 - 24 + 5 = -15$.
   - $f(4) = 2(64) - 3(16) - 12(4) + 5 = 128 - 48 - 48 + 5 = 37$.

   Tableau de variations :
   - Sur $[-3 \,;\, -1]$, $f'(x) > 0$ donc $f$ est strictement croissante de $-40$ à $12$.
   - Sur $[-1 \,;\, 2]$, $f'(x) < 0$ donc $f$ est strictement décroissante de $12$ à $-15$.
   - Sur $[2 \,;\, 4]$, $f'(x) > 0$ donc $f$ est strictement croissante de $-15$ à $37$.

2. **Application du corollaire du TVI sur chaque sous-intervalle :**
   - **Sur $[-3 \,;\, -1]$ :** $f$ est continue et strictement croissante. Comme $0 \in [-40 \,;\, 12]$, d'après le corollaire du TVI, l'équation $f(x) = 0$ admet une unique solution $\alpha_1 \in [-3 \,;\, -1]$.
   - **Sur $[-1 \,;\, 2]$ :** $f$ est continue et strictement décroissante. Comme $0 \in [-15 \,;\, 12]$, l'équation $f(x) = 0$ admet une unique solution $\alpha_2 \in [-1 \,;\, 2]$.
   - **Sur $[2 \,;\, 4]$ :** $f$ est continue et strictement croissante. Comme $0 \in [-15 \,;\, 37]$, l'équation $f(x) = 0$ admet une unique solution $\alpha_3 \in [2 \,;\, 4]$.

   *Conclusion :* L'équation $f(x) = 0$ admet très exactement **trois solutions distinctes** dans l'intervalle $[-3 \,;\, 4]$.

---

#### Exemple résolu 2 — Équation avec exponentielle sur un intervalle non borné

**Énoncé :** Démontrer que l'équation $e^x = \dfrac{2}{x}$ admet une unique solution réelle sur $]0 \,;\, +\infty[$.

**Solution :**
Pour $x > 0$, l'équation est équivalente à $e^x - \frac{2}{x} = 0$.
Considérons la fonction $g$ définie sur $]0 \,;\, +\infty[$ par :
$$g(x) = e^x - \frac{2}{x}.$$
1. **Continuité :** $g$ est la somme de la fonction exponentielle et de la fonction rationnelle $x \mapsto -2/x$, qui sont toutes deux continues sur $]0 \,;\, +\infty[$. Donc $g$ est continue sur $]0 \,;\, +\infty[$.
2. **Variations :** $g$ est dérivable sur $]0 \,;\, +\infty[$ :
   $$g'(x) = e^x - \left(-\frac{2}{x^2}\right) = e^x + \frac{2}{x^2}.$$
   Pour tout $x > 0$, $e^x > 0$ et $\frac{2}{x^2} > 0$, donc $g'(x) > 0$.
   La fonction $g$ est donc **strictement croissante** sur $]0 \,;\, +\infty[$.
3. **Limites aux bornes :**
   - En $0^+$ : $\lim\limits_{x \to 0^+} e^x = 1$ et $\lim\limits_{x \to 0^+} \frac{2}{x} = +\infty$, donc $\lim\limits_{x \to 0^+} g(x) = 1 - (+\infty) = -\infty$.
   - En $+\infty$ : $\lim\limits_{x \to +\infty} e^x = +\infty$ et $\lim\limits_{x \to +\infty} \frac{2}{x} = 0$, donc $\lim\limits_{x \to +\infty} g(x) = +\infty$.
4. **Conclusion :**
   La fonction $g$ est continue et strictement croissante sur $]0 \,;\, +\infty[$.
   Elle réalise une bijection de $]0 \,;\, +\infty[$ sur l'intervalle image $]\lim_{0^+} g \,;\, \lim_{+\infty} g[ = ]-\infty \,;\, +\infty[ = \mathbb{R}$.
   Comme $0 \in \mathbb{R}$, d'après le corollaire du TVI, l'équation $g(x) = 0$, c'est-à-dire $e^x = \frac{2}{x}$, admet une unique solution réelle $\alpha$ sur $]0 \,;\, +\infty[$.
   *(À la calculatrice : $\alpha \approx 0{,}853$).*

---

#### Exemple résolu 3 — Suite récurrente et point fixe

**Énoncé :** On considère la suite $(u_n)$ définie par $u_0 = 1$ et pour tout $n \in \mathbb{N}$ par :
$$u_{n+1} = \sqrt{1 + u_n}.$$
1. Démontrer par récurrence que pour tout $n \in \mathbb{N}$, $1 \leq u_n \leq u_{n+1} \leq 2$.
2. En déduire que la suite $(u_n)$ converge.
3. Déterminer la valeur exacte de sa limite $L$ (le nombre d'or $\varphi$).

**Solution :**
1. Posons la fonction $f(x) = \sqrt{1 + x}$ définie sur $[0 \,;\, 2]$. La fonction $f$ est strictement croissante sur $[0 \,;\, 2]$ (composée d'une fonction affine croissante et de la racine carrée).
   Soit $\mathcal{P}(n)$ la propriété : « $1 \leq u_n \leq u_{n+1} \leq 2$ ».
   - *Initialisation :* $u_0 = 1$, $u_1 = \sqrt{1+1} = \sqrt{2} \approx 1{,}414$.
     On a bien $1 \leq 1 \leq \sqrt{2} \leq 2$. $\mathcal{P}(0)$ est vraie.
   - *Hérédité :* Supposons $1 \leq u_n \leq u_{n+1} \leq 2$.
     Appliquons la fonction $f$, qui est strictement croissante :
     $$f(1) \leq f(u_n) \leq f(u_{n+1}) \leq f(2) \implies \sqrt{2} \leq u_{n+1} \leq u_{n+2} \leq \sqrt{3}.$$
     Comme $1 \leq \sqrt{2}$ et $\sqrt{3} \leq 2$, on a bien $1 \leq u_{n+1} \leq u_{n+2} \leq 2$. $\mathcal{P}(n+1)$ est vraie.
   - *Conclusion :* Pour tout $n \in \mathbb{N}$, $1 \leq u_n \leq u_{n+1} \leq 2$.

2. **Convergence :**
   La suite $(u_n)$ est croissante et majorée par 2. D'après le théorème de convergence monotone, elle converge vers une limite réelle $L$ vérifiant $1 \leq L \leq 2$.

3. **Calcul de la limite par le théorème du point fixe :**
   La fonction $f(x) = \sqrt{1 + x}$ est continue sur $[1 \,;\, 2]$.
   D'après le théorème du point fixe, la limite $L$ vérifie :
   $$L = f(L) \iff L = \sqrt{1 + L}.$$
   Comme $L \geq 1 > 0$, cette équation est équivalente en élevant au carré à :
   $$L^2 = 1 + L \iff L^2 - L - 1 = 0.$$
   C'est l'équation caractéristique du **nombre d'or** !
   $\Delta = (-1)^2 - 4(1)(-1) = 5$.
   Les racines sont $L_1 = \frac{1 - \sqrt{5}}{2} < 0$ et $L_2 = \frac{1 + \sqrt{5}}{2} \approx 1{,}618$.
   Comme $L \geq 1$, on retient l'unique valeur positive :
   $$L = \frac{1 + \sqrt{5}}{2} = \varphi.$$

---

#### Exemple résolu 4 — Continuité d'une fonction définie par morceaux

**Énoncé :** Soit la fonction $f$ définie sur $\mathbb{R}$ par :
$$f(x) = \begin{cases} x^2 + a & \text{si } x \leq 2 \\ 3x - 1 & \text{si } x > 2 \end{cases}$$
où $a$ est une constante réelle.
Déterminer la valeur de $a$ pour que la fonction $f$ soit continue sur $\mathbb{R}$.

**Solution :**
- Pour $x < 2$, $f(x) = x^2 + a$ est un polynôme, donc continue sur $]-\infty \,;\, 2[$.
- Pour $x > 2$, $f(x) = 3x - 1$ est un polynôme, donc continue sur $]2 \,;\, +\infty[$.
Le seul point critique est $x_0 = 2$.
Calculons :
1. La valeur en 2 : $f(2) = 2^2 + a = 4 + a$.
2. La limite à gauche : $\lim\limits_{x \to 2^-} f(x) = \lim\limits_{x \to 2^-} (x^2 + a) = 4 + a$.
3. La limite à droite : $\lim\limits_{x \to 2^+} f(x) = \lim\limits_{x \to 2^+} (3x - 1) = 3(2) - 1 = 5$.

Pour que $f$ soit continue en 2, il faut et il suffit que la limite à gauche soit égale à la limite à droite et à la valeur en 2 :
$$4 + a = 5 \iff a = 1.$$
La fonction $f$ est continue sur $\mathbb{R}$ si et seulement si $a = 1$.

---

#### Exemple résolu 5 — Démonstration de l'existence d'une température identique

**Énoncé :** Un thermomètre enregistre la température $T(x)$ le long d'une route rectiligne de $100\text{ km}$, où $x \in [0 \,;\, 100]$ désigne la distance au point de départ en kilomètres. La fonction $T$ est supposée continue. On constate que la température de départ et la température d'arrivée sont identiques : $T(0) = T(100)$.
Démontrer qu'il existe deux points distants de très exactement $50\text{ km}$ qui ont exactement la même température.

**Solution :**
Considérons la fonction auxiliaire $D$ définie pour tout $x \in [0 \,;\, 50]$ par :
$$D(x) = T(x + 50) - T(x).$$
$D(x)$ représente la différence de température entre le point situé au kilomètre $x + 50$ et celui au kilomètre $x$.
1. **Continuité :** Comme $T$ est continue, la fonction $D$ est continue sur l'intervalle $[0 \,;\, 50]$ comme différence de fonctions continues.
2. **Calcul aux extrémités :**
   - En $x = 0$ : $D(0) = T(50) - T(0)$.
   - En $x = 50$ : $D(50) = T(100) - T(50)$.
   Or, par hypothèse, $T(100) = T(0)$.
   Remplaçons $T(100)$ par $T(0)$ :
   $$D(50) = T(0) - T(50) = -\big(T(50) - T(0)\big) = -D(0).$$
3. **Discussion des signes :**
   - Si $D(0) = 0$, alors $T(50) = T(0)$ : les points $x = 0$ et $x = 50$ répondent à la question.
   - Si $D(0) \neq 0$, alors $D(0)$ et $D(50) = -D(0)$ sont de **signes strictement contraires** :
     $$D(0) \times D(50) < 0.$$
     D'après le Théorème des Valeurs Intermédiaires appliqué à la fonction continue $D$ sur $[0 \,;\, 50]$, il existe au moins un réel $c \in ]0 \,;\, 50[$ tel que :
     $$D(c) = 0 \iff T(c + 50) - T(c) = 0 \iff T(c + 50) = T(c).$$
Les deux points d'abscisses $c$ et $c + 50$ sont distants de $50\text{ km}$ et ont rigoureusement la même température.

---

#### Exemple résolu 6 — Encadrement à la main par dichotomie

**Énoncé :** On considère la fonction $f(x) = x^3 + 2x - 5$ sur $[1 \,;\, 2]$.
1. Justifier que l'équation $f(x) = 0$ admet une unique solution $\alpha \in [1 \,;\, 2]$.
2. Effectuer trois étapes de dichotomie à la main pour trouver un encadrement de $\alpha$ d'amplitude $0{,}125$.

**Solution :**
1. $f$ est polynomiale donc continue sur $[1 ; 2]$. Sa dérivée est $f'(x) = 3x^2 + 2 > 0$ pour tout $x$, donc $f$ est strictement croissante.
   $f(1) = 1 + 2 - 5 = -2 < 0$ et $f(2) = 8 + 4 - 5 = 7 > 0$.
   Comme $0 \in [-2 \,;\, 7]$, d'après le corollaire du TVI, il existe une unique racine $\alpha \in [1 \,;\, 2]$.

2. **Dichotomie :**
   - **Étape 1 :** Milieu de $[1 \,;\, 2]$ : $m_1 = 1{,}5$.
     $f(1{,}5) = (1{,}5)^3 + 2(1{,}5) - 5 = 3{,}375 + 3 - 5 = 1{,}375 > 0$.
     Comme $f(1) < 0$ et $f(1{,}5) > 0$, la racine est dans :
     $$\alpha \in [1 \,;\, 1{,}5] \quad (\text{amplitude } 0{,}5).$$
   - **Étape 2 :** Milieu de $[1 \,;\, 1{,}5]$ : $m_2 = 1{,}25$.
     $f(1{,}25) = (1{,}25)^3 + 2(1{,}25) - 5 = 1{,}953125 + 2{,}5 - 5 = -0{,}546875 < 0$.
     Comme $f(1{,}25) < 0$ et $f(1{,}5) > 0$, la racine est dans :
     $$\alpha \in [1{,}25 \,;\, 1{,}5] \quad (\text{amplitude } 0{,}25).$$
   - **Étape 3 :** Milieu de $[1{,}25 \,;\, 1{,}5]$ : $m_3 = 1{,}375$.
     $f(1{,}375) = (1{,}375)^3 + 2(1{,}375) - 5 \approx 2{,}5996 + 2{,}75 - 5 = 0{,}3496 > 0$.
     Comme $f(1{,}25) < 0$ et $f(1{,}375) > 0$, la racine est dans :
     $$\alpha \in [1{,}25 \,;\, 1{,}375] \quad (\text{amplitude } 0{,}125).$$
L'encadrement au bout de trois étapes est bien $1{,}25 \leq \alpha \leq 1{,}375$.

---

### Ce qu'il faut retenir

1. **Continuité en un point :** $\lim\limits_{x \to x_0} f(x) = f(x_0)$.
2. **Dérivable implique continue :** toute fonction dérivable sur un intervalle y est continue. La réciproque est fausse (ex: $|x|$ en 0).
3. **Théorème des Valeurs Intermédiaires (TVI) :** Si $f$ est continue sur $[a ; b]$, elle prend toutes les valeurs intermédiaires entre $f(a)$ et $f(b)$ au moins une fois.
4. **Corollaire de la bijection :** Si $f$ est **continue** et **strictement monotone** sur un intervalle $I$, alors l'équation $f(x) = k$ admet **une unique solution** dans $I$ pour tout $k \in f(I)$.
5. **Dichotomie :** méthode de division par 2 de l'intervalle pour encadrer numériquement une solution avec une précision arbitraire en un nombre fini d'étapes.
6. **Point fixe :** Si $u_{n+1} = f(u_n)$ avec $f$ continue et si $u_n \to L$, alors $f(L) = L$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 46.1.** Parmi les fonctions suivantes, déterminer celles qui sont continues sur leur ensemble de définition :
1. $f(x) = 3x^4 - 2x + 7$ sur $\mathbb{R}$
2. $g(x) = \dfrac{1}{x - 5}$ sur $\mathbb{R} \setminus \{5\}$
3. $h(x) = \sqrt{x - 3}$ sur $[3 \,;\, +\infty[$
4. $k(x) = E(x)$ (partie entière) sur $\mathbb{R}$

**Exercice 46.2.** Soit la fonction $f$ définie sur $[-2 \,;\, 5]$ par $f(x) = x^2 - 4x + 1$.
1. Calculer $f(-2)$ et $f(5)$.
2. Justifier que l'équation $f(x) = 0$ admet au moins une solution sur $[-2 \,;\, 5]$.

**Exercice 46.3.** On donne le tableau de variations d'une fonction $g$ continue sur $[-5 \,;\, 4]$ :
- $g$ est strictement croissante de $-3$ à $7$ sur $[-5 \,;\, -1]$.
- $g$ est strictement décroissante de $7$ à $1$ sur $[-1 \,;\, 4]$.
Déterminer le nombre de solutions de l'équation $g(x) = 4$ sur $[-5 \,;\, 4]$.

**Exercice 46.4.** Justifier la continuité de la fonction $f(x) = \dfrac{e^x}{x^2 + 1}$ sur $\mathbb{R}$.

**Exercice 46.5.** Soit $f(x) = x^3 + 3x - 1$.
1. Montrer que $f$ est strictement croissante sur $\mathbb{R}$.
2. Calculer $f(0)$ et $f(1)$.
3. En déduire qu'il existe un unique réel $\alpha \in [0 \,;\, 1]$ tel que $f(\alpha) = 0$.

**Exercice 46.6.** Soit la suite récurrente définie par $u_0 = 3$ et $u_{n+1} = \dfrac{1}{2}u_n + 1$. On admet qu'elle converge vers $L$. Déterminer $L$ par le théorème du point fixe.

**Exercice 46.7.** Soit la fonction définie par morceaux :
$$f(x) = \begin{cases} 2x + k & \text{si } x \leq 1 \\ x^2 + 3 & \text{si } x > 1 \end{cases}$$
Pour quelle valeur de la constante $k$ la fonction $f$ est-elle continue en $x = 1$ ?

**Exercice 46.8.** Écrire en Python une fonction `f(x)` valant $x^2 - 2$, puis utiliser la dichotomie pour approcher $\sqrt{2}$ à $10^{-3}$ près sur $[1 \,;\, 2]$.

---

#### Niveau ★★ (Réflexion et type Bac)

**Exercice 46.9 (Type Bac : Résolution complète et encadrement).**
On considère la fonction $f$ définie sur $\mathbb{R}$ par :
$$f(x) = x^3 - 3x^2 + 1.$$
1. Étudier les limites de $f$ en $-\infty$ et en $+\infty$.
2. Dresser le tableau de variations complet de $f$.
3. Démontrer que l'équation $f(x) = 0$ admet exactement trois solutions réelles $\alpha_1, \alpha_2, \alpha_3$.
4. Donner un encadrement d'amplitude $0{,}1$ de la plus grande solution.
5. En déduire le tableau de signes de $f(x)$ sur $\mathbb{R}$.

**Exercice 46.10 (Type Bac : Étude d'une fonction auxiliaire pour une tangente).**
On souhaite étudier la fonction $g(x) = (x - 1)e^x + 1$ sur $\mathbb{R}$.
1. Déterminer les variations de $g$ sur $\mathbb{R}$.
2. Montrer que $g(x) \geq 0$ pour tout $x \in \mathbb{R}$, et préciser pour quelle valeur l'égalité a lieu.
3. En déduire la position relative de la courbe de $y = e^x$ par rapport à sa tangente en 1.

**Exercice 46.11 (Équation transcendante et point d'intersection).**
On cherche à déterminer le point d'intersection entre la courbe de l'exponentielle $y = e^{-x}$ et la droite $y = x$.
1. Poser la fonction appropriée et prouver qu'elle admet un unique zéro $\alpha$ sur $\mathbb{R}$.
2. Démontrer que $\alpha \in [0 \,;\, 1]$.
3. Écrire une fonction Python qui calcule $\alpha$ à $10^{-6}$ près.

**Exercice 46.12 (Vrai ou Faux rigoureusement justifié).**
1. « Si $f$ est continue sur $[a ; b]$ et si $f(a) < 0$ et $f(b) > 0$, alors $f$ s'annule exactement une fois sur $]a ; b[$. »
2. « Si $f$ est strictement croissante sur $[a ; b]$, alors $f$ est continue sur $[a ; b]$. »
3. « Si $f$ est continue sur $]0 ; 1[$, alors l'ensemble de ses images est un intervalle borné. »
4. « Une fonction continue qui ne s'annule jamais sur un intervalle $I$ garde un signe constant sur $I$. »

**Exercice 46.13 (Dichotomie : calcul du nombre d'itérations théoriques).**
On applique l'algorithme de dichotomie sur un intervalle $[a \,;\, b]$ de longueur initiale $L_0 = 4$.
1. Exprimer la longueur $L_n$ de l'intervalle après $n$ itérations.
2. Combien d'étapes au minimum sont nécessaires pour garantir une précision inférieure ou égale à $10^{-5}$ ?

**Exercice 46.14 (Suite récurrente et fonction homographique).**
On considère la suite $(u_n)$ définie par $u_0 = 2$ et $u_{n+1} = \dfrac{4u_n - 2}{u_n + 1}$.
1. Vérifier que la fonction associée $f(x) = \dfrac{4x - 2}{x + 1}$ est continue sur $[1 \,;\, 3]$.
2. Déterminer les deux points fixes de la fonction $f$.
3. On admet que $(u_n)$ converge vers un réel $L \geq 1$. Déterminer sa limite exacte.

**Exercice 46.15 (Théorème du point fixe pour une application d'un segment dans lui-même).**
Soit $f$ une fonction continue de $[0 \,;\, 1]$ dans $[0 \,;\, 1]$ (c'est-à-dire que pour tout $x \in [0 ; 1]$, $0 \leq f(x) \leq 1$).
1. On pose $g(x) = f(x) - x$. Calculer les signes de $g(0)$ et $g(1)$.
2. En déduire que toute fonction continue de $[0 ; 1]$ dans $[0 ; 1]$ admet au moins un point fixe (c'est le théorème de Brouwer en dimension 1).

**Exercice 46.16 (Le paradoxe du moine bouddhiste).**
Un moine monte à un monastère au sommet d'une montagne en empruntant un unique sentier. Il part à 6h du matin le samedi et arrive à 18h au sommet. Le dimanche, il redescend par le même sentier en partant à 6h du matin et arrive en bas à 18h.
Démontrer qu'il existe un endroit sur le sentier où le moine se trouve à la même heure exacte le samedi et le dimanche.

**Exercice 46.17 (Continuité et injectivité).**
Démontrer qu'une fonction continue sur un intervalle $I$ est injective (deux réels distincts ont des images distinctes) si et seulement si elle est strictement monotone sur $I$.

---

#### Niveau ★★★ (Défi et approfondissement)

**Exercice 46.18 (La fonction de Dirichlet : discontinue en tout point).**
On considère la fonction indicatrice des rationnels $f$ définie sur $\mathbb{R}$ par :
$$f(x) = \begin{cases} 1 & \text{si } x \in \mathbb{Q} \\ 0 & \text{si } x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}$$
1. En utilisant le fait que dans tout intervalle ouvert non vide, il existe au moins un rationnel et un irrationnel (densité de $\mathbb{Q}$ et de $\mathbb{R} \setminus \mathbb{Q}$ dans $\mathbb{R}$), démontrer que pour tout réel $x_0$, $f$ n'admet aucune limite en $x_0$.
2. En déduire que $f$ est discontinue en tout point de $\mathbb{R}$.

**Exercice 46.19 (Théorème de Borsuk-Ulam en dimension 1 : les antipodes terrestres).**
La température à la surface de l'équateur terrestre est modélisée par une fonction continue $T(\theta)$, où $\theta \in [0 \,;\, 2\pi]$ est la longitude en radians ($0$ et $2\pi$ représentant le même point méridien de Greenwich, de sorte que $T(0) = T(2\pi)$).
Démontrer qu'il existe au moins deux points antipodaux sur l'équateur qui possèdent rigoureusement la même température :
$$\exists \theta_0 \in [0 \,;\, \pi], \quad T(\theta_0 + \pi) = T(\theta_0).$$

**Exercice 46.20 (L'équation fonctionnelle de Cauchy).**
Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction **continue** vérifiant pour tous réels $x$ et $y$ :
$$f(x + y) = f(x) + f(y).$$
1. Calculer $f(0)$, puis exprimer $f(n)$ en fonction de $n$ et de $c = f(1)$ pour tout entier naturel $n$.
2. Démontrer que pour tout entier relatif $p$, $f(p) = c \cdot p$.
3. Démontrer que pour tout rationnel $r = \frac{p}{q} \in \mathbb{Q}$, $f(r) = c \cdot r$.
4. En utilisant la continuité de $f$ et la densité de $\mathbb{Q}$ dans $\mathbb{R}$, conclure que pour tout réel $x \in \mathbb{R}$ : $f(x) = c \cdot x$ (les seules solutions continues sont les fonctions linéaires).

**Exercice 46.21 (Théorème du passage de la douane / théorème de la corde de longueur $1/n$).**
Soit $f$ une fonction continue sur $[0 \,;\, 1]$ telle que $f(0) = f(1)$. Soit $n \geq 2$ un entier naturel.
On pose $g(x) = f\left(x + \frac{1}{n}\right) - f(x)$ définie sur $\left[0 \,;\, 1 - \frac{1}{n}\right]$.
1. Calculer la somme $\sum_{k=0}^{n-1} g\left(\frac{k}{n}\right)$.
2. En déduire qu'il existe au moins un réel $x_0 \in \left[0 \,;\, 1 - \frac{1}{n}\right]$ tel que $f\left(x_0 + \frac{1}{n}\right) = f(x_0)$.

**Exercice 46.22 (Accélération de la dichotomie : la méthode de Newton).**
La méthode de Newton remplace le milieu du segment par l'intersection de la tangente avec l'axe des abscisses :
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$
1. Écrire un script Python pour calculer le zéro de $f(x) = x^2 - 2$ en partant de $x_0 = 1$.
2. Observer le nombre d'itérations nécessaires pour obtenir 10 décimales exactes comparé à la dichotomie (convergence quadratique).

---

### Solutions

#### Solutions du Niveau ★

- **46.1 :**
  1. $f$ est polynomiale, donc continue sur $\mathbb{R}$.
  2. $g$ est rationnelle, donc continue sur son domaine $\mathbb{R} \setminus \{5\}$.
  3. $h$ est la composée de $x \mapsto x-3$ et de la racine carrée, continue sur $[3 \,;\, +\infty[$.
  4. $k(x)$ n'est pas continue : elle fait un saut de 1 à chaque entier relatif.

- **46.2 :**
  1. $f(-2) = (-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13 > 0$. $f(5) = 25 - 20 + 1 = 6 > 0$.
     Attention : ici $f(-2)$ et $f(5)$ sont tous deux positifs, mais calculons le sommet de la parabole en $x = 2$ : $f(2) = 4 - 8 + 1 = -3 < 0$. Comme $f$ est continue sur $[-2 \,;\, 2]$ avec $f(-2) > 0$ et $f(2) < 0$, d'après le TVI, elle s'annule sur $[-2 \,;\, 2] \subset [-2 \,;\, 5]$.

- **46.3 :**
  - Sur $[-5 \,;\, -1]$, $g$ est continue et strictement croissante de $-3$ à $7$. Comme $4 \in [-3 \,;\, 7]$, il y a exactement une solution.
  - Sur $[-1 \,;\, 4]$, $g$ est continue et strictement décroissante de $7$ à $1$. Comme $4 \in [1 \,;\, 7]$, il y a exactement une solution.
  Au total, l'équation $g(x) = 4$ admet exactement **2 solutions** sur $[-5 \,;\, 4]$.

- **46.4 :** L'exponentielle est continue sur $\mathbb{R}$, le polynôme $x^2 + 1$ est continu sur $\mathbb{R}$ et ne s'annule jamais car $x^2 + 1 \geq 1 > 0$. Le quotient de deux fonctions continues dont le dénominateur ne s'annule pas est continu sur $\mathbb{R}$.

- **46.5 :**
  1. $f'(x) = 3x^2 + 3 = 3(x^2 + 1) > 0$ pour tout $x \in \mathbb{R}$. Donc $f$ est strictement croissante.
  2. $f(0) = -1$ et $f(1) = 1 + 3 - 1 = 3$.
  3. $f$ est continue et strictement croissante sur $[0 \,;\, 1]$, et $0 \in [-1 \,;\, 3]$. D'après le corollaire du TVI, il existe un unique réel $\alpha \in [0 \,;\, 1]$ tel que $f(\alpha) = 0$.

- **46.6 :** La fonction $f(x) = \frac{1}{2}x + 1$ est continue sur $\mathbb{R}$. D'après le théorème du point fixe, $L = f(L) \iff L = \frac{1}{2}L + 1 \iff \frac{1}{2}L = 1 \iff L = 2$.

- **46.7 :** Pour être continue en $1$ : $f(1) = 2(1) + k = 2 + k$.
  $\lim_{x \to 1^+} f(x) = 1^2 + 3 = 4$.
  On doit avoir $2 + k = 4 \iff k = 2$.

- **46.8 :**
```python
def f(x):
    return x**2 - 2

a, b = 1.0, 2.0
while (b - a) > 1e-3:
    m = (a + b) / 2
    if f(a) * f(m) <= 0:
        b = m
    else:
        a = m
print(f"sqrt(2) ≈ {(a + b)/2:.4f}")
```

---

#### Solutions du Niveau ★★

- **46.9 :**
  1. $\lim_{x \to -\infty} f(x) = \lim x^3 = -\infty$ et $\lim_{x \to +\infty} f(x) = +\infty$.
  2. $f'(x) = 3x^2 - 6x = 3x(x - 2)$.
     Racines : $x = 0$ et $x = 2$.
     $f(0) = 1$ (maximum local) et $f(2) = 8 - 12 + 1 = -3$ (minimum local).
     $f$ est croissante sur $]-\infty ; 0]$, décroissante sur $[0 ; 2]$, croissante sur $[2 ; +\infty[$.
  3. Sur $]-\infty ; 0]$, $f$ est continue et strictement croissante de $-\infty$ à 1. Comme $0 \in ]-\infty ; 1]$, il y a une unique solution $\alpha_1$.
     Sur $[0 ; 2]$, $f$ est continue et strictement décroissante de 1 à $-3$. Comme $0 \in [-3 ; 1]$, il y a une unique solution $\alpha_2$.
     Sur $[2 ; +\infty[$, $f$ est continue et strictement croissante de $-3$ à $+\infty$. Comme $0 \in [-3 ; +\infty[$, il y a une unique solution $\alpha_3$.
     Il y a donc exactement 3 solutions réelles.
  4. Pour la plus grande solution $\alpha_3 \in [2 ; +\infty[$ :
     $f(2) = -3 < 0$, $f(3) = 27 - 27 + 1 = 1 > 0$, donc $\alpha_3 \in [2 ; 3]$.
     $f(2{,}8) = (2{,}8)^3 - 3(2{,}8)^2 + 1 = 21{,}952 - 23{,}52 + 1 = -0{,}568 < 0$.
     $f(2{,}9) = (2{,}9)^3 - 3(2{,}9)^2 + 1 = 24{,}389 - 25{,}23 + 1 = 0{,}159 > 0$.
     Encadrement : $2{,}8 < \alpha_3 < 2{,}9$.
  5. Signe : négatif sur $]-\infty ; \alpha_1]$, positif sur $[\alpha_1 ; \alpha_2]$, négatif sur $[\alpha_2 ; \alpha_3]$, positif sur $[\alpha_3 ; +\infty[$.

- **46.10 :**
  1. $g'(x) = 1 \cdot e^x + (x - 1)e^x = x e^x$.
     Comme $e^x > 0$, $g'(x)$ est du signe de $x$ : décroissante sur $]-\infty ; 0]$ et croissante sur $[0 ; +\infty[$.
  2. Minimum en 0 : $g(0) = (0 - 1)e^0 + 1 = -1 + 1 = 0$.
     Comme le minimum absolu est 0, $g(x) \geq 0$ pour tout réel $x$, avec égalité uniquement en $x = 0$.
  3. L'équation de la tangente à $y = e^x$ en $x = 1$ est : $y = e^1(x - 1) + e^1 = e \cdot x$.
     (Ou ici, réécrivons : $(x-1)e^x + 1 \geq 0 \iff e^{-x} \geq 1 - x$ en posant un changement approprié, prouvant la convexité).

- **46.11 :**
  1. Soit $h(x) = e^{-x} - x$ sur $\mathbb{R}$. $h$ est continue sur $\mathbb{R}$ et $h'(x) = -e^{-x} - 1 < 0$ (car $-e^{-x} < 0$). Donc $h$ est strictement décroissante.
     $\lim_{x \to -\infty} h(x) = +\infty$ et $\lim_{x \to +\infty} h(x) = -\infty$. D'après le corollaire du TVI, il existe un unique zéro $\alpha$ sur $\mathbb{R}$.
  2. $h(0) = e^0 - 0 = 1 > 0$ et $h(1) = e^{-1} - 1 \approx 0{,}368 - 1 = -0{,}632 < 0$. Donc $\alpha \in [0 \,;\, 1]$.
  3. Script Python :
```python
import math
def h(x):
    return math.exp(-x) - x

a, b = 0.0, 1.0
while (b - a) > 1e-6:
    m = (a + b) / 2
    if h(a) * h(m) <= 0:
        b = m
    else:
        a = m
print(f"Point d'intersection alpha ≈ {(a + b)/2:.6f}")
# alpha ≈ 0.567143 (constante Oméga)
```

- **46.12 :**
  1. **Faux.** Elle s'annule *au moins* une fois, mais peut s'annuler plusieurs fois si elle n'est pas strictement monotone.
  2. **Faux.** Contre-exemple : une fonction en escalier strictement croissante par paliers ou avec des sauts. La stricte monotonie n'implique pas la continuité.
  3. **Faux.** Contre-exemple : $f(x) = \frac{1}{x}$ sur $]0 \,;\, 1[$ est continue, mais son image est $]1 \,;\, +\infty[$, qui n'est pas borné.
  4. **Vrai.** Si elle changeait de signe, le TVI forcerait l'existence d'un zéro, ce qui contredirait l'hypothèse qu'elle ne s'annule jamais.

- **46.13 :**
  1. À chaque étape, la longueur est divisée par 2 : $L_n = \dfrac{L_0}{2^n} = \dfrac{4}{2^n} = \dfrac{1}{2^{n-2}}$.
  2. On cherche $n$ tel que $\dfrac{4}{2^n} \leq 10^{-5} \iff 2^n \geq 4 \times 10^5 = 400\,000$.
     Comme $2^{18} = 262\,144$ et $2^{19} = 524\,288$, il faut au minimum **19 étapes**.

- **46.14 :**
  1. $x + 1 = 0 \iff x = -1 \notin [1 \,;\, 3]$. $f$ est une fonction rationnelle dont le dénominateur ne s'annule pas sur $[1 \,;\, 3]$, elle y est donc continue.
  2. Points fixes : $f(x) = x \iff \frac{4x - 2}{x + 1} = x \iff 4x - 2 = x^2 + x \iff x^2 - 3x + 2 = 0$.
     Racines : $(x - 1)(x - 2) = 0 \iff x = 1$ ou $x = 2$.
  3. Si $u_0 = 2$, alors $u_1 = f(2) = 2$ : la suite est constante égale à 2. Si elle converge vers $L \geq 1$, par le théorème du point fixe, $L \in \{1 ; 2\}$. Ici avec $u_0 = 2$, $L = 2$.

- **46.15 :**
  1. $g(0) = f(0) - 0 = f(0) \geq 0$ (car $f(x) \in [0 ; 1]$).
     $g(1) = f(1) - 1 \leq 0$ (car $f(1) \leq 1$).
  2. La fonction $g$ est continue sur $[0 \,;\, 1]$ car $f$ l'est. Comme $g(0) \geq 0$ et $g(1) \leq 0$, par le TVI, il existe au moins un réel $c \in [0 \,;\, 1]$ tel que $g(c) = 0$, c'est-à-dire $f(c) = c$.

- **46.16 :** Soit $x(t)$ la position du moine le samedi à l'heure $t \in [6 \,;\, 18]$ (avec $x(6) = 0$ et $x(18) = D$, où $D$ est la distance totale).
  Soit $y(t)$ sa position le dimanche à l'heure $t$ (avec $y(6) = D$ et $y(18) = 0$).
  Posons $h(t) = x(t) - y(t)$. $h$ est continue sur $[6 \,;\, 18]$.
  $h(6) = 0 - D = -D < 0$ et $h(18) = D - 0 = D > 0$.
  D'après le TVI, il existe un instant $t_0 \in ]6 \,;\, 18[$ tel que $h(t_0) = 0 \iff x(t_0) = y(t_0)$. À cette heure-là, le moine est exactement au même endroit.

- **46.17 :**
  - Si $f$ est strictement monotone, elle est clairement injective (si $x < y$, alors $f(x) < f(y)$ ou $f(x) > f(y)$, donc $f(x) \neq f(y)$).
  - Réciproquement, si $f$ n'est pas strictement monotone, elle admet un changement de sens de variation (ou n'est pas monotone), ce qui crée deux points distincts $a < b$ avec $f(a) = f(b)$ par le TVI, contredisant l'injectivité.

---

#### Solutions du Niveau ★★★

- **46.18 :**
  1. Soit $x_0 \in \mathbb{R}$. Dans tout intervalle $]x_0 - \varepsilon \,;\, x_0 + \varepsilon[$, il existe une infinité de rationnels (où $f(x) = 1$) et une infinité d'irrationnels (où $f(x) = 0$).
     Toute suite de rationnels tendant vers $x_0$ a pour image une suite constante égale à 1.
     Toute suite d'irrationnels tendant vers $x_0$ a pour image une suite constante égale à 0.
  2. Puisque les deux limites ($1$ et $0$) sont distinctes, $f$ ne possède aucune limite en $x_0$. Elle est donc discontinue en tout point de $\mathbb{R}$.

- **46.19 :** Posons $D(\theta) = T(\theta + \pi) - T(\theta)$ pour $\theta \in [0 \,;\, \pi]$.
  $D$ est continue sur $[0 \,;\, \pi]$.
  $D(0) = T(\pi) - T(0)$.
  $D(\pi) = T(2\pi) - T(\pi) = T(0) - T(\pi) = -D(0)$ car $T(2\pi) = T(0)$.
  Si $D(0) = 0$, $\theta = 0$ convient.
  Sinon, $D(0)$ et $D(\pi)$ sont de signes opposés : par le TVI, il existe $\theta_0 \in ]0 \,;\, \pi[$ tel que $D(\theta_0) = 0 \iff T(\theta_0 + \pi) = T(\theta_0)$.

- **46.20 :**
  1. $f(0 + 0) = f(0) + f(0) \implies f(0) = 0$. Par récurrence, $f(n) = n f(1) = c \cdot n$.
  2. $f(0) = f(p + (-p)) = f(p) + f(-p) = 0 \implies f(-p) = -f(p) = -c \cdot p = c \cdot (-p)$. Vrai pour tout $p \in \mathbb{Z}$.
  3. Soit $r = p/q$. Alors $q \cdot f(p/q) = f(q \cdot p/q) = f(p) = c \cdot p \implies f(p/q) = c \cdot \frac{p}{q}$.
  4. Pour tout réel $x$, il existe une suite de rationnels $(r_n)$ convergeant vers $x$. Par continuité de $f$ : $f(x) = \lim f(r_n) = \lim (c \cdot r_n) = c \cdot x$.

- **46.21 :**
  1. La somme est télescopique :
     $$\sum_{k=0}^{n-1} g\left(\frac{k}{n}\right) = \sum_{k=0}^{n-1} \left[f\left(\frac{k+1}{n}\right) - f\left(\frac{k}{n}\right)\right] = f(1) - f(0) = 0.$$
  2. Une somme de $n$ termes qui vaut 0 impose que tous les termes sont nuls, ou bien qu'il y en a au moins un positif (ou nul) et au moins un négatif (ou nul).
     La fonction continue $g$ prend donc une valeur positive ou nulle et une valeur négative ou nulle. Par le TVI, $g$ s'annule en un point $x_0$, d'où $f(x_0 + 1/n) = f(x_0)$.

- **46.22 :**
  1. Script Python :
```python
def f(x):
    return x**2 - 2
def f_prime(x):
    return 2*x

x = 1.0
for i in range(5):
    x = x - f(x) / f_prime(x)
    print(f"Étape {i+1} : x = {x:.12f}")
# Étape 1 : 1.500000000000
# Étape 2 : 1.416666666667
# Étape 3 : 1.414215686275
# Étape 4 : 1.414213562375 (12 décimales exactes en 4 étapes !)
```
  2. La dichotomie gagne 1 chiffre binaire par étape (il faut environ 33 étapes pour 10 décimales). Newton double le nombre de décimales exactes à chaque étape (convergence quadratique) : 4 à 5 étapes suffisent !

---

### La question qui ouvre la suite

Nous venons de voir que la continuité assure qu'une courbe ne se déchire jamais. Mais une courbe continue peut être pleine de pointes agressives (comme $|x|$ en zéro) ou de virages cassés.
Pour pouvoir parler de **vitesse**, d'**accélération** et de **trajectoire fluide**, il nous faut l'outil suprême du calcul différentiel : la dérivation.
Que se passe-t-il lorsque l'on dérive une fonction de fonction, comme une boîte de vitesses mécanique où un premier pignon entraîne un second, qui entraîne un troisième ?
Comment la dérivée seconde nous indique-t-elle si une courbe tourne son creux vers le ciel comme un bol qui retient la pluie (**convexité**) ou si elle traverse sa propre tangente (**point d'inflexion**) ?

C'est l'art des engrenages et de la courbure : rendez-vous au chapitre 47.
