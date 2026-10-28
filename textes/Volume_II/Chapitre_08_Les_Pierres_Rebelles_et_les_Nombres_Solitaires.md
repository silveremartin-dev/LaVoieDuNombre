# VOLUME II — L'ÂGE DU MARCHÉ ET DES PARTAGES (8 - 10 ans / CE2 - CM1)
## CHAPITRE 8 : Les Pierres Rebelles et les Nombres Solitaires

> *« Il y a des nombres qui acceptent docilement d'être pliés, rangés en bataillons et découpés en rectangles. Et il y a les nombres rebelles, sauvages, qui refusent de plier et se dressent comme des pierres solitaires dans le désert. Ces pierres sauvages sont les atomes de tous les nombres. »*

---

### Ce que tu vas découvrir

- Ce que sont les **multiples** d'un nombre (les nombres sur lesquels on tombe en sautant toujours de la même longueur).
- Ce que sont les **diviseurs** d'un nombre (les longueurs de rangées qui tombent juste).
- Des **astuces de détective** pour savoir, sans faire de division, si un nombre se partage par 2, 3, 5, 9 ou 10.
- Les **nombres premiers**, ces nombres qui refusent de former des rectangles, et pourquoi ils sont les briques de tous les autres nombres.
- Le **crible d'Ératosthène**, une machine à trier les nombres inventée il y a plus de 2 000 ans.

---

### 1. Le problème : la parade des gardes du marché

Tu as maintenant huit ans. Le campement de tentes s'est transformé en une petite cité au bord du fleuve. Chaque matin, des marchands arrivent des oasis lointaines avec des chameaux chargés d'épices, de poteries et d'étoffes de laine.

Pour que personne ne vole sur les étals, le gouverneur a recruté une petite troupe de gardes. Aujourd'hui, c'est la grande fête des moissons : les gardes doivent défiler sur la grand-place.

Le capitaine a sous ses ordres **12 soldats**. Il crie :
*« En formation rectangulaire ! Je veux des rangs parfaits, sans un seul soldat qui dépasse ! »*

Les 12 soldats obéissent avec le sourire :

- ils se rangent en **2 lignes de 6** : $2 \times 6 = 12$ ;
- puis en **3 lignes de 4** : $3 \times 4 = 12$ ;
- et pour passer la porte étroite de la ville, en **1 file de 12** : $1 \times 12 = 12$.

```
   Formation 2 × 6 :              Formation 3 × 4 :
   o o o o o o                    o o o o
   o o o o o o                    o o o o
                                  o o o o
```

Tout le monde applaudit : 12 est un nombre **docile**. Il adore former des rectangles.

Mais soudain, un messager arrive au galop : un des soldats doit partir porter une lettre au roi. Il reste **11 soldats**. Le capitaine siffle :
*« Reformez un rectangle ! »*

- Par rangs de 2 : cinq devant, cinq derrière… et le onzième se retrouve **tout seul** au bout !
- Par rangs de 3 : trois lignes de trois font 9… et **2 soldats** restent plantés là.
- Par rangs de 4 : $4 + 4 = 8$, il en reste **3** dehors.
- Par rangs de 5 : $5 + 5 = 10$, il en reste **1**.

```
   o o o o o
   o o o o o  o   <--- le soldat qui dépasse !
```

Le capitaine transpire sous son casque. Il a beau essayer : **avec 11 soldats, aucun rectangle n'est possible**, sauf la longue file de 1 sur 11.

Ce n'est la faute ni des soldats ni du capitaine. C'est le nombre 11 lui-même qui **refuse** de se casser. Pourquoi certains nombres sont-ils si souples, et d'autres si têtus ? Pour le comprendre, nous allons apprendre deux mots très importants : **multiple** et **diviseur**.

> **🖐️ À toi de jouer —** Prends 12 objets (boutons, haricots, pièces). Fabrique tous les rectangles possibles. Puis enlève un objet et recommence avec 11. Ressens dans tes doigts la différence !

---

### 2. Les multiples : sauter toujours de la même longueur

Imagine une grenouille sur une longue ligne graduée. Elle part de 0 et fait toujours des sauts de **3 cases**.

```
  0     3     6     9     12    15    18    21
  |--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|
  ^        ^        ^        ^        ^        ^        ^        ^
  départ   1 saut   2 sauts  3 sauts  4 sauts  ...
```

Les cases où elle pose ses pattes sont : $0, 3, 6, 9, 12, 15, 18, 21, \dots$
Ce sont exactement les résultats de la **table de 3** : $3 \times 0$, $3 \times 1$, $3 \times 2$, $3 \times 3$…

> **📐 Définition — Multiple**
> Un nombre est un **multiple de 3** s'il est dans la table de 3, c'est-à-dire s'il s'écrit $3 \times$ (un nombre entier).
> Plus généralement, un nombre est un **multiple de $b$** s'il s'écrit $b \times$ (un nombre entier).

Les trois petits points « $\dots$ » qu'on écrit à la fin d'une liste se lisent « **et ainsi de suite** ». Ils veulent dire : la liste continue toujours de la même façon, **sans jamais s'arrêter**. Car la grenouille peut sauter aussi longtemps qu'elle veut : il y a une **infinité** de multiples de 3 !

> **Exemple résolu 1 — Est-ce un multiple ?**
> *Question :* 42 est-il un multiple de 6 ? Et 45 ?
> *Je cherche dans la table de 6 :* $6 \times 7 = 42$. Oui, 42 est un multiple de 6.
> *Pour 45 :* $6 \times 7 = 42$ et $6 \times 8 = 48$. 45 est **entre** les deux, il n'est pas dans la table. 45 n'est **pas** un multiple de 6. (La grenouille de 6 saute par-dessus 45 sans s'y poser.)

> **Exemple résolu 2 — Les multiples communs**
> *Question :* Quels nombres sont à la fois multiples de 4 et de 6, jusqu'à 40 ?
> Multiples de 4 : 0, 4, 8, **12**, 16, 20, **24**, 28, 32, **36**, 40.
> Multiples de 6 : 0, 6, **12**, 18, **24**, 30, **36**.
> Les nombres présents dans les deux listes : **0, 12, 24, 36**. Deux grenouilles, l'une sautant de 4 en 4, l'autre de 6 en 6, se retrouvent sur ces cases-là !

---

### 3. Les diviseurs : les rangées qui tombent juste

Retournons voir les soldats. Avec 12 soldats, on a pu faire des rangées de 1, 2, 3, 4, 6 et 12 (car $4 \times 3$ et $6 \times 2$ marchent aussi, en tournant le rectangle). Avec 11, seulement des rangées de 1 et de 11.

> **📐 Définition — Diviseur**
> Un nombre $b$ est un **diviseur** de $a$ si l'on peut ranger $a$ objets en rangées de $b$ **sans qu'il en reste un seul**.
> Autrement dit : $a$ est dans la table de $b$.
> On dit aussi : « **$a$ est divisible par $b$** » ou « **$b$ divise $a$** ».

Tu remarques que les deux mots vont ensemble, comme les deux faces d'une même pièce :

$$12 = 3 \times 4 \quad \Longrightarrow \quad \begin{cases} 12 \text{ est un multiple de } 3 \\ 3 \text{ est un diviseur de } 12 \end{cases}$$

La grosse flèche « $\Longrightarrow$ » se lit « **donc** ».

> **💡 Le savais-tu ?** Plus tard, au collège et au lycée, les mathématiciens écriront « $3 \mid 12$ » (une petite barre verticale) pour dire « 3 divise 12 ». Ne confonds pas avec la barre de fraction, qui est couchée !

#### La méthode des paires pour trouver TOUS les diviseurs

Chaque rectangle donne **deux** diviseurs à la fois : sa largeur et sa longueur. Pour ne rien oublier, on cherche les paires dans l'ordre, en commençant par 1.

> **Exemple résolu 3 — Tous les diviseurs de 24**
> - $1 \times 24 = 24$ → diviseurs 1 et 24
> - $2 \times 12 = 24$ → diviseurs 2 et 12
> - $3 \times 8 = 24$ → diviseurs 3 et 8
> - 4 ? $4 \times 6 = 24$ → diviseurs 4 et 6
> - 5 ? $5 \times 4 = 20$, $5 \times 5 = 25$ : non.
> - 6 ? Déjà trouvé avec 4 ! Les paires recommencent à l'envers : **on peut s'arrêter**.
>
> Les diviseurs de 24 sont : **1, 2, 3, 4, 6, 8, 12, 24**. Il y en a 8, donc 4 rectangles différents.

```
     1 ───────────────────────── 24
        2 ─────────────── 12
            3 ─────── 8
               4 ─ 6          <- les paires se rejoignent au milieu
```

> **Exemple résolu 4 — Les diviseurs de 36 (un nombre carré)**
> $1 \times 36$, $2 \times 18$, $3 \times 12$, $4 \times 9$, $6 \times 6$.
> Diviseurs : **1, 2, 3, 4, 6, 9, 12, 18, 36**. Il y en a 9 : un nombre **impair** de diviseurs ! Pourquoi ? Parce que le rectangle $6 \times 6$ est un **carré** : le 6 est à la fois la largeur et la longueur, on ne le compte qu'une fois.

> **⚠️ Attention, piège ! — Les cas bizarres**
> - **1 est un diviseur de tous les nombres** : on peut toujours faire une seule file ($1 \times 12$, $1 \times 11$…).
> - **Tout nombre est un diviseur de lui-même** et un multiple de lui-même : $12 = 12 \times 1$.
> - **0 est un multiple de tous les nombres** : $0 = 3 \times 0 = 7 \times 0$. La grenouille, avant de sauter, est déjà sur 0 !
> - **On ne divise jamais par 0** : ranger 12 soldats en rangées de 0 soldat ? On pourrait faire des rangées vides pendant mille ans sans jamais placer personne. Cela n'a aucun sens.
> - Ne mélange pas les mots : « 3 est un **diviseur** de 12 » mais « 12 est un **multiple** de 3 ». Le **petit** divise, le **grand** est multiple.

---

### 4. Les astuces du détective : les critères de divisibilité

Au marché, un marchand a 3 471 dattes. Peut-il en faire des sachets de 3 sans qu'il en reste ? Faire la division serait long. Heureusement, les mathématiciens ont trouvé des **critères** : des petits indices qui permettent de répondre en un clin d'œil.

#### Les critères du dernier chiffre : 2, 5 et 10

Rappelle-toi : un nombre comme 3 471, c'est des milliers, des centaines, des dizaines et des unités. Or **une dizaine (10) se range toujours parfaitement par 2, par 5 et par 10** : $10 = 2 \times 5 = 5 \times 2 = 10 \times 1$. Et une centaine, un millier, ce ne sont que des paquets de dizaines ! Donc, tout ce qui est « dizaines et plus » tombe juste. **Seules les unités peuvent poser problème.** C'est pour ça qu'il suffit de regarder le **dernier chiffre**.

> **📐 Critères de divisibilité par 2, 5 et 10**
> - Un nombre est divisible par **2** si son chiffre des unités est **0, 2, 4, 6 ou 8**. On dit qu'il est **pair**. Sinon il est **impair**.
> - Un nombre est divisible par **5** si son chiffre des unités est **0 ou 5**.
> - Un nombre est divisible par **10** si son chiffre des unités est **0**.

> **Exemple résolu 5 — Le dernier chiffre parle**
> - 3 476 : se termine par 6 → divisible par 2 ; pas par 5 ; pas par 10.
> - 985 : se termine par 5 → divisible par 5 ; impair, donc pas par 2 ; pas par 10.
> - 7 230 : se termine par 0 → divisible par 2, par 5 **et** par 10.

#### Les critères magiques de la somme des chiffres : 3 et 9

Pour 3 et 9, regarder le dernier chiffre ne marche pas du tout ! (13 finit par 3, mais $13 = 3 \times 4 + 1$ n'est pas divisible par 3.) Il faut une astuce plus fine.

Regarde bien :
$$10 = 9 + 1 \qquad 100 = 99 + 1 \qquad 1\,000 = 999 + 1$$

Or $9$, $99$, $999$ se rangent parfaitement par paquets de 9 (et donc aussi par paquets de 3, puisque $9 = 3 \times 3$). Chaque dizaine, chaque centaine, chaque millier laisse donc **exactement 1 objet qui dépasse**.

Prenons 234 : c'est 2 centaines, 3 dizaines et 4 unités.
- Les 2 centaines laissent dépasser **2** objets (1 chacune).
- Les 3 dizaines laissent dépasser **3** objets.
- Les 4 unités sont **4** objets.

En tout, ce qui dépasse, c'est $2 + 3 + 4 = 9$ objets : **la somme des chiffres** ! Et 9 se range parfaitement par 9 et par 3. Donc 234 est divisible par 9 et par 3. (Vérifie : $234 = 9 \times 26$.)

> **📐 Critères de divisibilité par 3 et 9**
> - Un nombre est divisible par **3** si la **somme de ses chiffres** est un multiple de 3.
> - Un nombre est divisible par **9** si la **somme de ses chiffres** est un multiple de 9.

> **Exemple résolu 6 — Les dattes du marchand**
> 3 471 : $3 + 4 + 7 + 1 = 15$. 15 est dans la table de 3 ($3 \times 5$), donc **3 471 est divisible par 3** : le marchand peut faire ses sachets ! ($3\,471 = 3 \times 1\,157$.)
> Mais 15 n'est pas dans la table de 9 : 3 471 n'est **pas** divisible par 9.

> **Exemple résolu 7 — Quand la somme est encore grosse**
> 98 769 : $9 + 8 + 7 + 6 + 9 = 39$. Est-ce un multiple de 3 ? On recommence le truc : $3 + 9 = 12$, et $12 = 3 \times 4$. Oui ! Donc 98 769 est divisible par 3. Par 9 ? $39$ n'est pas dans la table de 9 ($9 \times 4 = 36$, $9 \times 5 = 45$) : non.

> **⚠️ Attention, piège !**
> - Pour 3 et 9, **on ne regarde pas le dernier chiffre** : 23 finit par 3 mais n'est pas divisible par 3 ($2 + 3 = 5$). 27 finit par 7 et il est divisible par 3 ($2 + 7 = 9$).
> - **Divisible par 9 ⟹ divisible par 3**, car $9 = 3 \times 3$. Mais **l'inverse est faux** : 12 est divisible par 3, pas par 9.
> - **Divisible par 2 et par 5 ⟹ divisible par 10** (le dernier chiffre doit être pair ET être 0 ou 5 : c'est forcément 0).
> - Un nombre **impair** n'est jamais divisible par 10, ni par 4, ni par 6 (car tous ces nombres sont pairs).

> **🖐️ À toi de jouer — Le jeu du détective**
> Un joueur annonce un grand nombre. L'autre doit dire le plus vite possible par quels nombres parmi 2, 3, 5, 9 et 10 il est divisible. Chaque bonne réponse rapporte un point ; une erreur en fait perdre un.

---

### 5. Les nombres premiers : les atomes des nombres

Revenons à notre soldat têtu. Le nombre 11 n'a que **deux** diviseurs : 1 et 11. Il ne forme aucun vrai rectangle.

> **📐 Définition — Nombre premier**
> Un **nombre premier** est un nombre entier qui a **exactement deux diviseurs** : 1 et lui-même.
> Un nombre (plus grand que 1) qui a plus de deux diviseurs est dit **composé** : on peut le « composer » en rectangle.

Le mot « premier » vient du latin *primus* : « le premier, celui qui vient avant tout ». Ce sont les nombres qui existent **avant** les autres, puisque tous les autres sont fabriqués avec eux, comme tu vas le voir.

Faisons l'inventaire des premiers nombres :

| Nombre | Rectangles possibles | Diviseurs | Premier ? |
|:---:|:---|:---|:---:|
| 1 | 1 × 1 | 1 | **Non** (un seul diviseur) |
| 2 | 1 × 2 | 1, 2 | Oui |
| 3 | 1 × 3 | 1, 3 | Oui |
| 4 | 1 × 4, 2 × 2 | 1, 2, 4 | Non |
| 5 | 1 × 5 | 1, 5 | Oui |
| 6 | 1 × 6, 2 × 3 | 1, 2, 3, 6 | Non |
| 7 | 1 × 7 | 1, 7 | Oui |
| 8 | 1 × 8, 2 × 4 | 1, 2, 4, 8 | Non |
| 9 | 1 × 9, 3 × 3 | 1, 3, 9 | Non |
| 10 | 1 × 10, 2 × 5 | 1, 2, 5, 10 | Non |
| 11 | 1 × 11 | 1, 11 | Oui |

> **⚠️ Attention, piège ! — Le cas de 1 et de 2**
> - **1 n'est pas premier.** Il n'a qu'**un seul** diviseur (lui-même), et la définition en demande exactement deux. Les mathématiciens l'ont exclu exprès : tu verras bientôt que sinon, la belle règle « chaque nombre se casse d'une seule façon en nombres premiers » ne marcherait plus (on pourrait ajouter autant de « × 1 » qu'on veut).
> - **2 est le seul nombre premier pair.** Tous les autres nombres pairs sont divisibles par 2, donc ils ont au moins trois diviseurs : 1, 2 et eux-mêmes.
> - **Impair ne veut pas dire premier !** 9, 15, 21, 25, 27 sont impairs… et composés ($9 = 3 \times 3$, $15 = 3 \times 5$, $21 = 3 \times 7$…). Méfie-toi surtout de **51** ($= 3 \times 17$) et de **91** ($= 7 \times 13$) : ils ont l'air premiers, mais ce sont des imposteurs !

#### Casser un nombre jusqu'aux atomes : l'arbre des facteurs

Prends n'importe quel nombre composé, par exemple **60**. Casse-le en deux morceaux multipliés, puis recasse chaque morceau tant que c'est possible :

```
              60
            /    \
           6      10
          / \    /  \
         2   3  2    5        <- on ne peut plus casser : ce sont des premiers !
```

$$60 = 2 \times 2 \times 3 \times 5$$

Les nombres qu'on multiplie s'appellent des **facteurs**. Ici, tous les facteurs sont premiers : on dit qu'on a **décomposé 60 en produit de facteurs premiers**.

> **Exemple résolu 8 — Un autre chemin pour 60**
> Et si on avait commencé par $60 = 4 \times 15$ ?
> $4 = 2 \times 2$ et $15 = 3 \times 5$. On trouve encore $60 = 2 \times 2 \times 3 \times 5$ !
> Quel que soit le chemin, **on arrive toujours aux mêmes atomes** (seul l'ordre peut changer). C'est une loi très profonde des nombres, que le Grec **Euclide** connaissait déjà et que tu démontreras au lycée.

C'est pour cela qu'on dit que les nombres premiers sont **les atomes des nombres** : comme toutes les choses sont faites d'atomes, **tous les nombres entiers plus grands que 1 sont faits de nombres premiers multipliés entre eux**.

