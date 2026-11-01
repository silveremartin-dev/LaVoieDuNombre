# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 34: The Jacquard Loom and the Function Box

> *“A function is not a frozen drawing in a book. It is a living machine: you slide a raw block of metal into the input slot, the cogs turn, the mechanical rule executes, and a finely crafted part emerges on the conveyor belt. Modern mathematics is the great workshop where these transformations unfold.”*

---

### What You Are About to Discover

- How the invention of punched cards by **Joseph Marie Jacquard** in Lyon and the brilliant insight of **Ada Lovelace** gave birth to the modern concept of a function.
- The fundamental vocabulary: **preimage (antécédent)**, **image**, **domain of definition** $\mathcal{D}_f$, and the ironclad rule of image uniqueness.
- How to construct and interpret a **function curve (graph)**, a table of values, and a **table of variations**.
- The concepts of **maximum**, **minimum** (local and global), and **parity** (even and odd functions, symmetries in the coordinate plane).
- A complete study of the **five parent (reference) functions**: the square function ($x^2$), the reciprocal function ($\frac{1}{x}$), the square root function ($\sqrt{x}$), the cube function ($x^3$), and the absolute value function ($|x|$).
- Solving equations $f(x) = k$, $f(x) = g(x)$, and inequalities graphically, along with the **composition** of function machines $g \circ f$.

---

### 1. The Problem: The Silk Weavers of Lyon and Ada Lovelace's Cards

At the very opening of the nineteenth century, on the steep hillsides of the Croix-Rousse in Lyon, France, the silk workshops of the *canuts* (silk weavers) echoed with the deafening clatter of wooden shuttles.

To weave a rich damask brocade embroidered with crimson roses and silver leaves, two workers were required at every loom: the master weaver seated before the reed, and a young child huddled in the dust below (the draw-boy or “draw-girl”) who pulled drawstrings by hand to raise warp threads one by one. The labor was grueling, ruinous to eyesight and posture, and a single moment of distraction by the child created an irreversible knot across the luxurious fabric.

In **1801**, the son of a Lyon weaver, **Joseph Marie Jacquard**, unveiled an automated mechanism that astonished Europe:
He replaced the draw-boy with an endless loop of **punched cardboard cards** linked together in a chain.
- A hole in the card? A needle passes through freely: the hook engages, lifting the silk thread.
- No hole? The solid card pushes the needle back: the silk thread remains lowered.

The Jacquard loom was the first programmable machine in human history!

```
    [ Punched Card ] ───► ┌──────────────────────────┐ ───► [ Patterned Silk ]
       (Input x)          │    The Jacquard Loom     │         (Output f(x))
                          │    (Mechanical Rule)     │
                          └──────────────────────────┘
```

In **1843**, in London, a young mathematician of extraordinary vision, **Ada Lovelace** (the only legitimate child of the poet Lord Byron), studied the mechanical blueprints of Charles Babbage's “Analytical Engine.” She immediately saw the profound parallel with the Lyon silk mills and penned this famous observation:
> *“We may say most aptly that the Analytical Engine weaves algebraical patterns just as the Jacquard-loom weaves flowers and leaves.”*

Ada Lovelace then drafted an algorithm for computing Bernoulli numbers: she had just composed the **world's very first computer program**.

What Jacquard realized in cardboard and Ada Lovelace formalized in thought is the very soul of what mathematicians define as a **Function**.

---

### 2. Anatomy of a Function: Vocabulary and Domain

#### 2.1 The Black Box ($x \mapsto f(x)$)

Put aside complicated graphs for a moment. Picture an **uncompromising industrial machine**:

```
             x (Raw input material: PREIMAGE / ANTÉCÉDENT)
             │
             ▼
      ┌───────────────┐
      │   Machine f   │   Rule: "Take input, multiply by 3,
      │               │          then subtract 5"
      └───────────────┘
             │
             ▼
           f(x) = 3x - 5  (Finished output part: IMAGE)
```

> **📐 Fundamental Definitions —**
> 1. A **function** $f$ is a mathematical process that assigns to each real number $x$ in a given set **at most one** unique real number, denoted $f(x)$.
> 2. We write:
>    $$f : x \mapsto f(x)$$
>    Read aloud as: “the function $f$ mapping $x$ to $f$ of $x$.”
> 3. **The Preimage (Antécédent):** the input number $x$ fed into the machine at the start.
> 4. **The Image:** the resulting output number $f(x)$ emerging at the end.

> **⚠️ Ironclad Rule — Uniqueness of the Image.**
> - A number $x$ has **at most one single image** under a function $f$. If you load the exact same flour into the oven under identical settings, two different loaves cannot emerge simultaneously!
> - Conversely, an output number $y$ may have **none, one, or several preimages**. For example, for the squaring machine ($f(x) = x^2$):
>   - The number $9$ has two preimages: $3$ and $-3$ (since $3^2 = 9$ and $(-3)^2 = 9$).
>   - The number $-4$ has no real preimage (no real square is negative).

#### 2.2 The Domain of Definition $\mathcal{D}_f$: Forbidden Values

All real machines have operating tolerances: drop a heavy iron crowbar into a small plastic coffee grinder, and the grinder shatters.
In mathematics, certain operations are forbidden across the real numbers.

> **📐 Definition — Domain of Definition.**
> The **domain of definition** of a function $f$, denoted $\mathcal{D}_f$, is the set of all real numbers $x$ for which the evaluation of $f(x)$ is mathematically valid and meaningful.

In high school mathematics, two operations necessitate checking for **forbidden values (domain restrictions)**:
1. **Division by zero:** The denominator of a fraction can **never** be zero.
   $$\frac{A}{B} \text{ exists if and only if } B \neq 0.$$
2. **The square root of a negative quantity:** The expression inside a square root must be non-negative.
   $$\sqrt{A} \text{ exists if and only if } A \ge 0.$$

---

### 3. Graphs, Variations, and Extrema

#### 3.1 The Function Graph in a Coordinate Plane

> **📐 Definition — Graph of a Function.**
> In a coordinate frame $(O\,; \vec{i}, \vec{j})$, the **graph (or representative curve)** of a function $f$, denoted $\mathcal{C}_f$, is the set of all points $M(x\,; y)$ whose $x$-coordinate lies in $\mathcal{D}_f$ and whose $y$-coordinate is its image $y = f(x)$:
> $$\mathcal{C}_f = \left\{ M(x\,; f(x)) \mid x \in \mathcal{D}_f \right\}.$$
> The equation of the curve is: $y = f(x)$.

To check whether a point $A(x_A\,; y_A)$ lies on the curve, compute $f(x_A)$. If it equals $y_A$, the point is on the curve; otherwise, it is not.

#### 3.2 Variations: Reading the Landscape

Imagine a hiker traversing the curve $\mathcal{C}_f$ from left to right (in the direction of increasing $x$).

```
         y ▲             Peak (Maximum)
           │                 ▲
           │               /   \
           │              /     \
           │             /       ▼
           │            /         \
           │           ▲           ▼
           │          /             \  Trough (Minimum)
           │         /               ▼
         O ┼────────┼─────────────────┼────────► x
                    a                 b
```

> **📐 Definition — Variations on an Interval $I$.**
> Let $f$ be a function defined on an interval $I$.
> 1. $f$ is **strictly increasing** on $I$ if for all real numbers $a$ and $b$ in $I$:
>    $$a < b \implies f(a) < f(b).$$
>    *(An increasing function preserves inequality order).*
> 2. $f$ is **strictly decreasing** on $I$ if for all real numbers $a$ and $b$ in $I$:
>    $$a < b \implies f(a) > f(b).$$
>    *(A decreasing function reverses inequality order).*
> 3. $f$ is **constant** on $I$ if for all $a, b \in I$, $f(a) = f(b)$.
> 4. A function is called **monotonic** on an interval if it is either purely increasing or purely decreasing across that interval.

#### 3.3 Extrema: Peaks and Troughs

> **📐 Definition — Maximum and Minimum.**
> Let $f$ be a function defined on domain $\mathcal{D}_f$ and let $x_0 \in \mathcal{D}_f$.
> - $f$ attains a **maximum** at $x_0$ on $\mathcal{D}_f$, with value $M = f(x_0)$, if for all $x \in \mathcal{D}_f$:
>   $$f(x) \le f(x_0).$$
> - $f$ attains a **minimum** at $x_0$ on $\mathcal{D}_f$, with value $m = f(x_0)$, if for all $x \in \mathcal{D}_f$:
>   $$f(x) \ge f(x_0).$$
> The term **extremum** (plural *extrema*) refers to either a maximum or a minimum.

---

### 4. Parity: Symmetry in the Mirror

#### 4.1 A Domain Centered at the Origin

To compare behavior to the left and right of the origin, the domain of definition must be symmetric with respect to zero:
$$\forall x \in \mathcal{D}_f, \quad -x \in \mathcal{D}_f.$$
For instance, $[-3\,; 3]$ and $\mathbb{R} \setminus \{0\}$ are symmetric about 0; whereas $[-2\,; 5]$ is not (for $x = 4$, $-4$ does not belong to the set).

#### 4.2 Even and Odd Functions

> **📐 Definition — Parity.**
> 1. A function $f$ is **even** if for all $x \in \mathcal{D}_f$:
>    $$f(-x) = f(x).$$
>    **Geometric property:** Its curve $\mathcal{C}_f$ is **symmetric with respect to the $y$-axis $(Oy)$** (reflectional symmetry).
> 2. A function $f$ is **odd** if for all $x \in \mathcal{D}_f$:
>    $$f(-x) = -f(x).$$
>    **Geometric property:** Its curve $\mathcal{C}_f$ is **symmetric with respect to the origin $O$** (half-turn rotational symmetry).

```
          EVEN FUNCTION                       ODD FUNCTION
        (Line Symmetry)                     (Point Symmetry)
              y ▲                                 y ▲
            \   │   /                               │       /
             \  │  /                                │      /
              \ │ /                                 │     /
        ───────\│/───────► x                ────────┼────o───► x
                O                                 / │
                                                 /  │
                                                /   │
```

---

### 5. The Five Parent Functions

These are the five cornerstone building blocks from which all high school function machinery is assembled.

#### 5.1 The Square Function: $f(x) = x^2$

- **Domain of definition:** $\mathcal{D}_f = \mathbb{R} = ]-\infty\,; +\infty[$.
- **Parity:** For every real $x$, $(-x)^2 = x^2$. The square function is **even**.
- **Variations:**
  - On $]-\infty\,; 0]$, it is strictly decreasing: if $a < b \le 0$, then $a^2 > b^2$.
  - On $[0\,; +\infty[$, it is strictly increasing: if $0 \le a < b$, then $a^2 < b^2$.
- **Graph:** An upward-opening **parabola** whose vertex is the origin $O(0\,; 0)$. Its absolute minimum is $0$, reached at $x = 0$.

> **Table of variations of $x \mapsto x^2$:**
>
> | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
> |---|---|---|---|---|---|
> | Variations of $x^2$ | $+\infty$ | $\searrow$ | $0$ | $\nearrow$ | $+\infty$ |

#### 5.2 The Reciprocal Function: $f(x) = \frac{1}{x}$

- **Domain of definition:** $\mathcal{D}_f = \mathbb{R}^* = \mathbb{R} \setminus \{0\} = ]-\infty\,; 0[ \cup ]0\,; +\infty[$.
- **Parity:** For all $x \neq 0$, $\frac{1}{-x} = -\frac{1}{x}$. The reciprocal function is **odd**.
- **Variations:**
  - Strictly decreasing on $]-\infty\,; 0[$.
  - Strictly decreasing on $]0\,; +\infty[$.
- **Graph:** A **hyperbola** in two distinct branches, point-symmetric about $O$. The coordinate axes serve as its **asymptotes**.

> **⚠️ Classic Pitfall Warning!**
> Never say that the reciprocal function is “decreasing on $\mathbb{R}^*$.”
> Take $a = -1$ and $b = 1$. Clearly $a < b$, but $f(a) = \frac{1}{-1} = -1$ and $f(b) = 1$. The value increased from $-1$ to $+1$!
> The function is strictly decreasing **on each of the two intervals taken separately**, but not on their disconnected union.

> **Table of variations of $x \mapsto \frac{1}{x}$:**
>
> | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
> |---|---|---|---|---|---|
> | Variations of $\frac{1}{x}$ | $0$ | $\searrow$ | $-\infty$ $\parallel$ $+\infty$ | $\searrow$ | $0$ |
>
> *(The double vertical bar $\parallel$ denotes the excluded value at $0$).*

#### 5.3 The Square Root Function: $f(x) = \sqrt{x}$

- **Domain of definition:** $\mathcal{D}_f = [0\,; +\infty[ = \mathbb{R}_+$.
- **Parity:** Meaningless (the domain is not symmetric about 0).
- **Variations:** Strictly increasing on $[0\,; +\infty[$.
  $$0 \le a < b \implies \sqrt{a} < \sqrt{b}.$$
- **Graph:** Half-branch of a horizontal parabola. It begins at $O(0\,; 0)$ with a vertical tangent at the origin.

#### 5.4 The Cube Function: $f(x) = x^3$

- **Domain of definition:** $\mathcal{D}_f = \mathbb{R}$.
- **Parity:** $(-x)^3 = (-1)^3 x^3 = -x^3$. The cube function is **odd**.
- **Variations:** Strictly increasing throughout all of $\mathbb{R}$.
  $$a < b \implies a^3 < b^3.$$
- **Graph:** Crosses the origin with a horizontal inflection point at $O(0\,; 0)$.

#### 5.5 The Absolute Value Function: $f(x) = |x|$

- **Domain of definition:** $\mathcal{D}_f = \mathbb{R}$.
- **Piecewise definition:**
  $$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$
- **Parity:** $|-x| = |x|$. The function is **even**.
- **Variations:**
  - Strictly decreasing on $]-\infty\,; 0]$ (slope $-1$).
  - Strictly increasing on $[0\,; +\infty[$ (slope $+1$).
- **Graph:** A sharp **V-shape**, formed by two rays meeting at a right angle at $O(0\,; 0)$. Its absolute minimum is $0$.

---

### 6. Graphical Solutions and Function Composition

#### 6.1 Graphical Solutions

1. **Solving $f(x) = k$:**
   Draw the horizontal line $y = k$. The solutions to the equation are the **$x$-coordinates** of the intersection points between curve $\mathcal{C}_f$ and line $y = k$.

2. **Solving $f(x) = g(x)$:**
   The solutions are the **$x$-coordinates** where curves $\mathcal{C}_f$ and $\mathcal{C}_g$ intersect.

3. **Solving $f(x) \le g(x)$:**
   The solutions are the intervals of the $x$-axis where curve $\mathcal{C}_f$ lies **below** (or touches) curve $\mathcal{C}_g$.

```
                 y ▲               Horizontal line y = k
                   │  Cf          /
                   │   \    k ───o───────o────► y = k
                   │    \       /│       │
                   │     \_____/ │       │
                 O ┼─────────────┼───────┼────────► x
                                 x1      x2
                         Solutions of f(x) = k : {x1, x2}
```

#### 6.2 Cascading Machines: Composition $g \circ f$

When two processing machines are linked in series:

```
             ┌───────────┐           ┌───────────┐
     x ────► │ Machine f │ ── f(x) ─►│ Machine g │ ───► g(f(x))
             └───────────┘           └───────────┘
```

> **📐 Definition — Composite Function.**
> Let $f$ and $g$ be two functions. The composite function of $f$ followed by $g$, denoted $g \circ f$ (read “g of f” or “g circle f”), is defined by:
> $$(g \circ f)(x) = g(f(x)).$$
> For this operation to be valid, $x$ must belong to $\mathcal{D}_f$, and the intermediate output $f(x)$ must lie within the domain of the second machine: $f(x) \in \mathcal{D}_g$.

> **⚠️ Pitfall Warning! Machine order is crucial.**
> In general, $g \circ f \neq f \circ g$.
> If $f(x) = x + 3$ and $g(x) = x^2$:
> - $(g \circ f)(x) = g(x + 3) = (x + 3)^2 = x^2 + 6x + 9$.
> - $(f \circ g)(x) = f(x^2) = x^2 + 3$.
> The two results are completely different!

---

### 7. Detailed Worked Examples

> **Worked Example 1 — Determining Domains of Definition.**
> Determine the domain of definition for each function:
> a) $f(x) = \frac{2x - 1}{x^2 - 9}$ \quad b) $g(x) = \sqrt{3x - 6}$ \quad c) $h(x) = \frac{1}{\sqrt{x} - 2}$
>
> **Step-by-Step Solution:**
> a) $f(x)$ is defined if and only if its denominator is non-zero:
>    $$x^2 - 9 \neq 0 \iff (x - 3)(x + 3) \neq 0 \iff x \neq 3 \text{ and } x \neq -3.$$
>    Hence $\mathcal{D}_f = \mathbb{R} \setminus \{-3\,; 3\} = ]-\infty\,; -3[ \cup ]-3\,; 3[ \cup ]3\,; +\infty[$.
>
> b) $g(x)$ contains a square root: the expression under the radical must be non-negative:
>    $$3x - 6 \ge 0 \iff 3x \ge 6 \iff x \ge 2.$$
>    Hence $\mathcal{D}_g = [2\,; +\infty[$.
>
> c) For $h(x)$, two conditions must hold simultaneously:
>    1. Square root exists: $\sqrt{x} \implies x \ge 0$.
>    2. Denominator is non-zero: $\sqrt{x} - 2 \neq 0 \iff \sqrt{x} \neq 2 \iff x \neq 4$.
>    Combining both yields: $\mathcal{D}_h = [0\,; 4[ \cup ]4\,; +\infty[$.

> **Worked Example 2 — Images and Preimages.**
> Let $f$ be defined on $\mathbb{R}$ by $f(x) = 2x^2 - 3x - 5$.
> 1. Calculate the images of $-2$ and $\frac{1}{2}$ under $f$.
> 2. Determine any preimages of $-5$ under $f$.
>
> **Solution:**
> 1. Computing images:
>    $$f(-2) = 2(-2)^2 - 3(-2) - 5 = 2(4) + 6 - 5 = 8 + 6 - 5 = 9.$$
>    $$f\left(\frac{1}{2}\right) = 2\left(\frac{1}{4}\right) - 3\left(\frac{1}{2}\right) - 5 = \frac{1}{2} - \frac{3}{2} - 5 = -1 - 5 = -6.$$
> 2. To find preimages of $-5$, solve $f(x) = -5$:
>    $$2x^2 - 3x - 5 = -5 \iff 2x^2 - 3x = 0.$$
>    Factoring out $x$:
>    $$x(2x - 3) = 0 \iff x = 0 \quad \text{or} \quad 2x - 3 = 0 \implies x = \frac{3}{2}.$$
>    The number $-5$ has two preimages under $f$: $0$ and $\frac{3}{2}$.

> **Worked Example 3 — Proving Variations Without Derivatives.**
> Let $f$ be defined on $]1\,; +\infty[$ by $f(x) = \frac{3}{x - 1}$.
> Prove rigorously that $f$ is strictly decreasing on this interval.
>
> **Solution:**
> Let $a$ and $b$ be two arbitrary real numbers in $]1\,; +\infty[$ such that $1 < a < b$.
> Build the expression step by step using inequality rules:
> 1. Subtract $1$:
>    $$0 < a - 1 < b - 1.$$
> 2. Apply the reciprocal function, which is strictly decreasing on $]0\,; +\infty[$ (reversing the order of positive numbers):
>    $$\frac{1}{a - 1} > \frac{1}{b - 1}.$$
> 3. Multiply by $3 > 0$ (preserving inequality order):
>    $$\frac{3}{a - 1} > \frac{3}{b - 1} \iff f(a) > f(b).$$
> Conclusion: Starting from $a < b$, we reached $f(a) > f(b)$.
> The order is inverted: the function $f$ is **strictly decreasing** on $]1\,; +\infty[$. $\blacksquare$

> **Worked Example 4 — Algebraic Parity Testing.**
> Determine the parity of each function:
> a) $f(x) = \frac{x^4 - 3}{x^2 + 1}$ \quad b) $g(x) = \frac{2x}{x^2 + 4}$ \quad c) $h(x) = x^3 - 2x + 1$
>
> **Solution:**
> a) $\mathcal{D}_f = \mathbb{R}$ because $x^2 + 1 > 0$ never vanishes. The domain is symmetric about 0.
>    $$f(-x) = \frac{(-x)^4 - 3}{(-x)^2 + 1} = \frac{x^4 - 3}{x^2 + 1} = f(x).$$
>    Hence $f$ is **even**.
>
> b) $\mathcal{D}_g = \mathbb{R}$, symmetric about 0.
>    $$g(-x) = \frac{2(-x)}{(-x)^2 + 4} = \frac{-2x}{x^2 + 4} = -\frac{2x}{x^2 + 4} = -g(x).$$
>    Hence $g$ is **odd**.
>
> c) $\mathcal{D}_h = \mathbb{R}$, symmetric about 0.
>    $$h(-x) = (-x)^3 - 2(-x) + 1 = -x^3 + 2x + 1.$$
>    Comparing:
>    - $h(x) = x^3 - 2x + 1 \neq h(-x)$, so $h$ is not even.
>    - $-h(x) = -x^3 + 2x - 1 \neq h(-x)$ (due to the $+1$ constant), so $h$ is not odd.
>    Conclusion: $h$ is **neither even nor odd**.

> **Worked Example 5 — Decomposing and Evaluating Composite Functions.**
> Let $f(x) = 2x - 5$ and $g(x) = \frac{1}{x}$.
> 1. Determine $(g \circ f)(x)$ and its domain of definition.
> 2. Determine $(f \circ g)(x)$ and its domain of definition.
>
> **Solution:**
> 1. $(g \circ f)(x) = g(f(x)) = g(2x - 5) = \frac{1}{2x - 5}$.
>    Existence condition: $2x - 5 \neq 0 \iff x \neq \frac{5}{2}$.
>    Thus $\mathcal{D}_{g \circ f} = \mathbb{R} \setminus \left\{\frac{5}{2}\right\}$.
>
> 2. $(f \circ g)(x) = f(g(x)) = f\left(\frac{1}{x}\right) = 2\left(\frac{1}{x}\right) - 5 = \frac{2}{x} - 5$.
>    Existence condition: $x \neq 0$.
>    Thus $\mathcal{D}_{f \circ g} = \mathbb{R}^*$.
>    *(Notice once again that the two composite functions are entirely different).*

> **Worked Example 6 — Graphical Solving and Parent Function Inversion.**
> Solve in $\mathbb{R}$:
> a) $x^2 \le 7$ \quad b) $\frac{1}{x} > 2$
>
> **Solution:**
> a) The square function is decreasing on $]-\infty\,; 0]$ and increasing on $[0\,; +\infty[$.
>    Equation $x^2 = 7$ has two roots: $-\sqrt{7}$ and $\sqrt{7}$.
>    The parabola $y = x^2$ lies below the horizontal line $y = 7$ for all $x$-values between these roots.
>    Thus the solution set is $\boxed{S = [-\sqrt{7}\,; \sqrt{7}]}$.
>
> b) Picture hyperbola $y = \frac{1}{x}$ and horizontal line $y = 2$:
>    - For $x \le 0$, $\frac{1}{x} < 0$, which can never exceed $2$.
>    - For $x > 0$, equation $\frac{1}{x} = 2$ gives $x = \frac{1}{2}$.
>    Since the reciprocal function is strictly decreasing on $]0\,; +\infty[$, obtaining a value greater than $2$ requires choosing inputs smaller than $\frac{1}{2}$ (while remaining strictly positive).
>    Thus the solution set is $\boxed{\left.S = \right]0\,; \frac{1}{2}\left[\right.}$.

---

### 8. In Computer Science: Value Tables and Root Sweeping in Python

In mathematics and data science, scripts are routinely used to generate values and pinpoint where functions cross zero:

```python
def f(x):
    """Defines function f(x) = x**3 - 3*x + 1"""
    return x**3 - 3*x + 1

def value_table(start, end, step):
    """Prints a table of values for function f."""
    print("  x   |  f(x)")
    print("------|--------")
    x = start
    while x <= end + 1e-9:
        print(f"{x:5.2f} | {f(x):7.3f}")
        x += step

# Display values from -2 to 2 with step 0.5
value_table(-2, 2, 0.5)

# Numerical root finding by step sweeping
def find_root(a, b, step=0.001):
    x = a
    while x <= b:
        if f(x) * f(x + step) <= 0:
            return round(x + step / 2, 3)
        x += step
    return None

solution = find_root(0, 1)
print(f"\nAn approximate root in [0, 1] is x ≈ {solution}")
```

---

### Key Takeaways

1. **Function:** $x \mapsto f(x)$. To every preimage $x \in \mathcal{D}_f$ corresponds **exactly one image** $f(x)$. A number may have $0$, $1$, or multiple preimages.
2. **Domain $\mathcal{D}_f$:**
   - Denominator $\neq 0$.
   - Quantity inside a square root $\ge 0$.
3. **Variations:**
   - Increasing: $a < b \implies f(a) \le f(b)$ (preserves order).
   - Decreasing: $a < b \implies f(a) \ge f(b)$ (reverses order).
4. **Parity:**
   - Even: $f(-x) = f(x)$, line symmetry across $y$-axis $(Oy)$.
   - Odd: $f(-x) = -f(x)$, rotational point symmetry about origin $O$.
5. **The 5 Parent Functions:**
   - Square $x^2$: $\mathcal{D} = \mathbb{R}$, even, decreasing on $\mathbb{R}_-$, increasing on $\mathbb{R}_+$, vertex $O(0\,; 0)$.
   - Reciprocal $\frac{1}{x}$: $\mathcal{D} = \mathbb{R}^*$, odd, decreasing on $]-\infty\,; 0[$ and on $]0\,; +\infty[$.
   - Square root $\sqrt{x}$: $\mathcal{D} = [0\,; +\infty[$, increasing.
   - Cube $x^3$: $\mathcal{D} = \mathbb{R}$, odd, increasing.
   - Absolute value $|x|$: $\mathcal{D} = \mathbb{R}$, even, V-shaped.
6. **Graphical Solution:** $f(x) = k$ $\iff$ $x$-coordinates of points where curve crosses horizontal height $k$.

---

### Exercises

#### Direct Application Exercises (★)

1. Given $f(x) = x^2 - 4x + 3$. Compute $f(0)$, $f(1)$, $f(2)$, and $f(-1)$.
2. State the domain of definition of $g(x) = \frac{1}{x - 7}$.
3. State the domain of definition of $h(x) = \sqrt{2x + 8}$.
4. Given $f(x) = 3x - 5$. What is the preimage of $10$ under $f$?
5. Is $f(x) = 5x^4 - 2x^2 + 1$ even, odd, or neither?
6. Is $g(x) = x^3 + 4x$ even, odd, or neither?
7. Solve in $\mathbb{R}$ the equation $x^2 = 25$.
8. Solve in $\mathbb{R}$ the inequality $x^2 < 16$.
9. Solve in $\mathbb{R}^*$ the equation $\frac{1}{x} = 5$.
10. Determine the values of $|-17|$, $|3.14|$, and $|5 - 9|$.

#### Practice and Reasoning Exercises (★★)

11. Determine the domain of definition of:
    a) $f(x) = \frac{x + 2}{x^2 - 4x}$ \quad b) $g(x) = \sqrt{10 - 2x}$ \quad c) $h(x) = \frac{\sqrt{x + 3}}{x - 1}$
12. Consider function $f$ defined on $[-4\,; 4]$ whose variations are:
    - Decreasing from $-4$ to $-1$, falling from $5$ to $-3$.
    - Increasing from $-1$ to $2$, rising from $-3$ to $4$.
    - Decreasing from $2$ to $4$, falling from $4$ to $1$.
    a) What is the global maximum of $f$ on $[-4\,; 4]$? At what $x$-value is it reached?
    b) What is the global minimum of $f$?
    c) How many solutions does $f(x) = 0$ have?
13. Prove without derivatives that $f(x) = x^2 - 6x + 5$ is strictly increasing on $[3\,; +\infty[$. *(Hint: write $f(x)$ as $(x - 3)^2 - 4$)*.
14. Solve in $\mathbb{R}$ the inequalities:
    a) $x^2 \ge 9$ \quad b) $\frac{1}{x} \le 3$
15. Investigate the parity of $f(x) = \frac{x^3}{x^2 + 1}$.
16. Given $f(x) = \sqrt{x}$ and $g(x) = x + 4$.
    Find explicit formulas for $(g \circ f)(x)$ and $(f \circ g)(x)$, specifying their domains.
17. Solve the equation $|2x - 3| = 7$.
18. Solve the inequality $|x - 5| \le 2$ by interpreting it as a distance on the number line.

#### Advanced Problems and Challenges (★★★)

19. **Decomposing Any Function into Even and Odd Parts.**
    Let $f$ be any function defined on $\mathbb{R}$.
    Define $p(x) = \frac{f(x) + f(-x)}{2}$ and $i(x) = \frac{f(x) - f(-x)}{2}$.
    a) Prove that $p$ is even and $i$ is odd.
    b) Prove that $f(x) = p(x) + i(x)$.
    c) Apply this decomposition to $f(x) = 2x^2 - 3x + 4$.
20. **Optimizing a Rectangular Enclosure.**
    A farmer has $40\text{ meters}$ of fencing to construct a rectangular pen against an existing stone wall (so no fence is needed along the wall).
    Let $x$ denote the length of each of the two sides perpendicular to the wall.
    a) Express the length of the third side in terms of $x$.
    b) For what values of $x$ is the pen physically realizable?
    c) Express the area $A(x)$ of the pen in terms of $x$.
    d) Prove that $A(x) = -2(x - 10)^2 + 200$.
    e) Deduce the value of $x$ that maximizes area, and give this maximum area.
21. **Arithmetic-Geometric Inequality.**
    For any strictly positive real $x > 0$, let $f(x) = x + \frac{1}{x}$.
    a) Expand $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2$.
    b) Deduce that for all $x > 0$, $x + \frac{1}{x} \ge 2$.
    c) For what value of $x$ does equality hold?
22. **Fixed Points of Functions.**
    A fixed point of a function $f$ is a number $x$ satisfying $f(x) = x$.
    Find all fixed points of the parent functions:
    a) $f(x) = x^2$ \quad b) $g(x) = \frac{1}{x}$ \quad c) $h(x) = \sqrt{x}$ \quad d) $k(x) = x^3$.

---

### Solutions

1. $f(0) = 3$. $f(1) = 1 - 4 + 3 = 0$. $f(2) = 4 - 8 + 3 = -1$. $f(-1) = (-1)^2 - 4(-1) + 3 = 1 + 4 + 3 = 8$.
2. Denominator non-zero: $x - 7 \neq 0 \iff x \neq 7$. Domain: $\mathcal{D}_g = \mathbb{R} \setminus \{7\}$.
3. Expression under radical non-negative: $2x + 8 \ge 0 \iff 2x \ge -8 \iff x \ge -4$. Domain: $\mathcal{D}_h = [-4\,; +\infty[$.
4. $3x - 5 = 10 \iff 3x = 15 \iff x = 5$. Preimage is $5$.
5. $f(-x) = 5(-x)^4 - 2(-x)^2 + 1 = 5x^4 - 2x^2 + 1 = f(x)$. The function is even.
6. $g(-x) = (-x)^3 + 4(-x) = -x^3 - 4x = -(x^3 + 4x) = -g(x)$. The function is odd.
7. $x^2 = 25 \iff x = 5$ or $x = -5$. $S = \{-5\,; 5\}$.
8. $x^2 < 16 \iff -4 < x < 4$. $S = ]-4\,; 4[$.
9. $\frac{1}{x} = 5 \iff x = \frac{1}{5} = 0.2$.
10. $|-17| = 17$; $|3.14| = 3.14$; $|5 - 9| = |-4| = 4$.
11. a) $x^2 - 4x = x(x - 4) \neq 0 \implies x \neq 0$ and $x \neq 4$. $\mathcal{D}_f = \mathbb{R} \setminus \{0\,; 4\}$.
    b) $10 - 2x \ge 0 \iff 2x \le 10 \iff x \le 5$. $\mathcal{D}_g = ]-\infty\,; 5]$.
    c) $x + 3 \ge 0 \iff x \ge -3$ and denominator $x - 1 \neq 0 \iff x \neq 1$. $\mathcal{D}_h = [-3\,; 1[ \cup ]1\,; +\infty[$.
12. a) Global maximum is $5$, reached at $x = -4$.
    b) Global minimum is $-3$, reached at $x = -1$.
    c) On $[-4\,; -1]$, $f$ decreases from $5$ to $-3$, crossing $0$ once. On $[-1\,; 2]$, it increases from $-3$ to $4$, crossing $0$ a second time. On $[2\,; 4]$, values span from $4$ down to $1$ (strictly positive), so it does not cross $0$. The equation $f(x) = 0$ has exactly $2$ solutions.
13. Vertex form: $(x - 3)^2 - 4 = x^2 - 6x + 9 - 4 = x^2 - 6x + 5$.
    Let $3 \le a < b$.
    Then $0 \le a - 3 < b - 3$.
    Since the square function is strictly increasing on $[0\,; +\infty[$, $(a - 3)^2 < (b - 3)^2$.
    Subtracting $4$: $(a - 3)^2 - 4 < (b - 3)^2 - 4 \iff f(a) < f(b)$.
    Order is preserved: $f$ is strictly increasing on $[3\,; +\infty[$.
14. a) $x^2 \ge 9 \iff x \le -3$ or $x \ge 3$. $S = ]-\infty\,; -3] \cup [3\,; +\infty[$.
    b) For $\frac{1}{x} \le 3$:
    - If $x < 0$, $\frac{1}{x} < 0 < 3$, so all strictly negative numbers are solutions: $]-\infty\,; 0[$.
    - If $x > 0$, $\frac{1}{x} \le 3 \iff x \ge \frac{1}{3}$.
    Solution set: $S = ]-\infty\,; 0[ \cup \left[\frac{1}{3}\,; +\infty\right[$.
15. $\mathcal{D}_f = \mathbb{R}$ (since $x^2 + 1 > 0$). Symmetric about 0.
    $f(-x) = \frac{(-x)^3}{(-x)^2 + 1} = \frac{-x^3}{x^2 + 1} = -f(x)$. The function is odd.
16. $(g \circ f)(x) = g(\sqrt{x}) = \sqrt{x} + 4$, defined on $[0\,; +\infty[$.
    $(f \circ g)(x) = f(x + 4) = \sqrt{x + 4}$, defined when $x + 4 \ge 0 \iff x \ge -4$, so domain is $[-4\,; +\infty[$.
17. $|2x - 3| = 7 \iff 2x - 3 = 7$ or $2x - 3 = -7$.
    $2x = 10 \implies x = 5$ or $2x = -4 \implies x = -2$. $S = \{-2\,; 5\}$.
18. $|x - 5|$ represents distance from $x$ to $5$. We seek $x$ within distance $2$ of $5$: $5 - 2 \le x \le 5 + 2 \iff 3 \le x \le 7$. $S = [3\,; 7]$.
19. a) $p(-x) = \frac{f(-x) + f(-(-x))}{2} = \frac{f(-x) + f(x)}{2} = p(x)$, so $p$ is even.
    $i(-x) = \frac{f(-x) - f(-(-x))}{2} = \frac{f(-x) - f(x)}{2} = -\frac{f(x) - f(-x)}{2} = -i(x)$, so $i$ is odd.
    b) $p(x) + i(x) = \frac{f(x) + f(-x) + f(x) - f(-x)}{2} = \frac{2f(x)}{2} = f(x)$. Every function can be decomposed into an even part and an odd part!
    c) For $f(x) = 2x^2 - 3x + 4$:
    $f(-x) = 2x^2 + 3x + 4$.
    $p(x) = \frac{(2x^2 - 3x + 4) + (2x^2 + 3x + 4)}{2} = 2x^2 + 4$ (even component).
    $i(x) = \frac{(2x^2 - 3x + 4) - (2x^2 + 3x + 4)}{2} = \frac{-6x}{2} = -3x$ (odd component).
20. a) Let $x$ be the width of each perpendicular side. The remaining length for the side opposite the wall is $40 - 2x$.
    b) We require $x > 0$ and $40 - 2x > 0 \iff 2x < 40 \iff x < 20$. Thus $x \in ]0\,; 20[$.
    c) Area: $A(x) = x(40 - 2x) = 40x - 2x^2$.
    d) Expand: $-2(x - 10)^2 + 200 = -2(x^2 - 20x + 100) + 200 = -2x^2 + 40x - 200 + 200 = 40x - 2x^2 = A(x)$.
    e) Since $(x - 10)^2 \ge 0$, $-2(x - 10)^2 \le 0$, hence $A(x) \le 200$.
    The maximum occurs when the squared term vanishes: $x - 10 = 0 \iff x = 10\text{ m}$.
    Maximum area is $200\text{ m}^2$ (dimensions: $10\text{ m} \times 20\text{ m}$).
21. a) $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2 = (\sqrt{x})^2 - 2 \times \sqrt{x} \times \frac{1}{\sqrt{x}} + \left(\frac{1}{\sqrt{x}}\right)^2 = x - 2 + \frac{1}{x}$.
    b) Any real square is non-negative: $\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2 \ge 0 \iff x - 2 + \frac{1}{x} \ge 0 \iff x + \frac{1}{x} \ge 2$.
    c) Equality holds if and only if $\sqrt{x} - \frac{1}{\sqrt{x}} = 0 \iff \sqrt{x} = \frac{1}{\sqrt{x}} \iff (\sqrt{x})^2 = 1 \iff x = 1$.
22. a) $x^2 = x \iff x^2 - x = 0 \iff x(x - 1) = 0 \implies x = 0$ or $x = 1$.
    b) $\frac{1}{x} = x \iff x^2 = 1 \iff x = 1$ or $x = -1$.
    c) $\sqrt{x} = x$ for $x \ge 0 \iff x = x^2 \implies x = 0$ or $x = 1$.
    d) $x^3 = x \iff x^3 - x = 0 \iff x(x^2 - 1) = 0 \iff x(x - 1)(x + 1) = 0 \implies x = 0, 1 \text{ or } -1$.

---

### The Question That Opens the Future

In the farmer's pen problem, we encountered a quadratic expression: $A(x) = -2x^2 + 40x$. To find its crest without guesswork, we used the vertex form $-2(x - 10)^2 + 200$.

This family of curves—the parabolas defined by quadratic polynomials $ax^2 + bx + c$—governs the trajectories of artillery shells, water jets in ornamental fountains, and the reflective mirrors of astronomical telescopes. How can we systematically find their vertices and roots without relying on trial-and-error tricks? What is the mysterious quantity $\Delta$ that geometers unlocked? That is what we will explore in **Galileo's Fountain and the Parabola**.
