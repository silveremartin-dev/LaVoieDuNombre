# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 53 : Le Cadenas à Code et les Façons de Choisir

> *« Rien n'est plus trompeur que l'intuition du nombre de possibles : l'esprit humain s'égare sitôt que les choix se multiplient. Mais dès que la pensée structure l'éventail — ordonner ou mêler, répéter ou exclure —, le dédale infini devient un édifice de cristal gouverné par de simples factorielles. »*

---

### Ce que tu vas découvrir

- Comment compter sans jamais énumérer un à un des millions d'objets grâce aux deux lois fondamentales : le **principe additif** et le **principe multiplicatif**.
- La distinction cruciale qui gouverne tout le dénombrement : **l'ordre compte-t-il ?** et **peut-on répéter les éléments ?**
- Les **$k$-uplets**, les **arrangements** et les **permutations**, articulés autour de la spectaculaire fonction factorielle $n!$.
- Les **combinaisons** $\binom{n}{k}$ (« $k$ parmi $n$ »), le **triangle de Pascal** et leurs propriétés de symétrie et de récurrence.
- La puissance de la **formule du binôme de Newton**, qui développe instantanément n'importe quelle puissance d'une somme $(a+b)^n$.
- Les pièges classiques de surcomptage et la stratégie du **passage au complémentaire**.

---

### 1. Le problème : compter l'invisible

#### 1.1 Le cadenas du vestiaire
Imagine un cadenas de vélo à 4 molettes, chacune portant les chiffres de 0 à 9. Tu as oublié la combinaison. Combien de tentatives te faudrait-il, au pire, pour être certain de l'ouvrir ?
Pour le premier chiffre, 10 choix. Pour le deuxième, 10 choix. Pour le troisième, 10 choix. Pour le quatrième, 10 choix.
Le nombre total de codes possibles est :
$$10 \times 10 \times 10 \times 10 = 10^4 = 10\,000.$$
À raison d'un essai toutes les 3 secondes sans pause, il te faudrait plus de 8 heures pour tout tester.

Changeons maintenant une seule règle : le fabricant garantit que **les 4 chiffres d'un code sont tous distincts** (aucun chiffre ne se répète). Combien de codes reste-t-il ?
- Premier chiffre : 10 choix possibles.
- Deuxième chiffre : seulement 9 choix (celui déjà utilisé est interdit).
- Troisième chiffre : 8 choix.
- Quatrième chiffre : 7 choix.
Le total tombe à :
$$10 \times 9 \times 8 \times 7 = 5\,040 \text{ codes}.$$
Près de la moitié des combinaisons s'est évaporée par la simple interdiction de répéter !

#### 1.2 Le menu du bistrot
Un restaurant propose une formule à midi : 3 entrées au choix, 4 plats de résistance et 3 desserts. Combien de repas complets différents (entrée + plat + dessert) un client peut-il composer ?
Ici, choisir une entrée n'empêche en rien de choisir n'importe quel plat, ni n'importe quel dessert. Les choix s'enchaînent de manière indépendante :
$$3 \times 4 \times 3 = 36 \text{ menus différents}.$$
Si tu venais y manger tous les midis du lundi au vendredi, il te faudrait plus de 7 semaines pour épuiser toutes les saveurs sans jamais prendre deux fois le même plateau !

#### 1.3 La main de cartes et l'équipe de sport
Considérons maintenant une situation différente : un entraîneur doit choisir 3 joueurs parmi 10 disponibles pour former une patrouille de relais.
Est-ce que choisir Alice, Bob et Chloé est différent de choisir Chloé, Bob et Alice ?
**Non.** L'équipe est la même. L'ordre dans lequel l'entraîneur prononce leurs prénoms n'a aucune importance : ils sont ensemble sur le terrain.

Si l'on comptait comme pour le cadenas sans répétition ($10 \times 9 \times 8 = 720$), on commettrait une erreur massive : le trio {Alice, Bob, Chloé} serait compté plusieurs fois :
- Alice, Bob, Chloé
- Alice, Chloé, Bob
- Bob, Alice, Chloé
- Bob, Chloé, Alice
- Chloé, Alice, Bob
- Chloé, Bob, Alice

Exactement 6 fois la même équipe ! Le vrai nombre d'équipes possibles n'est donc pas 720, mais :
$$\frac{720}{6} = 120.$$

#### 1.4 La crise du dénombrement
Ces trois scènes posent les bases d'une science rigoureuse : le **dénombrement** (*combinatorics* en anglais).
Dès que les ensembles grandissent, il devient physiquement impossible de dresser la liste exhaustive des possibles. Si une urne contient 50 boules et qu'on en tire 5, le nombre de tirages dépasse deux millions.
Le mathématicien ne liste pas : il **structure**, il **catégorise** et il **calcule**.

---

### 2. Les fondations : Ensembles finis, principe additif et principe multiplicatif

#### 2.1 Ensembles finis et cardinal
Soit $E$ un ensemble. On dit que $E$ est un **ensemble fini** s'il contient un nombre entier fini d'éléments.

> **📐 Définition — Cardinal d'un ensemble fini**
> Le nombre d'éléments d'un ensemble fini $E$ est appelé le **cardinal** de $E$.
> On le note $\text{Card}(E)$ ou, plus couramment au lycée et dans le supérieur, $|E|$ ou $\#E$.
> Si $E = \emptyset$ (ensemble vide), on a $|E| = 0$.

*Notation expliquée :* Le mot *cardinal* vient du latin *cardo*, « le gond, le pivot » : c'est le nombre fondamental autour duquel tourne la taille d'une collection. La notation $|E|$ rappelle la valeur absolue (qui mesure une taille ou une distance).

#### 2.2 Le principe additif : partitions et disjonction

> **📐 Propriété fondamentale — Principe additif**
> Soient $A$ et $B$ deux sous-ensembles finis d'un ensemble $E$.
> Si $A$ et $B$ sont **disjoints** (c'est-à-dire sans aucun élément commun : $A \cap B = \emptyset$), alors :
> $$|A \cup B| = |A| + |B|$$
> Plus généralement, si $A_1, A_2, \dots, A_m$ forment une **partition** de $E$ (ils sont deux à deux disjoints et leur réunion forme tout $E$), alors :
> $$|E| = |A_1| + |A_2| + \dots + |A_m| = \sum_{i=1}^m |A_i|$$

```
   Ensemble E
 ┌──────────────────────────┐
 │  ┌────────┐  ┌────────┐  │
 │  │   A    │  │   B    │  │   A ∩ B = ∅
 │  │ 5 élém │  │ 7 élém │  │   |A ∪ B| = 5 + 7 = 12
 │  └────────┘  └────────┘  │
 └──────────────────────────┘
```

Et si les deux ensembles se chevauchent ?
C'est la célèbre formule du crible (ou formule de Poincaré pour 2 ensembles) :

> **📐 Théorème — Formule des deux ensembles**
> Pour tous ensembles finis $A$ et $B$ :
> $$|A \cup B| = |A| + |B| - |A \cap B|$$

*Démonstration visuelle :* En additionnant $|A|$ et $|B|$, les éléments situés dans l'intersection $A \cap B$ ont été comptés deux fois. Il faut donc retrancher une fois $|A \cap B|$ pour rétablir le compte exact.

> **🧭 Méthode — Le principe du complémentaire**
> Si $A$ est une partie d'un ensemble fini $E$, son complémentaire $\overline{A}$ (ou $E \setminus A$) vérifie :
> $$|A| + |\overline{A}| = |E| \iff |A| = |E| - |\overline{A}|$$
> **Règle d'or :** Chaque fois qu'un problème contient les mots *« au moins un... »*, il est presque toujours dix fois plus rapide de dénombrer le contraire (*« aucun... »*) et de soustraire au total !

#### 2.3 Le principe multiplicatif et le produit cartésien

> **📐 Définition — Produit cartésien**
> Soient $A$ et $B$ deux ensembles. Le produit cartésien $A \times B$ est l'ensemble de tous les couples $(a, b)$ où $a \in A$ et $b \in B$ :
> $$A \times B = \{ (a, b) \mid a \in A, b \in B \}$$

> **📐 Théorème — Principe multiplicatif**
> Si $A$ et $B$ sont deux ensembles finis, alors :
> $$|A \times B| = |A| \times |B|$$
> De façon générale, pour $k$ ensembles finis $A_1, A_2, \dots, A_k$ :
> $$|A_1 \times A_2 \times \dots \times A_k| = |A_1| \times |A_2| \times \dots \times |A_k| = \prod_{i=1}^k |A_i|$$

*L'arbre de choix :*
Chaque choix successif correspond à une ramification. Si la première étape offre $n_1$ branches, et que de chacune partent $n_2$ sous-branches, le nombre total de feuilles au bout de l'arbre est $n_1 \times n_2$.

---

### 3. L'ordre compte : $k$-uplets, arrangements et factorielle

#### 3.1 Les $k$-uplets (avec remise / répétition autorisée)
On tire $k$ objets parmi $n$, **l'un après l'autre**, en remettant l'objet tiré dans le sac à chaque étape (ou en réutilisant le même symbole, comme sur une molette).

> **📐 Théorème — Nombre de $k$-uplets**
> Soit $E$ un ensemble à $n$ éléments. Un **$k$-uplet** (ou liste de longueur $k$) d'éléments de $E$ est un élément du produit cartésien $E^k = \underbrace{E \times E \times \dots \times E}_{k \text{ facteurs}}$.
> Le nombre de $k$-uplets d'un ensemble à $n$ éléments est :
> $$|E^k| = n^k$$

*Exemples concrets :*
- Nombre d'octets possibles (mots de 8 bits formés de 0 et de 1) : $2^8 = 256$.
- Nombre de codes de carte bancaire à 4 chiffres décimaux : $10^4 = 10\,000$.
- Nombre de résultats possibles lors de 5 lancers d'une pièce de monnaie (Pile ou Face) : $2^5 = 32$.

#### 3.2 Les arrangements ($k$-uplets d'éléments distincts, sans répétition)
Cette fois, on choisit $k$ éléments parmi $n$ **l'un après l'autre**, mais **sans remise** : chaque élément ne peut être utilisé qu'une seule fois.

> **📐 Définition & Théorème — Arrangements**
> Soit $E$ un ensemble à $n$ éléments et $k$ un entier tel que $0 \leq k \leq n$.
> Un **arrangement** de $k$ éléments de $E$ (ou $k$-uplet d'éléments distincts) est une liste ordonnée $(x_1, x_2, \dots, x_k)$ d'éléments deux à deux distincts de $E$.
> Le nombre de tels arrangements est noté $A_n^k$ et vaut :
> $$A_n^k = n \times (n-1) \times (n-2) \times \dots \times (n - k + 1)$$

*Démonstration :*
Pour la 1ʳᵉ place, nous avons $n$ candidats possibles.
Pour la 2ᵉ place, il en reste $n - 1$.
Pour la 3ᵉ place, il en reste $n - 2$.
...
Pour la $k$-ième place, il en reste $n - (k - 1) = n - k + 1$.
D'après le principe multiplicatif, on multiplie ces entiers.

#### 3.3 Permutations et la fonction factorielle $n!$
Que se passe-t-il si l'on prend tous les éléments, c'est-à-dire si $k = n$ ?
On ordonne la totalité des $n$ éléments : c'est une **permutation**.

> **📐 Définition & Théorème — Permutations et Factorielle**
> Une **permutation** d'un ensemble $E$ à $n$ éléments est un arrangement de tous les éléments de $E$ (un $n$-uplet d'éléments distincts de $E$).
> Le nombre de permutations d'un ensemble à $n$ éléments est noté $n!$ (qui se lit **« factorielle $n$ »**) :
> $$n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1$$
> Par convention fondamentale :
> $$0! = 1$$

*Notation expliquée :*
Le point d'exclamation a été introduit en 1808 par le mathématicien français **Christian Kramp** de Strasbourg, simplement pour abréger les écritures typographiques longues.
Pourquoi $0! = 1$ ?
1. **Combinatoire :** Combien de façons y a-t-il d'ordonner zéro objet ? Une seule façon : la liste vide !
2. **Algébrique :** Pour tout $n \geq 1$, on a $n! = n \times (n-1)!$. En appliquant cette formule pour $n = 1$, il vient $1! = 1 \times 0!$. Comme $1! = 1$, on doit impérativement poser $0! = 1$ pour maintenir la cohérence de l'arithmétique.

*Réécriture élégante de $A_n^k$ :*
Remarquons que l'on peut compléter le produit de $A_n^k$ jusqu'à 1 :
$$A_n^k = \frac{n \times (n-1) \times \dots \times (n-k+1) \times (n-k) \times \dots \times 1}{(n-k) \times \dots \times 1} = \frac{n!}{(n-k)!}$$

> **💡 Le savais-tu ? L'explosion factorielle**
> La factorielle croît à une vitesse vertigineuse :
> - $3! = 6$
> - $5! = 120$
> - $10! = 3\,628\,800$
> - $52! \approx 8{,}06 \times 10^{67}$
> Lorsque tu mélanges un jeu de 52 cartes convenablement, l'ordre obtenu n'a très probablement **jamais existé** dans toute l'histoire de l'humanité, et ne réapparaîtra probablement jamais avant l'extinction du Soleil !

---

### 4. L'ordre ne compte pas : Les combinaisons $\binom{n}{k}$

#### 4.1 La poignée de main et le sous-ensemble
Dans de nombreuses situations concrètes, l'ordre d'apparition n'a aucun sens :
- Tirer une main de 5 cartes au poker (qu'on reçoive l'As de pique en premier ou en dernier, on a l'As de pique en main).
- Choisir 3 délégués de classe parmi 30 élèves.
- Choisir 6 numéros parmi 49 sur une grille de Loto.

Dans ces cas, le résultat n'est pas un $k$-uplet (liste entre parenthèses), c'est une **partie** ou un **sous-ensemble** à $k$ éléments (noté entre accolades $\{x_1, \dots, x_k\}$).

> **📐 Définition — Combinaisons**
> Soit $E$ un ensemble à $n$ éléments et $k$ un entier tel que $0 \leq k \leq n$.
> Une **combinaison** de $k$ éléments parmi $n$ est un sous-ensemble (ou une partie) de $E$ ayant exactement $k$ éléments.
> Le nombre de ces combinaisons est noté $\binom{n}{k}$ (qui se lit **« $k$ parmi $n$ »**).
> *(Ancienne notation encore courante dans d'autres pays : $C_n^k$).*

#### 4.2 La formule magique

> **✍️ Démonstration exigible — Formule de $\binom{n}{k}$**
> Calculons le nombre d'arrangements $A_n^k$ de deux façons différentes :
> 1. D'une part, on sait que le nombre d'arrangements est $A_n^k = \frac{n!}{(n-k)!}$.
> 2. D'autre part, pour fabriquer un arrangement de $k$ éléments (une liste ordonnée), on peut procéder en deux étapes :
>    - **Étape 1 :** Choisir les $k$ éléments sans s'occuper de l'ordre. Par définition, il y a $\binom{n}{k}$ façons de le faire.
>    - **Étape 2 :** Ordonner ces $k$ éléments choisis pour former une liste. D'après le paragraphe précédent, il y a $k!$ façons de permuter ces $k$ éléments.
>
> D'après le principe multiplicatif :
> $$A_n^k = \binom{n}{k} \times k!$$
> En isolant $\binom{n}{k}$, on obtient le théorème fondamental :
>
> $$\binom{n}{k} = \frac{A_n^k}{k!} = \frac{n!}{k!(n-k)!}$$

*Exemple immédiat :*
Le nombre de mains de 3 cartes dans un jeu de 10 cartes :
$$\binom{10}{3} = \frac{10!}{3! \times 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120.$$
On retrouve exactement notre calcul intuitif du vestiaire !

#### 4.3 Propriétés fondamentales des combinaisons

1. **Valeurs remarquables :**
   $$\binom{n}{0} = 1 \quad \text{(un seul ensemble vide)}, \quad \binom{n}{1} = n, \quad \binom{n}{n} = 1$$

2. **Symétrie des choix :**
   $$\binom{n}{k} = \binom{n}{n-k}$$

> **✍️ Démonstration — Symétrie**
> - **Par le calcul :**
>   $$\binom{n}{n-k} = \frac{n!}{(n-k)!(n - (n-k))!} = \frac{n!}{(n-k)!k!} = \binom{n}{k}$$
> - **Par l'esprit combinatoire (magnifique !) :**
>   Choisir $k$ personnes parmi $n$ pour monter dans un bateau, c'est exactement désigner les $n-k$ personnes qui restent sur le quai ! À chaque groupe de $k$ choisis correspond un unique groupe de $n-k$ exclus. Il y a donc exactement autant de façons de faire l'un que l'autre.

#### 4.4 La relation de Pascal

> **📐 Théorème — Formule de Pascal**
> Pour tous entiers $n \geq 1$ et $1 \leq k \leq n$ :
> $$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

> **✍️ Démonstration combinatoire exigible — La méthode du témoin**
> Soit $E$ un ensemble à $n$ éléments. Isolons un élément particulier de $E$, appelons-le **Alice**.
> Nous voulons choisir un sous-ensemble de $k$ éléments parmi ces $n$ personnes. Il y a $\binom{n}{k}$ façons au total.
> Classons ces sous-ensembles en deux catégories disjointes :
> - **Catégorie 1 : Les comités qui contiennent Alice.**
>   Puisqu'Alice est déjà choisie d'office, il ne reste plus qu'à choisir $k-1$ camarades parmi les $n-1$ personnes restantes. Il y a $\binom{n-1}{k-1}$ façons de le faire.
> - **Catégorie 2 : Les comités qui ne contiennent pas Alice.**
>   Alice est écartée. Il faut donc choisir les $k$ membres du comité entièrement parmi les $n-1$ personnes restantes. Il y a $\binom{n-1}{k}$ façons.
>
> Ces deux catégories forment une partition de l'ensemble des comités possibles. Par le principe additif :
> $$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$
> La formule est démontrée sans une seule ligne de fraction d'algèbre !

---

### 5. Le Triangle de Pascal et le Binôme de Newton

#### 5.1 La construction du triangle
La formule de Pascal $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ stipule qu'un nombre est la somme de deux nombres de la ligne supérieure : celui situé juste au-dessus, et celui situé juste au-dessus à gauche.

```
 n \ k │  0    1    2    3    4    5    6    Somme de la ligne
───────┼───────────────────────────────────  ─────────────────
 n = 0 │  1                                         1 = 2⁰
 n = 1 │  1    1                                    2 = 2¹
 n = 2 │  1    2    1                               4 = 2²
 n = 3 │  1    3    3    1                          8 = 2³
 n = 4 │  1    4    6    4    1                    16 = 2⁴
 n = 5 │  1    5   10   10    5    1               32 = 2⁵
 n = 6 │  1    6   15   20   15    6    1          64 = 2⁶
```
Remarque la colonne de droite : la somme de tous les coefficients de la ligne $n$ vaut toujours $2^n$ !
Pourquoi ?
Parce que faire la somme de tous les $\binom{n}{k}$ pour $k$ allant de 0 à $n$, c'est compter tous les sous-ensembles possibles d'un ensemble à $n$ éléments (ceux à 0 élément, puis à 1, puis à 2... jusqu'à $n$).
Or pour chaque élément d'un ensemble, il y a 2 possibilités : soit il fait partie du sous-ensemble, soit il n'en fait pas partie.
Pour $n$ éléments, cela donne $2 \times 2 \times \dots \times 2 = 2^n$ sous-ensembles (l'ensemble des parties $\mathcal{P}(E)$).

$$\sum_{k=0}^n \binom{n}{k} = 2^n$$

#### 5.2 Le binôme de Newton

Rappelle-toi tes identités remarquables de collège et de Seconde :
- $(a+b)^1 = a + b$
- $(a+b)^2 = a^2 + 2ab + b^2$
- $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$

Regarde les coefficients :
- Ligne 1 : $1, 1$
- Ligne 2 : $1, 2, 1$
- Ligne 3 : $1, 3, 3, 1$
Ce sont très exactement les lignes du triangle de Pascal !

> **📐 Théorème fondamental — Formule du Binôme de Newton**
> Pour tous réels ou complexes $a$ et $b$, et pour tout entier naturel $n \in \mathbb{N}$ :
> $$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$
> En développant :
> $$(a+b)^n = \binom{n}{0} a^n + \binom{n}{1} a^{n-1}b + \binom{n}{2} a^{n-2}b^2 + \dots + \binom{n}{n} b^n$$

> **✍️ Démonstration combinatoire — Pourquoi cette formule est limpide**
> Développons le produit de $n$ parenthèses identiques :
> $$(a+b)^n = \underbrace{(a+b)(a+b)\dots(a+b)}_{n \text{ facteurs}}$$
> Lors de la grande distributivité, pour former chaque terme du résultat, on doit obligatoirement choisir **soit la lettre $a$, soit la lettre $b$** dans chacune des $n$ parenthèses.
> Si l'on choisit $k$ fois la lettre $b$, on aura obligatoirement choisi la lettre $a$ dans les $n-k$ autres parenthèses. Le monôme résultant est donc :
> $$a^{n-k} b^k$$
> Combien de fois ce terme $a^{n-k} b^k$ apparaît-il dans le développement ?
> Exactement autant de fois qu'il y a de façons de choisir les $k$ parenthèses fournissant la lettre $b$ parmi les $n$ parenthèses disponibles !
> C'est la définition même de **« $k$ parmi $n$ »**, soit $\binom{n}{k}$.
> La formule est ainsi démontrée avec une clarté totale.

---

### 6. Boîte à outils et pièges classiques

#### 6.1 L'organigramme de décision
Face à un énoncé de dénombrement, pose-toi **toujours** ces deux questions dans cet ordre :

```
                  L'ORDRE COMPTE-T-IL ?
                      /          \
                    OUI           NON
                   /                \
        PEUT-ON RÉPÉTER ?       PEUT-ON RÉPÉTER ?
           /          \                 \
         OUI          NON               NON
         /              \                 \
    k-uplets       Arrangements       Combinaisons
      n^k             A_n^k             (n parmi k)
                   = n!/(n-k)!        = n! / (k!(n-k)!)
                   (si k=n : n!)
```

#### 6.2 Les pièges mortels
> **⚠️ Attention, piège ! — Le surcomptage par fausse décomposition**
> *Exemple :* Dans une classe de 10 garçons et 12 filles, on veut former un groupe de 4 élèves contenant **au moins une fille**.
> - *Faux raisonnement tentant :* « Je choisis 1 fille parmi les 12 (12 façons), puis je choisis les 3 autres élèves parmi les 21 élèves restants ($\binom{21}{3}$ façons). Total : $12 \times \binom{21}{3}$. »
> **C'est faux !** Tu as surcompté les groupes ayant plusieurs filles. Par exemple, si tu as choisi Clara en première fille, puis Sophie parmi les 3 autres, cela produit le même groupe que si tu avais choisi Sophie en première fille et Clara parmi les 3 autres.
> - *La méthode correcte (complémentaire) :*
>   On compte tous les groupes possibles sans contrainte : $\binom{22}{4}$.
>   On soustrait les groupes qui ne contiennent **aucune fille** (c'est-à-dire 4 garçons) : $\binom{10}{4}$.
>   Nombre exact : $\binom{22}{4} - \binom{10}{4} = 7\,315 - 210 = 7\,105$.

> **🔍 L'histoire vraie — Les dés du Chevalier de Méré (1654)**
> Antoine Gombaud, dit le Chevalier de Méré, homme d'esprit et joueur invétéré, s'étonnait auprès de Blaise Pascal :
> *« En lançant 4 fois un dé à 6 faces, j'ai plus d'une chance sur deux d'obtenir au moins un 6. Mais en lançant 24 fois une paire de deux dés, j'ai moins d'une chance sur deux d'obtenir un double-six. Pourtant, $4/6 = 24/36$ ! Les mathématiques seraient-elles contradictoires ? »*
> Pascal prend sa plume et écrit à Pierre de Fermat. Ensemble, par échange de lettres, ils calculent avec le complémentaire :
> 1. Avec 1 dé en 4 lancers : probabilité de ne jamais avoir de 6 = $(5/6)^4 \approx 0{,}482$. Donc probabilité d'avoir au moins un 6 = $1 - 0{,}482 = 0{,}518 > 1/2$. (Avantageux !)
> 2. Avec 2 dés en 24 lancers : probabilité de ne jamais avoir de double 6 = $(35/36)^{24} \approx 0{,}509$. Donc au moins un double 6 = $1 - 0{,}509 = 0{,}491 < 1/2$. (Défavorable !)
> Le Chevalier perdait son argent à cause d'une fraction trompeuse. La théorie des probabilités et du dénombrement moderne venait de naître !

---

### 7. Exemples résolus pas à pas

#### Exemple 1 : Le digicode d'un immeuble
Le digicode d'une résidence comporte les touches 0 à 9 ainsi que les lettres A, B, C (soit 13 touches au total). Un code d'entrée est composé d'une lettre suivie de 3 chiffres.
1. Combien de codes peut-on créer au total ?
2. Combien de codes si les 3 chiffres doivent être tous distincts ?
3. Combien de codes si le code commence par A et ne contient aucun chiffre pair ?

**Solution détaillée :**
1. Un code est un 4-uplet $(L, c_1, c_2, c_3)$ appartenant à $\{A,B,C\} \times \{0..9\}^3$.
   Par le principe multiplicatif : $3 \times 10 \times 10 \times 10 = 3 \times 10^3 = 3\,000$ codes.
2. Pour la lettre : 3 choix. Pour les chiffres distincts, il s'agit d'un arrangement de 3 chiffres parmi 10 : $A_{10}^3 = 10 \times 9 \times 8 = 720$.
   Total : $3 \times 720 = 2\,160$ codes.
3. La lettre est fixée (A : 1 seul choix).
   Les chiffres impairs sont $\{1, 3, 5, 7, 9\}$, soit 5 chiffres disponibles.
   Puisqu'aucune interdiction de répétition n'est mentionnée, chaque chiffre a 5 possibilités :
   Total : $1 \times 5^3 = 125$ codes.

#### Exemple 2 : Composition d'un jury d'examen
Dans un lycée, 15 professeurs de sciences et 12 professeurs de lettres sont volontaires pour former un jury de grand oral composé de 4 personnes.
1. Combien de jurys différents peut-on constituer ?
2. Combien de jurys comportant exactement 2 professeurs de sciences et 2 professeurs de lettres ?
3. Combien de jurys comportant au moins un professeur de chaque discipline ?

**Solution détaillée :**
1. Un jury est un sous-ensemble de 4 personnes parmi les $15 + 12 = 27$ professeurs. L'ordre ne compte pas :
   $$\binom{27}{4} = \frac{27 \times 26 \times 25 \times 24}{4 \times 3 \times 2 \times 1} = 17\,550 \text{ jurys}.$$
2. On choisit indépendamment 2 professeurs de sciences parmi 15, ET 2 professeurs de lettres parmi 12 :
   $$\binom{15}{2} \times \binom{12}{2} = \frac{15 \times 14}{2} \times \frac{12 \times 11}{2} = 105 \times 66 = 6\,930 \text{ jurys}.$$
3. Le contraire de « au moins un de chaque discipline » est « jury 100% sciences OU jury 100% lettres ».
   - Nombre de jurys 100% sciences : $\binom{15}{4} = \frac{15 \times 14 \times 13 \times 12}{24} = 1\,365$.
   - Nombre de jurys 100% lettres : $\binom{12}{4} = \frac{12 \times 11 \times 10 \times 9}{24} = 495$.
   Ces deux cas étant disjoints, le total des jurys non mixtes est $1\,365 + 495 = 1\,860$.
   Par soustraction au total général :
   $$17\,550 - 1\,860 = 15\,690 \text{ jurys mixtes}.$$

#### Exemple 3 : Les mains de Poker
Dans un jeu de 52 cartes (4 couleurs : Pique, Cœur, Carreau, Trèfle ; 13 hauteurs de l'As au Roi), une « main » est une combinaison de 5 cartes. Le nombre total de mains est $\binom{52}{5} = 2\,598\,960$.
1. Dénombrer le nombre de « Carrés » (4 cartes de même hauteur + 1 cinquième carte quelconque).
2. Dénombrer le nombre de « Fulls » (3 cartes d'une même hauteur + 2 cartes d'une autre hauteur).

**Solution détaillée :**
1. **Carré :**
   - Étape 1 : Choisir la hauteur du carré parmi les 13 possibles : 13 choix.
   - Étape 2 : Prendre les 4 cartes de cette hauteur : $\binom{4}{4} = 1$ façon.
   - Étape 3 : Choisir la 5ᵉ carte parmi les 48 cartes restantes de hauteur différente : 48 choix.
   Total : $13 \times 1 \times 48 = 624$ carrés possibles.
2. **Full :**
   - Étape 1 : Choisir la hauteur du brelan (3 cartes) parmi les 13 hauteurs : 13 choix.
   - Étape 2 : Choisir les 3 couleurs du brelan parmi 4 : $\binom{4}{3} = 4$ façons.
   - Étape 3 : Choisir la hauteur de la paire parmi les 12 hauteurs restantes : 12 choix.
   - Étape 4 : Choisir les 2 couleurs de la paire parmi 4 : $\binom{4}{2} = 6$ façons.
   Total : $13 \times 4 \times 12 \times 6 = 3\,744$ fulls possibles.

#### Exemple 4 : Anagrammes et lettres répétées
Combien d'anagrammes distinctes (ayant un sens ou non) peut-on former avec le mot **PARALLELE** ?

**Solution détaillée :**
Le mot contient 9 lettres au total :
- P : 1 fois
- A : 2 fois
- R : 1 fois
- L : 3 fois
- E : 2 fois
Vérification de la somme : $1 + 2 + 1 + 3 + 2 = 9$.
Si toutes les lettres étaient dotées d'un indice (ex : $A_1, A_2, L_1, L_2, L_3$), il y aurait $9! = 362\,880$ permutations.
Mais intervertir les deux A entre eux ne modifie pas le mot (il y a $2!$ permutations neutres pour A).
De même, permuter les trois L entre eux donne $3!$ configurations identiques, et les deux E donnent $2!$.
D'après le principe des permutations avec répétition (ou choix successif des places) :
$$\text{Nombre d'anagrammes} = \frac{9!}{1! \times 2! \times 1! \times 3! \times 2!} = \frac{362\,880}{1 \times 2 \times 1 \times 6 \times 2} = \frac{362\,880}{24} = 15\,120.$$
*(Autre vision équivalente : choisir les 3 places des L parmi 9 ($\binom{9}{3}$), puis les 2 places des A parmi 6 restantes ($\binom{6}{2}$), puis les 2 places des E parmi 4 restantes ($\binom{4}{2}$), etc. Le produit donne exactement 15 120).*

#### Exemple 5 : Déplacements sur un quadrillage
Dans une ville carrée quadrillée, un piéton part du point $A(0,0)$ pour rejoindre le point $B(5,3)$. À chaque intersection, il ne peut se déplacer que vers l'Est ($E$, d'un pas vers la droite) ou vers le Nord ($N$, d'un pas vers le haut).
Combien de chemins minimaux mènent de $A$ à $B$ ?

```
 B(5,3)  ┌───┬───┬───┬───┬───┐
         │   │   │   │   │   │
         ├───┼───┼───┼───┼───┤
         │   │   │   │   │   │
         ├───┼───┼───┼───┼───┤
 A(0,0)  └───┴───┴───┴───┴───┘
```

**Solution détaillée :**
Pour aller de $(0,0)$ à $(5,3)$, tout trajet minimal doit comporter exactement 5 déplacements vers l'Est ($E$) et 3 déplacements vers le Nord ($N$).
La longueur totale de chaque chemin est donc de $5 + 3 = 8$ pas.
Un trajet est entièrement défini par un mot de 8 lettres composé de 5 lettres $E$ et 3 lettres $N$ (par exemple : $E-E-N-E-N-E-E-N$).
Il suffit donc de choisir l'emplacement des 3 déplacements vers le Nord parmi les 8 étapes du trajet :
$$\text{Nombre de chemins} = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56.$$
*(On aurait pu choisir les 5 emplacements vers l'Est : $\binom{8}{5} = \binom{8}{3} = 56$).*

#### Exemple 6 : Terme d'un développement du binôme
Dans le développement de $\left(2x^2 - \frac{1}{x}\right)^9$, déterminer le terme indépendant de $x$ (le terme constant).

**Solution détaillée :**
Par la formule du binôme de Newton avec $a = 2x^2$ et $b = -\frac{1}{x} = -x^{-1}$ :
$$\left(2x^2 - \frac{1}{x}\right)^9 = \sum_{k=0}^9 \binom{9}{k} (2x^2)^{9-k} \left(-\frac{1}{x}\right)^k$$
Isolons les puissances de $x$ dans le terme général :
$$T_k = \binom{9}{k} 2^{9-k} (x^2)^{9-k} (-1)^k x^{-k} = \binom{9}{k} 2^{9-k} (-1)^k \cdot x^{18 - 2k - k} = \binom{9}{k} 2^{9-k} (-1)^k \cdot x^{18 - 3k}$$
Le terme est indépendant de $x$ lorsque l'exposant de $x$ est nul :
$$18 - 3k = 0 \iff 3k = 18 \iff k = 6.$$
Puisque $k = 6$ est bien un entier compris entre 0 et 9, ce terme existe. Sa valeur est :
$$T_6 = \binom{9}{6} 2^{9-6} (-1)^6 = \binom{9}{3} \times 2^3 \times 1 = \frac{9 \times 8 \times 7}{6} \times 8 = 84 \times 8 = 672.$$
Le terme constant vaut **672**.

---

### Ce qu'il faut retenir

1. **Principes de base :**
   - Réunion d'ensembles disjoints : $|A \cup B| = |A| + |B|$.
   - Complémentaire : $|A| = |E| - |\overline{A}|$ (penser systématiquement au contraire pour *« au moins un »*).
   - Produit cartésien : $|A \times B| = |A| \times |B|$.

2. **Dénombrement avec ordre :**
   - Avec répétition ($k$-uplet) : $n^k$.
   - Sans répétition ($k$-uplet distincts / arrangements) : $A_n^k = \frac{n!}{(n-k)!} = n(n-1)\dots(n-k+1)$.
   - Permutation de $n$ éléments : $n! = n \times (n-1) \times \dots \times 1$, avec $0! = 1$.

3. **Dénombrement sans ordre :**
   - Combinaisons de $k$ parmi $n$ : $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.
   - Symétrie : $\binom{n}{k} = \binom{n}{n-k}$.
   - Relation de Pascal : $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

4. **Sommes et puissances :**
   - Somme d'une ligne du triangle de Pascal : $\sum_{k=0}^n \binom{n}{k} = 2^n$.
   - Binôme de Newton : $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 1.** Calculer à la main : $5!$, $\frac{8!}{6!}$, $\binom{7}{2}$, $\binom{9}{9}$, et $\binom{10}{7}$.
**Exercice 2.** Un mot de passe informatique doit comporter 8 caractères choisis parmi les 26 lettres minuscules de l'alphabet.
1. Combien de mots de passe peut-on former si la répétition est autorisée ?
2. Combien si toutes les lettres doivent être différentes ?
**Exercice 3.** Une course réunit 12 chevaux au départ. Combien y a-t-il de tiercés possibles :
1. Dans l'ordre exact ?
2. Dans le désordre (les trois chevaux qui montent sur le podium sans précision de rang) ?
**Exercice 4.** Démontrer par le calcul que $\binom{n}{2} = \frac{n(n-1)}{2}$. Que représente cette quantité si $n$ personnes se serrent toutes la main une fois ?
**Exercice 5.** Développer à l'aide de la formule du binôme :
1. $(x + 2)^4$
2. $(2x - 1)^3$
**Exercice 6.** Combien d'anagrammes peut-on former avec les lettres du mot **MATHS** ? Et avec le mot **LIVRE** ?
**Exercice 7.** Une urne contient 6 boules rouges, 4 vertes et 2 jaunes. On tire simultanément 3 boules. Combien y a-t-il de tirages possibles au total ?

#### Niveau ★★ (Réflexion et méthodes classiques)

**Exercice 8.** On lance 5 dés équilibrés à 6 faces (comme au Yahtzee).
1. Combien de lancers différents peut-on obtenir au total ?
2. Combien de lancers ne comportent aucun 6 ?
3. En déduire le nombre de lancers contenant au moins un 6.
**Exercice 9.** Combien de nombres entiers compris entre 1000 et 9999 (inclus) :
1. Ont tous leurs chiffres distincts ?
2. Sont des nombres pairs ayant tous leurs chiffres distincts ?
**Exercice 10.** Un club d'échecs compte 14 membres : 8 adultes et 6 jeunes. On doit désigner une équipe de 5 joueurs.
1. De combien de façons peut-on composer cette équipe ?
2. Combien d'équipes contiennent exactement 3 adultes et 2 jeunes ?
3. Combien d'équipes contiennent au moins un adulte et au moins un jeune ?
**Exercice 11.** Anagrammes avec doublons :
Combien d'anagrammes distinctes possède le mot **ANANAS** ?
**Exercice 12.** Un polygone convexe possède $n$ sommets ($n \geq 4$).
Combien de diagonales possède ce polygone ? *(Indication : une diagonale est un segment reliant deux sommets non consécutifs).*
**Exercice 13.** Déterminer le coefficient de $x^5$ dans le développement de $(3x - 2)^8$.
**Exercice 14.** Démontrer que pour tout entier $n \geq 1$ :
$$\sum_{k=0}^n (-1)^k \binom{n}{k} = \binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \dots + (-1)^n \binom{n}{n} = 0$$
*(Indication : appliquer le binôme de Newton à $(1 - 1)^n$).*
**Exercice 15.** Le problème des anniversaires.
Dans une classe de 30 élèves, on suppose que chaque élève est né un jour parmi les 365 jours de l'année (on ignore les années bissextiles), de façon indépendante.
1. Combien y a-t-il de répartitions d'anniversaires possibles pour les 30 élèves ?
2. Combien de répartitions où les 30 élèves ont tous des dates d'anniversaire distinctes ?
3. En déduire l'expression de la probabilité qu'au moins deux élèves aient leur anniversaire le même jour.

#### Niveau ★★★ (Approfondissements et défis)

**Exercice 16.** La formule du comité et du président :
1. Démontrer algébriquement que pour tous entiers $1 \leq k \leq n$ :
   $$k \binom{n}{k} = n \binom{n-1}{k-1}$$
2. Donner une interprétation combinatoire élégante de cette formule en considérant le choix d'un comité de $k$ personnes parmi $n$ avec la désignation d'un président au sein du comité.
**Exercice 17.** Calculer la somme :
$$S = \sum_{k=1}^n k \binom{n}{k} = 1\binom{n}{1} + 2\binom{n}{2} + 3\binom{n}{3} + \dots + n\binom{n}{n}$$
*(Indication : utiliser le résultat de l'exercice 16 ou dériver la fonction $f(x) = (1+x)^n$).*
**Exercice 18.** Le principe des bâtons et des étoiles (Stars and Bars).
On veut distribuer 10 bonbons identiques à 3 enfants (Alice, Bob et Chloé).
1. Combien de distributions possibles y a-t-il si chaque enfant peut recevoir 0, 1 ou plusieurs bonbons ?
2. Combien de distributions si chaque enfant doit obligatoirement recevoir au moins un bonbon ?
**Exercice 19.** Formule de Vandermonde.
En développant de deux façons l'égalité polynomiale $(1+x)^{m+n} = (1+x)^m (1+x)^n$, démontrer la relation :
$$\sum_{k=0}^p \binom{m}{k}\binom{n}{p-k} = \binom{m+n}{p}$$
Donner également une justification combinatoire de cette formule.
**Exercice 20.** Somme des carrés des coefficients binomiaux.
En utilisant la formule de Vandermonde (exercice 19) avec $m = n$ et $p = n$, démontrer que :
$$\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$$
**Exercice 21.** Les dérangements (problème des chapeaux).
$n$ personnes déposent leur manteau au vestiaire. À la sortie, le vestiaire distribue au hasard un manteau à chacun.
Un dérangement est une permutation où personne ne récupère son propre manteau.
Montrer par le principe d'inclusion-exclusion que le nombre de dérangements $D_n$ vaut :
$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$
**Exercice 22.** Les chemins de Dyck et les nombres de Catalan.
On considère des chemins sur une grille menant de $(0,0)$ à $(n,n)$ formés de déplacements $(+1, 0)$ et $(0, +1)$, sans jamais franchir la diagonale $y = x$ (c'est-à-dire restant toujours dans le demi-plan $y \leq x$).
Montrer par le principe de réflexion de Désiré André que le nombre de tels chemins est donné par le nombre de Catalan :
$$C_n = \frac{1}{n+1} \binom{2n}{n}$$

---

### Solutions

**Solution 1.**
- $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.
- $\frac{8!}{6!} = 8 \times 7 = 56$.
- $\binom{7}{2} = \frac{7 \times 6}{2 \times 1} = 21$.
- $\binom{9}{9} = 1$.
- $\binom{10}{7} = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.

**Solution 2.**
1. $26^8 = 208\,827\,064\,576$.
2. $A_{26}^8 = 26 \times 25 \times 24 \times 23 \times 22 \times 21 \times 20 \times 19 = 62\,990\,928\,000$.

**Solution 3.**
1. Tiercé dans l'ordre : $A_{12}^3 = 12 \times 11 \times 10 = 1\,320$.
2. Tiercé dans le désordre : $\binom{12}{3} = \frac{1\,320}{6} = 220$.

**Solution 4.**
$\binom{n}{2} = \frac{n!}{2!(n-2)!} = \frac{n(n-1)(n-2)!}{2(n-2)!} = \frac{n(n-1)}{2}$.
Une poignée de main implique 2 personnes distinctes sans notion d'ordre. Entre $n$ personnes, il y a donc $\binom{n}{2} = \frac{n(n-1)}{2}$ poignées de main échangées.

**Solution 5.**
1. $(x+2)^4 = \binom{4}{0}x^4 + \binom{4}{1}x^3(2) + \binom{4}{2}x^2(2^2) + \binom{4}{3}x(2^3) + \binom{4}{4}(2^4) = x^4 + 8x^3 + 24x^2 + 32x + 16$.
2. $(2x-1)^3 = (2x)^3 - 3(2x)^2(1) + 3(2x)(1^2) - 1^3 = 8x^3 - 12x^2 + 6x - 1$.

**Solution 6.**
- MATHS : 5 lettres distinctes, donc $5! = 120$ anagrammes.
- LIVRE : 5 lettres distinctes, donc $5! = 120$ anagrammes.

**Solution 7.**
Total des boules : $6 + 4 + 2 = 12$. Tirage simultané de 3 boules : $\binom{12}{3} = \frac{12 \times 11 \times 10}{6} = 220$ tirages.

**Solution 8.**
1. $6^5 = 7\,776$ lancers.
2. Pour chaque dé, 5 valeurs possibles excluant le 6 : $5^5 = 3\,125$ lancers.
3. Par passage au complémentaire : $7\,776 - 3\,125 = 4\,651$ lancers comportent au moins un 6.

**Solution 9.**
Un nombre à 4 chiffres s'écrit $c_1 c_2 c_3 c_4$ avec $c_1 \in \{1..9\}$ (9 choix) et $c_2, c_3, c_4 \in \{0..9\}$.
1. Chiffres distincts :
   - Pour $c_1$ : 9 choix (de 1 à 9).
   - Pour $c_2$ : 9 choix (de 0 à 9 sauf $c_1$).
   - Pour $c_3$ : 8 choix.
   - Pour $c_4$ : 7 choix.
   Total : $9 \times 9 \times 8 \times 7 = 4\,536$ nombres.
2. Nombres pairs à chiffres distincts ($c_4 \in \{0, 2, 4, 6, 8\}$) :
   - Cas 1 : $c_4 = 0$ (1 choix). Alors $c_1$ a 9 choix (de 1 à 9), $c_2$ a 8 choix, $c_3$ a 7 choix. Soit $1 \times 9 \times 8 \times 7 = 504$ nombres.
   - Cas 2 : $c_4 \in \{2, 4, 6, 8\}$ (4 choix). Alors $c_1$ ne peut être ni 0 ni $c_4$, donc il a $10 - 2 = 8$ choix. Ensuite $c_2$ a 8 choix (parmi les restants incluant 0), et $c_3$ a 7 choix. Soit $4 \times 8 \times 8 \times 7 = 1\,792$ nombres.
   Total : $504 + 1\,792 = 2\,296$ nombres pairs.

**Solution 10.**
1. Équipes sans contrainte : $\binom{14}{5} = \frac{14 \times 13 \times 12 \times 11 \times 10}{120} = 2\,002$.
2. 3 adultes et 2 jeunes : $\binom{8}{3} \times \binom{6}{2} = 56 \times 15 = 840$.
3. Contraire : équipe uniquement d'adultes ($\binom{8}{5} = 56$) ou uniquement de jeunes ($\binom{6}{5} = 6$).
   Total mixtes : $2\,002 - (56 + 6) = 1\,940$ équipes.

**Solution 11.**
Le mot ANANAS a 6 lettres avec 3 A, 2 N et 1 S.
Nombre d'anagrammes = $\frac{6!}{3! \times 2! \times 1!} = \frac{720}{6 \times 2} = 60$.

**Solution 12.**
Il y a $\binom{n}{2}$ segments reliant deux sommets quelconques. Parmi ces segments, $n$ sont les côtés du polygone. Le nombre de diagonales est donc :
$$\binom{n}{2} - n = \frac{n(n-1)}{2} - n = \frac{n^2 - 3n}{2} = \frac{n(n-3)}{2}.$$

**Solution 13.**
Dans $(3x - 2)^8 = \sum_{k=0}^8 \binom{8}{k} (3x)^k (-2)^{8-k}$, le terme en $x^5$ correspond à $k=5$ :
$\binom{8}{5} (3x)^5 (-2)^3 = 56 \times 243 x^5 \times (-8) = -108\,864 x^5$. Le coefficient est **$-108\,864$**.

**Solution 14.**
D'après le binôme de Newton, $(1 + x)^n = \sum_{k=0}^n \binom{n}{k} x^k$.
Pour $x = -1$ et $n \geq 1$ :
$$(1 + (-1))^n = 0^n = 0 = \sum_{k=0}^n \binom{n}{k} (-1)^k$$

**Solution 15.**
1. Pour chaque élève, 365 dates possibles : $365^{30}$.
2. Si toutes les dates sont distinctes : arrangement $A_{365}^{30} = 365 \times 364 \times \dots \times 336$.
3. Probabilité que deux élèves au moins partagent leur anniversaire :
   $$P = 1 - \frac{A_{365}^{30}}{365^{30}} \approx 1 - 0{,}2937 = 0{,}7063 \quad (\approx 70{,}6\,\% !)$$
   Dès 23 personnes, cette probabilité dépasse déjà 50 % !

**Solution 16.**
1. Algébriquement :
   $$k \binom{n}{k} = k \frac{n!}{k!(n-k)!} = \frac{n!}{(k-1)!(n-k)!} = n \frac{(n-1)!}{(k-1)!((n-1)-(k-1))!} = n \binom{n-1}{k-1}.$$
2. Interprétation : On veut former un comité de $k$ personnes parmi $n$ avec un président.
   - Méthode A : on choisit d'abord les $k$ membres du comité ($\binom{n}{k}$ façons), puis on choisit le président parmi ces $k$ membres ($k$ façons). Total : $k \binom{n}{k}$.
   - Méthode B : on choisit d'abord le président parmi les $n$ candidats ($n$ façons), puis on choisit les $k-1$ membres restants parmi les $n-1$ personnes disponibles ($\binom{n-1}{k-1}$ façons). Total : $n \binom{n-1}{k-1}$.
   Les deux méthodes dénombrant la même situation, l'égalité est démontrée.

**Solution 17.**
En utilisant la relation précédente $k\binom{n}{k} = n\binom{n-1}{k-1}$ :
$$S = \sum_{k=1}^n n \binom{n-1}{k-1} = n \sum_{j=0}^{n-1} \binom{n-1}{j} = n \cdot 2^{n-1}.$$

**Solution 18.**
1. Distribuer 10 bonbons à 3 enfants équivaut à placer 10 étoiles et 2 séparateurs (bâtons) parmi $10 + 2 = 12$ emplacements :
   Nombre de façons = $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$.
2. Si chaque enfant doit recevoir au moins un bonbon, on donne d'abord 1 bonbon à chacun (reste 7 bonbons). On distribue les 7 bonbons restants entre les 3 enfants sans contrainte :
   $\binom{7+3-1}{2} = \binom{9}{2} = 36$.

**Solution 19.**
Dans le produit $(1+x)^m (1+x)^n = (1+x)^{m+n}$, le coefficient de $x^p$ à droite est $\binom{m+n}{p}$.
À gauche, un terme en $x^p$ provient du produit d'un terme $\binom{m}{k} x^k$ du premier facteur par un terme $\binom{n}{p-k} x^{p-k}$ du second facteur, pour $k$ allant de 0 à $p$. La somme de ces produits donne $\sum_{k=0}^p \binom{m}{k}\binom{n}{p-k}$.
*Justification combinatoire :* Pour choisir $p$ personnes dans un groupe de $m$ hommes et $n$ femmes, on peut choisir $k$ hommes et $p-k$ femmes, pour tout $k \in \{0, \dots, p\}$.

**Solution 20.**
Dans la formule de Vandermonde avec $m = n$ et $p = n$ :
$$\sum_{k=0}^n \binom{n}{k}\binom{n}{n-k} = \binom{2n}{n}$$
Or par symétrie, $\binom{n}{n-k} = \binom{n}{k}$. Donc :
$$\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}.$$

**Solution 21.**
Soit $A_i$ l'ensemble des permutations laissant la $i$-ème personne avec son propre manteau.
On cherche $D_n = n! - |\bigcup_{i=1}^n A_i|$.
Par le principe d'inclusion-exclusion :
$$|\bigcup_{i=1}^n A_i| = \sum_{i} |A_i| - \sum_{i<j} |A_i \cap A_j| + \dots + (-1)^{n-1} |A_1 \cap \dots \cap A_n|$$
L'intersection de $k$ ensembles $A_i$ correspond aux permutations fixant au moins $k$ éléments précis, soit $(n-k)!$ permutations. Il y a $\binom{n}{k}$ telles intersections.
Le terme d'ordre $k$ vaut donc $\binom{n}{k} (n-k)! = \frac{n!}{k!}$.
D'où $D_n = n! - \sum_{k=1}^n (-1)^{k-1} \frac{n!}{k!} = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$.
*(Remarque : quand $n \to \infty$, $D_n / n! \to e^{-1} \approx 36{,}8\,\%$).*

**Solution 22.**
Le nombre total de chemins de $(0,0)$ à $(n,n)$ est $\binom{2n}{n}$.
Un chemin qui traverse la droite $y = x$ touche au moins une fois la droite $y = x + 1$.
Considérons le premier point de contact $P$ avec cette droite. En effectuant une symétrie axiale par rapport à $y = x + 1$ de toute la fin du chemin après $P$, le point d'arrivée $(n, n)$ est envoyé sur le point $(n-1, n+1)$.
Cette correspondance est une bijection entre les chemins qui traversent la diagonale et l'ensemble des chemins allant de $(0,0)$ à $(n-1, n+1)$.
Le nombre de chemins interdits est donc $\binom{2n}{n-1}$.
Le nombre de chemins de Dyck est ainsi :
$$C_n = \binom{2n}{n} - \binom{2n}{n-1} = \binom{2n}{n} - \frac{n}{n+1}\binom{2n}{n} = \frac{1}{n+1}\binom{2n}{n}.$$

---

### La question qui ouvre la suite

Nous venons d'apprendre à dénombrer le nombre de façons de choisir $k$ succès parmi $n$ essais : c'est le coefficient binomial $\binom{n}{k}$.
Mais que se passe-t-il lorsque chaque tentative individuelle est gouvernée par le hasard, avec une probabilité $p$ de réussir et $1-p$ d'échouer ?
Si nous lançons une pièce mille fois, combien de fois la face « Pile » va-t-elle apparaître ? Peut-on être certain que la fréquence se stabilisera autour de $50\,\%$ ?
C'est le saut vertigineux du dénombrement vers la loi binomiale et les grands théorèmes limites : bienvenue dans **le Chapitre 54 et les Mille Lancers de la Pièce**.
