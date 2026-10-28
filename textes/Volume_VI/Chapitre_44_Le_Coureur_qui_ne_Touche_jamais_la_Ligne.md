# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 44 : Le Coureur qui ne Touche jamais la Ligne

> *« Achille aux pieds légers ne rattrapera jamais la tortue, disait Zénon. Car pour l'atteindre, il doit d'abord parcourir la moitié de la distance, puis la moitié du reste, puis la moitié du reste encore. Une infinité d'étapes ne peut s'achever en un temps fini. L'erreur de Zénon n'était pas dans sa vue du monde, mais dans son manque d'un outil mathématique : le concept de limite. »*

---

### Ce que tu vas découvrir

- Comment le paradoxe grec de **Zénon d'Élée** a tenu tête aux penseurs pendant plus de deux millénaires, et comment la notion moderne de **limite** l'a enfin résolu.
- La **définition formelle** d'une suite convergente : l'idée intuitive d'un « tunnel » ou d'un intervalle ouvert qui emprisonne tous les termes à partir d'un certain rang, et la définition rigoureuse de la divergence vers $\pm\infty$.
- Les **théorèmes de comparaison** et le fameux **théorème d'encadrement des gendarmes**.
- Le **théorème de convergence des suites monotones bornées** : savoir qu'une suite converge avant même de connaître sa limite.
- Le comportement complet des **suites géométriques** $q^n$, démontré grâce à l'inégalité de Bernoulli (démonstration exigible au baccalauréat).
- L'**algorithme de seuil en Python** pour trouver quand une suite franchit une barrière fixée.

---

### 1. Le problème : Achille, la tortue et le stade infini

#### 1.1 Le paradoxe de la dichotomie

Cinq siècles avant notre ère, dans la cité grecque d'Élée au sud de l'Italie, le philosophe **Zénon** propose une série d'énigmes troublantes destinées à montrer que le mouvement est une illusion de nos sens.

Considère un coureur qui s'élance sur une piste de 100 mètres. Avant de franchir la ligne d'arrivée, il doit impérativement atteindre la moitié de la course : $50\text{ m}$.
Une fois aux $50\text{ m}$, il lui reste $50\text{ m}$ à courir ; il doit d'abord atteindre la moitié de ce reste, soit $75\text{ m}$.
Aux $75\text{ m}$, il doit parcourir la moitié du quart restant, soit atteindre $87{,}5\text{ m}$...

```
Départ                                                     Arrivée
[0] ───────────────┬───────────────┬───────┬───┬─┬[100]
                   50              75    87.5 93.75 ...
                  1/2             3/4     7/8 15/16
```

À chaque étape $n$, la distance parcourue en fraction de la piste totale est :
$$u_n = 1 - \frac{1}{2^n}.$$

Zénon argumente :
> *« Le coureur doit accomplir une infinité d'actes successifs : franchir le 1er intervalle, puis le 2e, puis le 3e... Or, personne ne peut accomplir une infinité de tâches en un temps fini. Donc, le coureur n'atteindra jamais la ligne. Pire : il ne peut même pas s'élancer, car avant de faire un mètre, il doit faire un demi-mètre, et avant cela un quart de mètre... »*

Pourtant, dans le monde réel, n'importe quel enfant franchit les 100 mètres en quelques secondes. Où se trouve la faille du raisonnement de Zénon ?

#### 1.2 La somme d'une infinité de morceaux

Regardons la distance totale parcourue comme une somme de tranches infiniment répétées :
$$S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \dots + \frac{1}{2^n} + \dots$$

Calculons la somme des $n$ premiers termes (notée $S_n$) :
- $S_1 = \frac{1}{2} = 0{,}5$
- $S_2 = \frac{1}{2} + \frac{1}{4} = \frac{3}{4} = 0{,}75$
- $S_3 = \frac{3}{4} + \frac{1}{8} = \frac{7}{8} = 0{,}875$
- $S_n = 1 - \frac{1}{2^n}$.

Plus $n$ devient grand, plus le terme $\frac{1}{2^n}$ devient minuscule :
- pour $n = 10$, $\frac{1}{2^{10}} = \frac{1}{1024} \approx 0{,}000976$ ;
- pour $n = 30$, $\frac{1}{2^{30}} \approx 0{,}00000000093$.

L'écart entre le coureur et la ligne d'arrivée ($100\text{ m}$) devient inférieur à la taille d'un cheveu, puis à celle d'une molécule, puis à celle du noyau d'un atome.
La faille de Zénon est de supposer qu'une somme d'une infinité de durées est nécessairement infinie. Mais si le coureur court à vitesse constante de $10\text{ m/s}$ :
- la première moitié prend $5\text{ s}$ ;
- le quart suivant prend $2{,}5\text{ s}$ ;
- le huitième suivant prend $1{,}25\text{ s}$...

Le temps total écoulé est lui aussi la somme :
$$T = 5 + 2{,}5 + 1{,}25 + 0{,}625 + \dots = 10\text{ secondes}.$$
Une infinité d'intervalles de temps peuvent parfaitement totaliser une durée finie !

Pour formaliser ce saut vertigineux de l'infiniment grand sans tomber dans des pièges métaphysiques, les mathématiciens du XIXᵉ siècle (Cauchy, Weierstrass) ont forgé un outil d'une précision chirurgicale : **la limite de suite**.

---

### 2. Définitions : apprivoiser l'infini

#### 2.1 Les notations expliquées

- Une suite réelle est notée $(u_n)_{n \in \mathbb{N}}$ ou simplement $(u_n)$. La lettre $n$ représente un entier naturel ($n = 0, 1, 2, 3 \dots$) qui joue le rôle d'un compteur de temps discret (tic-tac d'une horloge). $u_n$ désigne le terme de rang $n$.
- $\lim\limits_{n \to +\infty} u_n = L$ se lit : « la limite de $u_n$ quand $n$ tend vers plus l'infini est égale à $L$ ». L'abréviation $\lim$ vient du latin *limes*, qui désignait la frontière fortifiée de l'Empire romain.
- La flèche $\to$ se lit « tend vers ». On écrit aussi parfois $u_n \xrightarrow[n \to +\infty]{} L$.
- Un intervalle ouvert contenant un réel $L$ est un intervalle de la forme $]L - \varepsilon ; L + \varepsilon[$ avec $\varepsilon > 0$ (la lettre grecque $\varepsilon$, « epsilon », désignant traditionnellement une marge d'erreur aussi minuscule que l'on veut).

```
                 L - ε         L         L + ε
───────(───────────[───────────●───────────]───────────)───────► Axe des réels
                 ◄─────── 2ε ───────►
```

#### 2.2 Suite convergente : la définition officielle

Que signifie exactement : « quand $n$ devient très grand, les termes $u_n$ se rapprochent de $L$ » ?
Dire seulement « ils se rapprochent » est insuffisant. La suite $1 + \frac{1}{n}$ se rapproche de $-5$, mais sa limite n'est pas $-5$ ! Il faut qu'ils s'approchent de $L$ **d'aussi près que l'on veut**, et qu'ils **y restent pour toujours**.

> **📐 Définition — Limite finie (suite convergente).**
> On dit qu'une suite $(u_n)$ a pour limite le réel $L$ lorsque :
> **Tout intervalle ouvert contenant $L$ contient tous les termes de la suite à partir d'un certain rang.**
> On écrit alors :
> $$\lim_{n \to +\infty} u_n = L.$$
> Une suite qui possède une limite réelle finie $L$ est dite **convergente**. Dans le cas contraire, elle est dite **divergente**.

**Traduction géométrique et dynamique :**
Imagine un jeu entre deux personnes : un *Challenger* et un *Défenseur*.
1. Le Challenger choisit un intervalle ouvert $]a ; b[$ autour de $L$, aussi étroit et microscopique qu'il le souhaite (par exemple $]L - 0{,}001 \,;\, L + 0{,}001[$). C'est la « cible ».
2. Le Défenseur doit trouver un rang entier $N$ à partir duquel **tous** les termes suivants $u_N, u_{N+1}, u_{N+2}, \dots$ tombent dans la cible, sans jamais plus en ressortir.
Si le Défenseur a une stratégie pour gagner quel que soit l'intervalle imposé au départ, alors la suite converge vers $L$.

> **💡 Le savais-tu ?** En symboles formalisés au niveau supérieur, cela s'écrit avec les quantificateurs $\forall$ (« pour tout ») et $\exists$ (« il existe ») :
> $$\forall \varepsilon > 0, \;\exists N \in \mathbb{N}, \;\forall n \geq N, \; |u_n - L| < \varepsilon.$$
> Au lycée, le programme officiel utilise la formulation équivalente avec les intervalles ouverts : *« pour tout intervalle ouvert $I$ contenant $L$, il existe un rang $N$ tel que pour tout $n \geq N$, $u_n \in I$ »*.

#### 2.3 Suite divergente vers $+\infty$ ou $-\infty$

Une suite ne converge pas toujours vers un nombre. Elle peut exploser vers l'infini, ou osciller indéfiniment sans jamais se stabiliser.

> **📐 Définition — Limite infinie.**
> - On dit qu'une suite $(u_n)$ a pour limite $+\infty$ si tout intervalle de la forme $]A ; +\infty[$ (où $A$ est un réel arbitraire) contient tous les termes de la suite à partir d'un certain rang :
>   $$\lim_{n \to +\infty} u_n = +\infty.$$
> - On dit qu'une suite $(u_n)$ a pour limite $-\infty$ si tout intervalle de la forme $]-\infty ; B[$ (où $B$ est un réel arbitraire) contient tous les termes de la suite à partir d'un certain rang :
>   $$\lim_{n \to +\infty} u_n = -\infty.$$

**Sens concret :** Fixe une barre $A$ aussi haute que tu veux (un milliard, dix milliards...). À partir d'un certain rang $N$, la suite dépasse cette barre et ne redescend plus jamais en dessous.

> **⚠️ Attention, piège ! — « Divergente » ne veut pas dire « tend vers l'infini ».**
> Une suite divergente est simplement une suite qui **ne converge pas** vers un réel fini.
> - La suite $u_n = n^2$ diverge vers $+\infty$.
> - La suite $v_n = (-1)^n$ (qui vaut alternativement $+1, -1, +1, -1 \dots$) est **divergente**, mais elle ne tend ni vers $+\infty$ ni vers $-\infty$ ! Elle reste bornée entre $-1$ et $1$, mais n'a aucune limite.

#### 2.4 Unicité de la limite

> **📐 Propriété fondamentale — Unicité.**
> Lorsqu'une suite $(u_n)$ admet une limite (finie ou infinie), **cette limite est unique**. Une suite ne peut pas converger vers deux nombres distincts en même temps.

*Pourquoi ?* Si $u_n$ convergeait à la fois vers $L_1$ et $L_2$ avec $L_1 \neq L_2$, on pourrait entourer $L_1$ et $L_2$ de deux petits intervalles disjoints (ne se touchant pas). À partir d'un certain rang, les termes $u_n$ devraient se trouver simultanément dans les deux intervalles : impossible !

---

### 3. Les suites de référence et leurs limites

Le tableau suivant rassemble les briques fondamentales dont toutes les autres limites sont construites :

| Suite $u_n$ ($n \geq 1$) | Limite en $+\infty$ | Justification intuitive |
| :---: | :---: | :--- |
| $k$ (constante) | $k$ | Tous les termes valent déjà $k$. |
| $\dfrac{1}{n}$ | $0$ | Partager 1 gâteau entre un milliard d'invités donne une miette. |
| $\dfrac{1}{n^2}$, $\dfrac{1}{n^p}$ ($p \geq 1$) | $0$ | Le dénominateur explose encore plus vite. |
| $\dfrac{1}{\sqrt{n}}$ | $0$ | $\sqrt{n}$ grandit vers $+\infty$, son inverse s'écrase vers $0$. |
| $n$, $n^2$, $n^p$ ($p \geq 1$) | $+\infty$ | Les puissances d'entiers dépassent toute borne. |
| $\sqrt{n}$ | $+\infty$ | Même si elle ralentit, elle n'a aucun plafond. |

---

### 4. Opérations sur les limites et Formes Indéterminées

Quand on additionne, multiplie ou divise deux suites qui ont des limites connues, le bon sens mathématique s'applique la plupart du temps... sauf dans quatre situations ambiguës appelées **Formes Indéterminées** (notées F.I.).

#### 4.1 Les règles logiques directes

Si $\lim u_n = L$ et $\lim v_n = L'$ (avec $L, L' \in \mathbb{R}$) :
- **Somme :** $\lim (u_n + v_n) = L + L'$
- **Produit :** $\lim (u_n \times v_n) = L \times L'$
- **Quotient :** $\lim \left(\dfrac{u_n}{v_n}\right) = \dfrac{L}{L'}$ (à condition que $L' \neq 0$).

Avec les infinis :
- Un nombre fini $+$ l'infini donne l'infini : $5 + (+\infty) = +\infty$.
- $(+\infty) + (+\infty) = +\infty$ et $(-\infty) + (-\infty) = -\infty$.
- Produit des signes : $(+\infty) \times (-\infty) = -\infty$, $(-3) \times (-\infty) = +\infty$.
- Un nombre fini divisé par l'infini donne $0$ : $\dfrac{L}{\pm\infty} = 0$.
- Un nombre non nul divisé par un infiniment petit donne l'infini : si $u_n \to L > 0$ et $v_n \to 0$ avec $v_n > 0$, alors $\dfrac{u_n}{v_n} \to +\infty$.

#### 4.2 Les quatre Formes Indéterminées (F.I.)

Une forme est dite « indéterminée » quand **la seule connaissance des limites de chaque morceau ne suffit pas pour prédire le résultat global**. Le résultat dépend de qui est « le plus fort » :

1. **$\infty - \infty$** (somme de deux infinis de signes contraires) : qui l'emporte entre le géant positif et le géant négatif ?
2. **$0 \times \infty$** (produit d'un infiniment petit et d'un infiniment grand) : écrasement vers 0 ou explosion vers l'infini ?
3. **$\dfrac{\infty}{\infty}$** (quotient de deux infinis) : le numérateur court-il plus vite que le dénominateur ?
4. **$\dfrac{0}{0}$** (quotient de deux infiniment petits).

> **⚠️ Attention, piège ! — F.I. ne veut pas dire « pas de limite ».**
> « Indéterminée » ne signifie pas que le calcul est impossible ou que la limite n'existe pas ! Cela signifie simplement : *« Arrête-toi, ne conclus pas tout de suite : transforme l'expression pour lever le doute »*. La technique reine pour les polynômes et fractions est de **factoriser par le terme de plus haut degré**.

---

### 5. Les Théorèmes Fondamentaux

#### 5.1 Théorèmes de comparaison

> **📐 Théorème de comparaison (vers l'infini).**
> Soient $(u_n)$ et $(v_n)$ deux suites telles qu'à partir d'un certain rang :
> $$u_n \geq v_n.$$
> 1. Si $\lim\limits_{n \to +\infty} v_n = +\infty$, alors $\lim\limits_{n \to +\infty} u_n = +\infty$.
> 2. Si $\lim\limits_{n \to +\infty} u_n = -\infty$, alors $\lim\limits_{n \to +\infty} v_n = -\infty$.

*Image mentale :* Si ton ami $v_n$ grimpe vers le ciel sans limite et que tu marches constamment sur ses épaules ($u_n \geq v_n$), tu es inévitablement propulsé vers le ciel avec lui.

#### 5.2 Le Théorème d'Encadrement (dit « des Gendarmes »)

> **📐 Théorème — Théorème d'encadrement des gendarmes.**
> Soient $(u_n)$, $(v_n)$ et $(w_n)$ trois suites réelles.
> S'il existe un rang $N$ à partir duquel :
> $$v_n \leq u_n \leq w_n$$
> et si $\lim\limits_{n \to +\infty} v_n = \lim\limits_{n \to +\infty} w_n = L \in \mathbb{R}$,
> alors la suite $(u_n)$ converge et sa limite est :
> $$\lim\limits_{n \to +\infty} u_n = L.$$

```
 w_n (gendarme du haut)  ╲
                           ╲
 u_n (le suspect encadré) ───*───────► converge vers L
                           ╱
 v_n (gendarme du bas)   ╱
```

*Origine du nom :* Si deux gendarmes ($v_n$ et $w_n$) convergent tous les deux vers le même commissariat $L$ en tenant le suspect ($u_n$) encadré entre eux, le suspect n'a d'autre choix que d'entrer lui aussi dans le commissariat $L$.

> **✍️ Démonstration du théorème des gendarmes.**
> Soit $I$ un intervalle ouvert quelconque contenant $L$. Par définition d'un intervalle ouvert, il existe un réel $\varepsilon > 0$ tel que $]L - \varepsilon \,;\, L + \varepsilon[ \subset I$.
> Puisque $\lim v_n = L$, il existe un rang $N_1$ tel que pour tout $n \geq N_1$, $L - \varepsilon < v_n < L + \varepsilon$. En particulier, $L - \varepsilon < v_n$.
> Puisque $\lim w_n = L$, il existe un rang $N_2$ tel que pour tout $n \geq N_2$, $L - \varepsilon < w_n < L + \varepsilon$. En particulier, $w_n < L + \varepsilon$.
> De plus, par hypothèse, $v_n \leq u_n \leq w_n$ pour tout $n \geq N_0$.
> Posons alors $N = \max(N_0, N_1, N_2)$. Pour tout entier $n \geq N$, les trois conditions sont réunies simultanément :
> $$L - \varepsilon < v_n \leq u_n \leq w_n < L + \varepsilon \implies u_n \in ]L - \varepsilon \,;\, L + \varepsilon[ \subset I.$$
> Tout intervalle ouvert contenant $L$ contient donc tous les termes $u_n$ à partir du rang $N$. La suite $(u_n)$ converge bien vers $L$. $\blacksquare$

#### 5.3 Théorème de convergence des suites monotones

C'est l'un des théorèmes les plus profonds de l'analyse : il permet de savoir qu'une suite converge **sans même calculer sa limite**.

> **📐 Théorème de convergence monotone.**
> 1. Toute suite **croissante et majorée** converge vers une limite réelle $L$.
> 2. Toute suite **décroissante et minorée** converge vers une limite réelle $L$.

```
 Plafond (Majorant M) ───────────────────────────────────
                        Lim L ---------------------------
                         u_n    .-'""'-.
                              .'        '-.
                             /             '
 u_0 .-'
```

*Rappels de vocabulaire :*
- Une suite est **majorée** par $M$ si pour tout $n$, $u_n \leq M$.
- Une suite est **minorée** par $m$ si pour tout $n$, $u_n \geq m$.
- Une suite est **bornée** si elle est à la fois majorée et minorée ($m \leq u_n \leq M$).

> **⚠️ Attention, piège ! — Le majorant n'est pas forcément la limite !**
> Si une suite $(u_n)$ croissante est majorée par $10$, le théorème garantit qu'elle converge vers une limite $L$, et que $L \leq 10$. Mais la limite $L$ n'est pas obligatoirement $10$ ! Elle peut converger vers $2$, ou vers $\sqrt{3}$, car $10$ n'est qu'un plafond parmi d'autres.
> De plus, une suite croissante non majorée diverge toujours vers $+\infty$.

---

### 6. La limite des suites géométriques $q^n$

La suite géométrique fondamentale est définie par $u_n = q^n$ où $q$ est un nombre réel fixé appelé la raison. Son comportement dépend de la position de $q$ par rapport à $-1$ et $1$.

> **📐 Théorème — Limite de $q^n$.**
> - Si $q > 1$ : $\lim\limits_{n \to +\infty} q^n = +\infty$.
> - Si $q = 1$ : la suite est constante égale à $1$, donc $\lim\limits_{n \to +\infty} q^n = 1$.
> - Si $-1 < q < 1$ : $\lim\limits_{n \to +\infty} q^n = 0$.
> - Si $q \leq -1$ : la suite n'a pas de limite (elle oscille en changeant de signe).

#### Démonstration exigible au baccalauréat (cas $q > 1$)

Cette démonstration repose directement sur l'**inégalité de Bernoulli** établie au chapitre 43 : pour tout réel $a > 0$ et tout entier $n \in \mathbb{N}$, $(1+a)^n \geq 1 + na$.

> **✍️ Démonstration (exigible).**
> Soit $q$ un réel strictement supérieur à $1$.
> Posons $a = q - 1$. Comme $q > 1$, on a $a > 0$.
> On peut donc écrire : $q = 1 + a$.
> D'après l'inégalité de Bernoulli :
> $$q^n = (1 + a)^n \geq 1 + na.$$
> Or, comme $a > 0$, la suite affine $1 + na$ tend vers $+\infty$ :
> $$\lim_{n \to +\infty} (1 + na) = +\infty.$$
> Par le théorème de comparaison (5.1), comme $q^n \geq 1 + na$ pour tout $n$, on en déduit immédiatement :
> $$\lim_{n \to +\infty} q^n = +\infty. \quad \blacksquare$$

*Conséquence pour le cas $0 < q < 1$ :*
Si $0 < q < 1$, posons $q' = \frac{1}{q} > 1$.
Alors $q^n = \frac{1}{(q')^n}$. Comme $(q')^n \to +\infty$, le quotient tend vers $0$ : $\lim q^n = 0$.
Si $-1 < q < 0$, on a $|q^n| = |q|^n \to 0$ car $0 < |q| < 1$, d'où $q^n \to 0$ par encadrement $-|q|^n \leq q^n \leq |q|^n$.

---

### 7. Algorithme de Seuil en Python

Lorsqu'une suite converge vers un nombre ou diverge vers $+\infty$, une question pratique capitale se pose pour les ingénieurs, les financiers et les scientifiques :
*« À partir de quel rang $n$ la suite dépasse-t-elle une valeur seuil donnée ? »*

Puisqu'on ne connaît pas d'avance le rang d'arrêt, on utilise une boucle non bornée : la boucle `while` (tant que).

#### Exemple : Refroidissement d'un moteur
La température d'un moteur après $n$ minutes suit la suite géométrique décroissante :
$$T_n = 20 + 80 \times 0{,}9^n.$$
Le moteur est considéré comme froid dès que sa température descend en dessous de $30^\circ\text{C}$.

```python
def seuil_temperature(seuil):
    """Calcule le nombre de minutes nécessaires pour passer sous le seuil."""
    n = 0
    T = 100.0  # T_0 = 20 + 80 = 100 °C
    while T > seuil:
        n = n + 1
        T = 20 + 80 * (0.9 ** n)
    return n

# Test pour un seuil à 30 °C
minutes = seuil_temperature(30)
print(f"Le moteur passe sous 30°C au bout de {minutes} minutes.")
# Affichera : 20 minutes (car T_19 ≈ 30.8 °C et T_20 ≈ 29.7 °C)
```

> **🧭 Méthode — Structure standard d'un algorithme de seuil au Bac :**
> 1. Initialiser le compteur de rang : `n = 0`.
> 2. Initialiser la valeur de la suite : `u = u_0`.
> 3. Condition de la boucle `while` : mettre la condition **contraire** de ce que l'on cherche (on continue *tant que* le seuil n'est pas encore atteint).
> 4. Dans le corps de la boucle : actualiser le terme `u` et incrémenter `n = n + 1`.
> 5. Renvoyer `n` à la fin.

---

### 8. Exemples Résolus pas à pas

#### Exemple résolu 1 — Utiliser la définition avec un intervalle

**Énoncé :** Soit la suite $(u_n)_{n \geq 1}$ définie par $u_n = 3 + \dfrac{2}{n}$.
1. Quelle est la limite conjecturée $L$ de la suite ?
2. Déterminer un rang $N$ à partir duquel tous les termes $u_n$ appartiennent à l'intervalle ouvert $]2{,}99 \,;\, 3{,}01[$.

**Solution :**
1. Comme $\lim\limits_{n \to +\infty} \frac{1}{n} = 0$, on a $\lim\limits_{n \to +\infty} u_n = 3 + 2 \times 0 = 3$. La limite est $L = 3$.
2. L'intervalle $]2{,}99 \,;\, 3{,}01[$ s'écrit $]3 - 0{,}01 \,;\, 3 + 0{,}01[$.
On cherche pour quelles valeurs de $n$ on a $u_n \in ]2{,}99 \,;\, 3{,}01[$ :
$$2{,}99 < 3 + \frac{2}{n} < 3{,}01.$$
Comme $\frac{2}{n} > 0$ pour tout $n \geq 1$, l'inégalité de gauche $2{,}99 < 3 + \frac{2}{n}$ est toujours vraie.
Reste l'inégalité de droite :
$$3 + \frac{2}{n} < 3{,}01 \iff \frac{2}{n} < 0{,}01 \iff \frac{2}{n} < \frac{1}{100} \iff n > 200.$$
Puisque $n$ est un entier, dès le rang $N = 201$, tous les termes $u_n$ pour $n \geq 201$ sont garantis d'être dans l'intervalle $]2{,}99 \,;\, 3{,}01[$.

---

#### Exemple résolu 2 — Lever une indétermination rationnelle $\frac{\infty}{\infty}$

**Énoncé :** Déterminer la limite de la suite $(u_n)$ définie pour tout $n \geq 1$ par :
$$u_n = \frac{5n^2 - 3n + 2}{2n^2 + 7}.$$

**Solution :**
- Numérateur : $\lim (5n^2 - 3n + 2) = +\infty$.
- Dénominateur : $\lim (2n^2 + 7) = +\infty$.
Il s'agit d'une Forme Indéterminée du type « $\frac{\infty}{\infty}$ ».
*Méthode : on factorise le numérateur et le dénominateur par leur terme prépondérant ($n^2$) :*
$$u_n = \frac{n^2 \left(5 - \dfrac{3}{n} + \dfrac{2}{n^2}\right)}{n^2 \left(2 + \dfrac{7}{n^2}\right)}.$$
Pour $n \geq 1$, on simplifie par $n^2 \neq 0$ :
$$u_n = \frac{5 - \dfrac{3}{n} + \dfrac{2}{n^2}}{2 + \dfrac{7}{n^2}}.$$
Or :
$\lim \dfrac{3}{n} = 0$, $\lim \dfrac{2}{n^2} = 0$, donc $\lim \left(5 - \dfrac{3}{n} + \dfrac{2}{n^2}\right) = 5$.
$\lim \dfrac{7}{n^2} = 0$, donc $\lim \left(2 + \dfrac{7}{n^2}\right) = 2$.
Par quotient de limites, on conclut de manière irréfutable :
$$\lim_{n \to +\infty} u_n = \frac{5}{2}.$$

---

#### Exemple résolu 3 — Gendarmes et trigonométrie

**Énoncé :** Déterminer la limite de la suite $(v_n)_{n \geq 1}$ définie par :
$$v_n = \frac{3 + (-1)^n \cos(n)}{n + \sqrt{n}}.$$

**Solution :**
Les fonctions $\cos(n)$ et $(-1)^n$ oscillent sans fin et n'ont pas de limite quand $n \to +\infty$. Il est impossible d'appliquer les règles d'addition de limites. On pense immédiatement au **théorème des gendarmes**.
Pour tout entier $n$, $-1 \leq \cos(n) \leq 1$ et $(-1)^n \in \{-1 ; 1\}$.
Ainsi, le produit $(-1)^n \cos(n)$ reste impérativement encadré entre $-1$ et $1$ :
$$-1 \leq (-1)^n \cos(n) \leq 1.$$
Ajoutons 3 à chaque membre :
$$3 - 1 \leq 3 + (-1)^n \cos(n) \leq 3 + 1 \iff 2 \leq 3 + (-1)^n \cos(n) \leq 4.$$
Comme pour tout $n \geq 1$, le dénominateur $n + \sqrt{n}$ est strictement positif, on peut diviser sans changer le sens des inégalités :
$$\frac{2}{n + \sqrt{n}} \leq v_n \leq \frac{4}{n + \sqrt{n}}.$$
Étudions les limites des deux bornes :
- $\lim (n + \sqrt{n}) = +\infty$, donc $\lim\limits_{n \to +\infty} \dfrac{2}{n + \sqrt{n}} = 0$.
- De même, $\lim\limits_{n \to +\infty} \dfrac{4}{n + \sqrt{n}} = 0$.
Les deux suites encadrantes convergent vers la même limite $0$.
D'après le **théorème d'encadrement des gendarmes**, la suite $(v_n)$ converge et :
$$\lim_{n \to +\infty} v_n = 0.$$

---

#### Exemple résolu 4 — Somme géométrique et convergence

**Énoncé :** On considère la suite $(S_n)$ définie pour tout entier $n \geq 1$ par :
$$S_n = \sum_{k=1}^n \left(\frac{2}{3}\right)^k = \frac{2}{3} + \left(\frac{2}{3}\right)^2 + \dots + \left(\frac{2}{3}\right)^n.$$
1. Exprimer $S_n$ sous forme close sans symbole de sommation.
2. Déterminer la limite de $S_n$ quand $n \to +\infty$.

**Solution :**
1. $S_n$ est la somme des $n$ premiers termes consécutifs d'une suite géométrique de premier terme $a = \frac{2}{3}$ et de raison $q = \frac{2}{3}$.
La formule de la somme géométrique donne (avec $q \neq 1$) :
$$\text{Somme} = \text{Premier terme} \times \frac{1 - q^{\text{nombre de termes}}}{1 - q}.$$
Ici :
$$S_n = \frac{2}{3} \times \frac{1 - \left(\frac{2}{3}\right)^n}{1 - \frac{2}{3}} = \frac{2}{3} \times \frac{1 - \left(\frac{2}{3}\right)^n}{\frac{1}{3}} = \frac{2}{3} \times 3 \times \left(1 - \left(\frac{2}{3}\right)^n\right) = 2 \left(1 - \left(\frac{2}{3}\right)^n\right).$$
2. Comme $-1 < \frac{2}{3} < 1$, d'après le théorème sur les suites géométriques :
$$\lim_{n \to +\infty} \left(\frac{2}{3}\right)^n = 0.$$
Par opérations sur les limites :
$$\lim_{n \to +\infty} S_n = 2(1 - 0) = 2.$$

---

#### Exemple résolu 5 — Comparaison vers l'infini

**Énoncé :** Démontrer que la suite $(w_n)$ définie pour tout $n \geq 1$ par $w_n = 2n^2 - 5\sin(n) + (-1)^n$ tend vers $+\infty$.

**Solution :**
Pour tout entier $n$, on a $-1 \leq \sin(n) \leq 1$, donc $-5 \leq -5\sin(n) \leq 5$, et $(-1)^n \geq -1$.
Par conséquent :
$$w_n = 2n^2 - 5\sin(n) + (-1)^n \geq 2n^2 - 5 - 1 = 2n^2 - 6.$$
Or :
$$\lim_{n \to +\infty} (2n^2 - 6) = +\infty.$$
Comme $w_n \geq 2n^2 - 6$ pour tout $n \geq 1$, par le **théorème de comparaison**, on conclut immédiatement :
$$\lim_{n \to +\infty} w_n = +\infty.$$

---

#### Exemple résolu 6 — Suite récurrente et convergence monotone

**Énoncé :** Soit la suite $(u_n)$ définie par $u_0 = 0$ et pour tout $n \in \mathbb{N}$ par :
$$u_{n+1} = \frac{1}{2}u_n + 3.$$
1. Démontrer par récurrence que pour tout $n \in \mathbb{N}$, $u_n < 6$.
2. Démontrer que la suite $(u_n)$ est strictement croissante.
3. En déduire que la suite converge vers une limite $L$ que l'on déterminera.

**Solution :**
1. **Démonstration par récurrence :**
Pour $n \in \mathbb{N}$, posons $\mathcal{P}(n)$ : « $u_n < 6$ ».
- *Initialisation :* $u_0 = 0 < 6$. Donc $\mathcal{P}(0)$ est vraie.
- *Hérédité :* Soit $n \in \mathbb{N}$ fixé. Supposons $\mathcal{P}(n)$ vraie, c'est-à-dire $u_n < 6$.
Alors :
$$\frac{1}{2}u_n < \frac{1}{2} \times 6 = 3 \implies \frac{1}{2}u_n + 3 < 3 + 3 = 6 \implies u_{n+1} < 6.$$
Donc $\mathcal{P}(n+1)$ est vraie.
- *Conclusion :* Par récurrence, pour tout entier naturel $n$, $u_n < 6$. La suite est **majorée par 6**.

2. **Sens de variation :**
Calculons la différence $u_{n+1} - u_n$ :
$$u_{n+1} - u_n = \left(\frac{1}{2}u_n + 3\right) - u_n = -\frac{1}{2}u_n + 3 = \frac{1}{2}(6 - u_n).$$
D'après la question 1, $u_n < 6$, donc $6 - u_n > 0$.
Par suite, $u_{n+1} - u_n > 0$, ce qui prouve que la suite $(u_n)$ est **strictement croissante**.

3. **Convergence et calcul de la limite :**
La suite $(u_n)$ étant croissante et majorée par 6, le **théorème de convergence monotone** assure qu'elle converge vers une limite finie réelle $L \leq 6$.
Déterminons $L$ :
Puisque $\lim u_n = L$, on a également $\lim u_{n+1} = L$.
En passant à la limite dans la relation $u_{n+1} = \frac{1}{2}u_n + 3$, on obtient :
$$L = \frac{1}{2}L + 3 \iff L - \frac{1}{2}L = 3 \iff \frac{1}{2}L = 3 \iff L = 6.$$
La suite $(u_n)$ converge vers $6$.

---

### Ce qu'il faut retenir

1. **Définition de la convergence :** $\lim u_n = L$ signifie que tout intervalle ouvert contenant $L$ contient tous les termes de la suite à partir d'un rang $N$.
2. **Divergence vers $+\infty$ :** tout intervalle $]A ; +\infty[$ contient tous les termes de la suite à partir d'un certain rang.
3. **Formes Indéterminées :** $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$. Pour un quotient de polynômes en $n$, on factorise toujours par le terme de plus haut degré au numérateur et au dénominateur.
4. **Théorème des Gendarmes :** Si $v_n \leq u_n \leq w_n$ et $\lim v_n = \lim w_n = L$, alors $\lim u_n = L$.
5. **Théorème de Comparaison :** Si $u_n \geq v_n$ et $\lim v_n = +\infty$, alors $\lim u_n = +\infty$.
6. **Suites géométriques $q^n$ :**
   - Si $q > 1$, $\lim q^n = +\infty$ (prouvé par l'inégalité de Bernoulli $(1+a)^n \geq 1 + na$).
   - Si $-1 < q < 1$, $\lim q^n = 0$.
   - Si $q \leq -1$, pas de limite.
7. **Convergence monotone :** Croissante $+$ majorée $\implies$ convergente. Décroissante $+$ minorée $\implies$ convergente.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 44.1.** Déterminer la limite de chacune des suites suivantes quand $n \to +\infty$ :
1. $u_n = 4 - \dfrac{7}{n} + \dfrac{3}{n^2}$
2. $v_n = -3n^3 + 500$
3. $w_n = 5 \times 0{,}4^n$
4. $t_n = 2 \times 1{,}05^n$

**Exercice 44.2.** Pour chacune des suites géométriques suivantes, préciser si elle converge et, le cas échéant, donner sa limite :
1. $a_n = \left(-\dfrac{3}{4}\right)^n$
2. $b_n = \left(\dfrac{7}{5}\right)^n$
3. $c_n = (-1{,}2)^n$
4. $d_n = \dfrac{4^n}{3^n}$

**Exercice 44.3.** Calculer la limite des suites rationnelles suivantes :
1. $u_n = \dfrac{3n + 1}{5n - 2}$
2. $v_n = \dfrac{7n^2 - 4}{2n^3 + n}$
3. $w_n = \dfrac{n^4 - 1}{100n^3 + 5}$

**Exercice 44.4.** Soit $u_n = 5 + \dfrac{1}{n}$. Trouver un rang $N$ à partir duquel $u_n \in ]4{,}999 \,;\, 5{,}001[$.

**Exercice 44.5.** Démontrer que pour tout $n \geq 1$, $\dfrac{-1}{n} \leq \dfrac{\sin(n)}{n} \leq \dfrac{1}{n}$. En déduire $\lim\limits_{n \to +\infty} \dfrac{\sin(n)}{n}$.

**Exercice 44.6.** Une suite $(u_n)$ vérifie pour tout $n \in \mathbb{N}$ : $u_n \geq 3n^2 - 10n$. Déterminer sa limite en $+\infty$.

**Exercice 44.7.** Une population d'oiseaux compte initialement 500 individus et décroît de 5 % par an.
1. Exprimer la population $P_n$ au bout de $n$ années.
2. Quelle est la limite de $P_n$ quand $n \to +\infty$ ?

**Exercice 44.8.** Écrire en Python une fonction `seuil_geometrique(q, A)` qui prend en entrée une raison $q > 1$ et un seuil $A > 0$, et renvoie le premier rang $n$ tel que $q^n > A$.

---

#### Niveau ★★ (Réflexion et type Bac)

**Exercice 44.9 (Levée d'indéterminations avec racines).**
Soit $u_n = \sqrt{n+1} - \sqrt{n}$ pour $n \geq 0$.
1. Montrer qu'il s'agit d'une forme indéterminée en l'état.
2. En multipliant par l'expression conjuguée, montrer que $u_n = \dfrac{1}{\sqrt{n+1} + \sqrt{n}}$.
3. En déduire la limite de $(u_n)$.

**Exercice 44.10 (Type Bac : Étude complète d'une suite récurrente).**
On considère la suite $(u_n)$ définie par $u_0 = 1$ et pour tout $n \in \mathbb{N}$ :
$$u_{n+1} = \frac{2u_n + 3}{u_n + 2}.$$
1. Démontrer par récurrence que pour tout $n \in \mathbb{N}$, $1 \leq u_n \leq \sqrt{3}$.
2. Démontrer que pour tout $n \in \mathbb{N}$, $u_{n+1} - u_n = \dfrac{3 - u_n^2}{u_n + 2}$. En déduire le sens de variation de la suite $(u_n)$.
3. Justifier que la suite $(u_n)$ converge et déterminer sa limite exacte.

**Exercice 44.11 (Suite arithmético-géométrique et placement bancaire).**
Un capital de $10\,000$ € est placé à intérêts composés au taux annuel de 3 %. Chaque année, le titulaire dépose $500$ € supplémentaires immédiatement après le calcul des intérêts. On note $C_n$ le capital au bout de $n$ années ($C_0 = 10\,000$).
1. Exprimer $C_{n+1}$ en fonction de $C_n$.
2. On pose $v_n = C_n + \alpha$. Déterminer le réel $\alpha$ pour que $(v_n)$ soit une suite géométrique.
3. En déduire l'expression explicite de $C_n$ en fonction de $n$, puis déterminer $\lim\limits_{n \to +\infty} C_n$.

**Exercice 44.12 (Gendarmes et somme finie).**
Soit la suite $(S_n)$ définie pour tout entier $n \geq 1$ par :
$$S_n = \sum_{k=1}^n \frac{n}{n^2 + k} = \frac{n}{n^2 + 1} + \frac{n}{n^2 + 2} + \dots + \frac{n}{n^2 + n}.$$
1. Montrer que pour tout $k \in \{1 ; 2 ; \dots ; n\}$, on a $\dfrac{n}{n^2 + n} \leq \dfrac{n}{n^2 + k} \leq \dfrac{n}{n^2 + 1}$.
2. En déduire que pour tout $n \geq 1$ : $\dfrac{n^2}{n^2 + n} \leq S_n \leq \dfrac{n^2}{n^2 + 1}$.
3. En déduire la convergence de $(S_n)$ et sa limite.

**Exercice 44.13 (Vrai ou Faux avec justifications).**
Pour chacune des affirmations suivantes, préciser si elle est vraie ou fausse en apportant une preuve ou un contre-exemple précis :
1. « Si une suite converge, alors elle est bornée. »
2. « Si une suite est bornée, alors elle converge. »
3. « Si pour tout $n \in \mathbb{N}$, $u_n > 0$ et si $(u_n)$ converge vers $L$, alors $L > 0$. »
4. « Si $\lim\limits_{n \to +\infty} u_n^2 = 4$, alors $\lim\limits_{n \to +\infty} u_n = 2$. »

**Exercice 44.14 (Somme géométrique et paradoxe du coureur).**
Un coureur parcourt successivement $100\text{ m}$, puis $50\text{ m}$, puis $25\text{ m}$, et à chaque étape la moitié de l'étape précédente.
1. Calculer la distance totale parcourue après $n$ étapes.
2. Démontrer rigoureusement que la distance totale ne dépassera jamais $200\text{ m}$, quel que soit le nombre d'étapes franchies.

**Exercice 44.15 (Inégalité de Bernoulli et minoration).**
On considère la suite $u_n = 1{,}01^n$.
1. Grâce à l'inégalité de Bernoulli, donner une minoration affine de $u_n$.
2. En déduire un entier $N$ tel que pour tout $n \geq N$, $u_n \geq 1\,000\,000$.
3. Est-ce le plus petit entier qui convient ?

**Exercice 44.16 (Algorithme de seuil et temps d'arrêt).**
On considère la suite $(u_n)$ définie par $u_0 = 2$ et $u_{n+1} = 0{,}8 u_n + 1$.
1. Conjecturer la limite $L$ de $(u_n)$.
2. Écrire un script Python permettant de trouver le plus petit entier $n$ tel que $|u_n - L| < 10^{-5}$.

**Exercice 44.17 (Étude d'une suite auxiliaire géométrique).**
Soit $(u_n)$ définie par $u_0 = 4$ et $u_{n+1} = \dfrac{u_n}{2u_n + 1}$.
1. Calculer $u_1$ et $u_2$.
2. On admet que $u_n > 0$ pour tout $n$. On pose $v_n = \dfrac{1}{u_n}$. Montrer que $(v_n)$ est arithmétique.
3. En déduire l'expression de $v_n$, puis celle de $u_n$ en fonction de $n$, et déterminer sa limite.

---

#### Niveau ★★★ (Défi et approfondissement)

**Exercice 44.18 (La constante $e$ comme limite d'une suite).**
On considère les deux suites $(u_n)$ et $(v_n)$ définies pour tout $n \geq 1$ par :
$$u_n = \left(1 + \frac{1}{n}\right)^n \quad \text{et} \quad v_n = \left(1 + \frac{1}{n}\right)^{n+1}.$$
1. En calculant les premières valeurs à la calculatrice, conjecturer le comportement de $(u_n)$ et $(v_n)$.
2. On admet que $(u_n)$ est strictement croissante et que $(v_n)$ est strictement décroissante avec $u_n < v_n$. Démontrer que $\lim\limits_{n \to +\infty} (v_n - u_n) = 0$.
3. Que peut-on en déduire pour les deux suites ? (Elles convergent vers le nombre d'Euler $e \approx 2{,}71828$).

**Exercice 44.19 (La suite des moyennes arithmético-géométriques de Gauss).**
Soient $a_0 > 0$ et $b_0 > 0$ avec $a_0 < b_0$. On définit pour tout $n \in \mathbb{N}$ :
$$a_{n+1} = \sqrt{a_n b_n} \quad \text{et} \quad b_{n+1} = \frac{a_n + b_n}{2}.$$
1. Rappeler pourquoi pour tous réels strictement positifs $a$ et $b$, on a $\sqrt{ab} \leq \frac{a+b}{2}$.
2. Démontrer que pour tout $n \geq 1$, $a_n \leq b_n$.
3. Montrer que la suite $(a_n)$ est croissante et que la suite $(b_n)$ est décroissante.
4. En déduire que les deux suites convergent vers une même limite commune (la moyenne arithmético-géométrique de Gauss).

**Exercice 44.20 (Le flocon de Koch : périmètre infini et aire finie).**
Le flocon de Koch se construit par étapes à partir d'un triangle équilatéral de côté 1 et d'aire $A_0 = \frac{\sqrt{3}}{4}$. À chaque étape, on remplace le tiers central de chaque côté par un triangle équilatéral vers l'extérieur.
1. Le périmètre à l'étape $n$ est donné par $P_n = 3 \times \left(\frac{4}{3}\right)^n$. Quelle est la limite de $P_n$ ?
2. L'aire à l'étape $n$ vérifie $A_n = A_0 \left[1 + \frac{3}{5}\left(1 - \left(\frac{4}{9}\right)^n\right)\right]$. Calculer $\lim\limits_{n \to +\infty} A_n$.
3. Commenter le résultat géométrique paradoxal (une figure de frontière infinie emprisonnant une surface finie).

**Exercice 44.21 (Théorème de Césaro — Hors-programme / Olympiades).**
Soit $(u_n)$ une suite convergeant vers une limite finie $L$. On définit la suite des moyennes $(c_n)_{n \geq 1}$ par :
$$c_n = \frac{u_1 + u_2 + \dots + u_n}{n}.$$
1. Tester ce résultat sur la suite $u_n = 1 + \frac{1}{n}$.
2. Donner un exemple montrant que la réciproque est fausse (trouver une suite $(u_n)$ qui ne converge pas, mais dont la moyenne de Césaro $(c_n)$ converge).

**Exercice 44.22 (Théorème du point fixe pour les suites).**
Soit $f$ une fonction continue sur $[0 ; 1]$ telle que pour tout $x \in [0 ; 1]$, $f(x) \in [0 ; 1]$.
On suppose de plus qu'il existe une constante $k \in ]0 ; 1[$ telle que pour tous $x, y \in [0 ; 1]$ :
$$|f(x) - f(y)| \leq k |x - y|.$$
Soit $u_0 \in [0 ; 1]$ et $u_{n+1} = f(u_n)$.
1. Montrer que pour tout $n \in \mathbb{N}$, $|u_{n+1} - u_n| \leq k^n |u_1 - u_0|$.
2. Démontrer que la suite $(u_n)$ converge vers l'unique solution de $f(x) = x$ dans $[0 ; 1]$.

---

### Solutions

#### Solutions du Niveau ★

- **44.1 :**
  1. $\lim u_n = 4 - 0 + 0 = 4$.
  2. $\lim v_n = -\infty$ car $n^3 \to +\infty$ et $-3 < 0$.
  3. $0 < 0{,}4 < 1$ donc $\lim 0{,}4^n = 0$, d'où $\lim w_n = 0$.
  4. $1{,}05 > 1$ donc $\lim 1{,}05^n = +\infty$, d'où $\lim t_n = +\infty$.

- **44.2 :**
  1. Converge vers 0 car $|-3/4| = 3/4 < 1$.
  2. Diverge vers $+\infty$ car $7/5 > 1$.
  3. Diverge sans limite car $-1{,}2 \leq -1$ (oscille avec une amplitude croissante).
  4. $d_n = (4/3)^n$ avec $4/3 > 1$, donc diverge vers $+\infty$.

- **44.3 :**
  1. Factorisation : $u_n = \dfrac{n(3 + 1/n)}{n(5 - 2/n)} = \dfrac{3 + 1/n}{5 - 2/n} \to \dfrac{3}{5}$.
  2. $v_n = \dfrac{n^2(7 - 4/n^2)}{n^3(2 + 1/n^2)} = \dfrac{1}{n} \times \dfrac{7 - 4/n^2}{2 + 1/n^2} \to 0 \times \dfrac{7}{2} = 0$.
  3. $w_n = \dfrac{n^4(1 - 1/n^4)}{n^3(100 + 5/n^3)} = n \times \dfrac{1 - 1/n^4}{100 + 5/n^3} \to +\infty$.

- **44.4 :** On veut $4{,}999 < 5 + \dfrac{1}{n} < 5{,}001 \iff 0 < \dfrac{1}{n} < 0{,}001 = \dfrac{1}{1000} \iff n > 1000$. Le rang minimal est $N = 1001$.

- **44.5 :** Pour tout $n \geq 1$, $-1 \leq \sin(n) \leq 1$. En divisant par $n > 0$, $\dfrac{-1}{n} \leq \dfrac{\sin(n)}{n} \leq \dfrac{1}{n}$. Comme $\lim (-1/n) = \lim (1/n) = 0$, d'après le théorème des gendarmes, $\lim\limits_{n \to +\infty} \dfrac{\sin(n)}{n} = 0$.

- **44.6 :** Pour $n \geq 4$, $3n^2 - 10n = n(3n - 10) \to +\infty$. Comme $u_n \geq 3n^2 - 10n$, par comparaison, $\lim u_n = +\infty$.

- **44.7 :**
  1. Décroissance de 5 % correspond à multiplier par $1 - 0{,}05 = 0{,}95$. Donc $P_n = 500 \times 0{,}95^n$.
  2. Comme $0 < 0{,}95 < 1$, $\lim 0{,}95^n = 0$, donc $\lim P_n = 0$ (extinction théorique de la population).

- **44.8 :**
```python
def seuil_geometrique(q, A):
    n = 0
    u = 1.0
    while u <= A:
        n += 1
        u = q ** n
    return n
```

---

#### Solutions du Niveau ★★

- **44.9 :**
  1. $\lim \sqrt{n+1} = +\infty$ et $\lim \sqrt{n} = +\infty$, donc c'est une F.I. « $\infty - \infty$ ».
  2. Pour $n \geq 0$ :
     $$\sqrt{n+1} - \sqrt{n} = \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} = \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}}.$$
  3. Le dénominateur tend vers $+\infty$, donc par quotient de limite, $\lim u_n = 0$.

- **44.10 :**
  1. *Initialisation :* $n = 0$, $u_0 = 1 \in [1 ; \sqrt{3}]$ car $\sqrt{3} \approx 1{,}732$.
     *Hérédité :* Supposons $1 \leq u_n \leq \sqrt{3}$.
     La fonction $f(x) = \frac{2x+3}{x+2} = 2 - \frac{1}{x+2}$ est strictement croissante sur $[1 ; \sqrt{3}]$.
     Donc $f(1) \leq f(u_n) \leq f(\sqrt{3})$.
     Or $f(1) = 5/3 \approx 1{,}67 \geq 1$.
     Et $f(\sqrt{3}) = \frac{2\sqrt{3}+3}{\sqrt{3}+2} = \frac{\sqrt{3}(2+\sqrt{3})}{\sqrt{3}+2} = \sqrt{3}$.
     Ainsi $1 \leq u_{n+1} \leq \sqrt{3}$.
     *Conclusion :* Pour tout $n \in \mathbb{N}$, $1 \leq u_n \leq \sqrt{3}$.
  2. $u_{n+1} - u_n = \frac{2u_n+3}{u_n+2} - u_n = \frac{2u_n+3 - u_n(u_n+2)}{u_n+2} = \frac{3 - u_n^2}{u_n+2}$.
     Comme $u_n \leq \sqrt{3}$, on a $u_n^2 \leq 3$, donc $3 - u_n^2 \geq 0$. Comme $u_n \geq 1$, $u_n+2 > 0$.
     Donc $u_{n+1} - u_n \geq 0$ : la suite est croissante.
  3. La suite est croissante et majorée par $\sqrt{3}$, donc elle converge vers une limite $L \in [1 ; \sqrt{3}]$.
     En passant à la limite : $L = \frac{2L+3}{L+2} \iff L(L+2) = 2L+3 \iff L^2 = 3$.
     Comme $L \geq 1$, on a $L = \sqrt{3}$.

- **44.11 :**
  1. Augmenter de 3 % puis ajouter 500 donne : $C_{n+1} = 1{,}03 C_n + 500$.
  2. $v_{n+1} = C_{n+1} + \alpha = 1{,}03 C_n + 500 + \alpha$. On veut $v_{n+1} = 1{,}03 v_n = 1{,}03(C_n + \alpha) = 1{,}03 C_n + 1{,}03 \alpha$.
     On identifie : $500 + \alpha = 1{,}03 \alpha \iff 0{,}03 \alpha = 500 \iff \alpha = \frac{500}{0{,}03} = \frac{50\,000}{3}$.
  3. $(v_n)$ est une suite géométrique de raison $q = 1{,}03$ et de premier terme $v_0 = C_0 + \frac{50\,000}{3} = 10\,000 + \frac{50\,000}{3} = \frac{80\,000}{3}$.
     Donc $v_n = \frac{80\,000}{3} \times 1{,}03^n$, d'où $C_n = v_n - \alpha = \frac{80\,000}{3} \times 1{,}03^n - \frac{50\,000}{3}$.
     Comme $1{,}03 > 1$, $\lim 1{,}03^n = +\infty$, donc $\lim C_n = +\infty$.

- **44.12 :**
  1. Pour $1 \leq k \leq n$, on a $n^2 + 1 \leq n^2 + k \leq n^2 + n$. Par inversion de nombres strictement positifs : $\frac{1}{n^2 + n} \leq \frac{1}{n^2 + k} \leq \frac{1}{n^2 + 1}$. En multipliant par $n > 0$, on obtient l'inégalité demandée.
  2. En sommant ces inégalités pour $k$ allant de 1 à $n$, la somme comporte $n$ termes :
     $n \times \frac{n}{n^2 + n} \leq S_n \leq n \times \frac{n}{n^2 + 1} \iff \frac{n^2}{n^2 + n} \leq S_n \leq \frac{n^2}{n^2 + 1}$.
  3. $\lim \frac{n^2}{n^2+n} = \lim \frac{n^2}{n^2(1+1/n)} = 1$ et $\lim \frac{n^2}{n^2+1} = 1$. Par le théorème des gendarmes, $\lim S_n = 1$.

- **44.13 :**
  1. **Vrai.** Si $u_n \to L$, à partir d'un rang $N$, tous les termes sont dans $]L-1 ; L+1[$. Les termes précédents $u_0, \dots, u_{N-1}$ étant en nombre fini, on prend le minimum et le maximum de l'ensemble fini $\{u_0, \dots, u_{N-1}, L-1, L+1\}$, ce qui borne toute la suite.
  2. **Faux.** Contre-exemple : $u_n = (-1)^n$ est bornée entre $-1$ et $1$, mais ne converge pas.
  3. **Faux.** Contre-exemple : $u_n = \frac{1}{n+1} > 0$ pour tout $n \in \mathbb{N}$, mais $\lim u_n = 0$ (qui n'est pas strictement positif). Le passage à la limite transforme les inégalités strictes en inégalités larges.
  4. **Faux.** Contre-exemple : $u_n = 2 \times (-1)^n$. Alors $u_n^2 = 4$ pour tout $n$, donc $\lim u_n^2 = 4$, mais $(u_n)$ oscille entre $2$ et $-2$ et n'a aucune limite.

- **44.14 :**
  1. Distance à l'étape $n$ : $D_n = 100 \sum_{k=0}^{n-1} \left(\frac{1}{2}\right)^k = 100 \times \frac{1 - (1/2)^n}{1 - 1/2} = 200 \left(1 - \frac{1}{2^n}\right)$.
  2. Pour tout $n \geq 1$, $\frac{1}{2^n} > 0$, donc $1 - \frac{1}{2^n} < 1$, ce qui implique $D_n < 200$. De plus $\lim D_n = 200\text{ m}$. La distance tend vers $200\text{ m}$ sans jamais la dépasser pour un $n$ fini.

- **44.15 :**
  1. Avec $a = 0{,}01$, Bernoulli donne : $1{,}01^n = (1 + 0{,}01)^n \geq 1 + 0{,}01n$.
  2. On cherche $1 + 0{,}01n \geq 1\,000\,000 \iff 0{,}01n \geq 999\,999 \iff n \geq 99\,999\,900$. Le rang $N = 99\,999\,900$ convient à coup sûr.
  3. Non, ce n'est pas le plus petit : la puissance grandit beaucoup plus vite que la droite affine. Le vrai seuil (calculable avec le logarithme au chapitre 48) est $n = \lceil \frac{\ln(10^6)}{\ln(1{,}01)} \rceil = 1388$.

- **44.16 :**
  1. Si $u_n \to L$, alors $L = 0{,}8 L + 1 \iff 0{,}2 L = 1 \iff L = 5$.
  2. Script Python :
```python
n = 0
u = 2.0
while abs(u - 5.0) >= 1e-5:
    n += 1
    u = 0.8 * u + 1.0
print(f"Rang n trouvé : {n}")
```

- **44.17 :**
  1. $u_1 = \frac{4}{2(4)+1} = \frac{4}{9}$. $u_2 = \frac{4/9}{2(4/9)+1} = \frac{4/9}{17/9} = \frac{4}{17}$.
  2. $v_{n+1} = \frac{1}{u_{n+1}} = \frac{2u_n+1}{u_n} = 2 + \frac{1}{u_n} = v_n + 2$. $(v_n)$ est donc une suite arithmétique de raison $r = 2$ et de premier terme $v_0 = \frac{1}{u_0} = \frac{1}{4}$.
  3. $v_n = \frac{1}{4} + 2n = \frac{8n+1}{4}$. Par inversion : $u_n = \frac{1}{v_n} = \frac{4}{8n+1}$.
     On en déduit immédiatement : $\lim\limits_{n \to +\infty} u_n = 0$.

---

#### Solutions du Niveau ★★★

- **44.18 :**
  1. Pour $n = 10$, $u_{10} \approx 2{,}5937$, $v_{10} \approx 2{,}8531$. Pour $n = 1000$, $u_{1000} \approx 2{,}7169$, $v_{1000} \approx 2{,}7196$. Les deux semblent se resserrer autour de $2{,}718...$
  2. $v_n - u_n = \left(1 + \frac{1}{n}\right)^n \left(1 + \frac{1}{n} - 1\right) = \frac{1}{n} u_n$. Comme $u_n < v_n \leq v_1 = 4$, la suite $(u_n)$ est bornée par 4. Donc $0 < v_n - u_n \leq \frac{4}{n}$. Par les gendarmes, $\lim (v_n - u_n) = 0$.
  3. L'une est croissante, l'autre décroissante, et leur différence tend vers 0 : ce sont deux suites dites **adjacentes**. Elles convergent vers une même limite commune, qui définit le nombre $e \approx 2{,}71828$.

- **44.19 :**
  1. $(\sqrt{a} - \sqrt{b})^2 \geq 0 \iff a - 2\sqrt{ab} + b \geq 0 \iff \frac{a+b}{2} \geq \sqrt{ab}$ (inégalité arithmético-géométrique).
  2. Pour $n \geq 0$, $b_{n+1} - a_{n+1} = \frac{a_n+b_n}{2} - \sqrt{a_n b_n} \geq 0$, donc $a_{n+1} \leq b_{n+1}$ pour tout $n \geq 0$.
  3. $a_{n+1} - a_n = \sqrt{a_n b_n} - a_n = \sqrt{a_n}(\sqrt{b_n} - \sqrt{a_n}) \geq 0$ car $b_n \geq a_n$. Donc $(a_n)$ est croissante.
     De même, $b_{n+1} - b_n = \frac{a_n - b_n}{2} \leq 0$, donc $(b_n)$ est décroissante.
  4. $(a_n)$ est croissante et majorée par $b_0$, donc elle converge vers $L_a$. $(b_n)$ est décroissante et minorée par $a_0$, donc converge vers $L_b$.
     En passant à la limite dans $b_{n+1} = \frac{a_n+b_n}{2}$, on a $L_b = \frac{L_a+L_b}{2} \iff L_a = L_b$. Les deux suites convergent vers la même valeur, notée $M(a_0, b_0)$.

- **44.20 :**
  1. Comme $\frac{4}{3} > 1$, $\lim\limits_{n \to +\infty} \left(\frac{4}{3}\right)^n = +\infty$, donc le périmètre $P_n$ tend vers $+\infty$.
  2. Comme $0 < \frac{4}{9} < 1$, $\lim \left(\frac{4}{9}\right)^n = 0$.
     Donc $\lim A_n = A_0 \left(1 + \frac{3}{5}(1 - 0)\right) = A_0 \left(1 + \frac{3}{5}\right) = \frac{8}{5} A_0 = \frac{8}{5} \times \frac{\sqrt{3}}{4} = \frac{2\sqrt{3}}{5}$.
  3. Le flocon de Koch possède un périmètre infini tout en enfermant une aire finie strictement bornée. Il montre que la géométrie fractale brise l'intuition euclidienne usuelle.

- **44.21 :**
  1. $u_n \to 1$. $c_n = \frac{1}{n} \sum_{k=1}^n \left(1 + \frac{1}{k}\right) = 1 + \frac{1}{n}\sum_{k=1}^n \frac{1}{k}$. Or la somme harmonique $H_n = \sum_{k=1}^n \frac{1}{k}$ croît comme $\ln(n)$, donc $\frac{H_n}{n} \to 0$. Ainsi $c_n \to 1$.
  2. Prenons $u_n = (-1)^n$. La suite $(u_n)$ oscille et diverge.
     Mais $S_n = u_1 + \dots + u_n$ vaut $-1$ si $n$ est impair et $0$ si $n$ est pair.
     Donc $-\frac{1}{n} \leq c_n \leq 0$, ce qui implique par les gendarmes que $\lim c_n = 0$. La moyenne de Césaro converge vers 0 alors que $(u_n)$ diverge !

- **44.22 :**
  1. Par récurrence : pour $n = 0$, $|u_1 - u_0| \leq k^0 |u_1 - u_0|$ est vrai.
     Supposons $|u_{n+1} - u_n| \leq k^n |u_1 - u_0|$.
     Alors $|u_{n+2} - u_{n+1}| = |f(u_{n+1}) - f(u_n)| \leq k |u_{n+1} - u_n| \leq k \times k^n |u_1 - u_0| = k^{n+1} |u_1 - u_0|$.
  2. Puisque $0 < k < 1$, $\lim k^n = 0$. Les pas $|u_{n+1} - u_n|$ deviennent infiniment petits de façon géométrique. La suite est une suite de Cauchy dans un intervalle fermé borné, donc elle converge vers un réel $L \in [0 ; 1]$. Par continuité de $f$, $\lim f(u_n) = f(L)$, d'où $L = f(L)$. L'unicité découle de ce que si $f(x)=x$ et $f(y)=y$, $|x - y| = |f(x) - f(y)| \leq k |x - y| \implies (1 - k)|x - y| \leq 0$, ce qui impose $x = y$ car $1 - k > 0$.

---

### La question qui ouvre la suite

Jusqu'ici, notre compteur $n$ était un entier naturel qui sautait de marche en marche : $n = 0, 1, 2, 3...$
Mais que se passe-t-il si la variable n'est plus un coureur à pas discrets, mais un oiseau qui vole de façon parfaitement continue dans le ciel, ou une fusée qui accélère à chaque microseconde ?
Comment définir la limite d'une fonction $f(x)$ quand la variable réelle $x$ glisse de manière continue vers l'infini, ou pire, quand elle s'approche d'un point où la fonction semble se déchirer ou exploser ?

C'est le mystère des limites de fonctions et des lignes invisibles qui guident les courbes dans l'espace : **les asymptotes**. Rendez-vous au chapitre 45.
