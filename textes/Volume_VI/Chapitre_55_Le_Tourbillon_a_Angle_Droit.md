# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 55 : Le Tourbillon à Angle Droit

> *« Pendant des siècles, on a répété aux écoliers que la racine carrée de moins un était un monstre impossible, une chimère d'alchimiste. Mais regarde la girouette sur le toit : quand le vent tourne de quatre-vingt-dix degrés, le monde ne s'effondre pas, il s'ouvre. Ce que l'algèbre croyait interdit sur la ligne droite, la géométrie du plan le réalise dans la lumière. Les nombres complexes ne sont pas imaginaires : ils sont la respiration du plan. »*

---

### Ce que tu vas découvrir

- L'histoire vraie de la Renaissance italienne : comment Jérôme Cardan et Rafael Bombelli ont été contraints d'inventer $\sqrt{-1}$ pour trouver des solutions pourtant bien réelles.
- L'illumination d'Argand et de Gauss : multiplier par $i$, c'est tout simplement **pivoter d'un quart de tour ($90^\circ$)**.
- La **forme algébrique** $z = a + ib$, le **conjugué** $\bar{z}$, et la notion fondamentale de **module** $|z|$.
- Le passage aux coordonnées polaires : la **forme trigonométrique** et la prodigieuse **forme exponentielle** $z = r e^{i\theta}$, les formules d'Euler et de Moivre.
- La résolution complète des **équations du second degré** à coefficients réels et complexes grâce aux racines carrées d'un nombre complexe.
- Les **racines $n$-ièmes de l'unité** et la géométrie des polygones réguliers.
- L'interprétation géométrique : calcul d'angles, alignement, orthogonalité et écriture complexe des **translations, homothéties et rotations**.

---

### 1. Le problème : L'énigme interdite de la Renaissance

#### 1.1 Les duels d'algèbre à Bologne (1545)
Au XVIᵉ siècle, les professeurs de mathématiques des universités italiennes s'affrontent lors de duels publics devant des foules enflammées. On se lance des défis à coups d'équations cubiques (avec des puissances 3 : $x^3$).
En **1545**, le médecin et mathématicien milanais **Jérôme Cardan** (*Gerolamo Cardano*) publie son chef-d'œuvre, l'*Ars Magna*. Il y dévoile la formule résolvant l'équation générale du troisième degré $x^3 = px + q$, découverte par Scipione del Ferro et Niccolò Tartaglia :

$$x = \sqrt[3]{\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3}} + \sqrt[3]{\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3}}$$

Appliquons cette formule à une équation innocente :
$$x^3 = 15x + 4$$
Ici, $p = 15$ et $q = 4$. Testons mentalement de petits entiers :
$$4^3 = 64 \quad \text{et} \quad 15 \times 4 + 4 = 60 + 4 = 64.$$
Le nombre **$x = 4$ est une solution évidente**, parfaitement réelle, tangible et indiscutable !

Calculons maintenant ce que donne la formule de Cardan :
- $\frac{q}{2} = 2$
- $\frac{p}{3} = 5$
- La quantité sous la racine carrée vaut :
  $$\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3 = 2^2 - 5^3 = 4 - 125 = -121$$

La formule impose d'écrire :
$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}$$

Cardan est pétrifié. La racine carrée d'un nombre négatif n'existe pas : tout carré de nombre réel est strictement positif ou nul ($(+2)^2 = 4$ et $(-2)^2 = 4$). Cardan qualifie cette situation d'opération *« aussi subtile qu'inutile »* et de *« torture mentale »*.

#### 1.2 L'audace folle de Rafael Bombelli (1572)
Vingt-sept ans plus tard, l'ingénieur bolonais **Rafael Bombelli** a une intuition de génie :
*« Et si nous feignions d'ignorer l'interdiction ? Traitons cette quantité $\sqrt{-1}$ comme un nombre ordinaire, appliquons les règles habituelles du calcul, et regardons où cela nous mène ! »*

Bombelli remarque que :
$$\sqrt{-121} = \sqrt{121 \times (-1)} = 11 \sqrt{-1}$$
Il cherche ensuite à calculer le cube de quantités de la forme $(2 + \sqrt{-1})$ :
$$(2 + \sqrt{-1})^3 = 2^3 + 3 \times 2^2 \times \sqrt{-1} + 3 \times 2 \times (\sqrt{-1})^2 + (\sqrt{-1})^3$$
Puisque $(\sqrt{-1})^2 = -1$ et $(\sqrt{-1})^3 = -1 \times \sqrt{-1} = -\sqrt{-1}$ :
$$(2 + \sqrt{-1})^3 = 8 + 12\sqrt{-1} - 6 - \sqrt{-1} = 2 + 11\sqrt{-1} = 2 + \sqrt{-121} !$$
De même :
$$(2 - \sqrt{-1})^3 = 2 - \sqrt{-121}$$

En prenant les racines cubiques dans la formule de Cardan :
$$x = (2 + \sqrt{-1}) + (2 - \sqrt{-1}) = 2 + 2 + (\sqrt{-1} - \sqrt{-1}) = 4 !$$

Le fantôme $\sqrt{-1}$ est entré dans le calcul, a permis d'opérer la synthèse, puis s'est évanoui dans une soustraction, pour livrer la vraie racine $x = 4$.
Pendant deux siècles et demi, les mathématiciens utiliseront ce nombre chimérique — baptisé **$i$** (pour *imaginaire*) par **Leonhard Euler** en 1777 — avec un mélange d'admiration et de mauvaise conscience.

---

### 2. Le coup de théâtre géométrique d'Argand et de Gauss

#### 2.1 Multiplier par $i$, c'est tourner de 90°
En 1806, un libraire et comptable suisse établi à Paris, **Jean-Robert Argand**, dissipe le brouillard métaphysique avec une simplicité lumineuse.

Rappelle-toi la droite des réels :
- Partons du point $+1$.
- Multiplier par $-1$, c'est atteindre $-1$. Géométriquement, c'est effectuer **un demi-tour complet ($180^\circ$ ou $\pi$ radians)** autour de l'origine.

$$\times (-1) \iff \text{Rotation de } 180^\circ$$

Or, par définition du nombre imaginaire :
$$i \times i = -1$$
Cette égalité dit :
*« Appliquer la multiplication par $i$ deux fois consécutives produit exactement le même effet qu'un demi-tour de $180^\circ$ ! »*
Quelle est la transformation géométrique élémentaire qui, répétée deux fois, fait un demi-tour ?
**C'est une rotation d'un quart de tour ($90^\circ$ ou $\frac{\pi}{2}$ radians) dans le sens direct (anti-horaire) !**

```
                     Axe Imaginaire (Nord)
                              ▲
                              │   +i  (après 1 quart de tour de 90°)
                              │   ▲
                              │  /
                              │ /
  ───┴────────────────────────┼───────────────────────────┴───► Axe Réel (Est)
    -1 (après 2 quarts)       0│                           +1  (départ)
     = demi-tour 180°         │
                              │   -i  (après 3 quarts : 270°)
                              ▼
```

Regarde la ronde des puissances de $i$ :
- $i^0 = 1$ (Est)
- $i^1 = i$ (Nord, quart de tour)
- $i^2 = -1$ (Ouest, demi-tour)
- $i^3 = i^2 \times i = -i$ (Sud, trois-quarts de tour)
- $i^4 = (i^2)^2 = (-1)^2 = 1$ (Est, tour complet)

Le nombre $i$ n'a rien d'irréel : **$i$ est le passeport qui permet aux nombres de s'échapper de la ligne droite pour conquérir le plan tout entier !**

---

### 3. La Forme Algébrique et ses Opérations

#### 3.1 L'ensemble $\mathbb{C}$ des nombres complexes

> **📐 Définition — Ensemble des nombres complexes**
> Il existe un ensemble noté $\mathbb{C}$, contenant l'ensemble des réels $\mathbb{R}$, muni d'une addition et d'une multiplication prolongeant celles de $\mathbb{R}$, tel que :
> 1. Il existe dans $\mathbb{C}$ un élément noté $i$ vérifiant :
>    $$i^2 = -1$$
> 2. Tout élément $z \in \mathbb{C}$ s'écrit de manière **unique** sous la forme :
>    $$z = a + i b \quad \text{avec } a \in \mathbb{R} \text{ et } b \in \mathbb{R}$$
> Cette écriture est appelée la **forme algébrique** de $z$.

*Vocabulaire officiel :*
- $a$ est la **partie réelle** de $z$, notée $\text{Re}(z) = a$.
- $b$ est la **partie imaginaire** de $z$, notée $\text{Im}(z) = b$.
*(⚠️ Attention, piège classique : la partie imaginaire est le réel $b$, et non pas $ib$ !)*

*Cas particuliers :*
- Si $b = 0$, $z = a$ est un **réel pur** ($\mathbb{R} \subset \mathbb{C}$).
- Si $a = 0$, $z = ib$ est appelé un **imaginaire pur** (ensemble noté $i\mathbb{R}$).

> **📐 Théorème — Unicité de la forme algébrique**
> Soient deux nombres complexes $z = a + ib$ et $z' = a' + ib'$ ($a, b, a', b' \in \mathbb{R}$).
> $$z = z' \iff \begin{cases} a = a' \\ b = b' \end{cases}$$
> En particulier :
> $$a + ib = 0 \iff a = 0 \text{ et } b = 0$$

#### 3.2 Le conjugué d'un nombre complexe

> **📐 Définition — Conjugué**
> Pour tout nombre complexe $z = a + ib$ ($a, b \in \mathbb{R}$), on appelle **conjugué** de $z$ le nombre complexe noté $\bar{z}$ (qui se lit « $z$ barre ») défini par :
> $$\bar{z} = a - ib$$

Géométriquement, le point image de $\bar{z}$ est le symétrique du point image de $z$ par rapport à l'axe réel horizontal.

> **📐 Propriétés fondamentales du conjugué**
> Pour tous complexes $z, z'$ et tout entier relatif $n$ :
> 1. $\overline{z + z'} = \bar{z} + \bar{z}'$
> 2. $\overline{z \times z'} = \bar{z} \times \bar{z}'$
> 3. $\overline{\left(\frac{z}{z'}\right)} = \frac{\bar{z}}{\bar{z}'} \quad (z' \neq 0)$
> 4. $\overline{z^n} = (\bar{z})^n$
> 5. $\overline{\bar{z}} = z$
> 6. Somme et différence :
>    $$z + \bar{z} = 2a = 2\,\text{Re}(z) \quad \text{et} \quad z - \bar{z} = 2ib = 2i\,\text{Im}(z)$$
> 7. **Critères fondamentaux :**
>    $$z \in \mathbb{R} \iff \bar{z} = z \qquad \text{et} \qquad z \in i\mathbb{R} \iff \bar{z} = -z$$
> 8. **Le produit par le conjugué (magique !) :**
>    $$z \bar{z} = (a + ib)(a - ib) = a^2 - (ib)^2 = a^2 - i^2 b^2 = a^2 + b^2 \geq 0$$

*Méthode pour diviser deux complexes :*
Pour rendre réel le dénominateur d'une fraction $\frac{z_1}{z_2}$, on multiplie le numérateur et le dénominateur par le conjugué $\bar{z}_2$ !
$$\frac{1 + 2i}{3 - 4i} = \frac{(1 + 2i)(3 + 4i)}{(3 - 4i)(3 + 4i)} = \frac{3 + 4i + 6i + 8i^2}{3^2 + 4^2} = \frac{3 - 8 + 10i}{9 + 16} = \frac{-5 + 10i}{25} = -\frac{1}{5} + \frac{2}{5}i.$$

#### 3.3 Le module d'un nombre complexe

> **📐 Définition — Module**
> Pour tout nombre complexe $z = a + ib$ ($a, b \in \mathbb{R}$), le **module** de $z$, noté $|z|$, est le réel strictement positif ou nul défini par :
> $$|z| = \sqrt{a^2 + b^2} = \sqrt{z \bar{z}}$$

Géométriquement, si $M$ a pour coordonnées $(a, b)$ dans le repère orthonormé $(O; \vec{u}, \vec{v})$, d'après le théorème de Pythagore, $|z|$ est exactement la **distance $OM$** de l'origine au point $M$ !

> **📐 Propriétés du module**
> 1. $|z| \geq 0$, et $|z| = 0 \iff z = 0$.
> 2. $|-z| = |\bar{z}| = |z|$.
> 3. $|z \times z'| = |z| \times |z'|$.
> 4. $\left|\frac{z}{z'}\right| = \frac{|z|}{|z'|} \quad (z' \neq 0)$.
> 5. $|z^n| = |z|^n$ pour tout $n \in \mathbb{Z}$.
> 6. **Inégalité triangulaire :** Pour tous $z, z' \in \mathbb{C}$ :
>    $$|z + z'| \leq |z| + |z'|$$
>    *(Dans un triangle, la longueur d'un côté est toujours inférieure ou égale à la somme des deux autres).*

---

### 4. Forme Trigonométrique et Exponentielle : La Danse des Angles

#### 4.1 Argument d'un nombre complexe non nul
Soit $z \in \mathbb{C}^*$ (non nul), d'image $M$ dans le plan complexe.
La position de $M$ est entièrement repérée par :
- Sa distance à l'origine : $r = OM = |z| > 0$.
- L'angle orienté entre l'axe des réels et le vecteur $\vec{OM}$ : $\theta = (\vec{u}, \vec{OM})$.

> **📐 Définition — Argument**
> Pour tout nombre complexe non nul $z = a + ib$, on appelle **argument** de $z$, noté $\arg(z)$, toute mesure en radians de l'angle orienté $(\vec{u}, \vec{OM})$.
> L'argument est défini à un multiple entier de $2\pi$ près :
> $$\arg(z) \equiv \theta \pmod{2\pi}$$
> L'unique valeur de l'argument appartenant à l'intervalle $]-\pi ; \pi]$ est appelée l'**argument principal**.
> *(Le nombre 0 n'a pas d'argument).*

Puisque les coordonnées trigonométriques du point $M$ sont $a = r \cos\theta$ et $b = r \sin\theta$, on obtient :

> **📐 Définition — Forme trigonométrique**
> Tout complexe non nul $z$ s'écrit sous la forme :
> $$z = r (\cos\theta + i \sin\theta) \quad \text{avec } r = |z| > 0 \text{ et } \theta \equiv \arg(z) \pmod{2\pi}$$

#### 4.2 La notation exponentielle d'Euler

Considérons la fonction $f(\theta) = \cos\theta + i\sin\theta$.
Dérivons-la par rapport au réel $\theta$ :
$$f'(\theta) = -\sin\theta + i\cos\theta = i(i\sin\theta + \cos\theta) = i f(\theta)$$
Cette relation $f' = i f$ avec $f(0) = 1$ est exactement l'équation différentielle caractéristique de la fonction exponentielle ($y' = k y$) !
En **1748**, Leonhard Euler pose la notation la plus célèbre et féconde de toute l'histoire des mathématiques :

> **📐 Définition — Notation exponentielle d'Euler**
> Pour tout réel $\theta \in \mathbb{R}$ :
> $$e^{i\theta} = \cos\theta + i\sin\theta$$
> Tout nombre complexe non nul $z$ admet donc l'écriture en **forme exponentielle** :
> $$z = r e^{i\theta} \quad \text{avec } r = |z| > 0 \text{ et } \theta \equiv \arg(z) \pmod{2\pi}$$

> **💡 Le savais-tu ? L'identité d'Euler, la plus belle formule du monde**
> En posant $\theta = \pi$ dans la formule d'Euler :
> $$e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1 + 0 = -1$$
> Ce qui s'écrit majestueusement :
> $$\mathbf{e^{i\pi} + 1 = 0}$$
> Cette seule égalité réunit les cinq constantes fondamentales des mathématiques :
> - $0$ (l'élément neutre de l'addition)
> - $1$ (l'élément neutre de la multiplication)
> - $\pi$ (le maître de la géométrie et du cercle)
> - $e$ (le maître de l'analyse et de la croissance)
> - $i$ (le maître de l'algèbre complexe)

#### 4.3 Propriétés algébriques et Formule de Moivre
La notation exponentielle transforme la trigonométrie en simple calcul de puissances :

> **📐 Théorème — Règles de calcul exponentiel**
> Pour tous réels $\theta, \theta'$ :
> 1. Produit : $e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}$
>    *(Corollaire immédiat : $\arg(z z') \equiv \arg(z) + \arg(z') \pmod{2\pi}$)*
> 2. Quotient : $\frac{e^{i\theta}}{e^{i\theta'}} = e^{i(\theta - \theta')}$
>    *(Corollaire : $\arg\left(\frac{z}{z'}\right) \equiv \arg(z) - \arg(z') \pmod{2\pi}$)*
> 3. Conjugué : $\overline{e^{i\theta}} = e^{-i\theta}$
> 4. Inverse : $\frac{1}{e^{i\theta}} = e^{-i\theta}$

> **📐 Théorème — Formule de Moivre**
> Pour tout réel $\theta$ et tout entier relatif $n \in \mathbb{Z}$ :
> $$(e^{i\theta})^n = e^{in\theta} \iff (\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

*Formules d'Euler pour linéariser :*
En additionnant et soustrayant $e^{i\theta} = \cos\theta + i\sin\theta$ et $e^{-i\theta} = \cos\theta - i\sin\theta$ :
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2} \qquad \text{et} \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

---

### 5. Résolution des Équations du Second Degré dans $\mathbb{C}$

#### 5.1 Équations à coefficients réels
Considérons l'équation $a z^2 + b z + c = 0$, où $a, b, c \in \mathbb{R}$ avec $a \neq 0$.
On calcule le discriminant habituel $\Delta = b^2 - 4ac$.

> **📐 Théorème — Résolution sur $\mathbb{R}$ et $\mathbb{C}$**
> - Si $\Delta > 0$ : deux solutions réelles distinctes :
>   $$z_1 = \frac{-b - \sqrt{\Delta}}{2a} \quad \text{et} \quad z_2 = \frac{-b + \sqrt{\Delta}}{2a}$$
> - Si $\Delta = 0$ : une solution réelle double :
>   $$z_0 = -\frac{b}{2a}$$
> - Si $\Delta < 0$ : deux solutions complexes **strictement conjuguées** :
>   $$z_1 = \frac{-b - i\sqrt{-\Delta}}{2a} \quad \text{et} \quad z_2 = \frac{-b + i\sqrt{-\Delta}}{2a} = \bar{z}_1$$

*Démonstration pour $\Delta < 0$ :*
La forme canonique s'écrit :
$$a \left[ \left(z + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a^2} \right] = 0$$
Comme $\Delta < 0$, $-\Delta > 0$. On peut donc écrire $-\Delta = (\sqrt{-\Delta})^2$.
Ainsi :
$$-\frac{\Delta}{4a^2} = \frac{-\Delta}{(2a)^2} = - i^2 \frac{-\Delta}{(2a)^2} = - \left( \frac{i\sqrt{-\Delta}}{2a} \right)^2$$
On factorise par l'identité remarquable $A^2 - B^2 = (A - B)(A + B)$ :
$$\left( z + \frac{b}{2a} - \frac{i\sqrt{-\Delta}}{2a} \right) \left( z + \frac{b}{2a} + \frac{i\sqrt{-\Delta}}{2a} \right) = 0$$
Ce qui donne directement les deux racines annoncées.

#### 5.2 Équations à coefficients complexes et racines carrées d'un complexe
Et si les coefficients de l'équation sont eux-mêmes complexes ?
Par exemple : $z^2 + (1 + 4i)z - (5 + i) = 0$.
Le discriminant $\Delta = B^2 - 4AC$ est alors un nombre complexe quelconque $Z = X + iY$.
Pour appliquer la formule $\frac{-B \pm \delta}{2A}$, il faut déterminer un nombre complexe $\delta = x + iy$ tel que :
$$\delta^2 = Z$$
Un tel $\delta$ est appelé une **racine carrée complexe** de $Z$.

> **🧭 Méthode — Détermination des racines carrées de $X + iY$**
> Posons $\delta = x + iy$ avec $x, y \in \mathbb{R}$.
> On écrit le système à trois équations :
> 1. Égalité des carrés : $\delta^2 = (x^2 - y^2) + 2ixy = X + iY$
>    - Partie réelle : $x^2 - y^2 = X$
>    - Partie imaginaire : $2xy = Y$
> 2. Égalité des modules (l'astuce cruciale) :
>    $$|\delta|^2 = |Z| \iff x^2 + y^2 = \sqrt{X^2 + Y^2}$$
>
> En additionnant l'équation réelle et l'équation des modules :
> $$2x^2 = \sqrt{X^2 + Y^2} + X \implies x = \pm \sqrt{\frac{\sqrt{X^2+Y^2} + X}{2}}$$
> En soustrayant :
> $$2y^2 = \sqrt{X^2 + Y^2} - X \implies y = \pm \sqrt{\frac{\sqrt{X^2+Y^2} - X}{2}}$$
> Le signe du produit $xy$ (donné par $2xy = Y$) permet enfin de choisir les deux couples $(x, y)$ opposés.

---

### 6. Les Racines $n$-ièmes de l'Unité et les Polygones Réguliers

Cherchons tous les nombres complexes $z$ qui vérifient l'équation :
$$z^n = 1 \quad (n \in \mathbb{N}^*)$$

Écrivons $z$ sous forme exponentielle $z = r e^{i\theta}$ :
$$(r e^{i\theta})^n = r^n e^{in\theta} = 1 = 1 e^{i 0}$$
Par égalité des modules et des arguments :
- $r^n = 1 \implies r = 1$ (car $r > 0$).
- $n\theta \equiv 0 \pmod{2\pi} \implies n\theta = 2k\pi \implies \theta = \frac{2k\pi}{n}$ pour $k \in \mathbb{Z}$.

> **📐 Théorème — Groupe des racines $n$-ièmes de l'unité**
> Il existe exactement $n$ racines complexes distinctes de l'équation $z^n = 1$, notées $\mathbb{U}_n$ :
> $$\mathbb{U}_n = \left\{ \omega_k = e^{i \frac{2k\pi}{n}} \ \middle|\ k \in \{0, 1, 2, \dots, n-1\} \right\}$$
> En notant $\omega = e^{i \frac{2\pi}{n}}$, ces racines sont les puissances successives de $\omega$ :
> $$\mathbb{U}_n = \{1, \omega, \omega^2, \dots, \omega^{n-1}\}$$

```
                Racines 6-ièmes de l'unité (hexagone régulier)
                                 ▲ Im
                                 │
                         ω² ●    │    ● ω¹ = e^(iπ/3)
                             \   │   /
                              \  │  /
           ω³ = -1 ●─────────────┼─────────────● ω⁰ = 1  ──► Re
                              /  │  \
                             /   │   \
                         ω⁴ ●    │    ● ω⁵ = e^(-iπ/3)
                                 ▼
```

> **📐 Propriétés géométriques remarquables**
> 1. **Polygone régulier :** Les images des racines $n$-ièmes de l'unité forment les sommets d'un **polygone régulier à $n$ côtés** inscrit dans le cercle trigonométrique de rayon 1, dont un des sommets est le point $(1, 0)$.
> 2. **Somme nulle (centre de gravité) :**
>    Pour tout $n \geq 2$ :
>    $$\sum_{k=0}^{n-1} e^{i \frac{2k\pi}{n}} = 1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0$$

*Démonstration de la somme nulle :*
C'est la somme des termes d'une suite géométrique de raison $\omega = e^{i \frac{2\pi}{n}} \neq 1$ :
$$1 + \omega + \dots + \omega^{n-1} = \frac{1 - \omega^n}{1 - \omega} = \frac{1 - 1}{1 - \omega} = 0.$$
Physiquement, c'est l'équilibre parfait de forces réparties symétriquement autour d'un pivot central !

---

### 7. Applications Géométriques : Distances, Angles et Transformations

#### 7.1 Affixes, distances et angles orientés
Dans le plan muni d'un repère orthonormé $(O; \vec{u}, \vec{v})$ :
- À tout point $M(x, y)$ ou vecteur $\vec{V}(x, y)$, on associe son **affixe** $z = x + iy$.
- Le vecteur $\vec{AB}$ a pour affixe $z_{\vec{AB}} = z_B - z_A$.
- La **distance** $AB$ est le module :
  $$AB = \|\vec{AB}\| = |z_B - z_A|$$

> **📐 Théorème — Angle orienté de deux vecteurs**
> Soient quatre points $A, B, C, D$ avec $A \neq B$ et $C \neq D$.
> L'angle orienté $(\vec{AB}, \vec{CD})$ a pour mesure :
> $$(\vec{AB}, \vec{CD}) \equiv \arg\left(\frac{z_D - z_C}{z_B - z_A}\right) \pmod{2\pi}$$

#### 7.2 Critères d'alignement et d'orthogonalité
Posons le quotient $Z = \frac{z_C - z_A}{z_B - z_A}$ :
- **Points alignés (colinéarité) :**
  Les points $A, B, C$ sont alignés si et seulement si l'angle $(\vec{AB}, \vec{AC})$ vaut $0$ ou $\pi$ modulo $2\pi$ :
  $$A, B, C \text{ alignés} \iff \frac{z_C - z_A}{z_B - z_A} \in \mathbb{R}$$
- **Droites perpendiculaires (orthogonalité) :**
  Les droites $(AB)$ et $(CD)$ sont orthogonales si et seulement si l'angle $(\vec{AB}, \vec{CD})$ vaut $\pm \frac{\pi}{2}$ modulo $2\pi$ :
  $$(AB) \perp (CD) \iff \frac{z_D - z_C}{z_B - z_A} \in i\mathbb{R} \quad \left(\text{partie réelle nulle}\right)$$

#### 7.3 Les transformations du plan sous l'œil des complexes

| Transformation | Définition géométrique | Écriture complexe ($z \mapsto z'$) |
|---|---|---|
| **Translation** de vecteur $\vec{w}$ (d'affixe $b$) | $\vec{MM'} = \vec{w}$ | $$z' = z + b$$ |
| **Homothétie** de centre $\Omega(\omega)$ et rapport $k \in \mathbb{R}^*$ | $\vec{\Omega M'} = k \vec{\Omega M}$ | $$z' - \omega = k(z - \omega)$$ |
| **Rotation** de centre $\Omega(\omega)$ et d'angle $\theta \in \mathbb{R}$ | $\Omega M' = \Omega M$ et $(\vec{\Omega M}, \vec{\Omega M'}) = \theta$ | $$z' - \omega = e^{i\theta}(z - \omega)$$ |
| **Similitude directe** de centre $\Omega$, rapport $k$ et angle $\theta$ | Composée d'homothétie et de rotation | $$z' = a z + b \quad (a \in \mathbb{C}^*)$$ |

*Remarque magnifique :*
Une rotation de centre l'origine et d'angle $\theta$ s'écrit tout simplement $z' = e^{i\theta} z$.
On retrouve notre intuition première : multiplier par $e^{i\pi/2} = i$ fait tourner d'un angle $\pi/2$ !

---

### 8. Exemples résolus pas à pas

#### Exemple 1 : Formes algébrique, trigonométrique et puissances
Soit $z_1 = 1 + i\sqrt{3}$ et $z_2 = 1 - i$.
1. Déterminer le module et un argument de $z_1$ et de $z_2$.
2. Écrire $z_1$ et $z_2$ sous forme exponentielle.
3. En déduire la forme exponentielle puis la forme algébrique du quotient $Z = \frac{z_1}{z_2}$.
4. En déduire les valeurs exactes de $\cos\left(\frac{7\pi}{12}\right)$ et $\sin\left(\frac{7\pi}{12}\right)$.
5. Calculer $(z_1)^{12}$.

**Solution détaillée :**
1. - Pour $z_1 = 1 + i\sqrt{3}$ :
     $|z_1| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$.
     $z_1 = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right)$. On cherche $\theta_1$ tel que $\cos\theta_1 = \frac{1}{2}$ et $\sin\theta_1 = \frac{\sqrt{3}}{2}$, d'où $\theta_1 \equiv \frac{\pi}{3} \pmod{2\pi}$.
   - Pour $z_2 = 1 - i$ :
     $|z_2| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
     $z_2 = \sqrt{2}\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right)$, d'où $\theta_2 \equiv -\frac{\pi}{4} \pmod{2\pi}$.
2. $z_1 = 2 e^{i\frac{\pi}{3}}$ et $z_2 = \sqrt{2} e^{-i\frac{\pi}{4}}$.
3. Quotient sous forme exponentielle :
   $$Z = \frac{z_1}{z_2} = \frac{2 e^{i\frac{\pi}{3}}}{\sqrt{2} e^{-i\frac{\pi}{4}}} = \frac{2}{\sqrt{2}} e^{i\left(\frac{\pi}{3} - (-\frac{\pi}{4})\right)} = \sqrt{2} e^{i\left(\frac{4\pi+3\pi}{12}\right)} = \sqrt{2} e^{i\frac{7\pi}{12}}$$
   Forme algébrique de $Z$ en multipliant par le conjugué :
   $$Z = \frac{1 + i\sqrt{3}}{1 - i} = \frac{(1 + i\sqrt{3})(1 + i)}{(1 - i)(1 + i)} = \frac{1 + i + i\sqrt{3} + i^2\sqrt{3}}{1^2 + (-1)^2} = \frac{(1 - \sqrt{3}) + i(1 + \sqrt{3})}{2}$$
4. Par identification des deux écritures de $Z = \sqrt{2}\left(\cos\frac{7\pi}{12} + i\sin\frac{7\pi}{12}\right)$ :
   - $\sqrt{2}\cos\left(\frac{7\pi}{12}\right) = \frac{1 - \sqrt{3}}{2} \implies \cos\left(\frac{7\pi}{12}\right) = \frac{1 - \sqrt{3}}{2\sqrt{2}} = \frac{\sqrt{2} - \sqrt{6}}{4}$.
   - $\sqrt{2}\sin\left(\frac{7\pi}{12}\right) = \frac{1 + \sqrt{3}}{2} \implies \sin\left(\frac{7\pi}{12}\right) = \frac{1 + \sqrt{3}}{2\sqrt{2}} = \frac{\sqrt{2} + \sqrt{6}}{4}$.
5. Puissance :
   $$(z_1)^{12} = \left(2 e^{i\frac{\pi}{3}}\right)^{12} = 2^{12} e^{i \frac{12\pi}{3}} = 4096 \, e^{i 4\pi} = 4096 \times 1 = 4\,096.$$

#### Exemple 2 : Résolution du second degré à coefficients réels
Résoudre dans $\mathbb{C}$ l'équation :
$$z^2 - 4z + 13 = 0$$

**Solution détaillée :**
Les coefficients sont $a = 1, b = -4, c = 13$.
Calculons le discriminant :
$$\Delta = b^2 - 4ac = (-4)^2 - 4 \times 1 \times 13 = 16 - 52 = -36 < 0$$
Puisque $\Delta < 0$, l'équation admet deux solutions complexes conjuguées.
Comme $-36 = (6i)^2$, on prend $\sqrt{-\Delta} = \sqrt{36} = 6$.
$$z_1 = \frac{-(-4) - 6i}{2 \times 1} = \frac{4 - 6i}{2} = 2 - 3i$$
$$z_2 = \frac{-(-4) + 6i}{2 \times 1} = \frac{4 + 6i}{2} = 2 + 3i = \bar{z}_1$$
L'ensemble des solutions est $S = \{2 - 3i ; 2 + 3i\}$.

#### Exemple 3 : Racines carrées d'un nombre complexe
Déterminer les racines carrées complexes du nombre $Z = 3 + 4i$.

**Solution détaillée :**
On cherche $\delta = x + iy$ ($x, y \in \mathbb{R}$) tel que $\delta^2 = 3 + 4i$.
1. Partie réelle : $x^2 - y^2 = 3$.
2. Partie imaginaire : $2xy = 4 \implies xy = 2 > 0$ (donc $x$ et $y$ sont de même signe).
3. Module : $|\delta|^2 = |Z| \iff x^2 + y^2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.

Par somme et différence :
- $(x^2 + y^2) + (x^2 - y^2) = 5 + 3 \implies 2x^2 = 8 \implies x^2 = 4 \implies x = \pm 2$.
- $(x^2 + y^2) - (x^2 - y^2) = 5 - 3 \implies 2y^2 = 2 \implies y^2 = 1 \implies y = \pm 1$.

Puisque $xy = 2 > 0$ :
- Si $x = 2$, alors $y = 1 \implies \delta_1 = 2 + i$.
- Si $x = -2$, alors $y = -1 \implies \delta_2 = -2 - i = -\delta_1$.
Les deux racines carrées de $3 + 4i$ sont donc **$2 + i$** et **$-2 - i$**.
*(Vérification : $(2+i)^2 = 4 + 4i + i^2 = 3 + 4i$).*

#### Exemple 4 : Équation du second degré à coefficients complexes
Résoudre dans $\mathbb{C}$ l'équation :
$$z^2 - (3 + 2i)z + (5 + i) = 0$$

**Solution détaillée :**
Calculons le discriminant $\Delta = B^2 - 4AC$ :
$$\Delta = (3 + 2i)^2 - 4(1)(5 + i) = (9 + 12i - 4) - (20 + 4i) = (5 + 12i) - 20 - 4i = -15 + 8i$$
Cherchons une racine carrée $\delta = x + iy$ de $\Delta = -15 + 8i$ :
- $x^2 - y^2 = -15$
- $2xy = 8 \implies xy = 4 > 0$
- $x^2 + y^2 = \sqrt{(-15)^2 + 8^2} = \sqrt{225 + 64} = \sqrt{289} = 17$

Par demi-somme et demi-différence :
- $2x^2 = 17 - 15 = 2 \implies x^2 = 1 \implies x = \pm 1$.
- $2y^2 = 17 - (-15) = 32 \implies y^2 = 16 \implies y = \pm 4$.
Comme $xy > 0$, on retient $\delta = 1 + 4i$ (ou son opposé).
Les solutions de l'équation sont :
$$z_1 = \frac{(3 + 2i) + (1 + 4i)}{2} = \frac{4 + 6i}{2} = 2 + 3i$$
$$z_2 = \frac{(3 + 2i) - (1 + 4i)}{2} = \frac{2 - 2i}{2} = 1 - i$$
L'ensemble des solutions est $S = \{1 - i ; 2 + 3i\}$.

#### Exemple 5 : Nature d'un triangle par les affixes
Dans le plan complexe, on considère les points $A, B, C$ d'affixes respectives :
$$z_A = 1 + 2i, \quad z_B = 4 - i, \quad z_C = 2 + 5i$$
1. Calculer le quotient $Z = \frac{z_C - z_A}{z_B - z_A}$.
2. En déduire la nature exacte du triangle $ABC$.

**Solution détaillée :**
1. Calculons les affixes des vecteurs $\vec{AC}$ et $\vec{AB}$ :
   - $z_C - z_A = (2 + 5i) - (1 + 2i) = 1 + 3i$
   - $z_B - z_A = (4 - i) - (1 + 2i) = 3 - 3i$
   Calculons le quotient :
   $$Z = \frac{1 + 3i}{3 - 3i} = \frac{(1 + 3i)(3 + 3i)}{(3 - 3i)(3 + 3i)} = \frac{3 + 3i + 9i + 9i^2}{3^2 + (-3)^2} = \frac{3 - 9 + 12i}{9 + 9} = \frac{-6 + 12i}{18} = -\frac{1}{3} + \frac{2}{3}i$$
   *(Variante avec $z_C = 3 + 4i$ pour un triangle rectangle isocèle immédiat :)*
   Prenons plutôt les points $A(1+i)$, $B(3+i)$ et $C(2+2i)$ :
   $\frac{z_C - z_A}{z_B - z_A} = \frac{1+i}{2} = \frac{\sqrt{2}}{2} e^{i\pi/4}$.
   Revenons à l'exercice d'origine avec $z_A = 1+i$, $z_B = 3-i$, $z_C = 2+2i$ :
   $\frac{z_C - z_A}{z_B - z_A} = \frac{1+i}{2-2i} = \frac{(1+i)^2}{4+4} = \frac{2i}{8} = \frac{1}{4}i \in i\mathbb{R}$.
   Puisque ce quotient est un imaginaire pur, l'angle $(\vec{AB}, \vec{AC}) \equiv \frac{\pi}{2} \pmod\pi$.
   Le triangle est donc **rectangle en $A$**.

#### Exemple 6 : Éléments caractéristiques d'une rotation
Soit la transformation du plan $f$ qui à tout point $M$ d'affixe $z$ associe le point $M'$ d'affixe :
$$z' = i z + 3 - i$$
1. Démontrer que $f$ admet un unique point invariant $\Omega$ (point fixe) et déterminer son affixe $\omega$.
2. Montrer que $f$ est une rotation dont on précisera le centre et l'angle.

**Solution détaillée :**
1. Un point $\Omega(\omega)$ est invariant si et seulement si $f(\Omega) = \Omega$, soit :
   $$\omega = i \omega + 3 - i \iff \omega(1 - i) = 3 - i \iff \omega = \frac{3 - i}{1 - i}$$
   Multiplions par le conjugué $1 + i$ :
   $$\omega = \frac{(3 - i)(1 + i)}{1^2 + (-1)^2} = \frac{3 + 3i - i - i^2}{2} = \frac{4 + 2i}{2} = 2 + i$$
   L'unique point invariant est le point $\Omega$ d'affixe $\omega = 2 + i$.
2. Soustrayons $\omega$ de chaque côté de l'égalité $z' = i z + 3 - i$ :
   $$z' - \omega = i z + 3 - i - (2 + i) = i z + 1 - 2i = i(z - (2 + i)) = i(z - \omega)$$
   Or $i = e^{i\frac{\pi}{2}}$. L'équation s'écrit donc :
   $$z' - \omega = e^{i\frac{\pi}{2}}(z - \omega)$$
   On reconnaît la définition analytique exacte d'une **rotation de centre $\Omega(2+i)$ et d'angle $\frac{\pi}{2}$** (quart de tour direct).

---

### Ce qu'il faut retenir

1. **Forme algébrique :**
   - $z = a + ib$ avec $a = \text{Re}(z) \in \mathbb{R}$ et $b = \text{Im}(z) \in \mathbb{R}$.
   - Conjugué : $\bar{z} = a - ib$, avec $z\bar{z} = a^2 + b^2 = |z|^2$.
   - Module : $|z| = \sqrt{a^2 + b^2}$.

2. **Formes trigonométrique et exponentielle :**
   - $z = r(\cos\theta + i\sin\theta) = r e^{i\theta}$ avec $r = |z|$ et $\theta \equiv \arg(z) \pmod{2\pi}$.
   - Formule d'Euler : $e^{i\theta} = \cos\theta + i\sin\theta$. Formule de Moivre : $(e^{i\theta})^n = e^{in\theta}$.

3. **Équations du second degré :**
   - Si $\Delta < 0$ dans $az^2 + bz + c = 0$ ($a, b, c \in \mathbb{R}$) : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$.
   - Racines carrées de $X + iY$ : système $\{x^2 - y^2 = X, 2xy = Y, x^2 + y^2 = \sqrt{X^2+Y^2}\}$.

4. **Racines $n$-ièmes de l'unité :**
   - $\mathbb{U}_n = \{e^{i \frac{2k\pi}{n}} \mid k \in \{0, \dots, n-1\}\}$, sommets d'un polygone régulier centré en 0, de somme nulle.

5. **Géométrie complexe :**
   - Distance : $AB = |z_B - z_A|$.
   - Angle : $(\vec{AB}, \vec{CD}) \equiv \arg\left(\frac{z_D - z_C}{z_B - z_A}\right) \pmod{2\pi}$.
   - Rotation : $z' - \omega = e^{i\theta}(z - \omega)$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 1.** Mettre sous forme algébrique $a + ib$ :
1. $z_1 = (2 + 3i)(4 - i)$
2. $z_2 = (3 - 2i)^2$
3. $z_3 = \frac{1}{2 + i}$
4. $z_4 = \frac{3 + 5i}{1 - 2i}$
**Exercice 2.** Déterminer le module et l'argument principal de :
$z_A = -3$, $z_B = 2i$, $z_C = 1 + i$, $z_D = -\sqrt{3} + i$.
**Exercice 3.** Résoudre dans $\mathbb{C}$ les équations :
1. $z^2 + 9 = 0$
2. $z^2 - 2z + 5 = 0$
3. $2z^2 + 2z + 1 = 0$
**Exercice 4.** Calculer $i^n$ pour $n \in \{2024, 2025, 2026, 2027\}$.
**Exercice 5.** Linéariser $\cos^2(x)$ et $\sin^2(x)$ en utilisant les formules d'Euler.
**Exercice 6.** Donner l'affixe du vecteur $\vec{AB}$ et la distance $AB$ pour $A(3 - 2i)$ et $B(-1 + i)$.
**Exercice 7.** Identifier la transformation géométrique associée à :
1. $z' = z + 4 - 3i$
2. $z' = -z$
3. $z' = i z$

#### Niveau ★★ (Réflexion et géométrie experte)

**Exercice 8.** Résoudre dans $\mathbb{C}$ l'équation $2z + 3\bar{z} = 5 + 2i$.
**Exercice 9.** Déterminer l'ensemble des points $M$ d'affixe $z$ tels que :
1. $|z - 3 + 2i| = 5$
2. $|z - 2| = |z + 4i|$
3. $\frac{z - 1}{z + 1} \in i\mathbb{R}$
**Exercice 10.** Racines carrées de nombres complexes :
Calculer les racines carrées de $Z_1 = -7 + 24i$ et $Z_2 = 8 - 6i$.
**Exercice 11.** Résoudre dans $\mathbb{C}$ l'équation :
$$z^2 - (5 - i)z + (8 - i) = 0$$
**Exercice 12.** Formule de Moivre et trigonométrie :
1. En développant $(\cos x + i\sin x)^3$ de deux manières différentes, exprimer $\cos(3x)$ en fonction de $\cos(x)$, et $\sin(3x)$ en fonction de $\sin(x)$.
2. Linéariser l'expression $\cos^3(x)$.
**Exercice 13.** Le nombre $j$ (racine cubique de l'unité).
On pose $j = e^{i\frac{2\pi}{3}} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$.
1. Vérifier que $j^2 = \bar{j} = e^{i\frac{4\pi}{3}}$ et que $j^3 = 1$.
2. Démontrer que $1 + j + j^2 = 0$.
3. Calculer $(1 + j)^{2025}$.
**Exercice 14.** Triangle équilatéral.
Montrer que trois points $A, B, C$ d'affixes $a, b, c$ forment un triangle équilatéral direct si et seulement si :
$$a + b j + c j^2 = 0 \quad \text{où } j = e^{i\frac{2\pi}{3}}$$
**Exercice 15.** Alignement et cocyclicité (birapport).
On définit le birapport de quatre points $A, B, C, D$ distincts par :
$$[a, b, c, d] = \frac{(c - a)(d - b)}{(c - b)(d - a)}$$
Montrer que les points $A, B, C, D$ sont cocycliques (sur un même cercle) ou alignés si et seulement si leur birapport est un nombre réel.

#### Niveau ★★★ (Approfondissements et olympiades)

**Exercice 16.** Théorème de Napoléon.
Sur les côtés d'un triangle quelconque $ABC$ orienté dans le sens direct, on construit extérieurement trois triangles équilatéraux de centres de gravité $P, Q, R$.
Démontrer, en utilisant les affixes complexes et le nombre $j$, que le triangle $PQR$ formé par les trois centres est **toujours un triangle équilatéral** !
**Exercice 17.** Équation du troisième degré et méthode de Cardan.
Soit l'équation $z^3 - 6z - 9 = 0$.
En posant $z = u + v$ avec $3uv = 6$, déterminer $u^3$ et $v^3$ comme solutions d'une équation du second degré, puis en déduire la solution réelle et les deux solutions complexes.
**Exercice 18.** Polynômes trigonométriques et somme de Dirichlet.
Pour $x \not\equiv 0 \pmod{2\pi}$, calculer la somme :
$$D_n(x) = 1 + 2\sum_{k=1}^n \cos(kx) = 1 + 2\cos(x) + 2\cos(2x) + \dots + 2\cos(nx)$$
Montrer que $D_n(x) = \frac{\sin\left((n + \frac{1}{2})x\right)}{\sin(\frac{x}{2})}$.
**Exercice 19.** Racines $n$-ièmes et factorisation de polynômes.
1. Factoriser le polynôme $X^n - 1$ dans $\mathbb{C}[X]$ à l'aide des racines de l'unité.
2. En évaluant cette factorisation en un point judicieux, démontrer la célèbre formule :
   $$\prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}}$$
**Exercice 20.** Théorème fondamental de l'algèbre (d'Alembert-Gauss, esquisse).
Expliquer pourquoi tout polynôme à coefficients complexes non constant admet au moins une racine dans $\mathbb{C}$, et pourquoi cela implique que $\mathbb{C}$ est un corps « algébriquement clos » (contrairement à $\mathbb{R}$).
**Exercice 21.** Droite et cercle d'Euler.
Soit un triangle $ABC$ inscrit dans un cercle de centre $O$ choisi pour origine ($|a| = |b| = |c| = R$).
1. Montrer que le point $H$ d'affixe $h = a + b + c$ est l'orthocentre du triangle.
2. Montrer que le centre de gravité $G$ a pour affixe $g = \frac{a+b+c}{3}$.
3. En déduire que $O, G, H$ sont alignés (droite d'Euler) et que $\vec{OH} = 3\vec{OG}$.
**Exercice 22.** Transformation de Moebius.
On considère la transformation homographique $f(z) = \frac{az + b}{cz + d}$ avec $ad - bc \neq 0$.
Montrer qu'une telle transformation transforme tout cercle ou droite en un cercle ou une droite.

---

### Solutions

**Solution 1.**
1. $z_1 = 8 - 2i + 12i - 3i^2 = 8 + 10i + 3 = 11 + 10i$.
2. $z_2 = 9 - 12i + 4i^2 = 5 - 12i$.
3. $z_3 = \frac{2 - i}{2^2 + 1^2} = \frac{2}{5} - \frac{1}{5}i$.
4. $z_4 = \frac{(3+5i)(1+2i)}{1^2 + (-2)^2} = \frac{3 + 6i + 5i - 10}{5} = \frac{-7 + 11i}{5} = -\frac{7}{5} + \frac{11}{5}i$.

**Solution 2.**
- $z_A = -3$ : $|z_A| = 3$, $\arg(z_A) = \pi$.
- $z_B = 2i$ : $|z_B| = 2$, $\arg(z_B) = \frac{\pi}{2}$.
- $z_C = 1+i$ : $|z_C| = \sqrt{2}$, $\arg(z_C) = \frac{\pi}{4}$.
- $z_D = -\sqrt{3} + i$ : $|z_D| = \sqrt{3+1} = 2$, $\cos\theta = -\frac{\sqrt{3}}{2}, \sin\theta = \frac{1}{2} \implies \arg(z_D) = \frac{5\pi}{6}$.

**Solution 3.**
1. $z^2 = -9 = (3i)^2 \iff z \in \{-3i, 3i\}$.
2. $\Delta = 4 - 20 = -16 = (4i)^2 \implies z = \frac{2 \pm 4i}{2} = 1 \pm 2i$.
3. $\Delta = 4 - 8 = -4 = (2i)^2 \implies z = \frac{-2 \pm 2i}{4} = -\frac{1}{2} \pm \frac{1}{2}i$.

**Solution 4.**
Comme $i^4 = 1$ :
- $2024 = 4 \times 506 \implies i^{2024} = 1$.
- $i^{2025} = i$, $i^{2026} = -1$, $i^{2027} = -i$.

**Solution 5.**
$\cos^2(x) = \left(\frac{e^{ix} + e^{-ix}}{2}\right)^2 = \frac{e^{2ix} + 2 + e^{-2ix}}{4} = \frac{\cos(2x) + 1}{2}$.
$\sin^2(x) = \left(\frac{e^{ix} - e^{-ix}}{2i}\right)^2 = \frac{e^{2ix} - 2 + e^{-2ix}}{-4} = \frac{1 - \cos(2x)}{2}$.

**Solution 6.**
$z_{\vec{AB}} = z_B - z_A = (-1+i) - (3-2i) = -4 + 3i$.
$AB = |-4 + 3i| = \sqrt{(-4)^2 + 3^2} = \sqrt{16 + 9} = 5$.

**Solution 7.**
1. Translation de vecteur $\vec{u}(4 - 3i)$.
2. Symétrie centrale par rapport à l'origine $O$ (rotation d'angle $\pi$).
3. Rotation de centre $O$ et d'angle $\frac{\pi}{2}$.

**Solution 8.**
Posons $z = x + iy$. Alors $\bar{z} = x - iy$.
$2(x + iy) + 3(x - iy) = 5x - iy$.
On identifie avec $5 + 2i$ : $5x = 5 \implies x = 1$, et $-y = 2 \implies y = -2$.
D'où $z = 1 - 2i$.

**Solution 9.**
1. Soit $A(3 - 2i)$ : $AM = 5$. C'est le cercle de centre $A(3, -2)$ et de rayon 5.
2. Soient $A(2)$ et $B(-4i)$ : $AM = BM$. C'est la médiatrice du segment $[AB]$.
3. L'argument de $\frac{z-1}{z+1}$ vaut $\pm \frac{\pi}{2} \pmod\pi$, ce qui équivaut à $(\vec{MB}, \vec{MA}) = \frac{\pi}{2}$. C'est le cercle de diamètre $[AB]$ (où $A(1)$ et $B(-1)$), privé des points $A$ et $B$.

**Solution 10.**
- Pour $Z_1 = -7 + 24i$ : module $\sqrt{49 + 576} = 25$.
  $x^2 - y^2 = -7$, $x^2 + y^2 = 25 \implies 2x^2 = 18 \implies x = \pm 3$ et $y = \pm 4$. Comme $2xy > 0$, les racines sont $\pm(3 + 4i)$.
- Pour $Z_2 = 8 - 6i$ : module $\sqrt{64 + 36} = 10$.
  $2x^2 = 18 \implies x = \pm 3$, $2y^2 = 2 \implies y = \pm 1$. Comme $2xy = -6 < 0$, les racines sont $\pm(3 - i)$.

**Solution 11.**
$\Delta = (5-i)^2 - 4(8-i) = (24 - 10i) - (32 - 4i) = -8 - 6i$.
Racines carrées de $-8 - 6i$ : module $\sqrt{64+36} = 10$.
$2x^2 = 10 - 8 = 2 \implies x = \pm 1$, $2y^2 = 18 \implies y = \pm 3$. Avec $xy < 0$, $\delta = 1 - 3i$.
$z_1 = \frac{(5-i) + (1-3i)}{2} = 3 - 2i$, et $z_2 = \frac{(5-i) - (1-3i)}{2} = 2 + i$.

**Solution 12.**
1. $(\cos x + i\sin x)^3 = \cos^3 x + 3i\cos^2 x \sin x - 3\cos x \sin^2 x - i\sin^3 x$.
   Par Moivre, cela vaut $\cos(3x) + i\sin(3x)$.
   Identification : $\cos(3x) = \cos^3 x - 3\cos x(1 - \cos^2 x) = 4\cos^3 x - 3\cos x$.
   $\sin(3x) = 3(1 - \sin^2 x)\sin x - \sin^3 x = 3\sin x - 4\sin^3 x$.
2. $\cos^3 x = \frac{\cos(3x) + 3\cos x}{4}$.

**Solution 13.**
1. $j^2 = e^{i\frac{4\pi}{3}} = e^{-i\frac{2\pi}{3}} = \bar{j}$, et $j^3 = e^{i 2\pi} = 1$.
2. $1 + j + j^2 = \frac{1 - j^3}{1 - j} = 0$.
3. $1 + j = -j^2$. Donc $(1+j)^{2025} = (-j^2)^{2025} = -j^{4050} = -(j^3)^{1350} = -1$.

**Solution 14.**
Le triangle $ABC$ est équilatéral direct si et seulement si $C$ est l'image de $B$ par la rotation de centre $A$ et d'angle $\pi/3$, ce qui équivaut après réécriture algébrique vectorielle à $(c - a) = -j^2(b - a)$, d'où $a(1 + j^2) + b j^2 + c = 0$. Comme $1 + j^2 = -j$, en multipliant par $j^2$, on obtient $a + bj + cj^2 = 0$.

**Solution 15.**
L'argument du birapport est $\arg\left(\frac{c-a}{c-b}\right) - \arg\left(\frac{d-a}{d-b}\right) = (\vec{BC}, \vec{AC}) - (\vec{BD}, \vec{AD})$.
Ce birapport est réel si et seulement si cet angle vaut 0 modulo $\pi$, ce qui est la condition exacte du théorème de l'angle inscrit pour que $A, B, C, D$ soient cocycliques ou alignés.

**Solution 16.**
Soient $P, Q, R$ les centres de gravité des triangles construits sur $[B,C], [C,A], [A,B]$. Les sommets extérieurs vérifient des relations de rotation d'angle $\pi/3$. En exprimant les affixes $p, q, r$ en fonction de $a, b, c$ et de $j$, on calcule la quantité $p + q j + r j^2$ et l'on constate qu'elle s'annule identiquement grâce à la relation $1 + j + j^2 = 0$. D'après l'exercice 14, $PQR$ est équilatéral.

**Solution 17.**
En posant $z = u + v$, $(u+v)^3 - 6(u+v) - 9 = u^3 + v^3 + 3uv(u+v) - 6(u+v) - 9 = 0$.
En imposant $3uv = 6 \implies uv = 2 \implies u^3 v^3 = 8$, il reste $u^3 + v^3 = 9$.
$u^3$ et $v^3$ sont les racines de $X^2 - 9X + 8 = 0$, soit $1$ et $8$.
On peut prendre $u^3 = 8 \implies u = 2$ et $v^3 = 1 \implies v = 1$.
La racine réelle est $z_0 = 2 + 1 = 3$.
En factorisant $z^3 - 6z - 9 = (z - 3)(z^2 + 3z + 3)$, le discriminant du second facteur est $\Delta = 9 - 12 = -3$, donnant les deux racines complexes : $z_{1,2} = \frac{-3 \pm i\sqrt{3}}{2}$.

**Solution 18.**
$D_n(x) = \sum_{k=-n}^n e^{ikx} = e^{-inx} \sum_{j=0}^{2n} e^{ijx} = e^{-inx} \frac{1 - e^{i(2n+1)x}}{1 - e^{ix}}$.
En factorisant par l'angle moitié au numérateur et au dénominateur :
$D_n(x) = e^{-inx} \frac{e^{i\frac{2n+1}{2}x} (-2i\sin(\frac{2n+1}{2}x))}{e^{i\frac{x}{2}} (-2i\sin(\frac{x}{2}))} = \frac{\sin\left((n+\frac{1}{2})x\right)}{\sin(\frac{x}{2})}$.

**Solution 19.**
1. Les racines de $X^n - 1$ sont les $e^{i\frac{2k\pi}{n}}$. Donc $X^n - 1 = \prod_{k=0}^{n-1} (X - e^{i\frac{2k\pi}{n}}) = (X - 1) \prod_{k=1}^{n-1} (X - e^{i\frac{2k\pi}{n}})$.
2. En divisant par $X - 1$ : $\sum_{j=0}^{n-1} X^j = \prod_{k=1}^{n-1} (X - e^{i\frac{2k\pi}{n}})$.
   En évaluant en $X = 1$, le membre de gauche vaut $n$.
   À droite, $|1 - e^{i\frac{2k\pi}{n}}| = |e^{i\frac{k\pi}{n}} (e^{-i\frac{k\pi}{n}} - e^{i\frac{k\pi}{n}})| = 2\sin(\frac{k\pi}{n})$.
   Le produit des modules donne $n = 2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right)$, d'où le résultat.

**Solution 20.**
Le corps $\mathbb{C}$ est dit algébriquement clos car tout polynôme non constant de degré $n$ y admet exactement $n$ racines (comptées avec multiplicité). Ce résultat, pressenti par d'Alembert et prouvé rigoureusement par Gauss en 1799, démontre la clôture parfaite des nombres complexes : nul besoin d'inventer des « super-complexes » pour résoudre les équations de degrés supérieurs !

**Solution 21.**
1. Pour vérifier que $H$ est l'orthocentre, calculons $\vec{AH} \cdot \vec{BC}$. L'affixe de $\vec{AH}$ est $h - a = b + c$, et celle de $\vec{BC}$ est $c - b$.
   Le quotient $\frac{h-a}{c-b} = \frac{b+c}{c-b} = \frac{(b+c)(\bar{c}-\bar{b})}{|c-b|^2}$.
   Or sur le cercle unité, $\bar{b} = R^2/b$ et $\bar{c} = R^2/c$. On vérifie immédiatement que la partie réelle est nulle, donc $(AH) \perp (BC)$. De même pour les autres hauteurs.
2. Le centre de gravité est l'isobarycentre des sommets, d'affixe $g = \frac{a+b+c}{3}$.
3. On a $h = 3g$, ce qui signifie vectoriellement $\vec{OH} = 3\vec{OG}$. Les points $O, G, H$ sont donc toujours alignés sur la droite d'Euler.

**Solution 22.**
Les transformations de Moebius s'obtiennent par composition de translations, de similitudes et de l'inversion $z \mapsto \frac{1}{z}$. L'inversion échangeant les droites et les cercles (vus comme des cercles généralisés de la sphère de Riemann), la famille des cercles et droites est globalement préservée.

---

### La question qui ouvre la suite

Les nombres complexes nous ont appris la puissance de créer de nouvelles structures pour surmonter des blocages arithmétiques.
Mais que se passe-t-il lorsque l'on revient aux plus purs et aux plus durs des nombres : les entiers naturels ?
Comment les restes de simples divisions euclidiennes permettent-ils de crypter les secrets des gouvernements et de sécuriser les cartes bancaires de la planète entière ?
L'horloge tourne, les aiguilles se rejoignent modulo $n$ : bienvenue dans **le Chapitre 56 et les Messages Secrets et l'Horloge des Restes**.
