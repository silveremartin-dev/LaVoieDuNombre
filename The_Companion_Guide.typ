#set document(
  title: "THE WAY OF THE NUMBER — The Companion Guide",
  author: "Silvère Martin-Michiellot & Antigravity"
)

#set page(
  paper: "a4",
  margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 [
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[THE WAY OF THE NUMBER — The Companion Guide],
        text(size: 8.5pt, fill: rgb("#64748b"), font: "Liberation Sans")[Didactic Foundations & Practical Keys]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    let page-num = counter(page).get().first()
    [
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      #v(2pt)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#94a3b8"), font: "Liberation Sans")[A Constructive & Embodied Pedagogy],
        text(size: 8.5pt, fill: rgb("#1e293b"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      )
    ]
  }
)

#set text(
  font: ("Liberation Serif", "Times New Roman", "Georgia"),
  size: 9.5pt,
  lang: "en"
)

#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 1.3em
)

// Oliver Byrne (1847) Editorial Palette
#let c-blue = rgb("#1d4ed8")
#let c-red = rgb("#b91c1c")
#let c-amber = rgb("#d97706")
#let c-dark = rgb("#0f172a")
#let c-green = rgb("#15803d")
#let c-purple = rgb("#7e22ce")

// Didactic Callout Blocks
#let principle(title, body) = block(
  fill: rgb("#f0f9ff"),
  stroke: (left: 4pt + c-blue),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-blue, size: 9pt)[🏛️ EPISTEMOLOGICAL PRINCIPLE: #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

#let vigilance(title, body) = block(
  fill: rgb("#fef2f2"),
  stroke: (left: 4pt + c-red),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-red, size: 9pt)[⚠️ DIDACTIC VIGILANCE: #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

#let workshop(title, body) = block(
  fill: rgb("#fefce8"),
  stroke: (left: 4pt + c-amber),
  inset: (x: 12pt, y: 8pt),
  radius: (right: 4pt),
  width: 100%,
  [
    #text(weight: "bold", fill: c-amber, size: 9pt)[🛠️ WORKSHOP PRAXIS: #title]
    #v(3pt)
    #set text(size: 8.5pt)
    #body
  ]
)

// ==========================================
// COMPANION GUIDE COVER
// ==========================================
#align(center)[
  #v(1.5cm)
  #text(size: 11pt, weight: "bold", fill: c-blue, tracking: 3pt)[PEDAGOGICAL ENGINEERING HANDBOOK FOR MENTORS AND TEACHERS]
  #v(0.6cm)
  #text(size: 26pt, weight: "bold", fill: c-dark)[THE WAY OF THE NUMBER]
  #v(0.2cm)
  #text(size: 18pt, weight: "bold", fill: c-purple)[The Companion Guide]
  #v(0.2cm)
  #text(size: 11pt, style: "italic", fill: rgb("#475569"))[Didactic Foundations, Epistemological Pillars, and Practical Keys\ (From the First Pebble to Advanced Mathematics)]
  #v(0.4cm)
  #text(size: 11pt, weight: "bold", fill: c-blue)[Silvère Martin-Michiellot & Antigravity]
  #v(0.6cm)
  #line(length: 45%, stroke: 2pt + c-amber)
  #v(0.8cm)
]

#block(
  fill: rgb("#f8fafc"),
  inset: 14pt,
  radius: 6pt,
  stroke: 1pt + rgb("#e2e8f0"),
  [
    #align(center)[
      #text(size: 10pt, style: "italic", fill: rgb("#334155"))[
        “Mathematics is not taught by pouring lukewarm water into a passive vessel. A child truly understands only what they have first experienced with their muscles, constructed with their hands, and reinvented to overcome real resistance from the physical world. The adult’s role is to ensure that the concrete tool does not become a cage, and that bodily action elevates into pure logical light.”
      ]
    ]
  ]
)

#v(0.8cm)
#outline(title: [Table of Contents], indent: 1.5em, depth: 2)
#pagebreak()

= PART I — THE EPISTEMOLOGICAL ENGINE: THE FOUR SCIENTIFIC PILLARS

Why does the collection *The Way of the Number* deliberately reject traditional lecture-based exposition? This guide discloses the four scientific foundations governing the instructional progression.

== 1. Jean Piaget: Genetic Epistemology and Operational Reversibility
The human brain does not leap over developmental stages. Enforcing abstract formulas (formal stage) onto a child still situated in the concrete operational stage induces acute cognitive paralysis.
- *Ages 6–8 (Volume I):* Direct sensory manipulation of physical objects (pebbles, egg cartons, two-pan balance scale, chocolate bars).
- *Ages 8–11 (Volume II):* Conservation of substance and area (sharing cakes, unit fractions, sand excavations).
- *Ages 11–15 (Volumes III & IV):* Transition to formal thought, mental experiments, unknown $x$ as a sealed mystery pouch.
- *Ages 15–18 (Volumes V & VI):* Formal deductive reasoning, free vectors, function machines $f(x)$, complex units $i$, continuous differential flows.

#principle([Operational Reversibility])[
A mathematical concept is robust only when the learner realizes that the inverse operation restores the initial state: addition is illuminated by subtraction, multiplication by division, and differentiation by integration.
]

== 2. George Lakoff & Rafael Núñez: Embodied Metaphors
All abstract mathematical thoughts originate in sensorimotor projections:
- *Object Collection (Volumes I & II):* A number is a physical heap of stones; addition is stacking.
- *Path Traversal (Volumes II to VI):* A number is a forward step along a trail. Moving East $= +$; moving West $= -$. Facing West ($-1$) and stepping backward ($-1$) propels the body East ($+1$): the nightmare of $(-1) times (-1) = +1$ dissolves through a single physical movement.
- *The Workshop Machine (Volumes V & VI):* A mathematical function $f$ is an automated processing machine transforming raw material $x$ into a finished product $f(x)$.
- *The Infinite Microscope (Volume VI):* Any smooth curve examined under sufficient magnification becomes indistinguishable from a straight line (the curved Earth appears locally flat beneath our feet).

== 3. Oliver Byrne (1847): Chromatic Semiotics
Replacing abstract monochrome letters with functional primary colors enables the human visual cortex to validate geometric proofs in a twentieth of a second:
- *Royal Blue (\#1d4ed8):* Positive motor action, Horizontal displacement, $x$-abscissa, base vector.
- *Vermilion Red (\#b91c1c):* Constraint, Vertical height $y$, physical reaction, divisor.
- *Golden Amber (\#d97706):* Product, Interior Area, Energy, remainder, cross-product $2 a b$.
- *Emerald Green (\#15803d):* Validation, overall resultant, Chasles' relation, tangent line.
- *Deep Slate (\#0f172a):* Reference skeleton, coordinate axes, neutral background grid.

== 4. Guy Brousseau & Gaston Bachelard: Obstacles and Crises
A new mathematical concept never arrives by arbitrary decree: it is born from the failure of the preceding tool to handle an authentic crisis:
- Tallying by direct sight fails at 5 objects $arrow.r$ birth of the physical tally counter (*calculus*).
- Repeated addition is too slow under incoming bad weather $arrow.r$ birth of the multiplicative rectangle.
- Whole numbers fail to distribute 2 fish among 4 hunters $arrow.r$ birth of fractional units.
- Fractions fail to measure the diagonal of a 1-meter square $arrow.r$ birth of irrational numbers ($sqrt(2)$).
- The real number line cannot solve $x^2 = -1$ $arrow.r$ birth of the complex imaginary unit $i$.

#pagebreak()

= PART II — THE INDEPENDENT CRITICAL AUDIT: THREE CRUCIAL VIGILANCES

The external didactic evaluation committee established three golden rules for mentors:

== 1. Surpassing the Metaphorical Obstacle (Bachelard vs. Lakoff)
Bodily metaphor is indispensable to spark initial intuition, but it turns into a rigid obstacle if the learner cannot transcend it:
- *The Rectangle Limitation:* Viewing multiplication as a physical area ($4 times 6 = 24$) collapses before negative products $(-3 times -5 = +15)$ or probabilities. The mentor must make clear that the sign rule is necessitated by the *algebraic consistency of the distributive law*.
- *The Skier Limitation:* The skier model for derivatives presupposes a smooth slope. It breaks down at corners ($|x|$ at $0$) and oscillating functions. The mentor must guide the student from physical sensation to the formal limit of the difference quotient.

== 2. Working Memory and Mechanical Drills
Working memory holds only 4 to 7 informational chunks simultaneously (Miller's law, Sweller).
- If a high school senior must mentally search for $7 times 8 = 56$ during an integration by parts, working memory saturates and understanding collapses.
- The mentor will therefore ensure that *Practitioner Fluency Drills* are practiced diligently: standard vertical algorithms, times tables, binomial expansions, and basic derivatives must become instant spinal reflexes.

== 3. The Primacy of Visual Geometry (Duval's Registers)
Geometric intuition emerges from constant translation between graphic diagrams and symbolic equations. The mentor will always have students draw and color figures before setting up algebraic formulas.

#pagebreak()

= PART III — CONDUCTING THE WORKSHOP & THE EDGE CASES DOCTRINE

#vigilance([The Golden Rule: The Isolated Edge Cases Laboratory])[
To never destabilize a student during the acquisition of a new procedure, edge cases ($4 times 0$, division by zero, exponent zero, null vector) must *never* be introduced in the opening lesson.
They are always examined subsequently, in a dedicated enclosure titled *The Edge Cases Laboratory*, approached as an intriguing engineering puzzle.
]

== 1. Volume I (Ages 6–8): The Hand, the Balance Scale, and the Brick Wall
- *Vertical Arithmetic:* Utilize a two-column box (Tens / Units). Never mention “carrying over” without executing the physical exchange of 10 pebbles for 1 cork marker.
- *Vertical Multiplication:* Highlight the placeholder zero in red when moving to the tens row ($146 times 23$).
- *The Zero Edge Case:* Illustrate $4 times 0 = 0$ by flattening the area rectangle to zero height (zero as an absorbing element).

== 2. Volume II (Ages 8–11): The Market and the Division Bracket
- *The Long Division Algorithm:* Drill the four-beat sequence *D-M-S-B* (Divide, Multiply, Subtract, Bring down).
- *Two-Digit Divisors ($7 thin 845 div 23$):* Mandate the preliminary drafting of the divisor's multiples on scratch paper ($23 times 1, 23 times 2, 23 times 3dots$).
- *The Quotient Zero Trap ($615 div 3 = 205$):* Emphasize that whenever a digit is brought down, a digit MUST be inscribed in the quotient, even if it is zero.
- *Division by Zero:* Prove why $0 div 5 = 0$, but $5 div 0$ is strictly impossible ($0 times q = 5$ has no solution).

== 3. Volume IV (Ages 13–15): Identities and Inequalities
- *Binomial Identities:* Have the student sketch the partitioned square to visually demonstrate that $(a+b)^2 eq a^2 + b^2$ and permanently fix the $2 a b$ cross-term.
- *Inequalities:* Physically show why multiplying by a negative flips the sign ($<$ becomes $>$) through reflection across the origin.

== 4. Volumes V & VI (Ages 15–18): Vectors, Flux, and Integrals
- *Dot Product:* Do not settle for $x x' + y y'$. Illustrate effective work: the barge towline hauled along a canal by a horse.
- *Complex Numbers:* Introduce $i$ as a geometric $90^circle$ quarter-turn operator in the Cartesian plane.
- *Integrals:* Differentiation slices Kepler's wine barrel with a scalpel; integration stitches the slices back with a golden thread.

#pagebreak()

= PART IV — BRIDGING WITH CURRICULA AND HIGH-STAKES EXAMINATIONS

To ensure top academic honors on national and international examinations, mentors must strictly uphold three canonical proof formats:
1. *Mathematical Induction:* Explicit base case verification, ritual formulation of the induction hypothesis for a fixed integer $n$, and formal closing declaration.
2. *Intermediate Value Theorem (IVT):* Rigorous verification of the 3 requirements: continuous function, strictly monotonic on the interval, and intermediate target value.
3. *Vector Formatting:* Mandatory arrow accents ($arrow(u), arrow(A B)$), and careful distinction between geometric direction (line of support) and sense (arrowhead orientation).

= PATRIMONIAL BIBLIOGRAPHY & AUTHORITATIVE REFERENCES

1. *Gaston Bachelard*, The Formation of the Scientific Mind (1938).
2. *Guy Brousseau*, Theory of Didactical Situations in Mathematics (1997).
3. *Oliver Byrne*, The First Six Books of the Elements of Euclid (London, 1847).
4. *Michel Chasles*, Historical Overview of the Origin and Development of Geometric Methods (1837).
5. *Raymond Duval*, Semiosis and Human Thinking (1995).
6. *George Lakoff & Rafael Núñez*, Where Mathematics Comes From (2000).
7. *Jean Piaget*, Genetic Epistemology (1970).
8. *Simon Stevin*, De Thiende / The Tenth (Leiden, 1585).
9. *Al-Khwarizmi*, The Compendious Book on Calculation by Completion and Balancing (Baghdad, c. 820).
