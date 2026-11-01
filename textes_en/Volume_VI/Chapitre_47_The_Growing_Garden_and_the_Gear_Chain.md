# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 47: The Growing Garden and the Gear Chain

> *“Never memorize a differentiation formula as a mere magic incantation to pass an exam. Look at the toothed sprockets of a bicycle gearing up the effort from pedal to rear wheel: each speed multiplies the preceding one. Look at a ceramic bowl catching rainwater without losing a drop: its upward-facing contour is a convex curve, and it is the acceleration of its slope that decides whether it gathers or spills.”*

---

### What You Will Discover

- Why differentiating a composite function operates exactly like a **bicycle gearbox**: the celebrated chain rule $(g \circ u)' = u' \cdot (g' \circ u)$.
- The three indispensable powerhouse formulas for the Baccalaureate: the derivatives of $e^{u(x)}$, $\sqrt{u(x)}$, and $(u(x))^n$.
- The **second derivative** $f''(x)$: after instantaneous velocity comes **acceleration** and the curvature of the trajectory.
- **Convexity**: understanding intuitively and geometrically what it means for a curve to be “bowl-shaped” (opening upward) or “bell-shaped” (opening downward).
- The fundamental curriculum equivalences: secant lines lying above the curve, tangent lines lying below the curve, and the positivity of $f''(x)$.
- **Inflection points**: the exact spot where a cyclist straightens the handlebars to switch curves, where the curve **crosses its own tangent**.
- **Convexity inequalities**, including the celebrated $e^x \geq x + 1$ for all real $x$.

---

### 1. The Problem: Cascading Gears and the Soup Bowl

#### 1.1 The Cyclist and the Gearbox

Imagine a racing bicycle equipped with a large 50-tooth chainring at the crankset and a small 25-tooth cog on the rear wheel.
- When the cyclist turns the pedals through an angle $x$, the front chainring turns through an angle $u = x$.
- The chain transmits the motion: because the rear cog has half as many teeth as the chainring, the cog rotates twice as fast:
  $$u \mapsto y = 2u.$$
- The rear wheel, locked to the cog, turns the tire against the asphalt: each rotation of the wheel propels the bicycle forward by a distance $z = 2.10 \times y$ meters.

```
 [ Crankset ] ────── Chain ──────► [ Rear Cog ] ────── Axle ──────► [ Wheel / Road ]
   Angle x                           Speed u                          Distance z
      │                                 │                                  │
      └───────── Rate du/dx = 1 ────────┴────── Rate dz/du = 4.2 ──────────┘
```

If the cyclist presses slightly faster on the pedals (variation $\Delta x$):
- the intermediate speed changes at a certain rate: $\dfrac{\Delta u}{\Delta x}$;
- the final wheel speed changes relative to the intermediate speed at the rate: $\dfrac{\Delta z}{\Delta u}$.

At what rate does the distance $z$ vary with respect to the initial effort $x$ on the pedals?
The physical common-sense answer is immediate: one **multiplies the transmission ratios**!

$$\frac{\Delta z}{\Delta x} = \frac{\Delta z}{\Delta u} \times \frac{\Delta u}{\Delta x}.$$

The German physicist and mathematician Gottfried Wilhelm Leibniz wrote this formula as early as 1684 in the luminous form:

$$\frac{dz}{dx} = \frac{dz}{du} \cdot \frac{du}{dx}.$$

The two $du$ terms appear to cancel out just like in a basic fraction of numbers! This is the secret of differentiating composite functions: **sensitivities chain together through multiplication**.

#### 1.2 The Gardener and the Bowl That Catches the Rain

Now observe two vessels set out in a garden in springtime:
1. A hollow bowl resting on its base: it fills with rainwater. If you stretch a straight string between two opposite points on its rim (a secant line), the entire bowl bottom plunges **below** the string. If you lay a flat ruler tangent beneath the bowl, the entire vessel rests **above** the ruler. This is a **convex** curve.
2. A glass bell jar placed upside down: rainwater slides down its sides and runs off. A secant chord stays beneath the bell, and a tangent line remains above it. This is a **concave** curve.

```
    Convex Curve (Bowl holding water)              Concave Curve (Bell shedding water)
              A                 B
               \   Secant [AB]   /                            .--- Tangent
                \---------------/                            /   .-'""'-.
                 \             /                            /   /   /\   \
                  '._       _.'                                /   /  \   \
                     '-----'                                  /   /    \   \
          ─────── Tangent at base ───────
```

How can the derivative distinguish between these two shapes? How can a single equation predict whether a mountain hairpin tightens or flattens out?
This is the role of the **second derivative**.

---

### 2. The Derivative of a Composite Function: The Chain Rule

#### 2.1 The Notations Explained

- Let $u$ be a function defined on an interval $I$ with values in an interval $J$, and let $g$ be a function defined on $J$.
- The composite function is denoted $g \circ u$ (read “g circle u” or “g composed with u”): for all $x \in I$, $(g \circ u)(x) = g\big(u(x)\big)$.
- Note the order of evaluation: in $g\big(u(x)\big)$, one computes $u(x)$ **first** (the inner function), and then feeds that result to $g$ (the outer function).
- The derivative is denoted $(g \circ u)'$ or $[g(u(x))]'$.

#### 2.2 The Fundamental Theorem

> **📐 Theorem — Derivative of a composite function (Chain Rule).**
> Let $u$ be a function differentiable on an interval $I$, and let $g$ be a function differentiable on an interval $J$ containing $u(I)$.
> Then the composite function $f = g \circ u$ is differentiable on the interval $I$, and for every real number $x \in I$:
> $$(g \circ u)'(x) = u'(x) \times g'\big(u(x)\big).$$

*Spoken aloud:* “The derivative of $g(u)$ is $u'$ multiplied by $g'$ evaluated at $u$.”

> **✍️ Idea of the proof.**
> Let $x_0 \in I$. Form the difference quotient of the composite function between $x$ and $x_0$:
> $$\frac{g(u(x)) - g(u(x_0))}{x - x_0}.$$
> If $u(x) \neq u(x_0)$ in a neighborhood of $x_0$, we can cleverly insert the intermediate factor $u(x) - u(x_0)$ in numerator and denominator:
> $$\frac{g(u(x)) - g(u(x_0))}{x - x_0} = \frac{g(u(x)) - g(u(x_0))}{u(x) - u(x_0)} \times \frac{u(x) - u(x_0)}{x - x_0}.$$
> As $x \to x_0$:
> - By continuity of the differentiable function $u$, we have $\lim\limits_{x \to x_0} u(x) = u(x_0)$.
> - Setting $Y = u(x)$ and $Y_0 = u(x_0)$, the first factor becomes $\dfrac{g(Y) - g(Y_0)}{Y - Y_0}$, which tends to the derivative $g'(Y_0) = g'\big(u(x_0)\big)$ since $g$ is differentiable at $u(x_0)$.
> - The second factor is the difference quotient of $u$, which by definition tends to $u'(x_0)$.
> By the product rule for limits:
> $$(g \circ u)'(x_0) = g'\big(u(x_0)\big) \times u'(x_0) = u'(x_0) \cdot g'\big(u(x_0)\big). \quad \blacksquare$$

---

### 3. The Three Powerhouse Formulas of the Baccalaureate

All delicate derivatives in the advanced mathematics exam are immediate special cases of this chain rule, substituting $g$ with the curriculum's three primary functions:

#### 3.1 Derivative of $e^{u(x)}$: The Sovereign Function

Take $g(y) = e^y$. We know that $g'(y) = e^y$.
Applying the general formula $(g \circ u)' = u' \cdot g'(u)$:

> **📐 Property — Derivative of composite exponential.**
> Let $u$ be a function differentiable on an interval $I$.
> The function $f : x \mapsto e^{u(x)}$ is differentiable on $I$, and for all $x \in I$:
> $$\mathbf{\big(e^{u(x)}\big)' = u'(x) \, e^{u(x)}}.$$

*Lightning example:* Let $f(x) = e^{-3x^2 + 5x}$.
Here $u(x) = -3x^2 + 5x$, so $u'(x) = -6x + 5$.
We apply the rule directly: $f'(x) = (-6x + 5)e^{-3x^2 + 5x}$.

#### 3.2 Derivative of $\sqrt{u(x)}$

Take $g(y) = \sqrt{y}$ defined for $y > 0$. Its derivative is $g'(y) = \dfrac{1}{2\sqrt{y}}$.

> **📐 Property — Derivative of composite square root.**
> Let $u$ be a function differentiable and **strictly positive** on an interval $I$.
> The function $f : x \mapsto \sqrt{u(x)}$ is differentiable on $I$, and for all $x \in I$:
> $$\mathbf{\big(\sqrt{u(x)}\big)' = \frac{u'(x)}{2\sqrt{u(x)}}}.$$

> **⚠️ Caution, trap! — The condition $u(x) > 0$.**
> The function $\sqrt{u(x)}$ is defined whenever $u(x) \geq 0$, but it is **differentiable** only where $u(x) > 0$ (strictly positive). If $u(x_0) = 0$, the curve typically displays a vertical half-tangent at $x_0$, and the denominator $2\sqrt{u(x)}$ would vanish!

#### 3.3 Derivative of $(u(x))^n$

Take $g(y) = y^n$ with $n \in \mathbb{Z}^*$. Its derivative is $g'(y) = n y^{n-1}$.

> **📐 Property — Derivative of composite power.**
> Let $u$ be a function differentiable on an interval $I$.
> For any non-zero integer $n \geq 1$ (or $n < 0$ on intervals where $u(x) \neq 0$):
> $$\mathbf{\big(u^n\big)' = n \, u'(x) \, \big(u(x)\big)^{n-1}}.$$

*Fundamental special case:* For $n = -1$, the formula gives the derivative of the reciprocal:
$$\left(\frac{1}{u}\right)' = \big(u^{-1}\big)' = -1 \cdot u' \cdot u^{-2} = \mathbf{-\frac{u'}{u^2}}.$$

#### Summary Comparison Table

| Simple function $f(x)$ | Derivative $f'(x)$ | Composite function $f(x)$ | Derivative $f'(x)$ | Validity Condition |
| :---: | :---: | :---: | :---: | :--- |
| $x^n$ | $n x^{n-1}$ | $\big(u(x)\big)^n$ | $\mathbf{n \, u'(x) \, \big(u(x)\big)^{n-1}}$ | $u$ differentiable ($u \neq 0$ if $n \leq 0$) |
| $\dfrac{1}{x}$ | $-\dfrac{1}{x^2}$ | $\dfrac{1}{u(x)}$ | $\mathbf{-\dfrac{u'(x)}{\big(u(x)\big)^2}}$ | $u(x) \neq 0$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ | $\sqrt{u(x)}$ | $\mathbf{\dfrac{u'(x)}{2\sqrt{u(x)}}}$ | $\mathbf{u(x) > 0}$ |
| $e^x$ | $e^x$ | $e^{u(x)}$ | $\mathbf{u'(x) \, e^{u(x)}}$ | $u$ differentiable on $I$ |

---

### 4. The Second Derivative: After Velocity, Acceleration

#### 4.1 Definition and Notations

When the derivative function $f'$ is itself differentiable on an interval $I$, its own derivative is called the **second derivative** of $f$, and is denoted:

$$\mathbf{f''(x)} \quad \text{or} \quad \mathbf{\frac{d^2f}{dx^2}(x)} \quad \text{(Leibniz notation)}.$$

- $f(x)$ describes **position** (altitude, temperature, capital).
- $f'(x)$ describes **instantaneous rate of change / velocity** (slope of the tangent).
- $f''(x)$ describes **acceleration**: the rate at which the slope itself increases or decreases.

*In physics:* If $x(t)$ represents the position of a body over time, its velocity is $v(t) = x'(t)$ and its acceleration is $a(t) = v'(t) = x''(t)$.
Isaac Newton founded all classical mechanics on this universal law:
$$F = m \cdot a = m \cdot x''(t).$$
Without the second derivative, it is impossible to understand planetary gravitation or vehicle braking dynamics.

---

### 5. Convexity: The Bowl, the Chords, and the Tangents

#### 5.1 Fundamental Geometric Definition

> **📐 Geometric Definition — Convex / Concave function.**
> Let $f$ be a function defined on an interval $I$.
> - We say that $f$ is **convex** on $I$ if, for any two points $A$ and $B$ on the graph $\mathcal{C}_f$, the line segment $[AB]$ (the chord) lies entirely **above or on** the curve on the interval between $A$ and $B$.
> - We say that $f$ is **concave** on $I$ if, for any two points $A$ and $B$ on the curve, the segment $[AB]$ lies entirely **below or on** the curve.

```
       CONVEX (chord ABOVE)                        CONCAVE (chord BELOW)
       y ▲                                          y ▲
         │  A             B                           │         .---. Curve arc
         │   \   Chord   /                            │        /  _  \
         │    \  [AB]   /                             │    A  /.-' '-.\  B
         │     \_______/  Curve arc                   │      /─────────\  Chord [AB]
         └──────────────────────► x                   └──────────────────────► x
```

*Practical remark:* A function $f$ is concave if and only if $-f$ is convex.

#### 5.2 Equivalent Characterizations (Curriculum Theorem)

For a twice-differentiable function, the syllabus establishes a magnificent triple equivalence connecting chord geometry, tangent placement, and differential calculus:

> **📐 Fundamental Theorem — Characterizations of convexity.**
> Let $f$ be a twice-differentiable function on an interval $I$. The following statements are **strictly equivalent**:
> 1. $f$ is **convex** on $I$;
> 2. The derivative function $f'$ is **increasing** on $I$;
> 3. For all $x \in I$, the second derivative is non-negative: **$f''(x) \geq 0$**;
> 4. The curve $\mathcal{C}_f$ lies entirely **above all its tangent lines**.

And symmetrically for concavity:

> **📐 Theorem — Characterizations of concavity.**
> Let $f$ be twice differentiable on an interval $I$. The following statements are equivalent:
> 1. $f$ is **concave** on $I$;
> 2. The derivative function $f'$ is **decreasing** on $I$;
> 3. For all $x \in I$, the second derivative is non-positive: **$f''(x) \leq 0$**;
> 4. The curve $\mathcal{C}_f$ lies entirely **below all its tangent lines**.

#### 5.3 Convexity Inequalities

Because the curve of a convex function always lies above its tangent line at any point with abscissa $x_0$, we immediately have for all real $x$:

$$\mathbf{f(x) \geq f'(x_0)(x - x_0) + f(x_0)}.$$

Let us apply this powerful property to the exponential function $f(x) = e^x$ at $x_0 = 0$:
- $f(0) = e^0 = 1$;
- $f'(x) = e^x \implies f'(0) = 1$;
- $f''(x) = e^x > 0$ on $\mathbb{R}$, so the exponential is **strictly convex** on $\mathbb{R}$.

The tangent at 0 has equation: $y = 1 \cdot (x - 0) + 1 = x + 1$.
Because the curve lies above its tangent, we obtain the fundamental high-school inequality:

> **📐 Remarkable Convexity Inequality — The exponential above its tangent:**
> For every real number $x \in \mathbb{R}$:
> $$\mathbf{e^x \geq x + 1}.$$
> With equality if and only if $x = 0$.

```
       y ▲                        /  y = e^x (convex)
         │                       /
         │                     /  /  y = x + 1 (tangent at 0)
         │                   /  /
       1 ┼                  * /
         │                 /
─────────┼────────────────┼────────────────► x
        -1                0
```

This inequality allows one to prove in two lines that $\lim\limits_{x \to +\infty} e^x = +\infty$, since $e^x \geq x + 1 \to +\infty$.

---

### 6. The Inflection Point: Where the Bend Reverses

Imagine driving a car along a winding country road:
- At first, the road turns right: you steer clockwise (the curvature is convex).
- Later, the road sweeps left: you steer counterclockwise (the curvature becomes concave).
- There is an infinitesimal moment, right between the two turns, where **your steering wheel passes exactly through dead center (neutral)**.

This transition moment is an **inflection point**.

#### 6.1 Geometric Definition

> **📐 Definition — Inflection point.**
> Let $f$ be a function differentiable on an interval $I$.
> An **inflection point** is any point $A\big(x_0 \,;\, f(x_0)\big)$ on the curve $\mathcal{C}_f$ where the curve **crosses its tangent line**.

```
              Curve f(x)
                 \
                  \        Tangent T
        Concave    \      /
      (under T)     \    /
                     \  /
           ───────────*─────────── Inflection Point (x_0, f(x_0))
                     / \
                    /   \     Convex
                   /     \  (above T)
                  /       \
```

#### 6.2 Characterization via the Second Derivative

> **📐 Fundamental Theorem — Necessary and sufficient condition for inflection.**
> Let $f$ be a twice-differentiable function on an interval $I$.
> The point $A\big(x_0 \,;\, f(x_0)\big)$ is an **inflection point** if and only if:
> **The second derivative $f''$ vanishes at $x_0$ AND CHANGES SIGN.**

> **⚠️ Caution, trap! — Vanishing alone is NOT SUFFICIENT!**
> This is a favorite trap on Baccalaureate exams.
> If $f''(x_0) = 0$, this does **not guarantee** that $x_0$ is an inflection point! One must imperatively check that $f''$ **changes sign** (from $+$ to $-$ or from $-$ to $+$).
> **Striking counterexample:** Consider $f(x) = x^4$.
> - $f'(x) = 4x^3$;
> - $f''(x) = 12x^2$.
> At $x_0 = 0$, we have $f''(0) = 12 \times 0^2 = 0$.
> Yet for all $x \neq 0$, $12x^2 > 0$: the second derivative is strictly positive! It vanishes at 0 without ever changing sign.
> The graph of $x^4$ is entirely convex (a flattened bowl), and its tangent at 0 is the $x$-axis ($y = 0$). The curve stays strictly above its tangent: **there is no inflection point at 0!**

---

### 7. Traps to Avoid!

> **⚠️ Caution, trap! — Forgetting $u'(x)$ in composite derivatives.**
> - Writing $\left(e^{5x}\right)' = e^{5x}$ is false! The correct answer is $5e^{5x}$.
> - Writing $\left(\sqrt{x^2 + 1}\right)' = \frac{1}{2\sqrt{x^2+1}}$ is false! The correct answer is $\frac{2x}{2\sqrt{x^2+1}} = \frac{x}{\sqrt{x^2+1}}$.
> - Writing $\left((3x - 2)^4\right)' = 4(3x - 2)^3$ is false! The correct answer is $4 \times 3 \times (3x - 2)^3 = 12(3x - 2)^3$.
> Golden rule: whenever the inner argument is anything other than a plain $x$, **you must bring $u'(x)$ out in front**.

> **⚠️ Caution, trap! — Confusing monotonicity with convexity.**
> - A function can be **increasing and convex** (e.g., $e^x$ on $\mathbb{R}$, $x^2$ on $[0 ; +\infty[$).
> - A function can be **increasing and concave** (e.g., $\sqrt{x}$ on $[0 ; +\infty[$, $\ln x$ on $]0 ; +\infty[$).
> - A function can be **decreasing and convex** (e.g., $e^{-x}$ on $\mathbb{R}$, $\frac{1}{x}$ on $]0 ; +\infty[$).
> - A function can be **decreasing and concave** (e.g., $-x^2$ on $[0 ; +\infty[$).
> The sign of $f'$ determines variation (rising or falling); the sign of $f''$ determines curvature (cupping upward or bulging downward).

---

### 8. Step-by-Step Worked Examples

#### Worked Example 1 — Differentiating Multiple Composite Functions

**Problem:** Compute the derivative of each of the following functions, stating the domain of differentiability:
1. $f(x) = e^{-x^2 + 4x}$ on $\mathbb{R}$
2. $g(x) = \sqrt{3x^2 + 6}$ on $\mathbb{R}$
3. $h(x) = (2x^3 - 5x)^4$ on $\mathbb{R}$
4. $k(x) = \dfrac{1}{(x^2 + 1)^3}$ on $\mathbb{R}$

**Solution:**
1. $f$ has the form $e^u$ with $u(x) = -x^2 + 4x$.
   $u'(x) = -2x + 4$.
   $$f'(x) = u'(x)e^{u(x)} = (-2x + 4)e^{-x^2 + 4x}.$$
2. $g$ has the form $\sqrt{u}$ with $u(x) = 3x^2 + 6$.
   For all real $x$, $3x^2 + 6 \geq 6 > 0$, so $g$ is differentiable on $\mathbb{R}$.
   $u'(x) = 6x$.
   $$g'(x) = \frac{u'(x)}{2\sqrt{u(x)}} = \frac{6x}{2\sqrt{3x^2 + 6}} = \frac{3x}{\sqrt{3x^2 + 6}}.$$
3. $h$ has the form $u^4$ with $u(x) = 2x^3 - 5x$.
   $u'(x) = 6x^2 - 5$.
   $$h'(x) = 4 \, u'(x) \, \big(u(x)\big)^3 = 4(6x^2 - 5)(2x^3 - 5x)^3.$$
4. Write $k(x) = (x^2 + 1)^{-3}$, which is $u^{-3}$ with $u(x) = x^2 + 1$.
   $u'(x) = 2x$.
   $$k'(x) = -3 \cdot u'(x) \cdot \big(u(x)\big)^{-4} = -3(2x)(x^2 + 1)^{-4} = \frac{-6x}{(x^2 + 1)^4}.$$

---

#### Worked Example 2 — Complete Study of Convexity for a Polynomial Function

**Problem:** Consider the function $f$ defined on $\mathbb{R}$ by $f(x) = x^4 - 2x^3 - 12x^2 + 5x - 1$.
1. Compute $f'(x)$ and the second derivative $f''(x)$.
2. Determine the intervals where $f$ is convex, and those where $f$ is concave.
3. Deduce the coordinates of the inflection points of the graph $\mathcal{C}_f$.

**Solution:**
1. $f$ is twice differentiable on $\mathbb{R}$ as a polynomial:
   - $f'(x) = 4x^3 - 6x^2 - 24x + 5$
   - $f''(x) = 12x^2 - 12x - 24 = 12(x^2 - x - 2)$.
2. Factoring the quadratic $x^2 - x - 2$:
   Its evident roots are $x_1 = -1$ and $x_2 = 2$ (since $(-1)^2 - (-1) - 2 = 0$ and $2^2 - 2 - 2 = 0$).
   The quadratic shares the sign of $a = 12 > 0$ outside the roots and is negative between them:
   - For $x \in ]-\infty \,;\, -1]$, $f''(x) \geq 0$: $f$ is **convex**.
   - For $x \in [-1 \,;\, 2]$, $f''(x) \leq 0$: $f$ is **concave**.
   - For $x \in [2 \,;\, +\infty[$, $f''(x) \geq 0$: $f$ is **convex**.
3. The second derivative $f''$ vanishes while changing sign at $x = -1$ and $x = 2$.
   The graph $\mathcal{C}_f$ admits two inflection points:
   - At $x = -1$: $f(-1) = 1 + 2 - 12 - 5 - 1 = -15$. First inflection point: $I_1(-1 \,;\, -15)$.
   - At $x = 2$: $f(2) = 16 - 16 - 48 + 10 - 1 = -39$. Second inflection point: $I_2(2 \,;\, -39)$.

---

#### Worked Example 3 — The Gaussian Bell Curve: Convexity and Inflections

**Problem:** Consider the Gaussian function $f(x) = e^{-x^2/2}$ defined on $\mathbb{R}$.
1. Compute $f'(x)$ and study the variations of $f$.
2. Compute $f''(x)$ and study its sign.
3. Determine the inflection points of the Gaussian bell curve.

**Solution:**
1. $f(x) = e^{u(x)}$ with $u(x) = -\frac{1}{2}x^2$, whence $u'(x) = -x$.
   $$f'(x) = -x e^{-x^2/2}.$$
   Since $e^{-x^2/2} > 0$ for all real $x$, $f'(x)$ has the sign of $-x$:
   - $f'(x) > 0$ on $]-\infty \,;\, 0[$: $f$ is strictly increasing.
   - $f'(x) < 0$ on $]0 \,;\, +\infty[$: $f$ is strictly decreasing.
   - At $x = 0$, $f(0) = e^0 = 1$ is the absolute maximum.

2. Differentiate $f'(x)$ as a product $u \cdot v$ with $u(x) = -x$ ($u' = -1$) and $v(x) = e^{-x^2/2}$ ($v' = -x e^{-x^2/2}$):
   $$f''(x) = u'v + uv' = (-1)e^{-x^2/2} + (-x)(-x e^{-x^2/2}) = (-1 + x^2)e^{-x^2/2} = (x^2 - 1)e^{-x^2/2}.$$
   Since $e^{-x^2/2} > 0$, the sign of $f''(x)$ matches $x^2 - 1 = (x - 1)(x + 1)$:
   - $f''(x) \geq 0$ on $]-\infty \,;\, -1] \cup [1 \,;\, +\infty[$: $f$ is **convex** there.
   - $f''(x) \leq 0$ on $[-1 \,;\, 1]$: $f$ is **concave** there.

3. The second derivative $f''$ vanishes while changing sign at $x = -1$ and $x = 1$.
   The associated $y$-values are $f(-1) = f(1) = e^{-1/2} = \frac{1}{\sqrt{e}} \approx 0.6065$.
   The bell curve admits exactly **two inflection points** at $(-1 \,;\, e^{-1/2})$ and $(1 \,;\, e^{-1/2})$.
   *(In probability and statistics, these inflection points correspond precisely to one standard deviation $\pm \sigma$ from the mean).*

---

#### Worked Example 4 — Tangent Line and Relative Position via Convexity

**Problem:** Consider the function $f(x) = (2x - 1)e^x$ on $\mathbb{R}$.
1. Compute $f'(x)$ and $f''(x)$.
2. Prove that $f$ is convex on $[-\frac{1}{2} \,;\, +\infty[$.
3. Determine the equation of the tangent line $(T)$ to $\mathcal{C}_f$ at the point with abscissa 0.
4. Deduce the relative position of $\mathcal{C}_f$ with respect to $(T)$ on $[-\frac{1}{2} \,;\, +\infty[$.

**Solution:**
1. **Derivatives:**
   $f'(x) = 2e^x + (2x - 1)e^x = (2x + 1)e^x$.
   $f''(x) = 2e^x + (2x + 1)e^x = (2x + 3)e^x$.
2. **Convexity:**
   Since $e^x > 0$, the sign of $f''(x)$ is that of $2x + 3$.
   For all $x \geq -\frac{1}{2}$, we have $2x + 3 \geq 2(-\frac{1}{2}) + 3 = -1 + 3 = 2 > 0$.
   Thus $f''(x) \geq 0$ on $[-\frac{1}{2} \,;\, +\infty[$, proving that $f$ is **strictly convex** on this interval.
3. **Tangent at 0:**
   $f(0) = (0 - 1)e^0 = -1$.
   $f'(0) = (0 + 1)e^0 = 1$.
   The equation of tangent $(T)$ is:
   $$y = f'(0)(x - 0) + f(0) = 1(x) - 1 = x - 1.$$
4. **Relative position:**
   Since $f$ is convex on $[-\frac{1}{2} \,;\, +\infty[$ and the contact point $0$ belongs to this interval ($0 \geq -\frac{1}{2}$), the curve $\mathcal{C}_f$ lies **above its tangent $(T)$** on $[-\frac{1}{2} \,;\, +\infty[$.
   That is, for all $x \geq -\frac{1}{2}$:
   $$(2x - 1)e^x \geq x - 1.$$

---

#### Worked Example 5 — Differentiating a Power Function with a Rational Base

**Problem:** Consider the function $f(x) = \left(\dfrac{x - 1}{x + 1}\right)^3$ defined on $\mathbb{R} \setminus \{-1\}$.
Compute its derivative $f'(x)$ and determine its monotonicity on its domain.

**Solution:**
Set $u(x) = \dfrac{x - 1}{x + 1}$.
Compute $u'(x)$ using the quotient rule $\left(\frac{w}{v}\right)' = \frac{w'v - wv'}{v^2}$:
$$u'(x) = \frac{1(x + 1) - (x - 1)(1)}{(x + 1)^2} = \frac{x + 1 - x + 1}{(x + 1)^2} = \frac{2}{(x + 1)^2}.$$
The function $f$ has the form $u^3$, so its derivative is $f'(x) = 3 \, u'(x) \, \big(u(x)\big)^2$:
$$f'(x) = 3 \times \frac{2}{(x + 1)^2} \times \left(\frac{x - 1}{x + 1}\right)^2 = \frac{6(x - 1)^2}{(x + 1)^4}.$$
Examine the sign of $f'(x)$:
- The denominator $(x + 1)^4$ is a 4th power, strictly positive for all $x \neq -1$.
- The numerator $6(x - 1)^2$ is a square multiplied by 6, hence non-negative, vanishing only at $x = 1$.
Consequently, $f'(x) \geq 0$ for all $x \in ]-\infty \,;\, -1[ \cup ]-1 \,;\, +\infty[$.
The function $f$ is therefore **strictly increasing** on $]-\infty \,;\, -1[$ and **strictly increasing** on $]-1 \,;\, +\infty[$.

---

#### Worked Example 6 — Finding the Inflection Point of an Economic Cost Function

**Problem:** A chemical company produces an output quantity $q \in [0 \,;\, 10]$ (in tons) of a polymer. The total production cost in thousands of euros is modeled by:
$$C(q) = q^3 - 6q^2 + 15q + 10.$$
1. Prove that the marginal cost $C'(q)$ is strictly increasing on $[2 \,;\, 10]$.
2. Determine the inflection point of the total cost curve and interpret it economically (law of diminishing returns).

**Solution:**
1. Compute the marginal cost (first derivative) and its rate of change (second derivative):
   $$C'(q) = 3q^2 - 12q + 15.$$
   $$C''(q) = 6q - 12 = 6(q - 2).$$
   For all $q > 2$, $C''(q) > 0$. Thus $C'$ is **strictly increasing** on $[2 \,;\, 10]$.
2. **Inflection point:**
   $C''(q) = 0 \iff 6q - 12 = 0 \iff q = 2$.
   - For $q < 2$, $C''(q) < 0$: the cost function is concave.
   - For $q > 2$, $C''(q) > 0$: the cost function is convex.
   The second derivative vanishes while changing sign at $q = 2$. The point with $q = 2$ is therefore the **inflection point** of the total cost curve.
   *Economic interpretation:*
   - For $q \in [0 \,;\, 2]$, production benefits from economies of scale: each additional ton costs less to produce than the preceding one (marginal cost is decreasing).
   - Past $q = 2$ tons, plant capacity begins to strain, machinery experiences wear, overtime wages accrue: each additional ton becomes progressively more expensive (diminishing returns). The point $q = 2$ marks the structural tipping point.

---

### Key Takeaways

1. **Chain Rule:** $(g \circ u)'(x) = u'(x) \cdot g'\big(u(x)\big)$.
2. **The 3 Essential Composite Derivatives:**
   - $\big(e^u\big)' = u' e^u$
   - $\big(\sqrt{u}\big)' = \dfrac{u'}{2\sqrt{u}}$ (for $u > 0$)
   - $\big(u^n\big)' = n u' u^{n-1}$
3. **Convexity and the Second Derivative:**
   - $f''(x) \geq 0 \iff f'$ is increasing $\iff f$ is convex $\iff$ curve lies above its tangents.
   - $f''(x) \leq 0 \iff f'$ is decreasing $\iff f$ is concave $\iff$ curve lies below its tangents.
4. **Inflection Point:** point where the curve crosses its tangent $\iff f''(x)$ vanishes **while changing sign**.
5. **Fundamental Convexity Inequality:** For all real $x$, $e^x \geq x + 1$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 47.1.** Determine the derivative of each of the following functions:
1. $f(x) = e^{4x - 1}$
2. $g(x) = e^{-x^3}$
3. $h(x) = \sqrt{5x + 2}$ on $]-\frac{2}{5} \,;\, +\infty[$
4. $k(x) = (3x - 7)^5$

**Exercise 47.2.** Compute the second derivative $f''(x)$ for the following functions:
1. $f(x) = 2x^4 - 5x^3 + x - 8$
2. $g(x) = e^{2x}$
3. $h(x) = \dfrac{1}{x}$ on $]0 \,;\, +\infty[$

**Exercise 47.3.** Consider the function $f(x) = x^3 - 6x^2 + 2x - 1$.
1. Compute $f''(x)$.
2. Determine the intervals where $f$ is convex, and where it is concave.
3. Identify the inflection point of its graph.

**Exercise 47.4.** The graph of a twice-differentiable function $f$ has a tangent line at $x_0 = 3$ with equation $y = 4x - 1$.
Given that $f''(x) \geq 0$ for all $x \in \mathbb{R}$, compare without calculation $f(3.1)$ and $11.4$.

**Exercise 47.5.** Determine the derivative of $f(x) = \sqrt{e^x + 1}$ on $\mathbb{R}$.

**Exercise 47.6.** Let $f(x) = x e^{-x}$. Compute $f'(x)$ and $f''(x)$.

**Exercise 47.7.** A function $f$ satisfies $f''(x) = (x - 3)^2 (x + 1)$.
What are the abscissas of the inflection points of the graph of $f$? (Watch out for the trap!).

**Exercise 47.8.** Determine the monotonicity of $f'(x)$ for $f(x) = \dfrac{x^3}{3} - x^2 + 5x$.

---

#### Level ★★ (Guided Reflection and Baccalaureate Style)

**Exercise 47.9 (Baccalaureate Style: Complete Study of an Exponential Function with Convexity).**
Consider the function $f$ defined on $\mathbb{R}$ by:
$$f(x) = (x^2 - 2x + 1)e^x.$$
1. Prove that for all real $x$, $f'(x) = (x^2 - 1)e^x$.
2. Construct the complete variation table of $f$ on $\mathbb{R}$, specifying the limits at $-\infty$ and at $+\infty$.
3. Compute $f''(x)$ and prove that $f''(x) = (x^2 + 2x - 1)e^x$.
4. Determine the intervals of convexity of $f$.
5. Determine the exact abscissas of the inflection points of $\mathcal{C}_f$.

**Exercise 47.10 (Relative Position and Convexity Inequality).**
Let $f(x) = \sqrt{x}$ defined on $[0 \,;\, +\infty[$.
1. Compute $f'(x)$ and $f''(x)$ for $x > 0$.
2. Deduce the concavity of the square root function on $]0 \,;\, +\infty[$.
3. Give the equation of the tangent line $(T)$ to the curve at $x_0 = 1$.
4. Deduce that for all $x > 0$: $\sqrt{x} \leq \dfrac{x + 1}{2}$.
   *(Thus retrieving the arithmetic-geometric mean inequality between $\sqrt{x}$ and the average of $x$ and $1$).*

**Exercise 47.11 (Baccalaureate Style: Skatepark Ramp Profile Analysis).**
An architect designs the cross-section of a skatepark ramp on $[-2 \,;\, 2]$ modeled by:
$$f(x) = \frac{1}{1 + e^{-2x}}.$$
1. Prove that $f'(x) = \dfrac{2e^{-2x}}{(1 + e^{-2x})^2}$.
2. Compute $f''(x)$ and show that it can be written as $f''(x) = \dfrac{4e^{-2x}(e^{-2x} - 1)}{(1 + e^{-2x})^3}$.
3. Determine the inflection point of the ramp. Why does this point correspond to the location where the ramp's steepness is maximal?

**Exercise 47.12 (True or False with Rigorous Arguments).**
1. “If $f''(x_0) = 0$, then the curve of $f$ has an inflection point at $x_0$.”
2. “If a function is strictly increasing, then it is convex.”
3. “The sum of two convex functions on an interval $I$ is a convex function on $I$.”
4. “The product of two convex functions on $I$ is always a convex function on $I$.”

**Exercise 47.13 (Differentiating Trigonometric Composite Functions).**
Compute the derivatives of:
1. $f(x) = \cos(3x^2 - 2)$
2. $g(x) = e^{\sin(x)}$
3. $h(x) = \sin^3(2x)$

**Exercise 47.14 (Convexity of the Reciprocal of a Function).**
Let $u$ be a twice-differentiable, strictly positive, and concave function on an interval $I$.
Set $f = \dfrac{1}{u}$.
1. Compute $f'$ and $f''$ in terms of $u, u'$, and $u''$.
2. Prove that $f$ is convex on $I$.

**Exercise 47.15 (Convexity Inequality for the Square Function).**
Let $f(x) = x^2$ on $\mathbb{R}$.
1. Recall why $f$ is convex.
2. State the geometric definition of convexity for two arbitrary real numbers $a$ and $b$ with midpoint $m = \frac{a+b}{2}$:
   show that $\left(\dfrac{a+b}{2}\right)^2 \leq \dfrac{a^2 + b^2}{2}$.
3. Prove this inequality algebraically by expanding $\frac{a^2+b^2}{2} - \left(\frac{a+b}{2}\right)^2$.

**Exercise 47.16 (Kinematics and Emergency Braking of a High-Speed Train).**
The position (in meters) of a high-speed train during an emergency braking sequence is given for $t \in [0 \,;\, 20]$ (in seconds) by:
$$x(t) = -0.15 t^3 + 4.5 t^2 + 30 t.$$
1. Determine the instantaneous velocity $v(t) = x'(t)$ of the train at $t = 0$ and at $t = 10\text{ s}$.
2. Determine the acceleration $a(t) = x''(t)$.
3. At what time is the deceleration experienced by the passengers strongest in intensity?

**Exercise 47.17 (Complete Study of the Derivative of $u^n$).**
Consider the function $f(x) = (x^2 - 4x + 3)^3$ on $\mathbb{R}$.
1. Determine the zeros of $f$.
2. Compute $f'(x)$ in factored form.
3. Construct the complete variation table of $f$.

---

#### Level ★★★ (Challenge and In-Depth Study)

**Exercise 47.18 (Jensen's Inequality for Convex Functions).**
Let $f$ be a convex function on an interval $I$.
1. The two-point convexity inequality states that for all $\lambda \in [0 \,;\, 1]$ and all $x, y \in I$:
   $$f\big(\lambda x + (1-\lambda)y\big) \leq \lambda f(x) + (1-\lambda)f(y).$$
   Interpret this inequality geometrically by connecting $\lambda$ to the position on the chord $[AB]$.
2. By induction, prove Jensen's inequality for $n$ numbers: if $x_1, x_2, \dots, x_n \in I$, then:
   $$f\left(\frac{x_1 + x_2 + \dots + x_n}{n}\right) \leq \frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}.$$
3. Apply Jensen's inequality to the convex function $f(x) = x^2$ to prove that the mean of squares is always greater than or equal to the square of the mean (non-negativity of variance).

**Exercise 47.19 (Rigorous Proof of Relative Position via Taylor-Lagrange).**
Let $f$ be twice differentiable on an interval $I$. Let $a \in I$.
Taylor's formula with integral remainder shows that for all $x \in I$:
$$f(x) - \big[f'(a)(x - a) + f(a)\big] = \int_a^x (x - t) f''(t) \, dt.$$
1. Show that the integrand $(x - t)f''(t)$ maintains a non-negative sign for $t$ between $a$ and $x$ provided that $f''(t) \geq 0$.
2. Deduce analytically that any function satisfying $f'' \geq 0$ lies above its tangent line at every point $a$.

**Exercise 47.20 (Cubic Polynomial with Imposed Inflection Point).**
Consider a general degree-3 polynomial: $P(x) = ax^3 + bx^2 + cx + d$ with $a \neq 0$.
1. Compute $P''(x)$.
2. Prove that the graph of **every degree-3 polynomial** has a unique inflection point $I$, whose abscissa is $x_I = -\dfrac{b}{3a}$.
3. Prove that the inflection point $I$ is the center of symmetry of the graph of $P$.

**Exercise 47.21 (Composite of Two Convex Functions).**
Let $u : I \to J$ and $g : J \to \mathbb{R}$ be two twice-differentiable functions.
1. Compute $(g \circ u)''(x)$ in terms of the first and second derivatives of $g$ and $u$.
2. Prove that if $u$ is convex and $g$ is **convex AND increasing**, then the composite $g \circ u$ is convex on $I$.
3. Give a counterexample showing that if $g$ is not increasing, the result can fail.

**Exercise 47.22 (General AM-GM Inequality via Convexity).**
Assume that the function $x \mapsto -\ln(x)$ is strictly convex on $]0 \,;\, +\infty[$.
1. Let $x_1, x_2, \dots, x_n$ be strictly positive real numbers. Apply Jensen's inequality to $-\ln(x)$.
2. Using logarithm properties, deduce the general Arithmetic Mean - Geometric Mean (AM-GM) inequality for $n$ numbers:
   $$\sqrt[n]{x_1 x_2 \dots x_n} \leq \frac{x_1 + x_2 + \dots + x_n}{n}.$$

---

### Solutions

#### Solutions for Level ★

- **47.1:**
  1. $u(x) = 4x - 1 \implies u'(x) = 4$. $f'(x) = 4e^{4x-1}$.
  2. $u(x) = -x^3 \implies u'(x) = -3x^2$. $g'(x) = -3x^2 e^{-x^3}$.
  3. $u(x) = 5x + 2 \implies u'(x) = 5$. $h'(x) = \dfrac{5}{2\sqrt{5x+2}}$.
  4. $u(x) = 3x - 7 \implies u'(x) = 3$. $k'(x) = 5 \times 3 \times (3x - 7)^4 = 15(3x - 7)^4$.

- **47.2:**
  1. $f'(x) = 8x^3 - 15x^2 + 1 \implies f''(x) = 24x^2 - 30x$.
  2. $g'(x) = 2e^{2x} \implies g''(x) = 4e^{2x}$.
  3. $h'(x) = -\frac{1}{x^2} = -x^{-2} \implies h''(x) = 2x^{-3} = \frac{2}{x^3}$.

- **47.3:**
  1. $f'(x) = 3x^2 - 12x + 2 \implies f''(x) = 6x - 12 = 6(x - 2)$.
  2. For $x \leq 2$, $f''(x) \leq 0$: $f$ is concave. For $x \geq 2$, $f''(x) \geq 0$: $f$ is convex.
  3. $f''$ vanishes while changing sign at $x = 2$. $f(2) = 8 - 24 + 4 - 1 = -13$. The inflection point is $I(2 \,;\, -13)$.

- **47.4:** Since $f''(x) \geq 0$, $f$ is convex on $\mathbb{R}$, so its curve lies above its tangent line $y = 4x - 1$.
  For $x = 3.1$, the tangent gives $4(3.1) - 1 = 12.4 - 1 = 11.4$.
  Since the curve is above the tangent, $f(3.1) \geq 11.4$.

- **47.5:** $u(x) = e^x + 1 > 0$, $u'(x) = e^x$. $f'(x) = \dfrac{e^x}{2\sqrt{e^x + 1}}$.

- **47.6:**
  $f'(x) = 1 \cdot e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}$.
  $f''(x) = (-1)e^{-x} + (1 - x)(-e^{-x}) = (-1 - 1 + x)e^{-x} = (x - 2)e^{-x}$.

- **47.7:** For all real $x$, $(x - 3)^2 \geq 0$. Thus $f''(x)$ has the sign of $x + 1$.
  - At $x = 3$, $f''(3) = 0$, but $f''$ does not change sign around 3: **no inflection point at 3!**
  - At $x = -1$, $f''(-1) = 0$ and $f''$ changes from negative to positive: **unique inflection point at $x = -1$**.

- **47.8:** $f'(x) = x^2 - 2x + 5$. The derivative of $f'$ is $f''(x) = 2x - 2 = 2(x - 1)$.
  $f'$ is strictly decreasing on $]-\infty \,;\, 1]$ and strictly increasing on $[1 \,;\, +\infty[$.

---

#### Solutions for Level ★★

- **47.9:**
  1. $f(x) = (x^2 - 2x + 1)e^x = (x-1)^2 e^x$.
     $f'(x) = (2x - 2)e^x + (x^2 - 2x + 1)e^x = (x^2 - 1)e^x$.
  2. Sign of $f'(x)$: since $e^x > 0$, it has the sign of $x^2 - 1 = (x - 1)(x + 1)$.
     Increasing on $]-\infty ; -1]$, decreasing on $[-1 ; 1]$, increasing on $[1 ; +\infty[$.
     At $-\infty$: $(x^2 - 2x + 1)e^x \to 0$ by comparative growth.
     At $+\infty$: $\lim f(x) = +\infty$.
     Local max at $-1$: $f(-1) = 4e^{-1} = 4/e \approx 1.47$. Local min at $1$: $f(1) = 0$.
  3. $f''(x) = (2x)e^x + (x^2 - 1)e^x = (x^2 + 2x - 1)e^x$.
  4. Roots of $x^2 + 2x - 1$: $\Delta = 4 - 4(1)(-1) = 8 = (2\sqrt{2})^2$.
     $x_1 = \frac{-2 - 2\sqrt{2}}{2} = -1 - \sqrt{2} \approx -2.41$.
     $x_2 = -1 + \sqrt{2} \approx 0.41$.
     $f$ is convex on $]-\infty \,;\, -1-\sqrt{2}]$ and on $[-1+\sqrt{2} \,;\, +\infty[$.
     $f$ is concave on $[-1-\sqrt{2} \,;\, -1+\sqrt{2}]$.
  5. The inflection point abscissas are $x_1 = -1 - \sqrt{2}$ and $x_2 = -1 + \sqrt{2}$.

- **47.10:**
  1. $f'(x) = \frac{1}{2\sqrt{x}} = \frac{1}{2} x^{-1/2}$.
     $f''(x) = \frac{1}{2} \left(-\frac{1}{2}\right) x^{-3/2} = -\frac{1}{4x\sqrt{x}}$.
  2. For all $x > 0$, $4x\sqrt{x} > 0$, so $f''(x) < 0$: the square root function is **strictly concave** on $]0 \,;\, +\infty[$.
  3. At $x_0 = 1$: $f(1) = 1$, $f'(1) = 1/2$. Tangent: $y = \frac{1}{2}(x - 1) + 1 = \frac{1}{2}x + \frac{1}{2} = \frac{x+1}{2}$.
  4. The graph of a concave function lies entirely below its tangents, so for all $x > 0$: $\sqrt{x} \leq \frac{x+1}{2}$.

- **47.11:**
  1. $f(x) = (1 + e^{-2x})^{-1}$.
     $f'(x) = -( -2e^{-2x} )(1 + e^{-2x})^{-2} = \frac{2e^{-2x}}{(1 + e^{-2x})^2}$.
  2. Differentiate as a quotient $u/v$:
     $u' = -4e^{-2x}$, $v' = 2(1 + e^{-2x})(-2e^{-2x}) = -4e^{-2x}(1 + e^{-2x})$.
     $f''(x) = \frac{-4e^{-2x}(1 + e^{-2x})^2 - 2e^{-2x}[-4e^{-2x}(1 + e^{-2x})]}{(1 + e^{-2x})^4} = \frac{-4e^{-2x}(1 + e^{-2x}) + 8e^{-4x}}{(1 + e^{-2x})^3} = \frac{4e^{-2x}(e^{-2x} - 1)}{(1 + e^{-2x})^3}$.
  3. $f''(x) = 0 \iff e^{-2x} - 1 = 0 \iff -2x = 0 \iff x = 0$.
     $f''$ changes sign at 0. The inflection point is $(0 \,;\, 1/2)$.
     Since $f''(0) = 0$, the first derivative $f'$ has an extremum at 0: $f'(0) = \frac{2}{(1+1)^2} = \frac{2}{4} = \frac{1}{2}$. This is the maximal slope of the ramp.

- **47.12:**
  1. **False.** Counterexample: $f(x) = x^4$ at 0 ($f''(0) = 0$ but $f'' \geq 0$ does not change sign).
  2. **False.** Counterexample: $f(x) = \sqrt{x}$ is strictly increasing and strictly concave.
  3. **True.** If $f$ and $g$ are convex, $(f + g)'' = f'' + g'' \geq 0$.
  4. **False.** Counterexample: $f(x) = x$ and $g(x) = -x$ are linear (convex/concave), but their product is $-x^2$, which is strictly concave!

- **47.13:**
  1. $(\cos u)' = -u' \sin u$. $u(x) = 3x^2 - 2 \implies u' = 6x$. $f'(x) = -6x \sin(3x^2 - 2)$.
  2. $(e^u)' = u' e^u$. $u(x) = \sin x \implies u' = \cos x$. $g'(x) = \cos(x)e^{\sin(x)}$.
  3. $h(x) = v^3$ with $v(x) = \sin(2x)$. $v'(x) = 2\cos(2x)$.
     $h'(x) = 3 v' v^2 = 3(2\cos(2x))\sin^2(2x) = 6\cos(2x)\sin^2(2x)$.

- **47.14:**
  1. $f = u^{-1} \implies f' = -u' u^{-2} = -\frac{u'}{u^2}$.
     $f'' = \left(-\frac{u'}{u^2}\right)' = -\frac{u'' u^2 - u'(2uu')}{u^4} = -\frac{u'' u - 2(u')^2}{u^3} = \frac{2(u')^2 - u u''}{u^3}$.
  2. Since $u$ is concave, $u'' \leq 0$, so $-u u'' \geq 0$ (since $u > 0$).
     Since $(u')^2 \geq 0$ and $u^3 > 0$, the numerator $2(u')^2 - u u'' \geq 0$ and the denominator is strictly positive.
     Thus $f'' \geq 0$: the function $f$ is convex on $I$.

- **47.15:**
  1. $f''(x) = 2 > 0$ on $\mathbb{R}$, so $f$ is convex.
  2. The segment connecting $(a ; a^2)$ and $(b ; b^2)$ has midpoint ordinate $\frac{a^2+b^2}{2}$. The image of the midpoint abscissa is $\left(\frac{a+b}{2}\right)^2$. By convexity, the curve lies below the chord: $\left(\frac{a+b}{2}\right)^2 \leq \frac{a^2+b^2}{2}$.
  3. $\frac{a^2+b^2}{2} - \frac{a^2+2ab+b^2}{4} = \frac{2a^2+2b^2 - a^2 - 2ab - b^2}{4} = \frac{a^2 - 2ab + b^2}{4} = \frac{(a-b)^2}{4} \geq 0$.

- **47.16:**
  1. $v(t) = x'(t) = -0.45 t^2 + 9 t + 30$.
     $v(0) = 30\text{ m/s}$ (i.e. $108\text{ km/h}$).
     $v(10) = -0.45(100) + 90 + 30 = -45 + 120 = 75\text{ m/s}$.
  2. $a(t) = x''(t) = -0.9 t + 9$.
  3. Acceleration $a(t)$ decreases linearly from $+9\text{ m/s}^2$ at $t = 0$ down to $a(20) = -0.9(20) + 9 = -18 + 9 = -9\text{ m/s}^2$. Maximum deceleration occurs at $t = 20\text{ s}$ with magnitude $9\text{ m/s}^2$ (almost 1 g!).

- **47.17:**
  1. $x^2 - 4x + 3 = 0 \iff (x - 1)(x - 3) = 0$. Zeros are $1$ and $3$.
  2. $f'(x) = 3(2x - 4)(x^2 - 4x + 3)^2 = 6(x - 2)(x - 1)^2(x - 3)^2$.
  3. For all $x \in \mathbb{R}$, $(x-1)^2(x-3)^2 \geq 0$. The sign of $f'(x)$ is that of $x - 2$.
     $f$ is strictly decreasing on $]-\infty \,;\, 2]$ and strictly increasing on $[2 \,;\, +\infty[$.
     Minimum at $x = 2$: $f(2) = (4 - 8 + 3)^3 = (-1)^3 = -1$.
     At $x = 1$ and $x = 3$, $f'(x) = 0$: horizontal inflection tangents (saddle points / flat spots).

---

#### Solutions for Level ★★★

- **47.18:**
  1. $\lambda x + (1-\lambda)y$ is the weighted average (convex combination) of the $x$-coordinates of $A(x, f(x))$ and $B(y, f(y))$, and $\lambda f(x) + (1-\lambda)f(y)$ is the corresponding $y$-coordinate on the chord $[AB]$. The inequality expresses that points on the graph lie below or on the chord.
  2. Induction on $n$: true for $n = 2$. Assume true for $n$.
     Write $\frac{x_1 + \dots + x_{n+1}}{n+1} = \frac{n}{n+1} \left(\frac{x_1 + \dots + x_n}{n}\right) + \frac{1}{n+1} x_{n+1}$.
     Applying 2-point convexity with $\lambda = \frac{n}{n+1}$, and then the induction hypothesis, gives the result for $n+1$.
  3. With $f(x) = x^2$: $\left(\frac{\sum x_i}{n}\right)^2 \leq \frac{\sum x_i^2}{n} \iff \overline{x}^2 \leq \overline{x^2} \iff V(X) = \overline{x^2} - \overline{x}^2 \geq 0$.

- **47.19:**
  1. If $x > a$, for all $t \in [a \,;\, x]$, $x - t \geq 0$. Since $f''(t) \geq 0$, the integrand is non-negative. Its integral from $a$ to $x$ is non-negative.
     If $x < a$, $x - t \leq 0$ for $t \in [x \,;\, a]$. The integral from $a$ to $x$ equals $-\int_x^a (x - t)f''(t) dt = \int_x^a (t - x)f''(t) dt \geq 0$.
  2. In both cases, $f(x) - [f'(a)(x - a) + f(a)] \geq 0$, rigorously proving that the curve remains above its tangent at every point $a$.

- **47.20:**
  1. $P'(x) = 3ax^2 + 2bx + c \implies P''(x) = 6ax + 2b$.
  2. $P''(x) = 0 \iff 6ax + 2b = 0 \iff x = -\frac{2b}{6a} = -\frac{b}{3a}$.
     Since $a \neq 0$, $6ax + 2b$ is a linear function with non-zero slope, which necessarily changes sign at $x_I = -\frac{b}{3a}$. Every cubic polynomial therefore has exactly one inflection point.
  3. Under the substitution $X = x - x_I$, the quadratic term vanishes in $P(X + x_I)$: the polynomial takes the form $aX^3 + pX + Y_I$, which satisfies $P(X) - Y_I = -(P(-X) - Y_I)$: an odd function centered at $(x_I ; Y_I)$, establishing point symmetry.

- **47.21:**
  1. $(g \circ u)' = u' \cdot (g' \circ u)$.
     By the product rule:
     $$(g \circ u)'' = u'' \cdot (g' \circ u) + u' \cdot [ (g' \circ u)' ] = u'' \cdot (g' \circ u) + (u')^2 \cdot (g'' \circ u).$$
  2. Since $u$ is convex, $u'' \geq 0$. Since $g$ is increasing, $g' \geq 0$, so $u'' \cdot (g' \circ u) \geq 0$.
     Furthermore, $(u')^2 \geq 0$, and since $g$ is convex, $g'' \geq 0$, so $(u')^2 \cdot (g'' \circ u) \geq 0$.
     The sum of two non-negative terms is non-negative: $(g \circ u)'' \geq 0$, so $g \circ u$ is convex.
  3. Counterexample if $g$ is not increasing: $u(x) = x^2$ (convex on $\mathbb{R}$) and $g(y) = -y$ (convex on $\mathbb{R}$).
     The composite is $(g \circ u)(x) = -x^2$, which is strictly concave!

- **47.22:**
  1. Let $f(x) = -\ln(x)$ on $]0 \,;\, +\infty[$. $f'(x) = -1/x$, $f''(x) = 1/x^2 > 0$: $f$ is strictly convex.
     By Jensen's inequality:
     $$-\ln\left(\frac{x_1 + \dots + x_n}{n}\right) \leq \frac{-\ln(x_1) - \dots - \ln(x_n)}{n} = -\frac{1}{n} \ln(x_1 \dots x_n) = -\ln\big((x_1 \dots x_n)^{1/n}\big).$$
  2. Multiply by $-1$ (reversing the inequality):
     $$\ln\left(\frac{x_1 + \dots + x_n}{n}\right) \geq \ln\left((x_1 \dots x_n)^{1/n}\right).$$
     Since the exponential function is strictly increasing:
     $$\frac{x_1 + \dots + x_n}{n} \geq \sqrt[n]{x_1 x_2 \dots x_n}. \quad \blacksquare$$

---

### The Question That Opens What Follows

We have seen that the exponential function $x \mapsto e^x$ is the sovereign of functions: it turns addition into multiplication, its derivative is equal to itself, and its curve is entirely convex above its tangent $y = x + 1$.
Yet what happens if an astronomer or a navigator needs to retrace the steps in reverse?
What if one knows the final power and seeks **the exponent that produced it**?
How did a graduated slide rule and printed calculation tables enable seventeenth-century sailors to navigate across oceans without performing a single long multiplication by hand?

This is the saga of **John Napier** and the **natural logarithm** function. See you in Chapter 48.
