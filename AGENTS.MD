# AGENT.MD — MANIFESTE, OBJECTIFS ET DIRECTIVES DE CONCEPTION
## Projet : « LA VOIE DU NOMBRE — Une Odyssée Constructive, du Premier Caillou au Baccalauréat »

> Ce document définit l'architecture intellectuelle, les objectifs pédagogiques fondamentaux, l'analyse des obstacles cognitifs et les protocoles opérationnels que tout agent (humain ou IA) doit respecter lors de la rédaction, de la révision ou de l'extension de la collection.

---

## 1. TITRE ET IDENTITÉ DE L'ŒUVRE

- **Titre Officiel :** *LA VOIE DU NOMBRE*
- **Sous-titre :** *Une Odyssée Constructive, du Premier Caillou au Baccalauréat*
- **Livre Compagnon :** *LE GUIDE DE L'ACCOMPAGNATEUR — Fondations Didactiques, Épistémologiques et Clés Pratiques*
- **Architecture :** 58 chapitres répartis en 6 volumes d'apprentissage progressif (CP à Terminale Spécialité et Maths Expertes).

---

## 2. LES TROIS IMPÉRATIFS ÉPISTÉMOLOGIQUES MAJEURS (ISSUES DE L'AUDIT INDÉPENDANT)

L'audit épistémologique et didactique indépendant a dégagé trois principes recteurs qui doivent guider toute contribution :

### A. Le Dépassement de « l'Obstacle Métaphorique » (Bachelard / Brousseau vs Lakoff)
La métaphore corporelle (le tas de cailloux, la marche sur le sentier, le rectangle de briques, la planche de ski) est indispensable pour allumer l'étincelle de la compréhension sans sidération. **Cependant, toute métaphore physique devient un obstacle épistémologique si elle n'est pas émancipée au bon moment.**
- *La limite du rectangle :* la multiplication est d'abord une aire rectangulaire ($4 \times 6 = 24$). Mais cette image s'effondre pour le produit de deux nombres négatifs ($(-3) \times (-5) = +15$) ou de probabilités ($\frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$). L'élève doit comprendre que la règle des signes relève de la **cohérence algébrique de la distributivité**, et non d'une géométrie impossible à surfaces négatives.
- *La limite du skieur :* la dérivée comme planche sous les semelles fonctionne pour les courbes lisses ($C^1$). Elle devient un piège devant les points anguleux ($|x|$ en 0) ou les fonctions oscillantes ($x^2 \sin(1/x)$).
- **Règle d'or :** L'expérience sensible est l'échafaudage de lancement ; dès que l'outil est éprouvé, l'agent doit expliciter la transition vers le formalisme logique autonome.

### B. La Gestion de la Mémoire de Travail et la Symétrie de Charge
- *La dérive verbale :* à vouloir tout expliquer par de longues proses narratives, l'ouvrage risque d'épuiser l'élève de 16-17 ans devant des chapitres de 50 à 70 Ko.
- **Règle d'or :** La narration historique et humaine doit immédiatement être relayée par :
  1. Des fiches réflexes structurées (« Ce qu'il faut retenir »).
  2. Des arbres de décision algorithmiques clairs.
  3. Des **gammes mécaniques d'automatismes (drill)** pour libérer 100 % de la mémoire de travail avant d'aborder des problèmes complexes.

### C. L'Impasse du « Tout-Texte » en Géométrie : Le Primat des Figures Vectorielles
- La géométrie ne peut pas s'enseigner par du texte seul ou des approximations typographiques en ASCII.
- Selon la théorie des registres sémiotiques (Duval), l'intelligence géométrique naît du va-et-vient constant entre le tracé visuel et l'équation algébrique.
- **Règle d'or :** Tout chapitre de géométrie, d'analyse ou de cinématique doit comporter des figures vectorielles nettes (SVG nativement inclus dans le Markdown, schémas Typst/CeTZ haute précision en PDF, diagrammes Mermaid pour les arbres de probabilités et organigrammes décisionnels, et illustrations générées pertinentes).

---

## 3. LA DOCTRINE DU « LABORATOIRE DES CAS LIMITES »

Pour éviter de saturer l'attention cognitive de l'élève lors de la phase d'acquisition du geste principal, les cas pathologiques doivent être **isolés** :
1. **Étape 1 — Le Réflexe Central :** On apprend d'abord la règle générale sur des cas massifs (ex. $4 \times 3 = 12$, la dérivée d'un polynôme, la division par un entier positif non nul).
2. **Étape 2 — L'Enclos du Cas Limite :** Dans une sous-section séparée (`🛠️ Le Laboratoire des Cas Limites`), on explore les frontières sans polluer le réflexe :
   - Que fait $4 \times 0$ ? Que fait $0 \times 0$ ?
   - Pourquoi $\frac{0}{5} = 0$, mais $\frac{5}{0}$ est rigoureusement impossible ?
   - Pourquoi $a^0 = 1$, et pourquoi $0^0$ est indéterminé ?
   - Pourquoi le vecteur nul $\vec{0}$ a une norme nulle et toutes les directions à la fois ?

---

## 4. LA CHARTE GRAPHIQUE CHROMATIQUE D'OLIVER BYRNE (1847)

Toutes les figures SVG et schémas du livre respectent le code couleur fonctionnel :
- **Bleu (#1d4ed8) :** L'action motrice, l'avancée horizontale, l'axe des abscisses $x$, le premier vecteur $\vec{u}$, le côté horizontal.
- **Rouge (#b91c1c) :** La contrainte, la hauteur verticale $y$, l'obstacle, la réaction, le deuxième vecteur $\vec{v}$.
- **Jaune / Ambre (#d97706) :** Le produit, l'aire intérieure, l'énergie, le double produit $2ab$, le quotient.
- **Vert (#15803d) :** Le bilan global (Chasles), la validation, le résultat, la tangente stable.
- **Noir / Ardoise (#0f172a) :** Le squelette d'ancrage, les axes neutres, la grille de fond.

---

## 5. TECHNOLOGIES ET FORMATS D'EXPORTATION

- **Markdown enrichi :** formules en LaTeX `$...$` et `$$...$$`, figures vectorielles SVG inline intégrées directement dans les fichiers `.md`.
- **Diagrammes structurels :** blocs `mermaid` pour les arbres de probabilités, flux algorithmiques et classifications.
- **Typst pour l'édition de référence (PDF) :** typographie soignée, pagination continue, table des matières dynamique, index des notions et bibliographie patrimoniale complète.


---

## 6. LICENCE ET DIFFUSION LIBRE

L'ensemble de l'œuvre (*La Voie du Nombre* et *Le Guide de l'Accompagnateur*), textes, figures vectorielles et scripts de compilation, est publié sous licence **Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)**.
- Le code source Markdown et les figures SVG sont hébergés et versionnés sur un dépôt GitHub public.
- Les auteurs encouragent la redistribution, l'adaptation et la réutilisation pédagogique sous réserve de mention des crédits originaux et de partage sous licence identique.
