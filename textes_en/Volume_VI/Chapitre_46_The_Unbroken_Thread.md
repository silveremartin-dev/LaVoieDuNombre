# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 46: The Unbroken Thread

> *“Natura non facit saltus — Nature does not make jumps, said Gottfried Wilhelm Leibniz. If a train leaves Paris at noon and enters the station in Lyon at two o'clock, it did not vanish at Dijon only to reappear suddenly fifty kilometers down the line. It pressed against every meter, every millimeter of track without ever lifting its wheels. In mathematics, this fidelity to the path is called continuity, and it possesses the magical power to guarantee that an equation has a solution even when one is incapable of calculating it by hand.”*

---

### What You Will Discover

- The driving intuition of **continuity**: a graph drawn in a single stroke of the pen without ever lifting the nib from the paper, and its formal formulation $\lim\limits_{x \to x_0} f(x) = f(x_0)$.
- Why virtually all functions in physics and natural science are continuous, and the crucial implication: **differentiable implies continuous** (though the converse is false!).
- The **Intermediate Value Theorem (IVT)**: the absolute certainty of crossing a river when traveling from one bank to the other.
- The **corollary of the bijection** (IVT for strictly monotonic functions): the #1 tool on the Baccalaureate exam to prove the existence and uniqueness of the solution to an equation $f(x) = k$.
- The **bisection method** (dichotomy) for numerical bracketing and its implementation in **Python**.
- Recurrence sequences $u_{n+1} = f(u_n)$: how the continuity of $f$ forces the sequence limit to be a **fixed point** ($f(L) = L$).

---

### 1. The Problem: Crossing the River Without Teleporting

#### 1.1 The Hiker and the Invisible Bridge

Imagine a hiker departing from a valley at an elevation of $500\text{ meters}$ at 8:00 AM. At noon, she reaches the summit of the mountain at $2200\text{ meters}$.
Can you state with certainty that at some precise moment during the morning, her altimeter read exactly $1500\text{ meters}$?

```
 Altitude (m) ▲
        2200 ┼                                    * (Summit at 12:00)
             │                                .-'
        1500 ┼ - - - - - - - - - - - - - - - * - - - - - (Elevation crossed!)
             │                          _.-'
         500 ┼ * (Start at 8:00)     .-'
             └─┼─────────────────────────────┼─────► Time (h)
               8h                            12h
```

The answer is undeniably **yes**. Unless the hiker possessed a science-fiction teleportation device, her body moved continuously through space. She could not pass below the $1500\text{ m}$ mark and then above it without **intersecting** the horizontal plane at $1500\text{ m}$.

Now consider another phenomenon: parking garage fees.
- From 0 to 1 hour: €$2.00$.
- From 1 hour to 2 hours: €$4.00$.
If you parked for $1\text{ hour and } 1\text{ second}$, the machine directly charges you €$4.00$. The price took an **abrupt jump**. It never took the value €$2.87$ or €$3.50$. The pricing function is **discontinuous**.

```
 Fee (€) ▲
       4 ┼               [───────────)
         │               ▲ Jump
       2 ┼ [───────────) │
         └─┼─────────────┼───────────► Time (h)
           0             1           2
```

The fundamental question of mathematical analysis is this: *what mathematical guarantees do we possess when a curve has no breaks?*

---

### 2. Continuity: From the Stroke of a Pencil to the Formal Definition

#### 2.1 Definition at a Point

Intuitively, a function is continuous if one can trace its graph without lifting the pencil.
Yet how can a computer or an algebraic equation “know” whether a pencil was lifted? Mathematicians express this kinematic intuition through an equality of limits:

> **📐 Definition — Continuity at a point.**
> Let $f$ be a function defined on an open interval containing $x_0$.
> We say that **$f$ is continuous at $x_0$** if:
> $$\lim_{x \to x_0} f(x) = f(x_0).$$

**Deconstruction of the condition:**
For this equality to hold, three conditions must be satisfied simultaneously:
1. $f(x_0)$ exists (the function is well-defined at $x_0$);
2. $f(x)$ admits a finite limit as $x \to x_0$;
3. This limit rigorously coincides with the actual value $f(x_0)$.

If $\lim\limits_{x \to x_0^-} f(x) \neq \lim\limits_{x \to x_0^+} f(x)$, or if the limit does not equal $f(x_0)$, the curve exhibits a disruption (a hole or a jump): $f$ is said to be **discontinuous** at $x_0$.

#### 2.2 Continuity on an Interval

> **📐 Definition — Continuity on an interval.**
> A function $f$ is said to be **continuous on an interval $I$** if it is continuous at every point $x_0 \in I$.

#### 2.3 Continuity of Standard Functions

All standard reference functions studied in high school are continuous on every interval where they are defined:
- **Polynomial functions** (lines, parabolas...) are continuous on $\mathbb{R}$.
- **Rational functions** (quotients of polynomials) are continuous on each interval of their domain.
- The **square root function** $x \mapsto \sqrt{x}$ is continuous on $[0 \,;\, +\infty[$.
- The **absolute value function** $x \mapsto |x|$ is continuous on $\mathbb{R}$.
- The **exponential function** $x \mapsto e^x$ is continuous on $\mathbb{R}$.
- Trigonometric functions $\cos$ and $\sin$ are continuous on $\mathbb{R}$.

Furthermore, sums, products, quotients (provided the denominator is non-zero), and **composites** of continuous functions are continuous functions.

#### 2.4 The Vital Link: Differentiability and Continuity

> **📐 Fundamental Theorem — Differentiable implies continuous.**
> If a function $f$ is differentiable at a point $x_0$, then it is **necessarily continuous** at $x_0$.
> If $f$ is differentiable on an interval $I$, then it is continuous on $I$.

> **✍️ Proof (Required knowledge).**
> Assume $f$ is differentiable at $x_0$. This means the difference quotient has a finite limit denoted $f'(x_0)$:
> $$\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = f'(x_0).$$
> For all $x \neq x_0$, write:
> $$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \times (x - x_0).$$
> Take the limit as $x \to x_0$ applying the product rule for limits:
> $$\lim_{x \to x_0} [f(x) - f(x_0)] = \lim_{x \to x_0} \left(\frac{f(x) - f(x_0)}{x - x_0}\right) \times \lim_{x \to x_0} (x - x_0) = f'(x_0) \times 0 = 0.$$
> We immediately deduce:
> $$\lim_{x \to x_0} f(x) = f(x_0).$$
> The function $f$ is therefore continuous at $x_0$. $\blacksquare$

> **⚠️ Caution, trap! — The converse is FALSE!**
> A function can be perfectly continuous at a point without being differentiable there.
> **Classic Counterexample #1: The absolute value function $f(x) = |x|$ at 0.**
> Its graph forms a sharp corner (a V). It is drawn without lifting the pencil and is continuous at 0 because $\lim_{x \to 0} |x| = 0 = |0|$.
> However, its difference quotient at 0 is:
> - $\frac{|x| - 0}{x - 0} = \frac{x}{x} = 1$ for $x > 0$;
> - $\frac{|x| - 0}{x - 0} = \frac{-x}{x} = -1$ for $x < 0$.
> The right-hand limit ($1$) and left-hand limit ($-1$) differ: $f$ is **not differentiable at 0**.
> **Counterexample #2:** $f(x) = \sqrt{x}$ at 0 is continuous at 0 but not differentiable (vertical tangent).

---

### 3. The Intermediate Value Theorem (IVT)

#### 3.1 The General Statement

The Czech mathematician Bernard Bolzano (1817) and the French mathematician Augustin-Louis Cauchy (1821) provided the first rigorous proofs of this clear geometric principle:

> **📐 Intermediate Value Theorem (IVT).**
> Let $f$ be a function that is **continuous** on a closed interval $[a \,;\, b]$.
> For every real number $k$ between $f(a)$ and $f(b)$, there exists **at least one real number $c$** belonging to the interval $[a \,;\, b]$ such that:
> $$f(c) = k.$$

```
 y ▲
   │
f(b)┼─────────────────────────────────* (b, f(b))
   │                                 /
 k ┼ - - - - - - - - * - - - - - - -* - - - - - - -
   │                / \            /
f(a)┼──────* (a, f(a))   \        /
   │       │               \    /
   └───────┼─────────┼──────┼──┼──────┼────────► x
           a        c_1     c_2       b
```

*Crucial remarks:*
- The theorem asserts the **existence** of at least one solution, but it does not specify the exact count: on the diagram above, there are two solutions $c_1$ and $c_2$.
- If $f$ were not continuous, the curve could jump over the horizontal line $y = k$ without ever touching it!

#### 3.2 The Special Case of Zero: Bolzano's Theorem

This is the most common form in practical applications:

> **📐 Corollary — Sign change.**
> Let $f$ be a continuous function on $[a \,;\, b]$.
> If $f(a)$ and $f(b)$ have **opposite signs** (that is, $f(a) \times f(b) \leq 0$),
> then there exists at least one real number $c \in [a \,;\, b]$ such that $f(c) = 0$.

*In plain words:* To pass from a negative altitude (underwater) to a positive altitude (in the air), a continuous path must inevitably pierce the water's surface ($y = 0$).

---

### 4. The Bijection Theorem (IVT for Strictly Monotonic Functions)

On exams, one rarely seeks merely “at least one solution”: one seeks to prove that there is **exactly one** solution. To secure uniqueness, one must prevent the curve from reversing direction. We thus require the function to be **strictly monotonic** (always strictly increasing or always strictly decreasing).

> **📐 Theorem — Corollary of the IVT (Bijection Theorem).**
> Let $f$ be a function defined on an interval $I = [a \,;\, b]$. If:
> 1. $f$ is **continuous** on $[a \,;\, b]$;
> 2. $f$ is **strictly monotonic** (strictly increasing or strictly decreasing) on $[a \,;\, b]$;
>
> Then, for every real number $k$ between $f(a)$ and $f(b)$, the equation:
> $$f(x) = k$$
> admits **a unique solution** $\alpha$ in the interval $[a \,;\, b]$.

#### Extension to Open or Infinite Intervals

The theorem remains fully valid on an open interval $]a \,;\, b[$ or an infinite interval like $]-\infty \,;\, +\infty[$, $[0 \,;\, +\infty[$, etc.
One simply replaces the boundary values $f(a)$ and $f(b)$ with the **limits** of the function at the endpoints of the interval:
If $f$ is continuous and strictly increasing on $]a \,;\, b[$, then for every $k \in \left]\lim_{x \to a^+} f(x) \,;\, \lim_{x \to b^-} f(x)\right[$, the equation $f(x) = k$ admits a unique solution in $]a \,;\, b[$.

> **🧭 Method — Canonical Baccalaureate solution layout:**
> To justify that the equation $f(x) = k$ admits a unique solution $\alpha$ on an interval $I$:
> 1. **Continuity:** State that $f$ is continuous on $I$ (e.g., as a sum, product, or quotient of standard functions, or because it is differentiable there).
> 2. **Strict monotonicity:** Indicate that $f$ is strictly increasing (or decreasing) on $I$, justified by the sign of its derivative $f'(x)$.
> 3. **Membership in target range:** Compute the endpoint values (or their limits) and verify that $k$ belongs to the image interval: $k \in [f(a) \,;\, f(b)]$ (or $] \lim_a f \,;\, \lim_b f [$).
> 4. **Conclusion:** Conclude: *“According to the corollary of the intermediate value theorem (bijection theorem), the equation $f(x) = k$ admits a unique solution $\alpha$ in $I$.”*

---

### 5. Numerical Approximation: The Bisection Algorithm in Python

The IVT proves that a solution $\alpha$ exists and is unique, but does not provide its exact numerical closed form (which is often impossible to express using basic fractions or radicals).
To locate an approximate value of $\alpha$ with surgical precision (e.g., $10^{-6}$), one uses the **bisection method** (or dichotomy, from Greek *dicha*, “in two”, and *tomein*, “to cut”).

#### 5.1 Principle of Successive Halving

Suppose the root $\alpha$ is trapped in an interval $[a \,;\, b]$ with $f(a) \times f(b) < 0$.
1. Compute the midpoint of the interval: $m = \frac{a + b}{2}$.
2. Examine the sign of $f(m)$:
   - If $f(a)$ and $f(m)$ have opposite signs ($f(a) \times f(m) < 0$), then the root lies in the left half: replace $b$ with $m$.
   - Otherwise, the root lies in the right half: replace $a$ with $m$.
3. At each step, the interval width is **halved**.
After $n$ steps, the uncertainty on the root is reduced to $\frac{b - a}{2^n}$.

```
 Step 0:  [───────────────── α ───────────────]   Width L
                               m
 Step 1:  [──────── α ───────]                    Width L/2
                        m
 Step 2:            [── α ──]                    Width L/4
```

#### 5.2 Python Implementation

Consider the equation $x^3 + x - 1 = 0$ on $[0 \,;\, 1]$.
The function $f(x) = x^3 + x - 1$ is continuous, strictly increasing, with $f(0) = -1 < 0$ and $f(1) = 1 > 0$. There exists a unique solution $\alpha \in [0 \,;\, 1]$.

```python
def f(x):
    """Function whose zero is sought."""
    return x**3 + x - 1

def bisection(a, b, precision):
    """
    Returns an interval [a, b] bracketing the root of f(x) = 0
    with a width b - a <= precision.
    """
    while (b - a) > precision:
        m = (a + b) / 2
        # If f(a) and f(m) have opposite signs, root is in [a, m]
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return a, b

# Search for a bracketing to within 10^-4
lower, upper = bisection(0.0, 1.0, 1e-4)
print(f"Bracketing obtained: {lower:.5f} < alpha < {upper:.5f}")
# Output: 0.68231 < alpha < 0.68237
```

*Remarkable speed:* To achieve a precision of $10^{-6}$ (one millionth) starting from an initial interval of length 1:
Since $2^{20} = 1,048,576 > 10^6$, **just 20 iterations** suffice to deliver six accurate decimal places!

---

### 6. Recurrence Sequences $u_{n+1} = f(u_n)$ and Fixed Point Finding

In Chapter 44, we studied bounded monotonic sequences that converged to a limit $L$. But how can we calculate this limit $L$ when the sequence is generated by a recurrence relation $u_{n+1} = f(u_n)$?

Here is where continuity demonstrates its full power!

> **📐 Fixed-Point Theorem.**
> Let $(u_n)$ be a sequence defined by $u_0$ and the recurrence relation $u_{n+1} = f(u_n)$ for all $n \in \mathbb{N}$.
> If:
> 1. The sequence $(u_n)$ **converges** to a real number $L$;
> 2. The function $f$ is **continuous** at $L$;
>
> Then the limit $L$ is a solution to the equation:
> $$f(L) = L.$$
> Such a number $L$ is called a **fixed point** of the function $f$.

> **✍️ Proof.**
> Since $\lim\limits_{n \to +\infty} u_n = L$, the shifted sequence $(u_{n+1})$ clearly converges to the same limit: $\lim\limits_{n \to +\infty} u_{n+1} = L$.
> On the other hand, since $f$ is continuous at $L$, by composite limits:
> $$\lim_{n \to +\infty} f(u_n) = f\left(\lim_{n \to +\infty} u_n\right) = f(L).$$
> Now, for every integer $n$, $u_{n+1} = f(u_n)$.
> Taking the limit on both sides of the equality, we necessarily obtain:
> $$L = f(L). \quad \blacksquare$$

*Geometric interpretation (the cobweb / staircase diagram):*
The limit $L$ is the $x$-coordinate of an intersection point between the function curve $y = f(x)$ and the main diagonal line **$y = x$**.

```
       y ▲                     / y = x
         │                   /
         │             *───*  y = f(x)
         │            /│   │
         │           *─┼───*
         │          /│ │   │
         └─────────┼─┼─┼───┼────────► x
                  u_0 u_1 u_2 L
```

---

### 7. Traps to Avoid!

> **⚠️ Caution, trap! — Forgetting strict monotonicity.**
> If you state only that “$f$ is continuous on $[a ; b]$ and $k$ lies between $f(a)$ and $f(b)$”, the IVT guarantees only the existence of **at least one** solution. To assert that there is **exactly one**, explicit mention of **strict monotonicity** is absolutely essential. Omitting it results in lost points on exams.

> **⚠️ Caution, trap! — Non-continuous functions.**
> Consider the function $f(x) = \frac{1}{x}$ on $[-1 \,;\, 1] \setminus \{0\}$.
> We have $f(-1) = -1 < 0$ and $f(1) = 1 > 0$.
> Yet the equation $f(x) = 0$ has **no solution**!
> Why does the IVT fail to apply? Because the function is **not continuous at 0** (it is not even defined there). The thread is severed in the middle.

---

### 8. Step-by-Step Worked Examples

#### Worked Example 1 — Standard Exam Application of the IVT Corollary

**Problem:** Consider the function $f$ defined on $\mathbb{R}$ by $f(x) = 2x^3 - 3x^2 - 12x + 5$.
1. Construct the complete variation table of $f$ on $[-3 \,;\, 4]$.
2. Prove that the equation $f(x) = 0$ admits exactly three real solutions in the interval $[-3 \,;\, 4]$.

**Solution:**
1. **Differentiation and variations:**
   The function $f$ is a polynomial, hence differentiable on $\mathbb{R}$.
   For all $x \in [-3 \,;\, 4]$:
   $$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2).$$
   Factoring $x^2 - x - 2$: discriminant is $\Delta = (-1)^2 - 4(1)(-2) = 1 + 8 = 9 = 3^2$.
   The roots are $x_1 = \frac{1 - 3}{2} = -1$ and $x_2 = \frac{1 + 3}{2} = 2$.
   Thus $f'(x) = 6(x + 1)(x - 2)$.
   Compute key values:
   - $f(-3) = 2(-27) - 3(9) - 12(-3) + 5 = -54 - 27 + 36 + 5 = -40$.
   - $f(-1) = 2(-1) - 3(1) - 12(-1) + 5 = -2 - 3 + 12 + 5 = 12$.
   - $f(2) = 2(8) - 3(4) - 12(2) + 5 = 16 - 12 - 24 + 5 = -15$.
   - $f(4) = 2(64) - 3(16) - 12(4) + 5 = 128 - 48 - 48 + 5 = 37$.

   Variation table:
   - On $[-3 \,;\, -1]$, $f'(x) > 0$, so $f$ is strictly increasing from $-40$ to $12$.
   - On $[-1 \,;\, 2]$, $f'(x) < 0$, so $f$ is strictly decreasing from $12$ to $-15$.
   - On $[2 \,;\, 4]$, $f'(x) > 0$, so $f$ is strictly increasing from $-15$ to $37$.

2. **Applying the IVT corollary to each subinterval:**
   - **On $[-3 \,;\, -1]$:** $f$ is continuous and strictly increasing. Since $0 \in [-40 \,;\, 12]$, by the IVT corollary, $f(x) = 0$ has a unique solution $\alpha_1 \in [-3 \,;\, -1]$.
   - **On $[-1 \,;\, 2]$:** $f$ is continuous and strictly decreasing. Since $0 \in [-15 \,;\, 12]$, $f(x) = 0$ has a unique solution $\alpha_2 \in [-1 \,;\, 2]$.
   - **On $[2 \,;\, 4]$:** $f$ is continuous and strictly increasing. Since $0 \in [-15 \,;\, 37]$, $f(x) = 0$ has a unique solution $\alpha_3 \in [2 \,;\, 4]$.

   *Conclusion:* The equation $f(x) = 0$ has exactly **three distinct solutions** in the interval $[-3 \,;\, 4]$.

---

#### Worked Example 2 — Equation with Exponential on an Unbounded Interval

**Problem:** Prove that the equation $e^x = \dfrac{2}{x}$ admits a unique real solution on $]0 \,;\, +\infty[$.

**Solution:**
For $x > 0$, the equation is equivalent to $e^x - \frac{2}{x} = 0$.
Consider the function $g$ defined on $]0 \,;\, +\infty[$ by:
$$g(x) = e^x - \frac{2}{x}.$$
1. **Continuity:** $g$ is the sum of the exponential function and the rational function $x \mapsto -2/x$, both of which are continuous on $]0 \,;\, +\infty[$. Hence $g$ is continuous on $]0 \,;\, +\infty[$.
2. **Variations:** $g$ is differentiable on $]0 \,;\, +\infty[$:
   $$g'(x) = e^x - \left(-\frac{2}{x^2}\right) = e^x + \frac{2}{x^2}.$$
   For all $x > 0$, $e^x > 0$ and $\frac{2}{x^2} > 0$, so $g'(x) > 0$.
   The function $g$ is therefore **strictly increasing** on $]0 \,;\, +\infty[$.
3. **Endpoint limits:**
   - At $0^+$: $\lim\limits_{x \to 0^+} e^x = 1$ and $\lim\limits_{x \to 0^+} \frac{2}{x} = +\infty$, so $\lim\limits_{x \to 0^+} g(x) = 1 - (+\infty) = -\infty$.
   - At $+\infty$: $\lim\limits_{x \to +\infty} e^x = +\infty$ and $\lim\limits_{x \to +\infty} \frac{2}{x} = 0$, so $\lim\limits_{x \to +\infty} g(x) = +\infty$.
4. **Conclusion:**
   The function $g$ is continuous and strictly increasing on $]0 \,;\, +\infty[$.
   It establishes a bijection from $]0 \,;\, +\infty[$ onto the image interval $]\lim_{0^+} g \,;\, \lim_{+\infty} g[ = ]-\infty \,;\, +\infty[ = \mathbb{R}$.
   Since $0 \in \mathbb{R}$, by the IVT corollary, the equation $g(x) = 0$ (that is, $e^x = \frac{2}{x}$) admits a unique real solution $\alpha$ on $]0 \,;\, +\infty[$.
   *(By calculator: $\alpha \approx 0.853$).*

---

#### Worked Example 3 — Recurrence Sequence and Fixed Point

**Problem:** Consider the sequence $(u_n)$ defined by $u_0 = 1$ and for all $n \in \mathbb{N}$ by:
$$u_{n+1} = \sqrt{1 + u_n}.$$
1. Prove by induction that for all $n \in \mathbb{N}$, $1 \leq u_n \leq u_{n+1} \leq 2$.
2. Deduce that the sequence $(u_n)$ converges.
3. Determine the exact value of its limit $L$ (the golden ratio $\varphi$).

**Solution:**
1. Define the function $f(x) = \sqrt{1 + x}$ on $[0 \,;\, 2]$. The function $f$ is strictly increasing on $[0 \,;\, 2]$ (composite of an increasing linear function and the square root function).
   Let $\mathcal{P}(n)$ be the property: “$1 \leq u_n \leq u_{n+1} \leq 2$”.
   - *Base step:* $u_0 = 1$, $u_1 = \sqrt{1+1} = \sqrt{2} \approx 1.414$.
     Clearly $1 \leq 1 \leq \sqrt{2} \leq 2$. $\mathcal{P}(0)$ is true.
   - *Inductive step:* Assume $1 \leq u_n \leq u_{n+1} \leq 2$.
     Apply the function $f$, which is strictly increasing:
     $$f(1) \leq f(u_n) \leq f(u_{n+1}) \leq f(2) \implies \sqrt{2} \leq u_{n+1} \leq u_{n+2} \leq \sqrt{3}.$$
     Since $1 \leq \sqrt{2}$ and $\sqrt{3} \leq 2$, we have $1 \leq u_{n+1} \leq u_{n+2} \leq 2$. $\mathcal{P}(n+1)$ is true.
   - *Conclusion:* For all $n \in \mathbb{N}$, $1 \leq u_n \leq u_{n+1} \leq 2$.

2. **Convergence:**
   The sequence $(u_n)$ is increasing and bounded above by 2. By the monotone convergence theorem, it converges to a real limit $L$ satisfying $1 \leq L \leq 2$.

3. **Limit calculation via the fixed-point theorem:**
   The function $f(x) = \sqrt{1 + x}$ is continuous on $[1 \,;\, 2]$.
   By the fixed-point theorem, the limit $L$ satisfies:
   $$L = f(L) \iff L = \sqrt{1 + L}.$$
   Since $L \geq 1 > 0$, squaring both sides yields the equivalent equation:
   $$L^2 = 1 + L \iff L^2 - L - 1 = 0.$$
   This is the characteristic equation of the **golden ratio**!
   $\Delta = (-1)^2 - 4(1)(-1) = 5$.
   The roots are $L_1 = \frac{1 - \sqrt{5}}{2} < 0$ and $L_2 = \frac{1 + \sqrt{5}}{2} \approx 1.618$.
   Since $L \geq 1$, we retain the unique positive root:
   $$L = \frac{1 + \sqrt{5}}{2} = \varphi.$$

---

#### Worked Example 4 — Continuity of a Piecewise Defined Function

**Problem:** Consider the function $f$ defined on $\mathbb{R}$ by:
$$f(x) = \begin{cases} x^2 + a & \text{if } x \leq 2 \\ 3x - 1 & \text{if } x > 2 \end{cases}$$
where $a$ is a real constant.
Determine the value of $a$ so that $f$ is continuous on $\mathbb{R}$.

**Solution:**
- For $x < 2$, $f(x) = x^2 + a$ is a polynomial, hence continuous on $]-\infty \,;\, 2[$.
- For $x > 2$, $f(x) = 3x - 1$ is a polynomial, hence continuous on $]2 \,;\, +\infty[$.
The only critical point is $x_0 = 2$.
Compute:
1. The value at 2: $f(2) = 2^2 + a = 4 + a$.
2. The left-hand limit: $\lim\limits_{x \to 2^-} f(x) = \lim\limits_{x \to 2^-} (x^2 + a) = 4 + a$.
3. The right-hand limit: $\lim\limits_{x \to 2^+} f(x) = \lim\limits_{x \to 2^+} (3x - 1) = 3(2) - 1 = 5$.

For $f$ to be continuous at 2, it is necessary and sufficient that the left-hand limit, the right-hand limit, and the function value all match:
$$4 + a = 5 \iff a = 1.$$
The function $f$ is continuous on $\mathbb{R}$ if and only if $a = 1$.

---

#### Worked Example 5 — Proving the Existence of Identical Temperatures

**Problem:** A thermometer records the temperature $T(x)$ along a straight $100\text{ km}$ road, where $x \in [0 \,;\, 100]$ denotes the distance from the starting point in kilometers. The function $T$ is assumed to be continuous. Suppose the initial temperature and the final temperature are identical: $T(0) = T(100)$.
Prove that there exist two points exactly $50\text{ km}$ apart that share the exact same temperature.

**Solution:**
Define the auxiliary function $D$ for all $x \in [0 \,;\, 50]$ by:
$$D(x) = T(x + 50) - T(x).$$
$D(x)$ represents the temperature difference between the point at kilometer $x + 50$ and the point at kilometer $x$.
1. **Continuity:** Since $T$ is continuous, $D$ is continuous on the interval $[0 \,;\, 50]$ as the difference of continuous functions.
2. **Values at the endpoints:**
   - At $x = 0$: $D(0) = T(50) - T(0)$.
   - At $x = 50$: $D(50) = T(100) - T(50)$.
   Now, by assumption, $T(100) = T(0)$.
   Substitute $T(100)$ with $T(0)$:
   $$D(50) = T(0) - T(50) = -\big(T(50) - T(0)\big) = -D(0).$$
3. **Sign discussion:**
   - If $D(0) = 0$, then $T(50) = T(0)$: the points $x = 0$ and $x = 50$ satisfy the condition.
   - If $D(0) \neq 0$, then $D(0)$ and $D(50) = -D(0)$ have **strictly opposite signs**:
     $$D(0) \times D(50) < 0.$$
     By the Intermediate Value Theorem applied to the continuous function $D$ on $[0 \,;\, 50]$, there exists at least one real number $c \in ]0 \,;\, 50[$ such that:
     $$D(c) = 0 \iff T(c + 50) - T(c) = 0 \iff T(c + 50) = T(c).$$
The two points with coordinates $c$ and $c + 50$ are separated by $50\text{ km}$ and have identical temperatures.

---

#### Worked Example 6 — Manual Bisection Steps

**Problem:** Consider the function $f(x) = x^3 + 2x - 5$ on $[1 \,;\, 2]$.
1. Justify that the equation $f(x) = 0$ has a unique solution $\alpha \in [1 \,;\, 2]$.
2. Perform three manual bisection steps to find a bracketing of $\alpha$ of width $0.125$.

**Solution:**
1. $f$ is a polynomial, hence continuous on $[1 ; 2]$. Its derivative is $f'(x) = 3x^2 + 2 > 0$ for all $x$, so $f$ is strictly increasing.
   $f(1) = 1 + 2 - 5 = -2 < 0$ and $f(2) = 8 + 4 - 5 = 7 > 0$.
   Since $0 \in [-2 \,;\, 7]$, by the IVT corollary, there exists a unique root $\alpha \in [1 \,;\, 2]$.

2. **Bisection:**
   - **Step 1:** Midpoint of $[1 \,;\, 2]$: $m_1 = 1.5$.
     $f(1.5) = (1.5)^3 + 2(1.5) - 5 = 3.375 + 3 - 5 = 1.375 > 0$.
     Since $f(1) < 0$ and $f(1.5) > 0$, the root is in:
     $$\alpha \in [1 \,;\, 1.5] \quad (\text{width } 0.5).$$
   - **Step 2:** Midpoint of $[1 \,;\, 1.5]$: $m_2 = 1.25$.
     $f(1.25) = (1.25)^3 + 2(1.25) - 5 = 1.953125 + 2.5 - 5 = -0.546875 < 0$.
     Since $f(1.25) < 0$ and $f(1.5) > 0$, the root is in:
     $$\alpha \in [1.25 \,;\, 1.5] \quad (\text{width } 0.25).$$
   - **Step 3:** Midpoint of $[1.25 \,;\, 1.5]$: $m_3 = 1.375$.
     $f(1.375) = (1.375)^3 + 2(1.375) - 5 \approx 2.5996 + 2.75 - 5 = 0.3496 > 0$.
     Since $f(1.25) < 0$ and $f(1.375) > 0$, the root is in:
     $$\alpha \in [1.25 \,;\, 1.375] \quad (\text{width } 0.125).$$
The bracketing after three steps is $1.25 \leq \alpha \leq 1.375$.

---

### Key Takeaways

1. **Continuity at a point:** $\lim\limits_{x \to x_0} f(x) = f(x_0)$.
2. **Differentiable implies continuous:** every function differentiable on an interval is continuous there. The converse is false (e.g., $|x|$ at 0).
3. **Intermediate Value Theorem (IVT):** If $f$ is continuous on $[a ; b]$, it takes every value between $f(a)$ and $f(b)$ at least once.
4. **Bijection Theorem (IVT Corollary):** If $f$ is **continuous** and **strictly monotonic** on an interval $I$, then the equation $f(x) = k$ admits **a unique solution** in $I$ for all $k \in f(I)$.
5. **Bisection method:** interval-halving algorithm to numerically bracket a solution with arbitrary precision in a finite number of steps.
6. **Fixed point:** If $u_{n+1} = f(u_n)$ with $f$ continuous and if $u_n \to L$, then $f(L) = L$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 46.1.** Among the following functions, determine which ones are continuous on their domain of definition:
1. $f(x) = 3x^4 - 2x + 7$ on $\mathbb{R}$
2. $g(x) = \dfrac{1}{x - 5}$ on $\mathbb{R} \setminus \{5\}$
3. $h(x) = \sqrt{x - 3}$ on $[3 \,;\, +\infty[$
4. $k(x) = \lfloor x \rfloor$ (floor function) on $\mathbb{R}$

**Exercise 46.2.** Consider the function $f$ defined on $[-2 \,;\, 5]$ by $f(x) = x^2 - 4x + 1$.
1. Compute $f(-2)$ and $f(5)$.
2. Justify that the equation $f(x) = 0$ has at least one solution on $[-2 \,;\, 5]$.

**Exercise 46.3.** You are given the variation table of a continuous function $g$ on $[-5 \,;\, 4]$:
- $g$ is strictly increasing from $-3$ to $7$ on $[-5 \,;\, -1]$.
- $g$ is strictly decreasing from $7$ to $1$ on $[-1 \,;\, 4]$.
Determine the number of solutions of the equation $g(x) = 4$ on $[-5 \,;\, 4]$.

**Exercise 46.4.** Justify the continuity of the function $f(x) = \dfrac{e^x}{x^2 + 1}$ on $\mathbb{R}$.

**Exercise 46.5.** Let $f(x) = x^3 + 3x - 1$.
1. Show that $f$ is strictly increasing on $\mathbb{R}$.
2. Compute $f(0)$ and $f(1)$.
3. Deduce that there exists a unique real number $\alpha \in [0 \,;\, 1]$ such that $f(\alpha) = 0$.

**Exercise 46.6.** Consider the recurrence sequence defined by $u_0 = 3$ and $u_{n+1} = \dfrac{1}{2}u_n + 1$. Assuming it converges to $L$, determine $L$ using the fixed-point theorem.

**Exercise 46.7.** Consider the piecewise defined function:
$$f(x) = \begin{cases} 2x + k & \text{if } x \leq 1 \\ x^2 + 3 & \text{if } x > 1 \end{cases}$$
For what value of the constant $k$ is $f$ continuous at $x = 1$?

**Exercise 46.8.** Write a Python function `f(x)` returning $x^2 - 2$, then use bisection to approximate $\sqrt{2}$ to within $10^{-3}$ on $[1 \,;\, 2]$.

---

#### Level ★★ (Guided Reflection and Baccalaureate Style)

**Exercise 46.9 (Baccalaureate Style: Complete Solution and Bracketing).**
Consider the function $f$ defined on $\mathbb{R}$ by:
$$f(x) = x^3 - 3x^2 + 1.$$
1. Study the limits of $f$ at $-\infty$ and at $+\infty$.
2. Construct the complete variation table of $f$.
3. Prove that the equation $f(x) = 0$ admits exactly three real solutions $\alpha_1, \alpha_2, \alpha_3$.
4. Give a bracketing of width $0.1$ of the largest solution.
5. Deduce the sign table of $f(x)$ on $\mathbb{R}$.

**Exercise 46.10 (Baccalaureate Style: Study of an Auxiliary Function for a Tangent).**
We wish to study the function $g(x) = (x - 1)e^x + 1$ on $\mathbb{R}$.
1. Determine the variations of $g$ on $\mathbb{R}$.
2. Show that $g(x) \geq 0$ for all $x \in \mathbb{R}$, and state for which value equality holds.
3. Deduce the relative position of the curve $y = e^x$ with respect to its tangent at 1.

**Exercise 46.11 (Transcendental Equation and Intersection Point).**
We seek to determine the intersection point between the exponential curve $y = e^{-x}$ and the line $y = x$.
1. Set up the appropriate function and prove that it admits a unique zero $\alpha$ on $\mathbb{R}$.
2. Prove that $\alpha \in [0 \,;\, 1]$.
3. Write a Python function that computes $\alpha$ to within $10^{-6}$.

**Exercise 46.12 (True or False with Rigorous Justifications).**
1. “If $f$ is continuous on $[a ; b]$ and if $f(a) < 0$ and $f(b) > 0$, then $f$ vanishes exactly once on $]a ; b[$.”
2. “If $f$ is strictly increasing on $[a ; b]$, then $f$ is continuous on $[a ; b]$.”
3. “If $f$ is continuous on $]0 ; 1[$, then its set of images is a bounded interval.”
4. “A continuous function that never vanishes on an interval $I$ maintains a constant sign on $I$.”

**Exercise 46.13 (Bisection: Calculation of Theoretical Iteration Count).**
The bisection algorithm is applied to an interval $[a \,;\, b]$ of initial length $L_0 = 4$.
1. Express the length $L_n$ of the interval after $n$ iterations.
2. How many steps at minimum are required to guarantee a precision less than or equal to $10^{-5}$?

**Exercise 46.14 (Recurrence Sequence and Homographic Function).**
Consider the sequence $(u_n)$ defined by $u_0 = 2$ and $u_{n+1} = \dfrac{4u_n - 2}{u_n + 1}$.
1. Verify that the associated function $f(x) = \dfrac{4x - 2}{x + 1}$ is continuous on $[1 \,;\, 3]$.
2. Determine the two fixed points of $f$.
3. Assuming $(u_n)$ converges to a real number $L \geq 1$, determine its exact limit.

**Exercise 46.15 (Fixed-Point Theorem for a Function Mapping an Interval into Itself).**
Let $f$ be a continuous function from $[0 \,;\, 1]$ into $[0 \,;\, 1]$ (that is, for all $x \in [0 ; 1]$, $0 \leq f(x) \leq 1$).
1. Set $g(x) = f(x) - x$. Determine the signs of $g(0)$ and $g(1)$.
2. Deduce that every continuous function from $[0 ; 1]$ into $[0 ; 1]$ admits at least one fixed point (Brouwer's fixed-point theorem in dimension 1).

**Exercise 46.16 (The Buddhist Monk Paradox).**
A monk climbs to a monastery at the top of a mountain along a single path. He starts at 6:00 AM on Saturday and arrives at 6:00 PM at the summit. On Sunday, he walks down along the same path starting at 6:00 AM and arrives at the bottom at 6:00 PM.
Prove that there is a spot on the path that the monk occupies at the exact same time of day on both Saturday and Sunday.

**Exercise 46.17 (Continuity and Injectivity).**
Prove that a continuous function on an interval $I$ is injective (distinct inputs have distinct outputs) if and only if it is strictly monotonic on $I$.

---

#### Level ★★★ (Challenge and In-Depth Study)

**Exercise 46.18 (The Dirichlet Function: Discontinuous Everywhere).**
Consider the indicator function of the rationals $f$ defined on $\mathbb{R}$ by:
$$f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q} \\ 0 & \text{if } x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}$$
1. Using the fact that in every non-empty open interval there exists at least one rational and one irrational number (density of $\mathbb{Q}$ and $\mathbb{R} \setminus \mathbb{Q}$ in $\mathbb{R}$), prove that for any real number $x_0$, $f$ has no limit at $x_0$.
2. Deduce that $f$ is discontinuous at every point of $\mathbb{R}$.

**Exercise 46.19 (Borsuk-Ulam Theorem in Dimension 1: Terrestrial Antipodes).**
The temperature on the Earth's equator is modeled by a continuous function $T(\theta)$, where $\theta \in [0 \,;\, 2\pi]$ is longitude in radians ($0$ and $2\pi$ representing the Greenwich meridian, so that $T(0) = T(2\pi)$).
Prove that there exists at least one pair of antipodal points on the equator with the exact same temperature:
$$\exists \theta_0 \in [0 \,;\, \pi], \quad T(\theta_0 + \pi) = T(\theta_0).$$

**Exercise 46.20 (Cauchy's Functional Equation).**
Let $f : \mathbb{R} \to \mathbb{R}$ be a **continuous** function satisfying for all real $x$ and $y$:
$$f(x + y) = f(x) + f(y).$$
1. Compute $f(0)$, then express $f(n)$ in terms of $n$ and $c = f(1)$ for all natural numbers $n$.
2. Prove that for every integer $p \in \mathbb{Z}$, $f(p) = c \cdot p$.
3. Prove that for every rational $r = \frac{p}{q} \in \mathbb{Q}$, $f(r) = c \cdot r$.
4. Using the continuity of $f$ and the density of $\mathbb{Q}$ in $\mathbb{R}$, conclude that for all $x \in \mathbb{R}$: $f(x) = c \cdot x$ (the only continuous solutions are linear functions).

**Exercise 46.21 (Universal Chord Theorem of Length $1/n$).**
Let $f$ be a continuous function on $[0 \,;\, 1]$ such that $f(0) = f(1)$. Let $n \geq 2$ be a natural number.
Define $g(x) = f\left(x + \frac{1}{n}\right) - f(x)$ on $\left[0 \,;\, 1 - \frac{1}{n}\right]$.
1. Compute the sum $\sum_{k=0}^{n-1} g\left(\frac{k}{n}\right)$.
2. Deduce that there exists at least one real number $x_0 \in \left[0 \,;\, 1 - \frac{1}{n}\right]$ such that $f\left(x_0 + \frac{1}{n}\right) = f(x_0)$.

**Exercise 46.22 (Accelerating Bisection: Newton's Method).**
Newton's method replaces the interval midpoint with the intersection of the tangent line with the $x$-axis:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$
1. Write a Python script to compute the zero of $f(x) = x^2 - 2$ starting from $x_0 = 1$.
2. Observe the number of iterations required to obtain 10 exact decimal places compared to bisection (quadratic convergence).

---

### Solutions

#### Solutions for Level ★

- **46.1:**
  1. $f$ is a polynomial, hence continuous on $\mathbb{R}$.
  2. $g$ is a rational function, hence continuous on its domain $\mathbb{R} \setminus \{5\}$.
  3. $h$ is the composite of $x \mapsto x-3$ and the square root function, continuous on $[3 \,;\, +\infty[$.
  4. $k(x)$ is not continuous: it jumps by 1 at every integer.

- **46.2:**
  1. $f(-2) = (-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13 > 0$. $f(5) = 25 - 20 + 1 = 6 > 0$.
     Note: although both $f(-2)$ and $f(5)$ are positive, the vertex of the parabola is at $x = 2$, where $f(2) = 4 - 8 + 1 = -3 < 0$. Since $f$ is continuous on $[-2 \,;\, 2]$ with $f(-2) > 0$ and $f(2) < 0$, by the IVT, it vanishes on $[-2 \,;\, 2] \subset [-2 \,;\, 5]$.

- **46.3:**
  - On $[-5 \,;\, -1]$, $g$ is continuous and strictly increasing from $-3$ to $7$. Since $4 \in [-3 \,;\, 7]$, there is exactly one solution.
  - On $[-1 \,;\, 4]$, $g$ is continuous and strictly decreasing from $7$ to $1$. Since $4 \in [1 \,;\, 7]$, there is exactly one solution.
  In total, the equation $g(x) = 4$ admits exactly **2 solutions** on $[-5 \,;\, 4]$.

- **46.4:** The exponential is continuous on $\mathbb{R}$, the polynomial $x^2 + 1$ is continuous on $\mathbb{R}$ and never vanishes because $x^2 + 1 \geq 1 > 0$. The quotient of two continuous functions with a nowhere-zero denominator is continuous on $\mathbb{R}$.

- **46.5:**
  1. $f'(x) = 3x^2 + 3 = 3(x^2 + 1) > 0$ for all $x \in \mathbb{R}$. Thus $f$ is strictly increasing.
  2. $f(0) = -1$ and $f(1) = 1 + 3 - 1 = 3$.
  3. $f$ is continuous and strictly increasing on $[0 \,;\, 1]$, and $0 \in [-1 \,;\, 3]$. By the IVT corollary, there exists a unique real number $\alpha \in [0 \,;\, 1]$ such that $f(\alpha) = 0$.

- **46.6:** The function $f(x) = \frac{1}{2}x + 1$ is continuous on $\mathbb{R}$. By the fixed-point theorem, $L = f(L) \iff L = \frac{1}{2}L + 1 \iff \frac{1}{2}L = 1 \iff L = 2$.

- **46.7:** For continuity at $1$: $f(1) = 2(1) + k = 2 + k$.
  $\lim_{x \to 1^+} f(x) = 1^2 + 3 = 4$.
  We must have $2 + k = 4 \iff k = 2$.

- **46.8:**
```python
def f(x):
    return x**2 - 2

a, b = 1.0, 2.0
while (b - a) > 1e-3:
    m = (a + b) / 2
    if f(a) * f(m) <= 0:
        b = m
    else:
        a = m
print(f"sqrt(2) ≈ {(a + b)/2:.4f}")
```

---

#### Solutions for Level ★★

- **46.9:**
  1. $\lim_{x \to -\infty} f(x) = \lim x^3 = -\infty$ and $\lim_{x \to +\infty} f(x) = +\infty$.
  2. $f'(x) = 3x^2 - 6x = 3x(x - 2)$.
     Roots: $x = 0$ and $x = 2$.
     $f(0) = 1$ (local maximum) and $f(2) = 8 - 12 + 1 = -3$ (local minimum).
     $f$ is increasing on $]-\infty ; 0]$, decreasing on $[0 ; 2]$, and increasing on $[2 ; +\infty[$.
  3. On $]-\infty ; 0]$, $f$ is continuous and strictly increasing from $-\infty$ to 1. Since $0 \in ]-\infty ; 1]$, there is a unique solution $\alpha_1$.
     On $[0 ; 2]$, $f$ is continuous and strictly decreasing from 1 to $-3$. Since $0 \in [-3 ; 1]$, there is a unique solution $\alpha_2$.
     On $[2 ; +\infty[$, $f$ is continuous and strictly increasing from $-3$ to $+\infty$. Since $0 \in [-3 ; +\infty[$, there is a unique solution $\alpha_3$.
     There are thus exactly 3 real solutions.
  4. For the largest solution $\alpha_3 \in [2 ; +\infty[$:
     $f(2) = -3 < 0$, $f(3) = 27 - 27 + 1 = 1 > 0$, so $\alpha_3 \in [2 ; 3]$.
     $f(2.8) = (2.8)^3 - 3(2.8)^2 + 1 = 21.952 - 23.52 + 1 = -0.568 < 0$.
     $f(2.9) = (2.9)^3 - 3(2.9)^2 + 1 = 24.389 - 25.23 + 1 = 0.159 > 0$.
     Bracketing: $2.8 < \alpha_3 < 2.9$.
  5. Sign: negative on $]-\infty ; \alpha_1]$, positive on $[\alpha_1 ; \alpha_2]$, negative on $[\alpha_2 ; \alpha_3]$, positive on $[\alpha_3 ; +\infty[$.

- **46.10:**
  1. $g'(x) = 1 \cdot e^x + (x - 1)e^x = x e^x$.
     Since $e^x > 0$, $g'(x)$ shares the sign of $x$: decreasing on $]-\infty ; 0]$ and increasing on $[0 ; +\infty[$.
  2. Minimum at 0: $g(0) = (0 - 1)e^0 + 1 = -1 + 1 = 0$.
     Since the absolute minimum is 0, $g(x) \geq 0$ for all real $x$, with equality if and only if $x = 0$.
  3. The equation of the tangent line to $y = e^x$ at $x = 1$ is: $y = e^1(x - 1) + e^1 = e \cdot x$.
     (Notice $(x-1)e^x + 1 \geq 0$ demonstrates the convex position relative to the tangent).

- **46.11:**
  1. Let $h(x) = e^{-x} - x$ on $\mathbb{R}$. $h$ is continuous on $\mathbb{R}$ and $h'(x) = -e^{-x} - 1 < 0$ (since $-e^{-x} < 0$). Thus $h$ is strictly decreasing.
     $\lim_{x \to -\infty} h(x) = +\infty$ and $\lim_{x \to +\infty} h(x) = -\infty$. By the IVT corollary, there exists a unique zero $\alpha$ on $\mathbb{R}$.
  2. $h(0) = e^0 - 0 = 1 > 0$ and $h(1) = e^{-1} - 1 \approx 0.368 - 1 = -0.632 < 0$. Thus $\alpha \in [0 \,;\, 1]$.
  3. Python script:
```python
import math
def h(x):
    return math.exp(-x) - x

a, b = 0.0, 1.0
while (b - a) > 1e-6:
    m = (a + b) / 2
    if h(a) * h(m) <= 0:
        b = m
    else:
        a = m
print(f"Intersection point alpha ≈ {(a + b)/2:.6f}")
# alpha ≈ 0.567143 (Omega constant)
```

- **46.12:**
  1. **False.** It vanishes *at least* once, but could vanish multiple times if not strictly monotonic.
  2. **False.** Counterexample: a strictly increasing step function with jump discontinuities. Strict monotonicity does not imply continuity.
  3. **False.** Counterexample: $f(x) = \frac{1}{x}$ on $]0 \,;\, 1[$ is continuous, but its image is $]1 \,;\, +\infty[$, which is unbounded.
  4. **True.** If it changed sign, the IVT would force the existence of a zero, contradicting the assumption that it never vanishes.

- **46.13:**
  1. At each step, the length is divided by 2: $L_n = \dfrac{L_0}{2^n} = \dfrac{4}{2^n} = \dfrac{1}{2^{n-2}}$.
  2. We seek $n$ such that $\dfrac{4}{2^n} \leq 10^{-5} \iff 2^n \geq 4 \times 10^5 = 400,000$.
     Since $2^{18} = 262,144$ and $2^{19} = 524,288$, at least **19 steps** are necessary.

- **46.14:**
  1. $x + 1 = 0 \iff x = -1 \notin [1 \,;\, 3]$. $f$ is a rational function whose denominator does not vanish on $[1 \,;\, 3]$, so it is continuous there.
  2. Fixed points: $f(x) = x \iff \frac{4x - 2}{x + 1} = x \iff 4x - 2 = x^2 + x \iff x^2 - 3x + 2 = 0$.
     Roots: $(x - 1)(x - 2) = 0 \iff x = 1$ or $x = 2$.
  3. If $u_0 = 2$, then $u_1 = f(2) = 2$: the sequence is constantly equal to 2. If it converges to $L \geq 1$, by the fixed-point theorem, $L \in \{1 ; 2\}$. With $u_0 = 2$, $L = 2$.

- **46.15:**
  1. $g(0) = f(0) - 0 = f(0) \geq 0$ (since $f(x) \in [0 ; 1]$).
     $g(1) = f(1) - 1 \leq 0$ (since $f(1) \leq 1$).
  2. The function $g$ is continuous on $[0 \,;\, 1]$ because $f$ is continuous. Since $g(0) \geq 0$ and $g(1) \leq 0$, by the IVT, there exists at least one real number $c \in [0 \,;\, 1]$ such that $g(c) = 0$, that is, $f(c) = c$.

- **46.16:** Let $x(t)$ be the position of the monk on Saturday at time $t \in [6 \,;\, 18]$ (with $x(6) = 0$ and $x(18) = D$, where $D$ is the total distance).
  Let $y(t)$ be his position on Sunday at time $t$ (with $y(6) = D$ and $y(18) = 0$).
  Set $h(t) = x(t) - y(t)$. $h$ is continuous on $[6 \,;\, 18]$.
  $h(6) = 0 - D = -D < 0$ and $h(18) = D - 0 = D > 0$.
  By the IVT, there exists a time $t_0 \in ]6 \,;\, 18[$ such that $h(t_0) = 0 \iff x(t_0) = y(t_0)$. At that exact time, the monk is at the very same spot on the path.

- **46.17:**
  - If $f$ is strictly monotonic, it is clearly injective (if $x < y$, then $f(x) < f(y)$ or $f(x) > f(y)$, so $f(x) \neq f(y)$).
  - Conversely, if $f$ is not strictly monotonic, it has a local extremum or non-monotonic behavior, which by the IVT creates two distinct points $a < b$ with $f(a) = f(b)$, contradicting injectivity.

---

#### Solutions for Level ★★★

- **46.18:**
  1. Let $x_0 \in \mathbb{R}$. In every open interval $]x_0 - \varepsilon \,;\, x_0 + \varepsilon[$, there are infinitely many rationals (where $f(x) = 1$) and infinitely many irrationals (where $f(x) = 0$).
     Any sequence of rationals tending to $x_0$ yields an image sequence constant at 1.
     Any sequence of irrationals tending to $x_0$ yields an image sequence constant at 0.
  2. Since the two limits ($1$ and $0$) differ, $f$ has no limit at $x_0$. It is therefore discontinuous at every point of $\mathbb{R}$.

- **46.19:** Set $D(\theta) = T(\theta + \pi) - T(\theta)$ for $\theta \in [0 \,;\, \pi]$.
  $D$ is continuous on $[0 \,;\, \pi]$.
  $D(0) = T(\pi) - T(0)$.
  $D(\pi) = T(2\pi) - T(\pi) = T(0) - T(\pi) = -D(0)$ because $T(2\pi) = T(0)$.
  If $D(0) = 0$, $\theta = 0$ works.
  Otherwise, $D(0)$ and $D(\pi)$ have opposite signs: by the IVT, there exists $\theta_0 \in ]0 \,;\, \pi[$ such that $D(\theta_0) = 0 \iff T(\theta_0 + \pi) = T(\theta_0)$.

- **46.20:**
  1. $f(0 + 0) = f(0) + f(0) \implies f(0) = 0$. By induction, $f(n) = n f(1) = c \cdot n$.
  2. $f(0) = f(p + (-p)) = f(p) + f(-p) = 0 \implies f(-p) = -f(p) = -c \cdot p = c \cdot (-p)$. True for all $p \in \mathbb{Z}$.
  3. Let $r = p/q$. Then $q \cdot f(p/q) = f(q \cdot p/q) = f(p) = c \cdot p \implies f(p/q) = c \cdot \frac{p}{q}$.
  4. For any real number $x$, there exists a sequence of rationals $(r_n)$ converging to $x$. By continuity of $f$: $f(x) = \lim f(r_n) = \lim (c \cdot r_n) = c \cdot x$.

- **46.21:**
  1. The sum is telescoping:
     $$\sum_{k=0}^{n-1} g\left(\frac{k}{n}\right) = \sum_{k=0}^{n-1} \left[f\left(\frac{k+1}{n}\right) - f\left(\frac{k}{n}\right)\right] = f(1) - f(0) = 0.$$
  2. A sum of $n$ terms equaling 0 implies that either all terms are zero, or at least one is non-negative and at least one is non-positive.
     The continuous function $g$ therefore takes a value $\geq 0$ and a value $\leq 0$. By the IVT, $g$ vanishes at some point $x_0$, whence $f(x_0 + 1/n) = f(x_0)$.

- **46.22:**
  1. Python script:
```python
def f(x):
    return x**2 - 2
def f_prime(x):
    return 2*x

x = 1.0
for i in range(5):
    x = x - f(x) / f_prime(x)
    print(f"Step {i+1}: x = {x:.12f}")
# Step 1: 1.500000000000
# Step 2: 1.416666666667
# Step 3: 1.414215686275
# Step 4: 1.414213562375 (12 exact decimals in 4 steps!)
```
  2. Bisection gains 1 bit of precision per step (requiring about 33 steps for 10 decimal digits). Newton doubles the number of exact decimal places at every step (quadratic convergence): 4 to 5 steps are plenty!

---

### The Question That Opens What Follows

We have just seen that continuity ensures a curve never tears. But a continuous curve can be filled with sharp corners (like $|x|$ at zero) or abrupt kinks.
To speak of **velocity**, **acceleration**, and **smooth trajectory**, we need the supreme instrument of differential calculus: differentiation.
What happens when we differentiate a function of a function, like a mechanical gearbox where a first cog drives a second, which in turn drives a third?
How does the second derivative reveal whether a curve cups upward toward the sky like a bowl catching rain (**convexity**) or slices through its own tangent (**inflection point**)?

This is the art of gears and curvature: see you in Chapter 47.
