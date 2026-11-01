# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 49: The Swing and Oscillating Functions

> *“The pendular motion revealed to me that time is not a straight line fleeing away, but a breath that endlessly returns.”*
> — Inspired by the observations of Galileo Galilei (1583)

---

### What You Are About to Discover

- Why the back-and-forth swing of a pendulum is nothing other than **the shadow of a point moving around a circle at constant speed**.
- The geometry of the **unit trigonometric circle** and why the **radian** is the only natural angular measure for calculus.
- Essential symmetry properties: **evenness**, **oddness**, **$2\pi$-periodicity**, and sum and double-angle formulas.
- Differentiation of sine and cosine: the fundamental geometric proof that $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$, why $(\sin)' = \cos$, and $(\cos)' = -\sin$.
- The mystery of the quarter-turn: why taking the derivative advances phase by $\dfrac{\pi}{2}$.
- Composite derivatives of the form $t \mapsto \cos(\omega t + \varphi)$ and the harmonic oscillator differential equation $y'' + \omega^2 y = 0$.
- Comprehensive curve sketching: monotonicity, extrema, inflection points, and concavity of sinusoidal waveforms.
- Concrete real-world applications: acoustic soundwaves, $50\text{ Hz}$ alternating mains current, ocean tides, and seismology.

---

### 1. The Problem: The Pisa Chandelier and the Shadow of the Circle

#### 1.1 Galileo's Insight

In **1583**, a nineteen-year-old medical student named **Galileo Galilei** attended a religious service in the Cathedral of Pisa. His attention drifted toward the vaulted ceiling. A sacristan had just lit a large chandelier suspended from an immense iron chain and, in releasing it, set it swaying in a slow, steady rhythm.

Galileo noticed something extraordinary: whether the amplitude of the swing was broad at the beginning or shrank to a barely perceptible tremor as friction slowed it down, **the time required to complete a full back-and-forth cycle appeared precisely constant**.

Lacking a pocket watch—high-precision mechanical timekeepers had not yet been invented—Galileo took his own pulse at his wrist. He counted beats: four heartbeats for a wide swing, four heartbeats for a medium swing, four heartbeats for a tiny flutter. This was the discovery of the **isochronism of small pendular oscillations**.

This phenomenon is universal: a child's swing at the playground, a plucked violin string, water sloshing in an enclosed bay, alternating electrons surging through a radio antenna—all obey this very same fundamental rhythmic cadence.

```
                  Suspension point
                        │
                        │ \  θ
                        │  \
                        │   \ L
                        │    \
                        │     ●  Mass m
                        │    /
                  ←─────┼───►  Horizontal back-and-forth
```

#### 1.2 From the Circle to the Wave: Optical Projection

How can we represent this oscillatory back-and-forth movement mathematically?
Consider a simple thought experiment:
1. A large vertical wheel rotates at constant speed in a darkened room. A single bright luminous LED $M$ is fixed to its outer rim.
2. A distant light source projects the shadow of the dot $M$ horizontally onto a flat vertical wall behind the wheel.

What path does the shadow trace on the wall?
- When the dot reaches the top of the wheel, its shadow climbs to the highest point on the wall, momentarily slows down, comes to an infinitesimal standstill, and reverses downward.
- As the shadow passes through the horizontal center line, it travels at its maximum speed.
- At the bottom, it decelerates, halts instantaneously, and accelerates back upward.

The shadow on the wall executes **the exact motion of a pendulum or a swing**!
If we pull a strip of paper vertically past the wall at a constant speed, the moving shadow traces a pristine periodic curve: **a sinusoid**.

```
           Rotating wheel                              Wave traced on paper
                ▲ y                                               y ▲
            . ─── .                                                 │     _--_
         .    M    .          ─── Projection ───►                  1 ┼   /    \
        /     │     \                                               │  /      \
       │      │      │                                            0 ┼─*────────*────*──► t
        \     │     /                                               │           \  /
         .    O    .                                               -1 ┼            --
            . ─── .                                                 │  0    π   2π
```

Rectilinear oscillation is nothing other than **the orthogonal projection of uniform circular motion**. To understand the swing, we must master the geometry of the circle.

---

### 2. The Trigonometric Circle and Fundamental Symmetries

#### 2.1 The Radian: The Natural Measure of Arc Length

In elementary school, you learned to measure angles in degrees ($360^\circ$ for a full revolution). The number 360 was chosen by ancient Babylonian astronomers because it is divisible by 2, 3, 4, 5, 6, 8, 9, 10, 12, etc., and closely approximates the 365 days of a solar year.

In calculus and physics, however, degrees are an arbitrary and cumbersome choice: differentiating trigonometric functions expressed in degrees would introduce an unsightly scaling factor of $\dfrac{\pi}{180}$ into every single derivative!

The intrinsic, natural mathematical unit is the **radian**:

> **📐 Definition of the Radian —**
> In the Cartesian plane equipped with an orthonormal coordinate system $(O; \vec{i}, \vec{j})$, the **trigonometric circle** (or unit circle) $\mathcal{C}$ is the circle centered at the origin $O(0\,;0)$ with radius $R = 1$, oriented in the **counter-clockwise direction** (the positive or direct mathematical orientation).
> The measure of an angle in **radians** is defined as the **arc length** subtended by that angle along the unit circle of radius 1.

Since the circumference of a circle of radius 1 is $2\pi R = 2\pi$, a full revolution of $360^\circ$ corresponds to an angle of **$2\pi$ radians**.

| Degrees | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|---|---|---|---|---|---|---|---|---|
| **Radians** | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

#### 2.2 Wrapping the Real Line Around the Circle

Imagine a graduated real number line tangent to the trigonometric circle at the base point $I(1\,;0)$. Wrap this infinite line around the circumference:
- Positive numbers wrap counter-clockwise (upward and around);
- Negative numbers wrap clockwise (downward and around).

To every real number $x \in \mathbb{R}$ corresponds a unique point $M$ on the unit circle.

> **📐 Definition of the Cosine and Sine Functions —**
> For every real number $x$, let $M$ be the point on the unit circle paired with $x$ by wrapping the real number line.
> - The **cosine** of $x$, denoted $\cos x$, is the **abscissa** ($x$-coordinate) of point $M$.
> - The **sine** of $x$, denoted $\sin x$, is the **ordinate** ($y$-coordinate) of point $M$.
>
> $$M(x) = \big(\cos x \, ; \, \sin x\big).$$

```
                        y ▲
                          │  (0, 1)
                          │   . + .
                     M' . │ .       . M(x) = (cos x, sin x)
                       \  │          /
                        \ │  sin x  / |
                         \│        /  |
        ──────────────────┼───────*───┼────────► x
               (-1, 0)    │ O   cos x (1, 0)
                          │
                          │   . - .
                          │  (0, -1)
```

#### 2.3 Immediate Consequences and Special Angles

1. **Absolute Bounds:** Because the circle has unit radius, the coordinates of any point $M$ are bounded between $-1$ and $1$:
   $$\text{For all } x \in \mathbb{R} : \quad -1 \leq \cos x \leq 1 \quad \text{and} \quad -1 \leq \sin x \leq 1.$$

2. **The Circle Equation (Pythagorean Identity):** The right triangle formed by the coordinates of $M$ has perpendicular legs of lengths $|\cos x|$ and $|\sin x|$, and hypotenuse equal to the radius $OM = 1$. The Pythagorean theorem directly gives:
   $$\cos^2 x + \sin^2 x = 1.$$
   *(Notation reminder: $\cos^2 x$ means $(\cos x)^2$.)*

3. **Table of Special Values (Must be Mastered):**

| $x$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| **$\cos x$** | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ |
| **$\sin x$** | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ |

> **💡 Mnemonic Trick for the Sine Row:**
> Notice the pattern of square roots: $\sin 0 = \dfrac{\sqrt{0}}{2} = 0$, $\sin\dfrac{\pi}{6} = \dfrac{\sqrt{1}}{2} = \dfrac{1}{2}$, $\sin\dfrac{\pi}{4} = \dfrac{\sqrt{2}}{2}$, $\sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2}$, $\sin\dfrac{\pi}{2} = \dfrac{\sqrt{4}}{2} = 1$. The numerators march upward from $\sqrt{0}$ to $\sqrt{4}$, while the cosine row runs in reverse!

#### 2.4 Periodicity and Parity: The Power of Symmetry

Adding a full revolution around the circle corresponds to adding $2\pi$ to the wrapped arc length: the terminal point $M$ lands on the exact same location.

> **📐 Periodicity —**
> The cosine and sine functions are **periodic with period $2\pi$** (or $2\pi$-periodic). For every real number $x$ and every integer $k \in \mathbb{Z}$:
> $$\cos(x + 2k\pi) = \cos x \quad \text{and} \quad \sin(x + 2k\pi) = \sin x.$$

Now consider geometric reflections on the circle:
- The points associated with $x$ and $-x$ are symmetric with respect to **the horizontal axis $(Ox)$**. They share the same $x$-coordinate and have opposite $y$-coordinates.

> **📐 Parity —**
> - The cosine function is **even**: $\cos(-x) = \cos x$. Its Cartesian graph is symmetric with respect to **the vertical axis $(Oy)$**.
> - The sine function is **odd**: $\sin(-x) = -\sin x$. Its Cartesian graph is symmetric with respect to **the origin $O(0\,;0)$**.

#### 2.5 Associated Angle Identities (Reflections of the Circle)

Rotating point $M(x)$ by a half-turn ($+\pi$) or reflecting it across the coordinate axes produces key geometric relationships:

| Transformation | Angle | Cosine | Sine | Geometric Interpretation |
|---|---|---|---|---|
| Half-turn | $x + \pi$ | $-\cos x$ | $-\sin x$ | Central symmetry through $O$ |
| Supplementary angle | $\pi - x$ | $-\cos x$ | $\sin x$ | Reflection across vertical axis $(Oy)$ |
| Quarter-turn | $x + \dfrac{\pi}{2}$ | $-\sin x$ | $\cos x$ | Rotation by $+90^\circ$ |
| Complementary angle | $\dfrac{\pi}{2} - x$ | $\sin x$ | $\cos x$ | Reflection across diagonal line $y = x$ |

> **💡 Did you know? The Word "Cosine":**
> The prefix *co-* stands for *complementi*: the **cosine** of an angle is literally the **sine of the complementary angle** ($\cos x = \sin(\frac{\pi}{2}-x)$).

#### 2.6 Addition and Double-Angle Formulas

These algebraic identities decompose trigonometric functions of composite angles into products of elementary components:

> **📐 Addition Formulas —** For all real numbers $a$ and $b$:
> $$\cos(a + b) = \cos a \cos b - \sin a \sin b$$
> $$\cos(a - b) = \cos a \cos b + \sin a \sin b$$
> $$\sin(a + b) = \sin a \cos b + \cos a \sin b$$
> $$\sin(a - b) = \sin a \cos b - \cos a \sin b$$

> **📐 Double-Angle Formulas —** Setting $a = b = x$:
> $$\sin(2x) = 2 \sin x \cos x$$
> $$\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$$

> **Worked Example 1 — Exact Evaluation of $\cos\left(\dfrac{\pi}{12}\right)$.**
> Observe that $\dfrac{\pi}{12} = \dfrac{\pi}{3} - \dfrac{\pi}{4}$.
> Applying the cosine difference formula:
> $$\cos\left(\dfrac{\pi}{12}\right) = \cos\left(\dfrac{\pi}{3} - \dfrac{\pi}{4}\right) = \cos\dfrac{\pi}{3}\cos\dfrac{\pi}{4} + \sin\dfrac{\pi}{3}\sin\dfrac{\pi}{4}.$$
> Substituting the standard values:
> $$\cos\left(\dfrac{\pi}{12}\right) = \left(\dfrac{1}{2}\right)\left(\dfrac{\sqrt{2}}{2}\right) + \left(\dfrac{\sqrt{3}}{2}\right)\left(\dfrac{\sqrt{2}}{2}\right) = \dfrac{\sqrt{2} + \sqrt{6}}{4}.$$

---

### 3. Differentiation of Sine and Cosine: The Right-Angle Turn

To compute the instantaneous velocity of a pendulum or the acceleration of an oscillator, we must differentiate sine and cosine. But first, a fundamental question arises: **what is the derivative of $\sin x$ at $x = 0$?**

#### 3.1 The Fundamental Limit $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$

The difference quotient of the sine function at 0 is:
$$\tau(x) = \dfrac{\sin x - \sin 0}{x - 0} = \dfrac{\sin x}{x}.$$
As $x \to 0$, this yields the indeterminate form “$\dfrac{0}{0}$”. We resolve this using an elegant geometric comparison of areas.

> **📐 Fundamental Lemma (Trigonometric Squeeze) —**
> For every real number $x \in \left]0\,; \dfrac{\pi}{2}\right[$:
> $$\sin x \leq x \leq \tan x \quad \left(\text{where } \tan x = \dfrac{\sin x}{\cos x}\right).$$

> **✍️ Geometric Proof (Required Curriculum Proof) —**
> On the unit circle centered at $O$ with radius 1, consider:
> - The point $A(1\,;0)$;
> - The point $M(\cos x\,; \sin x)$ associated with an angle $x \in \left]0\,; \dfrac{\pi}{2}\right[$;
> - The point $T(1\,; \tan x)$, which is the intersection of the ray $[OM)$ with the vertical tangent line at $A$.
>
> We compare the areas of three geometric shapes nested inside one another:
> 1. The **inner triangle** $OAM$: base is $OA = 1$, height is the ordinate of $M$, which is $\sin x$.
>    $$\text{Area}(OAM) = \dfrac{\text{base} \times \text{height}}{2} = \dfrac{1 \times \sin x}{2} = \dfrac{\sin x}{2}.$$
> 2. The **circular sector** $OAM$ (the circular wedge of radius 1 subtending an angle $x$):
>    Since the area of a complete disk of radius 1 is $\pi(1)^2 = \pi$ for an angle of $2\pi$, the area of a sector of angle $x$ radians is directly proportional:
>    $$\text{Area}(\text{sector } OAM) = \dfrac{x}{2\pi} \times \pi = \dfrac{x}{2}.$$
> 3. The **outer triangle** $OAT$: base is $OA = 1$, height is $AT = \tan x$.
>    $$\text{Area}(OAT) = \dfrac{\text{base} \times \text{height}}{2} = \dfrac{1 \times \tan x}{2} = \dfrac{\tan x}{2}.$$
>
> Because triangle $OAM$ is strictly contained within circular sector $OAM$, which in turn is strictly contained within triangle $OAT$:
> $$\text{Area}(OAM) \leq \text{Area}(\text{sector } OAM) \leq \text{Area}(OAT) \iff \dfrac{\sin x}{2} \leq \dfrac{x}{2} \leq \dfrac{\tan x}{2}.$$
> Multiplying by 2 yields:
> $$\sin x \leq x \leq \tan x. \quad \blacksquare$$

```
                   T (1, tan x)
                   ▲
                   │\
                   │ \
                   │  \   M (cos x, sin x)
                   │   *
                   │  /│\
                   │ / │ \
                   │/  │  \
                   ┼───*───┼──►
                   O  cos  A (1, 0)
```

> **📐 Theorem — Fundamental Limit at 0:**
> $$\lim_{x \to 0} \dfrac{\sin x}{x} = 1.$$

> **✍️ Proof —**
> For every $x \in \left]0\,; \dfrac{\pi}{2}\right[$, we have $\sin x > 0$. Divide the inequality $\sin x \leq x \leq \dfrac{\sin x}{\cos x}$ by $\sin x$:
> $$1 \leq \dfrac{x}{\sin x} \leq \dfrac{1}{\cos x}.$$
> Taking reciprocals (all quantities being strictly positive):
> $$\cos x \leq \dfrac{\sin x}{x} \leq 1.$$
> This inequality is equally valid for $x \in \left]-\dfrac{\pi}{2}\,; 0\right[$, because $\cos(-x) = \cos x$ and $\dfrac{\sin(-x)}{-x} = \dfrac{-\sin x}{-x} = \dfrac{\sin x}{x}$.
> By the continuity of cosine at 0, $\lim\limits_{x \to 0} \cos x = \cos 0 = 1$.
> Applying the **Squeeze Theorem**:
> $$\lim_{x \to 0} \dfrac{\sin x}{x} = 1. \quad \blacksquare$$

> **Fundamental Corollary — The Limit of $\dfrac{1 - \cos x}{x^2}$ at 0:**
> $$\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2} \quad \text{and consequently} \quad \lim_{x \to 0} \dfrac{\cos x - 1}{x} = 0.$$
>
> *Proof:*
> Use the double-angle formula $\cos(2u) = 1 - 2\sin^2 u$ with $u = \dfrac{x}{2}$, giving $1 - \cos x = 2\sin^2\left(\dfrac{x}{2}\right)$.
> Then:
> $$\dfrac{1 - \cos x}{x^2} = \dfrac{2 \sin^2(x/2)}{x^2} = \dfrac{2}{4} \times \left(\dfrac{\sin(x/2)}{x/2}\right)^2 = \dfrac{1}{2} \left(\dfrac{\sin(x/2)}{x/2}\right)^2.$$
> As $x \to 0$, $u = \dfrac{x}{2} \to 0$, so $\dfrac{\sin(x/2)}{x/2} \to 1$.
> By the product of limits: $\lim\limits_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2} \times 1^2 = \dfrac{1}{2}$.
> Furthermore, $\dfrac{\cos x - 1}{x} = -x \times \dfrac{1 - \cos x}{x^2} \to 0 \times \dfrac{1}{2} = 0$. $\blacksquare$

#### 3.2 Calculating the Derivatives of Sine and Cosine

> **📐 Theorem (Required Curriculum Proofs) —**
> The functions $\sin$ and $\cos$ are differentiable on $\mathbb{R}$, and for every real number $x$:
> $$\sin'(x) = \cos x \quad \text{and} \quad \cos'(x) = -\sin x.$$

> **✍️ Proof for $\sin'(x)$ —**
> Let $x \in \mathbb{R}$ be fixed and let $h \neq 0$. Form the difference quotient of sine between $x$ and $x+h$:
> $$\tau(h) = \dfrac{\sin(x+h) - \sin x}{h}.$$
> Using the sine addition formula: $\sin(x+h) = \sin x \cos h + \cos x \sin h$.
> Hence:
> $$\tau(h) = \dfrac{\sin x \cos h + \cos x \sin h - \sin x}{h} = \sin x \left(\dfrac{\cos h - 1}{h}\right) + \cos x \left(\dfrac{\sin h}{h}\right).$$
> As $h \to 0$:
> - $\lim\limits_{h \to 0} \dfrac{\cos h - 1}{h} = 0$;
> - $\lim\limits_{h \to 0} \dfrac{\sin h}{h} = 1$.
>
> Therefore:
> $$\lim_{h \to 0} \tau(h) = \sin x \times 0 + \cos x \times 1 = \cos x.$$
> The sine function is differentiable for all $x \in \mathbb{R}$, and $\sin'(x) = \cos x$. $\blacksquare$

> **✍️ Proof for $\cos'(x)$ —**
> Using the cosine addition formula:
> $$\dfrac{\cos(x+h) - \cos x}{h} = \dfrac{\cos x \cos h - \sin x \sin h - \cos x}{h} = \cos x \left(\dfrac{\cos h - 1}{h}\right) - \sin x \left(\dfrac{\sin h}{h}\right).$$
> Taking the limit as $h \to 0$:
> $$\lim_{h \to 0} \dfrac{\cos(x+h) - \cos x}{h} = \cos x \times 0 - \sin x \times 1 = -\sin x.$$
> The cosine function is differentiable on $\mathbb{R}$, and $\cos'(x) = -\sin x$. $\blacksquare$

#### 3.3 The Mystery of the Quarter-Turn: Kinematic View

Why is the derivative of sine cosine, and the derivative of cosine **minus** sine?
Notice what happens when we advance phase by a quarter-turn, which is an angle of $+\dfrac{\pi}{2}$:
- $\sin\left(x + \dfrac{\pi}{2}\right) = \cos x$;
- $\cos\left(x + \dfrac{\pi}{2}\right) = -\sin x$.

> **Differentiating a sinusoid shifts it forward in phase by exactly one quarter of a cycle ($\dfrac{\pi}{2}$ radians)!**

In kinematics, if a particle travels around the unit circle counter-clockwise with position vector $\vec{OM}(t) = \cos t \, \vec{i} + \sin t \, \vec{j}$, its instantaneous velocity vector $\vec{v}(t) = \dfrac{d\vec{OM}}{dt}$ is:
$$\vec{v}(t) = -\sin t \, \vec{i} + \cos t \, \vec{j}.$$
Notice that the dot product $\vec{OM}(t) \cdot \vec{v}(t) = \cos t(-\sin t) + \sin t(\cos t) = 0$!
The velocity vector is **strictly perpendicular** to the radius vector: it points tangent to the circle in the direction of motion, exactly $90^\circ$ ahead of the position.

```
                      y ▲
                        │        velocity v (perpendicular to OM)
                        │         ▲
                        │        /
                        │       * M (cos t, sin t)
                        │      /
                        │     / radius OM
                        │    /
        ────────────────┼───*────────────► x
                        │  O
```

#### 3.4 Chain Rule with Trigonometric Functions

Applying the composite differentiation theorem $(f \circ u)' = u' \times (f' \circ u)$:

> **📐 Composition Formulas —** Let $u$ be a differentiable function on an interval $I$:
> 1. $\big(\sin(u(x))\big)' = u'(x) \cos(u(x))$
> 2. $\big(\cos(u(x))\big)' = -u'(x) \sin(u(x))$
>
> In particular, for harmonic oscillations $u(t) = \omega t + \varphi$ with constants $\omega, \varphi \in \mathbb{R}$:
> $$\big(\sin(\omega t + \varphi)\big)' = \omega \cos(\omega t + \varphi)$$
> $$\big(\cos(\omega t + \varphi)\big)' = -\omega \sin(\omega t + \varphi)$$

> **Worked Example 2 — Composite Derivatives.**
> 1. $f_1(x) = \sin(3x - \pi) \implies f'_1(x) = 3 \cos(3x - \pi)$.
> 2. $f_2(x) = \cos(x^2 + 1) \implies f'_2(x) = -(2x) \sin(x^2 + 1) = -2x \sin(x^2 + 1)$.
> 3. $f_3(x) = \sin^3(x) = (\sin x)^3 \implies f'_3(x) = 3(\sin x)^2 \times (\sin x)' = 3\sin^2 x \cos x$.
> 4. $f_4(x) = e^{-x} \cos(2x) \implies$ product rule $(uv)' = u'v + uv'$:
>    $$f'_4(x) = (-e^{-x})\cos(2x) + e^{-x}(-2\sin(2x)) = -e^{-x}\big(\cos(2x) + 2\sin(2x)\big).$$

#### 3.5 Second Derivatives and the Harmonic Oscillator Equation

Differentiating the function $f(t) = \cos(\omega t)$ twice:
- $f'(t) = -\omega \sin(\omega t)$;
- $f''(t) = -\omega \times \big(\omega \cos(\omega t)\big) = -\omega^2 \cos(\omega t) = -\omega^2 f(t)$.

Rearranging:
$$f''(t) + \omega^2 f(t) = 0.$$

> **💡 Master Discovery —**
> Sinusoidal functions are the **general solutions** to the second-order linear differential equation:
> $$y'' + \omega^2 y = 0.$$
> This is the foundational equation of classical mechanics: governing mass-spring systems (Hooke's law $m a = -k x$), inductor-capacitor LC circuits, acoustic vibrations, and electromagnetic waves!

---

### 4. Comprehensive Analysis of the Sine and Cosine Functions

Because sine and cosine are periodic with period $2\pi$, it suffices to study them on an interval of length $2\pi$, such as $[-\pi\,; \pi]$.
Exploiting parity:
- For cosine (even): analyze on $[0\,; \pi]$, then reflect across the vertical axis $(Oy)$ onto $[-\pi\,; \pi]$.
- For sine (odd): analyze on $[0\,; \pi]$, then reflect through the origin $O(0\,;0)$ onto $[-\pi\,; \pi]$.

Finally, translate the pattern indefinitely left and right by integer multiples of $2\pi \vec{i}$.

#### 4.1 Analysis of the Cosine Function

On the interval $[0\,; \pi]$:
- $\cos'(x) = -\sin x$.
- For all $x \in \; ]0\,; \pi[$, $\sin x > 0$, so $\cos'(x) < 0$.
- The cosine function is therefore **strictly decreasing** on $[0\,; \pi]$.
- $\cos 0 = 1$, $\cos\left(\dfrac{\pi}{2}\right) = 0$, and $\cos \pi = -1$.

Variation table on $[-\pi\,; \pi]$:

```
    x    │ -π                0                π
─────────┼───────────────────────────────────────
  cos'(x)│        +          0        -
─────────┼───────────────────┼───────────────────
         │                   1
  cos(x) │                 ↗   ↘
         │ -1                         -1
```

**Tangents and Concavity:**
- At $x = 0$, $\cos'(0) = 0$: the curve has a **horizontal tangent** at its maximum $(0\,;1)$.
- At $x = \pi$, $\cos'(\pi) = 0$: **horizontal tangent** at its minimum $(\pi\,;-1)$.
- Second derivative: $\cos''(x) = -\cos x$.
  On $\left[0\,; \dfrac{\pi}{2}\right]$, $\cos x \geq 0 \implies \cos''(x) \leq 0$: the function is **concave**.
  On $\left[\dfrac{\pi}{2}\,; \pi\right]$, $\cos x \leq 0 \implies \cos''(x) \geq 0$: the function is **convex**.
  An inflection point occurs at $x = \dfrac{\pi}{2}$, where the curve crosses the horizontal axis with a slope of $-1$.

#### 4.2 Analysis of the Sine Function

On the interval $[0\,; \pi]$:
- $\sin'(x) = \cos x$.
- On $\left[0\,; \dfrac{\pi}{2}\right[$, $\cos x > 0$: $\sin$ is **strictly increasing**.
- At $x = \dfrac{\pi}{2}$, $\cos\left(\dfrac{\pi}{2}\right) = 0$: horizontal tangent at $\left(\dfrac{\pi}{2}\,; 1\right)$.
- On $\left]\dfrac{\pi}{2}\,; \pi\right]$, $\cos x < 0$: $\sin$ is **strictly decreasing**.

Variation table on $[-\pi\,; \pi]$:

```
    x    │ -π        -π/2         0         π/2         π
─────────┼─────────────────────────────────────────────────
  sin'(x)│     -       0     +    1    +     0     -
─────────┼─────────────────────────────────────────────────
         │                   0              1
  sin(x) │                 ↗   ↘          ↗   ↘
         │ 0             -1         0              0
```

**Notable Tangents:**
- At $x = 0$, $\sin'(0) = 1$ and $\sin 0 = 0$. The tangent line at the origin is:
  $$y = x.$$
  For $x \approx 0$, the first-order approximation yields **$\sin x \approx x$**. This is the celebrated small-angle approximation widely used in physics!

```
              y ▲                     _---_ (π/2 ; 1)
                │                  _-'     '-_
              1 ┼                -'           '-
                │              /                 \  y = sin(x)
              0 ┼────────────*─────────────────────*────────► x
                │          0/ ¦                   π
             -1 ┼          /  ¦
                │        /    ¦
                │       / y = x (tangent at 0)
```

---

### 5. Solving Trigonometric Equations and Inequalities

#### 5.1 Fundamental Equations

> **🧭 Method — Solving $\cos x = \cos \alpha$:**
> Two points on the unit circle share the same abscissa if and only if their angles are equal or opposite, up to integer multiples of $2\pi$:
> $$\cos x = \cos \alpha \iff x = \alpha + 2k\pi \quad \text{or} \quad x = -\alpha + 2k\pi \quad (k \in \mathbb{Z}).$$

> **🧭 Method — Solving $\sin x = \sin \alpha$:**
> Two points on the unit circle share the same ordinate if and only if their angles are equal or supplementary ($\pi - \alpha$), up to integer multiples of $2\pi$:
> $$\sin x = \sin \alpha \iff x = \alpha + 2k\pi \quad \text{or} \quad x = \pi - \alpha + 2k\pi \quad (k \in \mathbb{Z}).$$

> **Worked Example 3 — Solving on a Specified Interval.**
> Solve $\cos(2x) = \dfrac{1}{2}$ on $[0\,; 2\pi]$.
> - Recall that $\dfrac{1}{2} = \cos\left(\dfrac{\pi}{3}\right)$.
> - The equation yields:
>   $$2x = \dfrac{\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{6} + k\pi$$
>   or
>   $$2x = -\dfrac{\pi}{3} + 2k\pi \iff x = -\dfrac{\pi}{6} + k\pi \quad (k \in \mathbb{Z}).$$
> - Select solutions lying within $[0\,; 2\pi]$:
>   - First family: $x = \dfrac{\pi}{6} + k\pi$:
>     - $k = 0 \implies x_1 = \dfrac{\pi}{6} \in [0\,; 2\pi]$;
>     - $k = 1 \implies x_2 = \dfrac{\pi}{6} + \pi = \dfrac{7\pi}{6} \in [0\,; 2\pi]$;
>     - $k = 2 \implies x = \dfrac{13\pi}{6} > 2\pi$ (out of bounds).
>   - Second family: $x = -\dfrac{\pi}{6} + k\pi$:
>     - $k = 0 \implies x = -\dfrac{\pi}{6} < 0$ (out of bounds);
>     - $k = 1 \implies x_3 = -\dfrac{\pi}{6} + \pi = \dfrac{5\pi}{6} \in [0\,; 2\pi]$;
>     - $k = 2 \implies x_4 = -\dfrac{\pi}{6} + 2\pi = \dfrac{11\pi}{6} \in [0\,; 2\pi]$.
> - Conclusion: $\mathcal{S} = \left\{ \dfrac{\pi}{6} \; ; \; \dfrac{5\pi}{6} \; ; \; \dfrac{7\pi}{6} \; ; \; \dfrac{11\pi}{6} \right\}$.

#### 5.2 Equations with Change of Variables

> **Worked Example 4 — Quadratic Trigonometric Equation.**
> Solve $2\sin^2 x - 3\sin x + 1 = 0$ on $[0\,; 2\pi[$.
> Set $X = \sin x$. The equation becomes:
> $$2X^2 - 3X + 1 = 0.$$
> $\Delta = (-3)^2 - 4(2)(1) = 9 - 8 = 1$.
> The roots for $X$ are $X_1 = \dfrac{3 - 1}{4} = \dfrac{1}{2}$ and $X_2 = \dfrac{3 + 1}{4} = 1$.
> 
> Back-substituting into $\sin x$:
> 1. $\sin x = 1 \iff x = \dfrac{\pi}{2}$.
> 2. $\sin x = \dfrac{1}{2} = \sin\left(\dfrac{\pi}{6}\right) \iff x = \dfrac{\pi}{6}$ or $x = \pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}$.
>
> The solutions in $[0\,; 2\pi[$ are: $\mathcal{S} = \left\{ \dfrac{\pi}{6} \; ; \; \dfrac{\pi}{2} \; ; \; \dfrac{5\pi}{6} \right\}$.

#### 5.3 Trigonometric Inequalities

To solve inequalities such as $\cos x \geq c$ or $\sin x < c$, read the arc directly off the unit circle by drawing the boundary line $x = c$ (vertical) or $y = c$ (horizontal).

> **Worked Example 5 — Inequality on $[-\pi\,; \pi]$.**
> Solve $\sin x \geq -\dfrac{\sqrt{2}}{2}$ on $[-\pi\,; \pi]$.
> Draw the horizontal line $y = -\dfrac{\sqrt{2}}{2}$.
> It intersects the unit circle at angles $-\dfrac{\pi}{4}$ and $-\dfrac{3\pi}{4}$.
> The region where the $y$-coordinate is greater than or equal to $-\dfrac{\sqrt{2}}{2}$ corresponds to the upper arc.
> Traversing the interval from $-\pi$ to $\pi$:
> - From $-\pi$ to $-\dfrac{3\pi}{4}$: $\sin x \geq -\dfrac{\sqrt{2}}{2}$;
> - From $-\dfrac{3\pi}{4}$ to $-\dfrac{\pi}{4}$: $\sin x < -\dfrac{\sqrt{2}}{2}$;
> - From $-\dfrac{\pi}{4}$ to $\pi$: $\sin x \geq -\dfrac{\sqrt{2}}{2}$.
>
> The solution set is:
> $$\mathcal{S} = \left[ -\pi \; ; \; -\dfrac{3\pi}{4} \right] \cup \left[ -\dfrac{\pi}{4} \; ; \; \pi \right].$$

---

### 6. The Realm of Signals and Waves: Concrete Modeling

In real physical systems, oscillations do not necessarily complete a cycle in $2\pi$ seconds, nor is their amplitude restricted to 1 unit. We describe general periodic phenomena using the canonical form of a **sinusoidal signal**:

$$s(t) = A \cos(\omega t + \varphi)$$

where:
- **$A > 0$** is the **amplitude** (peak excursion from equilibrium);
- **$\omega > 0$** is the **angular frequency** (in radians per second, $\text{rad}\cdot\text{s}^{-1}$);
- **$T = \dfrac{2\pi}{\omega}$** is the **period** (duration of one complete cycle in seconds);
- **$f = \dfrac{1}{T} = \dfrac{\omega}{2\pi}$** is the **frequency** (cycles per second, in Hertz, $\text{Hz}$);
- **$\varphi$** is the **initial phase** (phase offset at $t = 0$).

#### 6.1 Alternating Mains Current

In European residential electrical outlets, the voltage is a sinusoidal wave with frequency $f = 50\text{ Hz}$.
The angular frequency is $\omega = 2\pi f = 2\pi \times 50 = 100\pi \approx 314.16\text{ rad}\cdot\text{s}^{-1}$.
The period of oscillation is $T = \dfrac{1}{50} = 0.02\text{ s} = 20\text{ milliseconds}$.
An RMS voltage of $230\text{ V}$ corresponds to a peak amplitude of $U_{\max} = 230 \sqrt{2} \approx 325\text{ V}$:
$$u(t) = 325 \cos(100\pi t).$$

#### 6.2 Musical Notes and Acoustics

A pure tone produced by a tuning fork is a sinusoidal pressure wave traveling through air.
The standard orchestral reference note *A4* (concert pitch) vibrates at 440 cycles per second ($f = 440\text{ Hz}$).
Its acoustic wavelength in air (at speed of sound $c \approx 340\text{ m}\cdot\text{s}^{-1}$) is:
$$\lambda = \dfrac{c}{f} = \dfrac{340}{440} \approx 0.77\text{ m}.$$

> **💻 Python Simulation — Sampling a Sinusoid:**
> ```python
> import math
>
> def sinusoidal_signal(amplitude, frequency, duration, num_points):
>     omega = 2 * math.pi * frequency
>     step = duration / num_points
>     points = []
>     for i in range(num_points):
>         t = i * step
>         value = amplitude * math.sin(omega * t)
>         points.append((round(t, 4), round(value, 3)))
>     return points
>
> # Generate a 50 Hz signal over 0.02 seconds (1 complete period)
> sampled = sinusoidal_signal(amplitude=325, frequency=50, duration=0.02, num_points=5)
> print("Sampled points:", sampled)
> ```

---

### Key Takeaways

#### 1. The Unit Circle and Geometric Symmetries
- The radian measures arc length: $180^\circ = \pi\text{ rad}$.
- Circle coordinates: $M(x) = (\cos x\,; \sin x)$, whence $\cos^2 x + \sin^2 x = 1$ and $-1 \leq \cos x, \sin x \leq 1$.
- Periodicity: $\cos(x+2\pi) = \cos x$ and $\sin(x+2\pi) = \sin x$.
- Parity: $\cos(-x) = \cos x$ (cosine is even); $\sin(-x) = -\sin x$ (sine is odd).
- Angle shifts: $\cos\left(\dfrac{\pi}{2}-x\right) = \sin x$ and $\sin\left(\dfrac{\pi}{2}-x\right) = \cos x$.

#### 2. Fundamental Differentiation
- Key limits at the origin: $\lim\limits_{x \to 0} \dfrac{\sin x}{x} = 1$ and $\lim\limits_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$.
- Elementary derivatives:
  $$(\sin x)' = \cos x \quad \text{and} \quad (\cos x)' = -\sin x.$$
- Composite derivatives:
  $$\big(\sin(u)\big)' = u' \cos(u) \quad \text{and} \quad \big(\cos(u)\big)' = -u' \sin(u).$$
- In particular: $\big(\cos(\omega t + \varphi)\big)' = -\omega \sin(\omega t + \varphi)$.
- Second derivatives: $(\sin)''(x) = -\sin x$ and $(\cos)''(x) = -\cos x$.
- The harmonic oscillator differential equation: $y'' + \omega^2 y = 0$.

#### 3. Graphic Profiles and Tangents
- Tangent to $\sin$ at the origin: $y = x$. For small $x$, $\sin x \approx x$.
- Tangent to $\cos$ at $x = 0$: $y = 1$ (horizontal tangent).
- Period $T = \dfrac{2\pi}{\omega}$ and frequency $f = \dfrac{1}{T}$.

#### 4. Solving Trigonometric Equations
- $\cos x = \cos \alpha \iff x = \alpha + 2k\pi$ or $x = -\alpha + 2k\pi$.
- $\sin x = \sin \alpha \iff x = \alpha + 2k\pi$ or $x = \pi - \alpha + 2k\pi$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 49.1 —** Angle Conversions and Exact Values.
1. Convert the following angles to radians: $15^\circ$, $75^\circ$, $150^\circ$, $315^\circ$.
2. Without a calculator, compute the exact values of:
   $A = \cos\left(\dfrac{2\pi}{3}\right)$, $\quad B = \sin\left(-\dfrac{\pi}{4}\right)$, $\quad C = \cos\left(\dfrac{7\pi}{6}\right)$, $\quad D = \sin\left(\dfrac{5\pi}{2}\right)$.

**Exercise 49.2 —** Simplification of Trigonometric Expressions.
Simplify for all real $x$:
1. $E(x) = \cos(x + \pi) + \sin\left(x + \dfrac{\pi}{2}\right)$
2. $F(x) = \sin(\pi - x) - \cos\left(\dfrac{\pi}{2} - x\right)$
3. $G(x) = \cos(-x) + \cos(\pi - x) + \sin(-x) + \sin(\pi + x)$
4. $H(x) = (\cos x + \sin x)^2 + (\cos x - \sin x)^2$

**Exercise 49.3 —** Direct Derivatives.
Differentiate the following functions on $\mathbb{R}$:
1. $f_1(x) = 3\sin x - 2\cos x$
2. $f_2(x) = x \sin x$
3. $f_3(x) = \dfrac{\cos x}{x^2 + 1}$
4. $f_4(x) = \sin(5x - 2)$
5. $f_5(x) = \cos(4x^2)$

**Exercise 49.4 —** Elementary Equations in $\mathbb{R}$.
Solve in $\mathbb{R}$:
1. $\cos x = \dfrac{\sqrt{3}}{2}$
2. $\sin x = -\dfrac{1}{2}$
3. $\cos(3x) = 0$
4. $\sin(2x) = 1$

**Exercise 49.5 —** Equations on Restricted Intervals.
1. Solve $\cos x = -\dfrac{\sqrt{2}}{2}$ on the interval $[0\,; 2\pi]$.
2. Solve $\sin(2x) = \dfrac{\sqrt{3}}{2}$ on the interval $[-\pi\,; \pi]$.

**Exercise 49.6 —** Immediate Inequalities.
Solve on $[-\pi\,; \pi]$:
1. $\cos x > 0$
2. $\sin x \leq \dfrac{1}{2}$

**Exercise 49.7 —** Trigonometric Limits.
Evaluate:
1. $\lim\limits_{x \to 0} \dfrac{\sin(3x)}{x}$
2. $\lim\limits_{x \to 0} \dfrac{\tan x}{x}$
3. $\lim\limits_{x \to +\infty} \dfrac{\cos x}{x}$ (apply the Squeeze Theorem)

---

#### Level ★★ (Exploration and Exam Preparation)

**Exercise 49.8 —** Quadratic Equation in Cosine.
Solve on $[0\,; 2\pi[$:
$$2\cos^2 x + \cos x - 1 = 0.$$

**Exercise 49.9 —** Study of a Damped Oscillatory Function.
Let $f$ be defined on $[0\,; +\infty[$ by $f(t) = e^{-t} \sin t$.
1. Determine the limit of $f$ as $t \to +\infty$.
2. Calculate $f'(t)$ and show that $f'(t) = \sqrt{2} e^{-t} \cos\left(t + \dfrac{\pi}{4}\right)$.
3. Establish the table of variations of $f$ on $[0\,; 2\pi]$.
4. Sketch the curve showing the envelope curves $y = e^{-t}$ and $y = -e^{-t}$.

**Exercise 49.10 —** Complete Study of a Trigonometric Function.
Let $f$ be defined on $\mathbb{R}$ by:
$$f(x) = \cos(2x) + 2\cos x.$$
1. Show that $f$ is $2\pi$-periodic and even. Explain why its study can be restricted to $[0\,; \pi]$.
2. Compute $f'(x)$ and prove that $f'(x) = -2\sin x (2\cos x + 1)$.
3. Determine the sign of $f'(x)$ on $[0\,; \pi]$ and compile the variation table of $f$.
4. Determine the extrema of $f$ on $[0\,; \pi]$.

**Exercise 49.11 —** Tangents and Rational Trigonometric Functions.
Let $g(x) = \dfrac{\sin x}{2 + \cos x}$ defined on $\mathbb{R}$.
1. Justify why the denominator is never zero on $\mathbb{R}$.
2. Prove that $g$ is an odd function.
3. Compute $g'(x)$ and show that $g'(x) = \dfrac{2\cos x + 1}{(2 + \cos x)^2}$.
4. Find the equation of the tangent line $T$ at the origin $(0\,;0)$.

**Exercise 49.12 —** Addition Formulas and Angle Identities.
1. Prove that for all real numbers $a$ and $b$:
   $$\cos(a+b)\cos(a-b) = \cos^2 a - \sin^2 b.$$
2. Solve in $\mathbb{R}$ the equation $\cos(3x) = \sin(2x)$ by using $\sin(u) = \cos\left(\dfrac{\pi}{2} - u\right)$.

**Exercise 49.13 —** Convexity and Inflection Points.
Let $f(x) = \sin^2 x$ defined on $[0\,; \pi]$.
1. Express $f(x)$ in terms of $\cos(2x)$.
2. Compute $f'(x)$ and $f''(x)$.
3. Determine the intervals on which $f$ is convex, and concave.
4. State the coordinates of the inflection points on $[0\,; \pi]$.

**Exercise 49.14 —** Ocean Tide Modeling.
In a harbor in Brittany, water height $H(t)$ (in meters) as a function of time $t$ (in hours since midnight) is modeled by:
$$H(t) = 6 + 4 \cos\left(\dfrac{\pi}{6} t - \dfrac{\pi}{3}\right).$$
1. What is the tidal period?
2. What are the water heights at high tide and low tide?
3. At what time in the morning ($t \in [0\,; 12]$) is high tide reached?
4. A fishing trawler requires a minimum depth of $8\text{ meters}$ to navigate safely. During what morning hours can the trawler enter the harbor safely?

**Exercise 49.15 —** Indeterminate Forms Involving Trigonometry.
Evaluate, justifying each step:
1. $\lim\limits_{x \to 0} \dfrac{1 - \cos(2x)}{x \sin x}$
2. $\lim\limits_{x \to \pi/2} \dfrac{\cos x}{x - \dfrac{\pi}{2}}$
3. $\lim\limits_{x \to 0} \dfrac{\sqrt{1 + \sin x} - \sqrt{1 - \sin x}}{x}$

---

#### Level ★★★ (In-Depth Challenges)

**Exercise 49.16 —** Machin's Formula and the Calculation of $\pi$.
Define the tangent function by $\tan x = \dfrac{\sin x}{\cos x}$ for $x \in \left]-\dfrac{\pi}{2}\,; \dfrac{\pi}{2}\right[$.
1. Show that $\tan(a+b) = \dfrac{\tan a + \tan b}{1 - \tan a \tan b}$.
2. Let $\alpha$ be such that $\tan \alpha = \dfrac{1}{5}$. Calculate $\tan(2\alpha)$ and $\tan(4\alpha)$.
3. Deduce John Machin's celebrated formula (1706):
   $$\dfrac{\pi}{4} = 4 \arctan\left(\dfrac{1}{5}\right) - \arctan\left(\dfrac{1}{239}\right).$$
   *(Machin used this formula to compute the first 100 decimal digits of $\pi$ by hand!)*

**Exercise 49.17 —** Dirichlet's Trigonometric Sum.
For $n \in \mathbb{N}^*$ and $x \in \mathbb{R} \setminus 2\pi\mathbb{Z}$, define:
$$S_n(x) = \dfrac{1}{2} + \sum_{k=1}^n \cos(kx) = \dfrac{1}{2} + \cos x + \cos(2x) + \dots + \cos(nx).$$
1. Prove the identity: $2\sin\left(\dfrac{x}{2}\right)\cos(kx) = \sin\left(\left(k+\dfrac{1}{2}\right)x\right) - \sin\left(\left(k-\dfrac{1}{2}\right)x\right)$.
2. Multiplying $S_n(x)$ by $2\sin\left(\dfrac{x}{2}\right)$, use a telescoping sum to show:
   $$S_n(x) = \dfrac{\sin\left(\left(n+\dfrac{1}{2}\right)x\right)}{2\sin\left(\dfrac{x}{2}\right)}.$$
   *(This Dirichlet kernel lies at the heart of Fourier series analysis).*

**Exercise 49.18 —** Jordan's Inequality.
1. Prove that the function $f(x) = \dfrac{\sin x}{x}$ is strictly decreasing on $\left]0\,; \dfrac{\pi}{2}\right]$.
2. Deduce **Jordan's inequality**:
   $$\text{For all } x \in \left[0\,; \dfrac{\pi}{2}\right] : \quad \dfrac{2}{\pi} x \leq \sin x \leq x.$$
3. Give the geometric interpretation of this inequality using a chord and a tangent line.

**Exercise 49.19 —** Coupled Oscillating Systems and Phase Shift.
Consider two signals $s_1(t) = 3\cos(\omega t)$ and $s_2(t) = 4\sin(\omega t)$.
Define their superposition $S(t) = s_1(t) + s_2(t)$.
1. Show that there exists an amplitude $A > 0$ and a phase angle $\varphi \in [0\,; 2\pi[$ such that:
   $$S(t) = A \cos(\omega t - \varphi).$$
2. Compute the exact value of $A$ and estimate $\varphi$.
3. Generalization: Show that any linear combination $a\cos(\omega t) + b\sin(\omega t)$ can be written in the form $R\cos(\omega t - \theta)$ with $R = \sqrt{a^2 + b^2}$.

**Exercise 49.20 —** Absence of Limit at Infinity.
Prove rigorously using sequences that the function $x \mapsto \cos x$ has **no limit** as $x \to +\infty$.

---

### Solutions

#### Level ★ Solutions

**Solution 49.1:**
1. Conversion formula: $\theta_{\text{rad}} = \theta_{\text{deg}} \times \dfrac{\pi}{180}$.
   - $15^\circ = 15 \times \dfrac{\pi}{180} = \dfrac{\pi}{12}\text{ rad}$.
   - $75^\circ = 75 \times \dfrac{\pi}{180} = \dfrac{5\pi}{12}\text{ rad}$.
   - $150^\circ = 150 \times \dfrac{\pi}{180} = \dfrac{5\pi}{6}\text{ rad}$.
   - $315^\circ = 315 \times \dfrac{\pi}{180} = \dfrac{7\pi}{4}\text{ rad}$.
2. Exact values:
   - $A = \cos\left(\pi - \dfrac{\pi}{3}\right) = -\cos\left(\dfrac{\pi}{3}\right) = -\dfrac{1}{2}$.
   - $B = \sin\left(-\dfrac{\pi}{4}\right) = -\sin\left(\dfrac{\pi}{4}\right) = -\dfrac{\sqrt{2}}{2}$.
   - $C = \cos\left(\pi + \dfrac{\pi}{6}\right) = -\cos\left(\dfrac{\pi}{6}\right) = -\dfrac{\sqrt{3}}{2}$.
   - $D = \sin\left(2\pi + \dfrac{\pi}{2}\right) = \sin\left(\dfrac{\pi}{2}\right) = 1$.

**Solution 49.2:**
1. $E(x) = -\cos x + \cos x = 0$.
2. $F(x) = \sin x - \sin x = 0$.
3. $G(x) = \cos x - \cos x - \sin x - \sin x = -2\sin x$.
4. Expanding: $(\cos^2 x + 2\sin x \cos x + \sin^2 x) + (\cos^2 x - 2\sin x \cos x + \sin^2 x) = 2(\cos^2 x + \sin^2 x) = 2(1) = 2$.

**Solution 49.3:**
1. $f'_1(x) = 3\cos x - 2(-\sin x) = 3\cos x + 2\sin x$.
2. Product rule: $f'_2(x) = 1 \times \sin x + x \cos x = \sin x + x \cos x$.
3. Quotient rule: $f'_3(x) = \dfrac{(-\sin x)(x^2+1) - \cos x(2x)}{(x^2+1)^2} = \dfrac{-(x^2+1)\sin x - 2x\cos x}{(x^2+1)^2}$.
4. Chain rule: $f'_4(x) = 5\cos(5x - 2)$.
5. Chain rule: with $u(x) = 4x^2 \implies u'(x) = 8x$, we have $f'_5(x) = -8x \sin(4x^2)$.

**Solution 49.4:**
1. $\cos x = \dfrac{\sqrt{3}}{2} = \cos\left(\dfrac{\pi}{6}\right) \iff x = \dfrac{\pi}{6} + 2k\pi$ or $x = -\dfrac{\pi}{6} + 2k\pi$ ($k \in \mathbb{Z}$).
2. $\sin x = -\dfrac{1}{2} = \sin\left(-\dfrac{\pi}{6}\right) \iff x = -\dfrac{\pi}{6} + 2k\pi$ or $x = \pi - \left(-\dfrac{\pi}{6}\right) + 2k\pi = \dfrac{7\pi}{6} + 2k\pi$ ($k \in \mathbb{Z}$).
3. $\cos(3x) = 0 = \cos\left(\dfrac{\pi}{2}\right) \iff 3x = \dfrac{\pi}{2} + k\pi \iff x = \dfrac{\pi}{6} + \dfrac{k\pi}{3}$ ($k \in \mathbb{Z}$).
4. $\sin(2x) = 1 = \sin\left(\dfrac{\pi}{2}\right) \iff 2x = \dfrac{\pi}{2} + 2k\pi \iff x = \dfrac{\pi}{4} + k\pi$ ($k \in \mathbb{Z}$).

**Solution 49.5:**
1. $\cos x = -\dfrac{\sqrt{2}}{2} = \cos\left(\dfrac{3\pi}{4}\right)$.
   Solutions in $\mathbb{R}$: $x = \pm \dfrac{3\pi}{4} + 2k\pi$.
   Within $[0\,; 2\pi]$: for $k = 0$, $x_1 = \dfrac{3\pi}{4}$; for $k = 1$ in the negative branch, $x_2 = 2\pi - \dfrac{3\pi}{4} = \dfrac{5\pi}{4}$.
   $\mathcal{S} = \left\{\dfrac{3\pi}{4} \; ; \; \dfrac{5\pi}{4}\right\}$.
2. $\sin(2x) = \dfrac{\sqrt{3}}{2} = \sin\left(\dfrac{\pi}{3}\right)$.
   Hence $2x = \dfrac{\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{6} + k\pi$ or $2x = \dfrac{2\pi}{3} + 2k\pi \iff x = \dfrac{\pi}{3} + k\pi$.
   Within $[-\pi\,; \pi]$:
   - $x = \dfrac{\pi}{6} + k\pi$ yields $\dfrac{\pi}{6}$ (for $k = 0$) and $-\dfrac{5\pi}{6}$ (for $k = -1$).
   - $x = \dfrac{\pi}{3} + k\pi$ yields $\dfrac{\pi}{3}$ (for $k = 0$) and $-\dfrac{2\pi}{3}$ (for $k = -1$).
   $\mathcal{S} = \left\{ -\dfrac{5\pi}{6} \; ; \; -\dfrac{2\pi}{3} \; ; \; \dfrac{\pi}{6} \; ; \; \dfrac{\pi}{3} \right\}$.

**Solution 49.6:**
1. $\cos x > 0$ on $[-\pi\,; \pi]$: corresponds to points with strictly positive $x$-coordinates on the unit circle: $\mathcal{S} = \left]-\dfrac{\pi}{2} \; ; \; \dfrac{\pi}{2}\right[$.
2. $\sin x \leq \dfrac{1}{2}$ on $[-\pi\,; \pi]$: the line $y = 1/2$ intersects the circle at $\dfrac{\pi}{6}$ and $\dfrac{5\pi}{6}$.
   Points lying on or below this line over $[-\pi\,; \pi]$ form: $\mathcal{S} = \left[-\pi \; ; \; \dfrac{\pi}{6}\right] \cup \left[\dfrac{5\pi}{6} \; ; \; \pi\right]$.

**Solution 49.7:**
1. Substitute $u = 3x \to 0$:
   $\dfrac{\sin(3x)}{x} = 3 \times \dfrac{\sin u}{u} \to 3 \times 1 = 3$.
2. $\dfrac{\tan x}{x} = \dfrac{\sin x}{x \cos x} = \dfrac{\sin x}{x} \times \dfrac{1}{\cos x}$.
   As $x \to 0$, $\dfrac{\sin x}{x} \to 1$ and $\cos x \to 1$, so the limit is $1 \times 1 = 1$.
3. For $x > 0$, $-1 \leq \cos x \leq 1 \iff -\dfrac{1}{x} \leq \dfrac{\cos x}{x} \leq \dfrac{1}{x}$.
   Since $\lim\limits_{x \to +\infty} \pm\dfrac{1}{x} = 0$, the Squeeze Theorem gives $\lim\limits_{x \to +\infty} \dfrac{\cos x}{x} = 0$.

---

#### Level ★★ Solutions

**Solution 49.8:**
Let $X = \cos x$. Then $2X^2 + X - 1 = 0$.
$\Delta = 1^2 - 4(2)(-1) = 9 = 3^2$.
$X_1 = \dfrac{-1 - 3}{4} = -1$ and $X_2 = \dfrac{-1 + 3}{4} = \dfrac{1}{2}$.
- $\cos x = -1 \iff x = \pi$ on $[0\,; 2\pi[$.
- $\cos x = \dfrac{1}{2} = \cos\left(\dfrac{\pi}{3}\right) \iff x = \dfrac{\pi}{3}$ or $x = 2\pi - \dfrac{\pi}{3} = \dfrac{5\pi}{3}$.
$\mathcal{S} = \left\{ \dfrac{\pi}{3} \; ; \; \pi \; ; \; \dfrac{5\pi}{3} \right\}$.

**Solution 49.9:**
1. For all $t \geq 0$, $-1 \leq \sin t \leq 1 \iff -e^{-t} \leq e^{-t} \sin t \leq e^{-t}$.
   Since $\lim\limits_{t \to +\infty} e^{-t} = 0$, the Squeeze Theorem guarantees $\lim\limits_{t \to +\infty} f(t) = 0$.
2. Product rule: $f'(t) = -e^{-t}\sin t + e^{-t}\cos t = e^{-t}(\cos t - \sin t)$.
   Now $\cos t - \sin t = \sqrt{2}\left(\dfrac{\sqrt{2}}{2}\cos t - \dfrac{\sqrt{2}}{2}\sin t\right) = \sqrt{2}\cos\left(t + \dfrac{\pi}{4}\right)$.
   Hence $f'(t) = \sqrt{2} e^{-t} \cos\left(t + \dfrac{\pi}{4}\right)$.
3. On $[0\,; 2\pi]$, $e^{-t} > 0$, so $f'(t) = 0 \iff \cos\left(t + \dfrac{\pi}{4}\right) = 0$:
   $t + \dfrac{\pi}{4} = \dfrac{\pi}{2} \iff t_1 = \dfrac{\pi}{4}$, and $t + \dfrac{\pi}{4} = \dfrac{3\pi}{2} \iff t_2 = \dfrac{5\pi}{4}$.
   - On $\left[0\,; \dfrac{\pi}{4}\right]$, $f'(t) \geq 0$: $f$ rises from $0$ to $f(\pi/4) = \dfrac{\sqrt{2}}{2} e^{-\pi/4} \approx 0.322$.
   - On $\left[\dfrac{\pi}{4}\,; \dfrac{5\pi}{4}\right]$, $f'(t) \leq 0$: $f$ decreases to $f(5\pi/4) = -\dfrac{\sqrt{2}}{2} e^{-5\pi/4} \approx -0.014$.
   - On $\left[\dfrac{5\pi}{4}\,; 2\pi\right]$, $f'(t) \geq 0$: $f$ climbs back to $f(2\pi) = 0$.
4. The sinusoidal wave is pinched between the exponential boundaries $y = e^{-t}$ and $y = -e^{-t}$, tangentially touching them alternately at phased peaks and troughs.

**Solution 49.10:**
1. $f(x+2\pi) = \cos(2x+4\pi) + 2\cos(x+2\pi) = \cos(2x) + 2\cos x = f(x)$: $f$ is $2\pi$-periodic.
   $f(-x) = \cos(-2x) + 2\cos(-x) = \cos(2x) + 2\cos x = f(x)$: $f$ is even.
   Hence the analysis can be restricted to half a period: $[0\,; \pi]$.
2. $f'(x) = -2\sin(2x) - 2\sin x$.
   Using $\sin(2x) = 2\sin x \cos x$:
   $f'(x) = -4\sin x \cos x - 2\sin x = -2\sin x(2\cos x + 1)$.
3. On $]0\,; \pi[$, $\sin x > 0$, so $f'(x)$ has the opposite sign of $2\cos x + 1$:
   - $2\cos x + 1 = 0 \iff \cos x = -\dfrac{1}{2} \iff x = \dfrac{2\pi}{3}$.
   - On $\left[0\,; \dfrac{2\pi}{3}\right[$, $\cos x > -1/2 \implies 2\cos x + 1 > 0 \implies f'(x) < 0$.
   - On $\left]\dfrac{2\pi}{3}\,; \pi\right]$, $\cos x < -1/2 \implies 2\cos x + 1 < 0 \implies f'(x) > 0$.
   Thus $f$ is strictly decreasing on $\left[0\,; \dfrac{2\pi}{3}\right]$ and strictly increasing on $\left[\dfrac{2\pi}{3}\,; \pi\right]$.
4. - Maximum at $x = 0$: $f(0) = \cos 0 + 2\cos 0 = 3$.
   - Absolute minimum at $x = \dfrac{2\pi}{3}$: $f\left(\dfrac{2\pi}{3}\right) = \cos\left(\dfrac{4\pi}{3}\right) + 2\cos\left(\dfrac{2\pi}{3}\right) = -\dfrac{1}{2} - 1 = -\dfrac{3}{2}$.
   - Local maximum at $x = \pi$: $f(\pi) = \cos(2\pi) + 2\cos(\pi) = 1 - 2 = -1$.

**Solution 49.11:**
1. For all $x \in \mathbb{R}$, $\cos x \geq -1 \implies 2 + \cos x \geq 1 > 0$. The denominator never vanishes.
2. $g(-x) = \dfrac{\sin(-x)}{2 + \cos(-x)} = \dfrac{-\sin x}{2 + \cos x} = -g(x)$: $g$ is odd.
3. Quotient rule:
   $g'(x) = \dfrac{\cos x(2+\cos x) - \sin x(-\sin x)}{(2+\cos x)^2} = \dfrac{2\cos x + \cos^2 x + \sin^2 x}{(2+\cos x)^2} = \dfrac{2\cos x + 1}{(2+\cos x)^2}$.
4. At $x = 0$: $g(0) = 0$ and $g'(0) = \dfrac{2(1)+1}{(2+1)^2} = \dfrac{3}{9} = \dfrac{1}{3}$.
   The tangent line $T$ at the origin is: $y = \dfrac{1}{3}x$.

**Solution 49.12:**
1. Expanding the product:
   $\cos(a+b)\cos(a-b) = (\cos a \cos b - \sin a \sin b)(\cos a \cos b + \sin a \sin b) = \cos^2 a \cos^2 b - \sin^2 a \sin^2 b$.
   Substitute $\cos^2 b = 1 - \sin^2 b$ and $\sin^2 a = 1 - \cos^2 a$:
   $= \cos^2 a(1 - \sin^2 b) - (1 - \cos^2 a)\sin^2 b = \cos^2 a - \sin^2 b$.
2. $\cos(3x) = \sin(2x) \iff \cos(3x) = \cos\left(\dfrac{\pi}{2} - 2x\right)$.
   This generates two families:
   - $3x = \dfrac{\pi}{2} - 2x + 2k\pi \iff 5x = \dfrac{\pi}{2} + 2k\pi \iff x = \dfrac{\pi}{10} + \dfrac{2k\pi}{5}$ ($k \in \mathbb{Z}$).
   - $3x = -\left(\dfrac{\pi}{2} - 2x\right) + 2k\pi \iff 3x = -\dfrac{\pi}{2} + 2x + 2k\pi \iff x = -\dfrac{\pi}{2} + 2k\pi$ ($k \in \mathbb{Z}$).

**Solution 49.13:**
1. Using $\cos(2x) = 1 - 2\sin^2 x$, we obtain $f(x) = \sin^2 x = \dfrac{1 - \cos(2x)}{2} = \dfrac{1}{2} - \dfrac{1}{2}\cos(2x)$.
2. $f'(x) = -\dfrac{1}{2}(-2\sin(2x)) = \sin(2x)$.
   $f''(x) = 2\cos(2x)$.
3. The sign of $f''(x)$ matches that of $\cos(2x)$ on $[0\,; \pi]$:
   - For $2x \in [0\,; \pi/2] \iff x \in [0\,; \pi/4]$: $\cos(2x) \geq 0 \implies f''(x) \geq 0$, so $f$ is **convex**.
   - For $2x \in [\pi/2\,; 3\pi/2] \iff x \in [\pi/4\,; 3\pi/4]$: $\cos(2x) \leq 0 \implies f''(x) \leq 0$, so $f$ is **concave**.
   - For $2x \in [3\pi/2\,; 2\pi] \iff x \in [3\pi/4\,; \pi]$: $\cos(2x) \geq 0 \implies f''(x) \geq 0$, so $f$ is **convex**.
4. The second derivative vanishes with a sign change at $x = \dfrac{\pi}{4}$ and $x = \dfrac{3\pi}{4}$.
   The inflection points are $I_1\left(\dfrac{\pi}{4}\,; \dfrac{1}{2}\right)$ and $I_2\left(\dfrac{3\pi}{4}\,; \dfrac{1}{2}\right)$.

**Solution 49.14:**
1. Angular frequency is $\omega = \dfrac{\pi}{6}$. Period is $T = \dfrac{2\pi}{\omega} = \dfrac{2\pi}{\pi/6} = 12\text{ hours}$.
2. Cosine ranges between $-1$ and $1$:
   - High tide: $H_{\max} = 6 + 4(1) = 10\text{ meters}$.
   - Low tide: $H_{\min} = 6 + 4(-1) = 2\text{ meters}$.
3. High tide occurs when the cosine reaches $1$:
   $\dfrac{\pi}{6}t - \dfrac{\pi}{3} = 0 \iff \dfrac{\pi}{6}t = \dfrac{\pi}{3} \iff t = 2$.
   High tide occurs at **2:00 AM** (and next at $2 + 12 = 14$, i.e., 2:00 PM).
4. Safe navigation requires $H(t) \geq 8 \iff 6 + 4\cos\left(\dfrac{\pi}{6}t - \dfrac{\pi}{3}\right) \geq 8 \iff \cos\left(\dfrac{\pi}{6}t - \dfrac{\pi}{3}\right) \geq \dfrac{1}{2}$.
   Since $\cos \theta \geq \dfrac{1}{2} \iff -\dfrac{\pi}{3} \leq \theta \leq \dfrac{\pi}{3}$:
   $$-\dfrac{\pi}{3} \leq \dfrac{\pi}{6}t - \dfrac{\pi}{3} \leq \dfrac{\pi}{3} \iff 0 \leq \dfrac{\pi}{6}t \leq \dfrac{2\pi}{3} \iff 0 \leq t \leq 4.$$
   The trawler can navigate safely **between midnight and 4:00 AM** (and later between 12:00 PM and 4:00 PM).

**Solution 49.15:**
1. $1 - \cos(2x) = 2\sin^2 x$. The expression becomes $\dfrac{2\sin^2 x}{x \sin x} = 2 \dfrac{\sin x}{x}$.
   As $x \to 0$, this limit is $2 \times 1 = 2$.
2. Substitute $h = x - \dfrac{\pi}{2} \to 0$, so $x = \dfrac{\pi}{2} + h$.
   The quotient becomes $\dfrac{\cos(\pi/2 + h)}{h} = \dfrac{-\sin h}{h} = -\dfrac{\sin h}{h} \to -1$.
3. Multiply by the conjugate:
   $$\dfrac{\sqrt{1+\sin x} - \sqrt{1-\sin x}}{x} = \dfrac{(1+\sin x) - (1-\sin x)}{x(\sqrt{1+\sin x} + \sqrt{1-\sin x})} = \dfrac{\sin x}{x} \times \dfrac{2}{\sqrt{1+\sin x} + \sqrt{1-\sin x}}.$$
   As $x \to 0$, $\dfrac{\sin x}{x} \to 1$ and the second factor tends to $\dfrac{2}{\sqrt{1} + \sqrt{1}} = 1$. The limit is $1$.

---

#### Level ★★★ Solutions

**Solution 49.16:**
1. $\tan(a+b) = \dfrac{\sin(a+b)}{\cos(a+b)} = \dfrac{\sin a \cos b + \cos a \sin b}{\cos a \cos b - \sin a \sin b}$.
   Dividing numerator and denominator by $\cos a \cos b \neq 0$ immediately gives $\tan(a+b) = \dfrac{\tan a + \tan b}{1 - \tan a \tan b}$.
2. With $\tan \alpha = \dfrac{1}{5}$:
   $\tan(2\alpha) = \dfrac{2(1/5)}{1 - (1/5)^2} = \dfrac{2/5}{24/25} = \dfrac{5}{12}$.
   Then:
   $\tan(4\alpha) = \dfrac{2(5/12)}{1 - (5/12)^2} = \dfrac{5/6}{119/144} = \dfrac{120}{119}$.
3. Evaluate $\tan\left(4\alpha - \dfrac{\pi}{4}\right)$:
   Since $\tan\left(\dfrac{\pi}{4}\right) = 1$:
   $\tan\left(4\alpha - \dfrac{\pi}{4}\right) = \dfrac{\tan(4\alpha) - 1}{1 + \tan(4\alpha)} = \dfrac{\frac{120}{119} - 1}{1 + \frac{120}{119}} = \dfrac{1/119}{239/119} = \dfrac{1}{239}$.
   Taking the arctangent of both sides:
   $4\alpha - \dfrac{\pi}{4} = \arctan\left(\dfrac{1}{239}\right) \iff \dfrac{\pi}{4} = 4\arctan\left(\dfrac{1}{5}\right) - \arctan\left(\dfrac{1}{239}\right)$.

**Solution 49.17:**
1. Expand the right-hand side using addition formulas:
   $\sin\left(kx + \dfrac{x}{2}\right) - \sin\left(kx - \dfrac{x}{2}\right) = \left[\sin(kx)\cos\dfrac{x}{2} + \cos(kx)\sin\dfrac{x}{2}\right] - \left[\sin(kx)\cos\dfrac{x}{2} - \cos(kx)\sin\dfrac{x}{2}\right] = 2\cos(kx)\sin\dfrac{x}{2}$.
2. Multiply $S_n(x)$ by $2\sin\left(\dfrac{x}{2}\right)$:
   $$2\sin\left(\dfrac{x}{2}\right)S_n(x) = \sin\left(\dfrac{x}{2}\right) + \sum_{k=1}^n 2\sin\left(\dfrac{x}{2}\right)\cos(kx) = \sin\left(\dfrac{x}{2}\right) + \sum_{k=1}^n \left[\sin\left(\left(k+\dfrac{1}{2}\right)x\right) - \sin\left(\left(k-\dfrac{1}{2}\right)x\right)\right].$$
   The summation telescopes: all intermediate terms cancel except $-\sin\left(\dfrac{x}{2}\right)$ (which cancels the leading term) and the final term $\sin\left(\left(n+\dfrac{1}{2}\right)x\right)$.
   Hence: $2\sin\left(\dfrac{x}{2}\right)S_n(x) = \sin\left(\left(n+\dfrac{1}{2}\right)x\right)$.
   Dividing by $2\sin\left(\dfrac{x}{2}\right) \neq 0$ yields the Dirichlet kernel formula.

**Solution 49.18:**
1. For $x \in \left]0\,; \dfrac{\pi}{2}\right]$, $f'(x) = \dfrac{x\cos x - \sin x}{x^2} = \dfrac{\cos x(x - \tan x)}{x^2}$.
   By the fundamental lemma of Section 3.1, for all $x \in \left]0\,; \dfrac{\pi}{2}\right[$, $x < \tan x \iff x - \tan x < 0$.
   Since $\cos x > 0$ and $x^2 > 0$, we have $f'(x) < 0$. Thus $f$ is strictly decreasing.
2. For all $x \in \left]0\,; \dfrac{\pi}{2}\right]$:
   $f\left(\dfrac{\pi}{2}\right) \leq f(x) \leq \lim_{t \to 0^+} f(t) \iff \dfrac{\sin(\pi/2)}{\pi/2} \leq \dfrac{\sin x}{x} \leq 1 \iff \dfrac{2}{\pi} \leq \dfrac{\sin x}{x} \leq 1$.
   Multiplying by $x > 0$: $\dfrac{2}{\pi} x \leq \sin x \leq x$. This inequality holds at $x = 0$ as well.
3. Graphically on $\left[0\,; \dfrac{\pi}{2}\right]$, the sine curve is squeezed between its tangent at the origin ($y = x$) and the chord connecting $(0\,;0)$ to $\left(\dfrac{\pi}{2}\,; 1\right)$ ($y = \dfrac{2}{\pi}x$).

**Solution 49.19:**
1. $S(t) = 3\cos(\omega t) + 4\sin(\omega t)$.
   Factor out $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$:
   $S(t) = 5\left(\dfrac{3}{5}\cos(\omega t) + \dfrac{4}{5}\sin(\omega t)\right)$.
   Since $\left(\dfrac{3}{5}\right)^2 + \left(\dfrac{4}{5}\right)^2 = 1$, there exists a unique angle $\varphi \in [0\,; 2\pi[$ such that $\cos \varphi = \dfrac{3}{5}$ and $\sin \varphi = \dfrac{4}{5}$.
   Then $S(t) = 5(\cos(\omega t)\cos \varphi + \sin(\omega t)\sin \varphi) = 5\cos(\omega t - \varphi)$.
2. Amplitude is $A = 5$.
   $\tan \varphi = \dfrac{4/5}{3/5} = \dfrac{4}{3} \implies \varphi = \arctan\left(\dfrac{4}{3}\right) \approx 0.927\text{ rad} \approx 53.1^\circ$.
3. In general, let $R = \sqrt{a^2 + b^2} > 0$. Then $\left(\dfrac{a}{R}\right)^2 + \left(\dfrac{b}{R}\right)^2 = 1$.
   There exists $\theta$ such that $\cos \theta = \dfrac{a}{R}$ and $\sin \theta = \dfrac{b}{R}$.
   Then $a\cos(\omega t) + b\sin(\omega t) = R\big(\cos(\omega t)\cos \theta + \sin(\omega t)\sin \theta\big) = R\cos(\omega t - \theta)$.

**Solution 49.20:**
Assume for contradiction that $\lim\limits_{x \to +\infty} \cos x = L$.
By the sequential characterization of limits, for every sequence $(u_n)$ such that $u_n \to +\infty$, we must have $\cos(u_n) \to L$.
Choose $u_n = 2n\pi \to +\infty$. Then $\cos(u_n) = \cos(2n\pi) = 1$ for all $n$, so the sequence converges to $1$.
Now choose $v_n = \pi + 2n\pi \to +\infty$. Then $\cos(v_n) = \cos(\pi + 2n\pi) = -1$ for all $n$, so this sequence converges to $-1$.
Since the limits $1$ and $-1$ are distinct, this violates the uniqueness of limits.
Therefore, $\cos x$ has no limit as $x \to +\infty$.

---

### The Question that Opens What Follows

We have learned to measure slopes, rates of change, and velocities at every point along a curve: this is differential calculus. But what happens if we wish to travel in the opposite direction?
If we know the instantaneous velocity of a rocket at every single second of flight, how do we reconstruct the total distance traveled? If we know the curved profile of a barrel or the wavy contour of an undulating landscape, how do we calculate its exact enclosed volume or surface area?

How do we add together an infinity of infinitely thin slices to rebuild a whole?

Join us in Chapter 50 with **The Barrel Filled with Slices of Water** and the discovery of integral calculus.
