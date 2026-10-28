# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 25 : La Machine à Doubler et la Droite du Tarif

> *« Une équation est un instantané : elle fige la balance à la recherche d'un trésor immobile. Une fonction, c'est le film tout entier : elle saisit le mouvement du monde, où chaque cause entraîne un effet, où chaque pas en avant élève le voyageur vers une nouvelle altitude. »*

---

### Ce que tu vas découvrir

- Qu'est-ce qu'une **fonction** : la formidable « boîte magique » qui avale un nombre et en recrache un autre selon une loi immuable.
- Le vocabulaire officiel sans mystère : qui est l'**antécédent**, qui est l'**image**, et pourquoi on note $f(x)$ ou $x \mapsto f(x)$.
- Les trois miroirs d'une fonction : sa **formule**, son **tableau de valeurs** et sa **courbe graphique**.
- La **fonction linéaire** $f(x) = ax$ : l'incarnation géométrique de la proportionnalité, la droite fidèle qui ne quitte jamais l'origine $(0 ; 0)$.
- La **fonction affine** $f(x) = ax + b$ : la droite des abonnements du monde réel, son **coefficient directeur** $a$ (la pente) et son **ordonnée à l'origine** $b$ (le prix d'entrée).
- Comment lire et fabriquer ces droites d'un simple coup d'œil : « j'avance de 1, je monte de $a$ ».
- Des applications palpitantes : forfaits mobiles, compteurs de taxi, vitesses, et la célèbre conversion entre degrés Celsius et Fahrenheit.

---

### 1. Le problème : la forge magique et le compteur du loueur de barques

Imagine que tu visites un village perché au bord d'un grand lac de montagne. 
Au bout de la jetée, deux artisans proposent leurs services aux voyageurs.

Le premier est un vieil horloger inventeur. Dans son atelier, il a fabriqué une boîte d'acier munie d'une fente sur le dessus et d'un tiroir en bas. Il l'appelle sa **« Machine à Transformer »**. 
- Si tu glisses le chiffre **3** dans la fente, des engrenages tournent, et le tiroir éjecte le nombre **11**.
- Si tu glisses **5**, la machine éjecte **17**.
- Si tu glisses **0**, elle éjecte **2**.
- Si tu glisses **$-4$**, elle éjecte **$-10$**.

```
                         [ Entrée : x ]
                               │
                               ▼
                      ┌─────────────────┐
                      │    MACHINE f    │
                      │   « Multiplie   │
                      │    par 3 et     │
                      │    ajoute 2 »   │
                      └─────────────────┘
                               │
                               ▼
                         [ Sortie : f(x) ]
```

Les enfants du village se rassemblent : *« Quelle est la formule secrète cachée dans les rouages de la boîte ? »*
Regarde bien :
- $3 \times 3 + 2 = 9 + 2 = 11$.
- $5 \times 3 + 2 = 15 + 2 = 17$.
- $0 \times 3 + 2 = 2$.
- $(-4) \times 3 + 2 = -12 + 2 = -10$.

La règle universelle est démasquée : quel que soit le nombre $x$ jeté dans la boîte, celle-ci calcule $3x + 2$.

Juste à côté de l'atelier, le **loueur de barques** affiche ses conditions pour traverser le lac :
*« Pour monter à bord, chaque passager paie 10 € de droit fixe d'embarquement (gilet de sauvetage et assurance). Ensuite, chaque heure passée sur l'eau coûte 15 €. »*

Combien paiera une famille qui loue une barque pendant 1 heure ? 2 heures ? 4 heures ?
- Pour 1 h : $10 + 15 \times 1 = 25$ €.
- Pour 2 h : $10 + 15 \times 2 = 40$ €.
- Pour 4 h : $10 + 15 \times 4 = 70$ €.
- Pour $x$ heures : le tarif total est $T(x) = 15x + 10$.

Ces deux situations ne sont pas des équations où l'on cherche un $x$ unique. Ce sont des **règles vivantes de correspondance**, des liens de dépendance continue entre deux grandeurs. C'est l'essence même du concept de **fonction**, la colonne vertébrale des mathématiques modernes et de toutes les sciences de la nature.

---

### 2. Le concept de fonction et son vocabulaire

#### 2.1 Qu'est-ce qu'une fonction ?

> **📐 Définition — Fonction.**
> Une **fonction** est un procédé mathématique qui, à un nombre de départ (la variable), associe **un seul et unique** nombre d'arrivée (le résultat).

On donne souvent un petit nom à cette fonction : une lettre minuscule comme $f$, $g$, ou $h$ (pour « fonction »), ou une majuscule parlante comme $T$ (pour « Tarif ») ou $V$ (pour « Volume »).

#### 2.2 Antécédent et Image : ne jamais les confondre !

C'est le vocabulaire officiel que tu utiliseras jusqu'au Baccalauréat. Pour ne jamais les mélanger, retiens cette métaphore du miroir ou de la photographie :

```
      AVANT (Point de départ)  ──────>  APRÈS (Résultat visible)
           x : ANTÉCÉDENT               f(x) : IMAGE
       « Celui qui s'est posé           « Le portrait qui sort
          devant l'appareil »               de la machine »
```

- **L'antécédent** (du latin *antecedere*, « venir avant ») : c'est le nombre qu'on met **en entrée** dans la machine. C'est le $x$.
- **L'image** : c'est le résultat calculé qui sort **à l'arrivée**. C'est le $f(x)$.

> **⚠️ Attention capitale !**
> - Un antécédent possède **une seule et unique image** (la machine ne peut pas donner deux résultats contradictoires pour un même bouton pressé).
> - En revanche, une même image peut avoir **plusieurs antécédents différents** !
>   *Exemple :* Si la machine élève au carré ($f(x) = x^2$), l'image $9$ possède **deux antécédents** : $3$ (car $3^2 = 9$) et $-3$ (car $(-3)^2 = 9$).

#### 2.3 Les notations : comment écrire et comment lire

| Notation écrite | Prononciation à voix haute | Rôle exact |
|---|---|---|
| $f$ | « la fonction $f$ » | C'est le nom de la machine tout entière (l'outil). |
| $f(x)$ | « $f$ de $x$ » | C'est le **nombre d'arrivée** associé au nombre $x$. |
| $x \mapsto f(x)$ | « à $x$ on associe $f$ de $x$ » | C'est la flèche de processus (remarque le petit talon vertical au départ de la flèche $\mapsto$). |

*Exemple concret :*
Soit la fonction $g(x) = 2x - 5$.
- Calculons l'image de $4$ :
  On remplace $x$ par 4 : $g(4) = 2 \times 4 - 5 = 8 - 5 = 3$.
  On dit : « L'image de $4$ par la fonction $g$ est $3$ », ou « $4$ est un antécédent de $3$ par $g$ ».
- Cherchons l'antécédent de $11$ :
  On cherche la valeur de $x$ telle que $g(x) = 11$. C'est une équation !
  $$2x - 5 = 11 \implies 2x = 16 \implies x = 8.$$
  L'antécédent de $11$ par $g$ est $8$.

---

### 3. Les trois visages d'une même fonction

Une fonction est un être abstrait. Pour la voir et travailler avec elle, les mathématiciens disposent de trois représentations complémentaires :

```
             ┌───────────────────────────────┐
             │ 1. L'expression algébrique    │
             │    (La formule exacte)        │
             │    f(x) = 2x + 1              │
             └──────────────┬────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
 ┌──────────────────────┐        ┌──────────────────────┐
 │ 2. Le tableau        │        │ 3. La courbe         │
 │    de valeurs        │        │    représentative    │
 │ (Échantillons finis) │        │ (Vision géométrique  │
 │                      │        │     continue)        │
 └──────────────────────┘        └──────────────────────┘
```

#### 3.1 Le tableau de valeurs
On choisit quelques nombres pour $x$ sur la première ligne, et on calcule leur image $f(x)$ sur la seconde :

| $x$ (antécédents) | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|
| $f(x) = 2x + 1$ (images) | $-3$ | $-1$ | $1$ | $3$ | $5$ | $7$ |

Chaque colonne du tableau fournit les coordonnées d'un point : $(-2 ; -3)$, $(-1 ; -1)$, $(0 ; 1)$, $(1 ; 3)$, etc.

#### 3.2 La courbe représentative dans un repère
On place ces points dans un repère cartésien $(O ; I, J)$ :
- L'axe horizontal (l'axe des abscisses) porte les **antécédents $x$**.
- L'axe vertical (l'axe des ordonnées) porte les **images $y = f(x)$**.

> **📐 Définition — Courbe représentative.**
> La courbe représentative d'une fonction $f$ (notée $\mathcal{C}_f$) est l'ensemble de tous les points de coordonnées $(x \; ; \; f(x))$ du plan.

---

### 4. La fonction linéaire : la pure proportionnalité $f(x) = ax$

#### 4.1 Définition et sens concret

Une **fonction linéaire** est la plus simple et la plus noble des fonctions : c'est la traduction en langage algébrique d'une **situation de proportionnalité parfaite** (que tu as étudiée au Chapitre 13).

> **📐 Définition — Fonction linéaire.**
> Une fonction linéaire est une fonction définie par une formule de la forme :
> $$f(x) = ax$$
> où $a$ est un nombre fixe donné, appelé **coefficient de proportionnalité** (ou coefficient directeur).

*Exemples :*
- Acheter des cerises à 4 € le kilo : $P(x) = 4x$ ($a = 4$).
- Rouler à bicyclette à la vitesse constante de 20 km/h : distance $d(t) = 20t$ ($a = 20$).
- Une réduction de 30 % : le nouveau prix est $N(x) = (1 - 0{,}30)x = 0{,}7x$ ($a = 0{,}7$).

#### 4.2 Représentation graphique : la droite qui passe par l'origine

Si tu traces les points d'une fonction linéaire dans un repère, tu constates un miracle géométrique : **tous les points sont rigoureusement alignés avec l'origine du repère $O(0, 0)$** !

Pourquoi ? Parce que si tu n'achètes rien ($x = 0$), tu ne paies rien ($f(0) = a \times 0 = 0$).

```
             y ▲                    f(x) = 2x
               │                   /
             4 ┼                  /
               │                 /|
             2 ┼                * |
               │               /| |
             0 ┼──────────────*─┼─┼───────> x
                              0 1 2
                   Passe par l'origine O(0,0) !
```

> **📐 Théorème graphique —**
> La représentation graphique d'une fonction linéaire $f(x) = ax$ est **une droite qui passe par l'origine du repère $O(0, 0)$**.
> Réciproquement, toute droite non verticale qui passe par l'origine représente une fonction linéaire.

Pour tracer la droite d'une fonction linéaire, il suffit donc de calculer **un seul point supplémentaire** en plus de l'origine $(0 ; 0)$ !

---

### 5. La fonction affine : la droite générale du tarif $f(x) = ax + b$

#### 5.1 Définition : proportionnalité avec abonnement

Que se passe-t-il quand une situation comporte un prix fixe de départ (un forfait, une prise en charge, une caution) auquel s'ajoute un tarif proportionnel ? Ce n'est plus une proportionnalité pure, mais c'est une **fonction affine**.

> **📐 Définition — Fonction affine.**
> Une fonction affine est une fonction définie pour tout nombre réel $x$ par :
> $$f(x) = ax + b$$
> où $a$ et $b$ sont deux nombres fixés.
> - Le nombre $a$ s'appelle le **coefficient directeur** (ou pente de la droite).
> - Le nombre $b$ s'appelle l'**ordonnée à l'origine**.

#### 5.2 Pourquoi ce vocabulaire ?
1. **L'ordonnée à l'origine ($b$) :**
   Calculons l'image de 0 :
   $$f(0) = a \times 0 + b = 0 + b = b.$$
   Le point de la droite correspondant à $x = 0$ a pour coordonnées $(0 \; ; \; b)$. C'est très exactement l'endroit où la droite **traverse l'axe des ordonnées** (vertical) !
2. **Le coefficient directeur ($a$) :**
   Il dicte la « direction » et l'inclinaison de la droite :
   - Si $a > 0$, la fonction est **croissante** (la droite monte quand on va de gauche à droite).
   - Si $a < 0$, la fonction est **décroissante** (la droite descend).
   - Plus $|a|$ est grand, plus la droite est raide (pente forte). Plus $|a|$ est proche de 0, plus la droite est plate.

```
       y ▲               (a > 0 : Monte)       y ▲
         │                 /                     │ \
         │                /                      │  \
       b ┼───────────────*                     b ┼───*──────────── (a < 0 : Descend)
         │              /                        │    \
         │             /                         │     \
       0 ┼────────────┼──────────> x           0 ┼──────┼─────────> x
                      0                                 0
```

#### 5.3 Les cas particuliers remarquables
- Si $b = 0$, la formule devient $f(x) = ax$ : une fonction linéaire est simplement une **fonction affine particulière** qui démarre à $b = 0$.
- Si $a = 0$, la formule devient $f(x) = b$ : c'est une **fonction constante**. L'image vaut toujours $b$, quelle que soit la valeur de $x$. Sa représentation graphique est une **droite horizontale**.

---

### 6. L'art de tracer et de lire graphiquement

#### 6.1 L'escalier magique : « J'avance de 1, je monte de $a$ »

Pour tracer la droite d'équation $y = ax + b$ sans faire de tableau de calculs interminable, utilise la règle des marches d'escalier :

1. Place d'abord le point de départ sur l'axe vertical : le point $(0 \; ; \; b)$.
2. Depuis ce point, **avance horizontalement de 1 unité vers la droite**.
3. Puis :
   - Si $a$ est positif : **monte verticalement de $a$ unités**.
   - Si $a$ est négatif : **descends verticalement de $|a|$ unités**.
4. Tu obtiens un deuxième point. Pose ta règle entre les deux points : la droite est tracée !

```
              y ▲
                │
              4 ┼                 ● Nouveau point (1 ; 4)
                │                 ▲
                │                 │ Monte de a = 2
              2 ┼────●────────────┤
                │  (0 ; b)   Avance de 1
                │  (b = 2)
              0 ┼─────────────────┼───────> x
                0                 1
```

#### 6.2 Comment calculer le coefficient directeur $a$ à partir de deux points ?

Si une droite passe par deux points connus $A(x_A \; ; \; y_A)$ et $B(x_B \; ; \; y_B)$ (avec $x_A \neq x_B$), son coefficient directeur se calcule par le rapport fondamental :

$$a = \frac{\text{Variation verticale}}{\text{Variation horizontale}} = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x}.$$

Le symbole $\Delta$ (la lettre grecque « Delta » majuscule) signifie « différence » ou « variation ».
Cette formule affirme que la pente est le nombre d'unités dont on grimpe verticalement pour chaque unité franchie vers la droite.

---

### 7. L'histoire vraie : le thermomètre de Gabriel Fahrenheit et René de Réaumur

Au XVIIIᵉ siècle, les savants européens cherchent à mesurer précisément la chaleur.
En 1724, le physicien allemand Gabriel Fahrenheit invente le premier thermomètre à mercure fiable. Il fixe :
- $0^\circ\text{F}$ : la température la plus glaciale qu'il parvient à créer dans son laboratoire avec un mélange d'eau, de glace et de sel d'ammoniaque.
- $96^\circ\text{F}$ : la température du corps humain vivant (ajustée plus tard à $98{,}6^\circ\text{F}$).
Dans son échelle, l'eau gèle à $32^\circ\text{F}$ et bout à $212^\circ\text{F}$.

En 1742, l'astronome suédois Anders Celsius propose une échelle plus rationnelle basée sur l'eau pure :
- $0^\circ\text{C}$ pour la glace fondante.
- $100^\circ\text{C}$ pour l'ébullition de l'eau.

Comment passer instantanément de la température Celsius ($x$) à la température Fahrenheit ($f(x)$) ?
C'est exactement une **fonction affine** !
- Le point de congélation donne le point $A(0 \; ; \; 32)$.
- Le point d'ébullition donne le point $B(100 \; ; \; 212)$.

Calculons la pente $a$ et l'ordonnée à l'origine $b$ :
1. Puisque $x = 0$ donne $y = 32$, l'ordonnée à l'origine est immédiatement :
   $$b = 32.$$
2. Le coefficient directeur est :
   $$a = \frac{y_B - y_A}{x_B - x_A} = \frac{212 - 32}{100 - 0} = \frac{180}{100} = \frac{9}{5} = 1{,}8.$$

La formule universelle reliant les deux mondes est donc :
$$f(x) = 1{,}8x + 32 \quad \text{ou} \quad T_{\text{Fahrenheit}} = \frac{9}{5} T_{\text{Celsius}} + 32.$$

Quand il fait $20^\circ\text{C}$ dans ta chambre, un Américain lit sur son thermomètre :
$$f(20) = 1{,}8 \times 20 + 32 = 36 + 32 = 68^\circ\text{F} !$$

---

### 8. Exemples résolus pas à pas

#### Exemple 1 : Calculs d'images et d'antécédents
On considère la fonction affine $f$ définie par :
$$f(x) = -3x + 7.$$
1. Calculer l'image de $4$ et l'image de $-2$.
2. Déterminer l'antécédent de $-11$.
3. Déterminer l'antécédent de $0$.

**Résolution détaillée :**
1. Pour calculer une image, on injecte la valeur à la place de $x$ :
   - $f(4) = -3 \times 4 + 7 = -12 + 7 = -5$. L'image de $4$ est $-5$.
   - $f(-2) = -3 \times (-2) + 7 = +6 + 7 = 13$. L'image de $-2$ est $13$.
2. Chercher l'antécédent de $-11$, c'est trouver la valeur de $x$ qui vérifie $f(x) = -11$ :
   $$-3x + 7 = -11$$
   $$-3x = -11 - 7 = -18$$
   $$x = \frac{-18}{-3} = 6.$$
   L'antécédent de $-11$ par $f$ est $6$.
3. Pour l'antécédent de 0 :
   $$-3x + 7 = 0 \implies -3x = -7 \implies x = \frac{-7}{-3} = \frac{7}{3}.$$
   L'antécédent de $0$ est la fraction irréductible $\frac{7}{3}$.

---

#### Exemple 2 : Trouver l'expression d'une fonction affine passant par deux points
Une droite passe par les points $A(2 \; ; \; 5)$ et $B(6 \; ; \; 17)$.
Déterminer la formule de la fonction affine $f(x) = ax + b$ dont cette droite est la représentation graphique.

**Résolution détaillée :**
1. **Calcul du coefficient directeur $a$ :**
   $$a = \frac{y_B - y_A}{x_B - x_A} = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3.$$
   La formule est donc déjà de la forme $f(x) = 3x + b$.
2. **Calcul de l'ordonnée à l'origine $b$ :**
   Puisque le point $A(2 \; ; \; 5)$ appartient à la droite, on a $f(2) = 5$ :
   $$3 \times 2 + b = 5$$
   $$6 + b = 5 \implies b = 5 - 6 = -1.$$
3. **Conclusion :**
   La fonction affine cherchée est :
   $$f(x) = 3x - 1.$$
   *(Vérification immédiate avec le point B : $f(6) = 3 \times 6 - 1 = 18 - 1 = 17$. Parfait !)*

---

#### Exemple 3 : Déterminer $a$ et $b$ par lecture graphique
Sur un graphique fourni, une droite $(d)$ coupe l'axe vertical au point d'ordonnée $-3$.
Lorsqu'on avance de $2$ carreaux vers la droite, on doit monter de $5$ carreaux pour retomber exactement sur la droite.
1. Donner l'ordonnée à l'origine $b$.
2. Donner le coefficient directeur $a$.
3. En déduire la formule de la fonction associée.

**Résolution détaillée :**
1. La droite coupe l'axe vertical en $-3$, donc l'ordonnée à l'origine est immédiatement :
   $$b = -3.$$
2. Avancer de 2 en montant de 5 signifie :
   $$\Delta x = +2 \quad \text{et} \quad \Delta y = +5.$$
   Le coefficient directeur est :
   $$a = \frac{\Delta y}{\Delta x} = \frac{5}{2} = 2{,}5.$$
3. L'expression de la fonction est :
   $$f(x) = 2{,}5x - 3 \quad \left(\text{ou } f(x) = \frac{5}{2}x - 3\right).$$

---

#### Exemple 4 : Problème de forfait de téléphone portable
Un opérateur propose deux abonnements mobiles :
- **Forfait Éco :** 0,10 € la minute d'appel, sans aucun abonnement fixe mensuel.
- **Forfait Sérénité :** un abonnement mensuel fixe de 12 €, plus 0,02 € par minute d'appel.
1. Exprimer les fonctions $E(x)$ et $S(x)$ associées à ces deux forfaits pour une durée de $x$ minutes par mois.
2. Déterminer la nature de chacune de ces deux fonctions.
3. Calculer le montant de la facture pour 60 minutes de communication avec chaque forfait.
4. À partir de combien de minutes par mois le Forfait Sérénité devient-il plus rentable que le Forfait Éco ?

**Résolution détaillée :**
1. Pour $x$ minutes de communication :
   - $E(x) = 0{,}10x$.
   - $S(x) = 0{,}02x + 12$.
2. $E$ est une **fonction linéaire** (situation de proportionnalité pure, droite passant par l'origine).
   $S$ est une **fonction affine** non linéaire (présence d'un terme constant $b = 12$).
3. Pour 60 minutes :
   - $E(60) = 0{,}10 \times 60 = 6$ €.
   - $S(60) = 0{,}02 \times 60 + 12 = 1{,}20 + 12 = 13{,}20$ €.
4. Sérénité est plus avantageux si sa facture est inférieure à celle d'Éco :
   $$S(x) < E(x) \iff 0{,}02x + 12 < 0{,}10x$$
   $$12 < 0{,}10x - 0{,}02x \implies 12 < 0{,}08x \implies x > \frac{12}{0{,}08} = 150.$$
   Conclusion : Le Forfait Sérénité devient plus rentable dès que l'on téléphone **plus de 150 minutes (soit 2 h 30) par mois**.

---

#### Exemple 5 : Vitesse, distance et fonction affine
Une citerne d'eau contient 800 litres. À 8 h 00 du matin, on ouvre une vanne de vidange : l'eau s'écoule à un débit régulier et constant de 25 litres par minute.
1. Exprimer le volume d'eau $V(t)$ (en litres) restant dans la citerne en fonction du temps $t$ écoulé (en minutes).
2. Quelle est la nature de la fonction $V$ ? Quel est le signe de son coefficient directeur ?
3. Combien d'eau reste-t-il au bout de 12 minutes ?
4. Au bout de combien de temps la citerne sera-t-elle complètement vide ?

**Résolution détaillée :**
1. Au départ ($t = 0$), il y a 800 L. Chaque minute, on perd 25 L.
   Le volume restant est :
   $$V(t) = 800 - 25t = -25t + 800.$$
2. $V$ est une **fonction affine** avec $a = -25$ et $b = 800$.
   Son coefficient directeur est **négatif** ($a = -25 < 0$) : la fonction est donc **décroissante** (le volume diminue au cours du temps).
3. Pour $t = 12$ min :
   $$V(12) = -25 \times 12 + 800 = -300 + 800 = 500 \text{ litres}.$$
4. La citerne est vide lorsque le volume restant atteint 0 :
   $$V(t) = 0 \iff -25t + 800 = 0 \iff 25t = 800 \iff t = \frac{800}{25} = 32 \text{ minutes}.$$
   La citerne sera entièrement vidée à 8 h 32.

---

### Ce qu'il faut retenir

1. **Vocabulaire fondamental :**
   - $x$ est l'**antécédent** (nombre d'entrée).
   - $f(x)$ est l'**image** de $x$ par $f$ (nombre de sortie).
   - La notation $f : x \mapsto f(x)$ se lit « la fonction $f$ qui à $x$ associe $f(x)$ ».
2. **Fonction linéaire : $f(x) = ax$**
   - Représente une situation de **proportionnalité**.
   - Sa courbe est une **droite qui passe obligatoirement par l'origine $O(0, 0)$**.
3. **Fonction affine : $f(x) = ax + b$**
   - Sa courbe est une **droite** qui coupe l'axe vertical au point $(0 \; ; \; b)$.
   - $b$ est l'**ordonnée à l'origine** : $f(0) = b$.
   - $a$ est le **coefficient directeur** (la pente) :
     $$a = \frac{y_B - y_A}{x_B - x_A}.$$
     Si $a > 0$, la droite monte. Si $a < 0$, la droite descend. Si $a = 0$, la droite est horizontale (fonction constante).
4. **Lecture graphique d'une droite :**
   - Pour trouver l'image d'un nombre : on part de l'abscisse sur l'axe horizontal, on rejoint la droite verticalement, et on lit l'ordonnée sur l'axe vertical.
   - Pour trouver l'antécédent : on part de l'ordonnée sur l'axe vertical, on rejoint la droite horizontalement, et on lit l'abscisse sur l'axe horizontal.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 25.1** Vocabulaire et notations :
Soit une fonction $h$ telle que $h(3) = 7$.
1. Quelle est l'image de 3 par $h$ ?
2. Quel est un antécédent de 7 par $h$ ?
3. Traduire par une égalité de la forme $f(a) = b$ la phrase : « L'image de $-5$ par la fonction $f$ est $12$ ».
4. Traduire par une égalité la phrase : « $-2$ est un antécédent de $9$ par la fonction $g$ ».

**Exercice 25.2** Calculs d'images :
On considère la fonction affine $f(x) = 4x - 5$.
Calculer :
1. $f(0)$
2. $f(3)$
3. $f(-2)$
4. $f\left(\frac{1}{2}\right)$

**Exercice 25.3** Calculs d'antécédents :
Avec la même fonction $f(x) = 4x - 5$, déterminer l'antécédent de :
1. $15$
2. $-5$
3. $0$
4. $-13$

**Exercice 25.4** Identification de la nature d'une fonction :
Indiquer pour chaque fonction si elle est linéaire, affine non linéaire, ou ni l'une ni l'autre :
1. $f(x) = 5x$
2. $g(x) = 3x - 8$
3. $h(x) = x^2 + 1$
4. $k(x) = 7$
5. $m(x) = \frac{4}{x}$
6. $p(x) = \frac{x}{5} + 2$

**Exercice 25.5** Tracé de droites :
Dans un repère, tracer les représentations graphiques des fonctions suivantes :
1. $d_1 : f(x) = 2x$
2. $d_2 : g(x) = -x$
3. $d_3 : h(x) = 2x - 3$
4. $d_4 : k(x) = -0{,}5x + 2$

---

#### Niveau ★★ : Réflexion et enchaînements

**Exercice 25.6** Détermination de formule à partir de points :
1. Une fonction linéaire $g$ vérifie $g(4) = 14$. Déterminer l'expression de $g(x)$.
2. Une fonction affine $f$ passe par les points $A(1 \; ; \; 4)$ et $B(3 \; ; \; 10)$. Calculer son coefficient directeur $a$, son ordonnée à l'origine $b$, et en déduire $f(x)$.

**Exercice 25.7** Lecture graphique inversée :
On observe une droite représentant une fonction affine $f$.
La droite coupe l'axe des ordonnées en $(0 \; ; \; 4)$ et passe par le point $(4 \; ; \; 0)$.
1. Déterminer la valeur de $b$.
2. Calculer la pente $a$.
3. Écrire la formule de $f(x)$.
4. Quel est le sens de variation de la fonction $f$ ?

**Exercice 25.8** Le taxi de nuit :
Un chauffeur de taxi applique la tarification suivante :
- Prise en charge initiale dès l'allumage du compteur : 4,20 €.
- Prix du kilomètre parcouru : 1,60 €.
1. Écrire le montant de la course $C(x)$ pour une distance de $x$ kilomètres.
2. Combien coûte un trajet de 15 km ?
3. Un voyageur dispose d'un billet de 25 €. Quelle distance maximale peut-il parcourir ?

**Exercice 25.9** Point sur une droite (appartenance) :
Soit la fonction affine $f(x) = -2x + 7$.
1. Le point $M(3 \; ; \; 1)$ appartient-il à la droite représentative de $f$ ?
2. Le point $N(-4 \; ; \; 15)$ appartient-il à cette droite ?
3. Trouver l'abscisse du point $P$ de la droite qui a pour ordonnée $-9$.

**Exercice 25.10** Intersection de deux fonctions affines :
Soit les fonctions $f(x) = 2x - 1$ et $g(x) = -x + 5$.
1. Tracer les deux droites dans un repère.
2. Déterminer graphiquement les coordonnées de leur point d'intersection $I$.
3. Retrouver ces coordonnées par le calcul en résolvant l'équation $f(x) = g(x)$.

**Exercice 25.11** La bougie qui fond :
Une bougie mesure 24 cm de haut. Lorsqu'on l'allume, sa hauteur diminue de 1,5 cm par heure de combustion.
1. Exprimer la hauteur $h(t)$ de la bougie en centimètres après $t$ heures de combustion.
2. Quelle est la hauteur de la bougie après 6 heures ?
3. Au bout de combien d'heures la bougie sera-t-elle complètement consumée ?

---

#### Niveau ★★★ : Défis et recherche

**Exercice 25.12** Alignement de trois points :
On donne trois points dans un repère : $A(-2 \; ; \; -7)$, $B(2 \; ; \; 5)$ et $C(5 \; ; \; 14)$.
1. Déterminer la fonction affine $f$ dont la droite passe par $A$ et $B$.
2. Le point $C$ est-il aligné avec $A$ et $B$ ? (Indication : tester si $f(5) = 14$).

**Exercice 25.13** Parallélisme et droites :
On donne la droite $(d_1)$ représentant $f(x) = 3x - 4$.
On cherche une droite $(d_2)$ qui est **parallèle** à $(d_1)$ et qui passe par le point $E(2 \; ; \; 9)$.
1. Que peut-on dire du coefficient directeur de $(d_2)$ par rapport à celui de $(d_1)$ ?
2. En déduire la formule de la fonction affine $g$ associée à $(d_2)$.

**Exercice 25.14** Le mystère de la boîte à double saut :
Une fonction affine inconnue $f(x) = ax + b$ possède cette curieuse propriété :
Lorsqu'on l'applique deux fois de suite, c'est-à-dire en calculant $f(f(x))$, on obtient toujours le résultat $4x + 9$ !
1. Développer l'expression littérale $f(f(x)) = a(ax + b) + b$.
2. En identifiant les coefficients avec $4x + 9$, trouver les deux valeurs possibles pour $a$.
3. En déduire les deux fonctions affines solutions de cette énigme.

---

### Solutions

#### Niveau ★

**Solution 25.1**
1. L'image de 3 est 7.
2. Un antécédent de 7 est 3.
3. $f(-5) = 12$.
4. $g(-2) = 9$.

**Solution 25.2**
1. $f(0) = 4(0) - 5 = -5$.
2. $f(3) = 4(3) - 5 = 12 - 5 = 7$.
3. $f(-2) = 4(-2) - 5 = -8 - 5 = -13$.
4. $f\left(\frac{1}{2}\right) = 4 \times \frac{1}{2} - 5 = 2 - 5 = -3$.

**Solution 25.3**
1. $4x - 5 = 15 \implies 4x = 20 \implies x = 5$.
2. $4x - 5 = -5 \implies 4x = 0 \implies x = 0$.
3. $4x - 5 = 0 \implies 4x = 5 \implies x = \frac{5}{4} = 1{,}25$.
4. $4x - 5 = -13 \implies 4x = -8 \implies x = -2$.

**Solution 25.4**
1. $f(x) = 5x$ : linéaire (et affine avec $b = 0$).
2. $g(x) = 3x - 8$ : affine non linéaire ($a = 3, b = -8$).
3. $h(x) = x^2 + 1$ : ni l'une ni l'autre (présence de $x^2$, fonction non affine).
4. $k(x) = 7$ : constante (affine avec $a = 0, b = 7$).
5. $m(x) = \frac{4}{x}$ : ni l'une ni l'autre (fonction inverse, $x$ au dénominateur).
6. $p(x) = \frac{1}{5}x + 2$ : affine ($a = 0{,}2, b = 2$).

**Solution 25.5**
1. $d_1$ passe par $(0 ; 0)$ et $(1 ; 2)$.
2. $d_2$ passe par $(0 ; 0)$ et $(1 ; -1)$.
3. $d_3$ passe par $(0 ; -3)$ et $(1 ; -1)$ (ou $(2 ; 1)$).
4. $d_4$ passe par $(0 ; 2)$ et $(2 ; 1)$ (ou $(4 ; 0)$).

---

#### Niveau ★★

**Solution 25.6**
1. $g(x) = ax$. Puisque $g(4) = 14$, on a $4a = 14 \implies a = \frac{14}{4} = 3{,}5$. Donc $g(x) = 3{,}5x$.
2. $a = \frac{y_B - y_A}{x_B - x_A} = \frac{10 - 4}{3 - 1} = \frac{6}{2} = 3$.
   Donc $f(x) = 3x + b$.
   En utilisant $A(1 ; 4)$ : $3(1) + b = 4 \implies b = 1$.
   D'où $f(x) = 3x + 1$.

**Solution 25.7**
1. La droite coupe l'axe vertical en $(0 ; 4)$, donc $b = 4$.
2. Elle passe par $(4 ; 0)$. Donc $a = \frac{0 - 4}{4 - 0} = \frac{-4}{4} = -1$.
3. $f(x) = -x + 4$.
4. Puisque $a = -1 < 0$, la fonction est **strictement décroissante** (la droite descend).

**Solution 25.8**
1. $C(x) = 1{,}60x + 4{,}20$.
2. Pour 15 km : $C(15) = 1{,}60 \times 15 + 4{,}20 = 24 + 4{,}20 = 28{,}20$ €.
3. Avec 25 € : $1{,}60x + 4{,}20 \le 25 \implies 1{,}60x \le 20{,}80 \implies x \le \frac{20{,}80}{1{,}60} = 13$ km.
   Il peut parcourir au maximum 13 km.

**Solution 25.9**
1. Calculons $f(3)$ : $f(3) = -2(3) + 7 = -6 + 7 = 1$. L'ordonnée vaut bien 1, donc le point $M(3 \; ; \; 1)$ appartient bien à la droite.
2. Calculons $f(-4)$ : $f(-4) = -2(-4) + 7 = 8 + 7 = 15$. Oui, $N(-4 \; ; \; 15)$ appartient aussi à la droite.
3. On cherche $x$ tel que $f(x) = -9$ : $-2x + 7 = -9 \implies -2x = -16 \implies x = 8$. L'abscisse de $P$ est 8.

**Solution 25.10**
1. Les droites se tracent facilement : $f$ passe par $(0 ; -1)$ et $(2 ; 3)$ ; $g$ passe par $(0 ; 5)$ et $(2 ; 3)$.
2. Graphiquement, le point d'intersection est $I(2 \; ; \; 3)$.
3. Par le calcul :
   $$f(x) = g(x) \iff 2x - 1 = -x + 5 \iff 3x = 6 \iff x = 2.$$
   Puis $f(2) = 2(2) - 1 = 3$. Le point d'intersection est bien $I(2 \; ; \; 3)$.

**Solution 25.11**
1. $h(t) = -1{,}5t + 24$.
2. Après 6 heures : $h(6) = -1{,}5 \times 6 + 24 = -9 + 24 = 15 \text{ cm}$.
3. Bougie consumée : $h(t) = 0 \iff -1{,}5t + 24 = 0 \iff 1{,}5t = 24 \iff t = \frac{24}{1{,}5} = 16 \text{ heures}$.

---

#### Niveau ★★★

**Solution 25.12**
1. Calculons la droite passant par $A(-2 ; -7)$ et $B(2 ; 5)$ :
   $a = \frac{5 - (-7)}{2 - (-2)} = \frac{12}{4} = 3$.
   $f(x) = 3x + b$. Avec $B(2 ; 5)$ : $3(2) + b = 5 \implies 6 + b = 5 \implies b = -1$.
   Donc $f(x) = 3x - 1$.
2. Testons si $C(5 ; 14)$ appartient à cette droite :
   $f(5) = 3(5) - 1 = 15 - 1 = 14$.
   L'égalité est parfaitement vérifiée : le point $C$ est donc **aligné** avec les points $A$ et $B$ !

**Solution 25.13**
1. Deux droites sont parallèles si et seulement si elles possèdent le **même coefficient directeur** (la même inclinaison). Donc pour $(d_2)$, on a aussi $a = 3$.
2. La fonction $g$ s'écrit $g(x) = 3x + b$.
   Elle passe par $E(2 ; 9)$, donc $g(2) = 9$ :
   $$3(2) + b = 9 \implies 6 + b = 9 \implies b = 3.$$
   La formule est : $g(x) = 3x + 3$.

**Solution 25.14**
1. On applique $f$ au résultat $f(x) = ax + b$ :
   $$f(f(x)) = a(ax + b) + b = a^2x + ab + b = a^2x + b(a + 1).$$
2. On veut que cette formule soit égale à $4x + 9$ pour tout $x$ :
   - Pour le terme en $x$ : $a^2 = 4 \implies a = 2$ ou $a = -2$.
   - Pour le terme constant : $b(a + 1) = 9$.
3. Deux cas se présentent :
   - Premier cas : si $a = 2$, alors $b(2 + 1) = 9 \implies 3b = 9 \implies b = 3$.
     La première fonction est : $f_1(x) = 2x + 3$.
     *(Vérification : $f_1(f_1(x)) = 2(2x + 3) + 3 = 4x + 6 + 3 = 4x + 9$ !)*
   - Deuxième cas : si $a = -2$, alors $b(-2 + 1) = 9 \implies b(-1) = 9 \implies b = -9$.
     La deuxième fonction est : $f_2(x) = -2x - 9$.
     *(Vérification : $f_2(f_2(x)) = -2(-2x - 9) - 9 = 4x + 18 - 9 = 4x + 9$ !)*

---

### La question qui ouvre la suite

Jusqu'ici, les nombres nous ont servi à calculer des poids, des prix, des aires et des trajectoires droites. Mais regarde autour de toi : un motif de tissu qui se répète, les tuiles d'un toit, une fleur à six pétales, les mosaïques infinies de l'Alhambra de Grenade ou l'art vertigineux de Maurits Cornelis Escher. 

Comment un même triangle ou une même figure peut-il **glisser**, **pivoter**, se **refléter dans un miroir** ou **grossir comme sous une loupe** tout en conservant scrupuleusement sa forme ? C'est le monde enchanteur des transformations du plan que nous allons explorer dans le chapitre 26 : **Le Pliage de Papier et le Miroir Magique**.
