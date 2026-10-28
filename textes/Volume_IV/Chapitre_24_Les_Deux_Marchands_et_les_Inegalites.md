# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 24 : Les Deux Marchands et les Inégalités

> *« Tant que les deux plateaux sont de niveau, le monde dort dans une paix immobile. Mais dès qu'un plateau plonge, le mouvement naît. L'inégalité n'est pas un défaut de justice : c'est le moteur du commerce, le seuil de rentabilité, la frontière exacte où une décision devient meilleure qu'une autre. »*

---

### Ce que tu vas découvrir

- Comment raisonner sur une **balance déséquilibrée** sans la faire basculer.
- Les notations $\le, \ge, <, >$ : ce qu'elles veulent dire et comment les lire sans hésiter.
- La règle d'or des inégalités : pourquoi ajouter ou retrancher conserve l'ordre, pourquoi multiplier par un nombre positif ne change rien…
- … et pourquoi **multiplier ou diviser par un nombre négatif INVERSE le sens** de l'inégalité (le mystère du miroir et du thermomètre).
- Comment résoudre une **inéquation du premier degré** et peindre ses solutions sur une **droite graduée** avec des crochets orientés.
- Comment percer le secret de deux inconnues à la fois grâce aux **systèmes d'équations** : la méthode par **substitution** et la méthode par **combinaison linéaire**.
- L'interprétation géométrique lumineuse : un système n'est rien d'autre que le **point de rencontre de deux droites**.
- Des applications palpitantes à la vie réelle : comparer deux tarifs de marchands, calculer le seuil de rentabilité et réussir des mélanges parfaits.

---

### 1. Le problème : la foire aux épices de Venise et le dilemme du marchand

Nous sommes en **1340**, sur le quai du Rialto à **Venise**. Les galères reviennent d'Orient, les cales chargées de cannelle, de poivre noir et de safran. Deux marchands vénitiens, Giovanni et Marco, ont installé leurs étals face à face sur la place du marché. Tous deux vendent la même huile d'olive de Crète de première pression.

Mais chacun propose une formule tarifaire différente pour attirer les aubergistes et les marins :

* **Le marchand Giovanni** annonce :
  *« Entrée libre ! Aucun abonnement ! Je vends chaque litre d'huile d'olive au prix fixe de 6 ducats le litre. »*
* **Le marchand Marco**, plus rusé, propose :
  *« Payez une carte de client fidèle à 30 ducats pour la saison, et je vous livre chaque litre d'huile à seulement 4 ducats le litre ! »*

```
     Tarif Giovanni :  Prix = 6 × Nombre de litres
     Tarif Marco    :  Prix = 30 + 4 × Nombre de litres
```

Un tavernier s'arrête, hésitant, sa bourse à la ceinture. Il demande à son jeune commis :
*« Chez qui devons-nous acheter notre huile cette saison ? »*

Le commis répond avec bon sens :
*« Cela dépend de notre consommation, maître ! Si nous n'achetons que 2 litres pour la semaine, Giovanni nous coûte $2 \times 6 = 12$ ducats, alors que chez Marco, nous paierions $30 + 4 \times 2 = 38$ ducats : Giovanni est bien plus avantageux.
Mais si nous tenons une grande auberge et achetons 50 litres, Giovanni nous coûterait $50 \times 6 = 300$ ducats, tandis que Marco ne nous demanderait que $30 + 4 \times 50 = 230$ ducats : Marco devient nettement moins cher ! »*

Le maître aubergiste fronce les sourcils :
*« Très bien. Mais à partir de **combien de litres exactement** le tarif de Marco devient-il plus avantageux que celui de Giovanni ? »*

Ce n'est plus une égalité qu'il faut résoudre, mais une **inégalité** :
$$30 + 4x < 6x.$$
On cherche la zone où la dépense chez Marco est *strictement inférieure* à celle chez Giovanni.

Et ce n'est pas tout. Le lendemain, Giovanni et Marco s'associent pour vendre un lot de 100 amphores contenant au total 380 litres d'huile, certaines amphores faisant 3 litres et d'autres 5 litres. Combien y a-t-il d'amphores de chaque sorte ? C'est un problème à **deux inconnues**, où deux conditions doivent être satisfaites en même temps.

Pour répondre au tavernier et percer les secrets du marché, nous devons forger deux nouveaux outils : **les inéquations** et **les systèmes linéaires**.

---

### 2. Le langage des inégalités : comparer des grandeurs

#### 2.1 Les symboles et leur sens de lecture

En mathématiques, une égalité ($=$) affirme que deux grandeurs ont exactement la même valeur. Une **inégalité** traduit un déséquilibre : une grandeur est plus grande ou plus petite qu'une autre.

| Symbole | Signification | Lecture | Exemple |
|---|---|---|---|
| $<$ | Strictement inférieur | « est strictement plus petit que » | $3 < 7$ |
| $>$ | Strictement supérieur | « est strictement plus grand que » | $8 > 2$ |
| $\le$ ou $\leqslant$ | Inférieur ou égal | « est inférieur ou égal à » (au plus) | $x \le 10$ ($x$ vaut 10 ou moins) |
| $\ge$ ou $\geqslant$ | Supérieur ou égal | « est supérieur ou égal à » (au moins) | $x \ge 18$ ($x$ vaut 18 ou plus) |

> **💡 L'astuce visuelle de la pointe —** Le symbole s'ouvre toujours en grand vers le plus gros nombre et pointe son extrémité fine vers le plus petit :
> $$\text{GRAND} > \text{petit} \qquad \text{petit} < \text{GRAND}.$$

- **Inégalité stricte ($<$ ou $>$) :** L'égalité est exclue. Si l'âge $a > 12$, avoir 12 ans pile ne convient pas.
- **Inégalité large ($\le$ ou $\ge$) :** L'égalité est acceptée. Si la note $n \ge 10$, avoir 10 pile est suffisant pour réussir.

---

### 3. Les règles de la balance penchée

Reprenons l'image de la balance à deux plateaux d'Al-Khwarizmi, mais cette fois-ci, **le fléau penche**. Le plateau de gauche est plus haut que le plateau de droite : le côté gauche est plus léger que le côté droit ($A < B$).

```
                A (Plus léger)
                o─────o
                \     /
                 \   /                           B (Plus lourd)
        ───────────[■]────────                  o─────o
                              \                 \     /
                               \                 \   /
                                ───────────[■]────────
                                     ▲
```

Que se passe-t-il si nous effectuons des opérations sur les deux plateaux en même temps ?

#### 3.1 Règle 1 : Ajouter ou soustraire un même nombre

Si tu ajoutes 2 kg de plomb sur le plateau de gauche ET 2 kg de plomb sur le plateau de droite, le plateau de droite reste plus lourd. Le sens du déséquilibre ne change pas d'un millimètre.
De même, si tu retires 3 kg des deux côtés, la balance conserve son inclinaison.

> **📐 Règle fondamentale 1 — Addition et soustraction.**
> On ne change pas le sens d'une inégalité si l'on **ajoute** ou si l'on **soustrait** un même nombre aux deux membres :
> $$\text{Si } a < b, \text{ alors } a + c < b + c \quad \text{et} \quad a - c < b - c.$$

*Exemple numérique :*
On sait que $3 < 8$.
- Ajoutons $5$ : $3 + 5 < 8 + 5 \implies 8 < 13$ (vrai).
- Soustrayons $10$ : $3 - 10 < 8 - 10 \implies -7 < -2$ (vrai, $-7$ est bien plus froid que $-2$).

#### 3.2 Règle 2 : Multiplier ou diviser par un nombre POSITIF

Si tu triples le contenu du plateau gauche et que tu triples le contenu du plateau droit, le plateau lourd devient trois fois plus lourd, et le plateau léger trois fois plus léger. Le sens du déséquilibre reste rigoureusement le même.

> **📐 Règle fondamentale 2 — Multiplication et division par un nombre POSITIF ($c > 0$).**
> On ne change pas le sens d'une inégalité si l'on **multiplie** ou si l'on **divise** ses deux membres par un même nombre **strictement positif** :
> $$\text{Si } a < b \text{ et } c > 0, \text{ alors } a \times c < b \times c \quad \text{et} \quad \frac{a}{c} < \frac{b}{c}.$$

*Exemple numérique :*
On a $-4 < 6$. Multiplions par $3$ :
$$-4 \times 3 < 6 \times 3 \implies -12 < 18 \quad \text{(toujours vrai)}.$$

#### 3.3 Règle 3 : Le grand renversement ! Multiplier ou diviser par un nombre NÉGATIF

Voici maintenant le phénomène le plus surprenant de l'algèbre, celui qui piège tant d'élèves.

Prenons deux nombres évidents :
$$2 < 5.$$
Multiplions les deux membres par $-1$. Que deviennent-ils ?
- À gauche : $2 \times (-1) = -2$.
- À droite : $5 \times (-1) = -5$.

Comparons maintenant $-2$ et $-5$. Quel nombre est le plus grand ?
Sur un thermomètre, $-2^\circ\text{C}$ est plus chaud que $-5^\circ\text{C}$.
Sur la droite graduée, $-2$ est situé **à droite** de $-5$ :
$$-2 > -5 \text{ !}$$

**L'inégalité s'est inversée !** Le signe $<$ est devenu $>$.

```
     ───|──────|──────|──────|──────|──────|──────|──────|──────|──────|───>
       -5     -4     -3     -2     -1      0      1      2      3      5
        ▲                    ▲                    ▲                    ▲
        └────── < ───────────┘                    └──────── < ─────────┘
            -5 est PLUS PETIT que -2                  2 est PLUS PETIT que 5
```

> **📐 Règle fondamentale 3 — Multiplication et division par un nombre NÉGATIF ($c < 0$).**
> **Quand on multiplie ou que l'on divise les deux membres d'une inégalité par un nombre STRICTEMENT NÉGATIF, ON DOIT OBLIGATOIREMENT INVERSER LE SENS DE L'INÉGALITÉ !**
> $$\text{Si } a < b \text{ et } c < 0, \text{ alors } a \times c \mathbf{ > } b \times c \quad \text{et} \quad \frac{a}{c} \mathbf{ > } \frac{b}{c}.$$

**Pourquoi ce renversement ? Deux explications concrètes :**
1. **L'explication par le miroir :** Multiplier par $-1$, c'est faire pivoter la droite numérique d'un demi-tour autour du zéro. Ce qui était le plus loin vers la droite dans le monde positif ($+5$) se retrouve projeté le plus loin vers la gauche dans le monde négatif ($-5$). Le champion du grand devient le champion du petit !
2. **L'explication par la dette :** Avoir 200 € sur son compte est plus avantageux qu'avoir 500 € ? Non, $200 < 500$. Mais avoir une **dette** de 200 € ($-200$) est bien préférable à avoir une dette de 500 € ($-500$) ! Donc $-200 > -500$.

---

### 4. Résolution d'une inéquation et représentation graphique

#### 4.1 Qu'est-ce qu'une inéquation ?

Une inéquation du premier degré est une inégalité comportant une inconnue $x$.
Contrairement à une équation ordinaire qui n'a souvent qu'une ou deux solutions isolées ($x = 3$), une inéquation possède en général **une infinité de solutions** : tout un paquet de nombres, un intervalle continu.

#### 4.2 Exemple pas à pas de résolution

Résolvons l'inéquation du problème de nos marchands :
$$30 + 4x < 6x.$$

1. **Regrouper les termes en $x$ :**
   Soustrayons $4x$ des deux côtés (règle 1 : soustraire ne change pas le sens) :
   $$30 + 4x - 4x < 6x - 4x$$
   $$30 < 2x.$$
2. **Isoler $x$ :**
   Divisons les deux côtés par $+2$ (règle 2 : diviser par un nombre positif ne change pas le sens) :
   $$\frac{30}{2} < \frac{2x}{2} \implies 15 < x \quad \text{ou encore} \quad x > 15.$$
3. **Conclusion pour les marchands :**
   Dès que le tavernier achète **strictement plus de 15 litres d'huile**, le tarif de Marco devient plus avantageux ! Pour 15 litres pile, les deux marchands coûtent exactement la même somme ($15 \times 6 = 90$ ducats et $30 + 4 \times 15 = 90$ ducats).

#### 4.3 Un exemple avec inversion de sens

Résolvons l'inéquation :
$$-3x + 7 \le 22.$$

1. On soustrait $7$ des deux côtés :
   $$-3x \le 22 - 7 \implies -3x \le 15.$$
2. On doit diviser par le coefficient de $x$, qui est **$-3$ (négatif)**.
   **Alerte rouge : on inverse immédiatement le sens du symbole !**
   $$\frac{-3x}{-3} \ge \frac{15}{-3}$$
   $$x \ge -5.$$
Les solutions sont tous les nombres supérieurs ou égaux à $-5$.

#### 4.4 Représenter les solutions sur une droite graduée

Puisqu'il y a une infinité de solutions, on les représente graphiquement en surlignant (ou hachurant) la portion de la droite graduée qui convient.

Comment indiquer si le nombre frontière fait partie ou non des solutions ? **Grâce au sens des crochets !**

- **Le crochet est tourné VERS la zone des solutions :** le nombre frontière est **inclus** ($\le$ ou $\ge$).
  Exemple pour $x \ge -5$ :
  ```
  ──────────┼──────────[████████████████████████████████>
           -5          -5 est inclus (crochet vers la droite)
  ```
- **Le crochet tourne le DOS à la zone des solutions :** le nombre frontière est **exclu** ($<$ ou $>$).
  Exemple pour $x > 15$ :
  ```
  ──────────┼──────────]████████████████████████████████>
            0          15 est exclu (crochet qui repousse la zone)
  ```

> **🧭 Méthode — Noter les solutions sous forme d'intervalle.**
> Au collège et au lycée, on note l'ensemble des solutions $S$ avec des crochets :
> - Pour $x \ge -5$ : $S = [-5 \; ; \; +\infty[$ (se lit « intervalle fermé en $-5$ jusqu'à plus l'infini »).
> - Pour $x < 3$ : $S = ]-\infty \; ; \; 3[$ (se lit « de moins l'infini à 3 exclu »).
> Le symbole $\infty$ (« l'infini ») porte **toujours** un crochet ouvert vers l'extérieur, car l'infini n'est pas un nombre qu'on peut enfermer.

---

### 5. Systèmes de deux équations à deux inconnues

Revenons à la seconde énigme de Venise :
*Un marchand vend un lot de 100 amphores d'huile. Il y a des petites amphores de 3 litres et des grandes amphores de 5 litres. Le volume total d'huile est de 380 litres. Combien y a-t-il d'amphores de chaque sorte ?*

Ici, il y a **deux grandeurs inconnues** :
- Soit $x$ le nombre de petites amphores (de 3 L).
- Soit $y$ le nombre de grandes amphores (de 5 L).

Chaque phrase de l'énoncé fournit une équation :
1. *« 100 amphores au total »* $\implies x + y = 100$.
2. *« 380 litres au total »* $\implies 3x + 5y = 380$.

Ces deux équations forment ce qu'on appelle un **système de deux équations du premier degré à deux inconnues**. On les réunit avec une grande accolade :
$$\begin{cases} x + y = 100 & (L_1) \\ 3x + 5y = 380 & (L_2) \end{cases}$$

Résoudre ce système, c'est trouver le couple $(x, y)$ unique qui rend les deux égalités vraies en même temps. Il existe deux méthodes universelles pour y parvenir.

---

#### 5.1 Méthode 1 : La méthode par substitution (l'espion infiltré)

Le principe est simple : on utilise l'une des équations pour exprimer une lettre en fonction de l'autre, puis on va « injecter » cette expression dans la deuxième équation.

1. **Isoler une lettre facile :**
   Dans la première ligne $x + y = 100$, isolons $x$ :
   $$x = 100 - y.$$
2. **Substituer dans l'autre ligne :**
   Dans la deuxième ligne $3x + 5y = 380$, remplaçons la lettre $x$ par le paquet $(100 - y)$ :
   $$3(100 - y) + 5y = 380.$$
   Magie : il n'y a plus de $x$ ! C'est une simple équation à une seule inconnue $y$ !
3. **Résoudre pour $y$ :**
   $$300 - 3y + 5y = 380$$
   $$300 + 2y = 380$$
   $$2y = 380 - 300 = 80$$
   $$y = \frac{80}{2} = 40.$$
4. **Calculer la première inconnue $x$ :**
   Puisque $x = 100 - y$ :
   $$x = 100 - 40 = 60.$$
5. **Conclusion et vérification :**
   Le marchand a vendu $60$ petites amphores et $40$ grandes amphores.
   Vérification :
   - Total amphores : $60 + 40 = 100$ (exact).
   - Total litres : $60 \times 3 + 40 \times 5 = 180 + 200 = 380$ litres (exact !).
   Le couple solution s'écrit : $(x \; ; \; y) = (60 \; ; \; 40)$.

*Quand utiliser la substitution ?* Quand l'une des inconnues a pour coefficient $1$ ou $-1$ (comme $x$ ou $y$ dans $x + y = 100$), car elle s'isole immédiatement sans créer de fractions affreuses.

---

#### 5.2 Méthode 2 : La méthode par combinaison linéaire (le duel d'élimination)

Que faire quand toutes les inconnues ont des coefficients embarrassants, comme :
$$\begin{cases} 2x + 3y = 19 & (L_1) \\ 5x - 2y = 19 & (L_2) \end{cases}$$
Isoler $x$ dans la première ligne donnerait $x = \frac{19 - 3y}{2}$, ce qui remplirait le calcul de fractions compliquées.

La **combinaison linéaire** (aussi appelée méthode par addition ou élimination de Gauss) consiste à multiplier les lignes par des nombres bien choisis pour que les coefficients d'une même inconnue deviennent **opposés** (par exemple $+6y$ et $-6y$). En additionnant les deux lignes membre à membre, cette inconnue disparaît instantanément !

Résolvons ce système pas à pas :

1. **Choisir l'inconnue à éliminer :** Choisissons d'éliminer $y$.
   Le coefficient de $y$ est $+3$ dans $(L_1)$ et $-2$ dans $(L_2)$.
   Le plus petit multiple commun de 3 et 2 est 6.
2. **Multiplier les lignes :**
   - Multiplions toute la ligne $(L_1)$ par $2$ :
     $$2 \times (2x + 3y) = 2 \times 19 \implies 4x + 6y = 38.$$
   - Multiplions toute la ligne $(L_2)$ par $3$ :
     $$3 \times (5x - 2y) = 3 \times 19 \implies 15x - 6y = 57.$$
3. **Additionner les deux lignes membre à membre :**
   ```
        4x  +  6y  =  38
   +   15x  -  6y  =  57
   ─────────────────────
       19x  +   0  =  95
   ```
   Le terme en $y$ s'est évaporé !
4. **Trouver $x$ :**
   $$19x = 95 \implies x = \frac{95}{19} = 5.$$
5. **Trouver $y$ :**
   Remplaçons $x = 5$ dans n'importe quelle équation de départ, par exemple $(L_1)$ :
   $$2(5) + 3y = 19 \implies 10 + 3y = 19 \implies 3y = 9 \implies y = 3.$$
6. **Conclusion :**
   La solution du système est le couple $(x \; ; \; y) = (5 \; ; \; 3)$.

---

### 6. L'interprétation géométrique : deux droites qui se croisent

Chaque équation du premier degré à deux inconnues, comme $2x + 3y = 19$, correspond graphiquement à une **droite** dans le repère cartésien (Chapitre 20).
Chaque point $(x ; y)$ situé sur la droite est une solution de l'équation.

Résoudre le système, c'est chercher un point $(x ; y)$ qui appartient **à la fois à la première droite $(d_1)$ et à la deuxième droite $(d_2)$**.

```
          y ▲                     (d1)
            │                    /
            │                   /     (d2)
            │                  /     /
          3 ┼─────────────────*─────/──
            │                /│    /
            │               / │   /
            │              /  │  /
          ──┼─────────────┼───┼─┼────────> x
            0             2   5
                         Point d'intersection : (5 ; 3)
```

Il existe trois configurations géométriques possibles :

1. **Les droites sont sécantes (se coupent en un point unique) :**
   C'est le cas général. Le système admet **une solution unique** $(x_0 ; y_0)$.
2. **Les droites sont strictement parallèles (ne se rencontrent jamais) :**
   Le système n'admet **aucune solution** ($S = \emptyset$).
   *Exemple :* $\begin{cases} x + y = 4 \\ x + y = 10 \end{cases}$ (la somme de deux nombres ne peut pas valoir 4 et 10 en même temps !).
3. **Les droites sont confondues (l'une est posée sur l'autre) :**
   Les deux équations sont en fait deux écritures de la même droite (par exemple $x + y = 2$ et $2x + 2y = 4$).
   Le système admet **une infinité de solutions**.

---

### 7. L'histoire vraie : le secret des baguettes du livre des Neuf Chapitres

Deux siècles avant notre ère, dans la Chine des Han, les mathématiciens impériaux résolvaient déjà des systèmes d'équations pour gérer les récoltes de grains, la taille des corvées et les impôts de l'Empire.

Dans le plus grand classique des mathématiques chinoises, *Les Neuf Chapitres sur l'Art Mathématique* (*Jiuzhang Suanshu*), le chapitre 8 est intitulé *Fangcheng* (« Disposition en tableau rectangulaire »).

Les savants chinois disposaient des baguettes de bambou rouges (pour les nombres positifs) et noires (pour les nombres négatifs) sur un échiquier de feutre. Chaque colonne représentait une équation et chaque ligne une céréale différente (le millet supérieur, le millet moyen, le millet inférieur).

```
   [ 3 gerbes de millet supérieur ] + [ 2 gerbes de millet moyen ] + [ 1 gerbe de millet bas ] = 39 mesures
   [ 2 gerbes de millet supérieur ] + [ 3 gerbes de millet moyen ] + [ 1 gerbe de millet bas ] = 34 mesures
   [ 1 gerbe de millet supérieur ] + [ 2 gerbes de millet moyen ] + [ 3 gerbes de millet bas ] = 26 mesures
```

En faisant glisser les baguettes, en multipliant une colonne et en la soustrayant à une autre, ils éliminaient les grains un à un pour faire apparaître des zéros. Cette méthode chinoise vieille de 2 200 ans est exactement la **méthode du pivot de Gauss**, enseignée aujourd'hui dans toutes les universités du monde et programmée au cœur des supercalculateurs modernes !

---

### 8. Exemples résolus pas à pas

#### Exemple 1 : Résoudre une inéquation avec parenthèses et fractions simples
Résoudre dans les réels l'inéquation suivante et représenter les solutions :
$$4(2x - 3) - 5x \ge 7x - 24.$$

**Résolution détaillée :**
1. On développe le membre de gauche :
   $$8x - 12 - 5x \ge 7x - 24 \implies 3x - 12 \ge 7x - 24.$$
2. On regroupe les termes en $x$ à gauche en soustrayant $7x$ :
   $$3x - 7x - 12 \ge -24 \implies -4x - 12 \ge -24.$$
3. On ajoute $12$ des deux côtés :
   $$-4x \ge -24 + 12 \implies -4x \ge -12.$$
4. On divise par le coefficient devant $x$, qui est **$-4$ (négatif)**.
   **On inverse le sens du symbole ($\ge$ devient $\le$) :**
   $$x \le \frac{-12}{-4} \implies x \le 3.$$
5. Représentation graphique :
   Les solutions sont tous les nombres inférieurs ou égaux à 3.
   Le crochet est fermé en 3 et orienté vers la gauche (vers les solutions) :
   ```
   <████████████████████████████]──────────┼───────>
                                3          0
   ```
   Ensemble des solutions : $S = ]-\infty \; ; \; 3]$.

---

#### Exemple 2 : Inéquation avec quotient et gestion rigoureuse des signes
Résoudre l'inéquation :
$$\frac{2 - 5x}{3} > 4.$$

**Résolution détaillée :**
1. On multiplie les deux membres par $3$. Comme $3 > 0$, le sens est conservé :
   $$2 - 5x > 4 \times 3 \implies 2 - 5x > 12.$$
2. On soustrait 2 :
   $$-5x > 12 - 2 \implies -5x > 10.$$
3. On divise par **$-5$ (négatif)**, donc le symbole s'inverse ($>$ devient $<$) :
   $$x < \frac{10}{-5} \implies x < -2.$$
Conclusion : $S = ]-\infty \; ; \; -2[$. Le crochet en $-2$ est ouvert vers la droite (tourne le dos aux solutions car $-2$ est exclu).

---

#### Exemple 3 : Système résolu par substitution
Résoudre le système :
$$\begin{cases} 3x - y = 7 & (L_1) \\ 2x + 4y = 42 & (L_2) \end{cases}$$

**Résolution détaillée :**
1. Dans $(L_1)$, la variable $y$ a un coefficient $-1$, elle s'isole immédiatement :
   $$-y = 7 - 3x \implies y = 3x - 7.$$
2. On remplace $y$ par $(3x - 7)$ dans l'équation $(L_2)$ :
   $$2x + 4(3x - 7) = 42$$
   $$2x + 12x - 28 = 42$$
   $$14x - 28 = 42$$
   $$14x = 42 + 28 = 70 \implies x = \frac{70}{14} = 5.$$
3. On calcule $y$ avec l'expression trouvée à l'étape 1 :
   $$y = 3(5) - 7 = 15 - 7 = 8.$$
4. Vérification dans les deux équations de départ :
   - $(L_1)$ : $3(5) - 8 = 15 - 8 = 7$ (vrai).
   - $(L_2)$ : $2(5) + 4(8) = 10 + 32 = 42$ (vrai).
Conclusion : Le couple solution unique est $(x \; ; \; y) = (5 \; ; \; 8)$.

---

#### Exemple 4 : Système résolu par combinaison linéaire
Résoudre le système :
$$\begin{cases} 4x + 3y = 1 & (L_1) \\ 6x - 5y = 20 & (L_2) \end{cases}$$

**Résolution détaillée :**
Éliminons $y$. Les coefficients de $y$ sont $+3$ et $-5$.
Leur plus petit commun multiple est 15.
1. On multiplie $(L_1)$ par $5$ :
   $$5 \times (4x + 3y) = 5 \times 1 \implies 20x + 15y = 5.$$
2. On multiplie $(L_2)$ par $3$ :
   $$3 \times (6x - 5y) = 3 \times 20 \implies 18x - 15y = 60.$$
3. On additionne les deux nouvelles équations terme à terme :
   $$(20x + 18x) + (15y - 15y) = 5 + 60$$
   $$38x = 65 \implies x = \frac{65}{38}.$$
   *Remarque :* On peut aussi éliminer $x$ en multipliant $(L_1)$ par $3$ et $(L_2)$ par $-2$ :
   - $3 \times (L_1) \implies 12x + 9y = 3$
   - $-2 \times (L_2) \implies -12x + 10y = -40$
   Additionnons : $19y = -37 \implies y = -\frac{37}{19} = -\frac{74}{38}$.
Conclusion : Le couple solution est $\left( \frac{65}{38} \; ; \; -\frac{37}{19} \right)$.

---

#### Exemple 5 : Problème concret de billetterie (mise en système)
Pour financer leur voyage de fin d'année, les élèves de 3e organisent une soirée théâtre.
- Le tarif pour les adultes est de 8 €.
- Le tarif pour les enfants est de 4,50 €.
À la fin de la soirée, la caisse enregistre 240 spectateurs et une recette totale de 1 570 €.
Combien d'adultes et combien d'enfants ont assisté à la pièce ?

**Résolution détaillée :**
1. **Choix des inconnues :**
   - Soit $a$ le nombre d'adultes.
   - Soit $e$ le nombre d'enfants.
2. **Mise en équations :**
   - Nombre total de spectateurs : $a + e = 240$.
   - Recette totale en euros : $8a + 4{,}5e = 1570$.
3. **Résolution par substitution :**
   De la première équation, on tire $e = 240 - a$.
   On injecte dans la deuxième :
   $$8a + 4{,}5(240 - a) = 1570$$
   $$8a + 1080 - 4{,}5a = 1570$$
   $$3{,}5a + 1080 = 1570$$
   $$3{,}5a = 1570 - 1080 = 490$$
   $$a = \frac{490}{3{,}5} = \frac{4900}{35} = 140.$$
4. **Calcul de la seconde inconnue :**
   $$e = 240 - 140 = 100.$$
5. **Conclusion et phrase réponse :**
   Il y avait 140 adultes et 100 enfants dans la salle.
   Vérification : $140 \times 8 + 100 \times 4{,}5 = 1120 + 450 = 1570$ €. Tout est cohérent.

---

### Ce qu'il faut retenir

1. **Les règles d'or des inégalités :**
   - Ajouter ou soustraire un même nombre ne change **jamais** le sens de l'inégalité.
   - Multiplier ou diviser par un nombre **positif** ne change **pas** le sens.
   - Multiplier ou diviser par un nombre **négatif INVERSE OBLIGATOIREMENT le sens** ($<$ devient $>$, $\le$ devient $\ge$).
2. **Représentation sur droite graduée :**
   - Crochet fermé $[\text{ ou }]$ vers les solutions si le nombre est **inclus** ($\le, \ge$).
   - Crochet ouvert $]\text{ ou }[$ dos aux solutions si le nombre est **exclu** ($<, >$).
3. **Système de deux équations à deux inconnues :**
   $$\begin{cases} ax + by = c \\ a'x + b'y = c' \end{cases}$$
   - **Méthode par substitution :** isoler une inconnue dans une ligne et la remplacer dans l'autre (idéale si un coefficient vaut 1 ou $-1$).
   - **Méthode par combinaison :** multiplier les lignes pour obtenir des coefficients opposés devant une inconnue, puis additionner les deux lignes (universelle).
4. **Vision graphique :** La solution d'un système correspond aux coordonnées $(x ; y)$ du point d'intersection des deux droites associées.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 24.1** Compléter avec le symbole adapté ($<$ ou $>$) :
1. Sachant que $x < 5$, comparer $x + 4$ et $9$.
2. Sachant que $y \ge -2$, comparer $y - 3$ et $-5$.
3. Sachant que $a < b$, comparer $3a$ et $3b$.
4. Sachant que $u < v$, comparer $-4u$ et $-4v$.

**Exercice 24.2** Résoudre les inéquations simples du premier degré :
1. $x + 7 < 15$
2. $x - 9 \ge 3$
3. $4x \le 28$
4. $-5x < 35$
5. $-2x \ge -18$
6. $\frac{x}{3} > -4$

**Exercice 24.3** Représenter sur une droite graduée les ensembles de solutions suivants :
1. $x > 4$
2. $x \le -1$
3. $x \ge 2{,}5$
4. $x < 0$

**Exercice 24.4** Tester si le couple $(x = 3 \; ; \; y = 2)$ est solution des systèmes suivants :
1. $\begin{cases} 2x + y = 8 \\ x - y = 1 \end{cases}$
2. $\begin{cases} 3x - 4y = 1 \\ 5x + 2y = 20 \end{cases}$

**Exercice 24.5** Résoudre par la méthode de substitution :
1. $\begin{cases} y = 2x - 1 \\ 3x + y = 14 \end{cases}$
2. $\begin{cases} x + 2y = 8 \\ 3x - 4y = 4 \end{cases}$

**Exercice 24.6** Résoudre par la méthode de combinaison linéaire :
1. $\begin{cases} 2x + y = 11 \\ 3x - y = 9 \end{cases}$
2. $\begin{cases} 3x + 2y = 12 \\ 5x - 2y = 20 \end{cases}$

---

#### Niveau ★★ : Réflexion et enchaînements

**Exercice 24.7** Résoudre et donner l'ensemble des solutions sous forme d'intervalle :
1. $5x - 8 < 2x + 7$
2. $3(x - 2) - 4(2x + 1) \ge 5$
3. $\frac{3x - 1}{4} \le \frac{x + 2}{2}$

**Exercice 24.8** Inéquations à double encadrement :
Trouver tous les nombres $x$ vérifiant à la fois :
$$-3 \le 2x + 1 < 9.$$
*(Indication : retrancher 1 à chaque membre, puis diviser par 2).*

**Exercice 24.9** Résoudre les systèmes linéaires :
1. $\begin{cases} 4x + 3y = 25 \\ 2x - 5y = -7 \end{cases}$
2. $\begin{cases} 5x + 2y = 1 \\ 3x - 4y = 11 \end{cases}$
3. $\begin{cases} 2x - 3y = 7 \\ 4x - 6y = 10 \end{cases}$ (Que se passe-t-il graphiquement ?)

**Exercice 24.10** Le problème du parc de loisirs :
Un parc d'attractions propose deux formules :
- **Formule A :** 25 € l'entrée générale donnant un accès illimité à tous les manèges.
- **Formule B :** 9 € l'entrée simple, plus 2 € par attraction individuelle.
1. Écrire le prix payé pour chacune des formules si l'on fait $x$ attractions.
2. Résoudre une inéquation pour déterminer à partir de combien d'attractions la Formule A devient plus économique que la Formule B.

**Exercice 24.11** Le problème de l'alliage d'argent :
Un orfèvre dispose de deux lingots d'argent :
- Le premier lingot contient $80\,\%$ d'argent pur.
- Le second lingot contient $60\,\%$ d'argent pur.
Il veut fondre ces deux lingots pour obtenir exactement 500 grammes d'un nouvel alliage titré à $75\,\%$ d'argent pur.
Quelle masse de chaque lingot doit-il faire fondre ?

**Exercice 24.12** Géométrie et périmètre :
Un rectangle a une longueur qui dépasse sa largeur de 4 cm. Son périmètre est strictement inférieur à 36 cm.
Quelles valeurs peut prendre la largeur de ce rectangle ?

---

#### Niveau ★★★ : Défis et recherche

**Exercice 24.13** Intersection graphique de deux droites de tarifs :
Dans un repère orthogonal, on trace les deux droites d'équations :
$(d_1) : y = 2x + 1 \quad \text{et} \quad (d_2) : y = -x + 7.$
1. Trouver algébriquement les coordonnées de leur point d'intersection $K$.
2. Résoudre graphiquement puis par le calcul l'inéquation $2x + 1 \le -x + 7$.
3. Interpréter le résultat : quelle droite se situe en dessous de l'autre ?

**Exercice 24.14** Le problème des âges chinois :
Un père dit à son fils :
*« Aujourd'hui, j'ai quatre fois ton âge. Mais dans 20 ans, je n'aurai plus que le double de ton âge. »*
Quels sont les âges actuels du père et du fils ?

**Exercice 24.15** Système à paramètres (pour futurs scientifiques) :
On considère le système :
$$\begin{cases} ax + 2y = 4 \\ 3x + y = 2 \end{cases}$$
Pour quelle valeur du nombre $a$ ce système ne possède-t-il aucun couple solution unique ?
Que peut-on dire des deux droites associées pour cette valeur de $a$ ?

---

### Solutions

#### Niveau ★

**Solution 24.1**
1. $x + 4 < 9$ (on a ajouté 4 aux deux membres).
2. $y - 3 \ge -5$ (on a retranché 3 aux deux membres).
3. $3a < 3b$ (on a multiplié par $3 > 0$).
4. $-4u > -4v$ (on a multiplié par $-4 < 0$, le sens s'inverse !).

**Solution 24.2**
1. $x < 15 - 7 \implies x < 8$.
2. $x \ge 3 + 9 \implies x \ge 12$.
3. $x \le \frac{28}{4} \implies x \le 7$.
4. Division par $-5 < 0$ : $x > \frac{35}{-5} \implies x > -7$.
5. Division par $-2 < 0$ : $x \le \frac{-18}{-2} \implies x \le 9$.
6. Multiplication par $3 > 0$ : $x > -12$.

**Solution 24.3**
1. Zone hachurée à droite de 4, crochet ouvert tourné vers la gauche : $]4 \; ; \; +\infty[$.
2. Zone hachurée à gauche de $-1$, crochet fermé tourné vers la gauche : $]-\infty \; ; \; -1]$.
3. Zone hachurée à droite de $2{,}5$, crochet fermé tourné vers la droite : $[2{,}5 \; ; \; +\infty[$.
4. Zone hachurée à gauche de 0, crochet ouvert tourné vers la droite : $]-\infty \; ; \; 0[$.

**Solution 24.4**
1. $2(3) + 2 = 6 + 2 = 8$ (vrai) et $3 - 2 = 1$ (vrai). Le couple $(3 \; ; \; 2)$ est bien solution du premier système.
2. $3(3) - 4(2) = 9 - 8 = 1$ (vrai). Mais $5(3) + 2(2) = 15 + 4 = 19 \neq 20$ (faux !). Le couple n'est pas solution du second système.

**Solution 24.5**
1. On remplace $y$ par $2x - 1$ dans la deuxième équation :
   $3x + (2x - 1) = 14 \implies 5x - 1 = 14 \implies 5x = 15 \implies x = 3$.
   Puis $y = 2(3) - 1 = 5$. Solution : $(3 \; ; \; 5)$.
2. De la première ligne : $x = 8 - 2y$.
   Deuxième ligne : $3(8 - 2y) - 4y = 4 \implies 24 - 6y - 4y = 4 \implies -10y = -20 \implies y = 2$.
   Puis $x = 8 - 2(2) = 4$. Solution : $(4 \; ; \; 2)$.

**Solution 24.6**
1. En additionnant directement les deux lignes ($+y$ et $-y$ s'annulent) :
   $(2x + 3x) + (y - y) = 11 + 9 \implies 5x = 20 \implies x = 4$.
   Puis $2(4) + y = 11 \implies 8 + y = 11 \implies y = 3$. Solution : $(4 \; ; \; 3)$.
2. En additionnant directement ($+2y$ et $-2y$ s'annulent) :
   $8x = 32 \implies x = 4$.
   Puis $3(4) + 2y = 12 \implies 12 + 2y = 12 \implies 2y = 0 \implies y = 0$. Solution : $(4 \; ; \; 0)$.

---

#### Niveau ★★

**Solution 24.7**
1. $5x - 2x < 7 + 8 \implies 3x < 15 \implies x < 5$. Soit $S = ]-\infty \; ; \; 5[$.
2. $3x - 6 - 8x - 4 \ge 5 \implies -5x - 10 \ge 5 \implies -5x \ge 15 \implies x \le -3$ (inversion du sens). Soit $S = ]-\infty \; ; \; -3]$.
3. Multiplions par 4 (positif) : $3x - 1 \le 2(x + 2) \implies 3x - 1 \le 2x + 4 \implies x \le 5$. Soit $S = ]-\infty \; ; \; 5]$.

**Solution 24.8**
On soustrait 1 à chacun des trois membres :
$$-3 - 1 \le 2x < 9 - 1 \implies -4 \le 2x < 8.$$
On divise chacun des membres par $2 > 0$ :
$$-2 \le x < 4.$$
Les solutions sont tous les nombres réels compris entre $-2$ (inclus) et $4$ (exclu). $S = [-2 \; ; \; 4[$.

**Solution 24.9**
1. Multiplions la 2e équation par $-2$ : $-4x + 10y = 14$.
   Ajoutons à la 1re ($4x + 3y = 25$) : $13y = 39 \implies y = 3$.
   Puis $2x - 5(3) = -7 \implies 2x - 15 = -7 \implies 2x = 8 \implies x = 4$. Solution : $(4 \; ; \; 3)$.
2. Multiplions la 1re équation par 2 : $10x + 4y = 2$.
   Ajoutons à la 2e ($3x - 4y = 11$) : $13x = 13 \implies x = 1$.
   Puis $5(1) + 2y = 1 \implies 2y = -4 \implies y = -2$. Solution : $(1 \; ; \; -2)$.
3. Multiplions la 1re équation par 2 : $4x - 6y = 14$.
   La 2e équation est $4x - 6y = 10$.
   Soustrayons les deux lignes : $(4x - 4x) - (6y - 6y) = 14 - 10 \implies 0 = 4$, ce qui est **impossible** !
   Graphiquement, les deux droites ont la même pente : elles sont **strictement parallèles**. Il n'y a aucun point d'intersection, donc aucune solution ($S = \emptyset$).

**Solution 24.10**
1. Pour $x$ attractions : Prix Formule A $= 25$ € ; Prix Formule B $= 9 + 2x$ €.
2. La Formule A est plus économique si :
   $$25 < 9 + 2x \iff 25 - 9 < 2x \iff 16 < 2x \iff 8 < x \iff x > 8.$$
   Puisque le nombre d'attractions est un nombre entier, la Formule A devient plus avantageuse à partir de **9 attractions**.

**Solution 24.11**
Soit $x$ la masse (en g) du premier lingot (à 80 %) et $y$ la masse du second (à 60 %).
1. Masse totale : $x + y = 500$.
2. Masse d'argent pur : $0{,}80x + 0{,}60y = 0{,}75 \times 500 = 375$.
De la 1re équation : $y = 500 - x$.
Remplaçons dans la 2e :
$0{,}8x + 0{,}6(500 - x) = 375 \implies 0{,}8x + 300 - 0{,}6x = 375 \implies 0{,}2x = 75 \implies x = \frac{75}{0{,}2} = 375 \text{ g}$.
Puis $y = 500 - 375 = 125 \text{ g}$.
L'orfèvre doit faire fondre 375 g du premier lingot et 125 g du second.

**Solution 24.12**
Soit $\ell$ la largeur en cm. La longueur est $L = \ell + 4$.
Le périmètre est $P = 2(\ell + L) = 2(\ell + \ell + 4) = 2(2\ell + 4) = 4\ell + 8$.
L'énoncé indique que $P < 36$, d'où :
$$4\ell + 8 < 36 \implies 4\ell < 28 \implies \ell < 7.$$
De plus, une largeur doit être strictement positive ($\ell > 0$).
La largeur $\ell$ peut donc prendre n'importe quelle valeur strictement comprise entre 0 et 7 cm : $\ell \in ]0 \; ; \; 7[$.

---

#### Niveau ★★★

**Solution 24.13**
1. Au point d'intersection, les ordonnées $y$ sont égales :
   $$2x + 1 = -x + 7 \implies 3x = 6 \implies x = 2.$$
   Puis $y = 2(2) + 1 = 5$. Le point d'intersection est $K(2 \; ; \; 5)$.
2. Résolvons $2x + 1 \le -x + 7$ :
   $$3x \le 6 \implies x \le 2.$$
   L'ensemble des solutions est $S = ]-\infty \; ; \; 2]$.
3. Interprétation : pour toutes les abscisses $x \le 2$, la droite $(d_1)$ est située **en dessous** (ou coupe) la droite $(d_2)$. Au-delà de $x = 2$, c'est la droite $(d_1)$ qui passe au-dessus.

**Solution 24.14**
Soit $p$ l'âge actuel du père et $f$ l'âge actuel du fils.
1. « Aujourd'hui, j'ai 4 fois ton âge » : $p = 4f$.
2. « Dans 20 ans, le père aura $p + 20$ et le fils aura $f + 20$ » :
   $$p + 20 = 2(f + 20).$$
Substituons $p = 4f$ dans la deuxième égalité :
$$4f + 20 = 2f + 40 \implies 2f = 20 \implies f = 10.$$
Puis $p = 4 \times 10 = 40$.
Le père a aujourd'hui 40 ans et le fils a 10 ans.
Vérification dans 20 ans : le père aura 60 ans, le fils 30 ans, et 60 est bien le double de 30 !

**Solution 24.15**
Isolons $y$ dans la seconde équation : $y = 2 - 3x$.
Remplaçons dans la première équation :
$$ax + 2(2 - 3x) = 4 \implies ax + 4 - 6x = 4 \implies (a - 6)x = 0.$$
- Si $a \neq 6$, alors $a - 6 \neq 0$, et on trouve une solution unique $x = 0$ (d'où $y = 2$).
- Si $a = 6$, l'équation devient $0 \times x = 0$, ce qui est vrai pour **tout réel $x$** ! Dans ce cas, les deux équations sont en fait équivalentes ($6x + 2y = 4 \iff 3x + y = 2$). Les deux droites sont **confondues**, et il y a une infinité de solutions.
Pour avoir deux droites strictement parallèles (aucune solution), il aurait fallu une équation comme $6x + 2y = 5$.
Conclusion : la valeur critique est **$a = 6$**. Pour cette valeur, le déterminant s'annule ($a \times 1 - 2 \times 3 = a - 6 = 0$), et le système n'admet plus de solution unique.

---

### La question qui ouvre la suite

Regarde ce que nous venons de faire : à chaque nombre de litres d'huile $x$, nous avons associé un coût $P(x) = 6x$ ou $P(x) = 30 + 4x$. À chaque nombre de manèges, nous avons associé une dépense totale. 

Ce mécanisme puissant où un nombre en entrée produit un nombre unique en sortie s'appelle une **fonction**. Pourquoi ne pas regarder cette machine en face ? Quelle forme a le chemin tracé par une relation proportionnelle ou par un abonnement fixe ? C'est le grand voyage qui nous attend dans le chapitre 25 : **La Machine à Doubler et la Droite du Tarif**.
