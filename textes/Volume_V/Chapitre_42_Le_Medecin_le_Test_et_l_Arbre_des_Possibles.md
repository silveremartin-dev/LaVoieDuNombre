# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 42 : Le Médecin, le Test et l'Arbre des Possibles

> *« Le bon sens devant le hasard est un aveugle qui avance à tâtons. Quand un test médical fiable à 99 % vous déclare malade, la panique vous crie que vous êtes perdu à 99 %. Le mathématicien, lui, respire, trace un arbre dans l'espace des possibles, rétrécit l'univers, et découvre que vous avez neuf chances sur dix d'être parfaitement sain. »*

---

### Ce que tu vas découvrir

- Le paradoxe du test médical : comment un test presque infaillible peut produire une majorité de faux positifs pour une maladie rare.
- La notion révolutionnaire de **probabilité conditionnelle** : comment une information nouvelle **rétrécit l'univers des possibles**.
- Les lois de l'**arbre pondéré** : la règle du produit le long des branches et la somme des chemins.
- La **formule des probabilités totales** : découper l'univers en tranches pour calculer l'inconnu.
- La formule légendaire du pasteur **Thomas Bayes** pour remonter le temps des causes.
- La frontière capitale entre deux événements **indépendants** et deux événements **disjoints**.
- Les **variables aléatoires discrètes** : associer un gain en euros à chaque issue du hasard.
- L'**espérance mathématique** $E(X)$ : la moyenne à long terme et le juste prix d'un billet de loterie.
- La **variance** $V(X)$, l'**écart-type** $\sigma(X)$ et la **linéarité de l'espérance** : $E(aX + b) = aE(X) + b$.

---

### 1. Le problème : le cauchemar de Thomas dans le cabinet médical

Thomas a dix-sept ans. Pour son inscription sportive en compétition, le médecin lui fait passer un test de dépistage sanguin pour une anomalie cardiaque rare mais dangereuse, qui touche **1 personne sur 1 000** dans la population générale.

Trois jours plus tard, le téléphone sonne. La voix du médecin est grave :
*« Thomas, votre test sanguin est revenu positif. »*

Thomas sent la terre se dérober sous ses pieds. Il demande d'une voix tremblante :
*« Docteur, quelle est la fiabilité de votre test ? »*
Le médecin consulte la notice du laboratoire :
*« Le test est d'une fiabilité remarquable de **99 %** :*
- *Si une personne est malade, le test est positif dans 99 % des cas (sensibilité).*
- *Si une personne est saine, le test est négatif dans 99 % des cas (spécificité). »*

Thomas s'effondre sur sa chaise :
*« Le test est fiable à 99 %. Mon test est positif. J'ai donc 99 % de risque d'avoir cette maladie cardiaque ! »*

Thomas a-t-il raison de paniquer ?
La réponse des mathématiques est éclatante, spectaculaire, et va bouleverser ton intuition :
**NON ! Thomas a en réalité moins de 10 % de risque d'être malade !**
Il a plus de **90 % de chances d'être en parfaite santé** !

Comment est-ce possible ? Comment un test fiable à 99 % peut-il se tromper neuf fois sur dix lorsqu'il annonce une maladie ?

---

### 2. Le rétrécissement de l'univers : la probabilité conditionnelle

Pour comprendre ce prodige sans formule obscure, prenons un échantillon concret de **100 000 personnes** représentatives de la population :

```
                                 POPULATION TOTALE
                                  100 000 personnes
                                  /              \
                                 /                \
                    1 sur 1000  /                  \  999 sur 1000
                               /                    \
                       MALADES                      SAINS
                    100 personnes             99 900 personnes
                      /        \                  /        \
              99 %   /          \ 1 %     1 %    /          \ 99 %
                    /            \              /            \
                POSITIFS       NÉGATIFS     POSITIFS       NÉGATIFS
               99 malades      1 malade    999 sains     98 901 sains
```

Regarde attentivement les chiffres :
1. Sur 100 000 personnes, comme la maladie touche 1 personne sur 1 000, il y a **100 malades** et **99 900 personnes saines**.
2. Parmi les 100 malades : le test en détecte 99 % : il y a **99 tests positifs** (et 1 malade testé négatif par erreur).
3. Mais regarde maintenant les **99 900 personnes saines** :
   Le test est fiable à 99 %, ce qui signifie qu'il se trompe sur 1 % d'entre elles.
   1 % de 99 900, cela fait très exactement **999 personnes saines testées positives à tort** (des faux positifs) !

Et maintenant, mettons-nous dans la peau de Thomas :
Le médecin lui a annoncé que son test est positif. L'univers entier de Thomas vient de **rétrécir** : Thomas ne fait plus partie des 100 000 personnes du début, il fait partie du club restreint des personnes ayant reçu un **test positif** !

Combien y a-t-il de personnes positives au total dans la salle d'attente ?
$$\text{Total Positifs} = 99 \text{ (malades)} + 999 \text{ (sains)} = \mathbf{1 098 \text{ personnes}}.$$

Et parmi ces 1 098 personnes testées positives, combien sont véritablement malades ?
Seulement **99 personnes** !

La probabilité que Thomas soit malade sachant que son test est positif est donc :

$$P(\text{Malade sachant Positif}) = \frac{99}{1 098} \approx \mathbf{0{,}0902} = \mathbf{9{,}02\,\%}.$$

Plus de **91 % des gens testés positifs sont des personnes bien portantes** !
Pourquoi ? Parce que la maladie est tellement rare que le minuscule taux d'erreur de 1 % appliqué à l'immense océan des personnes saines produit dix fois plus de faux positifs que de vrais malades !

---

### 3. La théorie : définition et notation de la probabilité conditionnelle

#### 3.1 Définition officielle

Soit un univers $\Omega$ muni d'une loi de probabilité $P$. Soient $A$ et $B$ deux événements.

> **📐 Définition — Probabilité conditionnelle**
> Soit $A$ un événement de probabilité non nulle ($P(A) > 0$).
> On appelle **probabilité conditionnelle de $B$ sachant $A$**, notée $P_A(B)$ ou $P(B \mid A)$ :
>
> $$\boxed{P_A(B) = \frac{P(A \cap B)}{P(A)}}$$
>
> On prononce à voix haute : « **probabilité de B sachant A** ».

**Sens géométrique :**
On remplace le grand univers $\Omega$ de référence (qui pesait une probabilité 1) par le sous-ensemble $A$. L'événement $A$ devient le nouvel univers. La fraction de $B$ qui vit à l'intérieur de ce nouvel univers est la zone commune $A \cap B$, divisée par la taille de $A$.

```
     ┌───────────────────────────────────┐
     │  Univers Ω                        │
     │        ┌──────────────┐           │
     │        │ A            │           │
     │        │     ┌────────┼──────┐    │
     │        │     │ A ∩ B  │  B   │    │
     │        │     └────────┼──────┘    │
     │        └──────────────┘           │
     └───────────────────────────────────┘
     L'univers est réduit à la bulle A : P_A(B) = Aire(A ∩ B) / Aire(A)
```

#### 3.2 La règle du produit (principe multiplicatif)

En multipliant par $P(A)$, on obtient la formule fondamentale :

> **📐 Théorème — Règle du produit**
> Pour tous événements $A$ et $B$ avec $P(A) > 0$ :
>
> $$\boxed{P(A \cap B) = P(A) \times P_A(B)}$$

---

### 4. L'arbre pondéré et la formule des probabilités totales

#### 4.1 Les deux règles d'or de l'arbre pondéré

Un arbre pondéré est un outil visuel d'une puissance redoutable pour organiser chronologiquement les épreuves aléatoires successives.

```
                  P_A(B)
               .────────► B     ──► Chemin A ∩ B : P(A ∩ B) = P(A) × P_A(B)
        P(A)  /
       .─────► A
      /       \
     /         '────────► B̄     ──► Chemin A ∩ B̄ : P(A ∩ B̄) = P(A) × P_A(B̄)
    o         P_A(B̄)
     \
      \       .────────► B     ──► Chemin Ā ∩ B : P(Ā ∩ B) = P(Ā) × P_Ā(B)
       '─────► Ā
        P(Ā)  \
               '────────► B̄     ──► Chemin Ā ∩ B̄ : P(Ā ∩ B̄) = P(Ā) × P_Ā(B̄)
                  P_Ā(B̄)
```

> **📐 Règles de l'arbre pondéré**
> 1. **Règle des nœuds :** La somme des probabilités portées par les branches issues d'un même nœud est **toujours égale à 1**.
>    $$P(A) + P(\overline{A}) = 1, \qquad P_A(B) + P_A(\overline{B}) = 1.$$
> 2. **Règle du chemin (produit) :** La probabilité d'un chemin complet est le **produit** des probabilités inscrites sur chaque branche du chemin.
> 3. **Règle des feuilles (somme) :** La probabilité d'un événement final est la **somme** des probabilités de tous les chemins menant à cet événement.

#### 4.2 La formule des probabilités totales

> **📐 Définition — Partition de l'univers**
> On dit que des événements $A_1, A_2, \dots, A_n$ forment une **partition** de l'univers $\Omega$ si :
> - Ils sont deux à deux disjoints ($A_i \cap A_j = \varnothing$ pour $i \neq j$) ;
> - Leur réunion forme l'univers tout entier ($A_1 \cup A_2 \cup \dots \cup A_n = \Omega$) ;
> - Aucun d'eux n'est impossible ($P(A_i) > 0$).
>
> Le cas le plus fréquent est la partition élémentaire formée par un événement et son contraire : $\{A ; \overline{A}\}$.

> **📐 Théorème — Formule des probabilités totales**
> Si $A_1, A_2, \dots, A_n$ forment une partition de l'univers, alors pour tout événement $B$ :
>
> $$\boxed{P(B) = \sum_{i=1}^n P(B \cap A_i) = \sum_{i=1}^n P(A_i) \times P_{A_i}(B)}$$
>
> Dans le cas d'une partition à deux issues $\{A ; \overline{A}\}$ :
> $$\boxed{P(B) = P(A) \times P_A(B) + P(\overline{A}) \times P_{\overline{A}}(B)}$$

---

### 5. La formule de Bayes : remonter le temps des causes

En 1763, un pasteur presbytérien et mathématicien britannique, **Thomas Bayes**, publie à titre posthume un mémoire qui va bouleverser la philosophie des sciences. Il se pose la question inverse : *« Sachant que l'effet s'est produit (le test est positif), quelle est la probabilité que telle cause en soit à l'origine (le patient est malade) ? »*

> **📐 Théorème — Formule de Bayes**
> Soit $\{A ; \overline{A}\}$ une partition de l'univers et $B$ un événement de probabilité non nulle.
>
> $$\boxed{P_B(A) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \times P_A(B)}{P(A) \times P_A(B) + P(\overline{A}) \times P_{\overline{A}}(B)}}$$

Appliquons cette formule magistrale au cas de Thomas :
- Cause $M$ : « être malade », $P(M) = 0{,}001 \implies P(\overline{M}) = 0{,}999$.
- Effet $T$ : « test positif ».
  - Sensibilité : $P_M(T) = 0{,}99$.
  - Faux positifs : $P_{\overline{M}}(T) = 1 - 0{,}99 = 0{,}01$.
- Probabilité totale d'un test positif :
  $$P(T) = P(M)P_M(T) + P(\overline{M})P_{\overline{M}}(T) = (0{,}001 \times 0{,}99) + (0{,}999 \times 0{,}01)$$
  $$= 0{,}00099 + 0{,}00999 = 0{,}01098.$$
- Probabilité d'être malade sachant le test positif :
  $$P_T(M) = \frac{P(M \cap T)}{P(T)} = \frac{0{,}00099}{0{,}01098} = \frac{99}{1098} \approx \mathbf{9{,}02\,\%}.$$
La formule retrouve instantanément le résultat de notre tableau !

---

### 6. Indépendance : le hasard sans mémoire

Quand deux événements n'ont aucune influence l'un sur l'autre, connaître la réalisation du premier ne change absolument rien aux chances du second.

> **📐 Définition — Événements indépendants**
> Deux événements $A$ et $B$ sont dits **indépendants** si :
>
> $$\boxed{P(A \cap B) = P(A) \times P(B)}$$
>
> Si $P(A) > 0$, cela équivaut à :
> $$P_A(B) = P(B).$$

> **⚠️ Attention, piège absolu ! — Ne confonds jamais « indépendants » et « disjoints »**
> C'est l'erreur numéro un au lycée !
> - Deux événements sont **disjoints** (incompatibles) s'ils ne peuvent pas se produire en même temps : $A \cap B = \varnothing$, donc $P(A \cap B) = 0$.
> - Deux événements sont **indépendants** si la réalisation de l'un n'influence pas l'autre : $P(A \cap B) = P(A) \times P(B)$.
>
> Deux événements de probabilités non nulles qui sont disjoints ne sont **JAMAIS indépendants** ! Au contraire, ils sont hyper-dépendants : si $A$ se produit, on est certain à 100 % que $B$ ne s'est pas produit ($P_A(B) = 0 \neq P(B)$) !

---

### 7. Les variables aléatoires discrètes

Jusqu'ici, les issues du hasard étaient des mots ou des événements : « pile », « face », « malade », « carte rouge ».
Une **variable aléatoire** fait franchir un pas immense à l'analyse : elle associe à chaque issue **un nombre réel** (un gain d'argent, un nombre de clients, une durée d'attente).

> **📐 Définition — Variable aléatoire**
> Une **variable aléatoire discrète** $X$ sur un univers $\Omega$ est une fonction qui associe un nombre réel $x_i$ à chaque issue élémentaire de $\Omega$.
> On note $X(\Omega) = \{x_1, x_2, \dots, x_k\}$ l'ensemble des valeurs possibles prises par $X$.

#### 7.1 La loi de probabilité

Définir la **loi de probabilité** d'une variable aléatoire $X$, c'est déterminer pour chaque valeur $x_i$ la probabilité de l'événement $(X = x_i)$. On la présente sous forme de tableau :

| $x_i$ | $x_1$ | $x_2$ | $\dots$ | $x_k$ | **Total** |
|---|---|---|---|---|---|
| $P(X = x_i)$ | $p_1$ | $p_2$ | $\dots$ | $p_k$ | **1** |

La somme des probabilités doit toujours être égale à 1 : $\sum_{i=1}^k p_i = 1$.

#### 7.2 L'espérance mathématique : le juste prix d'un jeu

Imagine une loterie foraine : que peux-tu espérer gagner en moyenne par ticket si tu joues des millions de fois ?

> **📐 Définition — Espérance mathématique**
> L'**espérance mathématique** d'une variable aléatoire discrète $X$, notée $E(X)$, est la moyenne pondérée des valeurs prises par $X$ :
>
> $$\boxed{E(X) = \sum_{i=1}^k x_i \cdot P(X = x_i)}$$

- Si $X$ représente le gain algébrique d'un joueur (gain reçu moins la mise) :
  - $E(X) > 0$ : le jeu est **favorable** au joueur.
  - $E(X) < 0$ : le jeu est **défavorable** au joueur (c'est le cas de tous les jeux de casino et de la Française des Jeux !).
  - $E(X) = 0$ : le jeu est dit **équitable**.

#### 7.3 Variance et Écart-Type d'une variable aléatoire

De même qu'en statistique descriptive au chapitre 41, on mesure le risque et la dispersion des gains :

> **📐 Définition — Variance et Écart-type**
> - La **variance** de $X$ est :
>   $$\boxed{V(X) = E\big((X - E(X))^2\big) = \sum_{i=1}^k (x_i - E(X))^2 P(X = x_i)}$$
> - Formule de König-Huygens probabiliste :
>   $$\boxed{V(X) = E(X^2) - \big(E(X)\big)^2}$$
> - L'**écart-type** est :
>   $$\boxed{\sigma(X) = \sqrt{V(X)}}$$

#### 7.4 Propriétés fondamentales de linéarité

> **📐 Théorème — Transformation affine d'une variable aléatoire**
> Pour tous réels $a$ et $b$ :
>
> 1. $\boxed{E(aX + b) = aE(X) + b}$  (Linéarité de l'espérance)
> 2. $\boxed{V(aX + b) = a^2 V(X)}$
> 3. $\boxed{\sigma(aX + b) = |a|\sigma(X)}$

> **✍️ Démonstration de la linéarité**
> $$E(aX + b) = \sum_{i=1}^k (a x_i + b) p_i = \sum_{i=1}^k a x_i p_i + \sum_{i=1}^k b p_i = a \sum_{i=1}^k x_i p_i + b \sum_{i=1}^k p_i.$$
> Or $\sum x_i p_i = E(X)$ et $\sum p_i = 1$.
> Donc $E(aX + b) = aE(X) + b \times 1 = aE(X) + b. \quad \blacksquare$

---

### Exemples résolus pas à pas

> **✅ Exemple résolu 1 — Calcul de probabilité conditionnelle simple**
> Dans une classe de 32 élèves, 18 font de l'espagnol, 10 font de l'allemand, et 6 font les deux langues.
> On choisit un élève au hasard.
> 1. Quelle est la probabilité qu'il fasse de l'allemand ?
> 2. L'élève choisi fait de l'espagnol. Quelle est la probabilité qu'il fasse aussi de l'allemand ?
>
> **Solution détaillée :**
> Notons $E$ l'événement « faire espagnol » et $A$ « faire allemand ».
> $P(E) = \frac{18}{32}$, $P(A) = \frac{10}{32}$, et $P(E \cap A) = \frac{6}{32}$.
> 1. $P(A) = \frac{10}{32} = \frac{5}{16} = 0{,}3125$.
> 2. On cherche $P_E(A)$ (univers réduit aux élèves d'espagnol) :
>    $$P_E(A) = \frac{P(E \cap A)}{P(E)} = \frac{6/32}{18/32} = \frac{6}{18} = \frac{1}{3} \approx 0{,}333.$$

> **✅ Exemple résolu 2 — Arbre pondéré et probabilités totales**
> Une entreprise s'approvisionne en puces électroniques auprès de deux fournisseurs :
> - Le fournisseur $A$ fournit 70 % des puces. Parmi elles, 2 % sont défectueuses.
> - Le fournisseur $B$ fournit les 30 % restants. Parmi elles, 5 % sont défectueuses.
> On prélève une puce au hasard dans le stock.
> 1. Construire l'arbre pondéré.
> 2. Calculer la probabilité que la puce soit défectueuse.
> 3. La puce prélevée est défectueuse. Quelle est la probabilité qu'elle provienne du fournisseur $B$ ?
>
> **Solution détaillée :**
> 1. Données : $P(A) = 0{,}70$ et $P(B) = 0{,}30$.
>    $P_A(D) = 0{,}02$ et $P_B(D) = 0{,}05$.
> 2. D'après la formule des probabilités totales avec la partition $\{A ; B\}$ :
>    $$P(D) = P(A \cap D) + P(B \cap D) = P(A) \times P_A(D) + P(B) \times P_B(D)$$
>    $$P(D) = (0{,}70 \times 0{,}02) + (0{,}30 \times 0{,}05) = 0{,}014 + 0{,}015 = 0{,}029 = 2{,}9\,\%.$$
> 3. Formule de Bayes : on cherche $P_D(B)$ :
>    $$P_D(B) = \frac{P(B \cap D)}{P(D)} = \frac{0{,}015}{0{,}029} = \frac{15}{29} \approx 0{,}5172 = 51{,}7\,\%.$$
>    Bien que le fournisseur $B$ ne livre que 30 % des composants, il est responsable de plus de la moitié des pièces défectueuses !

> **✅ Exemple résolu 3 — Test de l'indépendance**
> On lance deux dés cubiques équilibrés à 6 faces, un rouge et un bleu.
> On note $A$ : « le dé rouge donne 4 » et $B$ : « la somme des deux dés vaut 7 ».
> Les événements $A$ et $B$ sont-ils indépendants ?
>
> **Solution détaillée :**
> Il y a $6 \times 6 = 36$ issues équiprobables.
> - Pour $A$ : 6 issues $(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)$, donc $P(A) = \frac{6}{36} = \frac{1}{6}$.
> - Pour $B$ : les paires donnant 7 sont $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$, soit 6 issues. Donc $P(B) = \frac{6}{36} = \frac{1}{6}$.
> - Pour $A \cap B$ : il n'y a qu'une seule issue où le dé rouge vaut 4 et la somme vaut 7 : c'est l'issue $(4, 3)$.
>   Donc $P(A \cap B) = \frac{1}{36}$.
> - Vérifions le produit :
>   $P(A) \times P(B) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.
> - Comme $P(A \cap B) = P(A) \times P(B)$, **les événements $A$ et $B$ sont rigoureusement indépendants** !
>   Savoir que le dé rouge donne 4 ne modifie en rien la probabilité que la somme fasse 7.

> **✅ Exemple résolu 4 — Variable aléatoire et espérance d'un jeu**
> Un forain propose le jeu suivant pour une mise de 5 € :
> On lance un dé équilibré à 6 faces :
> - Si l'on obtient un 6, on reçoit 20 € (gain net : $+15$ €).
> - Si l'on obtient un 4 ou un 5, on reçoit 6 € (gain net : $+1$ €).
> - Si l'on obtient 1, 2 ou 3, on ne reçoit rien (gain net : $-5$ €).
> 1. Définir la variable aléatoire $X$ représentant le gain net du joueur et donner sa loi de probabilité.
> 2. Calculer son espérance. Le jeu est-il favorable au forain ou au joueur ?
>
> **Solution détaillée :**
> 1. Les valeurs possibles de $X$ sont $X(\Omega) = \{-5 ; 1 ; 15\}$.
>    - $P(X = 15) = P(\{6\}) = \frac{1}{6}$
>    - $P(X = 1) = P(\{4; 5\}) = \frac{2}{6} = \frac{1}{3}$
>    - $P(X = -5) = P(\{1; 2; 3\}) = \frac{3}{6} = \frac{1}{2}$
>    Vérification : $\frac{1}{6} + \frac{2}{6} + \frac{3}{6} = 1$.
>
> 2. Espérance mathématique :
>    $$E(X) = \left(-5 \times \frac{3}{6}\right) + \left(1 \times \frac{2}{6}\right) + \left(15 \times \frac{1}{6}\right) = \frac{-15 + 2 + 15}{6} = \frac{2}{6} = +\frac{1}{3} \approx +0{,}33\text{ €}.$$
>    Comme $E(X) > 0$, le jeu est **favorable au joueur** ! En moyenne, le joueur gagne 33 centimes par partie. Le forain va rapidement faire faillite s'il ne modifie pas les règles !

> **✅ Exemple résolu 5 — Variance et écart-type d'une variable aléatoire**
> Calculer la variance $V(X)$ et l'écart-type $\sigma(X)$ pour le jeu de l'exemple 4.
>
> **Solution détaillée :**
> 1. Calculons $E(X^2)$ :
>    $$E(X^2) = (-5)^2 \times \frac{3}{6} + (1)^2 \times \frac{2}{6} + (15)^2 \times \frac{1}{6}$$
>    $$= 25 \times \frac{3}{6} + 1 \times \frac{2}{6} + 225 \times \frac{1}{6} = \frac{75 + 2 + 225}{6} = \frac{302}{6} = \frac{151}{3} \approx 50{,}33.$$
> 2. Formule de König-Huygens :
>    $$V(X) = E(X^2) - (E(X))^2 = \frac{151}{3} - \left(\frac{1}{3}\right)^2 = \frac{453}{9} - \frac{1}{9} = \frac{452}{9} \approx 50{,}22.$$
> 3. Écart-type :
>    $$\sigma(X) = \sqrt{\frac{452}{9}} = \frac{\sqrt{452}}{3} \approx 7{,}09\text{ €}.$$
>    L'écart-type est élevé : les gains subissent de fortes variations autour de la moyenne.

> **✅ Exemple résolu 6 — Linéarité de l'espérance**
> Une compagnie d'assurance garantit des flottes de vélos en libre-service. Le nombre de vélos accidentés par jour $X$ a une espérance $E(X) = 4$ et un écart-type $\sigma(X) = 1{,}5$.
> Chaque accident coûte 50 € de réparation, auxquels s'ajoute un forfait d'astreinte quotidien de 100 €.
> Le coût quotidien total est donc $Y = 50X + 100$.
> Déterminer l'espérance et l'écart-type du coût quotidien pour l'assureur.
>
> **Solution détaillée :**
> - Espérance : par linéarité :
>   $$E(Y) = E(50X + 100) = 50E(X) + 100 = 50(4) + 100 = 200 + 100 = 300\text{ €}.$$
> - Écart-type :
>   $$\sigma(Y) = \sigma(50X + 100) = |50| \times \sigma(X) = 50 \times 1{,}5 = 75\text{ €}.$$
> L'assureur doit provisionner en moyenne 300 € par jour, avec une fluctuation type de 75 €.

---

### Ce qu'il faut retenir

1. **Probabilité conditionnelle :**
   - $P_A(B) = \frac{P(A \cap B)}{P(A)}$ (univers réduit à $A$).
   - Règle du produit : $P(A \cap B) = P(A) \times P_A(B)$.

2. **Arbre pondéré et probabilités totales :**
   - Somme des branches d'un nœud = 1.
   - Probabilité d'un chemin = produit des branches.
   - Formule des probabilités totales : $P(B) = P(A)P_A(B) + P(\overline{A})P_{\overline{A}}(B)$.

3. **Formule de Bayes (inversion des conditionnements) :**
   - $P_B(A) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)P_A(B)}{P(A)P_A(B) + P(\overline{A})P_{\overline{A}}(B)}$.

4. **Indépendance :**
   - $A$ et $B$ indépendants $\iff P(A \cap B) = P(A) \times P(B) \iff P_A(B) = P(B)$.
   - Deux événements disjoints non impossibles ne sont jamais indépendants.

5. **Variables aléatoires :**
   - Espérance : $E(X) = \sum x_i p_i$. Linéarité : $E(aX+b) = aE(X)+b$.
   - Variance : $V(X) = E(X^2) - (E(X))^2$. Propriété : $V(aX+b) = a^2 V(X)$.
   - Écart-type : $\sigma(X) = \sqrt{V(X)}$. Propriété : $\sigma(aX+b) = |a|\sigma(X)$.

---

### Exercices

#### Niveau ★ (Applications directes, arbres simples)

1. On donne $P(A) = 0{,}4$, $P(B) = 0{,}5$ et $P(A \cap B) = 0{,}2$.
   Calculer $P_A(B)$ et $P_B(A)$. Les événements $A$ et $B$ sont-ils indépendants ?
2. On donne $P(A) = 0{,}6$ et $P_A(B) = 0{,}3$. Calculer $P(A \cap B)$.
3. Dans un arbre, une branche vers $A$ a une probabilité $0{,}7$. De $A$ partent deux branches vers $B$ et $\overline{B}$. Sachant que $P_A(B) = 0{,}4$, donner $P_A(\overline{B})$.
4. On tire une carte au hasard dans un jeu de 32 cartes. On note $R$ : « la carte est un Roi » et $C$ : « la carte est un Cœur ». $R$ et $C$ sont-ils indépendants ?
5. Soit une variable aléatoire $X$ dont la loi est donnée par :
   | $x_i$ | -2 | 0 | 3 |
   |---|---|---|---|
   | $P(X=x_i)$ | 0,3 | 0,5 | $p$ |
   Déterminer $p$, puis calculer $E(X)$.
6. On donne $E(X) = 5$ et $V(X) = 4$. Soit $Y = 3X - 2$. Calculer $E(Y)$, $V(Y)$ et $\sigma(Y)$.
7. Un sac contient 3 boules blanches et 2 boules noires. On tire successivement deux boules sans remise. Calculer la probabilité d'obtenir deux boules blanches.
8. Un QCM comporte 4 choix dont un seul est correct. Un candidat répond au hasard. Quelle est la probabilité qu'il trouve la bonne réponse sachant qu'il a déjà éliminé deux réponses fausses ?

#### Niveau ★★ (Arbres complets, Bayes et variables aléatoires)

9. Dans une usine textile, trois machines $M_1, M_2, M_3$ produisent respectivement 50 %, 30 % et 20 % des vêtements.
   Le taux de défauts est de 3 % pour $M_1$, 4 % pour $M_2$ et 5 % pour $M_3$.
   a) Calculer la probabilité qu'un vêtement choisi au hasard soit défectueux.
   b) Un vêtement est défectueux. Quelle est la probabilité qu'il provienne de la machine $M_1$ ?
10. Démontrer que si $A$ et $B$ sont deux événements indépendants, alors les événements $A$ et $\overline{B}$ sont également indépendants.
11. On lance une pièce équilibrée 3 fois de suite. Soit $X$ le nombre de « Face » obtenus.
    a) Déterminer les valeurs possibles de $X$ et établir sa loi de probabilité.
    b) Calculer $E(X)$ et $V(X)$.
12. Un jeu payant coûte 2 € la partie. On lance un dé équilibré :
    - Si le résultat est pair, on gagne 3 € (gain net : $+1$ €).
    - Si le résultat est 5, on gagne 6 € (gain net : $+4$ €).
    - Sinon, on ne gagne rien (gain net : $-2$ €).
    Le jeu est-il équitable ?
13. On lance deux dés cubiques. On note $A$ : « le premier dé donne un chiffre pair » et $B$ : « la somme des deux dés est impaire ».
    Montrer que $A$ et $B$ sont indépendants.
14. Dans une population, 60 % des personnes sont vaccinées contre la grippe. L'efficacité du vaccin est de 80 % (la probabilité d'attraper la grippe en étant vacciné est 5 fois plus faible). Le taux de grippe chez les non-vaccinés est de 25 %.
    a) Calculer le taux global de malades dans la population.
    b) Une personne attrape la grippe. Quelle est la probabilité qu'elle soit vaccinée ?
15. Soit une variable aléatoire $X$ telle que $E(X) = 10$ et $E(X^2) = 116$.
    Calculer la variance $V(X)$ et l'écart-type $\sigma(X)$.
16. Simulation Python : Écrire un script simulant 10 000 parties du jeu de l'exercice 12 et calculant la moyenne empirique des gains pour vérifier l'espérance théorique.

#### Niveau ★★★ (Défis et problèmes ouverts)

17. **Le paradoxe des deux enfants (Lewis Carroll / Martin Gardner) :**
    Une famille a deux enfants. On suppose que chaque enfant a une chance sur deux d'être une fille ou un garçon, de façon indépendante.
    a) On sait que l'aîné est une fille. Quelle est la probabilité que les deux enfants soient des filles ?
    b) On sait qu'au moins l'un des deux enfants est une fille. Quelle est la probabilité que les deux enfants soient des filles ? Expliquer le paradoxe.
18. **Le problème de Monty Hall (le jeu télévisé des trois portes) :**
    Dans un jeu télévisé, trois portes fermées $A, B, C$ vous font face. Derrière l'une se trouve une voiture de luxe ; derrière les deux autres, des chèvres.
    1. Vous choisissez la porte $A$.
    2. L'animateur, qui sait où se trouve la voiture, ouvre une des deux autres portes (par exemple la porte $B$) et dévoile une chèvre.
    3. Il vous demande alors : *« Souhaitez-vous garder la porte $A$ ou changer pour la porte $C$ ? »*
    En utilisant les probabilités conditionnelles, prouver rigoureusement pourquoi il faut absolument changer de porte pour doubler ses chances de gagner !
19. **La ruine du joueur :**
    Un joueur possède 2 € et joue à pile ou face contre la banque avec une pièce équilibrée. À chaque lancer, il gagne 1 € avec probabilité 0,5 ou perd 1 € avec probabilité 0,5. Le jeu s'arrête s'il atteint 4 € (victoire) ou s'il tombe à 0 € (ruine).
    Calculer la probabilité de ruine du joueur en posant un système d'équations de récurrence sur les probabilités conditionnelles.
20. **Loi géométrique tronquée :**
    On lance un dé équilibré jusqu'à obtenir un 6, avec un arrêt forcé au bout de 4 lancers maximum. Soit $X$ le nombre de lancers effectués.
    a) Donner la loi de probabilité de $X$.
    b) Calculer l'espérance $E(X)$.

---

### Solutions

**1.** $P_A(B) = \frac{P(A \cap B)}{P(A)} = \frac{0{,}2}{0{,}4} = 0{,}5$.
$P_B(A) = \frac{P(A \cap B)}{P(B)} = \frac{0{,}2}{0{,}5} = 0{,}4$.
$P(A) \times P(B) = 0{,}4 \times 0{,}5 = 0{,}2 = P(A \cap B)$. Oui, les événements sont indépendants !

**2.** $P(A \cap B) = P(A) \times P_A(B) = 0{,}6 \times 0{,}3 = 0{,}18$.

**3.** Somme des branches d'un nœud égale à 1 : $P_A(\overline{B}) = 1 - P_A(B) = 1 - 0{,}4 = 0{,}6$.

**4.** $P(R) = \frac{4}{32} = \frac{1}{8}$. $P(C) = \frac{8}{32} = \frac{1}{4}$.
$R \cap C$ est le Roi de Cœur : $P(R \cap C) = \frac{1}{32}$.
Or $P(R) \times P(C) = \frac{1}{8} \times \frac{1}{4} = \frac{1}{32}$. Les deux événements sont indépendants.

**5.** Somme des probabilités = 1 : $0{,}3 + 0{,}5 + p = 1 \implies p = 0{,}2$.
$E(X) = (-2 \times 0{,}3) + (0 \times 0{,}5) + (3 \times 0{,}2) = -0{,}6 + 0 + 0{,}6 = 0$.

**6.** $E(Y) = 3E(X) - 2 = 3(5) - 2 = 13$.
$V(Y) = 3^2 V(X) = 9 \times 4 = 36$.
$\sigma(Y) = \sqrt{36} = 6$ (ou $|3| \times \sqrt{4} = 3 \times 2 = 6$).

**7.** $P(B_1) = \frac{3}{5}$. Sachant qu'une blanche a été tirée, il reste 2 blanches sur 4 boules : $P_{B_1}(B_2) = \frac{2}{4} = \frac{1}{2}$.
$P(B_1 \cap B_2) = \frac{3}{5} \times \frac{1}{2} = \frac{3}{10} = 0{,}30$.

**8.** L'univers est réduit aux deux choix restants, un seul étant le bon : $P = \frac{1}{2} = 50\,\%$.

**9.**
a) Probabilités totales :
$P(D) = P(M_1)P_{M_1}(D) + P(M_2)P_{M_2}(D) + P(M_3)P_{M_3}(D)$
$P(D) = (0{,}50 \times 0{,}03) + (0{,}30 \times 0{,}04) + (0{,}20 \times 0{,}05) = 0{,}015 + 0{,}012 + 0{,}010 = 0{,}037 = 3{,}7\,\%$.
b) Bayes : $P_D(M_1) = \frac{P(M_1 \cap D)}{P(D)} = \frac{0{,}015}{0{,}037} = \frac{15}{37} \approx 0{,}4054 = 40{,}54\,\%$.

**10.** D'après la formule des probabilités totales : $P(A) = P(A \cap B) + P(A \cap \overline{B})$.
Donc $P(A \cap \overline{B}) = P(A) - P(A \cap B)$.
Comme $A$ et $B$ sont indépendants, $P(A \cap B) = P(A)P(B)$.
Substituons : $P(A \cap \overline{B}) = P(A) - P(A)P(B) = P(A)(1 - P(B)) = P(A)P(\overline{B})$.
L'égalité prouve que $A$ et $\overline{B}$ sont indépendants.

**11.**
a) $X \in \{0, 1, 2, 3\}$. Il y a $2^3 = 8$ issues équiprobables.
- $P(X=0) = P(\{PPP\}) = \frac{1}{8}$
- $P(X=1) = P(\{FPP, PFP, PPF\}) = \frac{3}{8}$
- $P(X=2) = P(\{FFP, FPF, PFF\}) = \frac{3}{8}$
- $P(X=3) = P(\{FFF\}) = \frac{1}{8}$
b) $E(X) = 0(\frac{1}{8}) + 1(\frac{3}{8}) + 2(\frac{3}{8}) + 3(\frac{1}{8}) = \frac{0 + 3 + 6 + 3}{8} = \frac{12}{8} = 1{,}5$.
$E(X^2) = 0^2(\frac{1}{8}) + 1^2(\frac{3}{8}) + 2^2(\frac{3}{8}) + 3^2(\frac{1}{8}) = \frac{0 + 3 + 12 + 9}{8} = \frac{24}{8} = 3$.
$V(X) = E(X^2) - (E(X))^2 = 3 - (1{,}5)^2 = 3 - 2{,}25 = 0{,}75 = \frac{3}{4}$.

**12.** Notons $G$ le gain net : $G \in \{+1 ; +4 ; -2\}$.
- Résultats pairs : $\{2, 4, 6\} \implies P(G = 1) = \frac{3}{6} = \frac{1}{2}$.
- Résultat 5 : $\{5\} \implies P(G = 4) = \frac{1}{6}$.
- Autres (1 et 3) : $\{1, 3\} \implies P(G = -2) = \frac{2}{6} = \frac{1}{3}$.
Espérance :
$E(G) = \left(1 \times \frac{3}{6}\right) + \left(4 \times \frac{1}{6}\right) + \left(-2 \times \frac{2}{6}\right) = \frac{3 + 4 - 4}{6} = \frac{3}{6} = +0{,}50\text{ €}$.
Le jeu n'est pas équitable ($E(G) \neq 0$) : il est favorable au joueur qui gagne en moyenne 50 centimes par partie.

**13.** $P(A) = \frac{3}{6} = \frac{1}{2}$.
Pour la somme impaire : elle est impaire si un dé est pair et l'autre impair. Il y a 18 issues sur 36, donc $P(B) = \frac{18}{36} = \frac{1}{2}$.
$A \cap B$ : le 1er dé est pair ET la somme est impaire, ce qui équivaut à : 1er dé pair ET 2nd dé impair.
Il y a $3 \times 3 = 9$ issues sur 36. Donc $P(A \cap B) = \frac{9}{36} = \frac{1}{4}$.
Comme $P(A) \times P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = P(A \cap B)$, les événements sont indépendants.

**14.**
a) $P(V) = 0{,}60$ et $P(\overline{V}) = 0{,}40$.
Taux chez non-vaccinés : $P_{\overline{V}}(M) = 0{,}25$.
Taux chez vaccinés : 5 fois plus faible $\implies P_V(M) = \frac{0{,}25}{5} = 0{,}05$.
$P(M) = P(V)P_V(M) + P(\overline{V})P_{\overline{V}}(M) = (0{,}60 \times 0{,}05) + (0{,}40 \times 0{,}25) = 0{,}03 + 0{,}10 = 0{,}13 = 13\,\%$.
b) Bayes : $P_M(V) = \frac{P(V \cap M)}{P(M)} = \frac{0{,}03}{0{,}13} = \frac{3}{13} \approx 23{,}08\,\%$.
(La grande majorité des malades, soit près de 77 %, sont non-vaccinés).

**15.** $V(X) = E(X^2) - (E(X))^2 = 116 - 10^2 = 116 - 100 = 16$.
$\sigma(X) = \sqrt{16} = 4$.

**16.**
```python
import random


def simuler_jeu(nb_parties=10000):
  gains = []
  for _ in range(nb_parties):
    de = random.randint(1, 6)
    if de in [2, 4, 6]:
      gain = 1  # 3 - 2
    elif de == 5:
      gain = 4  # 6 - 2
    else:
      gain = -2  # 0 - 2
    gains.append(gain)
  moyenne = sum(gains) / nb_parties
  print(f"Moyenne simulée : {moyenne:.4f} € (Théorie : 0.5000 €)")


simuler_jeu()
```

**17.**
L'univers des familles de 2 enfants est $\Omega = \{(G, G), (G, F), (F, G), (F, F)\}$, avec 4 issues équiprobables (1er enfant, 2nd enfant).
a) L'événement « l'aîné est une fille » est $A = \{(F, G), (F, F)\}$.
Dans cet univers réduit à 2 éléments, la probabilité que les deux soient des filles est $\frac{1}{2} = 50\,\%$.
b) L'événement « au moins un enfant est une fille » est $B = \{(G, F), (F, G), (F, F)\}$.
Cet univers réduit compte **3 éléments**. Un seul correspond à deux filles : $(F, F)$.
La probabilité est donc $\frac{1}{3} \approx 33{,}3\,\%$ !
Le paradoxe vient du fait que « au moins une fille » apporte moins d'information que « l'aîné est une fille » : l'ordre n'est pas spécifié.

**18.**
- Lorsque vous choisissez la porte $A$ au début, vous avez $P(\text{Voiture en } A) = \frac{1}{3}$.
  La probabilité que la voiture soit derrière l'une des deux autres portes ($B$ ou $C$) est de $\frac{2}{3}$.
- L'animateur ouvre alors délibérément une porte avec une chèvre parmi $B$ et $C$. Il ne choisit pas au hasard : il élimine la mauvaise porte.
- La probabilité $\frac{2}{3}$ qui pesait sur le bloc $\{B, C\}$ se concentre désormais **entièrement sur la porte restante $C$** !
- Si vous gardez $A$, votre probabilité de gagner reste de $\frac{1}{3}$.
- Si vous changez pour $C$, votre probabilité de gagner passe à $\frac{2}{3}$.
Il faut donc changer de porte : cela double vos chances !

**19.** Notons $p_k$ la probabilité de se ruiner en partant d'une fortune de $k$ euros (pour $k \in \{0, 1, 2, 3, 4\}$).
Par hypothèse : $p_0 = 1$ (déjà ruiné) et $p_4 = 0$ (victoire atteinte).
Pour $k \in \{1, 2, 3\}$, après un lancer :
$p_k = 0{,}5 p_{k+1} + 0{,}5 p_{k-1} \iff 2p_k = p_{k+1} + p_{k-1} \iff p_{k+1} - p_k = p_k - p_{k-1}$.
La suite $(p_k)$ est donc arithmétique !
Comme $p_0 = 1$ et $p_4 = 0$, la raison est $r = \frac{0 - 1}{4} = -0{,}25$.
Donc $p_1 = 0{,}75$, $p_2 = 0{,}50$, $p_3 = 0{,}25$.
En partant avec 2 €, la probabilité de ruine est exactement $p_2 = 0{,}50 = 50\,\%$.

**20.**
a) Le succès (obtenir 6) a une probabilité $p = \frac{1}{6}$, l'échec a une probabilité $q = \frac{5}{6}$.
- $P(X=1) = \frac{1}{6}$.
- $P(X=2) = \frac{5}{6} \times \frac{1}{6} = \frac{5}{36}$.
- $P(X=3) = \left(\frac{5}{6}\right)^2 \times \frac{1}{6} = \frac{25}{216}$.
- $P(X=4)$ : on s'arrête au 4ᵉ lancer qu'on ait obtenu un 6 ou non, ce qui correspond à avoir échoué les 3 premiers lancers : $P(X=4) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}$.
Vérification : $\frac{36 + 30 + 25 + 125}{216} = \frac{216}{216} = 1$.
b) $E(X) = 1\left(\frac{36}{216}\right) + 2\left(\frac{30}{216}\right) + 3\left(\frac{25}{216}\right) + 4\left(\frac{125}{216}\right) = \frac{36 + 60 + 75 + 500}{216} = \frac{671}{216} \approx 3{,}106$ lancers.

---

### La question qui ouvre la suite

Nous voici parvenus au terme du Volume V.
De la corde de halage au cabinet du médecin, nous avons appris à manier les vecteurs, à mesurer les pentes instantanées avec les dérivées, à décrire la prolifération exponentielle et à dompter le hasard.
Mais regarde bien la route qui monte vers le sommet : que se passe-t-il si l'on répète une expérience non pas 4 fois, mais une infinité de fois ? Comment prouver une vérité pour tous les entiers d'un coup grâce à la **récurrence** ? Comment calculer l'aire d'une surface courbée en empilant une infinité de tranches d'eau ?
C'est le royaume ultime du **Volume VI : L'Âge du Flux et de la Vitesse**, qui t'attend dès le prochain chapitre !
