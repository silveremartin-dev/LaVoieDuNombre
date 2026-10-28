# VOLUME V — L'Âge de la Flèche et de la Boussole (15 - 17 ans / 2nde - 1ère spécialité)
## CHAPITRE 36 : Les Marches de l'Escalier et le Prêt de l'Usurier

> *« Une courbe continue coule comme l'eau d'une rivière, sans jamais lever la plume du papier. Mais le temps des hommes avance par saccades : les battements du cœur, les tic-tacs de l'horloge, les marches d'un escalier de pierre et les intérêts qui tombent à la fin du mois. Une suite numérique est un voyage où chaque pas s'appuie sur le précédent pour s'élancer vers l'infini. »*

---

### Ce que tu vas découvrir

- La différence fondamentale entre une grandeur continue et une **suite numérique** indexée par les entiers naturels $n \in \mathbb{N}$.
- Les deux grandes façons d'engendrer une suite : la formule **explicite** $u_n = f(n)$ et la relation de **récurrence** $u_{n+1} = g(u_n)$.
- Les **suites arithmétiques** : l'escalier régulier où l'on ajoute toujours la même raison $r$, et l'astuce légendaire du jeune **Carl Friedrich Gauss** pour sommer les entiers.
- Les **suites géométriques** : la multiplication en chaîne par la raison $q$, le vertige du prêt à intérêts et le piège de l'échiquier de Sissa.
- Comment déterminer le **sens de variation** d'une suite et appréhender intuitivement sa **limite** à l'infini.
- La programmation d'un **algorithme de seuil** en Python pour savoir quand une quantité dépasse un plafond donné.

---

### 1. Le problème : les deux banquiers de Florence

Dans la Florence de la Renaissance, deux marchands d'étoffes, Matteo et Cosimo, cherchent un financement pour affréter une caravelle vers l'Orient. Chacun a besoin d'emprunter $1\,000$ florins d'or pour une durée de 10 ans.

Ils s'adressent à deux prêteurs sur le Ponte Vecchio :

```
       CONTRAT MATTEO (Prêt arithmétique)          CONTRAT COSIMO (Prêt géométrique)
   Chaque année, Matteo rembourse              Chaque année, la dette de Cosimo
   une pénalité FIXE de 100 florins.           augmente de 10 % (taux composé).
   
   Année 0 : 1 000 florins                     Année 0 : 1 000 florins
   Année 1 : 1 100 florins                     Année 1 : 1 100 florins
   Année 2 : 1 200 florins                     Année 2 : 1 210 florins
   Année 3 : 1 300 florins                     Année 3 : 1 331 florins
   ...                                         ...
   Année 10 : 2 000 florins                    Année 10 : 2 593,74 florins !
```

Regarde attentivement ce qui s'est produit :
- Pour Matteo, chaque année ajoute **le même montant fixe** : $+100$ florins. C'est un escalier régulier. En 10 ans, il paie $1\,000 + 10 \times 100 = 2\,000$ florins.
- Pour Cosimo, la première année semble identique ($+100$ florins). Mais la deuxième année, les $10\ \%$ s'appliquent sur les $1\,100$ florins déjà dus : la dette grossit de $110$ florins ! La troisième année, les $10\ \%$ s'appliquent sur $1\,210$ florins ($+121$ florins). Les intérêts font des petits qui font eux-mêmes des petits : c'est le mécanisme redoutable des **intérêts composés**. En 10 ans, Cosimo doit près de $2\,594$ florins, soit $60\ \%$ de plus que Matteo !

Ces deux contrats incarnent les deux familles royales des suites discrètes :
- Les **suites arithmétiques**, gouvernées par l'**addition répétée**.
- Les **suites géométriques**, propulsées par la **multiplication répétée**.

---

### 2. Qu'est-ce qu'une suite numérique ?

#### 2.1 Définition et notations

Une fonction usuelle $f(x)$ accepte n'importe quel nombre réel : $x = 0$, $x = 1{,}5$, $x = \sqrt{2}$, $x = \pi$…
Une **suite** est beaucoup plus sobre : elle n'accepte que des **numéros d'ordre entiers** : $0, 1, 2, 3, 4\dots$

> **📐 Définition — Suite numérique.**
> Une **suite numérique** est une fonction dont l'ensemble de départ est l'ensemble des entiers naturels $\mathbb{N}$ (ou une partie de $\mathbb{N}$ débutant à un certain rang $n_0$).
> Pour tout entier naturel $n$, l'image de $n$ se note en **indice** :
> $$u_n \quad \text{(au lieu de } u(n)\text{)}.$$
> On lit à voix haute : « u indice n ».
> - $n$ est le **rang** (ou l'**indice**).
> - $u_n$ est le **terme de rang $n$** (ou terme général).
> - La suite tout entière se note entre parenthèses : $(u_n)$ ou $(u_n)_{n \in \mathbb{N}}$.

> **⚠️ Attention, piège ! Ne confonds jamais $u_n$ et $(u_n)$ !**
> - $u_n$ est un **nombre réel isolé** (par exemple $u_3 = 8$).
> - $(u_n)$ avec des parenthèses désigne **la suite tout entière**, la machine infinie qui engendre la liste $\{u_0, u_1, u_2, u_3, \dots\}$.

#### 2.2 Les deux modes d'engendrement

##### Mode 1 : La définition explicite ($u_n = f(n)$)
Le terme $u_n$ est exprimé directement en fonction de l'entier $n$.
*Exemple :* $u_n = 3n^2 - 1$.
- Pour calculer $u_0$, on remplace $n$ par 0 : $u_0 = 3(0)^2 - 1 = -1$.
- Pour calculer $u_{100}$, nul besoin de calculer les 99 termes précédents : $u_{100} = 3(100)^2 - 1 = 30\,000 - 1 = 29\,999$.

##### Mode 2 : La définition par récurrence ($u_{n+1} = g(u_n)$)
On donne :
1. Le **premier terme** pour ancrer la suite (par exemple $u_0 = 2$).
2. Une **règle de passage** qui explique comment fabriquer le terme suivant à partir du terme actuel : $u_{n+1} = g(u_n)$.
*Exemple :* $u_0 = 2$ et $u_{n+1} = 3u_n - 4$.
- $u_1 = 3u_0 - 4 = 3(2) - 4 = 2$.
- $u_2 = 3u_1 - 4 = 3(2) - 4 = 2$.
*(Ici la suite reste constante !)*

> **⚠️ Attention, piège ! Dans une suite récurrente, on avance de proche en proche.**
> Pour calculer $u_{10}$ avec une formule de récurrence, tu es obligé de calculer d'abord $u_1, u_2, u_3\dots$ jusqu'à $u_9$. C'est le principe des dominos : chaque domino fait tomber le suivant.

#### 2.3 Représentation graphique d'une suite

Puisque la variable $n$ ne prend que des valeurs entières ($0, 1, 2, 3\dots$), la représentation graphique d'une suite est un **nuage de points isolés** de coordonnées $(n\,; u_n)$.
Il ne faut **jamais relier ces points d'un trait plein**, car les nombres réels intermédiaires (comme $n = 1{,}5$) n'ont aucun sens pour une suite !

```
         un ▲
            │                     o (3, u3)
            │           o (2, u2)
            │
            │  o (1, u1)
            │
          o ┼ (0, u0)
            │
          O ┼───┼───────┼───────┼───────► n
            0   1       2       3
```

---

### 3. Les suites arithmétiques : l'escalier régulier

#### 3.1 Définition et terme général

> **📐 Définition — Suite arithmétique.**
> Une suite $(u_n)$ est dite **arithmétique** s'il existe un nombre réel fixe $r$, appelé la **raison**, tel que pour tout entier naturel $n$ :
> $$\boxed{u_{n+1} = u_n + r}$$

Pour passer d'une marche à la suivante, on ajoute toujours le même nombre $r$ :
- $u_1 = u_0 + r$
- $u_2 = u_1 + r = (u_0 + r) + r = u_0 + 2r$
- $u_3 = u_2 + r = (u_0 + 2r) + r = u_0 + 3r$

En continuant ainsi jusqu'au rang $n$ :

> **📐 Théorème — Formule explicite du terme général.**
> Si $(u_n)$ est une suite arithmétique de premier terme $u_0$ et de raison $r$, alors pour tout $n \in \mathbb{N}$ :
> $$\boxed{u_n = u_0 + nr}$$
> Si le premier terme est $u_p$ (au rang $p$), la formule devient :
> $$u_n = u_p + (n - p)r.$$

**Remarque :**
Les points d'une suite arithmétique sont tous alignés sur la droite d'équation $y = rx + u_0$. La raison $r$ joue exactement le rôle du coefficient directeur (la pente) !
- Si $r > 0$ : la suite est **strictement croissante**.
- Si $r < 0$ : la suite est **strictement décroissante**.
- Si $r = 0$ : la suite est **constante**.

#### 3.2 L'escalier de Gauss : somme des entiers consécutifs

En 1784, dans une école de Brunswick en Allemagne, un maître d'école fatigué ordonne à ses élèves de sept ans d'additionner tous les nombres de $1$ à $100$ :
$$S = 1 + 2 + 3 + 4 + \dots + 99 + 100.$$
Le maître espère avoir la paix pendant une heure. Mais au bout de quelques secondes, un jeune garçon pose son ardoise sur le pupitre en disant : *« Ligget se ! »* (« La voici ! »). Le résultat inscrit était $5\,050$, parfaitement exact.

Cet enfant s'appelait **Carl Friedrich Gauss**.

```
    1   +   2   +   3   + ... +  98  +  99  + 100
  100   +  99   +  98   + ... +   3  +   2  +   1
  ────────────────────────────────────────────────
  101   + 101   + 101   + ... + 101  + 101  + 101   (100 fois la somme 101 !)
```

> **✍️ Démonstration (exigible) — Somme des $n$ premiers entiers.**
> Pour tout entier naturel $n \ge 1$ :
> $$\boxed{1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}}$$
> 
> *Preuve :*
> Écrivons la somme $S_n$ dans l'ordre croissant, puis juste en dessous dans l'ordre décroissant :
> $$S_n = 1 + 2 + 3 + \dots + (n-1) + n$$
> $$S_n = n + (n-1) + (n-2) + \dots + 2 + 1$$
> Additionnons les deux lignes colonne par colonne :
> $$2S_n = (1 + n) + (2 + n - 1) + (3 + n - 2) + \dots + (n + 1).$$
> Chaque paire entre parenthèses vaut exactement $n + 1$.
> Combien y a-t-il de colonnes ? Il y en a exactement $n$.
> Donc :
> $$2S_n = n \times (n + 1) \implies S_n = \frac{n(n + 1)}{2}. \quad \blacksquare$$

Pour $n = 100$ : $S_{100} = \frac{100 \times 101}{2} = 50 \times 101 = 5\,050$.

#### 3.3 Somme des termes consécutifs d'une suite arithmétique

> **📐 Théorème général — Somme arithmétique.**
> Pour toute suite arithmétique :
> $$\boxed{S = \sum_{k=p}^n u_k = u_p + u_{p+1} + \dots + u_n = (\text{nombre de termes}) \times \frac{\text{premier terme} + \text{dernier terme}}{2}}$$
> où le nombre de termes est donné par : $\text{dernier indice} - \text{premier indice} + 1 = n - p + 1$.

---

### 4. Les suites géométriques : le vertige de la multiplication

#### 4.1 Définition et terme général

> **📐 Définition — Suite géométrique.**
> Une suite $(u_n)$ est dite **géométrique** s'il existe un nombre réel fixe $q$, appelé la **raison**, tel que pour tout entier naturel $n$ :
> $$\boxed{u_{n+1} = q \times u_n}$$

Pour passer d'un terme au suivant, on multiplie toujours par le même nombre $q$ :
- $u_1 = q \times u_0$
- $u_2 = q \times u_1 = q \times (q u_0) = u_0 \times q^2$
- $u_3 = q \times u_2 = u_0 \times q^3$

> **📐 Théorème — Formule explicite du terme général.**
> Si $(u_n)$ est une suite géométrique de premier terme $u_0$ et de raison $q$, alors pour tout $n \in \mathbb{N}$ :
> $$\boxed{u_n = u_0 \times q^n}$$
> Si le premier terme est $u_p$ (au rang $p$), la formule devient :
> $$u_n = u_p \times q^{n-p}.$$

#### 4.2 L'échiquier de Sissa et l'explosion exponentielle

Le sage indien Sissa inventa le jeu d'échecs pour divertir son roi. Ravi, le monarque lui proposa la récompense de son choix. Sissa répondit modestement :
> « Seigneur, déposez un grain de blé sur la première case, deux sur la deuxième, quatre sur la troisième, huit sur la quatrième, et doublez ainsi sur chaque case jusqu'à la 64ᵉ case de l'échiquier. »

Le roi sourit de cette demande apparemment dérisoire. Mais ses intendants revinrent pâles comme la mort :
- Case 1 : $u_0 = 1 = 2^0$
- Case 2 : $u_1 = 2 = 2^1$
- Case 3 : $u_2 = 4 = 2^2$
- Case 64 : $u_{63} = 2^{63} \approx 9{,}22 \times 10^{18}$ grains !

Le nombre total de grains sur l'échiquier vaut :
$$S = 1 + 2 + 4 + \dots + 2^{63} = 2^{64} - 1 \approx 18{,}4 \times 10^{18}\text{ grains}.$$
Cela représente plus de $1\,200$ milliards de tonnes de blé, soit la production mondiale actuelle de blé pendant plus de deux mille ans ! Le roi ne pouvait pas honorer sa promesse.

#### 4.3 Somme des puissances consécutives d'un nombre $q$

> **✍️ Démonstration (exigible) — Somme des puissances de $q$.**
> Pour tout réel $q \neq 1$ et tout entier $n \ge 0$ :
> $$\boxed{1 + q + q^2 + q^3 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}}$$
> 
> *Preuve (par la méthode du télescopage) :*
> Posons $S_n = 1 + q + q^2 + \dots + q^n$.
> Multiplions les deux membres par $q$ :
> $$q S_n = q(1 + q + q^2 + \dots + q^n) = q + q^2 + q^3 + \dots + q^{n+1}.$$
> Soustrayons maintenant cette ligne à la ligne d'origine ($S_n - qS_n$) :
> $$S_n - qS_n = (1 + q + q^2 + \dots + q^n) - (q + q^2 + q^3 + \dots + q^{n+1}).$$
> Regarde l'effet magique : tous les termes intermédiaires s'annulent deux à deux en diagonale !
> Seuls survivent le tout premier terme ($1$) et le tout dernier ($-q^{n+1}$) :
> $$S_n(1 - q) = 1 - q^{n+1}.$$
> Puisque $q \neq 1$, on peut diviser par $1 - q$ :
> $$S_n = \frac{1 - q^{n+1}}{1 - q}. \quad \blacksquare$$

> **📐 Théorème général — Somme géométrique.**
> Pour toute suite géométrique de raison $q \neq 1$ :
> $$\boxed{S = (\text{premier terme}) \times \frac{1 - q^{\text{nombre de termes}}}{1 - q}}$$

---

### 5. Variations et intuition de la limite

#### 5.1 Les trois méthodes pour étudier les variations d'une suite

Pour savoir si une suite monte ($u_{n+1} \ge u_n$) ou descend ($u_{n+1} \le u_n$) :

1. **Méthode 1 : Étudier le signe de la différence $u_{n+1} - u_n$ (Méthode universelle).**
   - Si pour tout $n$, $u_{n+1} - u_n > 0$, la suite $(u_n)$ est strictement croissante.
   - Si pour tout $n$, $u_{n+1} - u_n < 0$, la suite $(u_n)$ est strictement décroissante.

2. **Méthode 2 : Comparer le quotient $\frac{u_{n+1}}{u_n}$ avec $1$ (uniquement si tous les termes sont strictement positifs !).**
   - Si $\frac{u_{n+1}}{u_n} > 1$, la suite est strictement croissante.
   - Si $\frac{u_{n+1}}{u_n} < 1$, la suite est strictement décroissante.

3. **Méthode 3 : Passer par la fonction associée si $u_n = f(n)$.**
   Si la fonction $f$ est croissante sur $[0\,; +\infty[$, alors la suite $u_n = f(n)$ est croissante.

#### 5.2 Limite d'une suite géométrique selon la raison $q$

Que devient $q^n$ lorsque $n$ devient gigantesque ($n \to +\infty$) ?

- **Si $q > 1$ :** La suite explose vers l'infini : $\lim_{n \to +\infty} q^n = +\infty$. (Exemple : $2^n$).
- **Si $q = 1$ :** La suite est constante égale à 1.
- **Si $-1 < q < 1$ :** La suite s'écrase vers zéro : $\lim_{n \to +\infty} q^n = 0$. (Exemple : $\left(\frac{1}{2}\right)^n \to 0$).
- **Si $q \le -1$ :** La suite oscille sans admettre de limite (Exemple : $(-1)^n = 1, -1, 1, -1\dots$).

---

### 6. En informatique : l'algorithme de seuil en Python

Un problème fondamental en gestion, en biologie et en physique consiste à savoir **à quel rang $n$** une suite dépasse une valeur critique donnée (le seuil). On utilise pour cela une boucle `while` (tant que) :

```python
def seuil_croissance(valeur_initiale, taux, seuil):
    """
    Calcule le nombre d'années nécessaires pour dépasser un seuil.
    Exemple : un capital initial de 1000 € placé à 5 % par an (raison q = 1.05)
    doit dépasser 2000 € (doubler).
    """
    n = 0
    u = valeur_initiale
    
    while u < seuil:
        u = u * (1 + taux)  # On applique le taux annuel
        n += 1              # On passe à l'année suivante
        
    return n, round(u, 2)

annees, montant_final = seuil_croissance(1000, 0.05, 2000)
print(f"Le capital aura doublé au bout de {annees} ans, atteignant {montant_final} €.")
# Affiche : Le capital aura doublé au bout de 15 ans, atteignant 2078.93 €.
```

---

### 7. Exemples résolus détaillés

> **Exemple résolu 1 — Reconstitution d'une suite arithmétique.**
> Soit $(u_n)$ une suite arithmétique telle que $u_4 = 17$ et $u_9 = 37$.
> 1. Déterminer la raison $r$ et le premier terme $u_0$.
> 2. Exprimer $u_n$ en fonction de $n$.
> 3. Calculer la valeur de $u_{50}$.
>
> **Solution :**
> 1. Selon la formule du terme général : $u_9 = u_4 + (9 - 4)r$.
>    $$37 = 17 + 5r \iff 5r = 37 - 17 = 20 \iff r = \frac{20}{5} = 4.$$
>    Pour trouver $u_0$, on utilise $u_4 = u_0 + 4r$ :
>    $$17 = u_0 + 4(4) \iff 17 = u_0 + 16 \iff u_0 = 1.$$
> 2. Le terme général est donc : $\boxed{u_n = 1 + 4n}$.
> 3. Pour $n = 50$ : $u_{50} = 1 + 4(50) = 1 + 200 = 201$.

> **Exemple résolu 2 — Calcul d'une somme arithmétique de termes.**
> Calculer la somme :
> $$S = 7 + 11 + 15 + 19 + \dots + 123.$$
>
> **Solution :**
> Les termes progressent de $+4$ en $+4$ : c'est une suite arithmétique de raison $r = 4$, de premier terme $u_0 = 7$.
> Le terme général est $u_n = 7 + 4n$.
> Trouvons le rang du dernier terme $123$ :
> $$7 + 4n = 123 \iff 4n = 116 \iff n = 29.$$
> Les termes vont de $u_0$ à $u_{29}$ : il y a donc $29 - 0 + 1 = 30\text{ termes}$.
> Appliquons la formule de la somme arithmétique :
> $$S = (\text{nombre de termes}) \times \frac{\text{premier} + \text{dernier}}{2} = 30 \times \frac{7 + 123}{2} = 30 \times \frac{130}{2} = 30 \times 65 = 1\,950.$$

> **Exemple résolu 3 — Suite géométrique et somme de puissances.**
> Soit $(v_n)$ la suite géométrique de premier terme $v_0 = 5$ et de raison $q = 3$.
> 1. Calculer $v_1, v_2$ et $v_6$.
> 2. Calculer la somme $S = v_0 + v_1 + v_2 + \dots + v_6$.
>
> **Solution :**
> 1. $v_1 = 5 \times 3 = 15$.
>    $v_2 = 15 \times 3 = 45$.
>    Formule générale : $v_n = 5 \times 3^n$.
>    Pour $n = 6$ : $v_6 = 5 \times 3^6 = 5 \times 729 = 3\,645$.
> 2. Nombre de termes de $v_0$ à $v_6$ : $6 - 0 + 1 = 7\text{ termes}$.
>    $$S = v_0 \times \frac{1 - q^7}{1 - q} = 5 \times \frac{1 - 3^7}{1 - 3} = 5 \times \frac{1 - 2\,187}{-2} = 5 \times \frac{-2\,186}{-2} = 5 \times 1\,093 = 5\,465.$$

> **Exemple résolu 4 — Étude du sens de variation d'une suite.**
> Déterminer le sens de variation des suites suivantes :
> a) $u_n = \frac{n}{n + 1}$ pour $n \in \mathbb{N}$ \quad b) $v_n = \frac{3^n}{n!}$ pour $n \ge 1$
>
> **Solution :**
> a) Étudions le signe de la différence $u_{n+1} - u_n$ :
>    $$u_{n+1} - u_n = \frac{n + 1}{(n + 1) + 1} - \frac{n}{n + 1} = \frac{n + 1}{n + 2} - \frac{n}{n + 1}.$$
>    Mettons au même dénominateur $(n + 2)(n + 1) > 0$ :
>    $$u_{n+1} - u_n = \frac{(n + 1)^2 - n(n + 2)}{(n + 2)(n + 1)} = \frac{n^2 + 2n + 1 - (n^2 + 2n)}{(n + 2)(n + 1)} = \frac{1}{(n + 2)(n + 1)}.$$
>    Le numérateur est $1 > 0$ et le dénominateur est strictement positif pour tout $n \in \mathbb{N}$.
>    Donc $u_{n+1} - u_n > 0$ pour tout $n$ : la suite $(u_n)$ est **strictement croissante**.
>
> b) Tous les termes de la suite $v_n$ sont strictement positifs. Comparons le quotient $\frac{v_{n+1}}{v_n}$ à 1 :
>    $$\frac{v_{n+1}}{v_n} = \frac{\frac{3^{n+1}}{(n+1)!}}{\frac{3^n}{n!}} = \frac{3^{n+1}}{3^n} \times \frac{n!}{(n+1)!} = 3 \times \frac{n!}{(n+1)n!} = \frac{3}{n + 1}.$$
>    - Si $n = 1$ : $\frac{v_2}{v_1} = \frac{3}{2} > 1$ (la suite commence par augmenter : $v_1 = 3, v_2 = 4{,}5$).
>    - Si $n = 2$ : $\frac{v_3}{v_2} = \frac{3}{3} = 1$ ($v_3 = v_2 = 4{,}5$).
>    - Dès que $n \ge 3$ : $n + 1 \ge 4$, donc $\frac{3}{n+1} < 1$, ce qui implique $v_{n+1} < v_n$.
>    La suite $(v_n)$ est **strictement décroissante à partir du rang $n = 2$**.

> **Exemple résolu 5 — Suite arithmético-géométrique.**
> Un refuge pour animaux compte $200$ bêtes au 1ᵉʳ janvier 2025. Chaque année, $20\ \%$ des animaux sont adoptés et quittent le refuge, mais $50$ nouveaux animaux abandonnés sont recueillis.
> On note $u_n$ le nombre d'animaux au bout de $n$ années.
> 1. Établir la relation de récurrence liant $u_{n+1}$ et $u_n$.
> 2. On pose $v_n = u_n - 250$. Démontrer que $(v_n)$ est une suite géométrique.
> 3. En déduire l'expression de $u_n$ en fonction de $n$, puis la limite de $u_n$ lorsque $n \to +\infty$.
>
> **Solution :**
> 1. Si $20\ \%$ des animaux partent, il en reste $80\ \%$, soit une multiplication par $0{,}8$. En ajoutant les 50 nouveaux :
>    $$u_0 = 200 \quad \text{et} \quad u_{n+1} = 0{,}8u_n + 50.$$
> 2. Exprimons $v_{n+1}$ en fonction de $v_n$ :
>    $$v_{n+1} = u_{n+1} - 250 = (0{,}8u_n + 50) - 250 = 0{,}8u_n - 200.$$
>    Factorisons $0{,}8$ :
>    $$v_{n+1} = 0{,}8(u_n - 250) = 0{,}8 v_n.$$
>    La suite $(v_n)$ est une **suite géométrique de raison $q = 0{,}8$** et de premier terme :
>    $$v_0 = u_0 - 250 = 200 - 250 = -50.$$
> 3. D'après le cours : $v_n = v_0 \times q^n = -50 \times (0{,}8)^n$.
>    Comme $u_n = v_n + 250$, on en déduit :
>    $$\boxed{u_n = 250 - 50 \times (0{,}8)^n}.$$
>    Puisque $-1 < 0{,}8 < 1$, on a $\lim_{n \to +\infty} (0{,}8)^n = 0$.
>    Par conséquent :
>    $$\lim_{n \to +\infty} u_n = 250 - 50 \times 0 = 250.$$
>    La population du refuge se stabilisera à long terme autour de $250$ animaux.

> **Exemple résolu 6 — Représentation en toile d'araignée d'une suite récurrente.**
> Soit la suite récurrente définie par $u_0 = 0$ et $u_{n+1} = \frac{1}{2}u_n + 1$.
> Représenter graphiquement les quatre premiers termes sur un repère orthonormé avec la droite $y = x$.
>
> **Solution et méthode :**
> On trace dans un repère la droite d'équation $y = x$ (la diagonale) et la droite représentative de la fonction $g(x) = \frac{1}{2}x + 1$.
> 1. On part de $u_0 = 0$ sur l'axe des abscisses.
> 2. On monte verticalement jusqu'à la droite $y = g(x)$ : le point atteint a pour ordonnée $g(u_0) = u_1 = 1$.
> 3. On se déplace horizontalement jusqu'à la droite $y = x$ : ce déplacement reporte la valeur $u_1 = 1$ sur l'axe des abscisses sans refaire de calcul !
> 4. On monte à nouveau verticalement jusqu'à la droite $y = g(x)$ pour trouver $u_2 = g(1) = 1{,}5$.
> 5. On repart horizontalement vers $y = x$, puis verticalement vers la courbe pour trouver $u_3 = g(1{,}5) = 1{,}75$.
> Les segments successifs forment un « escalier » qui converge vers le point d'intersection des deux droites :
> $$x = \frac{1}{2}x + 1 \iff \frac{1}{2}x = 1 \iff x = 2.$$
> La suite $(u_n)$ croît en se rapprochant de sa limite $L = 2$.

---

### Ce qu'il faut retenir

1. **Suite :** fonction indexée par les entiers $n \in \mathbb{N}$. Terme $u_n$, suite $(u_n)$.
2. **Définition explicite vs récurrente :**
   - Explicite : $u_n = f(n)$ (accès direct).
   - Récurrente : $u_0$ et $u_{n+1} = g(u_n)$ (calcul pas à pas).
3. **Suites arithmétiques :**
   - Définition : $u_{n+1} = u_n + r$.
   - Terme général : $u_n = u_0 + nr$ (ou $u_n = u_p + (n-p)r$).
   - Somme de Gauss : $1 + 2 + \dots + n = \frac{n(n+1)}{2}$.
   - Somme générale : $(\text{nb de termes}) \times \frac{\text{premier} + \text{dernier}}{2}$.
4. **Suites géométriques :**
   - Définition : $u_{n+1} = q \times u_n$.
   - Terme général : $u_n = u_0 \times q^n$ (ou $u_n = u_p \times q^{n-p}$).
   - Somme de puissances : $1 + q + q^2 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$).
   - Somme générale : $(\text{premier}) \times \frac{1 - q^{\text{nb de termes}}}{1 - q}$.
5. **Variations :** signe de $u_{n+1} - u_n$ ou quotient $\frac{u_{n+1}}{u_n}$ comparé à 1.
6. **Limite géométrique :** si $|q| < 1$, alors $q^n \to 0$. Si $q > 1$, alors $q^n \to +\infty$.

---

### Exercices

#### Exercices d'application directe (★)

1. Soit la suite explicite $u_n = 2n^2 - 3$. Calculer $u_0, u_1, u_2$ et $u_{10}$.
2. Soit la suite récurrente $v_0 = 4$ et $v_{n+1} = 2v_n - 3$. Calculer $v_1, v_2$ et $v_3$.
3. Une suite arithmétique a pour premier terme $u_0 = 5$ et pour raison $r = 3$. Donner l'expression de $u_n$, puis calculer $u_{20}$.
4. Une suite géométrique a pour premier terme $v_0 = 3$ et pour raison $q = 2$. Donner l'expression de $v_n$, puis calculer $v_8$.
5. Calculer la somme des entiers de $1$ à $50$ : $S = 1 + 2 + 3 + \dots + 50$.
6. Calculer la somme géométrique : $S = 1 + 2 + 4 + 8 + \dots + 2^{10}$.
7. La suite $u_n = 5 - 4n$ est-elle arithmétique ? Préciser sa raison et son sens de variation.
8. La suite $v_n = 7 \times 0{,}6^n$ est-elle géométrique ? Préciser sa raison et sa limite quand $n \to +\infty$.
9. Déterminer le sens de variation de la suite $u_n = 3n + 7$.
10. Soit une suite arithmétique telle que $u_3 = 10$ et $u_5 = 16$. Trouver la raison $r$.

#### Exercices d'entraînement et de réflexion (★★)

11. On considère la suite arithmétique $(u_n)$ telle que $u_2 = 11$ et $u_7 = 36$.
    a) Calculer la raison $r$ et le terme initial $u_0$.
    b) À partir de quel rang $n$ a-t-on $u_n > 1\,000$ ?
12. Calculer la somme : $S = 12 + 15 + 18 + 21 + \dots + 150$.
13. On place un capital de $5\,000\text{ €}$ sur un compte à intérêts composés au taux annuel de $4\ \%$.
    On note $C_n$ la valeur du capital après $n$ années.
    a) Exprimer $C_{n+1}$ en fonction de $C_n$, puis $C_n$ en fonction de $n$.
    b) Quel sera le capital disponible au bout de 10 ans ?
    c) Écrire un script Python pour trouver au bout de combien d'années le capital aura dépassé $8\,000\text{ €}$.
14. Déterminer le sens de variation de la suite $u_n = \frac{2^n}{n}$ pour $n \ge 1$.
15. Déterminer le sens de variation de la suite $w_n = n^2 - 10n + 3$ pour $n \in \mathbb{N}$.
16. Calculer la somme des puissances de 3 : $S = 1 + 3 + 9 + 27 + \dots + 3^7$.
17. Soit la suite récurrente définie par $u_0 = 1$ et $u_{n+1} = \sqrt{u_n + 2}$.
    a) Calculer $u_1$ et $u_2$ sous forme exacte et approchée.
    b) Déterminer graphiquement la valeur vers laquelle semble converger cette suite en cherchant le point fixe de $f(x) = \sqrt{x + 2}$.
18. Soit $(u_n)$ une suite géométrique positive telle que $u_1 = 6$ et $u_3 = 24$.
    Déterminer la raison $q$, le premier terme $u_0$ et calculer la somme $u_0 + u_1 + \dots + u_8$.

#### Exercices d'approfondissement et défis (★★★)

19. **Le paradoxe du flocon de Koch.**
    Le flocon de neige de Koch est une fractale obtenue en partant d'un triangle équilatéral de côté 1 (étape 0). À chaque étape, on remplace le tiers central de chaque côté par un triangle équilatéral pointant vers l'extérieur.
    - Étape 0 : nombre de côtés $N_0 = 3$, longueur d'un côté $\ell_0 = 1$.
    - À l'étape $n+1$, chaque segment est divisé en 4 segments de longueur 3 fois plus petite.
    a) Exprimer le nombre de côtés $N_n$ en fonction de $n$.
    b) Exprimer la longueur $\ell_n$ d'un côté en fonction de $n$.
    c) En déduire le périmètre $P_n = N_n \times \ell_n$ du flocon à l'étape $n$.
    d) Quelle est la limite du périmètre quand $n \to +\infty$ ?
20. **Somme des carrés des entiers.**
    On cherche à démontrer que :
    $$1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}.$$
    a) Vérifier cette formule pour $n = 1, 2, 3$.
    b) En développant $(k + 1)^3 - k^3 = 3k^2 + 3k + 1$, sommer cette égalité pour $k$ allant de $1$ à $n$ et en déduire la formule.
21. **Le paradoxe d'Achille et la tortue revisité.**
    La tortue part avec $100\text{ mètres}$ d'avance sur Achille. Achille court à $10\text{ m/s}$ et la tortue avance à $1\text{ m/s}$.
    - Pour franchir les $100\text{ m}$, Achille met $t_0 = 10\text{ s}$. Pendant ce temps, la tortue a avancé de $10\text{ m}$.
    - Pour franchir ces $10\text{ m}$, Achille met $t_1 = 1\text{ s}$. La tortue a avancé de $1\text{ m}$.
    - Pour franchir ce mètre, Achille met $t_2 = 0{,}1\text{ s}$, etc.
    a) Exprimer le temps $t_n$ de la $n$-ième étape. Quelle est la nature de la suite $(t_n)$ ?
    b) Calculer le temps total $T_n = t_0 + t_1 + \dots + t_n$ au bout de $n$ étapes.
    c) Quelle est la limite de $T_n$ quand $n \to +\infty$ ? Achille dépasse-t-il la tortue ?
22. **La suite de Fibonacci et le nombre d'or.**
    On définit la célèbre suite de Fibonacci par $F_0 = 0, F_1 = 1$ et pour tout $n \in \mathbb{N}$ :
    $$F_{n+2} = F_{n+1} + F_n.$$
    a) Calculer les dix premiers termes $F_0, F_1, F_2, \dots, F_9$.
    b) On considère le rapport $r_n = \frac{F_{n+1}}{F_n}$ pour $n \ge 1$. Calculer $r_1, r_2, r_3, r_4, r_5$.
    c) Vers quelle valeur remarquable ce rapport semble-t-il se rapprocher ?

---

### Solutions

1. $u_0 = -3$. $u_1 = 2(1) - 3 = -1$. $u_2 = 2(4) - 3 = 5$. $u_{10} = 2(100) - 3 = 197$.
2. $v_1 = 2(4) - 3 = 5$. $v_2 = 2(5) - 3 = 7$. $v_3 = 2(7) - 3 = 11$.
3. $u_n = 5 + 3n$. $u_{20} = 5 + 3(20) = 65$.
4. $v_n = 3 \times 2^n$. $v_8 = 3 \times 256 = 768$.
5. $S = \frac{50 \times 51}{2} = 25 \times 51 = 1\,275$.
6. $S = \frac{1 - 2^{11}}{1 - 2} = \frac{1 - 2\,048}{-1} = 2\,047$.
7. $u_{n+1} - u_n = [5 - 4(n+1)] - [5 - 4n] = -4$. C'est une suite arithmétique de raison $r = -4$. Comme $r < 0$, elle est strictement décroissante.
8. $v_{n+1} = 7 \times 0{,}6^{n+1} = 0{,}6 \times (7 \times 0{,}6^n) = 0{,}6 v_n$. Suite géométrique de raison $q = 0{,}6$. Comme $|0{,}6| < 1$, $\lim_{n \to +\infty} v_n = 0$.
9. $u_{n+1} - u_n = [3(n+1) + 7] - [3n + 7] = 3 > 0$. Strictement croissante.
10. $u_5 = u_3 + 2r \iff 16 = 10 + 2r \iff 2r = 6 \iff r = 3$.
11. a) $u_7 = u_2 + 5r \iff 36 = 11 + 5r \iff 5r = 25 \iff r = 5$.
       $u_2 = u_0 + 2r \iff 11 = u_0 + 10 \iff u_0 = 1$. Terme général : $u_n = 1 + 5n$.
    b) $1 + 5n > 1\,000 \iff 5n > 999 \iff n > 199{,}8$. À partir du rang $n = 200$.
12. Suite arithmétique de raison $r = 3$. $u_0 = 12$, $u_n = 12 + 3n = 150 \iff 3n = 138 \iff n = 46$.
    Nombre de termes : $46 - 0 + 1 = 47\text{ termes}$.
    $S = 47 \times \frac{12 + 150}{2} = 47 \times 81 = 3\,807$.
13. a) Augmenter de $4\ \%$ revient à multiplier par $1{,}04$. $C_{n+1} = 1{,}04 C_n$.
       $C_n = 5\,000 \times (1{,}04)^n$.
    b) $C_{10} = 5\,000 \times (1{,}04)^{10} \approx 5\,000 \times 1{,}48024 \approx 7\,401{,}22\text{ €}$.
    c) Script Python :
       ```python
       n, c = 0, 5000
       while c <= 8000:
           c *= 1.04
           n += 1
       print(n)  # Affiche 12 ans (c ≈ 8005.16 €)
       ```
14. $u_n > 0$ pour tout $n \ge 1$.
    $\frac{u_{n+1}}{u_n} = \frac{2^{n+1}}{n+1} \times \frac{n}{2^n} = 2 \times \frac{n}{n+1} = \frac{2n}{n+1}$.
    Comparons à 1 : $\frac{2n}{n+1} > 1 \iff 2n > n + 1 \iff n > 1$.
    Pour $n = 1$ : $u_1 = 2, u_2 = 2 \implies u_1 = u_2$.
    Pour tout $n \ge 2$, $\frac{u_{n+1}}{u_n} > 1$, donc la suite $(u_n)$ est strictement croissante à partir de $n = 2$.
15. $w_{n+1} - w_n = [(n+1)^2 - 10(n+1) + 3] - [n^2 - 10n + 3] = n^2 + 2n + 1 - 10n - 10 + 3 - n^2 + 10n - 3 = 2n - 9$.
    - Si $n \le 4$ : $2n - 9 < 0$, la suite décroît ($w_0 = 3, w_1 = -6, w_2 = -13, w_3 = -18, w_4 = -21, w_5 = -22$).
    - Si $n \ge 5$ : $2n - 9 > 0$, la suite est strictement croissante.
16. $S = \frac{1 - 3^8}{1 - 3} = \frac{1 - 6\,561}{-2} = \frac{-6\,560}{-2} = 3\,280$.
17. a) $u_1 = \sqrt{1 + 2} = \sqrt{3} \approx 1{,}732$. $u_2 = \sqrt{\sqrt{3} + 2} \approx \sqrt{3{,}732} \approx 1{,}932$.
    b) Point fixe : $x = \sqrt{x + 2} \implies x^2 = x + 2 \iff x^2 - x - 2 = 0 \iff (x - 2)(x + 1) = 0$.
       Comme $x \ge 0$, la solution est $x = 2$. La suite converge vers $2$.
18. $u_3 = u_1 \times q^2 \iff 24 = 6q^2 \iff q^2 = 4 \implies q = 2$ (la suite étant positive).
    $u_1 = u_0 \times q \iff 6 = 2u_0 \iff u_0 = 3$.
    Nombre de termes de $u_0$ à $u_8$ : 9 termes.
    $S = 3 \times \frac{1 - 2^9}{1 - 2} = 3 \times \frac{1 - 512}{-1} = 3 \times 511 = 1\,533$.
19. a) À chaque étape, chaque côté est remplacé par 4 segments : $N_n = 3 \times 4^n$.
    b) La longueur d'un segment est divisée par 3 : $\ell_n = \left(\frac{1}{3}\right)^n$.
    c) Périmètre : $P_n = N_n \times \ell_n = 3 \times 4^n \times \frac{1}{3^n} = 3 \times \left(\frac{4}{3}\right)^n$.
    d) Comme $\frac{4}{3} > 1$, $\lim_{n \to +\infty} \left(\frac{4}{3}\right)^n = +\infty$, donc $\lim_{n \to +\infty} P_n = +\infty$.
    Le flocon de Koch enferme une aire finie à l'intérieur d'un périmètre infini !
20. a) Pour $n = 1$ : $1^2 = 1$ et $\frac{1 \times 2 \times 3}{6} = 1$.
       Pour $n = 2$ : $1 + 4 = 5$ et $\frac{2 \times 3 \times 5}{6} = 5$.
       Pour $n = 3$ : $1 + 4 + 9 = 14$ et $\frac{3 \times 4 \times 7}{6} = 14$.
    b) En sommant $(k+1)^3 - k^3$ de $k=1$ à $n$, par télescopage la somme vaut $(n+1)^3 - 1$.
       D'autre part, la somme vaut $3\sum k^2 + 3\sum k + \sum 1 = 3\sum k^2 + 3\frac{n(n+1)}{2} + n$.
       On isole $\sum k^2$ :
       $3\sum k^2 = (n+1)^3 - 1 - \frac{3n(n+1)}{2} - n = (n+1)[(n+1)^2 - 1] - \frac{3n(n+1)}{2} = (n+1)n(n+2) - \frac{3n(n+1)}{2} = n(n+1)\left(n + 2 - \frac{3}{2}\right) = n(n+1)\left(\frac{2n+1}{2}\right)$.
       En divisant par 3 : $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.
21. a) $t_n = 10 \times (0{,}1)^n$. C'est une suite géométrique de premier terme $t_0 = 10$ et de raison $q = 0{,}1$.
    b) $T_n = 10 \times \frac{1 - (0{,}1)^{n+1}}{1 - 0{,}1} = 10 \times \frac{1 - (0{,}1)^{n+1}}{0{,}9} = \frac{100}{9}\left[1 - (0{,}1)^{n+1}\right]$.
    c) Comme $|0{,}1| < 1$, $(0{,}1)^{n+1} \to 0$.
       $\lim_{n \to +\infty} T_n = \frac{100}{9} \approx 11{,}11\text{ secondes}$.
       Le paradoxe de Zénon d'Élée est résolu : une somme infinie d'intervalles de temps peut avoir une durée totale finie ! Au bout de $11{,}11\text{ s}$, Achille dépasse la tortue.
22. a) $F_0 = 0, F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, F_6 = 8, F_7 = 13, F_8 = 21, F_9 = 34$.
    b) $r_1 = \frac{1}{1} = 1$ ; $r_2 = \frac{2}{1} = 2$ ; $r_3 = \frac{3}{2} = 1{,}5$ ; $r_4 = \frac{5}{3} \approx 1{,}667$ ; $r_5 = \frac{8}{5} = 1{,}6$.
    c) Le rapport oscille et se rapproche du **nombre d'or** $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1{,}6180339887\dots$

---

### La question qui ouvre la suite

Dans ce chapitre, nous avons vu des suites avancer par bonds discrets, et nous avons calculé des grandeurs qui tournent ou qui oscillent. Mais imagine maintenant une roue de fête foraine qui tourne sans fin, ou une vague qui monte et redescend avec une régularité parfaite.

Comment mesurer les angles non plus en degrés rigides, mais en déroulant un ruban souple sur un cercle de rayon 1 ? Comment le cosinus et le sinus, découverts dans les triangles rectangles du collège, deviennent-ils les battements d'ondes qui décrivent le son, la lumière et le courant alternatif ? C'est ce que nous allons découvrir dans **La Grande Roue et le Cercle qui s'Enroule**.
