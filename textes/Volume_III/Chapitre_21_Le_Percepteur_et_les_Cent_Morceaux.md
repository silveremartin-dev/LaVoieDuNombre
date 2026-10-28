# VOLUME III — L'ÂGE DES ARPENTEURS ET DES BÂTISSEURS (10 - 13 ans / CM2 - 6e - 5e)
## CHAPITRE 21 : Le Percepteur et les Cent Morceaux

> *« Comment comparer la part d'un pauvre bûcheron qui donne trois pièces d'argent sur dix et celle d'un riche marchand qui en verse trente sur cent cinquante ? Pour rendre la justice aveugle et comparer l'incomparable, l'esprit humain a inventé le miroir magique où chaque foule est ramenée à une assemblée idéale de cent citoyens. »*

---

### Ce que tu vas découvrir

- Pourquoi le **pourcentage** est une simple fraction déguisée sur cent ($\% = \frac{\dots}{100}$).
- Les deux gestes essentiels : **appliquer** un pourcentage (prendre $p\%$ d'une quantité) et **calculer** un taux en pourcentage ($\frac{\text{partie}}{\text{total}} \times 100$).
- Le secret des **coefficients multiplicateurs** pour les hausses ($1 + \frac{t}{100}$) et les baisses ($1 - \frac{t}{100}$).
- Le vocabulaire des statistiques : **population**, **caractère**, **effectifs** et **fréquences**.
- Les représentations graphiques : **diagramme en bâtons**, **histogramme** et **diagramme circulaire**.
- Les trois indicateurs clés d'une série statistique : la **moyenne**, la **médiane** et l'**étendue**.

---

### 1. Le problème : la foire médiévale et la querelle des marchands

Nous sommes au XIIIe siècle, au cœur de la Champagne, lors de la grande foire de Troyes. Des marchands venus de Venise, de Flandre et de Castille ont dressé des centaines d'étals couverts d'épices, de soieries et de cuirs précieux.

À la fin de la semaine, le **percepteur d'impôts du comte** s'installe à une lourde table de chêne avec sa cassette de fer et son registre relié de cuir. Deux marchands de tissus se présentent devant lui pour acquitter la taxe sur leurs bénéfices.

- Le marchand **Geoffroy** a réalisé un bénéfice modeste de **150 écus d'argent**. Le percepteur lui réclame **30 écus**.
- Le marchand **Barthélemy**, un grand drapier flamand, a engrangé un bénéfice opulent de **400 écus d'argent**. Le percepteur lui réclame **72 écus**.

Barthélemy s'insurge et frappe la table du poing :
*« C'est une injustice scandaleuse ! On me prend 72 écus alors qu'on n'en demande que 30 à Geoffroy ! Je paie plus du double de ce qu'il verse ! »*

Geoffroy réplique vivement :
*« Mais enfin, Barthélemy, tu as gagné une fortune colossale comparé à moi ! Mes 30 écus représentent une boucherie sur mon modeste étal, alors que tes 72 écus ne sont qu'une goutte d'eau dans tes coffres dorés ! »*

```
         Geoffroy (Petit marchand)                 Barthélemy (Grand marchand)
     ┌────────────────────────┐ (150 écus)     ┌────────────────────────────────────────┐ (400 écus)
     │ Taxe : 30 écus │       │                │ Taxe : 72 écus │                       │
     └────────────────────────┘                └────────────────────────────────────────┘
          Part = 30 / 150                           Part = 72 / 400
```

Le prévôt de la foire est appelé pour trancher le différend. Qui est le marchand le plus lourdement taxé ?
Pour répondre avec équité, on ne peut pas se contenter de regarder le nombre brut d'écus prélevés (72 contre 30). Il faut comparer la **proportion** prélevée par rapport au total gagné :
- Pour Geoffroy : $\frac{30}{150} = \frac{3}{15} = \frac{1}{5} = 0{,}20$.
- Pour Barthélemy : $\frac{72}{400} = \frac{18}{100} = 0{,}18$.

Imaginons que chaque marchand ait gagné une bourse de référence de **100 écus** :
- Geoffroy aurait versé **20 écus pour cent écus gagnés**.
- Barthélemy n'aurait versé que **18 écus pour cent écus gagnés** !

C'est Geoffroy qui subit l'impôt le plus lourd !
Pour comparer des quantités issues de groupes de tailles totalement différentes, l'humanité a inventé un dénominateur universel : **le nombre cent**. C'est la naissance du **pourcentage**.

---

### 2. Le Pourcentage : une fraction sur cent

#### 2.1 La notation et la signification

> **📐 Définition — Pourcentage**
> Un **pourcentage** est une manière d'écrire une fraction dont le **dénominateur est égal à 100**.
> $$t\% = \frac{t}{100}$$
> Le symbole **$\%$** se lit **« pour cent »**.

- $50\% = \frac{50}{100} = \frac{1}{2} = 0{,}5$ (la moitié).
- $25\% = \frac{25}{100} = \frac{1}{4} = 0{,}25$ (le quart).
- $75\% = \frac{75}{100} = \frac{3}{4} = 0{,}75$ (les trois quarts).
- $10\% = \frac{10}{100} = \frac{1}{10} = 0{,}1$ (le dixième).
- $100\% = \frac{100}{100} = 1$ (la totalité, l'ensemble complet).

> **💡 D'où vient le symbole $\%$ ?**
> Au XVe siècle en Italie, les marchands écrivaient en abrégé *« per cento »* sous la forme *p. 100* ou *p. c.*. Avec la rapidité de la plume des scribes, le *p* s'est effacé, le trait de fraction s'est incliné, et les deux zéros de 100 sont venus se percher de part et d'autre de la barre pour former le signe moderne $\%$.

#### 2.2 Les deux calculs fondamentaux

| Question posée | Ce que l'on cherche | Formule de calcul |
|---|---|---|
| **Appliquer un pourcentage** :<br>« Que vaut $p\%$ de la quantité $Q$ ? » | Une **valeur concrète** (en €, en kg, en élèves…) | $\text{Résultat} = Q \times \frac{p}{100}$ |
| **Calculer un pourcentage** :<br>« Quelle proportion représente la partie $A$ dans le total $T$ ? » | Un **taux en $\%$** | $\text{Taux } t\% = \frac{A}{T} \times 100$ |

---

### 3. Évolutions en pourcentage et Coefficients Multiplicateurs

Dans la vie quotidienne (soldes de vêtements, hausses de tarifs d'électricité, inflation), les quantités ne restent pas immobiles : elles **augmentent** ou **diminuent** d'un certain pourcentage.

#### 3.1 La méthode traditionnelle (en deux étapes)
Un blouson coûte $80\text{ €}$. Le magasin affiche une remise de $30\%$.
1. On calcule le montant de la remise :
   $$\text{Remise} = 80 \times \frac{30}{100} = 24\text{ €}$$
2. On soustrait la remise du prix initial :
   $$\text{Nouveau prix} = 80 - 24 = 56\text{ €}$$

#### 3.2 L'arme secrète du collège : le Coefficient Multiplicateur
Remarquons que l'on peut factoriser ce calcul en une seule multiplication fulgurante :
$$\text{Nouveau prix} = 80 - 80 \times \frac{30}{100} = 80 \times \left(1 - \frac{30}{100}\right) = 80 \times 0{,}70 = 56\text{ €}$$

Payer avec $30\%$ de réduction, c'est payer **$70\%$ du prix de départ** !

> **📐 Théorème — Coefficients Multiplicateurs**
> - Pour **augmenter** une quantité de $t\%$, on la multiplie par :
>   $$C = 1 + \frac{t}{100}$$
>   *(Exemple : une hausse de $20\% \implies \times 1{,}20$ ; une hausse de $5\% \implies \times 1{,}05$)*
>
> - Pour **diminuer** une quantité de $t\%$, on la multiplie par :
>   $$C = 1 - \frac{t}{100}$$
>   *(Exemple : une baisse de $15\% \implies \times 0{,}85$ ; une baisse de $40\% \implies \times 0{,}60$)*

---

### 4. Les Statistiques : faire parler les nombres

Lorsqu'une ville, un hôpital ou un collège recueille des milliers de données (les tailles des élèves, les salaires des employés, les notes d'un contrôle), le cerveau humain est incapable de tirer du sens d'une liste brute de chiffres en vrac.
Les **statistiques** sont la science qui organise, résume et éclaire ces masses d'informations.

#### 4.1 Le vocabulaire officiel
- La **population** : l'ensemble des personnes ou objets étudiés (ex : *tous les élèves de la classe de 5e A*).
- Un **individu** : un membre de cette population (ex : *l'élève Thomas*).
- Le **caractère** : la propriété que l'on observe chez chaque individu (ex : *la note obtenue au contrôle sur 20*).
- L'**effectif** d'une valeur : le nombre de fois où cette valeur apparaît dans la liste.
- L'**effectif total** (noté $N$) : le nombre total d'individus dans la population.
- La **fréquence** d'une valeur : la proportion d'individus qui possèdent cette valeur :
  $$f = \frac{\text{effectif}}{\text{effectif total}}$$
  La fréquence s'exprime par un nombre compris entre 0 et 1, ou en pourcentage ($f \times 100$).
  **La somme de toutes les fréquences est toujours égale à 1 (soit $100\%$).**

#### 4.2 Les trois représentations graphiques usuelles

```
   1. DIAGRAMME EN BÂTONS         2. HISTOGRAMME (classes)        3. DIAGRAMME CIRCULAIRE
        Effectif                       Effectif
        ▲                              ▲                                   .---.
      6 |    |                       6 |    ┌───┐                        .'     '.
      4 |    |   |                   4 | ┌──┤   ├───┐                   / 40% \ 25%/
      2 |  | | | |                   2 | │  │   │   │                  |-------●---|
      0 └──┴─┴─┴─┴─►                 0 └─┴──┴───┴───┴─►                 \  35% /   /
          8 10 12 15                     [0;5[ [5;10[ [10;15[            '.     .'
             Notes                           Intervalles                   '---'
```

Dans un **diagramme circulaire** (camembert), la surface et l'angle au centre de chaque secteur sont strictement proportionnels à l'effectif :
$$\text{Angle en degrés} = \text{Fréquence} \times 360^\circ$$

---

### 5. Les trois gardiens de la série : Moyenne, Médiane et Étendue

Pour résumer une série statistique en quelques chiffres représentatifs, on utilise trois indicateurs majeurs.

#### 5.1 La Moyenne ($\bar{x}$)
La **moyenne** est la valeur que chacun recevrait si l'on mettait tout en commun équitablement.
- **Moyenne simple :**
  $$\bar{x} = \frac{\text{somme de toutes les valeurs}}{\text{nombre total de valeurs}}$$
- **Moyenne pondérée (avec des effectifs ou des coefficients) :**
  $$\bar{x} = \frac{(n_1 \times x_1) + (n_2 \times x_2) + \dots + (n_k \times x_k)}{N}$$

#### 5.2 La Médiane ($Me$) : la justice du milieu
La **médiane** est la valeur centrale qui coupe la population ordonnée en deux groupes d'effectifs rigoureusement égaux :
- Au moins $50\%$ des individus ont une valeur inférieure ou égale à la médiane.
- Au moins $50\%$ des individus ont une valeur supérieure ou égale à la médiane.

> **🧭 Méthode — Comment déterminer la médiane d'une série**
> 1. Range **obligatoirement** les valeurs dans l'ordre croissant (du plus petit au plus grand).
> 2. Calcule la moitié de l'effectif total : $\frac{N}{2}$.
>    - **Cas 1 : $N$ est impair ($N = 2k + 1$) :**
>      La médiane est la valeur située exactement au rang $k + 1$.
>      *(Exemple : $N = 7 \implies \frac{7}{2} = 3{,}5$. La médiane est la 4e valeur).*
>    - **Cas 2 : $N$ est pair ($N = 2k$) :**
>      La médiane est la demi-somme (la moyenne) entre la $k$-ième et la $(k+1)$-ième valeur.
>      *(Exemple : $N = 8 \implies \frac{8}{2} = 4$. Médiane $= \frac{4\text{e valeur} + 5\text{e valeur}}{2}$).*

#### 5.3 L'Étendue ($E$) : la mesure de l'écart
L'**étendue** mesure la dispersion des résultats, c'est-à-dire l'écartement extrême de la série :
$$E = \text{Valeur maximale} - \text{Valeur minimale}$$
Une faible étendue indique que les valeurs sont très resserrées (série homogène). Une grande étendue montre une forte disparité.

---

### 6. Attention aux pièges !

> **⚠️ Attention, piège ! — Les illusions classiques**
> 1. **Le piège de la hausse suivie de la baisse :**
>    *« Si un article augmente de $20\%$ puis baisse de $20\%$, revient-il à son prix initial ? »*
>    **NON, JAMAIS !**
>    Testons avec un prix initial de $100\text{ €}$ :
>    - Hausse de $20\% \implies 100 \times 1{,}20 = 120\text{ €}$.
>    - Baisse de $20\%$ sur les $120\text{ €} \implies 120 \times (1 - 0{,}20) = 120 \times 0{,}80 = \mathbf{96\text{ €}}$ !
>    On a perdu $4\text{ €}$ au passage, car la baisse de $20\%$ s'applique sur un montant plus grand !
> 2. **Additionner des pourcentages de groupes différents :**
>    Si une classe de 20 élèves compte $50\%$ de filles et une autre classe de 30 élèves compte $40\%$ de filles, la proportion globale n'est PAS de $50\% + 40\% = 90\%$, ni de $\frac{50+40}{2} = 45\%$ !
>    Il faut compter les personnes réelles : $10 + 12 = 22$ filles sur $50$ élèves, soit $\frac{22}{50} = 44\%$.
> 3. **Confondre moyenne et médiane :**
>    Dans une petite entreprise de 5 personnes, 4 ouvriers gagnent $1\,500\text{ €}$ par mois et le grand patron gagne $21\,000\text{ €}$.
>    - Salaire moyen : $\frac{4 \times 1500 + 21000}{5} = \frac{27000}{5} = \mathbf{5\,400\text{ €}}$ !
>    - Salaire médian : la 3e personne gagne **$1\,500\text{ €}$**.
>    La moyenne donne l'illusion trompeuse que tout le monde est riche. La médiane montre la réalité de la majorité des employés !

---

### 7. Exemples résolus

#### Exemple résolu 1 — Appliquer un pourcentage dans une recette
Pour fabriquer $1{,}2\text{ kg}$ de pâte à brioche, un boulanger utilise $55\%$ de farine, $20\%$ de beurre, $15\%$ d'œufs et $10\%$ de sucre et levure.
Quelle masse de beurre (en grammes) doit-il peser ?

*Solution :*
- Convertissons la masse totale en grammes : $1{,}2\text{ kg} = 1\,200\text{ g}$.
- La proportion de beurre est de $20\%$.
- Calcul :
  $$\text{Masse de beurre} = 1\,200 \times \frac{20}{100} = 1\,200 \times 0{,}20 = 240\text{ grammes}$$
Le boulanger doit peser $240\text{ g}$ de beurre. ✔

#### Exemple résolu 2 — Calculer un taux d'admission
Dans un collège, 138 élèves de troisième se sont présentés à l'examen du brevet des collèges.
124 d'entre eux ont été admis.
Quel est le taux de réussite de ce collège ? Arrondir au dixième de pourcentage.

*Solution :*
- Effectif admis (la partie) : $A = 124$.
- Effectif total (le tout) : $T = 138$.
- Calcul du taux :
  $$t = \frac{A}{T} \times 100 = \frac{124}{138} \times 100 \approx 0{,}89855 \times 100 \approx 89{,}9\%$$
Le taux de réussite au brevet est de $89{,}9\%$. ✔

#### Exemple résolu 3 — Les soldes d'hiver et le coefficient multiplicateur
Un magasin de sport applique une démarque de $40\%$ sur une paire de baskets affichée initialement à $115\text{ €}$.
Quel est le nouveau prix soldé des baskets ?

*Solution :*
- Le coefficient multiplicateur associé à une baisse de $40\%$ est :
  $$C = 1 - \frac{40}{100} = 1 - 0{,}40 = 0{,}60$$
- Nouveau prix :
  $$\text{Prix soldé} = 115 \times 0{,}60 = 69\text{ €}$$
La paire de baskets coûte désormais $69\text{ €}$. ✔

#### Exemple résolu 4 — Tableau statistique complet d'un contrôle
Voici les notes sur 20 obtenues par les 25 élèves d'une classe de 5e :

| Note ($x_i$) | 8 | 10 | 12 | 14 | 16 | 18 | Total |
|---|---|---|---|---|---|---|---|
| Effectif ($n_i$) | 3 | 5 | 7 | 6 | 3 | 1 | 25 |
| Fréquence en $\%$ | ? | ? | ? | ? | ? | ? | $100\%$ |
| Angle en degrés | ? | ? | ? | ? | ? | ? | $360^\circ$ |

1. Compléter le tableau des fréquences et des angles pour un diagramme circulaire.
2. Calculer la note moyenne de la classe.
3. Déterminer la note médiane et l'étendue.

*Solution :*
1. Pour chaque colonne, la fréquence est $\frac{n_i}{25} \times 100$ et l'angle est $\frac{n_i}{25} \times 360^\circ$ :
   - Pour la note 8 : Fréquence $= \frac{3}{25} \times 100 = 12\%$ ; Angle $= 0{,}12 \times 360^\circ = 43{,}2^\circ$.
   - Pour la note 10 : Fréquence $= \frac{5}{25} \times 100 = 20\%$ ; Angle $= 0{,}20 \times 360^\circ = 72^\circ$.
   - Pour la note 12 : Fréquence $= \frac{7}{25} \times 100 = 28\%$ ; Angle $= 0{,}28 \times 360^\circ = 100{,}8^\circ$.
   - Pour la note 14 : Fréquence $= \frac{6}{25} \times 100 = 24\%$ ; Angle $= 0{,}24 \times 360^\circ = 86{,}4^\circ$.
   - Pour la note 16 : Fréquence $= \frac{3}{25} \times 100 = 12\%$ ; Angle $= 0{,}12 \times 360^\circ = 43{,}2^\circ$.
   - Pour la note 18 : Fréquence $= \frac{1}{25} \times 100 = 4\%$ ; Angle $= 0{,}04 \times 360^\circ = 14{,}4^\circ$.
2. **Moyenne pondérée :**
   $$\bar{x} = \frac{3 \times 8 + 5 \times 10 + 7 \times 12 + 6 \times 14 + 3 \times 16 + 1 \times 18}{25}$$
   $$\bar{x} = \frac{24 + 50 + 84 + 84 + 48 + 18}{25} = \frac{308}{25} = 12{,}32$$
   La moyenne de la classe est de $12{,}32 / 20$.
3. **Médiane et Étendue :**
   - L'effectif total est $N = 25$ (impair).
   - $\frac{25 + 1}{2} = 13$. La médiane est la **13e note** de la liste ordonnée.
   - Cumulons les effectifs :
     - Jusqu'à 8 : 3 élèves.
     - Jusqu'à 10 : $3 + 5 = 8$ élèves.
     - Jusqu'à 12 : $8 + 7 = 15$ élèves.
     La 13e note se trouve dans le groupe des 12 ! Donc la note médiane est $Me = \mathbf{12}$.
   - **Étendue :** $E = 18 - 8 = \mathbf{10}$ points. ✔

#### Exemple résolu 5 — Deux augmentations successives
Le prix du carburant augmente de $10\%$ au mois de janvier, puis augmente à nouveau de $10\%$ au mois de février.
1. Quel est le pourcentage total d'augmentation sur ces deux mois ?
2. Quel prix atteint un litre affiché au départ à $1{,}50\text{ €}$ ?

*Solution :*
1. Calculons le coefficient multiplicateur global en multipliant les coefficients :
   $$C_1 = 1 + \frac{10}{100} = 1{,}10$$
   $$C_2 = 1 + \frac{10}{100} = 1{,}10$$
   $$C_{\text{global}} = C_1 \times C_2 = 1{,}10 \times 1{,}10 = 1{,}21$$
   Or $1{,}21 = 1 + \frac{21}{100}$.
   La hausse totale n'est pas de $20\%$, mais de **$21\%$** !
2. Prix final du litre :
   $$P_{\text{final}} = 1{,}50 \times 1{,}21 = 1{,}815\text{ €} \approx 1{,}82\text{ €}$$
Le litre coûte désormais $1{,}815\text{ €}$. ✔

---

### Ce qu'il faut retenir

1. **Pourcentage :**
   - $t\% = \frac{t}{100}$.
   - Prendre $p\%$ de $Q$ : $Q \times \frac{p}{100}$.
   - Calculer un pourcentage : $\frac{\text{Partie}}{\text{Total}} \times 100$.
2. **Coefficients multiplicateurs :**
   - Augmentation de $t\%$ : $\times \left(1 + \frac{t}{100}\right)$.
   - Diminution de $t\%$ : $\times \left(1 - \frac{t}{100}\right)$.
   - Pour des évolutions successives : on **multiplie** les coefficients ($C_{\text{total}} = C_1 \times C_2$).
3. **Statistiques :**
   - **Fréquence :** $f = \frac{\text{effectif}}{N}$.
   - **Angle circulaire :** $\text{angle} = f \times 360^\circ$.
   - **Moyenne :** la somme de toutes les valeurs divisée par l'effectif total.
   - **Médiane :** la valeur qui sépare la série ordonnée en deux moitiés égales ($50\% / 50\%$).
   - **Étendue :** $\text{valeur maximale} - \text{valeur minimale}$.

---

### Exercices

#### Niveau ★ (Application directe)

**Exercice 1.** Écris chaque pourcentage sous la forme d'une fraction simplifiée puis d'un nombre décimal :
$10\%$ ; $20\%$ ; $25\%$ ; $50\%$ ; $75\%$ ; $5\%$.

**Exercice 2.** Calcule mentalement :
1. $50\%$ de $84\text{ €}$
2. $25\%$ de $120\text{ kg}$
3. $10\%$ de $350\text{ m}$
4. $1\%$ de $2\,500\text{ habitants}$

**Exercice 3.** Donne le coefficient multiplicateur associé à :
1. Une hausse de $12\%$
2. Une baisse de $25\%$
3. Une augmentation de $3{,}5\%$
4. Une remise exceptionnelle de $50\%$

**Exercice 4.** Dans une boîte de 40 chocolats, il y a 14 chocolats noirs.
Quel est le pourcentage de chocolats noirs dans la boîte ?

**Exercice 5.** Calcule la moyenne simple des cinq notes suivantes : $11$ ; $14$ ; $09$ ; $17$ ; $14$.

#### Niveau ★★ (Problèmes et graphiques)

**Exercice 6. Le smartphone soldé.**
Un téléphone portable coûte $340\text{ €}$. Pendant les soldes, son prix diminue de $15\%$.
1. Quel est le montant de l'économie réalisée en euros ?
2. Quel est le nouveau prix du téléphone ?

**Exercice 7. Facture d'électricité.**
Sur une facture d'électricité de $150\text{ €}$ hors taxes, l'État applique une TVA de $20\%$.
Quel est le montant total toutes taxes comprises (TTC) payé par le client ?

**Exercice 8. L'évolution trompeuse.**
Le prix d'un billet de train augmente de $25\%$. Quelques mois plus tard, la compagnie ferroviaire annonce une promotion de « $25\%$ de réduction immédiate ».
Un voyageur pense que le billet est revenu à son prix de départ. A-t-il raison ? Justifie par un calcul précis en prenant un billet qui coûtait $100\text{ €}$ au début.

**Exercice 9. Déterminer la médiane (cas pair et impair).**
Détermine la médiane et l'étendue de chacune des deux séries de températures relevées à midi :
- Semaine A : $14^\circ\text{C}$ ; $17^\circ\text{C}$ ; $12^\circ\text{C}$ ; $19^\circ\text{C}$ ; $21^\circ\text{C}$ ; $15^\circ\text{C}$ ; $18^\circ\text{C}$.
- Semaine B : $13^\circ\text{C}$ ; $16^\circ\text{C}$ ; $11^\circ\text{C}$ ; $20^\circ\text{C}$ ; $14^\circ\text{C}$ ; $18^\circ\text{C}$.

**Exercice 10. Le diagramme circulaire des animaux de compagnie.**
Une enquête menée auprès de 180 foyers d'un quartier donne les résultats suivants :
- 72 foyers ont un chien.
- 54 foyers ont un chat.
- 36 foyers ont des rongeurs ou oiseaux.
- 18 foyers n'ont aucun animal.
1. Calcule la fréquence de chaque catégorie en pourcentage.
2. Calcule l'angle en degrés correspondant à chaque catégorie pour construire un diagramme circulaire.

**Exercice 11. Moyenne coefficientée au collège.**
Un élève a obtenu les notes suivantes en mathématiques ce trimestre :
- Deux interrogations courtes (coefficient 1) : $12$ et $15$.
- Deux devoirs surveillés importants (coefficient 3) : $14$ et $10$.
Quelle est sa moyenne trimestrielle ?

#### Niveau ★★★ (Défis et esprit critique)

**Exercice 12. Le mystère du salaire moyen de l'usine.**
Une petite usine emploie 20 personnes réparties ainsi :
- 1 directeur général payé $10\,000\text{ €}$ par mois.
- 3 ingénieurs payés chacun $4\,000\text{ €}$ par mois.
- 16 ouvriers payés chacun $1\,500\text{ €}$ par mois.
1. Calcule le salaire moyen dans cette entreprise.
2. Calcule le salaire médian.
3. Pourquoi un syndicat d'ouvriers et le directeur général n'utiliseront-ils pas le même indicateur lors des négociations salariales ? Explique le pouvoir de manipulation de la moyenne.

**Exercice 13. Retrouver le prix initial (la marche arrière).**
Après une réduction de $20\%$ pendant les soldes, un manteau d'hiver coûte $120\text{ €}$.
Quel était son prix initial avant la remise ?
*(Attention piège : ne calcule surtout pas $120 + 20\%$ de 120 ! Utilise le coefficient multiplicateur).*

**Exercice 14. Évolutions successives et taux global.**
Le prix d'une console de jeux augmente de $5\%$ en 2024, puis de $8\%$ en 2025.
1. Quel est le taux global d'augmentation sur les deux ans réunis ?
2. Si le prix baisse ensuite de $12\%$ en 2026, la console est-elle finalement plus chère ou moins chère qu'au début de l'année 2024 ?

**Exercice 15. Le paradoxe de Simpson.**
Dans un hôpital, deux chirurgiens (Dr Martin et Dr Dupont) réalisent deux types d'opérations : des opérations bénignes (simples) et des opérations à haut risque (difficiles).
- Pour les opérations simples :
  - Dr Martin réussit 95 opérations sur 100 ($95\%$).
  - Dr Dupont réussit 19 opérations sur 20 ($95\%$).
- Pour les opérations difficiles :
  - Dr Martin réussit 10 opérations sur 20 ($50\%$).
  - Dr Dupont réussit 45 opérations sur 100 ($45\%$).
1. Pour les opérations difficiles, quel chirurgien a le meilleur taux de réussite ?
2. Calcule maintenant le taux de réussite global de chaque chirurgien toutes opérations confondues.
3. Quel chirurgien a le meilleur taux global ? Que remarques-tu d'incroyable ? Explique ce paradoxe.

---

### Solutions

**Exercice 1.**
- $10\% = \frac{1}{10} = 0{,}10$
- $20\% = \frac{1}{5} = 0{,}20$
- $25\% = \frac{1}{4} = 0{,}25$
- $50\% = \frac{1}{2} = 0{,}50$
- $75\% = \frac{3}{4} = 0{,}75$
- $5\% = \frac{1}{20} = 0{,}05$

**Exercice 2.**
1. $84 / 2 = 42\text{ €}$.
2. $120 / 4 = 30\text{ kg}$.
3. $350 / 10 = 35\text{ m}$.
4. $2\,500 / 100 = 25\text{ habitants}$.

**Exercice 3.**
1. $1 + 0{,}12 = 1{,}12$.
2. $1 - 0{,}25 = 0{,}75$.
3. $1 + 0{,}035 = 1{,}035$.
4. $1 - 0{,}50 = 0{,}50$.

**Exercice 4.**
Taux $= \frac{14}{40} \times 100 = \frac{7}{20} \times 100 = 35\%$.

**Exercice 5.**
Somme $= 11 + 14 + 9 + 17 + 14 = 65$.
Moyenne $= \frac{65}{5} = 13 / 20$.

**Exercice 6.**
1. Économie : $340 \times 0{,}15 = 51\text{ €}$.
2. Nouveau prix : $340 - 51 = 289\text{ €}$ (ou $340 \times 0{,}85 = 289\text{ €}$).

**Exercice 7.**
Montant TTC $= 150 \times (1 + 0{,}20) = 150 \times 1{,}20 = 180\text{ €}$.

**Exercice 8.**
Prix initial : $100\text{ €}$.
Après hausse de $25\%$ : $100 \times 1{,}25 = 125\text{ €}$.
Après baisse de $25\%$ : $125 \times (1 - 0{,}25) = 125 \times 0{,}75 = 93{,}75\text{ €}$.
Le voyageur a tort : le billet coûte $93{,}75\text{ €}$, soit $6{,}25\text{ €}$ de moins que le prix de départ !

**Exercice 9.**
- **Semaine A (7 valeurs) :** Ordre croissant : $12, 14, 15, \mathbf{17}, 18, 19, 21$.
  Médiane $= \mathbf{17^\circ\text{C}}$ (la 4e valeur).
  Étendue $= 21 - 12 = 9^\circ\text{C}$.
- **Semaine B (6 valeurs) :** Ordre croissant : $11, 13, \mathbf{14}, \mathbf{16}, 18, 20$.
  Médiane $= \frac{14 + 16}{2} = \mathbf{15^\circ\text{C}}$.
  Étendue $= 20 - 11 = 9^\circ\text{C}$.

**Exercice 10.**
Effectif total $N = 180$.
1. Fréquences :
   - Chiens : $\frac{72}{180} = 40\%$.
   - Chats : $\frac{54}{180} = 30\%$.
   - Rongeurs/oiseaux : $\frac{36}{180} = 20\%$.
   - Aucun : $\frac{18}{180} = 10\%$.
2. Angles :
   - Chiens : $0{,}40 \times 360^\circ = 144^\circ$.
   - Chats : $0{,}30 \times 360^\circ = 108^\circ$.
   - Rongeurs/oiseaux : $0{,}20 \times 360^\circ = 72^\circ$.
   - Aucun : $0{,}10 \times 360^\circ = 36^\circ$.

**Exercice 11.**
Somme des coefficients : $1 + 1 + 3 + 3 = 8$.
Moyenne $= \frac{1 \times 12 + 1 \times 15 + 3 \times 14 + 3 \times 10}{8} = \frac{12 + 15 + 42 + 30}{8} = \frac{99}{8} = 12{,}375 / 20$.

**Exercice 12.**
1. Somme des salaires : $1 \times 10\,000 + 3 \times 4\,000 + 16 \times 1\,500 = 10\,000 + 12\,000 + 24\,000 = 46\,000\text{ €}$.
   Salaire moyen : $\frac{46\,000}{20} = \mathbf{2\,300\text{ €}}$.
2. Effectif total $N = 20$. Les 16 premiers salaires sont de $1\,500\text{ €}$.
   La 10e et la 11e valeur sont toutes deux de $1\,500\text{ €}$.
   Salaire médian : $\mathbf{1\,500\text{ €}}$.
3. Le directeur mettra en avant le salaire moyen ($2\,300\text{ €}$) pour affirmer : *« Nos salariés sont très bien payés en moyenne »*, alors que $80\%$ d'entre eux ne gagnent que $1\,500\text{ €}$ ! Les syndicats s'appuieront sur la médiane pour dénoncer que la moitié au moins des employés est au salaire de base.

**Exercice 13.**
Soit $P_0$ le prix initial. Une baisse de $20\%$ correspond à la multiplication par $1 - 0{,}20 = 0{,}80$.
$P_0 \times 0{,}80 = 120 \implies P_0 = \frac{120}{0{,}80} = \frac{1\,200}{8} = 150\text{ €}$.
Le prix initial était de $150\text{ €}$ ! (Vérification : $150 - 20\% \text{ de } 150 = 150 - 30 = 120\text{ €}$).

**Exercice 14.**
1. $C_{\text{global}} = (1 + 0{,}05) \times (1 + 0{,}08) = 1{,}05 \times 1{,}08 = 1{,}134$.
   Hausse globale : $1{,}134 - 1 = 0{,}134 = \mathbf{+13{,}4\%}$ (et non $13\%$).
2. Avec la baisse de $12\%$ ($C_3 = 0{,}88$) :
   $C_{\text{final}} = 1{,}134 \times 0{,}88 = 0{,}99792$.
   Puisque $0{,}99792 < 1$, la console est finalement **légèrement moins chère** qu'au départ (baisse finale de $0{,}208\%$).

**Exercice 15.**
1. Opérations difficiles : Dr Martin a $50\%$, Dr Dupont a $45\%$. C'est **Dr Martin** qui a le meilleur taux.
2. Taux globaux :
   - Dr Martin : réussites $= 95 + 10 = 105$ sur un total de $100 + 20 = 120$ opérations.
     Taux global $= \frac{105}{120} = 0{,}875 = \mathbf{87{,}5\%}$.
   - Dr Dupont : réussites $= 19 + 45 = 64$ sur un total de $20 + 100 = 120$ opérations.
     Taux global $= \frac{64}{120} \approx 0{,}533 = \mathbf{53{,}3\%}$.
3. Dr Martin a un taux global de $87{,}5\%$ contre $53{,}3\%$ pour Dr Dupont !
   Le paradoxe : pour les opérations simples, ils ont le même taux ($95\%$). Pour les opérations difficiles, Dr Martin est meilleur ($50\%$ contre $45\%$). Et pourtant, globalement, Dr Martin écrase Dr Dupont !
   Explication : Dr Martin a fait $83\%$ d'opérations simples (à très fort taux de succès), alors que Dr Dupont a pris en charge $83\%$ d'opérations très risquées. Ce phénomène statistique spectaculaire s'appelle le **paradoxe de Simpson** : un facteur caché (ici, la difficulté des cas traités) fausse la comparaison globale !

---

### La question qui ouvre la suite

Nous voici parvenus au terme du Volume III. Nous savons désormais mesurer la terre, tracer des angles droits au compas et à la corde, calculer des longueurs inaccessibles avec Thalès et Pythagore, nous repérer dans un plan cartésien et résumer des foules de données avec des pourcentages.

Mais jusqu'ici, tous nos nombres étaient connus, ou retrouvés par de simples règles arithmétiques.
Que faire lorsqu'un problème cache un nombre secret sous un sac scellé sur une balance, et que ce nombre est mélangé à des opérations complexes ?

Comment inventer une langue nouvelle où les nombres inconnus s'écrivent avec des lettres comme $x$, et où la balance de justice devient une équation ?
C'est le grand passage vers l'adolescence des mathématiques : **le Volume IV et le Sac Mystère sur la Balance d'Al-Khwarizmi** !
