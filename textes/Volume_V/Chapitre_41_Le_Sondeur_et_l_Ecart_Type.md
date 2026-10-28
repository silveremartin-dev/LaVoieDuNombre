# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 41 : Le Sondeur et l'Écart-Type

> *« Si vous mettez votre tête dans un four brûlant et vos pieds dans un bloc de glace, un statisticien imprudent vous dira que, "en moyenne", votre température corporelle est idéale. La moyenne est un phare qui éclaire le centre, mais qui plonge dans l'ombre les tempêtes de la périphérie. Pour comprendre le monde réel, il faut mesurer l'éparpillement. »*

---

### Ce que tu vas découvrir

- Le piège mortel de la moyenne : pourquoi deux usines, deux classes ou deux traitements médicaux ayant la même moyenne peuvent être radicalement opposés.
- Les indicateurs de position : la **moyenne pondérée** ($\bar{x}$) contre la **médiane** ($M_e$), et pourquoi la médiane ne se laisse pas tromper par les milliardaires.
- Les sentinelles du quart : les **quartiles** $Q_1$ et $Q_3$, et l'**écart interquartile**.
- L'art du résumé graphique : le **diagramme en boîte à moustaches** (*boxplot*) de John Tukey.
- Le mystère du carré : pourquoi la somme des écarts à la moyenne s'annule toujours ($\sum (x_i - \bar{x}) = 0$), et pourquoi il a fallu inventer la **variance** et l'**écart-type** $\sigma$.
- La formule magique de **König-Huygens** pour calculer la variance en un clin d'œil.
- La loi de l'échantillonnage : comment un sondeur peut prédire le vote de 45 millions d'électeurs en interrogeant seulement 1 000 personnes, grâce à l'**intervalle de fluctuation**.
- Des simulations d'échantillonnage programmées en **Python**.

---

### 1. Le problème : les deux usines d'arbres de transmission

Nous sommes dans une usine aéronautique de pointe près de Toulouse.
L'usine fabrique des axes de transmission en titane destinés aux réacteurs d'avions de ligne. Le cahier des charges des ingénieurs est formel : pour s'insérer au millième de millimètre près dans les roulements à billes de la turbine, le diamètre nominal d'un axe doit être exactement de **$50{,}00$ millimètres**. Un axe de $50{,}10$ mm coincera le moteur ; un axe de $49{,}90$ mm créera un jeu mécanique destructeur à 10 000 tours par minute.

Deux entreprises sous-traitantes, l'atelier **Alpha** et l'atelier **Beta**, soumettent chacune un lot de 1 000 axes usinés.
Le responsable qualité mesure les échantillons :

- Dans l'atelier **Alpha**, la moyenne des diamètres est très exactement de **$50{,}00$ mm**.
- Dans l'atelier **Beta**, la moyenne des diamètres est également très exactement de **$50{,}00$ mm**.

Un acheteur naïf dirait : *« Les deux ateliers se valent, choisissons le moins cher ! »*
Mais le directeur technique examine les pièces d'un peu plus près au microscope électronique :

```
Atelier Alpha :
   Toutes les pièces sont comprises entre 49,98 mm et 50,02 mm.
   Elles sont quasi parfaites, regroupées comme un essaim serré autour de 50,00 mm.

                                 |
                               |||||
                              |||||||
                         ────┼┼┼┼┼┼┼┼┼────
                            49,99  50  50,01

Atelier Beta :
   Une pièce fait 46,00 mm, une autre 54,00 mm, une autre 48,20 mm...
   Les pièces sont dispersées dans un désordre effrayant !

             |         |         |         |         |
             |    |    |    |    |    |    |    |    |
        ─────┼────┼────┼────┼────┼────┼────┼────┼────┼────
            46   47   48   49   50   51   52   53   54
```

Dans l'atelier Beta, **aucune pièce ou presque ne pourra être montée dans l'avion** ! Certaines sont beaucoup trop grosses, d'autres beaucoup trop fines, même si par un pur hasard de symétrie, leur moyenne mathématique tombe pile sur 50 mm. Si l'on montait les pièces de l'atelier Beta, les avions s'écraseraient.

Voilà la crise intellectuelle qui a donné naissance à la statistique moderne :
**Un indicateur de position (la moyenne) ne sert à rien s'il n'est pas accompagné d'un indicateur de dispersion (l'écart-type).**

---

### 2. Les indicateurs de position : Moyenne contre Médiane

Soit une série statistique quantitative discrète où la variable prend les valeurs ordonnées $x_1 < x_2 < \dots < x_p$, associées aux effectifs respectifs $n_1, n_2, \dots, n_p$.
L'effectif total est noté $N = \sum_{i=1}^p n_i$.

#### 2.1 La moyenne pondérée ($\bar{x}$)

La moyenne est le centre de gravité de la série : c'est la valeur que chacun recevrait si l'on mettait toutes les ressources en commun pour les redistribuer équitablement.

> **📐 Définition — Moyenne pondérée**
> La **moyenne pondérée** d'une série statistique, notée $\bar{x}$ (lire « **x barre** »), est donnée par :
>
> $$\boxed{\bar{x} = \frac{\sum_{i=1}^p n_i x_i}{N} = \sum_{i=1}^p f_i x_i}$$
>
> où $f_i = \frac{n_i}{N}$ désigne la fréquence de la valeur $x_i$.

**Propriété de linéarité :**
Si l'on multiplie toutes les valeurs par une constante $a$ et qu'on leur ajoute une constante $b$ (transformation affine $y_i = a x_i + b$), la nouvelle moyenne devient simplement :
$$\bar{y} = a \bar{x} + b.$$

#### 2.2 La médiane ($M_e$) : la justice du rang

La médiane ne s'intéresse pas à la masse totale, mais au **rang** dans la file d'attente.

> **📐 Définition — Médiane**
> La **médiane** d'une série statistique ordonnée par ordre croissant, notée $M_e$, est une valeur qui sépare la population en deux groupes de même effectif :
> - Au moins 50 % des individus ont une valeur inférieure ou égale à $M_e$ ;
> - Au moins 50 % des individus ont une valeur supérieure ou égale à $M_e$.

**Méthode pratique de calcul :**
1. Si l'effectif total $N$ est **impair** : $N = 2k + 1$.
   La médiane est la valeur de l'individu situé au rang $k+1$.
   *(Exemple : pour $N = 9$, $\frac{9+1}{2} = 5$ : la médiane est la 5ᵉ valeur).*
2. Si l'effectif total $N$ est **pair** : $N = 2k$.
   La médiane est généralement prise comme la demi-somme des valeurs situées aux rangs $k$ et $k+1$.
   *(Exemple : pour $N = 10$, on prend la moyenne entre la 5ᵉ et la 6ᵉ valeur).*

> **🔍 L'histoire vraie — Le bar de Bill Gates**
> Imagine un petit café de quartier où dix ouvriers et employés discutent au comptoir. Chacun gagne 2 000 € par mois.
> Le salaire moyen est de 2 000 €, et le salaire médian est de 2 000 €.
> Soudain, le milliardaire **Bill Gates** pousse la porte et s'assoit au comptoir. Ses revenus mensuels sont estimés à 10 millions d'euros.
> Recalculons instantanément les statistiques du bar :
> - Le **salaire moyen** explose : $\frac{10 \times 2\,000 + 10\,000\,000}{11} \approx \mathbf{910\,900\text{ € par mois}}$ !
>   Le statisticien imprudent conclurait : « Dans ce café, le client moyen est presque millionnaire ! » Ce qui est absurde.
> - Le **salaire médian**, lui, range les 11 clients par ordre croissant. Le 6ᵉ client de la file gagne toujours **2 000 €** !
> La médiane n'a pas bougé d'un centime : elle est **robuste** aux valeurs extrêmes (*outliers*), tandis que la moyenne est hypersensible.

---

### 3. Les quartiles et le diagramme en boîte à moustaches

Pour sonder plus finement la répartition, on découpe la série en **quatre quarts** de 25 % chacun.

#### 3.1 Définitions officielles des quartiles

> **📐 Définition — Quartiles**
> Dans une série ordonnée de taille $N$ :
> - Le **premier quartile**, noté $Q_1$, est la plus petite valeur de la série telle qu'au moins **25 %** des données soient inférieures ou égales à $Q_1$. Son rang dans la liste ordonnée est le premier entier supérieur ou égal à $\frac{N}{4}$ (noté $\lceil N/4 \rceil$).
> - Le **troisième quartile**, noté $Q_3$, est la plus petite valeur de la série telle qu'au moins **75 %** des données soient inférieures ou égales à $Q_3$. Son rang est le premier entier supérieur ou égal à $\frac{3N}{4}$ (noté $\lceil 3N/4 \rceil$).
> - Le deuxième quartile $Q_2$ n'est autre que la médiane $M_e$.

> **📐 Définition — Écart interquartile**
> La différence entre le troisième et le premier quartile s'appelle l'**écart interquartile** :
>
> $$\boxed{IQR = Q_3 - Q_1}$$
>
> Il mesure la largeur de l'intervalle dans lequel sont concentrés les **50 % centraux** de la population. Comme la médiane, cet indicateur est insensible aux valeurs aberrantes.

#### 3.2 La boîte à moustaches de John Tukey (1977)

Inventé par le grand statisticien américain **John Tukey**, le diagramme en boîte à moustaches (*boxplot*) résume une distribution en un coup d'œil :

```
                  Boîte centrale (50 % des données)
                ┌───────────────────┬──────────────┐
     ├──────────┤                   │              ├──────────┤
     │          │                   │              │          │
    Min         Q₁               Médiane          Q₃         Max
     |◄──25 %──►|◄──────25 %───────►|◄────25 %────►|◄──25 %──►|
```

- La **boîte rectangulaire** s'étend de $Q_1$ à $Q_3$. Sa longueur est l'écart interquartile.
- Le trait vertical au milieu de la boîte marque la **médiane**. Si la médiane n'est pas au centre de la boîte, la distribution est asymétrique.
- Les deux **moustaches** s'étirent de part et d'autre jusqu'au minimum et au maximum (ou jusqu'aux valeurs extrêmes non aberrantes).

---

### 4. Le mystère du carré : Variance et Écart-Type

Revenons à nos deux usines d'arbres de transmission. Comment mesurer mathématiquement la distance moyenne des pièces par rapport à la cible $\bar{x}$ ?

#### 4.1 La première fausse bonne idée : la moyenne des écarts

L'idée la plus naturelle serait de calculer l'écart $(x_i - \bar{x})$ pour chaque individu, puis d'en faire la moyenne.
Testons cela sur un exemple simple : trois notes $8, 12, 16$.
La moyenne vaut $\bar{x} = \frac{8 + 12 + 16}{3} = 12$.
Les écarts à la moyenne sont :
- Pour 8 : $8 - 12 = -4$
- Pour 12 : $12 - 12 = 0$
- Pour 16 : $16 - 12 = +4$

Faisons la somme de ces écarts : $(-4) + 0 + (+4) = \mathbf{0}$ !
Les écarts positifs ont été exactement annulés par les écarts négatifs !

> **📐 Théorème — La somme des écarts est toujours nulle**
> Pour toute série statistique :
>
> $$\sum_{i=1}^p n_i (x_i - \bar{x}) = 0$$

> **✍️ Démonstration**
> Développons la somme :
> $$\sum_{i=1}^p n_i (x_i - \bar{x}) = \sum_{i=1}^p n_i x_i - \sum_{i=1}^p n_i \bar{x} = \sum_{i=1}^p n_i x_i - \bar{x} \sum_{i=1}^p n_i = N \bar{x} - \bar{x} \times N = 0. \quad \blacksquare$$

La moyenne des écarts bruts est **toujours égale à zéro**, quelle que soit la dispersion de la série ! Elle ne sert strictement à rien.

#### 4.2 L'artifice du carré : la Variance

Pour empêcher les signes négatifs de neutraliser les signes positifs, les mathématiciens élèvent chaque écart **au carré** : $(-4)^2 = +16$ ! Un carré est toujours positif.

> **📐 Définition — Variance**
> La **variance** d'une série statistique, notée $V$, est la moyenne des carrés des écarts à la moyenne :
>
> $$\boxed{V = \frac{1}{N} \sum_{i=1}^p n_i (x_i - \bar{x})^2 = \sum_{i=1}^p f_i (x_i - \bar{x})^2}$$

#### 4.3 L'écart-type ($\sigma$) : retrouver l'unité physique

La variance résout le problème du signe, mais elle crée un monstre dimensionnel :
Si l'on mesure des longueurs en **mètres** (m), les écarts sont en mètres, mais leurs carrés sont en **mètres carrés** ($\text{m}^2$) ! La variance d'une série de tailles humaines s'exprime en $\text{m}^2$, ce qui n'a aucun sens physique.
Pour revenir à l'unité de départ (des mètres, des euros, des millimètres), on applique la **racine carrée** :

> **📐 Définition — Écart-type**
> L'**écart-type**, noté $\sigma$ (lettre grecque minuscule « **sigma** »), est la racine carrée de la variance :
>
> $$\boxed{\sigma = \sqrt{V} = \sqrt{\frac{1}{N} \sum_{i=1}^p n_i (x_i - \bar{x})^2}}$$

**Sens intuitif :**
L'écart-type représente l'**écart type** (au sens d'écart modèle, d'écart caractéristique) que fait en moyenne un individu par rapport à la moyenne du groupe.
- Dans l'atelier Alpha : $\bar{x} = 50{,}00$ mm et $\sigma = \mathbf{0{,}01\text{ mm}}$ (dispersion infime).
- Dans l'atelier Beta : $\bar{x} = 50{,}00$ mm et $\sigma = \mathbf{2{,}45\text{ mm}}$ (dispersion colossale).
Grâce à $\sigma$, l'ingénieur démasque immédiatement l'atelier défaillant !

---

### 5. La formule de König-Huygens : le raccourci magique

Calculer chaque terme $(x_i - \bar{x})^2$ à la main est un calvaire dès que la moyenne comporte des virgules. Heureusement, deux savants du XVIIᵉ siècle, le mathématicien allemand **Samuel König** et le physicien hollandais **Christiaan Huygens**, ont démontré une formule alternative éblouissante :

> **📐 Théorème — Formule de König-Huygens**
> La variance est égale à **la moyenne des carrés moins le carré de la moyenne** :
>
> $$\boxed{V = \overline{x^2} - (\bar{x})^2}$$
>
> où $\overline{x^2} = \frac{1}{N} \sum_{i=1}^p n_i x_i^2$ désigne la moyenne des carrés des valeurs.

> **✍️ Démonstration**
> Développons le carré dans l'expression de la variance :
> $$V = \frac{1}{N} \sum_{i=1}^p n_i \big(x_i^2 - 2x_i\bar{x} + \bar{x}^2\big).$$
> Distribuons la somme :
> $$V = \frac{1}{N}\sum n_i x_i^2 - \frac{2\bar{x}}{N}\sum n_i x_i + \frac{\bar{x}^2}{N}\sum n_i.$$
> Or $\frac{1}{N}\sum n_i x_i^2 = \overline{x^2}$, $\frac{1}{N}\sum n_i x_i = \bar{x}$, et $\sum n_i = N$.
> L'expression devient :
> $$V = \overline{x^2} - 2\bar{x}(\bar{x}) + \frac{\bar{x}^2}{N}(N) = \overline{x^2} - 2(\bar{x})^2 + (\bar{x})^2 = \overline{x^2} - (\bar{x})^2. \quad \blacksquare$$

> **💡 Propriété de transformation affine —**
> Si l'on pose $y_i = a x_i + b$, alors :
> $$V(aX + b) = a^2 V(X) \quad \text{et} \quad \boxed{\sigma(aX + b) = |a| \cdot \sigma(X)}$$
> Remarque : ajouter une constante $b$ (par exemple donner 2 points de bonus à toute la classe) translate toutes les notes sans modifier leur dispersion : l'écart-type reste inchangé !

---

### 6. Échantillonnage, fluctuation et simulation en Python

Comment un institut de sondage peut-il estimer le résultat d'une élection présidentielle avec seulement 1 000 personnes interrogées par téléphone ?
C'est le miracle mathématique de la **fluctuation d'échantillonnage**.

#### 6.1 Le principe de la fluctuation

Supposons qu'une proportion réelle $p$ de citoyens dans le pays entier soutienne une certaine mesure.
Si l'on tire au sort un échantillon de taille $n$, la fréquence observée $f$ dans cet échantillon ne sera presque jamais exactement égale à $p$ : elle va osciller autour de $p$.
Cependant, pour un échantillon suffisamment grand ($n \ge 30$, $np \ge 5$, $n(1-p) \ge 5$), les mathématiques démontrent que dans **au moins 95 % des cas**, la fréquence observée $f$ tombe dans une fourchette très précise :

> **📐 Définition — Intervalle de fluctuation à 95 %**
> - Au niveau Seconde :
>   $$I = \left[ p - \frac{1}{\sqrt{n}} \ ; \ p + \frac{1}{\sqrt{n}} \right]$$
> - Formule asymptotique précise de Première Spécialité (issue de la loi normale) :
>   $$\boxed{I_{0{,}95} = \left[ p - 1{,}96 \sqrt{\frac{p(1-p)}{n}} \ ; \ p + 1{,}96 \sqrt{\frac{p(1-p)}{n}} \right]}$$

#### 6.2 Simulation d'échantillonnage en Python

Pour vérifier expérimentalement ce phénomène, simulons 1 000 sondages de taille $n = 100$ dans une population où la vraie proportion vaut $p = 0{,}40$ (40 %) :

```python
import random


def simuler_echantillon(n, p):
  """Simule le tirage d'un échantillon de taille n et renvoie la fréquence f."""
  succes = sum(1 for _ in range(n) if random.random() < p)
  return succes / n


def etude_fluctuation(nb_echantillons=1000, n=100, p=0.40):
  borne_inf = p - 1.96 * (p * (1 - p) / n) ** 0.5
  borne_sup = p + 1.96 * (p * (1 - p) / n) ** 0.5

  dans_intervalle = 0
  for _ in range(nb_echantillons):
    f = simuler_echantillon(n, p)
    if borne_inf <= f <= borne_sup:
      dans_intervalle += 1

  pourcentage = (dans_intervalle / nb_echantillons) * 100
  print(f"Intervalle théorique à 95 % : [{borne_inf:.4f} ; {borne_sup:.4f}]")
  print(
      f"Proportion d'échantillons tombés dans l'intervalle : {pourcentage:.1f} %"
  )


etude_fluctuation()
```

Résultat d'une exécution :
```
Intervalle théorique à 95 % : [0.3040 ; 0.4960]
Proportion d'échantillons tombés dans l'intervalle : 95.3 %
```
Exactement ce que la théorie prédisait : 95 % des échantillons tombent dans la cible !

---

### Exemples résolus pas à pas

> **✅ Exemple résolu 1 — Calcul pas à pas de la moyenne et de l'écart-type**
> Les notes obtenues par un groupe de 20 élèves à un devoir sont réparties ainsi :
>
> | Note $x_i$ | 6 | 8 | 10 | 12 | 15 | 18 |
> |---|---|---|---|---|---|---|
> | Effectif $n_i$ | 2 | 4 | 6 | 5 | 2 | 1 |
>
> Calculer la moyenne $\bar{x}$, la variance $V$ et l'écart-type $\sigma$.
>
> **Solution détaillée :**
> Effectif total : $N = 2 + 4 + 6 + 5 + 2 + 1 = 20$.
> 1. Moyenne :
>    $$\sum n_i x_i = (2 \times 6) + (4 \times 8) + (6 \times 10) + (5 \times 12) + (2 \times 15) + (1 \times 18)$$
>    $$= 12 + 32 + 60 + 60 + 30 + 18 = 212.$$
>    $$\bar{x} = \frac{212}{20} = 10{,}6.$$
>
> 2. Formule de König-Huygens pour la variance :
>    Calculons $\sum n_i x_i^2$ :
>    $$2(36) + 4(64) + 6(100) + 5(144) + 2(225) + 1(324)$$
>    $$= 72 + 256 + 600 + 720 + 450 + 324 = 2422.$$
>    $$\overline{x^2} = \frac{2422}{20} = 121{,}1.$$
>    $$V = \overline{x^2} - (\bar{x})^2 = 121{,}1 - (10{,}6)^2 = 121{,}1 - 112{,}36 = 8{,}74.$$
>
> 3. Écart-type :
>    $$\sigma = \sqrt{V} = \sqrt{8{,}74} \approx 2{,}96.$$
>    La moyenne de la classe est de $10{,}6$ avec un écart-type de près de $3$ points.

> **✅ Exemple résolu 2 — Détermination de la médiane et des quartiles**
> Déterminer $M_e$, $Q_1$, $Q_3$ et l'écart interquartile pour la série de notes de l'exemple 1.
>
> **Solution détaillée :**
> Dressons le tableau des effectifs cumulés croissants (ECC) :
>
> | Note $x_i$ | 6 | 8 | 10 | 12 | 15 | 18 |
> |---|---|---|---|---|---|---|
> | Effectif $n_i$ | 2 | 4 | 6 | 5 | 2 | 1 |
> | ECC | 2 | 6 | 12 | 17 | 19 | 20 |
>
> - **Médiane :** $N = 20$ (pair). $\frac{N}{2} = 10$.
>   La médiane est la moyenne entre la 10ᵉ et la 11ᵉ valeur.
>   D'après les ECC, la 10ᵉ valeur est un 10, et la 11ᵉ est aussi un 10.
>   Donc $\boxed{M_e = 10}$.
> - **Premier quartile $Q_1$ :** $\frac{N}{4} = \frac{20}{4} = 5$.
>   $Q_1$ est la 5ᵉ valeur de la série ordonnée.
>   D'après les ECC, les valeurs de rang 3 à 6 sont des 8.
>   Donc $\boxed{Q_1 = 8}$.
> - **Troisième quartile $Q_3$ :** $\frac{3N}{4} = \frac{60}{4} = 15$.
>   $Q_3$ est la 15ᵉ valeur. D'après les ECC, les valeurs de rang 13 à 17 sont des 12.
>   Donc $\boxed{Q_3 = 12}$.
> - **Écart interquartile :** $IQR = Q_3 - Q_1 = 12 - 8 = 4$.
>   La moitié centrale de la classe a des notes comprises entre 8 et 12.

> **✅ Exemple résolu 3 — Comparaison de deux séries par boîte à moustaches**
> Deux sportifs $A$ et $B$ s'entraînent au tir à l'arc. Leurs scores sur 50 tirs donnent les résumés suivants :
> - Tireur $A$ : $\text{Min} = 5$, $Q_1 = 8$, $M_e = 9$, $Q_3 = 10$, $\text{Max} = 10$.
> - Tireur $B$ : $\text{Min} = 2$, $Q_1 = 6$, $M_e = 9$, $Q_3 = 9$, $\text{Max} = 10$.
> Comparer leurs performances.
>
> **Solution détaillée :**
> - Les deux tireurs ont la même médiane ($M_e = 9$) : au moins la moitié de leurs flèches sont plantées dans le 9 ou le 10.
> - Regardons l'éparpillement :
>   - Pour $A$ : $IQR = 10 - 8 = 2$, et l'étendue totale est de $10 - 5 = 5$. 75 % de ses tirs valent 8 ou plus.
>   - Pour $B$ : $IQR = 9 - 6 = 3$, et l'étendue vaut $10 - 2 = 8$. Un quart de ses tirs est inférieur ou égal à 6, et il a même fait un tir désastreux à 2.
> - **Conclusion :** Le tireur $A$ est bien plus **régulier et fiable** que le tireur $B$, même si leurs performances médianes semblent identiques.

> **✅ Exemple résolu 4 — Effet d'une transformation sur moyenne et écart-type**
> Un professeur fait un contrôle difficile : la moyenne est $\bar{x} = 8$ et l'écart-type est $\sigma = 3$.
> Il décide d'harmoniser les notes en appliquant la formule suivante à chaque note $x$ :
> $$y = 1{,}2 x + 2.$$
> Déterminer la nouvelle moyenne $\bar{y}$ et le nouvel écart-type $\sigma_y$.
>
> **Solution détaillée :**
> - Par linéarité de la moyenne :
>   $$\bar{y} = 1{,}2 \bar{x} + 2 = 1{,}2(8) + 2 = 9{,}6 + 2 = 11{,}6.$$
> - Par propriété de l'écart-type : $\sigma(aX + b) = |a| \sigma(X)$.
>   $$\sigma_y = |1{,}2| \times \sigma = 1{,}2 \times 3 = 3{,}6.$$
> La moyenne monte de $3{,}6$ points, mais l'écart-type augmente aussi : les écarts entre élèves se sont légèrement creusés !

> **✅ Exemple résolu 5 — Prise de décision sur un échantillon**
> Une usine de fabrication de biscuits affirme que seulement 2 % de sa production présente des défauts de cuisson ($p = 0{,}02$).
> Une association de consommateurs achète un lot de $n = 500$ biscuits et découvre 18 biscuits brûlés.
> Peut-on rejeter l'affirmation du fabricant au seuil de confiance de 95 % ?
>
> **Solution détaillée :**
> 1. Conditions d'application :
>    $n = 500 \ge 30$, $np = 500 \times 0{,}02 = 10 \ge 5$, $n(1-p) = 500 \times 0{,}98 = 490 \ge 5$.
>    Les conditions sont vérifiées.
> 2. Intervalle de fluctuation asymptotique à 95 % :
>    $$I_{0{,}95} = \left[ 0{,}02 - 1{,}96 \sqrt{\frac{0{,}02 \times 0{,}98}{500}} \ ; \ 0{,}02 + 1{,}96 \sqrt{\frac{0{,}02 \times 0{,}98}{500}} \right].$$
>    Calculons l'écart-type de la proportion :
>    $$\sqrt{\frac{0{,}0196}{500}} = \sqrt{0{,}0000392} \approx 0{,}00626.$$
>    La marge d'erreur vaut $1{,}96 \times 0{,}00626 \approx 0{,}0123$.
>    $$I_{0{,}95} = [0{,}02 - 0{,}0123 \ ; \ 0{,}02 + 0{,}0123] = [0{,}0077 \ ; \ 0{,}0323].$$
>    En pourcentage : entre $0{,}77\text{ \%}$ et $3{,}23\text{ \%}$.
> 3. Fréquence observée dans l'échantillon :
>    $$f = \frac{18}{500} = 0{,}036 = 3{,}6\text{ \%}.$$
> 4. Décision :
>    La fréquence observée $f = 0{,}036 \notin I_{0{,}95}$ (elle dépasse la borne supérieure de $0{,}0323$).
>    **Conclusion :** Au seuil de 95 %, l'affirmation du fabricant doit être **rejetée**. Il y a anormalement trop de biscuits défectueux.

> **✅ Exemple résolu 6 — Détection de données aberrantes**
> Tukey a défini un critère rigoureux pour repérer une valeur aberrante (*outlier*) : une valeur est aberrante si elle est strictement en dehors de l'intervalle :
> $$[Q_1 - 1{,}5 \times IQR \ ; \ Q_3 + 1{,}5 \times IQR].$$
> Dans une entreprise, on a $Q_1 = 1800\text{ €}$ et $Q_3 = 2600\text{ €}$.
> Un salaire de 4 000 € est-il considéré comme aberrant ?
>
> **Solution détaillée :**
> - Écart interquartile : $IQR = 2600 - 1800 = 800\text{ €}$.
> - Seuil maximal acceptable :
>   $Q_3 + 1{,}5 \times IQR = 2600 + 1{,}5(800) = 2600 + 1200 = 3800\text{ €}$.
> - Comme $4000\text{ €} > 3800\text{ €}$, ce salaire dépasse la limite : il s'agit bel et bien d'une **valeur aberrante** au sens statistique.

---

### Ce qu'il faut retenir

1. **Indicateurs de position :**
   - Moyenne : $\bar{x} = \frac{1}{N} \sum n_i x_i = \sum f_i x_i$. Sensible aux valeurs extrêmes.
   - Médiane $M_e$ : valeur centrale (50 % au-dessus, 50 % en dessous). Robuste.
   - Quartiles : $Q_1$ (au moins 25 %) et $Q_3$ (au moins 75 %).

2. **Indicateurs de dispersion :**
   - Écart interquartile : $IQR = Q_3 - Q_1$.
   - Variance : $V = \frac{1}{N} \sum n_i (x_i - \bar{x})^2$.
   - Formule de König-Huygens : $\boxed{V = \overline{x^2} - (\bar{x})^2}$.
   - Écart-type : $\boxed{\sigma = \sqrt{V}}$ (exprimé dans la même unité que les données).

3. **Transformation affine $y = ax + b$ :**
   - $\bar{y} = a\bar{x} + b$
   - $V(aX + b) = a^2 V(X)$
   - $\sigma(aX + b) = |a|\sigma(X)$

4. **Échantillonnage et fluctuation (à 95 %) :**
   - $I_{0{,}95} = \left[ p - 1{,}96 \sqrt{\frac{p(1-p)}{n}} \ ; \ p + 1{,}96 \sqrt{\frac{p(1-p)}{n}} \right]$ (pour $n \ge 30$, $np \ge 5$, $n(1-p) \ge 5$).
   - Si la fréquence observée $f \notin I_{0{,}95}$, on rejette l'hypothèse de proportion $p$.

---

### Exercices

#### Niveau ★ (Calculs directs d'indicateurs)

1. Calculer la moyenne et la médiane de la série : $4, 7, 9, 11, 14$.
2. Calculer la moyenne et la médiane de la série : $3, 5, 8, 12, 16, 20$.
3. Une série de 5 valeurs a pour moyenne 10. Quatre des valeurs sont $6, 8, 11, 13$. Trouver la cinquième valeur.
4. Calculer la variance et l'écart-type de la série $2, 4, 6, 8, 10$.
5. On sait que $\overline{x^2} = 53$ et $\bar{x} = 7$. Calculer la variance $V$ et l'écart-type $\sigma$.
6. Si les salaires d'une entreprise ont un écart-type $\sigma = 250\text{ €}$, quel sera le nouvel écart-type si chaque salarié reçoit une augmentation forfaitaire de 100 € ?
7. Même question si chaque salaire est augmenté de 5 % (multiplié par 1,05).
8. Déterminer $Q_1$, $M_e$ et $Q_3$ pour la série ordonnée de 12 valeurs :
   $1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 18, 20$.

#### Niveau ★★ (Analyses comparatives et propriétés)

9. Soit la série statistique suivante :
   | Valeur $x_i$ | 10 | 20 | 30 | 40 |
   |---|---|---|---|---|
   | Effectif $n_i$ | 3 | 5 | 8 | 4 |
   a) Calculer $\bar{x}$.
   b) Utiliser la formule de König-Huygens pour trouver $V$ et $\sigma$.
10. Démontrer que pour deux nombres réels $a$ et $b$, la variance de la série $\{a; b\}$ est égale à $\left(\frac{a - b}{2}\right)^2$.
11. Un contrôle est passé par deux groupes :
    - Groupe 1 (15 élèves) : moyenne $\bar{x}_1 = 12$.
    - Groupe 2 (25 élèves) : moyenne $\bar{x}_2 = 10$.
    Calculer la moyenne globale de l'ensemble des 40 élèves.
12. Dans une classe, les notes ont pour moyenne 11 et pour écart-type 2,5. Le professeur décide de normaliser les notes pour que la moyenne passe à 12 et l'écart-type à 3.
    Quelle transformation affine $y = ax + b$ doit-il appliquer ?
13. Un échantillon de 400 électeurs révèle que 228 comptent voter pour le candidat $C$.
    Calculer l'intervalle de fluctuation au niveau 95 % sous l'hypothèse que la population est partagée à égalité ($p = 0{,}50$). Peut-on affirmer que le candidat $C$ a une avance significative ?
14. Les températures maximales enregistrées en juillet dans deux stations météo donnent :
    - Station A : $\bar{x} = 28^\circ\text{C}$, $\sigma = 1{,}5^\circ\text{C}$.
    - Station B : $\bar{x} = 28^\circ\text{C}$, $\sigma = 6{,}2^\circ\text{C}$.
    Commenter le climat des deux stations.
15. Écrire une fonction Python `statistiques(liste)` qui prend une liste de nombres et renvoie son effectif, sa moyenne, sa variance et son écart-type sans utiliser de bibliothèque externe.

#### Niveau ★★★ (Défis théoriques et modélisation)

16. **Variance d'une réunion de deux séries :**
    Soient deux séries statistiques de tailles $N_1$ et $N_2$, de moyennes $\bar{x}_1$ et $\bar{x}_2$, et de variances $V_1$ et $V_2$.
    Démontrer que la variance $V$ de la série réunie de taille $N = N_1 + N_2$ vérifie :
    $$V = \frac{N_1 V_1 + N_2 V_2}{N} + \frac{N_1 N_2}{N^2}(\bar{x}_1 - \bar{x}_2)^2.$$
    Interpréter physiquement les deux termes (dispersion intra-groupe et dispersion inter-groupe).
17. **Inégalité de Bienaymé-Tchebychev (découverte) :**
    Soit une série statistique de moyenne $\bar{x}$ et d'écart-type $\sigma$.
    Montrer que la proportion d'individus situés à une distance supérieure ou égale à $2\sigma$ de la moyenne ne peut jamais dépasser $\frac{1}{4} = 25\text{ \%}$, quelle que soit la forme de la série !
18. **L'élection présidentielle et la marge d'erreur :**
    Un sondage interroge $n$ personnes pour départager deux finalistes d'une élection au coude-à-coude ($p \approx 0{,}50$).
    Combien de personnes au minimum faut-il interroger pour que la marge d'erreur à 95 % ($1{,}96 \sqrt{\frac{p(1-p)}{n}}$) soit strictement inférieure à 1 % (soit $0{,}01$) ?
19. **La moyenne des rangs :**
    On considère la série des $n$ premiers entiers naturels non nuls : $1, 2, 3, \dots, n$.
    a) Calculer la moyenne $\bar{x}$ en fonction de $n$.
    b) En utilisant $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$, démontrer que la variance vaut $V = \frac{n^2 - 1}{12}$.
20. **Algorithme de détection de valeurs aberrantes en Python :**
    Écrire un programme Python qui prend une liste de données brutes, calcule $Q_1$, $Q_3$, l'intervalle de Tukey et extrait la liste de toutes les valeurs aberrantes.

---

### Solutions

**1.** Moyenne : $\bar{x} = \frac{4 + 7 + 9 + 11 + 14}{5} = \frac{45}{5} = 9$.
Médiane : 3ᵉ valeur sur 5, donc $M_e = 9$.

**2.** Moyenne : $\bar{x} = \frac{3 + 5 + 8 + 12 + 16 + 20}{6} = \frac{64}{6} \approx 10{,}67$.
Médiane : demi-somme des 3ᵉ et 4ᵉ valeurs : $M_e = \frac{8 + 12}{2} = 10$.

**3.** Somme totale = $5 \times 10 = 50$.
Somme des quatre valeurs = $6 + 8 + 11 + 13 = 38$.
La 5ᵉ valeur est $50 - 38 = 12$.

**4.** $\bar{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = 6$.
Écarts à la moyenne : $-4, -2, 0, 2, 4$.
Carrés des écarts : $16, 4, 0, 4, 16$.
Variance : $V = \frac{16 + 4 + 0 + 4 + 16}{5} = \frac{40}{5} = 8$.
Écart-type : $\sigma = \sqrt{8} = 2\sqrt{2} \approx 2{,}83$.

**5.** $V = \overline{x^2} - (\bar{x})^2 = 53 - 7^2 = 53 - 49 = 4$.
$\sigma = \sqrt{4} = 2$.

**6.** L'écart-type est insensible aux additions : le nouvel écart-type est toujours $\sigma = 250\text{ €}$.

**7.** $y = 1{,}05 x \implies \sigma_y = 1{,}05 \times \sigma = 1{,}05 \times 250 = 262{,}50\text{ €}$.

**8.** $N = 12$.
- $Q_1$ : rang $\frac{12}{4} = 3 \implies$ 3ᵉ valeur, soit $Q_1 = 4$.
- Médiane : demi-somme des 6ᵉ et 7ᵉ valeurs $\implies M_e = \frac{9 + 10}{2} = 9{,}5$.
- $Q_3$ : rang $\frac{3 \times 12}{4} = 9 \implies$ 9ᵉ valeur, soit $Q_3 = 13$.

**9.**
a) $N = 3 + 5 + 8 + 4 = 20$.
$\sum n_i x_i = 3(10) + 5(20) + 8(30) + 4(40) = 30 + 100 + 240 + 160 = 530$.
$\bar{x} = \frac{530}{20} = 26{,}5$.
b) $\sum n_i x_i^2 = 3(100) + 5(400) + 8(900) + 4(1600) = 300 + 2000 + 7200 + 6400 = 15900$.
$\overline{x^2} = \frac{15900}{20} = 795$.
$V = \overline{x^2} - (\bar{x})^2 = 795 - (26{,}5)^2 = 795 - 702{,}25 = 92{,}75$.
$\sigma = \sqrt{92{,}75} \approx 9{,}63$.

**10.** Moyenne : $\bar{x} = \frac{a+b}{2}$.
Les écarts sont $a - \frac{a+b}{2} = \frac{a-b}{2}$, et $b - \frac{a+b}{2} = \frac{b-a}{2} = -\frac{a-b}{2}$.
La moyenne des carrés des écarts vaut :
$V = \frac{1}{2}\left[\left(\frac{a-b}{2}\right)^2 + \left(-\frac{a-b}{2}\right)^2\right] = \left(\frac{a-b}{2}\right)^2$.

**11.** Moyenne pondérée globale :
$\bar{x} = \frac{N_1 \bar{x}_1 + N_2 \bar{x}_2}{N_1 + N_2} = \frac{15 \times 12 + 25 \times 10}{40} = \frac{180 + 250}{40} = \frac{430}{40} = 10{,}75$.

**12.** On veut $\sigma_y = |a|\sigma \iff 3 = a \times 2{,}5 \iff a = \frac{3}{2{,}5} = 1{,}2$.
On veut ensuite $\bar{y} = a\bar{x} + b \iff 12 = 1{,}2(11) + b \iff 12 = 13{,}2 + b \iff b = -1{,}2$.
La formule est : $y = 1{,}2 x - 1{,}2$.

**13.** Fréquence observée : $f = \frac{228}{400} = 0{,}57$.
Sous l'hypothèse $p = 0{,}50$, l'intervalle à 95 % est :
$I = \left[ 0{,}50 - 1{,}96\sqrt{\frac{0{,}25}{400}} \ ; \ 0{,}50 + 1{,}96\sqrt{\frac{0{,}25}{400}} \right] = [0{,}50 - 1{,}96 \times 0{,}025 \ ; \ 0{,}50 + 1{,}96 \times 0{,}025] = [0{,}451 \ ; \ 0{,}549]$.
Comme $f = 0{,}57 > 0{,}549$, la fréquence sort de l'intervalle : le candidat $C$ a une avance statistiquement significative par rapport au 50/50.

**14.** Les deux stations ont la même température moyenne ($28^\circ$C).
Mais la station A a un écart-type très faible ($1{,}5^\circ$C) : c'est un climat très régulier et tempéré (sans doute une île océanique).
La station B a un écart-type important ($6{,}2^\circ$C) : les températures y subissent de violentes variations entre jours étouffants et vagues d'orage (climat continental).

**15.**
```python
def statistiques(liste):
  N = len(liste)
  moyenne = sum(liste) / N
  variance = sum((x - moyenne) ** 2 for x in liste) / N
  ecart_type = variance**0.5
  return {'effectif': N, 'moyenne': moyenne, 'ecart_type': ecart_type}
```

**16.** Notons $S_1 = \sum_{x \in G_1} x^2$ et $S_2 = \sum_{x \in G_2} x^2$.
Par König-Huygens dans chaque groupe : $S_1 = N_1 (V_1 + \bar{x}_1^2)$ et $S_2 = N_2 (V_2 + \bar{x}_2^2)$.
Dans le groupe réuni : $\bar{x} = \frac{N_1 \bar{x}_1 + N_2 \bar{x}_2}{N}$, et $V = \frac{S_1 + S_2}{N} - \bar{x}^2$.
En développant et simplifiant, les termes croisés font apparaître :
$V = \frac{N_1 V_1 + N_2 V_2}{N} + \frac{N_1 N_2}{N^2}(\bar{x}_1 - \bar{x}_2)^2$.
- Le premier terme représente la **dispersion intra-groupe** (la moyenne des variances de chaque groupe).
- Le second terme représente la **dispersion inter-groupe** (l'écart entre les moyennes des deux groupes).

**17.** Soit $E$ l'ensemble des individus vérifiant $|x_i - \bar{x}| \ge 2\sigma$, et $N_E$ leur nombre.
Pour chaque individu de $E$, $(x_i - \bar{x})^2 \ge 4\sigma^2$.
La somme de tous les carrés d'écarts vérifie :
$N V = \sum_{i=1}^N (x_i - \bar{x})^2 \ge \sum_{i \in E} (x_i - \bar{x})^2 \ge N_E \times 4\sigma^2$.
Comme $V = \sigma^2$, on a $N \sigma^2 \ge N_E \times 4\sigma^2$.
En divisant par $4N \sigma^2$, il vient : $\frac{N_E}{N} \le \frac{1}{4} = 25\text{ \%}$.

**18.** Marge d'erreur : $1{,}96 \sqrt{\frac{0{,}5 \times 0{,}5}{n}} = 1{,}96 \times \frac{0{,}5}{\sqrt{n}} = \frac{0{,}98}{\sqrt{n}}$.
On veut $\frac{0{,}98}{\sqrt{n}} < 0{,}01 \iff \sqrt{n} > \frac{0{,}98}{0{,}01} = 98 \iff n > 98^2 = 9\,604$.
Il faut interroger au moins **9 605 personnes** pour garantir une marge d'erreur inférieure à 1 %.

**19.**
a) $\bar{x} = \frac{1}{n} \sum_{k=1}^n k = \frac{1}{n} \times \frac{n(n+1)}{2} = \frac{n+1}{2}$.
b) $\overline{x^2} = \frac{1}{n} \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6}$.
Par König-Huygens :
$V = \overline{x^2} - (\bar{x})^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4} = (n+1)\left[ \frac{2(2n+1) - 3(n+1)}{12} \right] = (n+1)\frac{4n+2-3n-3}{12} = \frac{(n+1)(n-1)}{12} = \frac{n^2 - 1}{12}$.

**20.**
```python
import math


def detecter_outliers(donnees):
  s = sorted(donnees)
  N = len(s)
  q1 = s[math.ceil(N / 4) - 1]
  q3 = s[math.ceil(3 * N / 4) - 1]
  iqr = q3 - q1
  seuil_bas = q1 - 1.5 * iqr
  seuil_haut = q3 + 1.5 * iqr
  outliers = [x for x in donnees if x < seuil_bas or x > seuil_haut]
  return {'Q1': q1, 'Q3': q3, 'IQR': iqr, 'outliers': outliers}
```

---

### La question qui ouvre la suite

Nous savons désormais décrire et résumer des données passées.
Mais comment passer de la constatation des faits passés à **la prédiction du futur** ?
Comment calculer la probabilité qu'un patient soit réellement malade lorsqu'un test médical à 99 % de fiabilité s'allume en rouge ? Pourquoi nos intuitions sur le hasard nous trompent-elles presque toujours ?
C'est le grand carrefour des **probabilités conditionnelles** et de la **formule de Bayes**, au chapitre suivant.
