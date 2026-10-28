# VOLUME IV — L'ÂGE DE LA BALANCE ET DES MYSTÈRES (12 - 15 ans / 5e - 4e - 3e)
## CHAPITRE 22 : Le Sac Mystère sur la Balance d'Al-Khwarizmi

> *« L'ignorant force la serrure et déchire le sac pour voir ce qui est caché. Le mathématicien regarde les deux bras de la balance, retire un poids à gauche, un poids à droite, et l'inconnue se dévoile d'elle-même dans la lumière de la raison. »*

---

### Ce que tu vas découvrir

- Pourquoi on se met soudain à **calculer avec des lettres**, et ce que veut dire exactement « $3x$ », « $x^2$ » ou « $a(b+c)$ ».
- Comment **réduire** une expression (ranger les pommes avec les pommes) et comment **développer** grâce à la **distributivité**, prouvée avec un simple rectangle.
- Comment **tester une égalité** : vraie pour une valeur, vraie pour toutes, ou fausse — et le pouvoir d'un seul **contre-exemple**.
- Comment résoudre n'importe quelle **équation du premier degré** avec les deux gestes de la balance.
- Comment **mettre un problème en équation** : âges, périmètres, programmes de calcul, et même l'énigme du tombeau de Diophante.
- Les **pièges** classiques : $2x + 3 \neq 5x$, $x \times x \neq 2x$, le signe « $-$ » devant une parenthèse, et les équations qui n'ont… aucune solution, ou une infinité.

---

### 1. Le problème : le Grand Bazar de Bagdad et le Sac d'Or

Tu as maintenant douze ou treize ans. Quittons les plaines d'Égypte, franchissons les sables du désert et entrons dans la plus fabuleuse métropole du monde médiéval : **Bagdad**, la « Cité de la Paix », vers l'an **820**.

Au cœur de la ville se dresse la *Maison de la Sagesse* (*Bayt al-Hikma*), une immense bibliothèque où des savants venus de Perse, d'Inde et de Grèce traduisent en arabe tous les manuscrits du monde : Euclide, Ptolémée, les astronomes indiens… Mais aujourd'hui, une foule animée se presse au grand bazar des orfèvres.

Au centre d'un cercle de marchands curieux, un homme drapé dans un manteau de brocart vert a posé sur une table une magnifique **balance en laiton à deux plateaux**.

* Sur le plateau de gauche, il dépose **un sac de toile brune solidement cousu**, scellé par un cachet de cire rouge. Personne ne sait ce qu'il contient ! À côté du sac, il pose **3 lingots de cuivre** pesant chacun un kilo.
* Sur le plateau de droite, il dépose **11 lingots de cuivre** d'un kilo.

Le fléau de la balance oscille lentement… et s'immobilise, **parfaitement horizontal**.

```
              [ Sac ] + 3 kg                     11 kg
                 o─────o                        o─────o
                 \     /                        \     /
                  \   /                          \   /
         ───────────[■]────────────────────────────[■]───────────
                                    ▲
                            Pivot de la balance
```

*« Ce sac contient de la poudre d'or pur. Celui qui me dira son poids exact sans briser le cachet repartira avec tout l'or ! Mais celui qui se trompe d'un seul gramme me donnera sa monture ! »*

Personne n'ose risquer son cheval. C'est alors qu'un astronome persan s'avance d'un pas tranquille : **Muhammad ibn Musa al-Khwarizmi**.

*« La vérité est déjà sous vos yeux. Les deux plateaux sont en équilibre. Si je retire la même chose des deux côtés en même temps, la balance restera-t-elle droite ? »* — *« Bien sûr ! »* répond la foule.

De la main gauche, il retire les **3 lingots** du plateau de gauche : le plateau s'allège et monte. Mais aussitôt, de la main droite, il retire **3 lingots** du plateau de droite. Le fléau redescend et se fige à nouveau, **horizontal**.

```
                 [ Sac ]                          8 kg
                 o─────o                        o─────o
                 \     /                        \     /
                  \   /                          \   /
         ───────────[■]────────────────────────────[■]───────────
                                    ▲
```

À gauche : le sac, tout seul. À droite : $11 - 3 = 8$ lingots. *« Le sac pèse huit kilos. »* Le marchand pâlit, brise le cachet, pèse le sac seul : **huit kilos pile**.

Jusqu'ici, rien que tu ne saches déjà faire « de tête ». Mais le lendemain, le marchand revient, vexé, avec des énigmes de plus en plus retorses : deux sacs identiques et 5 kg contre 17 kg ; trois sacs et 2 kg contre un sac et 10 kg ; puis des sacs dont il retire une partie du contenu… Au bout de quelques énigmes, le calcul de tête ne suffit plus. Il faut **une langue** pour écrire ces balances et **des règles** pour les manipuler sans se tromper. Cette langue, c'est le **calcul littéral**. Ces règles, ce sont celles de l'**algèbre**.

---

### 2. Calculer avec des lettres : pourquoi et comment

#### 2.1 La lettre est un nombre qui se cache

Une lettre, en mathématiques, n'est **pas** un mot ni une abréviation d'unité. C'est **un nombre** dont on ne connaît pas (encore) la valeur, ou dont la valeur peut changer.

- Quand la lettre représente un nombre précis mais **inconnu** (le poids du sac), on l'appelle une **inconnue**.
- Quand la lettre peut prendre **n'importe quelle valeur** (le côté d'un carré quelconque), on l'appelle une **variable**.

Tu connais déjà des formules avec des lettres : le périmètre d'un carré de côté $c$ est $4 \times c$ ; l'aire d'un rectangle est $L \times \ell$. Ces formules disent quelque chose de vrai **pour tous les carrés**, pour **tous les rectangles**, d'un seul coup. C'est la grande force des lettres : **une seule phrase pour une infinité de cas**.

> **📐 Définition — Expression littérale.** Une *expression littérale* est une suite de calculs dans laquelle certains nombres sont remplacés par des lettres. Exemples : $3x + 5$ ; $\; 2(a - 4)$ ; $\; x^2 - 7x + 1$.

#### 2.2 Les conventions d'écriture (et comment les lire)

Pour aller plus vite, les mathématiciens se sont mis d'accord sur quelques abréviations. Chacune a une lecture à voix haute.

| On écrit | Cela signifie | On lit |
|---|---|---|
| $3x$ | $3 \times x$ | « trois $x$ » |
| $ab$ | $a \times b$ | « $a$ $b$ » |
| $4(x+1)$ | $4 \times (x + 1)$ | « quatre facteur de $x$ plus un » ou « quatre fois parenthèse $x$ plus un » |
| $x^2$ | $x \times x$ | « $x$ au carré » ou « $x$ deux » |
| $x^3$ | $x \times x \times x$ | « $x$ au cube » |
| $1x$ | s'écrit simplement $x$ | « $x$ » |
| $-1x$ | s'écrit simplement $-x$ | « moins $x$ » |
| $0x$ | vaut $0$ | — |

Règles de sécurité :
- On **ne supprime jamais** le signe $\times$ entre **deux nombres** : $3 \times 5$ ne s'écrit surtout pas $35$ !
- Par habitude, on écrit le **nombre devant la lettre** : $x \times 3$ s'écrit $3x$ (et non $x3$).
- Les priorités opératoires du chapitre 18 s'appliquent toujours : puissances d'abord, puis multiplications, puis additions. Ainsi $3x^2$ veut dire $3 \times (x \times x)$ et **pas** $(3x) \times (3x)$.

> **🔍 L'histoire vraie — Qui a inventé les lettres ?** Al-Khwarizmi, lui, n'écrivait **aucun symbole** ! Tout était rédigé en phrases : « un bien et dix racines égalent trente-neuf dirhams » (ce que nous écrivons $x^2 + 10x = 39$). Il appelait l'inconnue *shay'* (« la chose »). Vers 250, le Grec **Diophante** utilisait déjà des abréviations. En 1591, le Français **François Viète**, conseiller du roi Henri IV et déchiffreur de codes secrets, a eu l'idée décisive : désigner les inconnues par des voyelles et les nombres connus par des consonnes. Enfin, en 1637, **René Descartes**, dans *La Géométrie*, prend les dernières lettres de l'alphabet $x, y, z$ pour les inconnues et les premières $a, b, c$ pour les nombres connus : c'est notre convention actuelle. On raconte souvent que le $x$ viendrait du mot arabe *shay'* transcrit en espagnol *xei* ; c'est une jolie légende, mais aucun document ne la prouve vraiment.

> **💡 Le savais-tu ?** Les signes $+$ et $-$ apparaissent imprimés en 1489 dans un livre d'arithmétique commerciale de l'Allemand Johannes Widmann. Le signe $=$ a été inventé en 1557 par le Gallois **Robert Recorde**, qui en avait assez d'écrire « est égal à » : il choisit deux traits parallèles de même longueur, « car aucune chose ne peut être plus égale que deux droites parallèles ».

#### 2.3 Calculer la valeur d'une expression (substituer)

*Substituer*, c'est remplacer la lettre par un nombre. Le geste est simple, mais il exige une précaution : **remettre les signes $\times$** et **mettre les nombres négatifs entre parenthèses**.

> **✏️ Exemple résolu 1 — Calculer une expression pour plusieurs valeurs.**
> Soit $A = 3x^2 - 5x + 2$. Calculer $A$ pour $x = 4$, puis pour $x = -2$.
>
> Pour $x = 4$ : $A = 3 \times 4^2 - 5 \times 4 + 2 = 3 \times 16 - 20 + 2 = 48 - 20 + 2 = 30$.
>
> Pour $x = -2$ : $A = 3 \times (-2)^2 - 5 \times (-2) + 2 = 3 \times 4 + 10 + 2 = 24$.
>
> Remarque : $(-2)^2 = (-2) \times (-2) = 4$ (règle des signes du chapitre 20), et $-5 \times (-2) = +10$.

> **⚠️ Attention, piège ! — Le carré et le signe moins.**
> - $-x^2$ veut dire « l'opposé de $x^2$ ». Pour $x = 3$ : $-x^2 = -9$.
> - $(-x)^2$ veut dire « le carré de l'opposé de $x$ ». Pour $x = 3$ : $(-3)^2 = 9$.
> - Pour $x = -2$, $3x^2 = 3 \times 4 = 12$, mais $(3x)^2 = (-6)^2 = 36$. La puissance ne s'applique **qu'à ce qui est juste avant elle**.
> - Et $x \times x = x^2$, **pas** $2x$ ! Pour $x = 5$ : $x^2 = 25$ alors que $2x = 10$.

---

### 3. Réduire : ranger les pommes avec les pommes

Imagine un étal du bazar : « 5 melons, 3 dattes, 2 melons, 7 dattes ». Tout marchand dira : « 7 melons et 10 dattes ». Il **regroupe ce qui est de même nature**. Mais il ne dira jamais « 17 melons-dattes » !

En calcul littéral, c'est pareil. $5x + 3 + 2x + 7$ se range en $7x + 10$. Les « $x$ » vont avec les « $x$ », les nombres seuls avec les nombres seuls. Mais $7x + 10$ ne peut pas devenir $17x$ : ce ne sont pas des objets de même nature.

> **📐 Définition — Termes semblables, réduire.**
> - Dans une somme, chaque morceau séparé par $+$ ou $-$ est un **terme**. Dans $5x^2 - 3x + 8$, les termes sont $5x^2$, $-3x$ et $8$.
> - Le nombre placé devant la partie littérale s'appelle le **coefficient** : dans $-3x$, le coefficient est $-3$.
> - Deux termes sont **semblables** s'ils ont **exactement la même partie littérale** : $4x$ et $-7x$ sont semblables ; $3x^2$ et $x^2$ aussi ; mais $3x$ et $3x^2$ **ne le sont pas**.
> - **Réduire** une expression, c'est regrouper les termes semblables en additionnant leurs coefficients, jusqu'à obtenir une écriture la plus courte possible.

Pourquoi a-t-on le droit d'écrire $5x + 2x = 7x$ ? Parce que $5x + 2x$, c'est « 5 sacs plus 2 sacs », donc 7 sacs. Nous le prouverons dans un instant avec la distributivité.

> **✏️ Exemple résolu 2 — Réduire.**
> a) $B = 5x + 3 - 2x + 7$. On regroupe : $(5x - 2x) + (3 + 7) = 3x + 10$.
>
> b) $C = 4x^2 - 3x + x^2 + 7x - 1$. Les $x^2$ : $4x^2 + x^2 = 5x^2$. Les $x$ : $-3x + 7x = 4x$. Les nombres : $-1$. Donc $C = 5x^2 + 4x - 1$.
>
> c) $D = 2a \times 3a$. Ici c'est un **produit** : on multiplie les nombres entre eux et les lettres entre elles : $2 \times 3 \times a \times a = 6a^2$.
>
> d) $E = 2a + 3a = 5a$ (somme), alors que $2a \times 3a = 6a^2$ (produit). Ne confonds jamais les deux !

> **⚠️ Attention, piège ! — Ce qu'on ne peut pas réduire.**
> - $2x + 3$ **ne vaut pas** $5x$. Test : pour $x = 10$, $2x + 3 = 23$ mais $5x = 50$.
> - $x^2 + x$ **ne vaut pas** $x^3$ ni $2x^2$. Test : pour $x = 2$, $x^2 + x = 6$, $x^3 = 8$, $2x^2 = 8$.
> - $3x^2 + 2x^2 = 5x^2$, **et non** $5x^4$ : on additionne des « paquets de $x^2$ », on ne multiplie rien.

---

### 4. La distributivité : un rectangle qui ne ment pas

#### 4.1 L'idée

Un orfèvre vend des colliers. Chaque collier contient $a$ perles d'or et $b$ perles d'argent. Une cliente en commande 3. Combien de perles en tout ? On peut compter collier par collier : $3 \times (a + b)$. Ou bien compter toutes les perles d'or, puis toutes les perles d'argent : $3a + 3b$. Le nombre de perles est le même ! Donc $3(a + b) = 3a + 3b$.

#### 4.2 La preuve par le rectangle

Dessine un rectangle de hauteur $k$ et de longueur $a + b$, coupé en deux.

```
            a              b
     ┌──────────────┬──────────┐
     │              │          │
  k  │   aire k×a   │ aire k×b │
     │              │          │
     └──────────────┴──────────┘
     ◄────────── a + b ─────────►
```

L'aire du grand rectangle est $k \times (a + b)$. Mais c'est aussi la somme des aires des deux petits : $k \times a + k \times b$. **Une même surface, deux façons de la calculer** : elles sont donc égales.

> **📐 Propriété — Distributivité simple.** Pour tous nombres $k$, $a$, $b$ :
> $$k(a + b) = ka + kb \qquad\text{et}\qquad k(a - b) = ka - kb.$$
> Lu de gauche à droite, on **développe** (on transforme un produit en somme). Lu de droite à gauche, on **factorise** (on transforme une somme en produit, en mettant en évidence le **facteur commun** $k$).

Le mot « distributivité » vient de l'image du facteur $k$ qui est **distribué** à chaque terme de la parenthèse, comme un facteur des postes distribue une lettre dans chaque boîte.

Et voici la preuve promise de $5x + 2x = 7x$ : c'est la distributivité lue à l'envers, $5x + 2x = (5 + 2)x = 7x$.

> **✏️ Exemple résolu 3 — Développer et réduire.**
> a) $3(2x - 5) = 3 \times 2x - 3 \times 5 = 6x - 15$.
>
> b) $-2(x - 4) = (-2) \times x - (-2) \times 4 = -2x + 8$. (Attention aux signes : $-2 \times (-4) = +8$.)
>
> c) $x(x + 3) = x \times x + x \times 3 = x^2 + 3x$.
>
> d) $F = 4(x + 2) - 3(2x - 1) = 4x + 8 - 6x + 3 = -2x + 11$.

#### 4.3 Le signe « moins » devant une parenthèse

Une parenthèse précédée de $-$ cache en réalité un facteur $-1$ : $-(a + b) = (-1) \times (a + b) = -a - b$. Conséquence :

> **📐 Règle — Supprimer des parenthèses.**
> - Précédée de $+$ : on enlève les parenthèses **sans rien changer**. $\; 7 + (3x - 2) = 7 + 3x - 2$.
> - Précédée de $-$ : on enlève les parenthèses **en changeant le signe de chaque terme** à l'intérieur. $\; 7 - (3x - 2) = 7 - 3x + 2 = 9 - 3x$.

> **⚠️ Attention, piège !** L'erreur la plus fréquente du collège : écrire $7 - (3x - 2) = 7 - 3x - 2$. On a oublié de changer le signe du **deuxième** terme. Test avec $x = 0$ : $7 - (0 - 2) = 9$, mais $7 - 0 - 2 = 5$. Le test démasque l'erreur en deux secondes.

#### 4.4 Factoriser : le chemin du retour

> **✏️ Exemple résolu 4 — Factoriser par un facteur commun.**
> a) $6x + 9$ : $6x = 3 \times 2x$ et $9 = 3 \times 3$. Facteur commun $3$ : $6x + 9 = 3(2x + 3)$.
>
> b) $5x^2 - 10x$ : $5x^2 = 5x \times x$ et $10x = 5x \times 2$. Facteur commun $5x$ : $5x^2 - 10x = 5x(x - 2)$.
>
> c) $7a + 7 = 7 \times a + 7 \times 1 = 7(a + 1)$. Ne pas oublier le « $1$ » !
>
> **Vérification systématique** : on redéveloppe. $5x(x - 2) = 5x^2 - 10x$ ✓.

Pourquoi factoriser ? Parce qu'un **produit** est souvent plus facile à étudier qu'une somme. Tu le verras au chapitre suivant, où la factorisation permettra de résoudre des équations qu'aucune balance ne sait résoudre.

---
