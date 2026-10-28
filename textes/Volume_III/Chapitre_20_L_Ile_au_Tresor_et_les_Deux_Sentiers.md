# VOLUME III — L'ÂGE DES ARPENTEURS ET DES BÂTISSEURS (10 - 13 ans / CM2 - 6e - 5e)
## CHAPITRE 20 : L'Île au Trésor et les Deux Sentiers

> *« Un nombre seul ne sait que mesurer la distance en ligne droite sur un sentier unique. Mais pour retrouver un coffre dans la plaine, guider un navire dans le brouillard ou cartographier chaque étoile du ciel, il faut ouvrir le monde en deux dimensions et marier l'algèbre à la géométrie. »*

---

### Ce que tu vas découvrir

- Le mystère de la carte au trésor et la mouche au plafond de **René Descartes**.
- Le **repère cartésien** : l'axe horizontal des **abscisses** ($x$), l'axe vertical des **ordonnées** ($y$) et les **quatre quadrants**.
- Comment lire et placer les **coordonnées** d'un point $(x\,;\,y)$ sans jamais les intervertir.
- La formule du **milieu d'un segment** : la simple moyenne des coordonnées.
- Le calcul de la **distance entre deux points** dans un repère grâce au théorème de Pythagore : $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.
- La **multiplication et la division des nombres relatifs** : pourquoi « moins par moins donne plus », démontrée par la marche arrière dans le temps et par la distributivité !

---

### 1. Le problème : la carte au trésor et l'angoisse du cercle

Imagine que tu viennes de débarquer sur une île sauvage de l'océan Indien.
Dans ta main crispée, tu tiens le vieux parchemin jauni d'un flibustier. L'encre est presque effacée par l'eau de mer, mais tu parviens à déchiffrer ces quelques mots tracés à la plume :
*« Le coffre aux pièces d'or est enterré à très exactement 50 mètres du grand menhir de pierre noire qui domine la plage. »*

Ton cœur bondit dans ta poitrine. Tu cours vers le menhir de pierre noire.
Tu plantes tes talons contre la roche, tu regardes devant toi et tu fais 50 mètres en direction de la forêt : tu sors ta pelle et tu commences à creuser frénétiquement dans le sable.
Tu creuses pendant une heure sous un soleil de plomb. Rien ! Pas le moindre coffre.

Tu t'arrêtes, épuisé, et tu réalises ton erreur tragique :
Le pirate a écrit : *« à 50 mètres du menhir »*.
Mais dans quelle direction ?
- À 50 mètres vers le Nord ?
- À 50 mètres vers l'Est, dans les vagues de l'océan ?
- À 50 mètres vers l'Ouest, sous les racines d'un grand bananier ?

```
                             50 m vers le Nord
                                     ●
                                   /   \
                                 /       \
     50 m vers l'Ouest ● ─── [ Menhir ] ─── ● 50 m vers l'Est
                                 \       /
                                   \   /
                                     ●
                             50 m vers le Sud
```

Comme nous l'avons appris au Chapitre 16, tous les points situés à 50 mètres du menhir forment **un cercle immense tout autour de la pierre** !
Si tu dois creuser tout le long de ce cercle, il te faudra creuser une tranchée de plus de 314 mètres de long. Le jour où tu auras fini, tu seras devenu un vieillard à barbe blanche !

Un seul nombre ne suffit pas pour désigner une position dans un plan.
Pour localiser un objet sans la moindre hésitation, il faut **deux informations indépendantes**.

---

### 2. La Mouche au Plafond de René Descartes

Pour résoudre cette énigme, quittons notre île aux flibustiers et faisons un bond dans le temps jusqu'au rude hiver de **1637**, en France.

Dans une chambre d'une vieille maison de briques, un homme de quarante ans est encore couché sous ses draps de plume au milieu de la matinée. Il s'appelle **René Descartes**.
Descartes a une santé fragile depuis son enfance, et ses professeurs du collège royal lui ont toujours accordé le privilège de rester au lit le matin pour se reposer et méditer tranquillement.

Alors qu'il regarde en l'air, une petite mouche noire vient se poser sur le plafond de plâtre blanc.
La mouche marche, s'arrête, redécolle et se pose un peu plus loin.
Descartes se pose alors une question que personne avant lui n'avait formulée ainsi :
*« Comment pourrais-je décrire la position exacte de cette mouche à un ami sans avoir besoin de monter sur un escabeau pour la pointer du doigt ? »*

```
     Mur du fond (Axe vertical Oy)
          ▲
          |
        4 |            ● Mouche M (3 ; 4)
        3 |            :
        2 |            :
        1 |            :
          +------------+------------► Mur de droite (Axe horizontal Ox)
          O   1   2    3    4    5
        Coin de
        la pièce
```

Descartes regarde les deux murs perpendiculaires qui se croisent dans le coin de sa chambre :
1. Il mesure la distance entre la mouche et le **mur de gauche** : disons **3 mètres**.
2. Il mesure la distance entre la mouche et le **mur du fond** : disons **4 mètres**.

*« C'est lumineux ! »* s'écrie Descartes. Le couple de nombres $(3\,;\,4)$ suffit à fixer la position de la mouche sans aucune ambiguïté possible !
Deux nombres pour repérer un point dans un espace à deux dimensions : Descartes venait d'inventer le **repère cartésien**.

---

### 3. Le Repère cartésien et les Quatre Quadrants

#### 3.1 Anatomie du repère

Sur une feuille à petits carreaux, nous traçons deux droites graduées perpendiculaires qui se coupent en leur zéro commun :

```
                                  Axe des ordonnées (y)
                                           ▲
                                         3 |       Quadrant II         Quadrant I
                                         2 |         (- , +)             (+ , +)
                                         1 |
     Axe des ◄───┼────┼────┼────┼────┼─────┼─────┼────┼────┼────┼────┼───► abscisses (x)
                 -5   -4   -3   -2   -1    O|    1    2    3    4    5
                                        -1 |
                                        -2 |       Quadrant III        Quadrant IV
                                        -3 |         (- , -)             (+ , -)
                                           ▼
```

> **📐 Définitions fondamentales — Le vocabulaire officiel**
> - Le point de croisement des deux axes est l'**origine**, notée $O$. Ses coordonnées sont $(0\,;\,0)$.
> - L'axe horizontal est l'**axe des abscisses** (noté souvent axe $(Ox)$). L'abscisse mesure le déplacement **gauche / droite**.
> - L'axe vertical est l'**axe des ordonnées** (noté souvent axe $(Oy)$). L'ordonnée mesure le déplacement **bas / haut**.
> - Un repère est dit **orthogonal** si les deux axes sont perpendiculaires. Il est dit **orthonormé** si les deux axes ont la même unité de longueur (par exemple 1 carreau = 1 cm sur les deux axes).

#### 3.2 La notation des coordonnées

Pour tout point $M$, on note :
$$M(x_M\,;\,y_M)$$
- $x_M$ est l'**abscisse** de $M$.
- $y_M$ est l'**ordonnée** de $M$.

> **🧭 Méthode mnémotechnique — Pour ne jamais confondre $x$ et $y$**
> 1. **L'ordre alphabétique :** Dans l'alphabet, **A**bscisse vient avant **O**rdonnée, tout comme **$x$** vient avant **$y$**. L'abscisse est TOUJOURS écrite en premier !
> 2. **L'ascenseur de l'immeuble :** Pour rendre visite à un ami dans un grand bâtiment, tu dois d'abord marcher dans la rue jusqu'à l'entrée de son allée (**abscisse horizontale $x$**), puis prendre l'ascenseur pour monter à son étage (**ordonnée verticale $y$**). Tu ne peux pas monter dans les airs avant d'être entré dans le bâtiment !

#### 3.3 Les quatre quadrants du plan
Les deux axes découpent le plan en quatre régions :
- **Quadrant I (en haut à droite) :** $x > 0$ et $y > 0$ (positif, positif).
- **Quadrant II (en haut à gauche) :** $x < 0$ et $y > 0$ (négatif, positif).
- **Quadrant III (en bas à gauche) :** $x < 0$ et $y < 0$ (négatif, négatif).
- **Quadrant IV (en bas à droite) :** $x > 0$ et $y < 0$ (positif, négatif).

---

### 4. Deux formules magiques du repère

Dès que des points possèdent des coordonnées numériques, nous n'avons plus besoin de tracer des figures pour faire de la géométrie : le calcul algébrique résout tout !

#### 4.1 Les coordonnées du milieu d'un segment

Soient deux points $A(x_A\,;\,y_A)$ et $B(x_B\,;\,y_B)$.
Où se trouve le milieu exact $I$ du segment $[AB]$ ?
Il se trouve exactement à mi-chemin horizontalement, et à mi-chemin verticalement. C'est simplement **la moyenne arithmétique** des coordonnées !

> **📐 Propriété — Coordonnées du milieu**
> Les coordonnées du milieu $I$ du segment $[AB]$ sont :
> $$x_I = \frac{x_A + x_B}{2} \quad \text{et} \quad y_I = \frac{y_A + y_B}{2}$$

#### 4.2 La distance entre deux points : Pythagore dans le repère

Comment calculer la longueur exacte du segment $[AB]$ reliant deux points quelconques du plan ?
Regarde le dessin suivant :

```
          yB |                     ● B(xB ; yB)
             |                   / |
             |                 /   |  Δy = yB - yA (hauteur verticale)
          yA |     A(xA ; yA)●─────● C(xB ; yA)
             |                 Δx = xB - xA (base horizontale)
             +───────────────┼─────┼────────► x
                            xA    xB
```

Traçons depuis $A$ une ligne horizontale, et depuis $B$ une ligne verticale. Elles se coupent en un point $C$ en formant un **triangle rectangle $ABC$** !
- La longueur de la base horizontale est : $AC = |x_B - x_A|$.
- La longueur de la hauteur verticale est : $BC = |y_B - y_A|$.
- L'hypoténuse est le segment $[AB]$ !

Appliquons le théorème de Pythagore dans le triangle $ABC$ rectangle en $C$ :
$$AB^2 = AC^2 + BC^2 = (x_B - x_A)^2 + (y_B - y_A)^2$$

En extrayant la racine carrée, on obtient la formule universelle de la distance cartésienne :

> **📐 Théorème — Distance entre deux points dans un repère orthonormé**
> Pour tous points $A(x_A\,;\,y_A)$ et $B(x_B\,;\,y_B)$ :
> $$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

---

### 5. La multiplication des relatifs : pourquoi moins par moins donne plus ?

En travaillant dans les quatre quadrants avec des coordonnées positives et négatives, nous rencontrons un défi fondamental du calcul : comment **multiplier** des nombres relatifs ?

Si l'addition et la soustraction sont intuitives (gagner ou perdre de l'argent, monter ou descendre en température), la multiplication de deux nombres négatifs semble au premier abord un mystère impénétrable. Pourquoi $(-3) \times (-4) = +12$ ?

Voici deux démonstrations irréfutables : l'une cinématographique, l'autre purement logique.

#### 5.1 La preuve par la vidéo : le marcheur et la marche arrière

Imagine un marcheur sur une longue route graduée en mètres, filmé par une caméra :
- Sa **vitesse** :
  - Marcher vers la droite (l'avenir, le positif) : vitesse **positive** $+2\text{ m/s}$.
  - Marcher à reculons vers la gauche : vitesse **négative** $-2\text{ m/s}$.
- Le **temps** sur la bande vidéo :
  - Regarder le film défiler normalement vers l'avant : temps **positif** $+3\text{ secondes}$.
  - Faire passer le film en marche arrière : temps **négatif** $-3\text{ secondes}$.

Où se trouve le marcheur sur l'écran ?

1. **$(+2) \times (+3) = +6$ :**
   Il marche vers l'avant à $2\text{ m/s}$, on regarde 3 secondes dans le futur $\implies$ il est à **$+6\text{ mètres}$** à droite.
2. **$(-2) \times (+3) = -6$ :**
   Il marche à reculons vers la gauche à $-2\text{ m/s}$, on regarde 3 secondes dans le futur $\implies$ il est à **$-6\text{ mètres}$** à gauche.
3. **$(+2) \times (-3) = -6$ :**
   Il marche vers la droite, mais on passe le film en marche arrière 3 secondes dans le passé $\implies$ il était à **$-6\text{ mètres}$** à gauche !
4. **$(-2) \times (-3) = +6$ :**
   Il marchait à reculons vers la gauche, et l'on passe la vidéo en marche arrière dans le passé ! Que voit-on sur l'écran ? **Quelqu'un qui avance vers la droite !** Il se trouvait à **$+6\text{ mètres}$** !
   *Passer en marche arrière un film où l'on recule, c'est voir quelqu'un avancer !*

#### 5.2 La preuve par la distributivité (la preuve algébrique)

Les mathématiciens exigent une preuve sans métaphore. La voici : nous voulons que la règle fondamentale de la distributivité $k \times (a + b) = k \times a + k \times b$ reste vraie pour tous les nombres.

Calculons l'expression suivante de deux manières :
$$E = (-3) \times [4 + (-4)]$$

- **Méthode 1 :**
  Calculons d'abord l'intérieur du crochet : $4 + (-4) = 0$.
  Donc : $E = (-3) \times 0 = \mathbf{0}$.

- **Méthode 2 :**
  Développons par distributivité :
  $$E = (-3) \times 4 + (-3) \times (-4)$$
  Nous savons déjà que $(-3) \times 4 = -12$ (car 4 dettes de 3 euros font 12 euros de dette).
  L'égalité devient :
  $$0 = -12 + [(-3) \times (-4)]$$

Pose-toi la question : quel nombre faut-il ajouter à $-12$ pour obtenir zéro ?
La seule et unique réponse possible dans l'univers est **$+12$** !
Par conséquent :
$$(-3) \times (-4) = \mathbf{+12}$$
Si moins par moins ne donnait pas plus, toutes les règles du calcul algébrique s'écrouleraient !

> **📐 La Règle des signes — Multiplication et Division**
> - Le produit (ou quotient) de deux nombres de **même signe** est **POSITIF** :
>   $$(+) \times (+) = (+) \quad \text{et} \quad (-) \times (-) = (+)$$
> - Le produit (ou quotient) de deux nombres de **signes contraires** est **NÉGATIF** :
>   $$(+) \times (-) = (-) \quad \text{et} \quad (-) \times (+) = (-)$$
>
> Pour un produit de plusieurs facteurs non nuls :
> - Si le nombre de facteurs négatifs est **pair**, le produit est **positif**.
> - Si le nombre de facteurs négatifs est **impair**, le produit est **négatif**.

---

### 6. Attention aux pièges !

> **⚠️ Attention, piège ! — Ne confonds pas addition et multiplication**
> 1. **La confusion mortelle :**
>    $$-3 - 5 = \mathbf{-8} \quad (\text{on perd } 3 \text{ puis on perd } 5, \text{c'est une addition !})$$
>    $$(-3) \times (-5) = \mathbf{+15} \quad (\text{c'est une multiplication !})$$
>    Ne dis jamais « moins et moins ça fait plus » sans préciser que cela ne vaut QUE pour la multiplication et la division !
> 2. **L'inversion abscisse / ordonnée :**
>    Le point $A(2\,;\,5)$ est situé à 2 carreaux vers la droite et 5 carreaux vers le haut.
>    Le point $B(5\,;\,2)$ est situé à 5 carreaux vers la droite et 2 carreaux vers le haut.
>    Ce sont deux points totalement distincts !
> 3. **Le signe moins dans la distance cartésienne :**
>    Si $x_A = -3$ et $x_B = 4$, la distance horizontale est :
>    $$x_B - x_A = 4 - (-3) = 4 + 3 = \mathbf{7}$$
>    Attention au double signe moins qui se transforme en addition !

---

### 7. Exemples résolus

#### Exemple résolu 1 — Lire et placer des coordonnées
Dans un repère orthonormé d'unité 1 carreau :
1. Place les points suivants : $A(3\,;\,2)$, $B(-4\,;\,3)$, $C(-2\,;\,-3)$, $D(5\,;\,-1)$, $E(0\,;\,4)$, $F(-3\,;\,0)$.
2. Indique dans quel quadrant ou sur quel axe se trouve chacun de ces points.

*Solution :*
- $A(3\,;\,2)$ : 3 carreaux à droite, 2 en haut $\to$ **Quadrant I**.
- $B(-4\,;\,3)$ : 4 carreaux à gauche, 3 en haut $\to$ **Quadrant II**.
- $C(-2\,;\,-3)$ : 2 carreaux à gauche, 3 en bas $\to$ **Quadrant III**.
- $D(5\,;\,-1)$ : 5 carreaux à droite, 1 en bas $\to$ **Quadrant IV**.
- $E(0\,;\,4)$ : abscisse nulle $\to$ situé sur **l'axe des ordonnées**.
- $F(-3\,;\,0)$ : ordonnée nulle $\to$ situé sur **l'axe des abscisses**. ✔

#### Exemple résolu 2 — Calculer le milieu d'un segment
On donne les points $M(-5\,;\,7)$ et $N(3\,;\,-1)$.
Calculer les coordonnées du milieu $K$ du segment $[MN]$.

*Solution :*
Appliquons la formule des coordonnées du milieu :
$$x_K = \frac{x_M + x_N}{2} = \frac{-5 + 3}{2} = \frac{-2}{2} = -1$$
$$y_K = \frac{y_M + y_N}{2} = \frac{7 + (-1)}{2} = \frac{6}{2} = 3$$
Le milieu est le point $K(-1\,;\,3)$. ✔

#### Exemple résolu 3 — Calculer la distance entre deux points
Soient les points $A(-2\,;\,1)$ et $B(4\,;\,9)$ dans un repère orthonormé en centimètres.
Calculer la longueur exacte du segment $[AB]$.

*Solution :*
Appliquons la formule de la distance cartésienne :
$$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$
Calculons chaque écart :
$$x_B - x_A = 4 - (-2) = 4 + 2 = 6$$
$$y_B - y_A = 9 - 1 = 8$$
Élevons au carré et additionnons :
$$AB^2 = 6^2 + 8^2 = 36 + 64 = 100$$
Extrayons la racine :
$$AB = \sqrt{100} = 10\text{ cm}$$
Le segment $[AB]$ mesure exactement $10\text{ cm}$. ✔

#### Exemple résolu 4 — Calculs de produits et quotients de relatifs
Calculer les expressions suivantes :
1. $P_1 = (-4) \times (+7)$
2. $P_2 = (-6) \times (-8)$
3. $Q_1 = \frac{-45}{9}$
4. $Q_2 = \frac{-56}{-7}$
5. $P_3 = (-2) \times (-3) \times (-1) \times (+4) \times (-5)$

*Solution :*
1. Signes contraires $\implies$ résultat négatif : $P_1 = -28$.
2. Même signe (deux négatifs) $\implies$ résultat positif : $P_2 = +48$.
3. Signes contraires $\implies$ résultat négatif : $Q_1 = -5$.
4. Même signe $\implies$ résultat positif : $Q_2 = +8$.
5. Comptons le nombre de facteurs négatifs dans $P_3$ : il y a 4 facteurs négatifs ($(-2), (-3), (-1), (-5)$).
   4 est pair $\implies$ le résultat final sera **positif**.
   Multiplions les valeurs : $2 \times 3 \times 1 \times 4 \times 5 = 120$.
   Donc $P_3 = +120$. ✔

#### Exemple résolu 5 — Déterminer la nature d'un triangle avec le repère
Dans un repère orthonormé, on donne les points :
$A(1\,;\,2)$, $B(4\,;\,6)$ et $C(-3\,;\,5)$.
Démontrer que le triangle $ABC$ est un triangle rectangle et isocèle.

*Solution :*
Calculons les carrés des trois longueurs grâce à la formule de distance :
- Pour $AB$ :
  $$AB^2 = (4 - 1)^2 + (6 - 2)^2 = 3^2 + 4^2 = 9 + 16 = 25 \implies AB = 5$$
- Pour $AC$ :
  $$AC^2 = (-3 - 1)^2 + (5 - 2)^2 = (-4)^2 + 3^2 = 16 + 9 = 25 \implies AC = 5$$
- Pour $BC$ :
  $$BC^2 = (-3 - 4)^2 + (5 - 6)^2 = (-7)^2 + (-1)^2 = 49 + 1 = 50$$

Analyse des résultats :
1. On a $AB = AC = 5$ : le triangle $ABC$ possède deux côtés de même longueur, il est donc **isocèle en $A$**.
2. Comparons les carrés :
   $$AB^2 + AC^2 = 25 + 25 = 50$$
   $$BC^2 = 50$$
   Puisque $AB^2 + AC^2 = BC^2$, d'après la **réciproque du théorème de Pythagore**, le triangle $ABC$ est **rectangle en $A$**.
Conclusion : $ABC$ est un **triangle rectangle isocèle en $A$**. ✔

---

### Ce qu'il faut retenir

1. **Repère cartésien :**
   - Axe horizontal $(Ox)$ : **abscisses**.
   - Axe vertical $(Oy)$ : **ordonnées**.
   - Coordonnées d'un point : $M(x\,;\,y)$ (ordre alphabétique : $x$ puis $y$).
2. **Milieu d'un segment $[AB]$ :**
   $$x_I = \frac{x_A + x_B}{2} \quad \text{et} \quad y_I = \frac{y_A + y_B}{2}$$
3. **Distance entre deux points (repère orthonormé) :**
   $$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$
4. **Règle des signes :**
   - Même signe $\implies$ résultat **positif** ($+ \times + = +$ et $- \times - = +$).
   - Signes différents $\implies$ résultat **négatif** ($+ \times - = -$ et $- \times + = -$).
   - Pour un produit : compter les signes $-$ (nombre pair $\implies +$ ; nombre impair $\implies -$).

---

### Exercices

#### Niveau ★ (Application directe)

**Exercice 1.** Donne les coordonnées des sommets du rectangle représenté ci-dessous :
$A$ est à 3 carreaux à gauche et 2 en haut ; $B$ est à 4 carreaux à droite et 2 en haut ; $C$ est à 4 carreaux à droite et 1 en bas ; $D$ est à 3 carreaux à gauche et 1 en bas.

**Exercice 2.** Calcule sans calculatrice :
1. $(-7) \times (-6)$
2. $(-8) \times (+9)$
3. $(+12) \times (-5)$
4. $\frac{-72}{-8}$
5. $\frac{-42}{+7}$

**Exercice 3.** Quel est le signe de chacun des produits suivants ? (Justifie sans calculer la valeur numérique) :
1. $(-3) \times (-5) \times (+2) \times (-7)$
2. $(-1) \times (-2) \times (-3) \times (-4) \times (-5) \times (-6)$
3. Le produit de 15 nombres négatifs et de 28 nombres positifs.

**Exercice 4.** On donne $A(2\,;\,4)$ et $B(8\,;\,10)$.
Calcule les coordonnées du milieu $I$ de $[AB]$.

**Exercice 5.** Calcule la distance $AB$ entre $A(1\,;\,2)$ et $B(4\,;\,6)$.

#### Niveau ★★ (Calculs et repérage)

**Exercice 6. Calculs de relatifs combinés.**
Calcule en respectant les priorités opératoires :
1. $E = (-3) \times (-4) + (-5) \times (+2)$
2. $F = 15 - (-2) \times (-6)$
3. $G = \frac{(-4) \times (-9)}{-3 - 3}$
4. $H = (-2)^4 - (-3)^3$

**Exercice 7. Retrouver l'extrémité d'un segment.**
Soit $A(-3\,;\,5)$ et $I(1\,;\,2)$.
On sait que $I$ est le milieu du segment $[AB]$.
Quelles sont les coordonnées du point $B$ ?

**Exercice 8. Le parallélogramme par les diagonales.**
On donne quatre points : $A(-2\,;\,1)$, $B(3\,;\,4)$, $C(5\,;\,1)$ et $D(0\,;\,-2)$.
1. Calcule les coordonnées du milieu du segment $[AC]$.
2. Calcule les coordonnées du milieu du segment $[BD]$.
3. Que peux-tu en déduire sur la nature du quadrilatère $ABCD$ ?

**Exercice 9. Le cercle circonscrit.**
Dans un repère orthonormé, on considère les points $E(-4\,;\,0)$ et $F(2\,;\,8)$.
1. Calcule les coordonnées du centre $O'$ du cercle de diamètre $[EF]$.
2. Calcule la longueur du diamètre $EF$, puis le rayon du cercle.
3. Le point $G(2\,;\,0)$ appartient-il à ce cercle ?

**Exercice 10. Périmètre d'un triangle.**
Soient les points $K(-1\,;\,2)$, $L(3\,;\,5)$ et $M(3\,;\,-1)$.
1. Calcule les longueurs exactes $KL$, $LM$ et $KM$.
2. Le triangle $KLM$ est-il isocèle ? Est-il rectangle ?

**Exercice 11. Carré d'un nombre négatif.**
Recopie et complète avec le signe $<$ ou $>$ :
1. $(-5)^2 \dots 0$
2. $-5^2 \dots 0$
3. $(-2)^3 \dots (-2)^2$
4. $(-1)^{100} \dots (-1)^{101}$

#### Niveau ★★★ (Défis et géométrie analytique)

**Exercice 12. La chasse au trésor du pirate.**
Sur une carte quadrillée dont l'origine $O(0\,;\,0)$ est le vieux phare de l'île, le coffre est enterré au point $T$.
Le carnet de bord indique :
- Le point de départ est la crique $A(-6\,;\,-4)$.
- Le trésor $T$ est aligné avec $A$ et la caverne $B(6\,;\,4)$, et il se situe aux trois quarts du trajet en partant de $A$ vers $B$.
1. Quelles sont les coordonnées du trésor $T$ ?
2. Quelle distance en mètres sépare le vieux phare du trésor $T$ (l'unité du repère vaut $10\text{ mètres}$) ?

**Exercice 13. Le symétrique d'un point.**
Soit $A(2\,;\,-3)$ et $S(-1\,;\,1)$.
On appelle $A'$ le symétrique du point $A$ par rapport au centre de symétrie $S$.
1. Que représente le point $S$ pour le segment $[AA']$ ?
2. Détermine par le calcul les coordonnées de $A'$.

**Exercice 14. Démonstration de la règle des signes par une table.**
Construis un tableau à double entrée pour la multiplication avec les nombres $-3, -2, -1, 0, 1, 2, 3$ sur la première ligne et la première colonne.
Remplis d'abord la partie positive, puis prolonge chaque ligne et chaque colonne en observant la régularité des suites arithmétiques (sauts constants).
Explique pourquoi la case $(-3) \times (-3)$ ne peut valoir rien d'autre que $+9$.

**Exercice 15. Triangle équilatéral dans un repère.**
On pose deux points $A(0\,;\,0)$ et $B(4\,;\,0)$ sur l'axe des abscisses.
1. Quelles doivent être les coordonnées d'un point $C$ d'ordonnée positive pour que le triangle $ABC$ soit équilatéral ?
2. Le point $C$ a-t-il des coordonnées rationnelles ou irrationnelles ? Justifie.

---

### Solutions

**Exercice 1.**
$A(-3\,;\,2)$ ; $B(4\,;\,2)$ ; $C(4\,;\,-1)$ ; $D(-3\,;\,-1)$.

**Exercice 2.**
1. $(-7) \times (-6) = +42$.
2. $(-8) \times (+9) = -72$.
3. $(+12) \times (-5) = -60$.
4. $\frac{-72}{-8} = +9$.
5. $\frac{-42}{+7} = -6$.

**Exercice 3.**
1. 3 facteurs négatifs (impair) $\implies$ résultat **négatif**.
2. 6 facteurs négatifs (pair) $\implies$ résultat **positif**.
3. 15 facteurs négatifs (impair) $\implies$ résultat **négatif** (le nombre de facteurs positifs ne change jamais le signe).

**Exercice 4.**
$x_I = \frac{2 + 8}{2} = \frac{10}{2} = 5$ ; $y_I = \frac{4 + 10}{2} = \frac{14}{2} = 7$.
Donc $I(5\,;\,7)$.

**Exercice 5.**
$AB = \sqrt{(4 - 1)^2 + (6 - 2)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.

**Exercice 6.**
1. $E = (+12) + (-10) = 2$.
2. $F = 15 - (+12) = 15 - 12 = 3$.
3. $G = \frac{+36}{-6} = -6$.
4. $H = (+16) - (-27) = 16 + 27 = 43$.

**Exercice 7.**
$x_I = \frac{x_A + x_B}{2} \implies 1 = \frac{-3 + x_B}{2} \implies 2 = -3 + x_B \implies x_B = 5$.
$y_I = \frac{y_A + y_B}{2} \implies 2 = \frac{5 + y_B}{2} \implies 4 = 5 + y_B \implies y_B = -1$.
Le point cherché est $B(5\,;\,-1)$.

**Exercice 8.**
1. Milieu de $[AC]$ : $x = \frac{-2 + 5}{2} = \frac{3}{2} = 1{,}5$ ; $y = \frac{1 + 1}{2} = 1 \implies (1{,}5\,;\,1)$.
2. Milieu de $[BD]$ : $x = \frac{3 + 0}{2} = 1{,}5$ ; $y = \frac{4 + (-2)}{2} = \frac{2}{2} = 1 \implies (1{,}5\,;\,1)$.
3. Les diagonales $[AC]$ et $[BD]$ ont le même milieu. Or, un quadrilatère dont les diagonales se coupent en leur milieu est un **parallélogramme**. Donc $ABCD$ est un parallélogramme.

**Exercice 9.**
1. Centre $O'$ milieu de $[EF]$ : $x_{O'} = \frac{-4 + 2}{2} = -1$ ; $y_{O'} = \frac{0 + 8}{2} = 4 \implies O'(-1\,;\,4)$.
2. Diamètre : $EF = \sqrt{(2 - (-4))^2 + (8 - 0)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.
   Rayon $R = \frac{10}{2} = 5$.
3. Distance $O'G$ : $O'G = \sqrt{(2 - (-1))^2 + (0 - 4)^2} = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
   Puisque $O'G = R = 5$, le point $G$ est situé à une distance égale au rayon : **il appartient bien au cercle**.

**Exercice 10.**
1. $KL = \sqrt{(3 - (-1))^2 + (5 - 2)^2} = \sqrt{4^2 + 3^2} = \sqrt{25} = 5$.
   $LM = \sqrt{(3 - 3)^2 + (-1 - 5)^2} = \sqrt{0 + (-6)^2} = \sqrt{36} = 6$.
   $KM = \sqrt{(3 - (-1))^2 + (-1 - 2)^2} = \sqrt{4^2 + (-3)^2} = \sqrt{25} = 5$.
2. $KL = KM = 5 \implies$ le triangle $KLM$ est **isocèle en $K$**.
   Test de Pythagore : $LM^2 = 6^2 = 36$ ; $KL^2 + KM^2 = 25 + 25 = 50 \neq 36$. Il n'est pas rectangle.

**Exercice 11.**
1. $(-5)^2 = 25 > 0$.
2. $-5^2 = -25 < 0$.
3. $(-2)^3 = -8 < 4 = (-2)^2$.
4. $(-1)^{100} = +1 > -1 = (-1)^{101}$.

**Exercice 12.**
1. Déplacement total de $A$ à $B$ :
   Horizontal : $6 - (-6) = 12$ ; Vertical : $4 - (-4) = 8$.
   Les trois quarts du déplacement :
   Horizontal : $\frac{3}{4} \times 12 = 9 \implies x_T = -6 + 9 = 3$.
   Vertical : $\frac{3}{4} \times 8 = 6 \implies y_T = -4 + 6 = 2$.
   Le trésor est en $T(3\,;\,2)$.
2. Distance $OT = \sqrt{3^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13} \approx 3{,}6055$ unités.
   En mètres : $3{,}6055 \times 10\text{ m} \approx 36{,}1\text{ mètres}$.

**Exercice 13.**
1. $S$ est le milieu du segment $[AA']$.
2. $x_S = \frac{x_A + x_{A'}}{2} \implies -1 = \frac{2 + x_{A'}}{2} \implies -2 = 2 + x_{A'} \implies x_{A'} = -4$.
   $y_S = \frac{y_A + y_{A'}}{2} \implies 1 = \frac{-3 + y_{A'}}{2} \implies 2 = -3 + y_{A'} \implies y_{A'} = 5$.
   Donc $A'(-4\,;\,5)$.

**Exercice 14.**
Sur la ligne de $-3$ :
$(-3) \times 3 = -9$, $(-3) \times 2 = -6$, $(-3) \times 1 = -3$, $(-3) \times 0 = 0$.
À chaque case en allant vers la gauche, on **ajoute 3** !
Pour continuer la régularité arithmétique :
$(-3) \times (-1) = 0 + 3 = 3$
$(-3) \times (-2) = 3 + 3 = 6$
$(-3) \times (-3) = 6 + 3 = 9$.
La case $(-3) \times (-3)$ vaut obligatoirement $+9$.

**Exercice 15.**
1. La base $[AB]$ a une longueur de 4. Le milieu est en $x = 2$.
   Le sommet $C$ a donc pour abscisse $x_C = 2$.
   La hauteur d'un triangle équilatéral de côté 4 est $h = 4 \times \frac{\sqrt{3}}{2} = 2\sqrt{3}$ (d'après Pythagore : $h = \sqrt{4^2 - 2^2} = \sqrt{12} = 2\sqrt{3}$).
   Puisque l'ordonnée est positive, $y_C = 2\sqrt{3}$.
   Donc $C(2\,;\,2\sqrt{3})$.
2. L'abscisse 2 est un nombre rationnel, mais l'ordonnée $2\sqrt{3}$ est un nombre **irrationnel** car $\sqrt{3}$ est irrationnel.

---

### La question qui ouvre la suite

Grâce aux coordonnées cartésiennes, nous pouvons repérer chaque individu ou chaque trésor dans l'espace.
Mais que se passe-t-il lorsque l'on doit prélever un impôt équitable sur des centaines de marchands de richesses différentes, ou résumer les notes d'une classe entière d'élèves en un seul chiffre ?

Comment comparer équitablement des parts quand les totaux ne sont jamais les mêmes ? C'est le pouvoir des **pourcentages**, et la naissance des **statistiques** avec les moyennes, médianes et diagrammes du chapitre suivant !
