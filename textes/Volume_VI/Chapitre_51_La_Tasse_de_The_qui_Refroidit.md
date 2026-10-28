# VOLUME VI — L'Âge du Flux et de la Vitesse (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 51 : La Tasse de Thé qui Refroidit

> *« La nature ne nous livre pas les trajectoires déjà tracées ; elle nous donne seulement des lois locales qui relient l'état présent à la vitesse de son changement. Tout le reste est équation différentielle. »*
> — Henri Poincaré

---

### Ce que tu vas découvrir

- Pourquoi la plupart des lois fondamentales de la physique, de la biologie et de l'économie ne donnent pas directement la formule de ce qui arrive, mais **la relation entre une grandeur et sa vitesse de variation**.
- La loi phénoménologique du **refroidissement de Newton** (1701) : pourquoi ton café chaud refroidit très vite au début, puis de plus en plus lentement.
- L'équation différentielle linéaire homogène **$y' = ay$** : sa démonstration rigoureuse et ses solutions $y(t) = C e^{at}$.
- L'équation différentielle avec second membre constant **$y' = ay + b$** : la décomposition en *solution générale de l'équation homogène + solution particulière constante* : $y(t) = C e^{at} - \dfrac{b}{a}$.
- Le problème de Cauchy et la **condition initiale** $y(t_0) = y_0$ garantissant l'unicité de la trajectoire.
- Les grands modèles du monde réel : radioactivité, circuit RC en électronique, vitesse limite d'un parachutiste, modèles de population.
- La **méthode d'Euler** pas à pas : comment une machine résout numériquement n'importe quelle équation différentielle avec un script **Python**.

---

### 1. Le problème : la tasse de thé fumante sur la table

#### 1.1 L'observation d'Isaac Newton (1701)

Imagine une tasse de thé que l'on vient de verser, bouillante à $90^\circ\text{C}$, posée sur une table dans une cuisine où l'air ambiant est à $20^\circ\text{C}$.
Au bout d'une minute, la température a baissé de $10^\circ\text{C}$ : elle est à $80^\circ\text{C}$.
Au bout de deux minutes, sera-t-elle à $70^\circ\text{C}$ ? Au bout de neuf minutes, sera-t-elle à $0^\circ\text{C}$ ? Et au bout d'un quart d'heure, le thé va-t-il se transformer en glaçon ?

Évidemment non ! Chacun sait d'expérience que :
- Quand le thé est très chaud, il fume abondamment et refroidit à toute allure ;
- Quand le thé est tiède (par exemple $25^\circ\text{C}$), il ne perd qu'une fraction de degré par minute ;
- Il ne deviendra jamais plus froid que la pièce : sa température va s'approcher indéfiniment des $20^\circ\text{C}$ de la pièce sans jamais descendre en dessous.

En **1701**, **Isaac Newton** publie anonymement un court mémoire dans les *Philosophical Transactions of the Royal Society* intitulé *Scala graduum caloris* (« Échelle des degrés de chaleur »). Il y énonce une loi expérimentale universelle :

> **La loi de refroidissement de Newton —**
> La vitesse à laquelle un corps chaud perd sa chaleur par contact avec le milieu ambiant est **proportionnelle à l'écart de température** entre ce corps et le milieu environnant.

```
       Température T(t)
            ▲
      90°C  ┼ *
            │   \   Forte pente : refroidissement très rapide
            │     \
      50°C  ┼       '--.
            │           '--.   Pente faible : refroidissement ralenti
      20°C  ┼ - - - - - - - - - - - - - - - - -  Température ambiante Text
            │                                  (Asymptote horizontale)
         0  └──────────────────────────────────────► Temps t
```

#### 1.2 La traduction en équation mathématique

Notons $T(t)$ la température du thé à l'instant $t$.
La « vitesse à laquelle la température varie » à chaque instant, c'est très exactement le taux de variation instantané, c'est-à-dire **la dérivée $T'(t)$**.
L'écart avec la température ambiante $T_{\text{ext}}$ est la différence $T(t) - T_{\text{ext}}$.
La loi de Newton s'écrit donc en une seule ligne :
$$T'(t) = -k \big(T(t) - T_{\text{ext}}\big)$$
où $k > 0$ est une constante positive dépendant de la forme de la tasse, de la matière (porcelaine, métal) et de l'agitation de l'air. Le signe « $-$ » indique qu'il s'agit d'un refroidissement ($T'(t) < 0$ lorsque $T(t) > T_{\text{ext}}$).

En développant, on obtient :
$$T'(t) = -k T(t) + k T_{\text{ext}}.$$

C'est une **équation différentielle** : l'inconnue n'est pas un nombre $x$, mais **une fonction entière $t \mapsto T(t)$**, et l'équation relie cette fonction inconnue à sa propre dérivée !

---

### 2. L'équation différentielle homogène : $y' = ay$

#### 2.1 Définition et intuition

> **📐 Définition —**
> Soit $a$ un nombre réel fixé. L'équation différentielle :
> $$(E_0) : \quad y' = ay$$
> est appelée **équation différentielle linéaire homogène du premier ordre à coefficients constants**.
> Une solution de $(E_0)$ sur un intervalle $I$ est une fonction $f$ dérivable sur $I$ telle que pour tout $t \in I$ :
> $$f'(t) = a f(t).$$

**Ce que cela signifie :** On cherche une fonction dont la dérivée est proportionnelle à la fonction elle-même.
Connais-tu une fonction qui est égale à sa propre dérivée ? Oui ! C'est la fonction exponentielle : $(e^t)' = e^t$.
Et si l'on prend $y(t) = e^{at}$, la formule de dérivation d'une composée donne $(e^{at})' = a e^{at} = a y(t)$ !
Si l'on multiplie par n'importe quelle constante réelle $C$, la linéarité de la dérivation assure que $(C e^{at})' = C (a e^{at}) = a (C e^{at})$.
Toutes les fonctions de la forme $t \mapsto C e^{at}$ sont donc des solutions. Y en a-t-il d'autres ? La réponse est non.

#### 2.2 Théorème fondamental et démonstration

> **📐 Théorème (exigible au baccalauréat) —**
> Soit $a \in \mathbb{R}$.
> Les solutions sur $\mathbb{R}$ de l'équation différentielle $y' = ay$ sont les fonctions de la forme :
> $$y(t) = C e^{at}$$
> où $C$ est une constante réelle arbitraire.

> **✍️ Démonstration rigoureuse —**
> La démonstration se fait en deux étapes : existence puis unicité de la forme.
> 1. **Vérification :** Soit $C \in \mathbb{R}$. Posons $f(t) = C e^{at}$.
>    La fonction $f$ est dérivable sur $\mathbb{R}$, et pour tout $t \in \mathbb{R}$ :
>    $$f'(t) = C \times (a e^{at}) = a (C e^{at}) = a f(t).$$
>    Ainsi, toute fonction de la forme $C e^{at}$ est bien solution de $(E_0)$.
>
> 2. **Réciproque (unicité) :** Soit $g$ une solution quelconque de $y' = ay$ sur $\mathbb{R}$.
>    On sait donc que pour tout $t \in \mathbb{R}$, $g'(t) = a g(t)$.
>    Considérons la fonction auxiliaire $\varphi$ définie sur $\mathbb{R}$ par :
>    $$\varphi(t) = g(t) e^{-at}.$$
>    La fonction $\varphi$ est dérivable sur $\mathbb{R}$ comme produit de fonctions dérivables. Calculons sa dérivée à l'aide de la règle $(uv)' = u'v + uv'$ :
>    $$\varphi'(t) = g'(t) e^{-at} + g(t) (-a e^{-at}) = \big(g'(t) - a g(t)\big) e^{-at}.$$
>    Or, puisque $g$ est solution de $y' = ay$, on a $g'(t) - a g(t) = 0$ pour tout réel $t$ !
>    On en déduit :
>    $$\varphi'(t) = 0 \times e^{-at} = 0.$$
>    La dérivée de $\varphi$ est **identiquement nulle sur l'intervalle $\mathbb{R}$**.
>    Par conséquent, la fonction $\varphi$ est **constante** sur $\mathbb{R}$ : il existe une constante réelle $C$ telle que pour tout $t \in \mathbb{R}$ :
>    $$\varphi(t) = C \iff g(t) e^{-at} = C.$$
>    En multipliant les deux membres par $e^{at}$ (qui n'est jamais nul) :
>    $$g(t) = C e^{at}.$$
>    Toute solution est donc nécessairement de la forme $C e^{at}$. $\blacksquare$

#### 2.3 Unicité sous condition initiale : le problème de Cauchy

L'équation $y' = ay$ admet une infinité de solutions (une pour chaque valeur de la constante $C$). Graphiquement, cela donne toute une famille de courbes qui ne se coupent jamais :

```
       y ▲                     C = 2
         │                    /
         │      C = 1       /
         │        /       /
       1 ┼ - - - * - - - /
         │     /       /
       0 ┼───/───────/────────► t
         │  /
      -1 ┼ * C = -1
         │  \
```

Pour fixer la valeur de $C$ et déterminer l'unique trajectoire physique suivie par le système, il faut connaître **l'état initial** à un instant $t_0$.

> **📐 Théorème d'existence et d'unicité (Problème de Cauchy) —**
> Pour tous réels $t_0$ et $y_0$, l'équation différentielle $y' = ay$ admet **une unique solution** $f$ vérifiant la condition initiale :
> $$f(t_0) = y_0.$$
> Cette solution est donnée pour tout $t \in \mathbb{R}$ par :
> $$f(t) = y_0 \, e^{a(t - t_0)}.$$

> **✍️ Justification —**
> Les solutions sont de la forme $f(t) = C e^{at}$.
> La condition initiale s'écrit :
> $$f(t_0) = y_0 \iff C e^{a t_0} = y_0 \iff C = y_0 e^{-a t_0}.$$
> L'expression de la fonction devient alors :
> $$f(t) = (y_0 e^{-a t_0}) e^{at} = y_0 \, e^{a(t - t_0)}.$$
> La constante $C$ étant uniquement déterminée, la solution est unique. $\blacksquare$

> **Exemple résolu 1 — Décroissance radioactive.**
> Un échantillon d'iode 131 contient initialement $N_0 = 10^8$ noyaux radioactifs à $t = 0$.
> Le nombre de noyaux $N(t)$ obéit à l'équation différentielle $N'(t) = -0{,}0866 N(t)$ (le temps $t$ étant exprimé en jours).
> 1. Déterminer l'expression de $N(t)$.
> 2. Calculer le nombre de noyaux restants au bout de 8 jours.
>
> *Résolution :*
> 1. C'est l'équation $y' = ay$ avec $a = -0{,}0866$.
>    Les solutions sont $N(t) = C e^{-0{,}0866 t}$.
>    Condition initiale : $N(0) = C e^0 = C = 10^8$.
>    Donc $N(t) = 10^8 e^{-0{,}0866 t}$.
> 2. Pour $t = 8$ jours :
>    $N(8) = 10^8 e^{-0{,}0866 \times 8} = 10^8 e^{-0{,}6928} \approx 10^8 \times 0{,}50017 \approx 5 \times 10^7$ noyaux.
>    (La moitié de l'échantillon s'est désintégrée : la demi-vie de l'iode 131 est d'environ 8 jours !).

---

### 3. L'équation avec second membre : $y' = ay + b$

Dans la réalité, les phénomènes ne s'éteignent pas toujours vers zéro : la tasse de thé ne descend pas à $0^\circ\text{K}$, elle se stabilise à la température ambiante $20^\circ\text{C}$ ; un condensateur ne se charge pas vers l'infini, il se charge vers la tension du générateur $E$.
L'équation s'écrit alors avec un terme constant :
$$(E) : \quad y' = ay + b \quad (a \neq 0).$$

#### 3.1 La recherche d'une solution constante particulière

Cherchons s'il existe une solution constante $y(t) = k$ (avec $k \in \mathbb{R}$) à cette équation.
Puisque $y$ est constante, sa dérivée est nulle : $y'(t) = 0$.
L'équation devient :
$$0 = ak + b \iff ak = -b \iff k = -\dfrac{b}{a}.$$

> **La solution particulière constante de $y' = ay + b$ est :**
> $$y_p(t) = -\dfrac{b}{a}.$$
> On l'appelle souvent **l'état d'équilibre** ou le régime permanent du système.

#### 3.2 Théorème de structure des solutions

> **📐 Théorème (Résolution générale de $y' = ay + b$) —**
> Soient $a \neq 0$ et $b$ deux nombres réels.
> Les solutions sur $\mathbb{R}$ de l'équation différentielle $y' = ay + b$ sont les fonctions :
> $$y(t) = C e^{at} - \dfrac{b}{a}$$
> où $C$ est une constante réelle arbitraire.

> **✍️ Démonstration (exigible) —**
> Notons $(E) : y' = ay + b$ et $(E_0) : y' = ay$ l'équation homogène associée.
> Posons $y_p(t) = -\dfrac{b}{a}$. On sait que $y'_p = 0 = a y_p + b$, donc $y_p$ est une solution particulière de $(E)$.
> 
> Soit $f$ une fonction dérivable sur $\mathbb{R}$.
> Démontrons que :
> $$f \text{ est solution de } (E) \iff f - y_p \text{ est solution de } (E_0).$$
> 
> En effet :
> - $(f - y_p)' = f' - y'_p = f' - 0 = f'$.
> - D'autre part, $a(f - y_p) = af - ay_p = af - a\left(-\dfrac{b}{a}\right) = af + b$.
> 
> Ainsi :
> $$(f - y_p)' = a(f - y_p) \iff f' = af + b.$$
> 
> Cela signifie que la différence $f - y_p$ est une solution de l'équation homogène $y' = ay$.
> D'après le théorème de la section 2.2, il existe donc une constante $C \in \mathbb{R}$ telle que :
> $$(f - y_p)(t) = C e^{at} \iff f(t) = C e^{at} + y_p(t) \iff f(t) = C e^{at} - \dfrac{b}{a}.$$
> $\blacksquare$

> **🧭 Le principe fondamental de superposition :**
> $$\text{Solution Générale de } (E) = \underbrace{C e^{at}}_{\text{Solution générale de l'homogène}} + \underbrace{\left(-\dfrac{b}{a}\right)}_{\text{Solution particulière constante}}$$

#### 3.3 Condition initiale pour $y' = ay + b$

Pour déterminer $C$ à partir d'une condition initiale $y(t_0) = y_0$ :
$$y(t_0) = y_0 \iff C e^{a t_0} - \dfrac{b}{a} = y_0 \iff C e^{a t_0} = y_0 + \dfrac{b}{a} \iff C = \left(y_0 + \dfrac{b}{a}\right) e^{-a t_0}.$$
En réinjectant :
$$y(t) = \left(y_0 + \dfrac{b}{a}\right) e^{a(t - t_0)} - \dfrac{b}{a}.$$

> **Exemple résolu 2 — La tasse de thé résolue.**
> Reprenons notre thé à $90^\circ\text{C}$ dans une pièce à $20^\circ\text{C}$.
> L'équation est $T'(t) = -0{,}1 T(t) + 2$ (avec $t$ en minutes).
> 1. Déterminer la solution générale de l'équation.
> 2. Déterminer l'unique solution vérifiant $T(0) = 90$.
> 3. Quelle sera la température du thé au bout de 20 minutes ?
> 4. Au bout de combien de temps le thé sera-t-il buvable, c'est-à-dire à $45^\circ\text{C}$ ?
>
> *Résolution pas à pas :*
> 1. C'est l'équation $y' = ay + b$ avec $a = -0{,}1$ et $b = 2$.
>    La constante d'équilibre est $-\dfrac{b}{a} = -\dfrac{2}{-0{,}1} = 20$.
>    Les solutions générales sont :
>    $$T(t) = C e^{-0{,}1 t} + 20.$$
> 2. Condition initiale $T(0) = 90$ :
>    $$T(0) = C e^0 + 20 = 90 \iff C + 20 = 90 \iff C = 70.$$
>    La température du thé à l'instant $t$ est donc :
>    $$T(t) = 70 e^{-0{,}1 t} + 20.$$
> 3. Au bout de 20 minutes :
>    $$T(20) = 70 e^{-0{,}1 \times 20} + 20 = 70 e^{-2} + 20 \approx 70 \times 0{,}1353 + 20 \approx 9{,}47 + 20 = 29{,}5^\circ\text{C}.$$
> 4. On cherche $t$ tel que $T(t) = 45$ :
>    $$70 e^{-0{,}1 t} + 20 = 45 \iff 70 e^{-0{,}1 t} = 25 \iff e^{-0{,}1 t} = \dfrac{25}{70} = \dfrac{5}{14}.$$
>    En appliquant la fonction $\ln$ (chapitre 48) :
>    $$-0{,}1 t = \ln\left(\dfrac{5}{14}\right) = -\ln\left(\dfrac{14}{5}\right) \iff t = 10 \ln(2{,}8) \approx 10 \times 1{,}0296 \approx 10{,}3\text{ minutes}.$$
>    Le thé sera buvable au bout d'environ 10 minutes et 18 secondes.

---

### 4. Les grands modèles du monde réel

#### 4.1 La charge d'un condensateur (circuit RC)

Dans un circuit électrique comprenant un générateur de tension constante $E$, une résistance $R$ et un condensateur de capacité $C$ montés en série, la loi des mailles s'écrit :
$$u_R(t) + u_C(t) = E.$$
Or la loi d'Ohm donne $u_R = R i(t)$ et le courant traversant le condensateur est $i(t) = C \dfrac{du_C}{dt}$.
On obtient l'équation différentielle :
$$R C \dfrac{du_C}{dt} + u_C(t) = E \iff u'_C(t) = -\dfrac{1}{RC} u_C(t) + \dfrac{E}{RC}.$$

Posons $\tau = RC$ (la **constante de temps** du circuit, exprimée en secondes). L'équation devient :
$$u'_C(t) = -\dfrac{1}{\tau} u_C(t) + \dfrac{E}{\tau}.$$
Avec la condition initiale d'un condensateur initialement déchargé ($u_C(0) = 0$), la solution est :
$$u_C(t) = E \left(1 - e^{-t/\tau}\right).$$

```
       u_C(t) ▲
            E ┼ - - - - - - - - - - - - - - - - - -  Tension max E
              │                      ..-------''
              │                 _--''
        0,63E ┼ - - - - - - - *
              │           _--'¦
              │        .-'    ¦
            0 └───────*───────┴────────────────────► Temps t
                      0       τ
```

> **Propriété remarquable de la constante de temps $\tau$ :**
> À $t = \tau$, la tension vaut $u_C(\tau) = E(1 - e^{-1}) \approx E(1 - 0{,}368) = 0{,}632 E$.
> Le condensateur est chargé à **$63{,}2\,\%$**.
> À $t = 3\tau$, il est chargé à $95\,\%$. À $t = 5\tau$, il est chargé à $99{,}3\,\%$ (charge quasi-totale).

#### 4.2 La chute d'un corps avec frottement fluide (vitesse limite)

Un parachutiste de masse $m$ saute d'un avion. Il est soumis à son poids $P = mg$ (vers le bas) et aux frottements de l'air proportionnels à sa vitesse $F = -k v$ (vers le haut).
La deuxième loi de Newton ($m a = \sum F$) donne :
$$m v'(t) = mg - k v(t) \iff v'(t) = -\dfrac{k}{m} v(t) + g.$$

C'est une équation de la forme $y' = ay + b$ avec $a = -\dfrac{k}{m}$ et $b = g$.
La solution constante d'équilibre est la **vitesse limite** $v_{\text{lim}}$ :
$$v_{\text{lim}} = -\dfrac{b}{a} = -\dfrac{g}{-k/m} = \dfrac{mg}{k}.$$
Si le parachutiste s'élance avec une vitesse initiale nulle $v(0) = 0$, sa vitesse à chaque seconde est :
$$v(t) = \dfrac{mg}{k} \left(1 - e^{-\frac{k}{m}t}\right).$$
Le parachutiste accélère d'abord sous l'effet de la pesanteur, puis la résistance de l'air équilibre le poids : sa vitesse plafonne à $v_{\text{lim}}$.

---

### 5. La méthode d'Euler : résoudre quand on ne sait pas intégrer

Dans le monde réel, beaucoup d'équations différentielles sont non linéaires (par exemple $y' = y^2 - t$ ou $y' = \sin(yt)$) et ne possèdent aucune formule exacte avec des exponentielles ou des logarithmes !
Comment les ingénieurs de la NASA ou les climatologues prédisent-ils l'avenir de ces systèmes ?
Grâce à une idée géométrique géniale due à **Leonhard Euler** en 1768 : **remplacer la courbe inconnue par une suite de petits segments de tangentes**.

#### 5.1 Le principe géométrique

Soit l'équation différentielle $y' = f(t, y)$ avec la condition initiale $y(t_0) = y_0$.
On choisit un petit pas de temps $h > 0$.
1. **Au point de départ $(t_0\,; y_0)$ :**
   La pente de la tangente est connue grâce à l'équation différentielle :
   $$\text{Pente} = y'(t_0) = f(t_0, y_0).$$
2. **Pour avancer d'un pas $h$ :**
   On suit cette droite tangente pendant une durée $h$. L'abscisse devient $t_1 = t_0 + h$.
   La nouvelle ordonnée approchée $y_1$ est donnée par l'approximation affine :
   $$y_1 = y_0 + h \times y'(t_0) = y_0 + h \times f(t_0, y_0).$$
3. **On recommence depuis $(t_1\,; y_1)$ :**
   On recalcule la nouvelle pente $f(t_1, y_1)$ et on avance d'un nouveau pas $h$ :
   $$y_{n+1} = y_n + h \times f(t_n, y_n) \quad \text{avec} \quad t_{n+1} = t_n + h.$$

```
       y ▲                                           Vraie courbe y(t)
         │                                       ..---*---..
         │                                 _--''     /
         │                           *---''         /
         │                     *---''              /
         │               *---''                   /  Segments d'Euler (pas h)
       y₀┼─────────*---''
         │         │
       0 └─────────┴───────┴───────┴───────┴───────► t
                   t₀      t₁      t₂      t₃
                   |<- h ->|
```

Plus le pas $h$ est choisi petit ($h = 0{,}01$, $h = 0{,}001$), plus la ligne brisée se rapproche de la courbe exacte !

#### 5.2 Script Python de la méthode d'Euler

Voici le programme officiel Python implémentant la méthode d'Euler pour résoudre $y' = -2y$ avec $y(0) = 1$ sur $[0\,; 2]$, et comparant le résultat avec la solution théorique exacte $y(t) = e^{-2t}$ :

```python
import math

def methode_euler(a, b, y0, n):
    """
    Résout y' = -2y sur [a, b] avec y(a) = y0 en n étapes.
    """
    h = (b - a) / n
    t = a
    y = y0
    resultats = [(t, y, math.exp(-2 * t))]
    
    for _ in range(n):
        # Pente calculée d'après l'équation différentielle y' = -2y
        pente = -2 * y
        y = y + h * pente
        t = t + h
        y_exact = math.exp(-2 * t)
        resultats.append((round(t, 4), round(y, 4), round(y_exact, 4)))
    
    return resultats

# Exécution avec 10 pas de h = 0.2
points = methode_euler(0, 2, 1.0, 10)
print(f"{'t':<6} | {'y_Euler':<10} | {'y_Exact':<10} | {'Erreur':<10}")
print("-" * 42)
for t_val, y_e, y_ex in points:
    err = abs(y_e - y_ex)
    print(f"{t_val:<6} | {y_e:<10} | {y_ex:<10} | {err:<10.4f}")
```

---

### Ce qu'il faut retenir

#### 1. L'équation différentielle linéaire $y' = ay$
- Les solutions sur $\mathbb{R}$ sont de la forme :
  $$y(t) = C e^{at} \quad (C \in \mathbb{R}).$$
- Si $a > 0$, les solutions tendent vers $\pm\infty$ quand $t \to +\infty$ (croissance exponentielle explosive).
- Si $a < 0$, les solutions tendent vers $0$ quand $t \to +\infty$ (décroissance exponentielle vers l'équilibre).
- Condition initiale : pour $y(t_0) = y_0$, l'unique solution est $y(t) = y_0 e^{a(t - t_0)}$.

#### 2. L'équation avec second membre constant $y' = ay + b$ ($a \neq 0$)
- Solution générale :
  $$y(t) = C e^{at} - \dfrac{b}{a}.$$
- Le terme $-\dfrac{b}{a}$ est la **solution particulière constante**, représentant la valeur d'équilibre à long terme (asymptote horizontale lorsque $a < 0$).

#### 3. Équation avec second membre variable $y' = ay + f(t)$
- Pour résoudre $y' = ay + f(t)$, on cherche une solution particulière $y_p(t)$ (souvent de même nature que $f$ : polynôme si $f$ est polynomiale, exponentielle si $f$ est exponentielle), puis la solution générale est $y(t) = C e^{at} + y_p(t)$.

#### 4. La méthode d'Euler
- Algorithme de pas $h$ :
  $$t_{n+1} = t_n + h \quad \text{et} \quad y_{n+1} = y_n + h \times y'(t_n).$$

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 51.1 —** Équations homogènes simples.
Résoudre sur $\mathbb{R}$ les équations différentielles suivantes :
1. $y' = 3y$
2. $y' = -5y$
3. $2y' + 6y = 0$
4. $4y' - y = 0$

**Exercice 51.2 —** Conditions initiales pour $y' = ay$.
Déterminer l'unique solution vérifiant la condition initiale donnée :
1. $y' = 2y$ avec $y(0) = 7$
2. $y' = -3y$ avec $y(0) = -4$
3. $y' = 0{,}5y$ avec $y(2) = 10$
4. $y' = -y$ avec $y(1) = e$

**Exercice 51.3 —** Équations avec second membre constant $y' = ay + b$.
Résoudre sur $\mathbb{R}$ :
1. $y' = -2y + 6$
2. $y' = 4y - 8$
3. $3y' + 9y = 18$
4. $y' = -0{,}2y + 5$

**Exercice 51.4 —** Conditions initiales pour $y' = ay + b$.
1. Résoudre $y' = -y + 3$ avec $y(0) = 1$.
2. Résoudre $y' = 2y - 10$ avec $y(0) = 5$.
3. Résoudre $2y' + y = 4$ avec $y(0) = 0$.

**Exercice 51.5 —** Détermination de l'asymptote.
Soit $f$ une solution de l'équation $y' = -3y + 12$.
1. Déterminer l'expression générale de $f(t)$.
2. Quelle est la limite de $f(t)$ quand $t \to +\infty$ ?
3. En déduire l'équation de l'asymptote horizontale commune à toutes les courbes solutions.

**Exercice 51.6 —** Un pas de la méthode d'Euler.
Soit l'équation $y' = 2t + y$ avec $y(0) = 1$.
En appliquant la méthode d'Euler avec un pas $h = 0{,}1$, calculer les valeurs approchées $y_1 \approx y(0{,}1)$ et $y_2 \approx y(0{,}2)$.

---

#### Niveau ★★ (Réflexion et Baccalauréat)

**Exercice 51.7 —** La tasse de café de l'inspecteur (Scène de crime).
Un corps sans vie est découvert dans une pièce maintenue à une température constante de $20^\circ\text{C}$.
À 14h00, le médecin légiste mesure la température du corps : elle est de $30^\circ\text{C}$.
À 15h00, il mesure à nouveau la température : elle est descendue à $28^\circ\text{C}$.
On suppose que le refroidissement obéit à la loi de Newton : $T'(t) = -k(T(t) - 20)$, et que la température d'une personne vivante est de $37^\circ\text{C}$.
1. En prenant $t = 0$ à 14h00, exprimer la température $T(t)$ en fonction de $t$ et de la constante $k$.
2. À l'aide de la mesure effectuée à 15h00 ($t = 1$), déterminer la valeur exacte puis approchée de $k$.
3. Déterminer l'heure exacte du décès de la victime.

**Exercice 51.8 —** Décharge d'un condensateur à travers une résistance.
Un condensateur de capacité $C = 50\,\mu\text{F}$ chargé sous une tension $U_0 = 12\text{ V}$ est déconnecté puis branché aux bornes d'un résistor de résistance $R = 20\,\text{k}\Omega$.
1. Établir l'équation différentielle vérifiée par la tension $u(t)$ aux bornes du condensateur.
2. Calculer la constante de temps $\tau = RC$.
3. Résoudre l'équation et donner l'expression de $u(t)$.
4. Au bout de combien de temps la tension devient-elle inférieure à $1\text{ V}$ ?

**Exercice 51.9 —** Perfusion d'un médicament dans le sang (Type Bac).
On administre à un patient un antibiotique par perfusion intraveineuse continue à débit constant.
La quantité de médicament $q(t)$ présente dans le sang (en milligrammes) à l'instant $t$ (en heures) vérifie l'équation :
$$q'(t) = -0{,}15 q(t) + 30.$$
Au début de la perfusion ($t = 0$), le patient n'a aucun médicament dans l'organisme : $q(0) = 0$.
1. Résoudre cette équation différentielle et déterminer l'expression de $q(t)$.
2. Étudier le sens de variation de $q$ sur $[0\,; +\infty[$.
3. Déterminer la limite de $q(t)$ quand $t \to +\infty$. Quelle est la quantité maximale que l'organisme atteindra à long terme ?
4. Le traitement n'est efficace que lorsque la quantité de médicament dépasse $150\text{ mg}$. Au bout de combien de temps ce seuil d'efficacité est-il atteint ?

**Exercice 51.10 —** Équation avec second membre affine $y' = ay + f(t)$.
On considère l'équation différentielle :
$$(E) : \quad y' - 2y = 4x - 6.$$
1. Déterminer deux réels $m$ et $p$ tels que la fonction affine $y_p(x) = mx + p$ soit une solution particulière de $(E)$.
2. Résoudre l'équation homogène $(E_0) : y' - 2y = 0$.
3. En déduire l'ensemble des solutions de l'équation $(E)$.
4. Déterminer l'unique solution $f$ vérifiant la condition $f(0) = 1$.

**Exercice 51.11 —** Équation avec second membre trigonométrique.
Soit l'équation différentielle $(E) : y' + y = \cos x + \sin x$.
1. Montrer que la fonction $g(x) = \sin x$ est une solution particulière de $(E)$.
2. En déduire la solution générale de $(E)$.
3. Déterminer la solution vérifiant $y(0) = 2$.

**Exercice 51.12 —** Vitesse limite d'une goutte de pluie.
Une goutte de pluie de masse $m = 4 \times 10^{-5}\text{ kg}$ tombe verticalement d'un nuage sans vitesse initiale. Elle subit la pesanteur ($g = 9{,}81\text{ m}\cdot\text{s}^{-2}$) et une force de frottement de l'air proportionnelle à sa vitesse : $F = -k v$ avec $k = 5 \times 10^{-5}\text{ kg}\cdot\text{s}^{-1}$.
1. Écrire l'équation différentielle vérifiée par la vitesse $v(t)$.
2. Déterminer la vitesse limite $v_{\text{lim}}$ de la goutte.
3. Résoudre l'équation différentielle pour exprimer $v(t)$ en fonction de $t$.
4. Calculer la durée nécessaire pour que la goutte atteigne $99\,\%$ de sa vitesse limite.

**Exercice 51.13 —** Tangente commune et raccordement.
On considère l'équation $y' = -2y + 4$.
1. Résoudre cette équation.
2. Existe-t-il une courbe solution dont la tangente au point d'abscisse 0 passe par le point $A(1\,; 0)$ ? Si oui, déterminer cette solution.

---

#### Niveau ★★★ (Approfondissement et Défis)

**Exercice 51.14 —** Modèle logistique de Verhulst (dynamique des populations).
Le modèle malthusien $y' = ay$ prédit une population qui explose vers l'infini, ce qui est impossible dans un milieu aux ressources limitées.
En 1838, **Pierre-François Verhulst** propose l'équation différentielle logistique :
$$(E_L) : \quad y' = a y \left(1 - \dfrac{y}{K}\right)$$
où $K > 0$ est la capacité de charge maximale de l'environnement, et $a > 0$ le taux intrinsèque de croissance.
Soit $y$ une solution ne s'annulant pas et bornée entre 0 et $K$. Posons la fonction $z(t) = \dfrac{1}{y(t)}$.
1. Calculer la dérivée $z'(t)$ en fonction de $y(t)$ et $y'(t)$.
2. En remplaçant $y'(t)$ par sa valeur issue de $(E_L)$, montrer que $z$ vérifie l'équation différentielle linéaire :
   $$z' + az = \dfrac{a}{K}.$$
3. Résoudre cette équation en $z(t)$.
4. En déduire l'expression explicite de la population $y(t)$ en fonction de la population initiale $y_0 = y(0)$.
5. Étudier les limites de $y(t)$ en $-\infty$ et $+\infty$. Quelle est la forme de la courbe obtenue ?

**Exercice 51.15 —** L'équation différentielle du second ordre $y'' + \omega^2 y = 0$.
Soit $\omega > 0$. On cherche toutes les fonctions deux fois dérivables sur $\mathbb{R}$ vérifiant :
$$(H) : \quad y'' + \omega^2 y = 0.$$
1. Vérifier que pour toutes constantes réelles $A$ et $B$, la fonction $y(t) = A \cos(\omega t) + B \sin(\omega t)$ est solution.
2. Soit $f$ une solution quelconque de $(H)$.
   Posons $u(t) = \omega f(t) \sin(\omega t) + f'(t) \cos(\omega t)$ et $v(t) = \omega f(t) \cos(\omega t) - f'(t) \sin(\omega t)$.
   Calculer les dérivées $u'(t)$ et $v'(t)$.
3. En déduire que $u$ et $v$ sont des fonctions constantes, et prouver ainsi que **toutes** les solutions de $(H)$ sont de la forme $A\cos(\omega t) + B\sin(\omega t)$.

**Exercice 51.16 —** Analyse d'erreur de la méthode d'Euler.
Soit l'équation $y' = y$ avec $y(0) = 1$ sur $[0\,; 1]$. La solution exacte est $y(t) = e^t$, donc $y(1) = e$.
On applique la méthode d'Euler avec $n$ sous-intervalles de pas $h = \dfrac{1}{n}$.
1. Écrire la relation de récurrence donnant $y_{k+1}$ en fonction de $y_k$.
2. En déduire l'expression de $y_n$ en fonction de $n$.
3. Retrouver ainsi la célèbre limite classique d'Euler : $\lim\limits_{n \to +\infty} \left(1 + \dfrac{1}{n}\right)^n = e$.

---

### Solutions

#### Solutions du Niveau ★

**Solution 51.1 :**
1. $y' = 3y \implies y(t) = C e^{3t}$ avec $C \in \mathbb{R}$.
2. $y' = -5y \implies y(t) = C e^{-5t}$ avec $C \in \mathbb{R}$.
3. $2y' + 6y = 0 \iff 2y' = -6y \iff y' = -3y \implies y(t) = C e^{-3t}$.
4. $4y' - y = 0 \iff 4y' = y \iff y' = \dfrac{1}{4}y \implies y(t) = C e^{t/4}$.

**Solution 51.2 :**
1. $y(t) = C e^{2t}$. Condition : $y(0) = C e^0 = C = 7$. Solution : $y(t) = 7 e^{2t}$.
2. $y(t) = C e^{-3t}$. Condition : $y(0) = C = -4$. Solution : $y(t) = -4 e^{-3t}$.
3. $y(t) = C e^{0{,}5t}$. Condition : $y(2) = C e^{0{,}5 \times 2} = C e^1 = 10 \iff C = 10 e^{-1}$.
   Solution : $y(t) = (10 e^{-1}) e^{0{,}5t} = 10 e^{0{,}5t - 1}$.
4. $y(t) = C e^{-t}$. Condition : $y(1) = C e^{-1} = e \iff C = e \times e^1 = e^2$.
   Solution : $y(t) = e^2 e^{-t} = e^{2-t}$.

**Solution 51.3 :**
Formule générale pour $y' = ay + b$ : $y(t) = C e^{at} - \dfrac{b}{a}$.
1. $a = -2, b = 6 \implies -\dfrac{b}{a} = -\dfrac{6}{-2} = 3$. Solution : $y(t) = C e^{-2t} + 3$.
2. $a = 4, b = -8 \implies -\dfrac{b}{a} = -\dfrac{-8}{4} = 2$. Solution : $y(t) = C e^{4t} + 2$.
3. $3y' = -9y + 18 \iff y' = -3y + 6 \implies -\dfrac{b}{a} = -\dfrac{6}{-3} = 2$. Solution : $y(t) = C e^{-3t} + 2$.
4. $a = -0{,}2, b = 5 \implies -\dfrac{b}{a} = -\dfrac{5}{-0{,}2} = 25$. Solution : $y(t) = C e^{-0{,}2t} + 25$.

**Solution 51.4 :**
1. $y(t) = C e^{-t} + 3$. Condition $y(0) = C + 3 = 1 \iff C = -2$. Solution : $y(t) = -2e^{-t} + 3$.
2. $y(t) = C e^{2t} + 5$. Condition $y(0) = C + 5 = 5 \iff C = 0$. Solution constante : $y(t) = 5$.
3. $y' = -0{,}5y + 2$. Solution générale : $y(t) = C e^{-0{,}5t} + 4$. Condition $y(0) = C + 4 = 0 \iff C = -4$. Solution : $y(t) = -4e^{-0{,}5t} + 4 = 4(1 - e^{-0{,}5t})$.

**Solution 51.5 :**
1. $a = -3, b = 12 \implies -\dfrac{b}{a} = 4$. Donc $f(t) = C e^{-3t} + 4$.
2. Comme $-3 < 0$, $\lim\limits_{t \to +\infty} e^{-3t} = 0$, donc pour toute constante $C$ : $\lim\limits_{t \to +\infty} f(t) = 4$.
3. La droite d'équation $y = 4$ est asymptote horizontale en $+\infty$ pour toutes les courbes solutions.

**Solution 51.6 :**
- À $t_0 = 0$, $y_0 = 1$. La dérivée est $y'(0) = 2(0) + 1 = 1$.
  $y_1 = y_0 + h \times y'(0) = 1 + 0{,}1 \times 1 = 1{,}1$ à $t_1 = 0{,}1$.
- À $t_1 = 0{,}1$, $y_1 = 1{,}1$. La dérivée approchée est $y'(0{,}1) \approx 2(0{,}1) + 1{,}1 = 0{,}2 + 1{,}1 = 1{,}3$.
  $y_2 = y_1 + h \times y'(t_1) = 1{,}1 + 0{,}1 \times 1{,}3 = 1{,}1 + 0{,}13 = 1{,}23$ à $t_2 = 0{,}2$.

---

#### Solutions du Niveau ★★

**Solution 51.7 :**
1. L'équation est $T'(t) = -k T(t) + 20k$.
   La solution générale est $T(t) = C e^{-kt} + 20$.
   À 14h00 ($t = 0$), $T(0) = 30 \implies C + 20 = 30 \iff C = 10$.
   Donc $T(t) = 10 e^{-kt} + 20$.
2. À 15h00 ($t = 1$), $T(1) = 28$ :
   $10 e^{-k \times 1} + 20 = 28 \iff 10 e^{-k} = 8 \iff e^{-k} = 0{,}8 \iff -k = \ln(0{,}8) \iff k = -\ln(0{,}8) = \ln\left(\dfrac{5}{4}\right) \approx 0{,}22314\text{ h}^{-1}$.
3. Soit $t_d$ l'heure du décès. À cet instant, la température était de $37^\circ\text{C}$ :
   $10 e^{-k t_d} + 20 = 37 \iff 10 e^{-k t_d} = 17 \iff e^{-k t_d} = 1{,}7$.
   En prenant le logarithme népérien :
   $$-k t_d = \ln(1{,}7) \iff t_d = -\dfrac{\ln(1{,}7)}{k} = -\dfrac{\ln(1{,}7)}{-\ln(0{,}8)} \approx -\dfrac{0{,}53063}{0{,}22314} \approx -2{,}378\text{ heures}.$$
   Convertissons $-2{,}378\text{ h}$ en heures et minutes :
   $0{,}378 \times 60 \approx 23\text{ minutes}$.
   Le décès a eu lieu $2\text{ heures et } 23\text{ minutes}$ avant 14h00, soit précisément à **11h37 du matin**.

**Solution 51.8 :**
1. Lors de la décharge, $u_R + u_C = 0 \iff R i + u = 0 \iff R C u'(t) + u(t) = 0 \iff u'(t) = -\dfrac{1}{RC} u(t)$.
2. $\tau = RC = 20 \times 10^3 \times 50 \times 10^{-6} = 1\,000 \times 10^{-3} = 1{,}0\text{ seconde}$.
3. L'équation est $u'(t) = -u(t)$. La solution avec $u(0) = 12\text{ V}$ est :
   $u(t) = 12 e^{-t}$.
4. $u(t) < 1 \iff 12 e^{-t} < 1 \iff e^{-t} < \dfrac{1}{12} \iff -t < -\ln 12 \iff t > \ln 12 \approx 2{,}48\text{ secondes}$.

**Solution 51.9 :**
1. C'est $y' = ay + b$ avec $a = -0{,}15$ et $b = 30$.
   Valeur d'équilibre : $-\dfrac{b}{a} = -\dfrac{30}{-0{,}15} = 200$.
   La solution générale est $q(t) = C e^{-0{,}15t} + 200$.
   Condition initiale $q(0) = 0 \implies C + 200 = 0 \iff C = -200$.
   Donc $q(t) = 200(1 - e^{-0{,}15t})$.
2. $q'(t) = -200(-0{,}15 e^{-0{,}15t}) = 30 e^{-0{,}15t} > 0$. La quantité $q(t)$ est strictement croissante sur $[0\,; +\infty[$.
3. Comme $-0{,}15 < 0$, $\lim\limits_{t \to +\infty} e^{-0{,}15t} = 0$, donc $\lim\limits_{t \to +\infty} q(t) = 200\text{ mg}$. L'organisme ne dépassera jamais $200\text{ mg}$.
4. $q(t) \geq 150 \iff 200(1 - e^{-0{,}15t}) \geq 150 \iff 1 - e^{-0{,}15t} \geq 0{,}75 \iff e^{-0{,}15t} \leq 0{,}25$.
   En appliquant $\ln$ : $-0{,}15t \leq \ln(0{,}25) = -\ln 4 \iff t \geq \dfrac{\ln 4}{0{,}15} \approx \dfrac{1{,}3863}{0{,}15} \approx 9{,}24\text{ heures}$ (soit environ 9h et 14 minutes).

**Solution 51.10 :**
1. $y_p(x) = mx + p \implies y'_p(x) = m$.
   Injectons dans $(E)$ : $m - 2(mx + p) = 4x - 6 \iff -2mx + (m - 2p) = 4x - 6$.
   Par identification des coefficients polynomiaux :
   - Pour le terme en $x$ : $-2m = 4 \iff m = -2$.
   - Pour la constante : $m - 2p = -6 \iff -2 - 2p = -6 \iff -2p = -4 \iff p = 2$.
   La fonction particulière est $y_p(x) = -2x + 2$.
2. $y' = 2y \implies y(x) = C e^{2x}$.
3. Par le principe de superposition, la solution générale de $(E)$ est :
   $y(x) = C e^{2x} - 2x + 2$ avec $C \in \mathbb{R}$.
4. Condition $f(0) = 1$ : $C e^0 - 0 + 2 = 1 \iff C + 2 = 1 \iff C = -1$.
   L'unique solution est $f(x) = -e^{2x} - 2x + 2$.

**Solution 51.11 :**
1. $g(x) = \sin x \implies g'(x) = \cos x$.
   $g'(x) + g(x) = \cos x + \sin x$. L'équation est bien vérifiée ! $g$ est solution particulière.
2. L'équation homogène associée est $y' + y = 0 \iff y' = -y$, de solution $C e^{-x}$.
   La solution générale est donc $y(x) = C e^{-x} + \sin x$.
3. $y(0) = C e^0 + \sin 0 = C = 2$. La solution est $y(x) = 2e^{-x} + \sin x$.

**Solution 51.12 :**
1. $v'(t) = -\dfrac{k}{m}v(t) + g$.
   Calculons $\dfrac{k}{m} = \dfrac{5 \times 10^{-5}}{4 \times 10^{-5}} = 1{,}25\text{ s}^{-1}$.
   L'équation s'écrit : $v'(t) = -1{,}25 v(t) + 9{,}81$.
2. $v_{\text{lim}} = \dfrac{9{,}81}{1{,}25} = 7{,}848\text{ m}\cdot\text{s}^{-1}$ (environ $28{,}3\text{ km/h}$).
3. Solution générale : $v(t) = C e^{-1{,}25t} + 7{,}848$.
   Condition $v(0) = 0 \iff C + 7{,}848 = 0 \iff C = -7{,}848$.
   $v(t) = 7{,}848(1 - e^{-1{,}25t})$.
4. $v(t) = 0{,}99 v_{\text{lim}} \iff 1 - e^{-1{,}25t} = 0{,}99 \iff e^{-1{,}25t} = 0{,}01$.
   $-1{,}25 t = \ln(0{,}01) = -\ln(100) \iff t = \dfrac{\ln 100}{1{,}25} \approx \dfrac{4{,}605}{1{,}25} \approx 3{,}68\text{ secondes}$.

**Solution 51.13 :**
1. $y' = -2y + 4 \implies y(x) = C e^{-2x} + 2$.
2. L'équation de la tangente en $x = 0$ est :
   $y = y'(0)(x - 0) + y(0)$.
   Or $y(0) = C + 2$ et $y'(0) = -2y(0) + 4 = -2(C+2) + 4 = -2C$.
   La tangente a pour équation : $y = -2C x + (C + 2)$.
   Elle passe par $A(1\,; 0)$ si et seulement si :
   $0 = -2C(1) + C + 2 \iff -C + 2 = 0 \iff C = 2$.
   Il existe une unique solution : $y(x) = 2e^{-2x} + 2$.

---

#### Solutions du Niveau ★★★

**Solution 51.14 :**
1. $z(t) = \dfrac{1}{y(t)} \implies z'(t) = -\dfrac{y'(t)}{(y(t))^2}$.
2. D'après $(E_L)$, $y'(t) = a y(t) - \dfrac{a}{K}(y(t))^2$.
   Injectons dans $z'$ :
   $z'(t) = -\dfrac{a y(t) - \frac{a}{K}(y(t))^2}{(y(t))^2} = -\dfrac{a}{y(t)} + \dfrac{a}{K} = -a z(t) + \dfrac{a}{K}$.
   En passant $-az$ à gauche : $z'(t) + a z(t) = \dfrac{a}{K}$. C'est bien une équation linéaire !
3. $z' = -az + \dfrac{a}{K}$ a pour solution d'équilibre $-\dfrac{a/K}{-a} = \dfrac{1}{K}$.
   Donc $z(t) = B e^{-at} + \dfrac{1}{K}$ avec $B \in \mathbb{R}$.
4. À $t = 0$, $z(0) = \dfrac{1}{y_0} = B + \dfrac{1}{K} \implies B = \dfrac{1}{y_0} - \dfrac{1}{K} = \dfrac{K - y_0}{K y_0}$.
   Alors $z(t) = \dfrac{1}{K} \left(1 + \dfrac{K - y_0}{y_0} e^{-at}\right)$.
   Puisque $y(t) = \dfrac{1}{z(t)}$ :
   $$y(t) = \dfrac{K}{1 + \left(\dfrac{K - y_0}{y_0}\right) e^{-at}}.$$
5. Quand $t \to +\infty$, $e^{-at} \to 0$ (car $a > 0$), donc $\lim\limits_{t \to +\infty} y(t) = \dfrac{K}{1 + 0} = K$.
   La courbe est une **courbe en S** (sigmoïde), qui part de $y_0$ et plafonne harmonieusement à la capacité limite $K$.

**Solution 51.15 :**
1. Pour $y(t) = A\cos(\omega t) + B\sin(\omega t)$ :
   $y'(t) = -A\omega\sin(\omega t) + B\omega\cos(\omega t)$.
   $y''(t) = -A\omega^2\cos(\omega t) - B\omega^2\sin(\omega t) = -\omega^2 y(t)$.
   Donc $y'' + \omega^2 y = 0$. Ces fonctions sont bien solutions.
2. Dérivons $u(t) = \omega f(t)\sin(\omega t) + f'(t)\cos(\omega t)$ :
   $u'(t) = \omega f'(t)\sin(\omega t) + \omega^2 f(t)\cos(\omega t) + f''(t)\cos(\omega t) - \omega f'(t)\sin(\omega t) = \big(f''(t) + \omega^2 f(t)\big)\cos(\omega t)$.
   Or $f$ vérifie $(H)$, donc $f''(t) + \omega^2 f(t) = 0$. D'où $u'(t) = 0$.
   De même, un calcul direct donne $v'(t) = -\big(f''(t) + \omega^2 f(t)\big)\sin(\omega t) = 0$.
3. $u$ et $v$ sont dérivables sur $\mathbb{R}$ de dérivées nulles, elles sont donc constantes : $u(t) = B\omega$ et $v(t) = A\omega$.
   En formant la combinaison $\dfrac{u(t)\sin(\omega t) + v(t)\cos(\omega t)}{\omega}$, on obtient :
   $f(t)\big(\sin^2(\omega t) + \cos^2(\omega t)\big) = f(t) = A\cos(\omega t) + B\sin(\omega t)$.
   Toute solution est obligatoirement de cette forme !

**Solution 51.16 :**
1. $y' = y \implies y_{k+1} = y_k + h y'(t_k) = y_k + h y_k = (1 + h) y_k$.
2. Avec $y_0 = 1$ et $h = \dfrac{1}{n}$, la suite $(y_k)$ est une suite géométrique de raison $\left(1 + \dfrac{1}{n}\right)$.
   Donc au bout des $n$ étapes, la valeur approchée en $t = n h = 1$ est :
   $y_n = y_0 \times \left(1 + \dfrac{1}{n}\right)^n = \left(1 + \dfrac{1}{n}\right)^n$.
3. Comme la méthode d'Euler converge vers la solution exacte $y(1) = e^1 = e$ quand le pas $h \to 0$ ($n \to +\infty$), on en déduit immédiatement :
   $$\lim_{n \to +\infty} \left(1 + \dfrac{1}{n}\right)^n = e.$$

---

### La question qui ouvre la suite

Jusqu'à présent, nous avons décrit des mouvements et des phénomènes sur une ligne droite (le temps $t$) ou sur un plan en deux dimensions (la feuille de papier avec $x$ et $y$).
Mais notre univers physique n'est pas plat : la Terre flotte dans un espace à trois dimensions, les cathédrales élèvent leurs voûtes vers le ciel, les satellites tournent sur des orbites inclinées et les avions naviguent avec latitude, longitude et altitude.

Comment repérer un point, tracer une droite et définir l'équation d'un plan incliné dans un espace en trois dimensions ? Comment calculer la distance d'un point à un mur dans une cathédrale ?

Rendez-vous au chapitre 52 avec **la cathédrale dans l'espace** et la géométrie vectorielle en 3D.
