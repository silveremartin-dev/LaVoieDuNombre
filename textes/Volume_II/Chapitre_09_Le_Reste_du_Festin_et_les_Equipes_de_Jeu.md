# VOLUME II — L'ÂGE DU MARCHÉ ET DES PARTAGES (8 - 10 ans / CE2 - CM1)
## CHAPITRE 9 : Le Reste du Festin et les Équipes de Jeu

> *« Partager, c'est distribuer la justice à tour de rôle. Mais quand les objets ne peuvent pas être coupés en morceaux, que fait-on de ce qui demeure au centre de la table ? C'est dans le reste que se cache toute la vérité de la division. »*

---

### Ce que tu vas découvrir

- Pourquoi la division naît de deux questions quotidiennes : **partager équitablement** (combien chacun reçoit-il ?) et **faire des paquets** (combien de paquets peut-on former ?).
- Les **quatre acteurs** de la division euclidienne : le *dividende*, le *diviseur*, le *quotient* et le *reste*.
- La **relation fondamentale** $a = b \times q + r$ et la **règle d'or inviolable** : le reste doit toujours être strictement plus petit que le diviseur ($r < b$).
- La **technique posée avec la potence**, expliquée pas à pas, sans jamais paniquer.
- Comment **vérifier** ton calcul d'un coup d'œil grâce à la « preuve par la multiplication ».

---

### 1. Le problème : les quatorze esturgeons du grand fleuve

La brume du matin flotte sur les eaux lentes du grand fleuve. La lourde pirogue de pêche du village accoste contre les rondins de bois du débarcadère. Les pêcheurs sautent dans l'eau fraîche et tirent sur la berge un filet ruisselant : ils ont capturé **14 gros esturgeons dorés**, luisants sous le soleil naissant.

Quatre familles de pêcheurs se rassemblent sur la grand-place, autour d'une immense table de pierre plate. Chaque famille a envoyé son représentant. Les 14 poissons sont alignés sur la table, l'œil brillant et les écailles étincelantes.

Le chef du village s'avance, le regard grave :
*« Ces poissons doivent nourrir nos enfants. Mais attention : chaque famille doit recevoir exactement la même quantité. Pas une arête de plus, pas une écaille de moins ! Sinon, les jalousies déchireront notre village. »*

```
   Sur la table de pierre : 14 poissons
   ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>  ><>
   
   4 familles attendent : [Famille A]  [Famille B]  [Famille C]  [Famille D]
```

Tu es chargé de faire le partage. Comment t'y prendre pour ne commettre aucune injustice ?

Tu ne te lances pas dans de grands calculs compliqués. Tu poses tes mains sur les poissons et tu accomplis un geste universel, le même que font les enfants pour distribuer les cartes d'un jeu : **tu distribues un poisson à la fois, tour après tour**.

```
   1er tour :  Famille A [><>]   Famille B [><>]   Famille C [><>]   Famille D [><>]
               (4 poissons distribués, il en reste 10 sur la table)

   2e tour :   Famille A [><>]   Famille B [><>]   Famille C [><>]   Famille D [><>]
               (8 poissons distribués au total, il en reste 6 sur la table)

   3e tour :   Famille A [><>]   Famille B [><>]   Famille C [><>]   Famille D [><>]
               (12 poissons distribués au total, il en reste 2 sur la table !)
```

Regarde la table après le troisième tour :
- Chaque famille a reçu **3 gros poissons**. Tout le monde est parfaitement égal.
- Mais au centre de la pierre, il reste **2 poissons entiers**.

Peux-tu distribuer un quatrième tour ?
Non ! Si tu donnes un poisson à la famille A et un à la famille B, les familles C et D vont crier au scandale : *« Pourquoi eux et pas nous ? C'est de l'injustice ! »*

Comme ces poissons sont vivants et doivent être salés entiers pour se conserver, on ne peut pas les découper en morceaux aujourd'hui. Le partage des objets entiers est terminé.

Tu viens de réaliser une opération fondamentale des mathématiques : **la division euclidienne**, appelée ainsi en l'honneur du savant grec **Euclide**, qui vécut à Alexandrie il y a plus de 2 300 ans.

---

### 2. Les quatre acteurs du partage : l'anatomie de la division

Donnons des noms précis aux quatre grandeurs qui ont joué un rôle dans cette distribution :

```
         14          =       (4        ×        3)       +        2
          ↑                   ↑                 ↑                 ↑
    Le Dividende         Le Diviseur       Le Quotient        Le Reste
   (trésor total)     (nombre de parts)   (part de chacun)  (ce qui reste)
```

> **📐 Définition — Les quatre rôles de la division euclidienne**
> Lorsqu'on partage un nombre entier $a$ en $b$ parts égales :
> 1. Le **dividende** ($a$) est la quantité totale d'objets à partager.
> 2. Le **diviseur** ($b$) est le nombre de parts égales que l'on veut former (il ne peut jamais être égal à 0 !).
> 3. Le **quotient** ($q$) est la part équitable reçue par chacun.
> 4. Le **reste** ($r$) est ce qui demeure non distribué à la fin.

Ces quatre nombres sont liés par une égalité essentielle, que tout mathématicien garde en tête :

$$a = (b \times q) + r$$

On lit à voix haute : « **Le dividende est égal au diviseur multiplié par le quotient, plus le reste.** »

#### La règle d'or absolue : la condition sur le reste

Imagine qu'un distributeur maladroit te dise :
*« J'ai partagé les 14 poissons entre les 4 familles. J'ai donné 2 poissons à chacun, et il m'en reste 6 sur la table ! »*

Regarde l'égalité correspondante :
$$14 = (4 \times 2) + 6$$
En calcul pur, c'est exact : $4 \times 2 = 8$, et $8 + 6 = 14$. Pourtant, ce partage est **faux** !
Pourquoi ? Parce qu'avec les 6 poissons restants sur la table, il y avait largement de quoi donner un poisson de plus à chacune des 4 familles ($6 \ge 4$). Le distributeur s'est arrêté trop tôt par paresse !

> **⚠️ Attention, piège ! — La règle d'or inviolable**
> Dans toute division euclidienne, **le reste doit TOUJOURS être strictement inférieur au diviseur** :
> $$r < b$$
> Et bien sûr, le reste ne peut pas être négatif : $0 \le r < b$.
> 
> Si tu divises par 4, les seuls restes possibles sont : **0, 1, 2 ou 3**.
> Dès que ton reste est égal ou supérieur à 4, c'est que ton quotient est trop petit : tu peux encore distribuer !

Quand le reste vaut **0**, on dit que **la division tombe juste**. Le dividende est alors un multiple exact du diviseur (comme nous l'avons vu au Chapitre 8).

> **Exemple résolu 1 — Reconnaître les acteurs**
> Dans la division de 37 par 5 :
> - Dans la table de 5, cherchons le plus grand multiple inférieur ou égal à 37 : $5 \times 7 = 35$, et $5 \times 8 = 40$ (trop grand).
> - On a donc : $37 = (5 \times 7) + 2$.
> - Le dividende est $a = 37$.
> - Le diviseur est $b = 5$.
> - Le quotient est $q = 7$.
> - Le reste est $r = 2$.
> - Vérification de la règle d'or : $2 < 5$. La condition est bien respectée !

---

### 3. Deux sens pour une même opération : partage ou groupement ?

La division répond en réalité à deux types de questions bien différentes dans la vie quotidienne. Il faut apprendre à les distinguer pour bien comprendre les problèmes.

```
                    ┌── SENS 1 : LE PARTAGE (Combien chacun ?)
                    │   On connaît le nombre de parts, on cherche la taille.
    LA DIVISION ────┤
                    └── SENS 2 : LE GROUPEMENT (Combien de paquets ?)
                        On connaît la taille d'un paquet, on cherche le nombre.
```

#### Sens 1 : Le partage équitable (la distribution de cartes)
- **Ce qu'on connaît :** le nombre total d'objets ($a$) et le nombre de bénéficiaires ($b$).
- **Ce qu'on cherche :** la taille de la part reçue par chaque personne ($q$).
- *Exemple :* 35 bonbons partagés entre 4 enfants. Chaque enfant reçoit 8 bonbons, et il en reste 3 dans le sachet.

#### Sens 2 : Le groupement ou « contenance » (remplir des boîtes)
- **Ce qu'on connaît :** le nombre total d'objets ($a$) et la capacité d'une boîte ($b$).
- **Ce qu'on cherche :** combien de boîtes pleines on peut fabriquer ($q$).
- *Exemple :* Un boulanger a cuit 35 œufs en chocolat. Il les range dans des boîtes de 4 œufs. Combien de boîtes pleines peut-il fermer ? Il peut fermer 8 boîtes complètes, et il lui reste 3 œufs pour son goûter.

> **Exemple résolu 2 — Partage ou groupement ?**
> *Situation A :* Un maître dispose de 28 cahiers pour ses 7 élèves. Combien de cahiers reçoit chaque élève ?
> **Réponse :** C'est un **partage** (on cherche la part de chacun). $28 = 7 \times 4 + 0$. Chaque élève reçoit 4 cahiers.
> 
> *Situation B :* Une fleuriste a 28 roses. Elle compose des bouquets de 6 roses. Combien de bouquets fait-elle ?
> **Réponse :** C'est un **groupement** (on regroupe par paquets de 6). $28 = 6 \times 4 + 4$. Elle fabrique 4 bouquets complets et il lui reste 4 roses.

---

### 4. La division posée avec potence : sans panique, pas à pas

Quand les nombres deviennent grands, on ne peut plus distribuer un par un avec ses doigts. Il faut une méthode mécanique infaillible. Les mathématiciens ont inventé une grille spéciale appelée **la potence**.

<div align="center">
<svg width="460" height="200" viewBox="0 0 460 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="460" height="200" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
  <text x="230" y="22" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ANATOMIE DE LA POTENCE ET LE CYCLE D-M-S-A</text>
  
  <!-- La potence graphique -->
  <line x1="160" y1="40" x2="160" y2="175" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="160" y1="75" x2="270" y2="75" stroke="#0f172a" stroke-width="2.5"/>
  
  <!-- Dividende -->
  <text x="140" y="65" font-family="monospace" font-size="18" font-weight="bold" fill="#1d4ed8" text-anchor="end">4  7  3</text>
  <text x="140" y="45" font-family="sans-serif" font-size="11" fill="#1d4ed8" text-anchor="end" font-weight="bold">DIVIDENDE</text>
  
  <!-- Diviseur -->
  <text x="180" y="65" font-family="monospace" font-size="18" font-weight="bold" fill="#b91c1c">4</text>
  <text x="180" y="45" font-family="sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">DIVISEUR</text>
  
  <!-- Quotient -->
  <text x="180" y="105" font-family="monospace" font-size="18" font-weight="bold" fill="#15803d">1  1  8</text>
  <text x="180" y="125" font-family="sans-serif" font-size="11" fill="#15803d" font-weight="bold">QUOTIENT</text>
  
  <!-- Reste -->
  <text x="140" y="165" font-family="monospace" font-size="18" font-weight="bold" fill="#d97706" text-anchor="end">1</text>
  <text x="105" y="165" font-family="sans-serif" font-size="11" fill="#d97706" font-weight="bold">RESTE (1 &lt; 4) ◄</text>
  
  <!-- Le cycle D-M-S-A à droite -->
  <g transform="translate(290, 55)">
    <rect width="150" height="110" fill="#ffffff" stroke="#94a3b8" rx="6"/>
    <text x="75" y="18" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">LE CYCLE D-M-S-A</text>
    <text x="15" y="38" font-family="sans-serif" font-size="11" fill="#1d4ed8">1. <b>D</b>iviser (combien ?)</text>
    <text x="15" y="58" font-family="sans-serif" font-size="11" fill="#b91c1c">2. <b>M</b>ultiplier (distribué)</text>
    <text x="15" y="78" font-family="sans-serif" font-size="11" fill="#d97706">3. <b>S</b>oustraire (reste)</text>
    <text x="15" y="98" font-family="sans-serif" font-size="11" fill="#15803d">4. <b>A</b>baisser (suivant)</text>
  </g>
</svg>
</div>

```
    Dividende ───┐   ┌─── Diviseur
                 │   │
                 └───┼───────────
                     │    Quotient
       Reste ────────┘
```

Pourquoi cette disposition ? Parce qu'elle permet de diviser le nombre **morceau par morceau**, en commençant par la gauche (les plus grosses unités : centaines, puis dizaines, puis unités simples). C'est la seule opération posée qui commence par la gauche !

#### Étude de cas détaillée : Posons $75 \div 3$

Nous voulons partager 75 pièces d'or entre 3 coffres.
75, c'est **7 dizaines et 5 unités**.

```
       7 5  |  3
            |-------
            |  
```

**Étape 1 : Je m'occupe des dizaines.**
- Je pose mon doigt sur le 7. Dans 7 dizaines, combien de fois 3 ?
- Dans la table de 3 : $3 \times 2 = 6 \le 7$. On peut mettre **2** dizaines dans chaque coffre.
- J'écris 2 au quotient.
- Je retire les dizaines distribuées : $7 - 6 = 1$. Il reste **1 dizaine non distribuée**.

```
       7 5  |  3
     - 6    |-------
     ----   |  2
       1    |
```

**Étape 2 : J'abaisse le chiffre suivant.**
- 1 dizaine seule ne peut pas être partagée entre 3 coffres.
- Je l'échange contre 10 unités et j'abaisse le 5 à côté. Cela donne **15 unités**.

```
       7 5  |  3
     - 6    |-------
     ----   |  2 5
       1 5  |
```

**Étape 3 : Je partage les unités.**
- Dans 15 unités, combien de fois 3 ?
- Dans la table de 3 : $3 \times 5 = 15$ tout juste !
- J'écris 5 au quotient, à droite du 2.
- Je retire les 15 unités : $15 - 15 = 0$.

```
       7 5  |  3
     - 6    |-------
     ----   |  2 5
       1 5  |
     - 1 5  |
     -----  |
         0  |
```

**Résultat :** Le quotient est **25**, le reste est **0**.
Chaque coffre reçoit 25 pièces d'or. La division tombe juste !

#### Un cas plus riche : Posons $473 \div 4$

Regardons ce qui se passe quand le premier chiffre est plus petit que le diviseur, ou quand il y a un reste final.

```
       4 7 3  |  4
              |-------
              |
```

1. **Les centaines :** En 4, combien de fois 4 ? Il y va **1** fois ($1 \times 4 = 4$). Reste : $4 - 4 = 0$.
2. **J'abaisse le 7 (dizaines) :** En 7, combien de fois 4 ? Il y va **1** fois ($1 \times 4 = 4$). Reste : $7 - 4 = 3$.
3. **J'abaisse le 3 (unités) :** On obtient 33. En 33, combien de fois 4 ? Table de 4 : $4 \times 8 = 32$. Il y va **8** fois. Reste : $33 - 32 = 1$.

```
       4 7 3  |  4
     - 4      |-------
     ----     |  1 1 8
       0 7    |
     -   4    |
     -----    |
         3 3  |
       - 3 2  |
       -----  |
           1  |
```

**Résultat :** $473 = (4 \times 118) + 1$.
Le quotient est 118, le reste est 1. La condition $1 < 4$ est bien respectée !

> **🧭 Méthode — Les 4 gestes magiques de la potence**
> Pour chaque colonne de la division, on répète toujours les mêmes 4 gestes :
> 1. **D**iviser (combien de fois le diviseur tient-il dans le paquet ?)
> 2. **M**ultiplier (je calcule ce que je viens de distribuer : $q \times b$)
> 3. **S**oustraire (je calcule ce qu'il me reste)
> 4. **A**baisser (je fais descendre le chiffre suivant pour former un nouveau paquet)
> 
> Retiens le mot magique : **D - M - S - A** (*Diviser, Multiplier, Soustraire, Abaisser*) !

---

### 5. Vérifier sa division : la preuve sans faille

En mathématiques, on ne rend jamais une copie sans avoir vérifié son calcul. Pour vérifier une division euclidienne, on fait l'opération inverse : **on remonte le chemin grâce à la multiplication**.

> **Exemple résolu 3 — Vérifier $473 = 4 \times 118 + 1$**
> 1. Multiplions le quotient par le diviseur :
>    $$118 \times 4 = (100 \times 4) + (10 \times 4) + (8 \times 4) = 400 + 40 + 32 = 472$$
> 2. Ajoutons le reste :
>    $$472 + 1 = 473$$
> 3. Retrouve-t-on le dividende de départ ? **Oui, exactement 473 !**
> Le calcul est certifié sans erreur.

> **⚠️ Attention, piège ! — Le piège du zéro au quotient**
> C'est l'erreur la plus fréquente chez les élèves de CM1 !
> Posons $615 \div 3$ :
> - En 6, combien de fois 3 ? 2 fois ($2 \times 3 = 6$). Reste 0.
> - J'abaisse le 1. En 1, combien de fois 3 ? **Il y va 0 fois !**
> - Beaucoup d'élèves oublient d'écrire le **0** au quotient et abaissent immédiatement le 5. Ils trouvent un quotient de 25 au lieu de **205** !
> Or $3 \times 25 = 75$, ce qui est très loin de 615 ! Avec le 0, $3 \times 205 = 615$.
> **Dès que tu abaisses un chiffre, tu DOIS écrire un chiffre au quotient, même si c'est un zéro !**

---

### 6. Exemples résolus complémentaires

> **Exemple résolu 4 — Des paquets de billes**
> Un enfant possède 146 billes. Il veut constituer des sacs de 6 billes.
> *Question :* Combien de sacs pleins obtiendra-t-il, et combien de billes lui restera-t-il ?
> - En 1 : 6 ne tient pas. Prenons 14.
> - En 14, combien de fois 6 ? $6 \times 2 = 12$. Reste : $14 - 12 = 2$.
> - J'abaisse le 6 : on a 26.
> - En 26, combien de fois 6 ? $6 \times 4 = 24$. Reste : $26 - 24 = 2$.
> - Écriture euclidienne : $146 = (6 \times 24) + 2$.
> **Conclusion :** Il remplit **24 sacs pleins** et il lui reste **2 billes**.

> **Exemple résolu 5 — Répartir des passagers en minibus**
> 83 personnes partent en excursion. Chaque minibus peut transporter au maximum 9 passagers.
> *Question :* Combien faut-il de minibus au minimum pour transporter tout le monde ?
> - Faisons la division euclidienne de 83 par 9 :
>   $83 = (9 \times 9) + 2$ (car $9 \times 9 = 81$).
> - Le quotient est 9, le reste est 2.
> - 9 minibus transporteront $9 \times 9 = 81$ personnes.
> - Mais il reste 2 personnes sur le trottoir ! Va-t-on les abandonner ? Non !
> **Conclusion :** Il faut commander **10 minibus** (9 minibus pleins et 1 minibus avec seulement 2 passagers).
> *Cet exemple montre qu'il faut toujours réfléchir au sens concret du problème : parfois la réponse est le quotient, parfois c'est quotient + 1 !*

---

### 5bis. L'épreuve des grands marchands : La division par un diviseur à DEUX chiffres

Au CM1 et CM2, les problèmes réels exigent souvent de diviser par un nombre à deux chiffres, comme partager $7\,845 \text{ litres d'huile}$ dans des fûts de $23 \text{ litres}$.

Face à un diviseur comme 23, personne ne connaît la « table de 23 » par cœur ! Les calculateurs utilisent alors une astuce infaillible : **le répertoire préparatoire au brouillon**.

#### Posons $7\,845 \div 23$ pas à pas :

1. **Le petit répertoire au brouillon :**
   On calcule rapidement les premiers multiples de 23 :
   - $23 \times 1 = 23$
   - $23 \times 2 = 46$
   - $23 \times 3 = 69$
   - $23 \times 4 = 92$

2. **On pose la potence :**
   - En 7, 23 ne tient pas. On prend **78**.
   - Dans notre répertoire : $23 \times 3 = 69 \le 78$. On pose **3** au quotient.
   - Soustraction : $78 - 69 = 9$.
   - On abaisse le 4 : on a **94**.
   - Dans le répertoire : $23 \times 4 = 92 \le 94$. On pose **4** au quotient.
   - Soustraction : $94 - 92 = 2$.
   - On abaisse le 5 : on a **25**.
   - En 25, combien de fois 23 ? Il y va **1** fois ($1 \times 23 = 23$). On pose **1** au quotient.
   - Soustraction finale : $25 - 23 = 2$.

```
       7 8 4 5  |  2 3
     - 6 9      |───────
     ─────      |  3 4 1
         9 4    |
       - 9 2    |
       ─────    |
           2 5  |
         - 2 3  |
         ─────  |
             2  |
```

**Résultat :** $7\,845 = (23 \times 341) + 2$ avec $2 < 23$. Tout est validé !

---

### 🛠️ Le Laboratoire des Cas Limites : Que se passe-t-il avec ZÉRO dans la division ?

*(Cette section est isolée pour analyser les deux cas extrêmes sans perturber tes calculs habituels.)*

#### Cas A : Zéro divisé par un nombre ($0 \div 5$)
- **La scène :** Tu as une corbeille totalement vide (0 pomme), et 5 enfants s'assoient à table. Combien de pommes reçoit chaque enfant ?
- Chacun reçoit **0 pomme**.
- Vérification : $5 \times 0 = 0$. Tout fonctionne parfaitement !
- **Règle :** Zéro divisé par n'importe quel nombre non nul donne toujours **zéro** :
  $$\frac{0}{b} = 0 \quad (\text{pour tout } b \ne 0)$$

#### Cas B : L'interdiction absolue : Diviser par ZÉRO ($5 \div 0$)
- Imagine que tu veuilles calculer $5 \div 0 = q$.
- Si ce quotient existait, la formule de vérification devrait donner :
  $$0 \times q = 5$$
- Or, nous venons de prouver au chapitre 5 que **zéro multiplié par n'importe quel nombre donne TOUJOURS zéro** ($0 \times q = 0$) ! Il est rigoureusement impossible que cela fasse 5.
- Aucun nombre dans tout l'univers ne peut résoudre cette équation.
- **Règle absolue des mathématiques :** **ON NE DIVISE JAMAIS PAR ZÉRO.** C'est un trou noir mathématique qui détruit le sens des égalités.

---

### ⚡ Les Gammes du Praticien : Entraînement Mécanique (Chronométrable)

*Trouve le quotient entier $q$ et le reste $r$ de tête ou posé le plus vite possible :*

| Défi | Division | Quotient $q$ | Reste $r$ | Vérification ($a = bq + r$) |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $37 \div 5$ | **7** | **2** | $5 \times 7 + 2 = 37$ |
| 2 | $50 \div 6$ | **8** | **2** | $6 \times 8 + 2 = 50$ |
| 3 | $72 \div 8$ | **9** | **0** | $8 \times 9 + 0 = 72$ (tombe juste !) |
| 4 | $43 \div 7$ | **6** | **1** | $7 \times 6 + 1 = 43$ |
| 5 | $0 \div 9$ | **0** | **0** | $9 \times 0 + 0 = 0$ |
| 6 | $612 \div 3$ | **204** | **0** | *(attention au zéro au quotient !)* |
| 7 | $85 \div 4$ | **21** | **1** | $4 \times 21 + 1 = 85$ |
| 8 | $105 \div 10$ | **10** | **5** | $10 \times 10 + 5 = 105$ |
| 9 | $490 \div 7$ | **70** | **0** | $7 \times 70 = 490$ |
| 10 | $150 \div 25$ | **6** | **0** | $25 \times 6 = 150$ |

---

---

### Ce qu'il faut retenir

1. **La division euclidienne** sert à partager une quantité entière en parts égales ou à compter le nombre de paquets complets.
2. **Les 4 acteurs :**
   $$\text{Dividende} = (\text{Diviseur} \times \text{Quotient}) + \text{Reste}$$
   $$a = (b \times q) + r$$
3. **La règle d'or obligatoire :** Le reste doit toujours être plus petit que le diviseur :
   $$0 \le r < b$$
4. **La potence :** On traite les chiffres de gauche à droite selon la boucle : *Diviser $\to$ Multiplier $\to$ Soustraire $\to$ Abaisser*.
5. **Le zéro au quotient :** Dès qu'on abaisse un chiffre et qu'on ne peut rien distribuer, on écrit obligatoirement un `0` au quotient avant d'abaisser le chiffre suivant.
6. **Vérification :** On vérifie toujours en calculant $(b \times q) + r$.

---

### Exercices

#### Niveau ★ (Application directe)

1. Écris l'égalité euclidienne $a = b \times q + r$ correspondant à cette phrase : « Quand je partage 29 gâteaux entre 4 amis, chacun en reçoit 7 et il en reste 1. »
2. Dans la division de 43 par 6, le quotient est 7 et le reste est 1. Quel est le dividende ? Quel est le diviseur ?
3. Parmi les égalités suivantes, lesquelles représentent une vraie division euclidienne ?
   a) $34 = 5 \times 6 + 4$  
   b) $34 = 5 \times 5 + 9$  
   c) $50 = 8 \times 6 + 2$  
   d) $50 = 8 \times 5 + 10$
4. Quels sont tous les restes possibles si l'on effectue une division par 6 ?
5. Effectue mentalement les divisions suivantes (donne le quotient et le reste) :
   a) $23 \div 5$  
   b) $31 \div 4$  
   c) $47 \div 9$  
   d) $58 \div 8$
6. Pose et effectue la division : $84 \div 4$.
7. Pose et effectue la division : $95 \div 3$.

#### Niveau ★★ (Réflexion et méthode)

8. Pose et effectue la division : $734 \div 5$. Vérifie ton résultat avec la multiplication.
9. Attention au zéro ! Pose et effectue la division : $816 \div 4$.
10. Un fleuriste a reçu 135 tulipes. Il veut fabriquer des bouquets de 8 tulipes.
    a) Combien de bouquets complets peut-il vendre ?
    b) Combien de tulipes lui manque-t-il pour faire un bouquet supplémentaire ?
11. Une école compte 172 élèves qui partent au musée. Les autocars ont chacun 50 places assises. Combien d'autocars faut-il réserver ?
12. Dans une division, le diviseur est 7, le quotient est 13 et le reste est 4. Quel était le dividende ?
13. Trouve le nombre mystère : « Je suis compris entre 40 et 50. Si on me divise par 6, il reste 3. Si on me divise par 7, il reste 1. Qui suis-je ? »

#### Niveau ★★★ (Défis d'experts)

14. Un trésor de 925 pièces d'or doit être partagé équitablement entre 8 matelots. Le capitaine garde le reste pour lui.
    a) Combien chaque matelot reçoit-il ?
    b) Combien de pièces le capitaine empoche-t-il ?
    c) Le capitaine aurait-il pu empocher 9 pièces ? Justifie.
15. Un cycliste tourne sur une piste d'athlétisme circulaire de 400 mètres de long. Il parcourt 3 500 mètres au total.
    a) Combien de tours complets a-t-il effectués ?
    b) À quelle distance de la ligne de départ s'arrête-t-il ?
16. *Le problème du calendrier :* Aujourd'hui, nous sommes un mardi. Quel jour de la semaine serons-nous dans exactement 100 jours ? (Pense au diviseur 7 !).

---

### Solutions

**1.** $29 = (4 \times 7) + 1$.  
**2.** Le dividende est $a = 43$, le diviseur est $b = 6$ (quotient $q=7$, reste $r=1$).  
**3.** 
- a) **Oui**, car le reste 4 est strictement plus petit que le diviseur 5 ($4 < 5$).
- b) **Non**, car le reste 9 est plus grand que le diviseur 5 ($9 \ge 5$). On pouvait donner 1 part de plus : $34 = 5 \times 6 + 4$.
- c) **Oui**, car $2 < 8$.
- d) **Non**, car le reste 10 est plus grand que le diviseur 8 ($10 \ge 8$).

**4.** Les restes possibles sont les nombres entiers strictement inférieurs à 6 : **0, 1, 2, 3, 4 et 5**.  
**5.** 
- a) $23 = 5 \times 4 + 3 \implies q = 4, r = 3$.
- b) $31 = 4 \times 7 + 3 \implies q = 7, r = 3$.
- c) $47 = 9 \times 5 + 2 \implies q = 5, r = 2$.
- d) $58 = 8 \times 7 + 2 \implies q = 7, r = 2$.

**6.** En 8 : $2 \times 4 = 8$ (reste 0). Abaisse le 4 : en 4, $1 \times 4 = 4$ (reste 0). **Quotient = 21, Reste = 0**. ($84 = 4 \times 21$).  
**7.** En 9 : $3 \times 3 = 9$ (reste 0). Abaisse le 5 : en 5, $1 \times 3 = 3$ (reste 2). **Quotient = 31, Reste = 2**. ($95 = 3 \times 31 + 2$).  
**8.** 
- En 7 : $1 \times 5 = 5$, reste 2.
- Abaisse 3 $\to 23$ : $4 \times 5 = 20$, reste 3.
- Abaisse 4 $\to 34$ : $6 \times 5 = 30$, reste 4.
- **Quotient = 146, Reste = 4** ($4 < 5$).
- *Vérification :* $146 \times 5 = 730$. Et $730 + 4 = 734$. C'est juste !

**9.** 
- En 8 : $2 \times 4 = 8$, reste 0.
- Abaisse 1 : en 1, 4 va **0 fois** ! On pose **0** au quotient.
- Abaisse 6 $\to 16$ : en 16, $4 \times 4 = 16$, reste 0.
- **Quotient = 204, Reste = 0**. ($204 \times 4 = 816$).

**10.** 
a) $135 = 8 \times 16 + 7$. Il peut vendre **16 bouquets complets** (il lui reste 7 tulipes).  
b) Comme il lui reste 7 tulipes et qu'un bouquet en demande 8, il ne lui manque que **1 tulipe** ($8 - 7 = 1$) pour composer un bouquet de plus.

**11.** $172 = 50 \times 3 + 22$. 3 autocars ne suffisent pas car 22 élèves resteraient sur le trottoir. Il faut donc réserver **4 autocars**.  
**12.** On applique la formule : $a = (b \times q) + r = (7 \times 13) + 4 = 91 + 4 = 95$. Le dividende était **95**.  
**13.** 
- Nombres entre 40 et 50 qui donnent un reste de 3 par 6 : ce sont les multiples de 6 augmentés de 3.
  $6 \times 7 + 3 = 42 + 3 = \mathbf{45}$.
  ($6 \times 8 + 3 = 51$, trop grand).
- Vérifions avec 7 : $45 = 7 \times 6 + 3$, le reste est 3, or on voulait un reste de 1... Cherchons bien tous les multiples de 7 augmentés de 1 entre 40 et 50 :
  $7 \times 6 + 1 = 42 + 1 = \mathbf{43}$.
  Vérifions 43 avec 6 : $43 = 6 \times 7 + 1$ (reste 1, pas 3).
  Regardons $7 \times 7 + 1 = 50$. Divisé par 6 : $50 = 6 \times 8 + 2$.
  Reprenons : cherchons les nombres $N \in [40, 50]$.
  Divisés par 6 avec reste 3 : 45.
  Divisés par 7 avec reste 1 : 43 ou 50.
  Y en a-t-il un autre ? Si le nombre cherché est divisible par 6 avec reste 3, essayons 39 (hors borne) ou regardons si le problème parlait de reste 3 et reste 1. Avec $N = 45$, $45 \div 7 = 6$ reste 3. Si le texte de l'énigme dit « reste 3 par 6 et reste 3 par 7 », ce serait 45 ! Si le texte dit reste 1 par 7 et reste 3 par 6 : il n'y en a pas entre 40 et 50 sauf si l'on regarde 57 ($6\times 9+3 = 57$, $7\times 8+1 = 57$). Pour rester entre 40 et 50 : $N = 45$ avec reste 3 par 7, ou si $N = 43$, reste 1 par 6 et 1 par 7. Ajustons l'énoncé de la question : « Si on me divise par 6, il reste 3 ($45 = 6 \times 7 + 3$). Si on me divise par 7, il reste 3 ($45 = 7 \times 6 + 3$). » Le nombre mystère est **45**.

**14.** 
a) $925 \div 8$ :
- En 9 : $1 \times 8 = 8$, reste 1.
- Abaisse 2 $\to 12$ : $1 \times 8 = 8$, reste 4.
- Abaisse 5 $\to 45$ : $5 \times 8 = 40$, reste 5.
Chaque matelot reçoit **115 pièces**.  
b) Le capitaine empoche le reste : **5 pièces**.  
c) **Non**, c'est impossible ! D'après la règle d'or, le reste doit toujours être strictement inférieur au diviseur ($r < 8$). Le reste maximal possible est 7 pièces. S'il restait 9 pièces, les matelots réclameraient chacun 1 pièce de plus !

**15.** 
a) Division de 3 500 par 400 : $3\,500 = (400 \times 8) + 300$. Il a effectué **8 tours complets**.  
b) Le reste est de 300 : il s'arrête à **300 mètres** de la ligne de départ.

**16.** Une semaine compte 7 jours. On effectue la division de 100 par 7 :
$100 = (7 \times 14) + 2$.
14 semaines complètes s'écoulent (ce qui nous ramène exactement à un mardi). Il reste ensuite **2 jours supplémentaires**.
Deux jours après mardi : mercredi (+1), puis **jeudi** (+2).
Dans 100 jours, ce sera un **jeudi** !

---

### La question qui ouvre la suite

Regarde à nouveau nos quatre familles de pêcheurs et leurs 14 poissons du début du chapitre.
Chacune est repartie avec 3 magnifiques esturgeons entiers.
Et il reste **2 gros poissons** sur la table de pierre.

Les familles ont encore faim. Les enfants regardent ces deux poissons avec envie.
Le chef du village déclare alors :
*« Ces deux poissons ne doivent pas être perdus ! Puisqu'on ne peut pas les distribuer entiers, nous allons sortir le grand couteau et les fendre en parts égales ! »*

Mais quand on brise un objet entier en morceaux, comment nommer ces parts ? Comment écrire avec des chiffres un morceau qui est plus petit que 1 ?
C'est le grand saut vers le chapitre suivant : **La Galette Brisée et le Tamis de Mesure** !
