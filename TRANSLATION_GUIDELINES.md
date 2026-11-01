# TRANSLATION GUIDELINES & INTERNATIONAL ROADMAP
## Official Title, Mathematical Notation Equivalences & 1:1 Translation Protocol
### Reference French Edition: *LA VOIE DU NOMBRE* — International English Edition: *THE WAY OF THE NUMBER*

> This document defines the definitive editorial identity, mathematical notation conversion matrix, terminology glossary, and layout rules for the translation and international adaptation of *La Voie du Nombre* (*The Way of the Number*).

---

## 1. OFFICIAL TITLES & EDITORIAL IDENTITY

- **French Reference Edition:**
  - **Title:** **LA VOIE DU NOMBRE**
  - **Subtitle:** *Une Odyssée Constructive, du Premier Caillou aux Mathématiques Avancées du Lycée*
  - **Companion Book:** *Le Guide de l'Accompagnateur — Fondements Didactiques, Piliers Épistémologiques et Clés Pratiques*
- **International English Edition:**
  - **Title:** **THE WAY OF THE NUMBER**
  - **Subtitle:** *A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics*
  - **Companion Book:** *The Companion Guide — Didactic Foundations, Epistemological Pillars, and Practical Keys*
- **Pedagogical Mission:** An ambitious mathematical journey spanning elementary arithmetic to advanced calculus and linear algebra, structured around 58 chapters and 6 progressive volumes. It overcomes metaphorical obstacles through physical scaffolding and ascends to autonomous mathematical formalism.

---

## 2. MATHEMATICAL NOTATION EQUIVALENCES (FR $\leftrightarrow$ EN)

| Concept | French Notation (FR) | International / Anglo-American (EN) | Typst Syntax & Rules |
| :--- | :--- | :--- | :--- |
| **Open Interval** | $]a, b[$ | $(a, b)$ or $]a, b[$ | Preserve clean brackets or use standard Typst delimiters. Never let `lr(]` split across lines. |
| **Half-Open Interval** | $[a, b[$ or $]a, b]$ | $[a, b)$ or $(a, b]$ (or $[a, b[$, $]a, b]$) | Keep notation consistent within the chapter. |
| **Decimal Separator** | Virgule : $3{,}14$ | Point : $3.14$ | Use decimal dot $3.14$ in prose and math in the English edition. |
| **Thousands Separator** | Espace insécable : $10~000$ | Comma or thin space : $10{,}000$ or $10\,000$ | Standard English: $10{,}000$. |
| **Vector Notation** | $\vec{u}$ or $\overrightarrow{A B}$ | $\vec{u}$ or $\mathbf{u}$, $\overrightarrow{AB}$ | Typst: `arrow(u)` or `arrow(A B)`. |
| **Dot Product** | $\vec{u} \cdot \vec{v}$ | $\mathbf{u} \cdot \mathbf{v}$ or $\vec{u} \cdot \vec{v}$ | Typst: `arrow(u) dot arrow(v)`. |
| **Cross Product** | $\vec{u} \wedge \vec{v}$ | $\mathbf{u} \times \mathbf{v}$ | Typst: `arrow(u) times arrow(v)`. |
| **Differential Operator** | $d x$ (italique ou droit) | $\mathrm{d}x$ | Typst: `thin d x`. |
| **GCD / LCM** | $\mathrm{PGCD} / \mathrm{PPCM}$ | $\gcd / \mathrm{lcm}$ | Typst: `gcd(a, b)` and `lcm(a, b)`. |

---

## 3. CORE MATHEMATICAL TERMINOLOGY GLOSSARY

| French Mathematical Term | Official English Equivalent | Common Pitfalls to Avoid |
| :--- | :--- | :--- |
| **Théorème des Valeurs Intermédiaires (TVI)** | Intermediate Value Theorem (IVT) | Do not invent literal translations. |
| **Théorème de la bijection / Corollaire du TVI** | Monotone Function Theorem / IVT Corollary | Standard high-school terminology. |
| **Sens de variation** | Monotonicity / Trend / Increasing-Decreasing nature | Never write "sense of variation". |
| **Tableau de variations** | Sign and variation chart / Derivative sign table | Translate all column headers ($x$, $f'(x)$, $f(x)$). |
| **Tangente horizontale** | Horizontal tangent ($f'(x_0) = 0$) | Always check extrema and saddle points. |
| **Nombre dérivé** | Derivative value at a point / Instantaneous rate of change | Distinguish from the derivative function $f'$. |
| **Primitive** | Antiderivative / Indefinite integral | In English high schools, "antiderivative" is standard. |
| **Intégration par parties (IPP)** | Integration by parts (IBP) | $\int u v' = u v - \int u' v$. |
| **Suite arithmétique / géométrique** | Arithmetic / Geometric sequence (or progression) | Note: sequence = *suite*, series = *série* ($\sum$). |
| **Raison d'une suite** | Common difference ($r$, arithmetic) / Common ratio ($q$, geometric) | "Reason" is an unacceptable false friend. |
| **Identités remarquables** | Special algebraic identities / Polynomial identities | $(a+b)^2 = a^2 + 2ab + b^2$, etc. |
| **Produit en croix** | Cross-multiplication | Rule of three / proportional cross-multiplication. |
| **Équation cartésienne** | Cartesian equation (e.g. $a x + b y + c = 0$) | Standard coordinate geometry. |
| **Repère orthonormé** | Orthonormal coordinate system / Cartesian plane | Axes perpendicular with identical unit length. |
| **Loi binomiale** | Binomial distribution $\mathcal{B}(n, p)$ | Notation: $X \sim \mathcal{B}(n, p)$. |
| **Espérance / Variance / Écart-type** | Expected value (Mean) / Variance / Standard deviation | $E(X)$, $V(X)$, $\sigma(X)$. |

---

## 4. OLIVER BYRNE COLOR SEMIOTIC CHARTER (1847)

All figures in `figures/` and `figures_en/` adhere to the functional color charter:

| Role / Concept | Hex Code | Primary Usage |
| :--- | :--- | :--- |
| **Driving Motor Action / Abscissa** | `#1d4ed8` (Royal Blue) | Horizontal movement, $x$-axis, primary vector $\vec{u}$, width. |
| **Vertical Constraint / Obstacle** | `#b91c1c` (Crimson Red) | Vertical coordinate $y$, height, reaction force, secondary vector $\vec{v}$. |
| **Product / Internal Area / Work** | `#d97706` (Amber / Gold) | Rectangular area, energy, cross-term $2ab$, scalar work $W = \vec{F}\cdot\vec{d}$. |
| **Equilibrium / Final Result / Tangent** | `#15803d` (Emerald Green) | Chasles' relation balance, stable tangent, verified solution. |
| **Neutral Grid / Framework** | `#0f172a` (Slate / Ink) | Coordinate grid, bounding boxes, labels, neutral text. |

---

## 5. DIDACTIC CALLOUT MACROS (1:1 CORRESPONDENCE)

| Macro | Color / Theme | French Role | English Usage |
| :--- | :--- | :--- | :--- |
| `#principe(title: [...])[...]` | Blue (`#1d4ed8`) | Définition fondamentale, Règle | Fundamental Definition, Core Rule |
| `#alerte(title: [...])[...]` | Red (`#b91c1c`) | Attention au piège !, Vigilance | Caution: Classic Trap!, Watch Out! |
| `#cas_limite(title: [...])[...]` | Yellow / Amber (`#d97706`) | Cas limite, Laboratoire frontière | Boundary Case & Edge-Case Lab |
| `#methode(title: [...])[...]` | Purple (`#7c3aed`) | Méthode pas à pas, Algorithme | Step-by-Step Method, Algorithm |
| `#exemple_resolu(title: [...])[...]` | Green (`#15803d`) | Exemple résolu, Application directe | Step-by-Step Worked Example |
| `#decouvre(title: [...])[...]` | Teal / Bronze (`#0284c7`) | Histoire des maths, Le savais-tu ? | Discovery, Historical Context |

---

## 6. ASSET PAIRING AND DIRECTORY ARCHITECTURE

- **Figures FR:** `figures/vol_1/` to `figures/vol_6/`, `figures/histoire/`, `figures/nature/`.
- **Figures EN:** `figures_en/vol_1/` to `figures_en/vol_6/`, `figures_en/histoire/`, `figures_en/nature/`.
- **File Names:** Strictly 1:1 identical (e.g. `figures/vol_5/fig_37_cercle_trigo_quadrants.svg` $\leftrightarrow$ `figures_en/vol_5/fig_37_cercle_trigo_quadrants.svg`).
- **Zero French Residuals:** Every `<text>` and `<tspan>` in `figures_en/` must be 100% in English.
- **Strict XML Integrity:** Escape all `<` as `&lt;` and `&` as `&amp;` to ensure Typst builds without SVG parser failures.
