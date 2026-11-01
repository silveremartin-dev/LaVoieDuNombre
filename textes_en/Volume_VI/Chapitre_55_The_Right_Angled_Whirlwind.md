# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 55: The Right-Angled Whirlwind

> *“For centuries, schoolmasters taught that the square root of minus one was an impossible monster, an alchemist's chimera. But look at the weather vane on the rooftop: when the wind turns ninety degrees, the world does not collapse—it opens up. What algebra thought forbidden along the straight line, the geometry of the plane brings to light. Complex numbers are not imaginary: they are the breathing of the two-dimensional plane.”*

---

### What You Are About to Discover

- The true story of the Italian Renaissance: how Gerolamo Cardano and Rafael Bombelli were forced to invent $\sqrt{-1}$ to discover solutions that were indisputably real.
- The epiphany of Argand and Gauss: multiplying by $i$ simply means **rotating by a quarter-turn ($90^\circ$)**.
- The **algebraic form** $z = a + ib$, the **complex conjugate** $\bar{z}$, and the fundamental concept of **modulus** $|z|$.
- The transition to polar coordinates: the **trigonometric form** and the extraordinary **exponential form** $z = r e^{i\theta}$, along with Euler's and De Moivre's formulas.
- Complete solution of **quadratic equations** with real and complex coefficients via complex square roots.
- The **$n$-th roots of unity** and the geometry of regular polygons.
- Geometric interpretations: computing angles, collinearity, orthogonality, and the complex representation of **translations, homotheties, and rotations**.

---

### 1. The Problem: The Forbidden Enigma of the Renaissance

#### 1.1 The Algebra Duels in Bologna (1545)
In the 16th century, mathematics professors at Italian universities clashed in public duels before roaring crowds. Challengers hurled cubic equations (involving $x^3$) at one another.
In **1545**, the Milanese physician and polymath **Gerolamo Cardano** published his masterwork, the *Ars Magna*. In it, he unveiled the formula for solving the general cubic equation $x^3 = px + q$, discovered by Scipione del Ferro and Niccolò Tartaglia:

$$x = \sqrt[3]{\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3}} + \sqrt[3]{\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3}}$$

Let us apply this formula to an apparently harmless equation:
$$x^3 = 15x + 4$$
Here, $p = 15$ and $q = 4$. Let us test small integers mentally:
$$4^3 = 64 \quad \text{and} \quad 15 \times 4 + 4 = 60 + 4 = 64.$$
The number **$x = 4$ is an obvious solution**, perfectly real, tangible, and indisputable!

Now let us compute what Cardano's formula yields:
- $\frac{q}{2} = 2$
- $\frac{p}{3} = 5$
- The quantity under the square root is:
  $$\left(\frac{q}{2}\right)^2 - \left(\frac{p}{3}\right)^3 = 2^2 - 5^3 = 4 - 125 = -121$$

The formula demands that we write:
$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}$$

Cardano was frozen in his tracks. The square root of a negative number did not exist: every square of a real number is non-negative ($(+2)^2 = 4$ and $(-2)^2 = 4$). Cardano called this impasse an operation *“as subtle as it is useless”* and a *“mental torture.”*

#### 1.2 The Audacity of Rafael Bombelli (1572)
Twenty-seven years later, the Bolognese engineer **Rafael Bombelli** had an intuition of genius:
*“What if we pretend to ignore the prohibition? Let us treat this quantity $\sqrt{-1}$ as an ordinary number, apply the standard rules of arithmetic, and see where it leads us!”*

Bombelli observed that:
$$\sqrt{-121} = \sqrt{121 \times (-1)} = 11 \sqrt{-1}$$
He then calculated the cube of quantities of the form $(2 + \sqrt{-1})$:
$$(2 + \sqrt{-1})^3 = 2^3 + 3 \times 2^2 \times \sqrt{-1} + 3 \times 2 \times (\sqrt{-1})^2 + (\sqrt{-1})^3$$
Since $(\sqrt{-1})^2 = -1$ and $(\sqrt{-1})^3 = -1 \times \sqrt{-1} = -\sqrt{-1}$:
$$(2 + \sqrt{-1})^3 = 8 + 12\sqrt{-1} - 6 - \sqrt{-1} = 2 + 11\sqrt{-1} = 2 + \sqrt{-121}!$$
Similarly:
$$(2 - \sqrt{-1})^3 = 2 - \sqrt{-121}$$

Taking the cube roots in Cardano's formula:
$$x = (2 + \sqrt{-1}) + (2 - \sqrt{-1}) = 2 + 2 + (\sqrt{-1} - \sqrt{-1}) = 4!$$

The phantom $\sqrt{-1}$ entered the calculation, carried out the synthesis, and vanished in a cancellation, delivering the undeniably real root $x = 4$.
For two and a half centuries, mathematicians used this chimerical number—named **$i$** (for *imaginary*) by **Leonhard Euler** in 1777—with a mixture of admiration and unease.

---

### 2. The Geometric Breakthrough of Argand and Gauss

#### 2.1 Multiplying by $i$ Means Rotating by 90°
In 1806, a Swiss accountant and bookseller living in Paris, **Jean-Robert Argand**, dispelled the metaphysical fog with illuminating clarity.

Recall the real number line:
- Start at $+1$.
- Multiplying by $-1$ brings us to $-1$. Geometrically, this corresponds to a **half-turn ($180^\circ$ or $\pi$ radians)** around the origin.

$$\times (-1) \iff \text{Rotation by } 180^\circ$$

By definition of the imaginary unit:
$$i \times i = -1$$
This algebraic identity states:
*“Applying multiplication by $i$ twice in succession produces the exact same geometric outcome as a $180^\circ$ half-turn!”*
What elementary geometric transformation, when applied twice consecutively, produces a half-turn?
**A rotation by a quarter-turn ($90^\circ$ or $\frac{\pi}{2}$ radians) in the counterclockwise (positive) direction!**

```
                     Imaginary Axis (North)
                               ▲
                               │   +i  (after 1 quarter-turn of 90°)
                               │   ▲
                               │  /
                               │ /
   ───┴────────────────────────┼───────────────────────────┴───► Real Axis (East)
     -1 (after 2 quarters)     0│                           +1  (start)
      = 180° half-turn         │
                               │   -i  (after 3 quarters: 270°)
                               ▼
```

Observe the cyclic progression of powers of $i$:
- $i^0 = 1$ (East)
- $i^1 = i$ (North, quarter-turn)
- $i^2 = -1$ (West, half-turn)
- $i^3 = i^2 \times i = -i$ (South, three-quarter turn)
- $i^4 = (i^2)^2 = (-1)^2 = 1$ (East, full turn)

The number $i$ is not fictitious: **$i$ is the gateway allowing numbers to break free from the line and inhabit the entire two-dimensional plane!**

---

### 3. The Algebraic Form and Its Operations

#### 3.1 The Field $\mathbb{C}$ of Complex Numbers

> **📐 Definition — The Set of Complex Numbers**
> There exists a set denoted by $\mathbb{C}$, containing the set of real numbers $\mathbb{R}$, equipped with addition and multiplication operations extending those of $\mathbb{R}$, such that:
> 1. There exists an element $i \in \mathbb{C}$ satisfying:
>    $$i^2 = -1$$
> 2. Every element $z \in \mathbb{C}$ can be written **uniquely** in the form:
>    $$z = a + i b \quad \text{where } a \in \mathbb{R} \text{ and } b \in \mathbb{R}$$
> This expression is called the **algebraic (or Cartesian) form** of $z$.

*Standard Terminology:*
- $a$ is the **real part** of $z$, denoted $\text{Re}(z) = a$.
- $b$ is the **imaginary part** of $z$, denoted $\text{Im}(z) = b$.
*(⚠️ Frequent Trap: The imaginary part is the real number $b$, not $ib$!)*

*Special Cases:*
- If $b = 0$, $z = a$ is **purely real** ($\mathbb{R} \subset \mathbb{C}$).
- If $a = 0$, $z = ib$ is called **purely imaginary** (the set is denoted $i\mathbb{R}$).

> **📐 Theorem — Uniqueness of Algebraic Form**
> Let $z = a + ib$ and $z' = a' + ib'$ ($a, b, a', b' \in \mathbb{R}$).
> $$z = z' \iff \begin{cases} a = a' \\ b = b' \end{cases}$$
> In particular:
> $$a + ib = 0 \iff a = 0 \text{ and } b = 0$$

#### 3.2 The Complex Conjugate

> **📐 Definition — Complex Conjugate**
> For any complex number $z = a + ib$ ($a, b \in \mathbb{R}$), the **complex conjugate** of $z$, denoted $\bar{z}$ (read “$z$ bar”), is defined by:
> $$\bar{z} = a - ib$$

Geometrically, the point representing $\bar{z}$ is the reflection of the point representing $z$ across the horizontal real axis.

> **📐 Fundamental Properties of the Conjugate**
> For all complex numbers $z, z'$ and any integer $n \in \mathbb{Z}$:
> 1. $\overline{z + z'} = \bar{z} + \bar{z}'$
> 2. $\overline{z \times z'} = \bar{z} \times \bar{z}'$
> 3. $\overline{\left(\frac{z}{z'}\right)} = \frac{\bar{z}}{\bar{z}'} \quad (z' \neq 0)$
> 4. $\overline{z^n} = (\bar{z})^n$
> 5. $\overline{\bar{z}} = z$
> 6. Sum and difference:
>    $$z + \bar{z} = 2a = 2\,\text{Re}(z) \quad \text{and} \quad z - \bar{z} = 2ib = 2i\,\text{Im}(z)$$
> 7. **Fundamental Criteria:**
>    $$z \in \mathbb{R} \iff \bar{z} = z \qquad \text{and} \qquad z \in i\mathbb{R} \iff \bar{z} = -z$$
> 8. **Product with the Conjugate:**
>    $$z \bar{z} = (a + ib)(a - ib) = a^2 - (ib)^2 = a^2 - i^2 b^2 = a^2 + b^2 \geq 0$$

*Method for Dividing Complex Numbers:*
To make the denominator of a fraction $\frac{z_1}{z_2}$ real, multiply both numerator and denominator by the conjugate $\bar{z}_2$:
$$\frac{1 + 2i}{3 - 4i} = \frac{(1 + 2i)(3 + 4i)}{(3 - 4i)(3 + 4i)} = \frac{3 + 4i + 6i + 8i^2}{3^2 + 4^2} = \frac{3 - 8 + 10i}{9 + 16} = \frac{-5 + 10i}{25} = -\frac{1}{5} + \frac{2}{5}i.$$

#### 3.3 The Modulus of a Complex Number

> **📐 Definition — Modulus**
> For any complex number $z = a + ib$ ($a, b \in \mathbb{R}$), the **modulus** of $z$, denoted $|z|$, is the non-negative real number defined by:
> $$|z| = \sqrt{a^2 + b^2} = \sqrt{z \bar{z}}$$

Geometrically, if $M$ has coordinates $(a, b)$ in the orthonormal frame $(O; \vec{u}, \vec{v})$, by the Pythagorean theorem, $|z|$ is precisely the **distance $OM$** from the origin to point $M$!

> **📐 Properties of the Modulus**
> 1. $|z| \geq 0$, and $|z| = 0 \iff z = 0$.
> 2. $|-z| = |\bar{z}| = |z|$.
> 3. $|z \times z'| = |z| \times |z'|$.
> 4. $\left|\frac{z}{z'}\right| = \frac{|z|}{|z'|} \quad (z' \neq 0)$.
> 5. $|z^n| = |z|^n$ for all $n \in \mathbb{Z}$.
> 6. **Triangle Inequality:** For all $z, z' \in \mathbb{C}$:
>    $$|z + z'| \leq |z| + |z'|$$
>    *(In any triangle, the length of one side is at most the sum of the other two).*

---

### 4. Trigonometric and Exponential Forms: The Dance of Angles

#### 4.1 Argument of a Non-Zero Complex Number
Let $z \in \mathbb{C}^*$ (non-zero), represented by point $M$ in the complex plane.
The position of $M$ is uniquely determined by:
- Its distance from the origin: $r = OM = |z| > 0$.
- The oriented angle between the positive real axis and vector $\vec{OM}$: $\theta = (\vec{u}, \vec{OM})$.

> **📐 Definition — Argument**
> For any non-zero complex number $z = a + ib$, an **argument** of $z$, denoted $\arg(z)$, is any radian measure of the oriented angle $(\vec{u}, \vec{OM})$.
> The argument is defined modulo $2\pi$:
> $$\arg(z) \equiv \theta \pmod{2\pi}$$
> The unique value of the argument lying in the interval $(-\pi, \pi]$ is called the **principal argument**.
> *(The number 0 has no argument).*

Since the coordinates of $M$ are $a = r \cos\theta$ and $b = r \sin\theta$, we obtain:

> **📐 Definition — Trigonometric Form**
> Every non-zero complex number $z$ can be written as:
> $$z = r (\cos\theta + i \sin\theta) \quad \text{where } r = |z| > 0 \text{ and } \theta \equiv \arg(z) \pmod{2\pi}$$

#### 4.2 Euler's Exponential Notation

Consider the function $f(\theta) = \cos\theta + i\sin\theta$.
Differentiating with respect to the real variable $\theta$:
$$f'(\theta) = -\sin\theta + i\cos\theta = i(i\sin\theta + \cos\theta) = i f(\theta)$$
This differential relation $f' = i f$ with initial condition $f(0) = 1$ is the defining characteristic of the exponential function ($y' = k y$)!
In **1748**, Leonhard Euler introduced what is celebrated as one of the most fruitful notations in mathematical history:

> **📐 Definition — Euler's Exponential Notation**
> For every real number $\theta \in \mathbb{R}$:
> $$e^{i\theta} = \cos\theta + i\sin\theta$$
> Every non-zero complex number $z$ thus admits an **exponential form**:
> $$z = r e^{i\theta} \quad \text{where } r = |z| > 0 \text{ and } \theta \equiv \arg(z) \pmod{2\pi}$$

> **💡 Did You Know? Euler's Identity, the Most Beautiful Formula**
> Setting $\theta = \pi$ in Euler's formula yields:
> $$e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1 + 0 = -1$$
> Which writes majestically as:
> $$\mathbf{e^{i\pi} + 1 = 0}$$
> This single equation links the five fundamental constants of mathematics:
> - $0$ (the additive identity)
> - $1$ (the multiplicative identity)
> - $\pi$ (the master of circles and geometry)
> - $e$ (the master of growth and analysis)
> - $i$ (the master of complex algebra)

#### 4.3 Algebraic Properties and De Moivre's Formula
Exponential notation transforms trigonometry into elementary exponent rules:

> **📐 Theorem — Exponent Rules for Complex Exponentials**
> For all real numbers $\theta, \theta'$:
> 1. Product: $e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}$
>    *(Immediate corollary: $\arg(z z') \equiv \arg(z) + \arg(z') \pmod{2\pi}$)*
> 2. Quotient: $\frac{e^{i\theta}}{e^{i\theta'}} = e^{i(\theta - \theta')}$
>    *(Corollary: $\arg\left(\frac{z}{z'}\right) \equiv \arg(z) - \arg(z') \pmod{2\pi}$)*
> 3. Conjugate: $\overline{e^{i\theta}} = e^{-i\theta}$
> 4. Reciprocal: $\frac{1}{e^{i\theta}} = e^{-i\theta}$

> **📐 Theorem — De Moivre's Formula**
> For any real number $\theta$ and any integer $n \in \mathbb{Z}$:
> $$(e^{i\theta})^n = e^{in\theta} \iff (\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

*Euler's Formulas for Linearization:*
Adding and subtracting $e^{i\theta} = \cos\theta + i\sin\theta$ and $e^{-i\theta} = \cos\theta - i\sin\theta$:
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2} \qquad \text{and} \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

---

### 5. Solving Quadratic Equations in $\mathbb{C}$

#### 5.1 Equations with Real Coefficients
Consider the equation $a z^2 + b z + c = 0$, where $a, b, c \in \mathbb{R}$ with $a \neq 0$.
Compute the standard discriminant $\Delta = b^2 - 4ac$.

> **📐 Theorem — Quadratic Solutions over $\mathbb{R}$ and $\mathbb{C}$**
> - If $\Delta > 0$: two distinct real roots:
>   $$z_1 = \frac{-b - \sqrt{\Delta}}{2a} \quad \text{and} \quad z_2 = \frac{-b + \sqrt{\Delta}}{2a}$$
> - If $\Delta = 0$: a single double real root:
>   $$z_0 = -\frac{b}{2a}$$
> - If $\Delta < 0$: two distinct complex roots that are **complex conjugates**:
>   $$z_1 = \frac{-b - i\sqrt{-\Delta}}{2a} \quad \text{and} \quad z_2 = \frac{-b + i\sqrt{-\Delta}}{2a} = \bar{z}_1$$

*Proof for $\Delta < 0$:*
Completing the square yields:
$$a \left[ \left(z + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a^2} \right] = 0$$
Since $\Delta < 0$, $-\Delta > 0$. We can write $-\Delta = (\sqrt{-\Delta})^2$.
Thus:
$$-\frac{\Delta}{4a^2} = \frac{-\Delta}{(2a)^2} = - i^2 \frac{-\Delta}{(2a)^2} = - \left( \frac{i\sqrt{-\Delta}}{2a} \right)^2$$
Factoring via the difference of squares $A^2 - B^2 = (A - B)(A + B)$:
$$\left( z + \frac{b}{2a} - \frac{i\sqrt{-\Delta}}{2a} \right) \left( z + \frac{b}{2a} + \frac{i\sqrt{-\Delta}}{2a} \right) = 0$$
Directly producing the two stated roots.

#### 5.2 Equations with Complex Coefficients and Complex Square Roots
What if the equation has complex coefficients?
For example: $z^2 + (1 + 4i)z - (5 + i) = 0$.
The discriminant $\Delta = B^2 - 4AC$ is an arbitrary complex number $Z = X + iY$.
To apply the quadratic formula $\frac{-B \pm \delta}{2A}$, we need to find a complex number $\delta = x + iy$ such that:
$$\delta^2 = Z$$
Such a number $\delta$ is called a **complex square root** of $Z$.

> **🧭 Method — Finding Complex Square Roots of $X + iY$**
> Let $\delta = x + iy$ with $x, y \in \mathbb{R}$.
> Set up the three-equation system:
> 1. Equality of squares: $\delta^2 = (x^2 - y^2) + 2ixy = X + iY$
>    - Real part: $x^2 - y^2 = X$
>    - Imaginary part: $2xy = Y$
> 2. Equality of moduli (the crucial shortcut):
>    $$|\delta|^2 = |Z| \iff x^2 + y^2 = \sqrt{X^2 + Y^2}$$
>
> Adding the real-part equation to the modulus equation:
> $$2x^2 = \sqrt{X^2 + Y^2} + X \implies x = \pm \sqrt{\frac{\sqrt{X^2+Y^2} + X}{2}}$$
> Subtracting:
> $$2y^2 = \sqrt{X^2 + Y^2} - X \implies y = \pm \sqrt{\frac{\sqrt{X^2+Y^2} - X}{2}}$$
> The sign condition on $xy$ (governed by $2xy = Y$) determines the two opposite pairs $(x, y)$.

---

### 6. The $n$-th Roots of Unity and Regular Polygons

Let us find all complex numbers $z$ satisfying:
$$z^n = 1 \quad (n \in \mathbb{N}^*)$$

Express $z$ in exponential form $z = r e^{i\theta}$:
$$(r e^{i\theta})^n = r^n e^{in\theta} = 1 = 1 e^{i 0}$$
Equating moduli and arguments:
- $r^n = 1 \implies r = 1$ (since $r > 0$).
- $n\theta \equiv 0 \pmod{2\pi} \implies n\theta = 2k\pi \implies \theta = \frac{2k\pi}{n}$ for $k \in \mathbb{Z}$.

> **📐 Theorem — The Group of $n$-th Roots of Unity**
> There exist exactly $n$ distinct complex solutions to $z^n = 1$, denoted $\mathbb{U}_n$:
> $$\mathbb{U}_n = \left\{ \omega_k = e^{i \frac{2k\pi}{n}} \ \middle|\ k \in \{0, 1, 2, \dots, n-1\} \right\}$$
> Setting $\omega = e^{i \frac{2\pi}{n}}$, these roots are the successive powers of $\omega$:
> $$\mathbb{U}_n = \{1, \omega, \omega^2, \dots, \omega^{n-1}\}$$

```
                6th Roots of Unity (Regular Hexagon)
                                 ▲ Im
                                 │
                         ω² ●    │    ● ω¹ = e^(iπ/3)
                             \   │   /
                              \  │  /
           ω³ = -1 ●─────────────┼─────────────● ω⁰ = 1  ──► Re
                              /  │  \
                             /   │   \
                         ω⁴ ●    │    ● ω⁵ = e^(-iπ/3)
                                 ▼
```

> **📐 Geometric Properties**
> 1. **Regular Polygon:** The points representing the $n$-th roots of unity form the vertices of a **regular $n$-sided polygon** inscribed in the unit circle, with one vertex at $(1, 0)$.
> 2. **Vanishing Sum (Center of Gravity):**
>    For every $n \geq 2$:
>    $$\sum_{k=0}^{n-1} e^{i \frac{2k\pi}{n}} = 1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0$$

*Proof of the Vanishing Sum:*
This is a geometric series with common ratio $\omega = e^{i \frac{2\pi}{n}} \neq 1$:
$$1 + \omega + \dots + \omega^{n-1} = \frac{1 - \omega^n}{1 - \omega} = \frac{1 - 1}{1 - \omega} = 0.$$
Physically, this represents the equilibrium of forces symmetrically distributed around a center of rotation!

---

### 7. Geometric Applications: Distances, Angles, and Transformations

#### 7.1 Affixes, Distances, and Oriented Angles
In the complex plane equipped with an orthonormal frame $(O; \vec{u}, \vec{v})$:
- To every point $M(x, y)$ or vector $\vec{V}(x, y)$, we associate its **affix (complex coordinate)** $z = x + iy$.
- The vector $\vec{AB}$ has affix $z_{\vec{AB}} = z_B - z_A$.
- The **distance** $AB$ is the modulus:
  $$AB = \|\vec{AB}\| = |z_B - z_A|$$

> **📐 Theorem — Oriented Angle Between Two Vectors**
> For any four points $A, B, C, D$ with $A \neq B$ and $C \neq D$:
> $$(\vec{AB}, \vec{CD}) \equiv \arg\left(\frac{z_D - z_C}{z_B - z_A}\right) \pmod{2\pi}$$

#### 7.2 Collinearity and Orthogonality Criteria
Define the ratio $Z = \frac{z_C - z_A}{z_B - z_A}$:
- **Collinear Points (Alignment):**
  Points $A, B, C$ are collinear if and only if the angle $(\vec{AB}, \vec{AC})$ equals $0$ or $\pi$ modulo $2\pi$:
  $$A, B, C \text{ collinear} \iff \frac{z_C - z_A}{z_B - z_A} \in \mathbb{R}$$
- **Perpendicular Lines (Orthogonality):**
  Lines $(AB)$ and $(CD)$ are perpendicular if and only if the angle $(\vec{AB}, \vec{CD})$ equals $\pm \frac{\pi}{2}$ modulo $2\pi$:
  $$(AB) \perp (CD) \iff \frac{z_D - z_C}{z_B - z_A} \in i\mathbb{R} \quad \left(\text{purely imaginary}\right)$$

#### 7.3 Plane Transformations via Complex Numbers

| Transformation | Geometric Definition | Complex Mapping ($z \mapsto z'$) |
|---|---|---|
| **Translation** by vector $\vec{w}$ (affix $b$) | $\vec{MM'} = \vec{w}$ | $$z' = z + b$$ |
| **Homothety (Dilation)** with center $\Omega(\omega)$ and ratio $k \in \mathbb{R}^*$ | $\vec{\Omega M'} = k \vec{\Omega M}$ | $$z' - \omega = k(z - \omega)$$ |
| **Rotation** with center $\Omega(\omega)$ and angle $\theta \in \mathbb{R}$ | $\Omega M' = \Omega M$ and $(\vec{\Omega M}, \vec{\Omega M'}) = \theta$ | $$z' - \omega = e^{i\theta}(z - \omega)$$ |
| **Direct Similitude** with center $\Omega$, ratio $k$, and angle $\theta$ | Composition of homothety and rotation | $$z' = a z + b \quad (a \in \mathbb{C}^*)$$ |

*Elegance of Rotation:*
A rotation centered at the origin by angle $\theta$ is simply expressed as $z' = e^{i\theta} z$.
Multiplying by $e^{i\pi/2} = i$ rotates the plane by $\pi/2$!

---

### 8. Step-by-Step Worked Examples

#### Example 1: Algebraic Form, Trigonometric Form, and Powers
Let $z_1 = 1 + i\sqrt{3}$ and $z_2 = 1 - i$.
1. Determine the modulus and a principal argument of $z_1$ and $z_2$.
2. Write $z_1$ and $z_2$ in exponential form.
3. Deduce the exponential form and then the algebraic form of the quotient $Z = \frac{z_1}{z_2}$.
4. Deduce the exact values of $\cos\left(\frac{7\pi}{12}\right)$ and $\sin\left(\frac{7\pi}{12}\right)$.
5. Calculate $(z_1)^{12}$.

**Detailed Solution:**
1. - For $z_1 = 1 + i\sqrt{3}$:
     $|z_1| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$.
     $z_1 = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right)$. We seek $\theta_1$ such that $\cos\theta_1 = \frac{1}{2}$ and $\sin\theta_1 = \frac{\sqrt{3}}{2}$, yielding $\theta_1 \equiv \frac{\pi}{3} \pmod{2\pi}$.
   - For $z_2 = 1 - i$:
     $|z_2| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
     $z_2 = \sqrt{2}\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right)$, yielding $\theta_2 \equiv -\frac{\pi}{4} \pmod{2\pi}$.
2. $z_1 = 2 e^{i\frac{\pi}{3}}$ and $z_2 = \sqrt{2} e^{-i\frac{\pi}{4}}$.
3. Quotient in exponential form:
   $$Z = \frac{z_1}{z_2} = \frac{2 e^{i\frac{\pi}{3}}}{\sqrt{2} e^{-i\frac{\pi}{4}}} = \frac{2}{\sqrt{2}} e^{i\left(\frac{\pi}{3} - (-\frac{\pi}{4})\right)} = \sqrt{2} e^{i\left(\frac{4\pi+3\pi}{12}\right)} = \sqrt{2} e^{i\frac{7\pi}{12}}$$
   Algebraic form by multiplying numerator and denominator by the conjugate:
   $$Z = \frac{1 + i\sqrt{3}}{1 - i} = \frac{(1 + i\sqrt{3})(1 + i)}{(1 - i)(1 + i)} = \frac{1 + i + i\sqrt{3} + i^2\sqrt{3}}{1^2 + (-1)^2} = \frac{(1 - \sqrt{3}) + i(1 + \sqrt{3})}{2}$$
4. Equating the two forms of $Z = \sqrt{2}\left(\cos\frac{7\pi}{12} + i\sin\frac{7\pi}{12}\right)$:
   - $\sqrt{2}\cos\left(\frac{7\pi}{12}\right) = \frac{1 - \sqrt{3}}{2} \implies \cos\left(\frac{7\pi}{12}\right) = \frac{1 - \sqrt{3}}{2\sqrt{2}} = \frac{\sqrt{2} - \sqrt{6}}{4}$.
   - $\sqrt{2}\sin\left(\frac{7\pi}{12}\right) = \frac{1 + \sqrt{3}}{2} \implies \sin\left(\frac{7\pi}{12}\right) = \frac{1 + \sqrt{3}}{2\sqrt{2}} = \frac{\sqrt{2} + \sqrt{6}}{4}$.
5. Power:
   $$(z_1)^{12} = \left(2 e^{i\frac{\pi}{3}}\right)^{12} = 2^{12} e^{i \frac{12\pi}{3}} = 4096 \, e^{i 4\pi} = 4096 \times 1 = 4\,096.$$

#### Example 2: Solving Real-Coefficient Quadratics
Solve in $\mathbb{C}$:
$$z^2 - 4z + 13 = 0$$

**Detailed Solution:**
Coefficients are $a = 1, b = -4, c = 13$.
Compute the discriminant:
$$\Delta = b^2 - 4ac = (-4)^2 - 4 \times 1 \times 13 = 16 - 52 = -36 < 0$$
Since $\Delta < 0$, the equation has two complex conjugate roots.
With $-36 = (6i)^2$, we have $\sqrt{-\Delta} = \sqrt{36} = 6$.
$$z_1 = \frac{-(-4) - 6i}{2 \times 1} = \frac{4 - 6i}{2} = 2 - 3i$$
$$z_2 = \frac{-(-4) + 6i}{2 \times 1} = \frac{4 + 6i}{2} = 2 + 3i = \bar{z}_1$$
The solution set is $S = \{2 - 3i ; 2 + 3i\}$.

#### Example 3: Finding Square Roots of a Complex Number
Find the complex square roots of $Z = 3 + 4i$.

**Detailed Solution:**
We seek $\delta = x + iy$ ($x, y \in \mathbb{R}$) such that $\delta^2 = 3 + 4i$.
1. Real part: $x^2 - y^2 = 3$.
2. Imaginary part: $2xy = 4 \implies xy = 2 > 0$ (so $x$ and $y$ share the same sign).
3. Modulus: $|\delta|^2 = |Z| \iff x^2 + y^2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.

Adding and subtracting:
- $(x^2 + y^2) + (x^2 - y^2) = 5 + 3 \implies 2x^2 = 8 \implies x^2 = 4 \implies x = \pm 2$.
- $(x^2 + y^2) - (x^2 - y^2) = 5 - 3 \implies 2y^2 = 2 \implies y^2 = 1 \implies y = \pm 1$.

Since $xy = 2 > 0$:
- If $x = 2$, then $y = 1 \implies \delta_1 = 2 + i$.
- If $x = -2$, then $y = -1 \implies \delta_2 = -2 - i = -\delta_1$.
The two complex square roots of $3 + 4i$ are **$2 + i$** and **$-2 - i$**.
*(Verification: $(2+i)^2 = 4 + 4i + i^2 = 3 + 4i$).*

#### Example 4: Quadratic Equation with Complex Coefficients
Solve in $\mathbb{C}$:
$$z^2 - (3 + 2i)z + (5 + i) = 0$$

**Detailed Solution:**
Compute the discriminant $\Delta = B^2 - 4AC$:
$$\Delta = (3 + 2i)^2 - 4(1)(5 + i) = (9 + 12i - 4) - (20 + 4i) = (5 + 12i) - 20 - 4i = -15 + 8i$$
Find a square root $\delta = x + iy$ of $\Delta = -15 + 8i$:
- $x^2 - y^2 = -15$
- $2xy = 8 \implies xy = 4 > 0$
- $x^2 + y^2 = \sqrt{(-15)^2 + 8^2} = \sqrt{225 + 64} = \sqrt{289} = 17$

By half-sum and half-difference:
- $2x^2 = 17 - 15 = 2 \implies x^2 = 1 \implies x = \pm 1$.
- $2y^2 = 17 - (-15) = 32 \implies y^2 = 16 \implies y = \pm 4$.
Since $xy > 0$, we choose $\delta = 1 + 4i$.
The solutions are:
$$z_1 = \frac{(3 + 2i) + (1 + 4i)}{2} = \frac{4 + 6i}{2} = 2 + 3i$$
$$z_2 = \frac{(3 + 2i) - (1 + 4i)}{2} = \frac{2 - 2i}{2} = 1 - i$$
The solution set is $S = \{1 - i ; 2 + 3i\}$.

#### Example 5: Geometric Nature of a Triangle via Affixes
In the complex plane, consider points $A, B, C$ with respective coordinates:
$$z_A = 1 + i, \quad z_B = 3 - i, \quad z_C = 2 + 2i$$
1. Calculate the quotient $Z = \frac{z_C - z_A}{z_B - z_A}$.
2. Deduce the exact nature of triangle $ABC$.

**Detailed Solution:**
1. Compute the affixes of vectors $\vec{AC}$ and $\vec{AB}$:
   - $z_C - z_A = (2 + 2i) - (1 + i) = 1 + i$
   - $z_B - z_A = (3 - i) - (1 + i) = 2 - 2i$
   Evaluate the quotient:
   $$Z = \frac{1 + i}{2 - 2i} = \frac{(1 + i)(2 + 2i)}{(2 - 2i)(2 + 2i)} = \frac{2 + 2i + 2i + 2i^2}{2^2 + (-2)^2} = \frac{4i}{8} = \frac{1}{2}i \in i\mathbb{R}$$
2. Since the quotient is purely imaginary, the angle $(\vec{AB}, \vec{AC}) \equiv \frac{\pi}{2} \pmod\pi$.
   Therefore, triangle $ABC$ is **right-angled at $A$**.

#### Example 6: Identifying a Rotation
Consider the plane transformation $f$ mapping every point $M$ with affix $z$ to $M'$ with affix:
$$z' = i z + 3 - i$$
1. Prove that $f$ has a unique invariant (fixed) point $\Omega$ and find its affix $\omega$.
2. Show that $f$ is a rotation and specify its center and angle.

**Detailed Solution:**
1. A point $\Omega(\omega)$ is fixed if and only if $f(\Omega) = \Omega$:
   $$\omega = i \omega + 3 - i \iff \omega(1 - i) = 3 - i \iff \omega = \frac{3 - i}{1 - i}$$
   Multiply numerator and denominator by $1 + i$:
   $$\omega = \frac{(3 - i)(1 + i)}{1^2 + (-1)^2} = \frac{3 + 3i - i - i^2}{2} = \frac{4 + 2i}{2} = 2 + i$$
   The unique invariant point is $\Omega$ with affix $\omega = 2 + i$.
2. Subtract $\omega$ from both sides of $z' = i z + 3 - i$:
   $$z' - \omega = i z + 3 - i - (2 + i) = i z + 1 - 2i = i(z - (2 + i)) = i(z - \omega)$$
   Since $i = e^{i\frac{\pi}{2}}$, the mapping becomes:
   $$z' - \omega = e^{i\frac{\pi}{2}}(z - \omega)$$
   This is the standard equation of a **rotation with center $\Omega(2+i)$ and angle $\frac{\pi}{2}$** (a positive quarter-turn).

---

### Key Takeaways

1. **Algebraic Form:**
   - $z = a + ib$ with $a = \text{Re}(z) \in \mathbb{R}$ and $b = \text{Im}(z) \in \mathbb{R}$.
   - Complex conjugate: $\bar{z} = a - ib$, with $z\bar{z} = a^2 + b^2 = |z|^2$.
   - Modulus: $|z| = \sqrt{a^2 + b^2}$.

2. **Trigonometric and Exponential Forms:**
   - $z = r(\cos\theta + i\sin\theta) = r e^{i\theta}$ with $r = |z|$ and $\theta \equiv \arg(z) \pmod{2\pi}$.
   - Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$. De Moivre's formula: $(e^{i\theta})^n = e^{in\theta}$.

3. **Quadratic Equations:**
   - If $\Delta < 0$ in $az^2 + bz + c = 0$ ($a, b, c \in \mathbb{R}$): $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$.
   - Complex square roots of $X + iY$: solve $\{x^2 - y^2 = X, 2xy = Y, x^2 + y^2 = \sqrt{X^2+Y^2}\}$.

4. **$n$-th Roots of Unity:**
   - $\mathbb{U}_n = \{e^{i \frac{2k\pi}{n}} \mid k \in \{0, \dots, n-1\}\}$, representing vertices of a regular polygon centered at 0 with zero sum.

5. **Complex Geometry:**
   - Distance: $AB = |z_B - z_A|$.
   - Angle: $(\vec{AB}, \vec{CD}) \equiv \arg\left(\frac{z_D - z_C}{z_B - z_A}\right) \pmod{2\pi}$.
   - Rotation: $z' - \omega = e^{i\theta}(z - \omega)$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 1.** Write in algebraic form $a + ib$:
1. $z_1 = (2 + 3i)(4 - i)$
2. $z_2 = (3 - 2i)^2$
3. $z_3 = \frac{1}{2 + i}$
4. $z_4 = \frac{3 + 5i}{1 - 2i}$
**Exercise 2.** Determine the modulus and principal argument of:
$z_A = -3$, $z_B = 2i$, $z_C = 1 + i$, $z_D = -\sqrt{3} + i$.
**Exercise 3.** Solve in $\mathbb{C}$:
1. $z^2 + 9 = 0$
2. $z^2 - 2z + 5 = 0$
3. $2z^2 + 2z + 1 = 0$
**Exercise 4.** Compute $i^n$ for $n \in \{2024, 2025, 2026, 2027\}$.
**Exercise 5.** Linearize $\cos^2(x)$ and $\sin^2(x)$ using Euler's formulas.
**Exercise 6.** State the affix of vector $\vec{AB}$ and distance $AB$ for $A(3 - 2i)$ and $B(-1 + i)$.
**Exercise 7.** Identify the geometric transformation associated with:
1. $z' = z + 4 - 3i$
2. $z' = -z$
3. $z' = i z$

#### Level ★★ (Exploration and Advanced Geometry)

**Exercise 8.** Solve in $\mathbb{C}$: $2z + 3\bar{z} = 5 + 2i$.
**Exercise 9.** Determine the locus of points $M$ with affix $z$ such that:
1. $|z - 3 + 2i| = 5$
2. $|z - 2| = |z + 4i|$
3. $\frac{z - 1}{z + 1} \in i\mathbb{R}$
**Exercise 10.** Complex square roots:
Calculate the complex square roots of $Z_1 = -7 + 24i$ and $Z_2 = 8 - 6i$.
**Exercise 11.** Solve in $\mathbb{C}$:
$$z^2 - (5 - i)z + (8 - i) = 0$$
**Exercise 12.** De Moivre's formula and trigonometry:
1. Expanding $(\cos x + i\sin x)^3$ in two ways, express $\cos(3x)$ in terms of $\cos(x)$, and $\sin(3x)$ in terms of $\sin(x)$.
2. Linearize $\cos^3(x)$.
**Exercise 13.** The number $j$ (primitive cube root of unity).
Let $j = e^{i\frac{2\pi}{3}} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$.
1. Verify that $j^2 = \bar{j} = e^{i\frac{4\pi}{3}}$ and $j^3 = 1$.
2. Prove that $1 + j + j^2 = 0$.
3. Compute $(1 + j)^{2025}$.
**Exercise 14.** Equilateral triangles.
Show that three points $A, B, C$ with affixes $a, b, c$ form a positively oriented equilateral triangle if and only if:
$$a + b j + c j^2 = 0 \quad \text{where } j = e^{i\frac{2\pi}{3}}$$
**Exercise 15.** Collinearity and concyclicity (cross-ratio).
Define the cross-ratio of four distinct points $A, B, C, D$ by:
$$[a, b, c, d] = \frac{(c - a)(d - b)}{(c - b)(d - a)}$$
Show that $A, B, C, D$ are concyclic (lying on a common circle) or collinear if and only if their cross-ratio is real.

#### Level ★★★ (Deepening and Olympiads)

**Exercise 16.** Napoleon's Theorem.
On the sides of an arbitrary positively oriented triangle $ABC$, construct three equilateral triangles externally with centroids $P, Q, R$.
Prove, using complex affixes and the root $j$, that triangle $PQR$ is **always equilateral**!
**Exercise 17.** Cardano's cubic method.
Consider $z^3 - 6z - 9 = 0$.
Setting $z = u + v$ with $3uv = 6$, determine $u^3$ and $v^3$ as roots of a quadratic equation, and deduce the real solution and the two complex roots.
**Exercise 18.** Trigonometric polynomials and the Dirichlet kernel.
For $x \not\equiv 0 \pmod{2\pi}$, compute the sum:
$$D_n(x) = 1 + 2\sum_{k=1}^n \cos(kx) = 1 + 2\cos(x) + 2\cos(2x) + \dots + 2\cos(nx)$$
Show that $D_n(x) = \frac{\sin\left((n + \frac{1}{2})x\right)}{\sin(\frac{x}{2})}$.
**Exercise 19.** Roots of unity and polynomial factorization.
1. Factor the polynomial $X^n - 1$ in $\mathbb{C}[X]$ using roots of unity.
2. By evaluating this factorization at a suitable point, prove the identity:
   $$\prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}}$$
**Exercise 20.** Fundamental Theorem of Algebra (D'Alembert-Gauss, outline).
Explain why every non-constant polynomial with complex coefficients has at least one root in $\mathbb{C}$, and why this implies that $\mathbb{C}$ is algebraically closed (unlike $\mathbb{R}$).
**Exercise 21.** Euler Line and Euler Circle.
Let triangle $ABC$ be inscribed in a circle centered at origin $O$ ($|a| = |b| = |c| = R$).
1. Show that $H$ with affix $h = a + b + c$ is the orthocenter.
2. Show that centroid $G$ has affix $g = \frac{a+b+c}{3}$.
3. Deduce that $O, G, H$ are collinear (Euler line) and $\vec{OH} = 3\vec{OG}$.
**Exercise 22.** Möbius Transformations.
Consider the linear fractional transformation $f(z) = \frac{az + b}{cz + d}$ with $ad - bc \neq 0$.
Show that such a map transforms circles and lines into circles or lines.

---

### Solutions

**Solution 1:**
1. $z_1 = 8 - 2i + 12i - 3i^2 = 8 + 10i + 3 = 11 + 10i$.
2. $z_2 = 9 - 12i + 4i^2 = 5 - 12i$.
3. $z_3 = \frac{2 - i}{2^2 + 1^2} = \frac{2}{5} - \frac{1}{5}i$.
4. $z_4 = \frac{(3+5i)(1+2i)}{1^2 + (-2)^2} = \frac{3 + 6i + 5i - 10}{5} = \frac{-7 + 11i}{5} = -\frac{7}{5} + \frac{11}{5}i$.

**Solution 2:**
- $z_A = -3$: $|z_A| = 3$, $\arg(z_A) = \pi$.
- $z_B = 2i$: $|z_B| = 2$, $\arg(z_B) = \frac{\pi}{2}$.
- $z_C = 1+i$: $|z_C| = \sqrt{2}$, $\arg(z_C) = \frac{\pi}{4}$.
- $z_D = -\sqrt{3} + i$: $|z_D| = \sqrt{3+1} = 2$, $\cos\theta = -\frac{\sqrt{3}}{2}, \sin\theta = \frac{1}{2} \implies \arg(z_D) = \frac{5\pi}{6}$.

**Solution 3:**
1. $z^2 = -9 = (3i)^2 \iff z \in \{-3i, 3i\}$.
2. $\Delta = 4 - 20 = -16 = (4i)^2 \implies z = \frac{2 \pm 4i}{2} = 1 \pm 2i$.
3. $\Delta = 4 - 8 = -4 = (2i)^2 \implies z = \frac{-2 \pm 2i}{4} = -\frac{1}{2} \pm \frac{1}{2}i$.

**Solution 4:**
Since $i^4 = 1$:
- $2024 = 4 \times 506 \implies i^{2024} = 1$.
- $i^{2025} = i$, $i^{2026} = -1$, $i^{2027} = -i$.

**Solution 5:**
$\cos^2(x) = \left(\frac{e^{ix} + e^{-ix}}{2}\right)^2 = \frac{e^{2ix} + 2 + e^{-2ix}}{4} = \frac{\cos(2x) + 1}{2}$.
$\sin^2(x) = \left(\frac{e^{ix} - e^{-ix}}{2i}\right)^2 = \frac{e^{2ix} - 2 + e^{-2ix}}{-4} = \frac{1 - \cos(2x)}{2}$.

**Solution 6:**
$z_{\vec{AB}} = z_B - z_A = (-1+i) - (3-2i) = -4 + 3i$.
$AB = |-4 + 3i| = \sqrt{(-4)^2 + 3^2} = \sqrt{16 + 9} = 5$.

**Solution 7:**
1. Translation by vector with affix $4 - 3i$.
2. Central symmetry with respect to origin $O$ (rotation by angle $\pi$).
3. Rotation centered at $O$ by angle $\frac{\pi}{2}$.

**Solution 8:**
Set $z = x + iy$. Then $\bar{z} = x - iy$.
$2(x + iy) + 3(x - iy) = 5x - iy$.
Equate to $5 + 2i$: $5x = 5 \implies x = 1$, and $-y = 2 \implies y = -2$.
Hence $z = 1 - 2i$.

**Solution 9:**
1. Let $A(3 - 2i)$: $AM = 5$. This is the circle centered at $A(3, -2)$ with radius 5.
2. Let $A(2)$ and $B(-4i)$: $AM = BM$. This is the perpendicular bisector of segment $[AB]$.
3. The argument of $\frac{z-1}{z+1}$ is $\pm \frac{\pi}{2} \pmod\pi$, which means $(\vec{MB}, \vec{MA}) \equiv \frac{\pi}{2} \pmod\pi$. This is the circle with diameter $[AB]$ (where $A(1)$ and $B(-1)$), excluding points $A$ and $B$.

**Solution 10:**
- For $Z_1 = -7 + 24i$: modulus $\sqrt{49 + 576} = 25$.
  $x^2 - y^2 = -7$, $x^2 + y^2 = 25 \implies 2x^2 = 18 \implies x = \pm 3$ and $y = \pm 4$. Since $2xy > 0$, the roots are $\pm(3 + 4i)$.
- For $Z_2 = 8 - 6i$: modulus $\sqrt{64 + 36} = 10$.
  $2x^2 = 18 \implies x = \pm 3$, $2y^2 = 2 \implies y = \pm 1$. Since $2xy = -6 < 0$, the roots are $\pm(3 - i)$.

**Solution 11:**
$\Delta = (5-i)^2 - 4(8-i) = (24 - 10i) - (32 - 4i) = -8 - 6i$.
Square roots of $-8 - 6i$: modulus $\sqrt{64+36} = 10$.
$2x^2 = 10 - 8 = 2 \implies x = \pm 1$, $2y^2 = 18 \implies y = \pm 3$. With $xy < 0$, $\delta = 1 - 3i$.
$z_1 = \frac{(5-i) + (1-3i)}{2} = 3 - 2i$, and $z_2 = \frac{(5-i) - (1-3i)}{2} = 2 + i$.

**Solution 12:**
1. $(\cos x + i\sin x)^3 = \cos^3 x + 3i\cos^2 x \sin x - 3\cos x \sin^2 x - i\sin^3 x$.
   By De Moivre, this equals $\cos(3x) + i\sin(3x)$.
   Equating parts: $\cos(3x) = \cos^3 x - 3\cos x(1 - \cos^2 x) = 4\cos^3 x - 3\cos x$.
   $\sin(3x) = 3(1 - \sin^2 x)\sin x - \sin^3 x = 3\sin x - 4\sin^3 x$.
2. $\cos^3 x = \frac{\cos(3x) + 3\cos x}{4}$.

**Solution 13:**
1. $j^2 = e^{i\frac{4\pi}{3}} = e^{-i\frac{2\pi}{3}} = \bar{j}$, and $j^3 = e^{i 2\pi} = 1$.
2. $1 + j + j^2 = \frac{1 - j^3}{1 - j} = 0$.
3. $1 + j = -j^2$. Thus $(1+j)^{2025} = (-j^2)^{2025} = -j^{4050} = -(j^3)^{1350} = -1$.

**Solution 14:**
Triangle $ABC$ is positively oriented equilateral if and only if $C$ is the image of $B$ under rotation centered at $A$ by angle $\pi/3$, which translates after vector rewriting to $(c - a) = -j^2(b - a)$, hence $a(1 + j^2) + b j^2 + c = 0$. Since $1 + j^2 = -j$, multiplying by $j^2$ yields $a + bj + cj^2 = 0$.

**Solution 15:**
The argument of the cross-ratio is $\arg\left(\frac{c-a}{c-b}\right) - \arg\left(\frac{d-a}{d-b}\right) = (\vec{BC}, \vec{AC}) - (\vec{BD}, \vec{AD})$.
This cross-ratio is real if and only if this angle difference is 0 modulo $\pi$, which is precisely the inscribed angle theorem condition for $A, B, C, D$ to be concyclic or collinear.

**Solution 16:**
Let $P, Q, R$ be the centroids of the equilateral triangles constructed on sides $[B,C], [C,A], [A,B]$. The outer vertices satisfy rotation relations of angle $\pi/3$. Expressing $p, q, r$ in terms of $a, b, c$ and $j$, computing $p + q j + r j^2$ vanishes identically due to $1 + j + j^2 = 0$. By Exercise 14, $PQR$ is equilateral.

**Solution 17:**
Setting $z = u + v$, $(u+v)^3 - 6(u+v) - 9 = u^3 + v^3 + 3uv(u+v) - 6(u+v) - 9 = 0$.
Setting $3uv = 6 \implies uv = 2 \implies u^3 v^3 = 8$, leaving $u^3 + v^3 = 9$.
$u^3$ and $v^3$ are roots of $X^2 - 9X + 8 = 0$, which are $1$ and $8$.
Set $u^3 = 8 \implies u = 2$ and $v^3 = 1 \implies v = 1$.
The real root is $z_0 = 2 + 1 = 3$.
Factoring $z^3 - 6z - 9 = (z - 3)(z^2 + 3z + 3)$, the discriminant of the quadratic factor is $\Delta = 9 - 12 = -3$, yielding the two complex roots: $z_{1,2} = \frac{-3 \pm i\sqrt{3}}{2}$.

**Solution 18:**
$D_n(x) = \sum_{k=-n}^n e^{ikx} = e^{-inx} \sum_{j=0}^{2n} e^{ijx} = e^{-inx} \frac{1 - e^{i(2n+1)x}}{1 - e^{ix}}$.
Factoring out half-angles in numerator and denominator:
$D_n(x) = e^{-inx} \frac{e^{i\frac{2n+1}{2}x} (-2i\sin(\frac{2n+1}{2}x))}{e^{i\frac{x}{2}} (-2i\sin(\frac{x}{2}))} = \frac{\sin\left((n+\frac{1}{2})x\right)}{\sin(\frac{x}{2})}$.

**Solution 19:**
1. The roots of $X^n - 1$ are $e^{i\frac{2k\pi}{n}}$. Thus $X^n - 1 = \prod_{k=0}^{n-1} (X - e^{i\frac{2k\pi}{n}}) = (X - 1) \prod_{k=1}^{n-1} (X - e^{i\frac{2k\pi}{n}})$.
2. Dividing by $X - 1$: $\sum_{j=0}^{n-1} X^j = \prod_{k=1}^{n-1} (X - e^{i\frac{2k\pi}{n}})$.
   Evaluating at $X = 1$, the left side equals $n$.
   On the right, $|1 - e^{i\frac{2k\pi}{n}}| = |e^{i\frac{k\pi}{n}} (e^{-i\frac{k\pi}{n}} - e^{i\frac{k\pi}{n}})| = 2\sin(\frac{k\pi}{n})$.
   Taking the product of moduli gives $n = 2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right)$, proving the formula.

**Solution 20:**
The field $\mathbb{C}$ is algebraically closed because every non-constant polynomial of degree $n$ splits completely into $n$ linear factors over $\mathbb{C}$ (counted with multiplicity). Proved rigorously by Gauss in 1799, this theorem demonstrates the completeness of the complex numbers: no further extension fields are needed to solve higher-degree polynomial equations.

**Solution 21:**
1. To check that $H$ is the orthocenter, compute the dot product $\vec{AH} \cdot \vec{BC}$. The affix of $\vec{AH}$ is $h - a = b + c$, and that of $\vec{BC}$ is $c - b$.
   The ratio $\frac{h-a}{c-b} = \frac{b+c}{c-b} = \frac{(b+c)(\bar{c}-\bar{b})}{|c-b|^2}$.
   On the unit circle, $\bar{b} = R^2/b$ and $\bar{c} = R^2/c$. The real part vanishes, proving $(AH) \perp (BC)$. The same holds for other altitudes.
2. The centroid $G$ has affix $g = \frac{a+b+c}{3}$.
3. We have $h = 3g$, which translates vectorially to $\vec{OH} = 3\vec{OG}$. Hence $O, G, H$ are collinear along the Euler line.

**Solution 22:**
Möbius transformations are compositions of translations, dilatations/rotations, and inversion $z \mapsto \frac{1}{z}$. Since inversion maps lines and circles into lines or circles (viewed as circles on the Riemann sphere), this family of curves is preserved.

---

### The Question That Opens the Next Step

Complex numbers demonstrated the supreme power of constructing new mathematical structures to overcome algebraic obstacles.
What happens when we return to the most primal and unyielding numbers: the natural integers?
How can the remainders of simple division algorithms safeguard state secrets and secure bank cards across the globe?
The clock ticks, hands align modulo $n$: welcome to **Chapter 56 and Secret Messages and the Clock of Remainders**.
