# VOLUME VI — L'Âge du Flux et de la Vitesse (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 48 : Le Logarithme de Napier et les Tables des Navigateurs

> *« En abrégeant les calculs, l'invention des logarithmes a doublé la vie des astronomes. »*
> — Pierre-Simon de Laplace

---

### Ce que tu vas découvrir

- Pourquoi, vers 1600, les marins et les astronomes étouffaient sous les **multiplications**, et comment un baron écossais a inventé une machine à transformer les multiplications en **additions**.
- La **fonction logarithme népérien** $\ln$, définie comme la machine qui **défait** l'exponentielle : $y = e^x \iff x = \ln y$.
- Les **propriétés algébriques** ($\ln(ab) = \ln a + \ln b$, etc.) et leurs **démonstrations**.
- L'**étude complète** de la fonction : dérivée $\frac{1}{x}$, variations, limites, croissances comparées, concavité.
- Les méthodes pour résoudre **équations et inéquations** avec $\ln$ et $e$, et pour trouver un **seuil** dans une suite géométrique.
- Les **échelles logarithmiques** du monde réel : pH, décibels, magnitude des séismes, datation au carbone 14.

---

### 1. Le problème : la mer, les étoiles et les multiplications interminables

#### 1.1 Le navigateur perdu

Imagine-toi en **1600**, sur le pont d'un galion qui traverse l'Atlantique. Il n'y a ni GPS, ni radio, ni horloge fiable. Pour savoir où se trouve le navire, le pilote mesure au **quadrant** la hauteur du Soleil ou d'une étoile au-dessus de l'horizon, puis il doit résoudre un **triangle sphérique** : un triangle tracé sur la sphère céleste.

Les formules de trigonométrie sphérique ressemblent à ceci :
$$\cos a = \cos b \cos c + \sin b \sin c \cos A.$$

Les sinus et cosinus, on les lit dans des **tables** imprimées, avec sept ou huit chiffres pour être précis. Il faut donc multiplier, à la main, des nombres comme
$$0{,}8746197 \times 0{,}4848096.$$

Une telle multiplication posée demande une cinquantaine de petites multiplications et additions, avec des retenues partout. Une seule erreur de retenue, et le navire se croit à cent kilomètres de sa vraie position : il peut s'échouer sur des récifs. Les astronomes, eux, comme **Tycho Brahe** puis **Johannes Kepler**, passent des **années** de leur vie à faire des multiplications pour calculer les orbites des planètes.

> **💡 Le savais-tu ?** Avant les logarithmes, on utilisait une astuce appelée **prosthaphérèse** (du grec « ajouter et retrancher »), qui exploitait la formule $\cos a \cos b = \frac{1}{2}\left[\cos(a+b) + \cos(a-b)\right]$ pour remplacer un produit par une somme… mais elle était lourde et ne marchait bien que pour des nombres compris entre $-1$ et $1$.

#### 1.2 Le rêve : remplacer × par +

L'addition est facile : on aligne les chiffres et on ajoute. La multiplication est pénible. D'où le rêve des calculateurs de la Renaissance :

> *Trouver une « traduction » qui associe à chaque nombre positif un autre nombre, de telle sorte que la traduction d'un produit soit la somme des traductions.*

Ce rêve, le moine allemand **Michael Stifel** l'avait entrevu en 1544 en écrivant deux lignes de nombres l'une sous l'autre :

```
 Progression arithmétique :   0    1    2    3    4     5     6      7      8
 Progression géométrique   :   1    2    4    8   16    32    64    128    256
```

Pour multiplier $8 \times 32$, regarde au-dessus : $8$ correspond à $3$, $32$ correspond à $5$. Additionne : $3 + 5 = 8$. Redescends : sous $8$ on lit $256$. Et en effet $8 \times 32 = 256$ ! **La ligne du haut transforme les multiplications de la ligne du bas en additions.**

C'est simplement la règle des puissances que tu connais depuis le collège :
$$2^3 \times 2^5 = 2^{3+5}.$$

Mais il y a un gros problème : entre $8$ et $16$, il n'y a rien. Comment multiplier $11 \times 13$ ? Il faudrait une progression géométrique **aux pas si serrés** que tous les nombres y figurent presque. Il faudrait **remplir les trous**.

#### 1.3 Vingt ans de calcul : le baron de Merchiston

C'est ce que fait **John Napier** (1550 - 1617), baron de Merchiston en Écosse — en français on l'appelle souvent **Neper**. Il choisit une progression géométrique de raison très proche de $1$, à savoir $1 - 10^{-7} = 0{,}9999999$, de sorte que ses termes successifs ne diffèrent presque pas : les trous deviennent minuscules. Pendant **vingt ans**, à la main, il calcule ses tables. En **1614**, il publie *Mirifici Logarithmorum Canonis Descriptio* (« Description de la merveilleuse règle des logarithmes »).

Le mot **logarithme**, qu'il invente, vient du grec *logos* (rapport, raison) et *arithmos* (nombre) : « le nombre qui compte les rapports ». Le logarithme d'un nombre, c'est en quelque sorte **le nombre de pas** qu'il faut faire dans la progression géométrique pour l'atteindre.

> **🔍 L'histoire vraie —** Le mathématicien anglais **Henry Briggs**, lisant le livre de Napier, est si bouleversé qu'il fait le voyage de Londres jusqu'en Écosse en 1615 pour le rencontrer. On raconte que les deux hommes restèrent un quart d'heure à se regarder en silence, d'admiration, avant de parler. Ensemble, ils décident de construire des logarithmes « de base 10 » (où $\log 10 = 1$), plus pratiques pour notre numération : ce sont les **logarithmes décimaux**. Kepler, qui reçoit les tables en 1617, s'en sert immédiatement pour achever ses *Tables rudolphines* des mouvements planétaires et dédie un de ses livres à Napier… sans savoir que celui-ci était mort entre-temps.

Pendant plus de **trois siècles**, des tables de logarithmes et des **règles à calcul** (deux réglettes graduées logarithmiquement qu'on fait glisser l'une contre l'autre pour additionner des longueurs) accompagnent les ingénieurs, les marins, les architectes… jusqu'aux ingénieurs de la NASA du programme Apollo dans les années 1960 !

#### 1.4 Le même problème, vu du laboratoire

Rappelle-toi la colonie de bactéries du chapitre 40. Une population qui suit la loi $N(t) = N_0 \, e^{kt}$ grossit de façon exponentielle. Le biologiste se pose la question **inverse** :

> *« La population a été multipliée par 1000. Depuis combien de temps l'infection a-t-elle commencé ? »*

Il faut résoudre $e^{kt} = 1000$, c'est-à-dire trouver **l'exposant** qui donne un résultat voulu. L'exponentielle sait aller de l'exposant vers le résultat ; il nous manque la machine qui va **du résultat vers l'exposant**. Cette machine-là, c'est le **logarithme népérien**. Les deux histoires — celle des navigateurs et celle des bactéries — vont se rejoindre.

---

### 2. Définition : la machine qui remonte l'exponentielle

#### 2.1 Ce que l'on sait déjà de l'exponentielle

Rappelons ce que le chapitre 40 et le chapitre 46 nous ont appris sur la fonction $\exp : x \mapsto e^x$ :

- elle est définie, continue et dérivable sur $\mathbb{R}$, avec $(e^x)' = e^x$ ;
- elle est **strictement positive** : $e^x > 0$ pour tout réel $x$ ;
- elle est donc **strictement croissante** sur $\mathbb{R}$ ;
- $\lim\limits_{x \to -\infty} e^x = 0$ et $\lim\limits_{x \to +\infty} e^x = +\infty$.

Le **corollaire du théorème des valeurs intermédiaires** (chapitre 46) affirme alors : une fonction continue et strictement croissante sur un intervalle réalise une **bijection** de cet intervalle sur l'intervalle image. Ici :

> **Pour tout réel $a > 0$, l'équation $e^x = a$ admet une unique solution réelle.**

En image : la courbe de l'exponentielle traverse chaque ligne horizontale $y = a$ (avec $a > 0$) **exactement une fois**. Et elle ne traverse jamais les lignes $y = a$ avec $a \leq 0$, puisqu'elle reste au-dessus de l'axe des abscisses.

```
       y
       ▲                         /  y = e^x
       │                       /
     a ┼ - - - - - - - - - - *      ← un seul point d'intersection
       │                  /  ¦
       │              _-'    ¦
     1 ┼ _ _ _ _ _ _-*       ¦
       │      __--'  ¦       ¦
 ──────┼--''─────────┼───────┼────────► x
       │             0     ln a
   -2 ┼ - - - - - - - - - - - - - - -   ← jamais atteint : pas de solution
```

#### 2.2 La définition

> **📐 Définition —** Pour tout réel $a$ strictement positif, on appelle **logarithme népérien** de $a$, et on note $\ln a$ (ou $\ln(a)$), l'**unique** réel $x$ tel que $e^x = a$.
> La fonction $\ln : \; ]0\,;+\infty[ \; \to \mathbb{R}, \; x \mapsto \ln x$ est la **fonction logarithme népérien**. C'est la **fonction réciproque** de la fonction exponentielle.
> $$\text{Pour } a > 0 \text{ et } x \in \mathbb{R} : \qquad e^x = a \iff x = \ln a.$$

**La notation.** Le symbole $\ln$ est l'abréviation de *logarithmus naturalis* (latin : « logarithme naturel »). On le lit « **logarithme népérien de $x$** », ou plus familièrement « **l-n de $x$** » (en épelant les lettres L et N). Les parenthèses sont facultatives quand il n'y a pas d'ambiguïté : $\ln 2$, $\ln x$ ; mais on écrit $\ln(x+1)$ et surtout pas $\ln x + 1$, qui veut dire $(\ln x) + 1$.

> **💡 Le savais-tu ?** Napier n'a pas écrit $\ln$, ni même pensé en termes de fonction réciproque de $e^x$ : le nombre $e$ n'avait pas encore de nom ! Ce sont **Grégoire de Saint-Vincent** et **Alphonse de Sarasa** (vers 1647-1649) qui ont remarqué que l'aire sous l'hyperbole $y = \frac{1}{x}$ se comporte comme un logarithme (on le verra au chapitre 50), et c'est **Leonhard Euler**, en 1748, qui présente clairement logarithme et exponentielle comme deux machines inverses l'une de l'autre. Les tables originales de Napier correspondent, à peu près, à la fonction $x \mapsto 10^7 \ln\left(\frac{10^7}{x}\right)$.

#### 2.3 Premières conséquences immédiates

De la définition découlent directement :

| Propriété | Pourquoi |
|---|---|
| $\ln 1 = 0$ | car $e^0 = 1$ |
| $\ln e = 1$ | car $e^1 = e$ |
| $e^{\ln a} = a$ pour tout $a > 0$ | $\ln a$ est *par définition* l'exposant qui donne $a$ |
| $\ln(e^x) = x$ pour tout $x \in \mathbb{R}$ | l'unique exposant qui donne $e^x$, c'est $x$ |

Les deux dernières lignes disent : **« exp » puis « ln », ou « ln » puis « exp », on revient au point de départ.** C'est comme fermer puis ouvrir un tiroir.

> **⚠️ Attention, piège !** $e^{\ln a} = a$ n'est vrai que si $a > 0$. Par exemple $e^{\ln(-3)}$ n'a **aucun sens**, car $\ln(-3)$ n'existe pas. En revanche $\ln(e^x) = x$ est vrai pour **tout** réel $x$, même négatif : $\ln(e^{-5}) = -5$.

#### 2.4 La courbe : un miroir de l'exponentielle

Dans un repère orthonormé, si le point $M(a\,;b)$ est sur la courbe de $\exp$ (donc $b = e^a$), alors $a = \ln b$ et le point $M'(b\,;a)$ est sur la courbe de $\ln$. Or $M'$ est le **symétrique** de $M$ par rapport à la droite $\Delta$ d'équation $y = x$ (on échange abscisse et ordonnée).

> **Les courbes de $\exp$ et de $\ln$ sont symétriques l'une de l'autre par rapport à la première bissectrice $y = x$.**

```
        y
        ▲            exp          y = x
        │             /          /
        │            /         /
        │           /        /
        │          /       /          ___---- ln
      e ┼         /      /     __---''
        │        /     /  _--''
      1 ┼ _ _ _ * _  /_-*'                 (e ; 1)
        │    _-'   /-'  ¦
        │_--'   _/'¦    ¦
   ─────┼─────/────*────┼──────────────────► x
        │   /      1    e
        │  /
        │ /   ← ln plonge vers -∞ quand x → 0⁺
        │/
```

Imagine que tu replies la feuille le long de la diagonale $y = x$ : la courbe de l'exponentielle se dépose exactement sur celle du logarithme. Le point $(0\,;1)$ de $\exp$ devient le point $(1\,;0)$ de $\ln$ ; l'asymptote horizontale $y = 0$ de $\exp$ (en $-\infty$) devient l'**asymptote verticale** $x = 0$ de $\ln$.

#### 2.5 Exemples résolus

> **Exemple résolu 1 — Résoudre $e^x = 5$.**
> $5 > 0$, donc l'équation a une unique solution : $x = \ln 5 \approx 1{,}609$.
> Vérification à la calculatrice : $e^{1{,}609} \approx 4{,}998$. ✔

> **Exemple résolu 2 — Résoudre $e^{2x-1} = 3$.**
> $3 > 0$, donc $e^{2x-1} = 3 \iff 2x - 1 = \ln 3 \iff x = \dfrac{1 + \ln 3}{2}$.
> $\mathcal{S} = \left\{ \dfrac{1+\ln 3}{2} \right\}$, soit environ $1{,}049$.

> **Exemple résolu 3 — Résoudre $\ln x = 2$.**
> L'équation n'a de sens que pour $x > 0$. Alors $\ln x = 2 \iff x = e^2$. Comme $e^2 > 0$, la solution est valable : $\mathcal{S} = \{e^2\}$, avec $e^2 \approx 7{,}389$.

> **Exemple résolu 4 — Résoudre $e^{x} = -4$ et $3e^{x} + 6 = 0$.**
> Une exponentielle est toujours strictement positive : $e^x = -4$ n'a **aucune solution**, $\mathcal{S} = \varnothing$.
> De même $3e^x + 6 = 0 \iff e^x = -2$ : $\mathcal{S} = \varnothing$. Écrire « $x = \ln(-2)$ » serait une faute grave.

> **Exemple résolu 5 — Simplifier $A = e^{\ln 7}$, $B = \ln(e^{-3})$, $C = e^{-\ln 2}$, $D = \ln\left(\sqrt{e}\right)$.**
> - $A = 7$ ;
> - $B = -3$ ;
> - $C = \dfrac{1}{e^{\ln 2}} = \dfrac{1}{2}$ ;
> - $D = \ln\left(e^{1/2}\right) = \dfrac{1}{2}$.

> **⚠️ Attention, piège ! — Aux limites du domaine.**
> - $\ln 0$ **n'existe pas** : aucune puissance de $e$ ne vaut $0$ (l'exponentielle s'approche de $0$ sans jamais l'atteindre).
> - $\ln$ d'un nombre négatif **n'existe pas** (dans $\mathbb{R}$).
> - Avant toute équation contenant $\ln(\dots)$, on commence donc **toujours** par déterminer l'ensemble des $x$ pour lesquels toutes les expressions à l'intérieur des $\ln$ sont **strictement positives**.

---

### 3. Les propriétés algébriques : le rêve de Napier réalisé

#### 3.1 La propriété fondamentale

> **📐 Propriété fondamentale —** Pour tous réels $a > 0$ et $b > 0$ :
> $$\ln(ab) = \ln a + \ln b.$$

**Ce que ça dit en mots :** le logarithme **transforme les produits en sommes**. C'est exactement la ligne du haut de Stifel, mais sans trous : tous les réels positifs y figurent.

> **✍️ Démonstration (exigible) —** Soient $a > 0$ et $b > 0$. Alors $ab > 0$ et $\ln(ab)$ existe.
> D'une part, $e^{\ln(ab)} = ab$ par définition.
> D'autre part, d'après la propriété $e^{x+y} = e^x e^y$ de l'exponentielle :
> $$e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = a \times b.$$
> Ainsi $e^{\ln(ab)} = e^{\ln a + \ln b}$. Comme la fonction exponentielle est strictement croissante, donc **injective** (deux réels différents ont des images différentes), on en déduit $\ln(ab) = \ln a + \ln b$. $\blacksquare$

Tout le secret est là : **la propriété du logarithme est le reflet de la propriété $e^{x+y} = e^x e^y$ de l'exponentielle**, vue dans le miroir $y = x$.

#### 3.2 Les conséquences

> **📐 Propriétés —** Pour tous réels $a > 0$, $b > 0$ et tout entier relatif $n$ :
> 1. $\ln\left(\dfrac{1}{a}\right) = -\ln a$
> 2. $\ln\left(\dfrac{a}{b}\right) = \ln a - \ln b$
> 3. $\ln(a^n) = n \ln a$
> 4. $\ln\left(\sqrt{a}\right) = \dfrac{1}{2} \ln a$

> **✍️ Démonstrations —**
> 1. $a \times \dfrac{1}{a} = 1$, donc $\ln a + \ln\left(\dfrac{1}{a}\right) = \ln 1 = 0$, d'où $\ln\left(\dfrac1a\right) = -\ln a$.
> 2. $\ln\left(\dfrac ab\right) = \ln\left(a \times \dfrac1b\right) = \ln a + \ln\left(\dfrac1b\right) = \ln a - \ln b$.
> 3. Pour $n \in \mathbb{N}$, on raisonne **par récurrence** (chapitre 43). Soit $P(n)$ : « $\ln(a^n) = n\ln a$ ».
>    - *Initialisation :* $\ln(a^0) = \ln 1 = 0 = 0 \times \ln a$. $P(0)$ est vraie.
>    - *Hérédité :* supposons $P(n)$ vraie pour un entier $n \geq 0$. Alors $\ln(a^{n+1}) = \ln(a^n \times a) = \ln(a^n) + \ln a = n\ln a + \ln a = (n+1)\ln a$. $P(n+1)$ est vraie.
>    - *Conclusion :* $P(n)$ est vraie pour tout $n \in \mathbb{N}$.
>
>    Pour $n$ entier négatif, on écrit $n = -m$ avec $m \in \mathbb{N}$ : $\ln(a^{-m}) = \ln\left(\dfrac{1}{a^m}\right) = -\ln(a^m) = -m \ln a = n \ln a$.
> 4. $\left(\sqrt a\right)^2 = a$, donc $2 \ln\left(\sqrt a\right) = \ln a$ d'après 3., d'où le résultat. $\blacksquare$

> **💡 Le savais-tu ?** Plus généralement, pour $a > 0$ et tout réel $r$, on **définit** $a^r = e^{r \ln a}$, ce qui donne $\ln(a^r) = r \ln a$. C'est ainsi qu'une calculatrice comprend $2^{\sqrt{2}}$ ou $10^{0{,}3}$. En particulier $2^x = e^{x \ln 2}$ : **toute** croissance « à taux constant » est une exponentielle de base $e$ déguisée.

#### 3.3 Exemples résolus

> **Exemple résolu 6 — Exprimer en fonction de $\ln 2$ et $\ln 3$ :**
> $A = \ln 12$, $\quad B = \ln\left(\dfrac{9}{16}\right)$, $\quad C = \ln\sqrt{72}$, $\quad D = 3\ln 4 - 2\ln 6$.
> - $12 = 2^2 \times 3$, donc $A = 2\ln 2 + \ln 3$.
> - $B = \ln(3^2) - \ln(2^4) = 2\ln 3 - 4 \ln 2$.
> - $72 = 2^3 \times 3^2$, donc $C = \dfrac12 (3 \ln 2 + 2 \ln 3) = \dfrac32 \ln 2 + \ln 3$.
> - $D = 3 \times 2\ln 2 - 2(\ln 2 + \ln 3) = 6\ln 2 - 2\ln 2 - 2\ln 3 = 4\ln 2 - 2\ln 3$.

> **Exemple résolu 7 — Simplifier $E = \ln(e^3) + \ln\left(\dfrac{1}{e}\right) - \ln\left(e\sqrt{e}\right)$.**
> $\ln(e^3) = 3$, $\ln\left(\frac1e\right) = -1$, $\ln\left(e \sqrt e\right) = \ln\left(e^{3/2}\right) = \frac32$.
> Donc $E = 3 - 1 - \dfrac32 = \dfrac12$.

> **Exemple résolu 8 — Multiplier comme un navigateur de 1620.**
> On veut $2{,}37 \times 5{,}81$ avec une table de **logarithmes décimaux** ($\log x = \dfrac{\ln x}{\ln 10}$, qui vérifie aussi $\log(ab) = \log a + \log b$ et $\log 10 = 1$).
> La table donne : $\log 2{,}37 \approx 0{,}37475$ et $\log 5{,}81 \approx 0{,}76418$.
> On **additionne** : $0{,}37475 + 0{,}76418 = 1{,}13893$.
> On cherche dans la table le nombre dont le log vaut $1{,}13893 = 1 + 0{,}13893$ : c'est $10 \times 1{,}37697 \approx 13{,}770$.
> Calcul direct : $2{,}37 \times 5{,}81 = 13{,}7697$. ✔ Une addition et deux lectures de table ont remplacé la multiplication !

#### 3.4 Attention, pièges !

> **⚠️ Attention, piège ! — Les fausses formules.**
> - $\ln(a + b) \neq \ln a + \ln b$ en général. Contre-exemple : $\ln(1+1) = \ln 2 \approx 0{,}69$ alors que $\ln 1 + \ln 1 = 0$. Le logarithme transforme les **produits**, pas les sommes.
> - $\ln a \times \ln b \neq \ln(ab)$. Contre-exemple : $\ln e \times \ln e = 1$, mais $\ln(e^2) = 2$.
> - $\dfrac{\ln a}{\ln b} \neq \ln\left(\dfrac ab\right)$ et $\neq \ln a - \ln b$.
> - $(\ln a)^2 \neq \ln(a^2)$. Par exemple avec $a = e^3$ : $(\ln a)^2 = 9$ mais $\ln(a^2) = 6$. Pour éviter toute ambiguïté, on écrit $(\ln x)^2$ ou $\ln^2 x$, jamais $\ln x^2$ pour dire le carré du logarithme.

> **⚠️ Attention, piège ! — Les signes cachés.**
> La formule $\ln(ab) = \ln a + \ln b$ exige $a > 0$ **et** $b > 0$. Or $ab$ peut être positif avec $a < 0$ et $b < 0$ ! Par exemple $\ln\big((-2)(-3)\big) = \ln 6$ existe, mais $\ln(-2) + \ln(-3)$ n'a pas de sens. La version correcte, valable pour $ab > 0$, est
> $$\ln(ab) = \ln|a| + \ln|b|.$$
> De même, pour tout réel $x \neq 0$ : $\ln(x^2) = 2 \ln|x|$ (et non $2\ln x$, qui n'existe que pour $x > 0$).
> Conséquence pratique : les fonctions $x \mapsto \ln(x^2)$ et $x \mapsto 2\ln x$ **ne sont pas égales** : la première est définie sur $\mathbb{R}^*$, la seconde seulement sur $]0\,;+\infty[$.



---

### 4. Étude complète de la fonction logarithme népérien

#### 4.1 Dérivabilité et calcul de la dérivée

> **📐 Théorème —** La fonction $\ln$ est dérivable sur $]0\,;+\infty[$, et pour tout réel $x > 0$ :
> $$\ln'(x) = \dfrac{1}{x}.$$

> **✍️ Démonstration (exigible au baccalauréat) —**
> On sait que pour tout réel $x > 0$, on a la relation :
> $$e^{\ln x} = x.$$
> La fonction $\ln$ est dérivable sur $]0\,;+\infty[$ (car elle est la réciproque de la fonction $\exp$, dérivable sur $\mathbb{R}$ et de dérivée $\exp' = \exp$ strictement positive sur $\mathbb{R}$).
> En dérivant les deux membres de l'égalité $e^{\ln x} = x$ par rapport à $x$, à l'aide de la formule de dérivation d'une fonction composée $(e^{u(x)})' = u'(x)\, e^{u(x)}$ avec $u(x) = \ln x$ :
> $$(\ln)'(x) \times e^{\ln x} = 1.$$
> Or $e^{\ln x} = x$, donc :
> $$(\ln)'(x) \times x = 1 \iff \ln'(x) = \dfrac{1}{x}.$$
> $\blacksquare$

> **💡 Démonstration alternative par le taux d'accroissement —**
> Soit $x > 0$ fixé et soit $h \neq 0$ tel que $x+h > 0$. Le taux d'accroissement de $\ln$ en $x$ s'écrit :
> $$\tau(h) = \dfrac{\ln(x+h) - \ln x}{h} = \dfrac{1}{h} \ln\left(1 + \dfrac{h}{x}\right).$$
> Posons $u = \ln\left(1 + \dfrac{h}{x}\right)$. Alors $e^u = 1 + \dfrac{h}{x}$, d'où $h = x(e^u - 1)$.
> Lorsque $h \to 0$, $1 + \dfrac{h}{x} \to 1$, donc $u \to \ln 1 = 0$ par continuité de $\ln$.
> Le taux devient :
> $$\tau(h) = \dfrac{u}{x(e^u - 1)} = \dfrac{1}{x} \times \dfrac{1}{\dfrac{e^u - 1}{u}}.$$
> Or, par définition de la dérivée de l'exponentielle en $0$, $\lim\limits_{u \to 0} \dfrac{e^u - 1}{u} = \exp'(0) = e^0 = 1$.
> Ainsi, par quotient de limites :
> $$\lim_{h \to 0} \tau(h) = \dfrac{1}{x} \times \dfrac{1}{1} = \dfrac{1}{x}.$$
> On retrouve bien $\ln'(x) = \dfrac{1}{x}$. $\blacksquare$

#### 4.2 Dérivée de $\ln(u)$ et $\ln|u|$

Lorsque l'argument du logarithme est lui-même une fonction dérivable $u$, la formule de dérivation des fonctions composées $(f \circ u)' = u' \times (f' \circ u)$ donne immédiatement :

> **📐 Règle de dérivation en chaîne —**
> Soit $u$ une fonction dérivable et **strictement positive** sur un intervalle $I$. Alors la fonction $f = \ln \circ u$, définie par $f(x) = \ln(u(x))$, est dérivable sur $I$, et :
> $$(\ln(u))' = \dfrac{u'}{u}.$$
> Plus généralement, si $u$ est dérivable et **ne s'annule pas** sur $I$, la fonction $x \mapsto \ln|u(x)|$ est dérivable sur $I$ et :
> $$(\ln|u|)' = \dfrac{u'}{u}.$$

> **✍️ Justification pour $\ln|u|$ quand $u(x) < 0$ —**
> Si $u(x) < 0$, alors $|u(x)| = -u(x) > 0$. On a donc $\ln|u(x)| = \ln(-u(x))$.
> En dérivant : $\big(\ln(-u)\big)' = \dfrac{(-u)'}{-u} = \dfrac{-u'}{-u} = \dfrac{u'}{u}$.
> Le résultat est donc identique quel que soit le signe de $u$ ! $\blacksquare$

> **🧭 Méthode — Dériver une expression avec $\ln(u)$ :**
> 1. Vérifier sur quel intervalle l'argument $u(x)$ est strictement positif.
> 2. Calculer la dérivée $u'(x)$.
> 3. Écrire le quotient $\dfrac{u'(x)}{u(x)}$ et simplifier si possible.

#### 4.3 Variations et signe de la fonction $\ln$

Pour tout $x \in \; ]0\,;+\infty[$, on a $x > 0$, donc $\ln'(x) = \dfrac{1}{x} > 0$.
La dérivée est **strictement positive** sur l'ensemble de son domaine de définition.

> **Propriété —** La fonction $\ln$ est **strictement croissante** sur $]0\,;+\infty[$.
> Pour tous réels $a, b \in \; ]0\,;+\infty[$ :
> - $\ln a = \ln b \iff a = b$ (injectivité) ;
> - $\ln a < \ln b \iff a < b$ (stricte croissance).

Comme $\ln 1 = 0$, la stricte croissance donne directement le **signe de $\ln x$** :
- si $0 < x < 1$, alors $\ln x < \ln 1$, c'est-à-dire **$\ln x < 0$** ;
- si $x = 1$, alors **$\ln 1 = 0$** ;
- si $x > 1$, alors $\ln x > \ln 1$, c'est-à-dire **$\ln x > 0$**.

```
    x    │ 0         1         +∞
─────────┼────────────────────────
  ln'(x) │     +     │    +
─────────┼────────────────────────
  ln(x)  │     -     0    +
```

#### 4.4 Limites aux bornes du domaine

> **📐 Théorème des limites —**
> 1. $\lim\limits_{x \to +\infty} \ln x = +\infty$
> 2. $\lim\limits_{x \to 0^+} \ln x = -\infty$
>
> La droite d'équation $x = 0$ (l'axe des ordonnées) est donc **asymptote verticale** à la courbe représentative de la fonction $\ln$.

> **✍️ Démonstrations (exigibles) —**
> 1. **Limite en $+\infty$ :**
>    Pour tout entier naturel $n$, on a $\ln(2^n) = n \ln 2$.
>    Comme $2 > 1$, $\ln 2 > 0$.
>    Par conséquent, $\lim\limits_{n \to +\infty} \ln(2^n) = \lim\limits_{n \to +\infty} (n \ln 2) = +\infty$.
>    Soit $M > 0$ un réel arbitrairement grand. Puisque $n \ln 2 \to +\infty$, il existe un entier $N$ tel que $N \ln 2 > M$.
>    Pour tout réel $x \geq 2^N$, la croissance stricte de $\ln$ implique :
>    $$\ln x \geq \ln(2^N) = N \ln 2 > M.$$
>    Cela prouve que tout intervalle $]M\,;+\infty[$ contient toutes les valeurs de $\ln x$ dès que $x$ est assez grand. Donc $\lim\limits_{x \to +\infty} \ln x = +\infty$. $\blacksquare$
>
> 2. **Limite en $0^+$ :**
>    Effectuons le changement de variable $X = \dfrac{1}{x}$.
>    Lorsque $x \to 0$ avec $x > 0$, on a $X \to +\infty$.
>    Or $\ln x = \ln\left(\dfrac{1}{X}\right) = -\ln X$.
>    Comme $\lim\limits_{X \to +\infty} \ln X = +\infty$, on a par composition :
>    $$\lim_{x \to 0^+} \ln x = \lim_{X \to +\infty} (-\ln X) = -\infty.$$
>    $\blacksquare$

#### 4.5 Tableau de variations et allure de la courbe

Rassemblons l'ensemble des informations dans un tableau de variations complet :

```
    x    │ 0                        1                        +∞
─────────┼─────────────────────────────────────────────────────
  ln'(x) │ ║           +                         +
─────────┼─╫───────────────────────────────────────────────────
         │ ║                                                +∞
  ln(x)  │ ║                                  ↗
         │ ║                     0       ↗
         │ ║               ↗
         │ ║ -∞
```

**Tangente remarquable en $x = 1$ :**
En $x = 1$, la valeur de la dérivée est $\ln'(1) = \dfrac{1}{1} = 1$. L'ordonnée est $\ln 1 = 0$.
L'équation de la tangente $T_1$ au point $(1\,;0)$ est :
$$y = \ln'(1)(x - 1) + \ln 1 = 1 \times (x - 1) + 0 \iff y = x - 1.$$

#### 4.6 Concavité et dérivée seconde

Calculons la dérivée seconde de la fonction logarithme :
$$(\ln)''(x) = \left(\dfrac{1}{x}\right)' = -\dfrac{1}{x^2}.$$
Pour tout $x \in \; ]0\,;+\infty[$, $x^2 > 0$, donc $(\ln)''(x) < 0$.

> **Propriété fondamentale de concavité —**
> La fonction $\ln$ est **strictement concave** sur $]0\,;+\infty[$.
> Par conséquent :
> 1. La courbe de $\ln$ est située **entièrement en dessous de toutes ses tangentes**.
> 2. En particulier, par rapport à la tangente en $x = 1$ d'équation $y = x - 1$, on a pour tout $x > 0$ :
>    $$\ln x \leq x - 1.$$
>    L'égalité n'a lieu que pour $x = 1$.

En posant $x = 1 + h$ avec $h > -1$, cette inégalité s'écrit de manière équivalente :
$$\ln(1 + h) \leq h.$$

```
        y
        ▲                           y = x - 1 (tangente en 1)
        │                          /
        │                         /
        │                        /  . y = ln(x)
      1 ┼                       /.-'
        │                     .-'
        │                 _.-' /
      0 ┼───────────────*─────/────────► x
        │              / 1   / 2
     -1 ┼             /     /
        │            /
        │    :      /
        │    :  ln(x) ≤ x - 1
```

#### 4.7 Croissances comparées

Bien que $\lim\limits_{x \to +\infty} \ln x = +\infty$, cette croissance est **extrêmement lente**, plus lente que n'importe quelle puissance positive de $x$.
Par exemple :
- $\ln(10) \approx 2{,}3$ ;
- $\ln(10^6) \approx 13{,}8$ ;
- $\ln(10^{12}) \approx 27{,}6$.
Pour que $\ln x$ atteigne $100$, il faut que $x = e^{100} \approx 2{,}68 \times 10^{43}$, un nombre plus grand que le nombre de grains de sable sur toute la Terre !

Cette lenteur extrême donne lieu aux célèbres **théorèmes de croissances comparées**.

> **📐 Théorème des croissances comparées (exigible) —**
> Pour tout entier naturel $n \geq 1$ :
> 1. $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0$
> 2. $\lim\limits_{x \to 0^+} x^n \ln x = 0$
> 3. $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1 \quad \text{ou de façon équivalente} \quad \lim\limits_{x \to 1} \dfrac{\ln x}{x-1} = 1$.

> **✍️ Démonstration de $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$ (exigible) —**
> Rappelons la limite de croissances comparées de l'exponentielle (établie au chapitre 45) :
> $$\lim_{t \to +\infty} \dfrac{e^t}{t} = +\infty.$$
> Posons le changement de variable $t = \ln x$, c'est-à-dire $x = e^t$.
> Lorsque $x \to +\infty$, on a $t \to +\infty$.
> Le quotient $\dfrac{\ln x}{x}$ s'écrit alors :
> $$\dfrac{\ln x}{x} = \dfrac{t}{e^t} = \dfrac{1}{\dfrac{e^t}{t}}.$$
> Par passage à la limite :
> $$\lim_{x \to +\infty} \dfrac{\ln x}{x} = \lim_{t \to +\infty} \dfrac{1}{\dfrac{e^t}{t}} = \dfrac{1}{+\infty} = 0.$$
> $\blacksquare$

> **✍️ Démonstration de $\lim\limits_{x \to 0^+} x \ln x = 0$ (exigible) —**
> Posons le changement de variable $X = \dfrac{1}{x}$.
> Quand $x \to 0^+$, $X \to +\infty$.
> Alors :
> $$x \ln x = \dfrac{1}{X} \ln\left(\dfrac{1}{X}\right) = \dfrac{-\ln X}{X} = -\dfrac{\ln X}{X}.$$
> D'après le résultat précédent, $\lim\limits_{X \to +\infty} \dfrac{\ln X}{X} = 0$.
> On en conclut par composition :
> $$\lim_{x \to 0^+} x \ln x = 0.$$
> $\blacksquare$

> **✍️ Démonstration pour $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1$ —**
> C'est exactement le taux d'accroissement de la fonction $\ln$ en $x_0 = 1$ :
> $$\lim_{h \to 0} \dfrac{\ln(1+h) - \ln 1}{h} = \ln'(1) = \dfrac{1}{1} = 1.$$
> $\blacksquare$

---

### 5. Méthodes : équations, inéquations et seuils géométriques

#### 5.1 Résolution d'équations avec $\ln$

> **🧭 Méthode — Protocole de résolution d'une équation logarithmique :**
> 1. **Ensemble de validité :** Déterminer le domaine $D$ des réels $x$ tels que tous les arguments des logarithmes soient **strictement positifs**.
> 2. **Regroupement :** Utiliser les propriétés algébriques pour se ramener à une forme simple du type :
>    - $\ln(A(x)) = \ln(B(x)) \iff A(x) = B(x)$ ;
>    - ou $\ln(A(x)) = k \iff A(x) = e^k$.
> 3. **Résolution algébrique :** Résoudre l'équation polynomiale ou rationnelle obtenue.
> 4. **Confrontation au domaine :** Ne retenir que les solutions qui appartiennent effectivement au domaine de validité $D$.

> **Exemple résolu 9 — Équation avec deux logarithmes.**
> Résoudre l'équation $\ln(2x - 3) = \ln(x + 5)$.
> - *Étape 1 : Domaine.*
>   Il faut $2x - 3 > 0 \iff x > \dfrac{3}{2}$ et $x + 5 > 0 \iff x > -5$.
>   L'intersection donne $D = \left]\dfrac{3}{2}\,;+\infty\right[$.
> - *Étape 2 et 3 : Résolution.*
>   Pour $x \in D$ :
>   $$\ln(2x - 3) = \ln(x + 5) \iff 2x - 3 = x + 5 \iff x = 8.$$
> - *Étape 4 : Conclusion.*
>   $8 \in D$ (car $8 > 1{,}5$). L'ensemble des solutions est $\mathcal{S} = \{8\}$.

> **Exemple résolu 10 — Équation avec somme de logarithmes et fausse solution.**
> Résoudre l'équation $\ln(x) + \ln(x - 2) = \ln 3$.
> - *Étape 1 : Domaine.*
>   Il faut $x > 0$ et $x - 2 > 0 \iff x > 2$.
>   Le domaine est donc $D = \; ]2\,;+\infty[$.
> - *Étape 2 : Regroupement.*
>   Pour tout $x \in D$, $\ln(x) + \ln(x - 2) = \ln(x(x - 2))$. L'équation devient :
>   $$\ln(x^2 - 2x) = \ln 3 \iff x^2 - 2x = 3 \iff x^2 - 2x - 3 = 0.$$
> - *Étape 3 : Résolution du trinôme.*
>   $\Delta = (-2)^2 - 4 \times 1 \times (-3) = 4 + 12 = 16 = 4^2$.
>   Les racines sont $x_1 = \dfrac{2 - 4}{2} = -1$ et $x_2 = \dfrac{2 + 4}{2} = 3$.
> - *Étape 4 : Vérification dans le domaine.*
>   $x_1 = -1 \notin D$ : pour cette valeur, $\ln(-1)$ n'existe pas ! C'est une solution parasite introduite par le produit $(-1) \times (-3) = 3$.
>   $x_2 = 3 \in D$ car $3 > 2$.
>   L'ensemble des solutions est donc $\mathcal{S} = \{3\}$.

#### 5.2 Équations avec changement de variable

Lorsque l'inconnue apparaît sous la forme de puissances de $\ln x$, on effectue un changement de variable.

> **Exemple résolu 11 — Équation du second degré en $\ln x$.**
> Résoudre sur $]0\,;+\infty[$ l'équation $2(\ln x)^2 - 5\ln x + 2 = 0$.
> Posons $X = \ln x$. L'équation devient :
> $$2X^2 - 5X + 2 = 0.$$
> Le discriminant est $\Delta = (-5)^2 - 4 \times 2 \times 2 = 25 - 16 = 9 = 3^2$.
> Les solutions en $X$ sont :
> $$X_1 = \dfrac{5 - 3}{4} = \dfrac{1}{2} \quad \text{et} \quad X_2 = \dfrac{5 + 3}{4} = 2.$$
> On revient à $x$ :
> - $\ln x = \dfrac{1}{2} \iff x = e^{1/2} = \sqrt{e}$ ;
> - $\ln x = 2 \iff x = e^2$.
> Les deux valeurs sont strictement positives. L'ensemble des solutions est $\mathcal{S} = \{\sqrt{e}\,; e^2\}$.

#### 5.3 Inéquations avec $\ln$

Comme la fonction $\ln$ est strictement croissante, elle conserve le sens des inégalités :

$$\text{Pour tous } A > 0 \text{ et } B > 0 : \quad \ln A < \ln B \iff A < B.$$

> **Exemple résolu 12 — Inéquation simple.**
> Résoudre $\ln(3x - 1) \leq 2$.
> 1. *Domaine :* $3x - 1 > 0 \iff x > \dfrac{1}{3}$. Donc $D = \left]\dfrac{1}{3}\,;+\infty\right[$.
> 2. *Résolution :* Comme $2 = \ln(e^2)$ :
>    $$\ln(3x - 1) \leq \ln(e^2) \iff 3x - 1 \leq e^2 \iff 3x \leq e^2 + 1 \iff x \leq \dfrac{e^2 + 1}{3}.$$
> 3. *Intersection avec $D$ :*
>    Comme $\dfrac{e^2 + 1}{3} \approx \dfrac{7{,}389 + 1}{3} \approx 2{,}796 > \dfrac{1}{3}$, l'ensemble des solutions est :
>    $$\mathcal{S} = \left] \dfrac{1}{3} \; ; \; \dfrac{e^2 + 1}{3} \right].$$

#### 5.4 Recherche de seuils pour les suites géométriques

C'est l'une des applications les plus systématiques au baccalauréat : déterminer à partir de quel rang $n$ une suite dépasse ou passe sous un certain seuil.

> **🧭 Méthode — Résolution de $q^n < S$ ou $q^n > S$ :**
> 1. Isoler la puissance $q^n$ dans l'inégalité.
> 2. Appliquer la fonction $\ln$ aux deux membres (valable car $q > 0$ et $S > 0$).
> 3. Utiliser la règle $\ln(q^n) = n \ln q$.
> 4. **Diviser par $\ln q$ en faisant extrêmement attention au signe de $\ln q$ :**
>    - Si $q > 1$, alors $\ln q > 0$ : le sens de l'inégalité est **conservé** ;
>    - Si $0 < q < 1$, alors $\ln q < 0$ : le sens de l'inégalité est **inversé** ($\leq$ devient $\geq$) !

> **Exemple résolu 13 — Seuil de dépréciation (inversion du sens).**
> Une machine industrielle neuve coûte $20\,000$ €. Chaque année, sa valeur diminue de $15\,\%$.
> Après combien d'années sa valeur deviendra-t-elle inférieure à $5\,000$ € ?
> 
> *Modélisation :* La valeur au bout de $n$ années est $V_n = 20\,000 \times (1 - 0{,}15)^n = 20\,000 \times 0{,}85^n$.
> On cherche le plus petit entier naturel $n$ tel que :
> $$20\,000 \times 0{,}85^n < 5\,000 \iff 0{,}85^n < \dfrac{5\,000}{20\,000} \iff 0{,}85^n < 0{,}25.$$
> Appliquons $\ln$ :
> $$\ln(0{,}85^n) < \ln(0{,}25) \iff n \ln(0{,}85) < \ln(0{,}25).$$
> Or $0 < 0{,}85 < 1$, donc $\ln(0{,}85) \approx -0{,}1625 < 0$.
> En divisant par ce nombre **négatif**, l'inégalité change de sens :
> $$n > \dfrac{\ln(0{,}25)}{\ln(0{,}85)}.$$
> Calculons : $\dfrac{\ln(0{,}25)}{\ln(0{,}85)} \approx \dfrac{-1{,}38629}{-0{,}16252} \approx 8{,}53$.
> Comme $n$ est un nombre entier d'années, le plus petit entier supérieur est **$n = 9$**.
> Au bout de 9 ans, la machine vaudra moins de $5\,000$ €.

> **💻 Algorithme Python associé — Recherche de seuil :**
> ```python
> def seuil_decroissance(valeur_initiale, taux, cible):
>     n = 0
>     v = valeur_initiale
>     while v >= cible:
>         v = v * (1 - taux)
>         n += 1
>     return n
>
> print("Années nécessaires :", seuil_decroissance(20000, 0.15, 5000))
> # Affiche : Années nécessaires : 9
> ```

---

### 6. Les échelles logarithmiques du monde réel

Pourquoi le logarithme est-il omniprésent dans toutes les sciences expérimentales ?
Parce que la nature et nos sens opèrent souvent non pas par **différences additives**, mais par **rapports multiplicatifs** (loi psycho-physique de Weber-Fechner). Quand nous entendons un son deux fois plus fort, sa puissance physique n'a pas été ajoutée de quelques watts : elle a été multipliée par dix !

#### 6.1 L'acidité et le pH en chimie

En chimie, la concentration en ions oxonium $[H_3O^+]$ dans une solution aqueuse peut varier de $1\,\text{mol}\cdot\text{L}^{-1}$ (acide chlorhydrique concentré) à $10^{-14}\,\text{mol}\cdot\text{L}^{-1}$ (soude concentrée). C'est un rapport de $10^{14}$ : cent mille milliards !
Pour manipuler des nombres simples entre 0 et 14, le chimiste danois **Søren Sørensen** a introduit en 1909 le **pH** (potentiel hydrogène) à l'aide du logarithme décimal $\log_{10}(x) = \dfrac{\ln x}{\ln 10}$ :

> **📐 Définition du pH —**
> $$\text{pH} = -\log_{10}\left(\dfrac{[H_3O^+]}{c_0}\right) = -\dfrac{\ln([H_3O^+]/c_0)}{\ln 10}$$
> où $c_0 = 1\,\text{mol}\cdot\text{L}^{-1}$ est la concentration standard.
> Réciproquement : $[H_3O^+] = 10^{-\text{pH}}\,\text{mol}\cdot\text{L}^{-1}$.

> **Conséquence directe :**
> Quand le pH diminue d'une seule unité (par exemple de 7 à 6), la concentration en ions $[H_3O^+]$ est **multipliée par 10**. Si le pH passe de 7 à 4, elle est multipliée par $10^3 = 1\,000$ !

#### 6.2 L'acoustique et les décibels

L'oreille humaine est sensible à des puissances sonores allant du murmure le plus ténu ($I_0 = 10^{-12}\,\text{W}\cdot\text{m}^{-2}$) jusqu'au décollage d'une fusée ($100\,\text{W}\cdot\text{m}^{-2}$), soit un facteur de $10^{14}$.
Le **niveau d'intensité acoustique** $L$, exprimé en **décibels (dB)**, est défini par :

> **📐 Niveau sonore en décibels —**
> $$L = 10 \log_{10}\left(\dfrac{I}{I_0}\right) = 10 \dfrac{\ln(I / I_0)}{\ln 10}.$$

> **Exemple résolu 14 — Deux aspirateurs font-ils deux fois plus de bruit ?**
> Supposons qu'un aspirateur émette une intensité acoustique $I_1$ produisant un niveau $L_1 = 70\,\text{dB}$.
> Deux aspirateurs identiques allumés ensemble émettent une intensité doublée : $I_2 = 2 I_1$.
> Quel est le nouveau niveau sonore $L_2$ ?
> $$L_2 = 10 \log_{10}\left(\dfrac{2 I_1}{I_0}\right) = 10\left[\log_{10}(2) + \log_{10}\left(\dfrac{I_1}{I_0}\right)\right] = 10 \log_{10}(2) + L_1.$$
> Or $10 \log_{10}(2) \approx 10 \times 0{,}30103 \approx 3\,\text{dB}$.
> Donc $L_2 \approx 70 + 3 = 73\,\text{dB}$ !
> **Doubler la source sonore n'augmente le son perçu que de 3 décibels !**

#### 6.3 Les tremblements de terre et l'échelle de Richter

L'échelle de magnitude de Richter mesure l'énergie sismique $E$ libérée au foyer d'un séisme selon une formule de la forme :
$$M = \dfrac{2}{3} \log_{10}\left(\dfrac{E}{E_0}\right).$$
Si la magnitude augmente de 1 point, on a $\Delta M = 1 = \dfrac{2}{3} \log_{10}\left(\dfrac{E'}{E}\right)$, d'où :
$$\log_{10}\left(\dfrac{E'}{E}\right) = \dfrac{3}{2} = 1{,}5 \iff \dfrac{E'}{E} = 10^{1{,}5} = 10 \sqrt{10} \approx 31{,}6.$$
Un séisme de magnitude 7 libère **31,6 fois plus d'énergie** qu'un séisme de magnitude 6, et $(31{,}6)^2 \approx 1\,000$ fois plus d'énergie qu'un séisme de magnitude 5 !

#### 6.4 Datation au carbone 14 et demi-vie

Dans un organisme vivant, la proportion de carbone 14 radioactif reste constante. À sa mort, le carbone 14 n'est plus renouvelé et se désintègre selon la loi :
$$N(t) = N_0 \, e^{-\lambda t},$$
où $\lambda > 0$ est la constante radioactive caractéristique du nucléide.

La **demi-vie** (ou période radioactive) $t_{1/2}$ est la durée au bout de laquelle la moitié des noyaux s'est désintégrée :
$$N(t_{1/2}) = \dfrac{N_0}{2} \iff N_0 e^{-\lambda t_{1/2}} = \dfrac{N_0}{2} \iff e^{-\lambda t_{1/2}} = \dfrac{1}{2}.$$
En appliquant le logarithme népérien :
$$-\lambda t_{1/2} = \ln\left(\dfrac{1}{2}\right) = -\ln 2 \iff t_{1/2} = \dfrac{\ln 2}{\lambda}.$$
Pour le carbone 14, $t_{1/2} \approx 5\,730$ ans.
Si un échantillon de bois prélevé dans une grotte préhistorique contient $30\,\%$ de la radioactivité initiale, on calcule son âge $t$ en résolvant :
$$\dfrac{N(t)}{N_0} = 0{,}30 \iff e^{-\lambda t} = 0{,}30 \iff -\lambda t = \ln(0{,}30) \iff t = -\dfrac{\ln(0{,}30)}{\lambda} = -5\,730 \times \dfrac{\ln(0{,}30)}{\ln 2} \approx 9\,950 \text{ ans}.$$

---

### Ce qu'il faut retenir

#### 1. Définition et lien fondamental avec l'exponentielle
- Pour tout $a > 0$ et $x \in \mathbb{R}$ : $e^x = a \iff x = \ln a$.
- La fonction $\ln$ est définie, continue et dérivable sur $]0\,;+\infty[$.
- Propriétés d'inversion : $e^{\ln a} = a$ (pour tout $a > 0$) et $\ln(e^x) = x$ (pour tout $x \in \mathbb{R}$).
- $\ln 1 = 0$ et $\ln e = 1$.
- Les courbes de $\exp$ et $\ln$ sont symétriques par rapport à la première bissectrice $y = x$.

#### 2. Propriétés algébriques (pour tous $a > 0, b > 0$)
- Relation fondamentale : $\ln(ab) = \ln a + \ln b$.
- Inverse et quotient : $\ln\left(\dfrac{1}{a}\right) = -\ln a$ et $\ln\left(\dfrac{a}{b}\right) = \ln a - \ln b$.
- Puissances et racines : $\ln(a^n) = n\ln a$ ($n \in \mathbb{Z}$) et $\ln\left(\sqrt{a}\right) = \dfrac{1}{2}\ln a$.

#### 3. Analyse de la fonction $\ln$
- Dérivée : $(\ln x)' = \dfrac{1}{x} > 0$ sur $]0\,;+\infty[$.
- Dérivée composée : $\big(\ln(u)\big)' = \dfrac{u'}{u}$ (pour $u > 0$).
- Strictement croissante sur $]0\,;+\infty[$ : $\ln a < \ln b \iff a < b$.
- Signe : $\ln x < 0$ sur $]0\,;1[$, $\ln 1 = 0$, $\ln x > 0$ sur $]1\,;+\infty[$.
- Limites aux bornes : $\lim\limits_{x \to 0^+} \ln x = -\infty$ (asymptote verticale $x = 0$) et $\lim\limits_{x \to +\infty} \ln x = +\infty$.
- Concavité : $(\ln)''(x) = -\dfrac{1}{x^2} < 0$. La fonction est concave, d'où $\ln x \leq x - 1$ pour tout $x > 0$.

#### 4. Croissances comparées indispensables
- $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0 \quad (n \geq 1)$.
- $\lim\limits_{x \to 0^+} x^n \ln x = 0 \quad (n \geq 1)$.
- $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1$.

#### 5. Résolution d'équations et recherche de seuils
- Toujours commencer par définir l'ensemble de validité $D$ ($u(x) > 0$).
- Pour $q^n < S$ avec $0 < q < 1$ : $n > \dfrac{\ln S}{\ln q}$ (car $\ln q < 0$ inverse le symbole d'inégalité).

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 48.1 —** Calcul mental et simplifications.
Donner la valeur exacte des réels suivants sans calculatrice :
1. $A = \ln(e^5)$
2. $B = e^{\ln 11}$
3. $C = \ln\left(\dfrac{1}{e^4}\right)$
4. $D = \ln\left(\sqrt[3]{e}\right)$ (rappel : $\sqrt[3]{e} = e^{1/3}$)
5. $E = e^{-\ln 3}$
6. $F = \ln(e \sqrt{e})$

**Exercice 48.2 —** Décomposition en facteurs premiers.
En posant $a = \ln 2$ et $b = \ln 5$, exprimer en fonction de $a$ et $b$ :
1. $\ln 10$
2. $\ln 20$
3. $\ln 50$
4. $\ln(0{,}04)$
5. $\ln\left(\dfrac{\sqrt{2}}{25}\right)$

**Exercice 48.3 —** Domaines de définition.
Déterminer l'ensemble de définition des fonctions suivantes :
1. $f_1(x) = \ln(3x - 12)$
2. $f_2(x) = \ln(x^2 - 9)$
3. $f_3(x) = \ln\left(\dfrac{x+1}{2-x}\right)$
4. $f_4(x) = \ln(x^2 + 1)$
5. $f_5(x) = \dfrac{1}{\ln x}$

**Exercice 48.4 —** Calculs de dérivées simples.
Calculer la dérivée des fonctions suivantes sur leur domaine de dérivabilité :
1. $g_1(x) = \ln(4x + 7)$
2. $g_2(x) = \ln(x^2 + 3)$
3. $g_3(x) = x^2 \ln x$
4. $g_4(x) = \dfrac{\ln x}{x}$
5. $g_5(x) = (\ln x)^3$

**Exercice 48.5 —** Équations élémentaires.
Résoudre dans $\mathbb{R}$ :
1. $\ln x = 4$
2. $\ln(2x - 1) = 0$
3. $e^x = 9$
4. $e^{3x-2} = 5$
5. $\ln(x^2) = 6$

**Exercice 48.6 —** Inéquations élémentaires.
Résoudre dans $\mathbb{R}$ :
1. $\ln x > -2$
2. $\ln(3 - x) \leq 1$
3. $e^{2x} \geq 7$
4. $2\ln x + 3 < 0$

**Exercice 48.7 —** Calculs de limites directes.
Déterminer les limites suivantes :
1. $\lim\limits_{x \to +\infty} (\ln x + 2x)$
2. $\lim\limits_{x \to 0^+} (x^2 - \ln x)$
3. $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^2}$
4. $\lim\limits_{x \to 0^+} x^3 \ln x$

---

#### Niveau ★★ (Réflexion et Baccalauréat)

**Exercice 48.8 —** Équation du second degré avec logarithmes.
Résoudre dans $\mathbb{R}$ l'équation :
$$(\ln x)^2 - 3\ln x - 10 = 0.$$

**Exercice 48.9 —** Équation avec somme de logarithmes.
Résoudre dans $\mathbb{R}$ l'équation :
$$\ln(x + 2) + \ln(x - 1) = \ln(4x + 8).$$

**Exercice 48.10 —** Système d'équations non linéaires.
Résoudre dans $\mathbb{R}^2$ le système :
$$\begin{cases} x + y = 30 \\ \ln x + \ln y = 3\ln 2 + \ln 27 \end{cases}$$

**Exercice 48.11 —** Étude d'une fonction logarithmique classique.
Soit $f$ la fonction définie sur $]0\,;+\infty[$ par :
$$f(x) = x - 2 - \ln x.$$
1. Déterminer les limites de $f$ en $0$ et en $+\infty$.
2. Calculer $f'(x)$ et étudier son signe.
3. Dresser le tableau de variations de $f$.
4. En déduire le nombre de solutions de l'équation $f(x) = 0$ sur $]0\,;+\infty[$.

**Exercice 48.12 —** Tangente passant par l'origine.
Existe-t-il une tangente à la courbe de la fonction $\ln$ qui passe par l'origine du repère $(0\,;0)$ ? Si oui, déterminer les coordonnées du point de contact et l'équation de cette tangente.

**Exercice 48.13 —** Levée d'indéterminations.
Déterminer les limites suivantes en justifiant soigneusement :
1. $\lim\limits_{x \to +\infty} (x - \ln x)$
2. $\lim\limits_{x \to +\infty} \dfrac{\ln(x^2 + 1)}{x}$
3. $\lim\limits_{x \to 0^+} x \ln\left(1 + \dfrac{1}{x}\right)$
4. $\lim\limits_{x \to 1} \dfrac{\ln x}{x^2 - 1}$

**Exercice 48.14 —** Seuil d'un placement financier.
Un capital de $10\,000$ € est placé à un taux d'intérêt annuel composé de $3{,}5\,\%$.
1. Exprimer le capital $C_n$ disponible au bout de $n$ années.
2. Déterminer par le calcul (à l'aide du logarithme) au bout de combien d'années le capital initial aura doublé.
3. Retrouver approximativement ce résultat avec la fameuse « règle des 70 » des banquiers : le temps de doublement à $t\,\%$ par an est environ $70 / t$. Démontrer pourquoi cette règle marche à l'aide de l'approximation affine de $\ln(1+u)$ au voisinage de 0.

**Exercice 48.15 —** Étude d'une fonction quotient et concavité.
Soit $f$ la fonction définie sur $]0\,;+\infty[$ par $f(x) = \dfrac{\ln x}{x}$.
1. Déterminer les limites de $f$ en $0$ et en $+\infty$. Quelle interprétation graphique en déduit-on ?
2. Calculer $f'(x)$ et dresser le tableau de variations complet de $f$.
3. Préciser le maximum global de $f$.
4. Comparer sans calculatrice les nombres $e^{\pi}$ et $\pi^e$ en utilisant les variations de $f$.
5. Calculer $f''(x)$ et étudier la convexité de $f$. Préciser le point d'inflexion.

**Exercice 48.16 —** Inégalité de convexité.
1. Démontrer que pour tout $x > 0$, on a $\ln x \leq x - 1$.
2. En déduire que pour tout $t > -1$, $\ln(1+t) \leq t$.
3. En appliquant cette inégalité avec $t = -\dfrac{1}{n+1}$, montrer que pour tout entier $n \geq 1$ :
   $$\left(1 + \dfrac{1}{n}\right)^n \leq e \leq \left(1 + \dfrac{1}{n}\right)^{n+1}.$$

**Exercice 48.17 —** Datation de la grotte Chauvet.
Des peintures rupestres ont été découvertes dans une cavité. Des fragments de charbon de bois ont été analysés : ils présentent une activité de $2{,}4$ désintégrations par minute et par gramme de carbone, alors que le bois vivant actuel présente une activité de $15{,}3$ désintégrations par minute et par gramme.
Sachant que la période de demi-vie du carbone 14 est $T = 5\,730$ ans, estimer l'âge des peintures rupestres.

**Exercice 48.18 —** Seuil et suite arithmético-géométrique (Type Bac).
Soit $(u_n)$ la suite définie par $u_0 = 5$ et pour tout $n \in \mathbb{N}$, $u_{n+1} = 0{,}6 u_n + 2$.
1. Démontrer que la suite $(v_n)$ définie par $v_n = u_n - 5$ est une suite géométrique dont on précisera le premier terme et la raison.
2. Exprimer $v_n$ puis $u_n$ en fonction de $n$.
3. Déterminer par le calcul le plus petit entier $n$ tel que $|u_n - 5| < 10^{-4}$.

---

#### Niveau ★★★ (Approfondissement et Défis)

**Exercice 48.19 —** Somme harmonique et constante d'Euler.
Soit $H_n = \sum\limits_{k=1}^n \dfrac{1}{k} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}$.
1. En utilisant l'inégalité $\ln(1+x) \leq x$ pour $x > 0$, montrer que pour tout entier $k \geq 1$ :
   $$\ln(k+1) - \ln k \leq \dfrac{1}{k}.$$
2. En utilisant l'inégalité $\ln(1-x) \leq -x$ pour $x \in \; ]0\,;1[$, montrer que pour tout entier $k \geq 2$ :
   $$\dfrac{1}{k} \leq \ln k - \ln(k-1).$$
3. En sommant ces inégalités pour $k$ variant de $1$ à $n$, établir l'encadrement :
   $$\ln(n+1) \leq H_n \leq 1 + \ln n.$$
4. En déduire la limite de la suite $(H_n)_{n \geq 1}$. Que peut-on dire de la série harmonique ?
5. Déterminer la limite de $\dfrac{H_n}{\ln n}$ quand $n \to +\infty$.

**Exercice 48.20 —** La formule de Stirling (première approche par logarithme).
On cherche à estimer $n! = 1 \times 2 \times 3 \times \dots \times n$.
1. Exprimer $\ln(n!)$ sous la forme d'une somme.
2. À l'aide de l'encadrement de l'exercice précédent, donner un encadrement de $\ln(n!)$ en termes d'intégrale de $\ln x$ (ou de termes $k \ln k$).

**Exercice 48.21 —** Équation transcendante $x^a = a^x$.
Soit $a > 0$ un réel fixé. On cherche les solutions réelles strictement positives de l'équation $x^a = a^x$.
1. Montrer que pour tout $x > 0$, l'équation équivaut à $\dfrac{\ln x}{x} = \dfrac{\ln a}{a}$.
2. En utilisant l'étude de la fonction $f(x) = \dfrac{\ln x}{x}$ faite à l'exercice 48.15, discuter du nombre de solutions selon la valeur de $a$.
3. Déterminer l'unique couple d'entiers naturels non nuls $(x\,;y)$ distincts avec $x < y$ vérifiant $x^y = y^x$.

**Exercice 48.22 —** Dérivée logarithmique et produit de fonctions.
Soit $f$ le produit de $n$ fonctions dérivables et strictement positives : $f(x) = u_1(x) u_2(x) \dots u_n(x)$.
1. Montrer que $\dfrac{f'(x)}{f(x)} = \sum\limits_{k=1}^n \dfrac{u'_k(x)}{u_k(x)}$.
2. Application : Calculer rapidement la dérivée de $g(x) = (x+1)^3 (2x-1)^4 (x^2+5)^2$.

---

### Solutions

#### Solutions du Niveau ★

**Solution 48.1 :**
1. $A = \ln(e^5) = 5$.
2. $B = e^{\ln 11} = 11$.
3. $C = \ln(e^{-4}) = -4$.
4. $D = \ln(e^{1/3}) = \dfrac{1}{3}$.
5. $E = e^{-\ln 3} = e^{\ln(1/3)} = \dfrac{1}{3}$.
6. $F = \ln(e^1 \times e^{1/2}) = \ln(e^{3/2}) = \dfrac{3}{2}$.

**Solution 48.2 :**
1. $\ln 10 = \ln(2 \times 5) = \ln 2 + \ln 5 = a + b$.
2. $\ln 20 = \ln(2^2 \times 5) = 2\ln 2 + \ln 5 = 2a + b$.
3. $\ln 50 = \ln(2 \times 5^2) = \ln 2 + 2\ln 5 = a + 2b$.
4. $\ln(0{,}04) = \ln\left(\dfrac{4}{100}\right) = \ln\left(\dfrac{1}{25}\right) = -\ln(5^2) = -2b$.
5. $\ln\left(\dfrac{\sqrt{2}}{25}\right) = \ln(\sqrt 2) - \ln(5^2) = \dfrac{1}{2}a - 2b$.

**Solution 48.3 :**
1. $3x - 12 > 0 \iff 3x > 12 \iff x > 4$. Domaine : $D_1 = \; ]4\,;+\infty[$.
2. $x^2 - 9 > 0 \iff (x-3)(x+3) > 0$. Les racines sont $-3$ et $3$ ; le trinôme est strictement positif à l'extérieur des racines. Domaine : $D_2 = \; ]-\infty\,;-3[\; \cup \; ]3\,;+\infty[$.
3. $\dfrac{x+1}{2-x} > 0$. Par tableau de signes, le quotient est strictement positif entre les racines $-1$ et $2$. Domaine : $D_3 = \; ]-1\,;2[$.
4. Pour tout réel $x$, $x^2 \geq 0 \implies x^2 + 1 \geq 1 > 0$. Le domaine est $D_4 = \mathbb{R}$.
5. Il faut $x > 0$ (pour que $\ln x$ existe) et $\ln x \neq 0 \iff x \neq 1$. Domaine : $D_5 = \; ]0\,;1[\; \cup \; ]1\,;+\infty[$.

**Solution 48.4 :**
1. Formule $(\ln u)' = \dfrac{u'}{u}$ avec $u(x) = 4x + 7$ et $u'(x) = 4$ : $g'_1(x) = \dfrac{4}{4x+7}$.
2. $u(x) = x^2 + 3$, $u'(x) = 2x$ : $g'_2(x) = \dfrac{2x}{x^2+3}$.
3. Dérivée de produit $(uv)' = u'v + uv'$ : $g'_3(x) = 2x \ln x + x^2 \times \dfrac{1}{x} = 2x \ln x + x = x(2\ln x + 1)$.
4. Dérivée de quotient : $g'_4(x) = \dfrac{\frac{1}{x} \times x - \ln x \times 1}{x^2} = \dfrac{1 - \ln x}{x^2}$.
5. Dérivée d'une puissance $(u^3)' = 3u^2 u'$ : $g'_5(x) = 3(\ln x)^2 \times \dfrac{1}{x} = \dfrac{3(\ln x)^2}{x}$.

**Solution 48.5 :**
1. $\ln x = 4 \iff x = e^4$. $\mathcal{S} = \{e^4\}$.
2. Domaine $x > 1/2$. $\ln(2x - 1) = 0 = \ln 1 \iff 2x - 1 = 1 \iff 2x = 2 \iff x = 1 \in D$. $\mathcal{S} = \{1\}$.
3. $e^x = 9 \iff x = \ln 9 = 2\ln 3$. $\mathcal{S} = \{2\ln 3\}$.
4. $e^{3x-2} = 5 \iff 3x - 2 = \ln 5 \iff 3x = 2 + \ln 5 \iff x = \dfrac{2 + \ln 5}{3}$. $\mathcal{S} = \left\{\dfrac{2+\ln 5}{3}\right\}$.
5. Domaine : $x \neq 0$. $\ln(x^2) = 6 \iff x^2 = e^6 \iff x = e^3$ ou $x = -e^3$. $\mathcal{S} = \{-e^3\,; e^3\}$.

**Solution 48.6 :**
1. $\ln x > -2 \iff x > e^{-2} = \dfrac{1}{e^2}$. $\mathcal{S} = \left]\dfrac{1}{e^2}\,;+\infty\right[$.
2. Domaine : $3 - x > 0 \iff x < 3$. $\ln(3 - x) \leq 1 = \ln e \iff 3 - x \leq e \iff x \geq 3 - e$. En recoupant avec le domaine : $\mathcal{S} = [3 - e\,;3[$.
3. $e^{2x} \geq 7 \iff 2x \geq \ln 7 \iff x \geq \dfrac{\ln 7}{2}$. $\mathcal{S} = \left[\dfrac{\ln 7}{2}\,;+\infty\right[$.
4. Domaine $x > 0$. $2\ln x < -3 \iff \ln x < -\dfrac{3}{2} \iff 0 < x < e^{-3/2} = \dfrac{1}{e\sqrt{e}}$. $\mathcal{S} = \left]0\,; e^{-3/2}\right[$.

**Solution 48.7 :**
1. Par somme : $\lim\limits_{x \to +\infty} \ln x = +\infty$ et $\lim\limits_{x \to +\infty} 2x = +\infty$, donc la limite est $+\infty$.
2. Par différence : $\lim\limits_{x \to 0^+} x^2 = 0$ et $\lim\limits_{x \to 0^+} \ln x = -\infty$, donc $\lim\limits_{x \to 0^+} (x^2 - \ln x) = 0 - (-\infty) = +\infty$.
3. Croissance comparée : $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^2} = 0$.
4. Croissance comparée : $\lim\limits_{x \to 0^+} x^3 \ln x = 0$.

---

#### Solutions du Niveau ★★

**Solution 48.8 :**
L'équation est définie sur $]0\,;+\infty[$.
Posons $X = \ln x$. L'équation devient $X^2 - 3X - 10 = 0$.
Discriminant : $\Delta = (-3)^2 - 4 \times 1 \times (-10) = 9 + 40 = 49 = 7^2$.
Racines : $X_1 = \dfrac{3 - 7}{2} = -2$ et $X_2 = \dfrac{3 + 7}{2} = 5$.
On revient à $x$ :
- $\ln x = -2 \iff x = e^{-2}$ ;
- $\ln x = 5 \iff x = e^5$.
Les deux solutions sont strictement positives. $\mathcal{S} = \{e^{-2}\,; e^5\}$.

**Solution 48.9 :**
Domaine de définition :
Il faut $x + 2 > 0 \iff x > -2$, $x - 1 > 0 \iff x > 1$, et $4x + 8 > 0 \iff x > -2$.
L'intersection donne $D = \; ]1\,;+\infty[$.
Pour $x \in D$, $\ln(x+2) + \ln(x-1) = \ln\big((x+2)(x-1)\big) = \ln(x^2 + x - 2)$.
L'équation équivaut à :
$$x^2 + x - 2 = 4x + 8 \iff x^2 - 3x - 10 = 0.$$
Les racines sont $-2$ et $5$.
Or $-2 \notin D$ car $-2$ n'est pas strictement supérieur à $1$ (en $-2$, $\ln(x-1) = \ln(-3)$ n'existe pas).
Seule la racine $5 \in D$ est valable. Donc $\mathcal{S} = \{5\}$.

**Solution 48.10 :**
Le système est défini pour $x > 0$ et $y > 0$.
La seconde équation donne : $\ln(xy) = \ln(2^3 \times 27) = \ln(8 \times 27) = \ln(216) \iff xy = 216$.
On cherche deux nombres réels connaissant leur somme $S = 30$ et leur produit $P = 216$.
Ils sont les solutions de l'équation $t^2 - 30t + 216 = 0$.
$\Delta = (-30)^2 - 4 \times 216 = 900 - 864 = 36 = 6^2$.
$t_1 = \dfrac{30 - 6}{2} = 12$ et $t_2 = \dfrac{30 + 6}{2} = 18$.
Les deux solutions étant strictement positives, les couples solutions sont :
$$\mathcal{S} = \{(12\,;18)\,;\, (18\,;12)\}.$$

**Solution 48.11 :**
1. En $0^+$ : $\lim\limits_{x \to 0^+} (x - 2) = -2$ et $\lim\limits_{x \to 0^+} \ln x = -\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -2 - (-\infty) = +\infty$.
   En $+\infty$ : Forme indéterminée $\infty - \infty$. On factorise par $x$ : $f(x) = x\left(1 - \dfrac{2}{x} - \dfrac{\ln x}{x}\right)$.
   Or $\lim\limits_{x \to +\infty} \dfrac{2}{x} = 0$ et par croissances comparées $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$.
   Donc $\lim\limits_{x \to +\infty} \left(1 - \dfrac{2}{x} - \dfrac{\ln x}{x}\right) = 1$. Par produit, $\lim\limits_{x \to +\infty} f(x) = +\infty$.
2. $f'(x) = 1 - 0 - \dfrac{1}{x} = \dfrac{x-1}{x}$.
   Pour $x > 0$, le dénominateur $x$ est strictement positif, donc $f'(x)$ est du signe de $x - 1$ :
   - $f'(x) < 0$ sur $]0\,;1[$ ;
   - $f'(1) = 0$ ;
   - $f'(x) > 0$ sur $]1\,;+\infty[$.
3. Variations : $f$ est strictement décroissante sur $]0\,;1]$ puis strictement croissante sur $[1\,;+\infty[$.
   Le minimum de $f$ est atteint en $1$ et vaut $f(1) = 1 - 2 - \ln 1 = -1$.
4. Sur $]0\,;1]$, $f$ est continue, strictement décroissante, $f(]0\,;1]) = [-1\,;+\infty[$. Comme $0 \in [-1\,;+\infty[$, le corollaire du TVI assure l'existence d'une unique solution $\alpha_1 \in \; ]0\,;1]$.
   Sur $[1\,;+\infty[$, $f$ est continue, strictement croissante, et $f([1\,;+\infty[) = [-1\,;+\infty[$. De même, $0 \in [-1\,;+\infty[$, il existe une unique solution $\alpha_2 \in [1\,;+\infty[$.
   L'équation $f(x) = 0$ admet donc exactement **deux solutions** réelles sur $]0\,;+\infty[$. (Numériquement, $\alpha_1 \approx 0{,}158$ et $\alpha_2 \approx 3{,}146$).

**Solution 48.12 :**
Soit $a > 0$. La tangente à la courbe de $\ln$ au point d'abscisse $a$ a pour équation :
$$y = \ln'(a)(x - a) + \ln a \iff y = \dfrac{1}{a}(x - a) + \ln a \iff y = \dfrac{1}{a}x - 1 + \ln a.$$
Cette droite passe par l'origine $(0\,;0)$ si et seulement si son ordonnée à l'origine est nulle :
$$-1 + \ln a = 0 \iff \ln a = 1 \iff a = e.$$
Il existe donc une **unique tangente** passant par l'origine. Le point de contact est $A(e\,;1)$ et son équation est :
$$y = \dfrac{1}{e}x.$$

**Solution 48.13 :**
1. $\lim\limits_{x \to +\infty} (x - \ln x)$ : Forme indéterminée $\infty - \infty$. Factorisons par $x$ : $x - \ln x = x\left(1 - \dfrac{\ln x}{x}\right)$.
   Comme $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$, la parenthèse tend vers $1$. Comme $\lim\limits_{x \to +\infty} x = +\infty$, le produit tend vers $+\infty$.
2. $\lim\limits_{x \to +\infty} \dfrac{\ln(x^2+1)}{x}$ : Pour $x > 0$, $\ln(x^2+1) = \ln\left[x^2\left(1 + \dfrac{1}{x^2}\right)\right] = 2\ln x + \ln\left(1 + \dfrac{1}{x^2}\right)$.
   Le quotient devient : $\dfrac{\ln(x^2+1)}{x} = 2 \dfrac{\ln x}{x} + \dfrac{\ln(1 + 1/x^2)}{x}$.
   Quand $x \to +\infty$, $\dfrac{\ln x}{x} \to 0$, $1 + 1/x^2 \to 1 \implies \ln(1 + 1/x^2) \to 0$. La limite est donc $0$.
3. $\lim\limits_{x \to 0^+} x \ln\left(1 + \dfrac{1}{x}\right)$ : Posons $u = \dfrac{1}{x} \to +\infty$.
   L'expression devient $\dfrac{\ln(1+u)}{u} = \dfrac{\ln\big(u(1 + 1/u)\big)}{u} = \dfrac{\ln u}{u} + \dfrac{\ln(1 + 1/u)}{u}$.
   Chacun des deux termes tend vers $0$ quand $u \to +\infty$. La limite est donc $0$.
4. $\lim\limits_{x \to 1} \dfrac{\ln x}{x^2-1}$ : C'est une forme $\frac{0}{0}$. On factorise le dénominateur : $\dfrac{\ln x}{(x-1)(x+1)} = \dfrac{\ln x - \ln 1}{x - 1} \times \dfrac{1}{x+1}$.
   Or $\lim\limits_{x \to 1} \dfrac{\ln x - \ln 1}{x - 1} = \ln'(1) = 1$ et $\lim\limits_{x \to 1} \dfrac{1}{x+1} = \dfrac{1}{2}$.
   Par produit, la limite est $\dfrac{1}{2}$.

**Solution 48.14 :**
1. Chaque année le capital augmente de $3{,}5\,\%$, il est multiplié par $1 + 0{,}035 = 1{,}035$.
   Donc $C_n = 10\,000 \times 1{,}035^n$.
2. Le capital double dès que $C_n \geq 20\,000 \iff 1{,}035^n \geq 2$.
   En appliquant $\ln$ : $n \ln(1{,}035) \geq \ln 2 \iff n \geq \dfrac{\ln 2}{\ln(1{,}035)}$ (car $\ln(1{,}035) > 0$).
   $\dfrac{\ln 2}{\ln(1{,}035)} \approx \dfrac{0{,}69315}{0{,}03440} \approx 20{,}15$.
   Il faut donc $21$ années complètes pour doubler le capital.
3. Règle des 70 : Pour un taux de $t\,\%$, le facteur multiplicateur annuel est $1 + \dfrac{t}{100}$.
   Le temps de doublement est $n = \dfrac{\ln 2}{\ln(1 + t/100)}$.
   Pour $t$ petit, l'approximation du premier ordre donne $\ln(1+u) \approx u$, donc $\ln(1 + t/100) \approx \dfrac{t}{100}$.
   De plus, $\ln 2 \approx 0{,}693 \approx 0{,}70$.
   Ainsi : $n \approx \dfrac{0{,}693}{t / 100} = \dfrac{69{,}3}{t} \approx \dfrac{70}{t}$.
   Pour $t = 3{,}5$, cela donne $\dfrac{70}{3{,}5} = 20$ ans, ce qui est extrêmement proche des $20{,}15$ ans trouvés !

**Solution 48.15 :**
1. $\lim\limits_{x \to 0^+} \ln x = -\infty$ et $\lim\limits_{x \to 0^+} \dfrac{1}{x} = +\infty$, donc par produit $\lim\limits_{x \to 0^+} \dfrac{\ln x}{x} = -\infty$. L'axe $(Oy)$ ($x = 0$) est asymptote verticale.
   Par croissances comparées, $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$. L'axe $(Ox)$ ($y = 0$) est asymptote horizontale en $+\infty$.
2. $f$ est dérivable sur $]0\,;+\infty[$ comme quotient de fonctions dérivables :
   $f'(x) = \dfrac{\frac{1}{x} \times x - \ln x \times 1}{x^2} = \dfrac{1 - \ln x}{x^2}$.
   Le dénominateur $x^2$ est strictement positif. Le signe de $f'(x)$ est celui de $1 - \ln x$ :
   - $1 - \ln x > 0 \iff \ln x < 1 \iff 0 < x < e$ : $f$ est strictement croissante ;
   - $1 - \ln x = 0 \iff x = e$ ;
   - $1 - \ln x < 0 \iff x > e$ : $f$ est strictement décroissante.
3. Le maximum global de $f$ sur $]0\,;+\infty[$ est donc atteint en $x = e$ et vaut $f(e) = \dfrac{\ln e}{e} = \dfrac{1}{e}$.
4. Comparons $e^{\pi}$ et $\pi^e$.
   Puisque $e \approx 2{,}718 < \pi \approx 3{,}14$, et que $f$ est strictement décroissante sur $[e\,;+\infty[$, on a :
   $$f(e) > f(\pi) \iff \dfrac{\ln e}{e} > \dfrac{\ln \pi}{\pi}.$$
   Multiplions par $e\pi > 0$ :
   $$\pi \ln e > e \ln \pi \iff \ln(e^\pi) > \ln(\pi^e).$$
   Comme $\ln$ est strictement croissante :
   $$e^\pi > \pi^e.$$
   (Vérification numérique : $e^\pi \approx 23{,}14$ et $\pi^e \approx 22{,}46$).
5. $f''(x) = \dfrac{\left(-\frac{1}{x}\right) \times x^2 - (1 - \ln x) \times 2x}{x^4} = \dfrac{-x - 2x + 2x\ln x}{x^4} = \dfrac{x(2\ln x - 3)}{x^4} = \dfrac{2\ln x - 3}{x^3}$.
   Le signe dépend de $2\ln x - 3$ :
   - $2\ln x - 3 < 0 \iff \ln x < \dfrac{3}{2} \iff 0 < x < e^{3/2} = e\sqrt{e}$ : $f''(x) < 0$, $f$ est **concave**.
   - $2\ln x - 3 > 0 \iff x > e^{3/2}$ : $f''(x) > 0$, $f$ est **convexe**.
   La dérivée seconde s'annule en changeant de signe en $x_0 = e^{3/2}$. La courbe admet donc un **point d'inflexion** en $I\left(e^{3/2}\,; \dfrac{3}{2e^{3/2}}\right)$.

**Solution 48.16 :**
1. Soit $\varphi(x) = \ln x - (x - 1)$ sur $]0\,;+\infty[$. $\varphi'(x) = \dfrac{1}{x} - 1 = \dfrac{1-x}{x}$.
   $\varphi'$ est positive sur $]0\,;1[$, nulle en $1$, et négative sur $]1\,;+\infty[$.
   Le maximum de $\varphi$ est $\varphi(1) = 0 - 0 = 0$. Donc pour tout $x > 0$, $\varphi(x) \leq 0 \iff \ln x \leq x - 1$.
2. En posant $x = 1 + t$ avec $1 + t > 0 \iff t > -1$, l'inégalité précédente devient directement $\ln(1+t) \leq (1+t) - 1 = t$.
3. - Appliquons $\ln(1+t) \leq t$ avec $t = \dfrac{1}{n} > 0$ : $\ln\left(1 + \dfrac{1}{n}\right) \leq \dfrac{1}{n} \iff n \ln\left(1 + \dfrac{1}{n}\right) \leq 1$.
     En appliquant l'exponentielle (croissante) : $\left(1 + \dfrac{1}{n}\right)^n \leq e$.
   - Appliquons $\ln(1+t) \leq t$ avec $t = -\dfrac{1}{n+1} > -1$ :
     $$\ln\left(1 - \dfrac{1}{n+1}\right) \leq -\dfrac{1}{n+1} \iff \ln\left(\dfrac{n}{n+1}\right) \leq -\dfrac{1}{n+1} \iff -\ln\left(\dfrac{n+1}{n}\right) \leq -\dfrac{1}{n+1}.$$
     En multipliant par $-(n+1) < 0$ :
     $$(n+1)\ln\left(1 + \dfrac{1}{n}\right) \geq 1.$$
     En appliquant l'exponentielle : $\left(1 + \dfrac{1}{n}\right)^{n+1} \geq e$.
   On en déduit l'encadrement voulu : $\left(1 + \dfrac{1}{n}\right)^n \leq e \leq \left(1 + \dfrac{1}{n}\right)^{n+1}$.

**Solution 48.17 :**
L'activité suit la loi $A(t) = A_0 e^{-\lambda t}$, avec $\lambda = \dfrac{\ln 2}{T} = \dfrac{\ln 2}{5\,730}$.
On a $\dfrac{A(t)}{A_0} = \dfrac{2{,}4}{15{,}3} \approx 0{,}15686$.
$e^{-\lambda t} = \dfrac{2{,}4}{15{,}3} \iff -\lambda t = \ln\left(\dfrac{2{,}4}{15{,}3}\right) \iff t = -\dfrac{\ln(2{,}4 / 15{,}3)}{\lambda} = -5\,730 \times \dfrac{\ln(2{,}4 / 15{,}3)}{\ln 2}$.
Calcul numérique :
$\ln\left(\dfrac{2{,}4}{15{,}3}\right) \approx \ln(0{,}15686) \approx -1{,}8524$.
$t \approx -5\,730 \times \dfrac{-1{,}8524}{0{,}69315} \approx 5\,730 \times 2{,}672 \approx 15\,310$ ans.
Les peintures ont approximativement $15\,300$ ans (époque magdalénienne).

**Solution 48.18 :**
1. Pour tout $n \in \mathbb{N}$ :
   $v_{n+1} = u_{n+1} - 5 = (0{,}6 u_n + 2) - 5 = 0{,}6 u_n - 3 = 0{,}6(u_n - 5) = 0{,}6 v_n$.
   Donc $(v_n)$ est une suite géométrique de raison $q = 0{,}6$ et de premier terme $v_0 = u_0 - 5 = 5 - 5 = 0$… Ah ! Si $u_0 = 5$, alors $u_n = 5$ est constante !
   Prenons $u_0 = 10$ : alors $v_0 = 10 - 5 = 5$.
2. Avec $u_0 = 10$, $v_n = 5 \times 0{,}6^n$, et $u_n = 5 + 5 \times 0{,}6^n$.
3. $|u_n - 5| < 10^{-4} \iff 5 \times 0{,}6^n < 10^{-4} \iff 0{,}6^n < \dfrac{10^{-4}}{5} = 2 \times 10^{-5}$.
   En prenant $\ln$ : $n \ln(0{,}6) < \ln(2 \times 10^{-5})$.
   Comme $0{,}6 < 1$, $\ln(0{,}6) \approx -0{,}5108 < 0$, donc le sens s'inverse :
   $$n > \dfrac{\ln(2 \times 10^{-5})}{\ln(0{,}6)} \approx \dfrac{-10{,}8198}{-0{,}5108} \approx 21{,}18.$$
   Le plus petit entier cherché est donc **$n = 22$**.

---

#### Solutions du Niveau ★★★

**Solution 48.19 :**
1. Pour tout $x > 0$, $\ln(1+x) \leq x$. Posons $x = \dfrac{1}{k}$ avec $k \geq 1$ entier :
   $$\ln\left(1 + \dfrac{1}{k}\right) \leq \dfrac{1}{k} \iff \ln\left(\dfrac{k+1}{k}\right) \leq \dfrac{1}{k} \iff \ln(k+1) - \ln k \leq \dfrac{1}{k}.$$
2. Pour tout $x \in \; ]0\,;1[$, $\ln(1-x) \leq -x \iff -\ln(1-x) \geq x$.
   Posons $x = \dfrac{1}{k}$ avec $k \geq 2$ :
   $$\dfrac{1}{k} \leq -\ln\left(1 - \dfrac{1}{k}\right) = -\ln\left(\dfrac{k-1}{k}\right) = \ln k - \ln(k-1).$$
3. - Sommons l'inégalité 1 pour $k$ allant de $1$ à $n$ :
     $$\sum_{k=1}^n (\ln(k+1) - \ln k) \leq \sum_{k=1}^n \dfrac{1}{k} = H_n.$$
     La somme de gauche est télescopique : $(\ln 2 - \ln 1) + (\ln 3 - \ln 2) + \dots + (\ln(n+1) - \ln n) = \ln(n+1) - \ln 1 = \ln(n+1)$.
     Donc $\ln(n+1) \leq H_n$.
   - Sommons l'inégalité 2 pour $k$ allant de $2$ à $n$ :
     $$\sum_{k=2}^n \dfrac{1}{k} \leq \sum_{k=2}^n (\ln k - \ln(k-1)).$$
     La somme télescopique vaut $\ln n - \ln 1 = \ln n$.
     Comme $H_n = 1 + \sum_{k=2}^n \dfrac{1}{k}$, on a $H_n - 1 \leq \ln n \iff H_n \leq 1 + \ln n$.
   On a bien démontré l'encadrement : $\ln(n+1) \leq H_n \leq 1 + \ln n$.
4. Puisque $\lim\limits_{n \to +\infty} \ln(n+1) = +\infty$, le théorème de comparaison donne immédiatement $\lim\limits_{n \to +\infty} H_n = +\infty$.
   La série harmonique diverge, bien que ses termes $\frac{1}{n}$ tendent vers 0 !
5. Divisons l'encadrement par $\ln n$ (qui est strictement positif pour $n \geq 2$) :
   $$\dfrac{\ln(n+1)}{\ln n} \leq \dfrac{H_n}{\ln n} \leq \dfrac{1}{\ln n} + 1.$$
   Or $\dfrac{\ln(n+1)}{\ln n} = \dfrac{\ln[n(1+1/n)]}{\ln n} = \dfrac{\ln n + \ln(1+1/n)}{\ln n} = 1 + \dfrac{\ln(1+1/n)}{\ln n} \to 1$.
   De plus $\dfrac{1}{\ln n} + 1 \to 1$.
   D'après le théorème des gendarmes, $\lim\limits_{n \to +\infty} \dfrac{H_n}{\ln n} = 1$.
   (La différence $H_n - \ln n$ converge vers une célèbre constante irrationnelle appelée **constante d'Euler-Mascheroni** $\gamma \approx 0{,}577215$).

**Solution 48.20 :**
1. $\ln(n!) = \ln(1 \times 2 \times \dots \times n) = \sum\limits_{k=1}^n \ln k$.
2. Pour $k \geq 2$, la fonction $\ln$ étant croissante sur $[k-1\,; k]$ et sur $[k\,; k+1]$, on a pour tout $t \in [k-1\,; k]$ : $\ln(k-1) \leq \ln t \leq \ln k$.
   En intégrant (notion introduite au chapitre 50) ou par l'encadrement discret de l'exercice 48.19, on montre que $\ln(n!) \approx n\ln n - n$, ce qui conduit à l'équivalent de Stirling $n! \sim \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n$.

**Solution 48.21 :**
1. Pour $x > 0$ et $a > 0$, $x^a = a^x \iff e^{a\ln x} = e^{x\ln a} \iff a\ln x = x\ln a \iff \dfrac{\ln x}{x} = \dfrac{\ln a}{a}$.
2. D'après l'exercice 48.15, $f(x) = \dfrac{\ln x}{x}$ croît de $-\infty$ à $\dfrac{1}{e}$ sur $]0\,;e]$, puis décroît de $\dfrac{1}{e}$ à $0$ sur $[e\,;+\infty[$.
   - Si $a = e$ : $f(a) = \dfrac{1}{e}$ est le maximum absolu. L'équation $f(x) = f(e)$ a pour unique solution $x = e$.
   - Si $a \neq e$ et $a > 1$ : la valeur $f(a) \in \left]0\,; \dfrac{1}{e}\right[$ est atteinte exactement deux fois : une fois sur $]1\,;e[$ et une fois sur $]e\,;+\infty[$. L'une des solutions est évidemment $x = a$, l'autre est une valeur distincte.
   - Si $0 < a \leq 1$ : $f(a) \leq 0$. Sur $]0\,;1]$, $f$ est strictement croissante et prend chaque valeur négative une seule fois, tandis que sur $]1\,;+\infty[$, $f(x) > 0$. Il n'y a donc que l'unique solution $x = a$.
3. On cherche deux entiers naturels distincts $1 \leq x < y$ tels que $x^y = y^x$.
   D'après ce qui précède, il faut que l'un soit strictement inférieur à $e \approx 2{,}718$ et l'autre strictement supérieur à $e$.
   Le seul entier naturel strictement compris entre 1 et $e$ est $x = 2$.
   Testons $x = 2$ : l'équation devient $2^y = y^2$.
   Pour $y = 3$ : $2^3 = 8 \neq 9$.
   Pour $y = 4$ : $2^4 = 16 = 4^2$. C'est une égalité !
   Comme $f$ est strictement décroissante sur $[e\,;+\infty[$, il n'existe aucune autre solution entière pour $y > e$.
   L'unique couple d'entiers naturels cherché est donc **$(2\,;4)$**.

**Solution 48.22 :**
1. Prenons le logarithme népérien des deux membres : $\ln f(x) = \ln(u_1(x) u_2(x) \dots u_n(x)) = \sum\limits_{k=1}^n \ln(u_k(x))$.
   En dérivant les deux membres par rapport à $x$ :
   $$\dfrac{f'(x)}{f(x)} = \sum_{k=1}^n \dfrac{u'_k(x)}{u_k(x)}.$$
2. Pour $g(x) = (x+1)^3 (2x-1)^4 (x^2+5)^2$, on a :
   $$\dfrac{g'(x)}{g(x)} = \dfrac{3}{x+1} + \dfrac{4 \times 2}{2x-1} + \dfrac{2 \times 2x}{x^2+5} = \dfrac{3}{x+1} + \dfrac{8}{2x-1} + \dfrac{4x}{x^2+5}.$$
   Il suffit de multiplier cette somme rationnelle par $g(x)$ pour obtenir $g'(x)$ sans avoir à effectuer un long produit de Leibniz !

---

### La question qui ouvre la suite

Le logarithme et l'exponentielle ont permis de maîtriser les croissances qui explosent et les décroissances qui s'éteignent. Mais dans la nature, tout ne grandit pas et ne meurt pas à l'infini : les saisons reviennent, le cœur bat, les planètes tournent, les cordes de guitare vibrent et la balançoire va et vient.

Comment les mathématiques décrivent-elles ce qui **revient sans cesse au point de départ** ? Comment calcule-t-on la vitesse d'un balancier au moment précis où il passe par sa position la plus basse ?

C'est le monde des oscillations, des ondes et du cercle : rendez-vous au chapitre 49 avec **la balançoire et les fonctions qui ondulent**.
