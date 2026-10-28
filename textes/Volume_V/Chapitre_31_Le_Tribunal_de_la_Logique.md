# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 31 : Le Tribunal de la Logique

> *« Au tribunal des mathématiques, aucune éloquence ne sauve un accusé. On n'y juge pas sur l'air sincère du témoin ni sur le nombre de ceux qui le croient : on y juge sur la preuve. Un seul contre-exemple suffit à condamner une affirmation, mais mille exemples ne suffisent pas à l'innocenter. »*

---

### Ce que tu vas découvrir

- Les grandes **familles de nombres** ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{D}$, $\mathbb{Q}$, $\mathbb{R}$), emboîtées comme des poupées russes, et pourquoi chacune a dû être inventée.
- Le langage des **ensembles** et des **intervalles** : $\in$, $\subset$, $\cup$, $\cap$, $[a\,;b[$, $+\infty$… et comment les lire à voix haute.
- La **valeur absolue**, qui mesure une distance sans se soucier du sens.
- Les règles du **tribunal** : implication, réciproque, contraposée, équivalence, quantificateurs « pour tout » et « il existe ».
- Les quatre grandes **armes de la preuve** : le raisonnement direct, le contre-exemple, la contraposée et le raisonnement par l'absurde — avec les démonstrations exigibles de Seconde ($\frac13$ n'est pas décimal, $\sqrt2$ est irrationnel, le carré d'un impair est impair…).

---

### 1. Le problème : la formule qui mentait quarante fois de suite

Imagine une salle d'audience. Sur le banc des accusés, il n'y a pas un homme, mais une **phrase**. Elle a été apportée par un élève enthousiaste, qui la défend avec passion :

> « Pour tout entier naturel $n$, le nombre $n^2 + n + 41$ est un nombre premier. »

L'avocat de la défense appelle les témoins à la barre, un par un.

| $n$ | $n^2+n+41$ | Premier ? |
|---|---|---|
| 0 | 41 | oui |
| 1 | 43 | oui |
| 2 | 47 | oui |
| 3 | 53 | oui |
| 4 | 61 | oui |
| 5 | 71 | oui |
| 10 | 151 | oui |
| 20 | 461 | oui |
| 30 | 971 | oui |
| 39 | 1601 | oui |

Quarante témoins ($n = 0, 1, 2, \dots, 39$) défilent, et **tous** confirment : le nombre obtenu est premier. Le public est convaincu. Le jury s'apprête à acquitter.

Alors le procureur se lève, très calme, et appelle un seul témoin : $n = 40$.

$$40^2 + 40 + 41 = 1600 + 40 + 41 = 1681 = 41 \times 41.$$

$1681$ n'est **pas** premier. La phrase est **fausse**. Le verdict tombe, sans appel.

> **💡 Le savais-tu ?** Ce polynôme a été remarqué par **Leonhard Euler** en 1772. Il produit des nombres premiers pour $n$ allant de $0$ à $39$ — un record étonnant — mais il échoue à $n = 40$. On peut d'ailleurs le voir sans calcul : pour $n = 41$, $41^2 + 41 + 41 = 41 \times 43$, divisible par $41$ de façon évidente.

Cette histoire résume tout ce chapitre :

1. **Vérifier des cas, même nombreux, ne prouve rien** pour une affirmation qui parle de *tous* les entiers.
2. **Un seul contre-exemple suffit** à démolir une affirmation universelle.
3. Pour *établir* une vérité générale, il faut un autre outil : la **démonstration**.

Au collège, tu as souvent « vu » qu'une propriété marchait sur des exemples. À partir de la Seconde, tu entres au tribunal. Il te faut un langage précis (de quels nombres parle-t-on ? que veut dire « si… alors » ?) et des méthodes de preuve. C'est ce que nous allons construire.

> **🔍 L'histoire vraie —** Vers 350 av. J.-C., **Aristote** fonde la logique en étudiant les *syllogismes* : « Tous les hommes sont mortels ; Socrate est un homme ; donc Socrate est mortel. » Plus de deux mille ans plus tard, en 1847 et 1854, l'Anglais **George Boole**, fils de cordonnier et largement autodidacte, transforme la logique en *calcul* : le vrai devient $1$, le faux $0$, « et » devient une multiplication. Sans le savoir, il vient d'écrire la grammaire de tous les ordinateurs du XXᵉ siècle.

---

### 2. Les familles de nombres : une histoire de crises

Chaque famille de nombres est née d'une **opération impossible**. Quand les outils existants ne suffisaient plus, il a fallu agrandir le monde des nombres.

#### 2.1 Les entiers naturels $\mathbb{N}$ : compter les cailloux

Les premiers nombres sont ceux du berger qui compte ses moutons : $0, 1, 2, 3, \dots$

> **📐 Définition —** L'ensemble des **entiers naturels** est
> $$\mathbb{N} = \{0\,;1\,;2\,;3\,;\dots\}.$$

**Notation expliquée.**
- Les **accolades** $\{\ \}$ servent à écrire un ensemble en donnant la liste de ses éléments. On lit « l'ensemble des éléments $0$, $1$, $2$… ». En France, on sépare les éléments par des points-virgules, pour ne pas confondre avec la virgule décimale.
- La lettre $\mathbb{N}$ vient de *naturale* (italien) : c'est **Giuseppe Peano** qui l'utilise en 1889. Le style « double barre » (on dit *gras de tableau*, ou *blackboard bold*) est né au tableau noir : il est difficile d'écrire une lettre en gras à la craie, alors on double un trait. Il s'est imposé dans les livres au milieu du XXᵉ siècle.
- On lit « $\mathbb{N}$ » tout simplement « N ».

Dans $\mathbb{N}$, on peut toujours additionner et multiplier. Mais **soustraire** pose problème : $3 - 5$ n'a pas de réponse dans $\mathbb{N}$.

#### 2.2 Les entiers relatifs $\mathbb{Z}$ : les dettes du marchand

Souviens-toi de l'ardoise du marchand (chapitre 14) : pour noter une dette, il faut des nombres négatifs.

> **📐 Définition —** L'ensemble des **entiers relatifs** est
> $$\mathbb{Z} = \{\dots\,;-3\,;-2\,;-1\,;0\,;1\,;2\,;3\,;\dots\}.$$

La lettre $\mathbb{Z}$ vient de l'allemand ***Zahlen*** (« les nombres »), en usage chez Dedekind et les mathématiciens allemands du XIXᵉ siècle. Dans $\mathbb{Z}$, on soustrait toujours. Mais on ne **divise** pas toujours : $7 \div 2$ n'est pas un entier.

#### 2.3 Les décimaux $\mathbb{D}$ : les dixièmes de Stevin

Le marchand qui pèse des épices a besoin de $2{,}35$ kg. Simon Stevin (chapitre 11) a popularisé ces nombres à virgule.

> **📐 Définition —** Un nombre est **décimal** s'il peut s'écrire sous la forme
> $$\frac{a}{10^n} \quad \text{avec } a \in \mathbb{Z} \text{ et } n \in \mathbb{N}.$$
> L'ensemble des décimaux se note $\mathbb{D}$.

Autrement dit : un décimal est un nombre qui s'écrit avec un nombre **fini** de chiffres après la virgule. Exemples : $2{,}35 = \frac{235}{10^2}$ ; $-0{,}007 = \frac{-7}{10^3}$ ; $12 = \frac{12}{10^0}$ (tout entier est décimal).

Le symbole $\in$ se lit « **appartient à** ». « $a \in \mathbb{Z}$ » signifie « $a$ est un élément de $\mathbb{Z}$ », c'est-à-dire « $a$ est un entier relatif ». Ce symbole est une version stylisée de la lettre grecque epsilon $\varepsilon$, initiale de ἐστί (*esti*, « est ») : c'est encore **Peano** qui l'introduit en 1889. Son contraire, $\notin$, se lit « n'appartient pas à ».

Tout semble aller pour le mieux… jusqu'au jour où l'on partage une galette en **trois**.

#### 2.4 Les rationnels $\mathbb{Q}$ : le partage en trois

> **📐 Définition —** Un nombre est **rationnel** s'il peut s'écrire sous la forme
> $$\frac{p}{q} \quad \text{avec } p \in \mathbb{Z} \text{ et } q \in \mathbb{N},\ q \neq 0.$$
> L'ensemble des rationnels se note $\mathbb{Q}$ (initiale de *quotient*, proposée par Peano en 1895).

Le mot « rationnel » vient du latin *ratio*, « rapport » : un rationnel est un **rapport** de deux entiers. Il n'a rien à voir avec le fait d'être « raisonnable »… même si l'histoire va jouer sur ce double sens.

La question naturelle : $\frac13$ est rationnel, mais est-il décimal ? Ta calculatrice affiche $0{,}333333333$, ce qui *ressemble* à un décimal. Mais l'écran est trop petit pour être honnête. Voici le premier procès du chapitre.

> **✍️ Démonstration (exigible) — $\frac13$ n'est pas un nombre décimal.**
>
> Raisonnons **par l'absurde** : supposons que $\frac13$ soit décimal. Il existerait alors un entier $a$ et un entier naturel $n$ tels que
> $$\frac13 = \frac{a}{10^n}.$$
> En multipliant les deux membres par $3 \times 10^n$, on obtient
> $$10^n = 3a.$$
> Ainsi $10^n$ serait un multiple de $3$. Or la somme des chiffres de $10^n$ (un « 1 » suivi de $n$ zéros) vaut $1$, qui n'est pas divisible par $3$ ; d'après le critère de divisibilité par 3, $10^n$ n'est **pas** un multiple de $3$.
>
> (Autre argument : $10^n = 2^n \times 5^n$ ; sa décomposition en facteurs premiers ne contient que des $2$ et des $5$, jamais de $3$.)
>
> On aboutit à une contradiction. L'hypothèse de départ est donc fausse : $\frac13 \notin \mathbb{D}$. $\blacksquare$

Le petit carré noir $\blacksquare$ marque la fin d'une démonstration. Les Anciens écrivaient « **CQFD** » : « ce qu'il fallait démontrer » (en latin *QED*, *quod erat demonstrandum*).

> **💡 Le savais-tu ?** Une fraction irréductible $\frac{p}{q}$ est décimale si et seulement si son dénominateur $q$ ne contient que des facteurs premiers $2$ et $5$. Ainsi $\frac{7}{40} = \frac{7}{2^3 \times 5} = 0{,}175$ est décimal, mais $\frac{1}{6} = \frac{1}{2 \times 3}$ ne l'est pas. Tous les rationnels ont une écriture décimale soit **finie**, soit **périodique** à partir d'un certain rang : $\frac{1}{7} = 0{,}\overline{142857}$ (la barre indique le bloc qui se répète indéfiniment).

#### 2.5 Les réels $\mathbb{R}$ : la diagonale qui brise la secte

Tu connais déjà ce drame (chapitre 19, *Le Secret interdit des Pythagoriciens*). La diagonale d'un carré de côté $1$ mesure $\sqrt2$, d'après Pythagore : $d^2 = 1^2 + 1^2 = 2$. Les Pythagoriciens croyaient que « tout est nombre », c'est-à-dire que toute longueur est un rapport d'entiers. La diagonale les a trahis. Nous allons maintenant rédiger la preuve avec la rigueur exigée au lycée. Nous avons d'abord besoin d'un petit lemme (un *lemme* est un résultat intermédiaire, une marche d'escalier vers le théorème).

> **✍️ Démonstration (exigible) — Le carré d'un nombre impair est impair.**
>
> Soit $n$ un entier impair. Par définition, il existe un entier $k$ tel que $n = 2k + 1$. Alors
> $$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.$$
> Comme $2k^2 + 2k$ est un entier, que l'on peut appeler $k'$, on a $n^2 = 2k' + 1$ : $n^2$ est impair. $\blacksquare$

De même, le carré d'un nombre pair $n = 2k$ est $n^2 = 4k^2 = 2(2k^2)$, pair.

> **📐 Conséquence (par contraposée) —** Si $n^2$ est pair, alors $n$ est pair.
>
> En effet, si $n$ n'était pas pair, il serait impair, et son carré serait impair d'après le lemme. Nous reviendrons en détail sur ce type de raisonnement (la contraposée) au paragraphe 6.

> **✍️ Démonstration (exigible) — $\sqrt2$ est irrationnel.**
>
> Raisonnons par l'absurde. Supposons que $\sqrt2$ soit rationnel. On peut alors l'écrire sous forme d'une **fraction irréductible** :
> $$\sqrt2 = \frac{p}{q}, \quad p \in \mathbb{N},\ q \in \mathbb{N}^*,\ \text{$p$ et $q$ sans diviseur commun autre que 1.}$$
> En élevant au carré : $2 = \dfrac{p^2}{q^2}$, donc
> $$p^2 = 2q^2.$$
> 1. $p^2$ est donc pair. D'après la conséquence ci-dessus, $p$ est pair : il existe un entier $k$ tel que $p = 2k$.
> 2. En remplaçant : $(2k)^2 = 2q^2$, soit $4k^2 = 2q^2$, soit $q^2 = 2k^2$. Donc $q^2$ est pair, et $q$ est pair.
> 3. Ainsi $p$ et $q$ sont tous deux pairs : ils ont $2$ comme diviseur commun. Cela **contredit** le fait que la fraction $\frac{p}{q}$ est irréductible.
>
> L'hypothèse « $\sqrt2$ est rationnel » mène à une absurdité : elle est fausse. Donc $\sqrt2 \notin \mathbb{Q}$. $\blacksquare$

La notation $\mathbb{N}^*$ (« N étoile ») désigne $\mathbb{N}$ privé de $0$. De même $\mathbb{R}^*$ désigne les réels non nuls.

> **📐 Définition —** L'ensemble des **nombres réels**, noté $\mathbb{R}$, est l'ensemble de toutes les abscisses des points d'une droite graduée. Un réel qui n'est pas rationnel est dit **irrationnel**.

Exemples d'irrationnels : $\sqrt2$, $\sqrt3$, $\pi$ (prouvé par Lambert en 1761), $\sqrt2 + 1$ (voir exercice 11).

#### 2.6 Les poupées russes : l'inclusion $\subset$

Tout entier naturel est un entier relatif ; tout relatif est décimal ; tout décimal est rationnel ($\frac{a}{10^n}$ est un quotient d'entiers) ; tout rationnel est réel.

> **📐 Définition —** On dit qu'un ensemble $A$ est **inclus** dans un ensemble $B$, et on note $A \subset B$, si tout élément de $A$ est aussi un élément de $B$. On lit « $A$ est inclus dans $B$ » ou « $A$ est une partie de $B$ ».

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R}$$

```
 ┌──────────────────────────────────────────────────────────┐
 │ R                                    √2     π    -√3     │
 │   ┌───────────────────────────────────────────┐          │
 │   │ Q                       1/3     -2/7      │          │
 │   │   ┌──────────────────────────────┐        │          │
 │   │   │ D            0,25    -1,7    │        │          │
 │   │   │   ┌──────────────────┐       │        │          │
 │   │   │   │ Z        -3  -1  │       │        │          │
 │   │   │   │   ┌──────────┐   │       │        │          │
 │   │   │   │   │ N  0 1 7 │   │       │        │          │
 │   │   │   │   └──────────┘   │       │        │          │
 │   │   │   └──────────────────┘       │        │          │
 │   │   └──────────────────────────────┘        │          │
 │   └───────────────────────────────────────────┘          │
 └──────────────────────────────────────────────────────────┘
```

Chaque inclusion est **stricte** : $-1 \in \mathbb{Z}$ mais $-1 \notin \mathbb{N}$ ; $0{,}5 \in \mathbb{D}$ mais $0{,}5 \notin \mathbb{Z}$ ; $\frac13 \in \mathbb{Q}$ mais $\frac13 \notin \mathbb{D}$ ; $\sqrt2 \in \mathbb{R}$ mais $\sqrt2 \notin \mathbb{Q}$.

> **⚠️ Attention, piège !** Ne confonds pas $\in$ et $\subset$.
> - $\in$ relie un **élément** à un **ensemble** : $3 \in \mathbb{N}$.
> - $\subset$ relie **deux ensembles** : $\{3\} \subset \mathbb{N}$, $\mathbb{N} \subset \mathbb{Z}$.
>
> Écrire « $3 \subset \mathbb{N}$ » ou « $\mathbb{N} \in \mathbb{Z}$ » est une faute de grammaire mathématique.

> **⚠️ Attention, piège !** Un nombre peut avoir plusieurs déguisements. $\frac{12}{4}$ a l'air d'une fraction, mais c'est $3$, un entier naturel. $\sqrt{9} = 3 \in \mathbb{N}$, $\sqrt{\frac{4}{9}} = \frac23 \in \mathbb{Q}$, $\frac{21}{75} = \frac{7}{25} = 0{,}28 \in \mathbb{D}$. Il faut toujours **simplifier** avant de juger.

> **Exemple résolu 1 — Classer des nombres.**
> Pour chaque nombre, donner le plus petit ensemble parmi $\mathbb{N}, \mathbb{Z}, \mathbb{D}, \mathbb{Q}, \mathbb{R}$ qui le contient :
> $$a = -\frac{18}{6},\quad b = \frac{3}{8},\quad c = \frac{5}{12},\quad d = \sqrt{16} - \sqrt{2},\quad e = (\sqrt{5})^2,\quad f = \frac{\pi}{2\pi}.$$
>
> - $a = -3$ : $a \in \mathbb{Z}$, et $a \notin \mathbb{N}$. Plus petit ensemble : $\mathbb{Z}$.
> - $b = \frac{3}{8} = \frac{3}{2^3}$ : dénominateur avec seulement des 2, donc décimal : $b = \frac{375}{1000} = 0{,}375$. Plus petit ensemble : $\mathbb{D}$.
> - $c = \frac{5}{12} = \frac{5}{2^2 \times 3}$, irréductible avec un facteur 3 au dénominateur : $c \in \mathbb{Q}$, $c \notin \mathbb{D}$. (On vérifie : $c = 0{,}41666\dots$)
> - $d = 4 - \sqrt2$. Si $d$ était rationnel, alors $\sqrt2 = 4 - d$ serait rationnel (différence de deux rationnels), ce qui est faux. Donc $d \in \mathbb{R}$, irrationnel.
> - $e = 5$ : $\mathbb{N}$.
> - $f = \frac12 = 0{,}5$ : $\mathbb{D}$. Le $\pi$ disparaît : ne te laisse pas impressionner par l'apparence !

---

### 3. Le langage des ensembles et des intervalles

#### 3.1 Décrire un ensemble

Il y a deux façons de décrire un ensemble :
- **en extension** : on donne la liste de ses éléments, $A = \{1\,;3\,;5\,;7\}$ ;
- **en compréhension** : on donne une propriété caractéristique, $A = \{x \in \mathbb{N} \mid x \text{ impair et } x < 8\}$.

La barre verticale $\mid$ (on trouve aussi « : » ou « ; ») se lit « **tel que** ». La phrase se lit : « l'ensemble des $x$ appartenant à $\mathbb{N}$ tels que $x$ est impair et strictement inférieur à $8$ ».

L'**ensemble vide**, qui ne contient aucun élément, se note $\varnothing$. Ce symbole a été introduit par **André Weil** (groupe Bourbaki) vers 1939, inspiré de la lettre norvégienne Ø. Attention : $\varnothing$ n'est pas $\{0\}$ ! $\{0\}$ contient un élément, le nombre zéro ; $\varnothing$ n'en contient aucun. Une boîte vide n'est pas une boîte contenant un zéro.

#### 3.2 Union, intersection, complémentaire

Soient $A$ et $B$ deux parties d'un ensemble $E$.

> **📐 Définitions —**
> - L'**intersection** $A \cap B$ (lire « $A$ inter $B$ ») est l'ensemble des éléments qui sont dans $A$ **et** dans $B$.
> - La **réunion** (ou union) $A \cup B$ (lire « $A$ union $B$ ») est l'ensemble des éléments qui sont dans $A$ **ou** dans $B$ (ou dans les deux).
> - Le **complémentaire** de $A$ dans $E$, noté $\overline{A}$ ou $E \setminus A$, est l'ensemble des éléments de $E$ qui **ne sont pas** dans $A$. Le symbole $\setminus$ se lit « privé de ».
> - $A$ et $B$ sont **disjoints** si $A \cap B = \varnothing$.

Pour retenir : $\cap$ ressemble à un « n » renversé… et à un pont étroit où ne passent que ceux qui ont les deux tickets ; $\cup$ ressemble à une coupe large, un **U** comme « **U**nion », qui recueille tout.

```
        A ∩ B                        A ∪ B
     ┌───────┐                    ┌───────┐
     │ A  ┌──┼────┐               │███████│████┐
     │    │██│    │               │███┌───┼────┤
     └────┼──┘  B │               └───┼███████B│
          └───────┘                   └────────┘
   (seule la zone commune)        (tout ce qui est colorié)
```

> **Exemple résolu 2 — Opérations sur des ensembles finis.**
> $E = \{1\,;2\,;\dots\,;12\}$, $A$ = ensemble des multiples de 2 dans $E$, $B$ = ensemble des multiples de 3 dans $E$.
> - $A = \{2\,;4\,;6\,;8\,;10\,;12\}$, $B = \{3\,;6\,;9\,;12\}$.
> - $A \cap B = \{6\,;12\}$ : ce sont les multiples de $6$.
> - $A \cup B = \{2\,;3\,;4\,;6\,;8\,;9\,;10\,;12\}$ (on ne répète pas 6 et 12).
> - $\overline{A \cup B} = \{1\,;5\,;7\,;11\}$ : les nombres de $E$ divisibles ni par 2 ni par 3.
> - Vérification des effectifs : $\text{card}(A \cup B) = \text{card}(A) + \text{card}(B) - \text{card}(A \cap B) = 6 + 4 - 2 = 8$. (Le *cardinal*, noté $\text{card}$, est le nombre d'éléments.)

#### 3.3 Les intervalles de $\mathbb{R}$

Sur la droite des réels, les ensembles les plus utiles sont des **morceaux de droite sans trou** : les intervalles.

> **📐 Définition —** Soient $a$ et $b$ deux réels avec $a < b$.
>
> | Notation | Ensemble des réels $x$ tels que | Lecture | Représentation |
> |---|---|---|---|
> | $[a\,;b]$ | $a \le x \le b$ | intervalle fermé $a$, $b$ | `[■■■■■■]` |
> | $]a\,;b[$ | $a < x < b$ | intervalle ouvert $a$, $b$ | `]■■■■■■[` |
> | $[a\,;b[$ | $a \le x < b$ | fermé en $a$, ouvert en $b$ | `[■■■■■■[` |
> | $]a\,;b]$ | $a < x \le b$ | ouvert en $a$, fermé en $b$ | `]■■■■■■]` |
> | $[a\,;+\infty[$ | $x \ge a$ | $a$, plus l'infini | `[■■■■■■→` |
> | $]a\,;+\infty[$ | $x > a$ | | `]■■■■■■→` |
> | $]-\infty\,;b]$ | $x \le b$ | moins l'infini, $b$ | `←■■■■■■]` |
> | $]-\infty\,;b[$ | $x < b$ | | `←■■■■■■[` |
>
> On a aussi $\mathbb{R} = ]-\infty\,;+\infty[$. Les réels $a$ et $b$ sont les **bornes** de l'intervalle ; $b - a$ est sa **longueur** (ou amplitude).

**Pourquoi ces crochets ?** La convention française est visuelle : le crochet **tourné vers l'intérieur** « attrape » la borne (elle est incluse) ; le crochet **tourné vers l'extérieur** la « repousse » (elle est exclue). Dans beaucoup de pays anglo-saxons, on écrit plutôt $(a, b)$ pour l'intervalle ouvert — ne t'en étonne pas si tu lis un livre étranger. On met un **point-virgule** entre les bornes pour éviter toute confusion avec la virgule décimale : $[1{,}5\,;2]$.

**Le symbole $\infty$** (« infini ») a été introduit par l'Anglais **John Wallis** en 1655. Il n'est **pas un nombre** : c'est une façon de dire « sans limite de ce côté ». C'est pourquoi le crochet est **toujours ouvert** du côté de $+\infty$ ou de $-\infty$ : on ne peut pas « atteindre » l'infini, donc on ne peut pas l'inclure.

> **⚠️ Attention, piège !**
> - $[3\,;+\infty]$ est **incorrect** : le crochet doit être ouvert en $+\infty$.
> - $[5\,;2]$ n'a pas de sens : on écrit toujours la plus petite borne à gauche.
> - $]2\,;2[ = \varnothing$, mais $[2\,;2] = \{2\}$ (un seul point).
> - L'intervalle $[1\,;3]$ contient une **infinité** de réels ($1{,}5$, $\sqrt2$, $2{,}999$…), pas seulement $1, 2, 3$ ! Ne confonds pas avec l'ensemble d'entiers $\{1\,;2\,;3\}$, qu'on note parfois $[\![1\,;3]\!]$.

**Notations utiles :** $\mathbb{R}_+ = [0\,;+\infty[$ (réels positifs ou nuls), $\mathbb{R}_- = ]-\infty\,;0]$, $\mathbb{R}^*_+ = ]0\,;+\infty[$ (strictement positifs), $\mathbb{R}^* = \mathbb{R} \setminus \{0\} = ]-\infty\,;0[ \cup ]0\,;+\infty[$.

> **Exemple résolu 3 — Intersection et réunion d'intervalles.**
> Soient $I = [-2\,;5[$ et $J = ]1\,;+\infty[$. Déterminer $I \cap J$ et $I \cup J$.
>
> On dessine les deux intervalles l'un sous l'autre :
> ```
>          -2        1         5
>   I :     [■■■■■■■■■■■■■■■■■■[
>   J :               ]■■■■■■■■■■■■■■■■■■■■■→
>   I∩J:              ]■■■■■■■■[
>   I∪J:    [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■→
> ```
> - $I \cap J$ : il faut être à la fois $\ge -2$, $< 5$ et $> 1$. La contrainte la plus forte à gauche est $x > 1$, à droite $x < 5$. Donc $I \cap J = ]1\,;5[$.
> - $I \cup J$ : il suffit d'être dans l'un des deux. On couvre tout depuis $-2$ (inclus) jusqu'à $+\infty$. Donc $I \cup J = [-2\,;+\infty[$.

> **Exemple résolu 4 — Traduire une inéquation en intervalle.**
> Résoudre dans $\mathbb{R}$ : $-3 < 2x + 1 \le 7$, et donner l'ensemble des solutions sous forme d'intervalle.
>
> On soustrait $1$ aux trois membres : $-4 < 2x \le 6$. On divise par $2$, qui est **positif** (l'ordre est conservé) : $-2 < x \le 3$.
> L'ensemble des solutions est $S = ]-2\,;3]$.

> **Exemple résolu 5 — Une réunion qui ne se simplifie pas.**
> Résoudre $x^2 > 9$ dans $\mathbb{R}$.
>
> $x^2 > 9 \iff x^2 - 9 > 0 \iff (x-3)(x+3) > 0$. Un produit de deux facteurs est strictement positif lorsque les deux facteurs sont de même signe. Tableau de signes :
>
> | $x$ | $-\infty$ | | $-3$ | | $3$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $x+3$ | | $-$ | $0$ | $+$ | | $+$ | |
> | $x-3$ | | $-$ | | $-$ | $0$ | $+$ | |
> | produit | | $+$ | $0$ | $-$ | $0$ | $+$ | |
>
> Donc $S = ]-\infty\,;-3[ \cup ]3\,;+\infty[$. Cette réunion de deux intervalles disjoints **n'est pas** un intervalle : il y a un « trou » entre $-3$ et $3$.
>
> ⚠️ L'erreur classique « $x^2 > 9 \iff x > 3$ » oublie toute la partie négative : $x = -4$ vérifie bien $(-4)^2 = 16 > 9$.

