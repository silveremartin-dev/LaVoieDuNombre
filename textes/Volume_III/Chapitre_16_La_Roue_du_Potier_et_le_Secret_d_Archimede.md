# VOLUME III — L'ÂGE DES ARPENTEURS ET DES BÂTISSEURS (10 - 13 ans / CM2 - 6e - 5e)
## CHAPITRE 16 : La Roue du Potier et le Secret d'Archimède

> *« Tout polygone à angles droits se laisse enfermer dans un quadrillage. Mais la courbe du cercle glisse entre les doigts de l'arpenteur. Pour mesurer l'anneau parfait, il fallait dérouler la circonférence sur la terre et découvrir ce nombre mystérieux, sans fin et sans répétition, que les sages de Syracuse ont traqué entre deux armées de polygones. »*

---

### Ce que tu vas découvrir

- La différence essentielle entre le **cercle** (la ligne du contour) et le **disque** (la surface pleine).
- Le vocabulaire de la rondeur : **centre**, **rayon**, **diamètre**, **corde** et **arc**.
- L'expérience du roulement et la constante magique : pourquoi le rapport du périmètre sur le diamètre donne toujours le même nombre $\pi \approx 3{,}14159\dots$
- L'incroyable exploit d'**Archimède de Syracuse** et sa méthode des polygones à 96 côtés.
- Les deux formules indispensables : le périmètre du cercle ($P = 2\pi r$) et l'aire du disque ($A = \pi r^2$), démontrée en transformant un disque en quasi-rectangle !

---

### 1. Le problème : la jante du char et le pot de terre

Tu as onze ans. Après avoir exploré les angles droits des arpenteurs d'Égypte au chapitre précédent, promenons-nous dans l'atelier d'un artisan de l'Antiquité.

Dans un coin sombre de l'échoppe, une roue lourde en bois tourne à plat sur un pivot de fer. C'est le **tour du potier**. L'artisan jette une motte d'argile grise au centre exact du plateau en mouvement. Ses mains mouillées effleurent la terre. Sous ses doigts, comme par enchantement, la masse informe s'évase en une coupe parfaitement ronde.

```
                  Tour du potier en rotation
                         ___________
                     .-'     O     '-.
                   .'   . - ' ' - .   '.
                  /   /      r      \   \
                 |   |       ●───────|---|  <- main du potier
                  \   \             /   /
                   '.   ' - . . - '   .'
                     '-.___________.-'
                             |
                             | pivot
```

Chaque point du bord extérieur de la coupe tourne à la même distance du pivot central. Si un côté était plus éloigné que l'autre, la coupe se déformerait et s'effondrerait immédiatement.

Le lendemain, le forgeron du village voisin fait face à un casse-tête bien plus rude. Il doit fabriquer une **jante en fer** pour entourer la grande roue de bois d'un char de combat. Cette bande de fer doit être forgée droite sur l'enclume, puis courbée en cercle chaud et emboîtée au millimètre près autour de la roue.
- Si le forgeron coupe une bande de fer trop courte de deux centimètres, elle ne fermera jamais le tour de la roue.
- S'il coupe une bande trop longue de deux centimètres, la jante flottera autour du bois et la roue éclatera au premier caillou sur la route.

Le forgeron mesure la largeur de sa roue : elle fait exactement **1 mètre de part en part**, en passant par le centre. 
Quelle longueur exacte de fer doit-il couper ?

Il prend une cordelette, tente de la plaquer sur le bord courbé de la roue, mais la cordelette glisse, s'étire et se détend. L'artisan peste :
*« Pourquoi est-il si facile de mesurer un carré ou un triangle avec une règle droite, et si difficile de mesurer la ligne courbe d'un cercle ? »*

Pour répondre à cette question, il faut faire ce que les premiers géomètres ont fait : faire rouler le cercle sur le sol.

---

### 2. Le vocabulaire du cercle et du disque

Avant de dérouler notre roue, mettons de l'ordre dans les mots. La langue française est très précise, et confondre ces termes est le piège le plus fréquent des débutants.

#### 2.1 Cercle ou disque ?

> **📐 Définition — Cercle et Disque**
> - Le **cercle** de centre $O$ et de rayon $r$ est l'ensemble de tous les points du plan situés à la même distance $r$ du point $O$. Le cercle est **une ligne courbe fermée**, c'est le bord vide (comme une alliance, un cerceau ou un anneau de fer).
> - Le **disque** de centre $O$ et de rayon $r$ est l'ensemble de tous les points du plan situés à une distance inférieure ou égale à $r$ du point $O$. Le disque est **une surface pleine** (comme une pièce de monnaie, une assiette ou une crêpe).

```
          LE CERCLE (la ligne)              LE DISQUE (la surface pleine)
                 .-""""-.                              .######.
               .'        '.                          .##########.
              /            \                        /############\
             |      O       |                      |###### O #####|
              \            /                        \############/
               '.        .'                          '##########'
                 '-....-'                              '######'
             (Périmètre seul)                        (Aire et Périmètre)
```

#### 2.2 Les segments et les lignes remarquables

Posons un point $O$ sur une feuille.

```
                             B
                            /
                           /   Rayon r
                          /
               A ────────●──────── B'
                 |       O       |
                 |<── Diamètre d ─►|
                        /
                       / Arc CD
                      C ─────── D
                         Corde
```

- Le **centre** : le point fixe $O$ situé au milieu exact de la figure.
- Le **rayon** : c'est à la fois le segment $[OB]$ qui relie le centre à un point du cercle, et la **longueur** $r = OB$ de ce segment. Tous les rayons d'un même cercle ont rigoureusement la même longueur.
- Le **diamètre** : c'est un segment $[AB']$ passant par le centre $O$ et joignant deux points opposés du cercle. Sa longueur se note souvent $d$. Comme il est formé de deux rayons bout à bout ($[AO]$ et $[OB']$), on a la relation fondamentale :
  $$d = 2 \times r \quad \text{ou} \quad r = \frac{d}{2}$$
- Une **corde** : un segment $[CD]$ qui relie deux points quelconques du cercle sans nécessairement passer par le centre. Le diamètre est simplement la plus longue de toutes les cordes possibles.
- Un **arc de cercle** : une portion de la courbe comprise entre deux points, notée $\wideparen{CD}$.

> **💡 Le savais-tu ?** Le mot *rayon* vient du latin *radius*, qui désignait le rayon d'une roue de charrette ou la baguette d'un devin. Le mot *diamètre* vient du grec *dia* (« à travers ») et *metron* (« mesure ») : c'est la mesure « de part en part » qui traverse la figure.

---

### 3. L'expérience du roulement et la constante magique

Revenons au forgeron et à sa roue. Imaginons une expérience très simple que tu peux réaliser chez toi avec une pièce de monnaie, un rouleau de ruban adhésif ou une boîte de conserve :

1. Prends un feutre et fais une petite marque rouge sur le bord de ta boîte cylindrique.
2. Pose la boîte sur une longue feuille de papier blanc posée au sol, de manière à ce que la marque rouge touche le bord gradué de ta règle au point $0$.
3. Fais rouler la boîte en ligne droite, sans qu'elle glisse, jusqu'à ce que la marque rouge touche à nouveau le sol après avoir fait **exactement un tour complet**.
4. Mesure la distance parcourue sur la règle : c'est la longueur du tour de la boîte, c'est-à-dire le **périmètre** de la boîte (aussi appelé **circonférence**).

```
   Départ (0 cm)                                     Arrivée (1 tour complet)
        |                                                        |
      ( O ● )                                                  ( O ● )
     ═══╧════════════════════════════════════════════════════════╧═════════
     0 cm                                                    Périmètre P
```

Faisons cette mesure avec des objets ronds de tailles très différentes :

| Objet mesuré | Diamètre $d$ mesuré | Périmètre $P$ mesuré | Rapport $\frac{P}{d}$ (division) |
|---|---|---|---|
| Pièce de 2 euros | $2{,}57\text{ cm}$ | $8{,}07\text{ cm}$ | $\frac{8{,}07}{2{,}57} \approx 3{,}140$ |
| Rouleau de ruban adhésif | $8{,}00\text{ cm}$ | $25{,}13\text{ cm}$ | $\frac{25{,}13}{8{,}00} \approx 3{,}141$ |
| Assiette ronde | $22{,}00\text{ cm}$ | $69{,}10\text{ cm}$ | $\frac{69{,}10}{22{,}00} \approx 3{,}141$ |
| Roue de bicyclette | $68{,}00\text{ cm}$ | $213{,}60\text{ cm}$ | $\frac{213{,}60}{68{,}00} \approx 3{,}141$ |

Regarde la dernière colonne avec attention : **le résultat de la division $\frac{P}{d}$ donne toujours le même nombre, environ $3{,}14$ !**
Que l'objet soit minuscule comme une tête d'épingle ou gigantesque comme la trajectoire de la Lune autour de la Terre, **le contour d'un cercle fait toujours un peu plus de trois fois son diamètre**.

Ce rapport constant ne dépend pas de la taille de l'objet : c'est une constante universelle de la géométrie de notre univers. Les mathématiciens lui ont donné le nom de la lettre grecque **$\pi$** (qui se prononce *« pi »*).

> **📐 La constante $\pi$ —**
> Pour tout cercle de périmètre $P$ et de diamètre $d$ :
> $$\frac{P}{d} = \pi \approx 3{,}1415926535\dots$$

Par conséquent, si l'on multiplie les deux côtés par le diamètre $d$, on obtient la célèbre formule du **périmètre du cercle** :
$$P = \pi \times d = 2 \times \pi \times r$$

On la retient souvent sous la forme chantante : **« Deux $\pi$ $r$ »**.

> **🔍 L'histoire vraie — D'où vient la lettre $\pi$ ?**
> La lettre $\pi$ est la première lettre du mot grec *periphereia* (qui a donné « périphérie » en français, c'est-à-dire le contour). C'est le mathématicien gallois William Jones qui l'a utilisée pour la première fois en 1706 dans un livre d'enseignement, mais c'est le géant suisse **Leonhard Euler** qui l'a rendue mondialement célèbre à partir de 1737 en l'adoptant dans tous ses traités.

---

### 4. Le secret d'Archimède : dompter le cercle avec des polygones

Les Babyloniens et les Égyptiens savaient déjà que le périmètre valait environ trois fois le diamètre. Les Égyptiens utilisaient une approximation proche de $\left(\frac{16}{9}\right)^2 \approx 3{,}16$, et la Bible (dans le premier livre des Rois) évoque un grand bassin circulaire de bronze de 10 coudées de diamètre et 30 coudées de circonférence ($\pi \approx 3$).

Mais personne ne savait calculer la valeur exacte de ce nombre avec certitude. C'est alors qu'entre en scène le plus grand génie scientifique de l'Antiquité : **Archimède de Syracuse** (vers 287 – 212 avant J.-C.).

#### 4.1 L'idée de génie : la cage aux polygones

Archimède se dit : *« Je ne sais pas mesurer une courbe directement. En revanche, je sais parfaitement calculer le périmètre d'une figure droite avec des côtés droits : un polygone régulier ! »*

Archimède imagine donc deux polygones réguliers qui emprisonnent le cercle comme dans un étau :
1. Un polygone **inscrit** (situé entièrement **à l'intérieur** du cercle, dont les sommets touchent le cercle).
2. Un polygone **circonscrit** (situé entièrement **à l'extérieur** du cercle, dont les côtés touchent le cercle).

```
         Polygone inscrit (intérieur)       Polygone circonscrit (extérieur)
                  .---.                             .-------.
                /   |   \                          / |     | \
               /    |    \                        /  |     |  \
              |─────●─────|                      |───●─────●───|
               \    |    /                        \  |     |  /
                \   |   /                          \ |     | /
                  '---'                             '-------'
         Périmètre intérieur < Périmètre cercle < Périmètre extérieur
```

C'est une évidence physique :
- Le chemin qui longe le polygone intérieur est plus court que le tour du cercle.
- Le chemin qui longe le polygone extérieur est plus long que le tour du cercle.

Donc :
$$\text{Périmètre du polygone inscrit} < P_{\text{cercle}} < \text{Périmètre du polygone circonscrit}$$

En divisant chaque terme par le diamètre, Archimède obtient un **encadrement** rigoureux de $\pi$ !

#### 4.2 L'escalade des 96 côtés

Archimède commence avec des hexagones réguliers (6 côtés). Il calcule précisément leurs périmètres grâce au théorème de Pythagore.
Puis, par une formule géométrique remarquable qu'il invente, il **double** le nombre de côtés :
- Polygones à 12 côtés (dodécagones) ;
- Polygones à 24 côtés ;
- Polygones à 48 côtés ;
- Et enfin, polygones à **96 côtés** !

Imagine le travail colossal : à 96 côtés, le polygone intérieur et le polygone extérieur collent tellement au cercle qu'à l'œil nu, il est impossible de voir la moindre différence entre la ligne brisée et la courbe.

Au terme de calculs manuels héroïques sur des fractions et des racines carrées, Archimède établit son résultat historique :
$$\frac{223}{71} < \pi < \frac{22}{7}$$

En calculant les valeurs décimales de ces deux fractions :
$$3{,}140845\dots < \pi < 3{,}142857\dots$$

Grâce à Archimède, le monde savait désormais sans l'ombre d'un doute que $\pi$ commence par **$3{,}14$**.
La fraction supérieure d'Archimède, **$\frac{22}{7}$**, est si commode qu'elle a été utilisée par tous les bâtisseurs et ingénieurs pendant près de deux mille ans pour faire des calculs rapides de tête !

---

### 5. L'aire du disque : transformer un cercle en rectangle

Nous savons maintenant mesurer la ficelle du bord ($P = 2\pi r$). Mais quelle est la **surface** du disque ? Combien de centimètres carrés de peinture faut-il pour recouvrir une table ronde ?

La réponse est donnée par une formule magique :
$$A = \pi \times r^2$$

D'où vient cette formule ? Pourquoi retrouve-t-on le carré du rayon ($r^2$) multiplié par le même nombre $\pi$ ?
Voici une démonstration visuelle d'une beauté à couper le souffle, attribuée à Léonard de Vinci et déjà pressentie par les géomètres grecs.

#### La métaphore de la tarte aux pommes

Imagine un grand disque en pâte à tarte de rayon $r$.
1. Découpons ce disque en un grand nombre de parts égales très fines (par exemple 16 parts, comme des pointes de flèches).
2. Séparons ces 16 parts et disposons-les alternativement, une pointe en haut, une pointe en bas, en les emboîtant les unes dans les autres :

```
          Disque découpé en parts                Parts réassemblées tête-bêche
                 .-""""-.                              /\/\/\/\/\/\/\/\
               .'  \  /  '.                           |                |  hauteur ≈ r
              /  \  \/  /  \                           \/\/\/\/\/\/\/\/
             |----\----/---|                           |◄──────────────►|
              \  /  /\  \  /                             base ≈ 1/2 P
               '.  /  \  .'
                 '-....-'
```

Regarde la nouvelle figure obtenue : elle ressemble étrangement à un **rectangle** (ou un parallélogramme presque parfait) !
- Quelle est la **hauteur** de ce rectangle ? C'est la longueur d'une part de tarte, c'est-à-dire le **rayon $r$** du cercle.
- Quelle est la **base** de ce rectangle ? Le bord ondulé supérieur est composé de la moitié des arcs des parts, et le bord inférieur de l'autre moitié. La base mesure donc la **moitié du périmètre du cercle** :
  $$\text{Base} = \frac{1}{2} \times P = \frac{1}{2} \times (2 \pi r) = \pi r$$

Quelle est l'aire de ce rectangle ?
$$\text{Aire} = \text{base} \times \text{hauteur} = (\pi r) \times r = \pi r^2$$

Si au lieu de 16 parts, nous découpons le disque en 100 parts, 1 000 parts, 1 000 000 de parts infiniment fines, les petites pointes ondulées deviennent absolument plates et droites : la figure devient un véritable rectangle parfait d'aire $\pi r^2$.

> **📐 Théorème — Aire du disque**
> L'aire $A$ d'un disque de rayon $r$ (et de diamètre $d = 2r$) est égale à :
> $$A = \pi \times r^2 = \pi \times r \times r$$
> En fonction du diamètre $d$ : $A = \pi \times \left(\frac{d}{2}\right)^2 = \frac{\pi \times d^2}{4}$.

---

### 6. Attention aux pièges !

> **⚠️ Attention, piège ! — Les confusions mortelles**
> 1. **Ne confonds pas rayon et diamètre !** Dans un énoncé, surligne immédiatement si l'on te donne le rayon ou le diamètre. Si une roue a un diamètre de $10\text{ cm}$, son rayon est de $5\text{ cm}$. Si tu écris $A = \pi \times 10^2$, ton résultat sera quatre fois trop grand !
> 2. **Ne confonds pas périmètre et aire !**
>    - Le périmètre est une **longueur** (en $\text{m}$, $\text{cm}$, $\text{mm}$) : $P = 2\pi r$. Le rayon y est à la puissance 1.
>    - L'aire est une **surface** (en $\text{m}^2$, $\text{cm}^2$, $\text{mm}^2$) : $A = \pi r^2$. Le rayon y est élevé au carré.
> 3. **Le piège du demi-cercle :** Le périmètre d'un demi-cercle fermé n'est PAS seulement la moitié de $2\pi r$. Il faut lui ajouter le bord plat qui le referme, c'est-à-dire le diamètre !
>    $$P_{\text{demi-disque}} = \pi r + 2r$$
> 4. **$\pi$ n'est ni $3{,}14$, ni $\frac{22}{7}$ !** Ce ne sont que des valeurs approchées très pratiques. Les décimales de $\pi$ se poursuivent à l'infini sans jamais présenter de séquence périodique qui se répète : $\pi = 3{,}141592653589793\dots$ (on dit que $\pi$ est un nombre irrationnel). Quand un problème demande la « valeur exacte », tu dois laisser le symbole $\pi$ dans ta réponse (ex : $16\pi\text{ cm}^2$).

---

### 7. Exemples résolus

#### Exemple résolu 1 — Le cerclage du tonneau
Un viticulteur veut entourer un tonneau circulaire avec un ruban d'acier. Le diamètre du tonneau mesure $80\text{ cm}$.
Quelle longueur de ruban doit-il découper au minimum ? (Prendre $\pi \approx 3{,}14$).

*Solution :*
- On cherche un périmètre. On connaît le diamètre $d = 80\text{ cm}$.
- Formule : $P = \pi \times d$.
- Calcul : $P = \pi \times 80 \approx 3{,}14 \times 80 = 251{,}2\text{ cm}$.
Il doit couper un ruban d'au moins $251{,}2\text{ cm}$ (soit environ $2{,}51\text{ m}$). ✔

#### Exemple résolu 2 — Le compteur de la bicyclette
Le pneu d'un vélo tout-terrain a un rayon $r = 35\text{ cm}$.
1. Quelle distance le vélo parcourt-il lorsque la roue fait exactement un tour complet ?
2. Combien de tours la roue effectue-t-elle pour un trajet de $1{,}1\text{ km}$ ?

*Solution :*
1. La distance parcourue en un tour correspond au périmètre de la roue :
   $$P = 2 \times \pi \times r = 2 \times \pi \times 35 = 70\pi \approx 219{,}91\text{ cm} \approx 2{,}20\text{ m}$$
2. Convertissons la distance totale en mètres : $1{,}1\text{ km} = 1\,100\text{ m}$.
   Nombre de tours :
   $$\text{Nombre de tours} = \frac{\text{Distance totale}}{\text{Périmètre}} = \frac{1\,100}{2{,}20} = 500\text{ tours}$$
   La roue fait exactement 500 tours complets. ✔

#### Exemple résolu 3 — La guerre des pizzas : un dilemme gourmand !
Dans une pizzeria, tu as le choix entre :
- Une **grande pizza** géante de $40\text{ cm}$ de diamètre pour 16 euros.
- Deux **petites pizzas** de $28\text{ cm}$ de diamètre pour 16 euros au total.
Quelle option te donne le plus de pizza à manger pour le même prix ?

*Solution :*
Calculons l'aire consommable dans chaque cas (attention aux rayons !) :
- Pour la grande pizza : le diamètre est de $40\text{ cm}$, donc son rayon est $r_1 = 20\text{ cm}$.
  $$A_1 = \pi \times r_1^2 = \pi \times 20^2 = 400\pi \approx 1\,256{,}6\text{ cm}^2$$
- Pour les deux petites pizzas : le diamètre est de $28\text{ cm}$, donc le rayon est $r_2 = 14\text{ cm}$.
  Aire d'une petite pizza : $A_{\text{petite}} = \pi \times 14^2 = 196\pi \approx 615{,}75\text{ cm}^2$.
  Pour deux petites pizzas :
  $$A_2 = 2 \times 196\pi = 392\pi \approx 1\,231{,}5\text{ cm}^2$$
*Conclusion :* $400\pi > 392\pi$. La grande pizza offre une surface supérieure à celle des deux petites réunies ! Le choix le plus avantageux est donc la grande pizza unique. ✔

#### Exemple résolu 4 — Retrouver le rayon à partir du périmètre ou de l'aire
1. Un arbre centenaire a une circonférence de tronc mesurée à $314\text{ cm}$. Quel est son diamètre ?
2. Une place circulaire a une aire de $706{,}5\text{ m}^2$. Quel est son rayon ? (Prendre $\pi \approx 3{,}14$).

*Solution :*
1. On sait que $P = \pi \times d$, donc :
   $$d = \frac{P}{\pi} \approx \frac{314}{3{,}14} = 100\text{ cm} = 1\text{ m}$$
   Le tronc a un diamètre d'un mètre.
2. On sait que $A = \pi \times r^2$, donc :
   $$r^2 = \frac{A}{\pi} \approx \frac{706{,}5}{3{,}14} = 225$$
   Quel nombre positif multiplié par lui-même donne $225$ ? On cherche la racine carrée : $15 \times 15 = 225$, donc $r = 15\text{ m}$.
   La place a un rayon de 15 mètres. ✔

#### Exemple résolu 5 — La piste d'athlétisme et la couronne circulaire
Un stade d'entraînement possède un parterre central circulaire de pelouse de rayon $R_1 = 30\text{ m}$, entouré d'une piste de course en tartan d'une largeur uniforme de $4\text{ m}$.
Quelle est l'aire de la piste de course ?

```
                   Piste (largeur 4 m)
                     . - - - - - .
                  .'     .---.     '.
                 /     /   R1  \     \
                |     |    ●────|─────|
                 \     \       /     /
                  '.     '---'     .'
                     ' - - - - - '
                         R2 = R1 + 4 m
```

*Solution :*
La surface de la piste forme une **couronne circulaire** : c'est la différence entre le grand disque extérieur et le petit disque intérieur.
- Rayon intérieur : $R_1 = 30\text{ m}$.
- Rayon extérieur : $R_2 = 30 + 4 = 34\text{ m}$.
- Aire du grand disque : $A_{\text{grand}} = \pi \times R_2^2 = \pi \times 34^2 = 1\,156\pi\text{ m}^2$.
- Aire du petit disque : $A_{\text{petit}} = \pi \times R_1^2 = \pi \times 30^2 = 900\pi\text{ m}^2$.
- Aire de la couronne :
  $$A_{\text{piste}} = A_{\text{grand}} - A_{\text{petit}} = 1\,156\pi - 900\pi = 256\pi \approx 256 \times 3{,}1416 \approx 804{,}25\text{ m}^2$$
La piste a une aire d'environ $804{,}25\text{ m}^2$. ✔

---

### Ce qu'il faut retenir

1. **Cercle vs Disque :**
   - Le cercle est la bordure courbe (longueur).
   - Le disque est la surface intérieure (aire).
2. **Rayon et Diamètre :**
   - Le diamètre vaut deux fois le rayon : $d = 2r \iff r = \frac{d}{2}$.
3. **Le nombre $\pi$ :**
   - C'est le quotient invariable du périmètre par le diamètre : $\pi = \frac{P}{d} \approx 3{,}14159\dots$
   - Archimède l'a encadré grâce à des polygones à 96 côtés : $\frac{223}{71} < \pi < \frac{22}{7}$.
4. **Formules fondamentales :**
   - **Périmètre du cercle :** $P = 2 \pi r = \pi d$.
   - **Aire du disque :** $A = \pi r^2 = \frac{\pi d^2}{4}$.
5. **Unités et valeurs exactes :**
   - Conserver $\pi$ pour donner la valeur exacte (ex: $25\pi\text{ cm}^2$).
   - Remplacer $\pi$ par $3{,}14$ ou la touche $\pi$ de la calculatrice pour une valeur arrondie.

---

### Exercices

#### Niveau ★ (Application directe)

**Exercice 1.** Complète le tableau suivant pour différents cercles (prendre $\pi \approx 3{,}14$) :
| Cercle | Rayon $r$ | Diamètre $d$ | Périmètre $P$ |
|---|---|---|---|
| A | $6\text{ cm}$ | ? | ? |
| B | ? | $18\text{ m}$ | ? |
| C | ? | ? | $31{,}4\text{ dm}$ |

**Exercice 2.** Calcule l'aire exacte (avec $\pi$) puis arrondie au dixième :
1. D'un disque de rayon $4\text{ cm}$.
2. D'un disque de diamètre $14\text{ m}$.

**Exercice 3.** Un jardinier souhaite poser une bordure en bois autour d'un massif de fleurs circulaire de $3\text{ m}$ de rayon. Quelle longueur de bordure doit-il acheter ?

**Exercice 4.** Une assiette a un diamètre de $24\text{ cm}$. Calcule son aire au $\text{cm}^2$ près.

**Exercice 5.** Donne la valeur exacte du périmètre d'un demi-cercle de rayon $5\text{ cm}$, comprenant son diamètre de fermeture.

#### Niveau ★★ (Réflexion et géométrie)

**Exercice 6.** Une table ronde a un périmètre de $376{,}8\text{ cm}$.
1. Quel est son rayon ?
2. Quelle est son aire en $\text{m}^2$ ?

**Exercice 7.** Une chèvre est attachée par une corde de $6\text{ mètres}$ à un piquet planté au milieu d'une vaste prairie plate.
1. Quelle est la forme géométrique de la zone d'herbe qu'elle peut brouter ?
2. Calcule l'aire exacte de cette zone de pâture.

**Exercice 8.** On double le rayon d'un disque (le rayon passe de $r$ à $2r$).
1. Par combien son périmètre est-il multiplié ?
2. Par combien son aire est-elle multipliée ? Justifie par un calcul littéral.

**Exercice 9.** Un terrain de sport a la forme d'un rectangle de $100\text{ m}$ de long sur $60\text{ m}$ de large, terminé à chaque extrémité par un demi-disque de diamètre $60\text{ m}$.
1. Calcule la longueur totale d'un tour de piste extérieur.
2. Calcule l'aire totale du terrain.

**Exercice 10.** Une roue de camion a un diamètre extérieur de $90\text{ cm}$. Le camion roule à une vitesse telle que la roue tourne à $10\text{ tours par seconde}$.
Quelle distance le camion parcourt-il en une minute ? Donne le résultat en mètres, puis en kilomètres par heure ($\text{km/h}$).

**Exercice 11.** Un CD audio a un diamètre extérieur de $12\text{ cm}$ et un trou central de diamètre $1{,}5\text{ cm}$.
Quelle est l'aire disponible pour enregistrer les données musicales ?

#### Niveau ★★★ (Défis et approfondissements)

**Exercice 12. Le carré et le cercle inscrits.**
Dans une plaque carrée en métal de $20\text{ cm}$ de côté, un artisan découpe le plus grand disque possible.
1. Quel est le diamètre de ce disque ?
2. Quelle est l'aire de métal perdue (les quatre coins qui tombent dans les chutes) ?
3. Quel pourcentage de la plaque de métal de départ a été gaspillé ?

**Exercice 13. Les lunules d'Hippocrate de Chios.**
Soit un triangle $ABC$ rectangle en $A$, avec $AB = 4\text{ cm}$ et $AC = 3\text{ cm}$. L'hypoténuse $BC$ mesure $5\text{ cm}$.
Sur chacun des trois côtés pris comme diamètres, on trace un demi-cercle vers l'extérieur.
Les deux croissants extérieurs formés au-dessus de l'hypoténuse s'appellent des *lunules*.
Montre que la somme des aires de ces deux lunules est exactement égale à l'aire du triangle rectangle $ABC$ !

**Exercice 14. La corde autour de la Terre.**
Imagine que l'on tende une corde bien serrée tout autour de l'équateur de la Terre (en supposant la Terre parfaitement sphérique, de circonférence $P_1 = 40\,000\text{ km}$).
On ajoute ensuite **1 mètre seulement** à cette corde ($P_2 = 40\,000\text{ km} + 1\text{ m}$), et on la soulève de manière uniforme tout autour de la Terre pour qu'elle forme un nouveau cercle concentrique.
Une souris peut-elle passer sous la corde sans se baisser ? Un chat ? Un être humain ?
*(Indication : calcule la différence d'altitude $h = r_2 - r_1$. Le résultat va te stupéfier !)*

**Exercice 15. La méthode d'Archimède pour l'hexagone.**
Soit un cercle de rayon $R = 1$.
1. Dessine un hexagone régulier inscrit dans ce cercle. Combien mesurent ses 6 côtés ? Déduis-en le périmètre de cet hexagone, et la minoration élémentaire de $\pi$ que cela donne.
2. Calcule le périmètre d'un carré circonscrit autour de ce cercle. Quelle majoration de $\pi$ obtiens-tu ? Entre quels deux nombres entiers $\pi$ est-il ainsi coincé ?

---

### Solutions

**Exercice 1.**
- Cercle A : $d = 2 \times 6 = 12\text{ cm}$ ; $P = \pi \times 12 \approx 3{,}14 \times 12 = 37{,}68\text{ cm}$.
- Cercle B : $r = 18 / 2 = 9\text{ m}$ ; $P = \pi \times 18 \approx 3{,}14 \times 18 = 56{,}52\text{ m}$.
- Cercle C : $d = P / \pi \approx 31{,}4 / 3{,}14 = 10\text{ dm}$ ; $r = 10 / 2 = 5\text{ dm}$.

**Exercice 2.**
1. $r = 4\text{ cm}$ : Aire exacte $A = \pi \times 4^2 = 16\pi\text{ cm}^2 \approx 50{,}3\text{ cm}^2$.
2. $d = 14\text{ m} \implies r = 7\text{ m}$ : Aire exacte $A = \pi \times 7^2 = 49\pi\text{ m}^2 \approx 153{,}9\text{ m}^2$.

**Exercice 3.**
$P = 2\pi r = 2 \times \pi \times 3 = 6\pi \approx 18{,}85\text{ m}$. Il doit acheter environ $18{,}9\text{ m}$ de bordure.

**Exercice 4.**
$d = 24\text{ cm} \implies r = 12\text{ cm}$.
$A = \pi \times 12^2 = 144\pi \approx 452{,}39\text{ cm}^2 \approx 452\text{ cm}^2$.

**Exercice 5.**
Le demi-cercle est composé de l'arc courbe de longueur $\frac{1}{2}(2\pi r) = \pi r = 5\pi\text{ cm}$, plus le diamètre de base $d = 2 \times 5 = 10\text{ cm}$.
Périmètre exact : $P = (5\pi + 10)\text{ cm} \approx 25{,}71\text{ cm}$.

**Exercice 6.**
1. $P = 2\pi r \implies r = \frac{P}{2\pi} \approx \frac{376{,}8}{2 \times 3{,}14} = \frac{376{,}8}{6{,}28} = 60\text{ cm}$.
2. $A = \pi r^2 = \pi \times 60^2 = 3\,600\pi \approx 11\,304\text{ cm}^2 = 1{,}1304\text{ m}^2$.

**Exercice 7.**
1. La zone accessible est un disque plein de centre le piquet et de rayon $6\text{ m}$.
2. Aire exacte : $A = \pi \times 6^2 = 36\pi\text{ m}^2 \approx 113{,}10\text{ m}^2$.

**Exercice 8.**
1. Nouveau périmètre : $P' = 2\pi(2r) = 2 \times (2\pi r) = 2P$. Le périmètre est **multiplié par 2**.
2. Nouvelle aire : $A' = \pi(2r)^2 = \pi \times 4r^2 = 4(\pi r^2) = 4A$. L'aire est **multipliée par 4** ($2^2$) !

**Exercice 9.**
1. Le contour comprend deux longueurs droites de $100\text{ m}$ et deux demi-cercles de diamètre $60\text{ m}$ qui forment ensemble un cercle complet de diamètre $60\text{ m}$ :
   $P_{\text{total}} = 2 \times 100 + \pi \times 60 = 200 + 60\pi \approx 200 + 188{,}5 = 388{,}5\text{ m}$.
2. L'aire comprend le rectangle central ($100 \times 60 = 6\,000\text{ m}^2$) plus le disque complet formé par les deux demi-disques de rayon $r = 30\text{ m}$ :
   $A_{\text{disque}} = \pi \times 30^2 = 900\pi \approx 2\,827{,}4\text{ m}^2$.
   $A_{\text{totale}} = 6\,000 + 900\pi \approx 8\,827{,}4\text{ m}^2$.

**Exercice 10.**
Périmètre d'un tour : $P = \pi \times 0{,}90\text{ m} \approx 2{,}8274\text{ m}$.
En une seconde, la roue fait 10 tours, soit une distance de $10 \times 2{,}8274 = 28{,}274\text{ m/s}$.
En une minute ($60\text{ s}$), le camion parcourt :
$D = 28{,}274 \times 60 \approx 1\,696{,}46\text{ m} \approx 1{,}70\text{ km}$.
Vitesse en $\text{km/h}$ : $28{,}274 \times 3{,}6 \approx 101{,}8\text{ km/h}$.

**Exercice 11.**
Rayon extérieur $R = 6\text{ cm}$, rayon intérieur $r = 0{,}75\text{ cm}$.
$A = \pi R^2 - \pi r^2 = \pi (6^2 - 0{,}75^2) = \pi (36 - 0{,}5625) = 35{,}4375\pi \approx 111{,}33\text{ cm}^2$.

**Exercice 12.**
1. Le plus grand disque a pour diamètre la largeur du carré, soit $d = 20\text{ cm}$, donc son rayon est $r = 10\text{ cm}$.
2. Aire du carré : $A_{\text{carré}} = 20 \times 20 = 400\text{ cm}^2$.
   Aire du disque : $A_{\text{disque}} = \pi \times 10^2 = 100\pi \approx 314{,}16\text{ cm}^2$.
   Aire perdue : $400 - 100\pi \approx 85{,}84\text{ cm}^2$.
3. Taux de gaspillage : $\frac{85{,}84}{400} \approx 0{,}2146 = 21{,}46\%$. Plus de 21% de la matière est perdue !

**Exercice 13.**
Le triangle $ABC$ est rectangle en $A$, son aire est $\frac{3 \times 4}{2} = 6\text{ cm}^2$.
Les demi-disques sur les côtés de l'angle droit ont pour rayons $r_1 = 2$ et $r_2 = 1{,}5$.
Leurs aires valent $\frac{1}{2}\pi(2^2) = 2\pi$ et $\frac{1}{2}\pi(1{,}5^2) = 1{,}125\pi$.
Le grand demi-disque sur l'hypoténuse a pour rayon $R = 2{,}5$ et pour aire $\frac{1}{2}\pi(2{,}5^2) = 3{,}125\pi$.
Remarquons que $2\pi + 1{,}125\pi = 3{,}125\pi$ ! La somme des deux petits demi-disques égale le grand demi-disque.
L'aire totale de la figure est (Triangle + 2 petits demi-disques).
Les lunules s'obtiennent en retirant le grand demi-disque :
$\text{Aire lunules} = (\text{Aire triangle} + 3{,}125\pi) - 3{,}125\pi = \text{Aire triangle} = 6\text{ cm}^2$.
Une figure courbée dont l'aire est rigoureusement égale à celle d'un polygone droit !

**Exercice 14.**
Notons $R_T$ le rayon de la Terre et $R_2$ le rayon avec la corde rallongée.
Circonférence initiale : $P_1 = 2\pi R_T$.
Circonférence rallongée : $P_2 = 2\pi R_2 = P_1 + 1\text{ mètre}$.
Soustrayons : $2\pi R_2 - 2\pi R_T = 1 \implies 2\pi(R_2 - R_T) = 1$.
Donc le soulèvement $h = R_2 - R_T$ vaut :
$$h = \frac{1}{2\pi} \approx \frac{1}{6{,}283} \approx 0{,}159\text{ m} \approx 16\text{ cm} !$$
Ce résultat est totalement indépendant du rayon de la Terre ! Qu'il s'agisse de la Terre, du Soleil ou d'une balle de tennis, rallonger la corde d'un mètre décolle la corde de $16\text{ cm}$ partout. Une souris, et même un gros chat, peuvent passer dessous sans aucun problème !

**Exercice 15.**
1. Un hexagone régulier inscrit se découpe en 6 triangles équilatéraux de côté égal au rayon $R = 1$.
   Chaque côté mesure donc $1$. Le périmètre vaut $6 \times 1 = 6$.
   Comme le diamètre vaut $2$, le rapport donne $\pi > \frac{6}{2} = 3$. Donc $\pi > 3$.
2. Le carré circonscrit a pour côté le diamètre du cercle, soit $2$.
   Son périmètre vaut $4 \times 2 = 8$.
   Le rapport extérieur donne $\pi < \frac{8}{2} = 4$.
   On en déduit l'encadrement immédiat : $3 < \pi < 4$.

---

### La question qui ouvre la suite

Nous savons désormais mesurer les figures rondes et courbées. Mais que faire lorsque l'objet à mesurer n'est ni un petit disque sous nos yeux ni une corde que l'on peut poser au sol, mais un géant de pierre vertigineux : la **Grande Pyramide de Khéops** ?

Comment un sage grec nommé **Thalès**, armé d'un simple bâton planté dans le sable brûlant du désert, a-t-il pu déterminer la hauteur exacte du plus grand tombeau du monde sans jamais y grimper ? C'est le secret des **proportions géométriques et des triangles semblables**, que nous allons percer au chapitre suivant.
