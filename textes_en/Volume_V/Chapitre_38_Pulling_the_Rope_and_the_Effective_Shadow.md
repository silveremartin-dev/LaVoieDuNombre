# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 38: Pulling the Rope and the Effective Shadow

> *“When you pull a burden with an oblique rope, your muscles burn, your brow drips with sweat, and yet the load crawls forward at a snail’s pace. Why? Because the universe does not reward you for effort spent into the void: it counts only the useful shadow of your force along the path.”*

---

### What You Are About to Discover

- Why ordinary multiplication between two numbers is not enough when we want to multiply **two arrows** (two vectors).
- The physical meaning of the **work of a force** and the discovery of the **scalar product** (dot product).
- The geometry of the **orthogonal projection**: how to let light fall from above to measure the effective shadow.
- The four faces of the dot product: by **cosine**, by **projection**, by **Cartesian coordinates** ($xx' + yy'$), and by **lengths alone** (polarization identities).
- The absolute criterion of **orthogonality** and its crowning application: finding the normal vector to a line and its Cartesian equation $ax + by + c = 0$.
- The powerful metric theorems of the triangle: **Al-Kashi's theorem** (generalized Pythagorean theorem / Law of Cosines) and the **median theorem**.
- Determining **geometric loci**: characterizing a circle by the dot product $\vec{MA} \cdot \vec{MB} = 0$.

---

### 1. The Problem: The Towhorse and the Coal Barge

At the dawn of the nineteenth century, in the furnace of the Industrial Revolution, coal is the lifeblood powering the steam engines. To transport thousands of tons of coal from northern collieries to the factories of Paris or London, the inland waterway network is the most economical route. Heavy, broad-beamed barges weighing over a hundred tons glide silently along the canals.

These barges do not yet have engines. They are towed from dry land by a powerful draft horse treading heavily along the dirt path running beside the canal: the **towpath**.

Observe the scene from a footbridge above the water:

```
                         Towpath
    Horse   o══════════════════════════════════════════════════════►
             \
              \  Taut hemp rope
               \  Muscular force F (angle θ)
                \
                 \
                  o────────────────────────────────────────────────►
                Barge         Straight displacement d along the canal
```

The canal is straight. The barge glides forward along a displacement vector $\vec{d}$.
But the horse cannot walk on water! It is forced to march along the bank. The long hemp rope therefore makes an **oblique angle $\theta$** relative to the direction of the canal.

The horse strains its haunches, its hooves dig into the clay, its chest presses into the leather harness collar: it exerts a considerable force $\vec{F}$.
Yet a young barge apprentice sitting by the tiller notices something puzzling:
*“The horse is exhausting itself, yet the barge moves forward only very slowly. Why?”*

The seasoned boatman replies:
*“Because part of its force pulls the boat sideways toward the bank! That part contributes nothing to moving forward: it tries only to ground the barge in the reeds. I have to fight against it constantly by leaning on the tiller. Only the part of the force pointing straight ahead, parallel to the water, produces useful motion.”*

```
                  F (total effort deployed)
                 ▲
                /│
               / │
              /  │  Wasted lateral component (pulls toward the bank)
             /   │
            /θ   │
           o─────┴────────────────────────────────► Canal (displacement d)
           |◄── Effective shadow ──►|
               ||F|| × cos(θ)
```

To measure the energy actually delivered to the boat, multiplying force by distance is not enough. We must **extract the effective shadow of the force along the direction of motion**.

---

### 2. The Work of a Force and the Geometric Definition

#### 2.1 From Physical Action to the Scalar Product

In physics, when an object undergoes a constant force $\vec{F}$ over a rectilinear displacement $\vec{d} = \vec{AB}$, the mechanical energy transferred is called the **work of the force**, denoted $W$ (for *Work*).

If the force were perfectly aligned with the motion ($\theta = 0$), the entire force would contribute: $W = \|\vec{F}\| \times \|\vec{d}\|$.
When the rope is tilted at an angle $\theta$, the effective shadow of the force along the path is $\|\vec{F}\| \cos\theta$. The work is then written:

$$W = \|\vec{F}\| \times \|\vec{d}\| \times \cos\theta.$$

To formalize this mathematical operation combining two vectors $\vec{u}$ and $\vec{v}$ to produce **a single real number** (a scalar, as opposed to a vector), mathematicians forged a universal concept.

> **📐 Definition — Scalar Product (by Norm and Cosine)**
> Let $\vec{u}$ and $\vec{v}$ be two vectors in the plane.
> - If either vector is the zero vector ($\vec{u} = \vec{0}$ or $\vec{v} = \vec{0}$), their scalar product is zero: $\vec{u} \cdot \vec{v} = 0$.
> - If $\vec{u} \neq \vec{0}$ and $\vec{v} \neq \vec{0}$, set $\vec{u} = \vec{OA}$ and $\vec{v} = \vec{OB}$. The **scalar product** (or **dot product**) of $\vec{u}$ and $\vec{v}$, denoted $\vec{u} \cdot \vec{v}$, is the real number defined by:
>
> $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\widehat{AOB}).$$

**Reading and Pronunciation:**
$\vec{u} \cdot \vec{v}$ is read aloud as “**$\vec{u}$ dot $\vec{v}$**”. The centered dot “$\cdot$” is reserved for this operation.

> **🔍 The True History — Where Does the Word “Scalar” Come From?**
> The word comes from the Latin *scala*, meaning “ladder” or “scale”. The Irish mathematician **William Rowan Hamilton** introduced it in 1843 when inventing quaternions: he called the pure numerical part, which is marked on a standard numerical scale, the “scalar part”, distinguishing it from the directional “vector part”. The modern dot product with a dot symbol was popularized by the American physicist **Josiah Willard Gibbs** in the late nineteenth century.

#### 2.2 The Three Regimes of the Rope

The value of the dot product depends on the angle $\theta$ between the two vectors:

1. **Acute angle ($0 \leqslant \theta < \frac{\pi}{2}$): strictly positive dot product.**
   $\cos\theta > 0$. The force assists the displacement: physicists speak of **motive work**. The shadow falls in the direction of motion.
2. **Right angle ($\theta = \frac{\pi}{2}$, or $90^\circ$): zero dot product.**
   $\cos\left(\frac{\pi}{2}\right) = 0$, hence $\vec{u} \cdot \vec{v} = 0$.
   If the horse pulls perpendicularly to the canal, the barge does not advance a millimeter along the waterway. All energy is wasted trying to collapse the bank.
3. **Obtuse angle ($\frac{\pi}{2} < \theta \leqslant \pi$): strictly negative dot product.**
   $\cos\theta < 0$. The force opposes the displacement: this is the role of brakes or hydrodynamic friction, which physicists call **resistive work**.

```
    θ acute: u · v > 0            θ = 90°: u · v = 0            θ obtuse: u · v < 0
       v                             v                               v
      ▲                             ▲                                 ▲
     /                             │                                   \
    /  θ                          │                                 θ   \
   o───────► u                    o───────► u                    ◄───────o
   Motive work                    Zero work                      u   Resistive work
```

> **⚠️ Beware: Common Pitfall! — A Scalar Is Not a Vector**
> The dot product of two vectors is **never a vector**! It is a **real number** (which can be positive, zero, or negative). Writing $\vec{u} \cdot \vec{v} = \vec{0}$ with an arrow over the zero is a severe error of notation. Always write $\vec{u} \cdot \vec{v} = 0$.

---

### 3. The Orthogonal Projection: Measuring the Cast Shadow

#### 3.1 Definition by Projection

Instead of calculating a cosine, it is often much faster to drop a perpendicular.

> **📐 Property — Definition by Orthogonal Projection**
> Let $\vec{u} = \vec{OA}$ and $\vec{v} = \vec{OB}$ be two non-zero vectors.
> Let $H$ be the orthogonal projection of point $B$ onto the line $(OA)$.
>
> $$\vec{u} \cdot \vec{v} = \vec{OA} \cdot \vec{OB} = \vec{OA} \cdot \vec{OH}.$$
>
> In terms of directed lengths along the axis $(OA)$:
> - If $\vec{OH}$ and $\vec{OA}$ point in the **same direction** (acute angle): $\vec{u} \cdot \vec{v} = OA \times OH$.
> - If $\vec{OH}$ and $\vec{OA}$ point in **opposite directions** (obtuse angle): $\vec{u} \cdot \vec{v} = - OA \times OH$.

```
    Case 1: Same direction                 Case 2: Opposite directions
           B                                            B
          /│                                            │\
         / │                                            │ \
        /  │                                            │  \
       o───┴─────────►                               ───┴───o────────►
       O   H         A                                  H   O        A
       u · v = + OA × OH                                u · v = - OA × OH
```

> **✍️ Proof**
> In the triangle $OHB$, right-angled at $H$:
> - If the angle $\widehat{AOB}$ is acute, $\cos(\widehat{AOB}) = \frac{OH}{OB}$, so $OH = OB \cos(\widehat{AOB})$.
>   Thus, $\vec{OA} \cdot \vec{OB} = OA \times OB \cos(\widehat{AOB}) = OA \times OH$.
> - If the angle $\widehat{AOB}$ is obtuse, the projected point $H$ lies on the opposite side of $O$. The adjacent angle inside the right-angled triangle is $\pi - \widehat{AOB}$.
>   Since $\cos(\pi - \theta) = -\cos\theta$, we have $OH = OB \cos(\pi - \widehat{AOB}) = -OB \cos(\widehat{AOB})$.
>   Consequently, $OA \times OB \cos(\widehat{AOB}) = -OA \times OH$.
> In both cases, the result exactly matches the stated formula. $\blacksquare$

> **💡 Did You Know? — The Symmetry of the Dot Product**
> Projecting $B$ onto $(OA)$ gives the exact same result as projecting $A$ onto $(OB)$!
> Indeed, $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta = \|\vec{v}\| \|\vec{u}\| \cos\theta = \vec{v} \cdot \vec{u}$.
> The dot product is **commutative**.

#### 3.2 The Scalar Square

What happens when we take the dot product of a vector with itself?
The angle between $\vec{u}$ and $\vec{u}$ is zero ($\theta = 0$), and $\cos(0) = 1$.

> **📐 Definition — Scalar Square**
> For any vector $\vec{u}$, we write $\vec{u}^2 = \vec{u} \cdot \vec{u}$. We have:
>
> $$\vec{u}^2 = \|\vec{u}\|^2.$$
>
> The scalar square of a vector is equal to the square of its norm. It is a **non-negative real number**, and $\vec{u}^2 = 0 \iff \vec{u} = \vec{0}$.
> For a geometric segment $[AB]$, we have $\vec{AB}^2 = AB^2$.

---

### 4. Analytical Expression in an Orthonormal Coordinate System

#### 4.1 The Formula $xx' + yy'$

When the plane is equipped with an orthonormal coordinate system $(O; \vec{i}, \vec{j})$, the unit basis vectors satisfy:
- $\|\vec{i}\| = 1$ and $\|\vec{j}\| = 1$, so $\vec{i}^2 = 1$ and $\vec{j}^2 = 1$.
- $\vec{i}$ and $\vec{j}$ are perpendicular, so $\vec{i} \cdot \vec{j} = 0$.

Here the beauty of algebra dramatically simplifies geometric computations:

> **📐 Theorem — Analytical Formula for the Dot Product**
> In an **orthonormal** coordinate system $(O; \vec{i}, \vec{j})$, if $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ and $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$, then:
>
> $$\boxed{\vec{u} \cdot \vec{v} = xx' + yy'}$$

> **✍️ Proof**
> By the bilinearity of the scalar product (expanding just like an ordinary product):
> $$\begin{aligned}
> \vec{u} \cdot \vec{v} &= (x\vec{i} + y\vec{j}) \cdot (x'\vec{i} + y'\vec{j}) \\
> &= xx'(\vec{i} \cdot \vec{i}) + xy'(\vec{i} \cdot \vec{j}) + yx'(\vec{j} \cdot \vec{i}) + yy'(\vec{j} \cdot \vec{j}).
> \end{aligned}$$
> Since $\vec{i} \cdot \vec{i} = 1$, $\vec{j} \cdot \vec{j} = 1$, and $\vec{i} \cdot \vec{j} = \vec{j} \cdot \vec{i} = 0$, the two cross-terms vanish entirely! We are left with:
> $$\vec{u} \cdot \vec{v} = xx'(1) + 0 + 0 + yy'(1) = xx' + yy'. \quad \blacksquare$$

> **⚠️ Beware: Common Pitfall! — Coordinate System Must Be Orthonormal**
> The formula $\vec{u} \cdot \vec{v} = xx' + yy'$ is **false** if the axes are not perpendicular or if the units on the two axes differ! It holds true only in an **orthonormal** coordinate system.

---

### 5. Polarization Identities: Computing with Lengths Alone

Can we find the dot product of two vectors without knowing their coordinates or the angle between them, using only the lengths of the segments that compose them?
Yes, thanks to **vector binomial identities**.

For any vectors $\vec{u}$ and $\vec{v}$:
$$\|\vec{u} + \vec{v}\|^2 = (\vec{u} + \vec{v})^2 = \vec{u}^2 + 2\vec{u}\cdot\vec{v} + \vec{v}^2 = \|\vec{u}\|^2 + 2\vec{u}\cdot\vec{v} + \|\vec{v}\|^2.$$

Isolating the dot product $\vec{u} \cdot \vec{v}$ yields the famous polarization formulas:

> **📐 Theorem — Polarization Identities**
> For all vectors $\vec{u}$ and $\vec{v}$:
>
> 1. $\vec{u} \cdot \vec{v} = \frac{1}{2}\left( \|\vec{u} + \vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2 \right)$
> 2. $\vec{u} \cdot \vec{v} = \frac{1}{2}\left( \|\vec{u}\|^2 + \|\vec{v}\|^2 - \|\vec{u} - \vec{v}\|^2 \right)$
> 3. $\vec{u} \cdot \vec{v} = \frac{1}{4}\left( \|\vec{u} + \vec{v}\|^2 - \|\vec{u} - \vec{v}\|^2 \right)$

In a triangle $ABC$ with $\vec{u} = \vec{AB}$ and $\vec{v} = \vec{AC}$, notice that $\vec{u} - \vec{v} = \vec{AB} - \vec{AC} = \vec{CB}$.
The second identity becomes:

$$\vec{AB} \cdot \vec{AC} = \frac{1}{2}\left( AB^2 + AC^2 - BC^2 \right).$$

This provides a direct bridge between the lengths of the three sides of a triangle and the dot product!

---

### 6. Orthogonality, Normal Vectors, and Equations of Lines

#### 6.1 The Orthogonality Criterion

> **📐 Fundamental Theorem of Orthogonality**
> Two vectors $\vec{u}$ and $\vec{v}$ are orthogonal if and only if:
>
> $$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0.$$
>
> In an orthonormal coordinate system with $\vec{u}(x;y)$ and $\vec{v}(x';y')$:
>
> $$\vec{u} \perp \vec{v} \iff xx' + yy' = 0.$$

#### 6.2 Normal Vector to a Line

In Grade 10, a line was characterized by a point and a *direction vector* $\vec{u}$ parallel to the line.
In Grade 11, the dot product allows a much more convenient approach: characterizing the line by an arrow that is **perpendicular** to it.

> **📐 Definition — Normal Vector**
> A non-zero vector $\vec{n}$ is said to be **normal** to a line $(d)$ if it is orthogonal to every direction vector of $(d)$.

```
                     ▲ n (normal vector)
                     │
                     │
           ──────────┼──────M─────────────────► Line (d)
                     A      AM ⟂ n
```

A point $M(x;y)$ belongs to the line $(d)$ passing through $A(x_A; y_A)$ with normal vector $\vec{n}(a; b)$ if and only if:

$$\vec{AM} \cdot \vec{n} = 0 \iff a(x - x_A) + b(y - y_A) = 0 \iff ax + by + (-ax_A - by_A) = 0.$$

Setting $c = -ax_A - by_A$, we retrieve the standard Cartesian equation!

> **📐 Theorem — Cartesian Equation and Normal Vector**
> - In an orthonormal coordinate system, every line with normal vector $\vec{n}\begin{pmatrix} a \\ b \end{pmatrix}$ has a Cartesian equation of the form:
>
> $$ax + by + c = 0 \quad (\text{with } (a; b) \neq (0; 0)).$$
>
> - Conversely, any equation of the form $ax + by + c = 0$ with $(a; b) \neq (0; 0)$ is the equation of a straight line having normal vector $\vec{n}\begin{pmatrix} a \\ b \end{pmatrix}$.

---

### 7. The Two Great Metric Theorems of the Triangle

#### 7.1 Al-Kashi's Theorem (Law of Cosines)

In an arbitrary triangle $ABC$, when the angle $\widehat{A}$ is not right, what becomes of the Pythagorean theorem?

> **📐 Al-Kashi's Theorem (Generalized Pythagorean Theorem / Law of Cosines)**
> Let $ABC$ be any triangle. Setting $a = BC$, $b = AC$, $c = AB$, and $\widehat{A} = \widehat{BAC}$:
>
> $$a^2 = b^2 + c^2 - 2bc \cos\widehat{A}.$$
>
> Likewise for the other two vertices:
> $$b^2 = a^2 + c^2 - 2ac \cos\widehat{B}, \qquad c^2 = a^2 + b^2 - 2ab \cos\widehat{C}.$$

```
                     A
                    / \
                c  /   \  b
                  /  Â  \
                 B───────C
                     a
```

> **✍️ Geometric Proof via the Dot Product**
> Write Chasles' relation for the vector $\vec{BC}$:
> $\vec{BC} = \vec{BA} + \vec{AC} = \vec{AC} - \vec{AB}$.
> Take the scalar square of both sides:
> $$BC^2 = \|\vec{BC}\|^2 = \|\vec{AC} - \vec{AB}\|^2 = \|\vec{AC}\|^2 - 2\vec{AC}\cdot\vec{AB} + \|\vec{AB}\|^2.$$
> Since $\|\vec{AC}\| = b$, $\|\vec{AB}\| = c$, and $\vec{AB}\cdot\vec{AC} = AB \times AC \cos\widehat{A} = bc\cos\widehat{A}$, substituting gives:
> $$a^2 = b^2 + c^2 - 2bc \cos\widehat{A}. \quad \blacksquare$$

Notice the beauty of the formula: if $\widehat{A} = 90^\circ$, then $\cos(90^\circ) = 0$, and the corrective term $-2bc\cos\widehat{A}$ vanishes: we recover exactly the Pythagorean theorem $a^2 = b^2 + c^2$! Al-Kashi contains Pythagoras as a special case.

> **🔍 The True History — Ghiyath al-Din Jamshid al-Kashi**
> A fifteenth-century Persian astronomer and mathematician, Al-Kashi worked at the Samarkand observatory under the patronage of Prince Ulugh Beg. In his masterpiece, *The Key to Arithmetic* (1427), he calculated $\pi$ to 16 correct decimal places (a world record that held for nearly two centuries) and compiled trigonometric tables of staggering precision. The formula that today bears his name in France enabled astronomers to solve any oblique triangle without dividing it into right-angled triangles.

#### 7.2 The Median Theorem (Apollonius's Theorem)

Consider a triangle $ABC$ and let $I$ be the **midpoint** of side $[BC]$. How can we relate the length of the median $AI$ to the lengths of the three sides?

> **📐 Median Theorem (Apollonius's Theorem)**
> In every triangle $ABC$, if $I$ is the midpoint of segment $[BC]$, then:
>
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2.$$

```
                     A
                    /│\
                   / │ \
                c /  │  \ b
                 /   │   \
                B────I────C
                   a/2 a/2
```

> **✍️ Proof**
> Express the vectors $\vec{AB}$ and $\vec{AC}$ passing through the midpoint $I$:
> $\vec{AB} = \vec{AI} + \vec{IB}$ and $\vec{AC} = \vec{AI} + \vec{IC}$.
> Take their scalar squares:
> $$AB^2 = \|\vec{AI} + \vec{IB}\|^2 = AI^2 + 2\vec{AI}\cdot\vec{IB} + IB^2,$$
> $$AC^2 = \|\vec{AI} + \vec{IC}\|^2 = AI^2 + 2\vec{AI}\cdot\vec{IC} + IC^2.$$
> Add the two equations side by side:
> $$AB^2 + AC^2 = 2AI^2 + 2\vec{AI}\cdot(\vec{IB} + \vec{IC}) + IB^2 + IC^2.$$
> Since $I$ is the midpoint of $[BC]$, we have $\vec{IB} + \vec{IC} = \vec{0}$! The cross-term cancels completely.
> Moreover, $IB = IC = \frac{BC}{2}$, so $IB^2 + IC^2 = \left(\frac{BC}{2}\right)^2 + \left(\frac{BC}{2}\right)^2 = 2\frac{BC^2}{4} = \frac{1}{2}BC^2$.
> We arrive directly at:
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2. \quad \blacksquare$$

---

### 8. Loci of Points and Equations of Circles

The dot product provides a method of unmatched elegance for finding the algebraic formula of a circle.

#### 8.1 Circle Defined by Center and Radius

A point $M(x;y)$ lies on the circle $\mathcal{C}$ with center $\Omega(x_\Omega; y_\Omega)$ and radius $R$ if and only if the distance $\Omega M$ equals $R$:

$$\Omega M^2 = R^2 \iff (x - x_\Omega)^2 + (y - y_\Omega)^2 = R^2.$$

#### 8.2 Circle Defined by Diameter $[AB]$

Recall from middle school: any triangle inscribed in a circle with a diameter as its hypotenuse is a **right-angled triangle**.
In other words: a point $M$ (distinct from $A$ and $B$) lies on the circle with diameter $[AB]$ if and only if the angle $\widehat{AMB}$ is a right angle, which vectorially translates to:

$$\vec{MA} \cdot \vec{MB} = 0.$$

(Note: if $M = A$ or $M = B$, one of the vectors is zero, so the dot product is still zero; the relation holds for all points on the circle.)

> **📐 Theorem — Equation of a Circle with Diameter $[AB]$**
> The circle with diameter $[AB]$, where $A(x_A; y_A)$ and $B(x_B; y_B)$, is the set of points $M(x;y)$ satisfying:
>
> $$\vec{MA} \cdot \vec{MB} = 0 \iff (x_A - x)(x_B - x) + (y_A - y)(y_B - y) = 0,$$
> or equivalently:
> $$\boxed{(x - x_A)(x - x_B) + (y - y_A)(y - y_B) = 0}$$

---

### Step-by-Step Worked Examples

> **✅ Worked Example 1 — Computing the Dot Product in Various Ways**
> Consider a square $ABCD$ of side length 4 and center $O$.
> Compute the following dot products:
> 1. $\vec{AB} \cdot \vec{AC}$
> 2. $\vec{AB} \cdot \vec{AD}$
> 3. $\vec{AB} \cdot \vec{CD}$
> 4. $\vec{OA} \cdot \vec{OB}$
>
> **Detailed Solution:**
> 1. By orthogonal projection: The orthogonal projection of $C$ onto the line $(AB)$ is point $B$. Therefore, $\vec{AB} \cdot \vec{AC} = \vec{AB} \cdot \vec{AB} = AB^2 = 4^2 = 16$.
> 2. By orthogonality: In a square, $(AB) \perp (AD)$, so the angle is a right angle: $\vec{AB} \cdot \vec{AD} = 0$.
> 3. Collinear vectors in opposite directions: $\vec{CD} = -\vec{AB}$. Hence $\vec{AB} \cdot \vec{CD} = -AB^2 = -16$.
> 4. In a square, the diagonals intersect perpendicularly at their midpoint $O$, so $(OA) \perp (OB)$. Thus, $\vec{OA} \cdot \vec{OB} = 0$.

> **✅ Worked Example 2 — Computing an Angle Using Coordinates**
> In an orthonormal coordinate system, three points are given: $A(1; 2)$, $B(4; 6)$, and $C(-2; 6)$.
> Compute the angle $\widehat{BAC}$ rounded to the nearest tenth of a degree.
>
> **Detailed Solution:**
> Determine the coordinates of vectors $\vec{AB}$ and $\vec{AC}$:
> - $\vec{AB}\begin{pmatrix} 4 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$;
> - $\vec{AC}\begin{pmatrix} -2 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$.
>
> 1. Analytical dot product:
>    $\vec{AB} \cdot \vec{AC} = xx' + yy' = 3 \times (-3) + 4 \times 4 = -9 + 16 = 7$.
> 2. Compute norms:
>    $\|\vec{AB}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
>    $\|\vec{AC}\| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
> 3. Extract the cosine:
>    $\vec{AB} \cdot \vec{AC} = \|\vec{AB}\| \times \|\vec{AC}\| \times \cos\widehat{BAC}$,
>    so $7 = 5 \times 5 \times \cos\widehat{BAC} = 25 \cos\widehat{BAC}$, giving $\cos\widehat{BAC} = \frac{7}{25} = 0.28$.
> 4. Using a calculator: $\widehat{BAC} = \arccos(0.28) \approx 73.7^\circ$.

> **✅ Worked Example 3 — Cartesian Equation Using a Normal Vector**
> Find a Cartesian equation of the line $(d)$ passing through the point $A(3; -1)$ and perpendicular to the line $(\Delta)$ with equation $2x - 5y + 7 = 0$.
>
> **Detailed Solution:**
> - The line $(\Delta)$ has normal vector $\vec{n_\Delta}\begin{pmatrix} 2 \\ -5 \end{pmatrix}$.
> - Since $(d)$ is perpendicular to $(\Delta)$, a normal vector to $(\Delta)$ serves as a **direction vector** for $(d)$.
>   Hence $\vec{u}_d = \begin{pmatrix} 2 \\ -5 \end{pmatrix}$.
> - A normal vector to $(d)$ must be orthogonal to $\vec{u}_d$. The vector $\vec{n}_d\begin{pmatrix} 5 \\ 2 \end{pmatrix}$ works since $2 \times 5 + (-5) \times 2 = 10 - 10 = 0$.
> - The equation of $(d)$ is therefore of the form $5x + 2y + c = 0$.
> - Since $A(3; -1) \in (d)$, its coordinates satisfy the equation:
>   $5(3) + 2(-1) + c = 0 \iff 15 - 2 + c = 0 \iff 13 + c = 0 \iff c = -13$.
> - The Cartesian equation of $(d)$ is therefore: $\boxed{5x + 2y - 13 = 0}$.

> **✅ Worked Example 4 — Length and Angle Calculation via Al-Kashi**
> A surveyor inspects a triangular parcel $ABC$. He measures $AB = 60\text{ m}$, $AC = 100\text{ m}$, and the angle $\widehat{BAC} = 60^\circ$.
> 1. Compute the distance $BC$.
> 2. Compute the angle $\widehat{ABC}$ to the nearest degree.
>
> **Detailed Solution:**
> 1. By Al-Kashi's theorem:
>    $BC^2 = AB^2 + AC^2 - 2 \times AB \times AC \times \cos\widehat{A}$.
>    $BC^2 = 60^2 + 100^2 - 2 \times 60 \times 100 \times \cos(60^\circ)$.
>    Since $\cos(60^\circ) = \frac{1}{2}$:
>    $BC^2 = 3600 + 10000 - 12000 \times 0.5 = 13600 - 6000 = 7600$.
>    Hence $BC = \sqrt{7600} \approx 87.18\text{ m}$.
>
> 2. For angle $\widehat{B}$, apply Al-Kashi isolating $\cos\widehat{B}$:
>    $AC^2 = AB^2 + BC^2 - 2 \times AB \times BC \times \cos\widehat{B}$,
>    $100^2 = 60^2 + 7600 - 2 \times 60 \times \sqrt{7600} \times \cos\widehat{B}$,
>    $10000 = 3600 + 7600 - 120\sqrt{7600} \cos\widehat{B} = 11200 - 120\sqrt{7600} \cos\widehat{B}$.
>    $120\sqrt{7600} \cos\widehat{B} = 11200 - 10000 = 1200$.
>    $\cos\widehat{B} = \frac{1200}{120\sqrt{7600}} = \frac{10}{\sqrt{7600}} \approx 0.1147$.
>    Whence $\widehat{B} = \arccos(0.1147) \approx 83^\circ$.

> **✅ Worked Example 5 — Equation of a Circle Defined by a Diameter**
> Given points $A(-1; 3)$ and $B(5; 1)$.
> 1. Determine a Cartesian equation of the circle $\mathcal{C}$ having diameter $[AB]$.
> 2. Find the coordinates of its center $\Omega$ and radius $R$, and verify the form $(x-x_\Omega)^2 + (y-y_\Omega)^2 = R^2$.
>
> **Detailed Solution:**
> 1. $M(x; y) \in \mathcal{C} \iff \vec{MA} \cdot \vec{MB} = 0$.
>    $\vec{MA}\begin{pmatrix} -1 - x \\ 3 - y \end{pmatrix}$ and $\vec{MB}\begin{pmatrix} 5 - x \\ 1 - y \end{pmatrix}$.
>    $\vec{MA} \cdot \vec{MB} = (-1 - x)(5 - x) + (3 - y)(1 - y) = 0$.
>    Expand:
>    $(-5 + x - 5x + x^2) + (3 - 3y - y + y^2) = 0 \iff x^2 - 4x + y^2 - 4y - 2 = 0$.
>
> 2. Center $\Omega$, midpoint of $[AB]$:
>    $x_\Omega = \frac{-1 + 5}{2} = 2$, and $y_\Omega = \frac{3 + 1}{2} = 2$, so $\Omega(2; 2)$.
>    Radius: $AB = \sqrt{(5 - (-1))^2 + (1 - 3)^2} = \sqrt{6^2 + (-2)^2} = \sqrt{36 + 4} = \sqrt{40} = 2\sqrt{10}$.
>    The radius is $R = \frac{AB}{2} = \sqrt{10}$, hence $R^2 = 10$.
>    The standard equation is $(x - 2)^2 + (y - 2)^2 = 10$.
>    Expanding: $x^2 - 4x + 4 + y^2 - 4y + 4 = 10 \iff x^2 - 4x + y^2 - 4y - 2 = 0$.
>    We obtain the exact same equation!

> **✅ Worked Example 6 — Using the Median Theorem**
> Let $ABC$ be a triangle such that $AB = 7$, $AC = 9$, and $BC = 8$.
> Compute the exact length of the median through $A$.
>
> **Detailed Solution:**
> Let $I$ be the midpoint of $[BC]$. The median through $A$ is the segment $[AI]$.
> By the median theorem:
> $$AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2.$$
> Substitute the known values:
> $$7^2 + 9^2 = 2AI^2 + \frac{1}{2}(8^2),$$
> $$49 + 81 = 2AI^2 + \frac{1}{2}(64),$$
> $$130 = 2AI^2 + 32.$$
> Isolate $AI^2$:
> $$2AI^2 = 130 - 32 = 98 \implies AI^2 = 49 \implies AI = \sqrt{49} = 7.$$
> The median measures exactly 7.

---

### Key Takeaways

1. **Four Equivalent Definitions of the Dot Product:**
   - Geometric: $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$.
   - By projection: $\vec{OA} \cdot \vec{OB} = \pm OA \times OH$ ($H$ is the orthogonal projection of $B$ onto line $(OA)$).
   - Analytical (orthonormal frame): $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix} \cdot \vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix} = xx' + yy'$.
   - Polarization: $\vec{u} \cdot \vec{v} = \frac{1}{2}\left(\|\vec{u}+\vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2\right)$.

2. **Orthogonality and Vector Geometry:**
   - $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0 \iff xx' + yy' = 0$.
   - A line with normal vector $\vec{n}(a; b)$ has Cartesian equation $ax + by + c = 0$.

3. **Fundamental Triangle Theorems:**
   - Al-Kashi (Law of Cosines): $a^2 = b^2 + c^2 - 2bc\cos\widehat{A}$.
   - Median: $AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2$ (where $I$ is the midpoint of $[BC]$).

4. **Circles:**
   - Center $\Omega(x_\Omega; y_\Omega)$ and radius $R$: $(x - x_\Omega)^2 + (y - y_\Omega)^2 = R^2$.
   - Diameter $[AB]$: $\vec{MA} \cdot \vec{MB} = 0 \iff (x - x_A)(x - x_B) + (y - y_A)(y - y_B) = 0$.

---

### Exercises

#### Level ★ (Direct Applications)

1. Let $\vec{u}$ and $\vec{v}$ be two vectors such that $\|\vec{u}\| = 5$, $\|\vec{v}\| = 6$, and the angle between them is $\frac{\pi}{3}$. Compute $\vec{u} \cdot \vec{v}$.
2. In an orthonormal frame, given $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} 2 \\ 5 \end{pmatrix}$. Compute $\vec{u} \cdot \vec{v}$.
3. Are the vectors $\vec{u}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} 9 \\ 6 \end{pmatrix}$ orthogonal?
4. Determine a normal vector $\vec{n}$ to the line with equation $3x - 7y + 11 = 0$.
5. Give a Cartesian equation of the line passing through $A(1; 4)$ with normal vector $\vec{n}\begin{pmatrix} 2 \\ -3 \end{pmatrix}$.
6. In a triangle $ABC$, given $AB = 5$, $AC = 8$, and $\widehat{A} = 60^\circ$. Compute the length $BC$.
7. Let $[AB]$ be a segment with $A(2; 1)$ and $B(6; 5)$. Write the equation of the circle with diameter $[AB]$.
8. Consider an equilateral triangle $ABC$ with side length $a = 6$. Compute the dot product $\vec{AB} \cdot \vec{AC}$.

#### Level ★★ (Reasoning and Geometry)

9. Consider a rectangle $ABCD$ such that $AB = 6$ and $BC = 3$. Let $I$ be the midpoint of $[AB]$. Compute $\vec{CA} \cdot \vec{DI}$.
10. Prove that in a rhombus, the diagonals intersect at right angles using the scalar product of $(\vec{u} + \vec{v})$ and $(\vec{u} - \vec{v})$.
11. In an orthonormal coordinate system, consider points $A(-2; 1)$, $B(2; 3)$, and $C(1; 5)$.
    a) Compute $\vec{BA} \cdot \vec{BC}$.
    b) Deduce the measure of angle $\widehat{ABC}$ to the nearest degree.
12. Find the real value $k$ such that the vectors $\vec{u}\begin{pmatrix} 2k - 1 \\ 3 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} 4 \\ k + 2 \end{pmatrix}$ are orthogonal.
13. Consider the triangle $MNP$ with $MN = 5$, $NP = 7$, and $MP = 8$. Compute the angle $\widehat{MNP}$ to the nearest tenth of a degree.
14. In a triangle $ABC$, given $AB = 6$, $AC = 10$, and median $AI = 6$. Compute the length of side $BC$.
15. Determine the set of points $M(x; y)$ whose coordinates satisfy:
    $$x^2 + y^2 - 6x + 8y = 0.$$
16. Find the distance from point $A(2; 3)$ to the line $(d)$ with equation $4x + 3y - 7 = 0$ using a normal vector.

#### Level ★★★ (Problems and Bac Challenges)

17. **Altitudes of a Triangle Concur:**
    Let $ABC$ be a triangle. Let $H$ be the intersection of the altitudes from $A$ and from $B$.
    a) Express the condition that $H$ lies on the first two altitudes using dot products.
    b) Deduce that $\vec{CH} \cdot \vec{AB} = 0$, and conclude that the three altitudes are concurrent.
18. **Geometric Locus and Level Set:**
    Let $A$ and $B$ be two distinct points with distance $AB = 6\text{ cm}$. Let $I$ be the midpoint of $[AB]$.
    Determine and describe the set of points $M$ in the plane satisfying:
    $$\vec{MA} \cdot \vec{MB} = 7.$$
19. **Rugby Kick Optimization:**
    A rugby player must attempt a conversion following a try scored near the corner flag. The goal posts are at $P_1(0; 2)$ and $P_2(0; -2)$. The kicker can move backward perpendicularly along the line $y = 5$. At what $x$-coordinate $x > 0$ should he place the ball so that the shooting angle $\widehat{P_1 M P_2}$ is maximized?
20. **Heron's Formula Proved by Al-Kashi:**
    Let $ABC$ be a triangle with side lengths $a, b, c$ and semi-perimeter $p = \frac{a+b+c}{2}$.
    Using the area formula $\mathcal{S} = \frac{1}{2}bc\sin\widehat{A}$ and Al-Kashi's formula for $\cos\widehat{A}$, prove the celebrated formula of Heron of Alexandria:
    $$\mathcal{S} = \sqrt{p(p-a)(p-b)(p-c)}.$$
21. **Power of a Point with Respect to a Circle:**
    Let $\mathcal{C}$ be a circle with center $\Omega$ and radius $R$, and let $M$ be any point in the plane. A line through $M$ intersects the circle at two points $A$ and $B$.
    Show that the dot product $\vec{MA} \cdot \vec{MB}$ is independent of the choice of secant line and always equals $M\Omega^2 - R^2$.

---

### Solutions

**1.** $\vec{u} \cdot \vec{v} = 5 \times 6 \times \cos\left(\frac{\pi}{3}\right) = 30 \times 0.5 = 15$.

**2.** $\vec{u} \cdot \vec{v} = (-3) \times 2 + 4 \times 5 = -6 + 20 = 14$.

**3.** $xx' + yy' = 4 \times 9 + (-6) \times 6 = 36 - 36 = 0$. Yes, the vectors are orthogonal.

**4.** The vector $\vec{n}\begin{pmatrix} 3 \\ -7 \end{pmatrix}$ is normal to the line.

**5.** $2(x - 1) - 3(y - 4) = 0 \iff 2x - 3y - 2 + 12 = 0 \iff 2x - 3y + 10 = 0$.

**6.** Al-Kashi: $BC^2 = 5^2 + 8^2 - 2 \times 5 \times 8 \times \cos(60^\circ) = 25 + 64 - 80 \times 0.5 = 89 - 40 = 49$. Hence $BC = 7$.

**7.** $(x - 2)(x - 6) + (y - 1)(y - 5) = 0 \iff x^2 - 8x + 12 + y^2 - 6y + 5 = 0 \iff x^2 + y^2 - 8x - 6y + 17 = 0$.

**8.** $\vec{AB} \cdot \vec{AC} = 6 \times 6 \times \cos(60^\circ) = 36 \times 0.5 = 18$.

**9.** Place an orthonormal coordinate system with origin $D$, $(DA)$ along the $x$-axis, and $(DC)$ along the $y$-axis. $D(0; 0)$, $A(3; 0)$, $B(3; 6)$, $C(0; 6)$. The midpoint $I$ of $[AB]$ has coordinates $(3; 3)$.
Thus, $\vec{CA}\begin{pmatrix} 3 - 0 \\ 0 - 6 \end{pmatrix} = \begin{pmatrix} 3 \\ -6 \end{pmatrix}$, and $\vec{DI}\begin{pmatrix} 3 \\ 3 \end{pmatrix}$.
The scalar product is: $\vec{CA} \cdot \vec{DI} = 3 \times 3 + (-6) \times 3 = 9 - 18 = -9$.

**10.** Let $\vec{u}$ and $\vec{v}$ be the two vectors along the adjacent sides of a rhombus. Since all sides of a rhombus are equal in length, $\|\vec{u}\| = \|\vec{v}\|$, hence $\|\vec{u}\|^2 - \|\vec{v}\|^2 = 0$.
The diagonals are represented by the vectors $\vec{u} + \vec{v}$ and $\vec{u} - \vec{v}$.
Compute their dot product using the vector identity:
$(\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v}) = \|\vec{u}\|^2 - \|\vec{v}\|^2 = 0$.
Since their dot product is zero, the diagonals of a rhombus are perpendicular.

**11.**
a) $\vec{BA}\begin{pmatrix} -2 - 2 \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} -4 \\ -2 \end{pmatrix}$, and $\vec{BC}\begin{pmatrix} 1 - 2 \\ 5 - 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$.
$\vec{BA} \cdot \vec{BC} = (-4) \times (-1) + (-2) \times 2 = 4 - 4 = 0$.
b) Because the dot product is zero, the vectors are orthogonal: $\widehat{ABC} = 90^\circ$ exactly!

**12.** $\vec{u} \perp \vec{v} \iff (2k - 1) \times 4 + 3 \times (k + 2) = 0 \iff 8k - 4 + 3k + 6 = 0 \iff 11k + 2 = 0 \iff k = -\frac{2}{11}$.

**13.** By Al-Kashi in $MNP$: $MP^2 = MN^2 + NP^2 - 2 \times MN \times NP \times \cos\widehat{N}$.
$8^2 = 5^2 + 7^2 - 2 \times 5 \times 7 \times \cos\widehat{N} \iff 64 = 25 + 49 - 70\cos\widehat{N} \iff 64 = 74 - 70\cos\widehat{N}$.
$70\cos\widehat{N} = 10 \iff \cos\widehat{N} = \frac{10}{70} = \frac{1}{7} \approx 0.1428$.
Thus $\widehat{MNP} = \arccos\left(\frac{1}{7}\right) \approx 81.8^\circ$.

**14.** Median theorem: $AB^2 + AC^2 = 2AI^2 + \frac{1}{2}BC^2$.
$6^2 + 10^2 = 2(6^2) + \frac{1}{2}BC^2 \iff 36 + 100 = 72 + \frac{1}{2}BC^2 \iff 136 = 72 + \frac{1}{2}BC^2$.
$\frac{1}{2}BC^2 = 64 \iff BC^2 = 128 \implies BC = \sqrt{128} = 8\sqrt{2} \approx 11.31$.

**15.** Complete the square: $(x^2 - 6x) + (y^2 + 8y) = 0 \iff (x - 3)^2 - 9 + (y + 4)^2 - 16 = 0 \iff (x - 3)^2 + (y + 4)^2 = 25$.
This is the circle with center $\Omega(3; -4)$ and radius $R = \sqrt{25} = 5$.

**16.** Let $H$ be the orthogonal projection of $A$ onto $(d)$. The distance from $A$ to $(d)$ is the length $AH$.
The vector $\vec{n}\begin{pmatrix} 4 \\ 3 \end{pmatrix}$ is normal to $(d)$, with norm $\|\vec{n}\| = \sqrt{4^2 + 3^2} = 5$.
Pick any point on $(d)$, for instance $B(1; 1)$ since $4(1) + 3(1) - 7 = 0$.
The vector $\vec{BA} = \begin{pmatrix} 2 - 1 \\ 3 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
The absolute value of the scalar product gives $|\vec{BA} \cdot \vec{n}| = \|\vec{n}\| \times AH$.
Since $\vec{BA} \cdot \vec{n} = 1 \times 4 + 2 \times 3 = 10$:
$10 = 5 \times AH \implies AH = \frac{10}{5} = 2$.
The distance is exactly 2.

**17.**
a) $H$ lies on the altitude from $A$, so $\vec{AH} \perp \vec{BC} \iff \vec{AH} \cdot \vec{BC} = 0$.
$H$ lies on the altitude from $B$, so $\vec{BH} \perp \vec{AC} \iff \vec{BH} \cdot \vec{AC} = 0$.
b) Compute $\vec{CH} \cdot \vec{AB}$:
$\vec{CH} \cdot \vec{AB} = \vec{CH} \cdot (\vec{CB} - \vec{CA}) = \vec{CH} \cdot \vec{CB} - \vec{CH} \cdot \vec{CA}$.
Notice that $\vec{CH} = \vec{CA} + \vec{AH} = \vec{CB} + \vec{BH}$.
Substituting cleverly:
$\vec{CH} \cdot \vec{CB} = (\vec{CA} + \vec{AH}) \cdot \vec{CB} = \vec{CA} \cdot \vec{CB} + \vec{AH} \cdot \vec{CB} = \vec{CA} \cdot \vec{CB} + 0$.
Similarly, $\vec{CH} \cdot \vec{CA} = (\vec{CB} + \vec{BH}) \cdot \vec{CA} = \vec{CB} \cdot \vec{CA} + \vec{BH} \cdot \vec{CA} = \vec{CB} \cdot \vec{CA} + 0$.
Thus, $\vec{CH} \cdot \vec{AB} = \vec{CA} \cdot \vec{CB} - \vec{CB} \cdot \vec{CA} = 0$.
The vector $\vec{CH}$ is therefore orthogonal to $\vec{AB}$: line $(CH)$ is the third altitude of the triangle. The three altitudes meet at the same point $H$: they are concurrent.

**18.** Express $\vec{MA}$ and $\vec{MB}$ through the midpoint $I$ of $[AB]$:
$\vec{MA} \cdot \vec{MB} = (\vec{MI} + \vec{IA}) \cdot (\vec{MI} + \vec{IB})$.
Since $\vec{IB} = -\vec{IA}$, we have the identity:
$\vec{MA} \cdot \vec{MB} = MI^2 - IA^2$.
Given $AB = 6$, $IA = 3$, so $IA^2 = 9$.
The equation becomes: $MI^2 - 9 = 7 \iff MI^2 = 16 \iff MI = 4$.
The desired locus is the **circle with center $I$ (midpoint of $[AB]$) and radius $R = 4\text{ cm}$**.

**19.** A point on the shooting line is $M(x; 5)$ with $x > 0$.
$\vec{MP_1}\begin{pmatrix} -x \\ 2 - 5 \end{pmatrix} = \begin{pmatrix} -x \\ -3 \end{pmatrix}$ and $\vec{MP_2}\begin{pmatrix} -x \\ -2 - 5 \end{pmatrix} = \begin{pmatrix} -x \\ -7 \end{pmatrix}$.
The scalar product is: $\vec{MP_1} \cdot \vec{MP_2} = (-x)(-x) + (-3)(-7) = x^2 + 21$.
The norms are: $\|\vec{MP_1}\| = \sqrt{x^2 + 9}$ and $\|\vec{MP_2}\| = \sqrt{x^2 + 49}$.
The cosine of angle $\theta = \widehat{P_1 M P_2}$ satisfies $\cos\theta = \frac{x^2 + 21}{\sqrt{(x^2+9)(x^2+49)}}$.
The angle $\theta$ is acute and reaches its maximum when $\cos\theta$ is minimized.
Squaring the expression: $\cos^2\theta = \frac{(x^2+21)^2}{x^4 + 58x^2 + 441} = \frac{x^4 + 42x^2 + 441}{x^4 + 58x^2 + 441} = 1 - \frac{16x^2}{x^4 + 58x^2 + 441} = 1 - \frac{16}{x^2 + 58 + \frac{441}{x^2}}$.
This cosine is minimal when the denominator $x^2 + \frac{441}{x^2}$ is minimized.
By the AM-GM inequality, the sum of two positive numbers with constant product $x^2 \times \frac{441}{x^2} = 441$ is minimized when they are equal:
$x^2 = \frac{441}{x^2} \iff x^4 = 441 \iff x^2 = 21 \iff x = \sqrt{21} \approx 4.58\text{ m}$.
The kicker should place the ball approximately 4.58 meters from the try line.

**20.**
The area of a triangle is given by $\mathcal{S} = \frac{1}{2}bc\sin\widehat{A}$.
Thus $4\mathcal{S} = 2bc\sin\widehat{A}$, so $16\mathcal{S}^2 = 4b^2 c^2 \sin^2\widehat{A} = 4b^2 c^2 (1 - \cos^2\widehat{A}) = (2bc - 2bc\cos\widehat{A})(2bc + 2bc\cos\widehat{A})$.
By Al-Kashi's theorem, $2bc\cos\widehat{A} = b^2 + c^2 - a^2$.
Substituting:
$2bc - (b^2 + c^2 - a^2) = a^2 - (b - c)^2 = (a - b + c)(a + b - c)$.
$2bc + (b^2 + c^2 - a^2) = (b + c)^2 - a^2 = (b + c - a)(b + c + a)$.
Since $p = \frac{a+b+c}{2}$, we have $a+b+c = 2p$, $b+c-a = 2(p-a)$, $a+c-b = 2(p-b)$, and $a+b-c = 2(p-c)$.
The product becomes:
$16\mathcal{S}^2 = 2(p-b) \times 2(p-c) \times 2(p-a) \times 2p = 16 p(p-a)(p-b)(p-c)$.
Dividing by 16 and taking the square root gives:
$\mathcal{S} = \sqrt{p(p-a)(p-b)(p-c)}$.

**21.** Let $A'$ be the point diametrically opposite to $A$ on the circle. Then triangle $AA'B$ is inscribed in a semicircle, so angle $\widehat{A'BA}$ is a right angle: $(BA') \perp (BA)$.
The orthogonal projection of $A'$ onto line $(AB)$ is therefore point $B$.
By projection: $\vec{MA} \cdot \vec{MB} = \vec{MA} \cdot \vec{MA'}$.
Now $\vec{MA} = \vec{M\Omega} + \vec{\Omega A}$ and $\vec{MA'} = \vec{M\Omega} + \vec{\Omega A'}$.
Since $A$ and $A'$ are diametrically opposite, $\vec{\Omega A'} = -\vec{\Omega A}$.
Hence:
$\vec{MA} \cdot \vec{MB} = (\vec{M\Omega} + \vec{\Omega A}) \cdot (\vec{M\Omega} - \vec{\Omega A}) = \|\vec{M\Omega}\|^2 - \|\vec{\Omega A}\|^2 = M\Omega^2 - R^2$.
This quantity depends solely on the position of $M$ and the circle's parameters, and is completely independent of the secant line chosen. It is the **power of point $M$ with respect to circle $\mathcal{C}$**.

---

### The Question Opening the Next Stage

The scalar product has enabled us to measure the inclination of a force relative to a straight path, and to calculate the slope of a rigid segment.
What happens, however, when the slope is no longer a straight line, but an **undulating curve** like a snow-covered hill down which a skier hurtles at full speed? How can we measure the tilt of the ski beneath the skier's boots at an infinitesimal instant, at a single point of contact? This is the great adventure of **differentiation**, which opens in the next chapter.
