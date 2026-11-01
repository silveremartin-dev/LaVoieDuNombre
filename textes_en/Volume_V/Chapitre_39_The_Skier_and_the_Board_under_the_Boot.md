# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 39: The Skier and the Board under the Boot

> *“Until now, our gaze took motionless photographs of the world: fixed positions, averages over long distances. But life is not an album of dead pictures: it is a continuous torrent. To measure the slope of a hill at the exact millisecond the heart beats, one must place a microscope upon flowing time.”*

---

### What You Are About to Discover

- The skier's paradox: how to measure the **slope at a single point**, when calculating a slope inherently requires two separate points.
- The **difference quotient** (rate of change) and the stroke of genius of **passing to the limit** as the gap $h$ approaches 0.
- Legendary notations: **Lagrange's** “$f'(a)$” and **Leibniz's** “$\frac{dy}{dx}$”.
- The equation of the **tangent line**: the rigid line that grazes the curve without cutting through it.
- Geometric proofs of standard derivatives: why $(x^2)' = 2x$ thanks to the **growing flowerbed**, and the derivatives of $x^n$, $\frac{1}{x}$, $\sqrt{x}$.
- Operations on functions: $(uv)' = u'v + uv'$ (proved via the expanding rectangle) and the quotient rule.
- The fundamental link between the **sign of the derivative** and **intervals of increase/decrease**, and hunting for **local extrema**.
- The boundary cases where differential calculus breaks down: the **corner point** (sharp turn) of the absolute value and the **vertical tangent** of the square root.
- Concrete problems in **optimization**: constructing the most spacious box or the most economical tin can.

---

### 1. The Problem: The Vertigo of the Descent

You are sixteen years old. You stand atop a high, snow-covered mountain peak, skis clipped to your boots, poles planted firmly in the fresh powder. Ahead unfolds a daunting Olympic run: this is no straight, even ramp; it is an unbroken succession of mogulled hills, sheer dips, and deceptive flats. The vertical profile of the mountain is a sinuous curve described by an elevation function $y = f(x)$.

You push off. The wind roars against your helmet, snow billowing in icy plumes beneath your steel edges. With every hundredth of a second, the incline under your boots shifts: gentle here, plunging precipitously into the void there.

In the hollow of the run, at the precise horizontal position $a$, a surge of centrifugal force crushes your thighs into the snow. Ask yourself this fundamental question of physics:

*“At this exact instant, at this very millisecond when my edges bite into the snowpack, what is the slope of the mountain beneath my boots?”*

```
   Elevation y
        ▲
        │                Profile of the hill y = f(x)
        │                   _--'""'--_   (Peak: Zero slope!)
        │                _-"          "-_
        │              /                  \
        │            /                      \
        │        _--' (Steep uphill slope)   \__
        │    _--'                                "---_ (Fast descent)
        +─────────────────────────────────────────────► Position x
                     a
```

Finding your altitude at this point is trivial: it is simply the value $f(a)$.
But what about **the slope**?
Ever since middle school, you have known that a slope (or gradient) is always calculated by dividing a vertical rise by a horizontal run between **two distinct points**:

$$\text{Slope} = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x}.$$

Yet, at this exact split second, you are at **only one single point**!
If you attempt to apply the formula taking the exact same point twice, $A(a; f(a))$, you obtain:

$$\text{Slope} = \frac{f(a) - f(a)}{a - a} = \frac{0}{0}.$$

Division by zero! A mathematical absurdity.
How can the mountain have a perfectly tangible, physical slope under your feet, while the raw slope formula collapses into $\frac{0}{0}$?

---

### 2. The Board under the Boot: From Secant to Tangent

#### 2.1 The Rigidity of the Ski

To untie this knot, listen to your body and inspect your equipment.
Under your boots, you have strapped two long boards of laminated wood, fiberglass, and hardened steel edges: skis. Even though the snow surface is humped and continuously curved, **your skis are straight, rigid objects**.

At every point where your weight presses down, the flat sole of your ski embraces the mountain's curve without sinking through it. It grazes the curve at a single instantaneous point of contact.
This straight line that caresses the curve at a point without locally crossing it is the **tangent line** to the curve.
And the slope beneath your boots is quite simply **the slope of your ski**!

```
                   Curve of the mountain
                         ..---*---..
                 ======*================   <--- The rigid ski (the Tangent!)
                     / |
               Δy   /  |  Vertical rise
                   /___|
                    Δx    Horizontal run
```

#### 2.2 The Difference Quotient: The Secant Line

To compute this slope without cheating with zero, imagine that the tail of your ski touches the snow at $A(a; f(a))$, and the tip touches the snow slightly ahead, at $M(a+h; f(a+h))$, where $h$ is a small, non-zero separation.

```
       Elevation
          ▲                   M (a+h ; f(a+h))
          │                  /│
          │                 / │ f(a+h) - f(a)
          │     A          /  │
          │      o────────┴───┘
          │      |    h
          └──────┴────────────┴─────► Position
                 a           a+h
```

The line $(AM)$ passing through two distinct points of the curve is called a **secant line**. Its slope is given by the ratio:

$$\tau(h) = \frac{f(a+h) - f(a)}{h}.$$

This fundamental ratio is called the **difference quotient** (or average rate of change) of the function $f$ between $a$ and $a+h$.
Because $h \neq 0$, this fraction is perfectly well-defined and computable!

#### 2.3 Passing to the Limit: The Zoom into the Infinitesimal

Now, imagine shortening your ski! Bring the tip closer and closer to the heel by letting $h$ shrink ever closer to zero:
$h = 0.1$, then $h = 0.01$, then $h = 0.000001$...
The point $M$ glides down along the hill, merging into point $A$.
The secant line $(AM)$ pivots smoothly and stabilizes onto a definite limiting position: **the tangent line**!

> **📐 Definition — Derivative at a Point**
> Let $f$ be a function defined on an open interval containing $a$.
> We say that $f$ is **differentiable at $a$** if the difference quotient $\frac{f(a+h)-f(a)}{h}$ approaches a finite limit as $h$ tends to 0.
> This limit is called the **derivative of $f$ at $a$**, denoted $f'(a)$:
>
> $$\boxed{f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}}$$
>
> Geometrically, $f'(a)$ is the **slope (gradient) of the tangent line** to the curve of $f$ at the point with abscissa $a$.

---

### 3. The Notations of History: Lagrange vs. Leibniz

Two giants of mathematics bequeathed to humanity two complementary ways of writing this single profound idea:

#### 3.1 Joseph-Louis Lagrange’s “Prime” Notation (1797)
The Franco-Italian mathematician **Joseph-Louis Lagrange** introduced the compact notation:
$$f'(a)$$
read aloud as: “**f prime of a**”. The prime mark signals that this new function is “derived” from the original function $f$. Differentiating a second time gives $f''(a)$ (“f double prime”). This is the fastest, cleanest notation for algebraic manipulation in secondary school.

#### 3.2 Gottfried Wilhelm Leibniz’s Differential Notation (1684)
A century earlier, the German polymath **Gottfried Wilhelm Leibniz** invented a magnificent notation directly reflecting the slope calculation $\frac{\Delta y}{\Delta x}$:
$$\frac{df}{dx}(a) \quad \text{or} \quad \frac{dy}{dx}$$
read as: “**d f over d x**” or “**the derivative of y with respect to x**”.
The Latin letter $d$ replaces the Greek letter $\Delta$ to signify an **infinitesimal** (infinitely tiny) variation. This notation continually reminds us that a derivative is the ratio of an infinitesimal change in height $dy$ to an infinitesimal change in horizontal position $dx$. Physicists cherish it because it immediately displays physical dimensions and units (e.g., meters per second: $\frac{dx}{dt} = \text{velocity}$).

---

### 4. The Equation of the Tangent Line to the Curve

Because the tangent line passes through the contact point $A(a; f(a))$ and has slope $f'(a)$, its point-slope equation follows directly from coordinate geometry:

$$y - y_A = m(x - x_A) \iff y - f(a) = f'(a)(x - a).$$

> **📐 Theorem — Equation of the Tangent Line**
> If $f$ is differentiable at $a$, the curve $\mathcal{C}_f$ admits at the point $A(a; f(a))$ a tangent line with equation:
>
> $$\boxed{y = f'(a)(x - a) + f(a)}$$

This line represents the **best local linear approximation** of the function near $a$. For any $x$ very close to $a$:
$$f(x) \approx f(a) + f'(a)(x - a).$$

---

### 5. Standard Derivatives Proved

Let us examine the foundational toolkit of functions. For each one, we compute the limit of the difference quotient with complete algebraic rigor.

#### 5.1 The Constant Function: $f(x) = k$
A perfectly level track has zero slope everywhere.
For any $h \neq 0$:
$$\frac{f(a+h) - f(a)}{h} = \frac{k - k}{h} = \frac{0}{h} = 0.$$
The limit as $h \to 0$ is 0. Therefore:
$$\boxed{(k)' = 0}$$

#### 5.2 The Linear Function: $f(x) = x$
A straight ramp inclined at 45° has a constant slope of 1.
$$\frac{(a+h) - a}{h} = \frac{h}{h} = 1 \xrightarrow[h \to 0]{} 1.$$
Therefore:
$$\boxed{(x)' = 1}$$

#### 5.3 The Square Function: Why $(x^2)' = 2x$?
Here enters the luminous demonstration of the expanding garden:

> **✍️ Geometric Proof — The Growing Flowerbed**
> Consider a square flowerbed with side length $x$. Its area is $S(x) = x^2$.
> In spring, the gardener expands the bed by adding a thin strip of soil of width $h$ to the East, and a strip of width $h$ to the North.
>
> ```
>                   x                h
>           ┌──────────────────────┬───┐
>           │                      │   │
>         x │    Original square   │ B │ h  (East strip: x × h)
>           │        (x²)          │   │
>           │                      │   │
>           ├──────────────────────┼───┤
>         h │     North strip      │ C │ h  (Corner: h²)
>           └──────────────────────┴───┘
>                      x             h
> ```
>
> The total new area added consists of three pieces:
> 1. An East strip of area $x \times h$;
> 2. A North strip of area $x \times h$;
> 3. A tiny square in the corner of area $h^2$.
>
> The total increase in area is:
> $$\Delta S = (x \times h) + (x \times h) + h^2 = 2xh + h^2.$$
> Divide by the expansion width $h$ to find the average rate of area growth:
> $$\frac{\Delta S}{h} = \frac{2xh + h^2}{h} = 2x + h.$$
> Now let $h$ shrink to zero!
> The tiny corner $h^2$ vanishes infinitely faster than the borders. All that remains is:
> $$\lim_{h \to 0} (2x + h) = 2x.$$
> The number 2 is not magic: **it represents the 2 open sides of the square expanding outward into space!** $\blacksquare$

By pure algebra:
$$\frac{(a+h)^2 - a^2}{h} = \frac{a^2 + 2ah + h^2 - a^2}{h} = \frac{2ah + h^2}{h} = 2a + h \xrightarrow[h \to 0]{} 2a.$$
Therefore:
$$\boxed{(x^2)' = 2x}$$

#### 5.4 The Power Function: $f(x) = x^n$ ($n \in \mathbb{N}^*$)
Extending this insight to a cube ($x^3$), the 3 expanding faces yield $(x^3)' = 3x^2$.
In dimension $n$, using the standard algebraic identity:
$$A^n - B^n = (A - B)(A^{n-1} + A^{n-2}B + \dots + AB^{n-2} + B^{n-1}),$$
with $A = a+h$ and $B = a$, the difference quotient becomes:
$$\frac{(a+h)^n - a^n}{h} = \frac{h \cdot \left((a+h)^{n-1} + (a+h)^{n-2}a + \dots + a^{n-1}\right)}{h}.$$
There are exactly $n$ terms inside the parentheses. As $h \to 0$, each term converges to $a^{n-1}$. Their sum is therefore $n a^{n-1}$.
$$\boxed{(x^n)' = n x^{n-1}}$$

#### 5.5 The Reciprocal Function: $f(x) = \frac{1}{x}$ on $\mathbb{R}^*$
For any $a \neq 0$ and $h$ sufficiently small:
$$\frac{f(a+h) - f(a)}{h} = \frac{\frac{1}{a+h} - \frac{1}{a}}{h} = \frac{\frac{a - (a+h)}{a(a+h)}}{h} = \frac{\frac{-h}{a(a+h)}}{h} = -\frac{1}{a(a+h)}.$$
As $h \to 0$, the denominator approaches $a \times a = a^2$.
The limit is therefore $-\frac{1}{a^2}$.
$$\boxed{\left(\frac{1}{x}\right)' = -\frac{1}{x^2}}$$

#### 5.6 The Square Root Function: $f(x) = \sqrt{x}$ on $]0; +\infty[$
For any $a > 0$, let us compute the difference quotient. We face an indeterminate form $\frac{0}{0}$. To resolve it, multiply numerator and denominator by the **conjugate radical** $(\sqrt{a+h} + \sqrt{a})$:
$$\frac{\sqrt{a+h} - \sqrt{a}}{h} = \frac{(\sqrt{a+h} - \sqrt{a})(\sqrt{a+h} + \sqrt{a})}{h(\sqrt{a+h} + \sqrt{a})} = \frac{(a+h) - a}{h(\sqrt{a+h} + \sqrt{a})} = \frac{h}{h(\sqrt{a+h} + \sqrt{a})} = \frac{1}{\sqrt{a+h} + \sqrt{a}}.$$
As $h \to 0$, the denominator approaches $\sqrt{a} + \sqrt{a} = 2\sqrt{a}$.
$$\boxed{(\sqrt{x})' = \frac{1}{2\sqrt{x}}}$$

---

### 6. Operations on Derived Functions

Let $u$ and $v$ be two differentiable functions on an interval $I$, and let $k$ be a real constant.

#### 6.1 Sum and Scalar Multiplication
- $(u + v)' = u' + v'$
- $(k \cdot u)' = k \cdot u'$

#### 6.2 Derivative of a Product: Why $(uv)' \neq u'v'$?
This is the most notorious trap in the history of mathematics. Even Leibniz fell into it in his initial notes in 1673, before correcting himself by sketching an expanding rectangle!

> **✍️ Geometric Proof — The Expanding Rectangle**
> Consider a rectangular field of dimensions $u(x)$ by $v(x)$. Its area is $A(x) = u(x) \times v(x)$.
> When $x$ increases by a small amount $h$, the width becomes $u + \Delta u$ and the length becomes $v + \Delta v$.
>
> ```
>                   u(x)              Δu
>           ┌──────────────────────┬──────┐
>           │                      │      │
>      v(x) │      Base area       │      │
>           │       u(x) × v(x)    │ v·Δu │
>           │                      │      │
>           ├──────────────────────┼──────┤
>        Δv │         u·Δv         │Δu·Δv │
>           └──────────────────────┴──────┘
> ```
>
> The newly added surface area is composed of three zones:
> 1. A vertical strip of area $v(x) \times \Delta u$;
> 2. A horizontal strip of area $u(x) \times \Delta v$;
> 3. A negligible corner of area $\Delta u \times \Delta v$.
>
> Dividing by $h$:
> $$\frac{\Delta A}{h} = v(x) \frac{\Delta u}{h} + u(x) \frac{\Delta v}{h} + \frac{\Delta u \cdot \Delta v}{h}.$$
> As $h \to 0$:
> - $\frac{\Delta u}{h} \to u'(x)$ and $\frac{\Delta v}{h} \to v'(x)$;
> - The third term vanishes because $\Delta u \to 0$!
> Only the two main strips remain:
> $$\boxed{(u \cdot v)' = u'v + uv'} \quad \blacksquare$$

#### 6.3 Derivative of the Reciprocal and Quotient
If $v(x) \neq 0$ on $I$:
- Reciprocal Rule:
  $$\boxed{\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}}$$
- Quotient Rule:
  Writing $\frac{u}{v} = u \times \frac{1}{v}$ and applying the product rule:
  $$\left(\frac{u}{v}\right)' = u'\left(\frac{1}{v}\right) + u\left(-\frac{v'}{v^2}\right) = \frac{u'v}{v^2} - \frac{uv'}{v^2} = \boxed{\frac{u'v - uv'}{v^2}}$$

> **⚠️ Caution: Classic Trap! — Order Matters in the Quotient Rule**
> In the numerator $u'v - uv'$, the minus sign makes the order crucial! It is always the derivative of the top ($u'$) multiplying the untouched bottom ($v$) first. Reversing the terms flips the sign of your entire result.

---

### 7. The Crucial Link: Sign of the Derivative and Monotonicity

Here differential calculus reveals its absolute power: it transforms a hard global geometric question (“is the function climbing or falling across an interval?”) into a straightforward local algebraic check (“what is the sign of a number?”).

> **📐 Fundamental Theorem — Monotonicity and Sign of the Derivative**
> Let $f$ be differentiable on an interval $I$.
> - If $f'(x) > 0$ for all $x \in I$, then $f$ is **strictly increasing** on $I$.
> - If $f'(x) < 0$ for all $x \in I$, then $f$ is **strictly decreasing** on $I$.
> - If $f'(x) = 0$ for all $x \in I$, then $f$ is **constant** on $I$.

Intuitively: if the tips of your skis point upward ($f'(x) > 0$) at every single millisecond of your glide, you cannot help but gain altitude overall!

---

### 8. Finding Local Extrema and Optimization

How do we pinpoint the highest crest of a hill or the deepest depression of a valley?
At the summit of a hill, the slope ceases to rise and prepares to fall: for one infinitesimal heartbeat, the ski levels out to absolute horizontality!

```
                Horizontal Tangent (f'(x₀) = 0)
                      =======================
                            ..---*---..
                          /             \
                    f' > 0               f' < 0
                   (Uphill)             (Downhill)
```

> **📐 Theorem — Local Extremum Condition**
> Let $f$ be differentiable on an open interval containing $x_0$.
> If $f$ attains a local extremum (maximum or minimum) at $x_0$, then:
> $$f'(x_0) = 0.$$
>
> **Converse and Practical Criterion:**
> If $f'(x_0) = 0$ and $f'$ **changes sign** at $x_0$, then $f$ attains a local extremum at $x_0$:
> - From $+$ to $-$: this is a **local maximum** (the curve rises, then falls).
> - From $-$ to $+$: this is a **local minimum** (the curve falls, then rises).

> **⚠️ Caution: Classic Trap! — $f'(x_0) = 0$ Does Not Guarantee an Extremum**
> Look at the cubic function $f(x) = x^3$. Its derivative is $f'(x) = 3x^2$.
> At $x = 0$, indeed $f'(0) = 0$ (the tangent is perfectly horizontal).
> But for all $x \neq 0$, $3x^2 > 0$: the derivative never changes sign! The curve climbs before 0 and continues climbing after 0. The origin $(0; 0)$ is a flat bench (an inflection point), not a summit or basin!

---

### 9. At the Boundaries of Differentiation: When Calculus Breaks Down

Are all functions differentiable everywhere? No! There are two primary geometric ways for a curve to reject differentiation at a point.

#### 9.1 The Corner Point: The Absolute Value at 0
Consider the absolute value function $f(x) = |x|$. Its graph forms a sharp “V” at the origin.
Compute the difference quotient at $0$:
$$\tau(h) = \frac{|0+h| - |0|}{h} = \frac{|h|}{h}.$$
- Approaching from the right ($h > 0$): $|h| = h$, so $\tau(h) = \frac{h}{h} = +1$.
- Approaching from the left ($h < 0$): $|h| = -h$, so $\tau(h) = \frac{-h}{h} = -1$.

The right-hand limit ($+1$) does not match the left-hand limit ($-1$)!
The ski cannot rest stably on a knife-edge apex without wobbling between two contradictory slopes.
We say that the absolute value function **is not differentiable at 0**. The graph possesses two half-tangents meeting at a sharp **corner point**.

#### 9.2 The Vertical Tangent: The Square Root at 0
Consider the function $f(x) = \sqrt{x}$ at $a = 0$.
For $h > 0$:
$$\tau(h) = \frac{\sqrt{0+h} - \sqrt{0}}{h} = \frac{\sqrt{h}}{h} = \frac{1}{\sqrt{h}}.$$
As $h \to 0^+$, $\sqrt{h}$ becomes an infinitesimally small positive quantity, so $\frac{1}{\sqrt{h}}$ blows up toward $+\infty$!
The limit is not a finite real number.
The square root function **is not differentiable at 0**.
Geometrically, the curve launches vertically: it has a **vertical half-tangent** along the $y$-axis ($x = 0$).

---

### Step-by-Step Worked Examples

> **✅ Worked Example 1 — Computing a Derivative from Definition**
> Let $f(x) = 3x^2 - 5x + 2$. Compute $f'(2)$ directly using the definition of the difference quotient.
>
> **Detailed Solution:**
> First find $f(2)$: $f(2) = 3(2^2) - 5(2) + 2 = 12 - 10 + 2 = 4$.
> Expand $f(2+h)$ for $h \neq 0$:
> $$\begin{aligned}
> f(2+h) &= 3(2+h)^2 - 5(2+h) + 2 \\
> &= 3(4 + 4h + h^2) - 10 - 5h + 2 \\
> &= 12 + 12h + 3h^2 - 10 - 5h + 2 = 4 + 7h + 3h^2.
> \end{aligned}$$
> Form the difference quotient:
> $$\frac{f(2+h) - f(2)}{h} = \frac{(4 + 7h + 3h^2) - 4}{h} = \frac{7h + 3h^2}{h} = \frac{h(7 + 3h)}{h} = 7 + 3h.$$
> Take the limit as $h \to 0$:
> $$\lim_{h \to 0} (7 + 3h) = 7.$$
> Thus $f$ is differentiable at $2$ and $\boxed{f'(2) = 7}$.

> **✅ Worked Example 2 — Equation of a Tangent Line**
> Let $f(x) = \frac{1}{x}$. Determine the equation of the tangent line to the curve of $f$ at the point with abscissa $a = 2$.
>
> **Detailed Solution:**
> - $y$-coordinate of the contact point: $f(2) = \frac{1}{2}$.
> - Derivative function: $f'(x) = -\frac{1}{x^2}$, so $f'(2) = -\frac{1}{2^2} = -\frac{1}{4}$.
> - Tangent line formula: $y = f'(2)(x - 2) + f(2)$.
> $$y = -\frac{1}{4}(x - 2) + \frac{1}{2} = -\frac{1}{4}x + \frac{2}{4} + \frac{1}{2} = -\frac{1}{4}x + 1.$$
> The tangent line equation is $\boxed{y = -\frac{1}{4}x + 1}$.

> **✅ Worked Example 3 — Product and Quotient Rules**
> Compute the derivatives of:
> 1. $g(x) = (2x - 3)(x^2 + 4x)$
> 2. $h(x) = \frac{3x - 1}{x^2 + 1}$
>
> **Detailed Solution:**
> 1. Product form $u \cdot v$ with $u(x) = 2x - 3 \implies u'(x) = 2$, and $v(x) = x^2 + 4x \implies v'(x) = 2x + 4$.
>    $$g'(x) = u'v + uv' = 2(x^2 + 4x) + (2x - 3)(2x + 4).$$
>    Expanding:
>    $g'(x) = (2x^2 + 8x) + (4x^2 + 8x - 6x - 12) = 6x^2 + 10x - 12$.
> 2. Quotient form $\frac{u}{v}$ with $u(x) = 3x - 1 \implies u'(x) = 3$, and $v(x) = x^2 + 1 \implies v'(x) = 2x$.
>    $$h'(x) = \frac{u'v - uv'}{v^2} = \frac{3(x^2 + 1) - (3x - 1)(2x)}{(x^2 + 1)^2}.$$
>    Expanding the numerator:
>    $3x^2 + 3 - (6x^2 - 2x) = 3x^2 + 3 - 6x^2 + 2x = -3x^2 + 2x + 3$.
>    Hence: $\boxed{h'(x) = \frac{-3x^2 + 2x + 3}{(x^2 + 1)^2}}$.

> **✅ Worked Example 4 — Complete Analysis of a Cubic Polynomial**
> Let $f(x) = 2x^3 - 9x^2 + 12x - 1$ defined on $\mathbb{R}$.
> Construct its complete variation table and determine all local extrema.
>
> **Detailed Solution:**
> 1. Derivative: $f'(x) = 2(3x^2) - 9(2x) + 12(1) - 0 = 6x^2 - 18x + 12$.
>    Factor out 6: $f'(x) = 6(x^2 - 3x + 2)$.
> 2. Roots of $f'(x)$:
>    The quadratic $x^2 - 3x + 2$ factors readily as $(x - 1)(x - 2)$, with roots $x_1 = 1$ and $x_2 = 2$.
>    The leading coefficient is positive ($a = 6 > 0$), so the parabola for $f'$ opens upward:
>    - $f'(x) > 0$ on $]-\infty; 1[$ and on $]2; +\infty[$;
>    - $f'(x) < 0$ on $]1; 2[$.
> 3. Key values:
>    $f(1) = 2(1)^3 - 9(1)^2 + 12(1) - 1 = 2 - 9 + 12 - 1 = 4$.
>    $f(2) = 2(8) - 9(4) + 12(2) - 1 = 16 - 36 + 24 - 1 = 3$.
> 4. Variation table:
>
> | $x$ | $-\infty$ | | $1$ | | $2$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
> | $f(x)$ | | $\nearrow$ | $4$ | $\searrow$ | $3$ | $\nearrow$ | |
>
> **Conclusion:**
> $f$ attains a **local maximum** of $4$ at $x = 1$, and a **local minimum** of $3$ at $x = 2$.

> **✅ Worked Example 5 — Concrete Optimization: The Open Box**
> From a square sheet of cardboard measuring 12 cm on each side, small squares of side length $x$ (with $0 < x < 6$) are cut from each of the four corners. The sides are then folded up to form an open-top rectangular box.
> What value of $x$ maximizes the box's volume?
>
> **Detailed Solution:**
> 1. Dimensions of the folded box:
>    - Base: square of side length $12 - 2x$.
>    - Height: $x$.
> 2. Volume function:
>    $V(x) = \text{Base Area} \times \text{Height} = (12 - 2x)^2 \times x = (144 - 48x + 4x^2)x = 4x^3 - 48x^2 + 144x$.
> 3. Derivative:
>    $V'(x) = 12x^2 - 96x + 144 = 12(x^2 - 8x + 12)$.
> 4. Finding critical points:
>    Roots of $x^2 - 8x + 12 = 0$:
>    $\Delta = (-8)^2 - 4(1)(12) = 64 - 48 = 16 = 4^2$.
>    $x_1 = \frac{8 - 4}{2} = 2$, and $x_2 = \frac{8 + 4}{2} = 6$.
>    Since $x \in ]0; 6[$, only the root $x = 2$ lies in the feasible domain.
>    For $x < 2$, $V'(x) > 0$ (volume expands). For $x > 2$, $V'(x) < 0$ (volume shrinks).
> 5. Conclusion:
>    The maximum volume is achieved when the cutouts measure **$x = 2$ cm**.
>    The maximal capacity is $V(2) = (12 - 4)^2 \times 2 = 8^2 \times 2 = 64 \times 2 = 128\text{ cm}^3$.

> **✅ Worked Example 6 — Tangent Parallel to a Given Line**
> Let $f(x) = x^2 - 4x + 1$. Are there any points on the parabola where the tangent line is parallel to the line $y = 2x - 5$?
>
> **Detailed Solution:**
> - Two lines are parallel if and only if they share the exact same slope.
> - The given line has slope $m = 2$.
> - The tangent line at abscissa $x$ has slope $f'(x)$.
> - Differentiating: $f'(x) = 2x - 4$.
> - Set up the equation $f'(x) = 2$:
>   $$2x - 4 = 2 \iff 2x = 6 \iff x = 3.$$
> - Calculate the corresponding $y$-value: $f(3) = 3^2 - 4(3) + 1 = 9 - 12 + 1 = -2$.
> - Conclusion: There is exactly one such point on the curve, $A(3; -2)$.
>   Its tangent line equation is $y = 2(x - 3) - 2 = 2x - 8$.

---

### What You Must Remember

1. **The Derivative $f'(a)$:**
   - Definition: $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$.
   - Geometric meaning: slope of the ski beneath the boot = slope of the tangent line at $A(a; f(a))$.
   - Equation of the tangent line: $\boxed{y = f'(a)(x - a) + f(a)}$.

2. **Table of Standard Derivatives:**
   | Function $f(x)$ | Derivative $f'(x)$ | Domain of Validity |
   |---|---|---|
   | $k$ (constant) | $0$ | $\mathbb{R}$ |
   | $x$ | $1$ | $\mathbb{R}$ |
   | $x^2$ | $2x$ | $\mathbb{R}$ |
   | $x^n$ ($n \in \mathbb{N}^*$) | $n x^{n-1}$ | $\mathbb{R}$ |
   | $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\mathbb{R}^* = ]-\infty; 0[ \cup ]0; +\infty[$ |
   | $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | $]0; +\infty[$ (not differentiable at 0) |

3. **Differentiation Rules:**
   - $(u + v)' = u' + v'$
   - $(k u)' = k u'$
   - $(u v)' = u'v + uv'$
   - $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$
   - $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

4. **Sign of Derivative and Monotonicity:**
   - $f'(x) > 0 \implies f$ is strictly increasing.
   - $f'(x) < 0 \implies f$ is strictly decreasing.
   - $f'(x_0) = 0$ with a sign change $\implies$ local extremum (peak or trough).

5. **Failures of Differentiability:**
   - $f(x) = |x|$ at 0: corner point (left-hand and right-hand slopes differ).
   - $f(x) = \sqrt{x}$ at 0: vertical half-tangent (difference quotient tends to $+\infty$).

---

### Exercises

#### Level ★ (Direct Derivative Calculations and Tangents)

1. Compute the derivative of $f(x) = 5x^3 - 4x^2 + 7x - 9$.
2. Compute the derivative of $g(x) = 3\sqrt{x} - \frac{4}{x}$ for $x > 0$.
3. Determine the derivative value $f'(3)$ for $f(x) = x^2 - 2x$.
4. Write the equation of the tangent line to the curve of $f(x) = x^2$ at the point with abscissa $a = 1$.
5. Determine the coordinates of the points where the curve of $f(x) = x^3 - 3x$ has a horizontal tangent line.
6. Let $f(x) = \frac{2x+1}{x-3}$ on $]3; +\infty[$. Compute $f'(x)$.
7. Differentiate $h(x) = (x^2 + 1)(3x - 2)$.
8. Determine the sign of the derivative of $f(x) = -2x^2 + 8x - 5$ and deduce the variation of $f$.
9. Is the function $f(x) = |x-3|$ differentiable at $x = 3$? Justify.
10. Determine the local linear approximation of $\sqrt{1+h}$ for $h$ near 0 using the derivative of $\sqrt{x}$ at 1.

#### Level ★★ (Function Studies and Geometry)

11. Construct the complete variation table of $f(x) = \frac{1}{3}x^3 - x^2 - 3x + 4$ on $\mathbb{R}$.
12. Let $f(x) = \frac{x^2 - 3x + 6}{x - 1}$ defined on $]1; +\infty[$.
    a) Compute $f'(x)$ and show that $f'(x) = \frac{(x-3)(x+1)}{(x-1)^2}$.
    b) Deduce the minimum value of $f$ on this interval.
13. Consider the parabola with equation $y = -x^2 + 4x - 1$.
    Does there exist a tangent line to this parabola that passes through the origin $(0; 0)$?
14. Consider the function $f(x) = x\sqrt{x}$ defined on $[0; +\infty[$.
    a) Show via the difference quotient that $f$ is differentiable at $0$ and determine $f'(0)$.
    b) Compute $f'(x)$ for $x > 0$ using the product rule and check consistency.
15. Determine the intersection points of the curve $f(x) = x^3 - 3x^2 + x$ with the tangent line to the curve at $x = 0$.
16. A projectile is launched upward. Its altitude in meters at time $t$ (in seconds) is given by $z(t) = -5t^2 + 20t + 1.5$.
    a) Compute the instantaneous velocity $v(t) = z'(t)$ at any instant $t$.
    b) At what time does the projectile reach its maximum height? What is this maximum height?
17. Prove by induction that for any integer $n \ge 1$, the derivative of $f_n(x) = x^n$ is indeed $f'_n(x) = n x^{n-1}$, using the product rule.
18. Let $f(x) = \frac{ax + b}{x - 2}$. Determine the real numbers $a$ and $b$ such that the curve passes through $A(3; 5)$ and has a tangent line at $A$ with slope $-7$.

#### Level ★★★ (Optimization and Open Problems)

19. **The Shepherd's Enclosure:**
    A shepherd has 100 meters of fencing to build a rectangular enclosure backed against a straight, sheer cliff face (no fence is required along the cliff side).
    What dimensions will give the sheep the largest possible grazing area?
20. **The Optimal Tin Can:**
    We wish to manufacture a closed cylindrical tin can of fixed volume $V = 1$ liter ($1000\text{ cm}^3$).
    We seek to minimize the surface area of metal needed (i.e., the total surface area of the cylinder).
    a) Express the height $h$ in terms of the radius $r$.
    b) Express the total surface area $S(r)$ in terms of $r$.
    c) Compute $S'(r)$ and prove that the most metal-efficient can satisfies $h = 2r$ (the height must equal the diameter!).
21. **Minimal Distance from a Point to a Parabola:**
    In a Cartesian coordinate system, consider the parabola $\mathcal{P}$ with equation $y = x^2$ and the point $A(0; 2)$.
    Which point on the parabola is closest to $A$? Show that the segment connecting $A$ to this optimal point is perpendicular to the tangent line at that point.
22. **Corner Point and Differentiability:**
    Let $f$ be defined by $f(x) = x|x|$.
    a) Express $f(x)$ without absolute value bars depending on the sign of $x$.
    b) Investigate the differentiability of $f$ at 0 by computing the limit of the difference quotient.
    c) What can you conclude? Does a function containing an absolute value always produce a sharp corner point?
23. **Common Tangents to Two Parabolas:**
    Consider the two parabolas $y = x^2$ and $y = -x^2 + 4x - 6$.
    Does there exist a line tangent to both parabolas simultaneously? If so, find its equation.
24. **The Lifeguard's Snell-Descartes Problem:**
    A lifeguard standing on the beach at point $A(0; a)$ with $a > 0$ spots a swimmer in distress at sea at $B(d; -b)$ with $b > 0$. The shoreline is the $x$-axis $y = 0$.
    The lifeguard runs on sand at speed $v_1$ and swims in water at a slower speed $v_2 < v_1$.
    He enters the water at point $M(x; 0)$ where $0 \le x \le d$.
    a) Express the total travel time $T(x)$ to reach the swimmer.
    b) Compute $T'(x)$ and prove that travel time is minimized when $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$ (Snell's law of optical refraction!).
25. **Rolle's Theorem (Intuitive Discovery):**
    Let $f$ be a differentiable function on $[a; b]$ such that $f(a) = f(b) = 0$.
    Provide an intuitive explanation using the skier why there must exist at least one point $c \in ]a; b[$ where $f'(c) = 0$.

---

### Solutions

**1.** $f'(x) = 5(3x^2) - 4(2x) + 7(1) - 0 = 15x^2 - 8x + 7$.

**2.** $g'(x) = 3\left(\frac{1}{2\sqrt{x}}\right) - 4\left(-\frac{1}{x^2}\right) = \frac{3}{2\sqrt{x}} + \frac{4}{x^2}$.

**3.** $f'(x) = 2x - 2$. At $x = 3$: $f'(3) = 2(3) - 2 = 4$.

**4.** $f(1) = 1^2 = 1$. $f'(x) = 2x \implies f'(1) = 2$.
Tangent line: $y = f'(1)(x - 1) + f(1) = 2(x - 1) + 1 = 2x - 1$.

**5.** $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x - 1)(x + 1)$.
Horizontal tangent $\iff f'(x) = 0 \iff x = 1$ or $x = -1$.
The points are $(1; -2)$ and $(-1; 2)$.

**6.** Quotient formula $\frac{u}{v}$: $u(x) = 2x+1 \implies u'=2$; $v(x) = x-3 \implies v'=1$.
$f'(x) = \frac{2(x-3) - (2x+1)(1)}{(x-3)^2} = \frac{2x - 6 - 2x - 1}{(x-3)^2} = -\frac{7}{(x-3)^2}$.

**7.** Product rule: $u = x^2+1 \implies u'=2x$; $v = 3x-2 \implies v'=3$.
$h'(x) = 2x(3x-2) + (x^2+1)(3) = 6x^2 - 4x + 3x^2 + 3 = 9x^2 - 4x + 3$.

**8.** $f'(x) = -4x + 8 = -4(x - 2)$.
$f'(x) > 0$ if $x < 2$ (the function $f$ is strictly increasing on $]-\infty; 2]$);
$f'(x) < 0$ if $x > 2$ (the function $f$ is strictly decreasing on $[2; +\infty[$).

**9.** Difference quotient at $3$: $\frac{|3+h-3| - |0|}{h} = \frac{|h|}{h}$.
As $h \to 0^+$, the limit is $+1$; as $h \to 0^-$, the limit is $-1$.
Since the two one-sided limits differ, $f$ is not differentiable at 3 (it has a sharp corner point).

**10.** Let $f(x) = \sqrt{x}$. We have $f(1) = 1$ and $f'(1) = \frac{1}{2\sqrt{1}} = \frac{1}{2}$.
The local linear approximation at 1 is $f(1+h) \approx f(1) + h f'(1) = 1 + \frac{1}{2}h$.
For example, $\sqrt{1.04} \approx 1 + \frac{0.04}{2} = 1.02$ (the true value is $1.0198\dots$).

**11.** $f'(x) = x^2 - 2x - 3 = (x - 3)(x + 1)$.
Roots: $x = -1$ and $x = 3$. Parabola opening upward.
- $f'(x) > 0$ on $]-\infty; -1[ \cup ]3; +\infty[$ ($f$ increasing);
- $f'(x) < 0$ on $]-1; 3[$ ($f$ decreasing).
Extrema:
$f(-1) = -\frac{1}{3} - 1 + 3 + 4 = \frac{17}{3} \approx 5.67$ (local maximum at $-1$);
$f(3) = 9 - 9 - 9 + 4 = -5$ (local minimum at $3$).

**12.**
a) $u(x) = x^2 - 3x + 6 \implies u'=2x - 3$; $v(x) = x-1 \implies v'=1$.
$f'(x) = \frac{(2x-3)(x-1) - (x^2-3x+6)(1)}{(x-1)^2} = \frac{2x^2 - 5x + 3 - x^2 + 3x - 6}{(x-1)^2} = \frac{x^2 - 2x - 3}{(x-1)^2}$.
The numerator factors as $(x - 3)(x + 1)$.
b) On $]1; +\infty[$, the denominator $(x-1)^2 > 0$ and $x+1 > 0$. The sign of $f'(x)$ depends solely on $x - 3$.
$f'(x) < 0$ on $]1; 3[$ and $f'(x) > 0$ on $]3; +\infty[$.
Thus $f$ attains an absolute minimum at $x = 3$, equal to $f(3) = \frac{9 - 9 + 6}{3 - 1} = \frac{6}{2} = 3$.

**13.** The tangent line at abscissa $a$ has equation $y = f'(a)(x - a) + f(a)$.
Here $f(a) = -a^2 + 4a - 1$ and $f'(a) = -2a + 4$.
The equation is $y = (-2a + 4)(x - a) - a^2 + 4a - 1 = (-2a + 4)x + 2a^2 - 4a - a^2 + 4a - 1 = (-2a + 4)x + a^2 - 1$.
This line passes through the origin $(0; 0)$ if and only if its $y$-intercept is zero:
$a^2 - 1 = 0 \iff a = 1$ or $a = -1$.
There exist **two** such tangent lines: at $x = 1$ (equation $y = 2x$) and at $x = -1$ (equation $y = 6x$).

**14.**
a) For $h > 0$: $\frac{f(h) - f(0)}{h} = \frac{h\sqrt{h} - 0}{h} = \sqrt{h}$.
As $h \to 0^+$, $\lim \sqrt{h} = 0$. Hence $f$ is differentiable at 0 with $f'(0) = 0$.
b) Product rule for $x > 0$: $f'(x) = (1)\sqrt{x} + x\left(\frac{1}{2\sqrt{x}}\right) = \sqrt{x} + \frac{x}{2\sqrt{x}} = \sqrt{x} + \frac{\sqrt{x}}{2} = \frac{3}{2}\sqrt{x}$.
As $x \to 0$, $\frac{3}{2}\sqrt{x} \to 0$, matching $f'(0) = 0$ perfectly.

**15.** At $x = 0$, $f(0) = 0$. $f'(x) = 3x^2 - 6x + 1 \implies f'(0) = 1$.
The tangent line at 0 has equation $y = 1(x - 0) + 0 \iff y = x$.
Intersection with the curve: $f(x) = x \iff x^3 - 3x^2 + x = x \iff x^3 - 3x^2 = 0 \iff x^2(x - 3) = 0$.
Roots: $x = 0$ (double root, tangency point) and $x = 3$.
For $x = 3$, $y = 3$. The second intersection point is $B(3; 3)$.

**16.**
a) $v(t) = z'(t) = -10t + 20$.
b) Altitude is maximized when velocity vanishes: $-10t + 20 = 0 \iff t = 2$ seconds.
Maximum height: $z(2) = -5(4) + 20(2) + 1.5 = -20 + 40 + 1.5 = 21.5$ meters.

**17.**
- Base case ($n=1$): $f_1(x) = x$, derivative is $1 = 1 \cdot x^0$. Holds.
- Inductive step: Assume true for $n$: $(x^n)' = n x^{n-1}$.
  Then $x^{n+1} = x^n \cdot x$. By the product rule:
  $(x^{n+1})' = (x^n)' \cdot x + x^n \cdot (x)' = (n x^{n-1}) \cdot x + x^n \cdot 1 = n x^n + x^n = (n+1)x^n$.
  The formula holds for $n+1$.
- Conclusion: By induction, for all $n \ge 1$, $(x^n)' = n x^{n-1}$.

**18.** $f(3) = 5 \iff \frac{3a + b}{3 - 2} = 5 \iff 3a + b = 5$.
Derivative: $f'(x) = \frac{a(x-2) - (ax+b)(1)}{(x-2)^2} = \frac{ax - 2a - ax - b}{(x-2)^2} = \frac{-2a - b}{(x-2)^2}$.
At $x = 3$, $f'(3) = \frac{-2a - b}{(3-2)^2} = -2a - b = -7 \iff 2a + b = 7$.
Solve the system:
$(3a + b) - (2a + b) = 5 - 7 \iff a = -2$.
Then $b = 5 - 3(-2) = 5 + 6 = 11$.
Thus $a = -2$ and $b = 11$.

**19.** Let $x$ denote the length of each of the two sides perpendicular to the cliff. The side parallel to the cliff then has length $100 - 2x$.
The enclosed area is $A(x) = x(100 - 2x) = -2x^2 + 100x$, for $x \in ]0; 50[$.
Derivative: $A'(x) = -4x + 100$.
$A'(x) = 0 \iff 4x = 100 \iff x = 25$ meters.
Since $A''(x) = -4 < 0$, this yields a maximum.
The parallel side measures $100 - 2(25) = 50$ meters.
The optimal enclosure is $25\text{ m} \times 50\text{ m}$, yielding a maximal area of $1250\text{ m}^2$.

**20.**
a) The volume of a cylinder is $V = \pi r^2 h = 1000 \implies h = \frac{1000}{\pi r^2}$.
b) Total surface area includes the top and bottom circular lids and the lateral wall:
$S(r) = 2(\pi r^2) + 2\pi r h = 2\pi r^2 + 2\pi r \left(\frac{1000}{\pi r^2}\right) = 2\pi r^2 + \frac{2000}{r}$.
c) Differentiating with respect to $r$:
$S'(r) = 4\pi r - \frac{2000}{r^2} = \frac{4\pi r^3 - 2000}{r^2}$.
The minimum occurs when $S'(r) = 0 \iff 4\pi r^3 = 2000 \iff 2\pi r^3 = 1000$.
Since $1000 = \pi r^2 h$, substituting yields:
$2\pi r^3 = \pi r^2 h \iff 2r = h$.
The height must exactly equal the base diameter.

**21.** Let $M(x; x^2)$ be a point on the parabola.
The squared distance is $AM^2 = (x - 0)^2 + (x^2 - 2)^2 = x^2 + x^4 - 4x^2 + 4 = x^4 - 3x^2 + 4$.
Let $g(x) = x^4 - 3x^2 + 4$.
Derivative: $g'(x) = 4x^3 - 6x = 2x(2x^2 - 3)$.
Roots: $x = 0$ or $x^2 = \frac{3}{2} \iff x = \pm \sqrt{\frac{3}{2}}$.
At $x = 0$, $g(0) = 4$ (distance 2).
At $x = \pm \sqrt{\frac{3}{2}}$, $g = \frac{9}{4} - \frac{9}{2} + 4 = \frac{7}{4}$, giving distance $\sqrt{7}/2 \approx 1.32 < 2$.
The closest points are $M_1\left(\sqrt{\frac{3}{2}}; \frac{3}{2}\right)$ and $M_2\left(-\sqrt{\frac{3}{2}}; \frac{3}{2}\right)$.
The vector $\vec{AM_1} = \begin{pmatrix} \sqrt{3/2} \\ -1/2 \end{pmatrix}$.
The tangent slope at that point is $f'(x) = 2x = 2\sqrt{3/2}$, so a direction vector of the tangent is $\vec{u}\begin{pmatrix} 1 \\ 2\sqrt{3/2} \end{pmatrix}$.
Dot product: $\vec{AM_1} \cdot \vec{u} = \sqrt{\frac{3}{2}} \times 1 + \left(-\frac{1}{2}\right) \times 2\sqrt{\frac{3}{2}} = \sqrt{\frac{3}{2}} - \sqrt{\frac{3}{2}} = 0$.
The vector is orthogonal to the tangent: the shortest path is perpendicular to the curve.

**22.**
a) If $x \ge 0$, $f(x) = x(x) = x^2$. If $x < 0$, $f(x) = x(-x) = -x^2$.
b) Difference quotient at 0: $\frac{f(h) - f(0)}{h} = \frac{h|h|}{h} = |h|$.
As $h \to 0$, $|h| \to 0$ from both sides!
Therefore $f$ is differentiable at 0 and $f'(0) = 0$.
c) Contrary to popular belief, the presence of an absolute value does not necessarily create a sharp corner point: here, the factor $x$ cushions the point, forcing it to adopt a flat horizontal tangent.

**23.** Let $y = mx + p$ be such a common tangent.
It is tangent to $y = x^2$ at abscissa $a$: so $m = 2a$ and $p = a^2 - 2a(a) = -a^2$.
It is tangent to $y = -x^2 + 4x - 6$ at abscissa $b$:
so $m = -2b + 4$ and $p = (-b^2 + 4b - 6) - (-2b + 4)b = b^2 - 6$.
Equating slopes and intercepts:
1) $2a = -2b + 4 \iff a + b = 2 \iff b = 2 - a$.
2) $-a^2 = b^2 - 6$.
Substitute $b$: $-a^2 = (2 - a)^2 - 6 = 4 - 4a + a^2 - 6 = a^2 - 4a - 2$.
$2a^2 - 4a - 2 = 0 \iff a^2 - 2a - 1 = 0$.
$\Delta = 4 - 4(-1) = 8 = (2\sqrt{2})^2$.
$a = \frac{2 \pm 2\sqrt{2}}{2} = 1 \pm \sqrt{2}$.
There are two common tangent lines. For $a = 1 + \sqrt{2}$, $m = 2 + 2\sqrt{2}$ and $p = -(1+\sqrt{2})^2 = -3 - 2\sqrt{2}$. The second is obtained with $a = 1 - \sqrt{2}$.

**24.**
a) Distance on sand: $d_1 = \sqrt{x^2 + a^2}$. Time on sand: $t_1 = \frac{\sqrt{x^2 + a^2}}{v_1}$.
Distance in water: $d_2 = \sqrt{(d - x)^2 + b^2}$. Time in water: $t_2 = \frac{\sqrt{(d - x)^2 + b^2}}{v_2}$.
Total travel time: $T(x) = \frac{\sqrt{x^2 + a^2}}{v_1} + \frac{\sqrt{(d - x)^2 + b^2}}{v_2}$.
b) Derivative of $\sqrt{x^2+a^2}$: $\frac{2x}{2\sqrt{x^2+a^2}} = \frac{x}{\sqrt{x^2+a^2}}$.
Derivative of $\sqrt{(d-x)^2+b^2}$: $\frac{-2(d-x)}{2\sqrt{(d-x)^2+b^2}} = -\frac{d-x}{\sqrt{(d-x)^2+b^2}}$.
Thus $T'(x) = \frac{x}{v_1 \sqrt{x^2 + a^2}} - \frac{d - x}{v_2 \sqrt{(d - x)^2 + b^2}}$.
Geometrically observe that $\frac{x}{\sqrt{x^2+a^2}} = \sin\theta_1$ and $\frac{d-x}{\sqrt{(d-x)^2+b^2}} = \sin\theta_2$ (angles relative to the normal to the shoreline).
Time is minimized when $T'(x) = 0 \iff \frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$.
This is Fermat-Snell's Law of Refraction: light minimizes its travel time!

**25.** The skier starts at elevation 0 at $a$ and returns to elevation 0 at $b$.
If he stayed on flat terrain the entire way ($f$ constant), the slope was zero everywhere.
If he climbed, he had to go up, reach a highest elevation (a maximum), then descend. At the exact summit of that hill, his skis were necessarily horizontal ($f'(c) = 0$).
If he dipped into a valley, he reached a lowest elevation (a minimum) before climbing back up: at the bottom of the valley, the skis were likewise horizontal ($f'(c) = 0$).
In all cases, there must exist at least one point where the tangent is perfectly horizontal.

---

### The Question That Opens What Follows

We have seen that the derivative measures the rate at which a function grows.
For a polynomial, differentiation lowers the degree. But imagine a living population: a bacterial colony in a Petri dish. The larger the colony, the more individuals divide, and the faster the population expands!
Does there exist anywhere in the universe a magical function that is **strictly equal to its own derivative**: $f' = f$? A function whose slope underfoot is at every millisecond equal to its current elevation? That is the mystery of the **exponential function**, in the next chapter.
