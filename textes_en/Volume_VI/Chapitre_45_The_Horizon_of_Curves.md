# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 45: The Horizon of Curves

> *“Asymptote comes from the ancient Greek asúmptōtos: ‘not falling together’, ‘not meeting’. It is the sailor's horizon: the further the ship ventures out to sea, the more the horizon seems to offer itself, yet the hull can never cross its threshold. In the Cartesian sky, asymptotes are the invisible rails guiding the destiny of curves toward infinity.”*

---

### What You Will Discover

- The fundamental transition from the discrete variable $n \in \mathbb{N}$ to the continuous variable $x \in \mathbb{R}$: how functions glide toward infinity or toward a point of rupture.
- Rigorous definitions of **finite and infinite limits**, as well as the indispensable notions of **left-hand limit and right-hand limit**.
- The **three families of asymptotes** (vertical, horizontal, oblique) and the method to determine the **relative position** of a curve with respect to its guide line.
- The complete toolkit to resolve the **four indeterminate forms**: factoring out the dominant term, multiplying by the conjugate expression, and recognizing difference quotients.
- The triumph of the **growth hierarchy (comparative growth)** of the exponential function over powers of $x$, with its **required Baccalaureate proof**.
- The theorem on the **limit of a composite function** $g(f(x))$.

---

### 1. The Problem: The Optical Lens and the Black Hole

#### 1.1 The Physicist and Focal Length

In an optics laboratory, a light ray passes through a thin converging lens of focal length $f > 0$. A luminous object is placed at a distance $p$ in front of the lens. The Descartes-Gauss thin lens formula relates the object distance $p$ to the position of the sharp image $p'$ formed on a screen behind the lens:

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f}.$$

Let us express the image position $p'$ as a function of the object distance $p$:

$$p'(p) = \frac{f \cdot p}{p - f}.$$

What happens as the experimenter moves the object closer to the lens?

```
               Object                     Lens                     Screen
                 |                          |                        |
                 |◄───────── p ────────────►|◄───────── p' ─────────►|
                 |                          |                        |
           [Light source]               (Focus F)
```

1. **If the object is infinitely far away ($p \to +\infty$)**:
   $$p'(p) = \frac{f \cdot p}{p(1 - f/p)} = \frac{f}{1 - f/p} \xrightarrow[p \to +\infty]{} f.$$
   The image forms precisely in the focal plane of the lens. The horizontal line $y = f$ is a **limiting boundary**, a ceiling that the image position cannot cross: it is a **horizontal asymptote**.

2. **If the object approaches the focal point ($p \to f$ with $p > f$)**:
   The denominator $p - f$ becomes an infinitely small positive number ($0.001$, $0.000001$...).
   The quotient $p'(p)$ explodes to astronomical values:
   $$\lim_{p \to f^+} p'(p) = +\infty.$$
   To view the sharp image, one would need to push the screen to the end of the room, then outside the building, then to the Moon! The emerging rays are parallel: the image is cast to infinity. The vertical line $x = f$ acts like an impassable cliff: it is a **vertical asymptote**.

#### 1.2 From Discrete Steps to Continuous Flux

In Chapter 44, the variable $n$ jumped from integer to integer: $n = 0, 1, 2, 3 \dots$ It made no sense to ask what happened between $n=2$ and $n=3$, and one could only take the limit of $n$ toward $+\infty$.

With functions of a real variable $x \mapsto f(x)$, the world becomes **fluid and continuous**.
The real variable $x$ can:
- flee toward $+\infty$ or toward $-\infty$;
- glide toward a fixed real number $x_0$ (for example $x \to 2$);
- approach a forbidden point from the left ($x < x_0$) or from the right ($x > x_0$).

---

### 2. Rigorous Definitions of Function Limits

#### 2.1 The Notations Explained

- $\lim\limits_{x \to +\infty} f(x) = L$: “the limit of $f(x)$ as $x$ tends to plus infinity is equal to $L$”.
- $\lim\limits_{x \to x_0} f(x) = L$: “the limit of $f(x)$ as $x$ tends to the real number $x_0$ is equal to $L$”.
- $x \to x_0^+$ or $x \xrightarrow[x > x_0]{} x_0$: “$x$ tends to $x_0$ through values strictly greater” (right-hand limit).
- $x \to x_0^-$ or $x \xrightarrow[x < x_0]{} x_0$: “$x$ tends to $x_0$ through values strictly less” (left-hand limit).

#### 2.2 Finite Limit at Infinity

> **📐 Definition — Finite limit at $+\infty$.**
> Let $f$ be a function defined on an interval $[a \,;\, +\infty[$, and let $L \in \mathbb{R}$.
> We say that **$f$ has limit $L$ at $+\infty$** if:
> **Every open interval containing $L$ contains all values $f(x)$ for sufficiently large $x$.**
> We write:
> $$\lim_{x \to +\infty} f(x) = L.$$
> (Analogous definition at $-\infty$ on an interval $]-\infty \,;\, b]$).

*Concrete meaning:* Draw a horizontal strip of width $2\varepsilon$ centered on $y = L$, as narrow as you wish. If you move sufficiently far to the right along the $x$-axis (past a certain threshold $X$), the graph of the function remains trapped inside this strip forever.

#### 2.3 Infinite Limit at a Point: The Vertical Wall

> **📐 Definition — Infinite limit at a real point $x_0$.**
> Let $x_0 \in \mathbb{R}$. We say that **$f(x)$ tends to $+\infty$ as $x$ tends to $x_0$** if:
> **For every real number $A > 0$, the interval $]A \,;\, +\infty[$ contains all values $f(x)$ for $x$ sufficiently close to $x_0$.**
> We write:
> $$\lim_{x \to x_0} f(x) = +\infty.$$

#### 2.4 Left-Hand and Right-Hand Limits

Some functions exhibit radically different behaviors depending on whether they are approached from the port side or starboard side. The archetype is the reciprocal function $f(x) = \frac{1}{x}$ near zero:
- If $x > 0$ and $x \to 0$: $x$ takes values like $0.1$; $0.001$; $0.00001$. The quotient $\frac{1}{x}$ is $10$; $1000$; $100,000$:
  $$\lim_{x \to 0^+} \frac{1}{x} = +\infty.$$
- If $x < 0$ and $x \to 0$: $x$ takes negative values like $-0.1$; $-0.001$. The quotient $\frac{1}{x}$ is $-10$; $-1000$:
  $$\lim_{x \to 0^-} \frac{1}{x} = -\infty.$$

```
             y ▲
               │         /  x > 0: climbs toward +∞
               │        /
               │       /
───────────────┼───────────────► x
             / │
            /  │
 x < 0:    /   │
 plunges to -∞ │
```

> **📐 Fundamental Theorem — Existence of the global two-sided limit at a point.**
> A function $f$ admits a limit $L$ at $x_0$ if and only if it admits both a left-hand limit and a right-hand limit at $x_0$, and these two limits are **equal**:
> $$\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = L.$$
> For $f(x) = \frac{1}{x}$ at 0, since $+\infty \neq -\infty$, the function has **no global two-sided limit** at 0.

---

### 3. Asymptotes: The Geometric Guide of Curves

An asymptote is a line that the curve $\mathcal{C}_f$ approaches arbitrarily closely as points on the curve recede toward infinity.

```
       Vertical Asymptote: x = a             Horizontal Asymptote: y = L
             │       /                             │
             │      /                              │             /~~~~~~\
             │     /                     ──────────┼────────────(─ y = L ─)────
             │    /                                │             \______/
         ────┼───*────────►                        │
             │ a                                   └──────────────────────►
```

#### 3.1 Horizontal Asymptote

> **📐 Definition — Horizontal asymptote.**
> If $\lim\limits_{x \to +\infty} f(x) = L$ (or if $\lim\limits_{x \to -\infty} f(x) = L$), where $L$ is a finite real number,
> then the line $\mathcal{D}$ with equation **$y = L$** is called a **horizontal asymptote** to the curve $\mathcal{C}_f$ in the neighborhood of $+\infty$ (or $-\infty$).

#### 3.2 Vertical Asymptote

> **📐 Definition — Vertical asymptote.**
> If $\lim\limits_{x \to a^+} f(x) = \pm\infty$ or if $\lim\limits_{x \to a^-} f(x) = \pm\infty$ (where $a \in \mathbb{R}$),
> then the line $\Delta$ with equation **$x = a$** is called a **vertical asymptote** to the curve $\mathcal{C}_f$.

#### 3.3 Oblique Asymptote

Sometimes the curve does not level off horizontally, but aligns itself along a slanted line with equation $y = ax + b$ with $a \neq 0$.

> **📐 Definition — Oblique asymptote.**
> The line $\mathcal{D}$ with equation **$y = ax + b$** is an oblique asymptote to the curve $\mathcal{C}_f$ at $+\infty$ (resp. $-\infty$) if:
> $$\lim_{x \to +\infty} \big[f(x) - (ax + b)\big] = 0 \quad \text{(resp. at } -\infty\text{)}.$$

*Geometric sense:* The vertical distance between the point on the curve $M(x ; f(x))$ and the point on the line $P(x ; ax + b)$ becomes infinitely small as one advances toward the ends of the coordinate plane.

#### 3.4 Determining Relative Position

To determine whether the curve $\mathcal{C}_f$ lies **above** or **below** its asymptote (horizontal $y = L$ or oblique $y = ax+b$), one applies the following universal method:

> **🧭 Method — Relative position of a curve and an asymptote:**
> 1. Compute the difference: $d(x) = f(x) - y_{\text{asymptote}}$.
> 2. Rigorously study the **sign** of $d(x)$:
>    - If $d(x) > 0$ on an interval, then $\mathcal{C}_f$ is **strictly above** the asymptote on that interval.
>    - If $d(x) < 0$ on an interval, then $\mathcal{C}_f$ is **strictly below** the asymptote.
>    - If $d(x) = 0$ at a point $x_1$, the curve **intersects / crosses** its asymptote at the point of abscissa $x_1$.

---

### 4. The Toolkit for Resolving Indeterminate Forms

Recall the four forms that prohibit immediate direct conclusions:
$$\text{I.F.: } \quad [\infty - \infty], \quad [0 \times \infty], \quad \left[\frac{\infty}{\infty}\right], \quad \left[\frac{0}{0}\right].$$

Here are the four fundamental techniques to master in Grade 12:

#### Method 1: Factoring Out the Dominant Term

At $+\infty$ or $-\infty$, in a polynomial or a rational function, the highest-degree term dictates the law to all others.
- For a polynomial: factor out the highest power of $x$.
- For a fraction: factor out the respective dominant powers from both numerator and denominator, then simplify.

> **⚠️ Caution, trap! — The sign under the square root at $-\infty$.**
> Always remember that for any real number $x$:
> $$\sqrt{x^2} = |x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$$
> As $x \to -\infty$, $x$ is a **strictly negative** number. Consequently:
> $$\sqrt{x^2} = -x \quad (\text{and not } +x \text{ !}).$$
> This is the single most heavily penalized error on Baccalaureate exams!

#### Method 2: The Conjugate Expression

When square roots clash in an indeterminacy of type $[\infty - \infty]$ or $[0/0]$, use the difference of squares identity $(a - b)(a + b) = a^2 - b^2$ to remove radicals from the problematic site:

$$\sqrt{A} - \sqrt{B} = \frac{(\sqrt{A} - \sqrt{B})(\sqrt{A} + \sqrt{B})}{\sqrt{A} + \sqrt{B}} = \frac{A - B}{\sqrt{A} + \sqrt{B}}.$$

The delicate subtraction $[\infty - \infty]$ turns into a well-behaved addition in the denominator $[\infty + \infty = \infty]$.

#### Method 3: Recognizing a Difference Quotient (Derivative)

An indeterminate form of type $\left[\frac{0}{0}\right]$ at a point $x_0$ very often conceals the very definition of the derivative:
$$\lim_{x \to x_0} \frac{g(x) - g(x_0)}{x - x_0} = g'(x_0).$$

Famous examples:
- $\lim\limits_{x \to 0} \dfrac{e^x - 1}{x}$: with $g(x) = e^x$, $g(0) = 1$, the limit is $g'(0) = e^0 = 1$.
- $\lim\limits_{x \to 0} \dfrac{\sin x}{x}$: with $g(x) = \sin x$, $g(0) = 0$, the limit is $\cos(0) = 1$.

---

### 5. Growth Hierarchy: Comparative Growth of the Exponential Function

When the exponential function confronts a polynomial or a power of $x$ at infinity, the explosive growth of $e^x$ infinitely surpasses any polynomial growth.

> **📐 Theorem — Comparative growth of the exponential function.**
> For any natural number $n \geq 1$:
> 1. $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$ $\quad$ and more generally $\quad$ $\lim\limits_{x \to +\infty} \dfrac{e^x}{x^n} = +\infty$
> 2. $\lim\limits_{x \to -\infty} x \, e^x = 0$ $\quad$ and more generally $\quad$ $\lim\limits_{x \to -\infty} x^n \, e^x = 0$

*Rule of thumb:* At $+\infty$ as well as at $-\infty$, **the exponential always dominates any power of $x$**.

#### Required Baccalaureate Proof: $\lim_{x \to +\infty} \frac{e^x}{x} = +\infty$

> **✍️ Proof (Required knowledge).**
> The goal is to obtain a lower bound for $e^x$ by a degree-2 polynomial, so that the quotient $\frac{e^x}{x}$ is bounded below by a degree-1 linear term tending to $+\infty$.
>
> **Step 1: Lower bound for the exponential function.**
> Consider the function $f$ defined on $[0 \,;\, +\infty[$ by:
> $$f(x) = e^x - \frac{x^2}{2}.$$
> Differentiate $f$ twice:
> - Its first derivative is $f'(x) = e^x - x$.
> - Its second derivative is $f''(x) = e^x - 1$.
>
> For all $x \geq 0$, $e^x \geq e^0 = 1$, so $f''(x) \geq 0$.
> Consequently, the derivative function $f'$ is strictly increasing on $[0 \,;\, +\infty[$.
> Now $f'(0) = e^0 - 0 = 1 > 0$.
> Since $f'$ is increasing and $f'(0) > 0$, for all $x \geq 0$ we have:
> $$f'(x) \geq f'(0) > 0.$$
> The function $f$ is therefore itself strictly increasing on $[0 \,;\, +\infty[$.
> Since $f(0) = e^0 - 0 = 1 > 0$, it follows that for all $x \geq 0$:
> $$f(x) > 0 \implies e^x > \frac{x^2}{2}.$$
>
> **Step 2: Passing to the quotient and conclusion.**
> For any real number $x > 0$, divide this inequality by $x$ (since $x > 0$, the inequality direction is preserved):
> $$\frac{e^x}{x} > \frac{x}{2}.$$
> Now:
> $$\lim_{x \to +\infty} \frac{x}{2} = +\infty.$$
> By the **comparison theorem** for limits, we conclude irrefutably:
> $$\lim_{x \to +\infty} \frac{e^x}{x} = +\infty. \quad \blacksquare$$

*Proof of $\lim\limits_{x \to -\infty} x e^x = 0$ via change of variable:*
Set $X = -x$. As $x \to -\infty$, we have $X \to +\infty$.
Then:
$$x \, e^x = (-X) \, e^{-X} = - \frac{X}{e^X} = - \frac{1}{\dfrac{e^X}{X}}.$$
Since $\lim\limits_{X \to +\infty} \dfrac{e^X}{X} = +\infty$, by the reciprocal of an infinite limit:
$$\lim_{x \to -\infty} x \, e^x = \lim_{X \to +\infty} \left(-\frac{1}{e^X/X}\right) = 0. \quad \blacksquare$$

---

### 6. Limit of a Composite Function

A composite function is a cascade: the output of the first machine $f$ becomes the input of the second machine $g$. This operation is denoted $(g \circ f)(x) = g(f(x))$.

> **📐 Theorem — Limit of a composite function.**
> Let $a, b, c$ denote either real numbers, $+\infty$, or $-\infty$.
> If:
> $$\lim_{x \to a} f(x) = b \quad \text{and} \quad \lim_{y \to b} g(y) = c,$$
> then:
> $$\lim_{x \to a} g(f(x)) = c.$$

> **🧭 Method — Writing out the limit of a composite on the Bac:**
> Never compute everything all at once. Clearly separate into two steps by introducing a dummy variable substitution:
> 1. *Inner step:* calculate $\lim\limits_{x \to a} f(x) = b$.
> 2. *Outer step:* set $X = f(x)$, and since $X \to b$, calculate $\lim\limits_{X \to b} g(X) = c$.
> 3. *Conclusion:* By composition of limits, $\lim\limits_{x \to a} g(f(x)) = c$.

---

### 7. Traps to Avoid!

> **⚠️ Caution, trap! — Crossing an asymptote.**
> A widespread misconception among students is that a curve “is never allowed to touch its asymptote”.
> This is **true for a vertical asymptote** $x = a$ (because the function is generally undefined there).
> But it is **completely false for a horizontal or oblique asymptote**!
> A horizontal asymptote $y = L$ describes solely what occurs **at the far edge of the world** (for $x \to \pm\infty$). In the meantime, for moderate values of $x$, the curve may intersect the horizontal line once, ten times, or even infinitely many times!
> *Example:* $f(x) = \frac{\sin x}{x}$ has the $x$-axis $y = 0$ as a horizontal asymptote, and crosses this axis at every integer multiple of $\pi$ ($\pi, 2\pi, 3\pi \dots$).

> **⚠️ Caution, trap! — Comparative growth applies only at infinity!**
> Never say: “$\lim\limits_{x \to 0} \frac{e^x}{x} = +\infty$ by comparative growth”!
> At 0, the numerator tends to $e^0 = 1$ and the denominator to 0. It is a direct quotient of a finite non-zero number by zero ($1/0^+$ or $1/0^-$), not comparative growth! Comparative growth compares the escape velocity toward infinity.

---

### 8. Step-by-Step Worked Examples

#### Worked Example 1 — Asymptotes and Resolving Indeterminacy at $+\infty$ and $-\infty$

**Problem:** Consider the function $f$ defined on $\mathbb{R} \setminus \{2\}$ by:
$$f(x) = \frac{3x - 1}{x - 2}.$$
1. Determine the limits of $f$ at the boundaries of its domain of definition ($+\infty$, $-\infty$, and at 2 from below and from above).
2. Deduce the equations of the asymptotes to the graph $\mathcal{C}_f$.
3. Study the relative position of $\mathcal{C}_f$ with respect to its horizontal asymptote.

**Solution:**
1. **Limits at infinity:**
   For $x \neq 0$:
   $$f(x) = \frac{x\left(3 - \dfrac{1}{x}\right)}{x\left(1 - \dfrac{2}{x}\right)} = \frac{3 - \dfrac{1}{x}}{1 - \dfrac{2}{x}}.$$
   Since $\lim\limits_{x \to \pm\infty} \frac{1}{x} = 0$ and $\lim\limits_{x \to \pm\infty} \frac{2}{x} = 0$, we obtain:
   $$\lim_{x \to +\infty} f(x) = 3 \quad \text{and} \quad \lim_{x \to -\infty} f(x) = 3.$$

   **Limits at 2:**
   Numerator: $\lim_{x \to 2} (3x - 1) = 3(2) - 1 = 5 > 0$.
   Denominator: $\lim_{x \to 2} (x - 2) = 0$.
   - If $x > 2$, $x - 2 > 0$, so the denominator tends to $0^+$. By quotient:
     $$\lim_{x \to 2^+} f(x) = +\infty.$$
   - If $x < 2$, $x - 2 < 0$, the denominator tends to $0^-$. By quotient:
     $$\lim_{x \to 2^-} f(x) = -\infty.$$

2. **Asymptotes:**
   - Since $\lim\limits_{x \to \pm\infty} f(x) = 3$, the line with equation **$y = 3$** is a horizontal asymptote to $\mathcal{C}_f$ at $+\infty$ and at $-\infty$.
   - Since $\lim\limits_{x \to 2} f(x) = \pm\infty$, the line with equation **$x = 2$** is a vertical asymptote to $\mathcal{C}_f$.

3. **Relative position with respect to the horizontal asymptote $y = 3$:**
   Compute the difference $d(x) = f(x) - 3$:
   $$d(x) = \frac{3x - 1}{x - 2} - 3 = \frac{(3x - 1) - 3(x - 2)}{x - 2} = \frac{3x - 1 - 3x + 6}{x - 2} = \frac{5}{x - 2}.$$
   - For all $x \in ]2 \,;\, +\infty[$, $x - 2 > 0$, so $d(x) > 0$: the curve $\mathcal{C}_f$ is **strictly above** the asymptote $y = 3$.
   - For all $x \in ]-\infty \,;\, 2[$, $x - 2 < 0$, so $d(x) < 0$: the curve $\mathcal{C}_f$ is **strictly below** the asymptote $y = 3$.

---

#### Worked Example 2 — The Sign Trap for $\sqrt{x^2}$ at $-\infty$

**Problem:** Determine the limit at $-\infty$ and at $+\infty$ of the function:
$$f(x) = \sqrt{x^2 + 4x + 5} + x.$$

**Solution:**
**At $+\infty$:**
$\lim\limits_{x \to +\infty} (x^2 + 4x + 5) = +\infty$, so $\lim \sqrt{x^2+4x+5} = +\infty$.
Since $\lim\limits_{x \to +\infty} x = +\infty$, by addition:
$$\lim_{x \to +\infty} f(x) = +\infty \quad (\text{no indeterminate form here!}).$$

**At $-\infty$:**
$\lim\limits_{x \to -\infty} \sqrt{x^2+4x+5} = +\infty$ and $\lim\limits_{x \to -\infty} x = -\infty$.
This is an indeterminate form $[\infty - \infty]$.
Use the **conjugate expression**:
$$f(x) = \frac{\left(\sqrt{x^2 + 4x + 5} + x\right)\left(\sqrt{x^2 + 4x + 5} - x\right)}{\sqrt{x^2 + 4x + 5} - x} = \frac{(x^2 + 4x + 5) - x^2}{\sqrt{x^2 + 4x + 5} - x} = \frac{4x + 5}{\sqrt{x^2 + 4x + 5} - x}.$$
Now factor out the dominant term in the denominator for $x < 0$:
$$\sqrt{x^2 + 4x + 5} = \sqrt{x^2\left(1 + \frac{4}{x} + \frac{5}{x^2}\right)} = |x|\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}}.$$
As $x \to -\infty$, we have $x < 0$, so $|x| = -x$!
$$\sqrt{x^2 + 4x + 5} - x = -x\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}} - x = -x \left[\sqrt{1 + \frac{4}{x} + \frac{5}{x^2}} + 1\right].$$
The numerator is $4x + 5 = x\left(4 + \frac{5}{x}\right)$.
Thus, for $x < 0$:
$$f(x) = \frac{x\left(4 + \dfrac{5}{x}\right)}{-x \left[\sqrt{1 + \dfrac{4}{x} + \dfrac{5}{x^2}} + 1\right]} = \frac{4 + \dfrac{5}{x}}{-\left(\sqrt{1 + \dfrac{4}{x} + \dfrac{5}{x^2}} + 1\right)}.$$
Take the limit as $x \to -\infty$:
- The numerator tends to $4 + 0 = 4$.
- The denominator tends to $-( \sqrt{1 + 0 + 0} + 1 ) = -(1 + 1) = -2$.
By quotient:
$$\lim_{x \to -\infty} f(x) = \frac{4}{-2} = -2.$$
*Geometric consequence:* The line with equation $y = -2$ is a horizontal asymptote to the curve at $-\infty$.

---

#### Worked Example 3 — Comparative Growth and Factoring Exponentials

**Problem:** Determine the limit at $+\infty$ and at $-\infty$ of the function $f(x) = (2x - 3)e^{-x} + 1$.

**Solution:**
**At $+\infty$:**
Write $f(x) = 2x e^{-x} - 3e^{-x} + 1 = \frac{2x}{e^x} - \frac{3}{e^x} + 1 = 2 \left(\frac{1}{\frac{e^x}{x}}\right) - \frac{3}{e^x} + 1$.
By comparative growth theorems, $\lim\limits_{x \to +\infty} \frac{e^x}{x} = +\infty$, so $\lim\limits_{x \to +\infty} \frac{x}{e^x} = 0$.
Moreover, $\lim\limits_{x \to +\infty} e^x = +\infty$, whence $\lim\limits_{x \to +\infty} \frac{3}{e^x} = 0$.
By addition of limits:
$$\lim_{x \to +\infty} f(x) = 2(0) - 0 + 1 = 1.$$
The line with equation $y = 1$ is a horizontal asymptote at $+\infty$.

**At $-\infty$:**
Set the substitution $X = -x$. As $x \to -\infty$, $X \to +\infty$.
Then:
$f(x) = (-2X - 3)e^X + 1 = -2X e^X - 3e^X + 1.$
As $X \to +\infty$, $e^X \to +\infty$ and $-2X - 3 \to -\infty$.
By product:
$$\lim_{x \to -\infty} (2x - 3) = -\infty \quad \text{and} \quad \lim_{x \to -\infty} e^{-x} = +\infty \implies \lim_{x \to -\infty} (2x - 3)e^{-x} = -\infty.$$
Hence:
$$\lim_{x \to -\infty} f(x) = -\infty.$$

---

#### Worked Example 4 — Limit of a Composite with Radical and Rational Functions

**Problem:** Determine the limit as $x \to +\infty$ of:
$$h(x) = \sqrt{\frac{4x^2 + 1}{x^2 - 3x + 2}}.$$

**Solution:**
Decompose the function by setting $f(x) = \frac{4x^2 + 1}{x^2 - 3x + 2}$ and $g(X) = \sqrt{X}$, so that $h(x) = g(f(x))$.
1. *Inner limit:*
   For $x > 0$:
   $$f(x) = \frac{x^2\left(4 + \dfrac{1}{x^2}\right)}{x^2\left(1 - \dfrac{3}{x} + \dfrac{2}{x^2}\right)} = \frac{4 + \dfrac{1}{x^2}}{1 - \dfrac{3}{x} + \dfrac{2}{x^2}}.$$
   Since $\lim\limits_{x \to +\infty} \frac{1}{x^2} = 0$, $\lim\limits_{x \to +\infty} \frac{3}{x} = 0$, and $\lim\limits_{x \to +\infty} \frac{2}{x^2} = 0$, we have:
   $$\lim_{x \to +\infty} f(x) = \frac{4}{1} = 4.$$
2. *Outer limit:*
   Set $X = f(x)$. As $X \to 4$:
   $$\lim_{X \to 4} g(X) = \lim_{X \to 4} \sqrt{X} = \sqrt{4} = 2.$$
3. *Conclusion:*
   By composition of limits:
   $$\lim_{x \to +\infty} h(x) = 2.$$
The line with equation $y = 2$ is a horizontal asymptote to the curve of $h$ at $+\infty$.

---

#### Worked Example 5 — Complete Determination of an Oblique Asymptote

**Problem:** Consider the function $f$ defined on $\mathbb{R} \setminus \{1\}$ by $f(x) = \frac{2x^2 - x + 3}{x - 1}$.
1. Determine real numbers $a, b, c$ such that for all $x \neq 1$: $f(x) = ax + b + \frac{c}{x - 1}$.
2. Prove that the line $\mathcal{D}$ with equation $y = 2x + 1$ is an oblique asymptote to the curve $\mathcal{C}_f$ at $+\infty$ and $-\infty$.
3. Specify the relative position of $\mathcal{C}_f$ with respect to $\mathcal{D}$.

**Solution:**
1. Expand the desired form:
   $$ax + b + \frac{c}{x - 1} = \frac{(ax + b)(x - 1) + c}{x - 1} = \frac{ax^2 - ax + bx - b + c}{x - 1} = \frac{ax^2 + (b - a)x + (c - b)}{x - 1}.$$
   Equating coefficients with $2x^2 - x + 3$:
   $$\begin{cases} a = 2 \\ b - a = -1 \implies b = a - 1 = 2 - 1 = 1 \\ c - b = 3 \implies c = 3 + b = 3 + 1 = 4 \end{cases}$$
   Thus for all $x \neq 1$:
   $$f(x) = 2x + 1 + \frac{4}{x - 1}.$$

2. Compute the difference between $f(x)$ and $y = 2x + 1$:
   $$f(x) - (2x + 1) = \frac{4}{x - 1}.$$
   Now $\lim\limits_{x \to +\infty} \frac{4}{x - 1} = 0$ and $\lim\limits_{x \to -\infty} \frac{4}{x - 1} = 0$.
   By definition, the line $\mathcal{D}$ with equation $y = 2x + 1$ is an **oblique asymptote** to the curve $\mathcal{C}_f$ at $+\infty$ and at $-\infty$.

3. **Relative position:**
   The sign of $f(x) - (2x + 1)$ is the sign of $\frac{4}{x - 1}$:
   - If $x > 1$, $x - 1 > 0 \implies \frac{4}{x - 1} > 0$: $\mathcal{C}_f$ is **strictly above** $\mathcal{D}$.
   - If $x < 1$, $x - 1 < 0 \implies \frac{4}{x - 1} < 0$: $\mathcal{C}_f$ is **strictly below** $\mathcal{D}$.

---

#### Worked Example 6 — Form $\frac{0}{0}$ Resolved via Difference Quotient

**Problem:** Determine without a calculator $\lim\limits_{x \to 0} \frac{e^{3x} - 1}{x}$.

**Solution:**
At $x = 0$, $e^0 - 1 = 0$ and the denominator is 0. This is an indeterminate form $[0/0]$.
Define the function $g(x) = e^{3x}$.
The function $g$ is differentiable on $\mathbb{R}$, and its derivative is $g'(x) = 3e^{3x}$.
Notice that $g(0) = e^0 = 1$.
The expression can be rewritten as:
$$\frac{e^{3x} - 1}{x} = \frac{g(x) - g(0)}{x - 0}.$$
By definition of the derivative:
$$\lim_{x \to 0} \frac{g(x) - g(0)}{x - 0} = g'(0) = 3e^{3 \times 0} = 3 \times 1 = 3.$$
The requested limit is therefore equal to $3$.

---

### Key Takeaways

1. **Definition of limit at infinity:** $\lim\limits_{x \to +\infty} f(x) = L$ if every open interval containing $L$ contains all values $f(x)$ for sufficiently large $x$.
2. **Asymptotes:**
   - $\lim\limits_{x \to \pm\infty} f(x) = L \iff y = L$ is a horizontal asymptote.
   - $\lim\limits_{x \to a^{\pm}} f(x) = \pm\infty \iff x = a$ is a vertical asymptote.
   - $\lim\limits_{x \to \pm\infty} [f(x) - (ax+b)] = 0 \iff y = ax+b$ is an oblique asymptote.
3. **Relative position:** determined by the sign of $f(x) - y_{\text{asymptote}}$.
4. **Indeterminate Forms:** $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.
5. **Comparative Growth:** $\lim\limits_{x \to +\infty} \frac{e^x}{x^n} = +\infty$ and $\lim\limits_{x \to -\infty} x^n e^x = 0$. In any direct confrontation, exponential growth dominates polynomial growth.
6. **Composite functions:** $\lim\limits_{x \to a} f(x) = b$ and $\lim\limits_{X \to b} g(X) = c \implies \lim\limits_{x \to a} g(f(x)) = c$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 45.1.** Determine by immediate inspection or elementary limit laws:
1. $\lim\limits_{x \to +\infty} (3x^3 - 5x + 1)$
2. $\lim\limits_{x \to -\infty} (-2x^4 + x^2)$
3. $\lim\limits_{x \to +\infty} \left(4 - \frac{2}{x} + \frac{5}{x^3}\right)$
4. $\lim\limits_{x \to 0^+} \left(\frac{3}{x} - 2\right)$

**Exercise 45.2.** Determine any asymptotes (vertical and horizontal) to the graphs of the following functions:
1. $f(x) = \dfrac{2x + 7}{x - 3}$ on $\mathbb{R} \setminus \{3\}$
2. $g(x) = \dfrac{1}{x^2 - 4}$ on $\mathbb{R} \setminus \{-2 ; 2\}$
3. $h(x) = 5 + e^{-x}$ on $[0 \,;\, +\infty[$

**Exercise 45.3.** Compute the left-hand limit and the right-hand limit of $f(x) = \dfrac{x + 1}{x - 4}$ at $x_0 = 4$. Does the function admit a global two-sided limit at 4?

**Exercise 45.4.** Resolve the indeterminacy for the following rational functions:
1. $\lim\limits_{x \to +\infty} \dfrac{4x^2 - 3x + 1}{2x^2 + 5x}$
2. $\lim\limits_{x \to -\infty} \dfrac{x^3 + 2}{5x^4 - x}$
3. $\lim\limits_{x \to +\infty} \dfrac{x^5 - 1}{x^2 + 100}$

**Exercise 45.5.** Use the comparative growth of the exponential to determine:
1. $\lim\limits_{x \to +\infty} (e^x - 3x^4)$
2. $\lim\limits_{x \to +\infty} \dfrac{e^x + 2}{x^3 + 1}$
3. $\lim\limits_{x \to -\infty} (x^2 + 1)e^x$

**Exercise 45.6.** Let $f(x) = \sqrt{2x + 3}$. Determine $\lim\limits_{x \to 3} \dfrac{f(x) - f(3)}{x - 3}$ by recognizing a difference quotient.

**Exercise 45.7.** Let $f(x) = 2x - 1 + \dfrac{3}{x^2+1}$. Prove that the line $y = 2x - 1$ is an oblique asymptote to $\mathcal{C}_f$ at $+\infty$ and determine the relative position of $\mathcal{C}_f$ with respect to this line.

**Exercise 45.8.** Determine by composition: $\lim\limits_{x \to +\infty} \exp\left(-\frac{1}{x^2}\right)$ and $\lim\limits_{x \to 0^+} \exp\left(-\frac{1}{x}\right)$.

---

#### Level ★★ (Guided Reflection and Baccalaureate Style)

**Exercise 45.9 (Baccalaureate Style: Function Study with Exponential).**
Consider the function $f$ defined on $\mathbb{R}$ by:
$$f(x) = (x - 2)e^x + x.$$
1. Determine the limit of $f$ at $-\infty$.
2. Prove that the line $(\Delta)$ with equation $y = x$ is an oblique asymptote to the curve $\mathcal{C}_f$ at $-\infty$.
3. Determine the relative position of $\mathcal{C}_f$ with respect to $(\Delta)$ on $]-\infty \,;\, +\infty[$.
4. Determine the limit of $f$ at $+\infty$.

**Exercise 45.10 (Conjugate Expression and Asymptotes).**
Let $f(x) = \sqrt{x^2 - 2x + 3}$.
1. Determine the limit of $f$ at $+\infty$.
2. Prove that for all $x > 0$:
   $$f(x) - (x - 1) = \frac{2}{\sqrt{x^2 - 2x + 3} + (x - 1)}.$$
3. Deduce that the line with equation $y = x - 1$ is an oblique asymptote to the curve at $+\infty$.

**Exercise 45.11 (The Square Root Trap at $-\infty$).**
Revisit the function of Exercise 45.10 at $-\infty$. Prove that the line with equation $y = -x + 1$ is an oblique asymptote to the curve at $-\infty$.

**Exercise 45.12 (Population Modeling: The Logistic Curve).**
The population of an animal species (in thousands) over time $t \geq 0$ (in years) is modeled by:
$$N(t) = \frac{10}{1 + 9e^{-0.5t}}.$$
1. Calculate the initial population $N(0)$.
2. Determine $\lim\limits_{t \to +\infty} N(t)$. Interpret this result in the context of the ecosystem (carrying capacity).
3. Determine the equation of the horizontal asymptote to the graph of $N$.

**Exercise 45.13 (Indeterminate Form Resolved via Clever Factoring).**
Determine the following limits:
1. $\lim\limits_{x \to 1} \dfrac{x^3 - 1}{x^2 - 1}$
2. $\lim\limits_{x \to 4} \dfrac{\sqrt{x} - 2}{x - 4}$
3. $\lim\limits_{x \to 0} \dfrac{\sqrt{1 + x} - 1}{x}$

**Exercise 45.14 (Rational Function and Partial Fraction Decomposition).**
Let $f(x) = \dfrac{3x^2 + 5x - 2}{x + 1}$.
1. Find three real numbers $a, b, c$ such that $f(x) = ax + b + \dfrac{c}{x + 1}$ for all $x \neq -1$.
2. Deduce all asymptotes to the graph of $f$.
3. Determine the coordinates of the intersection point of the two asymptotes.

**Exercise 45.15 (Composite and Trigonometric Functions).**
1. Determine $\lim\limits_{x \to +\infty} \cos\left(\frac{\pi x + 1}{2x - 3}\right)$.
2. Prove that the function $g(x) = x \sin\left(\frac{1}{x}\right)$ has limit 1 at $+\infty$. (Hint: set $X = 1/x$).

**Exercise 45.16 (Squeeze Theorem for Functions).**
Let $f(x) = \dfrac{2x + \sin(x)}{x - 1}$ defined on $]1 \,;\, +\infty[$.
1. Show that for all $x > 1$: $\dfrac{2x - 1}{x - 1} \leq f(x) \leq \dfrac{2x + 1}{x - 1}$.
2. Deduce $\lim\limits_{x \to +\infty} f(x)$.

**Exercise 45.17 (Complete Study of a Limit with a Parameter).**
Let $f_m(x) = \dfrac{m x^2 + 4x - 1}{2x^2 + 3}$ where $m$ is a real parameter.
Determine the limit of $f_m(x)$ as $x \to +\infty$ according to the values of the real number $m$.

---

#### Level ★★★ (Challenge and In-Depth Study)

**Exercise 45.18 (L'Hôpital's Rule — Higher Mathematics / Beyond Syllabus).**
Let $f$ and $g$ be two differentiable functions on an open interval containing $a$, such that $f(a) = g(a) = 0$ and $g'(a) \neq 0$.
1. By writing $\dfrac{f(x)}{g(x)} = \dfrac{\frac{f(x) - f(a)}{x - a}}{\frac{g(x) - g(a)}{x - a}}$, prove that:
   $$\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)}.$$
2. Use this result to compute: $\lim\limits_{x \to 0} \dfrac{e^{2x} - \cos(x)}{x}$.

**Exercise 45.19 (Parabolic Asymptote).**
Consider the function $f(x) = \dfrac{x^3 + 2x^2 - 1}{x - 1}$ for $x \neq 1$.
1. Show that there exists a quadratic polynomial $P(x)$ and a real number $R$ such that $f(x) = P(x) + \dfrac{R}{x - 1}$.
2. Deduce that as $x \to \pm\infty$, the graph of $f$ approaches a parabola with equation $y = P(x)$ (asymptotic parabola).

**Exercise 45.20 (A Function with No Limit at Zero).**
Consider the function $f(x) = \sin\left(\frac{1}{x}\right)$ defined on $\mathbb{R}^*$.
1. Calculate the values of $f(x)$ along the sequences $u_n = \dfrac{1}{2n\pi}$ and $v_n = \dfrac{1}{2n\pi + \pi/2}$ for $n \geq 1$.
2. What are the limits of $(u_n)$ and $(v_n)$ as $n \to +\infty$?
3. Deduce that the function $f$ has no limit at 0.

**Exercise 45.21 (Generalized Comparative Growth: Proof for all $n \in \mathbb{N}^*$).**
It is known that $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$.
1. Prove that for all $n \in \mathbb{N}^*$ and all $x > 0$:
   $$\frac{e^x}{x^n} = \frac{1}{n^n} \left(\frac{e^{x/n}}{x/n}\right)^n.$$
2. Setting $u = \dfrac{x}{n}$, deduce that $\lim\limits_{x \to +\infty} \dfrac{e^x}{x^n} = +\infty$.

**Exercise 45.22 (The Devil's Staircase and Limits at Infinity).**
Let $f(x) = x - \lfloor x \rfloor$ where $\lfloor x \rfloor$ denotes the floor function of $x$ (the greatest integer less than or equal to $x$).
1. Sketch the graph of $f$ on $[-2 \,;\, 3]$.
2. Does the function admit a limit as $x \to +\infty$?
3. Determine the left-hand limit and right-hand limit of $f$ at every integer $k \in \mathbb{Z}$.

---

### Solutions

#### Solutions for Level ★

- **45.1:**
  1. $\lim (3x^3 - 5x + 1) = \lim 3x^3 = +\infty$.
  2. $\lim (-2x^4 + x^2) = \lim -2x^4 = -\infty$ (since $x^4 \to +\infty$ and $-2 < 0$).
  3. $\lim (4 - 0 + 0) = 4$.
  4. For $x \to 0^+$, $3/x \to +\infty$, so $\lim = +\infty$.

- **45.2:**
  1. $\lim_{x \to \pm\infty} f(x) = 2 \implies y = 2$ is a horizontal asymptote. $\lim_{x \to 3} f(x) = \pm\infty \implies x = 3$ is a vertical asymptote.
  2. $\lim_{x \to \pm\infty} g(x) = 0 \implies y = 0$ is a horizontal asymptote. $x^2 - 4 = 0 \iff x = \pm 2$, yielding two vertical asymptotes: $x = 2$ and $x = -2$.
  3. $\lim_{x \to +\infty} e^{-x} = 0 \implies \lim_{x \to +\infty} h(x) = 5 \implies y = 5$ is a horizontal asymptote at $+\infty$.

- **45.3:** Numerator: $4 + 1 = 5 > 0$. Denominator: $x - 4 \to 0$.
  - If $x > 4$, $x - 4 > 0 \implies \lim_{x \to 4^+} f(x) = +\infty$.
  - If $x < 4$, $x - 4 < 0 \implies \lim_{x \to 4^-} f(x) = -\infty$.
  Since these one-sided limits differ, no global two-sided limit exists at 4.

- **45.4:**
  1. $\lim \frac{x^2(4 - 3/x + 1/x^2)}{x^2(2 + 5/x)} = \frac{4}{2} = 2$.
  2. $\lim \frac{x^3}{5x^4} = \lim \frac{1}{5x} = 0$.
  3. $\lim \frac{x^5}{x^2} = \lim x^3 = +\infty$.

- **45.5:**
  1. $e^x - 3x^4 = x^4 \left(\frac{e^x}{x^4} - 3\right) \to +\infty \times (+\infty - 3) = +\infty$.
  2. $\frac{e^x(1 + 2e^{-x})}{x^3(1 + x^{-3})} = \frac{e^x}{x^3} \times \frac{1 + 2e^{-x}}{1 + x^{-3}} \to +\infty \times 1 = +\infty$.
  3. $(x^2+1)e^x = x^2 e^x + e^x \to 0 + 0 = 0$ by comparative growth at $-\infty$.

- **45.6:** $f(3) = \sqrt{9} = 3$. The limit is the derivative $f'(3)$. Since $f'(x) = \frac{2}{2\sqrt{2x+3}} = \frac{1}{\sqrt{2x+3}}$, we have $f'(3) = \frac{1}{3}$.

- **45.7:** $f(x) - (2x - 1) = \frac{3}{x^2+1} \to 0$ at $+\infty$, so $y = 2x - 1$ is an oblique asymptote. Since $x^2 + 1 > 0$, the difference is strictly positive: $\mathcal{C}_f$ is strictly above the asymptote.

- **45.8:**
  - $\lim_{x \to +\infty} (-1/x^2) = 0$, so $\lim \exp(-1/x^2) = e^0 = 1$.
  - $\lim_{x \to 0^+} (-1/x) = -\infty$, so $\lim_{X \to -\infty} e^X = 0$.

---

#### Solutions for Level ★★

- **45.9:**
  1. At $-\infty$, $(x - 2)e^x = x e^x - 2e^x \to 0 - 0 = 0$ by comparative growth. Since $\lim_{x \to -\infty} x = -\infty$, we have $\lim_{x \to -\infty} f(x) = -\infty$.
  2. $f(x) - x = (x - 2)e^x \to 0$ as $x \to -\infty$. Thus $(\Delta) : y = x$ is an oblique asymptote at $-\infty$.
  3. Sign of $f(x) - x = (x - 2)e^x$: since $e^x > 0$, the sign matches $x - 2$.
     On $]-\infty \,;\, 2[$, $\mathcal{C}_f$ is below $(\Delta)$.
     On $]2 \,;\, +\infty[$, $\mathcal{C}_f$ is above $(\Delta)$.
     At $x = 2$, the curve crosses its asymptote at $(2 ; 2)$.
  4. At $+\infty$, $x - 2 \to +\infty$ and $e^x \to +\infty$, so $(x-2)e^x \to +\infty$, whence $\lim f(x) = +\infty$.

- **45.10:**
  1. $\lim_{x \to +\infty} (x^2 - 2x + 3) = +\infty \implies \lim_{x \to +\infty} f(x) = +\infty$.
  2. For $x > 0$:
     $$f(x) - (x - 1) = \frac{(\sqrt{x^2 - 2x + 3} - (x - 1))(\sqrt{x^2 - 2x + 3} + (x - 1))}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{(x^2 - 2x + 3) - (x - 1)^2}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{x^2 - 2x + 3 - (x^2 - 2x + 1)}{\sqrt{x^2 - 2x + 3} + (x - 1)} = \frac{2}{\sqrt{x^2 - 2x + 3} + (x - 1)}.$$
  3. As $x \to +\infty$, the denominator tends to $+\infty$, so the quotient tends to 0. Thus $y = x - 1$ is an oblique asymptote at $+\infty$.

- **45.11:** As $x \to -\infty$, set $X = -x > 0$.
  $f(x) = \sqrt{X^2 + 2X + 3}$. The conjectured asymptote is $y = -x + 1 = X + 1$.
  $f(x) - (-x + 1) = \sqrt{X^2 + 2X + 3} - (X + 1) = \frac{(X^2 + 2X + 3) - (X + 1)^2}{\sqrt{X^2 + 2X + 3} + (X + 1)} = \frac{2}{\sqrt{X^2 + 2X + 3} + X + 1} \xrightarrow[X \to +\infty]{} 0$.
  Hence $y = -x + 1$ is indeed an oblique asymptote at $-\infty$.

- **45.12:**
  1. $N(0) = \frac{10}{1 + 9e^0} = \frac{10}{10} = 1$ thousand individuals (i.e., 1000 individuals).
  2. As $t \to +\infty$, $-0.5t \to -\infty$, so $e^{-0.5t} \to 0$.
     Thus $\lim_{t \to +\infty} N(t) = \frac{10}{1 + 0} = 10$ thousand (10,000 individuals).
     The habitat can support a maximum of 10,000 animals due to limited resources (food, space): this is the environmental carrying capacity.
  3. The horizontal asymptote has equation $y = 10$.

- **45.13:**
  1. $x^3 - 1 = (x - 1)(x^2 + x + 1)$ and $x^2 - 1 = (x - 1)(x + 1)$.
     For $x \neq 1$, $\frac{x^3 - 1}{x^2 - 1} = \frac{x^2 + x + 1}{x + 1} \xrightarrow[x \to 1]{} \frac{3}{2}$.
  2. $\frac{\sqrt{x} - 2}{x - 4} = \frac{\sqrt{x} - 2}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \xrightarrow[x \to 4]{} \frac{1}{4}$.
  3. Conjugate expression: $\frac{\sqrt{1+x} - 1}{x} = \frac{(1+x) - 1}{x(\sqrt{1+x} + 1)} = \frac{1}{\sqrt{1+x} + 1} \xrightarrow[x \to 0]{} \frac{1}{2}$. (Or difference quotient of $\sqrt{1+x}$ at 0).

- **45.14:**
  1. $ax + b + \frac{c}{x+1} = \frac{ax^2 + (a+b)x + b+c}{x+1}$.
     Identification: $a = 3$, $a+b = 5 \implies b = 2$, $b+c = -2 \implies c = -4$.
     Thus $f(x) = 3x + 2 - \frac{4}{x+1}$.
  2. Vertical asymptote: $x = -1$.
     Oblique asymptote: $y = 3x + 2$ (since $\lim_{x \to \pm\infty} \frac{-4}{x+1} = 0$).
  3. The vertical asymptote has $x = -1$. On the oblique asymptote, $y = 3(-1) + 2 = -1$. The intersection point is $I(-1 ; -1)$.

- **45.15:**
  1. $\frac{\pi x + 1}{2x - 3} = \frac{\pi + 1/x}{2 - 3/x} \to \frac{\pi}{2}$. By continuity of cosine: $\lim = \cos(\pi/2) = 0$.
  2. Setting $X = 1/x$, as $x \to +\infty$, $X \to 0^+$.
     The expression becomes $\frac{\sin X}{X}$, whose limit at 0 is $\sin'(0) = \cos(0) = 1$.

- **45.16:**
  1. For all real $x$, $-1 \leq \sin(x) \leq 1$. Adding $2x$: $2x - 1 \leq 2x + \sin(x) \leq 2x + 1$. Since $x > 1$, $x - 1 > 0$, divide without reversing inequalities.
  2. $\lim_{x \to +\infty} \frac{2x - 1}{x - 1} = 2$ and $\lim_{x \to +\infty} \frac{2x + 1}{x - 1} = 2$. By the squeeze theorem, $\lim f(x) = 2$.

- **45.17:**
  $f_m(x) = \frac{x^2(m + 4/x - 1/x^2)}{x^2(2 + 3/x^2)} = \frac{m + 4/x - 1/x^2}{2 + 3/x^2} \xrightarrow[x \to +\infty]{} \frac{m}{2}$.
  The limit is therefore $\frac{m}{2}$ for any value of $m \in \mathbb{R}$.

---

#### Solutions for Level ★★★

- **45.18:**
  1. Since $f(a) = g(a) = 0$, $\frac{f(x)}{g(x)} = \frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}$. Taking the quotient of difference quotient limits, since $g'(a) \neq 0$, the limit equals $\frac{f'(a)}{g'(a)}$.
  2. With $f(x) = e^{2x} - \cos(x)$ and $g(x) = x$, we have $f(0) = 1 - 1 = 0$ and $g(0) = 0$.
     $f'(x) = 2e^{2x} + \sin(x) \implies f'(0) = 2 + 0 = 2$.
     $g'(x) = 1 \implies g'(0) = 1$.
     The limit is $\frac{f'(0)}{g'(0)} = \frac{2}{1} = 2$.

- **45.19:**
  1. Polynomial long division of $x^3 + 2x^2 - 1$ by $x - 1$:
     $x^3 + 2x^2 - 1 = (x - 1)(x^2 + 3x + 3) + 2$.
     Thus $f(x) = x^2 + 3x + 3 + \frac{2}{x - 1}$. Here $P(x) = x^2 + 3x + 3$ and $R = 2$.
  2. $\lim_{x \to \pm\infty} [f(x) - P(x)] = \lim_{x \to \pm\infty} \frac{2}{x - 1} = 0$. The parabola with equation $y = x^2 + 3x + 3$ closely hugs the curve at infinity.

- **45.20:**
  1. $f(u_n) = \sin(2n\pi) = 0$.
     $f(v_n) = \sin(2n\pi + \pi/2) = \sin(\pi/2) = 1$.
  2. $\lim u_n = 0$ and $\lim v_n = 0$.
  3. If $f$ had a limit $L$ at 0, then for any sequence tending to 0, the images would have to tend to $L$. But $f(u_n) \to 0$ and $f(v_n) \to 1$. Since $0 \neq 1$, $f$ oscillates infinitely fast near 0 and has no limit at 0.

- **45.21:**
  1. $\frac{1}{n^n} \left(\frac{e^{x/n}}{x/n}\right)^n = \frac{1}{n^n} \frac{(e^{x/n})^n}{(x/n)^n} = \frac{e^x}{n^n \frac{x^n}{n^n}} = \frac{e^x}{x^n}$.
  2. Set $u = x/n$. As $x \to +\infty$, $u \to +\infty$.
     Since $\lim_{u \to +\infty} \frac{e^u}{u} = +\infty$, we have $\lim_{u \to +\infty} \left(\frac{e^u}{u}\right)^n = +\infty$.
     Multiplying by the strictly positive constant $\frac{1}{n^n}$, we conclude that $\lim_{x \to +\infty} \frac{e^x}{x^n} = +\infty$.

- **45.22:**
  1. $f(x)$ is the fractional part of $x$. It is a sawtooth wave, periodic with period 1, composed of line segments of slope 1 equal to 0 at $k$ and approaching 1 as $x \to k^-$.
  2. The function oscillates periodically between 0 and 1 as $x \to +\infty$, so it admits no limit at $+\infty$.
  3. Let $k \in \mathbb{Z}$. For $x \in [k \,;\, k+1[$, $\lfloor x \rfloor = k$, so $f(x) = x - k \xrightarrow[x \to k^+]{} 0$.
     For $x \in ]k-1 \,;\, k[$, $\lfloor x \rfloor = k-1$, so $f(x) = x - (k-1) \xrightarrow[x \to k^-]{} k - k + 1 = 1$.
     The right-hand limit is 0 and the left-hand limit is 1: the curve undergoes a jump of height 1 at each integer.

---

### The Question That Opens What Follows

We have just seen that some functions undergo sudden disruptions: vertical asymptotes where curves tear apart toward infinity, or staircase steps where curves jump abruptly from one elevation to another.
Yet most laws of nature — the trajectory of a tennis ball, the water level rising in a vase, the growth of a plant — know no such instantaneous leaps.
How can we express with the highest mathematical rigor the idea that a curve can be drawn **in a single stroke of the pen, without ever lifting the nib from the page**?
And why does this fundamental property guarantee that in crossing a river from one bank to the other, one is mathematically certain to pass through every intermediate current?

This is the essence of **continuity** and the prestigious **Intermediate Value Theorem (IVT)**. See you in Chapter 46.
