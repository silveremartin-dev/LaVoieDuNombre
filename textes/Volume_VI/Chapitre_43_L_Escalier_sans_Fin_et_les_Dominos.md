# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 43 : L'Escalier sans Fin et les Dominos

> *« Pour gravir un escalier infini, il n'est pas nécessaire de voir la dernière marche. Il suffit d'être certain de deux choses : que l'on peut poser le pied sur la première, et que de n'importe quelle marche on sait toujours monter à la suivante. »*

---

### Ce que tu vas découvrir

- Pourquoi **vérifier** une propriété sur 10, 100 ou même un milliard d'exemples ne **prouve** rien, et comment des conjectures « évidentes » se sont effondrées.
- Le **raisonnement par récurrence** : une machine logique à trois temps (**initialisation**, **hérédité**, **conclusion**) qui permet de démontrer une infinité d'énoncés en un nombre fini de lignes.
- Comment **rédiger** une récurrence impeccable, comme on l'attend au baccalauréat.
- La célèbre **inégalité de Bernoulli** $(1+a)^n \geq 1 + na$, première démonstration exigible de l'année, qui servira dès le chapitre suivant.
- Les **pièges** : la récurrence sans initialisation, l'hérédité qui casse à un seul endroit (le paradoxe des chevaux), la récurrence « qui ne passe pas » et comment la renforcer.

---

### 1. Le problème : le piège des exemples

#### 1.1 Les nombres impairs et les carrés

Prends des cailloux et dispose-les en carrés emboîtés, comme le faisaient les pythagoriciens sur le sable :

```
  ●        ● ○        ● ○ ●        ● ○ ● ○
           ○ ○        ○ ○ ●        ○ ○ ● ○
                      ● ● ●        ● ● ● ○
                                   ○ ○ ○ ○
  1      1 + 3      1 + 3 + 5    1 + 3 + 5 + 7
  = 1     = 4         = 9          = 16
```

Chaque nouvelle « équerre » de cailloux (on l'appelait un **gnomon**) ajoute le nombre impair suivant, et le carré grandit d'un rang. On conjecture :

$$1 + 3 + 5 + \dots + (2n - 1) = n^2.$$

On vérifie pour $n = 1, 2, 3, 4, 5$... ça marche toujours. Mais **est-ce vrai pour tout $n$** ? Pour $n = 10^{100}$ ? Personne ne fera jamais le calcul. Le dessin nous convainc, mais un dessin ne montre que quelques cas.

#### 1.2 Le polynôme d'Euler qui fabriquait des nombres premiers

En 1772, Leonhard Euler remarque le polynôme $p(n) = n^2 + n + 41$. Calculons :

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 10 | 20 | 39 |
|---|---|---|---|---|---|---|---|---|---|
| $p(n)$ | 41 | 43 | 47 | 53 | 61 | 71 | 151 | 461 | 1601 |

Tous ces nombres sont **premiers** ! On peut vérifier les 40 valeurs de $n = 0$ à $n = 39$ : aucune exception. Quarante succès d'affilée... Un esprit pressé conclurait : « $n^2 + n + 41$ est toujours premier ». Et pourtant :

$$p(40) = 40^2 + 40 + 41 = 1600 + 81 = 1681 = 41 \times 41.$$

Raté. Et $p(41) = 41^2 + 41 + 41 = 41 \times 43$ n'est pas premier non plus.

#### 1.3 Les cercles et les régions

Place $n$ points sur un cercle, relie-les tous deux à deux par des cordes (en évitant que trois cordes se croisent au même point), et compte les régions découpées dans le disque :

| Nombre de points $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Nombre de régions | 1 | 2 | 4 | 8 | 16 | **31** |

Tout le monde parie sur 32 pour $n = 6$ : la suite des puissances de 2 semble évidente. Mais en dessinant avec soin, on trouve **31**. La véritable formule est $\binom{n}{4} + \binom{n}{2} + 1$, qui n'a rien à voir avec $2^{n-1}$.

#### 1.4 La crise

Ces trois exemples posent un problème profond. En mathématiques, on veut des énoncés **pour tout entier naturel $n$** : une infinité de cas. Or :

- vérifier des cas, même très nombreux, ne prouve rien (Euler, cercles) ;
- un dessin convaincant reste un dessin de quelques cas (les gnomons).

Il nous faut un outil qui **traite d'un seul coup l'infinité des entiers**. Cet outil, c'est le raisonnement par récurrence.

> **💡 Le savais-tu ?** Certaines conjectures résistent bien plus longtemps. La conjecture de Pólya (1919) sur les entiers ayant « plus de facteurs premiers en nombre impair que pair » a été vérifiée jusqu'à des centaines de millions avant qu'on trouve un contre-exemple, en 1958 ; le plus petit contre-exemple est $906\,150\,257$. Aucun ordinateur n'aurait suffi à « prouver » cette conjecture par vérification — et heureusement, puisqu'elle était fausse.

---

### 2. L'idée : les dominos et l'escalier

#### 2.1 Le geste

Aligne une très longue rangée de dominos debout. Pour être sûr qu'ils tombent **tous**, de quoi as-tu besoin ?

1. **Que le premier tombe** : tu le pousses du doigt.
2. **Que chaque domino, s'il tombe, fasse tomber le suivant** : ils sont assez proches les uns des autres.

Remarque bien : la condition 2 ne dit **pas** que les dominos tombent. Elle dit seulement : « *si* celui-ci tombe, *alors* le suivant tombe ». C'est une **implication**, une promesse de transmission.

```
   Pousse !
     ↓
    ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ...      Initialisation : le premier tombe.
    ╲ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ...      Hérédité : chaque chute entraîne la suivante.
    ╲ ╲ ╲ ╲ ╲ ▌ ▌ ▌ ▌ ...      Conclusion : ils tombent tous.
```

Si l'une des deux conditions manque, tout s'écroule... ou plutôt rien ne s'écroule :
- sans la poussée initiale, les dominos peuvent être parfaitement espacés, aucun ne bouge ;
- si un seul écart est trop grand (entre le 40ᵉ et le 41ᵉ, disons), la chaîne s'arrête là.

L'escalier offre la même image : pour gravir **toutes** les marches d'un escalier sans fin, il suffit de savoir monter sur la première marche, et de savoir passer de n'importe quelle marche à la suivante.

#### 2.2 Les notations

Avant d'énoncer le principe, précisons le vocabulaire.

- $\mathbb{N}$ (lire « N », l'ensemble des **entiers naturels**) $= \{0 ; 1 ; 2 ; 3 ; \dots\}$. La lettre double, dite « gras de tableau », a été popularisée au XXᵉ siècle par le groupe Bourbaki ; le N vient de « naturel ».
- On note $\mathcal{P}(n)$ (lire « P de n ») une **propriété** qui dépend de l'entier $n$ : c'est une **phrase** qui peut être vraie ou fausse selon la valeur de $n$. Par exemple $\mathcal{P}(n)$ : « $1 + 3 + \dots + (2n-1) = n^2$ ». Attention : $\mathcal{P}(n)$ n'est **pas un nombre**, c'est un énoncé. On ne l'additionne pas, on ne le multiplie pas : on dit qu'il est vrai ou faux.
- Le symbole $\Rightarrow$ (lire « implique » ou « entraîne ») : $A \Rightarrow B$ signifie « si $A$ est vrai, alors $B$ est vrai ».
- $n_0$ (lire « n zéro ») désigne le **rang de départ**, souvent $0$ ou $1$, parfois plus grand.
- Le symbole $\forall$ (lire « pour tout ») est un A renversé, pour l'allemand *alle* ou l'anglais *all* ; il a été introduit par Gerhard Gentzen en 1935.

#### 2.3 Le principe

> **📐 Définition — Principe de récurrence.** Soit $\mathcal{P}(n)$ une propriété dépendant d'un entier naturel $n$, et $n_0$ un entier naturel. Si :
> 1. **Initialisation** : $\mathcal{P}(n_0)$ est vraie ;
> 2. **Hérédité** : pour tout entier $n \geq n_0$, si $\mathcal{P}(n)$ est vraie alors $\mathcal{P}(n+1)$ est vraie ;
>
> alors **(conclusion)** $\mathcal{P}(n)$ est vraie pour tout entier $n \geq n_0$.

L'hypothèse « $\mathcal{P}(n)$ est vraie », que l'on utilise dans l'étape d'hérédité, s'appelle l'**hypothèse de récurrence** (souvent abrégée « HR »).

**Pourquoi ce principe est-il vrai ?** On peut le voir comme une propriété fondamentale des entiers naturels : on obtient tous les entiers en partant de $0$ et en ajoutant $1$ autant de fois qu'il le faut. Si la propriété « se propage » de chaque entier au suivant, et qu'elle est vraie au départ, aucun entier ne peut lui échapper. On peut aussi raisonner par l'absurde : s'il existait des entiers $n \geq n_0$ pour lesquels $\mathcal{P}(n)$ est fausse, il y en aurait un **plus petit**, disons $m$. Ce n'est pas $n_0$ (initialisation). Donc $m - 1 \geq n_0$, et $\mathcal{P}(m-1)$ est vraie puisque $m$ est le plus petit contre-exemple. Mais alors l'hérédité donne $\mathcal{P}(m)$ vraie : contradiction. Au XIXᵉ siècle, Giuseppe Peano fera de ce principe l'un des **axiomes** qui définissent les entiers naturels (1889).

> **🔍 L'histoire vraie —** On trouve des raisonnements de ce type chez le mathématicien persan **Al-Karaji** (vers l'an 1000), qui l'utilise pour la formule du binôme et la somme des cubes, puis chez **Francesco Maurolico**, qui en 1575 démontre ainsi que la somme des $n$ premiers nombres impairs vaut $n^2$ — exactement notre problème des gnomons ! Mais c'est **Blaise Pascal**, dans son *Traité du triangle arithmétique* (1654), qui en donne la première formulation explicite en deux temps : il démontre une propriété « pour la première base », puis montre que « si elle se trouve dans une base quelconque, elle se trouvera nécessairement dans la suivante ». Le nom d'« induction mathématique » est dû à Augustus De Morgan (1838) ; en France, on dit **récurrence**, du latin *recurrere*, « courir en arrière » : pour atteindre $n+1$, on revient à $n$.

> **⚠️ Attention, piège ! —** L'hérédité **ne suppose pas** que $\mathcal{P}(n)$ est vraie pour tout $n$ (ce serait supposer ce qu'on veut démontrer !). Elle consiste à **fixer** un entier $n \geq n_0$ quelconque, à **supposer** que $\mathcal{P}(n)$ est vraie pour cet entier-là, et à **en déduire** que $\mathcal{P}(n+1)$ est vraie. On démontre une implication, pas une vérité.

---

### 3. La méthode : rédiger une récurrence

> **🧭 Méthode — Rédaction type au baccalauréat.**
>
> *Pour tout entier naturel $n \geq n_0$, on note $\mathcal{P}(n)$ la propriété : « ... ».*
>
> **Initialisation.** Pour $n = n_0$ : on calcule séparément chaque membre et on constate que $\mathcal{P}(n_0)$ est vraie.
>
> **Hérédité.** Soit $n \geq n_0$ un entier fixé. On suppose que $\mathcal{P}(n)$ est vraie (hypothèse de récurrence) et on montre que $\mathcal{P}(n+1)$ est vraie, c'est-à-dire que « ... » (on écrit explicitement l'énoncé au rang $n+1$ : c'est **le but**).
> [Calculs utilisant l'hypothèse de récurrence, en signalant où elle sert.]
> Donc $\mathcal{P}(n+1)$ est vraie.
>
> **Conclusion.** La propriété est vraie au rang $n_0$ et héréditaire à partir de ce rang ; par le principe de récurrence, $\mathcal{P}(n)$ est vraie pour tout entier $n \geq n_0$.

Trois conseils d'expert :
1. **Écris le but** (l'énoncé au rang $n+1$) avant de calculer : tu sais où tu vas.
2. **Pars du membre au rang $n+1$** et fais-y apparaître le membre au rang $n$ pour pouvoir utiliser l'hypothèse.
3. **Signale l'utilisation de l'hypothèse** (« d'après l'hypothèse de récurrence... ») : c'est l'endroit où le correcteur regarde en premier. Une hérédité qui n'utilise jamais l'hypothèse de récurrence est presque toujours suspecte.

---

### 4. Exemples résolus

#### Exemple résolu 1 — Les gnomons de Pythagore

**Énoncé.** Démontrer que pour tout entier $n \geq 1$ : $1 + 3 + 5 + \dots + (2n-1) = n^2$.

**Notation.** On écrit aussi cette somme $\displaystyle\sum_{k=1}^{n} (2k-1)$. Le symbole $\sum$ (lire « somme ») est la lettre grecque **sigma majuscule**, notre S de « somme » ; Euler l'utilise dès 1755. On lit : « somme pour $k$ allant de 1 à $n$ de $2k - 1$ ». La lettre $k$ est **muette** : elle parcourt les valeurs $1, 2, \dots, n$ et disparaît du résultat.

**Solution.** Pour $n \geq 1$, soit $\mathcal{P}(n)$ : « $\displaystyle\sum_{k=1}^{n}(2k-1) = n^2$ ».

*Initialisation.* Pour $n = 1$ : la somme ne contient qu'un terme, $2 \times 1 - 1 = 1$, et $1^2 = 1$. $\mathcal{P}(1)$ est vraie.

*Hérédité.* Soit $n \geq 1$ fixé ; on suppose $\mathcal{P}(n)$ vraie. But : $\displaystyle\sum_{k=1}^{n+1}(2k-1) = (n+1)^2$.
$$\sum_{k=1}^{n+1}(2k-1) = \underbrace{\sum_{k=1}^{n}(2k-1)}_{= n^2 \text{ par HR}} + \big(2(n+1) - 1\big) = n^2 + 2n + 1 = (n+1)^2.$$
Donc $\mathcal{P}(n+1)$ est vraie.

*Conclusion.* Par récurrence, $\mathcal{P}(n)$ est vraie pour tout $n \geq 1$.

Remarque : l'hérédité est **exactement** le geste du gnomon : ajouter l'équerre de $2n+1$ cailloux transforme le carré $n \times n$ en carré $(n+1)\times(n+1)$. La récurrence est la version rigoureuse du dessin.

#### Exemple résolu 2 — La somme de Gauss

**Énoncé.** Démontrer que pour tout $n \geq 1$ : $1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$.

**Solution.** Soit $\mathcal{P}(n)$ : « $\displaystyle\sum_{k=1}^n k = \frac{n(n+1)}{2}$ ».

*Initialisation.* $n = 1$ : à gauche $1$, à droite $\frac{1 \times 2}{2} = 1$. Vrai.

*Hérédité.* Supposons $\mathcal{P}(n)$ vraie pour un $n \geq 1$ fixé. But : $\displaystyle\sum_{k=1}^{n+1} k = \frac{(n+1)(n+2)}{2}$.
$$\sum_{k=1}^{n+1} k = \frac{n(n+1)}{2} + (n+1) = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2}.$$
On a factorisé par $(n+1)$ : c'est le réflexe qui fait apparaître la forme voulue.

*Conclusion.* $\mathcal{P}(n)$ est vraie pour tout $n \geq 1$.

> **💡 Le savais-tu ?** Le jeune Carl Friedrich Gauss aurait trouvé cette somme pour $n = 100$ à l'école, en associant $1 + 100$, $2 + 99$, ... : 50 paires de 101, soit 5050. Sa méthode **trouve** la formule ; la récurrence la **vérifie**. Les deux démarches sont complémentaires : la récurrence est très efficace pour démontrer une formule, mais elle ne la devine pas.

#### Exemple résolu 3 — La somme des carrés

**Énoncé.** Démontrer que pour tout $n \geq 1$ : $\displaystyle\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.

**Solution.** *Initialisation.* $n = 1$ : $1^2 = 1$ et $\frac{1 \times 2 \times 3}{6} = 1$. Vrai.

*Hérédité.* Supposons la formule vraie au rang $n$. But : $\displaystyle\sum_{k=1}^{n+1} k^2 = \frac{(n+1)(n+2)(2n+3)}{6}$.
$$\sum_{k=1}^{n+1} k^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)\big[n(2n+1) + 6(n+1)\big]}{6} = \frac{(n+1)(2n^2 + 7n + 6)}{6}.$$
Or $(n+2)(2n+3) = 2n^2 + 3n + 4n + 6 = 2n^2 + 7n + 6$. Donc la somme vaut $\frac{(n+1)(n+2)(2n+3)}{6}$ : c'est le but.

*Conclusion.* La formule est vraie pour tout $n \geq 1$.

**Vérification numérique** : pour $n = 3$, $1 + 4 + 9 = 14$ et $\frac{3 \times 4 \times 7}{6} = 14$. ✓

#### Exemple résolu 4 — Une suite définie par récurrence

**Énoncé.** Soit $(u_n)$ la suite définie par $u_0 = 1$ et, pour tout $n \in \mathbb{N}$, $u_{n+1} = 2u_n + 3$. Calculer les premiers termes, conjecturer une formule explicite et la démontrer.

**Rappel de notation** (chapitre 36) : $(u_n)$ désigne la suite tout entière, $u_n$ (lire « u indice n ») son terme de rang $n$. La relation $u_{n+1} = 2u_n + 3$ est une **relation de récurrence** : chaque terme se calcule à partir du précédent. Le mot « récurrence » désigne donc à la fois une façon de *définir* une suite et une façon de *démontrer* : ce n'est pas un hasard, les deux reposent sur le même « pas à pas ».

**Recherche.** $u_0 = 1$, $u_1 = 5$, $u_2 = 13$, $u_3 = 29$, $u_4 = 61$. On remarque que $u_n + 3$ vaut $4, 8, 16, 32, 64$ : ce sont les $4 \times 2^n$. Conjecture : $u_n = 4 \times 2^n - 3 = 2^{n+2} - 3$.

**Démonstration.** Soit $\mathcal{P}(n)$ : « $u_n = 2^{n+2} - 3$ ».

*Initialisation.* $2^{0+2} - 3 = 4 - 3 = 1 = u_0$. Vrai.

*Hérédité.* Supposons $u_n = 2^{n+2} - 3$ pour un $n$ fixé. But : $u_{n+1} = 2^{n+3} - 3$.
$$u_{n+1} = 2u_n + 3 = 2\left(2^{n+2} - 3\right) + 3 = 2^{n+3} - 6 + 3 = 2^{n+3} - 3.$$

*Conclusion.* Pour tout $n \in \mathbb{N}$, $u_n = 2^{n+2} - 3$.

#### Exemple résolu 5 — Un résultat de divisibilité

**Énoncé.** Démontrer que pour tout $n \in \mathbb{N}$, $4^n - 1$ est divisible par 3.

**Rappel.** « $a$ est divisible par 3 » signifie : il existe un entier $k$ tel que $a = 3k$.

**Solution.** Soit $\mathcal{P}(n)$ : « il existe un entier $k$ tel que $4^n - 1 = 3k$ ».

*Initialisation.* $4^0 - 1 = 0 = 3 \times 0$. Vrai.

*Hérédité.* Supposons qu'il existe un entier $k$ tel que $4^n - 1 = 3k$, c'est-à-dire $4^n = 3k + 1$. Alors
$$4^{n+1} - 1 = 4 \times 4^n - 1 = 4(3k + 1) - 1 = 12k + 3 = 3(4k + 1),$$
et $4k + 1$ est un entier. Donc $4^{n+1} - 1$ est divisible par 3.

*Conclusion.* Pour tout $n$, $3$ divise $4^n - 1$.

L'astuce consiste à **traduire l'hypothèse en égalité** ($4^n = 3k + 1$) pour pouvoir la réinjecter dans un calcul.

#### Exemple résolu 6 — L'inégalité de Bernoulli (démonstration exigible)

> **📐 Propriété — Inégalité de Bernoulli.** Pour tout réel $a > -1$ (en particulier pour tout $a > 0$) et pour tout entier naturel $n$ :
> $$(1 + a)^n \geq 1 + na.$$

**Sens concret.** Place une somme à intérêts composés au taux $a$ (par exemple $a = 0{,}05$ pour 5 %) : au bout de $n$ années, le capital est multiplié par $(1+a)^n$. Avec des intérêts simples, il serait multiplié par $1 + na$. Bernoulli affirme que **les intérêts composés rapportent toujours au moins autant que les intérêts simples** : normal, on gagne aussi des intérêts sur les intérêts.

> **✍️ Démonstration.** Soit $a > -1$ fixé. Pour $n \in \mathbb{N}$, soit $\mathcal{P}(n)$ : « $(1+a)^n \geq 1 + na$ ».
>
> *Initialisation.* $n = 0$ : $(1+a)^0 = 1$ et $1 + 0 \times a = 1$. On a bien $1 \geq 1$.
>
> *Hérédité.* Soit $n \in \mathbb{N}$ fixé ; on suppose $(1+a)^n \geq 1 + na$. But : $(1+a)^{n+1} \geq 1 + (n+1)a$.
> On multiplie les deux membres de l'hypothèse par $1 + a$, qui est **strictement positif** puisque $a > -1$ ; le sens de l'inégalité est conservé :
> $$(1+a)^{n+1} = (1+a)^n (1+a) \geq (1+na)(1+a) = 1 + a + na + na^2 = 1 + (n+1)a + na^2.$$
> Or $na^2 \geq 0$, donc $1 + (n+1)a + na^2 \geq 1 + (n+1)a$. Par transitivité, $(1+a)^{n+1} \geq 1 + (n+1)a$.
>
> *Conclusion.* Pour tout $n \in \mathbb{N}$, $(1+a)^n \geq 1 + na$. $\blacksquare$

Le petit carré noir $\blacksquare$ (ou les lettres « CQFD », *ce qu'il fallait démontrer*, du latin *quod erat demonstrandum*) marque la fin d'une démonstration ; on l'appelle parfois le « tombeau » de Halmos, du nom du mathématicien Paul Halmos qui l'a popularisé.

**Où sert l'hypothèse $a > -1$ ?** Exactement à un endroit : multiplier une inégalité par $1+a$ sans en changer le sens. Si $1 + a$ était négatif, l'inégalité s'inverserait et la preuve s'effondrerait. Exemple : avec $a = -3$ et $n = 3$, $(1-3)^3 = -8$ alors que $1 + 3 \times (-3) = -8$ : égalité de justesse ; avec $n = 5$, $(-2)^5 = -32 < 1 - 15 = -14$. L'inégalité est **fausse**. Une hypothèse n'est jamais décorative.

**Pourquoi cette inégalité est-elle si importante ?** Parce qu'elle permet de minorer une puissance (difficile à manipuler) par une expression **affine** en $n$ (facile). Au chapitre 44, elle montrera que si $q > 1$, alors $q^n$ devient plus grand que n'importe quel nombre : il suffit d'écrire $q = 1 + a$ avec $a > 0$, et $q^n \geq 1 + na$, qui devient aussi grand qu'on veut.

**Application immédiate.** À partir de quel rang a-t-on à coup sûr $1{,}02^n \geq 1000$ ? Bernoulli donne $1{,}02^n \geq 1 + 0{,}02n$, et $1 + 0{,}02n \geq 1000$ dès que $n \geq 49\,950$. On obtient un rang **qui convient** (pas le plus petit : en réalité $1{,}02^n \geq 1000$ dès $n = 349$, ce que l'on saura calculer avec le logarithme au chapitre 48). Une minoration grossière suffit souvent pour prouver qu'un rang existe.

#### Exemple résolu 7 — Une inégalité qui ne démarre pas tout de suite

**Énoncé.** Démontrer que pour tout entier $n \geq 4$ : $2^n \geq n^2$.

**Exploration.**

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $2^n$ | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
| $n^2$ | 0 | 1 | 4 | **9** | 16 | 25 | 36 |

L'inégalité est vraie pour $n = 0, 1, 2$, **fausse pour $n = 3$** ($8 < 9$), puis vraie à partir de $4$. Le rang de départ $n_0 = 4$ n'est pas un caprice.

**Solution.** *Initialisation.* $n = 4$ : $2^4 = 16 \geq 16 = 4^2$. Vrai.

*Hérédité.* Soit $n \geq 4$ ; on suppose $2^n \geq n^2$. But : $2^{n+1} \geq (n+1)^2$.
D'après l'hypothèse, $2^{n+1} = 2 \times 2^n \geq 2n^2$. Il suffit donc de prouver que $2n^2 \geq (n+1)^2$, c'est-à-dire $2n^2 - (n^2 + 2n + 1) \geq 0$, soit $n^2 - 2n - 1 \geq 0$, soit $(n-1)^2 \geq 2$. Comme $n \geq 4$, $(n-1)^2 \geq 9 \geq 2$. Donc $2^{n+1} \geq 2n^2 \geq (n+1)^2$.

*Conclusion.* Pour tout $n \geq 4$, $2^n \geq n^2$.

**Leçon.** On a utilisé $n \geq 4$ (en fait $n \geq 3$ suffirait pour l'hérédité). L'hérédité **seule** est vraie dès $n = 3$, mais l'initialisation à $n = 3$ est fausse : c'est pour cela qu'il faut démarrer à 4.

#### Exemple résolu 8 — Une suite croissante et bornée

**Énoncé.** Soit $(u_n)$ définie par $u_0 = 1$ et $u_{n+1} = \sqrt{2 + u_n}$. Démontrer que pour tout $n \in \mathbb{N}$ : $0 \leq u_n \leq u_{n+1} \leq 2$.

**Idée.** Posons $f(x) = \sqrt{2 + x}$ sur $[-2 ; +\infty[$, de sorte que $u_{n+1} = f(u_n)$. La fonction $f$ est **croissante** (composée de $x \mapsto 2 + x$ croissante et de la racine carrée croissante) : elle **conserve l'ordre**. C'est l'outil-clé.

**Solution.** Soit $\mathcal{P}(n)$ : « $0 \leq u_n \leq u_{n+1} \leq 2$ ».

*Initialisation.* $u_0 = 1$ et $u_1 = \sqrt{3} \approx 1{,}732$. On a bien $0 \leq 1 \leq \sqrt 3 \leq 2$. Vrai.

*Hérédité.* Supposons $0 \leq u_n \leq u_{n+1} \leq 2$. Comme $f$ est croissante sur $[0 ; 2]$, on peut l'appliquer aux quatre membres sans changer l'ordre :
$$f(0) \leq f(u_n) \leq f(u_{n+1}) \leq f(2), \quad \text{soit} \quad \sqrt 2 \leq u_{n+1} \leq u_{n+2} \leq 2.$$
Comme $0 \leq \sqrt 2$, on obtient $0 \leq u_{n+1} \leq u_{n+2} \leq 2$ : c'est $\mathcal{P}(n+1)$.

*Conclusion.* Pour tout $n$, $0 \leq u_n \leq u_{n+1} \leq 2$. La suite est donc **croissante** et **majorée par 2**.

Cette technique — appliquer une fonction croissante à un encadrement — est l'une des plus utilisées au baccalauréat. Retiens-la. Et garde cette suite en mémoire : $u_n$ monte, sans jamais dépasser 2... s'approche-t-elle de 2 ? Rendez-vous au chapitre 44.

#### Exemple résolu 9 — Les dérivées successives

**Énoncé.** Soit $f(x) = x\,e^x$ sur $\mathbb{R}$. On note $f^{(n)}$ la **dérivée $n$-ième** de $f$ (on dérive $n$ fois ; $f^{(0)} = f$, $f^{(1)} = f'$, $f^{(2)} = f''$). Démontrer que pour tout $n \in \mathbb{N}$ : $f^{(n)}(x) = (x + n)\,e^x$.

**Notation.** Les parenthèses dans $f^{(n)}$ sont indispensables : $f^n$ pourrait signifier « $f$ à la puissance $n$ » ou « $f$ composée $n$ fois ». Lagrange avait introduit les primes $f'$, $f''$, $f'''$, mais au-delà de trois primes, on passe aux chiffres entre parenthèses.

**Solution.** *Initialisation.* $f^{(0)}(x) = f(x) = x e^x = (x + 0)e^x$. Vrai.

*Hérédité.* Supposons $f^{(n)}(x) = (x+n)e^x$ pour tout réel $x$. Alors $f^{(n+1)}$ est la dérivée de $f^{(n)}$ ; par la formule du produit $(uv)' = u'v + uv'$ avec $u = x + n$, $v = e^x$ :
$$f^{(n+1)}(x) = 1 \times e^x + (x+n)e^x = (x + n + 1)e^x.$$

*Conclusion.* Pour tout $n$, $f^{(n)}(x) = (x+n)e^x$.

---
