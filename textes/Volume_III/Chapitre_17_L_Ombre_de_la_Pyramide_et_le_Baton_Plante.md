# VOLUME III — L'ÂGE DES ARPENTEURS ET DES BÂTISSEURS (10 - 13 ans / CM2 - 6e - 5e)
## CHAPITRE 17 : L'Ombre de la Pyramide et le Bâton Planté

> *« Pourquoi vouloir escalader un géant de pierre au risque de sa vie ? Quand le soleil éclaire le monde, chaque être projette sur le sol le miroir fidèle de sa propre taille. Il suffit d'apprendre à lire l'ombre. »*

---

### Ce que tu vas découvrir

- Le défi historique de **Thalès de Milet** au pied de la Grande Pyramide de Khéops.
- Ce qu'est un **agrandissement** ou une **réduction** de rapport $k$.
- L'effet magique du coefficient $k$ sur le monde : pourquoi les longueurs sont multipliées par $k$, les aires par $k^2$ et les volumes par $k^3$.
- Le **théorème de Thalès** dans ses deux configurations officielles : les triangles emboîtés et le sablier (papillon).
- L'égalité des trois rapports de longueurs et la méthode infaillible du produit en croix.
- La **réciproque du théorème de Thalès** pour prouver avec certitude que deux droites sont parallèles.

---

### 1. Le problème : le défi insolent du Pharaon

Le vent du désert souffle en tourbillons sur le plateau de Gizeh, en Égypte, il y a deux mille six cents ans. Devant toi se dresse la Grande Pyramide du pharaon Khéops : une montagne artificielle de calcaire pur culminant à une hauteur vertigineuse.

Le Pharaon Amasis réunit les grands prêtres et les géomètres de sa cour au pied du géant :
*« Qui parmi vous est capable de me donner la hauteur exacte de ce tombeau sacré, depuis la roche du sol jusqu'à la pointe dorée qui touche le ciel ? »*

Les architectes baissent la tête, embarrassés :
*« Majesté, les parois sont lisses comme du verre et inclinées à pic. Aucun homme ne peut grimper avec une chaîne d'arpenteur sans glisser et s'écraser cent quarante mètres plus bas ! »*

Un voyageur étranger, venu de la cité grecque de Milet et vêtu d'un simple manteau de laine, s'avance calmement. Il s'appelle **Thalès**.
Thalès regarde la montagne de pierre, observe le soleil éclatant dans le ciel d'azur, puis sourit :
*« Majesté, je n'ai nul besoin d'escalader votre pyramide. Donnez-moi simplement un bâton de bois, et avant que le jour ne s'éteigne, je vous donnerai la hauteur exacte du monument sans avoir décollé mes pieds de la terre ! »*

Les prêtres égyptiens ricanent. Comment ce marchand grec pourrait-il mesurer un colosse avec un pauvre morceau de bois ?

```
      Rayon du Soleil
            \
             \
              \      Sommet de la Pyramide (Hauteur H inconnue)
               \     ▲
                \   / \
                 \ /   \
                  /     \
                 /       \           Sommet du bâton (h = 2 m)
                /         \             |
    ───────────●───────────●────────────●─────────► Sol
               |◄─── Ombre L ──►|       |◄─ l ─►| (ombre bâton)
```

---

### 2. De l'instant magique aux proportions universelles

#### 2.1 La première idée : l'heure magique

Thalès commence par s'asseoir dans le sable et observe la course du soleil.
- Tôt le matin, le soleil est bas : les ombres sont immenses et démesurées.
- À midi, le soleil est au zénith : les ombres sont minuscules, tassées sous les pieds.
- Puis au cours de l'après-midi, le soleil descend lentement, et les ombres recommencent à grandir.

Thalès plante son bâton verticalement dans le sable. Ce bâton mesure exactement **2 mètres**.
Il trace un repère dans le sable et surveille la pointe de l'ombre du bâton :
- À 14 h 00, l'ombre mesure $1{,}20\text{ m}$ (plus courte que le bâton).
- À 15 h 00, elle mesure $1{,}60\text{ m}$.
- Soudain, à **15 h 45**, Thalès mesure l'ombre : **elle mesure très exactement 2 mètres !**

À cet instant précis, un miracle géométrique se produit :
$$\text{Longueur de l'ombre du bâton} = \text{Hauteur réelle du bâton} = 2\text{ mètres}$$

Le rayon du soleil frappe le sol avec un angle de $45^\circ$, formant avec le bâton vertical et le sol un **triangle rectangle isocèle**.
Thalès crie aux serviteurs : *« Mesurez l'ombre de la pyramide maintenant ! »*
À cette seconde précise, la longueur de l'ombre de la pyramide (mesurée depuis le centre de sa base jusqu'au bout de son ombre projetée) est **rigoureusement égale à sa hauteur réelle** !

> **💡 Le savais-tu ?** Selon l'écrivain grec Plutarque, le pharaon Amasis fut tellement stupéfait de voir Thalès mesurer le monument en quelques pas qu'il le couvrit de cadeaux et le tint pour le plus sage des hommes vivants.

#### 2.2 Mais si le soleil ne nous attend pas ? L'idée des proportions

Cette méthode de « l'heure magique » est géniale, mais elle a un gros défaut : il faut attendre l'instant précis où l'angle fait $45^\circ$. Que faire s'il y a un nuage à 15 h 45 ? Que faire si l'on doit mesurer un arbre à 10 h du matin ?

Thalès comprit une vérité bien plus profonde : **les rayons du soleil, venant d'un astre situé à 150 millions de kilomètres, arrivent sur Terre en étant parfaitement parallèles entre eux.**

Par conséquent, à **n'importe quelle heure de la journée**, la pyramide et son ombre forment un triangle qui a **exactement la même forme** que le triangle formé par le bâton et son ombre ! L'un est simplement un **agrandissement** de l'autre.

```
       Triangle de la Pyramide                 Triangle du Bâton
                 S                                    A
                /|                                   /|
               / |                                  / |
              /  |                                 /  |
             /   | Hauteur H                      /   | Hauteur h
            /    |                               /    |
           /     |                              /     |
          /______|                             /______|
         O       H'                           B       C
          Ombre L                              Ombre l
```

Le rapport entre la hauteur et l'ombre est **le même pour tous les objets verticaux à un instant donné** :
$$\frac{\text{Hauteur Pyramide}}{\text{Ombre Pyramide}} = \frac{\text{Hauteur Bâton}}{\text{Ombre Bâton}} \iff \frac{H}{L} = \frac{h}{l}$$

D'où la formule qui donne la hauteur sans attendre :
$$H = L \times \frac{h}{l}$$

---

### 3. Agrandissement, réduction et le piège des dimensions

Avant d'énoncer le théorème dans toute sa généralité, arrêtons-nous sur ce que signifie « agrandir » ou « réduire » une figure. C'est l'un des chapitres où les intuitions trompent le plus facilement l'esprit humain !

#### 3.1 Le coefficient d'agrandissement ou de réduction

> **📐 Définition — Agrandissement et Réduction**
> - Modifier une figure en multipliant **toutes ses longueurs** par un même nombre strictement positif $k$ s'appelle :
>   - Un **agrandissement** si $k > 1$.
>   - Une **réduction** si $0 < k < 1$.
> - Le nombre $k$ est appelé le **rapport** ou **coefficient** d'agrandissement ou de réduction (ou **échelle**).
> - Dans un agrandissement ou une réduction, **la forme est conservée** : les angles restent strictement identiques, et les droites parallèles restent parallèles.

#### 3.2 L'effet sur les longueurs, les aires et les volumes

Voici la règle d'or qui gouverne toute la géométrie de notre univers à trois dimensions :

> **📐 Théorème fondamental — Effet du rapport $k$**
> Lorsque toutes les longueurs d'une figure ou d'un solide sont multipliées par un coefficient $k$ ($k > 0$) :
> - Les **longueurs** sont multipliées par $k$.
> - Les **aires** sont multipliées par $k^2$ ($k \times k$).
> - Les **volumes** sont multipliés par $k^3$ ($k \times k \times k$).

#### Pourquoi ce carré et ce cube ? La preuve par les cubes emboîtés

Prenons un petit cube de pâte à modeler de $1\text{ cm}$ de côté.
- Sa longueur est de $1\text{ cm}$.
- L'aire d'une face est de $1 \times 1 = 1\text{ cm}^2$.
- Son volume est de $1 \times 1 \times 1 = 1\text{ cm}^3$.

Maintenant, effectuons un agrandissement de rapport **$k = 2$** (on double toutes les dimensions : côté $= 2\text{ cm}$).

```
        Cube initial (k=1)             Cube agrandi (k=2)
             ┌─┐                            ┌───┬───┐
             │ │                            │   │   │  4 petits cubes devant
             └─┘                            ├───┼───┤
          Côté = 1 cm                       │   │   │
          Aire face = 1 cm²                 └───┴───┘
          Volume = 1 cm³                + 4 petits cubes derrière !
                                        Total = 8 cubes = 2³
```

Regarde bien :
1. La longueur d'une arête a été multipliée par **$2$** ($2\text{ cm}$).
2. L'aire d'une face carrée : elle contient maintenant $2 \times 2 = 4$ petits carrés. Elle a été multipliée par $2^2 = \mathbf{4}$ !
3. Le volume du cube : pour remplir le nouveau cube de $2\text{ cm}$ d'arête, il faut 4 petits cubes au rez-de-chaussée et 4 petits cubes au premier étage, soit $2 \times 2 \times 2 = 8$ petits cubes. Le volume a été multiplié par $2^3 = \mathbf{8}$ !

Si l'on triplait les longueurs ($k = 3$) :
- Les longueurs seraient $\times 3$.
- Les aires seraient $\times 3^2 = \mathbf{9}$.
- Les volumes seraient $\times 3^3 = \mathbf{27}$ !

> **💡 Le savais-tu ? — Pourquoi les géants de cinéma ne peuvent pas exister**
> C'est Galilée qui l'a compris le premier : si un être humain mesurait 10 fois sa taille ($k = 10$), il serait 10 fois plus grand, mais son poids (qui dépend de son volume) serait multiplié par $10^3 = \mathbf{1\,000}$ ! En revanche, la solidité de ses os (qui dépend de l'aire de leur section) ne serait multipliée que par $10^2 = \mathbf{100}$. Ses os subiraient une pression 10 fois trop forte : ses jambes se briseraient sous son propre poids au premier pas !

---

### 4. Le Théorème de Thalès dans le triangle

Revenons à la géométrie pure du collège. Comment s'énonce ce théorème dans un cahier de mathématiques ?

#### 4.1 Les deux configurations officielles

Le théorème s'applique lorsqu'une droite coupe deux côtés d'un triangle en étant **parallèle** au troisième côté. Il existe deux figures possibles :

```
    Configuration 1 : Les triangles emboîtés        Configuration 2 : Le Sablier (Papillon)
                     A                                            M       N
                    / \                                            \     /
                   /   \                                            \   /
                  M─────N   (MN) // (BC)                             \ /
                 /       \                                            A
                /         \                                          / \
               B───────────C                                        /   \
                                                                   B─────C   (MN) // (BC)
```

Dans les deux cas :
- Les droites $(MB)$ et $(NC)$ sont sécantes en $A$.
- Les droites $(MN)$ et $(BC)$ sont **strictement parallèles**.

Le triangle $AMN$ est une réplique exacte du triangle $ABC$ : c'est une réduction (ou un agrandissement) de rapport $k$.
Leurs angles sont identiques, et leurs côtés sont tous proportionnels deux à deux.

#### 4.2 L'énoncé du théorème de Thalès

> **📐 Théorème de Thalès —**
> Soient $(d)$ et $(d')$ deux droites sécantes en un point $A$.
> Soient $B$ et $M$ deux points de $(d)$, distincts de $A$.
> Soient $C$ et $N$ deux points de $(d')$, distincts de $A$.
> Si les droites $(MN)$ et $(BC)$ sont parallèles, alors :
> $$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$$

Chaque fraction compare un côté du « petit » triangle à son côté correspondant dans le « grand » triangle :
$$\frac{\text{côté de } AMN}{\text{côté de } ABC} = \text{constante } k$$

> **🧭 Méthode — Comment écrire l'égalité des rapports sans jamais se tromper**
> 1. Repère le **sommet commun** (le point où les deux sécantes se croisent, ici $A$).
> 2. Écris les deux premiers rapports en partant toujours de ce sommet commun :
>    $\frac{A\dots}{A\dots} = \frac{A\dots}{A\dots}$ (ex : $\frac{AM}{AB} = \frac{AN}{AC}$).
> 3. Pour le troisième rapport, « oublie » le sommet commun $A$ et prends les deux autres lettres des numérateurs, puis des dénominateurs : $\frac{MN}{BC}$.
> 4. Vérifie que tous les côtés du triangle du haut ($AM, AN, MN$) sont bien au **numérateur**, et tous ceux du triangle du bas ($AB, AC, BC$) au **dénominateur** (ou l'inverse, mais ne mélange jamais !).

---

### 5. La Réciproque du théorème de Thalès : prouver le parallélisme

Le théorème de Thalès dit :
$$\text{Si les droites sont parallèles} \implies \text{les rapports sont égaux.}$$

Que se passe-t-il si nous voulons faire le chemin inverse ? Nous arrivons sur un chantier naval ou sur un terrain d'arpentage, nous mesurons des longueurs au sol, et nous voulons savoir avec une certitude absolue si deux poutres ou deux rails sont **parallèles**.

C'est le rôle de la **réciproque du théorème de Thalès**.

> **📐 Réciproque du Théorème de Thalès —**
> Soient $(AB)$ et $(AC)$ deux droites sécantes en $A$.
> Soient $M$ un point de la droite $(AB)$ et $N$ un point de la droite $(AC)$.
> Si :
> 1. Les points $A, M, B$ et les points $A, N, C$ sont alignés **dans le même ordre**,
> 2. Et si $\frac{AM}{AB} = \frac{AN}{AC}$,
>
> alors les droites $(MN)$ et $(BC)$ sont **parallèles**.

#### La contraposée : prouver que des droites NE SONT PAS parallèles

Si après avoir calculé les deux quotients, tu découvres qu'ils ne sont pas égaux ($\frac{AM}{AB} \neq \frac{AN}{AC}$), alors tu peux conclure immédiatement (grâce à la contraposée du théorème de Thalès) que **les droites $(MN)$ et $(BC)$ ne sont pas parallèles**.

---

### 6. Attention aux pièges !

> **⚠️ Attention, piège ! — Les erreurs classiques du brevet**
> 1. **Mélanger le numérateur et le dénominateur :** Écrire $\frac{AM}{AB} = \frac{AC}{AN}$ est une faute grave. Tu as mis « petit sur grand » à gauche, et « grand sur petit » à droite. Le produit en croix sera totalement faux.
> 2. **Prendre le segment entre les deux parallèles au lieu du côté complet :** Dans la configuration emboîtée, le côté du grand triangle est $AB$. Certains élèves prennent par erreur la longueur $MB$. Or $MB$ n'est le côté d'aucun triangle ! Rappel : $AB = AM + MB$.
> 3. **Oublier la condition d'ordre dans la réciproque :** Pour appliquer la réciproque, il est **obligatoire** de mentionner dans ta rédaction : *« Les points $A, M, B$ d'une part, et $A, N, C$ d'autre part, sont alignés dans le même ordre. »* Sans cette phrase, la démonstration est incomplète.
> 4. **Multiplier une aire par $k$ au lieu de $k^2$ :** Si une carte est à l'échelle $\frac{1}{100}$, les longueurs sont divisées par $100$, mais l'aire d'un champ sur la carte est divisée par $100^2 = 10\,000$ !

---

### 7. Exemples résolus

#### Exemple résolu 1 — Le calcul de la pyramide par Thalès
Mesurons la pyramide de Khéops comme Thalès avec les véritables données historiques :
- Le bâton mesure $h = 2\text{ m}$. Son ombre au sol mesure $l = 3\text{ m}$.
- La pyramide a une base carrée de $230\text{ m}$ de côté.
- L'ombre du sommet de la pyramide dépasse du pied de la paroi de $74\text{ m}$.
Quelle est la hauteur $H$ de la pyramide ?

```
          Sommet
            ▲\
            │ \
            │  \ Paroi
            │   \
            │    \
     ───────┼─────┴───────────●  (Fin de l'ombre)
            │      │◄── 74 m ──►│
            │◄ demi-côté ►│
               115 m
```

*Solution :*
1. Calculons d'abord la longueur totale $L$ de l'ombre de la pyramide, mesurée depuis la verticale du sommet (le centre de la base carrée) :
   $$L = \text{demi-côté} + \text{ombre extérieure} = \frac{230}{2} + 74 = 115 + 74 = 189\text{ m}$$
2. Les rayons du soleil étant parallèles, nous appliquons l'égalité des proportions de Thalès :
   $$\frac{H}{h} = \frac{L}{l} \implies \frac{H}{2} = \frac{189}{3}$$
3. Calculons $H$ par un produit en croix :
   $$H = \frac{2 \times 189}{3} = 2 \times 63 = 126\text{ mètres}$$
La Grande Pyramide mesurait environ $126$ mètres ce jour-là (en tenant compte de l'érosion du sommet). ✔

#### Exemple résolu 2 — Calcul d'une longueur inconnue (configuration classique)
Sur la figure ci-contre, les droites $(AB)$ et $(AC)$ sont sécantes en $A$.
On donne : $AM = 3\text{ cm}$, $AB = 7{,}5\text{ cm}$, $AC = 10\text{ cm}$ et $BC = 12\text{ cm}$.
Les droites $(MN)$ et $(BC)$ sont parallèles.
Calculer les longueurs $AN$ et $MN$.

*Solution :*
- Rédaction type collège :
  Dans le triangle $ABC$, $M$ est un point du segment $[AB]$ et $N$ un point du segment $[AC]$.
  Puisque les droites $(MN)$ et $(BC)$ sont parallèles, d'après le **théorème de Thalès**, on a l'égalité des rapports :
  $$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$$
- Remplaçons par les valeurs numériques connues :
  $$\frac{3}{7{,}5} = \frac{AN}{10} = \frac{MN}{12}$$
- Calcul de $AN$ :
  $$AN = \frac{3 \times 10}{7{,}5} = \frac{30}{7{,}5} = 4\text{ cm}$$
- Calcul de $MN$ :
  $$MN = \frac{3 \times 12}{7{,}5} = \frac{36}{7{,}5} = 4{,}8\text{ cm}$$
Les longueurs cherchées sont $AN = 4\text{ cm}$ et $MN = 4{,}8\text{ cm}$. ✔

#### Exemple résolu 3 — La rivière infranchissable (configuration papillon)
Un géomètre souhaite mesurer la largeur $AB$ d'une rivière tumultueuse sans la traverser.
Il repère un arbre $A$ sur la rive opposée, plante un piquet $B$ en face sur sa rive, puis recule jusqu'à un point $O$ aligné avec $A$ et $B$.
Il trace ensuite deux lignes perpendiculaires et obtient la configuration sablier suivante :
- Les droites $(AB)$ et $(CD)$ se croisent en $O$.
- Les droites $(AB)$ et $(CD)$ sont telles que $(AC) // (BD)$... ou plus simplement, la droite $(AB)$ traverse la rivière :

```
         Arbre A (rive opposée)
            ●
             \
  ~~~~~~~~~~~~\~~~~~~~~~~~~~~~~~~~ Rivière
               \
                ● B (rive accessible)
                 \
                  \
                   ● O
                  / \
                 /   \
             C  ●─────● D   (CD accessible sur le pré)
```

On a les mesures suivantes : $OB = 15\text{ m}$, $OD = 20\text{ m}$, $OC = 36\text{ m}$ et $CD = 25\text{ m}$.
Les droites $(AC)$ et $(BD)$ se coupent en $O$, et $(AB)$ est parallèle à $(CD)$ n'est pas la bonne disposition : ici, ce sont $(AB)$ et $(CD)$ qui sont sécantes en $O$, et les droites $(AC)$ et $(BD)$ qui sont parallèles.
Prenons la configuration officielle : les droites $(AD)$ et $(BC)$ se coupent en $O$, avec $(AB) // (CD)$.
On donne : $OB = 12\text{ m}$, $OC = 30\text{ m}$, et $CD = 45\text{ m}$.
Calculer la distance $AB$.

*Solution :*
- Les droites $(AD)$ et $(BC)$ sont sécantes en $O$.
- Les droites $(AB)$ et $(CD)$ sont parallèles.
- D'après le **théorème de Thalès** dans la configuration en sablier :
  $$\frac{OA}{OD} = \frac{OB}{OC} = \frac{AB}{CD}$$
- Utilisons le rapport connu :
  $$\frac{12}{30} = \frac{AB}{45}$$
- Produit en croix :
  $$AB = \frac{12 \times 45}{30} = \frac{540}{30} = 18\text{ mètres}$$
La largeur $AB$ mesurée à travers la rivière vaut $18\text{ mètres}$. ✔

#### Exemple résolu 4 — Démontrer le parallélisme par la réciproque
Soit un triangle $ABC$ tel que $AB = 6\text{ cm}$ et $AC = 8\text{ cm}$.
Sur la demi-droite $[AB)$, on place un point $E$ tel que $AE = 15\text{ cm}$.
Sur la demi-droite $[AC)$, on place un point $F$ tel que $AF = 20\text{ cm}$.
Les droites $(BC)$ et $(EF)$ sont-elles parallèles ?

*Solution :*
- Calculons séparément les deux rapports de longueurs :
  $$\frac{AB}{AE} = \frac{6}{15} = \frac{2 \times 3}{5 \times 3} = \frac{2}{5} = 0{,}4$$
  $$\frac{AC}{AF} = \frac{8}{20} = \frac{2 \times 4}{5 \times 4} = \frac{2}{5} = 0{,}4$$
- On constate que :
  $$\frac{AB}{AE} = \frac{AC}{AF}$$
- Rédaction finale :
  Les points $A, B, E$ d'une part, et $A, C, F$ d'autre part, sont alignés dans le même ordre.
  De plus, $\frac{AB}{AE} = \frac{AC}{AF}$.
  Donc, d'après la **réciproque du théorème de Thalès**, les droites $(BC)$ et $(EF)$ sont bien parallèles. ✔

#### Exemple résolu 5 — L'architecte et la maquette de la tour
Une agence d'architecture réalise la maquette à l'échelle $\frac{1}{200}$ d'un futur gratte-ciel en verre.
1. La maquette a une hauteur de $1{,}40\text{ m}$. Quelle sera la hauteur réelle de la tour ?
2. La maquette utilise une surface vitrée de $0{,}35\text{ m}^2$. Quelle sera la surface vitrée réelle du gratte-ciel ?
3. Le volume intérieur de la maquette est de $0{,}05\text{ m}^3$. Quel sera le volume réel du bâtiment ?

*Solution :*
L'échelle de la maquette est une réduction de coefficient $k = \frac{1}{200}$.
Pour passer de la maquette à la réalité, on effectue un agrandissement de rapport inverse :
$$K = 200$$

1. **Pour les longueurs :** multiplication par $K = 200$.
   $$\text{Hauteur réelle} = 1{,}40 \times 200 = 280\text{ mètres}$$
2. **Pour les aires :** multiplication par $K^2 = 200^2 = 40\,000$.
   $$\text{Surface vitrée} = 0{,}35 \times 40\,000 = 14\,000\text{ m}^2$$
3. **Pour les volumes :** multiplication par $K^3 = 200^3 = 8\,000\,000$.
   $$\text{Volume réel} = 0{,}05 \times 8\,000\,000 = 400\,000\text{ m}^3$$
Observe l'explosion des chiffres : le volume est huit millions de fois plus grand que celui de la maquette ! ✔

---

### Ce qu'il faut retenir

1. **Agrandissement et Réduction :**
   - Rapport $k > 1$ : agrandissement ; $0 < k < 1$ : réduction.
   - Effet du coefficient $k$ :
     - Longueurs $\times k$
     - Aires $\times k^2$
     - Volumes $\times k^3$
2. **Théorème de Thalès (Calcul de longueurs) :**
   - **Conditions :** Deux droites sécantes en $A$, coupées par deux droites parallèles $(MN)$ et $(BC)$.
   - **Conclusion :** $\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$.
3. **Réciproque de Thalès (Preuve de parallélisme) :**
   - **Conditions :** Points alignés dans le même ordre sur deux droites sécantes, ET égalité de deux rapports : $\frac{AM}{AB} = \frac{AN}{AC}$.
   - **Conclusion :** Les droites $(MN)$ et $(BC)$ sont parallèles.
   - Si les rapports sont différents, la **contraposée** prouve que les droites ne sont pas parallèles.

---

### Exercices

#### Niveau ★ (Application directe)

**Exercice 1.** On applique un agrandissement de coefficient $k = 3$ à un triangle dont les côtés mesurent $4\text{ cm}$, $5\text{ cm}$ et $6\text{ cm}$.
Quelles sont les longueurs des côtés du triangle agrandi ?

**Exercice 2.** Un carré a une aire de $25\text{ cm}^2$. On réduit ses côtés d'un rapport $k = 0{,}4$.
1. Quelle est la longueur du côté du carré initial ?
2. Quelle est la longueur du côté du carré réduit ?
3. Quelle est l'aire du carré réduit ? Vérifie que $\text{Aire}' = k^2 \times \text{Aire}$.

**Exercice 3.** Dans un triangle $ABC$, on a $M \in [AB]$ et $N \in [AC]$ avec $(MN) // (BC)$.
On donne $AM = 2\text{ cm}$, $AB = 6\text{ cm}$ et $AN = 3\text{ cm}$.
Calcule la longueur $AC$.

**Exercice 4.** Configuration papillon : les droites $(AB)$ et $(CD)$ sont sécantes en $O$, et $(AC) // (BD)$.
On sait que $OA = 5\text{ cm}$, $OB = 15\text{ cm}$ et $AC = 4\text{ cm}$.
Calcule la longueur $BD$.

**Exercice 5.** Sur une droite, on a $AM = 4\text{ cm}$ et $AB = 10\text{ cm}$. Sur une autre droite sécante en $A$, on a $AN = 6\text{ cm}$ et $AC = 15\text{ cm}$.
Les rapports $\frac{AM}{AB}$ et $\frac{AN}{AC}$ sont-ils égaux ?

#### Niveau ★★ (Calculs et démonstrations)

**Exercice 6. La hauteur du clocher.**
Un après-midi, un promeneur de $1{,}80\text{ m}$ projette une ombre de $2{,}40\text{ m}$ sur le parvis d'une église.
Au même instant, l'ombre portée du clocher mesure $36\text{ mètres}$.
Quelle est la hauteur du clocher ?

**Exercice 7. Attention au segment piège !**
Dans un triangle $ABC$, on donne $AB = 12\text{ cm}$, $AC = 16\text{ cm}$.
Le point $M$ est sur $[AB]$ tel que $MB = 3\text{ cm}$. La parallèle à $(BC)$ passant par $M$ coupe $[AC]$ en $N$.
1. Calcule la longueur $AM$.
2. Calcule la longueur $AN$, puis la longueur $NC$.

**Exercice 8. Les deux étagères murales.**
Un menuisier fixe deux planches horizontales $[MN]$ et $[BC]$ entre deux montants inclinés se rejoignant au sommet $A$.
On mesure : $AM = 45\text{ cm}$, $MB = 30\text{ cm}$, $MN = 60\text{ cm}$.
Puisque les planches sont horizontales, elles sont parallèles entre elles.
Calcule la longueur de la grande planche $[BC]$.

**Exercice 9. Test de parallélisme.**
Soit un triangle $RST$ avec $RS = 7\text{ cm}$ et $RT = 9\text{ cm}$.
On place un point $P$ sur $[RS]$ tel que $RP = 2{,}8\text{ cm}$, et un point $Q$ sur $[RT]$ tel que $RQ = 3{,}6\text{ cm}$.
Les droites $(PQ)$ et $(ST)$ sont-elles parallèles ? Rédige soigneusement ta réponse.

**Exercice 10. Le contre-exemple de la réciproque.**
Soit un triangle $ABC$ avec $AB = 5\text{ cm}$, $AC = 8\text{ cm}$.
On place $D$ sur $[AB]$ tel que $AD = 2\text{ cm}$, et $E$ sur $[AC]$ tel que $AE = 3\text{ cm}$.
Les droites $(DE)$ et $(BC)$ sont-elles parallèles ? Justifie.

**Exercice 11. Peinture et carrelage : l'effet $k^2$.**
Un peintre en bâtiment met 2 heures et utilise un pot de 5 litres de peinture pour peindre un panneau publicitaire carré de $3\text{ mètres}$ de côté.
Combien de pots de peinture et combien d'heures de travail lui faudra-t-il pour peindre un panneau géant de même forme mais de $9\text{ mètres}$ de côté (en supposant qu'il travaille à la même vitesse) ?

#### Niveau ★★★ (Défis et modélisation)

**Exercice 12. L'obstacle infranchissable et le pantographe.**
Pour mesurer la distance entre deux balises $A$ et $B$ séparées par un étang marécageux, un géomètre choisit un point d'observation $S$ d'où il peut viser $A$ et $B$.
Il mesure sur la terre ferme : $SA = 120\text{ m}$ et $SB = 150\text{ m}$.
Il prolonge ensuite les visées au-delà de $S$ :
Sur la demi-droite opposée à $[SA)$, il place $A'$ tel que $SA' = 40\text{ m}$.
Sur la demi-droite opposée à $[SB)$, il place $B'$ tel que $SB' = 50\text{ m}$.
Il mesure directement avec son ruban la distance sur le pré : $A'B' = 36\text{ m}$.
1. Démontre que la droite $(A'B')$ est parallèle à la droite $(AB)$.
2. Détermine la distance inaccessible $AB$ à travers l'étang.

**Exercice 13. Le gâteau des trois frères : partage en parts d'aires égales.**
Un pâtissier prépare un grand biscuit triangulaire $ABC$ de hauteur $18\text{ cm}$.
Il souhaite le couper en trois parts de même aire à l'aide de deux coups de couteau horizontaux parallèles à la base $[BC]$, situés aux hauteurs $h_1$ et $h_2$ depuis le sommet $A$.
1. Par quel coefficient d'agrandissement l'aire est-elle multipliée pour passer du petit triangle du haut au triangle intermédiaire ? Et au grand triangle entier ?
2. À quelles hauteurs $h_1$ et $h_2$ depuis le sommet $A$ le pâtissier doit-il couper le gâteau ? *(Donne les valeurs exactes puis arrondies au millimètre).*

**Exercice 14. Le tronc de pyramide d'Égypte.**
On considère une pyramide régulière à base carrée de côté $10\text{ m}$ et de hauteur $12\text{ m}$.
Son volume initial est $V = \frac{1}{3} \times \text{Base} \times \text{Hauteur} = \frac{1}{3} \times 100 \times 12 = 400\text{ m}^3$.
On coupe cette pyramide à mi-hauteur (à $6\text{ m}$ du sommet) par un plan parallèle à la base.
1. Quel est le rapport de réduction $k$ de la petite pyramide supérieure ?
2. Quel est le volume de la petite pyramide retirée ?
3. Quel est le volume du « tronc de pyramide » restant en bas ? Quelle fraction du volume total représente-t-il ?

**Exercice 15. Thalès dans l'espace : la chambre noire et la photographie.**
Le premier appareil photo (la *camera obscura*) est une boîte fermée percée d'un minuscule trou $O$ au centre de sa face avant.
Un arbre de $15\text{ mètres}$ de haut est situé à $30\text{ mètres}$ en face du trou de la boîte.
La boîte a une profondeur de $20\text{ centimètres}$ entre le trou et le fond où se trouve la plaque photographique.
1. Fais un schéma en coupe montrant les rayons lumineux qui se croisent en $O$. Quelle est la nature de l'image sur le fond (à l'endroit ou à l'envers) ?
2. Quelle sera la hauteur de l'image de l'arbre imprimée sur la plaque photographique au fond de l'appareil ?

---

### Solutions

**Exercice 1.**
Chaque longueur est multipliée par $3$ :
$4 \times 3 = 12\text{ cm}$ ; $5 \times 3 = 15\text{ cm}$ ; $6 \times 3 = 18\text{ cm}$.

**Exercice 2.**
1. Côté initial : $\sqrt{25} = 5\text{ cm}$.
2. Côté réduit : $5 \times 0{,}4 = 2\text{ cm}$.
3. Aire réduite : $2 \times 2 = 4\text{ cm}^2$.
   Vérification : $k^2 \times \text{Aire initiale} = (0{,}4)^2 \times 25 = 0{,}16 \times 25 = 4\text{ cm}^2$. Exact !

**Exercice 3.**
D'après le théorème de Thalès : $\frac{AM}{AB} = \frac{AN}{AC} \implies \frac{2}{6} = \frac{3}{AC}$.
Produit en croix : $AC = \frac{6 \times 3}{2} = 9\text{ cm}$.

**Exercice 4.**
Configuration papillon : $\frac{OA}{OB} = \frac{AC}{BD} \implies \frac{5}{15} = \frac{4}{BD}$.
$BD = \frac{15 \times 4}{5} = 12\text{ cm}$.

**Exercice 5.**
$\frac{AM}{AB} = \frac{4}{10} = 0{,}4$.
$\frac{AN}{AC} = \frac{6}{15} = \frac{2}{5} = 0{,}4$.
Oui, les deux rapports sont rigoureusement égaux.

**Exercice 6.**
Parallélisme des rayons du soleil :
$\frac{H_{\text{clocher}}}{h_{\text{homme}}} = \frac{L_{\text{clocher}}}{l_{\text{homme}}} \implies \frac{H}{1{,}80} = \frac{36}{2{,}40}$.
$H = \frac{1{,}80 \times 36}{2{,}40} = 1{,}80 \times 15 = 27\text{ mètres}$.

**Exercice 7.**
1. $M \in [AB] \implies AM = AB - MB = 12 - 3 = 9\text{ cm}$.
2. D'après Thalès : $\frac{AM}{AB} = \frac{AN}{AC} \implies \frac{9}{12} = \frac{AN}{16}$.
   $AN = \frac{9 \times 16}{12} = \frac{144}{12} = 12\text{ cm}$.
   $NC = AC - AN = 16 - 12 = 4\text{ cm}$.

**Exercice 8.**
Attention : $AB = AM + MB = 45 + 30 = 75\text{ cm}$.
Thalès : $\frac{AM}{AB} = \frac{MN}{BC} \implies \frac{45}{75} = \frac{60}{BC}$.
$BC = \frac{75 \times 60}{45} = \frac{4500}{45} = 100\text{ cm} = 1\text{ mètre}$.

**Exercice 9.**
Calculons séparément :
$\frac{RP}{RS} = \frac{2{,}8}{7} = 0{,}4$.
$\frac{RQ}{RT} = \frac{3{,}6}{9} = 0{,}4$.
Les points $R, P, S$ d'une part, et $R, Q, T$ d'autre part, sont alignés dans le même ordre.
Comme $\frac{RP}{RS} = \frac{RQ}{RT}$, d'après la réciproque du théorème de Thalès, les droites $(PQ)$ et $(ST)$ sont parallèles.

**Exercice 10.**
Calculons : $\frac{AD}{AB} = \frac{2}{5} = 0{,}40$.
$\frac{AE}{AC} = \frac{3}{8} = 0{,}375$.
Comme $\frac{AD}{AB} \neq \frac{AE}{AC}$, d'après la contraposée du théorème de Thalès, les droites $(DE)$ et $(BC)$ ne sont pas parallèles.

**Exercice 11.**
Le côté passe de $3\text{ m}$ à $9\text{ m}$ : rapport des longueurs $k = \frac{9}{3} = 3$.
L'aire à peindre est multipliée par $k^2 = 3^2 = 9$ !
- Peinture : $5\text{ L} \times 9 = 45\text{ litres}$ (soit 9 pots).
- Temps : $2\text{ h} \times 9 = 18\text{ heures}$ de travail.

**Exercice 12.**
1. Les points $A', S, A$ et $B', S, B$ sont alignés dans cet ordre.
   Rapports : $\frac{SA'}{SA} = \frac{40}{120} = \frac{1}{3}$ et $\frac{SB'}{SB} = \frac{50}{150} = \frac{1}{3}$.
   Puisque les rapports sont égaux, d'après la réciproque de Thalès, $(A'B') // (AB)$.
2. D'après Thalès : $\frac{A'B'}{AB} = \frac{1}{3} \implies AB = 3 \times A'B' = 3 \times 36 = 108\text{ mètres}$.

**Exercice 13.**
1. Soit $A$ l'aire du triangle total. Le premier triangle du haut a pour aire $\frac{1}{3}A$.
   Le triangle intermédiaire a pour aire $\frac{2}{3}A$.
   Le rapport des aires est $k^2$. Donc le rapport des hauteurs est $k = \sqrt{\text{rapport des aires}}$.
2. Pour la première coupe : $k_1 = \sqrt{\frac{1}{3}} = \frac{1}{\sqrt{3}} \approx 0{,}57735$.
   $h_1 = 18 \times \frac{1}{\sqrt{3}} = \frac{18\sqrt{3}}{3} = 6\sqrt{3} \approx 10{,}39\text{ cm}$.
   Pour la deuxième coupe : $k_2 = \sqrt{\frac{2}{3}} = \frac{\sqrt{6}}{3} \approx 0{,}8165$.
   $h_2 = 18 \times \sqrt{\frac{2}{3}} = 6\sqrt{6} \approx 14{,}70\text{ cm}$.

**Exercice 14.**
1. La coupe est faite à mi-hauteur ($6\text{ m}$ sur $12\text{ m}$), donc le rapport de réduction est $k = \frac{6}{12} = \frac{1}{2} = 0{,}5$.
2. Le volume de la petite pyramide est multiplié par $k^3 = \left(\frac{1}{2}\right)^3 = \frac{1}{8}$.
   $V_{\text{petit}} = \frac{1}{8} \times 400 = 50\text{ m}^3$.
3. Le volume du tronc de pyramide restant est :
   $V_{\text{tronc}} = 400 - 50 = 350\text{ m}^3$.
   Il représente $\frac{350}{400} = \frac{7}{8}$ du volume total (soit 87,5 % du volume dans la moitié inférieure) !

**Exercice 15.**
1. Les rayons lumineux passent par le trou $O$ en ligne droite : le rayon venant du sommet de l'arbre arrive en bas de la plaque, et le rayon venant du pied de l'arbre arrive en haut. L'image se forme donc **renversée tête en bas**.
2. Il s'agit d'une configuration sablier de Thalès :
   Distance objet : $D = 30\text{ m} = 3\,000\text{ cm}$.
   Profondeur boîte : $d = 20\text{ cm}$.
   Hauteur arbre : $H = 15\text{ m} = 1\,500\text{ cm}$.
   Thalès : $\frac{h_{\text{image}}}{H_{\text{arbre}}} = \frac{d}{D} \implies \frac{h}{1\,500} = \frac{20}{3\,000} = \frac{1}{150}$.
   $h = \frac{1\,500}{150} = 10\text{ cm}$.
   L'arbre formera une image miniature de $10\text{ centimètres}$ de haut au fond de la boîte.

---

### La question qui ouvre la suite

Quand nous agrandissons un cube ou une pyramide, les volumes se multiplient par $k^3$ : ils grimpent à toute vitesse. Mais que se passe-t-il lorsque l'on ne se contente pas de tripler une dimension, mais que l'on répète une multiplication des dizaines de fois d'affilée ?

C'est l'histoire d'un roi d'Orient qui croyait offrir une modeste poignée de riz à l'inventeur du jeu d'échecs, et qui vit son royaume tout entier submergé sous une montagne de céréales. Bienvenue dans le monde vertigineux des **puissances, des priorités opératoires et de la notation scientifique** !
