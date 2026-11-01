# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 50: The Barrel Filled with Slices of Water

> *“If the derivative is the scalpel that slices time into infinitesimal instants to extract instantaneous velocity, the integral is the golden needle that sews all the crumbs back together to reconstruct the grand journey of space. Nothing is lost, everything accumulates within the memory of the curve.”*

---

### What You Are About to Discover

- How astronomer **Johannes Kepler**, outraged by a wine merchant during his own wedding in 1615, invented the method of infinitely thin slices to measure curved volumes.
- The concept of the **definite integral** $\int_a^b f(t)\,dt$: from Riemann sums of approximating rectangles to the exact area under a curve.
- The historical origin and meaning of the elongated symbol $\int$, introduced by Gottfried Wilhelm Leibniz in 1675.
- The **Fundamental Theorem of Calculus** and its rigorous proof: how and why integration is the exact **inverse operation** of differentiation.
- Finding **antiderivatives**: standard tables and mastering composite patterns ($u'u^n$, $\dfrac{u'}{u}$, $u'e^u$, etc.).
- Essential algebraic and geometric properties of integrals: **linearity**, **Chasles' relation**, **positivity**, **area between two curves**, and the **mean value**.
- The cornerstone technique of integral calculus: **Integration by Parts** (IBP), derived directly from the product rule of differentiation.
- A clean **Python** implementation of the midpoint Riemann sum numerical approximation.

---

### 1. The Problem: Kepler, the Wine Merchant, and the Rigged Dipstick

#### 1.1 The Wedding in Linz (1615)

In the autumn of **1615**, in the city of Linz on the banks of the Danube, the renowned astronomer **Johannes Kepler**—the man who unlocked the laws of planetary motion around the Sun—was preparing the banquet for his second wedding. To feast his guests, he purchased several large barrels of Austrian wine.

When the vintner delivered the bulging wooden casks, he pulled a simple notched iron rod, called a **gauging rod** or dipstick, from his pocket. He inserted the rod diagonally through the bung-hole (the opening situated at the widest bulge of the barrel) all the way to the farthest seam of the opposite base, pulled out the wet rod, read the notch, and announced the volume in liters and the price to be paid.

Kepler was dumbfounded:
> *“How can you possibly measure the capacity of a curved, bulging body with a single diagonal straight line? If a cask has steeply swollen flanks or nearly straight cylindrical flanks, your rod plunges to the exact same depth, yet the volume of wine inside is completely different! You are selling me air, or you are robbing me blind!”*

The merchant merely shrugged: wine merchants had gauged casks this way for generations. Kepler retreated to his study. For weeks, he set aside his astronomical calculations to resolve the enigma of the casks.

His breakthrough, published in his landmark treatise *Nova Stereometria Doliorum Vinariorum* (“New Stereometry of Wine Casks”, 1615), was brilliant in its simplicity:
To measure a volume bounded by curved surfaces, **one must mentally slice it into an infinity of flat, infinitely thin circular disks**, calculate the volume of each disk (which is virtually a perfect flat cylinder), and then **add all these disks together** from the bottom to the top!

```
                  Cask sliced into thin disks:
          ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
         (    │   │   │   │   │   │   │   │    )
        (     │   │   │   │   │   │   │   │     )  Each slice is a flat circular disk
       (      │   │   │   │   │   │   │   │      ) of infinitesimal thickness dt
        (     │   │   │   │   │   │   │   │     )
         (    │   │   │   │   │   │   │   │    )
          └───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

#### 1.2 The Speedometer and the Broken Odometer

Consider a modern analogy.
Imagine you are driving an automobile across an open desert. Your odometer is broken: it permanently reads $0\text{ km}$. However, your speedometer functions flawlessly, and a continuous chart recorder plots your instantaneous speed $v(t)$ in kilometers per hour as time $t$ progresses.

How can you determine the exact total distance traveled between departure at time $t = a$ and arrival at time $t = b$?

1. **The Case of Constant Velocity:** If you cruise at a steady speed of $90\text{ km/h}$ for $2\text{ hours}$, the distance is:
   $$\text{Distance} = \text{Speed} \times \text{Time} = 90 \times 2 = 180\text{ kilometers}.$$
   Graphically, in a coordinate system where time is on the horizontal axis and speed on the vertical axis, this distance corresponds precisely to the **area of the rectangle** of base $[0\,; 2]$ and height $90$!

```
    Speed v(t)
        ▲
     90 ┼─────────────────────────┐
        │                         │   Area of rectangle
        │   Distance = 90 × 2     │   = 180 km
        │        = 180            │
      0 └─────────────────────────┴──────► Time t
        0                         2h
```

2. **The Case of Variable Velocity:** In real-world driving, velocity fluctuates constantly: accelerating, braking, idling. The curve $v(t)$ undulates.
   To calculate total distance, partition time into tiny intervals of duration $\Delta t$. During a split second $\Delta t$, the velocity $v(t)$ barely has time to change: it is practically constant.
   The small incremental distance covered during that slice is the area of a slender rectangle of width $\Delta t$ and height $v(t)$:
   $$\Delta d \approx v(t) \times \Delta t.$$
   The total distance traveled is the sum of these millions of tiny rectangles. And as the width $\Delta t$ shrinks to an infinitesimal increment (denoted $dt$), the sum of the rectangular areas converges to the **exact area under the velocity curve**!

---

### 2. From Riemann Sums to the Definite Integral

#### 2.1 Riemann Sums

Let $f$ be a continuous, positive function defined on a closed interval $[a\,; b]$ (with $a < b$).
We wish to compute the area of the planar region bounded by:
- The graph $\mathcal{C}_f$;
- The horizontal axis ($y = 0$);
- The vertical lines $x = a$ and $x = b$.

This geometric region is known as the **curvilinear trapezoid** or the area under the curve.

```
       y ▲                    Curve y = f(t)
         │                     ..---*---..
         │                   / | | | | | | \
         │                 /   | | | | | |   \   Each strip has
         │               /     | | | | | |     \ width Δt
         │             /       | | | | | |       \ and height f(t)
       0 └────────────┴────────┴─┴─┴─┴─┴─┴────────┴──────► t
                      a                           b
```

To approximate this area, divide the interval $[a\,; b]$ into $n$ equal sub-intervals of width $\Delta x = \dfrac{b - a}{n}$ using the subdivision points:
$$x_k = a + k \dfrac{b - a}{n} \quad (k = 0, 1, 2, \dots, n).$$

Over each sub-interval $[x_k\,; x_{k+1}]$, construct a rectangle of height $f(x_k)$ (the left Riemann sum).
The total area of these $n$ rectangles forms the **left Riemann sum**:
$$S_n = \sum_{k=0}^{n-1} f(x_k) \times \Delta x = \sum_{k=0}^{n-1} f\left(a + k\dfrac{b-a}{n}\right) \dfrac{b-a}{n}.$$

As the number of subdivisions $n$ tends to infinity ($n \to +\infty$), the width of each strip vanishes ($\Delta x \to 0$), the step-like staircase hugs the curve without leaving any gaps, and the sum $S_n$ converges to a unique real number: the **definite integral of $f$ from $a$ to $b$**.

#### 2.2 Leibniz's Notation: $\int_a^b f(t)\,dt$

> **🔍 True History — October 29, 1675 in Paris:**
> It was the German philosopher and polymath **Gottfried Wilhelm Leibniz** who introduced the integral sign $\int$.
> Leibniz pondered: *“What are we doing? We are computing the Sum of an infinity of infinitely slender slices.”*
> He took the first letter of the Latin word **Summa** (sum): the letter **S**.
> With his quill pen, he stretched it vertically into an elegant, elongated symbol: $\int$.
> And to denote the infinitely small width of each slice, he wrote $dt$ (the differential of $t$).

When you encounter the formula:
$$\int_a^b f(t) \, dt$$
here is what it communicates:
- $\int$: “Compute the continuous sum…”
- from lower bound $a$ (starting point) to upper bound $b$ (endpoint);
- of rectangles of height $f(t)$;
- and infinitesimal base width $dt$.

> **Note on Dummy Variables:**
> The variable $t$ beneath the integral sign is a **dummy variable**: it merely scans the interval from $a$ to $b$. It can be replaced by any other letter without altering the numerical value of the integral:
> $$\int_a^b f(t)\,dt = \int_a^b f(x)\,dx = \int_a^b f(u)\,du.$$

#### 2.3 Python Implementation: Midpoint Riemann Sums

Here is a clean Python script that approximates the definite integral of a continuous function using the midpoint rule:

```python
def rectangle_integral(f, a, b, n):
    """
    Computes an approximation of the definite integral of f from a to b
    using the midpoint Riemann sum method.
    """
    width = (b - a) / n
    total_sum = 0.0
    for k in range(n):
        # Midpoint of the k-th sub-interval
        x_mid = a + (k + 0.5) * width
        total_sum += f(x_mid)
    return total_sum * width

# Test on f(x) = x^2 from 0 to 3 (exact theoretical area is 9)
def square(x):
    return x**2

print("Approximation with 10 rectangles   :", rectangle_integral(square, 0, 3, 10))
print("Approximation with 100 rectangles  :", rectangle_integral(square, 0, 3, 100))
print("Approximation with 1000 rectangles :", rectangle_integral(square, 0, 3, 1000))
# With 1000 rectangles, we obtain 8.9999988... virtually 9!
```

---

### 3. The Fundamental Theorem of Calculus: The Miraculous Bridge

Computing sums of millions of rectangles by hand would be an agonizing, impossible task. Here enters what is widely considered the crown jewel of mathematical analysis, discovered independently by **Isaac Newton** and **Gottfried Wilhelm Leibniz** between 1666 and 1675.

#### 3.1 The Area Accumulation Function

Let $f$ be a continuous, positive function on $[a\,; b]$.
Hold the lower limit $a$ fixed, and let the upper limit vary as a free variable $x \in [a\,; b]$.
Define the **area accumulation function** $A$:
$$A(x) = \int_a^x f(t) \, dt.$$

$A(x)$ measures the **accumulated area swept under the curve from $a$ to $x$**.
What is the rate of change of this accumulated area when the upper boundary advances by a tiny increment $h > 0$?

```
       y ▲                        y = f(t)
         │                        ..---*---..
         │                      /      |   | \
         │                    /        | h |   \   Added strip of width h:
         │                  /          |   |     \ area is A(x+h) - A(x) ≈ f(x) × h!
         │                /   Area     |   |       \
       0 └───────────────┴──── A(x) ───┴───┴────────┴──────► t
                         a             x  x+h        b
```

When moving from $x$ to $x+h$, the total area increases by the slender strip spanning from $x$ to $x+h$:
$$\Delta A = A(x+h) - A(x) = \int_x^{x+h} f(t) \, dt.$$
This strip has base width $h$ and a nearly constant height equal to $f(x)$ (since $f$ is continuous).
Its area is therefore approximately:
$$A(x+h) - A(x) \approx f(x) \times h \iff \dfrac{A(x+h) - A(x)}{h} \approx f(x).$$
As $h \to 0$, the difference quotient of the area function becomes **precisely the height of the curve $f(x)$**!

> **The derivative of the accumulation function is the original function itself:**
> $$A'(x) = f(x).$$

#### 3.2 Rigorous Proof of the Fundamental Theorem of Calculus

> **📐 Fundamental Theorem of Calculus (Required Curriculum Proof) —**
> Let $f$ be a continuous function on an interval $I$, and let $a \in I$.
> The function $A$ defined on $I$ by:
> $$A(x) = \int_a^x f(t) \, dt$$
> is differentiable on $I$, and for every $x \in I$:
> $$A'(x) = f(x).$$

> **✍️ Proof —**
> Let $x \in I$ and let $h > 0$ such that $x + h \in I$.
> By Chasles' relation for integrals:
> $$A(x+h) - A(x) = \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt = \int_x^{x+h} f(t)\,dt.$$
> Because $f$ is continuous on the closed interval $[x\,; x+h]$, the Extreme Value Theorem guarantees that $f$ attains an absolute minimum $m_h$ and an absolute maximum $M_h$ on $[x\,; x+h]$:
> $$\text{For all } t \in [x\,; x+h] : \quad m_h \leq f(t) \leq M_h.$$
> Integrating this bounding across the interval $[x\,; x+h]$ of length $h$:
> $$\int_x^{x+h} m_h \, dt \leq \int_x^{x+h} f(t) \, dt \leq \int_x^{x+h} M_h \, dt \iff m_h \times h \leq A(x+h) - A(x) \leq M_h \times h.$$
> Dividing by $h > 0$:
> $$m_h \leq \dfrac{A(x+h) - A(x)}{h} \leq M_h.$$
> Because $f$ is continuous at $x$, as $h \to 0^+$, the interval $[x\,; x+h]$ collapses down to the single point $x$.
> The minimum $m_h$ and maximum $M_h$ both converge to $f(x)$:
> $$\lim_{h \to 0^+} m_h = f(x) \quad \text{and} \quad \lim_{h \to 0^+} M_h = f(x).$$
> By the **Squeeze Theorem**:
> $$\lim_{h \to 0^+} \dfrac{A(x+h) - A(x)}{h} = f(x).$$
> An identical argument for $h < 0$ yields $\lim\limits_{h \to 0^-} \dfrac{A(x+h) - A(x)}{h} = f(x)$.
> We conclude that $A$ is differentiable at $x$ and $A'(x) = f(x)$. $\blacksquare$

---

### 4. Antiderivatives and the Evaluation of Definite Integrals

#### 4.1 What Is an Antiderivative?

> **📐 Definition —**
> Let $f$ be a continuous function on an interval $I$.
> An **antiderivative** (or primitive) of $f$ on $I$ is any function $F$ differentiable on $I$ such that:
> $$\text{For all } x \in I : \quad F'(x) = f(x).$$

> **Fundamental Properties of Antiderivatives —**
> If $F$ is an antiderivative of $f$ on an interval $I$, then:
> 1. For any real constant $C$, the function $x \mapsto F(x) + C$ is also an antiderivative of $f$ (since the derivative of a constant is zero: $(F+C)' = F' + 0 = f$).
> 2. Conversely, any other antiderivative $G$ of $f$ on $I$ differs from $F$ by only a constant: there exists $C \in \mathbb{R}$ such that $G(x) = F(x) + C$.
> 3. For any initial condition $(x_0\,; y_0)$ with $x_0 \in I$, there exists **a unique** antiderivative of $f$ satisfying $F(x_0) = y_0$.

#### 4.2 The Evaluation Formula for Definite Integrals

Thanks to the Fundamental Theorem, evaluating a definite integral requires no rectangles whatsoever:

> **📐 Theorem (Evaluating Integrals via Antiderivatives) —**
> Let $f$ be a continuous function on $[a\,; b]$, and let $F$ be any antiderivative of $f$ on $[a\,; b]$. Then:
> $$\int_a^b f(t) \, dt = [F(t)]_a^b = F(b) - F(a).$$

> **✍️ Proof —**
> Define $A(x) = \int_a^x f(t)\,dt$. By the Fundamental Theorem, $A$ is an antiderivative of $f$ on $[a\,; b]$.
> Since $F$ is another antiderivative of $f$, there exists a constant $C \in \mathbb{R}$ such that for all $x \in [a\,; b]$:
> $$A(x) = F(x) + C.$$
> Evaluate at $x = a$:
> $$A(a) = \int_a^a f(t)\,dt = 0 \implies F(a) + C = 0 \iff C = -F(a).$$
> Thus, for all $x \in [a\,; b]$:
> $$A(x) = F(x) - F(a).$$
> Setting $x = b$ yields immediately:
> $$\int_a^b f(t)\,dt = A(b) = F(b) - F(a).$$
> Notice that if we had chosen any other antiderivative $G(x) = F(x) + K$, the constant $K$ cancels upon subtraction:
> $$G(b) - G(a) = (F(b) + K) - (F(a) + K) = F(b) - F(a).$$
> The evaluation is entirely independent of the arbitrary constant chosen! $\blacksquare$

#### 4.3 Table of Standard Antiderivatives

This table is the exact mirror image of the derivative table, read in reverse:

| Function $f(x)$ | An Antiderivative $F(x)$ | Validity Domain |
|---|---|---|
| $0$ | $k$ (constant) | $\mathbb{R}$ |
| $a$ (constant) | $ax$ | $\mathbb{R}$ |
| $x$ | $\dfrac{x^2}{2}$ | $\mathbb{R}$ |
| $x^n \quad (n \in \mathbb{N})$ | $\dfrac{x^{n+1}}{n+1}$ | $\mathbb{R}$ |
| $x^\alpha \quad (\alpha \in \mathbb{R}, \alpha \neq -1)$ | $\dfrac{x^{\alpha+1}}{\alpha+1}$ | $]0\,; +\infty[$ |
| $\dfrac{1}{x^2} = x^{-2}$ | $-\dfrac{1}{x}$ | $]-\infty\,; 0[$ or $]0\,; +\infty[$ |
| $\dfrac{1}{\sqrt{x}} = x^{-1/2}$ | $2\sqrt{x}$ | $]0\,; +\infty[$ |
| $\dfrac{1}{x}$ | $\ln|x|$ | $]-\infty\,; 0[$ or $]0\,; +\infty[$ |
| $e^x$ | $e^x$ | $\mathbb{R}$ |
| $e^{kx} \quad (k \neq 0)$ | $\dfrac{1}{k} e^{kx}$ | $\mathbb{R}$ |
| $\cos x$ | $\sin x$ | $\mathbb{R}$ |
| $\sin x$ | $-\cos x$ | $\mathbb{R}$ |

#### 4.4 Antiderivatives of Composite Functions

Recognizing the chain rule in reverse is the core operational skill of integral calculus:

| Pattern in Integrand | An Antiderivative | Condition on $u$ |
|---|---|---|
| $u'(x) \times \big(u(x)\big)^n \quad (n \in \mathbb{Z}, n \neq -1)$ | $\dfrac{\big(u(x)\big)^{n+1}}{n+1}$ | If $n < -1$, $u(x) \neq 0$ |
| $\dfrac{u'(x)}{u(x)}$ | $\ln|u(x)|$ | $u(x) \neq 0$ |
| $u'(x) \, e^{u(x)}$ | $e^{u(x)}$ | None |
| $\dfrac{u'(x)}{\sqrt{u(x)}}$ | $2\sqrt{u(x)}$ | $u(x) > 0$ |
| $u'(x) \cos(u(x))$ | $\sin(u(x))$ | None |
| $u'(x) \sin(u(x))$ | $-\cos(u(x))$ | None |

> **Worked Example 1 — Direct Antiderivatives.**
> 1. $f_1(x) = 3x^4 - 2x^2 + 5 \implies F_1(x) = 3\left(\dfrac{x^5}{5}\right) - 2\left(\dfrac{x^3}{3}\right) + 5x = \dfrac{3}{5}x^5 - \dfrac{2}{3}x^3 + 5x$.
> 2. $f_2(x) = \dfrac{3}{x} + e^{-2x}$ on $]0\,;+\infty[ \implies F_2(x) = 3\ln x - \dfrac{1}{2}e^{-2x}$.

> **Worked Example 2 — Recognizing Composite Patterns.**
> 1. $f(x) = (2x + 1)(x^2 + x + 4)^3$.
>    Let $u(x) = x^2 + x + 4$. Then $u'(x) = 2x + 1$.
>    The expression is formatted as $u' u^3$.
>    An antiderivative is:
>    $$F(x) = \dfrac{u^4}{4} = \dfrac{(x^2 + x + 4)^4}{4}.$$
>
> 2. $g(x) = \dfrac{2x}{x^2 + 3}$.
>    Let $u(x) = x^2 + 3$. Then $u'(x) = 2x$.
>    This is of the form $\dfrac{u'}{u}$ with $u(x) > 0$.
>    An antiderivative is $G(x) = \ln(x^2 + 3)$.
>
> 3. $h(x) = \dfrac{x}{x^2 + 1}$.
>    The derivative of $x^2 + 1$ is $2x$, but the numerator contains only $x$.
>    Insert the required constant 2 by multiplying and dividing by 2:
>    $$h(x) = \dfrac{1}{2} \times \dfrac{2x}{x^2 + 1} = \dfrac{1}{2} \dfrac{u'}{u} \implies H(x) = \dfrac{1}{2} \ln(x^2 + 1).$$
>
> 4. $k(x) = x e^{-x^2}$.
>    The derivative of $-x^2$ is $-2x$. Adjust the constant:
>    $$k(x) = -\dfrac{1}{2} \times (-2x) e^{-x^2} = -\dfrac{1}{2} u' e^u \implies K(x) = -\dfrac{1}{2} e^{-x^2}.$$

---

### 5. Algebraic Properties of the Definite Integral

These structural properties hold for any continuous functions on the specified intervals.

#### 5.1 Linearity

> **📐 Linearity Property —** For all constants $\alpha, \beta \in \mathbb{R}$ and continuous functions $f, g$:
> $$\int_a^b \big(\alpha f(t) + \beta g(t)\big) \, dt = \alpha \int_a^b f(t) \, dt + \beta \int_a^b g(t) \, dt.$$

#### 5.2 Chasles' Relation

> **📐 Chasles' Relation —** For all real numbers $a, b, c$ belonging to an interval where $f$ is continuous:
> $$\int_a^c f(t) \, dt + \int_c^b f(t) \, dt = \int_a^b f(t) \, dt.$$
> In particular:
> - $\int_a^a f(t) \, dt = 0$ (a region with zero width has zero area);
> - $\int_b^a f(t) \, dt = -\int_a^b f(t) \, dt$ (reversing the integration limits flips the sign).

#### 5.3 Positivity and Order Preservation

> **📐 Positivity —** Let $a \leq b$.
> - If for all $t \in [a\,; b]$, $f(t) \geq 0$, then $\int_a^b f(t) \, dt \geq 0$.
> - If for all $t \in [a\,; b]$, $f(t) \leq g(t)$, then $\int_a^b f(t) \, dt \leq \int_a^b g(t) \, dt$.
> - Triangle inequality for integrals: $\left| \int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)| \, dt$.

> **⚠️ Common Pitfall! — Order of Limits Matters!**
> The rule “$f \geq 0 \implies \int_a^b f(t)\,dt \geq 0$” strictly assumes **$a \leq b$**.
> If the integration limits are reversed ($a > b$), the integral of a strictly positive function is **negative**!

#### 5.4 Area Enclosed Between Two Curves

Let $f$ and $g$ be two continuous functions on $[a\,; b]$ such that for all $x \in [a\,; b]$, **$f(x) \geq g(x)$** (the graph of $f$ lies on or above that of $g$).
The area $\mathcal{A}$ of the region bounded by both curves and the vertical lines $x = a$ and $x = b$ is the area under $f$ minus the area under $g$:

$$\mathcal{A} = \int_a^b \big(f(x) - g(x)\big) \, dx.$$

```
       y ▲               ..---*---.. y = f(x) (upper curve)
         │             / : : : : : : \
         │           / : : Area  : : : \
         │          ( : : :  A  : : : : )
         │           \ : : : : : : : : /
         │             '--.......---'   y = g(x) (lower curve)
       0 └───────────┴─────────────────┴──────► x
                     a                 b
```

#### 5.5 The Mean Value of a Function

How can one define the average temperature of a day if temperature $T(t)$ fluctuates continuously from hour to hour? One cannot simply sum an infinity of readings and divide by infinity!
We use the **integral mean value**:

> **📐 Definition — Mean Value:**
> Let $f$ be continuous on $[a\,; b]$ with $a < b$.
> The **mean value** (or average value) of $f$ on $[a\,; b]$, denoted $\mu$ (or $\overline{f}$), is the real number:
> $$\mu = \dfrac{1}{b - a} \int_a^b f(t) \, dt.$$

**Geometric Interpretation:** $\mu$ is the height of a rectangle sharing the same base $[a\,; b]$ that encloses **the exact same area** as the undulating region beneath the graph of $f$:
$$\text{Area}(f) = \mu \times (b - a).$$

---

### 6. Integration by Parts (IBP): The Master Technique

When an integrand is a product of two distinct families of functions (such as $x e^x$ or $x \cos x$), and cannot be recognized as a composite pattern $u' e^u$, no elementary antiderivative formula applies directly.
We turn to **Integration by Parts**, which is the integral counterpart of the product rule for differentiation.

#### 6.1 Theorem and Proof

> **📐 Integration by Parts Theorem (Required Curriculum Proof) —**
> Let $u$ and $v$ be differentiable functions on $[a\,; b]$ whose derivatives $u'$ and $v'$ are continuous on $[a\,; b]$. Then:
> $$\int_a^b u'(t) v(t) \, dt = \Big[ u(t) v(t) \Big]_a^b - \int_a^b u(t) v'(t) \, dt.$$

> **✍️ Proof —**
> From the product rule of differentiation, for all $t \in [a\,; b]$:
> $$(uv)'(t) = u'(t) v(t) + u(t) v'(t).$$
> Isolating $u'(t) v(t)$:
> $$u'(t) v(t) = (uv)'(t) - u(t) v'(t).$$
> Integrating both sides from $a$ to $b$ using linearity:
> $$\int_a^b u'(t) v(t) \, dt = \int_a^b (uv)'(t) \, dt - \int_a^b u(t) v'(t) \, dt.$$
> An antiderivative of $(uv)'$ is simply the product $uv$!
> Hence:
> $$\int_a^b (uv)'(t) \, dt = \Big[ u(t) v(t) \Big]_a^b = u(b)v(b) - u(a)v(a).$$
> Substituting this back yields the required formula:
> $$\int_a^b u'(t) v(t) \, dt = \Big[ u(t) v(t) \Big]_a^b - \int_a^b u(t) v'(t) \, dt. \quad \blacksquare$$

#### 6.2 Strategy: Choosing $u'$ and $v$

The goal of integration by parts is to trade an intractable integral for a **simpler** one.
Generally, we assign **$v(t)$** to be the factor that **simplifies upon differentiation** (polynomials lose a degree when differentiated!).

> **🧭 The LIATE / ALPES Heuristic for Choosing $v(x)$ (the factor to differentiate):**
> Choose $v(x)$ to be whichever function type appears highest on this list:
> 1. **L** : **Logarithms** ($\ln x$)
> 2. **I** : **Inverse trigonometric functions** ($\arctan x$, etc.)
> 3. **A** : **Algebraic / Polynomials** ($x, x^2, x^3, \dots$)
> 4. **T** : **Trigonometric functions** ($\sin x, \cos x$)
> 5. **E** : **Exponentials** ($e^x, e^{2x}, \dots$)

> **Worked Example 3 — Evaluating $\int_0^1 x e^x \, dx$.**
> We have the product of a polynomial $x$ and an exponential $e^x$.
> According to the LIATE rule, the polynomial $x$ takes precedence over the exponential for differentiation:
> - Set $v(x) = x \implies v'(x) = 1$ (the polynomial degree drops!)
> - Set $u'(x) = e^x \implies u(x) = e^x$
>
> Both $u$ and $v$ are continuously differentiable on $[0\,; 1]$.
> Integrating by parts:
> $$\int_0^1 x e^x \, dx = \Big[ x e^x \Big]_0^1 - \int_0^1 1 \times e^x \, dx.$$
> Evaluating the boundary bracket: $[x e^x]_0^1 = 1 e^1 - 0 e^0 = e$.
> The remaining integral is trivial: $\int_0^1 e^x \, dx = [e^x]_0^1 = e^1 - e^0 = e - 1$.
> Therefore:
> $$\int_0^1 x e^x \, dx = e - (e - 1) = \mathbf{1}.$$

> **Worked Example 4 — The Clever Trick to Integrate $\ln x$.**
> How do we find an antiderivative of $\ln x$ on $]0\,; +\infty[$?
> There is no obvious product? Write it as $\ln x = 1 \times \ln x$!
> Set:
> - $v(x) = \ln x \implies v'(x) = \dfrac{1}{x}$ (the logarithm vanishes!)
> - $u'(x) = 1 \implies u(x) = x$
>
> Then:
> $$\int \ln x \, dx = x \ln x - \int x \times \dfrac{1}{x} \, dx = x \ln x - \int 1 \, dx = x \ln x - x + C.$$
>
> > **Memorable Formula — An antiderivative of $\ln x$ is:**
> > $$F(x) = x \ln x - x.$$
> Immediate verification by differentiation:
> $(x \ln x - x)' = 1 \times \ln x + x \times \dfrac{1}{x} - 1 = \ln x + 1 - 1 = \ln x$. Impeccable! ✔

---

### Key Takeaways

#### 1. The Definite Integral
- $\int_a^b f(t)\,dt$ represents the signed algebraic area enclosed between the graph of $f$, the horizontal axis, and the vertical lines $x = a$ and $x = b$.
- The unit of area (u.a.) is the area of the unit coordinate cell $\|\vec{i}\| \times \|\vec{j}\|$.

#### 2. The Fundamental Theorem of Calculus
- If $f$ is continuous on $I$ and $a \in I$, the function $A(x) = \int_a^x f(t)\,dt$ is differentiable on $I$ and **$A'(x) = f(x)$**.
- For any antiderivative $F$ of $f$ on $[a\,; b]$:
  $$\int_a^b f(t) \, dt = [F(t)]_a^b = F(b) - F(a).$$

#### 3. Standard Antiderivatives Summary
- $x^n \to \dfrac{x^{n+1}}{n+1} \quad (n \neq -1)$
- $\dfrac{1}{x} \to \ln|x|$
- $e^{ax} \to \dfrac{1}{a} e^{ax}$
- $\cos(ax) \to \dfrac{1}{a} \sin(ax)$ and $\sin(ax) \to -\dfrac{1}{a} \cos(ax)$
- $u' u^n \to \dfrac{u^{n+1}}{n+1}$
- $\dfrac{u'}{u} \to \ln|u|$
- $u' e^u \to e^u$

#### 4. Key Properties
- Linearity: $\int (\alpha f + \beta g) = \alpha \int f + \beta \int g$.
- Chasles' relation: $\int_a^c f + \int_c^b f = \int_a^b f$.
- Positivity: if $a \leq b$ and $f \geq 0$, then $\int_a^b f \geq 0$.
- Area between curves: $\mathcal{A} = \int_a^b (f(x) - g(x))\,dx$ whenever $f \geq g$.
- Mean value: $\mu = \dfrac{1}{b - a} \int_a^b f(t)\,dt$.

#### 5. Integration by Parts
$$\int_a^b u' v = [uv]_a^b - \int_a^b u v'.$$

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 50.1 —** Elementary Antiderivatives.
Determine an antiderivative for each of the following functions on the indicated domain:
1. $f_1(x) = 4x^3 - 6x^2 + 2x - 7$ on $\mathbb{R}$
2. $f_2(x) = \dfrac{5}{x^2} - \dfrac{2}{\sqrt{x}}$ on $]0\,;+\infty[$
3. $f_3(x) = e^{3x} - 2e^{-x}$ on $\mathbb{R}$
4. $f_4(x) = 3\cos(2x) + \sin(4x)$ on $\mathbb{R}$
5. $f_5(x) = \dfrac{4}{x}$ on $]0\,;+\infty[$

**Exercise 50.2 —** Antiderivatives Satisfying Initial Conditions.
1. Find the antiderivative $F$ of $f(x) = 3x^2 - 4x + 1$ such that $F(1) = 5$.
2. Find the antiderivative $G$ of $g(x) = e^{2x}$ such that $G(0) = 2$.

**Exercise 50.3 —** Direct Definite Integrals.
Evaluate the exact values of the following definite integrals:
1. $I_1 = \int_1^3 (3x^2 - 2x + 1) \, dx$
2. $I_2 = \int_0^2 e^{3x} \, dx$
3. $I_3 = \int_1^e \dfrac{1}{x} \, dx$
4. $I_4 = \int_0^{\pi/2} \cos x \, dx$
5. $I_5 = \int_0^1 (2x + 1)^3 \, dx$

**Exercise 50.4 —** Recognizing Composite Patterns $u'u^n$ and $u'e^u$.
Compute the following integrals:
1. $J_1 = \int_0^1 2x(x^2 + 1)^4 \, dx$
2. $J_2 = \int_0^2 3x^2 e^{x^3} \, dx$
3. $J_3 = \int_1^2 \dfrac{2x + 3}{x^2 + 3x + 1} \, dx$
4. $J_4 = \int_0^{\pi/4} \cos x \sin^3 x \, dx$

**Exercise 50.5 —** Chasles' Relation and Symmetry.
Let $f$ be continuous on $[-a\,; a]$ with $a > 0$.
1. Recall why $\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$ if $f$ is even.
2. Recall why $\int_{-a}^a f(x)\,dx = 0$ if $f$ is odd.
3. Deduce instantaneously without any antiderivative computation the value of:
   $$K = \int_{-2}^2 (x^7 - 3x^3 + \sin x) \, dx.$$

**Exercise 50.6 —** Mean Value.
Compute the mean value of $f(x) = x^2$ on the interval $[0\,; 3]$. Interpret geometrically.

**Exercise 50.7 —** Simple Geometric Area.
Compute the area of the region bounded by the parabola $y = 4 - x^2$ and the horizontal axis.

---

#### Level ★★ (Exploration and Exam Preparation)

**Exercise 50.8 —** Basic Integration by Parts.
Evaluate using integration by parts:
1. $A_1 = \int_0^{\pi} x \sin x \, dx$
2. $A_2 = \int_1^e x \ln x \, dx$
3. $A_3 = \int_0^1 (2x + 1) e^{-x} \, dx$

**Exercise 50.9 —** Repeated Integration by Parts.
Evaluate $B = \int_0^1 x^2 e^x \, dx$ using two successive integrations by parts.

**Exercise 50.10 —** Area Enclosed Between Two Curves.
Consider the two parabolas:
$$y = f(x) = -x^2 + 4x \quad \text{and} \quad y = g(x) = x^2 - 2x.$$
1. Determine the coordinates of their intersection points.
2. Determine their relative positions on the interval bounded by these intersections.
3. Compute the area of the closed region bounded by these curves.

**Exercise 50.11 —** Functions Defined by Integrals.
Let $F$ be defined on $]0\,;+\infty[$ by:
$$F(x) = \int_1^x \dfrac{e^t}{t} \, dt.$$
1. Determine $F(1)$.
2. Justify why $F$ is differentiable on $]0\,;+\infty[$ and find $F'(x)$.
3. Deduce the monotonicity of $F$ on $]0\,;+\infty[$.
4. Prove that for all $t \geq 1$, $\dfrac{e^t}{t} \geq e$. Deduce that for all $x \geq 1$:
   $$F(x) \geq e(x - 1).$$
5. Find the limit of $F(x)$ as $x \to +\infty$.

**Exercise 50.12 —** Sequence of Integrals (Exam Style).
For every integer $n \in \mathbb{N}$, define:
$$I_n = \int_0^1 x^n e^{-x} \, dx.$$
1. Calculate $I_0$.
2. Using integration by parts, establish for all $n \in \mathbb{N}$ the recurrence relation:
   $$I_{n+1} = (n + 1) I_n - \dfrac{1}{e}.$$
3. Deduce the exact values of $I_1$ and $I_2$.
4. Prove that for all $n \in \mathbb{N}$, $I_n \geq 0$.
5. Show that the sequence $(I_n)$ is decreasing.
6. Prove that for all $x \in [0\,; 1]$, $x^n e^{-1} \leq x^n e^{-x} \leq x^n$. Deduce bounds for $I_n$ and compute $\lim\limits_{n \to +\infty} I_n$.

**Exercise 50.13 —** Kepler's Wine Cask Revisited.
A barrel of length $2L = 1\text{ meter}$ (from $x = -0.5$ to $x = 0.5$) is modeled by revolving a parabolic arc around the horizontal axis.
The radius of the cask at horizontal position $x$ is given by:
$$R(x) = R_0 - k x^2$$
with $R_0 = 0.4\text{ m}$ (radius at the center / bung-hole) and $R(0.5) = 0.3\text{ m}$ at the ends.
1. Determine the constant $k$.
2. Recall that the volume of a circular slice of thickness $dx$ is $dV = \pi [R(x)]^2 \, dx$.
3. Express the total volume of the cask as a definite integral:
   $$V = \int_{-0.5}^{0.5} \pi [R(x)]^2 \, dx.$$
4. Evaluate this volume in liters. Compare it to a straight cylinder sharing the same average radius.

**Exercise 50.14 —** Partial Fraction Decomposition.
Let $f(x) = \dfrac{1}{x^2 - 1}$ defined on $]1\,;+\infty[$.
1. Find constants $a$ and $b$ such that for all $x > 1$:
   $$\dfrac{1}{x^2 - 1} = \dfrac{a}{x - 1} + \dfrac{b}{x + 1}.$$
2. Deduce an antiderivative of $f$ on $]1\,;+\infty[$.
3. Compute the integral $I = \int_2^3 \dfrac{1}{x^2 - 1} \, dx$.

**Exercise 50.15 —** Bounding and Rocket Flight.
A rocket is launched vertically. Its acceleration is modeled by $a(t) = \dfrac{400}{(t + 10)^2}$ for $t \in [0\,; 30]$ (in $\text{m}\cdot\text{s}^{-2}$).
At launch ($t = 0$), initial velocity is $v(0) = 0$.
1. Express velocity $v(t)$ by integrating acceleration.
2. Determine the velocity attained at $t = 30\text{ seconds}$.
3. Express altitude $h(t)$ by integrating velocity. Find the altitude at $t = 30\text{ s}$.

**Exercise 50.16 —** The Cauchy-Schwarz Inequality for Integrals.
Let $f$ and $g$ be continuous on $[a\,; b]$.
1. For any real parameter $\lambda$, expand $\int_a^b \big(f(t) + \lambda g(t)\big)^2 \, dt \geq 0$.
2. Viewing this as a quadratic in $\lambda$, deduce the **Cauchy-Schwarz inequality**:
   $$\left( \int_a^b f(t) g(t) \, dt \right)^2 \leq \left( \int_a^b (f(t))^2 \, dt \right) \left( \int_a^b (g(t))^2 \, dt \right).$$

---

#### Level ★★★ (In-Depth Challenges)

**Exercise 50.17 —** The Wallis Integrals.
For every natural number $n$, define:
$$W_n = \int_0^{\pi/2} \sin^n x \, dx.$$
1. Calculate $W_0$ and $W_1$.
2. Writing $\sin^{n+1} x = \sin x \times \sin^n x$, establish by integration by parts for $n \geq 1$:
   $$W_{n+1} = \dfrac{n}{n+1} W_{n-1}.$$
3. Deduce expressions for $W_{2p}$ and $W_{2p+1}$ in terms of factorials.
4. Show that $(W_n)$ is strictly positive and decreasing.
5. Prove that $\lim\limits_{n \to +\infty} \dfrac{W_{n+1}}{W_n} = 1$, and deduce **John Wallis' celebrated infinite product (1655)** for $\pi$:
   $$\dfrac{\pi}{2} = \lim_{p \to +\infty} \prod_{k=1}^p \dfrac{4k^2}{4k^2 - 1} = \dfrac{2}{1} \times \dfrac{2}{3} \times \dfrac{4}{3} \times \dfrac{4}{5} \times \dfrac{6}{5} \times \dfrac{6}{7} \times \dots$$

**Exercise 50.18 —** The Gaussian Integral.
Let $I = \int_0^{+\infty} e^{-x^2} \, dx$.
1. Justify the convergence of this improper integral by comparing it to $e^{-x}$ for $x \geq 1$.
2. Assuming $I^2 = \int_0^{+\infty} \int_0^{+\infty} e^{-(x^2+y^2)} \, dx \, dy$, convert to polar coordinates ($x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$) to show:
   $$I^2 = \int_0^{\pi/2} d\theta \times \int_0^{+\infty} r e^{-r^2} \, dr.$$
3. Evaluate this integral directly and deduce:
   $$\int_{-\infty}^{+\infty} e^{-x^2} \, dx = \sqrt{\pi}.$$

**Exercise 50.19 —** The Euler-Maclaurin Sum Formula.
Let $f$ be continuously differentiable ($C^1$) on $[0\,; n]$.
1. Prove that $\int_0^1 (t - 1/2) f'(t) \, dt = \dfrac{f(0) + f(1)}{2} - \int_0^1 f(t) \, dt$.
2. Generalize this to connect the discrete sum $\sum_{k=0}^n f(k)$ to the integral $\int_0^n f(t)\,dt$.

**Exercise 50.20 —** The Mean Value Theorem for Integrals.
Let $f$ be continuous on $[a\,; b]$. Prove that there exists $c \in \; ]a\,; b[$ such that:
$$\int_a^b f(t) \, dt = f(c)(b - a).$$
*(This is the Integral Mean Value Theorem, the integral counterpart of the Mean Value Theorem applied to an antiderivative).*

---

### Solutions

#### Level ★ Solutions

**Solution 50.1:**
1. $F_1(x) = 4\left(\dfrac{x^4}{4}\right) - 6\left(\dfrac{x^3}{3}\right) + 2\left(\dfrac{x^2}{2}\right) - 7x = x^4 - 2x^3 + x^2 - 7x$.
2. $f_2(x) = 5x^{-2} - 2x^{-1/2} \implies F_2(x) = 5\left(-\dfrac{1}{x}\right) - 2(2\sqrt{x}) = -\dfrac{5}{x} - 4\sqrt{x}$.
3. $F_3(x) = \dfrac{1}{3}e^{3x} + 2e^{-x}$.
4. $F_4(x) = 3\left(\dfrac{1}{2}\sin(2x)\right) - \dfrac{1}{4}\cos(4x) = \dfrac{3}{2}\sin(2x) - \dfrac{1}{4}\cos(4x)$.
5. $F_5(x) = 4\ln x$.

**Solution 50.2:**
1. General antiderivatives: $F(x) = x^3 - 2x^2 + x + C$.
   Condition: $F(1) = 1 - 2 + 1 + C = C = 5$. Thus $F(x) = x^3 - 2x^2 + x + 5$.
2. General antiderivatives: $G(x) = \dfrac{1}{2}e^{2x} + C$.
   Condition: $G(0) = \dfrac{1}{2} + C = 2 \implies C = \dfrac{3}{2}$. Thus $G(x) = \dfrac{1}{2}e^{2x} + \dfrac{3}{2}$.

**Solution 50.3:**
1. $I_1 = [x^3 - x^2 + x]_1^3 = (27 - 9 + 3) - (1 - 1 + 1) = 21 - 1 = 20$.
2. $I_2 = \left[ \dfrac{1}{3}e^{3x} \right]_0^2 = \dfrac{1}{3}e^6 - \dfrac{1}{3}e^0 = \dfrac{e^6 - 1}{3}$.
3. $I_3 = [\ln x]_1^e = \ln e - \ln 1 = 1 - 0 = 1$.
4. $I_4 = [\sin x]_0^{\pi/2} = \sin(\pi/2) - \sin 0 = 1 - 0 = 1$.
5. Let $u = 2x+1 \implies u' = 2$. $I_5 = \dfrac{1}{2} \int_0^1 2(2x+1)^3 \, dx = \dfrac{1}{2} \left[ \dfrac{(2x+1)^4}{4} \right]_0^1 = \dfrac{1}{8}(3^4 - 1^4) = \dfrac{80}{8} = 10$.

**Solution 50.4:**
1. Pattern $u' u^4$ with $u(x) = x^2 + 1$: $J_1 = \left[ \dfrac{(x^2+1)^5}{5} \right]_0^1 = \dfrac{2^5}{5} - \dfrac{1^5}{5} = \dfrac{31}{5}$.
2. Pattern $u' e^u$ with $u(x) = x^3$: $J_2 = [e^{x^3}]_0^2 = e^{2^3} - e^0 = e^8 - 1$.
3. Pattern $\dfrac{u'}{u}$ with $u(x) = x^2 + 3x + 1 > 0$:
   $J_3 = [\ln(x^2 + 3x + 1)]_1^2 = \ln(11) - \ln(5) = \ln\left(\dfrac{11}{5}\right)$.
4. Pattern $u' u^3$ with $u(x) = \sin x$:
   $J_4 = \left[ \dfrac{\sin^4 x}{4} \right]_0^{\pi/4} = \dfrac{(\sqrt{2}/2)^4}{4} - 0 = \dfrac{1/4}{4} = \dfrac{1}{16}$.

**Solution 50.5:**
1. $\int_{-a}^a f = \int_{-a}^0 f + \int_0^a f$. By substitution $u = -x$, if $f$ is even, $\int_{-a}^0 f(x)\,dx = \int_0^a f(u)\,du$, giving $2\int_0^a f$.
2. If $f$ is odd, $\int_{-a}^0 f(x)\,dx = -\int_0^a f(u)\,du$, so the sum is 0.
3. The integrand $x \mapsto x^7 - 3x^3 + \sin x$ is a sum of odd functions, so it is odd. Across the symmetric interval $[-2\,; 2]$, the integral is **strictly zero: $K = 0$**.

**Solution 50.6:**
$\mu = \dfrac{1}{3 - 0} \int_0^3 x^2 \, dx = \dfrac{1}{3} \left[ \dfrac{x^3}{3} \right]_0^3 = \dfrac{1}{3} \times 9 = 3$.
Interpretation: a rectangle of width 3 and constant height $\mu = 3$ has area $3 \times 3 = 9$, exactly matching the area under the parabolic curve.

**Solution 50.7:**
The parabola crosses the horizontal axis when $4 - x^2 = 0 \iff x = \pm 2$.
On $[-2\,; 2]$, the function is positive and even.
$\mathcal{A} = \int_{-2}^2 (4 - x^2) \, dx = 2 \int_0^2 (4 - x^2) \, dx = 2 \left[ 4x - \dfrac{x^3}{3} \right]_0^2 = 2 \left( 8 - \dfrac{8}{3} \right) = \dfrac{32}{3} \approx 10.67$ u.a.

---

#### Level ★★ Solutions

**Solution 50.8:**
1. $A_1 = \int_0^\pi x \sin x \, dx$.
   Set $u'(x) = \sin x \implies u(x) = -\cos x$ and $v(x) = x \implies v'(x) = 1$.
   $A_1 = [-x \cos x]_0^\pi - \int_0^\pi (-\cos x) \, dx = (-\pi(-1) - 0) + [\sin x]_0^\pi = \pi + 0 = \pi$.
2. $A_2 = \int_1^e x \ln x \, dx$.
   Set $v(x) = \ln x \implies v'(x) = \dfrac{1}{x}$ and $u'(x) = x \implies u(x) = \dfrac{x^2}{2}$.
   $A_2 = \left[ \dfrac{x^2}{2} \ln x \right]_1^e - \int_1^e \dfrac{x^2}{2} \dfrac{1}{x} \, dx = \dfrac{e^2}{2} - \dfrac{1}{2}\left[\dfrac{x^2}{2}\right]_1^e = \dfrac{e^2}{2} - \dfrac{e^2 - 1}{4} = \dfrac{e^2 + 1}{4}$.
3. $A_3 = \int_0^1 (2x + 1) e^{-x} \, dx$.
   Set $v(x) = 2x+1 \implies v'(x) = 2$ and $u'(x) = e^{-x} \implies u(x) = -e^{-x}$.
   $A_3 = [-(2x+1)e^{-x}]_0^1 + 2\int_0^1 e^{-x} \, dx = (-3e^{-1} + 1) + 2[-e^{-x}]_0^1 = 1 - 3e^{-1} + 2(1 - e^{-1}) = 3 - \dfrac{5}{e}$.

**Solution 50.9:**
First IBP for $B = \int_0^1 x^2 e^x \, dx$:
$v(x) = x^2 \implies v'(x) = 2x$, $u'(x) = e^x \implies u(x) = e^x$.
$B = [x^2 e^x]_0^1 - 2 \int_0^1 x e^x \, dx = e - 2 \int_0^1 x e^x \, dx$.
From Worked Example 3, $\int_0^1 x e^x \, dx = 1$.
Hence $B = e - 2(1) = e - 2$.

**Solution 50.10:**
1. $f(x) = g(x) \iff -x^2 + 4x = x^2 - 2x \iff 2x^2 - 6x = 0 \iff 2x(x - 3) = 0$.
   Intersections occur at $x = 0$ and $x = 3$.
2. Relative positions: $f(x) - g(x) = 6x - 2x^2 = 2x(3 - x)$.
   On $[0\,; 3]$, both $2x \geq 0$ and $3 - x \geq 0$, so $f(x) \geq g(x)$.
   The graph of $f$ lies entirely above that of $g$.
3. $\mathcal{A} = \int_0^3 (6x - 2x^2) \, dx = \left[ 3x^2 - \dfrac{2x^3}{3} \right]_0^3 = (27 - 18) - 0 = 9$ area units.

**Solution 50.11:**
1. $F(1) = \int_1^1 \dfrac{e^t}{t} \, dt = 0$.
2. The integrand $t \mapsto \dfrac{e^t}{t}$ is continuous on $]0\,;+\infty[$. By the Fundamental Theorem of Calculus, $F$ is differentiable on $]0\,;+\infty[$ and $F'(x) = \dfrac{e^x}{x}$.
3. For all $x > 0$, $e^x > 0$ and $x > 0$, so $F'(x) > 0$. $F$ is strictly increasing on $]0\,;+\infty[$.
4. Let $\varphi(t) = \dfrac{e^t}{t}$ on $[1\,; +\infty[$. $\varphi'(t) = \dfrac{e^t(t-1)}{t^2} \geq 0$ for $t \geq 1$.
   The minimum is attained at $t = 1$: $\varphi(1) = e$.
   Thus for all $t \geq 1$, $\dfrac{e^t}{t} \geq e$.
   Integrating from $1$ to $x$ (with $x \geq 1$):
   $F(x) = \int_1^x \dfrac{e^t}{t} \, dt \geq \int_1^x e \, dt = e(x - 1)$.
5. Since $\lim\limits_{x \to +\infty} e(x - 1) = +\infty$, the comparison theorem yields $\lim\limits_{x \to +\infty} F(x) = +\infty$.

**Solution 50.12:**
1. $I_0 = \int_0^1 e^{-x} \, dx = [-e^{-x}]_0^1 = 1 - \dfrac{1}{e}$.
2. IBP on $I_{n+1} = \int_0^1 x^{n+1} e^{-x} \, dx$:
   $v(x) = x^{n+1} \implies v'(x) = (n+1)x^n$ and $u'(x) = e^{-x} \implies u(x) = -e^{-x}$.
   $I_{n+1} = [-x^{n+1} e^{-x}]_0^1 + (n+1)\int_0^1 x^n e^{-x} \, dx = -\dfrac{1}{e} + (n+1)I_n$.
3. $I_1 = 1 \times I_0 - \dfrac{1}{e} = 1 - \dfrac{2}{e}$.
   $I_2 = 2 I_1 - \dfrac{1}{e} = 2 - \dfrac{5}{e}$.
4. On $[0\,; 1]$, $x^n \geq 0$ and $e^{-x} > 0$, so the integrand is positive. With integration limits in order, $I_n \geq 0$.
5. $I_{n+1} - I_n = \int_0^1 x^n(x - 1)e^{-x} \, dx \leq 0$ because $x - 1 \leq 0$. The sequence is decreasing.
6. For $x \in [0\,; 1]$, $-1 \leq -x \leq 0 \implies e^{-1} \leq e^{-x} \leq 1$.
   Multiply by $x^n$: $x^n e^{-1} \leq x^n e^{-x} \leq x^n$.
   Integrating on $[0\,; 1]$ gives $\dfrac{1}{e(n+1)} \leq I_n \leq \dfrac{1}{n+1}$.
   By the Squeeze Theorem, $\lim\limits_{n \to +\infty} I_n = 0$.

**Solution 50.13:**
1. $R(0.5) = 0.4 - k(0.5)^2 = 0.3 \iff 0.4 - 0.25k = 0.3 \iff k = 0.4$.
   Thus $R(x) = 0.4(1 - x^2)$.
2. Each disk slice of thickness $dx$ has volume $dV = \pi R(x)^2 dx$.
3. $V = \int_{-0.5}^{0.5} \pi [R(x)]^2 \, dx$.
4. By even symmetry: $V = 2\pi \int_0^{0.5} 0.16(1 - 2x^2 + x^4) \, dx = 0.32\pi \left[ x - \dfrac{2}{3}x^3 + \dfrac{x^5}{5} \right]_0^{0.5} \approx 0.32\pi \times 0.42292 \approx 0.425\text{ m}^3 = 425\text{ liters}$.
   A simple cylinder of average radius $0.35\text{ m}$ would hold $\pi (0.35)^2 (1) \approx 0.385\text{ m}^3 = 385\text{ liters}$. The bulge adds 40 liters of wine!

**Solution 50.14:**
1. $\dfrac{a}{x-1} + \dfrac{b}{x+1} = \dfrac{(a+b)x + (a-b)}{x^2 - 1}$. Matching coefficients: $a + b = 0$ and $a - b = 1 \implies a = \dfrac{1}{2}, b = -\dfrac{1}{2}$.
   Thus $\dfrac{1}{x^2 - 1} = \dfrac{1}{2(x-1)} - \dfrac{1}{2(x+1)}$.
2. $F(x) = \dfrac{1}{2}\ln(x-1) - \dfrac{1}{2}\ln(x+1) = \dfrac{1}{2}\ln\left(\dfrac{x-1}{x+1}\right)$.
3. $I = [F(x)]_2^3 = \dfrac{1}{2}\ln(2/4) - \dfrac{1}{2}\ln(1/3) = \dfrac{1}{2}\ln(3/2)$.

**Solution 50.15:**
1. $a(t) = 400(t+10)^{-2}$. An antiderivative is $-\dfrac{400}{t+10}$.
   $v(t) = C - \dfrac{400}{t+10}$. With $v(0) = 0$, $C = 40$.
   Hence $v(t) = 40 - \dfrac{400}{t+10}$.
2. At $t = 30\text{ s}$: $v(30) = 40 - \dfrac{400}{40} = 30\text{ m}\cdot\text{s}^{-1}$ ($108\text{ km/h}$).
3. $h(t) = \int_0^t v(u)\,du = 40t - 400\ln\left(1 + \dfrac{t}{10}\right)$.
   At $t = 30\text{ s}$: $h(30) = 1200 - 400\ln 4 \approx 645.5\text{ meters}$.

**Solution 50.16:**
1. Expand the square: $(f(t) + \lambda g(t))^2 = (f(t))^2 + 2\lambda f(t)g(t) + \lambda^2 (g(t))^2 \geq 0$.
   Integrating yields a quadratic in $\lambda$:
   $P(\lambda) = \lambda^2 \left(\int_a^b g^2\right) + 2\lambda \left(\int_a^b fg\right) + \left(\int_a^b f^2\right) \geq 0$.
2. Since this quadratic is non-negative for all real $\lambda$, its discriminant cannot be positive ($\Delta' \leq 0$):
   $\left(\int_a^b fg\right)^2 - \left(\int_a^b g^2\right)\left(\int_a^b f^2\right) \leq 0$,
   which proves the Cauchy-Schwarz inequality.

---

#### Level ★★★ Solutions

**Solution 50.17:**
1. $W_0 = \int_0^{\pi/2} 1 \, dx = \dfrac{\pi}{2}$, and $W_1 = \int_0^{\pi/2} \sin x \, dx = [-\cos x]_0^{\pi/2} = 1$.
2. IBP with $u'(x) = \sin x \implies u(x) = -\cos x$ and $v(x) = \sin^n x \implies v'(x) = n\cos x \sin^{n-1} x$:
   $W_{n+1} = [-\cos x \sin^n x]_0^{\pi/2} + n\int_0^{\pi/2} \cos^2 x \sin^{n-1} x \, dx$.
   The boundary term vanishes. With $\cos^2 x = 1 - \sin^2 x$:
   $W_{n+1} = n W_{n-1} - n W_{n+1} \iff (n+1)W_{n+1} = n W_{n-1} \iff W_{n+1} = \dfrac{n}{n+1} W_{n-1}$.
3. By induction:
   $W_{2p} = \dfrac{(2p)!}{2^{2p} (p!)^2} \dfrac{\pi}{2}$, and $W_{2p+1} = \dfrac{2^{2p} (p!)^2}{(2p+1)!}$.
4. On $[0\,; \pi/2]$, $0 \leq \sin x \leq 1 \implies 0 \leq \sin^{n+1} x \leq \sin^n x$, hence $0 < W_{n+1} \leq W_n$.
5. From $W_{n+1} \leq W_n \leq W_{n-1}$, divide by $W_{n+1}$: $1 \leq \dfrac{W_n}{W_{n+1}} \leq 1 + \dfrac{1}{n} \to 1$.
   The ratio $\dfrac{W_{2p+1}}{W_{2p}}$ establishes Wallis' product formula converging to $\dfrac{2}{\pi}$.

**Solution 50.18:**
1. For $x \geq 1$, $x^2 \geq x \implies e^{-x^2} \leq e^{-x}$, which integrates to $e^{-1} < +\infty$, ensuring convergence.
2. Converting the quarter-plane to polar coordinates gives $\theta \in [0\,; \pi/2]$ and $r \in [0\,; +\infty[$, with Jacobian area element $r \, dr \, d\theta$.
3. $\int_0^{+\infty} r e^{-r^2} \, dr = \left[-\dfrac{1}{2}e^{-r^2}\right]_0^{+\infty} = \dfrac{1}{2}$.
   Then $I^2 = \dfrac{\pi}{2} \times \dfrac{1}{2} = \dfrac{\pi}{4} \implies I = \dfrac{\sqrt{\pi}}{2}$.
   By even symmetry over $\mathbb{R}$: $\int_{-\infty}^{+\infty} e^{-x^2} \, dx = 2I = \sqrt{\pi}$.

**Solution 50.19:**
1. IBP with $u'(t) = 1 \implies u(t) = t - 1/2$ and $v(t) = f(t) \implies v'(t) = f'(t)$:
   $\int_0^1 (t - 1/2) f'(t) \, dt = [(t - 1/2) f(t)]_0^1 - \int_0^1 f(t) \, dt = \dfrac{f(0)+f(1)}{2} - \int_0^1 f(t) \, dt$.
2. Summing this across intervals $[k\,; k+1]$ connects discrete sums to continuous integrals with extraordinary precision.

**Solution 50.20:**
Let $F(x) = \int_a^x f(t)\,dt$. $F$ is continuous on $[a\,; b]$ and differentiable on $]a\,; b[$.
By the Mean Value Theorem, there exists $c \in \; ]a\,; b[$ such that:
$$\dfrac{F(b) - F(a)}{b - a} = F'(c).$$
Since $F(b) - F(a) = \int_a^b f(t)\,dt$ and $F'(c) = f(c)$, we obtain $\int_a^b f(t)\,dt = f(c)(b - a)$.

---

### The Question that Opens What Follows

We now know how to compute the area under a curve whenever an explicit formula for the function is known. But what happens in the real world, when we do not know the formula of the function in advance, but only **a relationship linking the function to its own rate of change**?

When a hot cup of tea sits on a kitchen table, the rate at which it cools is directly proportional to the difference between its temperature and the ambient room temperature.
How can we uncover the complete temperature profile over time from this simple physical rule?

Welcome to the realm of **differential equations**: join us in Chapter 51 with **The Cooling Cup of Tea**.
