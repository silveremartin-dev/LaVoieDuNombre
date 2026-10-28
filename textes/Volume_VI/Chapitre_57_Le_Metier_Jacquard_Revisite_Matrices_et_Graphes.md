# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 57 : Le Métier Jacquard Revisité : Matrices et Graphes

> *« En 1801 à Lyon, Joseph Marie Jacquard perfore des cartons pour commander les fils de soie de son métier à tisser : une grille de trous orchestre la montée et la descente des navettes pour faire émerger des motifs d'une infinie complexité. Les matrices sont les cartons Jacquard de l'algèbre moderne : des grilles de nombres capables de déformer l'espace, de compter les trajectoires d'un réseau et de prédire l'équilibre futur des flux du monde. »*

---

### Ce que tu vas découvrir

- Comment une **matrice** encapsule un tableau d'opérations et transforme des vecteurs par le produit ligne $\times$ colonne.
- Pourquoi la multiplication des matrices est associative mais **non commutative** ($AB \neq BA$), et comment fonctionne la matrice identité $I_n$.
- Le calcul de l'**inverse d'une matrice $2 \times 2$** grâce au déterminant et la résolution instantanée de systèmes linéaires $AX = B$.
- La modélisation des réseaux par les **graphes** et la **matrice d'adjacence**.
- Le théorème fondamental qui démontre pourquoi la puissance $k$-ième d'une matrice d'adjacence $M^k$ compte exactement le **nombre de chemins de longueur $k$**.
- Les **chaînes de Markov** et les graphes probabilistes : calcul de l'**état stable** et les fondements de l'algorithme PageRank de Google.

---

### 1. Le problème : Les réseaux du monde et les tableaux de commande

#### 1.1 Le vol des compagnies aériennes
Considérons une petite compagnie aérienne desservant quatre villes : Paris (P), Londres (L), Madrid (M) et Rome (R).
Les liaisons directes quotidiennes sont les suivantes :
- De Paris vers Londres, Madrid et Rome.
- De Londres vers Paris et Madrid.
- De Madrid vers Paris et Rome.
- De Rome vers Paris uniquement.

Si un voyageur veut partir de Londres pour aller à Rome, il n'existe aucun vol direct. Mais peut-il s'y rendre avec **exactement une escale** (un trajet en deux vols) ? Et avec deux escales ?
Combien y a-t-il d'itinéraires possibles ?

Si l'on cherche à la main, on s'égare rapidement dans l'arborescence des bifurcations. Mais si l'on consigne ces liaisons dans une **grille binaire** (1 s'il y a un vol, 0 sinon), et qu'on multiplie cette grille par elle-même, un miracle se produit : **le calcul matriciel dénombre instantanément l'ensemble de tous les chemins possibles sur n'importe quel réseau !**

#### 1.2 La météo et les prédictions à long terme
Dans une région côtière, on observe le temps jour après jour.
- S'il fait beau aujourd'hui, il y a 80 % de chances qu'il fasse beau demain, et 20 % de chances qu'il pleuve.
- S'il pleut aujourd'hui, il y a 40 % de chances qu'il fasse beau demain, et 60 % de chances qu'il pleuve.

Quel temps fera-t-il dans une semaine ? Dans un an ?
Existe-t-il un climat moyen d'équilibre (par exemple 65 % de beaux jours et 35 % de jours pluvieux) vers lequel le système converge inévitablement, quel que soit le temps qu'il fait aujourd'hui ?
Pour répondre à cette question, nous devons croiser la théorie des probabilités avec l'algèbre des matrices : c'est la théorie des **chaînes de Markov**.

---

### 2. L'Objet Matrice et ses Opérations

#### 2.1 Définition d'une matrice

> **📐 Définition — Matrice**
> Soient $n$ et $p$ deux entiers naturels non nuls.
> Une **matrice** de dimension (ou taille) $n \times p$ (lire « $n$ lignes, $p$ colonnes ») à coefficients réels est un tableau rectangulaire de nombres disposés en $n$ lignes et $p$ colonnes :
>
> $$A = \begin{pmatrix}
> a_{1,1} & a_{1,2} & \dots & a_{1,p} \\
> a_{2,1} & a_{2,2} & \dots & a_{2,p} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n,1} & a_{n,2} & \dots & a_{n,p}
> \end{pmatrix} = (a_{i,j})_{\substack{1 \leq i \leq n \\ 1 \leq j \leq p}}$$
>
> Le coefficient $a_{i,j}$ est situé à l'intersection de la $i$-ième ligne et de la $j$-ième colonne.
> L'ensemble des matrices de taille $n \times p$ à coefficients réels est noté $\mathcal{M}_{n,p}(\mathbb{R})$.

*Vocabulaire :*
- Si $n = p$, la matrice est dite **carrée** d'ordre $n$. L'ensemble est noté $\mathcal{M}_n(\mathbb{R})$.
- Si $n = 1$, c'est une **matrice ligne** : $(x_1 \ x_2 \ \dots \ x_p)$.
- Si $p = 1$, c'est une **matrice colonne** : $\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$.
- La **matrice nulle** (notée $0_{n,p}$) a tous ses coefficients nuls.

#### 2.2 Addition et multiplication par un nombre réel
- **Addition :** Si $A$ et $B$ ont la **même dimension** $n \times p$, la somme $A + B$ s'obtient en additionnant les coefficients correspondants :
  $$(A + B)_{i,j} = a_{i,j} + b_{i,j}$$
- **Multiplication par un scalaire $\lambda \in \mathbb{R}$ :** On multiplie chaque case par $\lambda$ :
  $$(\lambda A)_{i,j} = \lambda a_{i,j}$$

#### 2.3 Le produit matriciel : Ligne par Colonne
La multiplication de deux matrices n'est **pas** une multiplication case par case ! Elle traduit la composition de transformations linéaires.

> **📐 Définition — Produit matriciel**
> Soit $A$ une matrice de taille $n \times \mathbf{k}$ et $B$ une matrice de taille $\mathbf{k} \times p$.
> *(Le nombre de colonnes de $A$ doit impérativement être égal au nombre de lignes de $B$ !)*
> Le produit $C = A \times B$ est une matrice de taille $n \times p$ dont le terme général $c_{i,j}$ est le produit scalaire de la **$i$-ième ligne de $A$** par la **$j$-ième colonne de $B$** :
>
> $$c_{i,j} = \sum_{m=1}^k a_{i,m} \cdot b_{m,j} = a_{i,1}b_{1,j} + a_{i,2}b_{2,j} + \dots + a_{i,k}b_{k,j}$$

```
                Ligne i de A : ( a_i,1   a_i,2  ...  a_i,k )
                                      │
                                      ▼
                Colonne j de B : ┌ b_1,j ┐
                                 │ b_2,j │
                                 │  ...  │
                                 └ b_k,j ┘
                                      │
                                      ▼
  c_i,j = a_i,1 · b_1,j + a_i,2 · b_2,j + ... + a_i,k · b_k,j
```

*Exemple fondamental en dimension $2 \times 2$ :*
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x & y \\ z & t \end{pmatrix} = \begin{pmatrix} ax + bz & ay + bt \\ cx + dz & cy + dt \end{pmatrix}$$

#### 2.4 Propriétés et pièges de la multiplication matricielle

> **⚠️ Attention, piège ! — Non-commutativité en général**
> Pour deux matrices carrées $A$ et $B$, en général :
> $$\mathbf{A B \neq B A}$$
> *Exemple :*
> $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ et $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
> $AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ alors que $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ !
> Elles ne commutent pas. Par conséquent, les identités remarquables comme $(A+B)^2 = A^2 + 2AB + B^2$ sont **fausses** pour les matrices (on a $(A+B)^2 = A^2 + AB + BA + B^2$).

> **⚠️ Deuxième piège — Diviseurs de zéro**
> Pour des réels, $ab = 0 \implies a = 0 \text{ ou } b = 0$.
> **C'est faux pour les matrices !**
> Prenons $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ :
> $$A^2 = A \times A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0_2$$
> Le produit de deux matrices non nulles peut être la matrice nulle !

#### 2.5 Matrice identité et puissances
La **matrice identité** d'ordre $n$, notée $I_n$, comporte des 1 sur sa diagonale principale et des 0 partout ailleurs :
$$I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
Pour toute matrice carrée $A \in \mathcal{M}_n(\mathbb{R})$ :
$$A \times I_n = I_n \times A = A$$
Pour tout entier $k \in \mathbb{N}$, on définit la puissance $A^k$ par $A^0 = I_n$ et $A^k = \underbrace{A \times A \times \dots \times A}_{k \text{ facteurs}}$.

---

### 3. Matrice Inverse et Systèmes Linéaires

#### 3.1 Définition de l'inversibilité

> **📐 Définition — Matrice inversible**
> Une matrice carrée $A \in \mathcal{M}_n(\mathbb{R})$ est dite **inversible** s'il existe une matrice carrée $B \in \mathcal{M}_n(\mathbb{R})$ telle que :
> $$A B = B A = I_n$$
> Si une telle matrice existe, elle est unique. On l'appelle la **matrice inverse** de $A$ et on la note **$A^{-1}$**.

*(⚠️ Il n'existe pas de « division » matricielle $\frac{B}{A}$ ! On multiplie par l'inverse $A^{-1}$, en veillant scrupuleusement à multiplier à gauche ou à droite).*

#### 3.2 Inversion des matrices de taille $2 \times 2$

> **📐 Théorème — Inverse d'une matrice $2 \times 2$**
> Soit $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
> On appelle **déterminant** de $A$ le nombre réel :
> $$\det(A) = ad - bc$$
> 1. La matrice $A$ est **inversible si et seulement si $\det(A) \neq 0$**.
> 2. Si $\det(A) \neq 0$, son inverse est donnée par la formule :
>
> $$\mathbf{A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}}$$

*Démonstration immédiate par vérification directe :*
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \begin{pmatrix} ad - bc & 0 \\ 0 & ad - bc \end{pmatrix} = (ad - bc) I_2$$
En divisant par le réel non nul $ad - bc$, on obtient rigoureusement $I_2$.

#### 3.3 Résolution de systèmes linéaires par inversion de matrice
Considérons un système de deux équations à deux inconnues :
$$\begin{cases} ax + by = \alpha \\ cx + dy = \beta \end{cases}$$
Ce système s'écrit sous forme d'une unique équation matricielle :
$$A X = B \quad \text{avec } A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \ X = \begin{pmatrix} x \\ y \end{pmatrix}, \ B = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$$

Si $\det(A) = ad - bc \neq 0$, la matrice $A$ est inversible.
En multipliant **à gauche par $A^{-1}$** :
$$A^{-1} (A X) = A^{-1} B \iff (A^{-1} A) X = A^{-1} B \iff I_2 X = A^{-1} B$$
D'où l'unique solution :
$$\mathbf{X = A^{-1} B}$$

---

### 4. Graphes et Matrice d'Adjacence

#### 4.1 Vocabulaire des graphes
Un **graphe** $G = (V, E)$ est constitué :
- D'un ensemble de **sommets** (ou nœuds, *vertices*) notés $\{1, 2, \dots, n\}$.
- D'un ensemble d'**arêtes** (liaisons bidirectionnelles dans un graphe non orienté) ou d'**arcs** (flèches orientées d'un sommet vers un autre dans un graphe orienté).
- Le **degré** d'un sommet est le nombre d'arêtes qui lui sont connectées.
- Une **chaîne** (ou un chemin) de longueur $k$ est une suite de $k$ arêtes consécutives reliant un sommet de départ à un sommet d'arrivée.

#### 4.2 La matrice d'adjacence

> **📐 Définition — Matrice d'adjacence**
> Soit $G$ un graphe d'ordre $n$ dont les sommets sont numérotés de 1 à $n$.
> La **matrice d'adjacence** de $G$ est la matrice carrée $M \in \mathcal{M}_n(\mathbb{R})$ dont le coefficient à la ligne $i$ et colonne $j$ vaut :
> $$m_{i,j} = \text{nombre d'arêtes (ou d'arcs) allant du sommet } i \text{ au sommet } j$$
> *(Dans un graphe simple non orienté, $m_{i,j} \in \{0, 1\}$ et $M$ est symétrique : $m_{i,j} = m_{j,i}$).*

```
       Graphe à 3 sommets                 Matrice d'adjacence M
             (1)
            /   ▲                          Vers 1  Vers 2  Vers 3
           /     \                       ┌                       ┐
          ▼       \               De 1   │   0       1       0   │
         (2) ───► (3)             De 2   │   0       0       1   │
                                  De 3   │   1       0       0   │
                                         └                       ┘
```

#### 4.3 Le théorème fondamental des chemins de longueur $k$

> **📐 Théorème fondamental — Puissances de la matrice d'adjacence**
> Soit $M$ la matrice d'adjacence d'un graphe à $n$ sommets.
> Pour tout entier naturel $k \geq 1$, le coefficient situé à la $i$-ième ligne et la $j$-ième colonne de la matrice **$M^k$** est égal au **nombre de chemins de longueur $k$ reliant le sommet $i$ au sommet $j$**.

> **✍️ Démonstration exigible par récurrence**
> Notons $c_{i,j}^{(k)}$ le coefficient $(i, j)$ de la matrice $M^k$, et $N_{i,j}^{(k)}$ le nombre de chemins de longueur $k$ allant de $i$ à $j$.
> Démontrons par récurrence sur $k \geq 1$ la propriété $\mathcal{P}(k) : \text{« Pour tous } i, j, \ c_{i,j}^{(k)} = N_{i,j}^{(k)} \text{ »}$.
>
> - **Initialisation ($k = 1$) :**
>   $M^1 = M$. Par définition de la matrice d'adjacence, $c_{i,j}^{(1)} = m_{i,j}$ est exactement le nombre d'arêtes directes reliant $i$ à $j$, c'est-à-dire le nombre de chemins de longueur 1. $\mathcal{P}(1)$ est vraie.
>
> - **Hérédité :**
>   Supposons la propriété vraie au rang $k \geq 1$ : pour tous sommets $i$ et $m$, $c_{i,m}^{(k)} = N_{i,m}^{(k)}$.
>   Considérons un chemin de longueur $k+1$ allant de $i$ à $j$.
>   Ce chemin est formé d'un chemin de longueur $k$ allant de $i$ à un certain sommet intermédiaire $m$, suivi d'une arête directe de $m$ vers $j$ (de longueur 1).
>   D'après le principe additif et le principe multiplicatif du Chapitre 53, le nombre total de tels chemins est la somme sur tous les sommets intermédiaires possibles $m \in \{1, \dots, n\}$ :
>   $$N_{i,j}^{(k+1)} = \sum_{m=1}^n N_{i,m}^{(k)} \times m_{m,j}$$
>   Par hypothèse de récurrence, $N_{i,m}^{(k)} = c_{i,m}^{(k)}$. Donc :
>   $$N_{i,j}^{(k+1)} = \sum_{m=1}^n c_{i,m}^{(k)} \cdot m_{m,j}$$
>   Or cette somme est précisément la formule du produit matriciel de la ligne $i$ de $M^k$ par la colonne $j$ de $M$ !
>   C'est exactement le coefficient $(i, j)$ de la matrice $M^k \times M = M^{k+1}$.
>   Donc $N_{i,j}^{(k+1)} = c_{i,j}^{(k+1)}$. L'hérédité est prouvée.
>
> - **Conclusion :** Par récurrence, la propriété est vraie pour tout $k \geq 1$.

---

### 5. Chaînes de Markov et Graphes Probabilistes

#### 5.1 Graphes probabilistes et matrice de transition
Un système aléatoire évolue au cours du temps entre $k$ états possibles (par exemple : États $E_1, E_2, \dots, E_k$).
À chaque unité de temps (étape $n$), le système passe d'un état à un autre selon des probabilités fixées.

> **📐 Définition — Matrice de transition**
> La **matrice de transition** $T$ d'un graphe probabiliste à $k$ états est la matrice carrée $k \times k$ dont le coefficient $t_{i,j}$ est la probabilité conditionnelle de passer à l'état $j$ sachant qu'on est à l'état $i$ :
> $$t_{i,j} = P_{(E_i)}(E_j)$$
> **Propriété stochastique :** Sur chaque ligne de $T$, la somme des coefficients vaut 1 :
> $$\sum_{j=1}^k t_{i,j} = 1 \quad (\text{car la somme des probabilités issues d'un sommet vaut 1})$$

#### 5.2 Évolution de la distribution probabiliste
On note $P_n$ la **matrice ligne** des probabilités à l'étape $n$ :
$$P_n = \begin{pmatrix} p_n^{(1)} & p_n^{(2)} & \dots & p_n^{(k)} \end{pmatrix} \quad \text{avec } \sum_{i=1}^k p_n^{(i)} = 1$$

> **📐 Théorème — Formule de récurrence matricielle**
> D'après la formule des probabilités totales :
> $$\mathbf{P_{n+1} = P_n \times T}$$
> Par récurrence immédiate, pour tout entier naturel $n$ :
> $$\mathbf{P_n = P_0 \times T^n}$$

```
                Graphe probabiliste à 2 états
                      0.8
                    ┌─────┐
                    ▼     │
                   ( A ) ─┼─────── 0.2 ──────► ( B ) ◄───┐
                          │                              │ 0.6
                          └─────── 0.4 ─────── (   ) ────┘
                                                 ▲
```
Pour ce graphe, la matrice de transition est :
$$T = \begin{pmatrix} 0{,}8 & 0{,}2 \\ 0{,}4 & 0{,}6 \end{pmatrix}$$
*(Vérification des lignes : $0{,}8 + 0{,}2 = 1$ et $0{,}4 + 0{,}6 = 1$).*

#### 5.3 L'État Stable (Distribution Stationnaire)

Que devient $P_n$ lorsque le nombre d'étapes $n$ devient très grand ?

> **📐 Définition & Théorème — État stable**
> Un vecteur ligne de probabilité $P = \begin{pmatrix} x & y \end{pmatrix}$ (ou $\begin{pmatrix} x & y & z \end{pmatrix}$) est appelé un **état stable** (ou distribution stationnaire) de la chaîne de Markov s'il vérifie :
>
> $$\mathbf{P = P \times T} \quad \text{avec} \quad \sum x_i = 1 \text{ et } x_i \geq 0$$
>
> Si tous les coefficients de la matrice de transition $T$ (ou d'une de ses puissances) sont strictement positifs (graphe connexe et apériodique), alors :
> Quel que soit l'état initial $P_0$, la suite des distributions $(P_n)$ converge vers cet unique état stable :
> $$\mathbf{\lim_{n \to +\infty} P_n = P}$$

*Méthode de calcul pour 2 états :*
Posons $P = \begin{pmatrix} x & y \end{pmatrix}$ avec $x + y = 1 \implies y = 1 - x$.
L'équation $P = PT$ donne :
$$\begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 0{,}8 & 0{,}2 \\ 0{,}4 & 0{,}6 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}$$
Ce qui équivaut au système :
$$\begin{cases} 0{,}8x + 0{,}4y = x \\ 0{,}2x + 0{,}6y = y \end{cases} \iff -0{,}2x + 0{,}4y = 0 \iff 0{,}4y = 0{,}2x \iff x = 2y$$
Comme $x + y = 1$ :
$$2y + y = 1 \iff 3y = 1 \iff y = \frac{1}{3} \quad \text{et} \quad x = \frac{2}{3}$$
L'état stable est donc $P = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} \end{pmatrix}$.
À long terme, il fera beau deux tiers du temps ($\approx 66{,}7\,\%$) et il pleuvra un tiers du temps ($\approx 33{,}3\,\%$), quelle que soit la météo initiale !

---

### 6. Le PageRank de Google : Un réseau géant de matrices

En 1998, deux doctorants de Stanford, **Larry Page et Sergey Brin**, fondent le moteur de recherche **Google**.
Leur coup de génie s'appelle le **PageRank**.
Internet est modélisé comme un graphe géant orienté où chaque page web est un sommet et chaque lien hypertexte est un arc.
Un internaute virtuel navigue au hasard :
- Depuis une page ayant $k$ liens sortants, il choisit l'un d'eux avec probabilité $\frac{1}{k}$.
- Avec une petite probabilité $\alpha \approx 0{,}15$, il s'ennuie et saute vers une page quelconque du Web au hasard.

Cette promenade aléatoire est une chaîne de Markov sur une matrice de taille plusieurs milliards par plusieurs milliards !
L'état stable de cette matrice attribue à chaque page web une probabilité d'occupation : **les pages les plus importantes sont celles dont la composante dans l'état stable est la plus élevée**.
C'est une simple équation $P = PT$ qui a fondé l'empire technologique le plus puissant du XXIᵉ siècle !

---

### 7. Exemples résolus pas à pas

#### Exemple 1 : Calcul de produit matriciel et non-commutativité
Soient les matrices $A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$ et $B = \begin{pmatrix} 2 & 0 \\ -1 & 4 \end{pmatrix}$.
1. Calculer $A \times B$.
2. Calculer $B \times A$.
3. Que constate-t-on ?

**Solution détaillée :**
1. Calcul de $A \times B$ :
   - Ligne 1, Col 1 : $1 \times 2 + 2 \times (-1) = 2 - 2 = 0$
   - Ligne 1, Col 2 : $1 \times 0 + 2 \times 4 = 8$
   - Ligne 2, Col 1 : $3 \times 2 + (-1) \times (-1) = 6 + 1 = 7$
   - Ligne 2, Col 2 : $3 \times 0 + (-1) \times 4 = -4$
   $$A B = \begin{pmatrix} 0 & 8 \\ 7 & -4 \end{pmatrix}$$
2. Calcul de $B \times A$ :
   - Ligne 1, Col 1 : $2 \times 1 + 0 \times 3 = 2$
   - Ligne 1, Col 2 : $2 \times 2 + 0 \times (-1) = 4$
   - Ligne 2, Col 1 : $(-1) \times 1 + 4 \times 3 = -1 + 12 = 11$
   - Ligne 2, Col 2 : $(-1) \times 2 + 4 \times (-1) = -2 - 4 = -6$
   $$B A = \begin{pmatrix} 2 & 4 \\ 11 & -6 \end{pmatrix}$$
3. On constate que $A B \neq B A$. La multiplication matricielle n'est pas commutative.

#### Exemple 2 : Inversion et résolution de système
On considère le système :
$$\begin{cases} 3x + 5y = 11 \\ 2x + 4y = 8 \end{cases}$$
1. Écrire le système sous forme matricielle $A X = B$.
2. Calculer $\det(A)$ et en déduire $A^{-1}$.
3. Résoudre le système par le calcul $X = A^{-1} B$.

**Solution détaillée :**
1. Forme matricielle :
   $$\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 11 \\ 8 \end{pmatrix}$$
   avec $A = \begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}$ et $B = \begin{pmatrix} 11 \\ 8 \end{pmatrix}$.
2. Calcul du déterminant :
   $$\det(A) = 3 \times 4 - 5 \times 2 = 12 - 10 = 2 \neq 0$$
   Comme $\det(A) \neq 0$, $A$ est inversible.
   D'après la formule de l'inverse :
   $$A^{-1} = \frac{1}{2} \begin{pmatrix} 4 & -5 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -2{,}5 \\ -1 & 1{,}5 \end{pmatrix}$$
3. Résolution :
   $$X = A^{-1} B = \frac{1}{2} \begin{pmatrix} 4 & -5 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 11 \\ 8 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 4 \times 11 + (-5) \times 8 \\ (-2) \times 11 + 3 \times 8 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 44 - 40 \\ -22 + 24 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
   La solution unique est donc **$x = 2$ et $y = 1$**.
   *(Vérification : $3(2) + 5(1) = 6 + 5 = 11$ et $2(2) + 4(1) = 4 + 4 = 8$).*

#### Exemple 3 : Dénombrement de chemins sur un graphe
Soit un graphe à 3 sommets $S_1, S_2, S_3$ dont la matrice d'adjacence est :
$$M = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$
*(C'est le triangle complet $K_3$ où chaque sommet est relié aux deux autres).*
1. Calculer $M^2$.
2. En déduire le nombre de chemins de longueur 2 reliant $S_1$ à lui-même, et reliant $S_1$ à $S_2$.
3. Calculer $M^3$ et déterminer le nombre de chemins de longueur 3 reliant $S_1$ à $S_2$.

**Solution détaillée :**
1. Calcul de $M^2$ :
   $$M^2 = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0+1+1 & 0+0+1 & 0+1+0 \\ 0+0+1 & 1+0+1 & 1+0+0 \\ 0+1+0 & 1+0+0 & 1+1+0 \end{pmatrix} = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$
2. - Le coefficient $(1, 1)$ de $M^2$ vaut 2 : il y a **2 chemins de longueur 2** reliant $S_1$ à $S_1$ (ce sont les allers-retours $S_1 \to S_2 \to S_1$ et $S_1 \to S_3 \to S_1$).
   - Le coefficient $(1, 2)$ de $M^2$ vaut 1 : il y a **1 seul chemin de longueur 2** reliant $S_1$ à $S_2$ (c'est $S_1 \to S_3 \to S_2$).
3. Calcul de $M^3 = M^2 \times M$ :
   $$M^3 = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0+1+1 & 2+0+1 & 2+1+0 \\ 0+2+1 & 1+0+1 & 1+2+0 \\ 0+1+2 & 1+0+2 & 1+1+0 \end{pmatrix} = \begin{pmatrix} 2 & 3 & 3 \\ 3 & 2 & 3 \\ 3 & 3 & 2 \end{pmatrix}$$
   Le coefficient $(1, 2)$ de $M^3$ est égal à **3** : il existe exactement 3 chemins de longueur 3 reliant $S_1$ à $S_2$ ($S_1 \to S_2 \to S_1 \to S_2$, $S_1 \to S_2 \to S_3 \to S_2$, et $S_1 \to S_3 \to S_1 \to S_2$).

#### Exemple 4 : Chaîne de Markov à 3 états (Abonnements téléphoniques)
Trois opérateurs téléphoniques A, B et C se partagent un marché. Chaque année :
- L'opérateur A conserve 70 % de ses clients, en perd 20 % vers B et 10 % vers C.
- L'opérateur B conserve 60 % de ses clients, en perd 20 % vers A et 20 % vers C.
- L'opérateur C conserve 80 % de ses clients, en perd 10 % vers A et 10 % vers B.
1. Écrire la matrice de transition $T$.
2. Si les parts de marché initiales sont $P_0 = \begin{pmatrix} 0{,}5 & 0{,}3 & 0{,}2 \end{pmatrix}$, calculer les parts au bout d'un an $P_1$.
3. Déterminer l'état stable $P = \begin{pmatrix} x & y & z \end{pmatrix}$ du marché.

**Solution détaillée :**
1. Matrice de transition :
   $$T = \begin{pmatrix} 0{,}7 & 0{,}2 & 0{,}1 \\ 0{,}2 & 0{,}6 & 0{,}2 \\ 0{,}1 & 0{,}1 & 0{,}8 \end{pmatrix}$$
   *(Chaque ligne somme bien à 1).*
2. Parts au bout d'un an :
   $$P_1 = P_0 \times T = \begin{pmatrix} 0{,}5 & 0{,}3 & 0{,}2 \end{pmatrix} \begin{pmatrix} 0{,}7 & 0{,}2 & 0{,}1 \\ 0{,}2 & 0{,}6 & 0{,}2 \\ 0{,}1 & 0{,}1 & 0{,}8 \end{pmatrix}$$
   - Pour A : $0{,}5 \times 0{,}7 + 0{,}3 \times 0{,}2 + 0{,}2 \times 0{,}1 = 0{,}35 + 0{,}06 + 0{,}02 = 0{,}43$ ($43\,\%$)
   - Pour B : $0{,}5 \times 0{,}2 + 0{,}3 \times 0{,}6 + 0{,}2 \times 0{,}1 = 0{,}10 + 0{,}18 + 0{,}02 = 0{,}30$ ($30\,\%$)
   - Pour C : $0{,}5 \times 0{,}1 + 0{,}3 \times 0{,}2 + 0{,}2 \times 0{,}8 = 0{,}05 + 0{,}06 + 0{,}16 = 0{,}27$ ($27\,\%$)
   $$P_1 = \begin{pmatrix} 0{,}43 & 0{,}30 & 0{,}27 \end{pmatrix}$$
3. L'état stable vérifie $P = PT$ et $x + y + z = 1$ :
   $$\begin{cases}
   0{,}7x + 0{,}2y + 0{,}1z = x \iff -0{,}3x + 0{,}2y + 0{,}1z = 0 \quad (L_1) \\
   0{,}2x + 0{,}6y + 0{,}1z = y \iff 0{,}2x - 0{,}4y + 0{,}1z = 0 \quad (L_2) \\
   x + y + z = 1 \quad (L_3)
   \end{cases}$$
   Soustrayons $(L_2)$ de $(L_1)$ :
   $$(-0{,}3x - 0{,}2x) + (0{,}2y - (-0{,}4y)) + (0{,}1z - 0{,}1z) = 0 \iff -0{,}5x + 0{,}6y = 0 \iff x = \frac{6}{5}y = 1{,}2y$$
   Remplaçons $x$ dans $(L_1)$ pour trouver $z$ :
   $$-0{,}3(1{,}2y) + 0{,}2y + 0{,}1z = 0 \iff -0{,}36y + 0{,}2y + 0{,}1z = 0 \iff 0{,}1z = 0{,}16y \iff z = 1{,}6y$$
   Utilisons la condition $x + y + z = 1$ :
   $$1{,}2y + y + 1{,}6y = 1 \iff 3{,}8y = 1 \iff y = \frac{1}{3{,}8} = \frac{10}{38} = \frac{5}{19} \approx 0{,}2632$$
   Puis :
   - $x = 1{,}2 \times \frac{5}{19} = \frac{6}{19} \approx 0{,}3158$
   - $z = 1{,}6 \times \frac{5}{19} = \frac{8}{19} \approx 0{,}4211$
   L'état stable est :
   $$P = \begin{pmatrix} \frac{6}{19} & \frac{5}{19} & \frac{8}{19} \end{pmatrix} \approx \begin{pmatrix} 31{,}6\,\% & 26{,}3\,\% & 42{,}1\,\% \end{pmatrix}$$
   À long terme, l'opérateur C dominera le marché avec plus de 42 % des parts.

#### Exemple 5 : Puissance $n$-ième par diagonalisation (Cas simple)
Soit la matrice $A = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$.
On donne $P = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ et son inverse $P^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
1. Calculer la matrice $D = P^{-1} A P$ et vérifier qu'elle est diagonale.
2. Pour tout $n \in \mathbb{N}$, exprimer $D^n$.
3. En déduire l'expression explicite de $A^n$ en fonction de $n$.

**Solution détaillée :**
1. Calculons d'abord $A P$ :
   $$A P = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 8-2 & 4-2 \\ 2+1 & 1+1 \end{pmatrix} = \begin{pmatrix} 6 & 2 \\ 3 & 2 \end{pmatrix}$$
   Calculons $D = P^{-1} (A P)$ :
   $$D = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 6 & 2 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 6-3 & 2-2 \\ -6+6 & -2+4 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$$
   $D$ est bien une matrice diagonale.
2. Pour une matrice diagonale, les puissances s'appliquent directement sur les termes diagonaux :
   $$D^n = \begin{pmatrix} 3^n & 0 \\ 0 & 2^n \end{pmatrix}$$
3. Puisque $D = P^{-1} A P$, en multipliant par $P$ à gauche et $P^{-1}$ à droite, on a $A = P D P^{-1}$.
   Par télescopage : $A^n = (P D P^{-1})(P D P^{-1})\dots(P D P^{-1}) = P D^n P^{-1}$.
   Calculons le produit :
   $$P D^n = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 3^n & 0 \\ 0 & 2^n \end{pmatrix} = \begin{pmatrix} 2 \cdot 3^n & 2^n \\ 3^n & 2^n \end{pmatrix}$$
   Puis $(P D^n) P^{-1}$ :
   $$A^n = \begin{pmatrix} 2 \cdot 3^n & 2^n \\ 3^n & 2^n \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 \cdot 3^n - 2^n & -2 \cdot 3^n + 2 \cdot 2^n \\ 3^n - 2^n & -3^n + 2 \cdot 2^n \end{pmatrix}$$
   *(Vérification pour $n = 1$ : $A^1 = \begin{pmatrix} 6 - 2 & -6 + 4 \\ 3 - 2 & -3 + 4 \end{pmatrix} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix} = A$). Formule exacte pour tout $n$ !*

#### Exemple 6 : La marche aléatoire sur un triangle
Une puce saute aléatoirement entre les sommets d'un triangle $A, B, C$.
À chaque saut, elle quitte son sommet actuel et choisit l'un des deux autres sommets avec équiprobabilité ($p = 0{,}5$).
Si la puce part du sommet $A$ au temps $n = 0$, quelle est la probabilité qu'elle se trouve à nouveau en $A$ après $n$ sauts ?

**Solution détaillée :**
La matrice de transition est :
$$T = \begin{pmatrix} 0 & 0{,}5 & 0{,}5 \\ 0{,}5 & 0 & 0{,}5 \\ 0{,}5 & 0{,}5 & 0 \end{pmatrix}$$
Soit $a_n$ la probabilité d'être en $A$ à l'étape $n$. Par symétrie évidente entre $B$ et $C$, la probabilité d'être en $B$ est égale à celle d'être en $C$, soit $b_n = c_n$.
Comme $a_n + b_n + c_n = 1$, on a $a_n + 2b_n = 1 \implies b_n = \frac{1 - a_n}{2}$.
D'après la première colonne de la matrice de transition :
$$a_{n+1} = 0 \cdot a_n + 0{,}5 b_n + 0{,}5 c_n = 0{,}5(b_n + c_n) = 0{,}5(2b_n) = b_n = \frac{1 - a_n}{2} = -\frac{1}{2}a_n + \frac{1}{2}$$
Il s'agit d'une suite arithmético-géométrique !
Recherche du point fixe : $\ell = -\frac{1}{2}\ell + \frac{1}{2} \iff \frac{3}{2}\ell = \frac{1}{2} \iff \ell = \frac{1}{3}$.
Posons $u_n = a_n - \frac{1}{3}$. Alors $u_{n+1} = -\frac{1}{2} u_n$.
La suite $(u_n)$ est géométrique de raison $-\frac{1}{2}$ et de premier terme $u_0 = a_0 - \frac{1}{3} = 1 - \frac{1}{3} = \frac{2}{3}$ (puisque la puce part de $A$, $a_0 = 1$).
Donc :
$$u_n = \frac{2}{3} \left(-\frac{1}{2}\right)^n \implies a_n = \frac{1}{3} + \frac{2}{3} \left(-\frac{1}{2}\right)^n$$
- Pour $n = 0$ : $a_0 = \frac{1}{3} + \frac{2}{3} = 1$.
- Pour $n = 1$ : $a_1 = \frac{1}{3} - \frac{1}{3} = 0$ (elle a sauté en $B$ ou $C$).
- Pour $n = 2$ : $a_2 = \frac{1}{3} + \frac{2}{3} \times \frac{1}{4} = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$.
- Quand $n \to +\infty$ : $\left(-\frac{1}{2}\right)^n \to 0$, donc $a_n \to \frac{1}{3}$. La puce passe un tiers de son temps sur chaque sommet.

---

### Ce qu'il faut retenir

1. **Calcul matriciel :**
   - Produit $A \times B$ : dimension $(n \times k) \times (k \times p) \to (n \times p)$. Ligne par colonne.
   - Non commutatif en général : $AB \neq BA$.
   - Diviseurs de zéro : $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.

2. **Inversion et systèmes :**
   - Matrice $2 \times 2$ : $\det(A) = ad - bc \neq 0 \iff A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
   - Résolution de système : $AX = B \iff X = A^{-1} B$.

3. **Graphes et matrice d'adjacence :**
   - Matrice d'adjacence $M$ : $m_{i,j}$ = nombre d'arêtes reliant $i$ à $j$.
   - **Théorème des chemins :** Le terme $(i, j)$ de $M^k$ est le nombre exact de chemins de longueur $k$ allant de $i$ à $j$.

4. **Chaînes de Markov :**
   - Matrice de transition $T$ : somme de chaque ligne égale à 1.
   - Évolution : $P_{n+1} = P_n \times T$ et $P_n = P_0 \times T^n$.
   - État stable : unique vecteur vérifiant $P = P \times T$ avec $\sum p_i = 1$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 1.** Soient $A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ et $B = \begin{pmatrix} 0 & 5 \\ 1 & -2 \end{pmatrix}$.
Calculer $2A - 3B$, $A \times B$, et $B \times A$.
**Exercice 2.** Calculer le déterminant et l'inverse (si elle existe) des matrices suivantes :
$M_1 = \begin{pmatrix} 5 & 2 \\ 2 & 1 \end{pmatrix}$, $M_2 = \begin{pmatrix} 3 & -6 \\ -2 & 4 \end{pmatrix}$, $M_3 = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.
**Exercice 3.** Résoudre sous forme matricielle le système :
$$\begin{cases} 4x + 3y = 25 \\ 2x + 5y = 23 \end{cases}$$
**Exercice 4.** On considère un graphe non orienté à 4 sommets $\{A, B, C, D\}$ dont les arêtes sont $[A, B], [A, C], [B, C], [C, D]$.
1. Dessiner le graphe.
2. Écrire sa matrice d'adjacence $M$.
3. Quel est le degré du sommet $C$ ?
**Exercice 5.** Une matrice de transition est donnée par $T = \begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix}$.
Si $P_0 = \begin{pmatrix} 0{,}6 & 0{,}4 \end{pmatrix}$, calculer $P_1$ et $P_2$.
**Exercice 6.** Déterminer l'état stable $P = \begin{pmatrix} x & y \end{pmatrix}$ associé à la matrice de transition $T = \begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix}$ de l'exercice 5.
**Exercice 7.** Calculer $A^2$ et $A^3$ pour $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Conjecturer $A^n$.

#### Niveau ★★ (Réflexion et graphes probabilistes)

**Exercice 8.** Puissances d'une matrice nilpotente.
Soit la matrice $N = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$.
1. Calculer $N^2$ et $N^3$.
2. En déduire $N^k$ pour tout $k \geq 3$.
3. Soit $A = I_3 + N$. En utilisant la formule du binôme de Newton (justifier son emploi), calculer $A^n$ pour tout entier $n \geq 2$.
**Exercice 9.** Graphe et connexité.
Soit un graphe d'ordre 4 de matrice d'adjacence $M$.
On calcule $S = M + M^2 + M^3$.
Démontrer que le graphe est connexe si et seulement si tous les coefficients non diagonaux de la matrice $S$ sont strictement positifs.
**Exercice 10.** Le modèle proie-prédateur matriciel (Modèle de Leslie).
Une population d'oiseaux est divisée en deux classes d'âge : les juvéniles $J_n$ et les adultes $A_n$.
Chaque année :
- Les adultes donnent naissance en moyenne à 2 juvéniles.
- 30 % des juvéniles survivent et deviennent adultes l'année suivante.
- 50 % des adultes survivent.
1. Écrire le système d'évolution sous forme matricielle $\begin{pmatrix} J_{n+1} \\ A_{n+1} \end{pmatrix} = L \begin{pmatrix} J_n \\ A_n \end{pmatrix}$.
2. Si la population initiale est de 100 juvéniles et 50 adultes, calculer la population à $n = 1$ et $n = 2$.
**Exercice 11.** Équation matricielle $A^2 - 4A + 3I = 0$.
Soit une matrice carrée $A$ vérifiant la relation $A^2 - 4A + 3I = 0$.
1. Démontrer que $A$ est inversible et exprimer $A^{-1}$ en fonction de $A$ et de $I$.
2. Montrer que pour tout $n \in \mathbb{N}$, il existe deux réels $a_n$ et $b_n$ tels que $A^n = a_n A + b_n I$.
**Exercice 12.** Chaîne de Markov à 3 états : la propagation d'une rumeur.
Dans un village, un individu apprend une information. À chaque étape, il peut la transmettre à son voisin.
Les états sont : $E_1$ (Ignorant), $E_2$ (Croyant), $E_3$ (Sceptique/Immunisé).
Matrice de transition :
$$T = \begin{pmatrix} 0{,}5 & 0{,}4 & 0{,}1 \\ 0 & 0{,}6 & 0{,}4 \\ 0 & 0 & 1 \end{pmatrix}$$
1. Quel est le statut de l'état $E_3$ (état absorbant) ?
2. Calculer $T^2$ et $T^3$.
3. Que devient la population à long terme ?
**Exercice 13.** Matrice stochastique et valeur propre 1.
Soit $T$ une matrice stochastique carrée d'ordre $n$ (somme des coefficients de chaque ligne égale à 1).
Soit $U$ le vecteur colonne dont toutes les coordonnées valent 1.
1. Calculer le produit matriciel $T \times U$.
2. Que peut-on en déduire sur le système $(T - I_n) X = 0$ ?
3. Pourquoi cela prouve-t-il qu'il existe toujours au moins un état stable non nul ?
**Exercice 14.** Inverse d'une matrice $3 \times 3$ par la méthode de Gauss-Jordan.
Inverser la matrice $A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{pmatrix}$ en résolvant le système $AX = Y$.
**Exercice 15.** Nombre d'arbres couvrants (Théorème de Kirchhoff, aperçu).
Pour un graphe simple, on définit la matrice Laplacienne $L = D - M$, où $D$ est la matrice diagonale des degrés et $M$ la matrice d'adjacence.
Calculer $L$ pour un triangle $K_3$ et calculer l'un de ses cofacteurs. Comparer avec le nombre d'arbres couvrants possibles.

#### Niveau ★★★ (Approfondissements et concours)

**Exercice 16.** Théorème de Cayley-Hamilton en dimension 2.
Soit $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
On pose sa trace $\text{Tr}(A) = a + d$ et son déterminant $\det(A) = ad - bc$.
Démontrer par le calcul direct l'identité fondamentale de Cayley-Hamilton :
$$A^2 - \text{Tr}(A) \cdot A + \det(A) \cdot I_2 = 0_2$$
**Exercice 17.** Suites récurrentes d'ordre 2 et puissances de matrices (Fibonacci).
Soit la suite de Fibonacci définie par $F_0 = 0$, $F_1 = 1$ et $F_{n+2} = F_{n+1} + F_n$.
1. Déterminer une matrice carrée $A \in \mathcal{M}_2(\mathbb{R})$ telle que $\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = A \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}$.
2. Démontrer par récurrence que pour tout $n \geq 1$ :
   $$A^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$
3. En calculant $\det(A^n)$ de deux manières différentes, démontrer la célèbre **identité de Cassini** :
   $$F_{n+1} F_{n-1} - F_n^2 = (-1)^n$$
**Exercice 18.** Convergence de la matrice de transition et projecteur spectral.
Soit $T = \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}$ avec $a, b \in ]0, 1[$.
1. Montrer que $T$ admet pour valeurs propres $\lambda_1 = 1$ et $\lambda_2 = 1 - a - b$.
2. Démontrer que $T^n = \frac{1}{a+b} \begin{pmatrix} b & a \\ b & a \end{pmatrix} + \frac{(1-a-b)^n}{a+b} \begin{pmatrix} a & -a \\ -b & b \end{pmatrix}$.
3. En déduire la limite $\lim_{n \to +\infty} T^n$ et retrouver l'état stable quelle que soit la distribution initiale.
**Exercice 19.** Théorème de Perron-Frobenius (Énoncé et sens géométrique).
Pour une matrice à coefficients strictement positifs, expliquer la signification du théorème de Perron-Frobenius : existence d'une plus grande valeur propre réelle positive dominante et unicité du vecteur propre associé positif (l'état stable).
**Exercice 20.** L'algorithme PageRank avec facteur d'amortissement (Damping Factor).
Écrire la matrice Google d'un mini-web à 3 pages où la page 1 pointe vers 2 et 3, la page 2 pointe vers 3, et la page 3 pointe vers 1.
Intégrer le facteur de téléportation $\alpha = 0{,}85$ et calculer le classement PageRank des 3 pages.
**Exercice 21.** Matrices de Hadamard et codes correcteurs d'erreurs.
Une matrice de Hadamard $H_n$ est une matrice carrée de taille $n$ dont les coefficients sont dans $\{-1, +1\}$ et telle que $H_n H_n^T = n I_n$.
Construire $H_2$ et $H_4$ par le produit de Kronecker et expliquer leur rôle dans la transmission des signaux des sondes spatiales Mariner et Voyager.
**Exercice 22.** Graphes eulériens et hamiltoniens.
Démontrer le théorème d'Euler : un graphe connexe admet un cycle eulérien (un parcours fermé passant par chaque arête une fois et une seule) si et seulement si tous ses sommets sont de degré pair.

---

### Solutions

**Solution 1.**
$2A - 3B = \begin{pmatrix} 4 & -2 \\ 6 & 8 \end{pmatrix} - \begin{pmatrix} 0 & 15 \\ 3 & -6 \end{pmatrix} = \begin{pmatrix} 4 & -17 \\ 3 & 14 \end{pmatrix}$.
$A \times B = \begin{pmatrix} 2(0)-1(1) & 2(5)-1(-2) \\ 3(0)+4(1) & 3(5)+4(-2) \end{pmatrix} = \begin{pmatrix} -1 & 12 \\ 4 & 7 \end{pmatrix}$.
$B \times A = \begin{pmatrix} 0(2)+5(3) & 0(-1)+5(4) \\ 1(2)-2(3) & 1(-1)-2(4) \end{pmatrix} = \begin{pmatrix} 15 & 20 \\ -4 & -9 \end{pmatrix}$.

**Solution 2.**
- $\det(M_1) = 5(1) - 2(2) = 1 \neq 0 \implies M_1^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -2 \\ -2 & 5 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -2 & 5 \end{pmatrix}$.
- $\det(M_2) = 3(4) - (-6)(-2) = 12 - 12 = 0$. $M_2$ n'est pas inversible.
- $\det(M_3) = \cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1 \neq 0$.
  $M_3^{-1} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} = M_3(-\theta)$ (la rotation inverse !).

**Solution 3.**
$A = \begin{pmatrix} 4 & 3 \\ 2 & 5 \end{pmatrix}$, $\det(A) = 20 - 6 = 14 \neq 0$.
$A^{-1} = \frac{1}{14}\begin{pmatrix} 5 & -3 \\ -2 & 4 \end{pmatrix}$.
$X = A^{-1} B = \frac{1}{14}\begin{pmatrix} 5 & -3 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 25 \\ 23 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 125 - 69 \\ -50 + 92 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 56 \\ 42 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$.
Solution : $x = 4$ et $y = 3$.

**Solution 4.**
1. Graphe en diamant avec une arête pendant vers $D$.
2. Ordre des sommets A, B, C, D :
   $$M = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
3. Le degré de $C$ est la somme de la ligne 3 : $1 + 1 + 0 + 1 = 3$.

**Solution 5.**
$P_1 = P_0 T = \begin{pmatrix} 0{,}6 & 0{,}4 \end{pmatrix}\begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix} = \begin{pmatrix} 0{,}54+0{,}12 & 0{,}06+0{,}28 \end{pmatrix} = \begin{pmatrix} 0{,}66 & 0{,}34 \end{pmatrix}$.
$P_2 = P_1 T = \begin{pmatrix} 0{,}66 & 0{,}34 \end{pmatrix}\begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix} = \begin{pmatrix} 0{,}594+0{,}102 & 0{,}066+0{,}238 \end{pmatrix} = \begin{pmatrix} 0{,}696 & 0{,}304 \end{pmatrix}$.

**Solution 6.**
$P = PT \iff \begin{pmatrix} x & y \end{pmatrix}\begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}$ avec $x + y = 1$.
$0{,}9x + 0{,}3y = x \iff 0{,}3y = 0{,}1x \iff x = 3y$.
$3y + y = 1 \iff 4y = 1 \iff y = 0{,}25$ et $x = 0{,}75$.
État stable : $P = \begin{pmatrix} 0{,}75 & 0{,}25 \end{pmatrix}$.

**Solution 7.**
$A^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
$A^3 = A^2 A = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$.
Par récurrence immédiate : $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$.

**Solution 8.**
1. $N^2 = \begin{pmatrix} 0 & 0 & 6 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $N^3 = 0_3$.
2. Pour $k \geq 3$, $N^k = 0_3$.
3. Comme $I_3$ et $N$ commutent ($I_3 N = N I_3 = N$), la formule du binôme s'applique :
   $A^n = (I_3 + N)^n = \sum_{k=0}^n \binom{n}{k} I_3^{n-k} N^k = \binom{n}{0}I_3 + \binom{n}{1}N + \binom{n}{2}N^2 + 0 = I_3 + n N + \frac{n(n-1)}{2}N^2$.
   $A^n = \begin{pmatrix} 1 & 2n & n + 3n(n-1) \\ 0 & 1 & 3n \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2n & 3n^2 - 2n \\ 0 & 1 & 3n \\ 0 & 0 & 1 \end{pmatrix}$.

**Solution 9.**
Dans un graphe à 4 sommets, si deux sommets distincts $i$ et $j$ sont connectés, ils peuvent l'être par un chemin de longueur 1, 2 ou au maximum 3 (sans boucle). Le coefficient $(i, j)$ de $S = M + M^2 + M^3$ est la somme des chemins de longueur 1, 2 et 3 reliant $i$ à $j$. Il est strictement positif pour tout couple $(i, j)$ avec $i \neq j$ si et seulement si tout sommet peut rejoindre n'importe quel autre, ce qui est la définition même de la connexité.

**Solution 10.**
1. $\begin{cases} J_{n+1} = 2 A_n \\ A_{n+1} = 0{,}3 J_n + 0{,}5 A_n \end{cases} \iff \begin{pmatrix} J_{n+1} \\ A_{n+1} \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0{,}3 & 0{,}5 \end{pmatrix} \begin{pmatrix} J_n \\ A_n \end{pmatrix}$.
2. Pour $n = 0$, $X_0 = \begin{pmatrix} 100 \\ 50 \end{pmatrix}$.
   $X_1 = \begin{pmatrix} 0 & 2 \\ 0{,}3 & 0{,}5 \end{pmatrix}\begin{pmatrix} 100 \\ 50 \end{pmatrix} = \begin{pmatrix} 100 \\ 55 \end{pmatrix}$.
   $X_2 = \begin{pmatrix} 0 & 2 \\ 0{,}3 & 0{,}5 \end{pmatrix}\begin{pmatrix} 100 \\ 55 \end{pmatrix} = \begin{pmatrix} 110 \\ 57{,}5 \end{pmatrix}$.

**Solution 11.**
1. $A^2 - 4A = -3I \iff A(A - 4I) = -3I \iff A \times \left[-\frac{1}{3}(A - 4I)\right] = I$.
   Donc $A$ est inversible et $A^{-1} = -\frac{1}{3}A + \frac{4}{3}I$.
2. Par division euclidienne du polynôme $X^n$ par $X^2 - 4X + 3 = (X-1)(X-3)$ :
   $X^n = (X^2 - 4X + 3)Q(X) + a_n X + b_n$.
   En évaluant en $A$, $A^n = a_n A + b_n I$.

**Solution 12.**
1. La ligne 3 est $(0 \ 0 \ 1)$ : une fois dans l'état $E_3$ (sceptique), la probabilité d'y rester est 1. C'est un état absorbant définitif.
2. Par calcul de puissances, les deux premières lignes ont des termes vers $E_3$ qui croissent à chaque étape.
3. À long terme, $\lim_{n \to +\infty} T^n = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$. Toute la population finit inexorablement dans l'état sceptique/immunisé $E_3$.

**Solution 13.**
1. Le coefficient $i$ de $T \times U$ est la somme des termes de la ligne $i$ de $T$, qui vaut 1 par définition d'une matrice stochastique. Donc $T \times U = U = 1 \cdot U$.
2. Cela signifie $(T - I_n)U = 0$. Le système admet une solution non nulle ($U \neq 0$), donc $\det(T - I_n) = 0$.
3. Comme $\det(T^T - I_n) = \det(T - I_n) = 0$, il existe aussi un vecteur ligne non nul $P$ tel que $P(T - I_n) = 0 \iff PT = P$. En normalisant pour que $\sum p_i = 1$, on obtient un état stable.

**Solution 14.**
Résolution de $\begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$.
Par élimination : $L_2 \leftarrow L_2 - 2L_1$ et $L_3 \leftarrow L_3 - 4L_1$, on trouve $z = a + b - \frac{1}{2}(c - 4a - \dots)$.
On obtient $A^{-1} = \begin{pmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{pmatrix}$.

**Solution 15.**
Pour le triangle $K_3$, chaque sommet est de degré 2 : $D = 2I_3$.
$L = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix}$.
Le cofacteur obtenu en rayant la 1ʳᵉ ligne et la 1ʳᵉ colonne est $\det\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = 4 - 1 = 3$.
D'après le théorème de Kirchhoff, il y a exactement 3 arbres couvrants (les 3 façons de retirer une arête pour obtenir un arbre), ce qui concorde parfaitement.

**Solution 16.**
$\text{Tr}(A) = a+d$ et $\det(A) = ad - bc$.
$A^2 = \begin{pmatrix} a^2+bc & ab+bd \\ ca+dc & cb+d^2 \end{pmatrix}$.
$(a+d)A = \begin{pmatrix} a^2+ad & ab+bd \\ ca+cd & ad+d^2 \end{pmatrix}$.
$A^2 - (a+d)A = \begin{pmatrix} bc-ad & 0 \\ 0 & bc-ad \end{pmatrix} = -(ad-bc)I_2 = -\det(A)I_2$.
D'où $A^2 - \text{Tr}(A)A + \det(A)I_2 = 0_2$.

**Solution 17.**
1. Comme $F_{n+1} = 1 \cdot F_n + 1 \cdot F_{n-1}$ et $F_n = 1 \cdot F_n + 0 \cdot F_{n-1}$, la matrice est $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
2. Pour $n = 1$ : $A^1 = \begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
   Hérédité immédiate en multipliant par $A$ et en utilisant la relation de récurrence de Fibonacci.
3. $\det(A) = 1(0) - 1(1) = -1$.
   Donc $\det(A^n) = (\det A)^n = (-1)^n$.
   D'autre part, $\det(A^n) = F_{n+1}F_{n-1} - F_n^2$. L'égalité donne l'identité de Cassini.

**Solution 18.**
1. Polynôme caractéristique $\det(T - \lambda I) = (\lambda - 1)(\lambda - (1 - a - b))$. Les racines sont 1 et $1 - a - b$.
2. En diagonalisant $T = P D P^{-1}$ avec $D = \begin{pmatrix} 1 & 0 \\ 0 & 1-a-b \end{pmatrix}$, le calcul de $P D^n P^{-1}$ donne exactement la décomposition demandée.
3. Comme $|1 - a - b| < 1$, $(1-a-b)^n \to 0$.
   La limite vaut $\frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix}$.
   Pour tout $P_0 = (x \ 1-x)$, $P_0 \lim T^n = \begin{pmatrix} \frac{b}{a+b} & \frac{a}{a+b} \end{pmatrix}$, qui est l'état stable universel.

**Solution 19.**
Le théorème garantit que pour toute matrice à coefficients strictement positifs, la valeur propre de plus grand module est réelle, strictement positive, simple, et son vecteur propre peut être choisi à coordonnées strictement positives. Cela signifie qu'aucun phénomène chaotique oscillant ne peut empêcher la convergence : le système atteint toujours un équilibre global stable et prévisible.

**Solution 20.**
Matrice brute de liens : $H = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$.
Matrice de Google : $G = 0{,}85 H + 0{,}15 \times \frac{1}{3} J$, où $J$ est la matrice remplie de 1.
La résolution de $P = PG$ donne l'importance relative de chaque page, la page 3 étant la plus citée et obtenant le rang le plus élevé.

**Solution 21.**
$H_2 = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
$H_4 = \begin{pmatrix} H_2 & H_2 \\ H_2 & -H_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{pmatrix}$.
Ces matrices orthogonales permettent d'émettre des codes à distance maximale : même si le signal spatial subit de fortes interférences, le récepteur terrestre retrouve le message par simple corrélation matricielle.

**Solution 22.**
À chaque passage dans un sommet, un cycle emprunte une arête entrante et une arête sortante, consommant 2 arêtes incidentes. Chaque sommet doit donc comporter un nombre pair d'arêtes. La réciproque s'obtient par l'algorithme de Fleury ou la décomposition en cycles disjoints.

---

### La question qui ouvre la suite

Nous voici parvenus au terme des structures de notre parcours.
Depuis le tout premier caillou que tu as ramassé sur le sol à six ans pour apprendre à compter, jusqu'aux matrices de transition qui ordonnent les milliards de pages du cyberespace mondial, quel chemin extraordinaire as-tu parcouru !
Pourquoi ces symboles inventés par l'esprit humain s'ajustent-ils avec une telle perfection au tissu de la réalité physique ?
Comment toutes les branches des mathématiques — arithmétique, géométrie, analyse, probabilités — se rejoignent-elles en un seul et même fleuve ?
Il est temps de contempler le panorama dans toute sa splendeur : tourne l'ultime page et entre dans **le Chapitre 58 et la Fin du Voyage**.
