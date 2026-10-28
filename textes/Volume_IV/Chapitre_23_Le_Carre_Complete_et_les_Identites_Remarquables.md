# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 23 : Le Carré Complété et les Identités Remarquables

> *« Ne récite pas une formule d'algèbre comme une incantation magique. Ferme les yeux et regarde le carrelage du sol : coupe un rectangle, déplace un coin, complète le carré manquant. Les lettres ne sont rien d'autre que les côtés de formes qui s'emboîtent sous tes doigts. »*

---

### Ce que tu vas découvrir

- Comment la **double distributivité** s'explique en coupant un rectangle en quatre parcelles de terre : $(a+b)(c+d) = ac + ad + bc + bd$.
- Les **trois identités remarquables**, démontrées sous tes yeux par de purs découpages géométriques de carrés et de rectangles.
- L'art du **calcul mental fulgurant** : calculer $101^2$, $99^2$ ou $48 \times 52$ en deux secondes sans calculatrice.
- La **factorisation** : le chemin du retour, où l'on transforme une somme en produit en dénichant le facteur commun caché ou l'empreinte d'une identité remarquable.
- L'**équation produit nul** : la clé magique pour résoudre des équations du second degré sans paniquer.
- La résolution complète de l'équation $x^2 = a$ selon le signe de $a$, et pourquoi un carré ne peut jamais valoir un nombre négatif.
- L'astuce historique grandiose d'**Al-Khwarizmi** : le « carré complété » qui a fondé l'algèbre mondiale il y a douze siècles.

---

### 1. Le problème : le jardin du calife et le coin manquant

Au printemps de l'an 825, dans les jardins suspendus du palais califal de Bagdad, le maître jardinier fait face à un casse-tête. Le calife désire agrandir son verger carré. 

Le verger actuel est un carré de côté inconnu $x$ mètres. Le calife ordonne :
*« Allongez deux côtés opposés de 5 mètres vers le nord, et allongez les deux autres côtés de 5 mètres vers l'est ! »*

Le jardinier s'exécute sur son plan. Le nouveau jardin a pour côté $(x + 5)$ mètres. Mais le grand intendant du trésor exige de connaître la formule exacte de l'aire totale pour commander les sacs de graines d'herbe :
*« Si le côté initial était $x$, la nouvelle surface est évidemment $x^2 + 5^2 = x^2 + 25$ ! »* affirme le vizir sans réfléchir.

Al-Khwarizmi, présent lors de l'entretien, esquisse un sourire et trace une figure dans le sable fin avec la pointe de sa canne de roseau :

```
             x             5
      ┌──────────────┬───────────┐
      │              │           │
    x │   x × x      │   5 × x   │
      │   = x²       │   = 5x    │
      │              │           │
      ├──────────────┼───────────┤
    5 │   x × 5      │   5 × 5   │
      │   = 5x       │   = 25    │
      └──────────────┴───────────┘
```

*« Regardez bien, noble vizir »*, dit Al-Khwarizmi. *« Votre calcul oublie deux immenses bandes de terrain ! Vous avez bien le vieux carré de $x^2$, et vous avez bien le petit coin carré de $25 \text{ m}^2$. Mais où avez-vous mis la parcelle de $5x$ en haut à droite, et l'autre parcelle de $5x$ en bas à gauche ? »*

L'aire réelle du grand jardin n'est pas $x^2 + 25$, mais :
$$(x + 5)^2 = x^2 + 5x + 5x + 25 = x^2 + 10x + 25.$$

Le vizir avait « oublié » $10x$ mètres carrés de gazon — de quoi laisser une moitié du jardin en friche !

Cette erreur est la plus célèbre de toute l'histoire des mathématiques scolaires. Des millions de collégiens la commettent chaque année en écrivant par inadvertance $(a+b)^2 = a^2 + b^2$. 

Dans ce chapitre, nous allons graver dans ton esprit, par le dessin et par le raisonnement, pourquoi ces deux morceaux du milieu apparaissent toujours, comment jongler entre développement et factorisation, et comment cette géométrie permet de percer les équations du second degré.

---

### 2. La double distributivité : quatre parcelles dans un rectangle

Au chapitre 22, tu as vu la **simple distributivité** : multiplier un nombre par une parenthèse, c'est distribuer le multiplicateur à chaque terme :
$$k(a + b) = ka + kb.$$
C'était l'aire d'un rectangle découpé en deux bandes verticales.

Que se passe-t-il si les deux côtés du rectangle sont eux-mêmes découpés en deux morceaux ?

#### 2.1 La preuve par le rectangle

Traçons un rectangle dont la longueur totale mesure $(a + b)$ et dont la largeur totale mesure $(c + d)$.

```
               a                 b
        ┌───────────────┬────────────────┐
        │               │                │
      c │    a × c      │     b × c      │
        │    = ac       │     = bc       │
        │               │                │
        ├───────────────┼────────────────┤
      d │    a × d      │     b × d      │
        │    = ad       │     = bd       │
        └───────────────┴────────────────┘
```

L'aire totale du grand rectangle peut se calculer de deux façons équivalentes :
1. **D'un seul coup :** Longueur $\times$ largeur, soit $(a + b)(c + d)$.
2. **Morceau par morceau :** On fait la somme des aires des 4 parcelles intérieures :
   $$ac + ad + bc + bd.$$

Puisque les deux calculs mesurent la même surface, ils sont rigoureusement égaux.

> **📐 Propriété fondamentale — La double distributivité.** Pour tous nombres relatifs $a, b, c, d$ :
> $$(a + b)(c + d) = ac + ad + bc + bd.$$
> Chaque terme de la première parenthèse est multiplié par chaque terme de la seconde parenthèse. Cela produit 4 multiplications.

#### 2.2 La règle des flèches et la gestion des signes

Pour ne rien oublier lors d'un calcul écrit, on visualise mentalement quatre flèches :

```
         ┌───── 1 ─────┐
         │   ┌── 2 ────┼───┐
         ▼   ▼         ▼   ▼
       ( a + b )  ×  ( c + d )
             ▲   ▲
             │   └─── 4 ───┘
             └─────── 3 ───┘
```

1. $a \times c = ac$
2. $a \times d = ad$
3. $b \times c = bc$
4. $b \times d = bd$

> **⚠️ Attention, piège ! Le signe appartient au terme qui le suit !**
> Quand une parenthèse contient une soustraction, par exemple $(2x - 3)(x + 4)$, considère que le premier facteur contient les termes $(+2x)$ et $(-3)$.
> On applique alors rigoureusement la règle des signes (Chapitre 20) :
> * $(+2x) \times (+x) = +2x^2$
> * $(+2x) \times (+4) = +8x$
> * $(-3) \times (+x) = -3x$
> * $(-3) \times (+4) = -12$
> Puis on **réduit** en regroupant les termes de même nature :
> $$(2x - 3)(x + 4) = 2x^2 + 8x - 3x - 12 = 2x^2 + 5x - 12.$$

---

### 3. Les trois identités remarquables

Certains produits reviennent si souvent dans les sciences et les calculs qu'on les appelle **remarquables**. Ils méritent d'être mémorisés comme des réflexes absolus. Mais avant de les retenir par cœur, regardons-les vivre sous nos yeux.

#### 3.1 Première identité : le carré d'une somme $(a+b)^2$

Considérons un carré de côté $(a + b)$.

<div align="center">
<svg width="340" height="340" viewBox="0 0 340 340" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="340" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="10"/>
  
  <g transform="translate(45, 45)">
    <!-- Carré a^2 (Bleu Byrne) -->
    <rect x="0" y="0" width="160" height="160" fill="#1d4ed8" fill-opacity="0.85" stroke="#1e3a8a" stroke-width="2"/>
    <text x="80" y="88" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="bold" text-anchor="middle">a²</text>
    
    <!-- Rectangle a x b haut-droite (Jaune/Ambre Byrne) -->
    <rect x="160" y="0" width="80" height="160" fill="#d97706" fill-opacity="0.85" stroke="#b45309" stroke-width="2"/>
    <text x="200" y="88" fill="#ffffff" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">ab</text>
    
    <!-- Rectangle a x b bas-gauche (Jaune/Ambre Byrne) -->
    <rect x="0" y="160" width="160" height="80" fill="#d97706" fill-opacity="0.85" stroke="#b45309" stroke-width="2"/>
    <text x="80" y="208" fill="#ffffff" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">ab</text>
    
    <!-- Petit carré b^2 (Rouge Byrne) -->
    <rect x="160" y="160" width="80" height="80" fill="#b91c1c" fill-opacity="0.85" stroke="#7f1d1d" stroke-width="2"/>
    <text x="200" y="208" fill="#ffffff" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">b²</text>
    
    <!-- Cotes du haut -->
    <text x="80" y="-12" fill="#1d4ed8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">a</text>
    <text x="200" y="-12" fill="#b91c1c" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">b</text>
    
    <!-- Cotes de gauche -->
    <text x="-15" y="88" fill="#1d4ed8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">a</text>
    <text x="-15" y="208" fill="#b91c1c" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">b</text>
  </g>
  <text x="170" y="320" fill="#0f172a" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">(a + b)² = a² (bleu) + 2ab (jaune) + b² (rouge)</text>
</svg>
</div>

```
             a             b
      ┌──────────────┬───────────┐
      │              │           │
    a │      a²      │    ab     │
      │              │           │
      ├──────────────┼───────────┤
    b │      ab      │    b²     │
      └──────────────┴───────────┘
```

L'aire totale est le carré de son côté : $(a + b)^2$.
Cette surface se partage en quatre morceaux naturels :
- un grand carré d'aire $a^2$ ;
- un petit carré d'aire $b^2$ ;
- deux rectangles identiques d'aire $a \times b = ab$.

En additionnant ces morceaux, on trouve :
$$(a + b)^2 = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2.$$

Le terme $2ab$ s'appelle le **double produit**.

> **📐 Première identité remarquable — Carré d'une somme.** Pour tous nombres relatifs $a$ et $b$ :
> $$(a + b)^2 = a^2 + 2ab + b^2.$$
> *En français :* « Le carré d'une somme est égal au carré du premier, plus le double produit, plus le carré du second. »

#### 3.2 Deuxième identité : le carré d'une différence $(a-b)^2$

Imaginons maintenant un grand carré de côté $a$, d'aire totale $a^2$. Nous voulons isoler un carré plus petit, situé dans le coin supérieur gauche, de côté $(a - b)$. Son aire est $(a - b)^2$.

```
               a - b            b
        ┌──────────────────┬─────────┐
        │                  │/////////│
  a - b │    (a - b)²      │/////////│
        │    CHERCHÉ       │/////////│
        ├──────────────────┼─────────┤
      b │//////////////////│xxxxxxxxx│
        │//////////////////│xxxxxxxxx│
        └──────────────────┴─────────┘
```

Comment obtenir l'aire de ce carré blanc $(a-b)^2$ à partir du grand carré $a^2$ ?
1. On retire la bande horizontale du bas, de longueur $a$ et de largeur $b$ : son aire est $a \times b = ab$.
2. On retire la bande verticale de droite, de longueur $a$ et de largeur $b$ : son aire est $a \times b = ab$.
3. **Mais attention !** Le petit carré du coin inférieur droit (marqué de `xxxx`), de côté $b$ et d'aire $b^2$, faisait partie à la fois de la bande horizontale et de la bande verticale ! En retirant les deux bandes, nous l'avons retiré **deux fois**.
4. Pour rétablir l'équilibre exact, il faut donc **rajouter une fois** ce petit coin $b^2$.

L'aire restante est donc :
$$(a - b)^2 = a^2 - ab - ab + b^2 = a^2 - 2ab + b^2.$$

Algébriquement, on retrouve ce résultat en appliquant la double distributivité à $(a - b)(a - b)$ :
$$(a - b)(a - b) = a \times a - a \times b - b \times a + (-b) \times (-b) = a^2 - 2ab + b^2.$$

> **📐 Deuxième identité remarquable — Carré d'une différence.** Pour tous nombres relatifs $a$ et $b$ :
> $$(a - b)^2 = a^2 - 2ab + b^2.$$
> *En français :* « Le carré d'une différence est égal au carré du premier, moins le double produit, plus le carré du second. »

> **⚠️ Attention, piège !** Dans $(a - b)^2 = a^2 - 2ab + b^2$, le dernier terme est **toujours précédé d'un signe $+$** ! En effet, $(-b) \times (-b) = +b^2$. Seul le double produit porte le signe $-$.

#### 3.3 Troisième identité : le produit de la somme par la différence $(a+b)(a-b)$

Partons d'un carré de côté $a$ (aire $a^2$) auquel on enlève un petit carré de côté $b$ situé dans un coin (aire $b^2$).
La surface qui reste a pour aire $a^2 - b^2$. C'est une forme en « L ».

```
           a - b            b
      ┌──────────────┬───────────┐
      │              │           │
a - b │      I       │    II     │
      │              │           │
      ├──────────────┴───────────┤
    b │           III            │  (Découpé !)
      └──────────────────────────┘
```

Découpons cette forme en deux morceaux le long du prolongement d'un côté :
- Le rectangle I de dimensions $(a - b) \times a$.
- Le rectangle restant qu'on peut déplacer et recoller.

Mieux encore : découpons la forme en L et réarrangeons-la en un seul grand rectangle de longueur $(a + b)$ et de largeur $(a - b)$ :

```
          ┌───────────────────────────┬─────────────┐
    a - b │             a             │      b      │
          └───────────────────────────┴─────────────┘
          <───────────────── a + b ─────────────────>
```

L'aire de ce nouveau rectangle est Longueur $\times$ Largeur $= (a + b)(a - b)$.
Puisque ce rectangle provient du grand carré $a^2$ privé du petit carré $b^2$, les deux aires sont strictement égales !

Algébriquement, par double distributivité :
$$(a + b)(a - b) = a \times a - a \times b + b \times a - b \times b = a^2 - ab + ba - b^2.$$
Les deux termes du milieu s'annulent car $-ab + ba = 0$. Il reste :
$$(a + b)(a - b) = a^2 - b^2.$$

> **📐 Troisième identité remarquable — Produit d'une somme par une différence.** Pour tous nombres relatifs $a$ et $b$ :
> $$(a + b)(a - b) = a^2 - b^2.$$
> On l'appelle souvent la **différence de deux carrés**.

#### 3.4 Tableau récapitulatif des identités remarquables

| Forme factorisée (produit) | | Forme développée (somme) | Nom |
|---|---|---|---|
| $(a + b)^2$ | $\Longleftrightarrow$ | $a^2 + 2ab + b^2$ | Carré d'une somme |
| $(a - b)^2$ | $\Longleftrightarrow$ | $a^2 - 2ab + b^2$ | Carré d'une différence |
| $(a + b)(a - b)$ | $\Longleftrightarrow$ | $a^2 - b^2$ | Différence de deux carrés |

- Aller de gauche à droite ($\longrightarrow$) : c'est **développer** (écrire sous forme de somme).
- Aller de droite à gauche ($\longleftarrow$) : c'est **factoriser** (écrire sous forme de produit).

#### 3.5 Calcul mental éclair grâce aux identités

Les identités remarquables ne servent pas seulement à manipuler des lettres : elles permettent de réaliser des calculs arithmétiques impressionnants sans brouillon ni calculatrice !

- **Calculer $101^2$ :**
  $$101^2 = (100 + 1)^2 = 100^2 + 2 \times 100 \times 1 + 1^2 = 10\,000 + 200 + 1 = 10\,201.$$
- **Calculer $99^2$ :**
  $$99^2 = (100 - 1)^2 = 100^2 - 2 \times 100 \times 1 + 1^2 = 10\,000 - 200 + 1 = 9\,801.$$
- **Calculer $52 \times 48$ :**
  Remarque que $52 = 50 + 2$ et $48 = 50 - 2$ !
  $$52 \times 48 = (50 + 2)(50 - 2) = 50^2 - 2^2 = 2\,500 - 4 = 2\,496.$$
- **Calculer $105 \times 95$ :**
  $$105 \times 95 = (100 + 5)(100 - 5) = 100^2 - 5^2 = 10\,000 - 25 = 9\,975.$$

> **💡 Le savais-tu ?** Dans l'Antiquité, les Babyloniens n'avaient pas de tables de multiplication pour tous les nombres. Ils disposaient en revanche de tables gravées de carrés ($1^2, 2^2, 3^2, \dots$). Pour multiplier deux nombres quelconques $x$ et $y$, ils utilisaient la formule :
> $$x \times y = \frac{(x + y)^2 - (x - y)^2}{4}.$$
> En calculant la somme, la différence, et en consultant leur table de carrés, ils trouvaient le produit instantanément !

---

### 4. La factorisation : retrouver les briques élémentaires

Développer est mécanique : il suffit de distribuer les flèches sans se tromper de signe. **Factoriser**, c'est l'inverse : c'est un travail d'enquêteur. On dispose d'une somme de termes éparpillés, et l'on cherche comment elle a été fabriquée à partir d'un produit.

Pourquoi vouloir à tout prix factoriser ? Parce qu'un produit est infiniment plus facile à étudier qu'une somme :
- Un produit permet de simplifier des fractions algébriques.
- Un produit permet de résoudre des équations complexes grâce à la règle du produit nul.

Il existe deux grandes techniques de factorisation au collège.

#### 4.1 Première technique : la recherche d'un facteur commun

On cherche un nombre, une lettre ou un bloc entre parenthèses qui multiplie **chacun** des termes de la somme.

**Cas 1 : Un facteur commun évident (nombre ou lettre seule)**
- Dans $6x + 15$ : on remarque que $6 = 3 \times 2$ et $15 = 3 \times 5$. Le facteur commun est $3$.
  $$6x + 15 = 3 \times 2x + 3 \times 5 = 3(2x + 5).$$
- Dans $x^2 - 7x$ : on remarque que $x^2 = x \times x$ et $7x = 7 \times x$. Le facteur commun est $x$.
  $$x^2 - 7x = x \times x - x \times 7 = x(x - 7).$$

**Cas 2 : Une parenthèse entière comme facteur commun**
Considérons l'expression :
$$A = (3x + 2)(x - 5) + (3x + 2)(2x + 1).$$
L'expression est une somme de deux grands termes. Le bloc $(3x + 2)$ est présent dans les deux termes : c'est notre **facteur commun**.

On le souligne, on l'écrit une seule fois au début, et on ouvre un grand crochet pour ramasser tout ce qui reste :
$$A = \underline{(3x + 2)}(x - 5) + \underline{(3x + 2)}(2x + 1)$$
$$A = \underline{(3x + 2)} \left[ (x - 5) + (2x + 1) \right]$$
$$A = (3x + 2) [ x - 5 + 2x + 1 ]$$
$$A = (3x + 2)(3x - 4).$$

> **⚠️ Attention, piège ! Quand le facteur commun est « tout seul » !**
> Soit l'expression $B = (2x + 1)^2 - (2x + 1)$.
> Rappelle-toi que $(2x + 1)^2 = (2x + 1)(2x + 1)$ et que $(2x + 1) = (2x + 1) \times 1$.
> Quand on factorise par $(2x + 1)$, le second terme ne disparaît pas dans le néant, il laisse derrière lui le nombre $1$ :
> $$B = \underline{(2x + 1)}(2x + 1) - \underline{(2x + 1)} \times 1 = \underline{(2x + 1)} \left[ (2x + 1) - 1 \right] = (2x + 1)(2x) = 2x(2x + 1).$$
> Écrire $B = (2x+1)(2x+1) = (2x+1)^2$ est une erreur dramatique !

#### 4.2 Deuxième technique : reconnaître une identité remarquable

Quand il n'y a aucun facteur commun visible dans tous les termes, on regarde la forme globale de l'expression :

1. **Trois termes, deux carrés positifs et un signe $+$ au milieu :**
   $$x^2 + 6x + 9 = x^2 + 2 \times x \times 3 + 3^2 = (x + 3)^2.$$
2. **Trois termes, deux carrés positifs et un signe $-$ au milieu :**
   $$4x^2 - 20x + 25 = (2x)^2 - 2 \times (2x) \times 5 + 5^2 = (2x - 5)^2.$$
3. **Deux termes seulement, séparés par un signe $-$ : c'est la différence de deux carrés !**
   $$x^2 - 49 = x^2 - 7^2 = (x + 7)(x - 7).$$
   $$9x^2 - 16 = (3x)^2 - 4^2 = (3x + 4)(3x - 4).$$

---

### 5. L'équation produit nul : la clé des degrés supérieurs

Au chapitre 22, nous savions résoudre les équations du premier degré, comme $3x + 5 = 14$. 
Mais comment résoudre une équation contenant du $x^2$, comme :
$$(2x - 6)(3x + 9) = 0 \quad \text{ou} \quad x^2 - 25 = 0 \text{ ?}$$

#### 5.1 La propriété fondamentale du zéro

Pose-toi cette question d'une simplicité enfantine :
*Si je multiplie deux nombres secrets $A$ et $B$, et que le résultat est égal à zéro ($A \times B = 0$), que peux-tu affirmer avec une certitude absolue ?*

Si tu choisis $A = 4$, pour que le produit fasse $0$, $B$ doit **obligatoirement** valoir $0$.
Si aucun des deux nombres ne vaut zéro (par exemple $2 \times 3 = 6$ ou $(-5) \times 0{,}1 = -0{,}5$), leur produit ne pourra **jamais** donner zéro !

> **📐 Théorème — Propriété du produit nul.** 
> Un produit de facteurs est nul **si et seulement si** l'un au moins de ses facteurs est nul :
> $$A \times B = 0 \quad \Longleftrightarrow \quad A = 0 \quad \text{ou} \quad B = 0.$$

Ce théorème est prodigieux : il permet de casser une équation compliquée de degré 2 en **deux petites équations toutes simples de degré 1** !

#### 5.2 Méthode de rédaction pas à pas

> **🧭 Méthode — Résoudre une équation produit nul.**
> Résolvons l'équation $(3x - 12)(2x + 8) = 0$.
> 
> 1. **Phrase rituelle :** « Un produit de facteurs est nul si et seulement si au moins l'un de ses facteurs est nul. »
> 2. **Séparation en deux branches :**
>    $$3x - 12 = 0 \quad \text{ou} \quad 2x + 8 = 0$$
> 3. **Résolution de chaque branche :**
>    - Première branche : $3x = 12 \implies x = \frac{12}{3} = 4$.
>    - Deuxième branche : $2x = -8 \implies x = \frac{-8}{2} = -4$.
> 4. **Conclusion :** L'équation admet deux solutions : $-4$ et $4$. On note l'ensemble des solutions $S = \{-4 \; ; \; 4\}$.

> **⚠️ Attention, piège ! Ne jamais diviser par $x$ !**
> Face à une équation comme $x^2 = 5x$, un réflexe tentant mais faux consiste à diviser les deux côtés par $x$ pour trouver $x = 5$.
> Ce faisant, **tu tues la solution $x = 0$** ! (Car on n'a pas le droit de diviser par zéro).
> **La bonne méthode :** on regroupe tout à gauche pour faire apparaître un zéro à droite, puis on factorise :
> $$x^2 - 5x = 0 \iff x(x - 5) = 0 \iff x = 0 \quad \text{ou} \quad x - 5 = 0 \iff x = 0 \quad \text{ou} \quad x = 5.$$
> Il y a bien deux solutions : $0$ et $5$.

---

### 6. Les équations du type $x^2 = a$

L'équation $x^2 = a$ est la plus pure des équations du second degré : quel nombre, multiplié par lui-même, donne $a$ ?

La réponse dépend entièrement du **signe de $a$**.

#### 6.1 Les trois cas possibles

1. **Si $a > 0$ (le nombre $a$ est strictement positif) :**
   Il existe **deux solutions opposées** : $\sqrt{a}$ et $-\sqrt{a}$.
   *Preuve rigoureuse par factorisation :*
   $$x^2 = a \iff x^2 - a = 0.$$
   Puisque $a > 0$, on peut écrire $a = (\sqrt{a})^2$.
   L'équation devient :
   $$x^2 - (\sqrt{a})^2 = 0.$$
   C'est la troisième identité remarquable $A^2 - B^2 = (A-B)(A+B)$ !
   $$(x - \sqrt{a})(x + \sqrt{a}) = 0.$$
   D'après la propriété du produit nul :
   $$x - \sqrt{a} = 0 \implies x = \sqrt{a} \quad \text{ou} \quad x + \sqrt{a} = 0 \implies x = -\sqrt{a}.$$
   *Exemple :* L'équation $x^2 = 9$ a pour solutions $\sqrt{9} = 3$ et $-\sqrt{9} = -3$.
   En effet, $3 \times 3 = 9$ et $(-3) \times (-3) = 9$.

2. **Si $a = 0$ :**
   L'équation $x^2 = 0$ a **une seule solution unique** : $x = 0$.

3. **Si $a < 0$ (le nombre $a$ est strictement négatif) :**
   L'équation $x^2 = a$ n'admet **aucune solution** (dans l'ensemble des nombres réels).
   *Pourquoi ?* Le carré de n'importe quel nombre réel est toujours positif ou nul :
   $(+5)^2 = +25$ et $(-5)^2 = +25$. Il est impossible qu'un nombre au carré donne un résultat négatif comme $-16$.
   *Exemple :* $x^2 = -4$ n'a aucune solution réelle. On écrit $S = \emptyset$ (ensemble vide).

```
                            Équation : x² = a
                                    │
           ┌────────────────────────┼────────────────────────┐
           ▼                        ▼                        ▼
         a > 0                    a = 0                    a < 0
    Deux solutions :         Une solution :          Aucune solution :
   x = √a  ou  x = -√a           x = 0                 Impossible !
```

---

### 7. L'histoire vraie : le chef-d'œuvre d'Al-Khwarizmi et le « carré complété »

Comment Al-Khwarizmi résolvait-il en l'an 820 une équation où se mêlent des carrés et des $x$, par exemple :
$$x^2 + 10x = 39 \text{ ?}$$

À cette époque, les formules avec $\Delta = b^2 - 4ac$ n'existaient pas encore. Al-Khwarizmi a inventé une méthode purement visuelle appelée le **carré complété** (*al-jabr wa'l-muqabala*).

1. Il dessine un carré de côté $x$, d'aire $x^2$.
2. Il doit lui ajouter $10x$. Il prend deux rectangles de côtés $x$ et $5$ (dont l'aire cumulée est $5x + 5x = 10x$) et les colle contre deux côtés du carré central :

```
             x             5
      ┌──────────────┬───────────┐
      │              │           │
    x │      x²      │    5x     │
      │              │           │
      ├──────────────┼ - - - - - ┤
    5 │      5x      │  MANQUE   │
      └──────────────┴ - - - - - ┘
```

La surface de cette forme en L vaut $x^2 + 5x + 5x = x^2 + 10x$. Or, nous savons que cette aire doit être égale à $39$.

3. Al-Khwarizmi remarque : *« Cette forme ressemble presque à un grand carré de côté $(x + 5)$ ! Il lui manque seulement le petit coin en bas à droite. »*
4. Quelle est l'aire de ce petit coin manquant ?
   C'est un carré de $5 \times 5 = 25$ !
5. Al-Khwarizmi décide donc de **compléter le carré** en ajoutant $25$ des deux côtés de la balance :
   $$(x^2 + 10x) + 25 = 39 + 25.$$
   La figure devient un grand carré parfait de côté $(x+5)$ :
   $$(x + 5)^2 = 64.$$
6. Il ne reste plus qu'à prendre la racine carrée :
   $$x + 5 = \sqrt{64} = 8.$$
7. En retranchant 5 :
   $$x = 8 - 5 = 3.$$

Vérifions : pour $x = 3$, on a $3^2 + 10 \times 3 = 9 + 30 = 39$. C'est parfaitement juste !
Toutes les formules du second degré que tu apprendras au lycée (au Chapitre 35) découlent de ce geste géométrique d'Al-Khwarizmi consistant à ajouter le coin manquant.

---

### 8. Exemples résolus pas à pas

#### Exemple 1 : Développer et réduire avec double distributivité et parenthèses négatives
Développer et réduire l'expression :
$$C = (3x - 2)(4x + 5) - (2x - 1)(x - 3).$$

**Résolution détaillée :**
Attention au signe « $-$ » entre les deux produits ! Pour ne pas faire d'erreur de signe, on conserve le deuxième développement à l'intérieur de grands crochets :

1. Premier produit :
   $$(3x - 2)(4x + 5) = 3x \times 4x + 3x \times 5 - 2 \times 4x - 2 \times 5 = 12x^2 + 15x - 8x - 10 = 12x^2 + 7x - 10.$$
2. Deuxième produit (dans les crochets) :
   $$(2x - 1)(x - 3) = 2x \times x + 2x \times (-3) - 1 \times x - 1 \times (-3) = 2x^2 - 6x - x + 3 = 2x^2 - 7x + 3.$$
3. On rassemble :
   $$C = (12x^2 + 7x - 10) - [2x^2 - 7x + 3].$$
4. On retire les crochets en inversant tous les signes intérieurs :
   $$C = 12x^2 + 7x - 10 - 2x^2 + 7x - 3.$$
5. On regroupe les termes semblables :
   $$C = (12x^2 - 2x^2) + (7x + 7x) + (-10 - 3) = 10x^2 + 14x - 13.$$

---

#### Exemple 2 : Développer avec les identités remarquables
Développer les expressions suivantes :
1. $D = (3x + 4)^2$
2. $E = (5x - 2)^2$
3. $F = (7x + 3)(7x - 3)$

**Résolution détaillée :**
1. $D$ est de la forme $(a + b)^2$ avec $a = 3x$ et $b = 4$ :
   $$D = (3x)^2 + 2 \times (3x) \times 4 + 4^2 = 9x^2 + 24x + 16.$$
   *(Piège évité : $(3x)^2 = 9x^2$ et non $3x^2$ !)*
2. $E$ est de la forme $(a - b)^2$ avec $a = 5x$ et $b = 2$ :
   $$E = (5x)^2 - 2 \times (5x) \times 2 + 2^2 = 25x^2 - 20x + 4.$$
3. $F$ est de la forme $(a + b)(a - b)$ avec $a = 7x$ et $b = 3$ :
   $$F = (7x)^2 - 3^2 = 49x^2 - 9.$$

---

#### Exemple 3 : Factoriser avec un facteur commun parenthèse
Factoriser l'expression :
$$G = (2x - 5)(x + 4) - (2x - 5)(3x - 1).$$

**Résolution détaillée :**
1. On repère le facteur commun présent dans les deux blocs : c'est $(2x - 5)$.
2. On le place en facteur commun devant de grands crochets :
   $$G = \underline{(2x - 5)} \left[ (x + 4) - (3x - 1) \right].$$
3. On simplifie à l'intérieur des crochets en faisant très attention au signe « $-$ » devant la seconde parenthèse :
   $$G = (2x - 5) [ x + 4 - 3x + 1 ].$$
4. On réduit :
   $$G = (2x - 5)(-2x + 5).$$

---

#### Exemple 4 : Factoriser une différence de deux carrés complexes
Factoriser l'expression :
$$H = (2x + 3)^2 - 36.$$

**Résolution détaillée :**
1. On remarque que $36 = 6^2$.
2. L'expression est donc de la forme $A^2 - B^2$ avec $A = (2x + 3)$ et $B = 6$.
3. On applique la formule $A^2 - B^2 = (A + B)(A - B)$ :
   $$H = \left[ (2x + 3) + 6 \right] \times \left[ (2x + 3) - 6 \right].$$
4. On réduit l'intérieur de chaque parenthèse :
   $$H = (2x + 9)(2x - 3).$$

---

#### Exemple 5 : Résoudre une équation complexe se ramenant à un produit nul
Résoudre dans les nombres réels l'équation :
$$(3x + 1)^2 = (x - 4)^2.$$

**Résolution détaillée :**
*Tentative interdite :* Prendre la racine carrée directement des deux côtés sans précaution, ou tout développer (ce qui donnerait une équation en $x^2$ qu'on ne saurait pas résoudre facilement).
*La bonne méthode :* Mettre tout à gauche pour faire apparaître « $= 0$ » et factoriser comme une différence de deux carrés :
$$(3x + 1)^2 - (x - 4)^2 = 0.$$
C'est de la forme $A^2 - B^2 = 0$ avec $A = (3x + 1)$ et $B = (x - 4)$.
$$[(3x + 1) + (x - 4)] \times [(3x + 1) - (x - 4)] = 0$$
$$[3x + 1 + x - 4] \times [3x + 1 - x + 4] = 0$$
$$(4x - 3)(2x + 5) = 0.$$

C'est une **équation produit nul** !
Un produit de facteurs est nul si et seulement si au moins l'un de ses facteurs est nul :
$$4x - 3 = 0 \quad \text{ou} \quad 2x + 5 = 0$$
$$4x = 3 \implies x = \frac{3}{4} = 0{,}75$$
$$2x = -5 \implies x = -\frac{5}{2} = -2{,}5.$$
Conclusion : L'équation possède deux solutions : $S = \left\{ -\frac{5}{2} \; ; \; \frac{3}{4} \right\}$.

---

### Ce qu'il faut retenir

1. **Double distributivité :**
   $$(a + b)(c + d) = ac + ad + bc + bd.$$
2. **Les 3 Identités remarquables (à connaître dans les deux sens) :**
   - Carré d'une somme : $(a + b)^2 = a^2 + 2ab + b^2$
   - Carré d'une différence : $(a - b)^2 = a^2 - 2ab + b^2$
   - Différence de deux carrés : $(a + b)(a - b) = a^2 - b^2$
3. **Erreurs fatales à bannir :**
   - $(a + b)^2 \neq a^2 + b^2$ (il manque le double produit $2ab$ !)
   - $(3x)^2 = 9x^2 \neq 3x^2$ (le carré porte aussi sur le 3)
4. **Factorisation :**
   - Chercher d'abord un facteur commun (nombre, $x$ ou parenthèse).
   - Si aucun facteur commun n'existe, identifier une identité remarquable ($a^2-b^2$, $a^2+2ab+b^2$ ou $a^2-2ab+b^2$).
5. **Équation produit nul :**
   $$A \times B = 0 \iff A = 0 \quad \text{ou} \quad B = 0.$$
6. **Équations du type $x^2 = a$ :**
   - Si $a > 0$ : deux solutions $x = \sqrt{a}$ et $x = -\sqrt{a}$.
   - Si $a = 0$ : une solution $x = 0$.
   - Si $a < 0$ : aucune solution.

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 23.1** Développer et réduire les expressions suivantes :
1. $A = (x + 3)(x + 7)$
2. $B = (2x + 1)(x - 4)$
3. $C = (x - 5)(3x - 2)$

**Exercice 23.2** Utiliser les identités remarquables pour développer :
1. $D = (x + 6)^2$
2. $E = (x - 5)^2$
3. $F = (x + 8)(x - 8)$
4. $G = (2x + 3)^2$
5. $H = (4x - 1)^2$
6. $I = (5x + 2)(5x - 2)$

**Exercice 23.3** Calculer astucieusement sans calculatrice en utilisant une identité remarquable :
1. $102^2$
2. $49^2$
3. $61 \times 59$
4. $1003 \times 997$

**Exercice 23.4** Factoriser en trouvant un facteur commun évident :
1. $J = 5x + 35$
2. $K = x^2 + 8x$
3. $L = 7x^2 - 14x$

**Exercice 23.5** Factoriser en utilisant les identités remarquables :
1. $M = x^2 - 81$
2. $N = x^2 + 10x + 25$
3. $P = x^2 - 12x + 36$
4. $Q = 4x^2 - 9$

**Exercice 23.6** Résoudre les équations produit nul suivantes :
1. $(x - 7)(x + 2) = 0$
2. $(2x - 10)(3x + 15) = 0$
3. $x(4x - 9) = 0$

**Exercice 23.7** Résoudre les équations $x^2 = a$ :
1. $x^2 = 49$
2. $x^2 = 17$
3. $x^2 = -9$
4. $x^2 = 0$

---

#### Niveau ★★ : Réflexion et enchaînements

**Exercice 23.8** Développer et réduire les expressions complexes :
1. $R = (3x - 2)^2 - (x + 4)(x - 4)$
2. $S = (2x + 1)^2 - (3x - 2)^2$

**Exercice 23.9** Factoriser en identifiant un bloc commun :
1. $T = (x - 3)(2x + 5) + (x - 3)(x - 1)$
2. $U = (3x + 2)(5x - 1) - (3x + 2)(2x + 7)$
3. $V = (4x - 3)^2 + (4x - 3)(x + 2)$

**Exercice 23.10** Factoriser les différences de carrés composées :
1. $W = (x + 2)^2 - 25$
2. $Z = 49 - (2x - 1)^2$
3. $Y = (3x - 5)^2 - (x + 1)^2$

**Exercice 23.11** Résoudre les équations en se ramenant à une équation produit nul :
1. $x^2 - 36 = 0$
2. $(2x + 3)(x - 1) = (2x + 3)(3x - 7)$
3. $9x^2 - 25 = 0$
4. $x^2 = 6x$

**Exercice 23.12** Programme de calcul et mystère :
On considère le programme de calcul suivant :
- Choisir un nombre entier.
- Lui ajouter 1.
- Élever le résultat au carré.
- Retrancher au résultat le carré du nombre de départ.
- Retrancher 1.
1. Tester ce programme avec 3, 5 et 10. Que remarque-t-on ?
2. Démontrer cette conjecture pour n'importe quel nombre choisi au départ en utilisant le calcul littéral.

**Exercice 23.13** L'astuce du tour de magie des carrés terminés par 5 :
Pour calculer de tête le carré d'un nombre se terminant par 5 (comme $35^2$), l'astuce consiste à multiplier le chiffre des dizaines ($3$) par le nombre suivant ($4$), ce qui fait $3 \times 4 = 12$, puis à coller $25$ au bout : on obtient $1225$ !
Un nombre se terminant par 5 s'écrit $10d + 5$, où $d$ est le nombre de dizaines.
Développer $(10d + 5)^2$ et démontrer pourquoi cette astuce fonctionne à tous les coups !

---

#### Niveau ★★★ : Défis et recherche

**Exercice 23.14** Résolution à la manière d'Al-Khwarizmi (carré complété) :
Résoudre l'équation $x^2 + 6x = 16$ en suivant pas à pas la méthode géométrique d'Al-Khwarizmi :
1. Écrire $x^2 + 6x$ sous la forme $(x + \dots)^2 - \dots$
2. En déduire une équation du type $(x + 3)^2 = \text{nombre}$.
3. Trouver la valeur positive de $x$.

**Exercice 23.15** Le grand défi de Pythagore et de l'algèbre :
Un triangle rectangle possède une hypoténuse qui mesure $(x + 8)$ cm. Ses deux côtés de l'angle droit mesurent respectivement $x$ cm et $(x + 7)$ cm.
1. En appliquant le théorème de Pythagore, écrire une équation vérifiée par $x$.
2. Développer et réduire cette équation pour la ramener sous la forme $x^2 - 2x - 15 = 0$.
3. Vérifier que $x^2 - 2x - 15 = (x - 5)(x + 3)$.
4. En déduire la valeur de $x$ et les longueurs des trois côtés du triangle.

**Exercice 23.16** La différence de deux cubes (pour les curieux) :
1. Développer l'expression $(a - b)(a^2 + ab + b^2)$.
2. Que remarque-t-on ?
3. En déduire une factorisation de $x^3 - 8$ (sachant que $8 = 2^3$).

---

### Solutions

#### Niveau ★

**Solution 23.1**
1. $A = x^2 + 7x + 3x + 21 = x^2 + 10x + 21$.
2. $B = 2x^2 - 8x + x - 4 = 2x^2 - 7x - 4$.
3. $C = 3x^2 - 2x - 15x + 10 = 3x^2 - 17x + 10$.

**Solution 23.2**
1. $D = x^2 + 2 \times x \times 6 + 6^2 = x^2 + 12x + 36$.
2. $E = x^2 - 2 \times x \times 5 + 5^2 = x^2 - 10x + 25$.
3. $F = x^2 - 8^2 = x^2 - 64$.
4. $G = (2x)^2 + 2 \times 2x \times 3 + 3^2 = 4x^2 + 12x + 9$.
5. $H = (4x)^2 - 2 \times 4x \times 1 + 1^2 = 16x^2 - 8x + 1$.
6. $I = (5x)^2 - 2^2 = 25x^2 - 4$.

**Solution 23.3**
1. $102^2 = (100 + 2)^2 = 100^2 + 2 \times 100 \times 2 + 2^2 = 10\,000 + 400 + 4 = 10\,404$.
2. $49^2 = (50 - 1)^2 = 50^2 - 2 \times 50 \times 1 + 1^2 = 2\,500 - 100 + 1 = 2\,401$.
3. $61 \times 59 = (60 + 1)(60 - 1) = 60^2 - 1^2 = 3\,600 - 1 = 3\,599$.
4. $1003 \times 997 = (1000 + 3)(1000 - 3) = 1000^2 - 3^2 = 1\,000\,000 - 9 = 999\,991$.

**Solution 23.4**
1. $J = 5(x + 7)$.
2. $K = x(x + 8)$.
3. $L = 7x(x - 2)$.

**Solution 23.5**
1. $M = x^2 - 9^2 = (x + 9)(x - 9)$.
2. $N = x^2 + 2 \times x \times 5 + 5^2 = (x + 5)^2$.
3. $P = x^2 - 2 \times x \times 6 + 6^2 = (x - 6)^2$.
4. $Q = (2x)^2 - 3^2 = (2x + 3)(2x - 3)$.

**Solution 23.6**
1. $x - 7 = 0$ ou $x + 2 = 0 \implies x = 7$ ou $x = -2$. $S = \{-2 \; ; \; 7\}$.
2. $2x - 10 = 0 \implies 2x = 10 \implies x = 5$ ou $3x + 15 = 0 \implies 3x = -15 \implies x = -5$. $S = \{-5 \; ; \; 5\}$.
3. $x = 0$ ou $4x - 9 = 0 \implies 4x = 9 \implies x = \frac{9}{4} = 2{,}25$. $S = \{0 \; ; \; 2{,}25\}$.

**Solution 23.7**
1. $x = \sqrt{49} = 7$ ou $x = -\sqrt{49} = -7$. $S = \{-7 \; ; \; 7\}$.
2. $x = \sqrt{17}$ ou $x = -\sqrt{17}$. $S = \{-\sqrt{17} \; ; \; \sqrt{17}\}$.
3. Aucun carré de réel n'est négatif. Aucune solution : $S = \emptyset$.
4. $x = 0$. Une seule solution : $S = \{0\}$.

---

#### Niveau ★★

**Solution 23.8**
1. $R = (9x^2 - 12x + 4) - (x^2 - 16) = 9x^2 - 12x + 4 - x^2 + 16 = 8x^2 - 12x + 20$.
2. $S = (4x^2 + 4x + 1) - (9x^2 - 12x + 4) = 4x^2 + 4x + 1 - 9x^2 + 12x - 4 = -5x^2 + 16x - 3$.

**Solution 23.9**
1. $T = (x - 3)[(2x + 5) + (x - 1)] = (x - 3)(3x + 4)$.
2. $U = (3x + 2)[(5x - 1) - (2x + 7)] = (3x + 2)[5x - 1 - 2x - 7] = (3x + 2)(3x - 8)$.
3. $V = (4x - 3)[(4x - 3) + (x + 2)] = (4x - 3)(5x - 1)$.

**Solution 23.10**
1. $W = (x + 2)^2 - 5^2 = [(x + 2) + 5][(x + 2) - 5] = (x + 7)(x - 3)$.
2. $Z = 7^2 - (2x - 1)^2 = [7 + (2x - 1)][7 - (2x - 1)] = [7 + 2x - 1][7 - 2x + 1] = (2x + 6)(-2x + 8)$. (On peut aussi factoriser par 2 dans chaque facteur : $Z = 4(x + 3)(-x + 4)$).
3. $Y = [(3x - 5) + (x + 1)][(3x - 5) - (x + 1)] = [4x - 4][2x - 6] = 4(x - 1) \times 2(x - 3) = 8(x - 1)(x - 3)$.

**Solution 23.11**
1. $x^2 - 36 = 0 \iff (x - 6)(x + 6) = 0 \iff x = 6$ ou $x = -6$. $S = \{-6 \; ; \; 6\}$.
2. On regroupe tout à gauche : $(2x + 3)(x - 1) - (2x + 3)(3x - 7) = 0$.
   Facteur commun $(2x + 3)$ : $(2x + 3)[(x - 1) - (3x - 7)] = 0 \iff (2x + 3)(-2x + 6) = 0$.
   Branches : $2x + 3 = 0 \implies x = -\frac{3}{2}$ ou $-2x + 6 = 0 \implies x = 3$. $S = \{-\frac{3}{2} \; ; \; 3\}$.
3. $(3x)^2 - 5^2 = 0 \iff (3x - 5)(3x + 5) = 0 \implies x = \frac{5}{3}$ ou $x = -\frac{5}{3}$. $S = \{-\frac{5}{3} \; ; \; \frac{5}{3}\}$.
4. $x^2 - 6x = 0 \iff x(x - 6) = 0 \implies x = 0$ ou $x = 6$. $S = \{0 \; ; \; 6\}$.

**Solution 23.12**
1. Pour 3 : $3 + 1 = 4 \to 4^2 = 16 \to 16 - 3^2 = 16 - 9 = 7 \to 7 - 1 = 6$ (le double de 3).
   Pour 5 : $5 + 1 = 6 \to 6^2 = 36 \to 36 - 25 = 11 \to 11 - 1 = 10$ (le double de 5).
   Pour 10 : $10 + 1 = 11 \to 11^2 = 121 \to 121 - 100 = 21 \to 21 - 1 = 20$ (le double de 10).
   Conjecture : le programme donne toujours le double du nombre choisi ($2n$).
2. Soit $n$ le nombre de départ.
   Le programme calcule : $(n + 1)^2 - n^2 - 1$.
   Développons : $(n^2 + 2n + 1) - n^2 - 1 = n^2 + 2n + 1 - n^2 - 1 = 2n$.
   La conjecture est rigoureusement démontrée pour tout entier $n$.

**Solution 23.13**
Développons $(10d + 5)^2$ avec la première identité remarquable :
$$(10d + 5)^2 = (10d)^2 + 2 \times (10d) \times 5 + 5^2 = 100d^2 + 100d + 25.$$
Factorisons $100d$ dans les deux premiers termes :
$$100d(d + 1) + 25 = [d \times (d + 1)] \times 100 + 25.$$
Multiplier $d \times (d + 1)$ par 100 revient exactement à décaler le résultat de deux rangs vers la gauche (chiffre des centaines), et ajouter 25 place exactement « 25 » sur les chiffres des dizaines et des unités ! L'astuce est mathématiquement infaillible.

---

#### Niveau ★★★

**Solution 23.14**
1. On sait que $(x + 3)^2 = x^2 + 6x + 9$. Donc $x^2 + 6x = (x + 3)^2 - 9$.
2. L'équation $x^2 + 6x = 16$ devient :
   $$(x + 3)^2 - 9 = 16 \iff (x + 3)^2 = 16 + 9 = 25.$$
3. Puisque $25 = 5^2$, on a $x + 3 = 5$ (pour la solution positive cherchée par Al-Khwarizmi), d'où $x = 5 - 3 = 2$.
   (La deuxième solution mathématique moderne est $x + 3 = -5 \implies x = -8$).

**Solution 23.15**
1. D'après le théorème de Pythagore :
   $$x^2 + (x + 7)^2 = (x + 8)^2.$$
2. Développons les deux côtés :
   $$x^2 + (x^2 + 14x + 49) = x^2 + 16x + 64$$
   $$2x^2 + 14x + 49 = x^2 + 16x + 64.$$
   On passe tout à gauche :
   $$(2x^2 - x^2) + (14x - 16x) + (49 - 64) = 0 \iff x^2 - 2x - 15 = 0.$$
3. Développons $(x - 5)(x + 3)$ :
   $$(x - 5)(x + 3) = x^2 + 3x - 5x - 15 = x^2 - 2x - 15.$$
   L'égalité est bien vérifiée !
4. L'équation devient $(x - 5)(x + 3) = 0$.
   Les solutions sont $x = 5$ ou $x = -3$.
   Une longueur ne pouvant être négative, on conserve uniquement $x = 5$.
   Les trois côtés du triangle mesurent donc :
   - Premier côté : $x = 5 \text{ cm}$
   - Deuxième côté : $x + 7 = 5 + 7 = 12 \text{ cm}$
   - Hypoténuse : $x + 8 = 5 + 8 = 13 \text{ cm}$.
   Vérification : $5^2 + 12^2 = 25 + 144 = 169 = 13^2$. C'est un triplet pythagoricien parfait !

**Solution 23.16**
1. Développons par simple et double distributivité :
   $$(a - b)(a^2 + ab + b^2) = a \times a^2 + a \times ab + a \times b^2 - b \times a^2 - b \times ab - b \times b^2$$
   $$= a^3 + a^2b + ab^2 - a^2b - ab^2 - b^3.$$
   Tous les termes intermédiaires s'annulent deux à deux !
   $$= a^3 - b^3.$$
2. On remarque que la différence de deux cubes se factorise selon la formule remarquable :
   $$a^3 - b^3 = (a - b)(a^2 + ab + b^2).$$
3. Pour $x^3 - 8 = x^3 - 2^3$, on applique avec $a = x$ et $b = 2$ :
   $$x^3 - 8 = (x - 2)(x^2 + 2x + 2^2) = (x - 2)(x^2 + 2x + 4).$$

---

### La question qui ouvre la suite

Grâce aux identités remarquables et au produit nul, tu sais maintenant dompter les égalités parfaites et les équilibres stricts. Mais dans la vraie vie et dans le commerce, les plateaux de la balance sont rarement au même niveau : l'un est souvent plus lourd que l'autre, un tarif est plus avantageux qu'un autre au-delà d'un certain seuil, et deux marchands se disputent la clientèle. 

Que se passe-t-il quand la balance penche ? Comment manipuler une **inégalité** sans faire basculer le monde à l'envers, et comment déterminer l'intersection de deux destins marchands ? C'est le mystère que nous allons percer dans le chapitre suivant : **Les Deux Marchands et les Inégalités**.
