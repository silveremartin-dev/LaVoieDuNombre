# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 54 : Les Mille Lancers de la Pièce

> *« Si vous lancez une pièce dix fois, le hasard peut vous faire la farce de vous donner dix Piles d'affilée. Mais lancez-la un million de fois : le désordre s'annule, les caprices s'éteignent, et de l'anarchie des lancers émerge une régularité de cristal. La loi des grands nombres n'est pas une contrainte magique imposée à la pièce : c'est la victoire mathématique inévitable de la multitude sur le singulier. »*

---

### Ce que tu vas découvrir

- Comment modéliser la répétition d'expériences aléatoires identiques et indépendantes par le **schéma de Bernoulli**.
- La construction rigoureuse de la **loi binomiale $\mathcal{B}(n, p)$** et la justification combinatoire de la formule $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
- Les démonstrations exigibles au baccalauréat de l'**espérance** $E(X) = np$ et de la **variance** $V(X) = np(1-p)$ par la décomposition en somme de variables de Bernoulli indépendantes.
- L'**inégalité de Markov** et l'**inégalité de Bienaymé-Tchebychev**, qui bornent la dispersion de n'importe quelle variable aléatoire.
- L'**inégalité de concentration** et la démonstration de la **loi faible des grands nombres** : pourquoi la fréquence observée converge infailliblement vers la probabilité théorique.
- Un script **Python** complet de simulation de 10 000 lancers pour observer visuellement le resserrement autour de la moyenne.

---

### 1. Le problème : le casino, le sondeur et l'assurance

#### 1.1 La pièce du joueur
Imagine que tu joues à Pile ou Face avec un inconnu dans un train. Tu paries 1 euro sur Face.
Au premier lancer : Pile. Tu perds 1 €.
Au deuxième lancer : Pile. Tu perds 2 €.
Au troisième : Pile. Tu commences à douter.
Au dixième lancer consécutif, la pièce affiche encore Pile !
L'inconnu te sourit et dit : *« C'est le hasard, mon ami. Au prochain lancer, Face a même plus de chances de sortir pour compenser ! »*
Deux erreurs fatales se cachent dans cette phrase :
1. **L'illusion du joueur (Gambler's fallacy) :** La pièce n'a aucune mémoire de ses lancers antérieurs. À chaque lancer, la probabilité d'avoir Face reste strictement égale à $\frac{1}{2}$.
2. **Le doute légitime :** Obtenir 10 Piles consécutifs avec une pièce équilibrée a une probabilité de $\left(\frac{1}{2}\right)^{10} = \frac{1}{1024} \approx 0{,}00098$, soit moins d'une chance sur mille. La pièce est très probablement pipée !

#### 1.2 Le sondeur et l'assureur
Comment un institut de sondage peut-il connaître l'opinion de 45 millions d'électeurs en interrogeant seulement 1 000 personnes avec une marge d'erreur inférieure à 3 % ?
Comment une compagnie d'assurance peut-elle garantir le remboursement des dégâts causés par les incendies alors qu'elle ignore totalement quelle maison va brûler cette année ?
Leur secret est identique : **individuellement, le résultat d'un tirage est imprévisible ; collectivement, la moyenne d'un grand nombre de tirages devient d'une certitude quasi absolue.**

Pour passer du caprice de l'essai unique à la certitude de la masse, les mathématiciens ont forgé deux outils monumentaux : la **loi binomiale** et le **théorème des grands nombres**.

---

### 2. De l'épreuve de Bernoulli à la loi binomiale

#### 2.1 L'épreuve de Bernoulli
Le physicien et mathématicien suisse **Jacques (Jacob) Bernoulli** (1655–1705) s'intéresse à l'expérience aléatoire la plus élémentaire qui soit : celle qui n'a que **deux issues possibles**.

> **📐 Définition — Épreuve de Bernoulli**
> Une **épreuve de Bernoulli** de paramètre $p \in ]0; 1[$ est une expérience aléatoire ne comportant que deux issues contraires :
> - L'une appelée conventionnellement **Succès** (notée $S$), avec la probabilité $P(S) = p$.
> - L'autre appelée conventionnellement **Échec** (notée $E$ ou $\overline{S}$), avec la probabilité $P(E) = 1 - p$ (souvent notée $q$).
>
> La variable aléatoire associée $X$ qui vaut $1$ en cas de succès et $0$ en cas d'échec suit une **loi de Bernoulli** de paramètre $p$, notée $X \sim \mathcal{B}(p)$.

*Tableau de la loi de Bernoulli :*
| $k$ | 0 | 1 |
|---|---|---|
| $P(X = k)$ | $1 - p$ | $p$ |

Calculons immédiatement ses caractéristiques :
- **Espérance :**
  $$E(X) = 0 \times P(X=0) + 1 \times P(X=1) = 0 \times (1-p) + 1 \times p = p$$
- **Variance :**
  D'après la formule de Koenig-Huygens ($V(X) = E(X^2) - (E(X))^2$) :
  Comme $X$ ne prend que les valeurs 0 et 1, on a $X^2 = X$, donc $E(X^2) = E(X) = p$.
  $$V(X) = p - p^2 = p(1 - p)$$
- **Écart-type :**
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{p(1-p)}$$

#### 2.2 Le schéma de Bernoulli

> **📐 Définition — Schéma de Bernoulli**
> On appelle **schéma de Bernoulli** de paramètres $n$ et $p$ la répétition de $n$ épreuves de Bernoulli identiques et **indépendantes**, de même paramètre de succès $p$.

*Que signifie l'indépendance ?*
Le résultat d'une épreuve n'influence en aucun cas les probabilités des épreuves suivantes. Par exemple, des lancers successifs d'une pièce, ou des tirages successifs de boules dans une urne **avec remise**. Si les tirages sont effectués *sans remise*, les épreuves ne sont pas indépendantes : ce n'est pas un schéma de Bernoulli !

#### 2.3 L'arbre pondéré et la loi binomiale
Représentons un schéma de Bernoulli à $n = 3$ essais sur un arbre pondéré :

![Arbre pondéré du schéma de Bernoulli à 3 épreuves indépendantes](figures/vol_6/fig_54_arbre_bernoulli.svg)

Considérons la variable aléatoire $X$ qui compte le **nombre total de succès** obtenus au bout des $n$ épreuves.
- $X$ peut prendre n'importe quelle valeur entière comprise entre $0$ et $n$.
- Combien vaut la probabilité d'obtenir exactement 2 succès pour $n = 3$ ?
  Regardons les chemins menant à 2 succès :
  - $S-S-E$ : probabilité $p \times p \times (1-p) = p^2(1-p)$
  - $S-E-S$ : probabilité $p \times (1-p) \times p = p^2(1-p)$
  - $E-S-S$ : probabilité $(1-p) \times p \times p = p^2(1-p)$
  Chaque chemin comportant 2 succès et 1 échec a exactement la même probabilité $p^2(1-p)$.
  Combien y a-t-il de tels chemins ? Exactement 3 chemins.
  D'où $P(X = 2) = 3 \times p^2(1-p)$.
  Et que vaut ce nombre 3 ? C'est le nombre de façons de choisir l'emplacement des 2 succès parmi les 3 épreuves, c'est-à-dire $\binom{3}{2} = 3$ !

> **📐 Théorème fondamental — Loi binomiale**
> Soit $X$ la variable aléatoire égale au nombre de succès dans un schéma de Bernoulli de $n$ épreuves indépendantes de paramètre $p$.
> On dit que $X$ suit la **loi binomiale de paramètres $n$ et $p$**, notée :
> $$X \sim \mathcal{B}(n, p)$$
> Pour tout entier $k \in \{0, 1, 2, \dots, n\}$, la probabilité d'obtenir exactement $k$ succès est :
>
> $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}$$

*Vérification de la cohérence :*
La somme de toutes les probabilités doit valoir 1 :
$$\sum_{k=0}^n P(X = k) = \sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1^n = 1.$$
C'est la formule du binôme de Newton du Chapitre 53 ! C'est précisément pour cela que cette loi s'appelle la **loi binomiale**.

---

### 3. Espérance et Variance : Les Démonstrations Exigibles

#### 3.1 Somme de variables aléatoires indépendantes
Soient $X_1, X_2, \dots, X_n$ les $n$ variables de Bernoulli associées aux $n$ épreuves :
$$X_i = \begin{cases} 1 & \text{si la } i\text{-ième épreuve est un succès} \\ 0 & \text{si c'est un échec} \end{cases}$$
Le nombre total de succès $X$ est tout simplement la somme de ces variables :
$$X = X_1 + X_2 + \dots + X_n = \sum_{i=1}^n X_i$$

Rappelons deux propriétés générales fondamentales vues en Première :
1. **Linéarité de l'espérance :** Pour toutes variables aléatoires $X$ et $Y$ (qu'elles soient indépendantes ou non) et tout réel $a$ :
   $$E(X + Y) = E(X) + E(Y) \quad \text{et} \quad E(aX) = a E(X)$$
2. **Additivité de la variance pour des variables indépendantes :**
   Si $X$ et $Y$ sont deux variables aléatoires **indépendantes** :
   $$V(X + Y) = V(X) + V(Y)$$
   *(Attention : si $a$ est une constante réelle, $V(aX) = a^2 V(X)$).*

#### 3.2 Démonstration de l'espérance de la loi binomiale

> **✍️ Démonstration exigible — Espérance de la loi binomiale**
> Soit $X \sim \mathcal{B}(n, p)$. On décompose $X$ sous la forme $X = \sum_{i=1}^n X_i$, où les $X_i$ sont $n$ variables de Bernoulli identiques de paramètre $p$.
> Pour chaque $i \in \{1, \dots, n\}$, on a $E(X_i) = p$.
> Par linéarité de l'espérance :
> $$E(X) = E\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n E(X_i) = \underbrace{p + p + \dots + p}_{n \text{ termes}} = np$$
>
> $$\mathbf{E(X) = n p}$$

*Sens intuitif :* Si tu lances 100 fois une pièce équilibrée ($p = 0{,}5$), tu t'attends en moyenne à obtenir $100 \times 0{,}5 = 50$ Piles. Si tu tires 60 fois un dé et que tu gagnes sur un 6 ($p = 1/6$), tu t'attends en moyenne à gagner $60 \times \frac{1}{6} = 10$ fois.

#### 3.3 Démonstration de la variance et de l'écart-type

> **✍️ Démonstration exigible — Variance de la loi binomiale**
> Puisque les épreuves sont mutuellement indépendantes dans un schéma de Bernoulli, les variables aléatoires $X_1, X_2, \dots, X_n$ sont indépendantes.
> Par additivité de la variance pour des variables indépendantes :
> $$V(X) = V\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n V(X_i)$$
> Or pour chaque variable de Bernoulli $X_i$, on a calculé que $V(X_i) = p(1 - p)$.
> D'où :
> $$V(X) = \sum_{i=1}^n p(1 - p) = \underbrace{p(1-p) + \dots + p(1-p)}_{n \text{ termes}} = np(1 - p)$$
>
> $$\mathbf{V(X) = n p (1 - p)}$$
>
> L'écart-type est par conséquent :
>
> $$\mathbf{\sigma(X) = \sqrt{n p (1 - p)}}$$

*Remarque cruciale sur les ordres de grandeur :*
- L'espérance $E(X)$ croît proportionnellement à $n$ (en ordre de grandeur $n$).
- L'écart-type $\sigma(X)$ croît seulement comme $\sqrt{n}$.
C'est cette asymétrie entre $n$ et $\sqrt{n}$ qui explique tout le miracle de la stabilisation statistique !

---

### 4. Dispersion et Concentration : De Markov à Bienaymé-Tchebychev

Comment mesurer la probabilité qu'une variable aléatoire s'éloigne beaucoup de sa moyenne ?

#### 4.1 L'inégalité de Markov
Le mathématicien russe **Andreï Markov** (1856–1922) a établi une borne universelle pour les variables positives.

> **📐 Théorème — Inégalité de Markov**
> Soit $Y$ une variable aléatoire prenant des valeurs positives ou nulles ($Y \geq 0$).
> Pour tout réel strictement positif $a > 0$ :
> $$P(Y \geq a) \leq \frac{E(Y)}{a}$$

> **✍️ Démonstration au programme — Inégalité de Markov**
> Soit $Y$ une variable aléatoire discrète prenant les valeurs positives $y_1, y_2, \dots, y_m \geq 0$.
> L'espérance s'écrit :
> $$E(Y) = \sum_{i=1}^m y_i P(Y = y_i)$$
> Découpons cette somme en deux parties : les valeurs strictement inférieures à $a$, et celles supérieures ou égales à $a$ :
> $$E(Y) = \sum_{y_i < a} y_i P(Y = y_i) + \sum_{y_i \geq a} y_i P(Y = y_i)$$
> Puisque toutes les valeurs $y_i$ et les probabilités sont positives ou nulles, la première somme est $\geq 0$. Donc :
> $$E(Y) \geq \sum_{y_i \geq a} y_i P(Y = y_i)$$
> Dans cette seconde somme, chaque terme $y_i$ vérifie $y_i \geq a$. On peut donc minorer chaque $y_i$ par $a$ :
> $$E(Y) \geq \sum_{y_i \geq a} a P(Y = y_i) = a \sum_{y_i \geq a} P(Y = y_i) = a P(Y \geq a)$$
> Comme $a > 0$, en divisant par $a$, il vient immédiatement :
> $$P(Y \geq a) \leq \frac{E(Y)}{a}$$

*Exemple frappant :* Si le revenu moyen d'un pays est de 2 000 € par mois, quelle proportion de la population peut gagner au moins 10 000 € ?
Ici $Y \geq 0$, $E(Y) = 2\,000$ et $a = 10\,000$.
$P(Y \geq 10\,000) \leq \frac{2\,000}{10\,000} = \frac{1}{5} = 20\,\%$.
Il est mathématiquement impossible que plus de 20 % des habitants gagnent plus de 5 fois le salaire moyen !

#### 4.2 L'inégalité de Bienaymé-Tchebychev
Le mathématicien français **Irénée-Jules Bienaymé** (1853) et son collègue russe **Pafnouti Tchebychev** (1867) ont eu l'idée géniale d'appliquer l'inégalité de Markov au carré de l'écart à la moyenne : $Y = (X - E(X))^2$.

> **📐 Théorème fondamental — Inégalité de Bienaymé-Tchebychev**
> Soit $X$ une variable aléatoire admettant une espérance $E(X)$ et une variance $V(X)$.
> Pour tout réel $\varepsilon > 0$ (epsilon) :
> $$P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$$

> **✍️ Démonstration exigible — Bienaymé-Tchebychev**
> Soit $\varepsilon > 0$. Remarquons l'équivalence fondamentale entre les événements :
> $$|X - E(X)| \geq \varepsilon \iff (X - E(X))^2 \geq \varepsilon^2$$
> Posons la variable aléatoire $Y = (X - E(X))^2$.
> - $Y$ est une variable aléatoire toujours positive ou nulle ($Y \geq 0$).
> - Son espérance est par définition la variance de $X$ : $E(Y) = E\left((X - E(X))^2\right) = V(X)$.
>
> Appliquons l'inégalité de Markov à la variable positive $Y$ avec le réel $a = \varepsilon^2 > 0$ :
> $$P(Y \geq \varepsilon^2) \leq \frac{E(Y)}{\varepsilon^2}$$
> En remplaçant $Y$ par sa définition et $E(Y)$ par $V(X)$ :
> $$P\left((X - E(X))^2 \geq \varepsilon^2\right) \leq \frac{V(X)}{\varepsilon^2}$$
> Ce qui donne exactement :
> $$P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$$

*Signification :*
La probabilité que la variable $X$ s'écarte de son espérance d'au moins $\varepsilon$ est plafonnée par un terme qui dépend directement de la variance et décroît très vite (comme l'inverse du carré de la distance $\varepsilon^2$).

---

### 5. La Loi Faible des Grands Nombres

#### 5.1 La moyenne empirique d'un échantillon
Considérons $n$ variables aléatoires indépendantes $X_1, X_2, \dots, X_n$ ayant **la même loi**, la même espérance $\mu = E(X_1)$ et la même variance $\sigma^2 = V(X_1)$.
On appelle **moyenne empirique** la variable aléatoire :
$$M_n = \frac{X_1 + X_2 + \dots + X_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i$$

Calculons l'espérance et la variance de cette moyenne :
- **Espérance de $M_n$ :**
  $$E(M_n) = E\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n} \sum_{i=1}^n E(X_i) = \frac{1}{n} \times n\mu = \mu$$
  La moyenne empirique est **sans biais** : en moyenne, elle vise exactement la valeur théorique $\mu$.
- **Variance de $M_n$ :**
  Par indépendance des variables $X_i$ et en sortant le facteur $\frac{1}{n}$ au carré :
  $$V(M_n) = V\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n V(X_i) = \frac{1}{n^2} \times n\sigma^2 = \frac{\sigma^2}{n}$$

Regarde bien cette fraction :
$$V(M_n) = \frac{V(X_1)}{n}$$
Quand la taille de l'échantillon $n$ devient géante, **la variance de la moyenne s'écrase vers zéro** !

#### 5.2 L'inégalité de concentration

> **📐 Théorème — Inégalité de concentration**
> Pour tout réel $\varepsilon > 0$ :
> $$P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$$

*Démonstration :*
Il suffit d'appliquer l'inégalité de Bienaymé-Tchebychev à la variable $M_n$ :
$$P(|M_n - E(M_n)| \geq \varepsilon) \leq \frac{V(M_n)}{\varepsilon^2}$$
En remplaçant $E(M_n) = \mu$ et $V(M_n) = \frac{V(X_1)}{n}$, on obtient la formule.

#### 5.3 Démonstration de la Loi Faible des Grands Nombres

> **✍️ Démonstration exigible — Loi faible des grands nombres**
> Soit $\varepsilon > 0$, fixé aussi petit que l'on veut (par exemple $\varepsilon = 0{,}001$).
> L'inégalité de concentration nous garantit que :
> $$0 \leq P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$$
> Lorsque $n$ tend vers $+\infty$, le numérateur $V(X_1)$ et $\varepsilon^2$ restent des constantes fixes.
> Donc :
> $$\lim_{n \to +\infty} \frac{V(X_1)}{n \varepsilon^2} = 0$$
> Par le théorème des gendarmes (théorème d'encadrement) :
>
> $$\mathbf{\lim_{n \to +\infty} P(|M_n - \mu| \geq \varepsilon) = 0}$$
>
> Ou, de manière équivalente pour l'événement contraire :
>
> $$\mathbf{\lim_{n \to +\infty} P(|M_n - \mu| < \varepsilon) = 1}$$

*Traduction philosophique et pratique :*
Quelle que soit la marge d'erreur $\varepsilon > 0$, aussi minuscule soit-elle, dès que l'échantillon $n$ est suffisamment grand, la probabilité que la moyenne des observations soit dans l'intervalle $]\mu - \varepsilon ; \mu + \varepsilon[$ tend vers 100 %.
Dans le cas particulier de lancers d'une pièce où $X_i \sim \mathcal{B}(p)$, $M_n = \frac{X}{n} = F_n$ est la **fréquence observée** de succès.
La fréquence observée d'un événement converge donc mathématiquement vers sa probabilité théorique $p$ !

---

### 6. Simulation Python : 10 000 lancers sous les yeux

Pour éprouver ce théorème, écrivons un programme Python qui simule $N = 10\,000$ lancers d'une pièce équilibrée ($p = 0{,}5$) et enregistre l'évolution de la fréquence de Pile au fur et à mesure :

```python
import random

def simulation_lancers(n):
    succes = 0
    historique_frequences = []
    
    for i in range(1, n + 1):
        # 1 = Pile (succès), 0 = Face (échec)
        tirage = random.choice([0, 1])
        succes += tirage
        frequence = succes / i
        historique_frequences.append((i, frequence))
        
    return historique_frequences

# Exemple d'exécution
resultats = simulation_lancers(10000)

# Affichage de quelques étapes clés
jalons = [10, 50, 100, 500, 1000, 5000, 10000]
print(f"{'Lancers (n)':<12} | {'Fréquence Pile':<15} | {'Écart à 0.5':<12}")
print("-" * 45)
for jalon in jalons:
    freq = resultats[jalon - 1][1]
    ecart = abs(freq - 0.5)
    print(f"{jalon:<12} | {freq:<15.4f} | {ecart:<12.4f}")
```

*Exemple typique de sortie console :*
```
Lancers (n)  | Fréquence Pile  | Écart à 0.5 
---------------------------------------------
10           | 0.7000          | 0.2000      
50           | 0.4400          | 0.0600      
100          | 0.5300          | 0.0300      
500          | 0.4880          | 0.0120      
1000         | 0.5040          | 0.0040      
5000         | 0.4982          | 0.0018      
10000        | 0.5007          | 0.0007      
```

Au début (10 lancers), la fréquence oscille sauvagement (de 0,30 à 0,70).
Vers 1 000 lancers, elle reste enfermée à moins de 1 % de 0,5.
À 10 000 lancers, la précision atteint le millième ! Le tourbillon aléatoire s'est cristallisé.

---

### 7. Exemples résolus pas à pas

#### Exemple 1 : Contrôle de qualité industriel
Une usine fabrique des ampoules LED. La probabilité qu'une ampoule soit défectueuse est $p = 0{,}02$. On prélève au hasard un lot de $n = 100$ ampoules. La production est suffisamment massive pour assimiler ce tirage à un tirage avec remise.
Soit $X$ le nombre d'ampoules défectueuses dans le lot.
1. Justifier la loi suivie par $X$ et donner ses paramètres.
2. Calculer l'espérance et l'écart-type de $X$.
3. Calculer la probabilité d'avoir exactement 2 ampoules défectueuses.
4. Calculer la probabilité d'avoir au moins une ampoule défectueuse.

**Solution détaillée :**
1. L'expérience consiste en la répétition de $n = 100$ épreuves identiques (tester une ampoule) à deux issues :
   - Succès $S$ : « l'ampoule est défectueuse », de probabilité $p = 0{,}02$.
   - Échec $\overline{S}$ : « l'ampoule fonctionne », de probabilité $1 - p = 0{,}98$.
   Le tirage étant assimilé à un tirage avec remise, les épreuves sont indépendantes.
   La variable aléatoire $X$ compte le nombre total de succès.
   Donc $X$ suit la **loi binomiale** de paramètres $n = 100$ et $p = 0{,}02$ : $X \sim \mathcal{B}(100 ; 0{,}02)$.
2. - Espérance : $E(X) = np = 100 \times 0{,}02 = 2$.
     En moyenne, un lot de 100 ampoules compte 2 ampoules défectueuses.
   - Variance : $V(X) = np(1-p) = 100 \times 0{,}02 \times 0{,}98 = 1{,}96$.
   - Écart-type : $\sigma(X) = \sqrt{1{,}96} = 1{,}4$.
3. Probabilité d'avoir exactement 2 défectueuses :
   $$P(X = 2) = \binom{100}{2} (0{,}02)^2 (0{,}98)^{98}$$
   Or $\binom{100}{2} = \frac{100 \times 99}{2} = 4\,950$.
   $(0{,}02)^2 = 0{,}0004$.
   $(0{,}98)^{98} \approx 0{,}1380$.
   $$P(X = 2) = 4\,950 \times 0{,}0004 \times 0{,}1380 \approx 0{,}2734 \quad (\approx 27{,}3\,\%).$$
4. « Au moins une défectueuse » correspond à $X \geq 1$.
   L'événement contraire est « aucune défectueuse », soit $X = 0$.
   $$P(X = 0) = \binom{100}{0} (0{,}02)^0 (0{,}98)^{100} = 1 \times 1 \times (0{,}98)^{100} \approx 0{,}1326.$$
   D'où :
   $$P(X \geq 1) = 1 - P(X = 0) = 1 - (0{,}98)^{100} \approx 1 - 0{,}1326 = 0{,}8674 \quad (\approx 86{,}7\,\%).$$

#### Exemple 2 : QCM au hasard
Un candidat se présente à un examen sans avoir révisé. Le test est un questionnaire à choix multiples (QCM) de 10 questions indépendantes. Pour chaque question, 4 réponses sont proposées, dont une seule est exacte. Le candidat coche une case au hasard pour chaque question.
Pour être reçu, il faut obtenir au moins 6 bonnes réponses.
Quelle est la probabilité que le candidat réussisse l'examen ?

**Solution détaillée :**
Soit $X$ le nombre de réponses exactes. Les 10 questions sont indépendantes avec $p = \frac{1}{4} = 0{,}25$.
Donc $X \sim \mathcal{B}(10 ; 0{,}25)$.
Le candidat réussit si $X \geq 6$.
$$P(X \geq 6) = P(X = 6) + P(X = 7) + P(X = 8) + P(X = 9) + P(X = 10)$$
Calculons chaque terme :
- $P(X = 6) = \binom{10}{6} (0{,}25)^6 (0{,}75)^4 = 210 \times \frac{1}{4096} \times \frac{81}{256} = \frac{17\,010}{1\,048\,576} \approx 0{,}01622$
- $P(X = 7) = \binom{10}{7} (0{,}25)^7 (0{,}75)^3 = 120 \times \frac{1}{16384} \times \frac{27}{64} = \frac{3\,240}{1\,048\,576} \approx 0{,}00309$
- $P(X = 8) = \binom{10}{8} (0{,}25)^8 (0{,}75)^2 = 45 \times \frac{1}{65536} \times \frac{9}{16} = \frac{405}{1\,048\,576} \approx 0{,}000386$
- $P(X = 9) = \binom{10}{9} (0{,}25)^9 (0{,}75)^1 = 10 \times \frac{3}{1\,048\,576} \approx 0{,}000029$
- $P(X = 10) = \binom{10}{10} (0{,}25)^{10} (0{,}75)^0 = \frac{1}{1\,048\,576} \approx 0{,}000001$

En sommant ces probabilités :
$$P(X \geq 6) \approx 0{,}01622 + 0{,}00309 + 0{,}00039 + 0{,}00003 + 0{,}000001 = 0{,}01973 \approx 1{,}97\,\%.$$
Le candidat a moins de $2\,\%$ de chances d'être admis au pur hasard.

#### Exemple 3 : Surréservation d'une compagnie aérienne (Overbooking)
Un avion dispose de 200 places. Une compagnie aérienne sait par expérience que 5 % des passagers ayant acheté un billet ne se présentent pas à l'embarquement ($p_{\text{présence}} = 0{,}95$).
La compagnie vend $n = 205$ billets.
1. Quelle est la probabilité que tous les passagers qui se présentent aient un siège ?
2. Quelle est la probabilité que la compagnie se retrouve en situation de surréservation critique (au moins un passager sans siège) ?

**Solution détaillée :**
1. Soit $Y$ le nombre de passagers qui se présentent à l'embarquement parmi les 205 acheteurs. En supposant les comportements des passagers indépendants, $Y \sim \mathcal{B}(205 ; 0{,}95)$.
   Tous les passagers qui se présentent ont un siège si et seulement si $Y \leq 200$.
   La probabilité contraire est $P(Y > 200) = P(Y = 201) + P(Y = 202) + P(Y = 203) + P(Y = 204) + P(Y = 205)$.
   Calculons ces 5 termes :
   - $P(Y = 205) = (0{,}95)^{205} \approx 0{,}000025$
   - $P(Y = 204) = 205 \times (0{,}95)^{204} \times 0{,}05 \approx 0{,}000270$
   - $P(Y = 203) = \binom{205}{2} (0{,}95)^{203} (0{,}05)^2 = 20\,910 \times (0{,}95)^{203} \times 0{,}0025 \approx 0{,}00144$
   - $P(Y = 202) = \binom{205}{3} (0{,}95)^{202} (0{,}05)^3 \approx 0{,}0051$
   - $P(Y = 201) = \binom{205}{4} (0{,}95)^{201} (0{,}05)^4 \approx 0{,}0133$
   Somme des cas critiques :
   $$P(Y > 200) \approx 0{,}0133 + 0{,}0051 + 0{,}0014 + 0{,}0003 + 0{,}0000 = 0{,}0201 \approx 2{,}01\,\%.$$
2. La probabilité d'un problème de surréservation est d'environ $2{,}0\,\%$.
   La probabilité que tout se passe bien est donc d'environ $1 - 0{,}0201 = 0{,}9799$, soit près de $98\,\%$.

#### Exemple 4 : Dimensionnement d'échantillon par Bienaymé-Tchebychev
On lance une pièce de monnaie équilibrée de paramètre $p = 0{,}5$. On note $F_n = \frac{X}{n}$ la fréquence observée de Pile sur $n$ lancers.
On souhaite que la probabilité que la fréquence s'écarte de 0,5 de plus de 0,02 soit inférieure à 0,05 (soit au plus 5 % de risque d'erreur supérieure à 2 centièmes).
Déterminer, à l'aide de l'inégalité de concentration, un nombre de lancers $n$ garantissant cette précision.

**Solution détaillée :**
Ici, $X_1 \sim \mathcal{B}(0{,}5)$, donc $\mu = 0{,}5$ et $V(X_1) = p(1-p) = 0{,}5 \times 0{,}5 = 0{,}25$.
La marge d'erreur tolérée est $\varepsilon = 0{,}02$.
D'après l'inégalité de concentration appliquée à $M_n = F_n$ :
$$P(|F_n - 0{,}5| \geq 0{,}02) \leq \frac{V(X_1)}{n \varepsilon^2} = \frac{0{,}25}{n \times (0{,}02)^2} = \frac{0{,}25}{n \times 0{,}0004} = \frac{625}{n}$$
Nous voulons que ce risque soit majoré par $0{,}05 = \frac{1}{20}$ :
$$\frac{625}{n} \leq 0{,}05 \iff n \geq \frac{625}{0{,}05} = 12\,500.$$
Il suffit donc de réaliser $12\,500$ lancers pour être absolument certain, sans aucune hypothèse supplémentaire, que le risque d'écart supérieur à 0,02 ne dépasse pas 5 %.
*(Remarque : Bienaymé-Tchebychev étant universelle, cette borne est très prudente. Avec la loi normale du supérieur, environ 2 500 lancers suffiraient).*

#### Exemple 5 : Test de dépistage médical en population
Un test de dépistage rapide a une probabilité de faux positif de $1\,\%$ ($p = 0{,}01$).
On teste un groupe de 500 personnes saines. Soit $X$ le nombre de faux positifs observés.
1. Déterminer $E(X)$ et $V(X)$.
2. Donner une borne supérieure de $P(|X - 5| \geq 4)$ à l'aide de Bienaymé-Tchebychev.

**Solution détaillée :**
1. $X \sim \mathcal{B}(500 ; 0{,}01)$.
   - $E(X) = np = 500 \times 0{,}01 = 5$.
   - $V(X) = np(1-p) = 500 \times 0{,}01 \times 0{,}99 = 4{,}95$.
2. L'espérance étant $E(X) = 5$, l'expression $|X - 5| \geq 4$ correspond à un écart $\varepsilon = 4$.
   Par l'inégalité de Bienaymé-Tchebychev :
   $$P(|X - 5| \geq 4) \leq \frac{V(X)}{4^2} = \frac{4{,}95}{16} \approx 0{,}3094.$$
   La probabilité d'avoir moins de 1 faux positif ou au moins 9 faux positifs est donc garantie inférieure à $31\,\%$.

#### Exemple 6 : Somme de deux variables binomiales indépendantes
Deux chaînes de fabrication indépendantes A et B produisent des pièces.
- La chaîne A produit 50 pièces par heure, avec une probabilité de défaut de $0{,}03$. Soit $X_A$ le nombre de pièces défectueuses de la chaîne A : $X_A \sim \mathcal{B}(50 ; 0{,}03)$.
- La chaîne B produit 70 pièces par heure, avec une probabilité de défaut de $0{,}03$. Soit $X_B$ le nombre de pièces défectueuses de la chaîne B : $X_B \sim \mathcal{B}(70 ; 0{,}03)$.
Soit $S = X_A + X_B$ le nombre total de pièces défectueuses produites en une heure par l'atelier.
1. Déterminer la loi de $S$.
2. Calculer $E(S)$ et $V(S)$.

**Solution détaillée :**
1. Chaque pièce de la chaîne A subit une épreuve de Bernoulli de paramètre $p = 0{,}03$. Il y en a 50 indépendantes.
   Chaque pièce de la chaîne B subit la même épreuve de Bernoulli de paramètre $p = 0{,}03$. Il y en a 70 indépendantes.
   Puisque les deux chaînes sont indépendantes et que **le paramètre de succès $p$ est identique**, la somme $S = X_A + X_B$ représente le nombre total de succès lors de $50 + 70 = 120$ épreuves de Bernoulli indépendantes de même paramètre $0{,}03$.
   Par conséquent :
   $$S \sim \mathcal{B}(120 ; 0{,}03)$$
   *(Attention capitale : cette propriété de stabilité de la loi binomiale n'est vraie que si le paramètre $p$ est le même pour les deux variables !)*
2. - $E(S) = np = 120 \times 0{,}03 = 3{,}6$.
   - $V(S) = np(1-p) = 120 \times 0{,}03 \times 0{,}97 = 3{,}492$.

---

### Ce qu'il faut retenir

1. **Loi de Bernoulli $\mathcal{B}(p)$ :**
   - 2 issues : Succès ($X=1$, probabilité $p$), Échec ($X=0$, probabilité $1-p$).
   - $E(X) = p$ et $V(X) = p(1-p)$.

2. **Loi Binomiale $\mathcal{B}(n, p)$ :**
   - Répétition de $n$ épreuves de Bernoulli identiques et indépendantes.
   - Formule : $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.
   - Espérance : $E(X) = np$.
   - Variance : $V(X) = np(1-p)$ ; Écart-type : $\sigma(X) = \sqrt{np(1-p)}$.

3. **Inégalités universelles :**
   - **Markov :** Si $Y \geq 0$ et $a > 0$, alors $P(Y \geq a) \leq \frac{E(Y)}{a}$.
   - **Bienaymé-Tchebychev :** Pour tout $\varepsilon > 0$, $P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$.
   - **Concentration :** Pour la moyenne empirique $M_n$, $P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$.

4. **Loi faible des grands nombres :**
   - $\lim_{n \to +\infty} P(|M_n - \mu| \geq \varepsilon) = 0$.
   - La fréquence expérimentale converge infailliblement vers la probabilité théorique lorsque le nombre d'essais tend vers l'infini.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 1.** Soit $X \sim \mathcal{B}(6 ; 0{,}3)$.
1. Calculer $E(X)$ et $V(X)$.
2. Calculer la probabilité exacte $P(X = 2)$.
3. Exprimer $P(X \geq 1)$ et calculer sa valeur arrondie à $10^{-4}$.
**Exercice 2.** On lance 8 fois de suite une pièce équilibrée. Soit $X$ le nombre de faces « Pile » obtenues.
1. Quelle est la loi suivie par $X$ ?
2. Calculer $P(X = 4)$.
**Exercice 3.** Un archer tire 5 flèches sur une cible. À chaque tir, la probabilité d'atteindre le centre est $p = 0{,}7$. On suppose les tirs indépendants.
Calculer la probabilité que l'archer atteigne le centre :
1. Exactement 5 fois.
2. Au moins une fois.
**Exercice 4.** Une variable aléatoire positive $Y \geq 0$ vérifie $E(Y) = 12$.
À l'aide de l'inégalité de Markov, majorer la probabilité $P(Y \geq 60)$.
**Exercice 5.** Une variable aléatoire $X$ a pour espérance $E(X) = 50$ et pour variance $V(X) = 8$.
À l'aide de l'inégalité de Bienaymé-Tchebychev, majorer la probabilité $P(|X - 50| \geq 6)$.
**Exercice 6.** Vrai ou Faux ? Justifier.
1. Si on lance 100 fois une pièce, la probabilité d'avoir exactement 50 Piles est égale à 0,5.
2. Si $X \sim \mathcal{B}(10 ; 0{,}4)$, alors $P(X \leq 9) = 1 - (0{,}4)^{10}$.
3. Pour toute variable aléatoire, $P(|X - E(X)| \geq 3\sigma) \leq \frac{1}{9}$.
**Exercice 7.** Une urne contient 3 boules blanches et 7 boules noires. On effectue 4 tirages successifs **avec remise**. Soit $X$ le nombre de boules blanches obtenues.
Donner la loi de $X$, son espérance et la probabilité d'avoir exactement 1 boule blanche.

#### Niveau ★★ (Réflexion et calculs de baccalauréat)

**Exercice 8.** Un traitement médical guérit une maladie dans $80\,\%$ des cas. On applique ce traitement à un groupe de 20 malades indépendants. Soit $X$ le nombre de guérisons.
1. Calculer la probabilité qu'exactement 16 malades guérissent.
2. Calculer la probabilité qu'au moins 18 malades guérissent.
**Exercice 9.** On lance $n$ fois un dé équilibré à 6 faces. On note $A$ l'événement : « obtenir au moins un 6 ».
Combien de fois au minimum faut-il lancer le dé pour que la probabilité d'obtenir au moins un 6 soit supérieure ou égale à 0,99 ?
**Exercice 10.** Inégalité de concentration pour un sondage.
On interroge $n$ personnes choisies au hasard pour connaître la proportion $p$ d'électeurs favorables à un projet. On note $F_n$ la fréquence observée dans l'échantillon.
1. Rappeler pourquoi $V(X_1) = p(1-p) \leq \frac{1}{4}$ pour tout $p \in [0; 1]$.
2. En déduire que $P(|F_n - p| \geq 0{,}05) \leq \frac{100}{n}$.
3. Quelle taille d'échantillon $n$ permet de garantir que la fréquence observée ne s'écarte pas de plus de 0,05 de la vraie proportion avec un risque inférieur à 1 % ?
**Exercice 11.** Mode de la loi binomiale.
Soit $X \sim \mathcal{B}(n, p)$.
1. Montrer que le rapport $\frac{P(X = k+1)}{P(X = k)}$ vaut $\frac{n - k}{k + 1} \frac{p}{1 - p}$.
2. En déduire pour quelle(s) valeur(s) de $k$ la probabilité $P(X = k)$ est maximale.
**Exercice 12.** Un serveur informatique traite 1 000 requêtes par minute. La durée de traitement de chaque requête est une variable aléatoire indépendante d'espérance $\mu = 40\text{ ms}$ et d'écart-type $\sigma = 15\text{ ms}$.
Majorer la probabilité que la durée moyenne des 1 000 requêtes s'écarte de 40 ms de plus de 2 ms.
**Exercice 13.** Deux variables $X_1 \sim \mathcal{B}(n_1, p)$ et $X_2 \sim \mathcal{B}(n_2, p)$ sont indépendantes.
Démontrer algébriquement, en utilisant la formule de Vandermonde du Chapitre 53, que $X_1 + X_2 \sim \mathcal{B}(n_1 + n_2, p)$.
**Exercice 14.** Loi géométrique tronquée (temps du premier succès).
On répète de manière indépendante une épreuve de Bernoulli de paramètre $p$. Soit $T$ le rang du premier succès.
1. Pour tout entier $k \geq 1$, déterminer $P(T = k)$.
2. Calculer $P(T > k)$ de manière directe et combinatoire.
3. Vérifier que $\sum_{k=1}^{+\infty} P(T = k) = 1$.
**Exercice 15.** Fluctuation de l'écart absolu.
Soit $X \sim \mathcal{B}(n ; 0{,}5)$.
Démontrer que $P(|X - 0{,}5n| \geq a\sqrt{n}) \leq \frac{1}{4a^2}$. En déduire l'ordre de grandeur des fluctuations autour de la moyenne.

#### Niveau ★★★ (Approfondissements et concours)

**Exercice 16.** Démonstration directe de l'espérance sans décomposition.
Retrouver la formule $E(X) = np$ pour $X \sim \mathcal{B}(n, p)$ par le calcul direct de la somme :
$$E(X) = \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k}$$
*(Indication : utiliser la formule du comité $k\binom{n}{k} = n\binom{n-1}{k-1}$ vue au Chapitre 53).*
**Exercice 17.** Démonstration directe de la variance par calcul de somme.
1. Calculer de même la quantité $E(X(X-1)) = \sum_{k=0}^n k(k-1) \binom{n}{k} p^k (1-p)^{n-k}$.
2. En déduire la valeur de $E(X^2)$, puis retrouver $V(X) = np(1-p)$.
**Exercice 18.** Règle de succession de Laplace.
On a tiré $n$ boules d'une urne avec remise, et obtenu $k$ succès. Quelle est la probabilité que le prochain tirage soit un succès si la composition initiale de l'urne était totalement inconnue ?
Montrer que l'estimation bayésienne uniforme mène à la formule de Laplace :
$$P(S_{n+1}) = \frac{k + 1}{n + 2}$$
Comparer avec l'estimation naïve $\frac{k}{n}$ pour $k = 0$ et $k = n$.
**Exercice 19.** Inégalité de Cantelli (Bienaymé-Tchebychev unilatérale).
Soit $X$ une variable aléatoire d'espérance 0 et de variance $\sigma^2$.
Démontrer que pour tout réel $a > 0$ :
$$P(X \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$$
*(Indication : pour tout $t > 0$, considérer la variable $(X + t)^2$ et optimiser le choix de $t$).*
**Exercice 20.** L'aiguille de Buffon et Monte-Carlo.
Un plan est strié de lignes parallèles distantes d'une largeur $D$. On y jette au hasard une aiguille de longueur $L \leq D$.
1. Sachant que la probabilité d'intersection est $p = \frac{2L}{\pi D}$, expliquer comment estimer la constante $\pi$ par simulation informatique.
2. Si l'on réalise $n$ lancers indépendants, déterminer à l'aide de l'inégalité de concentration le nombre de lancers nécessaires pour obtenir une précision de 0,01 sur $\pi$ avec un niveau de confiance garanti.
**Exercice 21.** Paradoxe du vote et théorème du jury de Condorcet.
Un jury de $n$ jurés indépendants ($n$ impair, $n = 2m+1$) doit trancher par vote majoritaire entre coupable et non coupable. Chaque juré a une probabilité individuelle $p > 0{,}5$ de prendre la bonne décision.
1. Exprimer la probabilité $P_n$ que la majorité du jury prenne la bonne décision.
2. Démontrer que $P_n > p$ et que $\lim_{n \to +\infty} P_n = 1$.
Interpréter ce résultat pour la démocratie et les jurys d'assises.
**Exercice 22.** Convergence presque sûre et loi forte des grands nombres (Aperçu).
Expliquer la différence conceptuelle entre la loi faible des grands nombres (qui affirme la convergence en probabilité $\lim P(|M_n - \mu| \geq \varepsilon) = 0$) et la loi forte d'Émile Borel et Kolmogorov (qui affirme que la trajectoire des fréquences converge vers $\mu$ avec probabilité 1).

---

### Solutions

**Solution 1.**
1. $E(X) = np = 6 \times 0{,}3 = 1{,}8$.
   $V(X) = np(1-p) = 6 \times 0{,}3 \times 0{,}7 = 1{,}26$.
2. $P(X = 2) = \binom{6}{2} (0{,}3)^2 (0{,}7)^4 = 15 \times 0{,}09 \times 0{,}2401 = 0{,}3241$.
3. $P(X \geq 1) = 1 - P(X = 0) = 1 - \binom{6}{0} (0{,}3)^0 (0{,}7)^6 = 1 - (0{,}7)^6 = 1 - 0{,}117649 = 0{,}8824$.

**Solution 2.**
1. Répétition de 8 épreuves de Bernoulli indépendantes avec $p = 0{,}5$. Donc $X \sim \mathcal{B}(8 ; 0{,}5)$.
2. $P(X = 4) = \binom{8}{4} (0{,}5)^4 (0{,}5)^4 = 70 \times (0{,}5)^8 = \frac{70}{256} = \frac{35}{128} \approx 0{,}2734$.

**Solution 3.**
$X \sim \mathcal{B}(5 ; 0{,}7)$.
1. $P(X = 5) = (0{,}7)^5 = 0{,}16807$.
2. $P(X \geq 1) = 1 - P(X = 0) = 1 - (0{,}3)^5 = 1 - 0{,}00243 = 0{,}99757$.

**Solution 4.**
Par l'inégalité de Markov : $P(Y \geq 60) \leq \frac{E(Y)}{60} = \frac{12}{60} = \frac{1}{5} = 0{,}20$.

**Solution 5.**
Par l'inégalité de Bienaymé-Tchebychev : $P(|X - 50| \geq 6) \leq \frac{V(X)}{6^2} = \frac{8}{36} = \frac{2}{9} \approx 0{,}222$.

**Solution 6.**
1. **Faux.** Pour $n = 100$ et $p = 0{,}5$, $P(X = 50) = \binom{100}{50} (0{,}5)^{100} \approx 0{,}0796$ (environ 8 %). La valeur moyenne est 50, mais la probabilité d'y tomber pile est dispersée sur les valeurs voisines.
2. **Faux.** $P(X \leq 9) = 1 - P(X = 10) = 1 - \binom{10}{10} (0{,}4)^{10} (0{,}6)^0 = 1 - (0{,}4)^{10}$. Donc l'affirmation est **Vraie** !
3. **Vrai.** Pour $\varepsilon = 3\sigma$, $P(|X - E(X)| \geq 3\sigma) \leq \frac{\sigma^2}{(3\sigma)^2} = \frac{1}{9}$.

**Solution 7.**
Tirage avec remise : $p = \frac{3}{10} = 0{,}3$. $n = 4$ épreuves indépendantes.
$X \sim \mathcal{B}(4 ; 0{,}3)$.
$E(X) = 4 \times 0{,}3 = 1{,}2$.
$P(X = 1) = \binom{4}{1} (0{,}3)^1 (0{,}7)^3 = 4 \times 0{,}3 \times 0{,}343 = 0{,}4116$.

**Solution 8.**
$X \sim \mathcal{B}(20 ; 0{,}8)$.
1. $P(X = 16) = \binom{20}{16} (0{,}8)^{16} (0{,}2)^4 = 4\,845 \times (0{,}8)^{16} \times (0{,}2)^4 \approx 0{,}2182$.
2. $P(X \geq 18) = P(X = 18) + P(X = 19) + P(X = 20)$.
   - $P(X = 18) = \binom{20}{18} (0{,}8)^{18} (0{,}2)^2 = 190 \times (0{,}8)^{18} \times 0{,}04 \approx 0{,}1369$
   - $P(X = 19) = 20 \times (0{,}8)^{19} \times 0{,}2 \approx 0{,}0576$
   - $P(X = 20) = (0{,}8)^{20} \approx 0{,}0115$
   Total : $P(X \geq 18) \approx 0{,}1369 + 0{,}0576 + 0{,}0115 = 0{,}2060 \quad (\approx 20{,}6\,\%)$.

**Solution 9.**
La probabilité de n'obtenir aucun 6 en $n$ lancers est $(5/6)^n$.
On veut $P(A) = 1 - (5/6)^n \geq 0{,}99 \iff (5/6)^n \leq 0{,}01$.
En appliquant le logarithme népérien ($\ln(5/6) < 0$, l'inégalité change de sens) :
$n \ln(5/6) \leq \ln(0{,}01) \iff n \geq \frac{\ln(0{,}01)}{\ln(5/6)} \approx \frac{-4{,}60517}{-0{,}18232} \approx 25{,}26$.
Il faut au minimum **26 lancers**.

**Solution 10.**
1. Pour la fonction $f(p) = p(1-p) = p - p^2$, sa dérivée $f'(p) = 1 - 2p$ s'annule en $p = 0{,}5$, où elle atteint son maximum $f(0{,}5) = 0{,}25 = \frac{1}{4}$.
2. Par l'inégalité de concentration avec $\varepsilon = 0{,}05$ :
   $P(|F_n - p| \geq 0{,}05) \leq \frac{V(X_1)}{n (0{,}05)^2} \leq \frac{0{,}25}{n \times 0{,}0025} = \frac{100}{n}$.
3. On veut $\frac{100}{n} \leq 0{,}01 \iff n \geq \frac{100}{0{,}01} = 10\,000$. Un échantillon de 10 000 personnes garantit ce résultat.

**Solution 11.**
1. $\frac{P(X = k+1)}{P(X = k)} = \frac{\frac{n!}{(k+1)!(n-k-1)!} p^{k+1} (1-p)^{n-k-1}}{\frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}} = \frac{n-k}{k+1} \frac{p}{1-p}$.
2. Le rapport est $\geq 1$ tant que $(n-k)p \geq (k+1)(1-p) \iff np - kp \geq k - kp + 1 - p \iff np + p - 1 \geq k \iff k \leq (n+1)p - 1$.
   La suite des probabilités est donc d'abord croissante, puis décroissante. Le mode (maximum) est atteint pour l'entier $k = \lfloor (n+1)p \rfloor$.

**Solution 12.**
Pour $n = 1000$ requêtes, la durée moyenne $M_n$ a pour espérance $\mu = 40$ et pour variance $V(M_n) = \frac{\sigma^2}{n} = \frac{15^2}{1000} = \frac{225}{1000} = 0{,}225$.
Par Bienaymé-Tchebychev avec $\varepsilon = 2$ :
$P(|M_n - 40| \geq 2) \leq \frac{V(M_n)}{2^2} = \frac{0{,}225}{4} = 0{,}05625$ (moins de $5{,}6\,\%$).

**Solution 13.**
Pour tout $k \in \{0, \dots, n_1+n_2\}$, l'événement $(X_1 + X_2 = k)$ est l'union disjointe des événements $(X_1 = j \text{ et } X_2 = k-j)$ pour $j \in \{0, \dots, k\}$.
Par indépendance :
$$P(X_1+X_2=k) = \sum_{j=0}^k \binom{n_1}{j} p^j (1-p)^{n_1-j} \binom{n_2}{k-j} p^{k-j} (1-p)^{n_2-(k-j)} = p^k (1-p)^{n_1+n_2-k} \sum_{j=0}^k \binom{n_1}{j}\binom{n_2}{k-j}$$
D'après la formule de Vandermonde, la somme vaut $\binom{n_1+n_2}{k}$.
On reconnaît immédiatement la formule d'une loi $\mathcal{B}(n_1+n_2, p)$.

**Solution 14.**
1. $T = k$ signifie $k-1$ échecs consécutifs suivis d'un succès : $P(T = k) = (1-p)^{k-1} p$.
2. $T > k$ signifie que les $k$ premières épreuves ont toutes été des échecs : $P(T > k) = (1-p)^k$.
3. $\sum_{k=1}^{+\infty} p (1-p)^{k-1} = p \sum_{j=0}^{+\infty} (1-p)^j = p \frac{1}{1 - (1-p)} = \frac{p}{p} = 1$.

**Solution 15.**
Pour $X \sim \mathcal{B}(n ; 0{,}5)$, $E(X) = 0{,}5n$ et $V(X) = 0{,}25n$.
Appliquons Bienaymé-Tchebychev avec $\varepsilon = a\sqrt{n}$ :
$P(|X - 0{,}5n| \geq a\sqrt{n}) \leq \frac{V(X)}{(a\sqrt{n})^2} = \frac{0{,}25n}{a^2 n} = \frac{1}{4a^2}$.
L'écart typique entre le nombre de succès et sa moyenne est donc de l'ordre de grandeur de $\sqrt{n}$.

**Solution 16.**
$E(X) = \sum_{k=1}^n k \binom{n}{k} p^k (1-p)^{n-k}$.
Or $k\binom{n}{k} = n\binom{n-1}{k-1}$.
$$E(X) = \sum_{k=1}^n n \binom{n-1}{k-1} p \cdot p^{k-1} (1-p)^{(n-1)-(k-1)} = np \sum_{j=0}^{n-1} \binom{n-1}{j} p^j (1-p)^{n-1-j} = np (p + (1-p))^{n-1} = np.$$

**Solution 17.**
1. $k(k-1)\binom{n}{k} = k(k-1)\frac{n!}{k!(n-k)!} = \frac{n!}{(k-2)!(n-k)!} = n(n-1)\binom{n-2}{k-2}$.
   En sommant pour $k \geq 2$ :
   $E(X(X-1)) = n(n-1)p^2 \sum_{j=0}^{n-2} \binom{n-2}{j} p^j (1-p)^{n-2-j} = n(n-1)p^2$.
2. $E(X^2) = E(X(X-1)) + E(X) = n(n-1)p^2 + np = n^2 p^2 - np^2 + np$.
   $V(X) = E(X^2) - (E(X))^2 = (n^2 p^2 - np^2 + np) - (np)^2 = np(1-p)$.

**Solution 18.**
Sous une loi a priori uniforme sur le paramètre inconnu $p \in [0, 1]$, la probabilité conditionnelle s'écrit à l'aide de la fonction Bêta :
$P(S_{n+1} \mid k \text{ succès sur } n) = \frac{\int_0^1 p \cdot p^k (1-p)^{n-k} dp}{\int_0^1 p^k (1-p)^{n-k} dp} = \frac{B(k+2, n-k+1)}{B(k+1, n-k+1)} = \frac{k+1}{n+2}$.
Pour $k = 0$ (aucun succès sur 10 essais), l'estimation naïve donne 0, alors que Laplace donne $\frac{1}{12} \approx 8{,}3\,\%$, évitant l'arrogance d'affirmer l'impossibilité d'un événement jamais encore observé.

**Solution 19.**
Pour tout $t > 0$, l'événement $X \geq a$ équivaut à $X + t \geq a + t$, ce qui implique $(X + t)^2 \geq (a + t)^2$.
Par Markov sur $(X+t)^2 \geq 0$ :
$P(X \geq a) \leq \frac{E((X+t)^2)}{(a+t)^2} = \frac{E(X^2) + 2tE(X) + t^2}{(a+t)^2} = \frac{\sigma^2 + t^2}{(a+t)^2}$.
En minimisant cette fonction par rapport à $t > 0$, la dérivée s'annule pour $t = \frac{\sigma^2}{a}$.
En substituant cette valeur optimale, on obtient exactement $P(X \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$.

**Solution 20.**
1. Si on lance $n$ aiguilles et qu'on compte $X$ intersections, la fréquence $F_n = \frac{X}{n}$ converge vers $p = \frac{2L}{\pi D}$. Une estimation de $\pi$ est donc $\hat{\pi}_n = \frac{2L}{D \cdot F_n}$.
2. Par l'inégalité de concentration, comme $V(X_1) \leq 1/4$, on majore la variance de la fréquence par $\frac{1}{4n}$. Pour obtenir une précision donnée sur $p$, on résout $\frac{1}{4n\varepsilon^2} \leq \alpha$, ce qui donne un nombre fini de lancers $n$ garantissant le résultat.

**Solution 21.**
1. La majorité est atteinte dès que $k \geq m+1 = \frac{n+1}{2}$. Donc $P_n = \sum_{k=m+1}^n \binom{n}{k} p^k (1-p)^{n-k}$.
2. D'après la loi des grands nombres, lorsque $n \to +\infty$, la fréquence de votes corrects converge vers $p > 0{,}5$. La probabilité que la majorité vote correctement tend donc vers 1. Ce théorème fonde la justification mathématique de la délibération collective : un grand groupe d'individus faillibles mais moyennement éclairés ($p > 0{,}5$) prend une décision quasi parfaite à la majorité.

**Solution 22.**
La loi faible indique que pour une taille d'échantillon $n$ fixée arbitrairement grande, la probabilité d'un écart ponctuel est infime. La loi forte garantit un résultat infiniment plus puissant : avec une probabilité égale à 1, la suite infinie entière des moyennes $(M_n)_{n \geq 1}$ converge vers $\mu$, ce qui interdit toute résurgence infinie de déviations.

---

### La question qui ouvre la suite

Nous venons de voir comment les lois statistiques gouvernent le monde réel des lancers de pièces et des mesures d'échantillons.
Mais que se passe-t-il lorsque l'algèbre elle-même se heurte à un mur absolu ?
Rappelle-toi l'équation $x^2 = -1$ : aucun nombre réel, aucun décompte de cailloux, aucune probabilité ne peut avoir un carré négatif.
Et pourtant, au XVIᵉ siècle, en tentant de résoudre de simples équations du troisième degré dont les solutions étaient d'évidents nombres entiers, des savants italiens ont été forcés d'inventer un nombre fantôme. Un nombre capable de faire pivoter le monde d'un quart de tour à angle droit.
Bienvenue dans le monde fascinant des nombres complexes : tourne la page pour découvrir **le Chapitre 55 et le Tourbillon à Angle Droit**.
