# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 30 : La Roulette du Destin et la Survie du Chasseur

> *« L'ignorant accuse le mauvais sort, consulte les devins ou tremble devant l'orage quand le danger approche. Le mathématicien regarde les sentiers de l'avenir, calcule la fraction de chance, et prend la décision qui sauve sa caravane. Le hasard n'est pas un monstre aveugle : c'est un arbre dont on peut compter les branches. »*

---

### Ce que tu vas découvrir

- Comment transformer la brume de l'incertitude en un **nombre précis entre 0 et 1** (la probabilité).
- Le vocabulaire officiel qui structure le hasard : **expérience aléatoire**, **issue**, **événement**, **événement certain, impossible et contraire**.
- Pourquoi la formule $P(E) = \dfrac{\text{nombre de cas favorables}}{\text{nombre de cas possibles}}$ ne marche qu'en cas d'**équiprobabilité**, et le piège monumental des deux dés.
- Comment explorer le futur à deux étapes grâce à l'**arbre de probabilités** et au **tableau à double entrée**.
- La différence cruciale entre un tirage **avec remise** et un tirage **sans remise**.
- Comment le hasard réel obéit à la loi des grands nombres : la **stabilisation des fréquences** et la simulation sur ordinateur.

---

### 1. Le problème : la caravane et la forêt des deux sentiers

Le crépuscule tombe sur la route de la soie. Une caravane de dix chameaux chargés de balles d'épices précieuses et de soieries s'arrête à l'orée d'une immense forêt sombre et brumeuse.
Pour atteindre l'oasis où se tient le grand marché annuel, le chef caravanier doit choisir entre deux routes :

```
                                  ┌─── Sentier des Marais (A) ───┐
                                  │    1 caravane sur 10 perdue   │
         Départ de la caravane ───┤                               ├─── Oasis de Jade
                                  │    Sentier des Gorges (B)     │
                                  └─── 4 caravanes sur 10 perdues ─┘
```

* **Le Sentier des Marais (Chemin A) :**
  C'est un chemin plat, facile pour les pattes des bêtes. Mais la région est couverte de fondrières de boue traîtresses. Les registres des marchands indiquent que sur 100 caravanes ayant emprunté ce chemin cette année, **10 se sont enlisées et ont tout perdu**, tandis que 90 sont arrivées saines et sauves.
* **Le Sentier des Gorges (Chemin B) :**
  C'est un défilé rocheux escarpé, deux fois plus court et plus rapide. Mais des brigands armés rôdent dans les cavernes : sur 100 caravanes, **40 ont été pillées**, et 60 ont réussi à franchir le défilé indemnes.

Le jeune chamelier s'écrie :
*« Prenons le chemin des gorges ! Nous arriverons demain à l'aube pour vendre au meilleur prix ! Avec un peu de chance, les brigands dormiront ! »*

Le vieux chef secoue la tête :
*« La chance n'est pas une prière qu'on lance au ciel. La chance est une fraction de matière. Celui qui ne sait pas peser le risque marche les yeux fermés vers le précipice ! »*

Pour la première fois dans l'histoire des mathématiques, nous n'allons plus seulement mesurer ce qui est sous nos yeux (une longueur, un poids, un nombre de carreaux), mais **ce qui n'est pas encore arrivé** !
Nous entrons dans le royaume des **Probabilités**.

---

### 2. Le vocabulaire officiel des probabilités

Pour parler du hasard avec la rigueur d'un géomètre, les mathématiciens ont forgé un vocabulaire très précis. Chaque mot a une définition stricte qu'il faut maîtriser.

#### 2.1 Expérience aléatoire et issue
> **📐 Définition — Expérience aléatoire.**
> Une expérience est dite **aléatoire** si :
> 1. On connaît à l'avance tous les résultats possibles ;
> 2. Le résultat final dépend uniquement du hasard et est **impossible à prévoir avec certitude**.

*Exemples :*
- Lancer une pièce de monnaie équilibrée et observer la face supérieure est une expérience aléatoire.
- Lâcher une pomme pour voir si elle tombe vers le sol n'est **pas** une expérience aléatoire (la gravité garantit qu'elle tombera toujours).

> **📐 Définition — Issue.**
> Une **issue** (ou événement élémentaire) est l'un des résultats possibles d'une expérience aléatoire. L'ensemble de toutes les issues s'appelle l'**univers** (souvent noté avec la lettre grecque $\Omega$, « oméga »).

*Exemple du dé à 6 faces :* Les issues possibles sont 1, 2, 3, 4, 5 et 6. L'univers est $\{1, 2, 3, 4, 5, 6\}$.

#### 2.2 Événements : impossible, certain, contraire
> **📐 Définition — Événement.**
> Un **événement** est un ensemble constitué de zéro, une ou plusieurs issues. On dit qu'un événement est **réalisé** si l'issue obtenue lors de l'expérience fait partie de cet événement.

Prenons le lancer d'un dé cubique ordinaire :
- L'événement $A$ : « Obtenir un nombre pair » est constitué des issues $\{2, 4, 6\}$. Si le dé tombe sur 4, l'événement $A$ est réalisé.
- **Événement impossible :** un événement qui ne contient aucune issue et ne peut jamais se produire. Sa probabilité est égale à **0**.
  *Exemple :* « Obtenir un 7 » avec un dé à 6 faces.
- **Événement certain :** un événement qui contient toutes les issues possibles et se produit toujours. Sa probabilité est égale à **1** (ou $100\,\%$) !
  *Exemple :* « Obtenir un nombre inférieur ou égal à 6 ».
- **Événement contraire :** l'événement contraire d'un événement $A$, noté **$\bar{A}$** (se lit **« A barre »** ou « non $A$ »), est l'événement qui est réalisé **exactement quand $A$ n'est pas réalisé**.

```
                   ┌───────────────────────────────────┐
                   │ Univers complet Ω (Totalité = 1)  │
                   │  ┌───────────────┐                │
                   │  │ Événement A   │  Contraire Ā   │
                   │  │ (Succès)      │  (Échecs)      │
                   │  └───────────────┘                │
                   └───────────────────────────────────┘
```

> **📐 Propriété capitale de l'événement contraire —**
> Pour tout événement $A$ :
> $$P(\bar{A}) = 1 - P(A) \qquad\text{ou encore}\qquad P(A) + P(\bar{A}) = 1$$

*Exemple :* Si la probabilité qu'il pleuve demain est $P(\text{Pluie}) = 0{,}3$ (soit $30\,\%$), alors la probabilité qu'il ne pleuve pas est :
$$P(\text{Pas de pluie}) = 1 - 0{,}3 = 0{,}7 \quad (\text{soit } 70\,\%).$$

---

### 3. Calculer une probabilité en situation d'équiprobabilité

#### 3.1 Qu'est-ce que l'équiprobabilité ?

On dit qu'une situation est d'**équiprobabilité** lorsque **toutes les issues possibles ont exactement la même chance d'apparaître**.
Dans les exercices, cette situation est signalée par des expressions clés :
- « Un dé cubique **équilibré** » (ou « non pipé ») ;
- « Une pièce de monnaie **parfaitement équilibrée** » ;
- « Des boules **indiscernables au toucher** » dans une urne ;
- « On tire une carte **au hasard** dans un jeu bien mélangé ».

#### 3.2 La formule reine

> **📐 Règle de Laplace — Probabilité sous équiprobabilité.**
> Dans une situation d'équiprobabilité, la probabilité d'un événement $E$ est égale au quotient du nombre d'issues favorables par le nombre total d'issues possibles :
> $$P(E) = \frac{\text{Nombre d'issues favorables à } E}{\text{Nombre total d'issues possibles}}$$

#### 3.3 Les trois visages d'une probabilité
Une probabilité est un nombre toujours compris entre 0 et 1 :
$$0 \le P(E) \le 1$$
On peut l'écrire sous trois formes équivalentes :
1. En **fraction** (valeur exacte) : $\dfrac{1}{4}$
2. En **nombre décimal** : $0{,}25$
3. En **pourcentage** : $25\,\%$

> **⚠️ Attention, piège !** Une probabilité ne peut **JAMAIS** être négative, ni supérieure à 1 (ou $100\,\%$) ! Si tu trouves $P = 1{,}25$ ou $P = -0{,}3$, ton calcul comporte obligatoirement une erreur. De plus, la somme des probabilités de toutes les issues élémentaires vaut **toujours 1**.

Revenons à notre caravane :
- Pour le Sentier des Marais : $P(\text{Péril}) = \dfrac{10}{100} = \dfrac{1}{10} = 0{,}10 = \mathbf{10\,\%}$.
- Pour le Sentier des Gorges : $P(\text{Péril}) = \dfrac{40}{100} = \dfrac{4}{10} = 0{,}40 = \mathbf{40\,\%}$.
Le risque dans les gorges est **quatre fois supérieur** ! Le chef sage choisit le marais, et la caravane arrive intacte.

---

### 4. Expériences à deux épreuves : Arbres et Tableaux

Quand une expérience aléatoire se déroule en plusieurs étapes successives (par exemple : lancer deux pièces de suite, lancer deux dés, ou tirer deux billes dans un sac), il devient difficile de deviner toutes les issues de tête. Deux outils graphiques permettent d'y voir clair.

#### 4.1 L'outil n°1 : Le tableau à double entrée (l'exemple roi des deux dés)

Si l'on lance deux dés à 6 faces et que l'on fait la somme des deux chiffres, combien y a-t-il de résultats possibles ?
Les sommes vont de $1+1 = 2$ jusqu'à $6+6 = 12$. Il y a donc 11 sommes différentes possibles.
Certains élèves pensent alors : *« La probabilité d'obtenir 7 est de 1 sur 11 ! »*
**C'est une erreur colossale !** Car toutes les sommes ne sont pas équiprobables !

Dressons le tableau de toutes les combinaisons possibles ($6 \times 6 = \mathbf{36\text{ cases équiprobables}}$) :

| Dé 1 \ Dé 2 | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 2 | 3 | 4 | 5 | 6 | **[7]** |
| **2** | 3 | 4 | 5 | 6 | **[7]** | 8 |
| **3** | 4 | 5 | 6 | **[7]** | 8 | 9 |
| **4** | 5 | 6 | **[7]** | 8 | 9 | 10 |
| **5** | 6 | **[7]** | 8 | 9 | 10 | 11 |
| **6** | **[7]** | 8 | 9 | 10 | 11 | 12 |

Regarde la grande diagonale des **7** :
- Pour obtenir la somme **2**, il n'y a qu'une seule case : $(1 ; 1) \implies P(2) = \dfrac{1}{36}$.
- Pour obtenir la somme **12**, une seule case : $(6 ; 6) \implies P(12) = \dfrac{1}{36}$.
- Mais pour obtenir la somme **7**, il y a **6 cases différentes** : $(1;6), (2;5), (3;4), (4;3), (5;2), (6;1)$ !
$$P(\text{Somme} = 7) = \frac{6}{36} = \frac{1}{6} \approx \mathbf{16{,}7\,\%}$$
La somme 7 est **six fois plus fréquente** que la somme 2 ! C'est la reine des dés.

```
       Distribution des sommes de deux dés :
       Probabilité
          ▲
     6/36 ┤                     ██ (7)
     5/36 ┤                  ██ ██ ██ (6, 7, 8)
     4/36 ┤               ██ ██ ██ ██ ██
     3/36 ┤            ██ ██ ██ ██ ██ ██ ██
     2/36 ┤         ██ ██ ██ ██ ██ ██ ██ ██ ██
     1/36 ┤      ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██
          └──────┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──►
                 2  3  4  5  6  7  8  9 10 11 12   Somme
```

#### 4.2 L'outil n°2 : L'arbre pondéré de probabilités

L'arbre est le couteau suisse des probabilités. Chaque embranchement représente une épreuve.

> **📐 Les trois lois sacrées de l'arbre de probabilités —**
> 1. **La somme des probabilités** portées sur les branches issues d'un même nœud est **toujours égale à 1**.
> 2. **Le long d'un chemin**, on **multiplie** les probabilités pour trouver la probabilité de l'issue finale (principe multiplicatif).
> 3. **La probabilité d'un événement** composé de plusieurs chemins est la **somme** des probabilités de ces chemins.

```
                        1re épreuve              2e épreuve            Chemin complet
                                          1/2
                                     ┌────────── Pile  ===> (Pile ; Pile) : 1/2 × 1/2 = 1/4
                                 1/2 │
                       ┌─────────────┤    1/2
                       │    Pile     └────────── Face  ===> (Pile ; Face) : 1/2 × 1/2 = 1/4
                       │
       Départ ─────────┤
                       │    Face     ┌────────── Pile  ===> (Face ; Pile) : 1/2 × 1/2 = 1/4
                       └─────────────┤    1/2
                                 1/2 │
                                     └────────── Face  ===> (Face ; Face) : 1/2 × 1/2 = 1/4
                                          1/2
```

---

### 5. Tirages avec remise et tirages sans remise

C'est l'un des points les plus cruciaux du programme de 3e.
Imagine une boîte contenant **3 boules rouges (R)** et **2 boules vertes (V)** (soit 5 boules au total).
On tire successivement deux boules.

#### Cas 1 : Tirage AVEC remise
Après avoir noté la couleur de la première boule, on la **remet dans la boîte** et on mélange avant le deuxième tirage.
- Au premier tirage : $P(R) = \dfrac{3}{5}$ et $P(V) = \dfrac{2}{5}$.
- Au deuxième tirage : la boîte est redevenue **strictement identique** !
  Les probabilités ne changent pas : $P(R) = \dfrac{3}{5}$ et $P(V) = \dfrac{2}{5}$.
- La probabilité d'obtenir deux rouges $(R ; R)$ est :
  $$P(R ; R) = \frac{3}{5} \times \frac{3}{5} = \frac{9}{25} = 0{,}36 = \mathbf{36\,\%}.$$

#### Cas 2 : Tirage SANS remise
Après le premier tirage, on garde la boule en main : **on ne la remet pas** !
- Au premier tirage : $P(R) = \dfrac{3}{5}$.
- Pour le second tirage, il ne reste plus que **4 boules au total** dans la boîte !
  - Si la première boule était rouge, il ne reste plus que 2 boules rouges sur 4 : $P(\text{2e } R) = \dfrac{2}{4}$.
  - La probabilité d'obtenir deux rouges $(R ; R)$ est :
    $$P(R ; R) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10} = 0{,}30 = \mathbf{30\,\%}.$$

> **⚠️ Attention, piège !** Dans un tirage sans remise, **le dénominateur diminue de 1** au second tour, et le numérateur de la couleur tirée diminue aussi de 1 !

---

### 6. Du hasard théorique au monde réel : la loi des grands nombres

Quand tu lances une pièce équilibrée, la probabilité théorique d'avoir Pile est de $p = 0{,}5$.
Est-ce que cela signifie que si tu lances la pièce 10 fois, tu obtiendras **exactement** 5 Piles et 5 Faces ?
Non ! Tu pourrais très bien obtenir 7 Piles et 3 Faces (soit une fréquence de $70\,\%$ de Piles).

Mais que se passe-t-il si tu lances la pièce 100 fois, 1 000 fois, 100 000 fois ?
Calculons la **fréquence observée** :
$$f = \frac{\text{Nombre de Piles observés}}{\text{Nombre total de lancers } N}$$

> **📐 Phénomène de stabilisation des fréquences (Loi des grands nombres) —**
> Lorsque l'on répète une expérience aléatoire un **très grand nombre de fois**, la fréquence observée d'un événement se rapproche et se stabilise autour de sa **probabilité théorique**.

```
   Fréquence f
      ▲
  1,0 ┼──o
      │   \
  0,7 ┼────o
      │     \
  0,5 ┼──────\───o──────o───o──────────────── Probabilité théorique = 0,5
      │       \ / \    / \ / \
  0,3 ┼────────o   \  /   o   \
      │             o          \
  0,0 ┴──┼──────┼───────┼───────┼─────────────►
         10    100    1 000   10 000   Nombre de lancers N
```

C'est ce principe qui permet aux compagnies d'assurance d'évaluer le prix de leurs contrats, aux météorologues de prévoir les tempêtes et aux casinos d'être certains de ne jamais perdre d'argent sur l'ensemble de l'année !

> **🔍 L'histoire vraie — Les lettres de Pascal et Fermat (1654)**
> En 1654, un joueur parisien, le **Chevalier de Méré**, soumet à **Blaise Pascal** une énigme qui enflammait les tavernes : « le problème des partis ». Deux joueurs jouent à pile ou face pour une cagnotte de 64 pièces d'or. Le premier à 3 victoires gagne tout. Mais la partie est brutalement interrompue par un incendie alors que le joueur A mène 2 à 1 ! Comment partager la bourse en toute justice ?
> Pascal échange des lettres avec le génial magistrat de Toulouse, **Pierre de Fermat**. Au lieu de regarder le passé, ils dessinent l'arbre de tous les avenirs possibles : sur les 4 fins de partie possibles, le joueur A en gagnait 3, et le joueur B seulement 1. La justice divine exigeait donc de donner $\frac{3}{4}$ du magot au joueur A (48 pièces) et $\frac{1}{4}$ au joueur B (16 pièces). Les probabilités modernes étaient nées !

---

### 7. Exemples résolus détaillés pas à pas

#### Exemple résolu 1 — Tirage dans un jeu de cartes (Équiprobabilité et événement contraire)
On tire au hasard une carte dans un jeu bien mélangé de 32 cartes (qui contient 4 couleurs : Cœur, Carreau, Trèfle, Pique, avec 8 cartes par couleur : 7, 8, 9, 10, Valet, Dame, Roi, As).
1. Quelle est la probabilité de tirer un As ?
2. Quelle est la probabilité de tirer une carte rouge (Cœur ou Carreau) ?
3. Quelle est la probabilité de tirer une carte qui n'est **pas** un Trèfle ?

*Solution rédigée :*
Puisque le jeu est bien mélangé, il y a équiprobabilité entre les 32 cartes.
1. Le jeu contient 4 As (un de chaque couleur).
   $$P(\text{As}) = \frac{4}{32} = \frac{1}{8} = \mathbf{0{,}125} \quad (12{,}5\,\%).$$
2. Il y a 8 cœurs et 8 carreaux, soit $8 + 8 = 16$ cartes rouges sur 32.
   $$P(\text{Rouge}) = \frac{16}{32} = \frac{1}{2} = \mathbf{0{,}5} \quad (50\,\%).$$
3. *Méthode par l'événement contraire :*
   L'événement $T$ est « Tirer un Trèfle ». Il y a 8 trèfles, donc $P(T) = \frac{8}{32} = \frac{1}{4}$.
   L'événement « Ne pas tirer un Trèfle » est l'événement contraire $\bar{T}$ :
   $$P(\bar{T}) = 1 - P(T) = 1 - \frac{1}{4} = \mathbf{\frac{3}{4}} = \mathbf{0{,}75} \quad (75\,\%).$$

---

#### Exemple résolu 2 — Expérience à deux épreuves successives (Le trousseau de clés)
Un trousseau comporte 4 clés en apparence identiques, mais **une seule** ouvre la porte du garage.
Un automobiliste étourdi essaie les clés au hasard, dans le noir. Dès qu'une clé ne marche pas, il l'écarte pour ne pas la retester (tirage sans remise).
Quelle est la probabilité qu'il ouvre la porte au deuxième essai exactement ?

*Solution rédigée :*
Pour ouvrir au deuxième essai, il faut impérativement deux événements consécutifs :
- Échec au 1er essai ($E_1$) ;
- Réussite au 2e essai ($R_2$).

Construisons les branches correspondantes :
1. Au 1er essai : il y a 3 mauvaises clés sur 4 clés au total :
   $$P(E_1) = \frac{3}{4}$$
2. Au 2e essai : la mauvaise clé a été écartée. Il ne reste plus que 3 clés au total, dont 1 seule bonne clé :
   $$P(R_2 \text{ sachant } E_1) = \frac{1}{3}$$
3. D'après la règle de multiplication le long d'un chemin :
   $$P(\text{Succès au 2e essai}) = P(E_1) \times P(R_2) = \frac{3}{4} \times \frac{1}{3} = \frac{3}{12} = \mathbf{\frac{1}{4}} = \mathbf{0{,}25}.$$
Chaque essai a rigoureusement $\frac{1}{4}$ de chance de succès !

---

#### Exemple résolu 3 — Tirage de billes avec et sans remise
Un sac contient 2 billes bleues et 3 billes jaunes. On tire au hasard deux billes successivement.
Quelle est la probabilité de tirer **deux billes de couleurs différentes** :
1. Dans le cas d'un tirage **avec remise** ?
2. Dans le cas d'un tirage **sans remise** ?

*Solution rédigée :*
Tirer deux billes de couleurs différentes correspond à deux chemins possibles : $(B ; J)$ ou $(J ; B)$.
1. **Cas avec remise :**
   - $P(B ; J) = \frac{2}{5} \times \frac{3}{5} = \frac{6}{25}$.
   - $P(J ; B) = \frac{3}{5} \times \frac{2}{5} = \frac{6}{25}$.
   On additionne les deux chemins disjoints :
   $$P(\text{Couleurs différentes}) = \frac{6}{25} + \frac{6}{25} = \frac{12}{25} = \mathbf{0{,}48} \quad (48\,\%).$$

2. **Cas sans remise :**
   - Pour $(B ; J)$ : première bleue ($2/5$), puis au deuxième tour il reste 4 billes dont 3 jaunes ($3/4$) :
     $$P(B ; J) = \frac{2}{5} \times \frac{3}{4} = \frac{6}{20} = \frac{3}{10}.$$
   - Pour $(J ; B)$ : première jaune ($3/5$), puis il reste 4 billes dont 2 bleues ($2/4$) :
     $$P(J ; B) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}.$$
   On additionne les deux chemins :
   $$P(\text{Couleurs différentes}) = \frac{3}{10} + \frac{3}{10} = \frac{6}{10} = \mathbf{0{,}60} \quad (60\,\%).$$
*Remarque : la probabilité change considérablement selon qu'il y a remise ou non !*

---

#### Exemple résolu 4 — L'astuce magique du « Au moins un »
On lance trois fois de suite une pièce équilibrée.
Quelle est la probabilité d'obtenir **au moins une fois Pile** ?

*Solution rédigée :*
« Obtenir au moins une fois Pile » signifie obtenir 1 Pile, 2 Piles ou 3 Piles. Calculer tous ces cas serait long.
Regardons l'**événement contraire** :
Le contraire de « avoir au moins un Pile » est **« n'avoir AUCUN Pile »**, c'est-à-dire obtenir trois Faces consécutives $(F ; F ; F)$.
- La probabilité d'avoir Face à un lancer est $\frac{1}{2}$.
- Les trois lancers étant indépendants :
  $$P(\text{Aucun Pile}) = P(F ; F ; F) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}.$$
- Par la formule de l'événement contraire :
  $$P(\text{Au moins un Pile}) = 1 - P(\text{Aucun Pile}) = 1 - \frac{1}{8} = \mathbf{\frac{7}{8}} = \mathbf{0{,}875} \quad (87{,}5\,\%).$$
En passant par le contraire, le calcul a pris une seule ligne !

---

#### Exemple résolu 5 — Dé à deux couleurs et jeu d'argent
Un jeu de fête foraine propose de lancer un dé spécial à 6 faces : 4 faces sont peintes en Vert et 2 faces sont peintes en Rouge.
Pour jouer, on paie 2 euros.
- Si le dé tombe sur Rouge, on gagne 5 euros (soit un bénéfice net de $+3$ €).
- Si le dé tombe sur Vert, on ne gagne rien (soit une perte nette de $-2$ €).
Le forain affirme : *« Venez tenter votre chance, vous pouvez gagner plus que votre mise ! »*
Le jeu est-il favorable au joueur ?

*Solution rédigée :*
Calculons les probabilités de gain :
- $P(\text{Rouge}) = \frac{2}{6} = \frac{1}{3} \approx 33{,}3\,\%$.
- $P(\text{Vert}) = \frac{4}{6} = \frac{2}{3} \approx 66{,}7\,\%$.

Imaginons que l'on joue 300 parties :
- On va tomber environ $300 \times \frac{1}{3} = 100$ fois sur Rouge, rapportant $100 \times (+3\text{ €}) = +300\text{ €}$.
- On va tomber environ $300 \times \frac{2}{3} = 200$ fois sur Vert, coûtant $200 \times (-2\text{ €}) = -400\text{ €}$.
Bilan pour 300 parties : $300 - 400 = -100$ euros !
En moyenne par partie, le joueur perd environ $\dfrac{-100}{300} \approx -0{,}33$ euro.
**Le jeu est défavorable au joueur** (et très avantageux pour le forain).

---

### Ce qu'il faut retenir

1. **Vocabulaire :**
   - **Expérience aléatoire** : résultat dû au hasard, non prévisible.
   - **Issues** : résultats possibles élémentaires.
   - **Événement impossible** ($P = 0$) ; **Événement certain** ($P = 1$).
   - **Événement contraire $\bar{A}$** : $P(\bar{A}) = 1 - P(A)$. Formule magique pour « au moins un » : $P(\text{au moins un}) = 1 - P(\text{aucun})$.

2. **Équiprobabilité :**
   $$P(E) = \frac{\text{Nombre de cas favorables}}{\text{Nombre de cas possibles}}$$
   Toujours vérifier : $0 \le P(E) \le 1$. La somme des probabilités de toutes les issues vaut $1$.

3. **Expériences à deux étapes :**
   - **Tableau à double entrée** : parfait pour 2 dés, 2 roulettes simples (nombre de cases = produit des issues).
   - **Arbre de probabilités** :
     - Somme des branches issues d'un même nœud = 1.
     - On **multiplie** les probabilités le long d'un chemin.
     - On **additionne** les probabilités des chemins qui réalisent l'événement.
   - **Avec remise** : probabilités constantes.
   - **Sans remise** : l'effectif diminue de 1 à chaque tirage.

4. **Loi des grands nombres :**
   - La **fréquence** observée lors d'un grand nombre d'expériences se rapproche et se stabilise autour de la **probabilité théorique**.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 1.**
Une urne opaque contient 4 boules rouges, 3 boules vertes et 5 boules bleues, indiscernables au toucher. On tire une boule au hasard.
1. Combien y a-t-il d'issues possibles ? Sont-elles équiprobables ?
2. Calcule la probabilité de tirer une boule rouge sous forme de fraction irréductible.
3. Calcule la probabilité de tirer une boule qui n'est pas verte.

**Exercice 2.**
On lance un dé cubique équilibré à 6 faces numérotées de 1 à 6. Calcule la probabilité des événements suivants :
- $A$ : « Obtenir un nombre impair ».
- $B$ : « Obtenir un multiple de 3 ».
- $C$ : « Obtenir un nombre strictement supérieur à 4 ».
- $D$ : « Obtenir un nombre premier ».

**Exercice 3.**
On fait tourner une roue de loterie partagée en 8 secteurs égaux : 3 secteurs sont peints en bleu, 4 en jaune et 1 en rouge.
1. Quelle est la probabilité de tomber sur le rouge ?
2. Quelle est la probabilité de ne pas tomber sur le bleu ?
3. Exprime ces probabilités en pourcentage.

**Exercice 4.**
On lance une pièce équilibrée deux fois de suite.
1. Dresse l'arbre des possibles avec les probabilités sur chaque branche.
2. Quelle est la probabilité d'obtenir deux fois Face ?
3. Quelle est la probabilité d'obtenir exactement une fois Pile et une fois Face ?

**Exercice 5.**
Dans un collège, $55\,\%$ des élèves sont demi-pensionnaires et les autres sont externes. On choisit un élève au hasard.
Quelle est la probabilité que cet élève soit externe ?

---

#### Niveau ★★ : Réflexion et situations combinées

**Exercice 6 (Le lancer de deux dés et le produit).**
On lance deux dés équilibrés à 6 faces et on **multiplie** les deux chiffres obtenus.
1. À l'aide d'un tableau à double entrée de taille $6 \times 6$, détermine toutes les issues possibles du produit.
2. Quelle est la probabilité que le produit soit égal à 12 ?
3. Quelle est la probabilité que le produit soit un nombre pair ?

**Exercice 7 (Chaussettes dans le tiroir dans le noir).**
Dans un tiroir se trouvent en vrac 6 chaussettes noires et 4 chaussettes bleues, totalement indiscernables au toucher.
Le matin, avant le lever du jour, Lucas tire au hasard et successivement deux chaussettes **sans les remettre**.
1. Construis l'arbre pondéré représentant cette expérience aléatoire.
2. Quelle est la probabilité que Lucas tire deux chaussettes noires ?
3. Quelle est la probabilité que Lucas tire deux chaussettes de la même couleur (pour être bien assorti) ?

**Exercice 8 (Le mot « PROBABILITÉ »).**
On écrit chacune des 11 lettres du mot « P R O B A B I L I T É » sur un carton identique, et on place les 11 cartons dans un sac. On tire un carton au hasard.
1. Quelle est la probabilité de tirer la lettre « B » ?
2. Quelle est la probabilité de tirer une voyelle (O, A, I, É) ?
3. Quelle est la probabilité de tirer une consonne ?

**Exercice 9 (Contrôle qualité en usine).**
Une usine fabrique des composants électroniques. Sur une chaîne de production, $3\,\%$ des composants présentent un défaut de soudure et sont défectueux.
Un technicien prélève au hasard deux composants successifs (on assimile ce tirage à un tirage avec remise en raison du très grand nombre de pièces produites).
1. Quelle est la probabilité que les deux composants soient défectueux ?
2. Quelle est la probabilité qu'aucun des deux composants ne soit défectueux ?
3. Quelle est la probabilité qu'au moins l'un des deux composants présente un défaut ?

**Exercice 10 (Le piège du joueur de casino).**
Un joueur est à la table de roulette. La bille s'est arrêtée sur une case Noire lors des 6 derniers tours consécutifs.
Le joueur s'écrie : *« Le Rouge n'est pas sorti depuis 6 tours, il a maintenant une chance énorme de sortir, je mise tout sur le Rouge ! »*
1. Que penses-tu du raisonnement de ce joueur ?
2. Quelle est la probabilité réelle que la bille tombe sur le Rouge au 7e tour (sur une roulette européenne avec 18 cases rouges, 18 cases noires et 1 case verte zéro) ?

**Exercice 11 (La cible de tir à l'arc).**
Une cible carrée de 40 cm de côté contient en son centre un disque rouge de 10 cm de rayon.
Un archer débutant tire une flèche qui atteint à coup sûr la cible, mais en un point totalement aléatoire (probabilité proportionnelle à l'aire).
1. Calcule l'aire totale de la cible carrée.
2. Calcule l'aire exacte du disque rouge central.
3. Quelle est la probabilité que la flèche se plante dans le disque rouge ? (Arrondir au centième).

---

#### Niveau ★★★ : Défis et approfondissements

**Exercice 12 (Le problème historique du Chevalier de Méré).**
Le Chevalier de Méré avait remarqué au XVIIe siècle qu'il gagnait souvent en pariant sur l'apparition d'au moins un 6 en lançant 4 fois de suite un dé à 6 faces.
1. Quelle est la probabilité de NE PAS obtenir de 6 lors d'un lancer de dé ?
2. Quelle est la probabilité de n'obtenir aucun 6 en 4 lancers indépendants ?
3. Déduis-en la probabilité d'obtenir au moins un 6 en 4 lancers. Le Chevalier avait-il raison de parier sur cet événement ?

**Exercice 13 (La simulation informatique des grands nombres).**
Un programme Python simule 10 000 lancers d'un dé cubique équilibré.
Voici le script utilisé :
```python
import random

lancers = 10000
faces_six = 0

for i in range(lancers):
  de = random.randint(1, 6)
  if de == 6:
    faces_six += 1

frequence = faces_six / lancers
print("Fréquence de 6 :", frequence)
```
1. Quelle est la probabilité théorique d'obtenir la face 6 lors d'un lancer ? Donne sa valeur sous forme de fraction puis de nombre décimal arrondi à 0,001.
2. Quelle valeur approximative affichera le programme pour `frequence` ?
3. Pourquoi la valeur affichée ne sera-t-elle généralement pas exactement égale à $1/6$ ? Quel nom donne-t-on à ce phénomène ?

**Exercice 14 (Le paradoxe des anniversaires dans la classe).**
Dans une classe de 3e de 25 élèves, le professeur affirme : *« Il y a plus d'une chance sur deux que deux élèves de cette classe soient nés le même jour de l'année ! »* (On suppose l'année non bissextile de 365 jours, et toutes les dates de naissance équiprobables).
Pour vérifier son affirmation, on étudie l'événement contraire : « Tous les 25 élèves ont des dates de naissance toutes différentes ».
1. Le premier élève a sa date de naissance n'importe quel jour (probabilité $365/365$). Quelle est la probabilité que le second élève soit né un jour différent du premier ?
2. Quelle est la probabilité que le 3e élève soit né un jour différent des deux premiers ?
3. Le produit des 25 probabilités donne environ $0{,}43$. Calcule alors la probabilité qu'au moins deux élèves fêtent leur anniversaire le même jour. Le professeur avait-il raison ?

**Exercice 15 (Le problème des partis revisité : Pascal et Fermat).**
Deux joueurs $A$ et $B$ misent chacun 50 pistoles dans une cagnotte (total : 100 pistoles). Le premier qui gagne 3 manches remporte tout.
Le score actuel est de 2 à 0 en faveur du joueur $A$. La partie est brutalement interrompue.
1. Au maximum, combien de manches supplémentaires auraient été nécessaires pour achever la partie ?
2. Trace l'arbre des manches restantes en supposant chaque manche équiprobable ($P = 1/2$).
3. Quelle est la probabilité que le joueur $B$ réussisse à remonter et à gagner la partie ?
4. Comment les 100 pistoles doivent-elles être équitablement réparties entre $A$ et $B$ ?

---

### Solutions

#### Solutions des exercices ★

- **Exercice 1 :** 
  1. Nombre total d'issues : $4 + 3 + 5 = 12$ boules. Comme elles sont indiscernables au toucher, elles sont équiprobables.
  2. $P(\text{Rouge}) = \frac{4}{12} = \mathbf{\frac{1}{3}}$.
  3. Il y a $4 + 5 = 9$ boules non vertes, ou $1 - \frac{3}{12} = \frac{9}{12} = \mathbf{\frac{3}{4}}$.
- **Exercice 2 :** 
  - $P(A) = \frac{3}{6} = \mathbf{\frac{1}{2}}$ (issues : 1, 3, 5).
  - $P(B) = \frac{2}{6} = \mathbf{\frac{1}{3}}$ (issues : 3, 6).
  - $P(C) = \frac{2}{6} = \mathbf{\frac{1}{3}}$ (issues : 5, 6).
  - $P(D) = \frac{3}{6} = \mathbf{\frac{1}{2}}$ (issues premières : 2, 3, 5 ; attention : 1 n'est pas premier !).
- **Exercice 3 :** 
  1. $P(\text{Rouge}) = \frac{1}{8} = \mathbf{0{,}125} = \mathbf{12{,}5\,\%}$.
  2. $P(\text{Non bleu}) = 1 - \frac{3}{8} = \frac{5}{8} = \mathbf{0{,}625} = \mathbf{62{,}5\,\%}$.
- **Exercice 4 :** 
  1. L'arbre a 4 branches terminales : $(P;P), (P;F), (F;P), (F;F)$, chacune avec probabilité $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
  2. $P(F ; F) = \mathbf{\frac{1}{4}} = 0{,}25$.
  3. Chemins favorables : $(P;F)$ et $(F;P) \implies \frac{1}{4} + \frac{1}{4} = \mathbf{\frac{1}{2}} = 0{,}5$.
- **Exercice 5 :** $P(\text{Externe}) = 1 - 0{,}55 = \mathbf{0{,}45} = \mathbf{45\,\%}$.

---

#### Solutions détaillées des exercices ★★

- **Exercice 6 (Produit de deux dés) :**
  1. Tableau des produits ($6 \times 6 = 36$ cases) :
     - Ligne 1 : 1, 2, 3, 4, 5, 6
     - Ligne 2 : 2, 4, 6, 8, 10, 12
     - Ligne 3 : 3, 6, 9, 12, 15, 18
     - Ligne 4 : 4, 8, 12, 16, 20, 24
     - Ligne 5 : 5, 10, 15, 20, 25, 30
     - Ligne 6 : 6, 12, 18, 24, 30, 36
  2. Les cases donnant 12 sont : $(2;6), (3;4), (4;3), (6;2)$, soit 4 cases.
     $$P(\text{Produit} = 12) = \frac{4}{36} = \mathbf{\frac{1}{9}} \approx 0{,}111.$$
  3. Le produit est impair seulement si les DEUX dés sont impairs (3 choix $\times$ 3 choix = 9 cases).
     Toutes les autres cases sont paires : $36 - 9 = 27$ cases paires.
     $$P(\text{Produit pair}) = \frac{27}{36} = \mathbf{\frac{3}{4}} = \mathbf{0{,}75}.$$

- **Exercice 7 (Chaussettes sans remise) :**
  Total de départ : $6 + 4 = 10$ chaussettes.
  1. Arbre :
     - 1er tirage : Noire ($6/10$), Bleue ($4/10$).
     - 2e tirage après Noire : Noire ($5/9$), Bleue ($4/9$).
     - 2e tirage après Bleue : Noire ($6/9$), Bleue ($3/9$).
  2. Deux noires : $P(N ; N) = \frac{6}{10} \times \frac{5}{9} = \frac{30}{90} = \mathbf{\frac{1}{3}} \approx 0{,}333$.
  3. Même couleur : deux noires ou deux bleues.
     $P(B ; B) = \frac{4}{10} \times \frac{3}{9} = \frac{12}{90}$.
     $$P(\text{Même couleur}) = \frac{30}{90} + \frac{12}{90} = \frac{42}{90} = \mathbf{\frac{7}{15}} \approx \mathbf{0{,}467} \quad (46{,}7\,\%).$$

- **Exercice 8 (Le mot PROBABILITÉ) :**
  Le mot compte 11 lettres : P (1), R (1), O (1), B (2), A (1), I (2), L (1), T (1), É (1).
  1. $P(\text{B}) = \mathbf{\frac{2}{11}}$.
  2. Voyelles : O, A, I, I, É $\implies 5$ voyelles. $P(\text{Voyelle}) = \mathbf{\frac{5}{11}}$.
  3. Consonnes : événement contraire $\implies 1 - \frac{5}{11} = \mathbf{\frac{6}{11}}$.

- **Exercice 9 (Contrôle qualité) :**
  Soit $D$ l'événement « pièce défectueuse », $P(D) = 0{,}03$, et $P(\bar{D}) = 0{,}97$.
  1. Deux défectueux : $P(D ; D) = 0{,}03 \times 0{,}03 = \mathbf{0{,}0009}$ (soit $0{,}09\,\%$, moins d'un sur mille).
  2. Aucun défectueux : $P(\bar{D} ; \bar{D}) = 0{,}97 \times 0{,}97 = \mathbf{0{,}9409} \approx \mathbf{94{,}1\,\%}$.
  3. Au moins un défectueux : contraire d'aucun défectueux :
     $$P = 1 - 0{,}9409 = \mathbf{0{,}0591} \approx \mathbf{5{,}91\,\%}.$$

- **Exercice 10 (Le piège du joueur) :**
  1. Le raisonnement du joueur est une **illusion classique** (appelée « sophisme du joueur »). La roulette n'a pas de mémoire : chaque tour est totalement indépendant des tours précédents. Les boules d'avant n'influencent aucunement la bille actuelle.
  2. Sur une roulette européenne de 37 cases (18 rouges, 18 noires, 1 zéro vert) :
     $$P(\text{Rouge}) = \frac{18}{37} \approx \mathbf{0{,}4865} \quad (48{,}65\,\%).$$
     La probabilité est rigoureusement la même qu'au premier tour !

- **Exercice 11 (La cible de tir à l'arc) :**
  1. Aire de la cible carrée : $\mathcal{A}_{\text{carré}} = 40 \times 40 = \mathbf{1\,600\text{ cm}^2}$.
  2. Aire du disque rouge : $\mathcal{A}_{\text{disque}} = \pi \times R^2 = \pi \times 10^2 = \mathbf{100\pi\text{ cm}^2} \approx 314{,}16\text{ cm}^2$.
  3. Probabilité :
     $$P = \frac{\mathcal{A}_{\text{disque}}}{\mathcal{A}_{\text{carré}}} = \frac{100\pi}{1\,600} = \frac{\pi}{16} \approx \mathbf{0{,}20} \quad (20\,\%).$$

---

#### Solutions détaillées des exercices ★★★

- **Exercice 12 (Le Chevalier de Méré) :**
  1. Probabilité de ne pas faire 6 : $P(\text{non 6}) = \frac{5}{6}$.
  2. Lors de 4 lancers indépendants, probabilité de n'obtenir aucun 6 :
     $$P(\text{aucun 6}) = \left(\frac{5}{6}\right)^4 = \frac{625}{1\,296} \approx 0{,}4823.$$
  3. Probabilité d'avoir au moins un 6 :
     $$P(\text{au moins un 6}) = 1 - 0{,}4823 = \mathbf{0{,}5177} \approx \mathbf{51{,}8\,\%}.$$
     Puisque $51{,}8\,\% > 50\,\%$, la probabilité est strictement supérieure à la moitié : le Chevalier de Méré avait raison, sur le long terme il était gagnant !

- **Exercice 13 (Simulation Python) :**
  1. La probabilité théorique est $p = \frac{1}{6} \approx \mathbf{0{,}167}$.
  2. Le programme affichera une valeur très proche de $0{,}167$ (par exemple $0{,}1658$ ou $0{,}1682$).
  3. En raison de la **fluctuation d'échantillonnage**, le hasard produit de légères variations autour de la valeur moyenne théorique. Ce n'est qu'à l'infini que l'égalité serait parfaite.

- **Exercice 14 (Le paradoxe des anniversaires) :**
  1. Pour que le 2e élève ait une date différente du 1er : $\frac{364}{365}$.
  2. Pour le 3e élève : $\frac{363}{365}$.
  3. La probabilité que tous les 25 élèves aient des dates différentes est le produit de ces 25 fractions : $P(\text{tous différents}) \approx 0{,}43$.
     Par conséquent, la probabilité qu'au moins deux élèves soient nés le même jour est :
     $$P(\text{au moins deux identiques}) = 1 - 0{,}43 = \mathbf{0{,}57} \quad (\mathbf{57\,\%}).$$
     Comme $57\,\% > 50\,\%$, le professeur avait totalement raison : il y a plus d'une chance sur deux !

- **Exercice 15 (Pascal et Fermat à 2 contre 0) :**
  1. Le joueur A n'a besoin que d'une seule victoire (il mène 2-0). Le joueur B doit enchaîner 3 victoires d'affilée pour gagner 3-2. Il suffit au maximum de **3 manches supplémentaires**.
  2. Arbre des manches supplémentaires :
     - Manche 1 : soit A gagne ($1/2$) $\implies$ A vainqueur (3-0).
     - Soit B gagne ($1/2$) :
       - Manche 2 : soit A gagne ($1/4$) $\implies$ A vainqueur (3-1).
       - Soit B gagne ($1/4$) :
         - Manche 3 : soit A gagne ($1/8$) $\implies$ A vainqueur (3-2).
         - Soit B gagne ($1/8$) $\implies$ B vainqueur (3-3 final).
  3. Le joueur B ne gagne que dans un seul scénario : gagner les 3 manches consécutives, de probabilité :
     $$P(\text{B gagne}) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \mathbf{\frac{1}{8}} = \mathbf{12{,}5\,\%}.$$
     Le joueur A a donc $P(\text{A gagne}) = 1 - \frac{1}{8} = \mathbf{\frac{7}{8}} = \mathbf{87{,}5\,\%}$.
  4. Répartition équitable des 100 pistoles :
     - Pour A : $\frac{7}{8} \times 100 = \mathbf{87{,}5\text{ pistoles}}$.
     - Pour B : $\frac{1}{8} \times 100 = \mathbf{12{,}5\text{ pistoles}}$.

---

### La question qui ouvre la suite

Ici s'achève notre grand voyage à travers le Collège.
Tu es parti du mystère des lettres d'Al-Khwarizmi, tu as équilibré des balances, dompté le théorème de Pythagore, mesuré la Terre avec Ératosthène, percé les secrets d'Euclide et appris à prédire l'incertain avec Pascal et Fermat.

Mais une immense frontière se dresse devant toi. Jusqu'à présent, nos nombres étaient soit des entiers comptés sur les doigts, soit des longueurs figées dans des figures immobiles.
Que se passe-t-il quand le vent souffle, quand un voilier lutte contre le courant en pleine tempête ? Comment représenter une force qui tire dans une direction précise avec une certaine intensité ?
Bienvenue au Lycée : au Volume V, les nombres vont prendre des flèches, s'envoler dans le ciel et devenir des **vecteurs**.
