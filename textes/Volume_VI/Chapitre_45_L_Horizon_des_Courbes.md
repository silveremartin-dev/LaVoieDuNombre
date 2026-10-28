# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 45 : L'Horizon des Courbes

> *« Asymptote vient du grec ancien asúmptōtos : "qui ne coïncide pas", "qui ne rencontre pas". C'est la ligne d'horizon du marin : plus le navire avance vers le large, plus l'horizon semble s'offrir à lui, sans que jamais sa coque ne puisse en franchir le seuil. Dans le ciel cartésien, les asymptotes sont les rails invisibles qui guident le destin des courbes vers l'infini. »*

---

### Ce que tu vas découvrir

- Le passage fondamental de la variable discrète $n \in \mathbb{N}$ à la variable continue $x \in \mathbb{R}$ : comment les fonctions glissent vers l'infini ou vers un point de rupture.
- Les définitions rigoureuses des **limites finies et infinies**, ainsi que les notions indispensables de **limite à gauche et limite à droite**.
- Les **trois familles d'asymptotes** (verticales, horizontales, obliques) et la méthode pour déterminer la **position relative** d'une courbe par rapport à sa droite guide.
- La panoplie complète pour lever les **quatre formes indéterminées** : factorisation par le terme prépondérant, quantité conjuguée, et taux d'accroissement.
- Le triomphe des **croissances comparées** de la fonction exponentielle sur les puissances de $x$, avec sa **démonstration exigible au baccalauréat**.
- Le théorème sur la **limite d'une fonction composée** $g(f(x))$.

---

### 1. Le problème : la lentille optique et le trou noir

#### 1.1 Le physicien et la distance focale

Dans un laboratoire d'optique, un rayon lumineux traverse une lentille mince convergente de distance focale $f > 0$. Un objet lumineux est placé à une distance $p$ en avant de la lentille. La formule de conjugaison de Descartes-Gauss relie la position de l'objet $p$ à la position de l'image nette $p'$ formée sur un écran en arrière :

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f}.$$

Exprimons la position de l'image $p'$ en fonction de la distance de l'objet $p$ :

$$p'(p) = \frac{f \cdot p}{p - f}.$$

Que se passe-t-il lorsque l'expérimentateur déplace l'objet vers la lentille ?

```
               Objet                     Lentille                  Écran
                 |                          |                        |
                 |◄───────── p ────────────►|◄───────── p' ─────────►|
                 |                          |                        |
           [Source lumineuse]            (Foyer F)
```

1. **Si l'objet est infiniment éloigné ($p \to +\infty$)** :
   $$p'(p) = \frac{f \cdot p}{p(1 - f/p)} = \frac{f}{1 - f/p} \xrightarrow[p \to +\infty]{} f.$$
   L'image se forme exactement dans le plan focal de la lentille. La droite horizontale $y = f$ est une **ligne de butée**, un plafond que l'image ne peut franchir : c'est une **asymptote horizontale**.

2. **Si l'objet s'approche du foyer focal ($p \to f$ avec $p > f$)** :
   Le dénominateur $p - f$ devient un nombre positif infiniment petit ($0{,}001$, $0{,}000001$...).
   Le quotient $p'(p)$ explose vers des grandeurs gigantesques :
   $$\lim_{p \to f^+} p'(p) = +\infty.$$
   Pour voir l'image nette, il faudrait reculer l'écran au bout de la pièce, puis hors du bâtiment, puis sur la Lune ! Les rayons émergent parallèles : l'image est rejetée à l'infini. La droite verticale $x = f$ agit comme une falaise infranchissable : c'est une **asymptote verticale**.

#### 1.2 Du pas discret au flux continu

Au chapitre 44, la variable $n$ sautait d'entier en entier : $n = 0, 1, 2, 3 \dots$ Il n'y avait aucun sens à se demander ce qui se passait entre $n=2$ et $n=3$, et l'on ne pouvait faire tendre $n$ que vers $+\infty$.

Avec les fonctions d'une variable réelle $x \mapsto f(x)$, le monde devient **fluide et continu**.
La variable réelle $x$ peut :
- s'enfuir vers $+\infty$ ou vers $-\infty$ ;
- glisser vers un nombre réel fixé $x_0$ (par exemple $x \to 2$) ;
- s'approcher d'un point interdit par la gauche ($x < x_0$) ou par la droite ($x > x_0$).

---

### 2. Définitions rigoureuses des limites de fonctions

#### 2.1 Les notations expliquées

- $\lim\limits_{x \to +\infty} f(x) = L$ : « la limite de $f(x)$ lorsque $x$ tend vers plus l'infini est égale à $L$ ».
- $\lim\limits_{x \to x_0} f(x) = L$ : « la limite de $f(x)$ lorsque $x$ tend vers le réel $x_0$ est égale à $L$ ».
- $x \to x_0^+$ ou $x \xrightarrow[x > x_0]{} x_0$ : « $x$ tend vers $x_0$ par valeurs strictement supérieures » (limite à droite).
- $x \to x_0^-$ ou $x \xrightarrow[x < x_0]{} x_0$ : « $x$ tend vers $x_0$ par valeurs strictement inférieures » (limite à gauche).

#### 2.2 Limite finie en l'infini

> **📐 Définition — Limite finie en $+\infty$.**
> Soit $f$ une fonction définie sur un intervalle $[a \,;\, +\infty[$, et soit $L \in \mathbb{R}$.
> On dit que **$f$ admet pour limite $L$ en $+\infty$** si :
> **Tout intervalle ouvert contenant $L$ contient toutes les valeurs $f(x)$ pour $x$ suffisamment grand.**
> On note :
> $$\lim_{x \to +\infty} f(x) = L.$$
> (Définition analogue en $-\infty$ sur un intervalle $]-\infty \,;\, b]$).

*Sens concret :* Trace une bande horizontale de largeur $2\varepsilon$ centrée sur $y = L$, aussi étroite que tu veux. Si tu avances assez loin vers la droite sur l'axe des abscisses (au-delà d'un certain seuil $X$), le graphe de la fonction s'enferme à tout jamais à l'intérieur de cette bande.

#### 2.3 Limite infinie en un point : le mur vertical

> **📐 Définition — Limite infinie en un point réel $x_0$.**
> Soit $x_0 \in \mathbb{R}$. On dit que **$f(x)$ tend vers $+\infty$ lorsque $x$ tend vers $x_0$** si :
> **Pour tout réel $A > 0$, l'intervalle $]A \,;\, +\infty[$ contient toutes les valeurs $f(x)$ pour $x$ suffisamment proche de $x_0$.**
> On note :
> $$\lim_{x \to x_0} f(x) = +\infty.$$

#### 2.4 Limites à gauche et à droite

Certaines fonctions adoptent des comportements radicalement opposés selon qu'on les approche par bâbord ou par tribord. L'archétype est la fonction inverse $f(x) = \frac{1}{x}$ au voisinage de zéro :
- Si $x > 0$ et $x \to 0$ : $x$ prend des valeurs comme $0{,}1$ ; $0{,}001$ ; $0{,}00001$. Le quotient $\frac{1}{x}$ vaut $10$ ; $1000$ ; $100\,000$ :
  $$\lim_{x \to 0^+} \frac{1}{x} = +\infty.$$
- Si $x < 0$ et $x \to 0$ : $x$ prend des valeurs négatives comme $-0{,}1$ ; $-0{,}001$. Le quotient $\frac{1}{x}$ vaut $-10$ ; $-1000$ :
  $$\lim_{x \to 0^-} \frac{1}{x} = -\infty.$$

```
             y ▲
               │         /  x > 0 : monte vers +∞
               │        /
               │       /
───────────────┼───────────────► x
             / │
            /  │
 x < 0 :   /   │
 plonge vers -∞│
```

> **📐 Théorème fondamental — Existence de la limite globale en un point.**
> Une fonction $f$ admet une limite $L$ en $x_0$ si et seulement si elle admet une limite à gauche et une limite à droite en $x_0$, et que ces deux limites sont **égales** :
> $$\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = L.$$
> Pour $f(x) = \frac{1}{x}$ en 0, comme $+\infty \neq -\infty$, la fonction n'a **pas de limite globale** en 0.

---

### 3. Les Asymptotes : le guide géométrique des courbes

Une asymptote est une droite dont la courbe représentative $\mathcal{C}_f$ se rapproche de plus en plus lorsque les points de la courbe s'éloignent vers l'infini.

```
       Asymptote verticale : x = a           Asymptote horizontale : y = L
             │       /                             │
             │      /                              │             /~~~~~~\
             │     /                     ──────────┼────────────(─ y = L ─)────
             │    /                                │             \______/
         ────┼───*────────►                        │
             │ a                                   └──────────────────────►
```

#### 3.1 Asymptote horizontale

> **📐 Définition — Asymptote horizontale.**
> Si $\lim\limits_{x \to +\infty} f(x) = L$ (ou si $\lim\limits_{x \to -\infty} f(x) = L$), où $L$ est un nombre réel fini,
> alors la droite $\mathcal{D}$ d'équation **$y = L$** est appelée **asymptote horizontale** à la courbe $\mathcal{C}_f$ au voisinage de $+\infty$ (ou de $-\infty$).

#### 3.2 Asymptote verticale

> **📐 Définition — Asymptote verticale.**
> Si $\lim\limits_{x \to a^+} f(x) = \pm\infty$ ou si $\lim\limits_{x \to a^-} f(x) = \pm\infty$ (où $a \in \mathbb{R}$),
> alors la droite $\Delta$ d'équation **$x = a$** est appelée **asymptote verticale** à la courbe $\mathcal{C}_f$.

#### 3.3 Asymptote oblique

Parfois, la courbe ne s'aplatit pas à l'horizontale, mais s'aligne le long d'une droite penchée d'équation $y = ax + b$ avec $a \neq 0$.

> **📐 Définition — Asymptote oblique.**
> La droite $\mathcal{D}$ d'équation **$y = ax + b$** est une asymptote oblique à la courbe $\mathcal{C}_f$ en $+\infty$ (resp. $-\infty$) si :
> $$\lim_{x \to +\infty} \big[f(x) - (ax + b)\big] = 0 \quad \text{(resp. en } -\infty\text{)}.$$

*Sens géométrique :* La distance verticale entre le point de la courbe $M(x ; f(x))$ et le point de la droite $P(x ; ax + b)$ devient infiniment petite à mesure qu'on avance vers le bout du repère.

#### 3.4 Étude de la position relative

Pour savoir si la courbe $\mathcal{C}_f$ se situe **au-dessus** ou **en dessous** de son asymptote (horizontale $y = L$ ou oblique $y = ax+b$), on applique la méthode universelle suivante :

> **🧭 Méthode — Position relative d'une courbe et d'une asymptote :**
> 1. On calcule la différence : $d(x) = f(x) - y_{\text{asymptote}}$.
> 2. On étudie rigoureusement le **signe** de $d(x)$ :
>    - Si $d(x) > 0$ sur un intervalle, alors $\mathcal{C}_f$ est **strictement au-dessus** de l'asymptote sur cet intervalle.
>    - Si $d(x) < 0$ sur un intervalle, alors $\mathcal{C}_f$ est **strictement en dessous** de l'asymptote.
>    - Si $d(x) = 0$ en un point $x_1$, la courbe **traverse** son asymptote au point d'abscisse $x_1$.

---

### 4. La Boîte à Outils pour lever les Formes Indéterminées

Rappelons les quatre formes interdites de conclusion directe :
$$\text{F.I. : } \quad [\infty - \infty], \quad [0 \times \infty], \quad \left[\frac{\infty}{\infty}\right], \quad \left[\frac{0}{0}\right].$$

Voici les quatre techniques fondamentales à maîtriser au lycée :

#### Méthode 1 : Factoriser par le terme prépondérant

En $+\infty$ ou $-\infty$, dans un polynôme ou une fraction rationnelle, le terme de plus haut degré dicte sa loi à tous les autres.
- Pour un polynôme : on factorise par la plus grande puissance de $x$.
- Pour une fraction : on factorise le numérateur et le dénominateur par leur puissance dominante respective, puis on simplifie.

> **⚠️ Attention, piège ! — Le signe sous la racine carrée en $-\infty$.**
> Rappelle-toi toujours que pour tout réel $x$ :
> $$\sqrt{x^2} = |x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}$$
> Lorsque $x \to -\infty$, $x$ est un nombre **strictement négatif**. Par conséquent :
> $$\sqrt{x^2} = -x \quad (\text{et non } +x \text{ !}).$$
> C'est l'erreur la plus sanctionnée dans les copies de baccalauréat !

#### Méthode 2 : La quantité conjuguée

Lorsque des racines carrées s'affrontent dans une indétermination du type $[\infty - \infty]$ ou $[0/0]$, on utilise l'identité remarquable $(a - b)(a + b) = a^2 - b^2$ pour chasser les radicaux du lieu du blocage :

$$\sqrt{A} - \sqrt{B} = \frac{(\sqrt{A} - \sqrt{B})(\sqrt{A} + \sqrt{B})}{\sqrt{A} + \sqrt{B}} = \frac{A - B}{\sqrt{A} + \sqrt{B}}.$$

La soustraction délicate $[\infty - \infty]$ se transforme en une addition bienveillante au dénominateur $[\infty + \infty = \infty]$.

#### Méthode 3 : Reconnaître un taux de variation (nombre dérivé)

Une forme indéterminée du type $\left[\frac{0}{0}\right]$ en un point $x_0$ cache très souvent la définition même de la dérivée :
$$\lim_{x \to x_0} \frac{g(x) - g(x_0)}{x - x_0} = g'(x_0).$$

Exemples célèbres :
- $\lim\limits_{x \to 0} \dfrac{e^x - 1}{x}$ : avec $g(x) = e^x$, $g(0) = 1$, la limite vaut $g'(0) = e^0 = 1$.
- $\lim\limits_{x \to 0} \dfrac{\sin x}{x}$ : avec $g(x) = \sin x$, $g(0) = 0$, la limite vaut $\cos(0) = 1$.

---

### 5. Les Croissances Comparées de l'Exponentielle

Quand la fonction exponentielle affronte un polynôme ou une puissance de $x$ en l'infini, l'explosion de $e^x$ surpasse infiniment toute croissance polynomiale.

> **📐 Théorème — Croissances comparées de l'exponentielle.**
> Pour tout entier naturel $n \geq 1$ :
> 1. $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$ $\quad$ et plus généralement $\quad$ $\lim\limits_{x \to +\infty} \dfrac{e^x}{x^n} = +\infty$
> 2. $\lim\limits_{x \to -\infty} x \, e^x = 0$ $\quad$ et plus généralement $\quad$ $\lim\limits_{x \to -\infty} x^n \, e^x = 0$

*Règle mnémotechnique :* En $+\infty$ comme en $-\infty$, **l'exponentielle l'emporte toujours sur les puissances de $x$**.

#### Démonstration exigible au baccalauréat : $\lim_{x \to +\infty} \frac{e^x}{x} = +\infty$

> **✍️ Démonstration (exigible).**
> L'objectif est d'obtenir une minoration de $e^x$ par un polynôme de degré 2 pour que le quotient $\frac{e^x}{x}$ soit minoré par un terme de degré 1 qui tend vers $+\infty$.
>
> **Étape 1 : Minoration de la fonction exponentielle.**
> Considérons la fonction $f$ définie sur $[0 \,;\, +\infty[$ par :
> $$f(x) = e^x - \frac{x^2}{2}.$$
> Dérivons deux fois la fonction $f$ :
> - Sa dérivée première est $f'(x) = e^x - x$.
> - Sa dérivée seconde est $f''(x) = e^x - 1$.
>
> Pour tout $x \geq 0$, $e^x \geq e^0 = 1$, donc $f''(x) \geq 0$.
> Par conséquent, la fonction dérivée $f'$ est strictement croissante sur $[0 \,;\, +\infty[$.
> Or $f'(0) = e^0 - 0 = 1 > 0$.
> Puisque $f'$ est croissante et que $f'(0) > 0$, pour tout $x \geq 0$ on a :
> $$f'(x) \geq f'(0) > 0.$$
> La fonction $f$ est donc elle-même strictement croissante sur $[0 \,;\, +\infty[$.
> Comme $f(0) = e^0 - 0 = 1 > 0$, il en résulte que pour tout $x \geq 0$ :
> $$f(x) > 0 \implies e^x > \frac{x^2}{2}.$$
>
> **Étape 2 : Passage au quotient et conclusion.**
> Pour tout réel $x > 0$, divisons cette inégalité par $x$ (comme $x > 0$, le sens de l'inégalité est conservé) :
> $$\frac{e^x}{x} > \frac{x}{2}.$$
> Or :
> $$\lim_{x \to +\infty} \frac{x}{2} = +\infty.$$
> D'après le **théorème de comparaison** des limites, on conclut de façon irréfutable :
> $$\lim_{x \to +\infty} \frac{e^x}{x} = +\infty. \quad \blacksquare$$

*Démonstration de $\lim\limits_{x \to -\infty} x e^x = 0$ par changement de variable :*
Posons $X = -x$. Lorsque $x \to -\infty$, on a $X \to +\infty$.
Alors :
$$x \, e^x = (-X) \, e^{-X} = - \frac{X}{e^X} = - \frac{1}{\dfrac{e^X}{X}}.$$
Comme $\lim\limits_{X \to +\infty} \dfrac{e^X}{X} = +\infty$, par inverse d'une limite infinie :
$$\lim_{x \to -\infty} x \, e^x = \lim_{X \to +\infty} \left(-\frac{1}{e^X/X}\right) = 0. \quad \blacksquare$$

---

### 6. Limite d'une Fonction Composée

Une fonction composée est une cascade : la sortie de la première machine $f$ devient l'entrée de la seconde machine $g$. On note cette opération $(g \circ f)(x) = g(f(x))$.

> **📐 Théorème — Limite d'une fonction composée.**
> Soient $a, b, c$ désignant soit des nombres réels, soit $+\infty$, soit $-\infty$.
> Si :
> $$\lim_{x \to a} f(x) = b \quad \text{et} \quad \lim_{y \to b} g(y) = c,$$
> alors :
> $$\lim_{x \to a} g(f(x)) = c.$$

> **🧭 Méthode — Rédiger une limite de composée au Bac :**
> Ne calcule jamais tout d'un coup. Sépare clairement en deux étapes en posant un changement de variable muet :
> 1. *Étape intérieure :* on calcule $\lim\limits_{x \to a} f(x) = b$.
> 2. *Étape extérieure :* on pose $X = f(x)$, et comme $X \to b$, on calcule $\lim\limits_{X \to b} g(X) = c$.
> 3. *Conclusion :* Par composition de limites, $\lim\limits_{x \to a} g(f(x)) = c$.

---

### 7. Attention, pièges !

> **⚠️ Attention, piège ! — Traverser une asymptote.**
> Une idée fausse très répandue chez les élèves est qu'une courbe n'a « jamais le droit de toucher son asymptote ».
> C'est **vrai pour une asymptote verticale** $x = a$ (car la fonction n'y est généralement pas définie).
> Mais c'est **complètement faux pour une asymptote horizontale ou oblique** !
> Une asymptote horizontale $y = L$ décrit uniquement ce qui se passe **au bout du monde** (pour $x \to \pm\infty$). Entre-temps, pour des valeurs modérées de $x$, la courbe peut couper la droite horizontale une fois, dix fois, ou même une infinité de fois !
> *Exemple :* $f(x) = \frac{\sin x}{x}$ a pour asymptote horizontale l'axe des abscisses $y = 0$, et traverse cet axe en tous les multiples de $\pi$ ($\pi, 2\pi, 3\pi \dots$).

> **⚠️ Attention, piège ! — Les croissances comparées ne s'appliquent qu'en l'infini !**
> Ne dis jamais : « $\lim\limits_{x \to 0} \frac{e^x}{x} = +\infty$ par croissances comparées » !
> En 0, le numérateur tend vers $e^0 = 1$ et le dénominateur vers 0. C'est une limite directe de quotient fini par zéro ($1/0^+$ ou $1/0^-$), pas une croissance comparée ! Les croissances comparées comparent la vitesse d'échappement vers l'infini.

---

### 8. Exemples Résolus pas à pas

#### Exemple résolu 1 — Asymptotes et levée d'indétermination en $+\infty$ et $-\infty$

**Énoncé :** Soit la fonction $f$ définie sur $\mathbb{R} \setminus \{2\}$ par :
$$f(x) = \frac{3x - 1}{x - 2}.$$
1. Déterminer les limites de $f$ aux bornes de son domaine de définition ($+\infty$, $-\infty$, et en 2 par valeurs inférieures et supérieures).
2. En déduire les équations des asymptotes à la courbe représentative $\mathcal{C}_f$.
3. Étudier la position relative de $\mathcal{C}_f$ par rapport à son asymptote horizontale.

**Solution :**
1. **Limites en l'infini :**
   Pour $x \neq 0$ :
   $$f(x) = \frac{x\left(3 - \dfrac{1}{x}\right)}{x\left(1 - \dfrac{2}{x}\right)} = \frac{3 - \dfrac{1}{x}}{1 - \dfrac{2}{x}}.$$
   Comme $\lim\limits_{x \to \pm\infty} \frac{1}{x} = 0$ et $\lim\limits_{x \to \pm\infty} \frac{2}{x} = 0$, on obtient :
   $$\lim_{x \to +\infty} f(x) = 3 \quad \text{et} \quad \lim_{x \to -\infty} f(x) = 3.$$

   **Limites en 2 :**
   Numérateur : $\lim_{x \to 2} (3x - 1) = 3(2) - 1 = 5 > 0$.
   Dénominateur : $\lim_{x \to 2} (x - 2) = 0$.
   - Si $x > 2$, $x - 2 > 0$, donc le dénominateur tend vers $0^+$. Par quotient :
     $$\lim_{x \to 2^+} f(x) = +\infty.$$
   - Si $x < 2$, $x - 2 < 0$, le dénominateur tend vers $0^-$. Par quotient :
     $$\lim_{x \to 2^-} f(x) = -\infty.$$

2. **Asymptotes :**
   - Comme $\lim\limits_{x \to \pm\infty} f(x) = 3$, la droite d'équation **$y = 3$** est asymptote horizontale à $\mathcal{C}_f$ en $+\infty$ et en $-\infty$.
   - Comme $\lim\limits_{x \to 2} f(x) = \pm\infty$, la droite d'équation **$x = 2$** est asymptote verticale à $\mathcal{C}_f$.

3. **Position relative par rapport à l'asymptote horizontale $y = 3$ :**
   Calculons la différence $d(x) = f(x) - 3$ :
   $$d(x) = \frac{3x - 1}{x - 2} - 3 = \frac{(3x - 1) - 3(x - 2)}{x - 2} = \frac{3x - 1 - 3x + 6}{x - 2} = \frac{5}{x - 2}.$$
   - Pour tout $x \in ]2 \,;\, +\infty[$, $x - 2 > 0$, donc $d(x) > 0$ : la courbe $\mathcal{C}_f$ est **strictement au-dessus** de l'asymptote $y = 3$.
   - Pour tout $x \in ]-\infty \,;\, 2[$, $x - 2 < 0$, donc $d(x) < 0$ : la courbe $\mathcal{C}_f$ est **strictement en dessous** de l'asymptote $y = 3$.

---

#### Exemple résolu 2 — Le piège du signe de $\sqrt{x^2}$ en $-\infty$

**Énoncé :** Déterminer la limite en $-\infty$ et en $+\infty$ de la fonction :
$$f(x) = \sqrt{x^2 + 4x + 5} + x.$$

**Solution :**
**En $+\infty$ :**
$\lim\limits_{x \to +\infty} (x^2 + 4x + 5) = +\infty$, donc $\lim \sqrt{x^2+4x+5} = +\infty$.
Comme $\lim\limits_{x \to +\infty} x = +\infty$, par somme :
$$\lim_{x \to +\infty} f(x) = +\infty \quad (\text{pas de forme indéterminée ici !}).$$

**En $-\infty$ :**
$\lim\limits_{x \to -\infty} \sqrt{x^2+4x+5} = +\infty$ et $\lim\limits_{x \to -\infty} x = -\infty$.
Il s'agit d'une forme indéterminée $[\infty - \infty]$.
Utilisons la **quantité conjuguée** :
$$f(x) = \frac{\left(\sqrt{x^2 + 4x + 5} + x\right)\left(\sqrt{x^2 + 4x + 5} - x\right)}{\sqrt{x^2 + 4x + 5} - x} = \frac{(x^2 + 4x + 5) - x^2}{\sqrt{x^2 + 4x + 5} - x} = \frac{4x + 5}{\sqrt{x^2 + 4x + 5} - x}.$$
Factorisons maintenant par le terme prépondérant au dénominateur pour $x < 0$ :
$$\sqrt{x^2 + 4x + 5} = \sqrt{x^2\left(1 + \frac{4}{x} + \frac{5}{x^2}\right)} = |x|\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}}.$$
Comme $x \to -\infty$, on a $x < 0$, donc $|x| = -x$ !
$$\sqrt{x^2 + 4x + 5} - x = -x\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}} - x = -x \left[\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}} + 1\right].$$
Le numérateur s'écrit $4x + 5 = x\left(4 + \frac{5}{x}\right)$.
Ainsi, pour $x < 0$ :
$$f(x) = \frac{x\left(4 + \dfrac{5}{x}\right)}{-x \left[\sqrt{1 + \dfrac{4}{x} + \dfrac{5}{x^2}} + 1\right]} = \frac{4 + \dfrac{5}{x}}{-\left(\sqrt{1 + \dfrac{4}{x} + \dfrac{5}{x^2}} + 1\right)}.$$
Passons à la limite quand $x \to -\infty$ :
- Le numérateur tend vers $4 + 0 = 4$.
- Le dénominateur tend vers $-( \sqrt{1 + 0 + 0} + 1 ) = -(1 + 1) = -2$.
Par quotient :
$$\lim_{x \to -\infty} f(x) = \frac{4}{-2} = -2.$$
*Conséquence géométrique :* La droite d'équation $y = -2$ est asymptote horizontale à la courbe en $-\infty$.

---

#### Exemple résolu 3 — Croissances comparées et factorisation d'exponentielle

**Énoncé :** Déterminer la limite en $+\infty$ et en $-\infty$ de la fonction $f(x) = (2x - 3)e^{-x} + 1$.

**Solution :**
**En $+\infty$ :**
Écrivons $f(x) = 2x e^{-x} - 3e^{-x} + 1 = \frac{2x}{e^x} - \frac{3}{e^x} + 1 = 2 \left(\frac{1}{\frac{e^x}{x}}\right) - \frac{3}{e^x} + 1$.
D'après les théorèmes de croissances comparées, $\lim\limits_{x \to +\infty} \frac{e^x}{x} = +\infty$, donc $\lim\limits_{x \to +\infty} \frac{x}{e^x} = 0$.
De plus, $\lim\limits_{x \to +\infty} e^x = +\infty$, d'où $\lim\limits_{x \to +\infty} \frac{3}{e^x} = 0$.
Par somme de limites :
$$\lim_{x \to +\infty} f(x) = 2(0) - 0 + 1 = 1.$$
La droite d'équation $y = 1$ est asymptote horizontale en $+\infty$.

**En $-\infty$ :**
Posons le changement de variable $X = -x$. Quand $x \to -\infty$, $X \to +\infty$.
Alors :
$f(x) = (-2X - 3)e^X + 1 = -2X e^X - 3e^X + 1.$
Quand $X \to +\infty$, $e^X \to +\infty$ et $-2X - 3 \to -\infty$.
Par produit :
$$\lim_{x \to -\infty} (2x - 3) = -\infty \quad \text{et} \quad \lim_{x \to -\infty} e^{-x} = +\infty \implies \lim_{x \to -\infty} (2x - 3)e^{-x} = -\infty.$$
D'où :
$$\lim_{x \to -\infty} f(x) = -\infty.$$

---

#### Exemple résolu 4 — Limite d'une composée avec racine et quotient

**Énoncé :** Déterminer la limite quand $x \to +\infty$ de :
$$h(x) = \sqrt{\frac{4x^2 + 1}{x^2 - 3x + 2}}.$$

**Solution :**
Décomposons la fonction en posant $f(x) = \frac{4x^2 + 1}{x^2 - 3x + 2}$ et $g(X) = \sqrt{X}$, de sorte que $h(x) = g(f(x))$.
1. *Limite intérieure :*
   Pour $x > 0$ :
   $$f(x) = \frac{x^2\left(4 + \dfrac{1}{x^2}\right)}{x^2\left(1 - \dfrac{3}{x} + \dfrac{2}{x^2}\right)} = \frac{4 + \dfrac{1}{x^2}}{1 - \dfrac{3}{x} + \dfrac{2}{x^2}}.$$
   Comme $\lim\limits_{x \to +\infty} \frac{1}{x^2} = 0$, $\lim\limits_{x \to +\infty} \frac{3}{x} = 0$ et $\lim\limits_{x \to +\infty} \frac{2}{x^2} = 0$, on a :
   $$\lim_{x \to +\infty} f(x) = \frac{4}{1} = 4.$$
2. *Limite extérieure :*
   Posons $X = f(x)$. Comme $X \to 4$ :
   $$\lim_{X \to 4} g(X) = \lim_{X \to 4} \sqrt{X} = \sqrt{4} = 2.$$
3. *Conclusion :*
   Par composition de limites :
   $$\lim_{x \to +\infty} h(x) = 2.$$
La droite d'équation $y = 2$ est asymptote horizontale à la courbe de $h$ en $+\infty$.

---

#### Exemple résolu 5 — Détermination complète d'une asymptote oblique

**Énoncé :** Soit la fonction $f$ définie sur $\mathbb{R} \setminus \{1\}$ par $f(x) = \frac{2x^2 - x + 3}{x - 1}$.
1. Déterminer les réels $a, b, c$ tels que pour tout $x \neq 1$ : $f(x) = ax + b + \frac{c}{x - 1}$.
2. Démontrer que la droite $\mathcal{D}$ d'équation $y = 2x + 1$ est asymptote oblique à la courbe $\mathcal{C}_f$ en $+\infty$ et $-\infty$.
3. Préciser la position relative de $\mathcal{C}_f$ par rapport à $\mathcal{D}$.

**Solution :**
1. Développons la forme souhaitée :
   $$ax + b + \frac{c}{x - 1} = \frac{(ax + b)(x - 1) + c}{x - 1} = \frac{ax^2 - ax + bx - b + c}{x - 1} = \frac{ax^2 + (b - a)x + (c - b)}{x - 1}.$$
   On identifie les coefficients avec $2x^2 - x + 3$ :
   $$\begin{cases} a = 2 \\ b - a = -1 \implies b = a - 1 = 2 - 1 = 1 \\ c - b = 3 \implies c = 3 + b = 3 + 1 = 4 \end{cases}$$
   On a donc pour tout $x \neq 1$ :
   $$f(x) = 2x + 1 + \frac{4}{x - 1}.$$

2. Calculons la différence entre $f(x)$ et $y = 2x + 1$ :
   $$f(x) - (2x + 1) = \frac{4}{x - 1}.$$
   Or $\lim\limits_{x \to +\infty} \frac{4}{x - 1} = 0$ et $\lim\limits_{x \to -\infty} \frac{4}{x - 1} = 0$.
   Par définition, la droite $\mathcal{D}$ d'équation $y = 2x + 1$ est donc **asymptote oblique** à la courbe $\mathcal{C}_f$ en $+\infty$ et en $-\infty$.

3. **Position relative :**
   Le signe de $f(x) - (2x + 1)$ est celui de $\frac{4}{x - 1}$ :
   - Si $x > 1$, $x - 1 > 0 \implies \frac{4}{x - 1} > 0$ : $\mathcal{C}_f$ est **strictement au-dessus** de $\mathcal{D}$.
   - Si $x < 1$, $x - 1 < 0 \implies \frac{4}{x - 1} < 0$ : $\mathcal{C}_f$ est **strictement en dessous** de $\mathcal{D}$.

---

#### Exemple résolu 6 — Forme $\frac{0}{0}$ résolue par le nombre dérivé

**Énoncé :** Déterminer sans calculatrice $\lim\limits_{x \to 0} \frac{e^{3x} - 1}{x}$.

**Solution :**
En $x = 0$, $e^0 - 1 = 0$ et le dénominateur vaut 0. C'est une forme indéterminée $[0/0]$.
Posons la fonction $g(x) = e^{3x}$.
La fonction $g$ est dérivable sur $\mathbb{R}$, et sa dérivée est $g'(x) = 3e^{3x}$.
Remarquons que $g(0) = e^0 = 1$.
L'expression s'écrit alors :
$$\frac{e^{3x} - 1}{x} = \frac{g(x) - g(0)}{x - 0}.$$
Par définition du nombre dérivé :
$$\lim_{x \to 0} \frac{g(x) - g(0)}{x - 0} = g'(0) = 3e^{3 \times 0} = 3 \times 1 = 3.$$
La limite cherchée est donc égale à $3$.

---

### Ce qu'il faut retenir

1. **Définition de limite en l'infini :** $\lim\limits_{x \to +\infty} f(x) = L$ si tout intervalle ouvert contenant $L$ contient toutes les valeurs $f(x)$ pour $x$ assez grand.
2. **Asymptotes :**
   - $\lim\limits_{x \to \pm\infty} f(x) = L \iff y = L$ est asymptote horizontale.
   - $\lim\limits_{x \to a^{\pm}} f(x) = \pm\infty \iff x = a$ est asymptote verticale.
   - $\lim\limits_{x \to \pm\infty} [f(x) - (ax+b)] = 0 \iff y = ax+b$ est asymptote oblique.
3. **Position relative :** signe de $f(x) - y_{\text{asymptote}}$.
4. **Formes Indéterminées :** $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.
5. **Croissances comparées :** $\lim\limits_{x \to +\infty} \frac{e^x}{x^n} = +\infty$ et $\lim\limits_{x \to -\infty} x^n e^x = 0$. En cas d'affrontement, l'exponentielle l'emporte toujours sur les polynômes.
6. **Composée :** $\lim\limits_{x \to a} f(x) = b$ et $\lim\limits_{X \to b} g(X) = c \implies \lim\limits_{x \to a} g(f(x)) = c$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 45.1.** Déterminer par lecture immédiate ou opérations élémentaires les limites suivantes :
1. $\lim\limits_{x \to +\infty} (3x^3 - 5x + 1)$
2. $\lim\limits_{x \to -\infty} (-2x^4 + x^2)$
3. $\lim\limits_{x \to +\infty} \left(4 - \frac{2}{x} + \frac{5}{x^3}\right)$
4. $\lim\limits_{x \to 0^+} \left(\frac{3}{x} - 2\right)$

**Exercice 45.2.** Déterminer les asymptotes éventuelles (verticales et horizontales) aux courbes des fonctions suivantes :
1. $f(x) = \dfrac{2x + 7}{x - 3}$ sur $\mathbb{R} \setminus \{3\}$
2. $g(x) = \dfrac{1}{x^2 - 4}$ sur $\mathbb{R} \setminus \{-2 ; 2\}$
3. $h(x) = 5 + e^{-x}$ sur $[0 \,;\, +\infty[$

**Exercice 45.3.** Calculer la limite à gauche et la limite à droite de $f(x) = \dfrac{x + 1}{x - 4}$ en $x_0 = 4$. La fonction admet-elle une limite globale en 4 ?

**Exercice 45.4.** Lever l'indétermination pour les fonctions rationnelles suivantes :
1. $\lim\limits_{x \to +\infty} \dfrac{4x^2 - 3x + 1}{2x^2 + 5x}$
2. $\lim\limits_{x \to -\infty} \dfrac{x^3 + 2}{5x^4 - x}$
3. $\lim\limits_{x \to +\infty} \dfrac{x^5 - 1}{x^2 + 100}$

**Exercice 45.5.** Utiliser les croissances comparées de l'exponentielle pour déterminer :
1. $\lim\limits_{x \to +\infty} (e^x - 3x^4)$
2. $\lim\limits_{x \to +\infty} \dfrac{e^x + 2}{x^3 + 1}$
3. $\lim\limits_{x \to -\infty} (x^2 + 1)e^x$

**Exercice 45.6.** Soit $f(x) = \sqrt{2x + 3}$. Déterminer $\lim\limits_{x \to 3} \dfrac{f(x) - f(3)}{x - 3}$ en reconnaissant un taux d'accroissement.

**Exercice 45.7.** Soit $f(x) = 2x - 1 + \dfrac{3}{x^2+1}$. Démontrer que la droite $y = 2x - 1$ est asymptote oblique à $\mathcal{C}_f$ en $+\infty$ et déterminer la position relative de $\mathcal{C}_f$ par rapport à cette droite.

**Exercice 45.8.** Déterminer par composition : $\lim\limits_{x \to +\infty} \exp\left(-\frac{1}{x^2}\right)$ et $\lim\limits_{x \to 0^+} \exp\left(-\frac{1}{x}\right)$.

---

#### Niveau ★★ (Réflexion et type Bac)

**Exercice 45.9 (Type Bac : Étude de fonction avec exponentielle).**
On considère la fonction $f$ définie sur $\mathbb{R}$ par :
$$f(x) = (x - 2)e^x + x.$$
1. Déterminer la limite de $f$ en $-\infty$.
2. Démontrer que la droite $(\Delta)$ d'équation $y = x$ est asymptote oblique à la courbe $\mathcal{C}_f$ en $-\infty$.
3. Préciser la position relative de $\mathcal{C}_f$ par rapport à $(\Delta)$ sur $]-\infty \,;\, +\infty[$.
4. Déterminer la limite de $f$ en $+\infty$.

**Exercice 45.10 (Quantité conjuguée et asymptotes).**
Soit $f(x) = \sqrt{x^2 - 2x + 3}$.
1. Déterminer la limite de $f$ en $+\infty$.
2. Démontrer que pour tout $x > 0$ :
   $$f(x) - (x - 1) = \frac{2}{\sqrt{x^2 - 2x + 3} + (x - 1)}.$$
3. En déduire que la droite d'équation $y = x - 1$ est asymptote oblique à la courbe en $+\infty$.

**Exercice 45.11 (Le piège de la racine en $-\infty$).**
Reprendre la fonction de l'exercice 45.10 en $-\infty$. Démontrer que la droite d'équation $y = -x + 1$ est asymptote oblique à la courbe en $-\infty$.

**Exercice 45.12 (Modélisation de population : la courbe logistique).**
Le nombre d'individus d'une population animale (en milliers) au cours du temps $t \geq 0$ (en années) est modélisé par :
$$N(t) = \frac{10}{1 + 9e^{-0{,}5t}}.$$
1. Calculer la population initiale $N(0)$.
2. Déterminer $\lim\limits_{t \to +\infty} N(t)$. Interpréter ce résultat dans le contexte du biotope (notion de capacité de charge).
3. Déterminer l'équation de l'asymptote horizontale au graphe de $N$.

**Exercice 45.13 (Forme indéterminée résolue par factorisation habile).**
Déterminer les limites suivantes :
1. $\lim\limits_{x \to 1} \dfrac{x^3 - 1}{x^2 - 1}$
2. $\lim\limits_{x \to 4} \dfrac{\sqrt{x} - 2}{x - 4}$
3. $\lim\limits_{x \to 0} \dfrac{\sqrt{1 + x} - 1}{x}$

**Exercice 45.14 (Fonction rationnelle et décomposition en éléments simples).**
Soit $f(x) = \dfrac{3x^2 + 5x - 2}{x + 1}$.
1. Trouver trois réels $a, b, c$ tels que $f(x) = ax + b + \dfrac{c}{x + 1}$ pour tout $x \neq -1$.
2. En déduire toutes les asymptotes à la courbe de $f$.
3. Déterminer les coordonnées du point d'intersection des deux asymptotes.

**Exercice 45.15 (Composée et fonctions trigonométriques).**
1. Déterminer $\lim\limits_{x \to +\infty} \cos\left(\frac{\pi x + 1}{2x - 3}\right)$.
2. Démontrer que la fonction $g(x) = x \sin\left(\frac{1}{x}\right)$ admet pour limite 1 en $+\infty$. (Poser $X = 1/x$).

**Exercice 45.16 (Gendarmes pour les fonctions).**
Soit $f(x) = \dfrac{2x + \sin(x)}{x - 1}$ définie sur $]1 \,;\, +\infty[$.
1. Montrer que pour tout $x > 1$ : $\dfrac{2x - 1}{x - 1} \leq f(x) \leq \dfrac{2x + 1}{x - 1}$.
2. En déduire $\lim\limits_{x \to +\infty} f(x)$.

**Exercice 45.17 (Étude complète d'une limite avec paramètre).**
Soit $f_m(x) = \dfrac{m x^2 + 4x - 1}{2x^2 + 3}$ où $m$ est un paramètre réel.
Déterminer la limite de $f_m(x)$ quand $x \to +\infty$ selon les valeurs du réel $m$.

---

#### Niveau ★★★ (Défi et approfondissement)

**Exercice 45.18 (La règle de L'Hôpital — Hors-programme / Supérieur).**
Soient $f$ et $g$ deux fonctions dérivables sur un intervalle ouvert contenant $a$, telles que $f(a) = g(a) = 0$ et $g'(a) \neq 0$.
1. En écrivant $\dfrac{f(x)}{g(x)} = \dfrac{\frac{f(x) - f(a)}{x - a}}{\frac{g(x) - g(a)}{x - a}}$, démontrer que :
   $$\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)}.$$
2. Utiliser ce résultat pour calculer : $\lim\limits_{x \to 0} \dfrac{e^{2x} - \cos(x)}{x}$.

**Exercice 45.19 (Asymptote parabolique).**
Soit la fonction $f(x) = \dfrac{x^3 + 2x^2 - 1}{x - 1}$ pour $x \neq 1$.
1. Montrer qu'il existe un polynôme du second degré $P(x)$ et un réel $R$ tels que $f(x) = P(x) + \dfrac{R}{x - 1}$.
2. En déduire que lorsque $x \to \pm\infty$, la courbe de $f$ se rapproche d'une parabole d'équation $y = P(x)$ (notion de parabole asymptote).

**Exercice 45.20 (Une fonction sans aucune limite en zéro).**
On considère la fonction $f(x) = \sin\left(\frac{1}{x}\right)$ définie sur $\mathbb{R}^*$.
1. Calculer les valeurs de $f(x)$ pour les suites $u_n = \dfrac{1}{2n\pi}$ et $v_n = \dfrac{1}{2n\pi + \pi/2}$ avec $n \geq 1$.
2. Quelles sont les limites de $(u_n)$ et $(v_n)$ quand $n \to +\infty$ ?
3. En déduire que la fonction $f$ ne possède aucune limite en 0.

**Exercice 45.21 (Croissances comparées généralisées : preuve pour tout $n \in \mathbb{N}^*$).**
On sait que $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$.
1. Démontrer que pour tout $n \in \mathbb{N}^*$ et tout $x > 0$ :
   $$\frac{e^x}{x^n} = \frac{1}{n^n} \left(\frac{e^{x/n}}{x/n}\right)^n.$$
2. En posant $u = \dfrac{x}{n}$, en déduire que $\lim\limits_{x \to +\infty} \dfrac{e^x}{x^n} = +\infty$.

**Exercice 45.22 (L'escalier du diable et limites à l'infini).**
Soit $f(x) = x - E(x)$ où $E(x)$ désigne la partie entière de $x$ (le plus grand entier relatif inférieur ou égal à $x$).
1. Tracer l'allure de la courbe de $f$ sur $[-2 \,;\, 3]$.
2. La fonction admet-elle une limite quand $x \to +\infty$ ?
3. Déterminer la limite à gauche et la limite à droite de $f$ en tout entier relatif $k \in \mathbb{Z}$.

---

### Solutions

#### Solutions du Niveau ★

- **45.1 :**
  1. $\lim (3x^3 - 5x + 1) = \lim 3x^3 = +\infty$.
  2. $\lim (-2x^4 + x^2) = \lim -2x^4 = -\infty$ (car $x^4 \to +\infty$ et $-2 < 0$).
  3. $\lim (4 - 0 + 0) = 4$.
  4. Pour $x \to 0^+$, $3/x \to +\infty$, donc $\lim = +\infty$.

- **45.2 :**
  1. $\lim_{x \to \pm\infty} f(x) = 2 \implies y = 2$ asymptote horizontale. $\lim_{x \to 3} f(x) = \pm\infty \implies x = 3$ asymptote verticale.
  2. $\lim_{x \to \pm\infty} g(x) = 0 \implies y = 0$ asymptote horizontale. $x^2 - 4 = 0 \iff x = \pm 2$, d'où deux asymptotes verticales : $x = 2$ et $x = -2$.
  3. $\lim_{x \to +\infty} e^{-x} = 0 \implies \lim_{x \to +\infty} h(x) = 5 \implies y = 5$ asymptote horizontale en $+\infty$.

- **45.3 :** Numérateur : $4 + 1 = 5 > 0$. Dénominateur : $x - 4 \to 0$.
  - Si $x > 4$, $x - 4 > 0 \implies \lim_{x \to 4^+} f(x) = +\infty$.
  - Si $x < 4$, $x - 4 < 0 \implies \lim_{x \to 4^-} f(x) = -\infty$.
  Comme ces limites diffèrent, il n'existe pas de limite globale en 4.

- **45.4 :**
  1. $\lim \frac{x^2(4 - 3/x + 1/x^2)}{x^2(2 + 5/x)} = \frac{4}{2} = 2$.
  2. $\lim \frac{x^3}{5x^4} = \lim \frac{1}{5x} = 0$.
  3. $\lim \frac{x^5}{x^2} = \lim x^3 = +\infty$.

- **45.5 :**
  1. $e^x - 3x^4 = x^4 \left(\frac{e^x}{x^4} - 3\right) \to +\infty \times (+\infty - 3) = +\infty$.
  2. $\frac{e^x(1 + 2e^{-x})}{x^3(1 + x^{-3})} = \frac{e^x}{x^3} \times \frac{1 + 2e^{-x}}{1 + x^{-3}} \to +\infty \times 1 = +\infty$.
  3. $(x^2+1)e^x = x^2 e^x + e^x \to 0 + 0 = 0$ par croissances comparées en $-\infty$.

- **45.6 :** $f(3) = \sqrt{9} = 3$. La limite est le nombre dérivé $f'(3)$. Comme $f'(x) = \frac{2}{2\sqrt{2x+3}} = \frac{1}{\sqrt{2x+3}}$, on a $f'(3) = \frac{1}{3}$.

- **45.7 :** $f(x) - (2x - 1) = \frac{3}{x^2+1} \to 0$ en $+\infty$, donc $y = 2x - 1$ est asymptote oblique. Comme $x^2 + 1 > 0$, la différence est strictement positive : $\mathcal{C}_f$ est au-dessus de l'asymptote.

- **45.8 :**
  - $\lim_{x \to +\infty} (-1/x^2) = 0$, donc $\lim \exp(-1/x^2) = e^0 = 1$.
  - $\lim_{x \to 0^+} (-1/x) = -\infty$, donc $\lim_{X \to -\infty} e^X = 0$.

---

#### Solutions du Niveau ★★

- **45.9 :**
  1. En $-\infty$, $(x - 2)e^x = x e^x - 2e^x \to 0 - 0 = 0$ par croissances comparées. Comme $\lim_{x \to -\infty} x = -\infty$, on a $\lim_{x \to -\infty} f(x) = -\infty$.
  2. $f(x) - x = (x - 2)e^x \to 0$ quand $x \to -\infty$. Donc $(\Delta) : y = x$ est asymptote oblique en $-\infty$.
  3. Signe de $f(x) - x = (x - 2)e^x$ : comme $e^x > 0$, le signe est celui de $x - 2$.
     Sur $]-\infty \,;\, 2[$, $\mathcal{C}_f$ est en dessous de $(\Delta)$.
     Sur $]2 \,;\, +\infty[$, $\mathcal{C}_f$ est au-dessus de $(\Delta)$.
     En $x = 2$, la courbe coupe son asymptote en $(2 ; 2)$.
  4. En $+\infty$, $x - 2 \to +\infty$ et $e^x \to +\infty$, donc $(x-2)e^x \to +\infty$, d'où $\lim f(x) = +\infty$.

- **45.10 :**
  1. $\lim_{x \to +\infty} (x^2 - 2x + 3) = +\infty \implies \lim_{x \to +\infty} f(x) = +\infty$.
  2. Pour $x > 0$ :
     $$f(x) - (x - 1) = \frac{(\sqrt{x^2 - 2x + 3} - (x - 1))(\sqrt{x^2 - 2x + 3} + (x - 1))}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{(x^2 - 2x + 3) - (x - 1)^2}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{x^2 - 2x + 3 - (x^2 - 2x + 1)}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{2}{\sqrt{x^2 - 2x + 3} + (x - 1)}.$$
  3. Quand $x \to +\infty$, le dénominateur tend vers $+\infty$, donc le quotient tend vers 0. Ainsi, $y = x - 1$ est asymptote oblique en $+\infty$.

- **45.11 :** Quand $x \to -\infty$, on pose $X = -x > 0$.
  $f(x) = \sqrt{X^2 + 2X + 3}$. L'asymptote conjecturée est $y = -x + 1 = X + 1$.
  $f(x) - (-x + 1) = \sqrt{X^2 + 2X + 3} - (X + 1) = \frac{(X^2 + 2X + 3) - (X + 1)^2}{\sqrt{X^2 + 2X + 3} + (X + 1)} = \frac{2}{\sqrt{X^2 + 2X + 3} + X + 1} \xrightarrow[X \to +\infty]{} 0$.
  Donc $y = -x + 1$ est bien asymptote oblique en $-\infty$.

- **45.12 :**
  1. $N(0) = \frac{10}{1 + 9e^0} = \frac{10}{10} = 1$ millier d'individus (soit 1000 individus).
  2. Quand $t \to +\infty$, $-0{,}5t \to -\infty$, donc $e^{-0{,}5t} \to 0$.
     Ainsi $\lim_{t \to +\infty} N(t) = \frac{10}{1 + 0} = 10$ milliers (10 000 individus).
     Le biotope ne peut nourrir qu'un maximum de 10 000 animaux en raison des ressources limitées (nourriture, espace) : c'est la capacité de charge du milieu.
  3. L'asymptote horizontale a pour équation $y = 10$.

- **45.13 :**
  1. $x^3 - 1 = (x - 1)(x^2 + x + 1)$ et $x^2 - 1 = (x - 1)(x + 1)$.
     Pour $x \neq 1$, $\frac{x^3 - 1}{x^2 - 1} = \frac{x^2 + x + 1}{x + 1} \xrightarrow[x \to 1]{} \frac{3}{2}$.
  2. $\frac{\sqrt{x} - 2}{x - 4} = \frac{\sqrt{x} - 2}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \xrightarrow[x \to 4]{} \frac{1}{4}$.
  3. Quantité conjuguée : $\frac{\sqrt{1+x} - 1}{x} = \frac{(1+x) - 1}{x(\sqrt{1+x} + 1)} = \frac{1}{\sqrt{1+x} + 1} \xrightarrow[x \to 0]{} \frac{1}{2}$. (Ou taux d'accroissement de $\sqrt{1+x}$ en 0).

- **45.14 :**
  1. $ax + b + \frac{c}{x+1} = \frac{ax^2 + (a+b)x + b+c}{x+1}$.
     Identification : $a = 3$, $a+b = 5 \implies b = 2$, $b+c = -2 \implies c = -4$.
     Donc $f(x) = 3x + 2 - \frac{4}{x+1}$.
  2. Asymptote verticale : $x = -1$.
     Asymptote oblique : $y = 3x + 2$ (car $\lim_{x \to \pm\infty} \frac{-4}{x+1} = 0$).
  3. L'asymptote verticale a pour abscisse $x = -1$. Sur l'asymptote oblique, $y = 3(-1) + 2 = -1$. Le point d'intersection est $I(-1 ; -1)$.

- **45.15 :**
  1. $\frac{\pi x + 1}{2x - 3} = \frac{\pi + 1/x}{2 - 3/x} \to \frac{\pi}{2}$. Par continuité du cosinus : $\lim = \cos(\pi/2) = 0$.
  2. Avec $X = 1/x$, quand $x \to +\infty$, $X \to 0^+$.
     L'expression devient $\frac{\sin X}{X}$, dont la limite en 0 est $\sin'(0) = \cos(0) = 1$.

- **45.16 :**
  1. Pour tout réel $x$, $-1 \leq \sin(x) \leq 1$. On ajoute $2x$ : $2x - 1 \leq 2x + \sin(x) \leq 2x + 1$. Comme $x > 1$, $x - 1 > 0$, on divise sans changer l'ordre.
  2. $\lim_{x \to +\infty} \frac{2x - 1}{x - 1} = 2$ et $\lim_{x \to +\infty} \frac{2x + 1}{x - 1} = 2$. Par le théorème des gendarmes, $\lim f(x) = 2$.

- **45.17 :**
  $f_m(x) = \frac{x^2(m + 4/x - 1/x^2)}{x^2(2 + 3/x^2)} = \frac{m + 4/x - 1/x^2}{2 + 3/x^2} \xrightarrow[x \to +\infty]{} \frac{m}{2}$.
  La limite est donc $\frac{m}{2}$ pour toute valeur de $m \in \mathbb{R}$.

---

#### Solutions du Niveau ★★★

- **45.18 :**
  1. Comme $f(a) = g(a) = 0$, $\frac{f(x)}{g(x)} = \frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}$. Par quotient de limites de taux d'accroissement, comme $g'(a) \neq 0$, la limite vaut $\frac{f'(a)}{g'(a)}$.
  2. Avec $f(x) = e^{2x} - \cos(x)$ et $g(x) = x$, on a $f(0) = 1 - 1 = 0$ et $g(0) = 0$.
     $f'(x) = 2e^{2x} + \sin(x) \implies f'(0) = 2 + 0 = 2$.
     $g'(x) = 1 \implies g'(0) = 1$.
     La limite vaut $\frac{f'(0)}{g'(0)} = \frac{2}{1} = 2$.

- **45.19 :**
  1. Division euclidienne de $x^3 + 2x^2 - 1$ par $x - 1$ :
     $x^3 + 2x^2 - 1 = (x - 1)(x^2 + 3x + 3) + 2$.
     Donc $f(x) = x^2 + 3x + 3 + \frac{2}{x - 1}$. Ici $P(x) = x^2 + 3x + 3$ et $R = 2$.
  2. $\lim_{x \to \pm\infty} [f(x) - P(x)] = \lim_{x \to \pm\infty} \frac{2}{x - 1} = 0$. La parabole d'équation $y = x^2 + 3x + 3$ épouse le tracé de la courbe à l'infini.

- **45.20 :**
  1. $f(u_n) = \sin(2n\pi) = 0$.
     $f(v_n) = \sin(2n\pi + \pi/2) = \sin(\pi/2) = 1$.
  2. $\lim u_n = 0$ et $\lim v_n = 0$.
  3. Si $f$ avait une limite $L$ en 0, alors pour toute suite tendant vers 0, l'image devrait tendre vers $L$. Or $f(u_n) \to 0$ et $f(v_n) \to 1$. Comme $0 \neq 1$, $f$ oscille infiniment vite au voisinage de 0 et n'admet aucune limite en 0.

- **45.21 :**
  1. $\frac{1}{n^n} \left(\frac{e^{x/n}}{x/n}\right)^n = \frac{1}{n^n} \frac{(e^{x/n})^n}{(x/n)^n} = \frac{e^x}{n^n \frac{x^n}{n^n}} = \frac{e^x}{x^n}$.
  2. Posons $u = x/n$. Quand $x \to +\infty$, $u \to +\infty$.
     Comme $\lim_{u \to +\infty} \frac{e^u}{u} = +\infty$, on a $\lim_{u \to +\infty} \left(\frac{e^u}{u}\right)^n = +\infty$.
     En multipliant par la constante strictement positive $\frac{1}{n^n}$, on conclut que $\lim_{x \to +\infty} \frac{e^x}{x^n} = +\infty$.

- **45.22 :**
  1. $f(x)$ est la « partie décimale » (ou fractionnaire) de $x$. C'est une fonction en dents de scie, périodique de période 1, formée de segments obliques de pente 1 valant 0 en $k$ et tendant vers 1 en $k^-$.
  2. La fonction oscille périodiquement entre 0 et 1 quand $x \to +\infty$, elle n'admet donc aucune limite en $+\infty$.
  3. Soit $k \in \mathbb{Z}$. Pour $x \in [k \,;\, k+1[$, $E(x) = k$, donc $f(x) = x - k \xrightarrow[x \to k^+]{} 0$.
     Pour $x \in ]k-1 \,;\, k[$, $E(x) = k-1$, donc $f(x) = x - (k-1) \xrightarrow[x \to k^-]{} k - k + 1 = 1$.
     La limite à droite vaut 0 et la limite à gauche vaut 1 : la courbe subit un saut de hauteur 1 à chaque entier.

---

### La question qui ouvre la suite

Nous venons de voir que certaines fonctions subissent de brutales ruptures : des asymptotes verticales où la courbe se déchire vers l'infini, ou des marches d'escalier où la courbe saute sans prévenir d'une altitude à une autre.
Mais la plupart des lois de la nature — la trajectoire d'une balle de tennis, le niveau de l'eau qui monte dans un vase, la croissance d'une plante — ne connaissent pas de tels sauts instantanés.
Comment exprimer avec la plus haute rigueur mathématique l'idée qu'une courbe se trace **d'un seul trait de crayon, sans jamais lever la pointe de la feuille** ?
Et pourquoi cette propriété fondamentale garantit-elle qu'en traversant un fleuve d'une rive à l'autre, on est absolument certain de couper le courant au milieu ?

C'est l'essence de la **continuité** et du prestigieux **Théorème des Valeurs Intermédiaires (TVI)**. Rendez-vous au chapitre 46.
