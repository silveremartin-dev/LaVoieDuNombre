# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 47 : Le Jardin qui Grandit et la Chaîne d'Engrenages

> *« Ne mémorise jamais une formule de dérivation comme une incantation magique pour réussir un examen. Regarde les roues dentées d'une bicyclette qui démultiplient l'effort de la pédale à la roue arrière : chaque vitesse multiplie la précédente. Regarde un bol de céramique qui recueille la pluie sans en perdre une goutte : sa forme tournée vers le ciel est une courbe convexe, et c'est l'accélération de sa pente qui décide si elle retient ou si elle verse. »*

---

### Ce que tu vas découvrir

- Pourquoi la dérivation d'une fonction composée fonctionne exactement comme une **boîte de vitesses de vélo** : la prestigieuse règle de la chaîne (*chain rule*) $(g \circ u)' = u' \cdot (g' \circ u)$.
- Les trois formules reines indispensables au baccalauréat : la dérivée de $e^{u(x)}$, de $\sqrt{u(x)}$ et de $(u(x))^n$.
- La **dérivée seconde** $f''(x)$ : après la vitesse instantanée, voici l'**accélération** et la courbure du tracé.
- La **convexité** : comprendre intuitivement et géométriquement ce qu'est une courbe « en forme de bol » tournée vers le haut ou « en cloche » tournée vers le bas.
- Les équivalences fondamentales du programme : sécantes au-dessus de la courbe, tangentes sous la courbe, et positivité de $f''(x)$.
- Les **points d'inflexion** : l'endroit précis où le cycliste redresse son guidon pour changer de virage, là où la courbe **traverse sa tangente**.
- Les **inégalités de convexité**, dont la célèbre $e^x \geq x + 1$ pour tout réel $x$.

---

### 1. Le problème : les engrenages en cascade et le bol de soupe

#### 1.1 Le cycliste et la boîte de vitesses

Imagine un vélo de course équipé d'un grand plateau de 50 dents au niveau du pédalier et d'un petit pignon de 25 dents sur la roue arrière.
- Lorsque le cycliste fait tourner ses pédales d'un angle $x$, le plateau avant tourne d'un angle $u = x$.
- La chaîne transmet le mouvement : puisque le pignon a deux fois moins de dents que le plateau, le pignon tourne deux fois plus vite :
  $$u \mapsto y = 2u.$$
- La roue arrière, solidaire du pignon, fait tourner le pneu sur le bitume : chaque tour de roue fait avancer le vélo d'une distance $z = 2{,}10 \times y$ mètres.

```
 [ Pédalier ] ────── Chaîne ──────► [ Pignon ] ────── Axe ──────► [ Roue / Sol ]
   Angle x                          Vitesse u                       Distance z
      │                                 │                                │
      └───────── Taux du/dx = 1 ────────┴────── Taux dz/du = 4.2 ────────┘
```

Si le cycliste appuie un peu plus vite sur les pédales (variation $\Delta x$) :
- la vitesse intermédiaire varie à un certain rythme : $\dfrac{\Delta u}{\Delta x}$ ;
- la vitesse finale de la roue varie par rapport à la vitesse intermédiaire au rythme : $\dfrac{\Delta z}{\Delta u}$.

À quelle vitesse la distance $z$ varie-t-elle par rapport à l'effort initial $x$ sur les pédales ?
La réponse du bon sens physique est immédiate : on **multiplie les rapports de démultiplication** !

$$\frac{\Delta z}{\Delta x} = \frac{\Delta z}{\Delta u} \times \frac{\Delta u}{\Delta x}.$$

Le physicien et mathématicien allemand Gottfried Wilhelm Leibniz écrivait cette formule dès 1684 sous la forme lumineuse :

$$\frac{dz}{dx} = \frac{dz}{du} \cdot \frac{du}{dx}.$$

Les deux $du$ semblent se simplifier comme dans une banale fraction de nombres ! C'est le secret de la dérivation des fonctions composées : **les sensibilités s'enchaînent par multiplication**.

#### 1.2 Le jardinier et le bol qui retient la pluie

Regarde maintenant deux récipients posés dans un jardin au printemps :
1. Un bol creux posé sur sa base : il se remplit d'eau de pluie. Si tu tires un trait droit entre deux points opposés du bord (une sécante), tout le fond du bol plonge **en dessous** du fil. Si tu poses une règle plate tangente sous le bol, tout le récipient repose **au-dessus** de la règle. C'est une courbe **convexe**.
2. Une cloche en verre posée à l'envers : l'eau de pluie glisse le long des parois et s'échappe. Une sécante reste sous la cloche, et une tangente reste au-dessus. C'est une courbe **concave**.

```
    Courbe Convexe (Bol qui retient l'eau)         Courbe Concave (Cloche qui verse l'eau)
              A                 B
               \   Sécante [AB]  /                            .--- Tangente
                \---------------/                            /   .-'""'-.
                 \             /                            /   /   /\   \
                  '._       _.'                                /   /  \   \
                     '-----'                                  /   /    \   \
          ─────── Tangente au fond ───────
```

Comment la dérivée peut-elle distinguer ces deux formes ? Comment une seule équation peut-elle prédire si un virage de montagne s'accentue ou s'adoucit ?
C'est le rôle de la **dérivée seconde**.

---

### 2. La Dérivée d'une Fonction Composée : la règle de la chaîne

#### 2.1 Les notations expliquées

- Soit $u$ une fonction définie sur un intervalle $I$ à valeurs dans un intervalle $J$, et soit $g$ une fonction définie sur $J$.
- La fonction composée est notée $g \circ u$ (lire « g rond u ») : pour tout $x \in I$, $(g \circ u)(x) = g\big(u(x)\big)$.
- Attention à l'ordre de lecture : dans $g\big(u(x)\big)$, on calcule **d'abord** $u(x)$ (la fonction intérieure), puis on donne le résultat à manger à $g$ (la fonction extérieure).
- La dérivée se note $(g \circ u)'$ ou $[g(u(x))]'$.

#### 2.2 Le Théorème Fondamental

> **📐 Théorème — Dérivée d'une fonction composée.**
> Soit $u$ une fonction dérivable sur un intervalle $I$, et soit $g$ une fonction dérivable sur un intervalle $J$ contenant $u(I)$.
> Alors la fonction composée $f = g \circ u$ est dérivable sur l'intervalle $I$, et pour tout réel $x \in I$ :
> $$(g \circ u)'(x) = u'(x) \times g'\big(u(x)\big).$$

*À voix haute :* « La dérivée de $g(u)$ est égale à $u'$ multiplié par $g'$ pris en $u$ ».

> **✍️ Idée de la démonstration.**
> Soit $x_0 \in I$. On forme le taux d'accroissement de la fonction composée entre $x$ et $x_0$ :
> $$\frac{g(u(x)) - g(u(x_0))}{x - x_0}.$$
> Si $u(x) \neq u(x_0)$ au voisinage de $x_0$, on peut insérer astucieusement le terme intermédiaire $u(x) - u(x_0)$ au numérateur et au dénominateur :
> $$\frac{g(u(x)) - g(u(x_0))}{x - x_0} = \frac{g(u(x)) - g(u(x_0))}{u(x) - u(x_0)} \times \frac{u(x) - u(x_0)}{x - x_0}.$$
> Lorsque $x \to x_0$ :
> - Par continuité de la fonction dérivable $u$, on a $\lim\limits_{x \to x_0} u(x) = u(x_0)$.
> - En posant $Y = u(x)$ et $Y_0 = u(x_0)$, le premier facteur devient $\dfrac{g(Y) - g(Y_0)}{Y - Y_0}$, qui tend vers le nombre dérivé $g'(Y_0) = g'\big(u(x_0)\big)$ puisque $g$ est dérivable en $u(x_0)$.
> - Le second facteur est le taux d'accroissement de $u$, qui tend par définition vers $u'(x_0)$.
> Par produit de limites :
> $$(g \circ u)'(x_0) = g'\big(u(x_0)\big) \times u'(x_0) = u'(x_0) \cdot g'\big(u(x_0)\big). \quad \blacksquare$$

---

### 3. Les Trois Formules Reines du Baccalauréat

Toutes les dérivées délicates de l'épreuve de spécialité mathématiques sont des cas particuliers immédiats de cette règle de la chaîne, où l'on remplace $g$ par les trois grandes fonctions du cours :

#### 3.1 Dérivée de $e^{u(x)}$ : la reine des fonctions

Prenons $g(y) = e^y$. On sait que $g'(y) = e^y$.
En appliquant la formule générale $(g \circ u)' = u' \cdot g'(u)$ :

> **📐 Propriété — Dérivée de l'exponentielle composée.**
> Soit $u$ une fonction dérivable sur un intervalle $I$.
> La fonction $f : x \mapsto e^{u(x)}$ est dérivable sur $I$, et pour tout $x \in I$ :
> $$\mathbf{\big(e^{u(x)}\big)' = u'(x) \, e^{u(x)}}.$$

*Exemple éclair :* Soit $f(x) = e^{-3x^2 + 5x}$.
Ici $u(x) = -3x^2 + 5x$, donc $u'(x) = -6x + 5$.
On applique directement : $f'(x) = (-6x + 5)e^{-3x^2 + 5x}$.

#### 3.2 Dérivée de $\sqrt{u(x)}$

Prenons $g(y) = \sqrt{y}$ définie pour $y > 0$. Sa dérivée est $g'(y) = \dfrac{1}{2\sqrt{y}}$.

> **📐 Propriété — Dérivée de la racine carrée composée.**
> Soit $u$ une fonction dérivable et **strictement positive** sur un intervalle $I$.
> La fonction $f : x \mapsto \sqrt{u(x)}$ est dérivable sur $I$, et pour tout $x \in I$ :
> $$\mathbf{\big(\sqrt{u(x)}\big)' = \frac{u'(x)}{2\sqrt{u(x)}}}.$$

> **⚠️ Attention, piège ! — La condition $u(x) > 0$.**
> La fonction $\sqrt{u(x)}$ est définie dès que $u(x) \geq 0$, mais elle n'est **dérivable** que là où $u(x) > 0$ (strictement positif). Si $u(x_0) = 0$, la courbe présente généralement une demi-tangente verticale en $x_0$, et le dénominateur $2\sqrt{u(x)}$ s'annulerait !

#### 3.3 Dérivée de $(u(x))^n$

Prenons $g(y) = y^n$ avec $n \in \mathbb{Z}^*$. Sa dérivée est $g'(y) = n y^{n-1}$.

> **📐 Propriété — Dérivée d'une puissance composée.**
> Soit $u$ une fonction dérivable sur un intervalle $I$.
> Pour tout entier relatif $n \geq 1$ (ou $n < 0$ sur les intervalles où $u(x) \neq 0$) :
> $$\mathbf{\big(u^n\big)' = n \, u'(x) \, \big(u(x)\big)^{n-1}}.$$

*Cas particulier fondamental :* Pour $n = -1$, la formule donne la dérivée de l'inverse :
$$\left(\frac{1}{u}\right)' = \big(u^{-1}\big)' = -1 \cdot u' \cdot u^{-2} = \mathbf{-\frac{u'}{u^2}}.$$

#### Tableau récapitulatif comparatif

| Fonction simple $f(x)$ | Dérivée $f'(x)$ | Fonction composée $f(x)$ | Dérivée $f'(x)$ | Condition de validité |
| :---: | :---: | :---: | :---: | :--- |
| $x^n$ | $n x^{n-1}$ | $\big(u(x)\big)^n$ | $\mathbf{n \, u'(x) \, \big(u(x)\big)^{n-1}}$ | $u$ dérivable ($u \neq 0$ si $n \leq 0$) |
| $\dfrac{1}{x}$ | $-\dfrac{1}{x^2}$ | $\dfrac{1}{u(x)}$ | $\mathbf{-\dfrac{u'(x)}{\big(u(x)\big)^2}}$ | $u(x) \neq 0$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ | $\sqrt{u(x)}$ | $\mathbf{\dfrac{u'(x)}{2\sqrt{u(x)}}}$ | $\mathbf{u(x) > 0}$ |
| $e^x$ | $e^x$ | $e^{u(x)}$ | $\mathbf{u'(x) \, e^{u(x)}}$ | $u$ dérivable sur $I$ |

---

### 4. La Dérivée Seconde : après la vitesse, l'accélération

#### 4.1 Définition et notations

Lorsque la fonction dérivée $f'$ est elle-même dérivable sur un intervalle $I$, sa propre dérivée est appelée la **dérivée seconde** de $f$, et on la note :

$$\mathbf{f''(x)} \quad \text{ou} \quad \mathbf{\frac{d^2f}{dx^2}(x)} \quad \text{(notation de Leibniz)}.$$

- $f(x)$ décrit la **position** (altitude, température, capital).
- $f'(x)$ décrit la **vitesse instantanée** d'évolution (pente de la tangente).
- $f''(x)$ décrit l'**accélération** : la vitesse à laquelle la pente elle-même augmente ou diminue.

*En physique :* Si $x(t)$ est la position d'un mobile au cours du temps, la vitesse est $v(t) = x'(t)$ et l'accélération est $a(t) = v'(t) = x''(t)$.
Isaac Newton a fondé toute la mécanique classique sur cette équation universelle :
$$F = m \cdot a = m \cdot x''(t).$$
Sans dérivée seconde, impossible de comprendre la gravitation des planètes ou le freinage d'un véhicule.

---

### 5. La Convexité : le bol, les cordes et les tangentes

#### 5.1 Définition géométrique fondamentale

> **📐 Définition géométrique — Fonction convexe / concave.**
> Soit $f$ une fonction définie sur un intervalle $I$.
> - On dit que $f$ est **convexe** sur $I$ si, pour tous points $A$ et $B$ appartenant à la courbe représentative $\mathcal{C}_f$, le segment $[AB]$ (la corde) est situé **au-dessus** de la courbe sur l'intervalle entre $A$ et $B$.
> - On dit que $f$ est **concave** sur $I$ si, pour tous points $A$ et $B$ de la courbe, le segment $[AB]$ est situé **en dessous** de la courbe.

```
       CONVEXE (segment AU-DESSUS)                  CONCAVE (segment EN DESSOUS)
       y ▲                                          y ▲
         │  A             B                           │         .---. Arc de courbe
         │   \  Segment  /                            │        /  _  \
         │    \ [AB]    /                             │    A  /.-' '-.\  B
         │     \_______/  Arc de courbe               │      /─────────\  Segment [AB]
         └──────────────────────► x                   └──────────────────────► x
```

*Remarque pratique :* Une fonction $f$ est concave si et seulement si son opposée $-f$ est convexe.

#### 5.2 Les caractérisations équivalentes (Théorème du programme)

Pour une fonction deux fois dérivable, le programme officiel établit une triple équivalence magistrale reliant la géométrie des cordes, le tracé des tangentes et le calcul différentiel :

> **📐 Théorème fondamental — Caractérisations de la convexité.**
> Soit $f$ une fonction deux fois dérivable sur un intervalle $I$. Les propositions suivantes sont **strictement équivalentes** :
> 1. $f$ est **convexe** sur $I$ ;
> 2. La fonction dérivée $f'$ est **croissante** sur $I$ ;
> 3. Pour tout $x \in I$, la dérivée seconde est positive ou nulle : **$f''(x) \geq 0$** ;
> 4. La courbe $\mathcal{C}_f$ est entièrement située **au-dessus de toutes ses tangentes**.

Et de façon symétrique pour la concavité :

> **📐 Théorème — Caractérisations de la concavité.**
> Soit $f$ deux fois dérivable sur un intervalle $I$. Les propositions suivantes sont équivalentes :
> 1. $f$ est **concave** sur $I$ ;
> 2. La fonction dérivée $f'$ est **décroissante** sur $I$ ;
> 3. Pour tout $x \in I$, la dérivée seconde est négative ou nulle : **$f''(x) \leq 0$** ;
> 4. La courbe $\mathcal{C}_f$ est entièrement située **en dessous de toutes ses tangentes**.

#### 5.3 Les Inégalités de Convexité

Puisque la courbe d'une fonction convexe est toujours au-dessus de sa tangente en n'importe quel point d'abscisse $x_0$, on a immédiatement pour tout réel $x$ :

$$\mathbf{f(x) \geq f'(x_0)(x - x_0) + f(x_0)}.$$

Appliquons cette propriété magique à la fonction exponentielle $f(x) = e^x$ au point $x_0 = 0$ :
- $f(0) = e^0 = 1$ ;
- $f'(x) = e^x \implies f'(0) = 1$ ;
- $f''(x) = e^x > 0$ sur $\mathbb{R}$, donc l'exponentielle est **strictement convexe** sur $\mathbb{R}$.

La tangente en 0 a pour équation : $y = 1 \cdot (x - 0) + 1 = x + 1$.
Puisque la courbe est au-dessus de sa tangente, on obtient l'inégalité fondamentale du lycée :

> **📐 Inégalité de convexité remarquable — L'exponentielle au-dessus de sa tangente :**
> Pour tout réel $x \in \mathbb{R}$ :
> $$\mathbf{e^x \geq x + 1}.$$
> Avec égalité si et seulement si $x = 0$.

```
       y ▲                        /  y = e^x (convexe)
         │                       /
         │                     /  /  y = x + 1 (tangente en 0)
         │                   /  /
       1 ┼                  * /
         │                 /
─────────┼────────────────┼────────────────► x
        -1                0
```

Cette inégalité permet de démontrer en deux lignes que $\lim\limits_{x \to +\infty} e^x = +\infty$, car $e^x \geq x + 1 \to +\infty$.

---

### 6. Le Point d'Inflexion : le virage qui s'inverse

Imagine que tu conduis une voiture sur une route de campagne sinueuse :
- Au début, la route tourne vers la droite : tu inclines ton volant vers la droite (la courbure est convexe).
- Plus loin, la route tourne vers la gauche : tu inclines ton volant vers la gauche (la courbure devient concave).
- Il y a un instant infinitésimal, pile entre les deux virages, où **ton volant repasse rigoureusement au centre (neutre)**.

Cet instant de transition est un **point d'inflexion**.

#### 6.1 Définition géométrique

> **📐 Définition — Point d'inflexion.**
> Soit $f$ une fonction dérivable sur un intervalle $I$.
> On appelle **point d'inflexion** tout point $A\big(x_0 \,;\, f(x_0)\big)$ de la courbe $\mathcal{C}_f$ où la courbe **traverse sa tangente**.

```
              Courbe f(x)
                 \
                  \        Tangente T
        Concave    \      /
     (sous la T.)   \    /
                     \  /
           ───────────*─────────── Point d'Inflexion (x_0, f(x_0))
                     / \
                    /   \     Convexe
                   /     \  (au-dessus de la T.)
                  /       \
```

#### 6.2 Caractérisation par la dérivée seconde

> **📐 Théorème fondamental — Condition nécessaire et suffisante d'inflexion.**
> Soit $f$ une fonction deux fois dérivable sur un intervalle $I$.
> Le point $A\big(x_0 \,;\, f(x_0)\big)$ est un **point d'inflexion** si et seulement si :
> **La dérivée seconde $f''$ s'annule en $x_0$ EN CHANGEANT DE SIGNE.**

> **⚠️ Attention, piège ! — L'annulation seule NE SUFFIT PAS !**
> C'est l'un des pièges favoris des épreuves de baccalauréat.
> Si $f''(x_0) = 0$, cela ne garantit **absolument pas** que $x_0$ soit un point d'inflexion ! Il faut impérativement vérifier que $f''$ **change de signe** (de $+$ vers $-$ ou de $-$ vers $+$).
> **Contre-exemple éclatant :** Soit $f(x) = x^4$.
> - $f'(x) = 4x^3$ ;
> - $f''(x) = 12x^2$.
> En $x_0 = 0$, on a bien $f''(0) = 12 \times 0^2 = 0$.
> Pourtant, pour tout $x \neq 0$, $12x^2 > 0$ : la dérivée seconde est toujours positive ! Elle s'annule en 0 sans jamais changer de signe.
> La courbe de $x^4$ est entièrement convexe (un bol aplati), et sa tangente en 0 est l'axe des abscisses ($y = 0$). La courbe reste constamment au-dessus de sa tangente : **il n'y a aucun point d'inflexion en 0 !**

---

### 7. Attention, pièges !

> **⚠️ Attention, piège ! — Oublier $u'(x)$ dans les dérivées de composées.**
> - Écrire $\left(e^{5x}\right)' = e^{5x}$ est faux ! La bonne réponse est $5e^{5x}$.
> - Écrire $\left(\sqrt{x^2 + 1}\right)' = \frac{1}{2\sqrt{x^2+1}}$ est faux ! La bonne réponse est $\frac{2x}{2\sqrt{x^2+1}} = \frac{x}{\sqrt{x^2+1}}$.
> - Écrire $\left((3x - 2)^4\right)' = 4(3x - 2)^3$ est faux ! La bonne réponse est $4 \times 3 \times (3x - 2)^3 = 12(3x - 2)^3$.
> Le réflexe absolu : dès que l'argument n'est pas un banal $x$, **on doit faire sortir $u'(x)$ devant**.

> **⚠️ Attention, piège ! — Confondre variations et convexité.**
> - Une fonction peut être **croissante et convexe** (ex: $e^x$ sur $\mathbb{R}$, $x^2$ sur $[0 ; +\infty[$).
> - Une fonction peut être **croissante et concave** (ex: $\sqrt{x}$ sur $[0 ; +\infty[$, $\ln x$ sur $]0 ; +\infty[$).
> - Une fonction peut être **décroissante et convexe** (ex: $e^{-x}$ sur $\mathbb{R}$, $\frac{1}{x}$ sur $]0 ; +\infty[$).
> - Une fonction peut être **décroissante et concave** (ex: $-x^2$ sur $[0 ; +\infty[$).
> Le signe de $f'$ donne les variations (monte ou descend) ; le signe de $f''$ donne la courbure (creux vers le haut ou bosse vers le bas).

---

### 8. Exemples Résolus pas à pas

#### Exemple résolu 1 — Dérivation de composées multiples

**Énoncé :** Calculer la fonction dérivée de chacune des fonctions suivantes en précisant le domaine de dérivation :
1. $f(x) = e^{-x^2 + 4x}$ sur $\mathbb{R}$
2. $g(x) = \sqrt{3x^2 + 6}$ sur $\mathbb{R}$
3. $h(x) = (2x^3 - 5x)^4$ sur $\mathbb{R}$
4. $k(x) = \dfrac{1}{(x^2 + 1)^3}$ sur $\mathbb{R}$

**Solution :**
1. $f$ est de la forme $e^u$ avec $u(x) = -x^2 + 4x$.
   $u'(x) = -2x + 4$.
   $$f'(x) = u'(x)e^{u(x)} = (-2x + 4)e^{-x^2 + 4x}.$$
2. $g$ est de la forme $\sqrt{u}$ avec $u(x) = 3x^2 + 6$.
   Pour tout réel $x$, $3x^2 + 6 \geq 6 > 0$, donc $g$ est dérivable sur $\mathbb{R}$.
   $u'(x) = 6x$.
   $$g'(x) = \frac{u'(x)}{2\sqrt{u(x)}} = \frac{6x}{2\sqrt{3x^2 + 6}} = \frac{3x}{\sqrt{3x^2 + 6}}.$$
3. $h$ est de la forme $u^4$ avec $u(x) = 2x^3 - 5x$.
   $u'(x) = 6x^2 - 5$.
   $$h'(x) = 4 \, u'(x) \, \big(u(x)\big)^3 = 4(6x^2 - 5)(2x^3 - 5x)^3.$$
4. Écrivons $k(x) = (x^2 + 1)^{-3}$, soit $u^{-3}$ avec $u(x) = x^2 + 1$.
   $u'(x) = 2x$.
   $$k'(x) = -3 \cdot u'(x) \cdot \big(u(x)\big)^{-4} = -3(2x)(x^2 + 1)^{-4} = \frac{-6x}{(x^2 + 1)^4}.$$

---

#### Exemple résolu 2 — Étude complète de convexité d'une fonction polynomiale

**Énoncé :** Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = x^4 - 2x^3 - 12x^2 + 5x - 1$.
1. Calculer $f'(x)$ puis la dérivée seconde $f''(x)$.
2. Déterminer les intervalles sur lesquels $f$ est convexe, et ceux sur lesquels $f$ est concave.
3. En déduire les coordonnées des points d'inflexion de la courbe $\mathcal{C}_f$.

**Solution :**
1. $f$ est deux fois dérivable sur $\mathbb{R}$ comme fonction polynôme :
   - $f'(x) = 4x^3 - 6x^2 - 24x + 5$
   - $f''(x) = 12x^2 - 12x - 24 = 12(x^2 - x - 2)$.
2. Factorisons le trinôme $x^2 - x - 2$ :
   Ses racines évidentes sont $x_1 = -1$ et $x_2 = 2$ (car $(-1)^2 - (-1) - 2 = 0$ et $2^2 - 2 - 2 = 0$).
   Le trinôme est du signe de $a = 12 > 0$ à l'extérieur des racines et strictement négatif entre les racines :
   - Pour $x \in ]-\infty \,;\, -1]$, $f''(x) \geq 0$ : la fonction $f$ est **convexe**.
   - Pour $x \in [-1 \,;\, 2]$, $f''(x) \leq 0$ : la fonction $f$ est **concave**.
   - Pour $x \in [2 \,;\, +\infty[$, $f''(x) \geq 0$ : la fonction $f$ est **convexe**.
3. La dérivée seconde $f''$ s'annule en changeant de signe en $x = -1$ et en $x = 2$.
   La courbe $\mathcal{C}_f$ admet donc deux points d'inflexion :
   - En $x = -1$ : $f(-1) = 1 + 2 - 12 - 5 - 1 = -15$. Premier point d'inflexion : $I_1(-1 \,;\, -15)$.
   - En $x = 2$ : $f(2) = 16 - 16 - 48 + 10 - 1 = -39$. Second point d'inflexion : $I_2(2 \,;\, -39)$.

---

#### Exemple résolu 3 — La courbe en cloche de Gauss : convexité et inflexions

**Énoncé :** On considère la fonction gaussienne $f(x) = e^{-x^2/2}$ définie sur $\mathbb{R}$.
1. Calculer $f'(x)$ et étudier les variations de $f$.
2. Calculer $f''(x)$ et étudier son signe.
3. Déterminer les points d'inflexion de la courbe en cloche de Gauss.

**Solution :**
1. $f(x) = e^{u(x)}$ avec $u(x) = -\frac{1}{2}x^2$, d'où $u'(x) = -x$.
   $$f'(x) = -x e^{-x^2/2}.$$
   Comme $e^{-x^2/2} > 0$ pour tout réel $x$, $f'(x)$ est du signe de $-x$ :
   - $f'(x) > 0$ sur $]-\infty \,;\, 0[$ : $f$ est strictement croissante.
   - $f'(x) < 0$ sur $]0 \,;\, +\infty[$ : $f$ est strictement décroissante.
   - En $x = 0$, $f(0) = e^0 = 1$ est le maximum absolu.

2. Dérivons $f'(x)$ sous forme d'un produit $u \cdot v$ avec $u(x) = -x$ ($u' = -1$) et $v(x) = e^{-x^2/2}$ ($v' = -x e^{-x^2/2}$) :
   $$f''(x) = u'v + uv' = (-1)e^{-x^2/2} + (-x)(-x e^{-x^2/2}) = (-1 + x^2)e^{-x^2/2} = (x^2 - 1)e^{-x^2/2}.$$
   Puisque $e^{-x^2/2} > 0$, le signe de $f''(x)$ est exactement celui de $x^2 - 1 = (x - 1)(x + 1)$ :
   - $f''(x) \geq 0$ sur $]-\infty \,;\, -1] \cup [1 \,;\, +\infty[$ : $f$ y est **convexe**.
   - $f''(x) \leq 0$ sur $[-1 \,;\, 1]$ : $f$ y est **concave**.

3. La dérivée seconde $f''$ s'annule en changeant de signe en $x = -1$ et en $x = 1$.
   Les ordonnées associées sont $f(-1) = f(1) = e^{-1/2} = \frac{1}{\sqrt{e}} \approx 0{,}6065$.
   La courbe en cloche admet donc exactement **deux points d'inflexion** en $(-1 \,;\, e^{-1/2})$ et $(1 \,;\, e^{-1/2})$.
   *(En statistiques et probabilités, ces points d'inflexion correspondent exactement à un écart-type $\pm \sigma$ de la moyenne).*

---

#### Exemple résolu 4 — Tangente et position relative par convexité

**Énoncé :** Soit la fonction $f(x) = (2x - 1)e^x$ sur $\mathbb{R}$.
1. Calculer $f'(x)$ et $f''(x)$.
2. Démontrer que $f$ est convexe sur $[-\frac{1}{2} \,;\, +\infty[$.
3. Déterminer l'équation de la tangente $(T)$ à la courbe $\mathcal{C}_f$ au point d'abscisse 0.
4. En déduire la position relative de $\mathcal{C}_f$ par rapport à $(T)$ sur $[-\frac{1}{2} \,;\, +\infty[$.

**Solution :**
1. **Dérivées :**
   $f'(x) = 2e^x + (2x - 1)e^x = (2x + 1)e^x$.
   $f''(x) = 2e^x + (2x + 1)e^x = (2x + 3)e^x$.
2. **Convexité :**
   Comme $e^x > 0$, le signe de $f''(x)$ est celui de $2x + 3$.
   Pour tout $x \geq -\frac{1}{2}$, on a $2x + 3 \geq 2(-\frac{1}{2}) + 3 = -1 + 3 = 2 > 0$.
   Ainsi, $f''(x) \geq 0$ sur $[-\frac{1}{2} \,;\, +\infty[$, ce qui prouve que $f$ est **strictement convexe** sur cet intervalle.
3. **Tangente en 0 :**
   $f(0) = (0 - 1)e^0 = -1$.
   $f'(0) = (0 + 1)e^0 = 1$.
   L'équation de la tangente $(T)$ est :
   $$y = f'(0)(x - 0) + f(0) = 1(x) - 1 = x - 1.$$
4. **Position relative :**
   Puisque $f$ est convexe sur $[-\frac{1}{2} \,;\, +\infty[$ et que le point d'abscisse $0$ appartient à cet intervalle ($0 \geq -\frac{1}{2}$), la courbe $\mathcal{C}_f$ est située **au-dessus de sa tangente $(T)$** sur $[-\frac{1}{2} \,;\, +\infty[$.
   C'est-à-dire que pour tout $x \geq -\frac{1}{2}$ :
   $$(2x - 1)e^x \geq x - 1.$$

---

#### Exemple résolu 5 — Dérivation d'une fonction puissance avec quotient

**Énoncé :** Soit la fonction $f(x) = \left(\dfrac{x - 1}{x + 1}\right)^3$ définie sur $\mathbb{R} \setminus \{-1\}$.
Calculer sa dérivée $f'(x)$ et déterminer son sens de variation sur son ensemble de définition.

**Solution :**
Posons $u(x) = \dfrac{x - 1}{x + 1}$.
Calculons d'abord $u'(x)$ par la formule du quotient $\left(\frac{w}{v}\right)' = \frac{w'v - wv'}{v^2}$ :
$$u'(x) = \frac{1(x + 1) - (x - 1)(1)}{(x + 1)^2} = \frac{x + 1 - x + 1}{(x + 1)^2} = \frac{2}{(x + 1)^2}.$$
La fonction $f$ est de la forme $u^3$, donc sa dérivée est $f'(x) = 3 \, u'(x) \, \big(u(x)\big)^2$ :
$$f'(x) = 3 \times \frac{2}{(x + 1)^2} \times \left(\frac{x - 1}{x + 1}\right)^2 = \frac{6(x - 1)^2}{(x + 1)^4}.$$
Étudions le signe de $f'(x)$ :
- Le dénominateur $(x + 1)^4$ est une puissance 4ème, strictement positive pour tout $x \neq -1$.
- Le numérateur $6(x - 1)^2$ est un carré multiplié par 6, donc toujours positif ou nul, s'annulant uniquement en $x = 1$.
Par conséquent, $f'(x) \geq 0$ pour tout $x \in ]-\infty \,;\, -1[ \cup ]-1 \,;\, +\infty[$.
La fonction $f$ est donc **strictement croissante** sur $]-\infty \,;\, -1[$ et **strictement croissante** sur $]-1 \,;\, +\infty[$.

---

#### Exemple résolu 6 — Trouver l'abscisse du point d'inflexion d'un coût moyen

**Énoncé :** Une entreprise produit une quantité $q \in [0 \,;\, 10]$ (en tonnes) d'un polymère chimique. Le coût total de production en milliers d'euros est modélisé par la fonction :
$$C(q) = q^3 - 6q^2 + 15q + 10.$$
1. Démontrer que le coût marginal $C'(q)$ est strictement croissant sur $[2 \,;\, 10]$.
2. Déterminer l'abscisse du point d'inflexion de la courbe du coût total et interpréter économiquement ce point (loi des rendements décroissants).

**Solution :**
1. Calculons le coût marginal (dérivée première) et sa variation (dérivée seconde) :
   $$C'(q) = 3q^2 - 12q + 15.$$
   $$C''(q) = 6q - 12 = 6(q - 2).$$
   Pour tout $q > 2$, $C''(q) > 0$. Donc la fonction $C'$ est **strictement croissante** sur $[2 \,;\, 10]$.
2. **Point d'inflexion :**
   $C''(q) = 0 \iff 6q - 12 = 0 \iff q = 2$.
   - Pour $q < 2$, $C''(q) < 0$ : la fonction coût est concave.
   - Pour $q > 2$, $C''(q) > 0$ : la fonction coût est convexe.
   La dérivée seconde s'annule en changeant de signe en $q = 2$. Le point d'abscisse $q = 2$ est donc le **point d'inflexion** de la courbe des coûts.
   *Interprétation économique :*
   - Pour $q \in [0 \,;\, 2]$, la production bénéficie d'économies d'échelle : chaque tonne supplémentaire coûte moins cher à fabriquer que la précédente (le coût marginal diminue).
   - À partir de $q = 2$ tonnes, l'atelier commence à saturer, les machines s'usent, les heures supplémentaires s'accumulent : chaque tonne supplémentaire coûte de plus en plus cher (rendements décroissants). $q = 2$ est le point de bascule de rentabilité.

---

### Ce qu'il faut retenir

1. **Règle de la chaîne :** $(g \circ u)'(x) = u'(x) \cdot g'\big(u(x)\big)$.
2. **Les 3 dérivées composées indispensables :**
   - $\big(e^u\big)' = u' e^u$
   - $\big(\sqrt{u}\big)' = \dfrac{u'}{2\sqrt{u}}$ (pour $u > 0$)
   - $\big(u^n\big)' = n u' u^{n-1}$
3. **Convexité et dérivée seconde :**
   - $f''(x) \geq 0 \iff f'$ croissante $\iff f$ convexe $\iff$ courbe au-dessus de ses tangentes.
   - $f''(x) \leq 0 \iff f'$ décroissante $\iff f$ concave $\iff$ courbe en dessous de ses tangentes.
4. **Point d'inflexion :** point où la courbe traverse sa tangente $\iff f''(x)$ s'annule **en changeant de signe**.
5. **Inégalité de convexité fondamentale :** Pour tout réel $x$, $e^x \geq x + 1$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 47.1.** Déterminer la fonction dérivée de chacune des fonctions suivantes :
1. $f(x) = e^{4x - 1}$
2. $g(x) = e^{-x^3}$
3. $h(x) = \sqrt{5x + 2}$ sur $]-\frac{2}{5} \,;\, +\infty[$
4. $k(x) = (3x - 7)^5$

**Exercice 47.2.** Calculer la dérivée seconde $f''(x)$ des fonctions suivantes :
1. $f(x) = 2x^4 - 5x^3 + x - 8$
2. $g(x) = e^{2x}$
3. $h(x) = \dfrac{1}{x}$ sur $]0 \,;\, +\infty[$

**Exercice 47.3.** On donne la fonction $f(x) = x^3 - 6x^2 + 2x - 1$.
1. Calculer $f''(x)$.
2. Déterminer les intervalles où $f$ est convexe, et ceux où elle est concave.
3. Préciser le point d'inflexion de sa courbe.

**Exercice 47.4.** La courbe d'une fonction deux fois dérivable $f$ admet une tangente en $x_0 = 3$ d'équation $y = 4x - 1$.
Sachant que $f''(x) \geq 0$ pour tout $x \in \mathbb{R}$, comparer sans calcul $f(3{,}1)$ et $11{,}4$.

**Exercice 47.5.** Déterminer la dérivée de $f(x) = \sqrt{e^x + 1}$ sur $\mathbb{R}$.

**Exercice 47.6.** Soit $f(x) = x e^{-x}$. Calculer $f'(x)$ et $f''(x)$.

**Exercice 47.7.** Une fonction $f$ vérifie $f''(x) = (x - 3)^2 (x + 1)$.
Quelles sont les abscisses des points d'inflexion de la courbe de $f$ ? (Attention au piège !).

**Exercice 47.8.** Déterminer les variations de $f'(x)$ pour $f(x) = \dfrac{x^3}{3} - x^2 + 5x$.

---

#### Niveau ★★ (Réflexion et type Bac)

**Exercice 47.9 (Type Bac : Étude complète d'une fonction avec exponentielle et convexité).**
On considère la fonction $f$ définie sur $\mathbb{R}$ par :
$$f(x) = (x^2 - 2x + 1)e^x.$$
1. Démontrer que pour tout réel $x$, $f'(x) = (x^2 - 1)e^x$.
2. Dresser le tableau de variations complet de $f$ sur $\mathbb{R}$ en précisant les limites en $-\infty$ et en $+\infty$.
3. Calculer $f''(x)$ et prouver que $f''(x) = (x^2 + 2x - 1)e^x$.
4. Déterminer les intervalles de convexité de $f$.
5. Déterminer les abscisses exactes des points d'inflexion de $\mathcal{C}_f$.

**Exercice 47.10 (Position relative et inégalité de convexité).**
Soit $f(x) = \sqrt{x}$ définie sur $[0 \,;\, +\infty[$.
1. Calculer $f'(x)$ et $f''(x)$ pour $x > 0$.
2. En déduire la concavité de la fonction racine carrée sur $]0 \,;\, +\infty[$.
3. Donner l'équation de la tangente $(T)$ à la courbe de la racine carrée en $x_0 = 1$.
4. En déduire que pour tout $x > 0$ : $\sqrt{x} \leq \dfrac{x + 1}{2}$.
   *(Retrouver ainsi l'inégalité arithmético-géométrique entre $\sqrt{x}$ et la moyenne de $x$ et $1$).*

**Exercice 47.11 (Type Bac : Étude de profil de rampe de skatepark).**
Un architecte conçoit la coupe transversale d'une rampe de skatepark sur $[-2 \,;\, 2]$ modélisée par la fonction :
$$f(x) = \frac{1}{1 + e^{-2x}}.$$
1. Démontrer que $f'(x) = \dfrac{2e^{-2x}}{(1 + e^{-2x})^2}$.
2. Calculer $f''(x)$ et montrer qu'elle s'écrit sous la forme $f''(x) = \dfrac{4e^{-2x}(e^{-2x} - 1)}{(1 + e^{-2x})^3}$.
3. Déterminer le point d'inflexion de la rampe. Pourquoi ce point correspond-il à la zone où la pente de la rampe est maximale en valeur absolue ?

**Exercice 47.12 (Vrai ou Faux rigoureusement argumenté).**
1. « Si $f''(x_0) = 0$, alors la courbe de $f$ admet un point d'inflexion en $x_0$. »
2. « Si une fonction est strictement croissante, alors elle est convexe. »
3. « La somme de deux fonctions convexes sur un intervalle $I$ est une fonction convexe sur $I$. »
4. « Le produit de deux fonctions convexes sur $I$ est toujours une fonction convexe sur $I$. »

**Exercice 47.13 (Dérivation d'une fonction composée trigonométrique).**
Calculer la dérivée des fonctions suivantes :
1. $f(x) = \cos(3x^2 - 2)$
2. $g(x) = e^{\sin(x)}$
3. $h(x) = \sin^3(2x)$

**Exercice 47.14 (Convexité de l'inverse d'une fonction).**
Soit $u$ une fonction deux fois dérivable, strictement positive et concave sur un intervalle $I$.
On pose $f = \dfrac{1}{u}$.
1. Calculer $f'$ puis $f''$ en fonction de $u, u'$ et $u''$.
2. Démontrer que $f$ est une fonction convexe sur $I$.

**Exercice 47.15 (Inégalité de convexité pour la fonction carré).**
Soit $f(x) = x^2$ sur $\mathbb{R}$.
1. Rappeler pourquoi $f$ est convexe.
2. Écrire la définition géométrique de la convexité pour deux réels quelconques $a$ et $b$ avec le milieu $m = \frac{a+b}{2}$ :
   montrer que $\left(\dfrac{a+b}{2}\right)^2 \leq \dfrac{a^2 + b^2}{2}$.
3. Démontrer algébriquement cette inégalité en développant $\frac{a^2+b^2}{2} - \left(\frac{a+b}{2}\right)^2$.

**Exercice 47.16 (Cinématique et freinage d'un TGV).**
La position (en mètres) d'un train à grande vitesse lors d'une séquence de freinage d'urgence est donnée pour $t \in [0 \,;\, 20]$ (en secondes) par :
$$x(t) = -0{,}15 t^3 + 4{,}5 t^2 + 30 t.$$
1. Déterminer la vitesse instantanée $v(t) = x'(t)$ du train à $t = 0$ et à $t = 10\text{ s}$.
2. Déterminer l'accélération $a(t) = x''(t)$.
3. À quel instant la décélération subie par les passagers est-elle la plus forte en intensité ?

**Exercice 47.17 (Étude complète de la dérivée de $u^n$).**
Soit la fonction $f(x) = (x^2 - 4x + 3)^3$ sur $\mathbb{R}$.
1. Déterminer les zéros de $f$.
2. Calculer $f'(x)$ sous forme factorisée.
3. Dresser le tableau de variations complet de $f$.

---

#### Niveau ★★★ (Défi et approfondissement)

**Exercice 47.18 (L'inégalité de Jensen pour les fonctions convexes).**
Soit $f$ une fonction convexe sur un intervalle $I$.
1. L'inégalité de convexité pour deux points affirme que pour tout $\lambda \in [0 \,;\, 1]$ et tous $x, y \in I$ :
   $$f\big(\lambda x + (1-\lambda)y\big) \leq \lambda f(x) + (1-\lambda)f(y).$$
   Interpréter cette inégalité géométriquement en reliant $\lambda$ à la position sur le segment $[AB]$.
2. Par récurrence, démontrer l'inégalité de Jensen pour $n$ nombres : si $x_1, x_2, \dots, x_n \in I$, alors :
   $$f\left(\frac{x_1 + x_2 + \dots + x_n}{n}\right) \leq \frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}.$$
3. Appliquer l'inégalité de Jensen à la fonction convexe $f(x) = x^2$ pour démontrer que la moyenne des carrés est toujours supérieure ou égale au carré de la moyenne (variance positive).

**Exercice 47.19 (Démonstration rigoureuse de la position relative par Taylor-Lagrange).**
Soit $f$ deux fois dérivable sur un intervalle $I$. Soit $a \in I$.
La formule de Taylor avec reste intégral (ou l'inégalité des accroissements finis appliquée à $g(t) = f(t) - f'(a)(t - a)$) montre que pour tout $x \in I$ :
$$f(x) - \big[f'(a)(x - a) + f(a)\big] = \int_a^x (x - t) f''(t) \, dt.$$
1. Montrer que la fonction intégrée $(x - t)f''(t)$ garde un signe positif pour $t$ entre $a$ et $x$ dès lors que $f''(t) \geq 0$.
2. En déduire de façon analytique pure que toute fonction vérifiant $f'' \geq 0$ est située au-dessus de sa tangente en tout point $a$.

**Exercice 47.20 (Recherche d'un polynôme de degré 3 avec point d'inflexion imposé).**
On considère un polynôme général de degré 3 : $P(x) = ax^3 + bx^2 + cx + d$ avec $a \neq 0$.
1. Calculer $P''(x)$.
2. Démontrer que la courbe de **tout polynôme de degré 3** admet un unique point d'inflexion $I$, dont l'abscisse est $x_I = -\dfrac{b}{3a}$.
3. Démontrer que le point d'inflexion $I$ est le centre de symétrie de la courbe de $P$.

**Exercice 47.21 (Composée de deux fonctions convexes).**
Soient $u : I \to J$ et $g : J \to \mathbb{R}$ deux fonctions deux fois dérivables.
1. Calculer $(g \circ u)''(x)$ en fonction des dérivées premières et secondes de $g$ et de $u$.
2. Démontrer que si $u$ est convexe et si $g$ est **convexe ET croissante**, alors la composée $g \circ u$ est convexe sur $I$.
3. Donner un contre-exemple montrant que si $g$ n'est pas croissante, le résultat peut être faux.

**Exercice 47.22 (Inégalité arithmético-géométrique générale par convexité).**
On admet que la fonction $x \mapsto -\ln(x)$ est strictement convexe sur $]0 \,;\, +\infty[$.
1. Soient $x_1, x_2, \dots, x_n$ des réels strictement positifs. Appliquer l'inégalité de Jensen à la fonction $-\ln(x)$.
2. En utilisant les propriétés du logarithme, en déduire l'inégalité arithmético-géométrique pour $n$ nombres :
   $$\sqrt[n]{x_1 x_2 \dots x_n} \leq \frac{x_1 + x_2 + \dots + x_n}{n}.$$

---

### Solutions

#### Solutions du Niveau ★

- **47.1 :**
  1. $u(x) = 4x - 1 \implies u'(x) = 4$. $f'(x) = 4e^{4x-1}$.
  2. $u(x) = -x^3 \implies u'(x) = -3x^2$. $g'(x) = -3x^2 e^{-x^3}$.
  3. $u(x) = 5x + 2 \implies u'(x) = 5$. $h'(x) = \dfrac{5}{2\sqrt{5x+2}}$.
  4. $u(x) = 3x - 7 \implies u'(x) = 3$. $k'(x) = 5 \times 3 \times (3x - 7)^4 = 15(3x - 7)^4$.

- **47.2 :**
  1. $f'(x) = 8x^3 - 15x^2 + 1 \implies f''(x) = 24x^2 - 30x$.
  2. $g'(x) = 2e^{2x} \implies g''(x) = 4e^{2x}$.
  3. $h'(x) = -\frac{1}{x^2} = -x^{-2} \implies h''(x) = 2x^{-3} = \frac{2}{x^3}$.

- **47.3 :**
  1. $f'(x) = 3x^2 - 12x + 2 \implies f''(x) = 6x - 12 = 6(x - 2)$.
  2. Pour $x \leq 2$, $f''(x) \leq 0$ : $f$ est concave. Pour $x \geq 2$, $f''(x) \geq 0$ : $f$ est convexe.
  3. $f''$ s'annule en changeant de signe en $x = 2$. $f(2) = 8 - 24 + 4 - 1 = -13$. Le point d'inflexion est $I(2 \,;\, -13)$.

- **47.4 :** Comme $f''(x) \geq 0$, $f$ est convexe sur $\mathbb{R}$, donc sa courbe est au-dessus de sa tangente $y = 4x - 1$.
  Pour $x = 3{,}1$, la tangente vaut $4(3{,}1) - 1 = 12{,}4 - 1 = 11{,}4$.
  Comme la courbe est au-dessus de la tangente, on a $f(3{,}1) \geq 11{,}4$.

- **47.5 :** $u(x) = e^x + 1 > 0$, $u'(x) = e^x$. $f'(x) = \dfrac{e^x}{2\sqrt{e^x + 1}}$.

- **47.6 :**
  $f'(x) = 1 \cdot e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}$.
  $f''(x) = (-1)e^{-x} + (1 - x)(-e^{-x}) = (-1 - 1 + x)e^{-x} = (x - 2)e^{-x}$.

- **47.7 :** Pour tout réel $x$, $(x - 3)^2 \geq 0$. Donc $f''(x)$ est du signe de $x + 1$.
  - En $x = 3$, $f''(3) = 0$, mais $f''$ ne change pas de signe autour de 3 : **pas de point d'inflexion en 3 !**
  - En $x = -1$, $f''(-1) = 0$ et $f''$ passe de négatif à positif : **unique point d'inflexion en $x = -1$**.

- **47.8 :** $f'(x) = x^2 - 2x + 5$. La dérivée de $f'$ est $f''(x) = 2x - 2 = 2(x - 1)$.
  $f'$ est strictement décroissante sur $]-\infty \,;\, 1]$ et strictement croissante sur $[1 \,;\, +\infty[$.

---

#### Solutions du Niveau ★★

- **47.9 :**
  1. $f(x) = (x^2 - 2x + 1)e^x = (x-1)^2 e^x$.
     $f'(x) = (2x - 2)e^x + (x^2 - 2x + 1)e^x = (x^2 - 1)e^x$.
  2. Signe de $f'(x)$ : comme $e^x > 0$, du signe de $x^2 - 1 = (x - 1)(x + 1)$.
     Croissante sur $]-\infty ; -1]$, décroissante sur $[-1 ; 1]$, croissante sur $[1 ; +\infty[$.
     En $-\infty$ : $(x^2 - 2x + 1)e^x \to 0$ par croissances comparées.
     En $+\infty$ : $\lim f(x) = +\infty$.
     Maximum local en $-1$ : $f(-1) = 4e^{-1} = 4/e \approx 1{,}47$. Minimum local en $1$ : $f(1) = 0$.
  3. $f''(x) = (2x)e^x + (x^2 - 1)e^x = (x^2 + 2x - 1)e^x$.
  4. Racines de $x^2 + 2x - 1$ : $\Delta = 4 - 4(1)(-1) = 8 = (2\sqrt{2})^2$.
     $x_1 = \frac{-2 - 2\sqrt{2}}{2} = -1 - \sqrt{2} \approx -2{,}41$.
     $x_2 = -1 + \sqrt{2} \approx 0{,}41$.
     $f$ est convexe sur $]-\infty \,;\, -1-\sqrt{2}]$ et sur $[-1+\sqrt{2} \,;\, +\infty[$.
     $f$ est concave sur $[-1-\sqrt{2} \,;\, -1+\sqrt{2}]$.
  5. Les abscisses des points d'inflexion sont $x_1 = -1 - \sqrt{2}$ et $x_2 = -1 + \sqrt{2}$.

- **47.10 :**
  1. $f'(x) = \frac{1}{2\sqrt{x}} = \frac{1}{2} x^{-1/2}$.
     $f''(x) = \frac{1}{2} \left(-\frac{1}{2}\right) x^{-3/2} = -\frac{1}{4x\sqrt{x}}$.
  2. Pour tout $x > 0$, $4x\sqrt{x} > 0$, donc $f''(x) < 0$ : la fonction racine carrée est **strictement concave** sur $]0 \,;\, +\infty[$.
  3. En $x_0 = 1$ : $f(1) = 1$, $f'(1) = 1/2$. Tangente : $y = \frac{1}{2}(x - 1) + 1 = \frac{1}{2}x + \frac{1}{2} = \frac{x+1}{2}$.
  4. La courbe d'une fonction concave est entièrement sous ses tangentes, donc pour tout $x > 0$ : $\sqrt{x} \leq \frac{x+1}{2}$.

- **47.11 :**
  1. $f(x) = (1 + e^{-2x})^{-1}$.
     $f'(x) = -( -2e^{-2x} )(1 + e^{-2x})^{-2} = \frac{2e^{-2x}}{(1 + e^{-2x})^2}$.
  2. On dérive comme un quotient $u/v$ :
     $u' = -4e^{-2x}$, $v' = 2(1 + e^{-2x})(-2e^{-2x}) = -4e^{-2x}(1 + e^{-2x})$.
     $f''(x) = \frac{-4e^{-2x}(1 + e^{-2x})^2 - 2e^{-2x}[-4e^{-2x}(1 + e^{-2x})]}{(1 + e^{-2x})^4} = \frac{-4e^{-2x}(1 + e^{-2x}) + 8e^{-4x}}{(1 + e^{-2x})^3} = \frac{4e^{-2x}(e^{-2x} - 1)}{(1 + e^{-2x})^3}$.
  3. $f''(x) = 0 \iff e^{-2x} - 1 = 0 \iff -2x = 0 \iff x = 0$.
     $f''$ change de signe en 0. Le point d'inflexion est $(0 \,;\, 1/2)$.
     Puisque $f''(0) = 0$, la dérivée première $f'$ admet un extremum en 0 : $f'(0) = \frac{2}{(1+1)^2} = \frac{2}{4} = \frac{1}{2}$. C'est la pente maximale de la rampe.

- **47.12 :**
  1. **Faux.** Contre-exemple : $f(x) = x^4$ en 0 ($f''(0) = 0$ mais $f'' \geq 0$ ne change pas de signe).
  2. **Faux.** Contre-exemple : $f(x) = \sqrt{x}$ est strictement croissante et strictement concave.
  3. **Vrai.** Si $f$ et $g$ sont convexes, $(f + g)'' = f'' + g'' \geq 0$.
  4. **Faux.** Contre-exemple : $f(x) = x$ et $g(x) = x$ sont convexes sur $\mathbb{R}$ (affines), mais leur produit $x^2$ est convexe, alors que pour $f(x) = x$ et $g(x) = -x$ (toutes deux convexes/concaves au sens large), le produit est $-x^2$ qui est concave !

- **47.13 :**
  1. $(\cos u)' = -u' \sin u$. $u(x) = 3x^2 - 2 \implies u' = 6x$. $f'(x) = -6x \sin(3x^2 - 2)$.
  2. $(e^u)' = u' e^u$. $u(x) = \sin x \implies u' = \cos x$. $g'(x) = \cos(x)e^{\sin(x)}$.
  3. $h(x) = v^3$ avec $v(x) = \sin(2x)$. $v'(x) = 2\cos(2x)$.
     $h'(x) = 3 v' v^2 = 3(2\cos(2x))\sin^2(2x) = 6\cos(2x)\sin^2(2x)$.

- **47.14 :**
  1. $f = u^{-1} \implies f' = -u' u^{-2} = -\frac{u'}{u^2}$.
     $f'' = \left(-\frac{u'}{u^2}\right)' = -\frac{u'' u^2 - u'(2uu')}{u^4} = -\frac{u'' u - 2(u')^2}{u^3} = \frac{2(u')^2 - u u''}{u^3}$.
  2. Comme $u$ est concave, $u'' \leq 0$, donc $-u u'' \geq 0$ (car $u > 0$).
     Comme $(u')^2 \geq 0$ et $u^3 > 0$, le numérateur $2(u')^2 - u u'' \geq 0$ et le dénominateur est strictement positif.
     Ainsi $f'' \geq 0$ : la fonction $f$ est convexe sur $I$.

- **47.15 :**
  1. $f''(x) = 2 > 0$ sur $\mathbb{R}$, donc $f$ est convexe.
  2. Le segment joignant $(a ; a^2)$ et $(b ; b^2)$ a pour milieu au niveau des ordonnées $\frac{a^2+b^2}{2}$. L'image du milieu des abscisses est $\left(\frac{a+b}{2}\right)^2$. Par convexité, la courbe est sous la sécante : $\left(\frac{a+b}{2}\right)^2 \leq \frac{a^2+b^2}{2}$.
  3. $\frac{a^2+b^2}{2} - \frac{a^2+2ab+b^2}{4} = \frac{2a^2+2b^2 - a^2 - 2ab - b^2}{4} = \frac{a^2 - 2ab + b^2}{4} = \frac{(a-b)^2}{4} \geq 0$.

- **47.16 :**
  1. $v(t) = x'(t) = -0{,}45 t^2 + 9 t + 30$.
     $v(0) = 30\text{ m/s}$ (soit $108\text{ km/h}$).
     $v(10) = -0{,}45(100) + 90 + 30 = -45 + 120 = 75\text{ m/s}$.
  2. $a(t) = x''(t) = -0{,}9 t + 9$.
  3. L'accélération $a(t)$ décroît linéairement de $+9\text{ m/s}^2$ à $t = 0$ jusqu'à $a(20) = -0{,}9(20) + 9 = -18 + 9 = -9\text{ m/s}^2$. La décélération maximale est atteinte à $t = 20\text{ s}$ avec une intensité de $9\text{ m/s}^2$ (presque 1 g !).

- **47.17 :**
  1. $x^2 - 4x + 3 = 0 \iff (x - 1)(x - 3) = 0$. Les zéros sont $1$ et $3$.
  2. $f'(x) = 3(2x - 4)(x^2 - 4x + 3)^2 = 6(x - 2)(x - 1)^2(x - 3)^2$.
  3. Pour tout $x \in \mathbb{R}$, $(x-1)^2(x-3)^2 \geq 0$. Le signe de $f'(x)$ est donc celui de $x - 2$.
     $f$ est strictement décroissante sur $]-\infty \,;\, 2]$ et strictement croissante sur $[2 \,;\, +\infty[$.
     Minimum en $x = 2$ : $f(2) = (4 - 8 + 3)^3 = (-1)^3 = -1$.
     En $x = 1$ et $x = 3$, $f'(x) = 0$ : tangentes horizontales avec méplats (points d'inflexion horizontaux).

---

#### Solutions du Niveau ★★★

- **47.18 :**
  1. $\lambda x + (1-\lambda)y$ est le barycentre des abscisses de $A(x, f(x))$ et $B(y, f(y))$, et $\lambda f(x) + (1-\lambda)f(y)$ est l'ordonnée correspondante sur le segment $[AB]$. L'inégalité traduit que le point de la courbe est en dessous du point du segment.
  2. Récurrence sur $n$ : vrai pour $n = 2$. Supposons vrai au rang $n$.
     Écrivons $\frac{x_1 + \dots + x_{n+1}}{n+1} = \frac{n}{n+1} \left(\frac{x_1 + \dots + x_n}{n}\right) + \frac{1}{n+1} x_{n+1}$.
     Par convexité à 2 points avec $\lambda = \frac{n}{n+1}$, puis par hypothèse de récurrence, on obtient le résultat pour $n+1$.
  3. Avec $f(x) = x^2$ : $\left(\frac{\sum x_i}{n}\right)^2 \leq \frac{\sum x_i^2}{n} \iff \overline{x}^2 \leq \overline{x^2} \iff V(X) = \overline{x^2} - \overline{x}^2 \geq 0$.

- **47.19 :**
  1. Si $x > a$, pour tout $t \in [a \,;\, x]$, $x - t \geq 0$. Comme $f''(t) \geq 0$, le produit est positif ou nul. Son intégrale de $a$ à $x$ est positive.
     Si $x < a$, $x - t \leq 0$ pour $t \in [x \,;\, a]$. L'intégrale de $a$ à $x$ s'écrit $-\int_x^a (x - t)f''(t) dt = \int_x^a (t - x)f''(t) dt \geq 0$.
  2. Dans les deux cas, $f(x) - [f'(a)(x - a) + f(a)] \geq 0$, ce qui prouve rigoureusement que la courbe reste au-dessus de sa tangente en tout point $a$.

- **47.20 :**
  1. $P'(x) = 3ax^2 + 2bx + c \implies P''(x) = 6ax + 2b$.
  2. $P''(x) = 0 \iff 6ax + 2b = 0 \iff x = -\frac{2b}{6a} = -\frac{b}{3a}$.
     Comme $a \neq 0$, $6ax + 2b$ est une droite de coefficient directeur non nul, elle change impérativement de signe en $x_I = -\frac{b}{3a}$. Tout polynôme cubique a donc un unique point d'inflexion.
  3. En effectuant le changement de variable $X = x - x_I$, le terme en $X^2$ disparaît dans $P(X + x_I)$ : le polynôme devient de la forme $aX^3 + pX + Y_I$, qui vérifie $P(X) - Y_I = -(P(-X) - Y_I)$ : c'est une fonction impaire centrée en $(x_I ; Y_I)$, d'où la symétrie centrale.

- **47.21 :**
  1. $(g \circ u)' = u' \cdot (g' \circ u)$.
     Par la règle du produit :
     $$(g \circ u)'' = u'' \cdot (g' \circ u) + u' \cdot [ (g' \circ u)' ] = u'' \cdot (g' \circ u) + (u')^2 \cdot (g'' \circ u).$$
  2. Comme $u$ est convexe, $u'' \geq 0$. Comme $g$ est croissante, $g' \geq 0$, donc $u'' \cdot (g' \circ u) \geq 0$.
     De plus, $(u')^2 \geq 0$, et comme $g$ est convexe, $g'' \geq 0$, donc $(u')^2 \cdot (g'' \circ u) \geq 0$.
     La somme de deux termes positifs est positive : $(g \circ u)'' \geq 0$, donc $g \circ u$ est convexe.
  3. Contre-exemple si $g$ n'est pas croissante : $u(x) = x^2$ (convexe sur $\mathbb{R}$) et $g(y) = -y$ (convexe au sens large sur $\mathbb{R}$).
     La composée est $(g \circ u)(x) = -x^2$, qui est strictement concave !

- **47.22 :**
  1. Soit $f(x) = -\ln(x)$ sur $]0 \,;\, +\infty[$. $f'(x) = -1/x$, $f''(x) = 1/x^2 > 0$ : $f$ est strictement convexe.
     Par l'inégalité de Jensen :
     $$-\ln\left(\frac{x_1 + \dots + x_n}{n}\right) \leq \frac{-\ln(x_1) - \dots - \ln(x_n)}{n} = -\frac{1}{n} \ln(x_1 \dots x_n) = -\ln\big((x_1 \dots x_n)^{1/n}\big).$$
  2. On multiplie par $-1$ (l'inégalité change de sens) :
     $$\ln\left(\frac{x_1 + \dots + x_n}{n}\right) \geq \ln\left((x_1 \dots x_n)^{1/n}\right).$$
     Par stricte croissance de l'exponentielle :
     $$\frac{x_1 + \dots + x_n}{n} \geq \sqrt[n]{x_1 x_2 \dots x_n}. \quad \blacksquare$$

---

### La question qui ouvre la suite

Nous avons vu que la fonction exponentielle $x \mapsto e^x$ est le roi des fonctions : elle transforme les additions en multiplications, sa dérivée est égale à elle-même, et sa courbe est entièrement convexe au-dessus de sa tangente $y = x + 1$.
Mais que se passe-t-il si un astronome ou un navigateur a besoin de faire le chemin inverse ?
Si l'on connaît la puissance finale et que l'on cherche **l'exposant qui l'a engendrée** ?
Comment une règle à calcul graduée et une table imprimée ont-elles permis aux marins du XVIIᵉ siècle de traverser les océans sans jamais faire une seule multiplication à la main ?

C'est l'épopée de **John Napier** et de la fonction **logarithme népérien**. Rendez-vous au chapitre 48.
