# VOLUME VI — L'ÂGE DU FLUX ET DE LA VITESSE (17 - 18 ans / Terminale spécialité + Maths expertes)
## CHAPITRE 56 : Les Messages Secrets et l'Horloge des Restes

> *« Sur le cadran d'une montre, après midi ne vient pas treize heures : l'aiguille revient à une heure. Cette arithmétique circulaire, que tout enfant pratique sans le savoir, est l'un des joyaux les plus profonds de l'esprit humain. C'est en étudiant les restes des divisions que Fermat perça le secret des puissances, et que trois siècles plus tard, l'humanité entière apprit à verrouiller ses secrets numériques derrière le cadenas indestructible des nombres premiers. »*

---

### Ce que tu vas découvrir

- La structure rigoureuse de la **divisibilité dans $\mathbb{Z}$** et de la **division euclidienne**.
- Le monde fascinant des **congruences modulo $n$** : l'arithmétique circulaire où les nombres s'enroulent sur un cercle.
- L'**algorithme d'Euclide étendu**, le **théorème de Bézout** et la résolution méthodique des **équations diophantiennes** $ax + by = c$.
- Le **théorème de Gauss**, pilier de l'arithmétique, et sa démonstration exigible.
- Le **Petit Théorème de Fermat** et la méthode d'**exponentiation modulaire rapide**.
- L'aventure du cryptage : du chiffre de César et du chiffrement affine jusqu'au protocole asymétrique **RSA**, bouclier de l'Internet moderne.

---

### 1. Le problème : Envoyer un secret aux yeux de tous

#### 1.1 Le coursier de César et la faiblesse de la clé partagée
Vers l'an 50 avant notre ère, Jules César envoie des ordres militaires à ses légions en Gaule. Pour éviter qu'un messager intercepté ne livre ses plans, il décale chaque lettre de 3 rangs dans l'alphabet :
- A devient D, B devient E... X devient A, Y devient B, Z devient C.
Le destinataire effectue le décalage inverse (-3).

Ce procédé présente une faille béante : quiconque connaît la règle peut déchiffrer tous les messages. Même en compliquant la formule (chiffrement affine), l'analyse des fréquences des lettres (le 'E' étant la lettre la plus fréquente en français) brise le code en quelques minutes.

Mais le problème fondamental de la cryptographie classique est encore plus grave : **le problème de l'échange de la clé**.
Si Alice et Bob veulent échanger des secrets, ils doivent d'abord convenir ensemble d'une clé secrète. Mais comment peuvent-ils convenir de cette clé sans qu'un espion placé entre eux ne l'intercepte ?

#### 1.2 La révolution asymétrique (1977)
Pendant deux mille ans, les souverains et les diplomates ont buté sur ce paradoxe.
Jusqu'en 1977, où trois chercheurs du MIT — **Ron Rivest, Adi Shamir et Leonard Adleman** — réalisent un coup d'éclat : inventer un cadenas à deux clés distinctes :
1. Une **clé publique**, que tout le monde peut voir et utiliser pour fermer le cadenas (chiffrer le message).
2. Une **clé privée**, que seul le destinataire possède, indispensable pour ouvrir le cadenas (déchiffrer le message).

Le fondement de ce cadenas inviolable ne repose sur aucun mécanisme physique : il repose sur un théorème d'arithmétique découvert par un magistrat toulousain en **1640**, Pierre de Fermat, et sur la théorie des **congruences** développée par Carl Friedrich Gauss.

---

### 2. Divisibilité et Division Euclidienne dans $\mathbb{Z}$

#### 2.1 La divisibilité dans l'ensemble des entiers relatifs $\mathbb{Z}$

> **📐 Définition — Divisibilité**
> Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z}$.
> On dit que **$a$ divise $b$** (ou que $b$ est un **multiple** de $a$, ou que $b$ est divisible par $a$), et l'on note **$a \mid b$**, s'il existe un entier relatif $k \in \mathbb{Z}$ tel que :
> $$b = k \cdot a$$

*Exemples :*
- $7 \mid 42$ car $42 = 6 \times 7$.
- $-3 \mid 15$ car $15 = (-5) \times (-3)$.
- $5 \mid 0$ car $0 = 0 \times 5$ (tout entier non nul divise 0).
- 0 ne divise aucun nombre non nul, car $0 \times k = 0 \neq b$.

> **📐 Propriétés fondamentales de la divisibilité**
> 1. **Réflexivité :** Pour tout $a \in \mathbb{Z}$, $a \mid a$.
> 2. **Transitivité :** Si $a \mid b$ et $b \mid c$, alors $a \mid c$.
> 3. **Combinaisons linéaires (essentielle !) :**
>    Si $a \mid b$ et $a \mid c$, alors pour tous entiers relatifs $u, v \in \mathbb{Z}$ :
>    $$a \mid (u b + v c)$$

*Démonstration de la combinaison linéaire :*
Si $b = k_1 a$ et $c = k_2 a$, alors $ub + vc = u(k_1 a) + v(k_2 a) = (u k_1 + v k_2) a$. Comme $(u k_1 + v k_2) \in \mathbb{Z}$, $a$ divise bien $ub + vc$.

#### 2.2 Le théorème de la division euclidienne

> **📐 Théorème fondamental — Division euclidienne dans $\mathbb{Z}$**
> Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z}^*$ (avec $b > 0$).
> Il existe un **unique** couple d'entiers relatifs $(q, r) \in \mathbb{Z} \times \mathbb{N}$ tel que :
> $$a = b q + r \quad \text{avec} \quad 0 \leq r < b$$
> - $a$ est le **dividende**.
> - $b$ est le **diviseur**.
> - $q$ est le **quotient**.
> - $r$ est le **reste**.

> **⚠️ Attention, piège ! — La division d'un nombre négatif**
> Soit $a = -23$ et $b = 5$.
> Une erreur fréquente consiste à écrire $-23 = 5 \times (-4) - 3$.
> C'est **interdit** ! Le reste $r$ doit impérativement être **positif ou nul** ($0 \leq r < 5$).
> L'unique écriture correcte est :
> $$-23 = 5 \times (-5) + 2$$
> Le quotient est $q = -5$ et le reste est $r = 2$ (qui vérifie bien $0 \leq 2 < 5$).

---

### 3. Les Congruences et l'Arithmétique de l'Horloge

En 1801, à l'âge de 24 ans, **Carl Friedrich Gauss** publie ses *Disquisitiones Arithmeticae*. Il y introduit une notation qui va révolutionner l'algèbre : la notion de **congruence**.

#### 3.1 Définition et sens circulaire

> **📐 Définition — Congruence modulo $n$**
> Soit $n$ un entier naturel non nul ($n \geq 2$).
> Deux entiers relatifs $a$ et $b$ sont dits **congrus modulo $n$**, ce que l'on note :
> $$a \equiv b \pmod n \quad \text{ou} \quad a \equiv b \ [n]$$
> si et seulement si leur différence $a - b$ est divisible par $n$ :
> $$n \mid (a - b) \iff \exists k \in \mathbb{Z}, \ a - b = k n$$

*Caractérisation par les restes :*
Deux entiers $a$ et $b$ sont congrus modulo $n$ si et seulement si **ils ont exactement le même reste** dans la division euclidienne par $n$.

*L'arithmétique de l'horloge :*
Sur une horloge à 12 heures, s'il est 9 heures et que l'on attend 7 heures, il sera 16 heures, ce qui correspond à 4 heures :
$$9 + 7 = 16 \equiv 4 \pmod{12}$$
L'ensemble des restes possibles modulo $n$ est fini : c'est $\{0, 1, 2, \dots, n-1\}$.

```
              Modulo 12 (Le cadran de l'horloge)
                           0 ≡ 12
                       11     1
                    10           2
                   9       o       3
                    8             4
                       7       5
                           6
```

#### 3.2 La compatibilité magique avec les opérations

> **📐 Théorème fondamental — Propriétés opératoires des congruences**
> Si $a \equiv b \pmod n$ et $c \equiv d \pmod n$, alors :
> 1. **Addition :** $a + c \equiv b + d \pmod n$
> 2. **Soustraction :** $a - c \equiv b - d \pmod n$
> 3. **Multiplication :** $a \times c \equiv b \times d \pmod n$
> 4. **Puissances entières :** Pour tout entier $k \in \mathbb{N}$, $a^k \equiv b^k \pmod n$

> **⚠️ Attention, piège absolu ! — L'interdiction de diviser naïvement**
> Dans une égalité classique, $6x = 6y \implies x = y$.
> **Dans les congruences, c'est faux en général !**
> Regarde : $2 \times 1 = 2 \equiv 2 \pmod 4$ et $2 \times 3 = 6 \equiv 2 \pmod 4$.
> Donc $2 \times 1 \equiv 2 \times 3 \pmod 4$.
> Pourtant, $1 \not\equiv 3 \pmod 4$ ! On ne peut pas « simplifier par 2 ».
> On ne peut diviser par $c$ dans $ac \equiv bc \pmod n$ que si **$c$ est premier avec $n$** ($\text{PGCD}(c, n) = 1$) !

---

### 4. PGCD, Algorithme d'Euclide et Théorème de Bézout

#### 4.1 L'algorithme d'Euclide
Le Plus Grand Commun Diviseur de deux entiers $a$ et $b$ non tous deux nuls est noté $\text{PGCD}(a, b)$ ou $a \wedge b$.
Euclide (-300) a établi que si $a = bq + r$, alors :
$$\text{PGCD}(a, b) = \text{PGCD}(b, r)$$
Le PGCD est le **dernier reste non nul** de la suite des divisions euclidiennes.

*Exemple : Calculons $\text{PGCD}(126, 48)$ :*
1. $126 = 48 \times 2 + 30$
2. $48 = 30 \times 1 + 18$
3. $30 = 18 \times 1 + 12$
4. $18 = 12 \times 1 + 6$
5. $12 = 6 \times 2 + 0$
Le dernier reste non nul est 6. Donc $\text{PGCD}(126, 48) = 6$.

#### 4.2 L'algorithme d'Euclide étendu et les coefficients de Bézout
En remontant les lignes de l'algorithme d'Euclide à l'envers, on peut toujours exprimer le PGCD comme une **combinaison linéaire** des deux entiers de départ !
Reprenons l'exemple :
- Ligne 4 : $6 = 18 - 12 \times 1$
- Ligne 3 : or $12 = 30 - 18 \times 1$, donc :
  $$6 = 18 - (30 - 18 \times 1) = 2 \times 18 - 1 \times 30$$
- Ligne 2 : or $18 = 48 - 30 \times 1$, donc :
  $$6 = 2 \times (48 - 30) - 1 \times 30 = 2 \times 48 - 3 \times 30$$
- Ligne 1 : or $30 = 126 - 48 \times 2$, donc :
  $$6 = 2 \times 48 - 3 \times (126 - 48 \times 2) = 2 \times 48 - 3 \times 126 + 6 \times 48 = -3 \times 126 + 8 \times 48$$

Nous avons trouvé deux entiers $u = -3$ et $v = 8$ tels que :
$$126 \times (-3) + 48 \times 8 = 6$$

#### 4.3 Le Théorème de Bézout

> **📐 Théorème fondamental de Bézout (1767)**
> Deux entiers relatifs non nuls $a$ et $b$ sont **premiers entre eux** ($\text{PGCD}(a, b) = 1$) si et seulement s'il existe deux entiers relatifs $u$ et $v$ tels que :
>
> $$\mathbf{a u + b v = 1}$$

*Sens réciproque immédiat :*
Si $au + bv = 1$, tout diviseur commun $d$ de $a$ et $b$ divise la combinaison linéaire $au + bv = 1$. Donc $d \mid 1$, d'où $d = \pm 1$. Le PGCD vaut donc 1.

#### 4.4 Résolution des équations diophantiennes $ax + by = c$

Une **équation diophantienne** (en l'honneur de Diophante d'Alexandrie) est une équation dont on cherche les solutions $(x, y)$ uniquement dans l'ensemble des entiers relatifs $\mathbb{Z}^2$.

> **🧭 Méthode — Résolution de $ax + by = c$**
> 1. **Condition d'existence :** Poser $d = \text{PGCD}(a, b)$.
>    L'équation admet des solutions entières si et seulement si **$d$ divise $c$**.
> 2. **Simplification :** On divise toute l'équation par $d$ pour obtenir $a'x + b'y = c'$ avec $\text{PGCD}(a', b') = 1$.
> 3. **Solution particulière :** On trouve une solution particulière $(x_0, y_0)$ à l'aide de l'algorithme d'Euclide étendu.
> 4. **Soustraction membre à membre :**
>    $a'x + b'y = c'$ et $a'x_0 + b'y_0 = c'$.
>    Par soustraction : $a'(x - x_0) = -b'(y - y_0) = b'(y_0 - y)$.
> 5. **Théorème de Gauss :** Comme $a'$ divise $b'(y_0 - y)$ et $\text{PGCD}(a', b') = 1$, $a'$ divise $(y_0 - y)$.
>    On en déduit l'ensemble de toutes les solutions $(x, y)$ indexées par un entier $k \in \mathbb{Z}$.

---

### 5. Le Théorème de Gauss

> **📐 Théorème fondamental de Gauss**
> Soient $a, b, c \in \mathbb{Z}$.
> Si **$a$ divise le produit $bc$** et si **$\text{PGCD}(a, b) = 1$**, alors :
>
> $$\mathbf{a \text{ divise } c}$$

> **✍️ Démonstration exigible — Théorème de Gauss**
> Supposons que $a \mid bc$ et que $\text{PGCD}(a, b) = 1$.
> Puisque $a$ et $b$ sont premiers entre eux, d'après le théorème de Bézout, il existe deux entiers $u, v \in \mathbb{Z}$ tels que :
> $$a u + b v = 1$$
> Multiplions les deux membres de cette égalité par l'entier $c$ :
> $$a c u + b c v = c$$
> Analysons les deux termes de gauche :
> - Le premier terme $a c u$ est évidemment un multiple de $a$ (il contient le facteur $a$).
> - Le second terme contient $bc$. Or par hypothèse, $a \mid bc$, donc il existe un entier $k$ tel que $bc = ka$. Le second terme s'écrit donc $(ka)v = a(kv)$, qui est aussi un multiple de $a$.
>
> On peut donc factoriser par $a$ dans le membre de gauche :
> $$a (cu + kv) = c$$
> Comme $(cu + kv) \in \mathbb{Z}$, cette égalité prouve rigoureusement que $a$ divise $c$.

*Corollaire (unicité de la décomposition en facteurs premiers) :*
Si un nombre premier $p$ divise un produit $x_1 x_2 \dots x_m$, alors $p$ divise nécessairement au moins l'un des facteurs $x_i$.

---

### 6. Le Petit Théorème de Fermat et l'Exponentiation Rapide

#### 6.1 Le Petit Théorème de Fermat (1640)

> **📐 Théorème — Petit Théorème de Fermat**
> Soit $p$ un nombre premier.
> 1. Pour tout entier relatif $a$ non divisible par $p$ ($\text{PGCD}(a, p) = 1$) :
>    $$\mathbf{a^{p-1} \equiv 1 \pmod p}$$
> 2. Pour tout entier relatif $a \in \mathbb{Z}$ (sans aucune restriction) :
>    $$\mathbf{a^p \equiv a \pmod p}$$

> **✍️ Démonstration classique par les restes**
> Soit $p$ premier et $a$ un entier non divisible par $p$.
> Considérons les $p-1$ multiples successifs : $a, 2a, 3a, \dots, (p-1)a$.
> Montrons que leurs restes modulo $p$ sont tous distincts et non nuls :
> Si $k_1 a \equiv k_2 a \pmod p$ avec $1 \leq k_2 \leq k_1 \leq p-1$, alors $p \mid (k_1 - k_2)a$.
> Comme $\text{PGCD}(a, p) = 1$, d'après le théorème de Gauss, $p \mid (k_1 - k_2)$.
> Or $0 \leq k_1 - k_2 < p$, ce qui impose $k_1 - k_2 = 0 \iff k_1 = k_2$.
> Les restes des nombres $\{a, 2a, \dots, (p-1)a\}$ modulo $p$ sont donc exactement les entiers $\{1, 2, \dots, p-1\}$ dans un ordre mélangé !
> Faisons le produit de ces $p-1$ congruences :
> $$a \times 2a \times 3a \times \dots \times (p-1)a \equiv 1 \times 2 \times \dots \times (p-1) \pmod p$$
> En factorisant $a$ dans chaque terme :
> $$a^{p-1} \times (p-1)! \equiv (p-1)! \pmod p$$
> Puisque $p$ est premier, aucun des facteurs de $(p-1)!$ n'est divisible par $p$, donc $\text{PGCD}((p-1)!, p) = 1$.
> D'après le théorème de Gauss (ou par multiplication par l'inverse modulaire de $(p-1)!$), on peut simplifier par $(p-1)!$ :
> $$a^{p-1} \equiv 1 \pmod p$$

#### 6.2 L'algorithme d'exponentiation modulaire rapide
Comment calculer une puissance astronomique comme $7^{100} \pmod{13}$ sans calculer un nombre à 85 chiffres ?
On utilise la décomposition binaire de l'exposant (méthode dite *Square-and-Multiply*) :
L'exposant $100$ s'écrit en binaire : $100 = 64 + 32 + 4$.
On calcule les carrés successifs modulo 13 :
- $7^1 \equiv 7 \pmod{13}$
- $7^2 = 49 = 3 \times 13 + 10 \equiv -3 \pmod{13}$
- $7^4 \equiv (-3)^2 = 9 \equiv -4 \pmod{13}$
- $7^8 \equiv (-4)^2 = 16 \equiv 3 \pmod{13}$
- $7^{16} \equiv 3^2 = 9 \equiv -4 \pmod{13}$
- $7^{32} \equiv (-4)^2 = 16 \equiv 3 \pmod{13}$
- $7^{64} \equiv 3^2 = 9 \equiv -4 \pmod{13}$

Il ne reste plus qu'à multiplier les puissances utiles :
$$7^{100} = 7^{64} \times 7^{32} \times 7^4 \equiv (-4) \times 3 \times (-4) = 48 \equiv 9 \pmod{13}.$$
Le calcul a pris 7 petites multiplications de nombres inférieurs à 50 au lieu de 99 multiplications géantes !

---

### 7. Applications à la Cryptographie : De César au RSA

#### 7.1 Le chiffrement affine
On associe à chaque lettre de l'alphabet un nombre de 0 à 25 (A=0, B=1, ..., Z=25).
La fonction de codage est :
$$y \equiv a x + b \pmod{26}$$

Pour que ce chiffrement soit **déchiffrable de façon unique**, deux lettres distinctes doivent obligatoirement donner deux codes distincts :
$$a x_1 + b \equiv a x_2 + b \pmod{26} \iff a(x_1 - x_2) \equiv 0 \pmod{26}$$
Cela n'impose $x_1 = x_2$ que si **$a$ est premier avec 26** : $\text{PGCD}(a, 26) = 1$.
Puisque $26 = 2 \times 13$, $a$ ne doit être divisible ni par 2, ni par 13.
Pour déchiffrer, on cherche l'**inverse modulaire** de $a$ modulo 26, c'est-à-dire l'entier $a'$ tel que $a a' \equiv 1 \pmod{26}$ (fourni par l'algorithme de Bézout).
La fonction de décodage est alors :
$$x \equiv a'(y - b) \pmod{26}$$

#### 7.2 Le principe du chiffrement asymétrique RSA

Voici le joyau absolu de la sécurité informatique moderne :

```
 Alice (Émettrice)                                    Bob (Destinataire)
 ─────────────────                                    ──────────────────
                                                      Choisit deux grands nombres
                                                      premiers p et q (secrets).
                                                      Calcule n = p × q.
                                                      Calcule φ(n) = (p-1)(q-1).
                                                      Choisit e premier avec φ(n).
                                                      Calcule d = e⁻¹ mod φ(n) (secret).
                                                            │
  Reçoit la Clé Publique (n, e) ◄───────────────────────────┘
  Possède le message M (entier < n)
  Calcule le message chiffré :
  C ≡ Mᵉ (mod n)
        │
        └────────────────────────► Reçoit le message chiffré C
                                   Applique sa Clé Privée (d) :
                                   M' ≡ Cᵈ (mod n)
                                   Résultat mathématique : M' = M !
```

> **✍️ Démonstration mathématique — Pourquoi le RSA déchiffre toujours exactement**
> Par construction, $d$ est l'inverse de $e$ modulo $\varphi(n) = (p-1)(q-1)$.
> Il existe donc un entier $k \in \mathbb{Z}$ tel que :
> $$e \cdot d = 1 + k(p-1)(q-1)$$
> Bob calcule $C^d \pmod n$. Or $C \equiv M^e \pmod n$, donc :
> $$C^d \equiv (M^e)^d = M^{ed} = M^{1 + k(p-1)(q-1)} \pmod n$$
> Montrons que cette quantité est congrue à $M$ modulo $p$ et modulo $q$ :
> - **Modulo $p$ :**
>   - Si $p$ divise $M$, alors $M \equiv 0 \pmod p$, donc $M^{ed} \equiv 0 \equiv M \pmod p$.
>   - Si $p$ ne divise pas $M$, par le Petit Théorème de Fermat, $M^{p-1} \equiv 1 \pmod p$.
>     Alors :
>     $$M^{ed} = M \times \left(M^{p-1}\right)^{k(q-1)} \equiv M \times 1^{k(q-1)} = M \pmod p$$
>   Dans tous les cas, $M^{ed} \equiv M \pmod p \iff p \mid (M^{ed} - M)$.
> - **Modulo $q$ :**
>   Par un raisonnement rigoureusement symétrique, $q \mid (M^{ed} - M)$.
>
> Puisque $p$ et $q$ sont deux nombres premiers distincts, ils sont premiers entre eux.
> D'après le théorème de Gauss (ou par produit des diviseurs premiers), leur produit $n = pq$ divise $(M^{ed} - M)$ :
> $$M^{ed} \equiv M \pmod n$$
> Le message d'origine réapparaît intact !

*Pourquoi est-il impossible de tricher ?*
Pour trouver la clé privée $d$, un espion doit calculer l'inverse de $e$ modulo $(p-1)(q-1)$.
Pour cela, il a impérativement besoin de connaître $p$ et $q$.
Or l'espion ne connaît que le nombre public $n = p \times q$.
Si $p$ et $q$ ont chacun 300 chiffres décimaux, le produit $n$ compte 600 chiffres. Décomposer un tel nombre en facteurs premiers nécessiterait des milliards d'années de calcul pour tous les superordinateurs de la Terre réunis !

---

### 8. Exemples résolus pas à pas

#### Exemple 1 : Résolution d'une congruence linéaire
Résoudre dans $\mathbb{Z}$ la congruence :
$$5x \equiv 3 \pmod{14}$$

**Solution détaillée :**
Pour résoudre cette équation, nous devons trouver un inverse de 5 modulo 14.
Cherchons une relation de Bézout entre 5 et 14 :
$$14 = 5 \times 2 + 4 \implies 4 = 14 - 5 \times 2$$
$$5 = 4 \times 1 + 1 \implies 1 = 5 - 4 \times 1 = 5 - (14 - 5 \times 2) = 5 \times 3 - 14 \times 1$$
On a donc $5 \times 3 - 14 \times 1 = 1$, ce qui signifie que :
$$5 \times 3 \equiv 1 \pmod{14}$$
L'inverse de 5 modulo 14 est donc **3**.
Multiplions les deux membres de la congruence initiale par 3 :
$$3 \times (5x) \equiv 3 \times 3 \pmod{14}$$
$$(3 \times 5) x \equiv 9 \pmod{14}$$
$$1 \cdot x \equiv 9 \pmod{14} \iff x \equiv 9 \pmod{14}$$
L'ensemble des solutions est l'ensemble des entiers de la forme :
$$x = 14k + 9 \quad (k \in \mathbb{Z})$$
*(Vérification : pour $x = 9$, $5 \times 9 = 45 = 14 \times 3 + 3 \equiv 3 \pmod{14}$).*

#### Exemple 2 : Résolution d'une équation diophantienne
Résoudre dans $\mathbb{Z}^2$ l'équation :
$$47x + 29y = 1$$

**Solution détaillée :**
1. **Algorithme d'Euclide pour 47 et 29 :**
   - $47 = 29 \times 1 + 18$
   - $29 = 18 \times 1 + 11$
   - $18 = 11 \times 1 + 7$
   - $11 = 7 \times 1 + 4$
   - $7 = 4 \times 1 + 3$
   - $4 = 3 \times 1 + 1$
   - $3 = 1 \times 3 + 0$
   Le dernier reste non nul est 1, donc $\text{PGCD}(47, 29) = 1$. L'équation admet des solutions.
2. **Remontée de l'algorithme :**
   - $1 = 4 - 3 \times 1$
   - $1 = 4 - (7 - 4) = 2 \times 4 - 7$
   - $1 = 2 \times (11 - 7) - 7 = 2 \times 11 - 3 \times 7$
   - $1 = 2 \times 11 - 3 \times (18 - 11) = 5 \times 11 - 3 \times 18$
   - $1 = 5 \times (29 - 18) - 3 \times 18 = 5 \times 29 - 8 \times 18$
   - $1 = 5 \times 29 - 8 \times (47 - 29) = 13 \times 29 - 8 \times 47 = 47 \times (-8) + 29 \times 13$
   Une solution particulière est donc $(x_0, y_0) = (-8, 13)$.
3. **Résolution générale :**
   $$47x + 29y = 1 \quad \text{et} \quad 47(-8) + 29(13) = 1$$
   Par soustraction :
   $$47(x - (-8)) + 29(y - 13) = 0 \iff 47(x + 8) = 29(13 - y)$$
   Puisque 47 divise $29(13 - y)$ et $\text{PGCD}(47, 29) = 1$, d'après le théorème de Gauss, 47 divise $(13 - y)$.
   Il existe donc un entier $k \in \mathbb{Z}$ tel que :
   $$13 - y = 47k \iff y = 13 - 47k$$
   En remplaçant dans l'égalité :
   $$47(x + 8) = 29(47k) \iff x + 8 = 29k \iff x = -8 + 29k$$
   L'ensemble des solutions dans $\mathbb{Z}^2$ est :
   $$S = \{(-8 + 29k \ ;\  13 - 47k) \mid k \in \mathbb{Z}\}$$

#### Exemple 3 : Déchiffrement d'un code affine
Un message a été crypté avec le chiffrement affine $y \equiv 7x + 5 \pmod{26}$.
On intercepte la lettre chiffrée **V** (qui correspond au rang 21).
Retrouver la lettre d'origine $x$.

**Solution détaillée :**
1. L'équation à résoudre est $7x + 5 \equiv 21 \pmod{26} \iff 7x \equiv 16 \pmod{26}$.
2. Cherchons l'inverse de 7 modulo 26 :
   $26 = 7 \times 3 + 5$
   $7 = 5 \times 1 + 2$
   $5 = 2 \times 2 + 1 \implies 1 = 5 - 2 \times 2 = 5 - 2(7 - 5) = 3 \times 5 - 2 \times 7 = 3(26 - 7 \times 3) - 2 \times 7 = 3 \times 26 - 11 \times 7$.
   Donc $-11 \times 7 \equiv 1 \pmod{26}$.
   Or $-11 \equiv 26 - 11 = 15 \pmod{26}$.
   Vérifions : $7 \times 15 = 105 = 4 \times 26 + 1 \equiv 1 \pmod{26}$.
   L'inverse de 7 modulo 26 est donc **15**.
3. Multiplions l'équation $7x \equiv 16 \pmod{26}$ par 15 :
   $$x \equiv 15 \times 16 \pmod{26}$$
   $15 \times 16 = 240$.
   Effectuons la division euclidienne de 240 par 26 :
   $240 = 26 \times 9 + 6$.
   Donc $x \equiv 6 \pmod{26}$.
4. Le rang 6 correspond à la lettre :
   $0 \to A, 1 \to B, 2 \to C, 3 \to D, 4 \to E, 5 \to F, 6 \to \mathbf{G}$.
   La lettre d'origine était un **G**.

#### Exemple 4 : Calcul de reste avec le Petit Théorème de Fermat
Déterminer le reste de la division euclidienne de $3^{2026}$ par 17.

**Solution détaillée :**
1. Le diviseur est $p = 17$, qui est un nombre premier.
2. L'entier $a = 3$ n'est pas divisible par 17 ($\text{PGCD}(3, 17) = 1$).
3. D'après le Petit Théorème de Fermat :
   $$3^{17-1} = 3^{16} \equiv 1 \pmod{17}$$
4. Effectuons la division euclidienne de la puissance 2026 par 16 :
   $$2026 = 16 \times 126 + 10$$
5. Décomposons la puissance :
   $$3^{2026} = 3^{16 \times 126 + 10} = (3^{16})^{126} \times 3^{10} \equiv 1^{126} \times 3^{10} \equiv 3^{10} \pmod{17}$$
6. Calculons $3^{10} \pmod{17}$ par carrés successifs :
   - $3^2 = 9$
   - $3^4 = 9^2 = 81 = 17 \times 4 + 13 \equiv -4 \pmod{17}$
   - $3^8 \equiv (-4)^2 = 16 \equiv -1 \pmod{17}$
   - $3^{10} = 3^8 \times 3^2 \equiv (-1) \times 9 = -9 \equiv 17 - 9 = 8 \pmod{17}$.
Le reste de la division de $3^{2026}$ par 17 est donc **8**.

#### Exemple 5 : Un exemple miniature complet du RSA
Bob prépare ses clés RSA :
1. Il choisit $p = 5$ et $q = 11$.
2. Calculer le module $n$ et la valeur de l'indicatrice $\varphi(n)$.
3. Bob choisit la clé publique $e = 3$. Vérifier que ce choix est valide.
4. Calculer la clé privée secrète $d$.
5. Alice veut envoyer le message secret $M = 9$. Chiffrer ce message pour obtenir $C$.
6. Montrer comment Bob déchiffre $C$ pour retrouver $M$.

**Solution détaillée :**
1. $n = p \times q = 5 \times 11 = 55$.
2. $\varphi(n) = (p-1)(q-1) = 4 \times 10 = 40$.
3. $e = 3$. Comme $40 = 3 \times 13 + 1$, $\text{PGCD}(3, 40) = 1$. Le choix $e = 3$ est parfaitement valide.
4. On cherche $d$ tel que $3d \equiv 1 \pmod{40}$.
   Or $3 \times 13 = 39 = 40 - 1 \equiv -1 \pmod{40}$, donc $3 \times (-13) \equiv 1 \pmod{40}$.
   Comme $-13 \equiv 40 - 13 = 27 \pmod{40}$, on a $d = 27$.
   *(Vérification : $3 \times 27 = 81 = 2 \times 40 + 1 \equiv 1$).*
   La clé privée de Bob est **$d = 27$**.
5. **Chiffrement par Alice :**
   $C \equiv M^e \pmod n \iff C \equiv 9^3 \pmod{55}$.
   $9^3 = 729$.
   Division de 729 par 55 : $729 = 55 \times 13 + 14$.
   Le message chiffré envoyé sur le réseau est **$C = 14$**.
6. **Déchiffrement par Bob :**
   Bob calcule $M \equiv C^d = 14^{27} \pmod{55}$.
   Décomposons l'exposant 27 en binaire : $27 = 16 + 8 + 2 + 1$.
   Calculons les puissances de 14 modulo 55 :
   - $14^1 \equiv 14$
   - $14^2 = 196 = 55 \times 3 + 31 \equiv 31 \equiv -24 \pmod{55}$
   - $14^4 \equiv (-24)^2 = 576 = 55 \times 10 + 26 \equiv 26 \pmod{55}$
   - $14^8 \equiv 26^2 = 676 = 55 \times 12 + 16 \equiv 16 \pmod{55}$
   - $14^{16} \equiv 16^2 = 256 = 55 \times 4 + 36 \equiv 36 \equiv -19 \pmod{55}$
   Multiplions :
   $14^{27} = 14^{16} \times 14^8 \times 14^2 \times 14 \equiv (-19) \times 16 \times 31 \times 14 \pmod{55}$.
   - $(-19) \times 16 = -304 = 55 \times (-6) + 26 \equiv 26$
   - $31 \times 14 = 434 = 55 \times 7 + 49 \equiv -6$
   - $26 \times (-6) = -156 = 55 \times (-3) + 9 \equiv 9 \pmod{55}$.
   Bob retrouve exactement **$M = 9$** !

#### Exemple 6 : Critères de divisibilité par les congruences
Démontrer à l'aide des congruences qu'un nombre entier est divisible par 9 si et seulement si la somme de ses chiffres est divisible par 9.

**Solution détaillée :**
Soit un entier naturel $N$ dont l'écriture décimale est $a_k a_{k-1} \dots a_1 a_0$ :
$$N = \sum_{j=0}^k a_j 10^j = a_0 + a_1 10 + a_2 10^2 + \dots + a_k 10^k$$
Remarquons que :
$$10 = 9 + 1 \equiv 1 \pmod 9$$
D'après les propriétés de compatibilité des congruences avec les puissances :
Pour tout entier $j \geq 0$, $10^j \equiv 1^j \equiv 1 \pmod 9$.
En multipliant par chaque chiffre $a_j$ et en sommant :
$$N = \sum_{j=0}^k a_j 10^j \equiv \sum_{j=0}^k a_j (1) \equiv \sum_{j=0}^k a_j \pmod 9$$
Le nombre $N$ et la somme de ses chiffres ont donc exactement le même reste modulo 9.
Par conséquent, $9 \mid N$ si et seulement si 9 divise la somme de ses chiffres décimaux.

---

### Ce qu'il faut retenir

1. **Divisibilité et Division :**
   - $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$.
   - Combinaisons linéaires : si $a \mid b$ et $a \mid c$, alors $a \mid (ub + vc)$.
   - Division euclidienne : $a = bq + r$ avec $0 \leq r < b$.

2. **Congruences :**
   - $a \equiv b \pmod n \iff n \mid (a - b)$ (même reste par $n$).
   - Compatible avec addition, soustraction, multiplication et puissances.
   - On ne peut simplifier $ac \equiv bc \pmod n$ par $c$ que si $\text{PGCD}(c, n) = 1$.

3. **Bézout et Gauss :**
   - $\text{PGCD}(a, b) = 1 \iff \exists u, v \in \mathbb{Z}, au + bv = 1$ (Bézout).
   - Si $a \mid bc$ et $\text{PGCD}(a, b) = 1$, alors $a \mid c$ (Gauss).

4. **Fermat et RSA :**
   - Petit théorème de Fermat : si $p$ premier et $p \nmid a$, alors $a^{p-1} \equiv 1 \pmod p$.
   - RSA : clé publique $(n, e)$ avec $n = pq$, clé privée $d \equiv e^{-1} \pmod{(p-1)(q-1)}$.
   - $C \equiv M^e \pmod n \implies M \equiv C^d \pmod n$.

---

### Exercices

#### Niveau ★ (Applications directes)

**Exercice 1.** Effectuer la division euclidienne dans $\mathbb{Z}$ :
1. De $157$ par $11$.
2. De $-75$ par $8$.
3. De $-140$ par $12$.
**Exercice 2.** Vrai ou Faux ? Justifier.
1. Si $a \equiv 3 \pmod 5$, alors $a^2 \equiv 4 \pmod 5$.
2. Si $a \equiv 2 \pmod 6$, alors $a$ est un nombre pair.
3. Si $3x \equiv 3y \pmod 7$, alors $x \equiv y \pmod 7$.
**Exercice 3.** Calculer le $\text{PGCD}(323, 187)$ par l'algorithme d'Euclide. Les nombres sont-ils premiers entre eux ?
**Exercice 4.** Trouver un couple d'entiers relatifs $(u, v)$ solution de l'identité de Bézout :
$$17 u + 11 v = 1$$
**Exercice 5.** Calculer le reste de la division euclidienne de $2^{100}$ par 7.
**Exercice 6.** Une pendule à 12 heures indique 8 heures. Quelle heure indiquera-t-elle dans 1 500 heures ?
**Exercice 7.** Résoudre dans $\mathbb{Z}$ l'équation $3x \equiv 1 \pmod{10}$.

#### Niveau ★★ (Réflexion et équations de baccalauréat)

**Exercice 8.** Résoudre dans $\mathbb{Z}^2$ l'équation diophantienne :
$$13x - 7y = 1$$
En déduire toutes les solutions vérifiant $0 \leq x \leq 50$.
**Exercice 9.** Chiffrement affine.
On utilise le chiffrement $y \equiv 5x + 7 \pmod{26}$.
1. Vérifier que ce codage est réversible.
2. Coder le mot **BAC**.
3. Trouver la fonction de déchiffrement et décoder la lettre **R** (rang 17).
**Exercice 10.** Déterminer le chiffre des unités de $7^{2025}$ dans son écriture décimale classique.
*(Indication : chercher le reste modulo 10).*
**Exercice 11.** Démontrer que pour tout entier naturel $n$, l'entier $A_n = 3^{2n+1} + 2^{n+2}$ est divisible par 7.
**Exercice 12.** Soit $n \in \mathbb{N}$. Démontrer que la fraction $\frac{2n+1}{3n+1}$ est irréductible pour tout entier $n$.
**Exercice 13.** Les voleurs de noix de coco.
Trois naufragés ramassent un tas de noix de coco. Pendant la nuit, le premier se réveille, partage le tas en 3 parts égales, constate qu'il reste 1 noix qu'il donne à un singe, et cache sa part. Le deuxième et le troisième font successivement de même.
Traduire ce problème par un système de congruences et trouver le nombre minimal de noix initiales.
**Exercice 14.** Théorème des restes chinois (Cas particulier).
Résoudre dans $\mathbb{Z}$ le système de congruences :
$$\begin{cases} x \equiv 2 \pmod 5 \\ x \equiv 3 \pmod 7 \end{cases}$$
**Exercice 15.** Nombres de Mersenne et Fermat.
Soit $p$ un nombre premier impair. On considère le nombre de Mersenne $M_p = 2^p - 1$.
Soit $q$ un diviseur premier de $M_p$. Démontrer que $q \equiv 1 \pmod{2p}$.

#### Niveau ★★★ (Approfondissements et concours)

**Exercice 16.** Démonstration du Théorème de Wilson.
Démontrer qu'un entier $p \geq 2$ est premier si et seulement si :
$$(p-1)! \equiv -1 \pmod p$$
*(Indication : regrouper chaque élément de $\{2, \dots, p-2\}$ avec son inverse modulaire distinct).*
**Exercice 17.** L'indicatrice d'Euler $\varphi(n)$.
1. Pour $p$ premier, justifier que $\varphi(p) = p - 1$ et $\varphi(p^k) = p^k - p^{k-1}$.
2. Démontrer le théorème d'Euler généralisant Fermat : si $\text{PGCD}(a, n) = 1$, alors $a^{\varphi(n)} \equiv 1 \pmod n$.
**Exercice 18.** Le test de primalité de Miller-Rabin.
Expliquer le principe du test probabiliste de Miller-Rabin fondé sur le théorème de Fermat et les racines carrées de 1 modulo $p$. Pourquoi permet-il de tester des nombres de 500 chiffres en une fraction de seconde ?
**Exercice 19.** Attaque de Wiener sur le chiffrement RSA.
Montrer que si l'exposant secret $d$ est choisi trop petit ($d < \frac{1}{3} n^{1/4}$), la clé privée peut être retrouvée rapidement à partir de la clé publique $(n, e)$ en utilisant le développement en fractions continues de $\frac{e}{n}$.
**Exercice 20.** L'ordre d'un élément dans $\mathbb{Z}/p\mathbb{Z}$.
Soit $p$ un nombre premier et $a$ un entier non divisible par $p$.
On appelle ordre de $a$ modulo $p$ le plus petit entier non nul $k$ tel que $a^k \equiv 1 \pmod p$.
Démontrer que $k$ divise obligatoirement $p - 1$.
**Exercice 21.** Résidus quadratiques et symbole de Legendre.
Soit $p$ un nombre premier impair. Un entier $a$ non multiple de $p$ est un carré modulo $p$ s'il existe $x$ tel que $x^2 \equiv a \pmod p$.
Démontrer le critère d'Euler :
$$a^{\frac{p-1}{2}} \equiv \begin{cases} +1 \pmod p & \text{si } a \text{ est un carré} \\ -1 \pmod p & \text{si } a \text{ n'est pas un carré} \end{cases}$$
**Exercice 22.** Le problème du logarithme discret et l'échange de clés de Diffie-Hellman.
Expliquer le protocole d'échange de clés de Diffie-Hellman fondé sur la fonction puissance $g^a \pmod p$. Pourquoi est-il simple de calculer $g^a \pmod p$ mais presque impossible de retrouver $a$ connaissant $g^a$ ?

---

### Solutions

**Solution 1.**
1. $157 = 11 \times 14 + 3$ ($q = 14, r = 3$).
2. $-75 = 8 \times (-10) + 5$ ($q = -10, r = 5$).
3. $-140 = 12 \times (-12) + 4$ ($q = -12, r = 4$).

**Solution 2.**
1. **Vrai.** $a \equiv 3 \pmod 5 \implies a^2 \equiv 3^2 = 9 \equiv 4 \pmod 5$.
2. **Vrai.** $a = 6k + 2 = 2(3k + 1)$, qui est divisible par 2.
3. **Vrai.** Comme $\text{PGCD}(3, 7) = 1$, on peut diviser par 3 par le théorème de Gauss.

**Solution 3.**
$323 = 187 \times 1 + 136$.
$187 = 136 \times 1 + 51$.
$136 = 51 \times 2 + 34$.
$51 = 34 \times 1 + 17$.
$34 = 17 \times 2 + 0$.
$\text{PGCD}(323, 187) = 17 \neq 1$. Ils ne sont pas premiers entre eux.

**Solution 4.**
$17 = 11 \times 1 + 6 \implies 6 = 17 - 11$.
$11 = 6 \times 1 + 5 \implies 5 = 11 - 6 = 11 - (17 - 11) = 2 \times 11 - 17$.
$6 = 5 \times 1 + 1 \implies 1 = 6 - 5 = (17 - 11) - (2 \times 11 - 17) = 2 \times 17 - 3 \times 11$.
Un couple solution est $(u, v) = (2, -3)$.

**Solution 5.**
Modulo 7, $2^3 = 8 \equiv 1 \pmod 7$.
Division de 100 par 3 : $100 = 3 \times 33 + 1$.
$2^{100} = (2^3)^{33} \times 2^1 \equiv 1^{33} \times 2 = 2 \pmod 7$. Le reste est 2.

**Solution 6.**
On cherche $8 + 1500 \pmod{12}$.
$1500 = 12 \times 125 + 0 \equiv 0 \pmod{12}$.
La pendule indiquera donc de nouveau **8 heures** pile.

**Solution 7.**
On cherche l'inverse de 3 modulo 10. Comme $3 \times 7 = 21 \equiv 1 \pmod{10}$, l'inverse est 7.
$3x \equiv 1 \implies 7 \times 3x \equiv 7 \times 1 \implies x \equiv 7 \pmod{10}$.
$S = \{10k + 7 \mid k \in \mathbb{Z}\}$.

**Solution 8.**
$13(1) - 7(2) = 13 - 14 = -1 \implies 13(-1) - 7(-2) = 1$. Solution particulière : $(-1, -2)$.
$13(x + 1) = 7(y + 2)$. Comme $\text{PGCD}(13, 7) = 1$, par Gauss : $x + 1 = 7k \implies x = 7k - 1$ et $y = 13k - 2$.
Pour $0 \leq x \leq 50$ : $0 \leq 7k - 1 \leq 50 \implies 1 \leq 7k \leq 51 \implies k \in \{1, 2, 3, 4, 5, 6, 7\}$.
7 couples solutions.

**Solution 9.**
1. $\text{PGCD}(5, 26) = 1$ car $26 = 2 \times 13$, donc le codage est bijectif.
2. B(1) : $5(1) + 7 = 12 \to$ M.
   A(0) : $5(0) + 7 = 7 \to$ H.
   C(2) : $5(2) + 7 = 17 \to$ R. BAC devient **MHR**.
3. Inverse de 5 modulo 26 : $5 \times 21 = 105 = 4 \times 26 + 1$, donc $5^{-1} \equiv 21$.
   $x \equiv 21(y - 7) \pmod{26}$.
   Pour R ($y = 17$) : $x \equiv 21(17 - 7) = 210 = 26 \times 8 + 2 \equiv 2 \pmod{26}$. Le rang 2 correspond à **C**.

**Solution 10.**
Cherchons $7^{2025} \pmod{10}$.
$7^1 \equiv 7$, $7^2 = 49 \equiv 9 \equiv -1$, $7^4 \equiv 1 \pmod{10}$.
$2025 = 4 \times 506 + 1$.
$7^{2025} = (7^4)^{506} \times 7^1 \equiv 1 \times 7 = 7 \pmod{10}$.
Le chiffre des unités est **7**.

**Solution 11.**
$3^{2n+1} = 3 \times (3^2)^n = 3 \times 9^n \equiv 3 \times 2^n \pmod 7$ (car $9 \equiv 2$).
$2^{n+2} = 2^2 \times 2^n = 4 \times 2^n \pmod 7$.
Somme : $A_n \equiv 3 \times 2^n + 4 \times 2^n = 7 \times 2^n \equiv 0 \pmod 7$. Donc $7 \mid A_n$.

**Solution 12.**
Soit $d$ un diviseur commun du numérateur et du dénominateur.
$d \mid (2n + 1)$ et $d \mid (3n + 1)$.
Alors $d$ divise la combinaison linéaire $3(2n + 1) - 2(3n + 1) = 6n + 3 - 6n - 2 = 1$.
Comme $d \mid 1$, on a $d = 1$. Les deux entiers sont toujours premiers entre eux, la fraction est irréductible.

**Solution 13.**
Soit $N$ le nombre de noix.
Chaque étape retire 1 noix et prend un tiers, laissant $2/3(N-1)$.
Après 3 étapes, les divisions successives mènent à la congruence $8N \equiv 17 \pmod{27} \implies N \equiv 25 \pmod{27}$.
Le plus petit nombre positif non nul possible est $N = 25$ (ou 79 si le partage final du matin est non nul).

**Solution 14.**
$x = 5k + 2$. En injectant dans la seconde : $5k + 2 \equiv 3 \pmod 7 \iff 5k \equiv 1 \pmod 7$.
L'inverse de 5 modulo 7 est 3 ($5 \times 3 = 15 \equiv 1$).
Donc $k \equiv 3 \pmod 7 \implies k = 7m + 3$.
D'où $x = 5(7m + 3) + 2 = 35m + 17$. Les solutions sont $x \equiv 17 \pmod{35}$.

**Solution 15.**
Si $q \mid (2^p - 1)$, alors $2^p \equiv 1 \pmod q$. L'ordre de 2 modulo $q$ divise le nombre premier $p$, donc l'ordre vaut $p$.
D'après Fermat, $2^{q-1} \equiv 1 \pmod q$, donc l'ordre $p$ divise $q-1$, ce qui signifie $q - 1 = kp \implies q \equiv 1 \pmod p$.
Comme $q$ est impair ($M_p$ étant impair), $q - 1$ est pair, donc $k$ est pair ($k = 2m$).
D'où $q = 2mp + 1 \equiv 1 \pmod{2p}$.

**Solution 16.**
Si $p$ est premier, chaque élément $x \in \{2, \dots, p-2\}$ possède un unique inverse modulaire distinct de lui-même (car $x^2 \equiv 1 \implies x = \pm 1$). Tous ces termes se neutralisent deux à deux dans le produit $(p-1)!$, ne laissant que $1 \times (p-1) \equiv -1 \pmod p$. La réciproque découle du fait que si $p$ est composé, un diviseur strict $d < p$ diviserait $(p-1)!$ et ne pourrait diviser $(p-1)! + 1$.

**Solution 17.**
1. Pour $p^k$, les entiers non premiers avec $p^k$ sont les multiples de $p$, soit $p^{k-1}$ entiers. Donc $\varphi(p^k) = p^k - p^{k-1}$.
2. En considérant les entiers premiers avec $n$ et en multipliant par $a$, le produit des éléments se conserve par bijectivité de la multiplication dans le groupe des inversibles $(\mathbb{Z}/n\mathbb{Z})^\times$, ce qui donne $a^{\varphi(n)} \equiv 1 \pmod n$.

**Solution 18.**
Si $n$ est premier, pour $n-1 = 2^s d$, la suite des élévations au carré à partir de $a^d$ doit terminer par 1, et la dernière valeur différente de 1 doit être $-1$. Si une autre valeur apparaît, $n$ est certainement composé. Ce test polynomial rapide est la clé de voûte de la génération des grands nombres premiers pour la cryptographie.

**Solution 19.**
Si $ed - k\varphi(n) = 1$, alors $\left|\frac{e}{n} - \frac{k}{d}\right| \leq \frac{1}{2d^2}$. D'après le théorème de Legendre sur les fractions continues, $\frac{k}{d}$ est nécessairement l'une des réduites de l'approximation de $\frac{e}{n}$, ce qui permet à un attaquant de calculer $d$ en un temps quasi instantané.

**Solution 20.**
Soit $k$ l'ordre de $a$. Effectuons la division euclidienne de $p-1$ par $k$ : $p-1 = kq + r$ avec $0 \leq r < k$.
Alors $a^{p-1} = (a^k)^q \times a^r \equiv 1^q \times a^r \equiv a^r \pmod p$.
Or d'après Fermat, $a^{p-1} \equiv 1 \pmod p$, donc $a^r \equiv 1 \pmod p$.
Comme $k$ est le plus petit entier strictement positif vérifiant cette propriété et que $r < k$, on a obligatoirement $r = 0$. Donc $k$ divise $p - 1$.

**Solution 21.**
D'après Fermat, $(a^{\frac{p-1}{2}})^2 = a^{p-1} \equiv 1 \pmod p$. Donc $a^{\frac{p-1}{2}}$ est solution de $X^2 \equiv 1 \pmod p$, d'où $a^{\frac{p-1}{2}} \equiv \pm 1 \pmod p$. Si $a = x^2$, alors $a^{\frac{p-1}{2}} = x^{p-1} \equiv 1$. Le polynôme $X^{\frac{p-1}{2}} - 1$ de degré $\frac{p-1}{2}$ ayant au plus $\frac{p-1}{2}$ racines, les carrés en sont les seules racines.

**Solution 22.**
Alice choisit $a$ secret, envoie $A = g^a \pmod p$. Bob choisit $b$ secret, envoie $B = g^b \pmod p$. La clé commune est $K = B^a = A^b = g^{ab} \pmod p$. Un espion qui intercepte $g^a$ et $g^b$ ne peut pas calculer $g^{ab}$ sans résoudre le problème du logarithme discret, réputé intraitable pour de grands modules premiers.

---

### La question qui ouvre la suite

Nous venons de voir comment les équations arithmétiques permettent de chiffrer des flux d'informations et de relier des variables entières.
Mais que se passe-t-il lorsque les flux à transformer ne sont plus de simples nombres isolés, mais des tableaux entiers de données, des réseaux d'interconnexions et des états probabilistes en perpétuelle transition ?
Comment modéliser l'évolution d'une population, le classement des pages web par Google ou les états d'une machine de Turing ?
Pour orchestrer ces flux multidimensionnels, les mathématiciens ont forgé un outil spectaculaire : les matrices et les graphes. Tourne la page pour découvrir **le Chapitre 57 et le Métier Jacquard Revisité : Matrices et Graphes**.
