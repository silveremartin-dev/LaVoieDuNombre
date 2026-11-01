# AGENTS.MD — MANIFESTO, PEDAGOGICAL OBJECTIVES, AND DESIGN DIRECTIVES
## Project: "THE WAY OF THE NUMBER — A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics"

> This document defines the intellectual architecture, fundamental pedagogical objectives, analysis of cognitive obstacles, and operational protocols that any agent (human or AI) must respect when writing, revising, or expanding the collection.

---

## 1. TITLE AND IDENTITY OF THE WORK

- **Official Title:** *THE WAY OF THE NUMBER* (*La Voie du Nombre*)
- **Subtitle:** *A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics*
- **Companion Book:** *THE COMPANION GUIDE — Didactic Foundations, Epistemological Pillars, and Practical Keys* (*Le Guide de l'Accompagnateur*)
- **Architecture:** 58 chapters distributed across 6 progressive learning volumes (Grade 1 / CP to Grade 12 / Terminale Spécialité & Advanced Mathematics).

---

## 2. THE THREE MAJOR EPISTEMOLOGICAL IMPERATIVES (FROM THE INDEPENDENT AUDIT)

The independent epistemological and didactic audit established three guiding principles that must govern any contribution:

### A. Overcoming the "Metaphorical Obstacle" (Bachelard / Brousseau vs. Lakoff)
Embodied physical metaphors (the heap of pebbles, walking along the trail, the brick rectangle, the ski board) are indispensable for sparking comprehension without paralysis. **However, every physical metaphor becomes an epistemological obstacle if it is not emancipated at the appropriate moment.**
- *The limit of the rectangle:* multiplication is initially introduced as a rectangular area ($4 \times 6 = 24$). But this imagery collapses when multiplying two negative numbers ($(-3) \times (-5) = +15$) or probabilities ($\frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$). The student must grasp that the sign rule stems from the **algebraic consistency of distributivity**, and not from an impossible geometry with negative surfaces.
- *The limit of the skier:* the derivative visualized as a ski board under the soles works for smooth curves ($C^1$). It becomes a trap when facing sharp corners ($|x|$ at 0) or oscillating functions ($x^2 \sin(1/x)$).
- **Golden Rule:** Sensible experience is the launch scaffold; as soon as the tool has been practiced, the agent must make explicit the transition toward autonomous logical formalism.

### B. Working Memory Management and Cognitive Load Symmetry
- *Verbal drift:* by attempting to explain everything through lengthy narrative prose, the work risks exhausting a 16–17-year-old student faced with chapters of 50 to 70 KB.
- **Golden Rule:** Historical and human narrative must immediately be followed by:
  1. Structured reflex summary cards ("Core Takeaways / What You Need to Remember").
  2. Clear algorithmic decision trees.
  3. **Mechanical automation drills** to free 100% of working memory before tackling complex problems.

### C. The Dead-End of "All-Text" Geometry: Primacy of Vector Graphics
- Geometry cannot be taught through text alone or typographical ASCII approximations.
- According to Duval's theory of semiotic registers, geometric insight emerges from constant back-and-forth between visual diagrams and algebraic equations.
- **Golden Rule:** Every chapter in geometry, analysis, or kinematics must include sharp vector figures (SVG natively embedded within Markdown, high-precision Typst/CeTZ diagrams in PDF, Mermaid diagrams for probability trees and decision flowcharts, and relevant curated illustrations).

---

## 3. THE DOCTRINE OF THE "EDGE-CASE LABORATORY"

To avoid overloading the student's cognitive bandwidth during initial skill acquisition, pathological cases must be **isolated**:
1. **Step 1 — The Core Reflex:** The general rule is first learned on robust, standard cases (e.g., $4 \times 3 = 12$, derivative of a polynomial, division by a non-zero positive integer).
2. **Step 2 — The Edge-Case Enclosure:** In a dedicated separate subsection (`🛠️ The Edge-Case Laboratory`), boundary conditions are explored without polluting the core reflex:
   - What happens with $4 \times 0$? What is $0 \times 0$?
   - Why is $\frac{0}{5} = 0$, but $\frac{5}{0}$ is strictly undefined and impossible?
   - Why is $a^0 = 1$, and why is $0^0$ an indeterminate form?
   - Why does the zero vector $\vec{0}$ have zero magnitude and all directions simultaneously?

---

## 4. OLIVER BYRNE'S COLOR SEMIOTIC CHARTER (1847)

All SVG diagrams and book illustrations adhere to a functional color code:
- **Blue (#1d4ed8):** Driving motor action, horizontal forward motion, abscissa axis $x$, first vector $\vec{u}$, horizontal side.
- **Red (#b91c1c):** Vertical constraint, height $y$, obstacle, reaction, second vector $\vec{v}$.
- **Yellow / Amber (#d97706):** Product, internal surface area, energy, cross-term $2ab$, quotient.
- **Green (#15803d):** Overall balance (Chasles' relation), validation, final result, stable tangent.
- **Black / Slate (#0f172a):** Anchoring framework, neutral axes, background grid.

---

## 5. TECHNOLOGIES AND EXPORT FORMATS

- **Enriched Markdown:** LaTeX formulas `$...$` and `$$...$$`, inline SVG vector figures natively integrated directly in `.md` files.
- **Structural Diagrams:** `mermaid` code blocks for probability trees, algorithmic flows, and conceptual classifications.
- **Typst for the Definitive Reference Edition (PDF):** meticulous typography, continuous pagination, dynamic table of contents, concept index, and comprehensive heritage bibliography.

---

## 5 bis. LAYOUT AND EDITORIAL FOLIATION

1. **Editorial Foliation (Page Numbering):**
   - *Counting vs. Display:* The entire interior block is counted, but folios are visible only on body text pages.
   - *Covers excluded from counting:* Covers 1, 2, 3, and 4 (front cover, inside covers, back cover) are never counted or numbered; the front cover is **never** page 1.
   - *Page 1 = first recto page of interior block:* p. 1 half-title (recto), p. 2 blank (verso), p. 3 full title, p. 4 copyright/legal notices, p. 5 epigraph/dedication, p. 6 blank, then table of contents — all counted but **mute** (no printed page number).
   - *Recto/Verso:* Odd pages on the right, even pages on the left. Every opening of a part, volume, chapter, or appendix starts on a recto (odd) page and remains mute in the header; the first visible folio appears on the subsequent page (or in the footer for chapter openers).
   - *Blank pages:* Counted in arithmetic order, never displaying folios or running headers.
   - *Placement:* Folios centered or placed on the outer margin (left on even pages, right on odd pages), **never on the inner gutter (binding side)**.
   - *Block ending:* The interior block ends on an even page (verso), followed by inside back cover (Cover 3) and back cover (Cover 4).

---

## 6. OPEN LICENSING AND FREE DISTRIBUTION

The entire work (*The Way of the Number* and *The Companion Guide*), including texts, vector graphics, and compilation scripts, is released under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.
- The Markdown source code and SVG figures are hosted and versioned on a public GitHub repository.
- The authors encourage redistribution, adaptation, and pedagogical reuse, provided original credits are attributed and derivatives are shared under an identical license.
