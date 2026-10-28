# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 39 : Le Skieur et la Planche sous la Semelle

> *« Jusqu'ici, notre regard prenait des photographies immobiles du monde : des positions figées, des moyennes sur de longues distances. Mais la vie n'est pas un album d'images mortes : elle est un torrent continu. Pour mesurer la pente d'une colline au moment précis où le cœur bat, il faut poser un microscope sur le temps qui coule. »*

---

### Ce que tu vas découvrir

- Le paradoxe du skieur : comment mesurer la **pente en un seul point**, alors qu'une pente exige deux points séparés.
- Le **taux d'accroissement** et le coup de génie du **passage à la limite** quand l'écart $h$ tend vers 0.
- Les notations légendaires : le « $f'(a)$ » de **Lagrange** et le « $\frac{dy}{dx}$ » de **Leibniz**.
- L'équation de la **tangente** : la droite rigide qui effleure la courbe sans la transpercer.
- La preuve géométrique des dérivées usuelles : pourquoi $(x^2)' = 2x$ grâce au **jardin qui grandit**, et les dérivées de $x^n$, $\frac{1}{x}$, $\sqrt{x}$.
- Les opérations sur les fonctions : $(uv)' = u'v + uv'$ (démontré par le rectangle mobile) et la formule du quotient.
- Le lien fondamental entre le **signe de la dérivée** et le **sens de variation**, et la traque des **extremums locaux**.
- Les cas limites où le calcul différentiel s'arrête : le **point anguleux** de la valeur absolue et la **tangente verticale** de la racine carrée.
- Des problèmes concrets d'**optimisation** : fabriquer la boîte la plus spacieuse ou le réservoir le moins cher.

---

### 1. Le problème : le vertige de la descente

Tu as seize ans. Tu te tiens au sommet d'une haute montagne enneigée, skis aux pieds, bâtons plantés dans la poudreuse. Devant toi s'ouvre une piste olympique redoutable : ce n'est pas une rampe droite et régulière, c'est une succession de collines bosselées, de cuvettes abruptes et de replats trompeurs. Le profil vertical de la montagne est une courbe sinueuse, décrite par une fonction d'altitude $y = f(x)$.

Tu t'élances. Le vent siffle dans ton casque, la neige vole en gerbes glacées sous tes carres. La pente change à chaque centième de seconde sous tes semelles : tantôt douce, tantôt plongeant vertigineusement vers le vide.

Au creux de la trajectoire, à l'abscisse exacte $a$, une sensation brutale comprime tes cuisses. Pose-toi cette question fondamentale de physicien :

*« À cet instant précis, à cette milliseconde où mes carres mordent la neige, quelle est la pente de la montagne sous mes pieds ? »*

```
   Altitude y
        ▲
        │                Courbe de la colline y = f(x)
        │                   _--'""'--_   (Sommet : Pente nulle !)
        │                _-"          "-_
        │              /                  \
        │            /                      \
        │        _--' (Forte pente montante) \__
        │    _--'                                "---_ (Descente rapide)
        +─────────────────────────────────────────────► Position x
                     a
```

Pour connaître ton altitude en ce point, c'est immédiat : c'est la valeur $f(a)$.
Mais pour **la pente** ?
Depuis le collège, tu as appris qu'une pente (un coefficient directeur) se calcule toujours en divisant une différence de hauteur par une différence horizontale entre **deux points distincts** :

$$\text{Pente} = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x}.$$

Or, à cet instant précis, tu n'es qu'en **un seul point** !
Si tu tentes d'appliquer la formule en prenant deux fois le même point $A(a; f(a))$, tu obtiens :

$$\text{Pente} = \frac{f(a) - f(a)}{a - a} = \frac{0}{0}.$$

Une division par zéro ! Une absurdité mathématique.
Comment la montagne peut-elle avoir une inclinaison parfaitement réelle et mesurable sous tes semelles, alors que la formule brute de la pente s'effondre en $\frac{0}{0}$ ?

---

### 2. La planche sous la semelle : de la sécante à la tangente

#### 2.1 La rigidité du ski

Pour dénouer ce paradoxe, écoute ton corps et regarde ton équipement.
Sous tes chaussures, tu as chaussé deux lattes en bois, fibres de verre et carres d'acier : des skis. Même si la piste de neige est bosselée et incurvée, **tes skis sont des objets droits et rigides**.

En chaque point où tu t'appuies, la semelle de ton ski vient épouser la courbure de la montagne sans s'enfoncer dedans. Elle effleure la courbe en un point d'appui unique.
Cette droite qui caresse la courbe en un point sans la traverser localement est la **tangente** à la courbe.
Et la pente sous tes pieds, c'est tout simplement **le coefficient directeur de ton ski** !

```
                   Courbe de la montagne
                         ..---*---..
                 ======*================   <--- Le ski rigide (la Tangente !)
                     / |
               Δy   /  |  Élévation verticale
                   /___|
                    Δx    Avancée horizontale
```

#### 2.2 Le taux d'accroissement : la corde sécante

Pour calculer cette pente sans tricher avec le zéro, imaginons que la pointe arrière de ton ski touche la neige en $A(a; f(a))$, et que la spatule avant touche la neige un peu plus loin, en $M(a+h; f(a+h))$, où $h$ est un petit écart non nul.

```
       Altitude
          ▲                   M (a+h ; f(a+h))
          │                  /│
          │                 / │ f(a+h) - f(a)
          │     A          /  │
          │      o────────┴───┘
          │      |    h
          └──────┴────────────┴─────► Position
                 a           a+h
```

La droite $(AM)$ qui coupe la courbe en deux points distincts s'appelle une **sécante**. Sa pente est donnée par le rapport :

$$\tau(h) = \frac{f(a+h) - f(a)}{h}.$$

Ce rapport fondamental s'appelle le **taux d'accroissement** (ou taux de variation) de la fonction $f$ entre $a$ et $a+h$.
Puisque $h \neq 0$, cette fraction est parfaitement calculable !

#### 2.3 Le passage à la limite : le zoom de l'infiniment petit

Maintenant, faisons raccourcir le ski ! Rapprochons la spatule avant de la spatule arrière en faisant devenir $h$ de plus en plus minuscule :
$h = 0{,}1$, puis $h = 0{,}01$, puis $h = 0{,}000001$...
Le point $M$ glisse le long de la colline et vient se fondre sur le point $A$.
La droite sécante $(AM)$ pivote doucement et vient se stabiliser sur une position limite : **la tangente** !

> **📐 Définition — Nombre dérivé**
> Soit $f$ une fonction définie sur un intervalle ouvert contenant $a$.
> On dit que $f$ est **dérivable en $a$** si le taux d'accroissement $\frac{f(a+h)-f(a)}{h}$ admet une limite finie quand $h$ tend vers 0.
> Cette limite est appelée le **nombre dérivé de $f$ en $a$**, et on la note $f'(a)$ :
>
> $$\boxed{f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}}$$
>
> Géométriquement, $f'(a)$ est le **coefficient directeur de la tangente** à la courbe représentative de $f$ au point d'abscisse $a$.

---

### 3. Les notations de l'Histoire : Lagrange contre Leibniz

Deux géants des mathématiques ont offert à l'humanité deux façons complémentaires d'écrire cette même idée :

#### 3.1 La notation « prime » de Joseph-Louis Lagrange (1797)
Le mathématicien franco-italien **Joseph-Louis Lagrange** introduit la notation compacte :
$$f'(a)$$
qui se lit à voix haute : « **f prime de a** ». L'apostrophe marque que cette nouvelle fonction est « dérivée » de la fonction d'origine $f$. Si l'on dérive une deuxième fois, on notera $f''(a)$ (« f seconde »). C'est la notation la plus rapide et la plus utilisée au lycée.

#### 3.2 La notation différentielle de Gottfried Wilhelm Leibniz (1684)
Un siècle plus tôt, le polymathe allemand **Gottfried Wilhelm Leibniz** invente une notation magistrale, inspirée directement du calcul de la pente $\frac{\Delta y}{\Delta x}$ :
$$\frac{df}{dx}(a) \quad \text{ou} \quad \frac{dy}{dx}$$
qui se lit : « **d de f sur d de x** » ou « **dérivée de y par rapport à x** ».
La lettre latine $d$ remplace la lettre grecque $\Delta$ pour indiquer une variation **infinitésimale** (infiniment petite). Cette notation rappelle en permanence qu'une dérivée est le rapport d'une minuscule variation de hauteur $dy$ sur une minuscule variation horizontale $dx$. Les physiciens l'adorent car elle porte directement les unités de mesure (par exemple des mètres par seconde : $\frac{dx}{dt} = \text{vitesse}$).

---

### 4. L'équation de la tangente à la courbe

Puisque la tangente passe par le point de contact $A(a; f(a))$ et possède un coefficient directeur égal à $f'(a)$, son équation réduite découle immédiatement de la formule des droites vue en Seconde :

$$y - y_A = m(x - x_A) \iff y - f(a) = f'(a)(x - a).$$

> **📐 Théorème — Équation de la tangente**
> Si $f$ est dérivable en $a$, la courbe représentative $\mathcal{C}_f$ admet au point $A(a; f(a))$ une tangente d'équation :
>
> $$\boxed{y = f'(a)(x - a) + f(a)}$$

Cette droite est la **meilleure approximation affine** de la fonction au voisinage de $a$. Pour $x$ très proche de $a$, on a l'approximation :
$$f(x) \approx f(a) + f'(a)(x - a).$$

---

### 5. Les dérivées usuelles démontrées

Passons en revue les fonctions de base. Pour chacune d'elles, nous allons calculer la limite du taux d'accroissement avec rigueur.

#### 5.1 La fonction constante : $f(x) = k$
Une piste parfaitement horizontale a une pente nulle partout.
Pour tout $h \neq 0$ :
$$\frac{f(a+h) - f(a)}{h} = \frac{k - k}{h} = \frac{0}{h} = 0.$$
La limite quand $h \to 0$ est 0. Donc :
$$\boxed{(k)' = 0}$$

#### 5.2 La fonction linéaire : $f(x) = x$
Une rampe droite inclinée à 45° a une pente constante égale à 1.
$$\frac{(a+h) - a}{h} = \frac{h}{h} = 1 \xrightarrow[h \to 0]{} 1.$$
Donc :
$$\boxed{(x)' = 1}$$

#### 5.3 La fonction carré : pourquoi $(x^2)' = 2x$ ?
C'est ici qu'intervient la sublime démonstration du jardinier :

> **✍️ Démonstration géométrique — Le parterre de fleurs qui grandit**
> Soit un parterre carré de fleurs de côté $x$. Sa surface est $S(x) = x^2$.
> Au printemps, le jardinier élargit le parterre d'une mince bande de terre de largeur $h$ vers l'Est et d'une bande de largeur $h$ vers le Nord.
>
> ```
>                   x                h
>           ┌──────────────────────┬───┐
>           │                      │   │
>         x │    Carré d'origine   │ B │ h  (Bande Est : x × h)
>           │        (x²)          │   │
>           │                      │   │
>           ├──────────────────────┼───┤
>         h │      Bande Nord      │ C │ h  (Coin : h²)
>           └──────────────────────┴───┘
>                      x             h
> ```
>
> L'accroissement total de terre est constitué de trois morceaux :
> 1. Une bande Est de surface $x \times h$ ;
> 2. Une bande Nord de surface $x \times h$ ;
> 3. Un minuscule carré dans le coin de surface $h^2$.
>
> Le gain total de surface est donc :
> $$\Delta S = (x \times h) + (x \times h) + h^2 = 2xh + h^2.$$
> Divisons par l'élargissement $h$ pour trouver le taux d'accroissement :
> $$\frac{\Delta S}{h} = \frac{2xh + h^2}{h} = 2x + h.$$
> Faisons maintenant tendre $h$ vers zéro !
> Le coin minuscule $h^2$ s'évanouit infiniment plus vite que les bordures. Il ne reste que :
> $$\lim_{h \to 0} (2x + h) = 2x.$$
> Le chiffre 2 n'a rien de magique : **ce sont les 2 côtés libres du carré qui s'étirent dans l'espace !** $\blacksquare$

Par le calcul algébrique pur :
$$\frac{(a+h)^2 - a^2}{h} = \frac{a^2 + 2ah + h^2 - a^2}{h} = \frac{2ah + h^2}{h} = 2a + h \xrightarrow[h \to 0]{} 2a.$$
Donc :
$$\boxed{(x^2)' = 2x}$$

#### 5.4 La fonction puissance : $f(x) = x^n$ ($n \in \mathbb{N}^*$)
En étendant l'idée à un cube ($x^3$), les trois faces libres donnent $(x^3)' = 3x^2$.
En dimension $n$, en utilisant l'identité algébrique remarquable :
$$A^n - B^n = (A - B)(A^{n-1} + A^{n-2}B + \dots + AB^{n-2} + B^{n-1}),$$
avec $A = a+h$ et $B = a$, le taux s'écrit :
$$\frac{(a+h)^n - a^n}{h} = \frac{h \cdot \left((a+h)^{n-1} + (a+h)^{n-2}a + \dots + a^{n-1}\right)}{h}.$$
Il y a exactement $n$ termes dans la parenthèse. Quand $h \to 0$, chacun de ces termes tend vers $a^{n-1}$. La somme vaut donc $n a^{n-1}$.
$$\boxed{(x^n)' = n x^{n-1}}$$

#### 5.5 La fonction inverse : $f(x) = \frac{1}{x}$ sur $\mathbb{R}^*$
Pour tout $a \neq 0$ et $h$ suffisamment petit :
$$\frac{f(a+h) - f(a)}{h} = \frac{\frac{1}{a+h} - \frac{1}{a}}{h} = \frac{\frac{a - (a+h)}{a(a+h)}}{h} = \frac{\frac{-h}{a(a+h)}}{h} = -\frac{1}{a(a+h)}.$$
Quand $h \to 0$, le dénominateur tend vers $a \times a = a^2$.
La limite vaut donc $-\frac{1}{a^2}$.
$$\boxed{\left(\frac{1}{x}\right)' = -\frac{1}{x^2}}$$

#### 5.6 La fonction racine carrée : $f(x) = \sqrt{x}$ sur $]0; +\infty[$
Pour tout $a > 0$, calculons le taux d'accroissement. Nous faisons face à une forme indéterminée $\frac{0}{0}$. Pour la débloquer, multiplions par l'**expression conjuguée** $(\sqrt{a+h} + \sqrt{a})$ :
$$\frac{\sqrt{a+h} - \sqrt{a}}{h} = \frac{(\sqrt{a+h} - \sqrt{a})(\sqrt{a+h} + \sqrt{a})}{h(\sqrt{a+h} + \sqrt{a})} = \frac{(a+h) - a}{h(\sqrt{a+h} + \sqrt{a})} = \frac{h}{h(\sqrt{a+h} + \sqrt{a})} = \frac{1}{\sqrt{a+h} + \sqrt{a}}.$$
Quand $h \to 0$, le dénominateur tend vers $\sqrt{a} + \sqrt{a} = 2\sqrt{a}$.
$$\boxed{(\sqrt{x})' = \frac{1}{2\sqrt{x}}}$$

---

### 6. Les opérations sur les fonctions dérivées

Soient $u$ et $v$ deux fonctions dérivables sur un intervalle $I$, et $k$ une constante réelle.

#### 6.1 Somme et multiplication par une constante
- $(u + v)' = u' + v'$
- $(k \cdot u)' = k \cdot u'$

#### 6.2 Dérivée d'un produit : pourquoi $(uv)' \neq u'v'$ ?
C'est le piège le plus célèbre de l'histoire des mathématiques. Même Leibniz est tombé dedans dans sa première ébauche en 1673, avant de se corriger en dessinant un rectangle !

> **✍️ Démonstration géométrique — Le rectangle dont les deux côtés s'allongent**
> Soit un champ rectangulaire de côtés $u(x)$ et $v(x)$. Son aire est $A(x) = u(x) \times v(x)$.
> Lorsque la variable $x$ avance d'une quantité $h$, la largeur devient $u + \Delta u$ et la longueur devient $v + \Delta v$.
>
> ```
>                   u(x)              Δu
>           ┌──────────────────────┬──────┐
>           │                      │      │
>      v(x) │      Aire de base    │      │
>           │       u(x) × v(x)    │ v·Δu │
>           │                      │      │
>           ├──────────────────────┼──────┤
>        Δv │         u·Δv         │Δu·Δv │
>           └──────────────────────┴──────┘
> ```
>
> La nouvelle aire ajoutée est formée de trois zones :
> 1. Une bande verticale de surface $v(x) \times \Delta u$ ;
> 2. Une bande horizontale de surface $u(x) \times \Delta v$ ;
> 3. Un coin minuscule de surface $\Delta u \times \Delta v$.
>
> Divisons par $h$ :
> $$\frac{\Delta A}{h} = v(x) \frac{\Delta u}{h} + u(x) \frac{\Delta v}{h} + \frac{\Delta u \cdot \Delta v}{h}.$$
> Quand $h \to 0$ :
> - $\frac{\Delta u}{h} \to u'(x)$ et $\frac{\Delta v}{h} \to v'(x)$ ;
> - le troisième terme s'évanouit car $\Delta u \to 0$ !
> Il reste les deux grandes bandes :
> $$\boxed{(u \cdot v)' = u'v + uv'} \quad \blacksquare$$

#### 6.3 Dérivée de l'inverse et du quotient
Si $v(x) \neq 0$ sur $I$ :
- Dérivée de l'inverse :
  $$\boxed{\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}}$$
- Dérivée du quotient :
  En écrivant $\frac{u}{v} = u \times \frac{1}{v}$ et en appliquant la formule du produit :
  $$\left(\frac{u}{v}\right)' = u'\left(\frac{1}{v}\right) + u\left(-\frac{v'}{v^2}\right) = \frac{u'v}{v^2} - \frac{uv'}{v^2} = \boxed{\frac{u'v - uv'}{v^2}}$$

> **⚠️ Attention, piège ! — L'ordre du numérateur dans le quotient**
> Dans la formule $\frac{u'v - uv'}{v^2}$, le signe moins fait que l'ordre des termes est capital ! C'est toujours la dérivée du haut ($u'$) qui multiplie le bas intact ($v$) en premier. Inverser l'ordre donne l'opposé du bon résultat.

---

### 7. Le lien crucial : signe de la dérivée et sens de variation

C'est ici que la dérivation révèle sa puissance absolue : elle transforme une question globale difficile (« la fonction monte-t-elle ou descend-elle ? ») en une question locale simple (« quel est le signe d'un nombre ? »).

> **📐 Théorème fondamental — Variations et signe de la dérivée**
> Soit $f$ une fonction dérivable sur un intervalle $I$.
> - Si pour tout $x \in I$, $f'(x) > 0$, alors la fonction $f$ est **strictement croissante** sur $I$.
> - Si pour tout $x \in I$, $f'(x) < 0$, alors la fonction $f$ est **strictement décroissante** sur $I$.
> - Si pour tout $x \in I$, $f'(x) = 0$, alors la fonction $f$ est **constante** sur $I$.

Intuitivement : si la semelle de ton ski pointe vers le haut ($f'(x) > 0$) à chaque instant de ta course, tu ne peux que prendre de l'altitude !

---

### 8. Recherche des extremums locaux et optimisation

Comment trouver le point culminant d'une colline ou le creux le plus profond d'une vallée ?
Au sommet d'une colline, la pente cesse de monter et s'apprête à descendre : pendant un instant infinitésimal, le ski redevient parfaitement horizontal !

```
                Tangente horizontale (f'(x₀) = 0)
                      =======================
                            ..---*---..
                          /             \
                    f' > 0               f' < 0
                   (Montée)             (Descente)
```

> **📐 Théorème — Condition d'extremum local**
> Soit $f$ une fonction dérivable sur un intervalle ouvert contenant $x_0$.
> Si $f$ admet un extremum local (maximum ou minimum) en $x_0$, alors :
> $$f'(x_0) = 0.$$
>
> **Réciproque et critère pratique :**
> Si $f'(x_0) = 0$ et si $f'$ **change de signe** en $x_0$, alors $f$ admet un extremum local en $x_0$ :
> - De $+$ vers $-$ : c'est un **maximum local** (la courbe monte puis descend).
> - De $-$ vers $+$ : c'est un **minimum local** (la courbe descend puis monte).

> **⚠️ Attention, piège ! — $f'(x_0) = 0$ ne garantit pas un extremum**
> Regarde la fonction cube $f(x) = x^3$. Sa dérivée est $f'(x) = 3x^2$.
> En $x = 0$, on a bien $f'(0) = 0$ (la tangente est horizontale).
> Mais pour tout $x \neq 0$, $3x^2 > 0$ : la dérivée ne change pas de signe ! La courbe monte avant 0 et continue de monter après 0. Le point $(0; 0)$ est un replat (un point d'inflexion), pas un sommet !

---

### 9. Aux limites de la dérivation : quand le calcul se brise

Toutes les fonctions sont-elles dérivables partout ? Non ! Il existe deux manières majeures pour une courbe de refuser la dérivation en un point.

#### 9.1 Le point anguleux : la valeur absolue en 0
Considérons la fonction valeur absolue $f(x) = |x|$. Sa courbe forme un « V » pointu en l'origine.
Calculons le taux d'accroissement en $0$ :
$$\tau(h) = \frac{|0+h| - |0|}{h} = \frac{|h|}{h}.$$
- Si l'on arrive par la droite ($h > 0$) : $|h| = h$, donc $\tau(h) = \frac{h}{h} = +1$.
- Si l'on arrive par la gauche ($h < 0$) : $|h| = -h$, donc $\tau(h) = \frac{-h}{h} = -1$.

La limite à droite ($+1$) est différente de la limite à gauche ($-1$) !
Le ski ne sait pas comment se poser sur la pointe sans vaciller entre deux inclinaisons.
On dit que la fonction valeur absolue **n'est pas dérivable en 0**. La courbe admet deux demi-tangentes qui forment un **point anguleux**.

#### 9.2 La tangente verticale : la racine carrée en 0
Considérons la fonction $f(x) = \sqrt{x}$ en $a = 0$.
Pour $h > 0$ :
$$\tau(h) = \frac{\sqrt{0+h} - \sqrt{0}}{h} = \frac{\sqrt{h}}{h} = \frac{1}{\sqrt{h}}.$$
Quand $h \to 0^+$, $\sqrt{h}$ devient infiniment petit et positif, donc $\frac{1}{\sqrt{h}}$ explose vers $+\infty$ !
La limite n'est pas un nombre réel fini.
La fonction racine carrée **n'est pas dérivable en 0**.
Géométriquement, la courbe démarre verticalement : elle admet une **demi-tangente verticale** d'équation $x = 0$.

---

### Exemples résolus pas à pas

> **✅ Exemple résolu 1 — Calcul de dérivée par définition**
> Soit $f(x) = 3x^2 - 5x + 2$. Calculer $f'(2)$ en utilisant la définition avec le taux d'accroissement.
>
> **Solution détaillée :**
> Calculons $f(2)$ : $f(2) = 3(2^2) - 5(2) + 2 = 12 - 10 + 2 = 4$.
> Évaluons $f(2+h)$ pour $h \neq 0$ :
> $$\begin{aligned}
> f(2+h) &= 3(2+h)^2 - 5(2+h) + 2 \\
> &= 3(4 + 4h + h^2) - 10 - 5h + 2 \\
> &= 12 + 12h + 3h^2 - 10 - 5h + 2 = 4 + 7h + 3h^2.
> \end{aligned}$$
> Formons le taux d'accroissement :
> $$\frac{f(2+h) - f(2)}{h} = \frac{(4 + 7h + 3h^2) - 4}{h} = \frac{7h + 3h^2}{h} = \frac{h(7 + 3h)}{h} = 7 + 3h.$$
> Prenons la limite quand $h \to 0$ :
> $$\lim_{h \to 0} (7 + 3h) = 7.$$
> Donc $f$ est dérivable en $2$ et $\boxed{f'(2) = 7}$.

> **✅ Exemple résolu 2 — Équation d'une tangente**
> Soit $f(x) = \frac{1}{x}$. Déterminer l'équation de la tangente à la courbe de $f$ au point d'abscisse $a = 2$.
>
> **Solution détaillée :**
> - Ordonnée du point de contact : $f(2) = \frac{1}{2}$.
> - Fonction dérivée : $f'(x) = -\frac{1}{x^2}$, donc $f'(2) = -\frac{1}{2^2} = -\frac{1}{4}$.
> - Formule de la tangente : $y = f'(2)(x - 2) + f(2)$.
> $$y = -\frac{1}{4}(x - 2) + \frac{1}{2} = -\frac{1}{4}x + \frac{2}{4} + \frac{1}{2} = -\frac{1}{4}x + 1.$$
> L'équation de la tangente est $\boxed{y = -\frac{1}{4}x + 1}$.

> **✅ Exemple résolu 3 — Dérivée d'un produit et d'un quotient**
> Calculer les fonctions dérivées de :
> 1. $g(x) = (2x - 3)(x^2 + 4x)$
> 2. $h(x) = \frac{3x - 1}{x^2 + 1}$
>
> **Solution détaillée :**
> 1. Forme $u \cdot v$ avec $u(x) = 2x - 3 \implies u'(x) = 2$, et $v(x) = x^2 + 4x \implies v'(x) = 2x + 4$.
>    $$g'(x) = u'v + uv' = 2(x^2 + 4x) + (2x - 3)(2x + 4).$$
>    Développons :
>    $g'(x) = (2x^2 + 8x) + (4x^2 + 8x - 6x - 12) = 6x^2 + 10x - 12$.
> 2. Forme $\frac{u}{v}$ avec $u(x) = 3x - 1 \implies u'(x) = 3$, et $v(x) = x^2 + 1 \implies v'(x) = 2x$.
>    $$h'(x) = \frac{u'v - uv'}{v^2} = \frac{3(x^2 + 1) - (3x - 1)(2x)}{(x^2 + 1)^2}.$$
>    Développons le numérateur :
>    $3x^2 + 3 - (6x^2 - 2x) = 3x^2 + 3 - 6x^2 + 2x = -3x^2 + 2x + 3$.
>    D'où : $\boxed{h'(x) = \frac{-3x^2 + 2x + 3}{(x^2 + 1)^2}}$.

> **✅ Exemple résolu 4 — Étude complète des variations d'un polynôme de degré 3**
> Soit $f(x) = 2x^3 - 9x^2 + 12x - 1$ définie sur $\mathbb{R}$.
> Dresser son tableau de variations complet et préciser ses extremums locaux.
>
> **Solution détaillée :**
> 1. Dérivée : $f'(x) = 2(3x^2) - 9(2x) + 12(1) - 0 = 6x^2 - 18x + 12$.
>    Factorisons par 6 : $f'(x) = 6(x^2 - 3x + 2)$.
> 2. Racines de $f'(x)$ :
>    Le trinôme $x^2 - 3x + 2$ a pour racines évidentes $x_1 = 1$ et $x_2 = 2$ (car $1 - 3 + 2 = 0$ et $1 \times 2 = 2$).
>    Le coefficient devant $x^2$ est positif ($a = 6 > 0$), donc la parabole de $f'$ est tournée vers le haut :
>    - $f'(x) > 0$ sur $]-\infty; 1[$ et sur $]2; +\infty[$ ;
>    - $f'(x) < 0$ sur $]1; 2[$.
> 3. Valeurs particulières :
>    $f(1) = 2(1)^3 - 9(1)^2 + 12(1) - 1 = 2 - 9 + 12 - 1 = 4$.
>    $f(2) = 2(8) - 9(4) + 12(2) - 1 = 16 - 36 + 24 - 1 = 3$.
> 4. Tableau de variations :
>
> | $x$ | $-\infty$ | | $1$ | | $2$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
> | $f(x)$ | | $\nearrow$ | $4$ | $\searrow$ | $3$ | $\nearrow$ | |
>
> **Conclusion :**
> $f$ admet un **maximum local** égal à $4$ atteint en $x = 1$, et un **minimum local** égal à $3$ atteint en $x = 2$.

> **✅ Exemple résolu 5 — Optimisation concrète : la boîte sans couvercle**
> Dans une feuille de carton carrée de 12 cm de côté, on découpe à chaque coin un petit carré de côté $x$ (avec $0 < x < 6$), puis on replie les bords pour former une boîte ouverte.
> Quelle valeur de $x$ donne à la boîte un volume maximal ?
>
> **Solution détaillée :**
> 1. Dimensions de la boîte pliée :
>    - La base est un carré de côté $12 - 2x$.
>    - La hauteur de la boîte est $x$.
> 2. Volume de la boîte :
>    $V(x) = \text{Base} \times \text{hauteur} = (12 - 2x)^2 \times x = (144 - 48x + 4x^2)x = 4x^3 - 48x^2 + 144x$.
> 3. Dérivée :
>    $V'(x) = 12x^2 - 96x + 144 = 12(x^2 - 8x + 12)$.
> 4. Recherche du maximum :
>    Racines de $x^2 - 8x + 12 = 0$ :
>    $\Delta = (-8)^2 - 4(1)(12) = 64 - 48 = 16 = 4^2$.
>    $x_1 = \frac{8 - 4}{2} = 2$, et $x_2 = \frac{8 + 4}{2} = 6$.
>    Comme $x \in ]0; 6[$, seule la solution $x = 2$ convient.
>    Pour $x < 2$, $V'(x) > 0$ (le volume grandit). Pour $x > 2$, $V'(x) < 0$ (le volume rétrécit).
> 5. Conclusion :
>    Le volume maximal est atteint pour une découpe de **$x = 2$ cm**.
>    Le volume vaut alors $V(2) = (12 - 4)^2 \times 2 = 8^2 \times 2 = 64 \times 2 = 128\text{ cm}^3$.

> **✅ Exemple résolu 6 — Tangente parallèle à une droite donnée**
> Soit $f(x) = x^2 - 4x + 1$. Existe-t-il des points sur la parabole où la tangente est parallèle à la droite d'équation $y = 2x - 5$ ?
>
> **Solution détaillée :**
> - Deux droites sont parallèles si et seulement si elles ont le même coefficient directeur.
> - La droite a pour pente $m = 2$.
> - La tangente au point d'abscisse $x$ a pour coefficient directeur $f'(x)$.
> - Calculons $f'(x)$ : $f'(x) = 2x - 4$.
> - On résout donc l'équation $f'(x) = 2$ :
>   $$2x - 4 = 2 \iff 2x = 6 \iff x = 3.$$
> - Ordonnée du point : $f(3) = 3^2 - 4(3) + 1 = 9 - 12 + 1 = -2$.
> - Conclusion : Il existe un unique point qui répond au problème, le point $A(3; -2)$.
>   La tangente y a pour équation $y = 2(x - 3) - 2 = 2x - 8$.

---

### Ce qu'il faut retenir

1. **Le nombre dérivé $f'(a)$ :**
   - Définition : $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$.
   - Sens géométrique : pente du ski sous le pied = coefficient directeur de la tangente en $A(a; f(a))$.
   - Équation de la tangente : $\boxed{y = f'(a)(x - a) + f(a)}$.

2. **Tableau des dérivées usuelles :**
   | Fonction $f(x)$ | Dérivée $f'(x)$ | Domaine de validité |
   |---|---|---|
   | $k$ (constante) | $0$ | $\mathbb{R}$ |
   | $x$ | $1$ | $\mathbb{R}$ |
   | $x^2$ | $2x$ | $\mathbb{R}$ |
   | $x^n$ ($n \in \mathbb{N}^*$) | $n x^{n-1}$ | $\mathbb{R}$ |
   | $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\mathbb{R}^* = ]-\infty; 0[ \cup ]0; +\infty[$ |
   | $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | $]0; +\infty[$ (non dérivable en 0) |

3. **Formules d'opérations :**
   - $(u + v)' = u' + v'$
   - $(k u)' = k u'$
   - $(u v)' = u'v + uv'$
   - $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$
   - $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

4. **Signe de la dérivée et variations :**
   - $f'(x) > 0 \implies f$ est strictement croissante.
   - $f'(x) < 0 \implies f$ est strictement décroissante.
   - $f'(x_0) = 0$ avec changement de signe $\implies$ extremum local (sommet ou creux).

5. **Cas de non-dérivabilité :**
   - $f(x) = |x|$ en 0 : point anguleux (pentes à gauche et à droite différentes).
   - $f(x) = \sqrt{x}$ en 0 : demi-tangente verticale (taux d'accroissement tend vers $+\infty$).

---

### Exercices

#### Niveau ★ (Calculs directs de dérivées et tangentes)

1. Calculer la dérivée de $f(x) = 5x^3 - 4x^2 + 7x - 9$.
2. Calculer la dérivée de $g(x) = 3\sqrt{x} - \frac{4}{x}$ pour $x > 0$.
3. Déterminer le nombre dérivé $f'(3)$ pour $f(x) = x^2 - 2x$.
4. Écrire l'équation de la tangente à la courbe de $f(x) = x^2$ au point d'abscisse $a = 1$.
5. Déterminer les abscisses des points où la courbe de $f(x) = x^3 - 3x$ admet une tangente horizontale.
6. Soit $f(x) = \frac{2x+1}{x-3}$ sur $]3; +\infty[$. Calculer $f'(x)$.
7. Dériver $h(x) = (x^2 + 1)(3x - 2)$.
8. Trouver le signe de la dérivée de $f(x) = -2x^2 + 8x - 5$ et en déduire le sens de variation de $f$.
9. La fonction $f(x) = |x-3|$ est-elle dérivable en $x = 3$ ? Justifier.
10. Déterminer l'approximation affine de $\sqrt{1+h}$ pour $h$ proche de 0 en utilisant la dérivée en 1 de $\sqrt{x}$.

#### Niveau ★★ (Études de fonctions et géométrie)

11. Dresser le tableau de variations complet de $f(x) = \frac{1}{3}x^3 - x^2 - 3x + 4$ sur $\mathbb{R}$.
12. Soit $f(x) = \frac{x^2 - 3x + 6}{x - 1}$ définie sur $]1; +\infty[$.
    a) Calculer $f'(x)$ et montrer que $f'(x) = \frac{(x-3)(x+1)}{(x-1)^2}$.
    b) En déduire le minimum de $f$ sur cet intervalle.
13. On considère la parabole d'équation $y = -x^2 + 4x - 1$.
    Existe-t-il une tangente à cette parabole qui passe par l'origine du repère $(0; 0)$ ?
14. Soit la fonction $f(x) = x\sqrt{x}$ définie sur $[0; +\infty[$.
    a) Montrer par le taux d'accroissement que $f$ est dérivable en $0$ et préciser $f'(0)$.
    b) Calculer $f'(x)$ pour $x > 0$ avec la règle du produit et vérifier la cohérence.
15. Déterminer les points d'intersection de la courbe de $f(x) = x^3 - 3x^2 + x$ avec la tangente à cette courbe en $x = 0$.
16. Un projectile est lancé en l'air. Son altitude en mètres à l'instant $t$ (en secondes) est donnée par $z(t) = -5t^2 + 20t + 1{,}5$.
    a) Calculer la vitesse instantanée $v(t) = z'(t)$ à chaque instant.
    b) À quel instant le projectile atteint-il son altitude maximale ? Quelle est cette altitude ?
17. Démontrer par récurrence que pour tout entier $n \ge 1$, la dérivée de $f_n(x) = x^n$ est bien $f'_n(x) = n x^{n-1}$, en utilisant la dérivée d'un produit.
18. Soit $f(x) = \frac{ax + b}{x - 2}$. Déterminer les réels $a$ et $b$ pour que la courbe passe par $A(3; 5)$ et y admette une tangente de coefficient directeur $-7$.

#### Niveau ★★★ (Optimisation et problèmes ouverts)

19. **La clôture du berger :**
    Un berger dispose de 100 mètres de grillage pour aménager un enclos rectangulaire adossé à une falaise rocheuse rectiligne (il n'y a donc pas besoin de grillage le long de la falaise).
    Quelles doivent être les dimensions de l'enclos pour que les moutons disposent de la plus grande surface possible ?
20. **La boîte de conserve optimale :**
    On souhaite fabriquer une boîte de conserve cylindrique fermée d'un volume donné $V = 1$ litre ($1000\text{ cm}^3$).
    On cherche à minimiser la quantité de métal nécessaire (c'est-à-dire l'aire totale du cylindre).
    a) Exprimer la hauteur $h$ en fonction du rayon $r$.
    b) Exprimer la surface totale $S(r)$ en fonction de $r$.
    c) Calculer $S'(r)$ et prouver que la boîte la plus économe en métal vérifie $h = 2r$ (la hauteur doit être exactement égale au diamètre !).
21. **La distance minimale d'un point à une parabole :**
    Dans un repère orthonormé, on considère la parabole $\mathcal{P}$ d'équation $y = x^2$ et le point $A(0; 2)$.
    Quel est le point de la parabole le plus proche de $A$ ? Montrer que le segment joignant $A$ à ce point optimal est perpendiculaire à la tangente à la parabole en ce point.
22. **Point anguleux et dérivabilité :**
    Soit la fonction définie par $f(x) = x|x|$.
    a) Exprimer $f(x)$ sans valeur absolue selon le signe de $x$.
    b) Étudier la dérivabilité de $f$ en 0 en calculant la limite du taux d'accroissement.
    c) Que peut-on en conclure ? Une fonction contenant une valeur absolue a-t-elle toujours un point anguleux ?
23. **Tangentes communes à deux paraboles :**
    Soient les deux paraboles d'équations $y = x^2$ et $y = -x^2 + 4x - 6$.
    Existe-t-il une droite tangente commune aux deux paraboles simultanément ? Si oui, déterminer son équation.
24. **Le problème de Snell-Descartes du maître-nageur :**
    Un sauveteur situé sur la plage en un point $A(0; a)$ avec $a > 0$ aperçoit un nageur en détresse dans la mer en $B(d; -b)$ avec $b > 0$. La ligne de rivage est l'axe des abscisses $y = 0$.
    Le sauveteur court sur le sable à la vitesse $v_1$ et nage dans l'eau à une vitesse plus lente $v_2 < v_1$.
    Il entre dans l'eau au point $M(x; 0)$ avec $0 \le x \le d$.
    a) Exprimer le temps total de parcours $T(x)$ pour atteindre le nageur.
    b) Calculer $T'(x)$ et montrer que le temps est minimal lorsque $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$ (loi de Snell-Descartes de la réfraction de la lumière !).
25. **Théorème de Rolle (découverte intuitive) :**
    Soit $f$ une fonction dérivable sur $[a; b]$ telle que $f(a) = f(b) = 0$.
    Justifier intuitivement à l'aide du skieur pourquoi il existe obligatoirement au moins un point $c \in ]a; b[$ où $f'(c) = 0$.

---

### Solutions

**1.** $f'(x) = 5(3x^2) - 4(2x) + 7(1) - 0 = 15x^2 - 8x + 7$.

**2.** $g'(x) = 3\left(\frac{1}{2\sqrt{x}}\right) - 4\left(-\frac{1}{x^2}\right) = \frac{3}{2\sqrt{x}} + \frac{4}{x^2}$.

**3.** $f'(x) = 2x - 2$. En $x = 3$ : $f'(3) = 2(3) - 2 = 4$.

**4.** $f(1) = 1^2 = 1$. $f'(x) = 2x \implies f'(1) = 2$.
Tangente : $y = f'(1)(x - 1) + f(1) = 2(x - 1) + 1 = 2x - 1$.

**5.** $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x - 1)(x + 1)$.
Tangente horizontale $\iff f'(x) = 0 \iff x = 1$ ou $x = -1$.

**6.** Formule $\frac{u}{v}$ : $u(x) = 2x+1 \implies u'=2$ ; $v(x) = x-3 \implies v'=1$.
$f'(x) = \frac{2(x-3) - (2x+1)(1)}{(x-3)^2} = \frac{2x - 6 - 2x - 1}{(x-3)^2} = -\frac{7}{(x-3)^2}$.

**7.** Règle du produit : $u = x^2+1 \implies u'=2x$ ; $v = 3x-2 \implies v'=3$.
$h'(x) = 2x(3x-2) + (x^2+1)(3) = 6x^2 - 4x + 3x^2 + 3 = 9x^2 - 4x + 3$.

**8.** $f'(x) = -4x + 8 = -4(x - 2)$.
$f'(x) > 0$ si $x < 2$ (la fonction $f$ est strictement croissante sur $]-\infty; 2]$) ;
$f'(x) < 0$ si $x > 2$ (la fonction $f$ est strictement décroissante sur $[2; +\infty[$).

**9.** Taux d'accroissement en $3$ : $\frac{|3+h-3| - |0|}{h} = \frac{|h|}{h}$.
Quand $h \to 0^+$, la limite vaut $+1$ ; quand $h \to 0^-$, la limite vaut $-1$.
Les deux limites étant distinctes, $f$ n'est pas dérivable en 3 (point anguleux).

**10.** Soit $f(x) = \sqrt{x}$. On a $f(1) = 1$ et $f'(1) = \frac{1}{2\sqrt{1}} = \frac{1}{2}$.
L'approximation affine en 1 est $f(1+h) \approx f(1) + h f'(1) = 1 + \frac{1}{2}h$.
Par exemple, $\sqrt{1{,}04} \approx 1 + \frac{0{,}04}{2} = 1{,}02$ (la vraie valeur est $1{,}0198\dots$).

**11.** $f'(x) = x^2 - 2x - 3 = (x - 3)(x + 1)$.
Racines : $x = -1$ et $x = 3$. Parabole tournée vers le haut.
- $f'(x) > 0$ sur $]-\infty; -1[ \cup ]3; +\infty[$ ($f$ croissante) ;
- $f'(x) < 0$ sur $]-1; 3[$ ($f$ décroissante).
Extremums :
$f(-1) = -\frac{1}{3} - 1 + 3 + 4 = \frac{17}{3} \approx 5{,}67$ (maximum local en $-1$) ;
$f(3) = 9 - 9 - 9 + 4 = -5$ (minimum local en $3$).

**12.**
a) $u(x) = x^2 - 3x + 6 \implies u'=2x - 3$ ; $v(x) = x-1 \implies v'=1$.
$f'(x) = \frac{(2x-3)(x-1) - (x^2-3x+6)(1)}{(x-1)^2} = \frac{2x^2 - 5x + 3 - x^2 + 3x - 6}{(x-1)^2} = \frac{x^2 - 2x - 3}{(x-1)^2}$.
Le trinôme se factorise en $(x - 3)(x + 1)$.
b) Sur $]1; +\infty[$, le dénominateur $(x-1)^2 > 0$ et $x+1 > 0$. Le signe dépend uniquement de $x - 3$.
$f'(x) < 0$ sur $]1; 3[$ et $f'(x) > 0$ sur $]3; +\infty[$.
$f$ admet un minimum absolu en $x = 3$, qui vaut $f(3) = \frac{9 - 9 + 6}{3 - 1} = \frac{6}{2} = 3$.

**13.** La tangente en un point $a$ a pour équation $y = f'(a)(x - a) + f(a)$.
Ici $f(a) = -a^2 + 4a - 1$ et $f'(a) = -2a + 4$.
L'équation est $y = (-2a + 4)(x - a) - a^2 + 4a - 1 = (-2a + 4)x + 2a^2 - 4a - a^2 + 4a - 1 = (-2a + 4)x + a^2 - 1$.
Cette droite passe par l'origine $(0; 0)$ si et seulement si l'ordonnée à l'origine est nulle :
$a^2 - 1 = 0 \iff a = 1$ ou $a = -1$.
Il existe donc **deux** tangentes passant par l'origine : celle au point d'abscisse $1$ (équation $y = 2x$) et celle au point d'abscisse $-1$ (équation $y = 6x$).

**14.**
a) Pour $h > 0$ : $\frac{f(h) - f(0)}{h} = \frac{h\sqrt{h} - 0}{h} = \sqrt{h}$.
Quand $h \to 0^+$, $\lim \sqrt{h} = 0$. Donc $f$ est bien dérivable en 0 et $f'(0) = 0$.
b) Règle du produit pour $x > 0$ : $f'(x) = (1)\sqrt{x} + x\left(\frac{1}{2\sqrt{x}}\right) = \sqrt{x} + \frac{x}{2\sqrt{x}} = \sqrt{x} + \frac{\sqrt{x}}{2} = \frac{3}{2}\sqrt{x}$.
Quand $x \to 0$, $\frac{3}{2}\sqrt{x} \to 0$, ce qui est parfaitement cohérent avec $f'(0) = 0$.

**15.** En $x = 0$, $f(0) = 0$. $f'(x) = 3x^2 - 6x + 1 \implies f'(0) = 1$.
La tangente en 0 a pour équation $y = 1(x - 0) + 0 \iff y = x$.
Intersection avec la courbe : $f(x) = x \iff x^3 - 3x^2 + x = x \iff x^3 - 3x^2 = 0 \iff x^2(x - 3) = 0$.
Solutions : $x = 0$ (racine double, point de tangence) et $x = 3$.
Pour $x = 3$, $y = 3$. Le second point d'intersection est $B(3; 3)$.

**16.**
a) $v(t) = z'(t) = -10t + 20$.
b) L'altitude est maximale lorsque la vitesse s'annule : $-10t + 20 = 0 \iff t = 2$ secondes.
L'altitude maximale est $z(2) = -5(4) + 20(2) + 1{,}5 = -20 + 40 + 1{,}5 = 21{,}5$ mètres.

**17.**
- Initialisation ($n=1$) : $f_1(x) = x$, sa dérivée est $1 = 1 \cdot x^0$. Vrai.
- Hérédité : Supposons la formule vraie au rang $n$ : $(x^n)' = n x^{n-1}$.
  Alors $x^{n+1} = x^n \cdot x$. D'après la dérivée d'un produit :
  $(x^{n+1})' = (x^n)' \cdot x + x^n \cdot (x)' = (n x^{n-1}) \cdot x + x^n \cdot 1 = n x^n + x^n = (n+1)x^n$.
  La formule est donc vraie au rang $n+1$.
- Conclusion : Par récurrence, pour tout $n \ge 1$, $(x^n)' = n x^{n-1}$.

**18.** $f(3) = 5 \iff \frac{3a + b}{3 - 2} = 5 \iff 3a + b = 5$.
Dérivée : $f'(x) = \frac{a(x-2) - (ax+b)(1)}{(x-2)^2} = \frac{ax - 2a - ax - b}{(x-2)^2} = \frac{-2a - b}{(x-2)^2}$.
En $x = 3$, $f'(3) = \frac{-2a - b}{(3-2)^2} = -2a - b = -7 \iff 2a + b = 7$.
On résout le système :
$(3a + b) - (2a + b) = 5 - 7 \iff a = -2$.
Puis $b = 5 - 3(-2) = 5 + 6 = 11$.
Donc $a = -2$ et $b = 11$.

**19.** Notons $x$ la longueur des deux côtés perpendiculaires à la falaise. Le côté parallèle à la falaise mesure alors $100 - 2x$.
L'aire est $A(x) = x(100 - 2x) = -2x^2 + 100x$, avec $x \in ]0; 50[$.
Dérivée : $A'(x) = -4x + 100$.
$A'(x) = 0 \iff 4x = 100 \iff x = 25$ mètres.
Comme $A''(x) = -4 < 0$, c'est un maximum.
L'autre côté mesure $100 - 2(25) = 50$ mètres.
L'enclos optimal fait $25\text{ m} \times 50\text{ m}$, pour une surface maximale de $1250\text{ m}^2$.

**20.**
a) Le volume d'un cylindre est $V = \pi r^2 h = 1000 \implies h = \frac{1000}{\pi r^2}$.
b) L'aire totale comprend les deux disques (haut et bas) et la paroi latérale :
$S(r) = 2(\pi r^2) + 2\pi r h = 2\pi r^2 + 2\pi r \left(\frac{1000}{\pi r^2}\right) = 2\pi r^2 + \frac{2000}{r}$.
c) Dérivons par rapport à $r$ :
$S'(r) = 4\pi r - \frac{2000}{r^2} = \frac{4\pi r^3 - 2000}{r^2}$.
Le minimum est atteint quand $S'(r) = 0 \iff 4\pi r^3 = 2000 \iff 2\pi r^3 = 1000$.
Or, comme $1000 = \pi r^2 h$, on a :
$2\pi r^3 = \pi r^2 h \iff 2r = h$.
La hauteur doit être rigoureusement égale au diamètre de la base.

**21.** Soit $M(x; x^2)$ un point de la parabole.
La distance au carré $AM^2 = (x - 0)^2 + (x^2 - 2)^2 = x^2 + x^4 - 4x^2 + 4 = x^4 - 3x^2 + 4$.
Posons $g(x) = x^4 - 3x^2 + 4$.
Dérivée : $g'(x) = 4x^3 - 6x = 2x(2x^2 - 3)$.
Racines : $x = 0$ ou $x^2 = \frac{3}{2} \iff x = \pm \sqrt{\frac{3}{2}}$.
En $x = 0$, $g(0) = 4$ (distance 2).
En $x = \pm \sqrt{\frac{3}{2}}$, $g = \frac{9}{4} - \frac{9}{2} + 4 = \frac{7}{4}$, d'où distance $\sqrt{7}/2 \approx 1{,}32 < 2$.
Les points les plus proches sont $M_1\left(\sqrt{\frac{3}{2}}; \frac{3}{2}\right)$ et $M_2\left(-\sqrt{\frac{3}{2}}; \frac{3}{2}\right)$.
Le vecteur $\vec{AM_1} = \begin{pmatrix} \sqrt{3/2} \\ -1/2 \end{pmatrix}$.
La pente de la tangente en ce point est $f'(x) = 2x = 2\sqrt{3/2}$, donc un vecteur directeur de la tangente est $\vec{u}\begin{pmatrix} 1 \\ 2\sqrt{3/2} \end{pmatrix}$.
Produit scalaire : $\vec{AM_1} \cdot \vec{u} = \sqrt{\frac{3}{2}} \times 1 + \left(-\frac{1}{2}\right) \times 2\sqrt{\frac{3}{2}} = \sqrt{\frac{3}{2}} - \sqrt{\frac{3}{2}} = 0$.
Le vecteur est orthogonal à la tangente : le plus court chemin est perpendiculaire à la courbe.

**22.**
a) Si $x \ge 0$, $f(x) = x(x) = x^2$. Si $x < 0$, $f(x) = x(-x) = -x^2$.
b) Taux d'accroissement en 0 : $\frac{f(h) - f(0)}{h} = \frac{h|h|}{h} = |h|$.
Quand $h \to 0$, $|h| \to 0$ que $h$ soit positif ou négatif !
Donc $f$ est dérivable en 0 et $f'(0) = 0$.
c) Contrairement aux idées reçues, la présence d'une valeur absolue ne crée pas forcément de point anguleux : ici, le facteur $x$ « adoucit » la pointe en la forçant à adopter une tangente horizontale plate.

**23.** Soit $y = mx + p$ une telle tangente commune.
Elle est tangente à $y = x^2$ au point d'abscisse $a$ : donc $m = 2a$ et $p = a^2 - 2a(a) = -a^2$.
Elle est tangente à $y = -x^2 + 4x - 6$ au point d'abscisse $b$ :
donc $m = -2b + 4$ et $p = (-b^2 + 4b - 6) - (-2b + 4)b = b^2 - 6$.
On égale les pentes et les ordonnées à l'origine :
1) $2a = -2b + 4 \iff a + b = 2 \iff b = 2 - a$.
2) $-a^2 = b^2 - 6$.
En remplaçant $b$ : $-a^2 = (2 - a)^2 - 6 = 4 - 4a + a^2 - 6 = a^2 - 4a - 2$.
$2a^2 - 4a - 2 = 0 \iff a^2 - 2a - 1 = 0$.
$\Delta = 4 - 4(-1) = 8 = (2\sqrt{2})^2$.
$a = \frac{2 \pm 2\sqrt{2}}{2} = 1 \pm \sqrt{2}$.
Il existe deux tangentes communes. Pour $a = 1 + \sqrt{2}$, $m = 2 + 2\sqrt{2}$ et $p = -(1+\sqrt{2})^2 = -3 - 2\sqrt{2}$. L'autre s'obtient avec $a = 1 - \sqrt{2}$.

**24.**
a) Distance sur le sable : $d_1 = \sqrt{x^2 + a^2}$. Temps sur le sable : $t_1 = \frac{\sqrt{x^2 + a^2}}{v_1}$.
Distance dans l'eau : $d_2 = \sqrt{(d - x)^2 + b^2}$. Temps dans l'eau : $t_2 = \frac{\sqrt{(d - x)^2 + b^2}}{v_2}$.
Temps total : $T(x) = \frac{\sqrt{x^2 + a^2}}{v_1} + \frac{\sqrt{(d - x)^2 + b^2}}{v_2}$.
b) Dérivée de $\sqrt{x^2+a^2}$ : $\frac{2x}{2\sqrt{x^2+a^2}} = \frac{x}{\sqrt{x^2+a^2}}$.
Dérivée de $\sqrt{(d-x)^2+b^2}$ : $\frac{-2(d-x)}{2\sqrt{(d-x)^2+b^2}} = -\frac{d-x}{\sqrt{(d-x)^2+b^2}}$.
Donc $T'(x) = \frac{x}{v_1 \sqrt{x^2 + a^2}} - \frac{d - x}{v_2 \sqrt{(d - x)^2 + b^2}}$.
Remarquons géométriquement que $\frac{x}{\sqrt{x^2+a^2}} = \sin\theta_1$ et $\frac{d-x}{\sqrt{(d-x)^2+b^2}} = \sin\theta_2$ (angles par rapport à la normale à la plage).
Le temps est minimal quand $T'(x) = 0 \iff \frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$.
C'est la loi de réfraction de Fermat-Descartes : la lumière minimise son temps de trajet !

**25.** Le skieur part de l'altitude 0 en $a$ et revient à l'altitude 0 en $b$.
S'il est resté sur du plat tout le long ($f$ constante), la pente a été nulle partout.
S'il a grimpé, il a dû monter, atteindre un point culminant (un maximum), puis redescendre. Au sommet exact de la colline, son ski s'est nécessairement retrouvé à l'horizontale ($f'(c) = 0$).
S'il a plongé dans un vallon, il a atteint un point le plus bas (un minimum) avant de remonter : au fond du vallon, le ski a également été horizontal ($f'(c) = 0$).
Dans tous les cas, il existe nécessairement au moins un point où la tangente est parfaitement horizontale.

---

### La question qui ouvre la suite

Nous avons vu que la dérivée mesure la vitesse à laquelle une fonction grandit.
Pour un polynôme, la dérivée baisse le degré. Mais imagine une population vivante : une colonie de bactéries dans une boîte de Pétri. Plus la colonie est grande, plus il y a d'individus qui se divisent, et plus la vitesse de multiplication est grande !
Existe-t-il dans tout l'univers une fonction magique qui est **rigoureusement égale à sa propre dérivée** : $f' = f$ ? Une fonction dont la pente sous les pieds est à chaque milliseconde égale à son altitude ? C'est le mystère de l'**exponentielle**, au chapitre suivant.
