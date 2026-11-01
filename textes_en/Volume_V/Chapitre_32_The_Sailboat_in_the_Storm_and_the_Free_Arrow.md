# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 32: The Sailboat in the Storm and the Free Arrow

> *“A point is an anchor holding a ship to the seabed. A Cartesian coordinate states where you are. But the sailor confronting the swell has little use for an anchor: he needs to know where the wind is driving him, at what speed, and how two competing currents merge into a single momentum. To liberate motion from the earth, humanity had to invent the flying arrow: the Vector.”*

---

### What You Are About to Discover

- Why the Cartesian coordinate plane was no longer enough for physicists, and how **Hermann Grassmann** freed displacement from its fixed tether in 1844.
- The fundamental triad defining a **vector**: direction, sense (orientation), and magnitude (norm)—along with the arrow notation $\vec{u}$ or $\vec{AB}$.
- **Chasles' relation** ($\vec{AB} + \vec{BC} = \vec{AC}$) understood as a relay of navigators or dispatch couriers, and the parallelogram rule.
- Multiplying a vector by a real number (scalar) and the concept of **collinear vectors**.
- How to translate geometry into algebraic calculations within a coordinate frame $(O\,; \vec{i}, \vec{j})$: vector coordinates, midpoint formula, and distance formula.
- The decisive arbiter of alignment and parallelism: the **determinant** $xy' - yx' = 0$.

---

### 1. The Problem: The Rowboat in the River Current

You stand at the oars of a fishing boat on the waters of a river five hundred meters wide. On the opposite bank, straight ahead of you to the North, stands the dock where your companions await you.

You grip both oars. You haul against the timber with all your muscle: your bow points straight **North**, and your effort propels you through the water at a steady speed of **$3\text{ km/h}$**. You mentally calculate that in ten minutes, you will tie up at the pontoon.

Yet the river is no tranquil pond. A strong current rushes from West to **East** at a speed of **$4\text{ km/h}$**.

Look at the scene from the riverbank:

```
                                  C (Actual landing point)
                                 ▲
                               / │
                 Actual       /   │
               trajectory    /     │  Oar propulsion (North: 3 km/h)
                            /       │
                          /         │
                         o──────────┴► B
                         A    River current (East: 4 km/h)
```

What forces act upon your vessel?
1. Your arms drive you North: in one hour, without current, you would travel $3\text{ km}$ North.
2. The water beneath your hull sweeps you East: in one hour, without rowing, you would drift $4\text{ km}$ East.

Both actions take place **simultaneously**. At the end of an imaginary hour in which both movements combine, you would be neither purely North nor purely East, but at point $C$. What distance have you covered relative to the riverbed?

The triangle formed by the eastward displacement ($4\text{ km}$), the northward displacement ($3\text{ km}$), and the actual trajectory is a right-angled triangle. The Pythagorean theorem gives the distance traveled:
$$d = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ km}.$$

Your actual speed relative to the banks is **$5\text{ km/h}$**, directed diagonally toward the Northeast!

This scenario reveals a fundamental limitation of ordinary numbers:
- A single number ($5\text{ km/h}$) states **how much**, but it does not state **where to**.
- The coordinate of a point $A(x_A, y_A)$ states **where one is**, but it is nailed to the grid drawn on the map. If the boat rows in the exact same manner a hundred kilometers downstream, the physical phenomenon is identical, even though the starting and ending coordinates are entirely different.

A new mathematical object was needed: an **autonomous arrow**, transportable anywhere without distortion, encoding tilt, orientation, and magnitude all at once.

---

### 2. Liberating the Arrow: The Birth of the Vector

#### 2.1 Grassmann's Breakthrough (1844)

For two centuries following René Descartes (1637), analytic geometry operated by chaining every point to a fixed origin $O(0, 0)$. To study the flight of a bird or the blast of a squall, one had to manipulate the coordinates of the starting point $A$, then those of the destination $B$, and compute differences.

In 1844, a high school teacher in Germany unknown to his contemporaries, **Hermann Günther Grassmann**, published a visionary treatise: *Die Lineale Ausdehnungslehre* (The Theory of Linear Extension). Grassmann introduced a revolutionary insight:
> “The point is a prison. What matters in physics is not the place where the action begins, but the action itself: pure transport.”

This geometric entity was given the name **vector**, from the Latin *vehere* (“to carry”, “to convey”—the root of *vehicle*).

#### 2.2 The Three Defining Characteristics of a Vector

> **📐 Definition — Vector.**
> A non-zero vector $\vec{u}$ is defined by three inseparable pieces of data:
> 1. **Its direction:** the line along which it lies (or any line parallel to it). This indicates the line of action of the movement (e.g., the North-South line, the horizontal axis, a $30^\circ$ incline).
> 2. **Its sense (or orientation):** the heading along that line, indicated by the arrowhead (e.g., Northward rather than Southward, left to right).
> 3. **Its magnitude (or norm):** the length of the directed line segment, denoted $\|\vec{u}\|$. It represents physical intensity (a speed in $\text{km/h}$, a force in newtons, a displacement in meters).

```
          Sense / Orientation (arrowhead points upward)
             ▲
            /
           /   Norm ||u|| (length of the arrow)
          /
         /
        o  Direction (the dotted reference line supporting the arrow)
       . 
      .
```

**Notation Explained.**
- We place a rightward arrow above the letter: $\vec{u}$, $\vec{v}$, $\vec{w}$. We read this aloud as: “vector u”, “vector v”.
- When the vector represents displacement explicitly from a point $A$ to a point $B$, we write $\vec{AB}$, read “vector AB”. Here, $A$ is the **initial point** (or origin/tail) of the representative, and $B$ is its **terminal point** (or tip/head).
- The **norm** is written with double vertical bars: $\|\vec{u}\|$ or $\|\vec{AB}\|$. We read “norm of u” or “magnitude of AB”. We always have $\|\vec{AB}\| = AB$ (the standard geometric length). Double bars are used to avoid confusion with the absolute value $|x|$ of a real number.

> **⚠️ Pitfall Warning! Never confuse direction and sense!**
> In everyday English, people often say “walk in the direction of Paris.” In mathematics, this is imprecise:
> - The **direction** is the railway line connecting Paris to Lyon.
> - The **sense** (or heading) is traveling from Paris toward Lyon, or from Lyon toward Paris.
> Two cars driving past each other head-on along the same straight highway share the **same direction**, but have **opposite senses**.

#### 2.3 The Zero Vector and Representatives

What happens if a traveler does not move a single millimeter?
His starting point $A$ and destination $A$ coincide. The corresponding displacement is the **zero vector**, denoted $\vec{0}$ (a zero topped by an arrow):
$$\vec{AA} = \vec{BB} = \vec{0}.$$
The zero vector has a magnitude equal to zero: $\|\vec{0}\| = 0$. It possesses neither a distinct direction nor a specific sense (it is said to have every possible direction).

> **💡 Did You Know? A vector is an infinity of arrows at once!**
> A vector $\vec{u}$ is not “glued” to one specific spot on paper. It is an equivalence class of displacements.
> If ten birds fly in tight formation, all heading South at $40\text{ km/h}$, each bird traces its own arrow across the sky. All these arrows have the same direction, the same sense, and the same length. They are called **representatives** (or bound arrows) of one and the same free vector $\vec{u}$.

```
    Bird 1              Bird 2              Bird 3
      A                   C                   E
      o                   o                   o
       \                   \                   \
        \   u = AB          \   u = CD          \   u = EF
         \                   \                   \
          ▼                   ▼                   ▼
          B                   D                   F
          
              AB = CD = EF = same free vector u!
```

#### 2.4 Vector Equality and Parallelograms

When can two arrows $\vec{AB}$ and $\vec{CD}$ be declared identical as vectors?

> **📐 Fundamental Theorem — Vector Equality.**
> Let $A, B, C, D$ be four points in the plane.
> $$\vec{AB} = \vec{CD} \iff \text{quadrilateral } ABDC \text{ is a parallelogram (possibly degenerate/flat)}.$$

> **⚠️ Pitfall Warning! The vertex order matters.**
> Pay close attention to the order of letters: $\vec{AB} = \vec{CD}$ means that $AB\mathbf{DC}$ is a parallelogram, **not** $ABCD$!
> To travel from $A$ to $B$, one performs the exact same translation as traveling from $C$ to $D$. The segments $[AD]$ and $[BC]$ therefore share the same midpoint: their diagonals bisect each other.

```
       A o────────────────────► B
         │                    │
         │                    │
         │                    │
       C o────────────────────► D
       
      Vector AB goes from A to B.
      Vector CD goes from C to D.
      The quadrilateral traced along its perimeter is A-B-D-C!
```

---

### 3. Operations on Vectors

#### 3.1 Chasles' Relation: The Courier Relay

How do we add two successive displacements?
Picture a royal missive carried by horse couriers:
- The first rider departs station $A$ and gallops to station $B$: displacement $\vec{AB}$.
- At station $B$, he hands the leather satchel to a second rider who immediately rides toward fortress $C$: displacement $\vec{BC}$.

What is the net outcome for the royal message? It departed from $A$ and has arrived at $C$.

> **📐 Theorem (Chasles' Relation, 1837) —**
> For any points $A, B, C$ in the plane:
> $$\vec{AB} + \vec{BC} = \vec{AC}.$$

<div align="center">
<svg width="440" height="210" viewBox="0 0 440 210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8" />
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#b91c1c" />
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#15803d" />
    </marker>
  </defs>
  <rect width="440" height="210" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
  
  <!-- Relais A vers B -->
  <line x1="50" y1="160" x2="210" y2="130" stroke="#1d4ed8" stroke-width="3" marker-end="url(#arr-blue)"/>
  <text x="125" y="165" fill="#1d4ed8" font-family="sans-serif" font-weight="bold" font-size="13">u = AB (1st leg)</text>
  <circle cx="50" cy="160" r="4" fill="#0f172a"/>
  <text x="35" y="175" font-family="sans-serif" font-weight="bold" font-size="12">A</text>

  <!-- Relais B vers C -->
  <line x1="210" y1="130" x2="370" y2="40" stroke="#b91c1c" stroke-width="3" marker-end="url(#arr-red)"/>
  <text x="310" y="105" fill="#b91c1c" font-family="sans-serif" font-weight="bold" font-size="13">v = BC (2nd leg)</text>
  <circle cx="210" cy="130" r="4" fill="#0f172a"/>
  <text x="210" y="150" font-family="sans-serif" font-weight="bold" font-size="12">B</text>

  <!-- Bilan direct A vers C -->
  <line x1="50" y1="160" x2="365" y2="43" stroke="#15803d" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arr-green)"/>
  <text x="160" y="75" fill="#15803d" font-family="sans-serif" font-weight="bold" font-size="14">AC = u + v (Chasles resultant)</text>
  <circle cx="370" cy="40" r="4" fill="#0f172a"/>
  <text x="380" y="45" font-family="sans-serif" font-weight="bold" font-size="12">C</text>
  
  <text x="220" y="198" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Chasles' relation: intermediate waypoint B vanishes, leaving only the direct path A → C</text>
</svg>
</div>

```
                        C
                       ▲
                      /
            v = BC   /
                    /
        u = AB     /     w = u + v = AC (Net resultant)
                  /
   A o──────────► B
```

**Historical Origin.**
This identity honors the French geometer **Michel Chasles** (1793–1880), professor at the Sorbonne and the École Polytechnique, who unified projective geometry and algebraic directed segment metrics.

> **💡 Did You Know? The pitfall of adding lengths.**
> $\vec{AB} + \vec{BC} = \vec{AC}$ is an equality of **vectors**. It **never** implies $AB + BC = AC$ for standard lengths, unless the three points lie aligned in the precise order $A, B, C$!
> In any non-degenerate triangle, the triangle inequality (Chapter 9) dictates:
> $$AC < AB + BC.$$
> The direct straight path is strictly shorter than detouring through $B$. The norm of the sum is always less than or equal to the sum of the norms: $\|\vec{u} + \vec{v}\| \le \|\vec{u}\| + \|\vec{v}\|$.

#### 3.2 The Opposite Vector and Subtraction

If we traverse the path in reverse, from $B$ back to $A$, the resulting vector has the same direction, the same magnitude, but the **opposite sense**. This is the **opposite vector**, denoted $-\vec{AB}$:
$$-\vec{AB} = \vec{BA}.$$

Applying Chasles' relation confirms:
$$\vec{AB} + \vec{BA} = \vec{AA} = \vec{0}.$$

To subtract a vector $\vec{v}$, we simply add its opposite:
$$\vec{u} - \vec{v} = \vec{u} + (-\vec{v}).$$

#### 3.3 The Parallelogram Rule (Concurrent Forces)

What should we do if two vectors emanate from the same initial point $A$, like two tugboats pulling on the same container ship?
Let $\vec{u} = \vec{AB}$ and $\vec{v} = \vec{AC}$.
To apply Chasles' relation, we simply place at point $B$ a representative of $\vec{v}$: we construct point $D$ such that $\vec{BD} = \vec{AC}$.
Then:
$$\vec{AB} + \vec{AC} = \vec{AB} + \vec{BD} = \vec{AD}.$$
The quadrilateral $ABDC$ forms a parallelogram, and the sum vector $\vec{AD}$ is its main diagonal.

```
       C o....................► D
        ▲                    ▲
         \                  /
      v   \                / v
           \              /
            o────────────► B
            A      u
```

#### 3.4 Multiplying a Vector by a Scalar

In physics and geometry, a real number is often called a **scalar** (from the Latin *scala*, ladder or scale), because it scales the magnitude of a quantity without changing its fundamental nature.

> **📐 Definition — Scalar Multiplication.**
> Let $\vec{u}$ be a vector and $k \in \mathbb{R}$ a real number. The vector $k\vec{u}$ is defined by:
> 1. If $k = 0$ or $\vec{u} = \vec{0}$, then $k\vec{u} = \vec{0}$.
> 2. If $k \neq 0$ and $\vec{u} \neq \vec{0}$:
>    - $k\vec{u}$ has the **same direction** as $\vec{u}$;
>    - $k\vec{u}$ has the **same sense** as $\vec{u}$ if $k > 0$, and the **opposite sense** if $k < 0$;
>    - its norm is $\|k\vec{u}\| = |k| \times \|\vec{u}\|$.

```
       -2u                -u         0        u          2u         3u
   ◄────────────    ◄──────      o      ──────►    ──────────►  ──────────────►
```

> **📐 Algebraic Properties —** For all vectors $\vec{u}, \vec{v}$ and all scalars $k, k'$:
> - $(k + k')\vec{u} = k\vec{u} + k'\vec{u}$ (distributivity with respect to scalar addition);
> - $k(\vec{u} + \vec{v}) = k\vec{u} + k\vec{v}$ (distributivity with respect to vector addition);
> - $k(k'\vec{u}) = (kk')\vec{u}$;
> - $1\vec{u} = \vec{u}$ and $(-1)\vec{u} = -\vec{u}$.

#### 3.5 Vector Characterization of the Midpoint

Let $[AB]$ be a line segment. The midpoint $I$ of $[AB]$ can be characterized in three equivalent vector ways:
1. $\vec{AI} = \vec{IB}$ (same direction, same sense, same half-length);
2. $\vec{IA} + \vec{IB} = \vec{0}$ ($I$ is the balance point between $A$ and $B$);
3. For any arbitrary point $M$ in the plane: $\vec{MA} + \vec{MB} = 2\vec{MI}$.

> **✍️ Proof — Midpoint Identity.**
> By Chasles' relation: $\vec{MA} = \vec{MI} + \vec{IA}$ and $\vec{MB} = \vec{MI} + \vec{IB}$.
> Summing term by term:
> $$\vec{MA} + \vec{MB} = (\vec{MI} + \vec{IA}) + (\vec{MI} + \vec{IB}) = 2\vec{MI} + (\vec{IA} + \vec{IB}).$$
> Since $I$ is the midpoint of $[AB]$, we know $\vec{IA} + \vec{IB} = \vec{0}$. Therefore:
> $$\vec{MA} + \vec{MB} = 2\vec{MI}. \quad \blacksquare$$

---

### 4. Vectors in a Cartesian Coordinate Frame

#### 4.1 The Basis $(\vec{i}, \vec{j})$ and Vector Coordinates

Equip the plane with an origin $O$ and two non-collinear vectors $\vec{i}$ and $\vec{j}$. The triad $(O\,; \vec{i}, \vec{j})$ constitutes a **coordinate frame** for the plane. If the directions of $\vec{i}$ and $\vec{j}$ are perpendicular and $\|\vec{i}\| = \|\vec{j}\| = 1$, the frame is called **orthonormal** (or Cartesian rectangular).

> **📐 Theorem and Definition — Coordinates of a Vector.**
> For every vector $\vec{u}$ in the plane, there exists a **unique** pair of real numbers $(x\,; y)$ such that:
> $$\vec{u} = x\vec{i} + y\vec{j}.$$
> We write $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ or $\vec{u}(x\,; y)$.
> $x$ is the **abscissa** ($x$-component) and $y$ is the **ordinate** ($y$-component).

```
                         y ▲
                           │             u = x i + y j
                       y ──┼ - - - - - - o 
                           │             ▲
                           │           / │
                           │       u /   │ y j
                           │       /     │
                           │     /       │
                       O ──┼────o────────┼────────► x
                           │   i        x
```

#### 4.2 Fundamental Coordinate Formulas

Let $A(x_A\,; y_A)$ and $B(x_B\,; y_B)$ be two points, and let $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ and $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ be two vectors.

> **📐 Key Formulas to Master —**
> 1. **Vector connecting two points (“Arrival minus Departure”):**
>    $$\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix}$$
> 2. **Vector addition:**
>    $$\vec{u} + \vec{v}\begin{pmatrix} x + x' \\ y + y' \end{pmatrix}$$
> 3. **Scalar multiplication:**
>    $$k\vec{u}\begin{pmatrix} kx \\ ky \end{pmatrix}$$
> 4. **Coordinates of the midpoint $I$ of $[AB]$:**
>    $$x_I = \frac{x_A + x_B}{2}, \quad y_I = \frac{y_A + y_B}{2}$$
> 5. **Norm of a vector (strictly in an orthonormal frame!):**
>    $$\|\vec{u}\| = \sqrt{x^2 + y^2}$$
>    and distance between two points:
>    $$AB = \|\vec{AB}\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}.$$

> **✍️ Proof — Coordinates of $\vec{AB}$.**
> By definition of point coordinates, $\vec{OA} = x_A\vec{i} + y_A\vec{j}$ and $\vec{OB} = x_B\vec{i} + y_B\vec{j}$.
> Using Chasles' relation:
> $$\vec{AB} = \vec{AO} + \vec{OB} = -\vec{OA} + \vec{OB} = \vec{OB} - \vec{OA}.$$
> Substituting:
> $$\vec{AB} = (x_B\vec{i} + y_B\vec{j}) - (x_A\vec{i} + y_A\vec{j}) = (x_B - x_A)\vec{i} + (y_B - y_A)\vec{j}.$$
> The coordinates of $\vec{AB}$ are therefore indeed $(x_B - x_A \,;\, y_B - y_A)$. $\blacksquare$

---

### 5. Collinearity and Determinants: The Art of Aiming True

#### 5.1 Definition of Collinearity

Two arrows may have different lengths and opposite orientations: if they lie on parallel lines, they have the **same direction**. In mathematics, they are termed **collinear** (from the Latin *cum*, together, and *linea*, line: “on the same line”).

> **📐 Definition — Collinear Vectors.**
> Two vectors $\vec{u}$ and $\vec{v}$ are said to be **collinear** if one is the scalar multiple of the other:
> $$\text{there exists } k \in \mathbb{R} \text{ such that } \vec{u} = k\vec{v} \quad \text{or} \quad \vec{v} = k\vec{u}.$$
> By convention, the zero vector $\vec{0}$ is collinear to **all** vectors in the plane (since $\vec{0} = 0 \times \vec{u}$).

#### 5.2 The Determinant of Two Vectors

How can one instantly test whether two vectors $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ and $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ are collinear, without guessing $k$?

> **📐 Definition and Theorem — Determinant in the Plane.**
> The **determinant** of vectors $\vec{u}$ and $\vec{v}$ in an orthonormal basis is the real number denoted $\det(\vec{u}, \vec{v})$, calculated by the cross-product rule:
> $$\det(\vec{u}, \vec{v}) = \begin{vmatrix} x & x' \\ y & y' \end{vmatrix} = x y' - y x'.$$
> **Fundamental Collinearity Criterion:**
> $$\vec{u} \text{ and } \vec{v} \text{ are collinear} \iff \det(\vec{u}, \vec{v}) = 0 \iff x y' - y x' = 0.$$

> **✍️ Proof — Collinearity Condition.**
> - **Forward direction ($\implies$):** Assume $\vec{u}$ and $\vec{v}$ are collinear. If $\vec{v} = \vec{0}$, then $x' = y' = 0$, so $xy' - yx' = x(0) - y(0) = 0$.
>   If $\vec{v} \neq \vec{0}$, there exists $k \in \mathbb{R}$ such that $\vec{u} = k\vec{v}$, which means $x = kx'$ and $y = ky'$.
>   Calculating the cross difference:
>   $$xy' - yx' = (kx')y' - (ky')x' = k x' y' - k y' x' = 0.$$
>
> - **Reverse direction ($\impliedby$):** Assume $xy' - yx' = 0$.
>   If $\vec{v} = \vec{0}$, then $\vec{u}$ and $\vec{v}$ are collinear by definition.
>   Assume $\vec{v} \neq \vec{0}$. At least one of its components is non-zero. Suppose, without loss of generality, that $x' \neq 0$.
>   Let $k = \frac{x}{x'}$, so that $x = kx'$.
>   The identity $xy' - yx' = 0$ then becomes:
>   $$(kx')y' - yx' = 0 \iff x'(ky' - y) = 0.$$
>   Since $x' \neq 0$, it follows that $ky' - y = 0$, hence $y = ky'$.
>   We therefore have both $x = kx'$ and $y = ky'$, which is concisely written $\vec{u} = k\vec{v}$. The vectors are collinear. $\blacksquare$

> **💡 Geometric Interpretation: Area of the Parallelogram.**
> The absolute value of the determinant $|\det(\vec{u}, \vec{v})|$ is exactly equal to the **area of the parallelogram** spanned by the two vectors $\vec{u}$ and $\vec{v}$!
> If the vectors are collinear, the parallelogram collapses flat: its area is zero, which yields $\det(\vec{u}, \vec{v}) = 0$.

#### 5.3 Two Major Geometric Applications

Thanks to the determinant, geometric problems of alignment and parallelism transform into direct algebraic tests:

1. **Parallelism of lines:**
   Two lines $(AB)$ and $(CD)$ are parallel if and only if their direction vectors $\vec{AB}$ and $\vec{CD}$ are collinear:
   $$(AB) \parallel (CD) \iff \det(\vec{AB}, \vec{CD}) = 0.$$

2. **Collinearity of three points:**
   Three distinct points $A, B, C$ are collinear if and only if the vectors $\vec{AB}$ and $\vec{AC}$ share the same direction:
   $$A, B, C \text{ are collinear} \iff \vec{AB} \text{ and } \vec{AC} \text{ are collinear} \iff \det(\vec{AB}, \vec{AC}) = 0.$$

---

### 6. Detailed Worked Examples

> **Worked Example 1 — Simplifying a Vector Expression Using Chasles.**
> Simplify the following vector expression as much as possible:
> $$\vec{W} = \vec{AB} - \vec{CB} + \vec{CD} - \vec{AD}.$$
>
> **Step-by-Step Method:**
> 1. Replace subtractions by the addition of the opposite:
>    $$-\vec{CB} = \vec{BC} \quad \text{and} \quad -\vec{AD} = \vec{DA}.$$
> 2. Rewrite the expression:
>    $$\vec{W} = \vec{AB} + \vec{BC} + \vec{CD} + \vec{DA}.$$
> 3. Chain consecutive terms using Chasles' relation:
>    $$\vec{AB} + \vec{BC} = \vec{AC},$$
>    $$\vec{AC} + \vec{CD} = \vec{AD},$$
>    $$\vec{AD} + \vec{DA} = \vec{AA} = \vec{0}.$$
> **Conclusion:** $\vec{W} = \vec{0}$.

> **Worked Example 2 — Calculating Coordinates and Distances.**
> In an orthonormal coordinate system $(O\,; \vec{i}, \vec{j})$, consider $A(-3\,; 2)$, $B(1\,; 5)$, and $C(4\,; 1)$.
> 1. Determine the coordinates of $\vec{AB}$ and the exact length $AB$.
> 2. Determine the coordinates of point $D$ such that $ABCD$ is a parallelogram.
>
> **Solution:**
> 1. Coordinates of $\vec{AB}$:
>    $$\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix} = \begin{pmatrix} 1 - (-3) \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}.$$
>    Norm of $\vec{AB}$ (distance $AB$):
>    $$AB = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5.$$
> 2. Caution: $ABCD$ is a parallelogram if and only if $\vec{AB} = \vec{DC}$ (or $\vec{AD} = \vec{BC}$).
>    Let $(x_D\,; y_D)$ denote the coordinates of $D$.
>    $$\vec{DC}\begin{pmatrix} x_C - x_D \\ y_C - y_D \end{pmatrix} = \begin{pmatrix} 4 - x_D \\ 1 - y_D \end{pmatrix}.$$
>    The equality $\vec{AB} = \vec{DC}$ translates into the system:
>    $$\begin{cases} 4 - x_D = 4 \implies x_D = 0 \\ 1 - y_D = 3 \implies y_D = 1 - 3 = -2 \end{cases}$$
>    The desired point is therefore $D(0\,; -2)$.
>    *(Verification via midpoints: midpoint of $[AC]$ is $\left(\frac{-3+4}{2}\,;\,\frac{2+1}{2}\right) = (0.5\,;\,1.5)$; midpoint of $[BD]$ is $\left(\frac{1+0}{2}\,;\,\frac{5+(-2)}{2}\right) = (0.5\,;\,1.5)$. The diagonals indeed bisect each other!)*

> **Worked Example 3 — Testing Point Collinearity with the Determinant.**
> Consider points $E(-2\,; -3)$, $F(2\,; 3)$, and $G(6\,; 9)$. Are they collinear?
>
> **Solution:**
> Compute coordinates of vectors $\vec{EF}$ and $\vec{EG}$:
> $$\vec{EF}\begin{pmatrix} 2 - (-2) \\ 3 - (-3) \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}, \quad \vec{EG}\begin{pmatrix} 6 - (-2) \\ 9 - (-3) \end{pmatrix} = \begin{pmatrix} 8 \\ 12 \end{pmatrix}.$$
> Compute the determinant:
> $$\det(\vec{EF}, \vec{EG}) = \begin{vmatrix} 4 & 8 \\ 6 & 12 \end{vmatrix} = 4 \times 12 - 6 \times 8 = 48 - 48 = 0.$$
> The determinant is zero, so vectors $\vec{EF}$ and $\vec{EG}$ are collinear.
> Since they share the common point $E$, points $E$, $F$, and $G$ are collinear.

> **Worked Example 4 — Finding a Parameter for Parallelism.**
> Let $\vec{u}\begin{pmatrix} 2m - 1 \\ 3 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} 5 \\ m + 2 \end{pmatrix}$ where $m \in \mathbb{R}$ is an unknown scalar.
> For what values of $m$ are these vectors collinear?
>
> **Solution:**
> $\vec{u}$ and $\vec{v}$ are collinear if and only if $\det(\vec{u}, \vec{v}) = 0$:
> $$(2m - 1)(m + 2) - 3 \times 5 = 0.$$
> Expanding:
> $$2m^2 + 4m - m - 2 - 15 = 0 \iff 2m^2 + 3m - 17 = 0.$$
> This is a quadratic equation. Its discriminant is:
> $$\Delta = 3^2 - 4 \times 2 \times (-17) = 9 + 136 = 145 > 0.$$
> There are two distinct real solutions:
> $$m_1 = \frac{-3 - \sqrt{145}}{4} \quad \text{and} \quad m_2 = \frac{-3 + \sqrt{145}}{4}.$$

> **Worked Example 5 — Pure Geometric Vector Decomposition.**
> Let $ABC$ be a triangle. Points $P$ and $Q$ are defined by $\vec{AP} = \frac{1}{3}\vec{AB}$ and $\vec{AQ} = \frac{1}{3}\vec{AC}$.
> Prove without using a coordinate frame that $(PQ) \parallel (BC)$.
>
> **Solution:**
> Express vector $\vec{PQ}$ in terms of $\vec{AB}$ and $\vec{AC}$ using Chasles' relation:
> $$\vec{PQ} = \vec{PA} + \vec{AQ} = -\vec{AP} + \vec{AQ} = -\frac{1}{3}\vec{AB} + \frac{1}{3}\vec{AC} = \frac{1}{3}(-\vec{AB} + \vec{AC}) = \frac{1}{3}(\vec{BA} + \vec{AC}).$$
> By Chasles' relation, $\vec{BA} + \vec{AC} = \vec{BC}$.
> Hence:
> $$\vec{PQ} = \frac{1}{3}\vec{BC}.$$
> Vector $\vec{PQ}$ is the product of vector $\vec{BC}$ by scalar $\frac{1}{3}$.
> Vectors $\vec{PQ}$ and $\vec{BC}$ are therefore collinear, which proves that lines $(PQ)$ and $(BC)$ are strictly parallel.
> *(Notice: we have just reproved Thales' theorem using vectors!)*

> **Worked Example 6 — The Centroid of a Triangle.**
> Let $ABC$ be a triangle. Let $G$ be the point defined by the relation:
> $$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}.$$
> 1. Let $A'$ be the midpoint of $[BC]$. Express $\vec{GB} + \vec{GC}$ in terms of $\vec{GA'}$.
> 2. Deduce that $G$ lies on median $(AA')$ and specify its location on the segment.
>
> **Solution:**
> 1. From the midpoint identity proven in §3.5, since $A'$ is the midpoint of $[BC]$, we have:
>    $$\vec{GB} + \vec{GC} = 2\vec{GA'}.$$
> 2. Substitute into the initial relation:
>    $$\vec{GA} + 2\vec{GA'} = \vec{0} \iff \vec{GA} = -2\vec{GA'} \iff -\vec{AG} = -2\vec{GA'} \iff \vec{AG} = 2\vec{GA'}.$$
>    Insert $G$ into the right-hand side using Chasles: $\vec{AA'} = \vec{AG} + \vec{GA'} = \vec{AG} + \frac{1}{2}\vec{AG} = \frac{3}{2}\vec{AG}$.
>    We deduce:
>    $$\vec{AG} = \frac{2}{3}\vec{AA'}.$$
>    Vectors $\vec{AG}$ and $\vec{AA'}$ are collinear: point $G$ is situated on the median line $(AA')$, two-thirds of the way from vertex $A$. $G$ is the **centroid** (isobarycenter) of triangle $ABC$.

---

### 7. In Computer Science: Testing Collinearity in Python

Here is a Python script that takes the coordinates of two vectors and tests their collinearity using the determinant:

```python
def determinant(ux, uy, vx, vy):
    """Calculates the determinant of two vectors u(ux, uy) and v(vx, vy)."""
    return ux * vy - uy * vx

def are_collinear(ux, uy, vx, vy, tolerance=1e-9):
    """Checks whether two vectors are collinear up to a given precision."""
    det = determinant(ux, uy, vx, vy)
    return abs(det) < tolerance

# Test with u(4, 6) and v(6, 9)
print("u and v collinear?", are_collinear(4, 6, 6, 9))  # Outputs True

# Test with u(3, -1) and v(2, 5)
print("u and v collinear?", are_collinear(3, -1, 2, 5))  # Outputs False
```

---

### Key Takeaways

1. **Vector:** a geometric entity characterized by a **direction** (line of action), a **sense** (arrowhead), and a **magnitude/norm** (length $\|\vec{u}\|$).
2. **Vector Equality:** $\vec{AB} = \vec{CD} \iff ABDC$ is a parallelogram.
3. **Chasles' Relation:** $\vec{AB} + \vec{BC} = \vec{AC}$. To subtract: $\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$ where $-\vec{AB} = \vec{BA}$.
4. **Midpoint $I$ of $[AB]$:** $\vec{AI} = \vec{IB} \iff \vec{IA} + \vec{IB} = \vec{0} \iff \vec{MA} + \vec{MB} = 2\vec{MI}$.
5. **Coordinates:**
   - $\vec{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix}$
   - Midpoint: $I\left(\frac{x_A+x_B}{2} \,;\, \frac{y_A+y_B}{2}\right)$
   - Norm: $\|\vec{u}\| = \sqrt{x^2+y^2}$ and $AB = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2}$ (in an orthonormal frame).
6. **Collinearity and Determinant:**
   - $\vec{u}$ and $\vec{v}$ are collinear $\iff \vec{u} = k\vec{v}$ (or one is zero) $\iff \det(\vec{u}, \vec{v}) = xy' - yx' = 0$.
   - Parallel lines: $(AB) \parallel (CD) \iff \det(\vec{AB}, \vec{CD}) = 0$.
   - Collinear points: $A, B, C$ collinear $\iff \det(\vec{AB}, \vec{AC}) = 0$.

---

### Exercises

#### Direct Application Exercises (★)

1. Let $MNOP$ be a parallelogram. Name three pairs of equal vectors.
2. Simplify the expression $\vec{u} = \vec{RS} + \vec{ST} + \vec{TR}$.
3. Simplify the expression $\vec{v} = \vec{AB} - \vec{AC} + \vec{BC}$.
4. Given vector $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$, compute its norm $\|\vec{u}\|$.
5. Given points $A(2\,; -5)$ and $B(-1\,; 7)$, calculate the coordinates of vector $\vec{AB}$.
6. Using the same points $A$ and $B$, calculate the coordinates of the midpoint $K$ of $[AB]$.
7. Calculate the exact distance $AB$.
8. Are the vectors $\vec{u}\begin{pmatrix} 6 \\ -4 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} -9 \\ 6 \end{pmatrix}$ collinear?
9. Are the vectors $\vec{w}\begin{pmatrix} 5 \\ 3 \end{pmatrix}$ and $\vec{z}\begin{pmatrix} 7 \\ 4 \end{pmatrix}$ collinear?
10. Find the real number $y$ such that $\vec{a}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ and $\vec{b}\begin{pmatrix} 10 \\ y \end{pmatrix}$ are collinear.

#### Practice and Reasoning Exercises (★★)

11. Let $A(1\,; 2)$, $B(4\,; 6)$, and $C(-2\,; -2)$. Are points $A, B, C$ collinear?
12. Consider four points $K(-1\,; 1)$, $L(3\,; 3)$, $M(5\,; 1)$, and $N(1\,; -1)$.
    a) Calculate coordinates of $\vec{KL}$ and $\vec{NM}$.
    b) What is the precise nature of quadrilateral $KLMN$?
13. Using points $K, L, M, N$ from Exercise 12, calculate lengths $KL$ and $LM$. Is the quadrilateral a rhombus? A rectangle?
14. Let $ABC$ be a triangle. Construct (or express) points $M$ and $N$ defined by:
    $$\vec{AM} = \vec{AB} + 2\vec{AC} \quad \text{and} \quad \vec{AN} = 2\vec{AB} + \vec{AC}.$$
    Express vector $\vec{MN}$ in terms of $\vec{AB}$ and $\vec{AC}$.
15. Consider points $A(-2\,; 3)$, $B(4\,; 1)$, and $C(2\,; 5)$.
    Determine the coordinates of point $E$ such that $\vec{AE} = 2\vec{AB} - 3\vec{BC}$.
16. Let $ABC$ be any arbitrary triangle. Let $D$ be the reflection of $A$ across $B$, and $E$ the reflection of $B$ across $C$. Express $\vec{DE}$ in terms of $\vec{AB}$ and $\vec{BC}$.
17. For what value of the real number $x$ are points $P(x\,; 3)$, $Q(2\,; -1)$, and $R(6\,; 7)$ collinear?
18. Given $\vec{u}\begin{pmatrix} 2 \\ -1 \end{pmatrix}$ and $\vec{v}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$, determine scalars $\alpha$ and $\beta$ such that vector $\vec{w}\begin{pmatrix} 7 \\ 0 \end{pmatrix}$ can be written $\vec{w} = \alpha\vec{u} + \beta\vec{v}$.

#### Advanced Problems and Challenges (★★★)

19. **The Vector Midpoint Theorem.**
    Let $ABC$ be a triangle. Let $I$ be the midpoint of $[AB]$ and $J$ the midpoint of $[AC]$.
    Prove using vector algebra that $\vec{IJ} = \frac{1}{2}\vec{BC}$. Deduce the relative position of lines $(IJ)$ and $(BC)$ as well as the ratio of their lengths.
20. **Varignon's Quadrilateral.**
    Let $ABCD$ be an arbitrary quadrilateral. Let $I, J, K, L$ be the midpoints of sides $[AB], [BC], [CD], [DA]$ respectively.
    a) Express $\vec{IJ}$ and $\vec{LK}$ in terms of the vertex vectors.
    b) Deduce that $IJKL$ is always a parallelogram.
21. **Concurrency of the Three Medians.**
    Let $ABC$ be a triangle. Let $A', B', C'$ be the midpoints of sides $[BC], [CA], [AB]$ respectively.
    Let $G$ be the point satisfying $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$.
    a) Prove that for any arbitrary point $M$ in the plane: $\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$.
    b) Deduce that $G$ belongs to each of the three medians $(AA')$, $(BB')$, and $(CC')$, and specify the point of concurrency.
22. **Aircraft Trajectory and Wind Drift.**
    An airplane flies on a heading due North with an airspeed of $600\text{ km/h}$ relative to the air mass. A gale-force wind blows from the Northwest toward the Southeast (at $45^\circ$ to the cardinal axes) at a speed of $100\sqrt{2}\text{ km/h}$.
    We choose an orthonormal coordinate system where the positive $x$-axis points East and the positive $y$-axis points North.
    a) Determine the components of the aircraft airspeed vector $\vec{v}_a$.
    b) Determine the components of the wind vector $\vec{v}_w$.
    c) Calculate the ground velocity vector $\vec{v}_s = \vec{v}_a + \vec{v}_w$.
    d) Deduce the actual ground speed of the aircraft and the angular drift of its track.

---

### Solutions

1. In parallelogram $MNOP$: $\vec{MN} = \vec{PO}$, $\vec{NO} = \vec{MP}$, $\vec{NM} = \vec{OP}$.
2. $\vec{RS} + \vec{ST} + \vec{TR} = \vec{RT} + \vec{TR} = \vec{RR} = \vec{0}$.
3. $\vec{v} = \vec{AB} + \vec{CA} + \vec{BC} = (\vec{CA} + \vec{AB}) + \vec{BC} = \vec{CB} + \vec{BC} = \vec{0}$.
4. $\|\vec{u}\| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
5. $\vec{AB}\begin{pmatrix} -1 - 2 \\ 7 - (-5) \end{pmatrix} = \begin{pmatrix} -3 \\ 12 \end{pmatrix}$.
6. $x_K = \frac{2 + (-1)}{2} = \frac{1}{2} = 0.5$ and $y_K = \frac{-5 + 7}{2} = \frac{2}{2} = 1$. Thus $K(0.5\,; 1)$.
7. $AB = \sqrt{(-3)^2 + 12^2} = \sqrt{9 + 144} = \sqrt{153} = 3\sqrt{17}$.
8. $\det(\vec{u}, \vec{v}) = 6 \times 6 - (-4) \times (-9) = 36 - 36 = 0$. Yes, they are collinear (we also observe $\vec{v} = -1.5\vec{u}$).
9. $\det(\vec{w}, \vec{z}) = 5 \times 4 - 3 \times 7 = 20 - 21 = -1 \neq 0$. No, they are not collinear.
10. $\det(\vec{a}, \vec{b}) = 4y - (-6) \times 10 = 4y + 60 = 0 \iff 4y = -60 \iff y = -15$.
11. $\vec{AB}\begin{pmatrix} 4 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ and $\vec{AC}\begin{pmatrix} -2 - 1 \\ -2 - 2 \end{pmatrix} = \begin{pmatrix} -3 \\ -4 \end{pmatrix}$.
    We immediately observe $\vec{AC} = -1\vec{AB}$ (or $\det = 3(-4) - 4(-3) = -12 + 12 = 0$). The vectors are collinear and share point $A$, so $A, B, C$ are collinear.
12. a) $\vec{KL}\begin{pmatrix} 3 - (-1) \\ 3 - 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$ and $\vec{NM}\begin{pmatrix} 5 - 1 \\ 1 - (-1) \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$.
    b) Since $\vec{KL} = \vec{NM}$, quadrilateral $KLMN$ is a parallelogram.
13. Length $KL = \sqrt{4^2 + 2^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$.
    Calculate $\vec{LM}\begin{pmatrix} 5 - 3 \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix}$.
    Length $LM = \sqrt{2^2 + (-2)^2} = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}$.
    Since $KL \neq LM$, consecutive sides are not equal: it is not a rhombus.
    Check whether sides are perpendicular: $KM^2$ with $\vec{KM}\begin{pmatrix} 5 - (-1) \\ 1 - 1 \end{pmatrix} = \begin{pmatrix} 6 \\ 0 \end{pmatrix} \implies KM^2 = 36$.
    Yet $KL^2 + LM^2 = 20 + 8 = 28 \neq 36$. Triangle $KLM$ is not right-angled, so $KLMN$ is not a rectangle. It is a general parallelogram.
14. By Chasles: $\vec{MN} = \vec{MA} + \vec{AN} = -\vec{AM} + \vec{AN}$.
    Substituting: $\vec{MN} = -(\vec{AB} + 2\vec{AC}) + (2\vec{AB} + \vec{AC}) = -\vec{AB} - 2\vec{AC} + 2\vec{AB} + \vec{AC} = \vec{AB} - \vec{AC} = \vec{CB}$.
15. $\vec{AB}\begin{pmatrix} 4 - (-2) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -2 \end{pmatrix}$ and $\vec{BC}\begin{pmatrix} 2 - 4 \\ 5 - 1 \end{pmatrix} = \begin{pmatrix} -2 \\ 4 \end{pmatrix}$.
    Then $\vec{AE} = 2\vec{AB} - 3\vec{BC} = 2\begin{pmatrix} 6 \\ -2 \end{pmatrix} - 3\begin{pmatrix} -2 \\ 4 \end{pmatrix} = \begin{pmatrix} 12 + 6 \\ -4 - 12 \end{pmatrix} = \begin{pmatrix} 18 \\ -16 \end{pmatrix}$.
    Since $A$ has coordinates $(-2\,; 3)$:
    $x_E = x_A + 18 = -2 + 18 = 16$ and $y_E = y_A - 16 = 3 - 16 = -13$. Thus $E(16\,; -13)$.
16. $D$ reflection of $A$ across $B \implies \vec{BD} = \vec{AB}$.
    $E$ reflection of $B$ across $C \implies \vec{BE} = 2\vec{BC}$.
    By Chasles: $\vec{DE} = \vec{DB} + \vec{BE} = -\vec{BD} + \vec{BE} = -\vec{AB} + 2\vec{BC}$.
17. $\vec{QR}\begin{pmatrix} 6 - 2 \\ 7 - (-1) \end{pmatrix} = \begin{pmatrix} 4 \\ 8 \end{pmatrix}$.
    $\vec{QP}\begin{pmatrix} x - 2 \\ 3 - (-1) \end{pmatrix} = \begin{pmatrix} x - 2 \\ 4 \end{pmatrix}$.
    $P, Q, R$ collinear $\iff \det(\vec{QR}, \vec{QP}) = 0 \iff 4 \times 4 - 8(x - 2) = 0 \iff 16 - 8x + 16 = 0 \iff 8x = 32 \iff x = 4$.
18. Equality $\vec{w} = \alpha\vec{u} + \beta\vec{v}$ gives the linear system:
    $$\begin{cases} 2\alpha + \beta = 7 \\ -\alpha + 3\beta = 0 \end{cases}$$
    From the second equation, $\alpha = 3\beta$. Substituting into the first: $2(3\beta) + \beta = 7 \iff 7\beta = 7 \iff \beta = 1$.
    Hence $\alpha = 3 \times 1 = 3$. Solution: $\alpha = 3, \beta = 1$.
19. $I$ midpoint of $[AB] \implies \vec{AI} = \frac{1}{2}\vec{AB}$, so $\vec{IA} = -\frac{1}{2}\vec{AB}$.
    $J$ midpoint of $[AC] \implies \vec{AJ} = \frac{1}{2}\vec{AC}$.
    By Chasles: $\vec{IJ} = \vec{IA} + \vec{AJ} = -\frac{1}{2}\vec{AB} + \frac{1}{2}\vec{AC} = \frac{1}{2}(\vec{BA} + \vec{AC}) = \frac{1}{2}\vec{BC}$.
    Since $\vec{IJ} = \frac{1}{2}\vec{BC}$, the vectors are collinear, so lines $(IJ)$ and $(BC)$ are parallel. Taking norms yields $IJ = \frac{1}{2}BC$.
20. a) In triangle $ABC$, by the vector midpoint theorem (Ex. 19), $\vec{IJ} = \frac{1}{2}\vec{AC}$.
    In triangle $ADC$, $L$ is the midpoint of $[AD]$ and $K$ the midpoint of $[CD]$. Thus $\vec{LK} = \frac{1}{2}\vec{AC}$.
    b) We find $\vec{IJ} = \vec{LK}$. A quadrilateral whose opposite sides form equal vectors is a parallelogram. Therefore $IJKL$ is always a parallelogram.
21. a) Let $M$ be an arbitrary point. By Chasles: $\vec{MA} + \vec{MB} + \vec{MC} = (\vec{MG} + \vec{GA}) + (\vec{MG} + \vec{GB}) + (\vec{MG} + \vec{GC}) = 3\vec{MG} + (\vec{GA} + \vec{GB} + \vec{GC}) = 3\vec{MG} + \vec{0} = 3\vec{MG}$.
    b) Choose $M = A'$ (midpoint of $[BC]$). Then $\vec{A'A} + \vec{A'B} + \vec{A'C} = 3\vec{A'G}$.
    Since $A'$ is the midpoint of $[BC]$, $\vec{A'B} + \vec{A'C} = \vec{0}$.
    The equality becomes $\vec{A'A} = 3\vec{A'G}$, or $\vec{AG} = \frac{2}{3}\vec{AA'}$.
    Point $G$ therefore lies on median $(AA')$, two-thirds from vertex $A$. Choosing $M = B'$ then $M = C'$ similarly yields $\vec{BG} = \frac{2}{3}\vec{BB'}$ and $\vec{CG} = \frac{2}{3}\vec{CC'}$. Point $G$ is therefore the unique point of concurrency of the three medians.
22. a) The aircraft flies due North ($x = 0$) at $600\text{ km/h}$: $\vec{v}_a\begin{pmatrix} 0 \\ 600 \end{pmatrix}$.
    b) The wind blows from Northwest to Southeast (angle $-45^\circ$, giving positive $x$ Eastward, negative $y$ Southward).
    Its speed is $100\sqrt{2}$. Since $\cos(45^\circ) = \sin(45^\circ) = \frac{\sqrt{2}}{2}$:
    $v_{wx} = 100\sqrt{2} \times \frac{\sqrt{2}}{2} = 100$, and $v_{wy} = -100$.
    Thus $\vec{v}_w\begin{pmatrix} 100 \\ -100 \end{pmatrix}$.
    c) Ground velocity: $\vec{v}_s = \vec{v}_a + \vec{v}_w = \begin{pmatrix} 0 + 100 \\ 600 - 100 \end{pmatrix} = \begin{pmatrix} 100 \\ 500 \end{pmatrix}$.
    d) Actual ground speed: $\|\vec{v}_s\| = \sqrt{100^2 + 500^2} = \sqrt{10000 + 250000} = \sqrt{260000} \approx 509.9\text{ km/h}$.
    Angular drift $\theta$ toward the East: $\tan\theta = \frac{100}{500} = 0.2 \implies \theta \approx 11.3^\circ$. The aircraft drifts more than $11^\circ$ to the right and loses nearly $90\text{ km/h}$ over ground!

---

### The Question That Opens the Future

We have learned to slide free arrows throughout the plane and to detect whether two arrows point along the same line using the determinant. But what happens when we drive a stake into the ground at point $A$ and let arrow $\vec{u}$ point out an infinite trajectory? We obtain a **straight line**.

How can we characterize the set of all points aligned along this line of sight? How do we link the algebraic equation of a line to its direction vectors, and how do we calculate the exact location where two trajectories intersect? That is what we will discover in **The Line of Sight**.
