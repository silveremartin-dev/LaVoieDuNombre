# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 29 : Le Partage d'Euclide

> *« Un nombre n'est pas une pâte molle qu'on étale à volonté : c'est un édifice bâti avec des pierres premières taillées dans le diamant. Trouve les briques fondamentales, et tu comprendras comment partager sans briser. »*

---

### Ce que tu vas découvrir

- Pourquoi certains nombres refusent d'être partagés et forment les **atomes de l'arithmétique** : les nombres premiers.
- Comment décomposer n'importe quel nombre entier en un **produit unique de facteurs premiers** grâce à l'arbre et à la potence.
- Ce qu'est le **PGCD** (Plus Grand Commun Diviseur) et comment le calculer de trois façons différentes.
- L'astuce fulgurante inventée par **Euclide** il y a plus de vingt-trois siècles pour trouver le diviseur commun en quelques divisions euclidiennes.
- Comment rendre une **fraction irréductible** d'un seul coup de baguette magique.
- Comment résoudre des casse-têtes concrets de la vie réelle : **paver une pièce sans casser un seul carreau** et composer des **colis cadeaux identiques** sans laisser une seule miette.

---

### 1. Le problème : la mosaïque du Pharaon et les paniers du scribe

Alexandrie, vers l'an **300 avant notre ère**.
Le roi Ptolémée Iᵉʳ fait construire une immense salle d'apparat dans son palais royal. Deux artisans se présentent devant l'architecte en chef, le front plissé par le souci.

* Le premier est le **maître mosaïste**. Le sol de la salle est un grand rectangle mesurant **420 centimètres de long sur 132 centimètres de large**. Le roi a ordonné :
  *« Je veux que ce sol soit recouvert de dalles de marbre carrées, toutes rigoureusement identiques. Je refuse qu'on découpe la moindre dalle sur les bords : chaque carreau doit être posé entier ! Et pour que le sol soit somptueux, je veux que ces dalles soient **les plus grandes possibles** ! »*
  Le mosaïste gémit : des carreaux de 1 cm marcheraient, bien sûr, mais il en faudrait 55 440 et ce serait minuscule ! Des carreaux de 2 cm marcheraient aussi. Mais quelle est la plus grande taille possible ?

* Le second artisan est le **scribe intendant** des fêtes. Pour honorer les dignitaires étrangers, il dispose de deux coffres de denrées précieuses :
  - Un coffre contenant **315 grenades d'Égypte** ;
  - Un coffre contenant **180 loukoums au miel**.
  Le roi exige que l'intendant prépare des corbeilles cadeaux pour les invités :
  *« Toutes les corbeilles doivent être rigoureusement identiques : exactement le même nombre de grenades et le même nombre de loukoums dans chaque panier. Et je ne veux aucun reste dans les coffres ! Enfin, je veux inviter **le plus grand nombre possible** de dignitaires ! »*

```
   Problème 1 : Pavage sans chute           Problème 2 : Corbeilles sans reste
   ┌───────────────────────────────┐
   │                               │         315 grenades      180 loukoums
   │   420 cm                      │          (à répartir)      (à répartir)
   │                               │                │                 │
   │ 132 cm                        │                ▼                 ▼
   │                               │         [ Panier 1 ]      [ Panier 2 ] ...
   └───────────────────────────────┘         Contenus rigoureusement identiques !
   Dalles carrées entières maximales ?       Nombre maximal d'invités ?
```

Comment résoudre ces deux énigmes sans tester tous les nombres au hasard pendant trois semaines ?
Dans les deux cas, le problème est le même : nous cherchons un nombre entier qui **divise parfaitement** deux nombres à la fois, et qui soit **le plus grand possible**.

Pour éclairer les artisans, un homme s'avance dans la cour du palais. Il tient sous le bras les papyrus de son grand chef-d'œuvre, les *Éléments*. Il s'appelle **Euclide**.

---

### 2. Multiples et diviseurs : le vocabulaire de la précision

Avant d'entrer dans l'atelier d'Euclide, il faut maîtriser la langue de l'arithmétique. Ces mots ont un sens précis qu'il ne faut jamais mélanger.

Soient deux nombres entiers positifs $a$ et $b$ (avec $b \neq 0$).
Si la division de $a$ par $b$ « tombe juste » — c'est-à-dire si le reste de la division euclidienne est égal à zéro —, on peut écrire :
$$a = b \times k \quad (\text{où } k \text{ est un entier}).$$

On dit alors indifféremment :
- **$a$ est un multiple de $b$** (ex. : 42 est un multiple de 6, car $42 = 6 \times 7$).
- **$b$ est un diviseur de $a$** (ex. : 6 est un diviseur de 42).
- **$b$ divise $a$** (noté parfois $b \mid a$).
- **$a$ est divisible par $b$**.

> **⚠️ Attention, piège ! Le sens de la phrase !**
> Ne confonds jamais le « père » et le « fils » :
> - Dire « 6 divise 42 » est **vrai**.
> - Dire « 42 divise 6 » est **totalement faux** ! (42 ne rentre pas dans 6).
> L'astuce pour ne pas hésiter : le **multiple** est toujours plus grand (ou égal), le **diviseur** est toujours plus petit (ou égal).

#### Rappel express : les critères de divisibilité
Pour savoir rapidement si un nombre en divise un autre sans poser la division :
- Un nombre est divisible par **2** s'il est pair (se termine par 0, 2, 4, 6, 8).
- Un nombre est divisible par **3** si la somme de ses chiffres est un multiple de 3 (ex. : $471 \implies 4+7+1 = 12$, divisible par 3).
- Un nombre est divisible par **4** si le nombre formé par ses deux derniers chiffres est un multiple de 4 (ex. : $3\,724 \implies 24 = 4 \times 6$, donc divisible par 4).
- Un nombre est divisible par **5** s'il se termine par 0 ou 5.
- Un nombre est divisible par **9** si la somme de ses chiffres est un multiple de 9 (ex. : $855 \implies 8+5+5 = 18$, divisible par 9).
- Un nombre est divisible par **10** s'il se termine par 0.

---

### 3. Les nombres premiers : les atomes de l'univers mathématique

Prends le nombre 12. Tu peux le découper : $12 = 3 \times 4$. Puis découper encore : $4 = 2 \times 2$. Tu obtiens $12 = 2 \times 2 \times 3$.
Peux-tu découper 2 ou 3 ? Non ! Deux et trois sont insécables. Ils ne peuvent être divisés que par 1 et par eux-mêmes.

> **📐 Définition officielle — Nombre premier.**
> Un nombre entier naturel est dit **premier** s'il possède **exactement deux diviseurs distincts** : 1 et lui-même.

Regarde attentivement les conséquences de cette définition :
- **Le nombre 0 n'est pas premier** : il a une infinité de diviseurs (n'importe quel nombre non nul divise 0).
- **Le nombre 1 n'est PAS premier** : il n'a qu'un **seul** diviseur (lui-même). La règle impose *deux* diviseurs distincts. Si 1 était premier, la décomposition en facteurs premiers perdrait son unicité ($6 = 2 \times 3 = 1 \times 2 \times 3 = 1 \times 1 \times 2 \times 3\dots$).
- **Le nombre 2 est premier** : c'est même le **seul nombre premier pair** de l'univers ! Tous les autres nombres pairs sont divisibles par 2, donc ils ne sont pas premiers.

#### La liste des nombres premiers inférieurs à 30
À connaître par cœur comme ses tables :
$$\mathbf{2, \quad 3, \quad 5, \quad 7, \quad 11, \quad 13, \quad 17, \quad 19, \quad 23, \quad 29}$$
*(Et en poussant un peu : 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97).*

> **💡 Le savais-tu ?**
> Dans le Livre IX des *Éléments*, Euclide a démontré une vérité vertigineuse : **il existe une infinité de nombres premiers**. Même si l'on voyageait pendant des millions d'années dans les nombres gigantesques, on ne manquerait jamais de nouveaux nombres premiers !

---

### 4. La décomposition en facteurs premiers

Voici le théorème le plus important de toute l'arithmétique. Il est si capital qu'on l'appelle le **théorème fondamental de l'arithmétique**.

> **📐 Théorème fondamental de l'arithmétique —**
> Tout nombre entier supérieur ou égal à 2 peut s'écrire comme un **produit de nombres premiers**.
> Cette décomposition est **unique**, à l'ordre des facteurs près.

C'est la « carte d'identité génétique » du nombre. Deux nombres différents ne peuvent jamais avoir la même décomposition.

#### Deux méthodes pratiques pour décomposer un nombre

Prenons le nombre **$360$** à décomposer.

##### Méthode 1 : L'arbre de décomposition (idéal pour calculer mentalement)
On coupe le nombre en deux facteurs évidents, puis on continue de couper les branches jusqu'à n'avoir que des nombres premiers au bout de chaque feuille.

```
                     360
                    /   \
                  36  ×  10
                 /  \    / \
                6 ×  6  2 × 5
               / \  / \
              2  3 2   3
```

On ramasse toutes les feuilles premières :
$$360 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 = \mathbf{2^3 \times 3^2 \times 5}$$

##### Méthode 2 : La potence verticale des divisions successives (méthode officielle infaillible)
On trace une barre verticale. À gauche, on écrit le nombre. À droite, on teste les nombres premiers dans l'ordre croissant ($2, 3, 5, 7, 11\dots$) et on divise dès que c'est possible :

```
     360 │ 2    (360 est pair, on divise par 2)
     180 │ 2    (180 est pair, on divise par 2)
      90 │ 2    (90 est pair, on divise par 2)
      45 │ 3    (45 : 4+5=9 multiple de 3, on divise par 3)
      15 │ 3    (15 est divisible par 3)
       5 │ 5    (5 est premier, on divise par 5)
       1 │      (C'est terminé !)
```

La colonne de droite donne directement les facteurs :
$$360 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 = \mathbf{2^3 \times 3^2 \times 5}.$$

---

### 5. Le PGCD : Plus Grand Commun Diviseur

#### 5.1 Définition

Quand on compare deux nombres entiers $a$ et $b$, certains entiers divisent à la fois $a$ et $b$ : ce sont leurs **diviseurs communs**.
Comme 1 divise tous les entiers, il y a toujours au moins un diviseur commun : le nombre 1.

> **📐 Définition — PGCD.**
> Parmi tous les diviseurs communs à deux nombres entiers non nuls $a$ et $b$, le plus grand d'entre eux est appelé le **Plus Grand Commun Diviseur**, noté **$\text{PGCD}(a ; b)$**.

> **📐 Définition — Nombres premiers entre eux.**
> Deux nombres entiers sont dits **premiers entre eux** lorsque leur seul diviseur commun est 1, c'est-à-dire :
> $$\text{PGCD}(a ; b) = 1$$
> *(Exemple : 8 et 15 ne sont pas des nombres premiers, mais ils sont premiers entre eux car les diviseurs de 8 sont {1, 2, 4, 8} et ceux de 15 sont {1, 3, 5, 15} ; le seul diviseur commun est 1).*

#### 5.2 Première méthode : Par la décomposition en facteurs premiers

Pour trouver le PGCD de deux nombres décomposés en produit de facteurs premiers :
1. On repère les **facteurs premiers communs** aux deux nombres.
2. Pour chaque facteur commun, on prend **le plus petit exposant** avec lequel il apparaît.
3. On multiplie ces facteurs entre eux.

*Exemple :* Calculons le PGCD de $180$ et $315$ (les denrées de notre banquet !) :
- $180 = 2^2 \times 3^2 \times 5$
- $315 = 3^2 \times 5 \times 7$

Facteurs communs : 3 et 5.
- La plus petite puissance de 3 est $3^2$.
- La plus petite puissance de 5 est $5^1$.
$$\text{PGCD}(180 ; 315) = 3^2 \times 5 = 9 \times 5 = \mathbf{45}.$$
Le scribe pourra donc confectionner au maximum **45 corbeilles identiques** !
Chaque corbeille contiendra :
- $315 \div 45 = 7$ grenades ;
- $180 \div 45 = 4$ loukoums.
Pas une seule miette de reste !

---

### 6. Les deux algorithmes historiques : soustractions et divisions

Quand les nombres sont très grands, trouver tous leurs diviseurs ou leur décomposition en facteurs premiers peut être long et fastidieux. Les Anciens ont trouvé des raccourcis fulgurants.

#### 6.1 L'algorithme des soustractions successives

Cet algorithme repose sur une propriété arithmétique très simple :
> **📐 Propriété des soustractions —**
> Si un nombre $d$ divise à la fois $a$ et $b$ (avec $a \ge b$), alors $d$ divise aussi leur différence $a - b$.
> Par conséquent : $\text{PGCD}(a ; b) = \text{PGCD}(b ; a - b)$.

**Le procédé :** On remplace le plus grand des deux nombres par leur différence, et on recommence jusqu'à obtenir deux nombres égaux. Ce nombre final est le PGCD !

*Exemple :* Calculons $\text{PGCD}(75 ; 45)$ :
- $75 - 45 = 30 \implies \text{on garde } 45 \text{ et } 30$
- $45 - 30 = 15 \implies \text{on garde } 30 \text{ et } 15$
- $30 - 15 = 15 \implies \text{on garde } 15 \text{ et } 15$
- $15 - 15 = 0$
Les deux nombres égaux obtenus sont 15, donc $\text{PGCD}(75 ; 45) = \mathbf{15}$.

> **⚠️ La limite des soustractions :**
> Imagine que tu doives calculer $\text{PGCD}(1\,000\,000 ; 2)$. Tu vas devoir soustraire 2 cinq cent mille fois ! C'est une perte de temps absurde. Heureusement, Euclide a eu une idée de génie.

#### 6.2 L'algorithme d'Euclide (divisions successives)

Au lieu de soustraire $b$ un par un, pourquoi ne pas soustraire d'un seul coup le plus de paquets de $b$ possibles ? C'est exactement le principe de la **division euclidienne** :
$$a = b \times q + r \quad (0 \le r < b)$$

> **📐 Théorème d'Euclide —**
> Si la division euclidienne de $a$ par $b$ donne un reste $r$, alors :
> $$\text{PGCD}(a ; b) = \text{PGCD}(b ; r)$$

**Le procédé de l'algorithme d'Euclide :**
1. On effectue la division euclidienne du plus grand nombre par le plus petit.
2. Si le reste n'est pas nul, on recommence en divisant le diviseur précédent par le reste obtenu.
3. On s'arrête dès que le reste est nul ($r = 0$).
4. **Le PGCD est le dernier reste NON NUL.**

*Exemple : Résolvons le problème de la mosaïque d'Alexandrie : $\text{PGCD}(420 ; 132)$.*

```
   Étape 1 :  420 = 132 × 3 + 24    (reste r₁ = 24 ≠ 0)
   Étape 2 :  132 =  24 × 5 + 12    (reste r₂ = 12 ≠ 0)
   Étape 3 :   24 =  12 × 2 +  0    (reste r₃ = 0)
```

Le reste est 0. Le dernier reste avant 0 est **12**.
Donc :
$$\text{PGCD}(420 ; 132) = \mathbf{12}.$$

Le maître mosaïste a sa réponse :
- Les plus grandes dalles possibles mesurent **$12\text{ cm} \times 12\text{ cm}$**.
- Sur la longueur, il posera $420 \div 12 = 35$ dalles.
- Sur la largeur, il posera $132 \div 12 = 11$ dalles.
- Au total, il posera $35 \times 11 = \mathbf{385\text{ dalles}}$, parfaitement ajustées sans couper aucun millimètre de marbre !

---

### 7. L'application reine : les fractions irréductibles

Tu as appris en classe de 5e à simplifier des fractions en divisant en haut et en bas par un même nombre. Mais souvent, on s'arrête trop tôt : on simplifie par 2, puis par 3, sans être certain d'avoir terminé.

> **📐 Définition — Fraction irréductible.**
> Une fraction $\dfrac{a}{b}$ est dite **irréductible** si son numérateur $a$ et son dénominateur $b$ sont **premiers entre eux**, c'est-à-dire si $\text{PGCD}(a ; b) = 1$. On ne peut plus la simplifier.

Grâce au PGCD, on peut rendre n'importe quelle fraction irréductible **en une seule étape** :

> **🧭 Méthode — Simplification maximale.**
> Pour rendre la fraction $\dfrac{a}{b}$ irréductible, il suffit de diviser le numérateur et le dénominateur par leur **PGCD** :
> $$\frac{a}{b} = \frac{a \div \text{PGCD}(a ; b)}{b \div \text{PGCD}(a ; b)}$$

*Exemple :* Rends irréductible la fraction $\dfrac{132}{420}$.
Nous venons de calculer que $\text{PGCD}(420 ; 132) = 12$.
$$\frac{132}{420} = \frac{132 \div 12}{420 \div 12} = \mathbf{\frac{11}{35}}.$$
Puisque 11 et 35 sont premiers entre eux, la fraction est garantie irréductible immédiatement !

---

### 8. Exemples résolus détaillés pas à pas

#### Exemple résolu 1 — Décomposition et diviseurs
1. Décompose l'entier $540$ en produit de facteurs premiers à l'aide de la potence.
2. Écris le résultat sous forme de puissances.
3. Le nombre 540 est-il divisible par 18 ? Par 24 ? Justifie sans poser de division.

*Solution rédigée :*
1. Potence de division :
   - $540 \div 2 = 270$
   - $270 \div 2 = 135$
   - $135 \div 3 = 45$ (car $1+3+5 = 9$)
   - $45 \div 3 = 15$
   - $15 \div 3 = 5$
   - $5 \div 5 = 1$
2. Donc : $540 = 2 \times 2 \times 3 \times 3 \times 3 \times 5 = \mathbf{2^2 \times 3^3 \times 5}$.
3. - Pour 18 : la décomposition de 18 est $18 = 2 \times 3^2$. Dans 540, on trouve bien au moins un facteur 2 (il y en a 2) et au moins deux facteurs 3 (il y en a 3). Donc **540 est bien divisible par 18**.
   - Pour 24 : la décomposition de 24 est $24 = 2^3 \times 3$. Or la décomposition de 540 ne contient que $2^2$ (seulement deux facteurs 2). Il manque un 2, donc **540 n'est pas divisible par 24**.

---

#### Exemple résolu 2 — Algorithme d'Euclide sur de grands nombres
Détermine le PGCD des nombres $1\,575$ et $420$ par l'algorithme d'Euclide.

*Solution rédigée :*
On applique les divisions euclidiennes successives :
- $1\,575 = 420 \times 3 + 315$  (le reste est $315 \neq 0$)
- $420 = 315 \times 1 + 105$    (le reste est $105 \neq 0$)
- $315 = 105 \times 3 + 0$      (le reste est $0$)

Le dernier reste non nul dans la suite des divisions est **105**.
Conclusion : $\mathbf{\text{PGCD}(1\,575 ; 420) = 105}$.

---

#### Exemple résolu 3 — Comparaison soustractions vs divisions
Calcule $\text{PGCD}(252 ; 105)$ :
1. Par l'algorithme des soustractions successives.
2. Par l'algorithme d'Euclide.

*Solution rédigée :*
1. **Soustractions successives :**
   - $252 - 105 = 147$
   - $147 - 105 = 42$
   - $105 - 42 = 63$
   - $63 - 42 = 21$
   - $42 - 21 = 21$
   - $21 - 21 = 0 \implies \mathbf{\text{PGCD} = 21}$. (5 soustractions)
2. **Algorithme d'Euclide :**
   - $252 = 105 \times 2 + 42$
   - $105 = 42 \times 2 + 21$
   - $42 = 21 \times 2 + 0 \implies \mathbf{\text{PGCD} = 21}$. (2 divisions)
On constate que l'algorithme d'Euclide est plus rapide et économique !

---

#### Exemple résolu 4 — Le problème de la kermesse
Pour la kermesse de l'école, les organisateurs disposent de 280 bracelets fluorescents et de 448 autocollants collectors.
Ils veulent préparer des sachets surprises tous identiques, contenant chacun le même nombre de bracelets et le même nombre d'autocollants, en utilisant tout le matériel.
1. Combien de sachets au maximum peuvent-ils préparer ?
2. Quelle sera alors la composition de chaque sachet ?

*Solution rédigée :*
1. Soit $N$ le nombre de sachets. Pour que tout soit utilisé sans reste et équitablement, $N$ doit être un diviseur de 280 et un diviseur de 448. Pour que le nombre de sachets soit maximal, $N$ doit être le **Plus Grand Commun Diviseur** de 448 et 280 : $N = \text{PGCD}(448 ; 280)$.
   Appliquons l'algorithme d'Euclide :
   - $448 = 280 \times 1 + 168$
   - $280 = 168 \times 1 + 112$
   - $168 = 112 \times 1 + 56$
   - $112 = 56 \times 2 + 0$
   Le dernier reste non nul est 56, donc $\text{PGCD}(448 ; 280) = 56$.
   On peut donc préparer au maximum **56 sachets identiques**.
2. Composition de chaque sachet :
   - Nombre de bracelets : $280 \div 56 = \mathbf{5\text{ bracelets}}$.
   - Nombre d'autocollants : $448 \div 56 = \mathbf{8\text{ autocollants}}$.

---

#### Exemple résolu 5 — Fraction irréductible et somme
On considère la fraction $A = \dfrac{1\,575}{420}$.
1. Rends la fraction $A$ irréductible.
2. Calcule la somme $S = \dfrac{1\,575}{420} + \dfrac{1}{4}$ sous la forme d'une fraction irréductible.

*Solution rédigée :*
1. D'après l'Exemple résolu 2, $\text{PGCD}(1\,575 ; 420) = 105$.
   On simplifie en divisant en haut et en bas par 105 :
   $$A = \frac{1\,575 \div 105}{420 \div 105} = \mathbf{\frac{15}{4}}.$$
2. Pour calculer la somme, on remplace la grande fraction par sa forme irréductible simplifiée :
   $$S = \frac{15}{4} + \frac{1}{4} = \frac{15 + 1}{4} = \frac{16}{4} = \mathbf{4}.$$
   Le calcul devient immédiat et d'une simplicité enfantine !

---

### Ce qu'il faut retenir

1. **Vocabulaire fondamental :**
   - $a = b \times k \iff a$ est un multiple de $b \iff b$ est un diviseur de $a$.
   - **Nombre premier** : exactement 2 diviseurs distincts (1 et lui-même). $0$ et $1$ ne sont PAS premiers. Le seul premier pair est $2$.

2. **Théorème fondamental de l'arithmétique :**
   - Tout entier supérieur ou égal à 2 se décompose de façon unique en produit de facteurs premiers ($N = p_1^{\alpha_1} \times p_2^{\alpha_2} \times \dots$).

3. **Le PGCD (Plus Grand Commun Diviseur) :**
   - C'est le plus grand entier qui divise simultanément les deux nombres.
   - Deux nombres sont **premiers entre eux** si leur $\text{PGCD} = 1$.
   - **Méthode par décomposition** : produit des facteurs premiers communs affectés du plus petit exposant.
   - **Algorithme d'Euclide** : on enchaîne les divisions euclidiennes $a = b \times q + r$. Le PGCD est le **dernier reste non nul**.

4. **Applications pratiques :**
   - **Fractions irréductibles** : diviser le numérateur et le dénominateur par leur PGCD.
   - **Découpages et lots** : le PGCD donne la dimension maximale des carreaux ou le nombre maximal de lots sans aucun reste.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 1.**
Parmi les nombres suivants, repère ceux qui sont des nombres premiers :
$$1 \quad ; \quad 2 \quad ; \quad 9 \quad ; \quad 13 \quad ; \quad 15 \quad ; \quad 21 \quad ; \quad 29 \quad ; \quad 31 \quad ; \quad 51 \quad ; \quad 91$$
Pour ceux qui ne le sont pas, justifie en donnant un diviseur autre que 1 et eux-mêmes.

**Exercice 2.**
En utilisant les critères de divisibilité, indique si le nombre $3\,420$ est divisible par 2, 3, 4, 5, 9 et 10. Justifie pour chaque critère.

**Exercice 3.**
Décompose en produit de facteurs premiers les nombres entiers suivants (en écrivant le résultat avec des puissances si nécessaire) :
a) $84$
b) $126$
c) $200$
d) $525$

**Exercice 4.**
À partir des décompositions $84 = 2^2 \times 3 \times 7$ et $126 = 2 \times 3^2 \times 7$ :
1. Quels sont les facteurs premiers communs à 84 et 126 ?
2. Calcule $\text{PGCD}(84 ; 126)$.
3. Rends la fraction $\dfrac{84}{126}$ irréductible.

**Exercice 5.**
Utilise l'algorithme des soustractions successives pour déterminer $\text{PGCD}(65 ; 39)$.

---

#### Niveau ★★ : Réflexion et situations concrètes

**Exercice 6 (Algorithme d'Euclide).**
1. À l'aide de l'algorithme d'Euclide, calcule $\text{PGCD}(756 ; 441)$ en présentant clairement chaque division euclidienne.
2. Les nombres 756 et 441 sont-ils premiers entre eux ? Pourquoi ?
3. Rends la fraction $\dfrac{441}{756}$ irréductible en une seule étape.

**Exercice 7 (Le carrelage de la terrasse).**
Un maçon doit poser du carrelage sur une terrasse rectangulaire mesurant 5,40 m de long sur 3,00 m de large.
Il veut utiliser des dalles carrées identiques les plus grandes possibles, sans aucune découpe.
1. Convertis les dimensions de la terrasse en centimètres.
2. Quelle doit être la longueur du côté d'une dalle ?
3. Combien de dalles le maçon devra-t-il poser en tout ?

**Exercice 8 (Le fleuriste équitable).**
Un fleuriste reçoit une livraison de 168 roses rouges et de 216 œillets blancs.
Il souhaite composer des bouquets tous identiques contenant chacun le même nombre de roses et le même nombre d'œillets, en utilisant toutes les fleurs.
1. Quel est le nombre maximal de bouquets qu'il peut réaliser ?
2. Combien de roses et combien d'œillets chaque bouquet comportera-t-il ?

**Exercice 9 (Le piège du faux nombre premier).**
Un élève affirme : *« Tous les nombres impairs supérieurs à 1 sont des nombres premiers, sauf s'ils se terminent par 5 ! »*
Montre que son affirmation est fausse en donnant au moins trois contre-exemples bien choisis parmi les nombres inférieurs à 100.

**Exercice 10 (La course sur circuit et les multiples).**
Deux pilotes de karting s'élancent en même temps sur une piste circulaire depuis la ligne de départ.
- Le premier pilote effectue un tour en 36 secondes.
- Le second pilote effectue un tour en 48 secondes.
1. Décompose 36 et 48 en produits de facteurs premiers.
2. Au bout de combien de temps les deux pilotes franchiront-ils à nouveau la ligne de départ ensemble pour la première fois ?
3. Combien de tours chacun aura-t-il alors parcourus ?

**Exercice 11 (Calculs avec fractions irréductibles).**
On donne l'expression suivante :
$$B = \frac{588}{882} - \frac{1}{6}$$
1. Calcule $\text{PGCD}(882 ; 588)$ par l'algorithme d'Euclide.
2. Déduis-en la forme irréductible de la fraction $\dfrac{588}{882}$.
3. Calcule alors l'expression $B$ et donne le résultat sous la forme d'une fraction irréductible.

---

#### Niveau ★★★ : Défis et approfondissements

**Exercice 12 (Les clôtures et les piquets du fermier).**
Un agriculteur possède un champ triangulaire dont les trois côtés mesurent 120 mètres, 144 mètres et 168 mètres.
Il souhaite planter des piquets de clôture tout autour de son champ, à intervalles réguliers et constants, avec un piquet obligatoirement planté à chaque sommet du triangle.
Pour faire des économies, il souhaite utiliser **le moins de piquets possible**.
1. Quelle doit être la distance entre deux piquets consécutifs ?
2. Combien de piquets devra-t-il planter au total le long de la clôture ?

**Exercice 13 (La preuve du roi Euclide : l'infinité des nombres premiers).**
Euclide a démontré que l'ensemble des nombres premiers est infini par un raisonnement par l'absurde remarquable.
Supposons qu'il n'y ait qu'un nombre fini de nombres premiers : notons-les tous $p_1, p_2, p_3, \dots, p_n$.
Considérons le nombre gigantesque $N$ obtenu en multipliant tous ces nombres premiers entre eux et en ajoutant 1 :
$$N = (p_1 \times p_2 \times p_3 \times \dots \times p_n) + 1$$
1. Si l'on divise $N$ par l'un quelconque des nombres premiers $p_1, p_2, \dots, p_n$, quel est le reste de la division euclidienne ?
2. Le nombre $N$ peut-il être divisible par l'un de ces nombres premiers ?
3. Conclus : pourquoi est-ce contradictoire, et pourquoi les nombres premiers sont-ils obligatoirement en nombre infini ?

**Exercice 14 (Le secret des engrenages).**
Une roue dentée $A$ de 54 dents entraîne une roue dentée $B$ de 42 dents. Deux dents particulières, une sur chaque roue, sont en contact au point de départ.
1. Calcule $\text{PGCD}(54 ; 42)$.
2. Après combien de dents engrenées ces deux mêmes dents se retrouveront-elles en contact pour la première fois ?
3. Combien de tours complets chaque roue aura-t-elle alors accomplis ?

**Exercice 15 (Le pavage de cubes dans un parallélépipède 3D).**
Un sculpteur dispose d'un bloc de marbre rectangulaire plein de 90 cm de longueur, 75 cm de largeur et 60 cm de hauteur.
Il veut découper ce bloc en petits cubes identiques, les plus grands possibles, sans perdre aucun morceau de marbre.
1. Décompose 90, 75 et 60 en produits de facteurs premiers.
2. Quel est le Plus Grand Commun Diviseur de ces trois nombres ?
3. Quelle sera l'arête de chaque petit cube ?
4. Combien de petits cubes le sculpteur obtiendra-t-il au total ?

---

### Solutions

#### Solutions des exercices ★

- **Exercice 1 :**
  - Nombres premiers : **2, 13, 29, 31**.
  - Non premiers :
    - 1 n'est pas premier (un seul diviseur).
    - 9 est divisible par 3 ($9 = 3 \times 3$).
    - 15 est divisible par 3 et 5 ($15 = 3 \times 5$).
    - 21 est divisible par 3 et 7 ($21 = 3 \times 7$).
    - 51 est divisible par 3 ($5 + 1 = 6$ ; $51 = 3 \times 17$).
    - 91 est divisible par 7 ($91 = 7 \times 13$).
- **Exercice 2 :** Pour 3 420 :
  - Par 2 : oui, il se termine par 0 (pair).
  - Par 3 : oui, $3+4+2+0 = 9$, multiple de 3.
  - Par 4 : oui, 20 est divisible par 4.
  - Par 5 : oui, se termine par 0.
  - Par 9 : oui, $3+4+2+0 = 9$, multiple de 9.
  - Par 10 : oui, se termine par 0.
- **Exercice 3 :**
  a) $84 = 2^2 \times 3 \times 7$.
  b) $126 = 2 \times 3^2 \times 7$.
  c) $200 = 2^3 \times 5^2$.
  d) $525 = 3 \times 5^2 \times 7$.
- **Exercice 4 :**
  1. Facteurs premiers communs : 2, 3 et 7.
  2. $\text{PGCD}(84 ; 126) = 2^1 \times 3^1 \times 7^1 = \mathbf{42}$.
  3. $\dfrac{84}{126} = \dfrac{84 \div 42}{126 \div 42} = \mathbf{\dfrac{2}{3}}$.
- **Exercice 5 :** Soustractions successives : $65 - 39 = 26 \implies 39 - 26 = 13 \implies 26 - 13 = 13 \implies 13 - 13 = 0$. Donc $\text{PGCD}(65 ; 39) = \mathbf{13}$.

---

#### Solutions détaillées des exercices ★★

- **Exercice 6 (Algorithme d'Euclide) :**
  1. Divisions successives :
     - $756 = 441 \times 1 + 315$
     - $441 = 315 \times 1 + 126$
     - $315 = 126 \times 2 + 63$
     - $126 = 63 \times 2 + 0$
     Le dernier reste non nul est 63, donc $\mathbf{\text{PGCD}(756 ; 441) = 63}$.
  2. Ils ne sont pas premiers entre eux car leur PGCD est $63 \neq 1$.
  3. Fraction irréductible : $\dfrac{441}{756} = \dfrac{441 \div 63}{756 \div 63} = \mathbf{\dfrac{7}{12}}$.

- **Exercice 7 (Le carrelage de la terrasse) :**
  1. Dimensions : $L = 5{,}40\text{ m} = 540\text{ cm}$, $\ell = 3{,}00\text{ m} = 300\text{ cm}$.
  2. La longueur du côté d'une dalle doit être un diviseur commun à 540 et 300, et le plus grand possible : c'est $\text{PGCD}(540 ; 300)$.
     Par Euclide :
     - $540 = 300 \times 1 + 240$
     - $300 = 240 \times 1 + 60$
     - $240 = 60 \times 4 + 0$
     Le PGCD est 60. Les dalles doivent mesurer **$60\text{ cm} \times 60\text{ cm}$**.
  3. Nombre de dalles :
     - Longueur : $540 \div 60 = 9$ dalles.
     - Largeur : $300 \div 60 = 5$ dalles.
     - Total : $9 \times 5 = \mathbf{45\text{ dalles}}$.

- **Exercice 8 (Le fleuriste) :**
  1. Le nombre maximal de bouquets est $\text{PGCD}(216 ; 168)$.
     - $216 = 168 \times 1 + 48$
     - $168 = 48 \times 3 + 24$
     - $48 = 24 \times 2 + 0$
     $\text{PGCD}(216 ; 168) = 24$. Il peut faire au maximum **24 bouquets**.
  2. Composition :
     - Roses : $168 \div 24 = \mathbf{7\text{ roses rouges}}$.
     - Œillets : $216 \div 24 = \mathbf{9\text{ œillets blancs}}$.

- **Exercice 9 (Le faux nombre premier) :**
  Trois contre-exemples parmi les nombres impairs ne se terminant pas par 5 :
  - $9$ ($9 = 3 \times 3$, impair, non premier) ;
  - $21$ ($21 = 3 \times 7$) ;
  - $27$ ($27 = 3 \times 9$) ;
  - $91$ ($91 = 7 \times 13$, piège très célèbre !).

- **Exercice 10 (La course sur circuit) :**
  1. $36 = 2^2 \times 3^2$ et $48 = 2^4 \times 3$.
  2. Le premier pilote passe sur la ligne aux temps multiples de 36 (36, 72, 108, 144...). Le second aux temps multiples de 48 (48, 96, 144...).
     Le premier moment commun est le Plus Petit Commun Multiple (PPCM), obtenu en prenant tous les facteurs premiers avec leur plus grand exposant :
     $$\text{PPCM}(36 ; 48) = 2^4 \times 3^2 = 16 \times 9 = \mathbf{144\text{ secondes}} = 2\text{ minutes et } 24\text{ secondes}.$$
  3. Nombre de tours :
     - Pilote 1 : $144 \div 36 = \mathbf{4\text{ tours}}$.
     - Pilote 2 : $144 \div 48 = \mathbf{3\text{ tours}}$.

- **Exercice 11 (Calcul avec fraction irréductible) :**
  1. Algorithme d'Euclide pour 882 et 588 :
     - $882 = 588 \times 1 + 294$
     - $588 = 294 \times 2 + 0 \implies \text{PGCD}(882 ; 588) = \mathbf{294}$.
  2. Forme irréductible : $\dfrac{588}{882} = \dfrac{588 \div 294}{882 \div 294} = \mathbf{\dfrac{2}{3}}$.
  3. Calcul de $B$ :
     $$B = \frac{2}{3} - \frac{1}{6} = \frac{4}{6} - \frac{1}{6} = \frac{3}{6} = \mathbf{\frac{1}{2}}.$$

---

#### Solutions détaillées des exercices ★★★

- **Exercice 12 (Les piquets de clôture) :**
  1. Pour que l'espacement $d$ soit constant et qu'il y ait un piquet à chaque sommet, $d$ doit diviser les trois côtés 120, 144 et 168. Pour avoir le moins de piquets possible, $d$ doit être le plus grand possible : c'est le PGCD des trois nombres.
     - $\text{PGCD}(120 ; 144)$ : $144 = 120 \times 1 + 24$, et $120 = 24 \times 5 + 0 \implies 24$.
     - Testons si 24 divise 168 : $168 = 24 \times 7 + 0$.
     Donc le PGCD des trois nombres est **24 mètres**. Les piquets seront espacés de 24 m.
  2. Le périmètre du champ est $120 + 144 + 168 = 432\text{ mètres}$.
     Puisque la clôture est un circuit fermé, le nombre total de piquets est :
     $$\frac{432}{24} = \mathbf{18\text{ piquets}}.$$

- **Exercice 13 (La preuve d'Euclide) :**
  1. Par définition, $N = (p_1 \times p_2 \times \dots \times p_n) + 1$. Le produit est un multiple exact de n'importe quel $p_k$. Donc la division de $N$ par $p_k$ donne un quotient entier et un reste égal à **1**.
  2. Comme le reste est 1 (et non 0), $N$ n'est divisible par **aucun** des nombres premiers de la liste.
  3. Or, d'après le théorème fondamental de l'arithmétique, $N$ (qui est plus grand que 1) possède au moins un diviseur premier. Ce diviseur premier ne fait donc pas partie de la liste $p_1, \dots, p_n$. Cela contredit l'hypothèse de départ que la liste contenait *tous* les nombres premiers. L'hypothèse était donc fausse : il existe obligatoirement une **infinité de nombres premiers**.

- **Exercice 14 (Les engrenages) :**
  1. Euclide : $54 = 42 \times 1 + 12 \implies 42 = 12 \times 3 + 6 \implies 12 = 6 \times 2 + 0$. Donc $\text{PGCD}(54 ; 42) = \mathbf{6}$.
  2. Le contact initial se reproduit après un nombre de passages de dents multiple de 54 et de 42, c'est-à-dire au PPCM :
     $$\text{PPCM}(54 ; 42) = \frac{54 \times 42}{\text{PGCD}(54 ; 42)} = \frac{2268}{6} = \mathbf{378\text{ dents engrenées}}.$$
  3. Nombre de tours :
     - Roue A : $378 \div 54 = \mathbf{7\text{ tours complets}}$.
     - Roue B : $378 \div 42 = \mathbf{9\text{ tours complets}}$.

- **Exercice 15 (Cubes 3D) :**
  1. Décompositions :
     - $90 = 2 \times 3^2 \times 5$
     - $75 = 3 \times 5^2$
     - $60 = 2^2 \times 3 \times 5$
  2. Facteurs communs aux trois nombres : 3 (exposant 1) et 5 (exposant 1).
     $\text{PGCD}(90 ; 75 ; 60) = 3 \times 5 = \mathbf{15}$.
  3. L'arête maximale de chaque petit cube est de **$15\text{ cm}$**.
  4. Nombre de cubes :
     - En longueur : $90 \div 15 = 6$
     - En largeur : $75 \div 15 = 5$
     - En hauteur : $60 \div 15 = 4$
     Total : $6 \times 5 \times 4 = \mathbf{120\text{ cubes}}$.

---

### La question qui ouvre la suite

Avec l'arithmétique d'Euclide, tout est réglé avec une précision absolue : chaque brique trouve sa place, chaque part tombe pile, chaque division est certaine.
Mais notre monde réel n'est pas fait que de coffres scellés et de dalles taillées au millimètre.

Que se passe-t-il lorsque la brume de l'avenir se lève, lorsqu'on jette un dé sur le tapis d'une auberge, ou lorsqu'un chef caravanier doit choisir entre deux routes incertaines ? Peut-on calculer rationnellement quand on ne sait pas ce qui va arriver ?
Rendez-vous au cœur du désert et dans les salons du XVIIe siècle : nous allons apprendre à dompter la **roulette du destin**.
