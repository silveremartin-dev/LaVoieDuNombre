# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 28 : Ératosthène et le Tour de la Terre

> *« Ne dis pas que la Terre est trop grande pour être mesurée par un homme. Donne-moi un simple bâton planté droit dans le sol, un rayon de soleil et un triangle rectangle : je te dirai le tour du monde avant que le jour ne s'éteigne. »*

---

### Ce que tu vas découvrir

- Comment **Ératosthène**, il y a plus de 2 200 ans, a mesuré la circonférence de la Terre avec un bâton, un puits et un chameau.
- Comment un triangle rectangle permet de fabriquer trois « ponts » indestructibles entre les **angles** et les **longueurs** : le **cosinus**, le **sinus** et la **tangente**.
- Le moyen mnémotechnique universel **CAH-SOH-TOA** (ou **SOH-CAH-TOA**) pour ne plus jamais hésiter.
- Pourquoi le cosinus et le sinus sont **toujours compris entre 0 et 1** dans un triangle rectangle.
- Comment calculer la **hauteur inaccessible d'une falaise**, la **largeur d'un fleuve** ou la trajectoire d'un navire sans bouger d'un pas.
- La formule magique de Pythagore déguisée : $\cos^2(x) + \sin^2(x) = 1$.

---

### 1. Le problème : le midi du solstice d'été à Alexandrie

Nous sommes le **21 juin**, vers l'an **240 avant notre ère**, sous le ciel bleu d'Égypte.
Dans la cité d'Alexandrie, le savant **Ératosthène** dirige la plus prestigieuse institution du monde antique : la Grande Bibliothèque. Des centaines de milliers de rouleaux de papyrus s'y alignent sur des étagères de cèdre.

Ératosthène a lu un rapport stupéfiant venu de la ville de **Syène** (l'actuelle ville d'Assouan), située à environ 800 kilomètres plus au sud, le long du Nil :
> *« Le jour du solstice d'été, à midi pile, le soleil illumine directement l'eau au fond des puits les plus profonds sans laisser la moindre ombre sur les parois. Les colonnes des temples ne projettent aucune ombre au sol. Les rayons tombent rigoureusement à la verticale. »*

Ératosthène attend le même jour, à la même heure, à **Alexandrie**.
Il plante dans le sol un **gnomon** — une tige verticale bien droite — et observe attentivement le sol.
Surprise : à Alexandrie, au même instant, **le bâton projette une ombre** !

```
             Rayons solaires (parallèles)
                │ │ │ │ │ │ │ │ │
                ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼

     Alexandrie :                          Syène :
       Bâton vertical                        Bâton vertical
          │                                     │
          │                                     │
       ───┴───────                           ───┴───────
          ▲                                     ▲
        Ombre projetée !                    Aucune ombre !
   (Le soleil est incliné)             (Le soleil est au zénith)
```

Comment est-ce possible ? Si la Terre était un disque plat, comme beaucoup d'anciens le croyaient encore, le Soleil — situé à une distance immense et envoyant des rayons parallèles — éclairerait Alexandrie exactement avec le même angle qu'à Syène. Il n'y aurait d'ombre nulle part, ou la même ombre partout !

Si le bâton d'Alexandrie a une ombre alors que celui de Syène n'en a pas, c'est que **la surface de la Terre est courbée** !

Ératosthène mesure la hauteur du bâton et la longueur de l'ombre au sol. Ces deux côtés forment un **triangle rectangle**. En comparant ces deux longueurs, il trouve que les rayons du soleil font avec la verticale un angle d'environ **$7{,}2^\circ$**.

```
                           Sommet du bâton
                                  ● S
                                 /│
                                / │
                               /  │  Bâton vertical (hauteur h)
                 Rayon de     /   │
                 soleil      / α  │
                            /     │
                           ●──────■ P (Pied du bâton)
                           O      Angle droit
                           <-- l ->
                         Ombre au sol
```

Or, grâce au théorème des angles alternes-internes (que tu as vu au Chapitre 15), cet angle de $7{,}2^\circ$ au sommet du bâton est **exactement égal à l'angle au centre de la Terre** qui sépare Alexandrie de Syène !

```
                                 Alexandrie
                                    /
                                   /  Angle α = 7,2°
                                  /
                                 ●─────── Syène
                                /
                               /
                              /
                             ● Centre de la Terre
```

Ératosthène fait alors une proportion lumineuse :
* Un tour complet de cercle mesure $360^\circ$.
* Or $7{,}2^\circ$, c'est exactement $\dfrac{7{,}2}{360} = \dfrac{1}{50}$ de tour !
* Donc la distance entre Alexandrie et Syène représente **le cinquantième de la circonférence de la Terre**.

Les chameliers et les arpenteurs royaux estiment cette distance à environ **5 000 stades** (environ 800 km).
Ératosthène multiplie :
$$\text{Tour de la Terre} = 50 \times 5\,000 = \mathbf{250\,000\text{ stades}} \approx \mathbf{40\,000\text{ kilomètres}} !$$

Un résultat d'une précision époustouflante pour l'époque : la mesure moderne réelle est de 40 075 km à l'équateur !

Mais admire le cœur de l'exploit : pour trouver l'angle de $7{,}2^\circ$, Ératosthène n'a pas pu monter dans le ciel avec un immense rapporteur. Il a mesuré **deux longueurs au sol** (la hauteur du bâton et son ombre) et il en a déduit **un angle**.

Cette science qui relie les longueurs des côtés et les angles d'un triangle s'appelle la **trigonométrie** (du grec *trigōnon*, triangle, et *metron*, mesure).

---

### 2. Le triangle rectangle : baptiser les trois côtés

Pour faire de la trigonométrie sans jamais s'embrouiller, il faut d'abord apprendre à regarder un triangle rectangle par les yeux d'un **angle aigu précis**.

Soit un triangle $ABC$, rectangle en $B$.
Ses deux angles aigus sont $\widehat{A}$ et $\widehat{C}$. Choisissons l'angle aigu $\widehat{A}$.

```
                 C
                 ▲
                 │ \
                 │  \
  Côté OPPOSÉ    │   \   HYPOTÉNUSE
  à l'angle A    │    \  (le plus long côté,
                 │     \  en face de l'angle droit)
                 │      \
                 ■───────● A
                 B   ^
                 Côté ADJACENT à l'angle A
```

Regardons les trois côtés depuis le sommet $A$ :
1. **L'hypoténuse :** c'est le côté situé en face de l'angle droit. C'est le plus long côté du triangle. Ici, c'est le segment $[AC]$. Son rôle ne dépend d'aucun angle particulier : c'est le maître du triangle rectangle.
2. **Le côté adjacent à l'angle $\widehat{A}$ :** le mot *adjacent* vient du latin *ad-jacere*, qui signifie « couché à côté ». C'est le côté de l'angle droit qui touche l'angle $\widehat{A}$. Ici, c'est le segment $[AB]$.
3. **Le côté opposé à l'angle $\widehat{A}$ :** c'est le côté de l'angle droit qui est en face de l'angle $\widehat{A}$, de l'autre côté du triangle. Ici, c'est le segment $[BC]$.

> **⚠️ Attention, piège ! Les rôles s'inversent si l'on change d'angle !**
> Si tu te places maintenant au sommet $C$ :
> - L'hypoténuse reste toujours $[AC]$.
> - Le côté **adjacent** à $\widehat{C}$ devient $[BC]$ !
> - Le côté **opposé** à $\widehat{C}$ devient $[AB]$ !
> Un côté n'est jamais « opposé » ou « adjacent » tout seul dans l'absolu : il l'est **relativement à l'angle considéré**.

---

### 3. Les trois rapports magiques : Cosinus, Sinus, Tangente

Imagine que tu dessines un triangle rectangle avec un angle aigu de $30^\circ$.
Que tu le dessines sur ton cahier (avec une hypoténuse de 10 cm), sur le tableau de la classe (hypoténuse de 1 mètre) ou dans la cour (hypoténuse de 10 mètres), ces trois triangles sont des **agrandissements ou réductions** les uns des autres (triangles semblables, Chapitre 17).

Puisque les formes sont identiques, **le rapport entre les longueurs des côtés ne dépend que de l'angle**, et absolument pas de la taille du dessin !

Pour un angle aigu donné $x$, ces rapports portent trois noms universels :

> **📐 Définitions fondamentales —** Dans un triangle rectangle :
>
> 1. Le **cosinus** de l'angle aigu est le quotient du côté adjacent par l'hypoténuse :
>    $$\cos(x) = \frac{\text{longueur du côté adjacent}}{\text{longueur de l'hypoténuse}}$$
>
> 2. Le **sinus** de l'angle aigu est le quotient du côté opposé par l'hypoténuse :
>    $$\sin(x) = \frac{\text{longueur du côté opposé}}{\text{longueur de l'hypoténuse}}$$
>
> 3. La **tangente** de l'angle aigu est le quotient du côté opposé par le côté adjacent :
>    $$\tan(x) = \frac{\text{longueur du côté opposé}}{\text{longueur du côté adjacent}}$$

#### Comment prononcer et écrire ces notations ?
- $\cos(x)$ s'écrit « cos » et se lit à voix haute **« cosinus de $x$ »**.
- $\sin(x)$ s'écrit « sin » et se lit à voix haute **« sinus de $x$ »**.
- $\tan(x)$ s'écrit « tan » (anciennement « tg ») et se lit à voix haute **« tangente de $x$ »**.

#### Le moyen mnémotechnique universel : CAH-SOH-TOA
Pour retenir ces trois formules sans jamais hésiter, les élèves du monde entier répètent cette formule magique comme le nom d'un sage guerrier amérindien :

$$\mathbf{C}\text{A}\text{H} \quad-\quad \mathbf{S}\text{O}\text{H} \quad-\quad \mathbf{T}\text{O}\text{A}$$

- **C**osinus = **A**djacent / **H**ypoténuse
- **S**inus = **O**pposé / **H**ypoténuse
- **T**angente = **O**pposé / **A**djacent

Certains préfèrent l'ordre inverse : **SOH - CAH - TOA**. Choisis celui qui chante le mieux à tes oreilles !

---

### 4. Deux propriétés capitales à comprendre

#### 4.1 Pourquoi cosinus et sinus sont-ils toujours compris entre 0 et 1 ?

Dans tout triangle rectangle, l'hypoténuse est **le plus grand côté**.
Par conséquent, la longueur du côté adjacent est strictement inférieure à l'hypoténuse, et la longueur du côté opposé est aussi strictement inférieure à l'hypoténuse.

Puisque le numérateur est plus petit que le dénominateur (et que ce sont des longueurs positives) :
$$\frac{\text{adjacent}}{\text{hypoténuse}} < 1 \qquad\text{et}\qquad \frac{\text{opposé}}{\text{hypoténuse}} < 1$$

> **📐 Propriété — Bornes du cosinus et du sinus.**
> Pour tout angle aigu $x$ d'un triangle rectangle ($0^\circ < x < 90^\circ$) :
> $$0 < \cos(x) < 1 \qquad\text{et}\qquad 0 < \sin(x) < 1$$

> **⚠️ Attention, piège !**
> Si lors d'un contrôle tu trouves $\cos(x) = 1{,}45$ ou $\sin(x) = 2{,}3$, **arrête-toi immédiatement** : c'est rigoureusement impossible ! Tu as très probablement inversé le numérateur et le dénominateur de ta fraction.
> En revanche, la **tangente** $\tan(x) = \frac{\text{opposé}}{\text{adjacent}}$ peut valoir n'importe quel nombre positif : elle peut valoir $0{,}5$, $1$, $10$ ou même $1\,000$ si le triangle est très étiré en hauteur !

#### 4.2 La relation fondamentale : Pythagore sous un nouveau masque

Que se passe-t-il si l'on calcule la somme des carrés du cosinus et du sinus d'un même angle $x$ ?
Prenons notre triangle rectangle avec l'adjacent noté $a$, l'opposé noté $b$, et l'hypoténuse notée $c$.
D'après le théorème de Pythagore (Chapitre 19) :
$$a^2 + b^2 = c^2$$

Calculons maintenant :
$$\cos^2(x) + \sin^2(x) = \left(\frac{a}{c}\right)^2 + \left(\frac{b}{c}\right)^2 = \frac{a^2}{c^2} + \frac{b^2}{c^2} = \frac{a^2 + b^2}{c^2}$$
Or $a^2 + b^2 = c^2$, donc :
$$\frac{a^2 + b^2}{c^2} = \frac{c^2}{c^2} = 1$$

> **📐 Théorème fondamental de la trigonométrie —**
> Pour tout angle $x$ :
> $$\cos^2(x) + \sin^2(x) = 1$$
> *(Remarque sur la notation : $\cos^2(x)$ signifie bien $(\cos(x))^2$, c'est-à-dire le cosinus multiplié par lui-même).*

De plus, en divisant le sinus par le cosinus :
$$\frac{\sin(x)}{\cos(x)} = \frac{\frac{\text{opposé}}{\text{hypoténuse}}}{\frac{\text{adjacent}}{\text{hypoténuse}}} = \frac{\text{opposé}}{\text{adjacent}} = \tan(x)$$

> **📐 Propriété du quotient —**
> $$\tan(x) = \frac{\sin(x)}{\cos(x)}$$

Ces deux formules permettent de trouver le sinus et la tangente d'un angle dès que l'on connaît son cosinus, sans même avoir besoin de connaître la mesure de l'angle !

> **💡 Le savais-tu ? D'où viennent ces mots étranges ?**
> Le mot **sinus** a une histoire de voyage linguistique incroyable. Les astronomes indiens du Ve siècle appelaient cette demi-corde géométrique *jya-ardha*, abrégé en *jiva*. Quand les savants arabes ont traduit ces traités au VIIIe siècle, ils ont transcrit le mot phonétiquement sous la forme *jiba*, écrit *jb* en arabe sans voyelles. Au XIIe siècle, à Tolède en Espagne, le traducteur Gérard de Crémone a confondu ce mot avec le mot arabe *jayb*, qui signifie « pli de vêtement, poche ou golfe ». Il l'a donc traduit en latin par **sinus**, qui signifie « pli, courbure, golfe » (qui a aussi donné le mot « sinueux ») !
> Quant à **cosinus**, c'est l'abréviation de *complementi sinus* : le sinus de l'angle complémentaire !

---

### 5. Utiliser la calculatrice : les deux modes d'emploi

Pour faire des calculs, tu vas utiliser les touches de ta calculatrice scientifique : `cos`, `sin`, `tan`.

> **⚠️ Attention, piège absolu ! Le mode de la calculatrice !**
> La calculatrice sait mesurer les angles en degrés (DEG) ou en radians (RAD). Au collège, **tous les angles sont en degrés**.
> Vérifie toujours qu'une petite lettre **D** ou **DEG** apparaît en haut de ton écran. Si tu vois un **R** ou **RAD**, tes calculs seront faux ! Pour basculer en degrés, consulte le menu `Config` ou `Mode` de ta machine.

#### Cas 1 : On connaît l'angle, on cherche le rapport
Tu tapes directement sur la touche :
- $\cos(60^\circ) = 0{,}5$ pile.
- $\sin(30^\circ) = 0{,}5$ pile.
- $\tan(45^\circ) = 1$ pile (car dans un demi-carré, côté opposé = côté adjacent !).
- $\cos(48^\circ) \approx 0{,}6691...$

#### Cas 2 : On connaît le rapport, on cherche l'angle (les touches inverses)
Si tu sais que $\cos(x) = 0{,}8$, quel est l'angle $x$ ?
On utilise la touche inverse, notée souvent **$\arccos$** ou **$\cos^{-1}$** (souvent accessible avec la touche `Seconde` ou `Shift` puis `cos`) :
- Si $\cos(x) = 0{,}8$, alors $x = \arccos(0{,}8) \approx 36{,}87^\circ$.
- Si $\sin(x) = 0{,}5$, alors $x = \arcsin(0{,}5) = 30^\circ$.
- Si $\tan(x) = 1$, alors $x = \arctan(1) = 45^\circ$.

---

### 6. Les deux grands types de problèmes du collège

En classe de 4e et 3e, tout problème de trigonométrie se ramène à l'un de ces deux défis :
1. **Calculer une longueur** quand on connaît un angle et une autre longueur.
2. **Calculer un angle** quand on connaît deux longueurs.

Voici la démarche infaillible en 4 étapes :

```
                  ┌───────────────────────────────────────────────┐
                  │ 1. Je fais un croquis et je repère            │
                  │    l'angle droit et l'angle utile.            │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 2. Je nomme les trois côtés :                 │
                  │    Hypoténuse / Adjacent / Opposé.            │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 3. Je choisis la bonne formule :              │
                  │    - Adjacent et Hypoténuse en jeu ? => CAH   │
                  │    - Opposé et Hypoténuse en jeu ?   => SOH   │
                  │    - Opposé et Adjacent en jeu ?     => TOA   │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 4. J'écris l'égalité, j'isole l'inconnue      │
                  │    (produit en croix) et je calcule.          │
                  └───────────────────────────────────────────────┘
```

---

### 7. Exemples résolus détaillés pas à pas

#### Exemple résolu 1 — Calculer une longueur au numérateur
Dans le triangle $KLM$ rectangle en $L$, on donne $KM = 8\text{ cm}$ et $\widehat{K} = 35^\circ$.
Calcule la longueur du côté $[LM]$, arrondie au millimètre près.

```
                     M
                     ▲
                     │ \
                     │  \
           LM = ?    │   \  KM = 8 cm
                     │    \
                     │ 35° \
                     ■──────● K
                     L
```

*Solution rédigée :*
1. **Nature du triangle :** Le triangle $KLM$ est rectangle en $L$.
2. **Repérage par rapport à l'angle connu $\widehat{K}$ :**
   - $[KM]$ est l'hypoténuse (longueur connue : 8 cm).
   - $[LM]$ est le côté **opposé** à l'angle $\widehat{K}$ (longueur cherchée).
3. **Choix de la formule :** Opposé et hypoténuse font penser à SOH $\implies$ on utilise le **sinus** :
   $$\sin(\widehat{K}) = \frac{LM}{KM}$$
4. **Calcul :**
   $$\sin(35^\circ) = \frac{LM}{8}$$
   En multipliant par 8 des deux côtés (ou produit en croix $\frac{\sin(35^\circ)}{1} = \frac{LM}{8}$) :
   $$LM = 8 \times \sin(35^\circ) \approx 8 \times 0{,}573576 \approx 4{,}588\text{ cm}$$
   La longueur $LM$ mesure environ **$4{,}6\text{ cm}$** (arrondie au millimètre).

---

#### Exemple résolu 2 — Calculer une longueur au dénominateur (le piège classique)
Dans le triangle $RST$ rectangle en $S$, on sait que $RS = 5\text{ cm}$ et $\widehat{R} = 40^\circ$.
Calcule la longueur de l'hypoténuse $[RT]$, arrondie au millimètre.

```
                     T
                     ▲
                     │ \
                     │  \  RT = ? (Hypoténuse)
                     │   \
                     │ 40°\
                     ■─────● R
                     S  5 cm
```

*Solution rédigée :*
1. Le triangle $RST$ est rectangle en $S$.
2. Par rapport à l'angle connu $\widehat{R} = 40^\circ$ :
   - $[RS]$ est le côté **adjacent** ($RS = 5\text{ cm}$).
   - $[RT]$ est l'**hypoténuse** (inconnue).
3. Adjacent et hypoténuse font penser à CAH $\implies$ on utilise le **cosinus** :
   $$\cos(\widehat{R}) = \frac{RS}{RT}$$
4. On remplace par les valeurs :
   $$\cos(40^\circ) = \frac{5}{RT}$$
   Pour sortir $RT$ du dénominateur, on utilise le produit en croix avec $\frac{\cos(40^\circ)}{1} = \frac{5}{RT}$ :
   $$RT \times \cos(40^\circ) = 5 \times 1 \implies RT = \frac{5}{\cos(40^\circ)}$$
   À la calculatrice :
   $$RT = \frac{5}{\cos(40^\circ)} \approx \frac{5}{0{,}766044} \approx 6{,}527\text{ cm}$$
   L'hypoténuse $[RT]$ mesure environ **$6{,}5\text{ cm}$**.
   *(Remarque d'auto-contrôle : l'hypoténuse mesure 6,5 cm, elle est bien plus longue que le côté adjacent de 5 cm. C'est cohérent !)*

---

#### Exemple résolu 3 — Calculer un angle aigu connaissant deux côtés
Un voilier approche d'un phare bâti sur un îlot rocheux. Le sommet de la falaise s'élève à 42 mètres au-dessus du niveau de la mer. Le bateau se trouve à 110 mètres à l'horizontale du pied de la falaise.
Sous quel angle d'élévation le marin voit-il le sommet de la falaise ? (arrondir au dixième de degré).

```
               Sommet F
                 ●
                 │\
                 │ \
         42 m    │  \
                 │   \
                 ■────● Bateau B
                 P   ^ Angle α = ?
                   110 m
```

*Solution rédigée :*
1. Le triangle $FPB$ formé par la falaise verticale, la ligne d'eau horizontale et la ligne de visée est rectangle en $P$.
2. Par rapport à l'angle cherché $\widehat{B}$ :
   - Le côté opposé est la hauteur de la falaise : $FP = 42\text{ m}$.
   - Le côté adjacent est la distance horizontale : $PB = 110\text{ m}$.
3. Opposé et adjacent font penser à TOA $\implies$ on utilise la **tangente** :
   $$\tan(\widehat{B}) = \frac{FP}{PB} = \frac{42}{110}$$
4. On utilise la fonction inverse $\arctan$ (ou $\tan^{-1}$) sur la calculatrice :
   $$\widehat{B} = \arctan\left(\frac{42}{110}\right) \approx \arctan(0{,}3818) \approx 20{,}899^\circ$$
   Le marin voit le sommet de la falaise sous un angle d'élévation d'environ **$20{,}9^\circ$**.

---

#### Exemple résolu 4 — Déterminer toutes les caractéristiques d'un triangle (« Résoudre » le triangle)
Soit un triangle $ABC$ rectangle en $A$ tel que $BC = 13\text{ cm}$ et $AB = 5\text{ cm}$.
1. Calcule la valeur exacte de la longueur $AC$.
2. Détermine la valeur exacte de $\cos(\widehat{B})$, puis la mesure arrondie au degré près de l'angle $\widehat{B}$.
3. Déduis-en sans nouveau calcul trigonométrique la mesure de l'angle $\widehat{C}$.

*Solution rédigée :*
1. D'après le théorème de Pythagore dans le triangle $ABC$ rectangle en $A$ :
   $$BC^2 = AB^2 + AC^2 \implies 13^2 = 5^2 + AC^2 \implies 169 = 25 + AC^2$$
   $$AC^2 = 169 - 25 = 144 \implies AC = \sqrt{144} = 12\text{ cm}.$$
2. Dans le triangle rectangle en $A$, par rapport à l'angle $\widehat{B}$ :
   $$\cos(\widehat{B}) = \frac{AB}{BC} = \frac{5}{13}$$
   À la calculatrice : $\widehat{B} = \arccos\left(\frac{5}{13}\right) \approx 67{,}38^\circ$, soit **$67^\circ$** au degré près.
3. Dans un triangle rectangle, les deux angles aigus sont complémentaires (leur somme vaut $90^\circ$) :
   $$\widehat{C} = 90^\circ - \widehat{B} \approx 90^\circ - 67{,}38^\circ \approx 22{,}62^\circ \approx \mathbf{23^\circ}.$$

---

#### Exemple résolu 5 — Trouver le sinus à partir du cosinus sans calculer l'angle
Un angle aigu noté $x$ vérifie $\cos(x) = \dfrac{3}{5} = 0{,}6$.
Calcule la valeur exacte de $\sin(x)$, puis celle de $\tan(x)$, sans jamais utiliser la touche $\arccos$ de la calculatrice.

*Solution rédigée :*
1. On utilise la relation fondamentale $\cos^2(x) + \sin^2(x) = 1$ :
   $$\left(\frac{3}{5}\right)^2 + \sin^2(x) = 1 \implies \frac{9}{25} + \sin^2(x) = 1$$
   $$\sin^2(x) = 1 - \frac{9}{25} = \frac{25 - 9}{25} = \frac{16}{25}$$
   Puisque $x$ est un angle aigu, son sinus est positif :
   $$\sin(x) = \sqrt{\frac{16}{25}} = \frac{4}{5} = \mathbf{0{,}8}.$$
2. On utilise la relation du quotient $\tan(x) = \frac{\sin(x)}{\cos(x)}$ :
   $$\tan(x) = \frac{\frac{4}{5}}{\frac{3}{5}} = \frac{4}{5} \times \frac{5}{3} = \frac{4}{3} \approx \mathbf{1{,}333...}$$
C'est exactement le célèbre triangle rectangle égyptien de côtés 3, 4 et 5 !

---

### Ce qu'il faut retenir

1. **Le vocabulaire dans le triangle rectangle :**
   - **Hypoténuse** : en face de l'angle droit, le plus grand côté.
   - **Côté adjacent** à un angle aigu : touche cet angle (côté de l'angle droit).
   - **Côté opposé** à un angle aigu : en face de cet angle.

2. **Les formules magiques (CAH-SOH-TOA) :**
   $$\cos(\text{angle}) = \frac{\text{Adjacent}}{\text{Hypoténuse}} \qquad \sin(\text{angle}) = \frac{\text{Opposé}}{\text{Hypoténuse}} \qquad \tan(\text{angle}) = \frac{\text{Opposé}}{\text{Adjacent}}$$

3. **Propriétés indispensables :**
   - Pour tout angle aigu d'un triangle rectangle : $0 < \cos(x) < 1$ et $0 < \sin(x) < 1$.
   - Formule fondamentale : $\cos^2(x) + \sin^2(x) = 1$.
   - Formule du quotient : $\tan(x) = \frac{\sin(x)}{\cos(x)}$.
   - Angles complémentaires : si $\alpha + \beta = 90^\circ$, alors $\cos(\alpha) = \sin(\beta)$ et $\sin(\alpha) = \cos(\beta)$.

4. **Méthode d'utilisation de la calculatrice :**
   - Vérifier impérativement le mode **Degrés (DEG)**.
   - Pour trouver une longueur : utiliser `cos`, `sin` ou `tan`.
   - Pour trouver un angle : utiliser `arccos` ($\cos^{-1}$), `arcsin` ($\sin^{-1}$) ou `arctan` ($\tan^{-1}$).

---

### Exercices

#### Niveau ★ : Application directe

**Exercice 1.**
Dans un triangle $DEF$ rectangle en $D$, nomme :
1. L'hypoténuse.
2. Le côté adjacent à l'angle $\widehat{E}$.
3. Le côté opposé à l'angle $\widehat{E}$.
4. Écris les rapports $\cos(\widehat{E})$, $\sin(\widehat{E})$ et $\tan(\widehat{E})$ avec les lettres des sommets.

**Exercice 2.**
À l'aide de ta calculatrice en mode Degrés, donne une valeur arrondie au millième de :
a) $\cos(25^\circ)$
b) $\sin(70^\circ)$
c) $\tan(12^\circ)$
d) $\tan(85^\circ)$

**Exercice 3.**
Trouve la mesure de l'angle aigu $x$ arrondie au dixième de degré près sachant que :
a) $\cos(x) = 0{,}72$
b) $\sin(x) = 0{,}35$
c) $\tan(x) = 1{,}8$
d) $\cos(x) = \frac{\sqrt{2}}{2}$

**Exercice 4.**
Soit un triangle $ABC$ rectangle en $B$ tel que $AB = 6\text{ cm}$ et $AC = 10\text{ cm}$.
Calcule la valeur exacte de $\cos(\widehat{A})$, puis déduis-en la mesure de l'angle $\widehat{A}$ arrondie au degré.

**Exercice 5.**
Dans un triangle $MNO$ rectangle en $N$, on sait que $MO = 12\text{ cm}$ et $\widehat{M} = 30^\circ$.
Calcule la longueur exacte de $[NO]$.

---

#### Niveau ★★ : Réflexion et situations concrètes

**Exercice 6 (La rampe d'accès).**
Une norme impose que les rampes d'accès pour fauteuils roulants ne fassent pas un angle supérieur à $5^\circ$ avec l'horizontale.
Une rampe a une longueur de 4 mètres et permet d'atteindre un perron situé à 40 cm de hauteur.
Cette rampe est-elle conforme à la réglementation ? Justifie par un calcul.

**Exercice 7 (L'arbre abattu par la foudre).**
Lors d'une tempête, un arbre vertical de 15 mètres de haut a été brisé en deux par la foudre. Le haut de l'arbre s'est couché sans se détacher du tronc restant : sa cime touche le sol en formant un angle de $28^\circ$ avec le sol horizontal.
À quelle hauteur le tronc s'est-il brisé ? (Arrondir au centimètre près).

**Exercice 8 (La traversée du fleuve).**
Un géomètre se tient sur la berge d'un fleuve au point $A$, exactement en face d'un arbre remarquable $C$ situé sur la berge opposée (le segment $[AC]$ est perpendiculaire aux deux berges parallèles).
Il marche de 50 mètres le long de la berge en ligne droite jusqu'à un point $B$. Depuis ce point $B$, il vise l'arbre $C$ et mesure au théodolite un angle $\widehat{ABC} = 38^\circ$.
Quelle est la largeur du fleuve, arrondie au mètre près ?

**Exercice 9 (Le losange et ses diagonales).**
Un losange $ABCD$ a des côtés de longueur 8 cm. L'un de ses angles intérieurs mesure $50^\circ$.
Rappelle les propriétés des diagonales d'un losange, puis calcule la longueur exacte de chacune des deux diagonales (arrondie au millimètre près).

**Exercice 10 (L'avion en phase de descente).**
Un avion de ligne vole à une altitude de 9 000 mètres à une vitesse constante de 720 km/h. Il entame sa descente vers la piste d'atterrissage selon un angle constant de $3^\circ$ par rapport à l'horizontale.
1. Quelle distance en vol (le long de sa trajectoire inclinée) doit-il parcourir pour toucher le sol ?
2. Combien de temps dure cette descente, en minutes et secondes ?

**Exercice 11 (Relations trigonométriques).**
Un angle aigu $\alpha$ vérifie $\sin(\alpha) = \dfrac{5}{13}$.
1. Sans calculer la mesure de l'angle $\alpha$, utilise la relation fondamentale pour déterminer la valeur exacte de $\cos(\alpha)$ sous forme de fraction irréductible.
2. Détermine ensuite la valeur exacte de $\tan(\alpha)$.
3. Vérifie tes résultats à l'aide de la calculatrice.

---

#### Niveau ★★★ : Défis et problèmes d'approfondissement

**Exercice 12 (La mesure de la tour inaccessible).**
Pour mesurer la hauteur d'une tour médiévale entourée de douves infranchissables, un arpenteur se place au point $A$ et mesure un angle de visée de $32^\circ$ vers le sommet de la tour.
Il recule ensuite de 25 mètres en ligne droite sur le sol plat jusqu'au point $B$, où le nouvel angle de visée vers le sommet n'est plus que de $24^\circ$.
Soit $h$ la hauteur de la tour et $x$ la distance entre le pied de la tour et le point $A$.
1. Exprime $x$ en fonction de $h$ et de $\tan(32^\circ)$.
2. Exprime $x + 25$ en fonction de $h$ et de $\tan(24^\circ)$.
3. En déduisant une équation d'inconnue $h$, calcule la hauteur de la tour au décimètre près.

**Exercice 13 (La mesure du gnomon d'Ératosthène).**
À Alexandrie, Ératosthène a planté un gnomon de 1 mètre de hauteur. L'ombre mesurée au sol mesurait environ 12,6 cm.
1. Calcule l'angle formé par les rayons du soleil avec le bâton vertical.
2. Retrouve-t-on bien la valeur historique de $7{,}2^\circ$ ?

**Exercice 14 (Formule de l'aire d'un triangle quelconque).**
Soit un triangle quelconque $ABC$ où l'on connaît deux côtés $AB = c$, $AC = b$, et l'angle aigu $\widehat{A}$ formé par ces deux côtés.
Soit $H$ le pied de la hauteur issue de $C$.
1. Dans le triangle $ACH$ rectangle en $H$, exprime la hauteur $CH$ en fonction de $b$ et de $\sin(\widehat{A})$.
2. Démontre la célèbre formule de l'aire :
   $$\text{Aire}(ABC) = \frac{1}{2} b c \sin(\widehat{A})$$
3. Calcule l'aire d'un triangle dont deux côtés mesurent 7 cm et 10 cm, formant un angle de $40^\circ$.

**Exercice 15 (Le triangle rectangle isocèle et les valeurs remarquables).**
Considère un carré $ABCD$ de côté 1. On trace la diagonale $[AC]$.
1. Quelle est la nature exacte du triangle $ABC$ ? Quelle est la mesure de ses angles aigus ?
2. Calcule la longueur exacte de la diagonale $[AC]$ à l'aide du théorème de Pythagore.
3. Déduis-en les valeurs exactes de $\cos(45^\circ)$, $\sin(45^\circ)$ et $\tan(45^\circ)$.

---

### Solutions

#### Solutions des exercices ★

- **Exercice 1 :** 1. Hypoténuse : $[EF]$. 2. Côté adjacent à $\widehat{E}$ : $[DE]$. 3. Côté opposé à $\widehat{E}$ : $[DF]$. 4. $\cos(\widehat{E}) = \frac{DE}{EF}$, $\sin(\widehat{E}) = \frac{DF}{EF}$, $\tan(\widehat{E}) = \frac{DF}{DE}$.
- **Exercice 2 :** a) $\approx 0{,}906$ ; b) $\approx 0{,}940$ ; c) $\approx 0{,}213$ ; d) $\approx 11{,}430$.
- **Exercice 3 :** a) $x = \arccos(0{,}72) \approx 43{,}9^\circ$ ; b) $x = \arcsin(0{,}35) \approx 20{,}5^\circ$ ; c) $x = \arctan(1{,}8) \approx 60{,}9^\circ$ ; d) $x = 45^\circ$ car $\cos(45^\circ) = \frac{\sqrt{2}}{2}$.
- **Exercice 4 :** $\cos(\widehat{A}) = \frac{AB}{AC} = \frac{6}{10} = 0{,}6$. À la calculatrice, $\widehat{A} = \arccos(0{,}6) \approx 53^\circ$.
- **Exercice 5 :** Dans $MNO$ rectangle en $N$, $\sin(\widehat{M}) = \frac{NO}{MO} \implies \sin(30^\circ) = \frac{NO}{12}$. Comme $\sin(30^\circ) = 0{,}5$, $NO = 12 \times 0{,}5 = 6\text{ cm}$.

---

#### Solutions détaillées des exercices ★★

- **Exercice 6 (La rampe d'accès) :**
  Soit $\alpha$ l'angle de la rampe avec l'horizontale. La rampe forme l'hypoténuse ($4\text{ m} = 400\text{ cm}$) et la hauteur du perron forme le côté opposé ($40\text{ cm}$).
  Dans ce triangle rectangle :
  $$\sin(\alpha) = \frac{\text{opposé}}{\text{hypoténuse}} = \frac{40}{400} = 0{,}1$$
  À la calculatrice : $\alpha = \arcsin(0{,}1) \approx 5{,}74^\circ$.
  Puisque $5{,}74^\circ > 5^\circ$, la pente est trop raide : **la rampe n'est pas conforme** à la réglementation.

- **Exercice 7 (L'arbre abattu) :**
  Soit $h$ la hauteur du tronc encore debout (côté opposé à l'angle de $28^\circ$).
  La partie brisée couchée forme l'hypoténuse de longueur $L$.
  La hauteur totale initiale de l'arbre est $h + L = 15$, d'où $L = 15 - h$.
  Dans le triangle rectangle formé avec le sol :
  $$\sin(28^\circ) = \frac{h}{L} = \frac{h}{15 - h}$$
  En multipliant par $(15 - h)$ :
  $$(15 - h) \times \sin(28^\circ) = h \implies 15 \sin(28^\circ) - h \sin(28^\circ) = h$$
  $$15 \sin(28^\circ) = h(1 + \sin(28^\circ)) \implies h = \frac{15 \sin(28^\circ)}{1 + \sin(28^\circ)}$$
  Comme $\sin(28^\circ) \approx 0{,}46947$ :
  $$h \approx \frac{15 \times 0{,}46947}{1 + 0{,}46947} = \frac{7{,}042}{1{,}46947} \approx 4{,}79\text{ m}.$$
  Le tronc s'est brisé à environ **4,79 mètres** de hauteur (et la cime mesure $15 - 4{,}79 = 10{,}21$ m).

- **Exercice 8 (La traversée du fleuve) :**
  Le triangle $ABC$ est rectangle en $A$. L'arbre est en $C$, l'observateur initial en $A$ et il a marché jusqu'en $B$ ($AB = 50\text{ m}$).
  Par rapport à l'angle $\widehat{B} = 38^\circ$, $[AC]$ est le côté opposé (la largeur du fleuve) et $[AB]$ est le côté adjacent ($50\text{ m}$).
  $$\tan(38^\circ) = \frac{AC}{AB} = \frac{AC}{50} \implies AC = 50 \times \tan(38^\circ)$$
  $\tan(38^\circ) \approx 0{,}781286$, d'où $AC \approx 50 \times 0{,}781286 \approx 39{,}06\text{ m}$.
  Le fleuve a une largeur d'environ **39 mètres**.

- **Exercice 9 (Le losange) :**
  Rappel : les diagonales d'un losange se coupent en leur milieu en formant un angle droit, et elles sont les bissectrices des angles intérieurs.
  Soit $O$ le centre du losange. Le triangle $AOB$ est rectangle en $O$. L'hypoténuse est le côté $AB = 8\text{ cm}$.
  L'angle en $A$ vaut la moitié de $50^\circ$, soit $\widehat{OAB} = 25^\circ$.
  - Côté adjacent $OA$ : $\cos(25^\circ) = \frac{OA}{AB} \implies OA = 8 \times \cos(25^\circ) \approx 7{,}2505\text{ cm}$.
    La grande diagonale mesure donc $AC = 2 \times OA \approx \mathbf{14{,}5\text{ cm}}$.
  - Côté opposé $OB$ : $\sin(25^\circ) = \frac{OB}{AB} \implies OB = 8 \times \sin(25^\circ) \approx 3{,}3809\text{ cm}$.
    La petite diagonale mesure donc $BD = 2 \times OB \approx \mathbf{6{,}8\text{ cm}}$.

- **Exercice 10 (L'avion en descente) :**
  1. Le triangle rectangle formé par l'altitude verticale ($9\,000\text{ m}$), la distance au sol et la trajectoire de l'avion a un angle d'inclinaison de $3^\circ$.
     L'altitude est le côté opposé à l'angle de $3^\circ$, et la trajectoire est l'hypoténuse $D$.
     $$\sin(3^\circ) = \frac{9\,000}{D} \implies D = \frac{9\,000}{\sin(3^\circ)} \approx \frac{9\,000}{0{,}052336} \approx 171\,966\text{ mètres} \approx \mathbf{172\text{ km}}.$$
  2. La vitesse de l'avion est $720\text{ km/h} = \frac{720\,000\text{ m}}{3\,600\text{ s}} = 200\text{ m/s}$.
     Le temps de vol est $t = \frac{D}{v} = \frac{171\,966}{200} \approx 859{,}8\text{ secondes}$.
     Comme $859{,}8 \div 60 \approx 14{,}33$ min, cela donne **14 minutes et 20 secondes**.

- **Exercice 11 (Relations fondamentales) :**
  1. $\cos^2(\alpha) = 1 - \sin^2(\alpha) = 1 - \left(\frac{5}{13}\right)^2 = 1 - \frac{25}{169} = \frac{144}{169}$.
     Comme $\alpha$ est aigu, $\cos(\alpha) = \sqrt{\frac{144}{169}} = \mathbf{\frac{12}{13}}$.
  2. $\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)} = \frac{5/13}{12/13} = \mathbf{\frac{5}{12}}$.
  3. Vérification : $\arcsin(5/13) \approx 22{,}62^\circ$. $\cos(22{,}62^\circ) \approx 0{,}923 \approx 12/13$. Tout concorde parfaitement.

---

#### Solutions détaillées des exercices ★★★

- **Exercice 12 (La tour inaccessible) :**
  1. Dans le triangle rectangle formé par la tour et le point $A$ : $\tan(32^\circ) = \frac{h}{x} \implies x = \frac{h}{\tan(32^\circ)}$.
  2. Dans le triangle rectangle formé par la tour et le point $B$ : $\tan(24^\circ) = \frac{h}{x + 25} \implies x + 25 = \frac{h}{\tan(24^\circ)}$.
  3. En soustrayant les deux expressions :
     $$(x + 25) - x = \frac{h}{\tan(24^\circ)} - \frac{h}{\tan(32^\circ)} \implies 25 = h \left(\frac{1}{\tan(24^\circ)} - \frac{1}{\tan(32^\circ)}\right)$$
     Calculons les valeurs :
     $\tan(24^\circ) \approx 0{,}44523 \implies \frac{1}{\tan(24^\circ)} \approx 2{,}2460$
     $\tan(32^\circ) \approx 0{,}62487 \implies \frac{1}{\tan(32^\circ)} \approx 1{,}6003$
     La différence vaut $2{,}2460 - 1{,}6003 = 0{,}6457$.
     D'où :
     $$h = \frac{25}{0{,}6457} \approx \mathbf{38{,}7\text{ mètres}}.$$
     La tour mesure environ **38,7 mètres**.

- **Exercice 13 (Le gnomon d'Ératosthène) :**
  1. Le bâton a une hauteur de $1\text{ m} = 100\text{ cm}$ (côté adjacent) et l'ombre au sol mesure $12{,}6\text{ cm}$ (côté opposé).
     $$\tan(\alpha) = \frac{12{,}6}{100} = 0{,}126$$
     À la calculatrice : $\alpha = \arctan(0{,}126) \approx 7{,}18^\circ$.
  2. En arrondissant au dixième, on trouve bien **$7{,}2^\circ$**, exactement la valeur mesurée par Ératosthène !

- **Exercice 14 (L'aire d'un triangle quelconque) :**
  1. Dans le triangle $ACH$ rectangle en $H$, par rapport à l'angle aigu $\widehat{A}$ : $\sin(\widehat{A}) = \frac{CH}{AC} = \frac{CH}{b} \implies CH = b \sin(\widehat{A})$.
  2. L'aire du triangle $ABC$ est donnée par $\frac{1}{2} \times \text{base} \times \text{hauteur} = \frac{1}{2} \times AB \times CH$.
     En remplaçant $AB$ par $c$ et $CH$ par $b \sin(\widehat{A})$ :
     $$\text{Aire} = \frac{1}{2} b c \sin(\widehat{A}).$$
  3. Pour $b = 7$, $c = 10$, $\widehat{A} = 40^\circ$ :
     $$\text{Aire} = \frac{1}{2} \times 7 \times 10 \times \sin(40^\circ) = 35 \times \sin(40^\circ) \approx 35 \times 0{,}64279 \approx \mathbf{22{,}5\text{ cm}^2}.$$

- **Exercice 15 (Le demi-carré et 45°) :**
  1. Le triangle $ABC$ a deux côtés de même longueur ($AB = BC = 1$) et un angle droit en $B$ : c'est un **triangle rectangle isocèle**. Ses deux angles aigus sont égaux et valent $(180^\circ - 90^\circ) / 2 = \mathbf{45^\circ}$.
  2. D'après le théorème de Pythagore : $AC^2 = AB^2 + BC^2 = 1^2 + 1^2 = 2 \implies AC = \mathbf{\sqrt{2}}$.
  3. Dans ce triangle :
     - $\cos(45^\circ) = \frac{\text{adjacent}}{\text{hypoténuse}} = \frac{1}{\sqrt{2}} = \mathbf{\frac{\sqrt{2}}{2}} \approx 0{,}707$.
     - $\sin(45^\circ) = \frac{\text{opposé}}{\text{hypoténuse}} = \frac{1}{\sqrt{2}} = \mathbf{\frac{\sqrt{2}}{2}} \approx 0{,}707$.
     - $\tan(45^\circ) = \frac{\text{opposé}}{\text{adjacent}} = \frac{1}{1} = \mathbf{1}$.

---

### La question qui ouvre la suite

Grâce à la trigonométrie, nous avons appris à arpenter l'espace continu, les angles célestes et les distances inaccessibles de la Terre. Mais que se passe-t-il si l'on quitte le monde des longueurs qui s'étirent pour revenir au monde des objets **entiers et indivisibles** ?

Comment carreler un sol rectangulaire avec des dalles carrées sans découper la moindre chute de marbre ? Comment répartir des trésors en parts rigoureusement égales sans casser une seule pièce ? 
C'est à Alexandrie, un siècle avant Ératosthène, qu'un autre géant de la pensée a gravé les règles éternelles du partage parfait. Prépare-toi à découvrir le secret des diviseurs et l'algorithme immortel d'**Euclide**.
