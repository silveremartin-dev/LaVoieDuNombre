# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 37 : La Grande Roue et le Cercle qui s'Enroule

> *« Le degré est une invention de marchands babyloniens qui aimaient le nombre 60. Le radian, lui, est une invention de la roue elle-même : c'est le cercle qui se mesure avec son propre rayon. »*

---

### Ce que tu vas découvrir

- Pourquoi le **degré** ne suffit plus quand on veut décrire un mouvement qui tourne sans fin (roues, planètes, ondes, moteurs).
- Une nouvelle unité d'angle, née du cercle lui-même : le **radian**.
- Comment **enrouler la droite des réels** autour d'un cercle de rayon 1, et donner ainsi un sens à $\cos(100)$, à $\sin(-7)$ ou à $\cos\left(\frac{37\pi}{4}\right)$.
- Les **valeurs remarquables** ($\frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}$) démontrées avec un carré et un triangle équilatéral.
- Les **angles associés** : comment les symétries du cercle permettent de tout ramener au premier quart de tour.
- Comment **résoudre** les équations $\cos x = a$ et $\sin x = a$, et dessiner les courbes ondulantes des fonctions cosinus et sinus.

---

### 1. Le problème : la cabine qui tourne sans fin

Tu es monté dans la grande roue de la fête foraine. Elle a un rayon de $20$ m, son axe est à $22$ m du sol, et ta cabine part du point le plus bas, à $2$ m du sol. La roue tourne lentement, régulièrement, dans le sens inverse des aiguilles d'une montre quand on la regarde depuis le parking.

Ton petit frère, resté en bas, te pose une question simple :

*« Quand ta cabine aura parcouru 50 mètres le long du cercle, tu seras à quelle hauteur ? Et après 300 mètres ? Et après 1 kilomètre ? »*

Tu sors ta trigonométrie de collège (chapitre 28) : dans un triangle rectangle, $\cos \widehat{A} = \frac{\text{adjacent}}{\text{hypoténuse}}$. Mais très vite, trois obstacles surgissent.

```
                     sommet (42 m)
                       .-*-.
                   .-'   |   '-.
                 .'      |      '.
                /        |        \
               |         O---------|   axe à 22 m
                \        |  20 m  /
                 '.      |      .'
                   '-.   |   .-'
                       '-*-'   ← départ de la cabine (2 m)
          ═══════════════════════════════  sol
```

**Obstacle 1 — Les angles de collège s'arrêtent à 90°.** Un triangle rectangle ne peut pas avoir un angle aigu de $120^\circ$, encore moins de $400^\circ$. Pourtant ta cabine, elle, continue de tourner : après un tour et demi, elle a « tourné de $540^\circ$ ».

**Obstacle 2 — Le degré n'a rien à voir avec la distance parcourue.** Ton frère parle en **mètres parcourus sur le cercle**. Pour passer des mètres aux degrés, il faut à chaque fois faire une règle de trois avec le périmètre $2\pi \times 20$. C'est maladroit : l'unité « degré » est étrangère au cercle.

**Obstacle 3 — Le sens compte.** Si la roue tourne à l'envers (pour faire descendre les passagers), il faut parler d'angles **négatifs**.

Il nous faut donc :
1. une unité d'angle **naturelle**, liée directement à la longueur d'arc ;
2. une définition du cosinus et du sinus valable pour **n'importe quel nombre réel**, positif ou négatif, petit ou énorme.

C'est exactement ce que les mathématiciens ont construit entre le XVIIᵉ et le XVIIIᵉ siècle, et que tu vas reconstruire avec une ficelle.

> **🔍 L'histoire vraie — Le sinus est une poche !**
> Vers 150 av. J.-C., l'astronome grec **Hipparque** dresse la première table de « cordes » pour calculer les positions des astres ; **Ptolémée** la perfectionne dans l'*Almageste* (IIᵉ siècle). En Inde, vers 499, **Aryabhata** préfère utiliser la **demi-corde**, qu'il nomme *ardha-jyā* (« demi-corde d'arc »), abrégé en *jyā* puis *jīva*. Les savants arabes transcrivent ce mot en *jība*, qui s'écrit sans voyelles comme *jayb*, « poche, pli d'un vêtement ». Au XIIᵉ siècle, en traduisant ces textes à Tolède, **Gérard de Crémone** traduit littéralement par le latin *sinus*, « pli, poche, baie ». Voilà pourquoi la plus célèbre fonction ondulante porte le nom d'un pli de tunique !

---

### 2. Le radian : mesurer un angle avec le rayon

#### 2.1 L'expérience de la ficelle

> **🖐️ À toi de jouer —** Prends une boîte de conserve ronde, une ficelle et un feutre. Coupe un morceau de ficelle exactement de la longueur du **rayon** de la boîte. Pose une extrémité sur le bord, puis plaque la ficelle le long du bord circulaire. Trace les deux rayons qui joignent le centre aux extrémités de la ficelle.

L'angle que tu viens de dessiner — celui qui intercepte un arc **de même longueur que le rayon** — est l'unité naturelle du cercle : c'est **un radian**.

```
                    . - ~ ~ ~ - .
                .'      arc = R     '.
              /         ______*        \
             |     R  /       |         |
             |      /  1 rad  |         |
             |    O-----------*         |
             |          R               |
              \                        /
                '.                  .'
                    ' - . _ _ . - '
```

Combien de ficelles « rayon » peut-on poser bout à bout autour du cercle ? Le périmètre vaut $2\pi R$, donc on en pose $\frac{2\pi R}{R} = 2\pi \approx 6{,}28$. Un tour complet mesure donc $2\pi$ radians. Avec $6$ ficelles, il manque encore un petit bout ($0{,}28$ ficelle) pour fermer le tour.

> **📐 Définition — Le radian**
> Dans un cercle de rayon $R$, un angle au centre mesure **$1$ radian** (symbole : **rad**) lorsqu'il intercepte un arc de longueur $R$.
> Un tour complet mesure $2\pi$ rad, donc :
> $$\boxed{\pi \text{ rad} = 180^\circ}$$

Le mot « radian » vient bien sûr de « rayon » (*radius* en latin). L'idée de mesurer les angles par la longueur d'arc remonte au mathématicien anglais **Roger Cotes** (1714) ; le nom *radian* apparaît imprimé pour la première fois en **1873**, dans des sujets d'examen de **James Thomson** (frère de Lord Kelvin), à Belfast.

> **💡 Le savais-tu ?** Le radian est sans dimension : c'est un rapport de deux longueurs ($\frac{\text{arc}}{\text{rayon}}$, mètres divisés par mètres). C'est pourquoi on omet souvent l'unité : on écrit « l'angle $\frac{\pi}{3}$ » plutôt que « $\frac{\pi}{3}$ rad ». Quand aucune unité n'est écrite, **c'est toujours le radian**.

#### 2.2 Conversions

La proportionnalité $\pi \text{ rad} \leftrightarrow 180^\circ$ donne :

$$\text{mesure en rad} = \text{mesure en degrés} \times \frac{\pi}{180} \qquad ; \qquad \text{mesure en degrés} = \text{mesure en rad} \times \frac{180}{\pi}.$$

| Degrés | $0$ | $30$ | $45$ | $60$ | $90$ | $120$ | $135$ | $150$ | $180$ | $270$ | $360$ |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Radians | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |

Et $1 \text{ rad} = \frac{180}{\pi}{}^\circ \approx 57{,}3^\circ$.

> **✅ Exemple résolu 1 — Conversions**
> a) Convertir $75^\circ$ en radians. b) Convertir $\frac{7\pi}{9}$ rad en degrés. c) Convertir $2{,}5$ rad en degrés.
>
> a) $75 \times \frac{\pi}{180} = \frac{75\pi}{180} = \frac{5\pi}{12}$ (on simplifie par $15$).
> b) $\frac{7\pi}{9} \times \frac{180}{\pi} = \frac{7 \times 180}{9} = 7 \times 20 = 140^\circ$.
> c) $2{,}5 \times \frac{180}{\pi} = \frac{450}{\pi} \approx 143{,}2^\circ$.

#### 2.3 Longueur d'arc et aire d'un secteur

Puisque le radian est défini par « arc = rayon pour 1 rad », la longueur d'arc est proportionnelle à l'angle : $1$ rad ↔ $R$, donc $\theta$ rad ↔ $R\theta$.

> **📐 Propriété — Longueur d'arc, aire de secteur**
> Dans un cercle de rayon $R$, un angle au centre de $\theta$ **radians** intercepte :
> - un arc de longueur $\boxed{\ell = R\,\theta}$ ;
> - un secteur angulaire (une « part de tarte ») d'aire $\boxed{\mathcal{A} = \frac{1}{2}R^2\theta}$.

*Justification de l'aire :* le disque entier (angle $2\pi$) a pour aire $\pi R^2$ ; par proportionnalité, l'angle $\theta$ donne $\pi R^2 \times \frac{\theta}{2\pi} = \frac{1}{2}R^2\theta$.

Remarque comme ces formules sont simples **en radians**. En degrés, il faudrait écrire $\ell = \frac{\pi R \alpha}{180}$ : le facteur parasite $\frac{\pi}{180}$ apparaît partout. C'est la première raison d'être du radian : **il fait disparaître les constantes inutiles**. Tu en verras une seconde, plus spectaculaire, en Terminale : la dérivée de $\sin x$ vaut $\cos x$ **seulement si $x$ est en radians**.

> **✅ Exemple résolu 2 — La cabine de la grande roue**
> La roue a un rayon de $20$ m. La cabine a parcouru $50$ m le long du cercle. De quel angle la roue a-t-elle tourné ? Et combien de tours complets après $1$ km ?
>
> $\theta = \frac{\ell}{R} = \frac{50}{20} = 2{,}5$ rad, soit environ $143{,}2^\circ$ (exemple 1 c).
> Pour $1000$ m : $\theta = \frac{1000}{20} = 50$ rad. Un tour vaut $2\pi \approx 6{,}283$ rad, et $\frac{50}{2\pi} \approx 7{,}96$ : la roue a fait $7$ tours complets et presque un huitième tour (il manque environ $0{,}04$ tour).

> **✅ Exemple résolu 3 — Une part de pizza**
> Une pizza de $30$ cm de diamètre est coupée en secteurs d'angle $\frac{\pi}{5}$. Quelle est la longueur de croûte et l'aire d'une part ? Combien de parts ?
>
> $R = 15$ cm. Croûte : $\ell = 15 \times \frac{\pi}{5} = 3\pi \approx 9{,}42$ cm. Aire : $\frac{1}{2} \times 15^2 \times \frac{\pi}{5} = \frac{225\pi}{10} = 22{,}5\pi \approx 70{,}7$ cm². Nombre de parts : $\frac{2\pi}{\pi/5} = 10$.

> **⚠️ Attention, piège ! — Le mode de la calculatrice**
> Les calculatrices ont un mode **DEG** et un mode **RAD**. Si tu tapes `cos(60)` en mode RAD, tu obtiens $\cos(60 \text{ rad}) \approx -0{,}952$, et non $0{,}5$ ! Inversement, `cos(π/3)` en mode DEG donne $\cos(1{,}047^\circ) \approx 0{,}9998$. Avant chaque contrôle, vérifie le mode. En Python, `math.cos` attend **toujours** des radians ; pour convertir, on utilise `math.radians(60)`.

> **⚠️ Attention, piège ! — Les formules d'arc en degrés**
> $\ell = R\theta$ est **fausse** si $\theta$ est en degrés : avec $R = 1$ et $\theta = 90$, on trouverait un arc de 90 m sur un cercle de périmètre $6{,}28$ m ! Toujours convertir en radians d'abord.

---

### 3. Le cercle trigonométrique et l'enroulement de la droite

#### 3.1 Le cercle unité orienté

On se place dans un repère orthonormé $(O ; \vec{\imath}, \vec{\jmath})$ — rappel : « orthonormé » signifie que les deux axes sont perpendiculaires et ont la même unité. On note $I(1;0)$ et $J(0;1)$.

> **📐 Définition — Cercle trigonométrique**
> Le **cercle trigonométrique** est le cercle $\mathcal{C}$ de centre $O$ et de rayon $1$, **orienté** : on choisit comme **sens direct** (ou sens positif, ou sens **trigonométrique**) le sens inverse des aiguilles d'une montre.

Pourquoi ce sens ? Parce que c'est celui qui fait passer de $I$ (sur l'axe des abscisses) à $J$ (sur l'axe des ordonnées) par le plus court chemin, comme on passe de $\vec{\imath}$ à $\vec{\jmath}$. C'est une **convention** — les horloges, elles, tournent dans l'autre sens, dit **indirect**.

Sur ce cercle de rayon $1$, la formule $\ell = R\theta$ devient $\ell = \theta$ : **la mesure d'un angle en radians est exactement la longueur de l'arc parcouru**. Voilà le grand intérêt du rayon $1$.

#### 3.2 L'enroulement : chaque réel devient un point

Imagine maintenant la droite des réels comme un **mètre ruban** infini, gradué. Tu la places verticalement, tangente au cercle au point $I$, l'origine $0$ de la droite posée sur $I$. Puis tu **enroules** :
- la demi-droite des réels positifs autour du cercle dans le **sens direct** ;
- la demi-droite des réels négatifs dans le **sens indirect**.

```
                 droite réelle (ruban)
                         ↑  2
                 J       |
              .-*-.      ↑  1
            .'     '.    |
           |    O    *---0   ← le 0 du ruban est posé sur I
            '.     .'    |
              '-*-'      ↓ -1
                         |
                         ↓ -2
     Le haut du ruban s'enroule vers J (sens direct),
     le bas s'enroule vers le bas (sens indirect).
```

Chaque réel $x$ du ruban vient se poser sur un point précis du cercle : on l'appelle le **point image** de $x$, noté $M(x)$.

- $x = \frac{\pi}{2}$ : on a enroulé un quart de périmètre ($\frac{2\pi}{4}$) : on arrive en $J$.
- $x = \pi$ : un demi-tour : point $I'(-1;0)$.
- $x = -\frac{\pi}{2}$ : un quart de tour en sens indirect : point $J'(0;-1)$.
- $x = 2\pi$ : un tour complet : retour en $I$.

> **📐 Définition — Point image d'un réel**
> À tout réel $x$, l'enroulement associe un unique point $M$ du cercle trigonométrique, appelé **image de $x$**. On dit aussi que $x$ est **une mesure en radians** de l'angle orienté $(\vec{OI}, \vec{OM})$.

#### 3.3 Un point, une infinité de réels : « modulo $2\pi$ »

Le ruban est infini, le cercle ne l'est pas : après un tour, on repasse aux mêmes endroits. Les réels $\frac{\pi}{3}$, $\frac{\pi}{3} + 2\pi = \frac{7\pi}{3}$, $\frac{\pi}{3} + 4\pi = \frac{13\pi}{3}$, $\frac{\pi}{3} - 2\pi = -\frac{5\pi}{3}$… ont tous **la même image**.

> **📐 Propriété — Réels de même image**
> Deux réels $x$ et $y$ ont la même image sur le cercle si et seulement si leur différence est un multiple entier de $2\pi$ :
> $$y = x + 2k\pi \quad \text{avec } k \in \mathbb{Z}.$$
> On écrit alors $y \equiv x \ [2\pi]$, et on lit « $y$ est congru à $x$ **modulo** $2\pi$ ».

*Lecture des notations :* $k \in \mathbb{Z}$ se lit « $k$ appartient à $\mathbb{Z}$ », c'est-à-dire « $k$ est un entier relatif » ($\dots, -2, -1, 0, 1, 2, \dots$) ; $\mathbb{Z}$ vient de l'allemand *Zahlen*, « nombres » (chapitre 31). Le mot *modulo* (« selon la mesure de ») a été introduit par **Gauss** en 1801 pour l'arithmétique des restes ; il signifie ici « à un nombre entier de tours près ».

> **📐 Définition — Mesure principale**
> Parmi tous les réels ayant la même image $M$, il en existe **un seul** dans l'intervalle $]-\pi ; \pi]$. On l'appelle la **mesure principale** de l'angle.

(Rappel de notation : $]-\pi ; \pi]$ désigne l'ensemble des réels $x$ tels que $-\pi < x \leqslant \pi$ ; le crochet tourné vers l'extérieur en $-\pi$ signifie que $-\pi$ est **exclu**, le crochet tourné vers l'intérieur en $\pi$ qu'il est **inclus**. On exclut $-\pi$ car il a la même image que $\pi$ : sans cela, le point $I'$ aurait deux mesures principales.)

> **🧭 Méthode — Trouver la mesure principale de $\frac{p\pi}{q}$**
> 1. Écrire $\frac{p}{q}$ et chercher le multiple **pair** le plus proche : on veut $\frac{p\pi}{q} = \alpha + 2k\pi$ avec $-\pi < \alpha \leqslant \pi$.
> 2. Concrètement : diviser $p$ par $2q$ pour savoir combien de tours complets ($2\pi = \frac{2q\pi}{q}$) retirer.
> 3. Ajuster d'un tour si le résultat sort de $]-\pi;\pi]$.

> **✅ Exemple résolu 4 — Mesures principales**
> Déterminer la mesure principale de : a) $\frac{37\pi}{4}$ ; b) $-\frac{17\pi}{3}$ ; c) $\frac{2023\pi}{6}$.
>
> a) Un tour vaut $\frac{8\pi}{4}$. On écrit $37 = 8 \times 4 + 5$, donc $\frac{37\pi}{4} = \frac{5\pi}{4} + 4 \times 2\pi$. Mais $\frac{5\pi}{4} > \pi$ : on retire encore un tour : $\frac{5\pi}{4} - 2\pi = -\frac{3\pi}{4}$. Mesure principale : $\boxed{-\frac{3\pi}{4}}$.
> *Vérification :* $-\frac{3\pi}{4} + 10\pi = -\frac{3\pi}{4} + \frac{40\pi}{4} = \frac{37\pi}{4}$ ✓.
>
> b) Un tour vaut $\frac{6\pi}{3}$. $-\frac{17\pi}{3} = -\frac{18\pi}{3} + \frac{\pi}{3} = -6\pi + \frac{\pi}{3}$. Comme $-6\pi = -3 \times 2\pi$, la mesure principale est $\boxed{\frac{\pi}{3}}$.
>
> c) Un tour vaut $\frac{12\pi}{6}$. $2023 = 12 \times 168 + 7$ (car $12 \times 168 = 2016$). Donc $\frac{2023\pi}{6} = \frac{7\pi}{6} + 168 \times 2\pi$. Or $\frac{7\pi}{6} > \pi$, donc on retire un tour : $\frac{7\pi}{6} - 2\pi = -\frac{5\pi}{6}$. Mesure principale : $\boxed{-\frac{5\pi}{6}}$.

> **⚠️ Attention, piège ! — Mesure principale et intervalle**
> La mesure principale est dans $]-\pi;\pi]$, **pas** dans $[0;2\pi[$. Pour $\frac{37\pi}{4}$, répondre $\frac{5\pi}{4}$ est faux comme « mesure principale » (même si $\frac{5\pi}{4}$ a bien la même image).

#### 3.4 Placer les points remarquables

En partageant le cercle en $4$, $8$, $12$ parts égales, on place les images des multiples de $\frac{\pi}{2}$, $\frac{\pi}{4}$, $\frac{\pi}{6}$ et $\frac{\pi}{3}$ :

<div align="center">
<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="10"/>
  
  <!-- Axes de coordonnées -->
  <line x1="30" y1="200" x2="370" y2="200" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="370,196 378,200 370,204" fill="#0f172a"/>
  <text x="365" y="190" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8">cosinus x</text>
  
  <line x1="200" y1="370" x2="200" y2="30" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="196,30 200,22 204,30" fill="#0f172a"/>
  <text x="210" y="32" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b91c1c">sinus x</text>
  
  <!-- Cercle unité R = 140 -->
  <circle cx="200" cy="200" r="140" fill="none" stroke="#64748b" stroke-width="2"/>
  
  <!-- Flèche sens trigo -->
  <path d="M 310 140 A 130 130 0 0 0 250 80" fill="none" stroke="#15803d" stroke-width="2.5" stroke-dasharray="4,2"/>
  <polygon points="245,75 258,82 250,90" fill="#15803d"/>
  <text x="300" y="105" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d">Sens direct (+)</text>

  <!-- Points remarquables et rayons (en utilisant r=140) -->
  <!-- 0 rad -->
  <circle cx="340" cy="200" r="4" fill="#1d4ed8"/>
  <text x="350" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">0 (2π)</text>

  <!-- pi/6 (30 deg: dx = 140*cos(30) = 121, dy = -140*sin(30) = -70) -> (321, 130) -->
  <line x1="200" y1="200" x2="321" y2="130" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="321" cy="130" r="4" fill="#d97706"/>
  <text x="330" y="130" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/6 (30°)</text>

  <!-- pi/4 (45 deg: dx = 99, dy = -99) -> (299, 101) -->
  <line x1="200" y1="200" x2="299" y2="101" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="299" cy="101" r="4" fill="#d97706"/>
  <text x="308" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/4 (45°)</text>

  <!-- pi/3 (60 deg: dx = 70, dy = -121) -> (270, 79) -->
  <line x1="200" y1="200" x2="270" y2="79" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="270" cy="79" r="4" fill="#d97706"/>
  <text x="275" y="70" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/3 (60°)</text>

  <!-- pi/2 (90 deg) -> (200, 60) -->
  <circle cx="200" cy="60" r="4" fill="#b91c1c"/>
  <text x="200" y="52" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">π/2 (90°)</text>

  <!-- pi (180 deg) -> (60, 200) -->
  <circle cx="60" cy="200" r="4" fill="#1d4ed8"/>
  <text x="45" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">π (180°)</text>

  <!-- 3pi/2 (270 deg) -> (200, 340) -->
  <circle cx="200" cy="340" r="4" fill="#b91c1c"/>
  <text x="200" y="360" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">-π/2 (ou 3π/2)</text>

  <!-- Centre O -->
  <circle cx="200" cy="200" r="3" fill="#0f172a"/>
  <text x="188" y="215" font-family="sans-serif" font-size="11" fill="#64748b">O</text>
</svg>
</div>

```
                          π/2
                  2π/3     J      π/3
             3π/4    *     *     *    π/4
          5π/6  *                   *  π/6
                                          
         π  I' *          O          * I   0
                                          
         -5π/6  *                   *  -π/6
            -3π/4    *     *     *    -π/4
                 -2π/3     J'    -π/3
                          -π/2
```

> **🧭 Méthode — Placer $\frac{k\pi}{n}$ rapidement**
> Compte en « parts de $\frac{\pi}{n}$ » : le demi-tour supérieur ($0$ à $\pi$) en contient $n$. Pour $\frac{5\pi}{6}$, on avance de $5$ parts sur $6$ dans le demi-cercle supérieur : on est presque en $I'$, juste au-dessus. Pour $-\frac{2\pi}{3}$, on descend (sens indirect) de $2$ parts sur $3$ dans le demi-cercle inférieur.

---

### 4. Cosinus et sinus d'un nombre réel

#### 4.1 La définition

Le point image $M(x)$ a deux coordonnées dans le repère $(O;\vec{\imath},\vec{\jmath})$. On leur donne un nom.

> **📐 Définition — Cosinus et sinus d'un réel**
> Soit $x$ un réel et $M$ son image sur le cercle trigonométrique. On appelle :
> - **cosinus de $x$**, noté $\cos x$ ou $\cos(x)$, l'**abscisse** de $M$ ;
> - **sinus de $x$**, noté $\sin x$ ou $\sin(x)$, l'**ordonnée** de $M$.
> $$M(x) = \big(\cos x \ ; \ \sin x\big).$$

```
                  y
                  ▲
               1  |    . - * M(x)
                  |  .'   /|
                  | /    / |
                  |/  1 /  | sin x
                  |    /   |
           -------O---/----+---------*---> x
                  | x ⌒     cos x    I (1;0)
                  |
                  |
```

Lecture : $\cos x$ se lit « cosinus de $x$ ». L'abréviation *cos* vient de *complementi sinus*, « sinus du complémentaire » (on verra plus bas que $\cos x = \sin(\frac{\pi}{2} - x)$). Les abréviations *sin* et *cos* se sont imposées au XVIIᵉ siècle, notamment grâce à l'Anglais **William Oughtred** ; c'est **Euler** qui, au XVIIIᵉ siècle, en fait des **fonctions** d'un nombre réel.

> **⚠️ Attention, piège ! — Ce n'est pas un produit**
> $\cos x$ n'est pas « $\cos \times x$ » : « cos » tout seul ne veut rien dire. Ainsi $\cos(2x) \neq 2\cos x$, et $\cos(a+b) \neq \cos a + \cos b$ (par exemple $\cos\left(\frac{\pi}{2} + \frac{\pi}{2}\right) = \cos\pi = -1$ alors que $\cos\frac{\pi}{2} + \cos\frac{\pi}{2} = 0$).
> Notation usuelle : $\cos^2 x$ signifie $(\cos x)^2$, le carré du cosinus — à ne pas confondre avec $\cos(x^2)$.

#### 4.2 Retour à la grande roue

Mettons l'origine au centre de la roue, unité $1$ = $20$ m, et mesurons l'angle à partir du point le plus bas… C'est plus simple de partir du repère habituel : la position de la cabine à l'angle $x$ (mesuré depuis le rayon horizontal de droite) est $(20\cos x \,;\, 20\sin x)$ par rapport à l'axe. Comme la cabine part du **bas**, qui correspond à $x = -\frac{\pi}{2}$, après avoir tourné de $\theta$ elle est à l'angle $x = \theta - \frac{\pi}{2}$. Sa hauteur au-dessus du sol est :

$$h(\theta) = 22 + 20\sin\left(\theta - \frac{\pi}{2}\right).$$

Nous verrons au §6 que $\sin\left(\theta - \frac{\pi}{2}\right) = -\cos\theta$, d'où la formule élégante $h(\theta) = 22 - 20\cos\theta$. Vérifions : $\theta = 0$ donne $22 - 20 = 2$ m (départ en bas) ✓, $\theta = \pi$ donne $22 + 20 = 42$ m (sommet) ✓.

Réponse au petit frère : après $50$ m, $\theta = 2{,}5$ rad et $h = 22 - 20\cos(2{,}5) \approx 22 - 20 \times (-0{,}8011) \approx 38{,}0$ m. Après $1$ km, $\theta = 50$ rad et $h = 22 - 20\cos 50 \approx 22 - 20 \times 0{,}9650 \approx 2{,}7$ m : presque revenu en bas, comme prévu (7,96 tours).

#### 4.3 Premières propriétés

> **📐 Propriétés fondamentales** — Pour tout réel $x$ et tout entier $k$ :
> 1. $-1 \leqslant \cos x \leqslant 1$ et $-1 \leqslant \sin x \leqslant 1$ ;
> 2. $\cos(x + 2k\pi) = \cos x$ et $\sin(x + 2k\pi) = \sin x$ ;
> 3. $\boxed{\cos^2 x + \sin^2 x = 1}$.

> **✍️ Démonstration**
> 1. $M$ est sur le cercle de centre $O$ et de rayon $1$, donc ses coordonnées sont comprises entre $-1$ et $1$.
> 2. $x$ et $x + 2k\pi$ ont la même image (§3.3), donc les mêmes coordonnées.
> 3. $OM = 1$. La formule de la distance dans un repère orthonormé (chapitre 20, conséquence de Pythagore) donne $OM^2 = (\cos x - 0)^2 + (\sin x - 0)^2$, donc $\cos^2 x + \sin^2 x = 1$. $\blacksquare$

#### 4.4 Cohérence avec le collège

Le nouveau cosinus contredit-il l'ancien ? Non.

> **📐 Propriété — Lien avec le triangle rectangle**
> Si $0 < x < \frac{\pi}{2}$, alors $\cos x$ et $\sin x$ coïncident avec le cosinus et le sinus de l'angle aigu de mesure $x$ dans un triangle rectangle.

> **✍️ Démonstration**
> Soit $M(x)$ avec $0 < x < \frac{\pi}{2}$ : $M$ est dans le quart de cercle supérieur droit. Soit $H$ le projeté orthogonal de $M$ sur l'axe des abscisses. Le triangle $OHM$ est rectangle en $H$, d'hypoténuse $OM = 1$, et l'angle $\widehat{HOM}$ mesure $x$ rad. Au sens du collège :
> $\cos \widehat{HOM} = \frac{OH}{OM} = \frac{OH}{1} = OH$, et $OH$ est précisément l'abscisse de $M$ (positive). De même $\sin\widehat{HOM} = \frac{HM}{OM} = HM$, qui est l'ordonnée de $M$. $\blacksquare$

#### 4.5 Les signes selon les quadrants

```
                     y
             sin > 0 | sin > 0
             cos < 0 | cos > 0
               (II)  |  (I)
          -----------O-----------> x
              (III)  |  (IV)
             sin < 0 | sin < 0
             cos < 0 | cos > 0
```

> **✅ Exemple résolu 5 — Utiliser $\cos^2 + \sin^2 = 1$**
> On sait que $x \in \left]\frac{\pi}{2} ; \pi\right[$ et $\sin x = \frac{3}{5}$. Calculer $\cos x$.
>
> $\cos^2 x = 1 - \sin^2 x = 1 - \frac{9}{25} = \frac{16}{25}$, donc $\cos x = \frac{4}{5}$ ou $\cos x = -\frac{4}{5}$.
> Or $x$ est dans le quadrant II, où le cosinus est négatif. Donc $\boxed{\cos x = -\frac{4}{5}}$.

> **⚠️ Attention, piège ! — Ne jamais oublier le signe**
> $\cos^2 x = \frac{16}{25}$ ne donne pas automatiquement $\cos x = \frac{4}{5}$. L'équation $X^2 = a$ (avec $a > 0$) a **deux** solutions $\sqrt a$ et $-\sqrt a$ (chapitre 23). C'est la **position du point** sur le cercle qui tranche.

