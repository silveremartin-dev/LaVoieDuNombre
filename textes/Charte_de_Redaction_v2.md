# CHARTE DE RÉDACTION — ÉDITION APPROFONDIE (V2)

Cette charte s'applique à **tous** les chapitres de la V2. Le plan de référence est `v2/Plan_de_Cours_Global_v2.md`. Les chapitres V1 (dossier parent `livre_mathematiques/`) servent de matière première : on garde leurs scènes, histoires vraies et métaphores, mais on les **approfondit largement**.

## 1. Esprit (inchangé)
- Les maths naissent d'un **problème concret** (survie, partage, construction, navigation, commerce, physique) que les outils précédents ne savent pas résoudre. Le chapitre montre la crise, puis l'invention, puis ses **limites** qui ouvrent le chapitre suivant.
- Les idées viennent du **corps et du geste** (cailloux, pas, balance, découpage, rotation, zoom, skieur...) avant les symboles.
- **Aucun nom de théoricien de la pédagogie** dans le texte élève (pas de Piaget, Lakoff, Núñez, Brousseau, Russell en tant que pédagogue). Les mathématiciens historiques sont, eux, bienvenus.
- Le ton **grandit avec le lecteur** : phrases courtes et tutoiement chaleureux à 6 ans ; ton de jeune chercheur à 17 ans, avec rigueur et vocabulaire officiel.

## 2. Ce qui manquait en V1 et qu'il faut absolument fournir
1. **Chaque notation est expliquée à sa première apparition** : ce qu'elle signifie, comment elle se lit à voix haute, pourquoi elle a cette forme, qui l'a inventée si c'est intéressant (ex. : $f'(x)$ « f prime de x » de Lagrange ; $\frac{dy}{dx}$ de Leibniz ; $\lim_{h \to 0}$ ; $\int$ = S allongé de « somme » ; $\sum$ ; $n!$ ; $\binom{n}{k}$ ; $\in$, $\mathbb{R}$, $[a;b[$...).
2. **Exemples résolus nombreux** : au moins 4 à 8 « Exemples résolus » détaillés pas à pas par chapitre (plus pour le lycée), allant du plus simple au plus riche.
3. **Cas limites et pièges** : une section « Aux limites » ou « Attention, piège ! » dans chaque grande partie : où la règle cesse de marcher, erreurs classiques, contre-exemples (ex. : division par zéro, $\sqrt{a+b} \neq \sqrt a + \sqrt b$, fonction continue non dérivable comme $|x|$ en 0, $\frac{0}{0}$, $\Delta < 0$, suite bornée non convergente, etc.).
4. **Approfondissement** : définition intuitive → définition précise → propriétés → preuve (visuelle ou rédigée, adaptée à l'âge) → méthode → applications. Pour le lycée, donner **les démonstrations exigibles du programme**.
5. **Exercices abondants et gradués** : une section finale « Exercices » avec au moins :
   - Volumes I–II : 12 à 20 exercices (jeux, manipulations, petits problèmes) ;
   - Volumes III–IV : 15 à 25 exercices ;
   - Volumes V–VI : 20 à 30 exercices dont des exercices type contrôle/Bac.
   Classés en ★ (application directe), ★★ (réflexion), ★★★ (défi). **Corrigés** dans une section « Solutions » en fin de chapitre (détaillés pour ★★ et ★★★, réponse brève pour ★).
6. **Couverture du programme officiel** : tout ce qui est listé pour le chapitre dans le plan V2 doit être traité, avec le vocabulaire officiel français (ex. « coefficient directeur », « ordonnée à l'origine », « discriminant », « hérédité »).

## 3. Structure type d'un chapitre
```
# VOLUME X — Titre du volume (âge / classes)
## CHAPITRE N : Titre
> Citation / phrase d'ouverture

### Ce que tu vas découvrir  (3-6 puces, langage simple)
### 1. Le problème  (scène concrète, histoire)
### 2..k. Parties de cours  (avec : idée intuitive, notation expliquée,
         définition encadrée, Exemples résolus, « Aux limites / Attention, piège ! »,
         « L'histoire vraie », « Le savais-tu ? », expériences « À toi de jouer »)
### Ce qu'il faut retenir  (fiche résumé : définitions, formules, méthodes)
### Exercices  (★ / ★★ / ★★★)
### Solutions
### La question qui ouvre la suite  (lien vers le chapitre suivant)
```
- Pour le lycée : ajouter des encadrés « Méthode » (comment rédiger), « Démonstration », et des mini-scripts **Python** quand le programme le prévoit (suites, seuils, dichotomie, Euler, simulation, Monte-Carlo).

## 4. Forme
- Markdown, maths en LaTeX `$...$` et `$$...$$`. Schémas en ASCII dans des blocs ``` quand c'est utile.
- Encadrés sous forme de citations Markdown avec titre en gras, ex. :
  `> **📐 Définition —** ...`, `> **⚠️ Attention, piège !** ...`, `> **🔍 L'histoire vraie —** ...`, `> **💡 Le savais-tu ?** ...`, `> **🧭 Méthode —** ...`, `> **✍️ Démonstration —** ...`.
- **Longueur visée** : Volume I : 15–25 Ko par chapitre ; Volume II–III : 20–35 Ko ; Volume IV : 25–40 Ko ; Volumes V–VI : 35–60 Ko par chapitre. La profondeur prime sur la longueur, mais un chapitre de Terminale de 9 Ko est inacceptable.
- Français soigné, accents corrects. Exactitude mathématique impérative : vérifier chaque calcul et chaque solution.
- Fichiers : `livre_mathematiques/v2/Volume_<Romain>/Chapitre_<NN>_<Titre_sans_accents_avec_underscores>.md` (NN sur deux chiffres).
