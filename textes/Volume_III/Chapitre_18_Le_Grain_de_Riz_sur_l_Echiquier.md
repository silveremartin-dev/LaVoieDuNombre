# VOLUME III — L'ÂGE DES ARPENTEURS ET DES BÂTISSEURS (10 - 13 ans / CM2 - 6e - 5e)
## CHAPITRE 18 : Le Grain de Riz sur l'Échiquier

> *« L'addition est le pas lent du marcheur qui avance pierre par pierre. La multiplication est la course du cavalier. Mais la puissance est l'envol fulgurant de la fusée : en quelques battements d'ailes, elle dépasse l'entendement des rois et emplit l'univers tout entier. »*

---

### Ce que tu vas découvrir

- La légende indienne du sage **Sissa** et l'avalanche de grains de riz sur l'échiquier.
- L'**ordre universel des opérations** (PEMDAS) : pourquoi sans règles du jeu, aucun calcul ne donnerait le même résultat.
- La notation **puissance** : comment écrire en un minuscule exposant des multiplications géantes ($a^n$).
- Les secrets des **puissances de 10** et les puissances à **exposants négatifs** ($10^{-n} = \frac{1}{10^n}$).
- Les quatre règles d'or pour multiplier, diviser et élever des puissances sans jamais s'emmêler.
- La **notation scientifique** et l'exploration des grandeurs, depuis le cœur de l'atome jusqu'aux confins des galaxies.

---

### 1. Le problème : la promesse imprudente du roi Belkib

Il y a plus de mille cinq cents ans, dans un somptueux palais du nord de l'Inde, vivait un roi puissant nommé Belkib (ou Shirham). Malgré toutes ses richesses, le monarque s'ennuyait profondément. Aucun spectacle de danse, aucun tournoi de cavalerie ne parvenait à chasser sa mélancolie.

Un jour, un sage de sa cour nommé **Sissa** se présenta devant le trône avec un coffret en bois d'ébène. Il en sortit un plateau de 64 cases carrées alternant le blanc et le noir, ainsi que deux armées de pièces sculptées : rois, cavaliers, tours et pions. C'était le jeu des échecs (alors appelé le *Chaturanga*).

Le roi fut immédiatement fasciné. Pendant des semaines, il apprit à élaborer des stratégies, à protéger son roi et à sacrifier des pions. Guéri de sa tristesse, il convoqua Sissa devant toute la cour :
*« Sissa, ton invention est sublime ! Demande-moi la récompense que tu désires, fût-ce la moitié de mes coffres d'or ou le plus beau de mes palais, je te l'accorderai ! »*

Sissa s'inclina avec humilité :
*« Grand roi, je ne suis qu'un modeste chercheur. Je ne demande ni or ni pierres précieuses. Posez simplement votre plateau d'échecs devant vous :*
- *Posez **1 grain de riz** sur la première case.*
- *Posez **2 grains de riz** sur la deuxième case.*
- *Posez **4 grains de riz** sur la troisième case.*
- *Et doublez ainsi le nombre de grains sur chaque case suivante jusqu'à la soixante-quatrième case.*
*Donnez-moi simplement ces quelques grains de riz, et je serai comblé. »*

```
     1ère case      2e case        3e case        4e case        ...        64e case
        ┌───┐          ┌───┐          ┌───┐          ┌───┐                     ┌───┐
        │ • │          │•• │          │••••│         │••••│                    │ ? │
        └───┘          └───┘          └───┘          │••••│                    └───┘
       1 grain        2 grains       4 grains       8 grains                 2⁶³ grains !
```

Le roi éclata de rire :
*« Quelle folle modestie ! Tu aurais pu réclamer un trésor royal, et tu me demandes une poignée de soupe d'oiseau ! Qu'on apporte un sac de riz de mes greniers et qu'on paie cet homme sur-le-champ ! »*

Mais le soir même, le grand trésorier du royaume revint blême et tremblant devant le roi :
*« Majesté… nous avons vidé tous les greniers du palais, tous les silos de la capitale, et nous n'avons même pas pu remplir la trentième case ! Pour satisfaire la demande de Sissa, toutes les récoltes de la Terre entière pendant plus de deux mille ans ne suffiraient pas ! »*

Comment le simple fait de doubler une quantité 63 fois de suite peut-il produire une montagne plus vaste que la Terre ? C'est le pouvoir sidérant de **l'exponentielle et des puissances**.

---

### 2. Les priorités opératoires : qui commande dans un calcul ?

Avant de manipuler des puissances colossales, il nous faut une boussole. Regarde ce calcul d'une simplicité désarmante :

$$2 + 3 \times 5$$

Si tu le donnes à deux personnes différentes dans la rue :
- La première calcule de gauche à droite : $2 + 3 = 5$, puis $5 \times 5 = \mathbf{25}$.
- La deuxième calcule la multiplication d'abord : $3 \times 5 = 15$, puis $2 + 15 = \mathbf{17}$.

Qui a raison ? $25$ ou $17$ ?

Dans la nature, ce n'est pas une question d'opinion ! Imagine que tu ailles au marché. Tu achètes 1 pomme à 2 euros, et 3 sachets de bonbons à 5 euros l'unité. Combien paies-tu ?
Tu paies évidemment $2 + 15 = 17$ euros, et non pas 25 euros ! La multiplication groupe les objets en paquets inséparables.

Pour que tous les ingénieurs, scientifiques et ordinateurs du monde entier s'accordent sur le même résultat, les mathématiciens ont fixé un code de la route universel : **les priorités opératoires**.

#### 2.1 La règle PEMDAS

On retient cette hiérarchie grâce au mot magique **PEMDAS** (ou « Parenthèses d'abord ! ») :

```
                  ┌──────────────────────────────────────────┐
                  │ 1. P : PARENTHÈSES (les plus intérieures)│
                  ├──────────────────────────────────────────┤
                  │ 2. E : EXPOSANTS (les Puissances)        │
                  ├──────────────────────────────────────────┤
                  │ 3. M / D : MULTIPLICATIONS & DIVISIONS   │
                  │    (au même niveau, de gauche à droite)  │
                  ├──────────────────────────────────────────┤
                  │ 4. A / S : ADDITIONS & SOUSTRACTIONS     │
                  │    (au même niveau, de gauche à droite)  │
                  └──────────────────────────────────────────┘
```

> **📐 Règle officielle — Priorités de calcul**
> 1. On effectue en priorité les calculs situés **entre les parenthèses**, en commençant par les parenthèses les plus intérieures.
> 2. On calcule les **puissances** (exposants).
> 3. On effectue les **multiplications et les divisions**, de gauche à droite.
> 4. On effectue enfin les **additions et les soustractions**, de gauche à droite.

#### 2.2 Le rôle du trait de fraction

Un trait de fraction horizontal joue le rôle de parenthèses invisibles pour tout ce qui est au-dessus (numérateur) et tout ce qui est en dessous (dénominateur) :
$$\frac{8 + 12}{2 + 3} = \frac{(8 + 12)}{(2 + 3)} = \frac{20}{5} = 4$$

---

### 3. La notation puissance : l'art de compresser l'écriture

Reprenons l'échiquier de Sissa.
- Case 1 : $1$
- Case 2 : $2$
- Case 3 : $2 \times 2 = 4$
- Case 4 : $2 \times 2 \times 2 = 8$
- Case 5 : $2 \times 2 \times 2 \times 2 = 16$

Pour la 10e case, nous devons écrire dix fois le chiffre 2 multiplié par lui-même. Pour la 64e case, il faudrait écrire une ligne de soixante-trois fois le chiffre 2 ! C'est interminable et illisible.

Au XVIIe siècle, le mathématicien français **René Descartes** a une idée lumineuse : inscrire le nombre de répétitions en tout petit, perché en haut à droite du nombre.

> **📐 Définition — Puissance d'un nombre**
> Pour tout nombre relatif $a$ et pour tout nombre entier positif $n \ge 1$ :
> $$a^n = \underbrace{a \times a \times a \times \dots \times a}_{n \text{ facteurs}}$$
> - $a$ s'appelle la **base**.
> - $n$ s'appelle l'**exposant**.
> - L'expression $a^n$ se lit **« $a$ puissance $n$ »** ou **« $a$ exposant $n$ »**.

#### Vocabulaire particulier pour 2 et 3
- $a^2$ se lit **« $a$ au carré »** (car c'est l'aire d'un carré de côté $a$).
- $a^3$ se lit **« $a$ au cube »** (car c'est le volume d'un cube d'arête $a$).

#### Cas particuliers vitaux : exposant 1 et exposant 0
- **Exposant 1 :** $a^1 = a$ (un seul facteur).
- **Exposant 0 :** pour tout nombre non nul $a \neq 0$, on pose :
  $$a^0 = 1$$

*Pourquoi $a^0 = 1$ ?* Regarde la suite en divisant par 2 à chaque marche descendante :
$$2^3 = 8 \xrightarrow{\div 2} 2^2 = 4 \xrightarrow{\div 2} 2^1 = 2 \xrightarrow{\div 2} 2^0 = \mathbf{1}$$
C'est la seule façon logique pour que la règle de division continue de fonctionner !

#### Combien de grains sur l'échiquier ?
Sur la 64e case, il y a :
$$2^{63} \approx 9{,}22 \times 10^{18} \text{ grains}$$
Et la somme de toutes les cases réunies vaut :
$$2^0 + 2^1 + 2^2 + \dots + 2^{63} = 2^{64} - 1 = \mathbf{18\,446\,744\,073\,709\,551\,615} \text{ grains !}$$
Soit plus de **18 milliards de milliards de grains de riz** ! Si l'on étalait cette moisson sur la France entière, le pays disparaîtrait sous une couche de riz de plus d'un mètre de hauteur.

---

### 4. Les puissances de 10 et les exposants négatifs

Le nombre $10$ est le roi de notre système décimal (hérité de nos dix doigts). Les puissances de 10 sont les championnes absolues du calcul scientifique.

#### 4.1 Puissances positives de 10 : l'armée des zéros

> **📐 Règle — Puissances positives de 10**
> Pour tout entier positif $n$ :
> $$10^n = 1\underbrace{000\dots0}_{n \text{ zéros}}$$
> Le chiffre de l'exposant indique **exactement le nombre de zéros** après le 1 !

- $10^1 = 10$ (dix)
- $10^2 = 100$ (cent)
- $10^3 = 1\,000$ (mille, préfixe *kilo*)
- $10^6 = 1\,000\,000$ (un million, préfixe *méga*)
- $10^9 = 1\,000\,000\,000$ (un milliard, préfixe *giga*)
- $10^{12} = 1\,000\,000\,000\,000$ (un billion ou mille milliards, préfixe *téra*)

#### 4.2 Exposants négatifs : plongée dans l'infiniment petit

Continuons à descendre l'escalier en divisant par 10 à chaque marche :

$$\begin{aligned}
10^3 &= 1\,000 \\
10^2 &= 100 \\
10^1 &= 10 \\
10^0 &= 1 \\
10^{-1} &= \frac{1}{10} = 0{,}1 \\
10^{-2} &= \frac{1}{10^2} = \frac{1}{100} = 0{,}01 \\
10^{-3} &= \frac{1}{10^3} = \frac{1}{1\,000} = 0{,}001
\end{aligned}$$

> **📐 Définition — Exposant négatif**
> Pour tout nombre non nul $a \neq 0$ et tout entier $n$ :
> $$a^{-n} = \frac{1}{a^n}$$
> En particulier pour $a = 10$ :
> $$10^{-n} = \frac{1}{10^n} = \underbrace{0{,}00\dots0}_{n \text{ zéros en tout}}1$$
> L'exposant négatif indique **l'inverse** de la puissance. Pour $10^{-n}$, il y a **$n$ zéros au total**, en comptant celui qui est placé avant la virgule !

- $10^{-1} = 0{,}1$ (un dixième, préfixe *déci*)
- $10^{-2} = 0{,}01$ (un centième, préfixe *centi*)
- $10^{-3} = 0{,}001$ (un millième, préfixe *milli*)
- $10^{-6} = 0{,}000\,001$ (un millionième, préfixe *micro*)
- $10^{-9} = 0{,}000\,000\,001$ (un milliardième, préfixe *nano*)

---

### 5. Les règles d'or du calcul sur les puissances

Quand on manipule des puissances de même base, le calcul se transforme comme par magie : **une multiplication devient une addition d'exposants !**

> **📐 Formules fondamentales des puissances**
> Pour tous entiers relatifs $m$ et $n$, et nombres $a$ et $b$ non nuls :
>
> 1. **Produit de puissances de même base :**
>    $$a^m \times a^n = a^{m+n}$$
>    *(Exemple : $10^3 \times 10^4 = 10^{3+4} = 10^7$)*
>
> 2. **Quotient de puissances de même base :**
>    $$\frac{a^m}{a^n} = a^{m-n}$$
>    *(Exemple : $\frac{10^7}{10^2} = 10^{7-2} = 10^5$ ; $\frac{10^3}{10^8} = 10^{3-8} = 10^{-5}$)*
>
> 3. **Puissance d'une puissance :**
>    $$(a^m)^n = a^{m \times n}$$
>    *(Exemple : $(10^3)^4 = 10^{3 \times 4} = 10^{12}$)*
>
> 4. **Puissance d'un produit :**
>    $$(a \times b)^n = a^n \times b^n$$
>    *(Exemple : $(2 \times 5)^3 = 2^3 \times 5^3 = 8 \times 125 = 1\,000 = 10^3$)*

---

### 6. La notation scientifique : écrire l'Univers

Comment comparer la masse d'un atome d'hydrogène ($0{,}000\,000\,000\,000\,000\,000\,000\,000\,001\,67\text{ kg}$) et celle de la Terre ($5\,972\,000\,000\,000\,000\,000\,000\,000\text{ kg}$) ?
C'est impossible à l'œil nu sans perdre le compte des zéros !
C'est pourquoi les savants ont inventé un format standardisé obligatoire : la **notation scientifique**.

> **📐 Définition — Notation scientifique**
> Un nombre est écrit en **notation scientifique** lorsqu'il est sous la forme :
> $$a \times 10^n$$
> où :
> - $a$ est un nombre décimal ayant **un seul chiffre non nul avant la virgule** (c'est-à-dire $1 \le a < 10$ ou $-10 < a \le -1$).
> - $n$ est un nombre entier relatif (positif ou négatif).

#### Méthode de conversion rapide
- Pour un grand nombre : on déplace la virgule vers la **gauche** de $n$ crans $\implies 10^{+n}$.
  $$149\,600\,000\text{ km} = 1{,}496 \times 10^8\text{ km} \quad (\text{distance Terre-Soleil})$$
- Pour un petit nombre : on déplace la virgule vers la **droite** de $n$ crans $\implies 10^{-n}$.
  $$0{,}000\,000\,12\text{ m} = 1{,}2 \times 10^{-7}\text{ m} \quad (\text{taille d'un virus})$$

```
      Échelle des ordres de grandeur dans l'Univers (en mètres)
   10⁻¹⁵ m      10⁻¹⁰ m       1 m        10⁶ m       10¹¹ m        10²¹ m
      |────────────|───────────|───────────|───────────|─────────────|
    Noyau        Atome       Humain      Terre     Système       Galaxie
   atomique                                        solaire     Voie Lactée
```

---

### 7. Attention aux pièges !

> **⚠️ Attention, piège ! — Les bévues monumentales**
> 1. **La fausse addition d'exposants :**
>    $$10^2 + 10^3 \neq 10^5 \quad !$$
>    Les puissances ne s'ajoutent JAMAIS entre elles directement !
>    $10^2 + 10^3 = 100 + 1\,000 = 1\,100$, alors que $10^5 = 100\,000$.
> 2. **Le piège du signe moins et des parenthèses :**
>    $$-3^2 = -(3 \times 3) = \mathbf{-9}$$
>    $$(-3)^2 = (-3) \times (-3) = \mathbf{+9}$$
>    Sans parenthèses, la puissance ne porte QUE sur le 3, pas sur le signe moins !
> 3. **Le format scientifique invalide :**
>    - $35 \times 10^4$ n'est **pas** en notation scientifique car $35 \ge 10$ (il faut écrire $3{,}5 \times 10^5$).
>    - $0{,}7 \times 10^{-3}$ n'est **pas** en notation scientifique car $0{,}7 < 1$ (il faut écrire $7 \times 10^{-4}$).
> 4. **Multiplier les bases au lieu d'additionner les exposants :**
>    $$2^3 \times 2^4 \neq 4^7 \quad \text{mais} \quad 2^{3+4} = 2^7 = 128$$

---

### 8. Exemples résolus

#### Exemple résolu 1 — Calcul avec priorités opératoires
Calculer la valeur exacte de l'expression suivante en détaillant les étapes :
$$A = 5 + 3 \times (4^2 - 6) - \frac{24}{2^3}$$

*Solution :*
Appliquons la règle PEMDAS rigoureusement :
1. Calcul à l'intérieur des parenthèses :
   - Puissance d'abord : $4^2 = 16$.
   - Soustraction : $16 - 6 = 10$.
   L'expression devient : $A = 5 + 3 \times 10 - \frac{24}{2^3}$.
2. Puissance restante au dénominateur :
   - $2^3 = 2 \times 2 \times 2 = 8$.
   L'expression devient : $A = 5 + 3 \times 10 - \frac{24}{8}$.
3. Multiplications et divisions :
   - $3 \times 10 = 30$.
   - $\frac{24}{8} = 3$.
   L'expression devient : $A = 5 + 30 - 3$.
4. Additions et soustractions de gauche à droite :
   - $5 + 30 = 35$, puis $35 - 3 = 32$.
Conclusion : $A = 32$. ✔

#### Exemple résolu 2 — Réduire une expression avec les puissances de 10
Écrire sous la forme d'une seule puissance de 10 :
$$B = \frac{10^5 \times (10^{-2})^3}{10^{-4}}$$

*Solution :*
1. On traite d'abord la puissance de puissance au numérateur :
   $$(10^{-2})^3 = 10^{-2 \times 3} = 10^{-6}$$
2. On effectue le produit au numérateur (addition des exposants) :
   $$10^5 \times 10^{-6} = 10^{5 + (-6)} = 10^{-1}$$
3. On effectue la division (soustraction de l'exposant du dénominateur) :
   $$B = \frac{10^{-1}}{10^{-4}} = 10^{-1 - (-4)} = 10^{-1 + 4} = 10^3$$
Conclusion : $B = 10^3$ (soit $1\,000$). ✔

#### Exemple résolu 3 — Conversion en notation scientifique
Donner la notation scientifique des nombres suivants :
1. $C = 548\,000\,000$ (population d'un continent)
2. $D = 0{,}000\,037$ (diamètre d'une fibre en mètre)
3. $E = 485 \times 10^6$
4. $F = 0{,}029 \times 10^{-4}$

*Solution :*
1. Pour $548\,000\,000$, on place la virgule après le premier chiffre 5. On a décalé de 8 rangs vers la gauche :
   $$C = 5{,}48 \times 10^8$$
2. Pour $0{,}000\,037$, on place la virgule après le 3. On a décalé de 5 rangs vers la droite :
   $$D = 3{,}7 \times 10^{-5}$$
3. $E = 485 \times 10^6 = (4{,}85 \times 10^2) \times 10^6 = 4{,}85 \times 10^{2+6} = 4{,}85 \times 10^8$.
4. $F = 0{,}029 \times 10^{-4} = (2{,}9 \times 10^{-2}) \times 10^{-4} = 2{,}9 \times 10^{-2 + (-4)} = 2{,}9 \times 10^{-6}$. ✔

#### Exemple résolu 4 — Calcul astronomique en notation scientifique
La lumière voyage dans le vide à une vitesse constante d'environ $v = 3 \times 10^8\text{ m/s}$.
La distance moyenne entre la Terre et le Soleil est de $d = 1{,}5 \times 10^{11}\text{ mètres}$.
Combien de temps (en secondes, puis en minutes et secondes) met un photon émis par le Soleil pour parvenir sur Terre ?

*Solution :*
On utilise la formule $t = \frac{d}{v}$ :
$$t = \frac{1{,}5 \times 10^{11}}{3 \times 10^8}$$
Séparons les nombres décimaux et les puissances de 10 :
$$t = \left(\frac{1{,}5}{3}\right) \times \left(\frac{10^{11}}{10^8}\right) = 0{,}5 \times 10^{11-8} = 0{,}5 \times 10^3\text{ secondes}$$
Calculons la valeur décimale :
$$t = 0{,}5 \times 1\,000 = 500\text{ secondes}$$
Convertissons en minutes ($1\text{ min} = 60\text{ s}$) :
$500 = 8 \times 60 + 20$.
Le rayon de soleil met **8 minutes et 20 secondes** pour atteindre nos yeux ! ✔

#### Exemple résolu 5 — L'épaisseur de la feuille pliée en deux
Une feuille de papier standard a une épaisseur de $e = 0{,}1\text{ mm} = 10^{-4}\text{ m}$.
Chaque fois qu'on la plie en deux, son épaisseur double.
1. Quelle sera l'épaisseur théorique de la feuille si l'on pouvait la plier 10 fois de suite ?
2. Et si l'on pouvait la plier 42 fois de suite ?

*Solution :*
1. Après 10 pliages, l'épaisseur est multipliée par $2^{10}$.
   Or $2^{10} = 1\,024 \approx 10^3$.
   $$\text{Épaisseur} = 0{,}1\text{ mm} \times 1\,024 = 102{,}4\text{ mm} \approx 10{,}24\text{ cm}$$
   La feuille dépasse déjà l'épaisseur d'un gros livre !
2. Après 42 pliages, l'épaisseur est :
   $$E = 0{,}1\text{ mm} \times 2^{42}$$
   Calculons $2^{42}$ : $2^{42} = (2^{10})^4 \times 2^2 \approx (1\,000)^4 \times 4 = 4 \times 10^{12}$.
   $$E \approx 10^{-4}\text{ m} \times (4{,}398 \times 10^{12}) \approx 4{,}4 \times 10^8\text{ mètres} = 440\,000\text{ kilomètres} !$$
   La distance moyenne de la Terre à la Lune est de $384\,400\text{ km}$.
   Une simple feuille de papier pliée 42 fois dépasse la Lune ! C'est l'illustration la plus spectaculaire de l'explosion des puissances. ✔

---

### Ce qu'il faut retenir

1. **Priorités opératoires (PEMDAS) :**
   Parenthèses $\to$ Exposants $\to$ Multiplications & Divisions (gauche à droite) $\to$ Additions & Soustractions (gauche à droite).
2. **Définition des puissances :**
   $a^n = \underbrace{a \times a \times \dots \times a}_{n \text{ fois}}$ ; $a^1 = a$ ; $a^0 = 1$ ($a \neq 0$).
3. **Exposants négatifs :**
   $a^{-n} = \frac{1}{a^n}$ ; en particulier $10^{-n} = \frac{1}{10^n} = 0{,}0\dots01$ ($n$ zéros en tout).
4. **Règles de calcul sur les puissances :**
   - $a^m \times a^n = a^{m+n}$
   - $\frac{a^m}{a^n} = a^{m-n}$
   - $(a^m)^n = a^{m \times n}$
   - $(a \times b)^n = a^n \times b^n$
5. **Notation scientifique :**
   Format unique : $a \times 10^n$ avec $1 \le a < 10$ (un seul chiffre non nul avant la virgule).

---

### Exercices

#### Niveau ★ (Application directe)

**Exercice 1.** Calcule la valeur numérique des expressions suivantes :
1. $A = 7 + 3 \times 4$
2. $B = (7 + 3) \times 4$
3. $C = 20 - 4 \times 2 + 1$
4. $D = 30 / 5 \times 2$

**Exercice 2.** Calcule sans calculatrice :
$2^4$ ; $3^3$ ; $5^2$ ; $10^5$ ; $7^0$ ; $(-2)^3$ ; $(-2)^4$ ; $-5^2$.

**Exercice 3.** Écris sous forme décimale :
$10^3$ ; $10^{-2}$ ; $10^{-5}$ ; $4{,}2 \times 10^3$ ; $7 \times 10^{-4}$.

**Exercice 4.** Écris sous la forme d'une seule puissance de 10 :
1. $10^4 \times 10^7$
2. $\frac{10^9}{10^3}$
3. $(10^5)^2$
4. $10^{-3} \times 10^{-5}$
5. $\frac{10^2}{10^{-4}}$

**Exercice 5.** Parmi les écritures suivantes, lesquelles sont en notation scientifique ? Justifie.
a) $3{,}45 \times 10^7$ ; b) $0{,}4 \times 10^{-3}$ ; c) $12 \times 10^5$ ; d) $9{,}99 \times 10^{-1}$ ; e) $1 \times 10^0$.

#### Niveau ★★ (Calculs et règles)

**Exercice 6.** Calcule en respectant strictement les priorités :
1. $G = 3 \times 2^3 - 4 \times (5 - 2^2)$
2. $H = \frac{5^2 - 3^2}{2^4 - 2 \times 4}$

**Exercice 7.** Écris sous la forme $a^n$ (où $a$ est un entier et $n$ un entier relatif) :
1. $2^5 \times 2^3 \times 2^{-4}$
2. $\frac{3^8}{(3^2)^3}$
3. $\frac{7^3 \times 7^{-5}}{7^{-4}}$
4. $8 \times 2^5$ *(Indication : écris 8 comme une puissance de 2)*.

**Exercice 8.** Mets chacun des nombres suivants en notation scientifique :
1. Diamètre du globule rouge : $0{,}000\,007\text{ m}$.
2. Vitesse de la lumière : $300\,000\,000\text{ m/s}$.
3. Population mondiale : $8\,100\,000\,000\text{ habitants}$.
4. Masse d'une goutte d'eau : $0{,}000\,05\text{ kg}$.

**Exercice 9.** Effectue les calculs suivants et donne le résultat final en notation scientifique :
1. $K = (3 \times 10^4) \times (5 \times 10^7)$
2. $L = \frac{8 \times 10^{-3}}{4 \times 10^5}$
3. $M = \frac{1{,}2 \times 10^5 \times 7 \times 10^{-2}}{2{,}4 \times 10^{-6}}$

**Exercice 10. Les bactéries attaquent !**
Une population de bactéries est placée dans une boîte de Pétri chauffée.
À midi ($t = 0$), il y a $1\,000$ bactéries ($10^3$).
Cette souche double toutes les 20 minutes.
1. Combien y a-t-il de bactéries à 13 h 00 ?
2. Combien y a-t-il de bactéries à 16 h 00 ? Donne la réponse en notation scientifique.

**Exercice 11. Comparer sans calculer.**
Range les nombres suivants par ordre croissant sans poser de calculs posés géants :
$$A = 4{,}5 \times 10^6 \quad ; \quad B = 8{,}2 \times 10^5 \quad ; \quad C = 1{,}1 \times 10^7 \quad ; \quad D = 9{,}9 \times 10^5$$

#### Niveau ★★★ (Défis et grands nombres)

**Exercice 12. Le Googol et le Googolplex.**
En 1920, le mathématicien américain Edward Kasner demanda à son neveu Milton Sirotta, âgé de 9 ans, d'inventer un nom pour un nombre colossal : le chiffre 1 suivi de 100 zéros. L'enfant répondit : « Un GOGOL ! » (qui inspirera plus tard le nom du moteur de recherche *Google*).
1. Écris un gogol sous la forme d'une puissance de 10.
2. Le nombre total d'atomes dans tout l'Univers observable est estimé à environ $10^{80}$. Un gogol est-il plus grand ou plus petit que le nombre d'atomes de l'Univers ? Combien de fois plus grand ?
3. Kasner définit ensuite le *Googolplex* : c'est le nombre 1 suivi d'un gogol de zéros ! Écris le Googolplex avec des puissances de 10. Pourquoi est-il physiquement impossible d'écrire ce nombre sur du papier dans notre univers ?

**Exercice 13. Le voyage interstellaire de la sonde Voyager 1.**
La sonde spatiale *Voyager 1* file à travers l'espace interstellaire à la vitesse vertigineuse de $17\text{ km/s}$, soit environ $6{,}12 \times 10^4\text{ km/h}$.
Elle se dirige vers l'étoile Proxima du Centaure, située à environ $4{,}24\text{ années-lumière}$ de la Terre.
Une année-lumière vaut environ $9{,}46 \times 10^{12}\text{ km}$.
1. Calcule la distance en kilomètres séparant la Terre de Proxima du Centaure en notation scientifique.
2. Combien d'heures, puis combien d'années faudra-t-il à la sonde pour parcourir cette distance ?

**Exercice 14. Simplification d'expression littérale avec puissances.**
Pour tous nombres réels non nuls $x$ et $y$, simplifie au maximum l'expression suivante :
$$Z = \frac{(x^2 y^{-3})^4 \times (x^{-1} y)^2}{x^5 y^{-8}}$$

**Exercice 15. Le piège de la somme des inverses de puissances.**
Calcule la valeur exacte de la somme :
$$S = \frac{1}{2^1} + \frac{1}{2^2} + \frac{1}{2^3} + \frac{1}{2^4} + \frac{1}{2^5} + \frac{1}{2^6}$$
Que remarques-tu par rapport au nombre 1 ? Que vaudrait cette somme si l'on continuait à l'infini ?

---

### Solutions

**Exercice 1.**
1. $A = 7 + 12 = 19$.
2. $B = 10 \times 4 = 40$.
3. $C = 20 - 8 + 1 = 12 + 1 = 13$.
4. $D = (30 / 5) \times 2 = 6 \times 2 = 12$ (de gauche à droite).

**Exercice 2.**
- $2^4 = 16$ ; $3^3 = 27$ ; $5^2 = 25$ ; $10^5 = 100\,000$ ; $7^0 = 1$.
- $(-2)^3 = -8$ ; $(-2)^4 = +16$ ; $-5^2 = -(5 \times 5) = -25$.

**Exercice 3.**
$10^3 = 1\,000$ ; $10^{-2} = 0{,}01$ ; $10^{-5} = 0{,}000\,01$ ;
$4{,}2 \times 10^3 = 4\,200$ ; $7 \times 10^{-4} = 0{,}000\,7$.

**Exercice 4.**
1. $10^4 \times 10^7 = 10^{4+7} = 10^{11}$.
2. $\frac{10^9}{10^3} = 10^{9-3} = 10^6$.
3. $(10^5)^2 = 10^{5 \times 2} = 10^{10}$.
4. $10^{-3} \times 10^{-5} = 10^{-3 + (-5)} = 10^{-8}$.
5. $\frac{10^2}{10^{-4}} = 10^{2 - (-4)} = 10^{2+4} = 10^6$.

**Exercice 5.**
- a) Oui ($1 \le 3{,}45 < 10$).
- b) Non ($0{,}4 < 1$).
- c) Non ($12 \ge 10$).
- d) Oui ($1 \le 9{,}99 < 10$).
- e) Oui ($1 \le 1 < 10$).

**Exercice 6.**
1. $G = 3 \times 8 - 4 \times (5 - 4) = 24 - 4 \times 1 = 24 - 4 = 20$.
2. $H = \frac{25 - 9}{16 - 8} = \frac{16}{8} = 2$.

**Exercice 7.**
1. $2^{5 + 3 - 4} = 2^4$.
2. $\frac{3^8}{3^6} = 3^{8-6} = 3^2$.
3. $\frac{7^{-2}}{7^{-4}} = 7^{-2 - (-4)} = 7^2$.
4. $8 = 2^3$, donc $8 \times 2^5 = 2^3 \times 2^5 = 2^8$.

**Exercice 8.**
1. $7 \times 10^{-6}\text{ m}$.
2. $3 \times 10^8\text{ m/s}$.
3. $8{,}1 \times 10^9\text{ habitants}$.
4. $5 \times 10^{-5}\text{ kg}$.

**Exercice 9.**
1. $K = (3 \times 5) \times (10^4 \times 10^7) = 15 \times 10^{11} = 1{,}5 \times 10^{12}$.
2. $L = \left(\frac{8}{4}\right) \times 10^{-3-5} = 2 \times 10^{-8}$.
3. $M = \left(\frac{1{,}2 \times 7}{2{,}4}\right) \times \frac{10^3}{10^{-6}} = \left(\frac{8{,}4}{2{,}4}\right) \times 10^{3 - (-6)} = 3{,}5 \times 10^9$.

**Exercice 10.**
1. En 1 heure, il y a 3 périodes de 20 minutes. La population double 3 fois :
   $N_1 = 1\,000 \times 2^3 = 1\,000 \times 8 = 8\,000$ bactéries.
2. À 16 h 00, 4 heures se sont écoulées, soit $4 \times 3 = 12$ périodes de 20 min.
   $N_2 = 10^3 \times 2^{12} = 10^3 \times 4\,096 = 4\,096\,000 = 4{,}096 \times 10^6$ bactéries.

**Exercice 11.**
On classe d'abord par puissance de 10 :
- Exposant 5 : $B = 8{,}2 \times 10^5$ et $D = 9{,}9 \times 10^5$. Comme $8{,}2 < 9{,}9$, $B < D$.
- Exposant 6 : $A = 4{,}5 \times 10^6$.
- Exposant 7 : $C = 1{,}1 \times 10^7$.
Ordre croissant : $B < D < A < C$.

**Exercice 12.**
1. Un gogol s'écrit $10^{100}$.
2. $10^{100}$ est immensément plus grand que $10^{80}$ :
   $\frac{10^{100}}{10^{80}} = 10^{100-80} = 10^{20}$.
   Un gogol est **cent milliards de milliards de fois plus grand** que le nombre total d'atomes de l'Univers observable !
3. Un Googolplex s'écrit $10^{\text{gogol}} = 10^{10^{100}}$.
   Pour l'écrire sous forme décimale ($1000\dots$), il faudrait écrire $10^{100}$ zéros. Même si l'on gravait un zéro sur chaque atome de l'univers ($10^{80}$ atomes), on manquerait d'atomes bien avant d'avoir écrit le milliardième du nombre !

**Exercice 13.**
1. $D = 4{,}24 \times (9{,}46 \times 10^{12}) \approx 40{,}11 \times 10^{12} = 4{,}011 \times 10^{13}\text{ km}$.
2. Temps en heures : $t = \frac{4{,}011 \times 10^{13}}{6{,}12 \times 10^4} \approx 0{,}6554 \times 10^9 = 6{,}554 \times 10^8\text{ heures}$.
   En années ($1\text{ an} \approx 365{,}25 \times 24 = 8\,766\text{ h}$) :
   $T = \frac{6{,}554 \times 10^8}{8\,766} \approx 74\,766\text{ années}$ !
   Il faudra près de 75 000 ans à la sonde pour croiser notre étoile voisine.

**Exercice 14.**
Développons le numérateur :
$(x^2 y^{-3})^4 = x^8 y^{-12}$.
$(x^{-1} y)^2 = x^{-2} y^2$.
Numérateur $= x^{8-2} y^{-12+2} = x^6 y^{-10}$.
Divisons par le dénominateur :
$Z = \frac{x^6 y^{-10}}{x^5 y^{-8}} = x^{6-5} y^{-10 - (-8)} = x^1 y^{-2} = \frac{x}{y^2}$.

**Exercice 15.**
$S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \frac{1}{64}$.
Même dénominateur (64) :
$S = \frac{32 + 16 + 8 + 4 + 2 + 1}{64} = \frac{63}{64} = 0{,}984375$.
La somme s'approche infiniment près de $1$, sans jamais le dépasser (il manque toujours $\frac{1}{2^n}$). Si l'on additionnait une infinité de termes, la somme vaudrait rigoureusement $1$ !

---

### La question qui ouvre la suite

Nous savons désormais que $a^2$ est le carré d'un nombre : $3^2 = 9$, $4^2 = 16$.
Mais que se passe-t-il si l'on cherche l'opération inverse ? Quel nombre, multiplié par lui-même, donne $2$ ?

Ce nombre innocent a brisé la secte la plus puissante de l'Antiquité grecque, provoqué des condamnations à mort en mer et révélé l'existence d'une race de nombres monstrueux que les fractions ne savent pas capturer : **les nombres irrationnels**. Pénétrons dans l'école mystique de Crotone avec **le Théorème de Pythagore** !
