# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 35: Galileo's Fountain and the Parabola

> *“Watch the water surge from the marble basin: it leaps forth with fire, seems to hesitate for an instant at the summit of its luminous arch, then falls back in a graceful curve into the pool. This perfect drawing that gravity traces in the air is not an arc of a circle: it is a parabola. From the scholars of Babylon and Baghdad to Galileo, the art of the second degree is the master key that unlocks the trajectories of worlds.”*

---

### What You Are About to Discover

- Why the trajectory of a water jet or a projectile subject to gravity inevitably forms a **parabola**.
- The metamorphosis of the expression: moving from the **expanded standard form** $ax^2 + bx + c$ to the **canonical (vertex) form** $a(x - \alpha)^2 + \beta$ through Al-Khwarizmi's completion of the square.
- The **vertex** $S(\alpha, \beta)$ and the axis of symmetry of a parabola.
- The unveiled mystery of the **discriminant** $\Delta = b^2 - 4ac$: the step-by-step proof that explains why it dictates whether there are 0, 1, or 2 roots.
- The **factored form** and the golden rule for the **sign of the quadratic trinomial** (“the sign of $a$ outside the roots”).
- **Viète's formulas** relating the roots to their sum $S = -\frac{b}{a}$ and product $P = \frac{c}{a}$.

---

### 1. The Problem: Galileo and the Water Jet of the Medici Gardens

In Florence, at the beginning of the summer of 1608, **Galileo Galilei** is strolling through the gardens of the Villa Medici. His gaze is drawn to a monumental fountain. A brass nozzle directs a jet of water at forty-five degrees: a slender crystalline stream shoots forth, rises toward the sky, rounds off at its zenith, and plunges back into the basin.

At that time, treatises on artillery inherited from Aristotelian physics claimed that a cannonball traveled in a straight line under the effect of the gunpowder blast, came to an abrupt halt in midair once its impetus was exhausted, and then dropped vertically to the ground!

Galileo knows this vision is absurd. He decomposes the motion of each droplet of water into two simultaneous, independent actions:
1. **Horizontally ($x$):** No obstacle impedes the water (neglecting air resistance). The droplet advances at a constant horizontal speed $v_0$:
   $$x(t) = v_0 \times t.$$
2. **Vertically ($y$):** The Earth pulls the droplet downward with a constant acceleration $g$. According to Galileo's law of falling bodies, the altitude decreases proportionally to the **square of elapsed time**:
   $$y(t) = -\frac{1}{2}g t^2 + h_0.$$

```
       y ▲               Vertex S
         │                 ╭───╮
         │               ╭╯     ╰╮
         │             ╭╯         ╰╮   Water Jet
         │            ╭╯             ╰╮
         │           o                 ╰╮
       h0┼──────────►                    ▼
         O ┼──────────────────────────────┼─────► x
                                         Impact
```

Let us eliminate time $t$! From the first equation, we get $t = \frac{x}{v_0}$. Substituting this value into the second equation, the altitude $y$ as a function of horizontal distance $x$ becomes:
$$y = -\frac{g}{2 v_0^2} x^2 + h_0.$$

This is an equation in which altitude depends on the **square** of the distance traveled: a **quadratic polynomial function** (a polynomial of the second degree). The resulting curve is neither a circle nor an ellipse: it is a **parabola**.

To calculate the maximum height reached by the water, or to determine the exact distance at which the jet hits the surface of the basin ($y = 0$), we must master the algebra of quadratic trinomials.

---

### 2. The Quadratic Trinomial and Canonical (Vertex) Form

#### 2.1 Definitions and Standard Form

> **📐 Definition — Quadratic Polynomial Function.**
> A **quadratic polynomial function** (or **quadratic trinomial**) is any function $f$ defined on $\mathbb{R}$ by:
> $$f(x) = ax^2 + bx + c$$
> where $a, b, c$ are fixed real numbers, with **$a \neq 0$**.
> This expression is called the **standard form** (or expanded form) of the trinomial.

- The term $a$ is the quadratic coefficient (we must have $a \neq 0$, otherwise the expression would reduce to an affine function $bx + c$).
- The term $b$ is the linear coefficient (degree 1).
- The term $c$ is the constant term (the $y$-intercept, since $f(0) = c$).

#### 2.2 Completing the Square: Al-Khwarizmi's Legacy

How can we find the vertex of a parabola without guesswork?
The brilliant idea dates back to the Persian mathematician **Al-Khwarizmi** (around 820 in Baghdad): it consists in geometrically reconstructing a perfect square so that the variable $x$ appears **only once** in the entire expression!

> **📐 Fundamental Theorem — The Canonical (Vertex) Form.**
> Every quadratic trinomial $f(x) = ax^2 + bx + c$ ($a \neq 0$) can be uniquely written in **canonical (vertex) form**:
> $$\boxed{f(x) = a(x - \alpha)^2 + \beta}$$
> where:
> $$\alpha = -\frac{b}{2a} \quad \text{and} \quad \beta = f(\alpha) = -\frac{b^2 - 4ac}{4a}.$$

> **✍️ Proof (Required knowledge) — Conversion to Canonical Form.**
> Start with the standard form:
> $$f(x) = ax^2 + bx + c.$$
> 1. Factor out the coefficient $a \neq 0$ from the first two terms:
>    $$f(x) = a\left[ x^2 + \frac{b}{a}x \right] + c.$$
> 2. Look at the expression inside the brackets: $x^2 + \frac{b}{a}x$ resembles the beginning of the expansion of a binomial square $(x + d)^2 = x^2 + 2dx + d^2$.
>    To make the cross-term $2dx$ equal to $\frac{b}{a}x$, we must choose $d = \frac{b}{2a}$.
>    We then have:
>    $$\left(x + \frac{b}{2a}\right)^2 = x^2 + 2\left(\frac{b}{2a}\right)x + \left(\frac{b}{2a}\right)^2 = x^2 + \frac{b}{a}x + \frac{b^2}{4a^2}.$$
>    From this, we deduce that:
>    $$x^2 + \frac{b}{a}x = \left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2}.$$
> 3. Substitute this identity back into the expression for $f(x)$:
>    $$f(x) = a\left[ \left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} \right] + c.$$
> 4. Distribute $a$ across the brackets:
>    $$f(x) = a\left(x + \frac{b}{2a}\right)^2 - a \times \frac{b^2}{4a^2} + c = a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a} + \frac{4ac}{4a}.$$
> 5. Combine the last two terms over the common denominator $4a$:
>    $$f(x) = a\left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a}.$$
> Setting $\alpha = -\frac{b}{2a}$ and $\beta = -\frac{b^2 - 4ac}{4a}$, we obtain the canonical form:
> $$f(x) = a(x - \alpha)^2 + \beta. \quad \blacksquare$$

---

### 3. Geometry of the Parabola: Vertex and Axis of Symmetry

Thanks to the canonical form $f(x) = a(x - \alpha)^2 + \beta$, the geometric properties of the curve become crystal clear:
Since a square of a real number is always non-negative:
$$(x - \alpha)^2 \ge 0 \quad \text{for all } x \in \mathbb{R},$$
with equality if and only if $x = \alpha$.

Two cases arise depending on the sign of $a$:

```
             CASE a > 0                                CASE a < 0
          (Opens UPWARD)                            (Opens DOWNWARD)
             y ▲                                       y ▲
           \   │   /                                     │      Vertex S(α, β)
            \  │  /                                      │        ╭───╮
             \ │ /                                     β ┼───────╭╯   ╰╮
              \│/                                        │      ╭╯     ╰╮
             β ┼───o Vertex S(α, β)                      │     ╭╯       ╰╮
               │   │                                     │    /           \
             O ┼───┼───────► x                         O ┼───┼─────────────► x
                   α                                         α
```

1. **If $a > 0$:**
   $a(x - \alpha)^2 \ge 0$, hence $f(x) \ge \beta$.
   The function attains an **absolute minimum** equal to $\beta$, reached at $x = \alpha$.
   The parabola **opens upward** (bowl shape).
   $f$ is strictly decreasing on $]-\infty, \alpha]$ and strictly increasing on $[\alpha, +\infty[$.

2. **If $a < 0$:**
   $a(x - \alpha)^2 \le 0$, hence $f(x) \le \beta$.
   The function attains an **absolute maximum** equal to $\beta$, reached at $x = \alpha$.
   The parabola **opens downward** (hill shape).
   $f$ is strictly increasing on $]-\infty, \alpha]$ and strictly decreasing on $[\alpha, +\infty[$.

> **📐 Fundamental Properties of the Parabola —**
> - The **vertex** of the parabola is the point $S(\alpha, \beta)$ with $\alpha = -\frac{b}{2a}$ and $\beta = f(\alpha)$.
> - The vertical line with equation $x = \alpha$ is the **axis of symmetry** of the parabola.

---

### 4. The Quadratic Equation and the Discriminant $\Delta$

Solving the equation $ax^2 + bx + c = 0$ corresponds geometrically to finding the points where the parabola intersects the horizontal axis ($y = 0$).

#### 4.1 The Birth of the Discriminant

Let us return to Step 3 of completing the square:
$$a\left[ \left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a^2} \right] = 0.$$
Since $a \neq 0$, this equation is equivalent to:
$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}.$$

The left-hand side is a perfect square: it is always greater than or equal to zero.
The denominator on the right-hand side, $4a^2 = (2a)^2$, is strictly positive.
Everything therefore depends exclusively on the sign of the numerator:
$$\Delta = b^2 - 4ac.$$

> **📐 Definition — Discriminant.**
> The real number $\Delta = b^2 - 4ac$ is called the **discriminant** of the trinomial $ax^2 + bx + c$.
> The uppercase Greek letter $\Delta$ (“Delta”) was chosen by nineteenth-century mathematicians because it is the initial letter of *discriminare* in Latin, which means “to separate”, “to distinguish”. It discriminates between the possible outcomes.

#### 4.2 The Three Fundamental Cases

> **📐 Fundamental Theorem — Solving $ax^2 + bx + c = 0$.**
> 
> 1. **If $\Delta < 0$:**
>    The right-hand side $\frac{\Delta}{4a^2}$ is strictly negative. But a real square can never be negative.
>    The equation has **no real solution** ($S = \varnothing$).
>    The parabola never crosses or touches the horizontal axis.
> 
> 2. **If $\Delta = 0$:**
>    The equation becomes $\left(x + \frac{b}{2a}\right)^2 = 0$, whence $x + \frac{b}{2a} = 0$.
>    The equation has **a unique real solution** (called a double root):
>    $$x_0 = -\frac{b}{2a}.$$
>    The vertex of the parabola rests exactly on the horizontal axis (the axis is tangent to the curve).
> 
> 3. **If $\Delta > 0$:**
>    The number $\Delta$ possesses a positive real square root $\sqrt{\Delta} > 0$.
>    The equation becomes:
>    $$\left(x + \frac{b}{2a}\right)^2 - \left(\frac{\sqrt{\Delta}}{2a}\right)^2 = 0.$$
>    Using the difference of two squares $A^2 - B^2 = (A - B)(A + B)$:
>    $$\left(x + \frac{b}{2a} - \frac{\sqrt{\Delta}}{2a}\right)\left(x + \frac{b}{2a} + \frac{\sqrt{\Delta}}{2a}\right) = 0.$$
>    By the zero-product property, the equation admits **two distinct real solutions**:
>    $$\boxed{x_1 = \frac{-b - \sqrt{\Delta}}{2a}} \quad \text{and} \quad \boxed{x_2 = \frac{-b + \sqrt{\Delta}}{2a}}.$$
>    The parabola crosses the horizontal axis at two distinct points with coordinates $(x_1, 0)$ and $(x_2, 0)$.

---

### 5. Factored Form and the Sign of the Trinomial

#### 5.1 Factored Form

Knowing the roots of a trinomial allows us to write it as a product of first-degree factors:

> **📐 Theorem — Factored Form.**
> - If $\Delta > 0$: $f(x) = a(x - x_1)(x - x_2)$.
> - If $\Delta = 0$: $f(x) = a(x - x_0)^2$.
> - If $\Delta < 0$: $f(x)$ cannot be factored into a product of linear factors in $\mathbb{R}$.

> **⚠️ Beware: Common Pitfall! Never forget the leading coefficient $a$!**
> This is the most common error: writing $(x - x_1)(x - x_2)$ while forgetting to multiply by the coefficient $a$ in front.
> For example, $2x^2 - 6x + 4 = 0$ has roots $1$ and $2$. Its factored form is $2(x - 1)(x - 2)$, and not $(x - 1)(x - 2)$ (which would expand to $x^2 - 3x + 2$).

#### 5.2 The Sign of the Trinomial

> **📐 Golden Rule — Sign of $ax^2 + bx + c$.**
> 
> 1. **If $\Delta < 0$:**
>    The trinomial never vanishes. It **always has the same sign as $a$** over all of $\mathbb{R}$.
> 
> 2. **If $\Delta = 0$:**
>    The trinomial vanishes at $x_0 = -\frac{b}{2a}$ and **has the same sign as $a$ everywhere else**.
> 
> 3. **If $\Delta > 0$:** (assuming $x_1 < x_2$)
>    The trinomial is:
>    - **of the sign of $a$ outside the roots** (for $x < x_1$ and for $x > x_2$);
>    - **of the opposite sign of $a$ (sign of $-a$) between the roots** (for $x_1 < x < x_2$).

> **Summary Sign Chart for $\Delta > 0$:**
>
> | $x$ | $-\infty$ | | $x_1$ | | $x_2$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | Sign of $ax^2+bx+c$ | | **sign of $a$** | $0$ | **sign of $-a$** | $0$ | **sign of $a$** | |

**Vivid Geometric Intuition:**
If $a > 0$, the parabola opens its arms toward the sky. To dip below the horizontal axis, it must plunge between the two roots: the bowl is below the axis (negative) exclusively *between* $x_1$ and $x_2$. Everywhere else, it stays above the axis (positive)!

---

### 6. Viète's Formulas: Sum and Product of the Roots

In 1591, the French jurist and cryptographer to King Henry IV, **François Viète**, discovered fascinating connections directly linking the coefficients of a polynomial to its roots, without calculating $\Delta$.

> **📐 Theorem (Viète's Formulas) —**
> If the trinomial $ax^2 + bx + c$ admits two real roots $x_1$ and $x_2$ (which may coincide if $\Delta = 0$), then:
> $$\boxed{S = x_1 + x_2 = -\frac{b}{a}} \quad \text{and} \quad \boxed{P = x_1 \times x_2 = \frac{c}{a}}.$$

> **✍️ Proof —**
> Expand the factored form $a(x - x_1)(x - x_2)$:
> $$a(x - x_1)(x - x_2) = a\left[ x^2 - (x_1 + x_2)x + x_1 x_2 \right] = ax^2 - a(x_1 + x_2)x + a(x_1 x_2).$$
> Matching coefficients with the standard form $ax^2 + bx + c$:
> $$-a(x_1 + x_2) = b \implies x_1 + x_2 = -\frac{b}{a},$$
> $$a(x_1 x_2) = c \implies x_1 x_2 = \frac{c}{a}. \quad \blacksquare$$

#### 6.1 Finding Two Numbers Knowing Their Sum and Product

Two numbers $u$ and $v$ have sum $S$ and product $P$ if and only if they are the solutions to the quadratic equation:
$$\boxed{X^2 - SX + P = 0}$$

#### 6.2 The Art of Spotting Obvious Roots

Before rushing to compute the discriminant, always check if an **obvious root** exists:
- **If $a + b + c = 0$**, then $x_1 = 1$ is an obvious root. The second root is then immediately $x_2 = \frac{c}{a}$.
- **If $a - b + c = 0$**, then $x_1 = -1$ is an obvious root. The second root is $x_2 = -\frac{c}{a}$.
- **If $c = 0$**, then $x_1 = 0$ is an obvious root, and $x_2 = -\frac{b}{a}$.

---

### 7. Detailed Worked Examples

> **Worked Example 1 — Converting to Canonical Form in Practice.**
> Write the trinomial $P(x) = 2x^2 - 8x + 11$ in canonical form.
> Deduce the coordinates of the vertex of the parabola and its extremum.
>
> **Solution:**
> 1. Factor the leading coefficient $a = 2$ out of the terms in $x$:
>    $$P(x) = 2(x^2 - 4x) + 11.$$
> 2. Complete the square: $x^2 - 4x = (x - 2)^2 - 4$.
> 3. Substitute back:
>    $$P(x) = 2\left[(x - 2)^2 - 4\right] + 11 = 2(x - 2)^2 - 8 + 11 = 2(x - 2)^2 + 3.$$
> **Conclusion:**
> The canonical form is $\boxed{P(x) = 2(x - 2)^2 + 3}$.
> Here $\alpha = 2$ and $\beta = 3$.
> The vertex of the parabola is the point $S(2, 3)$.
> Since $a = 2 > 0$, the function achieves an **absolute minimum equal to $3$**, attained at $x = 2$.
> (Note: since its minimum is $3 > 0$, the parabola never dips below 0, so $P(x) = 0$ has no real solution).

> **Worked Example 2 — Solving Equations with the Discriminant.**
> Solve the following three equations in $\mathbb{R}$:
> a) $3x^2 - 5x - 2 = 0$ \quad b) $4x^2 - 12x + 9 = 0$ \quad c) $2x^2 + 3x + 5 = 0$
>
> **Step-by-Step Solution:**
> a) $a = 3, b = -5, c = -2$.
>    $$\Delta = b^2 - 4ac = (-5)^2 - 4(3)(-2) = 25 + 24 = 49.$$
>    Since $\Delta = 49 > 0$, there are two distinct real solutions ($\sqrt{\Delta} = 7$):
>    $$x_1 = \frac{-(-5) - 7}{2(3)} = \frac{5 - 7}{6} = \frac{-2}{6} = -\frac{1}{3},$$
>    $$x_2 = \frac{-(-5) + 7}{2(3)} = \frac{5 + 7}{6} = \frac{12}{6} = 2.$$
>    $S = \left\{-\frac{1}{3}, 2\right\}$. Factored form: $3\left(x + \frac{1}{3}\right)(x - 2) = (3x + 1)(x - 2)$.
>
> b) $a = 4, b = -12, c = 9$.
>    $$\Delta = (-12)^2 - 4(4)(9) = 144 - 144 = 0.$$
>    Since $\Delta = 0$, there is a unique double root:
>    $$x_0 = -\frac{b}{2a} = -\frac{-12}{2(4)} = \frac{12}{8} = \frac{3}{2}.$$
>    $S = \left\{\frac{3}{2}\right\}$. Factored form: $4\left(x - \frac{3}{2}\right)^2 = (2x - 3)^2$.
>
> c) $a = 2, b = 3, c = 5$.
>    $$\Delta = 3^2 - 4(2)(5) = 9 - 40 = -31 < 0.$$
>    Since $\Delta < 0$, the equation has no real solutions: $S = \varnothing$.

> **Worked Example 3 — Solving a Quadratic Inequality.**
> Solve the following inequality in $\mathbb{R}$:
> $$-2x^2 + 7x - 3 \ge 0.$$
>
> **Solution:**
> 1. First, find the roots of the trinomial:
>    $$\Delta = 7^2 - 4(-2)(-3) = 49 - 24 = 25 > 0 \implies \sqrt{\Delta} = 5.$$
>    $$x_1 = \frac{-7 - 5}{2(-2)} = \frac{-12}{-4} = 3, \quad x_2 = \frac{-7 + 5}{2(-2)} = \frac{-2}{-4} = \frac{1}{2}.$$
> 2. Apply the rule for the sign of a quadratic trinomial:
>    Here, $a = -2 < 0$.
>    The trinomial has the sign of $a$ (negative) outside the roots, and the opposite sign (positive) between the roots.
> 3. Sign chart:
>
> | $x$ | $-\infty$ | | $\frac{1}{2}$ | | $3$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $-2x^2+7x-3$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
>
> We want the expression to be $\ge 0$.
> The solution set is therefore the closed interval: $\boxed{S = \left[\frac{1}{2}, 3\right]}$.

> **Worked Example 4 — Using Obvious Roots and Viète.**
> Solve the equation $15x^2 - 2x - 17 = 0$ mentally.
>
> **Solution:**
> Test the sum of the coefficients:
> $a = 15, b = -2, c = -17$.
> Compute $a - b + c = 15 - (-2) + (-17) = 15 + 2 - 17 = 0$.
> According to Section 6.2, $x_1 = -1$ is an obvious root!
> The product of the roots is $P = x_1 x_2 = \frac{c}{a} = -\frac{17}{15}$.
> Since $x_1 = -1$, we have $(-1) \times x_2 = -\frac{17}{15} \implies x_2 = \frac{17}{15}$.
> The solutions are immediately $\boxed{S = \left\{-1, \frac{17}{15}\right\}}$, without computing any discriminant!

> **Worked Example 5 — Finding Dimensions from Perimeter and Area.**
> A rectangular plot of land has a semi-perimeter of $29\text{ meters}$ and an area of $198\text{ m}^2$.
> What are the dimensions of this plot?
>
> **Solution:**
> Let $L$ and $\ell$ be the length and width.
> We know their sum $S = L + \ell = 29$ and their product $P = L \times \ell = 198$.
> By Viète's theorem, $L$ and $\ell$ are the solutions of the equation:
> $$X^2 - 29X + 198 = 0.$$
> Compute the discriminant:
> $$\Delta = (-29)^2 - 4(1)(198) = 841 - 792 = 49 > 0.$$
> $\sqrt{\Delta} = 7$.
> The solutions are:
> $$X_1 = \frac{29 - 7}{2} = \frac{22}{2} = 11, \quad X_2 = \frac{29 + 7}{2} = \frac{36}{2} = 18.$$
> The dimensions of the plot are therefore **$18\text{ meters}$ by $11\text{ meters}$**.
> *(Check: semi-perimeter $18 + 11 = 29\text{ m}$; area $18 \times 11 = 198\text{ m}^2$).*

> **Worked Example 6 — Biquadratic Equation Reducible to a Quadratic.**
> Solve the following equation in $\mathbb{R}$:
> $$x^4 - 5x^2 - 36 = 0.$$
>
> **Solution:**
> This equation has degree 4, but it contains only even powers ($x^4 = (x^2)^2$).
> Let us make a **substitution**: set $X = x^2$ (with the essential constraint $X \ge 0$).
> The equation becomes a quadratic equation in $X$:
> $$X^2 - 5X - 36 = 0.$$
> Compute the discriminant:
> $$\Delta = (-5)^2 - 4(1)(-36) = 25 + 144 = 169 = 13^2.$$
> The roots in $X$ are:
> $$X_1 = \frac{5 - 13}{2} = \frac{-8}{2} = -4, \quad X_2 = \frac{5 + 13}{2} = \frac{18}{2} = 9.$$
> Now return to the original variable $x$:
> - For $X_1 = -4$: the equation $x^2 = -4$ has no real solution because a real square cannot be negative.
> - For $X_2 = 9$: the equation $x^2 = 9$ immediately gives $x = -3$ or $x = 3$.
> The set of real solutions to the original equation is $\boxed{S = \{-3, 3\}}$.

---

### 8. In Computer Science: The Quadratic Solver in Python

Here is a Python script that implements the full analysis algorithm for a quadratic trinomial:

```python
import math

def analyze_trinomial(a, b, c):
    """Complete analysis of the trinomial a*x^2 + b*x + c."""
    if a == 0:
        return "Error: This is not a quadratic trinomial (a = 0)."
    
    # 1. Vertex of the parabola
    alpha = -b / (2 * a)
    beta = a * alpha**2 + b * alpha + c
    print(f"Vertex S: ({alpha:.3f}, {beta:.3f})")
    print(f"Orientation: opens {'UPWARD' if a > 0 else 'DOWNWARD'}")
    
    # 2. Discriminant
    delta = b**2 - 4 * a * c
    print(f"Discriminant Delta = {delta}")
    
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Two distinct real roots: x1 = {x1:.3f} and x2 = {x2:.3f}")
        print(f"Factored form: {a} * (x - {x1:.3f}) * (x - {x2:.3f})")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"One double root: x0 = {x0:.3f}")
        print(f"Factored form: {a} * (x - {x0:.3f})^2")
    else:
        print("No real roots.")
        print("No factorization in R.")

# Example call: 2x^2 - 7x + 3
analyze_trinomial(2, -7, 3)
```

---

### Key Takeaways

1. **Standard Form:** $f(x) = ax^2 + bx + c$ ($a \neq 0$).
2. **Canonical (Vertex) Form:** $f(x) = a(x - \alpha)^2 + \beta$ where:
   $$\alpha = -\frac{b}{2a} \quad \text{and} \quad \beta = f(\alpha) = -\frac{\Delta}{4a}.$$
   - Vertex of the parabola: $S(\alpha, \beta)$.
   - Axis of symmetry: line $x = \alpha$.
   - Opens upward if $a > 0$ (minimum $\beta$), opens downward if $a < 0$ (maximum $\beta$).
3. **Discriminant $\Delta = b^2 - 4ac$:**
   - $\Delta > 0$: 2 distinct real roots $x_1 = \frac{-b-\sqrt{\Delta}}{2a}$ and $x_2 = \frac{-b+\sqrt{\Delta}}{2a}$.
   - $\Delta = 0$: 1 double real root $x_0 = -\frac{b}{2a}$.
   - $\Delta < 0$: 0 real roots.
4. **Factored Form:**
   - If $\Delta > 0$: $a(x - x_1)(x - x_2)$.
   - If $\Delta = 0$: $a(x - x_0)^2$.
5. **Sign of the Trinomial:**
   - Always of the same sign as $a$, **except between the roots** (if $\Delta > 0$) where it takes the sign of $-a$.
6. **Viète's Formulas:**
   $$S = x_1 + x_2 = -\frac{b}{a}, \quad P = x_1 x_2 = \frac{c}{a}, \quad X^2 - SX + P = 0.$$

---

### Exercises

#### Direct Application Exercises (★)

1. Compute the discriminant $\Delta$ of the trinomial $f(x) = x^2 - 6x + 8$.
2. Compute the discriminant $\Delta$ of the trinomial $g(x) = 2x^2 + 4x + 5$.
3. Determine the coordinates of the vertex $S$ of the parabola with equation $y = 3(x - 4)^2 + 7$.
4. Determine the coordinates of the vertex $S$ of the parabola with equation $y = -2x^2 + 8x - 3$.
5. Solve the equation $x^2 - 9x + 20 = 0$ in $\mathbb{R}$.
6. Solve the equation $x^2 + 2x + 1 = 0$ in $\mathbb{R}$.
7. Solve the equation $3x^2 + x + 2 = 0$ in $\mathbb{R}$.
8. Give the factored form of $2x^2 - 10x + 12$.
9. Construct the sign chart for the trinomial $P(x) = x^2 - 4x - 5$.
10. Find the roots of $2x^2 + 3x - 5 = 0$ mentally using obvious roots.

#### Practice and Reasoning Exercises (★★)

11. Put the following trinomials into canonical form:
    a) $f(x) = x^2 - 10x + 21$ \quad b) $g(x) = -3x^2 + 12x - 7$
12. Solve the following inequalities in $\mathbb{R}$:
    a) $x^2 - 5x + 6 \le 0$ \quad b) $-x^2 + 2x + 8 > 0$ \quad c) $2x^2 - 3x + 5 > 0$
13. Find two real numbers knowing their sum $S = 13$ and their product $P = 40$.
14. For what values of the real parameter $m$ does the equation $x^2 + (m + 1)x + 4 = 0$ have a double root?
15. Solve the rational equation: $\frac{2x - 1}{x + 1} = \frac{x + 2}{x - 1}$.
16. Solve the biquadratic equation in $\mathbb{R}$: $x^4 - 13x^2 + 36 = 0$.
17. A tennis ball is hit from a height of $1\text{ meter}$. Its trajectory is modeled by $h(x) = -0.05x^2 + 0.8x + 1$, where $x$ is the horizontal distance traveled in meters and $h(x)$ is the height in meters.
    a) What is the maximum height reached by the ball?
    b) At what horizontal distance does the ball hit the ground ($h(x) = 0$)?
18. Determine the coordinates of the intersection points between the parabola $y = x^2 - 3x + 2$ and the line $y = 2x - 4$.

#### Deepening Exercises and Challenges (★★★)

19. **The Reduced Discriminant Formula $\Delta'$.**
    When the linear coefficient $b$ is even, we can write $b = 2b'$.
    a) Prove that $\Delta = 4(b'^2 - ac)$.
    b) Setting $\Delta' = b'^2 - ac$, prove that the roots simplify to $x = \frac{-b' \pm \sqrt{\Delta'}}{a}$.
    c) Use this simplified formula to solve $x^2 - 14x + 45 = 0$ and $5x^2 - 6x - 8 = 0$.
20. **Relative Position of Two Parabolas.**
    Consider the parabolas $\mathcal{P}_1 : y = x^2 - 4x + 3$ and $\mathcal{P}_2 : y = -x^2 + 2x + 11$.
    a) Determine the $x$-coordinates of the intersection points of these two curves.
    b) Study the sign of the difference and deduce on which interval $\mathcal{P}_1$ lies below $\mathcal{P}_2$.
21. **Lifeguard Optimization Problem.**
    A lifeguard marks off a rectangular swimming area along a straight beach using a rope of buoys $160\text{ meters}$ long (the beach side needs no buoys).
    What dimensions should the swimming area have so that the water surface enclosed is as large as possible?
22. **Tartaglia's Open Box.**
    From a square sheet of cardboard measuring $30\text{ cm}$ on each side, four identical small squares of side length $x$ are cut out from the four corners. The sides are then folded up to form an open rectangular box.
    a) What are the possible values for $x$?
    b) Express the volume $V(x)$ of the box as a function of $x$.
    c) Expand the expression and determine for which integer value of $x$ the volume appears to be maximized by testing $x = 1, 2, 3, 4, 5, 6$.

---

### Solutions

1. $\Delta = (-6)^2 - 4(1)(8) = 36 - 32 = 4$.
2. $\Delta = 4^2 - 4(2)(5) = 16 - 40 = -24$.
3. The equation is already in canonical form: the vertex is directly $S(4, 7)$.
4. $\alpha = -\frac{b}{2a} = -\frac{8}{2(-2)} = 2$. $\beta = -2(2)^2 + 8(2) - 3 = -8 + 16 - 3 = 5$. Thus $S(2, 5)$.
5. $\Delta = (-9)^2 - 4(1)(20) = 81 - 80 = 1$. $x_1 = \frac{9 - 1}{2} = 4, x_2 = \frac{9 + 1}{2} = 5$. $S = \{4, 5\}$.
6. Perfect square: $(x + 1)^2 = 0 \implies x_0 = -1$. $S = \{-1\}$.
7. $\Delta = 1^2 - 4(3)(2) = 1 - 24 = -23 < 0$. No real solution: $S = \varnothing$.
8. Roots of $2x^2 - 10x + 12 = 0$: $\Delta = 100 - 96 = 4$. $x_1 = 2, x_2 = 3$. Factored form: $2(x - 2)(x - 3)$.
9. Roots of $x^2 - 4x - 5$: $a - b + c = 1 - (-4) - 5 = 0 \implies x_1 = -1$ and $x_2 = 5$.
   Since $a = 1 > 0$, the trinomial is negative between $-1$ and $5$, and positive outside:
   positive on $]-\infty, -1[ \cup ]5, +\infty[$, zero at $-1$ and $5$, negative on $]-1, 5[$.
10. $a + b + c = 2 + 3 - 5 = 0 \implies x_1 = 1$.
    Product $P = \frac{c}{a} = -\frac{5}{2}$, hence $x_2 = -\frac{5}{2} = -2.5$. $S = \left\{-\frac{5}{2}, 1\right\}$.
11. a) $x^2 - 10x + 21 = (x - 5)^2 - 25 + 21 = (x - 5)^2 - 4$.
    b) $-3x^2 + 12x - 7 = -3(x^2 - 4x) - 7 = -3[(x - 2)^2 - 4] - 7 = -3(x - 2)^2 + 12 - 7 = -3(x - 2)^2 + 5$.
12. a) Roots: $2$ and $3$. $a = 1 > 0$. Negative between the roots: $S = [2, 3]$.
    b) $-x^2 + 2x + 8 = 0 \implies \Delta = 4 - 4(-1)(8) = 36$. Roots: $x_1 = \frac{-2 - 6}{-2} = 4, x_2 = \frac{-2 + 6}{-2} = -2$.
       $a = -1 < 0$, so positive between the roots: $S = ]-2, 4[$.
    c) $\Delta = 9 - 4(2)(5) = -31 < 0$. Since $a = 2 > 0$, the trinomial is strictly positive for all $x \in \mathbb{R}$: $S = \mathbb{R}$.
13. Equation $X^2 - 13X + 40 = 0$. $\Delta = 169 - 160 = 9$.
    $X_1 = \frac{13 - 3}{2} = 5, X_2 = \frac{13 + 3}{2} = 8$. The numbers are $5$ and $8$.
14. Double root $\iff \Delta = 0$.
    $\Delta = (m + 1)^2 - 4(1)(4) = (m + 1)^2 - 16 = 0 \iff (m + 1)^2 = 16 \iff m + 1 = 4$ or $m + 1 = -4$.
    Thus $m = 3$ or $m = -5$.
15. Excluded values: $x \neq -1$ and $x \neq 1$.
    Cross-multiplication: $(2x - 1)(x - 1) = (x + 2)(x + 1)$.
    $2x^2 - 3x + 1 = x^2 + 3x + 2 \iff x^2 - 6x - 1 = 0$.
    $\Delta = 36 - 4(1)(-1) = 40$. $x = \frac{6 \pm 2\sqrt{10}}{2} = 3 \pm \sqrt{10}$.
    Since both values differ from $1$ and $-1$, $S = \{3 - \sqrt{10}, 3 + \sqrt{10}\}$.
16. Set $X = x^2 \ge 0$. $X^2 - 13X + 36 = 0$.
    $\Delta = 169 - 144 = 25$. $X_1 = \frac{13 - 5}{2} = 4, X_2 = \frac{13 + 5}{2} = 9$.
    $x^2 = 4 \implies x = \pm 2$; $x^2 = 9 \implies x = \pm 3$. $S = \{-3, -2, 2, 3\}$.
17. a) Vertex: $\alpha = -\frac{0.8}{2(-0.05)} = \frac{0.8}{0.1} = 8\text{ meters}$.
       Maximum height: $\beta = h(8) = -0.05(64) + 0.8(8) + 1 = -3.2 + 6.4 + 1 = 4.2\text{ meters}$.
    b) $h(x) = 0 \iff -0.05x^2 + 0.8x + 1 = 0$. Multiply by $-20$: $x^2 - 16x - 20 = 0$.
       $\Delta = 256 + 80 = 336$. $\sqrt{336} \approx 18.33$.
       $x = \frac{16 + 18.33}{2} \approx 17.17\text{ meters}$ (the other root is negative). The ball hits the ground at approximately $17.17\text{ m}$.
18. $x^2 - 3x + 2 = 2x - 4 \iff x^2 - 5x + 6 = 0 \iff (x - 2)(x - 3) = 0$.
    $x$-coordinates: $x = 2$ and $x = 3$.
    $y$-coordinates: for $x = 2$, $y = 2(2) - 4 = 0$; for $x = 3$, $y = 2(3) - 4 = 2$.
    Points of intersection: $A(2, 0)$ and $B(3, 2)$.
19. a) $\Delta = (2b')^2 - 4ac = 4b'^2 - 4ac = 4(b'^2 - ac)$.
    b) $\sqrt{\Delta} = 2\sqrt{b'^2 - ac} = 2\sqrt{\Delta'}$.
       $x = \frac{-2b' \pm 2\sqrt{\Delta'}}{2a} = \frac{-b' \pm \sqrt{\Delta'}}{a}$.
    c) For $x^2 - 14x + 45 = 0$: $b' = -7$, $\Delta' = 49 - 45 = 4$. $x = 7 \pm 2 \implies S = \{5, 9\}$.
       For $5x^2 - 6x - 8 = 0$: $b' = -3$, $\Delta' = 9 - 5(-8) = 49$. $x = \frac{3 \pm 7}{5} \implies S = \{-0.8, 2\}$.
20. a) $x^2 - 4x + 3 = -x^2 + 2x + 11 \iff 2x^2 - 6x - 8 = 0 \iff x^2 - 3x - 4 = 0$.
       Obvious roots ($a - b + c = 1 - (-3) - 4 = 0$): $x_1 = -1$ and $x_2 = 4$.
    b) $\mathcal{P}_1$ lies below $\mathcal{P}_2 \iff \mathcal{P}_1 - \mathcal{P}_2 \le 0 \iff 2(x + 1)(x - 4) \le 0$.
       Since the coefficient $2 > 0$, the expression is negative between the roots: on $[-1, 4]$.
21. Let $x$ be the width of the two sides perpendicular to the beach. The length along the water is $160 - 2x$.
    Area: $A(x) = x(160 - 2x) = -2x^2 + 160x$.
    This is a quadratic trinomial with $a = -2 < 0$. Its maximum is attained at the vertex:
    $x = -\frac{160}{2(-2)} = 40\text{ meters}$.
    The length is then $160 - 2(40) = 80\text{ meters}$.
    Optimal dimensions: $40\text{ m} \times 80\text{ m}$ (maximum area: $3200\text{ m}^2$).
22. a) $x > 0$ and $2x < 30 \iff x < 15$. Hence $x \in ]0, 15[$.
    b) The base is a square of side length $30 - 2x$ and the height is $x$.
       $V(x) = x(30 - 2x)^2 = x(900 - 120x + 4x^2) = 4x^3 - 120x^2 + 900x$.
    c) Compute for several test values:
       $V(1) = 1(28)^2 = 784\text{ cm}^3$;
       $V(3) = 3(24)^2 = 1728\text{ cm}^3$;
       $V(5) = 5(20)^2 = 2000\text{ cm}^3$;
       $V(6) = 6(18)^2 = 1944\text{ cm}^3$.
       The volume appears to reach its maximum for $x = 5\text{ cm}$, attaining $2000\text{ cm}^3$ (which is exactly 2 liters!).

---

### The Question Opening the Next Stage

The quadratic degree has taught us to predict the continuous arch of a water jet soaring through space. But in the physical world, not all phenomena flow like a continuous stream:
- A bank account yields interest at the end of each discrete month;
- A bacterial colony doubles with every passing hour;
- A staircase is climbed step by step, $0, 1, 2, 3\dots$

How can we study a quantity that progresses in discrete jumps through time? How can we calculate the sum of a thousand steps without exhaustion? This is what we will discover in **The Staircase Steps and the Usurer's Loan**.
