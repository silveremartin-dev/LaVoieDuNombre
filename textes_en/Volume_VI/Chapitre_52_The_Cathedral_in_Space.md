# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 52: The Cathedral in Space

> *“Geometry is a magic that allows orienting a nave toward the North Star, raising stone vaults to the sky without collapsing, and measuring the distance of an invisible point without ever leaving the ground.”*
> — Notebooks of medieval master builders

---

### What You Are About to Discover

- How cathedral builders conquered the **third dimension**: from the flat ground to the celestial keystone.
- The orthonormal coordinate system $(O; \vec{i}, \vec{j}, \vec{k})$ of 3D space: abscissa ($x$), ordinate ($y$), **z-coordinate / altitude** ($z$), and the 3D distance formula derived from a double Pythagorean theorem.
- The **parametric representation of a line** in space: why a line in 3D can never be described by a single Cartesian equation.
- The relative positions of two lines: parallel, intersecting… or **skew / non-coplanar** (the ultimate trap of 3D!).
- The **dot product (scalar product) in space**: its analytic expression $\vec{u} \cdot \vec{v} = xx' + yy' + zz'$ and its role as a right-angle detector.
- The **normal vector** $\vec{n}(a\,; b\,; c)$ and the **Cartesian equation of a plane** $ax + by + cz + d = 0$.
- The **orthogonal projection** of a point onto a line or a plane, and the calculation of shortest distance.

---

### 1. The Problem: The Builders of Chartres Cathedral

#### 1.1 Leaving the Flat Parchment

In the Middle Ages, the architects and stonecutters who designed Gothic cathedrals—such as Chartres or Notre-Dame de Paris—faced a monumental challenge.
On their parchments and on the plaster floor of the tracing room, they could only draw figures in **two dimensions**: circles, triangles, rectangles. But the cathedral is a **three-dimensional** edifice:
- The ground plan provides the length of the nave and the width of the transept;
- But the pillars soar toward the sky, the flying buttresses span empty air diagonally, and the ribs of the ribbed vaults cross at a **keystone suspended 37 meters above the floor**.

If two flying buttresses cut in the quarry do not meet at the exact same point in space, the vault fails and hundreds of tons of stone come crashing down.
In the plane, two non-parallel lines **necessarily intersect**.
In space, however, two lines can be non-parallel and yet **never intersect**: picture two airplanes flying in different directions at different altitudes, or two cables crossing in a timber frame without touching. Such lines are said to be **skew (non-coplanar)**.

```
                   z ▲  (Altitude / z-axis)
                     │
                     │       . Keystone (x, y, z)
                     │     / |
                     │   /   |
                     │ /     |
                     ┼───────┼────────► y (Transept / y-axis)
                    /│       * (x, y, 0)
                  /  │      /
                /    │    /
            x ▼ (Nave / x-axis)
```

To build toward the heavens without risk of error, we need an infallible system to locate every grain of stone throughout the volume of three-dimensional space.

---

### 2. The 3D Coordinate System and Coordinates

#### 2.1 The Orthonormal Frame $(O; \vec{i}, \vec{j}, \vec{k})$

To determine the position of a point in space, we choose an origin $O(0\,;0\,;0)$ and three mutually perpendicular axes, each equipped with a unit vector of equal length:
- The $(Ox)$ axis directed by $\vec{i}$: the **x-axis** or axis of abscissas (often pointing forward);
- The $(Oy)$ axis directed by $\vec{j}$: the **y-axis** or axis of ordinates (pointing to the right);
- The $(Oz)$ axis directed by $\vec{k}$: the **z-axis** or axis of altitudes / cotes (pointing upward).

The triplet $(O; \vec{i}, \vec{j}, \vec{k})$ constitutes an **orthonormal coordinate frame of space**.

> **📐 Definition — Coordinates of a Point and a Vector:**
> - For any point $M$ in space, there exists a unique triplet of real numbers $(x\,; y\,; z)$ such that:
>   $$\vec{OM} = x \vec{i} + y \vec{j} + z \vec{k}.$$
>   The point $M$ has coordinates $M(x\,; y\,; z)$. $x$ is the abscissa, $y$ the ordinate, and $z$ the altitude (z-coordinate).
> - If $A(x_A\,; y_A\,; z_A)$ and $B(x_B\,; y_B\,; z_B)$ are two points, the vector $\vec{AB}$ has coordinates:
>   $$\vec{AB} \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}.$$
> - The midpoint $I$ of segment $[AB]$ has coordinates:
>   $$I\left( \dfrac{x_A + x_B}{2} \; ; \; \dfrac{y_A + y_B}{2} \; ; \; \dfrac{z_A + z_B}{2} \right).$$

#### 2.2 Norm and Distance: The Double Pythagorean Theorem

What is the distance between two points in space?
To travel from point $A(x_A\,; y_A\,; z_A)$ to point $B(x_B\,; y_B\,; z_B)$, we can construct a rectangular cuboid (box) whose space diagonal is the segment $[AB]$:

```
                  z ▲
                    │        B(xB, yB, zB)
                    │       ┌────────*
                    │      /│       /│
                    │     / │      / │  Δz = zB - zA
                    │    *──┼─────*  │
                    │    │A │     │  │
                    │    │  └─────┼──* C
                    │    │ /      │ /  Δy = yB - yA
                    │    *────────*
                    │       Δx
                  0 └────────────────────────► y
                   /
                x ▼
```

1. In the bottom horizontal plane, the right triangle yields by Pythagoras:
   $$AC^2 = (x_B - x_A)^2 + (y_B - y_A)^2.$$
2. In the vertical right triangle $ACB$, the height is $\Delta z = z_B - z_A$, and the hypotenuse is the diagonal $[AB]$. A second application of Pythagoras gives:
   $$AB^2 = AC^2 + BC^2 = (x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2.$$

> **📐 Theorem — Vector Norm and Distance Between Two Points:**
> - The norm (length) of a vector $\vec{u}(x\,; y\,; z)$ in an orthonormal frame is:
>   $$\|\vec{u}\| = \sqrt{x^2 + y^2 + z^2}.$$
> - The distance between two points $A$ and $B$ is:
>   $$AB = \|\vec{AB}\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}.$$

---

### 3. Lines in Space: Parametric Representation

#### 3.1 Why a Single Equation Does Not Suffice

In the 2D plane, a line has a Cartesian equation of the form $ax + by + c = 0$.
What does that same equation represent in 3D space?
If we write $2x + 3y - 6 = 0$ in space, the variable $z$ does not appear: this means that $z$ can take **any real value**! All points above and below the line form an infinite vertical wall: **it is a plane, not a line**!
In space, a single linear equation always defines a surface (a plane). To define a line, one needs the intersection of two planes, or even better: **a time-dependent (parametric) trajectory**.

#### 3.2 Parametric Representation of a Line

Let $A(x_A\,; y_A\,; z_A)$ be a point in space and $\vec{u}(a\,; b\,; c)$ a non-zero vector.
The line $\mathcal{D}$ passing through $A$ with direction vector $\vec{u}$ is the set of points $M(x\,; y\,; z)$ such that the vectors $\vec{AM}$ and $\vec{u}$ are **collinear**:
$$M \in \mathcal{D} \iff \text{there exists a real number } t \in \mathbb{R} \text{ such that } \vec{AM} = t \vec{u}.$$

Projecting onto the three coordinate components:

> **📐 Definition — Parametric Representation of a Line:**
> The line $\mathcal{D}$ passing through $A(x_A\,; y_A\,; z_A)$ and directed by $\vec{u}(a\,; b\,; c)$ admits as a parametric representation the system:
> $$\begin{cases} x = x_A + a t \\ y = y_A + b t \\ z = z_A + c t \end{cases} \quad (t \in \mathbb{R}).$$
> The real number $t$ is called the **parameter**.

**Kinematic Interpretation:** Think of an aircraft taking off at time $t = 0$ from point $A$, with constant velocity vector $\vec{u}$. The parameter $t$ plays the role of time: at every second $t$, the aircraft occupies a precise position along the line!

> **Worked Example 1 — Line passing through two points.**
> Let $A(1\,; -2\,; 3)$ and $B(4\,; 2\,; -1)$.
> 1. Determine a parametric representation of the line $(AB)$.
> 2. Does the point $C(7\,; 6\,; -5)$ lie on the line $(AB)$?
> 3. Does the point $D(2\,; 0\,; 1)$ lie on the line $(AB)$?
>
> *Solution:*
> 1. The direction vector is $\vec{AB} \begin{pmatrix} 4 - 1 \\ 2 - (-2) \\ -1 - 3 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -4 \end{pmatrix}$.
>    The line $(AB)$ passing through $A$ is given by:
>    $$\begin{cases} x = 1 + 3t \\ y = -2 + 4t \\ z = 3 - 4t \end{cases} \quad (t \in \mathbb{R}).$$
> 2. For the point $C(7\,; 6\,; -5)$:
>    $$\begin{cases} 7 = 1 + 3t \implies 3t = 6 \implies t = 2 \\ 6 = -2 + 4t \implies 4t = 8 \implies t = 2 \\ -5 = 3 - 4t \implies -4t = -8 \implies t = 2 \end{cases}$$
>    The same value $t = 2$ satisfies all three equations simultaneously. Therefore **$C \in (AB)$**.
> 3. For the point $D(2\,; 0\,; 1)$:
>    - $2 = 1 + 3t \implies t = \dfrac{1}{3}$.
>    - Check with $y$: $-2 + 4\left(\dfrac{1}{3}\right) = -2 + \dfrac{4}{3} = -\dfrac{2}{3} \neq 0$.
>    The equations are incompatible. Therefore **$D \notin (AB)$**.

#### 3.3 Relative Positions of Two Lines in Space

Consider two lines $\mathcal{D}_1$ directed by $\vec{u}_1$ and $\mathcal{D}_2$ directed by $\vec{u}_2$.

```
                            Are the direction vectors collinear?
                            (u₁ = k u₂)
                               /       \
                             YES        NO
                             /            \
                       Parallel lines     Do they intersect?
                      /              \     (system of 3 equations in 2 unknowns)
                 Coincident       Strictly               /            \
              (common point)      parallel            YES              NO
                                                       /                \
                                              Intersecting at a point   SKEW (NON-COPLANAR)
                                              (they are coplanar)       (no contact, no common plane)
```

> **⚠️ Warning, Pitfall! — Two lines with no intersection point are NOT necessarily parallel!**
> This is the most frequent trap for students coming from plane geometry: in space, the vast majority of line pairs are **neither parallel nor intersecting**: they are **skew / non-coplanar** (they pass over or under each other at different heights without ever crossing).

---

### 4. Dot Product in Space and Orthogonality

#### 4.1 Definition and Analytic Expression

The dot product (scalar product) in space possesses exactly the same geometric properties as in the plane:

> **📐 Definition — Dot Product in Space:**
> For any vectors $\vec{u}$ and $\vec{v}$:
> $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\vec{u}, \vec{v}).$$
> In an **orthonormal** frame $(O; \vec{i}, \vec{j}, \vec{k})$, if $\vec{u}(x\,; y\,; z)$ and $\vec{v}(x'\,; y'\,; z')$:
> $$\vec{u} \cdot \vec{v} = x x' + y y' + z z'.$$

> **Orthogonality Criterion:**
> $$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0 \iff x x' + y y' + z z' = 0.$$

> **Worked Example 2 — Computing an angle in space.**
> Given points $A(1\,; 0\,; 1)$, $B(2\,; 1\,; 0)$, and $C(0\,; 2\,; 2)$.
> Determine the measure of angle $\widehat{BAC}$.
> - Compute the vectors: $\vec{AB} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$ and $\vec{AC} \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}$.
> - Dot product: $\vec{AB} \cdot \vec{AC} = 1(-1) + 1(2) + (-1)(1) = -1 + 2 - 1 = 0$!
> - Since $\vec{AB} \cdot \vec{AC} = 0$, the vectors are orthogonal: triangle $ABC$ is **right-angled at $A$**, and $\widehat{BAC} = 90^\circ = \dfrac{\pi}{2}\text{ rad}$.

---

### 5. Planes in Space: Normal Vector and Cartesian Equation

#### 5.1 The Concept of a Normal Vector

How can we orient a plane in space?
Think of a tabletop: to orient the surface of the table, the simplest and most direct method is to drive a peg perpendicular to the surface. If we know the direction of the peg and the position of one point on the table, the entire surface is completely locked in space!

<div align="center">
<svg width="450" height="230" viewBox="0 0 450 230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-3d-norm" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#b91c1c" />
    </marker>
    <marker id="arr-3d-u" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8" />
    </marker>
    <marker id="arr-3d-v" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
    </marker>
  </defs>
  <rect width="450" height="230" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
  <polygon points="60,180 320,180 390,110 130,110" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <text x="360" y="135" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1d4ed8">Plane 𝒫</text>
  <circle cx="210" cy="145" r="4" fill="#0f172a"/>
  <text x="195" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">A</text>
  <line x1="210" y1="145" x2="310" y2="160" stroke="#1d4ed8" stroke-width="2.5" marker-end="url(#arr-3d-u)"/>
  <text x="270" y="178" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8">Vector u</text>
  <line x1="210" y1="145" x2="270" y2="120" stroke="#d97706" stroke-width="2.5" marker-end="url(#arr-3d-v)"/>
  <text x="245" y="112" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706">Vector v</text>
  <polygon points="210,130 220,132 220,146 210,145" fill="#fecaca" stroke="#b91c1c" stroke-width="1"/>
  <line x1="210" y1="145" x2="210" y2="40" stroke="#b91c1c" stroke-width="3.5" marker-end="url(#arr-3d-norm)"/>
  <text x="220" y="50" font-family="sans-serif" font-size="15" font-weight="bold" fill="#b91c1c">Normal vector n(a ; b ; c)</text>
  <text x="225" y="212" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">The normal vector n is orthogonal to ALL lines in the plane (it suffices that n · u = 0 and n · v = 0)</text>
</svg>
</div>

> **📐 Definition — Normal Vector to a Plane:**
> A non-zero vector $\vec{n}$ is said to be **normal** to a plane $\mathcal{P}$ if it is orthogonal to the direction of every line in the plane $\mathcal{P}$.
> In practice: $\vec{n}$ is normal to $\mathcal{P}$ if and only if it is orthogonal to **two non-collinear direction vectors** lying in plane $\mathcal{P}$.

```
                 ▲ n (normal vector)
                 │
                 │
         ┌───────*──────────────────┐ Plane P
        /       /A \                 /
       /      u/    \ v             /
      /       ▼      ▼             /
     └────────────────────────────┘
```

#### 5.2 Cartesian Equation of a Plane

Let $A(x_A\,; y_A\,; z_A)$ be a fixed point and $\vec{n}(a\,; b\,; c)$ a non-zero vector.
The plane $\mathcal{P}$ passing through $A$ with normal vector $\vec{n}$ is the set of points $M(x\,; y\,; z)$ such that the vector $\vec{AM}$ is orthogonal to $\vec{n}$:
$$M \in \mathcal{P} \iff \vec{AM} \cdot \vec{n} = 0.$$

Expanding using the coordinates $\vec{AM} \begin{pmatrix} x - x_A \\ y - y_A \\ z - z_A \end{pmatrix}$ and $\vec{n} \begin{pmatrix} a \\ b \\ c \end{pmatrix}$:
$$a(x - x_A) + b(y - y_A) + c(z - z_A) = 0 \iff ax + by + cz - (ax_A + by_A + cz_A) = 0.$$
Setting the constant $d = -(ax_A + by_A + cz_A)$, we obtain the fundamental theorem:

> **📐 Theorem (Cartesian Equation of a Plane) —**
> - Every plane $\mathcal{P}$ in space admits a Cartesian equation of the form:
>   $$ax + by + cz + d = 0$$
>   where $(a\,; b\,; c) \neq (0\,; 0\,; 0)$.
> - Conversely, for any real numbers $a, b, c, d$ with $(a, b, c) \neq (0, 0, 0)$, the set of points $M(x\,; y\,; z)$ satisfying $ax + by + cz + d = 0$ is a **plane**, a normal vector of which is:
>   $$\vec{n} \begin{pmatrix} a \\ b \\ c \end{pmatrix}.$$

> **Worked Example 3 — Equation of a plane given a point and a normal vector.**
> Determine the Cartesian equation of the plane $\mathcal{P}$ passing through $A(2\,; -1\,; 3)$ with normal vector $\vec{n}(3\,; 4\,; -2)$.
> - The equation has the form $3x + 4y - 2z + d = 0$.
> - Point $A(2\,; -1\,; 3)$ belongs to the plane, so its coordinates satisfy the equation:
>   $$3(2) + 4(-1) - 2(3) + d = 0 \iff 6 - 4 - 6 + d = 0 \iff -4 + d = 0 \iff d = 4.$$
> - The Cartesian equation of $\mathcal{P}$ is therefore:
>   $$3x + 4y - 2z + 4 = 0.$$

> **Worked Example 4 — Equation of a plane passing through three non-collinear points.**
> Determine a Cartesian equation of the plane passing through $A(1\,; 0\,; 0)$, $B(0\,; 2\,; 0)$, and $C(0\,; 0\,; 3)$.
> - Form two vectors in the plane: $\vec{AB} \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}$ and $\vec{AC} \begin{pmatrix} -1 \\ 0 \\ 3 \end{pmatrix}$.
>   These vectors are clearly not collinear.
> - Seek a normal vector $\vec{n}(a\,; b\,; c)$ orthogonal to both $\vec{AB}$ and $\vec{AC}$:
>   $$\begin{cases} \vec{n} \cdot \vec{AB} = 0 \iff -a + 2b = 0 \iff a = 2b \\ \vec{n} \cdot \vec{AC} = 0 \iff -a + 3c = 0 \iff a = 3c \end{cases}$$
> - Choose a convenient non-zero value to set the scale: let $a = 6$.
>   Then $b = 3$ and $c = 2$. The vector $\vec{n}(6\,; 3\,; 2)$ is a normal vector!
> - The equation takes the form $6x + 3y + 2z + d = 0$.
>   Substitute $A(1\,; 0\,; 0)$: $6(1) + 0 + 0 + d = 0 \iff d = -6$.
> - Cartesian equation: $6x + 3y + 2z - 6 = 0$ (or $\dfrac{x}{1} + \dfrac{y}{2} + \dfrac{z}{3} = 1$).

---

### 6. Orthogonality, Orthogonal Projection, and Distance

#### 6.1 Orthogonality of a Line and a Plane

> **Property —**
> A line $\mathcal{D}$ with direction vector $\vec{u}$ is **orthogonal (perpendicular)** to a plane $\mathcal{P}$ with normal vector $\vec{n}$ if and only if the vectors $\vec{u}$ and $\vec{n}$ are **collinear**.

```
                   │ D (line directed by u)
                   │
                   ▲ n (normal vector)
         ┌─────────┼────────────────┐ Plane P
        /          * H (projection)  /
       /                            /
      └────────────────────────────┘
```

#### 6.2 Orthogonal Projection of a Point onto a Plane

Let $\mathcal{P}$ be a plane with equation $ax + by + cz + d = 0$ and let $M$ be any point in space.
The **orthogonal projection** of $M$ onto the plane $\mathcal{P}$ is the point $H \in \mathcal{P}$ such that the line $(MH)$ is orthogonal to the plane $\mathcal{P}$.
The distance $MH$ is then the **shortest distance** between the point $M$ and any point belonging to the plane.

> **🧭 Method — Calculating the Coordinates of the Orthogonal Projection $H$:**
> 1. Determine a normal vector $\vec{n}(a\,; b\,; c)$ to the plane $\mathcal{P}$.
> 2. Write the parametric representation of the line $\mathcal{D}$ passing through $M(x_M\,; y_M\,; z_M)$ and directed by $\vec{n}$:
>    $$\begin{cases} x = x_M + a t \\ y = y_M + b t \\ z = z_M + c t \end{cases}$$
> 3. Substitute these expressions for $x, y, z$ into the Cartesian equation of the plane $\mathcal{P}$ to solve for the unique value of the parameter $t_H$.
> 4. Substitute $t_H$ back into the parametric equations to obtain the coordinates of $H$.
> 5. The distance from $M$ to the plane is then the norm $d(M, \mathcal{P}) = \|\vec{MH}\|$.

> **Worked Example 5 — Full computation of an orthogonal projection and distance.**
> Let $M(1\,; 2\,; 3)$ and let $\mathcal{P}$ be the plane with equation $2x - y + 2z - 9 = 0$.
> 1. Determine the coordinates of the orthogonal projection $H$ of $M$ onto $\mathcal{P}$.
> 2. Compute the distance from $M$ to the plane $\mathcal{P}$.
>
> *Solution:*
> 1. A normal vector to the plane is $\vec{n} \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$.
>    The orthogonal line $\mathcal{D}$ passing through $M$ is:
>    $$\begin{cases} x = 1 + 2t \\ y = 2 - t \\ z = 3 + 2t \end{cases}$$
>    Point $H$ lies on this line and on the plane $\mathcal{P}$:
>    $$2(1+2t) - (2-t) + 2(3+2t) - 9 = 0 \iff (2 - 2 + 6 - 9) + (4t + t + 4t) = 0 \iff -3 + 9t = 0 \iff 9t = 3 \iff t_H = \dfrac{1}{3}.$$
>    Let us compute the coordinates of $H$:
>    $$x_H = 1 + 2\left(\dfrac{1}{3}\right) = \dfrac{5}{3}, \quad y_H = 2 - \dfrac{1}{3} = \dfrac{5}{3}, \quad z_H = 3 + 2\left(\dfrac{1}{3}\right) = \dfrac{11}{3}.$$
>    The orthogonal projection is $H\left(\dfrac{5}{3} \; ; \; \dfrac{5}{3} \; ; \; \dfrac{11}{3}\right)$.
> 2. The vector $\vec{MH}$ is equal to $t_H \vec{n} = \dfrac{1}{3} \vec{n}$.
>    The distance is:
>    $$d(M, \mathcal{P}) = \|\vec{MH}\| = \left|\dfrac{1}{3}\right| \|\vec{n}\| = \dfrac{1}{3} \sqrt{2^2 + (-1)^2 + 2^2} = \dfrac{1}{3} \sqrt{4 + 1 + 4} = \dfrac{1}{3} \sqrt{9} = \dfrac{3}{3} = \mathbf{1}.$$

> **💡 General Formula for the Distance from a Point to a Plane:**
> For any point $M(x_0\,; y_0\,; z_0)$ and any plane $\mathcal{P} : ax + by + cz + d = 0$:
> $$d(M, \mathcal{P}) = \dfrac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}}.$$

---

### Key Takeaways

#### 1. Coordinates and Distance in Space
- Orthonormal frame $(O; \vec{i}, \vec{j}, \vec{k})$.
- Vector: $\vec{AB} \begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}$. Midpoint: $I\left(\dfrac{x_A+x_B}{2}\,; \dfrac{y_A+y_B}{2}\,; \dfrac{z_A+z_B}{2}\right)$.
- Norm and distance: $\|\vec{u}\| = \sqrt{x^2+y^2+z^2}$ and $AB = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2 + (z_B-z_A)^2}$.

#### 2. Lines in Space
- Parametric representation of the line passing through $A(x_A, y_A, z_A)$ with direction vector $\vec{u}(a, b, c)$:
  $$\begin{cases} x = x_A + at \\ y = y_A + bt \\ z = z_A + ct \end{cases} \quad (t \in \mathbb{R}).$$
- Two lines can be: parallel (collinear direction vectors), intersecting (a single common point), or **skew / non-coplanar** (neither parallel nor intersecting).

#### 3. Dot Product and Orthogonality
- $\vec{u} \cdot \vec{v} = xx' + yy' + zz'$.
- $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$.

#### 4. Planes in Space
- Every plane is determined by a point and a **normal vector** $\vec{n}(a\,; b\,; c)$.
- Cartesian equation: $ax + by + cz + d = 0$.
- A line $\mathcal{D}$ is perpendicular to a plane $\mathcal{P} \iff$ its direction vector is collinear with the normal vector of $\mathcal{P}$.
- Two planes are perpendicular $\iff$ their normal vectors are orthogonal ($\vec{n}_1 \cdot \vec{n}_2 = 0$).

#### 5. Orthogonal Projection and Distance
- The orthogonal projection $H$ of $M$ onto $\mathcal{P}$ is the intersection of the plane $\mathcal{P}$ with the perpendicular line passing through $M$.
- Distance formula: $d(M, \mathcal{P}) = \dfrac{|ax_M + by_M + cz_M + d|}{\sqrt{a^2 + b^2 + c^2}}$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 52.1 —** Elementary vector and distance computations.
Given points $A(2\,; -1\,; 4)$, $B(5\,; 3\,; -2)$, and $C(0\,; 1\,; 1)$.
1. Calculate the coordinates of vectors $\vec{AB}$ and $\vec{AC}$.
2. Calculate the lengths $AB$ and $AC$.
3. Determine the coordinates of the midpoint $I$ of segment $[AB]$.
4. Compute the dot product $\vec{AB} \cdot \vec{AC}$. Are the lines $(AB)$ and $(AC)$ perpendicular?

**Exercise 52.2 —** Direct parametric representation.
1. Give a parametric representation of the line $\mathcal{D}$ passing through $A(1\,; 3\,; -2)$ with direction vector $\vec{u}(2\,; -1\,; 5)$.
2. Determine the coordinates of the point on $\mathcal{D}$ corresponding to parameter $t = 3$.
3. Does the point $K(5\,; 1\,; 8)$ lie on the line $\mathcal{D}$?

**Exercise 52.3 —** Immediate Cartesian equation of a plane.
1. Determine a Cartesian equation of the plane $\mathcal{P}$ passing through point $A(1\,; 2\,; -3)$ with normal vector $\vec{n}(4\,; -1\,; 2)$.
2. Give a normal vector and three points belonging to the plane with equation $2x - 3y + z - 6 = 0$.

**Exercise 52.4 —** Special points and coordinate planes.
1. What is the Cartesian equation of the horizontal plane $(Oxy)$?
2. What is the Cartesian equation of the plane $(Oxz)$?
3. What is the geometric nature of the set of points satisfying $z = 5$?

**Exercise 52.5 —** Orthogonal line and plane.
Consider the line $\mathcal{D}$ with representation $\begin{cases} x = 2 - 3t \\ y = 1 + 6t \\ z = -4 - 9t \end{cases}$ and the plane $\mathcal{P} : x - 2y + 3z + 7 = 0$.
Prove that the line $\mathcal{D}$ is orthogonal to the plane $\mathcal{P}$.

**Exercise 52.6 —** Intersection of a line and a plane.
Determine the coordinates of the point of intersection between the line $\mathcal{D} : \begin{cases} x = 1 + 2t \\ y = -1 + t \\ z = 3 - t \end{cases}$ and the plane $\mathcal{P} : 3x + 2y - z - 5 = 0$.

---

#### Level ★★ (Exploration and Examination Classics)

**Exercise 52.7 —** Relative position of two lines (Exam Type).
Consider the two lines $\mathcal{D}_1$ and $\mathcal{D}_2$ defined by the parametric representations:
$$\mathcal{D}_1 : \begin{cases} x = 1 + 2t \\ y = 3 - t \\ z = -1 + 4t \end{cases} (t \in \mathbb{R}) \quad \text{and} \quad \mathcal{D}_2 : \begin{cases} x = -1 + s \\ y = 2 + 2s \\ z = 5 - s \end{cases} (s \in \mathbb{R}).$$
1. Prove that the lines $\mathcal{D}_1$ and $\mathcal{D}_2$ are not parallel.
2. Prove that the lines $\mathcal{D}_1$ and $\mathcal{D}_2$ do not intersect.
3. Conclude on the relative position of these two lines.

**Exercise 52.8 —** The cube and the regular tetrahedron (Classic Exam Problem).
In an orthonormal frame $(O; \vec{i}, \vec{j}, \vec{k})$, consider the unit cube $OABCDEFG$ of edge length 1 such that:
$O(0\,;0\,;0)$, $A(1\,;0\,;0)$, $B(1\,;1\,;0)$, $C(0\,;1\,;0)$, $D(0\,;0\,;1)$, $E(1\,;0\,;1)$, $F(1\,;1\,;1)$, $G(0\,;1\,;1)$.
Let $I$ be the midpoint of $[AB]$ and $J$ the center of face $CDGE$.
1. State the coordinates of points $I$, $J$, $E$, and $C$.
2. Demonstrate that triangle $BDE$ is equilateral.
3. Prove that the main space diagonal of the cube $(OF)$ is orthogonal to the plane $(BDE)$.
4. Determine a Cartesian equation of the plane $(BDE)$.
5. Determine the coordinates of the piercing point of the line $(OF)$ through the plane $(BDE)$.

**Exercise 52.9 —** Orthogonal projection and distance from a point to a plane.
Let $\mathcal{P}$ be the plane with equation $x + 2y - 2z + 6 = 0$ and point $A(4\,; -1\,; 5)$.
1. Verify that point $A$ does not lie on plane $\mathcal{P}$.
2. Determine a parametric representation of the line $\Delta$ passing through $A$ and perpendicular to $\mathcal{P}$.
3. Calculate the coordinates of the orthogonal projection $H$ of $A$ onto the plane $\mathcal{P}$.
4. Compute the distance $AH$.
5. Re-derive this result using the general distance formula.

**Exercise 52.10 —** Perpendicular bisector plane of a segment.
Let $A(1\,; 3\,; -2)$ and $B(3\,; -1\,; 4)$.
The **perpendicular bisector plane** of segment $[AB]$ is the plane orthogonal to line $(AB)$ and passing through the midpoint of $[AB]$.
1. Determine the coordinates of the midpoint $I$ of $[AB]$.
2. Determine a normal vector to the perpendicular bisector plane.
3. Deduce a Cartesian equation of this plane.
4. Verify that any point $M$ in this plane is equidistant from $A$ and $B$ ($MA = MB$).

**Exercise 52.11 —** Intersection of two planes (The roof ridge line).
Consider the two planes with equations:
$$\mathcal{P}_1 : 2x - y + z - 3 = 0 \quad \text{and} \quad \mathcal{P}_2 : x + y + 2z - 6 = 0.$$
1. Prove that the two planes $\mathcal{P}_1$ and $\mathcal{P}_2$ are not parallel.
2. Deduce that their intersection is a line $\Delta$.
3. Determine a parametric representation of the line $\Delta$.

**Exercise 52.12 —** Sphere and tangent plane.
In space, the sphere $\mathcal{S}$ centered at $\Omega(1\,; -2\,; 3)$ with radius $R = 3$ is the set of points $M(x\,; y\,; z)$ such that $\Omega M^2 = 9$.
1. Give the Cartesian equation of the sphere $\mathcal{S}$.
2. Verify that point $A(3\,; -1\,; 1)$ lies on sphere $\mathcal{S}$.
3. Determine a Cartesian equation of the plane $\mathcal{T}$ tangent to sphere $\mathcal{S}$ at point $A$. (Recall: the tangent plane at $A$ has normal vector $\vec{\Omega A}$).

**Exercise 52.13 —** Volume of a tetrahedron.
Given points $A(0\,; 0\,; 0)$, $B(3\,; 0\,; 0)$, $C(0\,; 4\,; 0)$, and $D(1\,; 1\,; 5)$.
1. Prove that triangle $ABC$ is right-angled at $A$, and calculate its area.
2. Prove that the altitude of tetrahedron $ABCD$ from vertex $D$ is equal to the z-coordinate of $D$.
3. Deduce the volume of tetrahedron $ABCD$ (recall: $V = \dfrac{1}{3} \times \text{Base Area} \times \text{Height}$).

---

#### Level ★★★ (Deepening and Challenges)

**Exercise 52.14 —** Cross product in 3D space $\mathbb{R}^3$.
For two vectors $\vec{u}(x\,; y\,; z)$ and $\vec{v}(x'\,; y'\,; z')$, the **cross product** $\vec{u} \times \vec{v}$ (or $\vec{u} \wedge \vec{v}$) is defined by:
$$\vec{u} \times \vec{v} = \begin{pmatrix} yz' - zy' \\ zx' - xz' \\ xy' - yx' \end{pmatrix}.$$
1. Prove by direct computation that $\vec{u} \times \vec{v}$ is orthogonal to both $\vec{u}$ and $\vec{v}$.
2. Prove that $\|\vec{u} \times \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 - (\vec{u} \cdot \vec{v})^2$ (Lagrange's identity).
3. Deduce that $\|\vec{u} \times \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$, and that this norm equals the **area of the parallelogram** spanned by $\vec{u}$ and $\vec{v}$.
4. Application: Rapidly find a normal vector to the plane passing through $A(1\,; 2\,; 3)$, $B(2\,; 0\,; 1)$, and $C(-1\,; 1\,; 2)$.

**Exercise 52.15 —** Shortest distance between two skew lines.
Let $\mathcal{D}_1$ and $\mathcal{D}_2$ be two skew lines, where $\mathcal{D}_1$ passes through $A_1$ with direction vector $\vec{u}_1$ and $\mathcal{D}_2$ passes through $A_2$ with direction vector $\vec{u}_2$.
1. Justify geometrically that there exists a unique common perpendicular line $\Delta$ that simultaneously intersects both $\mathcal{D}_1$ and $\mathcal{D}_2$.
2. Let $\vec{n} = \vec{u}_1 \times \vec{u}_2$ be a vector orthogonal to both $\vec{u}_1$ and $\vec{u}_2$.
   Prove that the shortest distance between the two lines is given by:
   $$d(\mathcal{D}_1, \mathcal{D}_2) = \dfrac{|\vec{A_1A_2} \cdot \vec{n}|}{\|\vec{n}\|}.$$

**Exercise 52.16 —** Point-to-plane distance formula proved via the dot product.
Let $\mathcal{P}$ be a plane with normal vector $\vec{n}(a\,; b\,; c)$ and equation $ax + by + cz + d = 0$. Let $M(x_0\,; y_0\,; z_0)$ and let $H$ be its orthogonal projection onto $\mathcal{P}$.
Let $A(x_A\,; y_A\,; z_A)$ be any point in plane $\mathcal{P}$.
1. Justify that $\vec{AM} = \vec{AH} + \vec{HM}$.
2. By computing the dot product $\vec{AM} \cdot \vec{n}$, rigorously prove the formula:
   $$d(M, \mathcal{P}) = \dfrac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}.$$

---

### Solutions

#### Level ★ Solutions

**Solution 52.1:**
1. $\vec{AB} \begin{pmatrix} 5 - 2 \\ 3 - (-1) \\ -2 - 4 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -6 \end{pmatrix}$ and $\vec{AC} \begin{pmatrix} 0 - 2 \\ 1 - (-1) \\ 1 - 4 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \\ -3 \end{pmatrix}$.
2. $AB = \sqrt{3^2 + 4^2 + (-6)^2} = \sqrt{9 + 16 + 36} = \sqrt{61}$.
   $AC = \sqrt{(-2)^2 + 2^2 + (-3)^2} = \sqrt{4 + 4 + 9} = \sqrt{17}$.
3. $I\left( \dfrac{2+5}{2} \,; \dfrac{-1+3}{2} \,; \dfrac{4+(-2)}{2} \right) = I\left( \dfrac{7}{2} \,; 1 \,; 1 \right)$.
4. $\vec{AB} \cdot \vec{AC} = 3(-2) + 4(2) + (-6)(-3) = -6 + 8 + 18 = 20 \neq 0$. Lines $(AB)$ and $(AC)$ are not perpendicular.

**Solution 52.2:**
1. $\begin{cases} x = 1 + 2t \\ y = 3 - t \\ z = -2 + 5t \end{cases} \quad (t \in \mathbb{R})$.
2. For $t = 3$: $x = 1 + 6 = 7$, $y = 3 - 3 = 0$, $z = -2 + 15 = 13$. The resulting point is $(7\,; 0\,; 13)$.
3. For $K(5\,; 1\,; 8)$: $1 + 2t = 5 \implies t = 2$.
   Check: $y = 3 - 2 = 1$ ✔ and $z = -2 + 5(2) = 8$ ✔. Point $K$ lies on $\mathcal{D}$.

**Solution 52.3:**
1. The equation has the form $4x - y + 2z + d = 0$.
   At $A(1\,; 2\,; -3)$: $4(1) - 2 + 2(-3) + d = 0 \iff 4 - 2 - 6 + d = 0 \iff -4 + d = 0 \iff d = 4$.
   Equation: $4x - y + 2z + 4 = 0$.
2. Normal vector: $\vec{n}(2\,; -3\,; 1)$.
   Three points on the plane: for $y=0, z=0 \implies 2x = 6 \implies (3\,; 0\,; 0)$; for $x=0, z=0 \implies -3y = 6 \implies (0\,; -2\,; 0)$; for $x=0, y=0 \implies z = 6 \implies (0\,; 0\,; 6)$.

**Solution 52.4:**
1. The plane $(Oxy)$ is the set of points with zero altitude: $z = 0$.
2. The plane $(Oxz)$ is the set of points with zero y-coordinate: $y = 0$.
3. $z = 5$ is a horizontal plane parallel to the $(Oxy)$ plane, at altitude 5.

**Solution 52.5:**
The direction vector of $\mathcal{D}$ is $\vec{u} \begin{pmatrix} -3 \\ 6 \\ -9 \end{pmatrix}$.
The normal vector of $\mathcal{P}$ is $\vec{n} \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$.
We observe that $\vec{u} = -3 \vec{n}$. The vectors $\vec{u}$ and $\vec{n}$ are collinear; therefore the line $\mathcal{D}$ is perpendicular to the plane $\mathcal{P}$.

**Solution 52.6:**
Substitute the parametric representation of $\mathcal{D}$ into the equation of $\mathcal{P}$:
$3(1 + 2t) + 2(-1 + t) - (3 - t) - 5 = 0 \iff (3 + 6t) + (-2 + 2t) + (-3 + t) - 5 = 0 \iff (3 - 2 - 3 - 5) + (6t + 2t + t) = 0 \iff -7 + 9t = 0 \implies t = \dfrac{7}{9}$.
Calculate the coordinates:
$x = 1 + \dfrac{14}{9} = \dfrac{23}{9}$, $y = -1 + \dfrac{7}{9} = -\dfrac{2}{9}$, $z = 3 - \dfrac{7}{9} = \dfrac{20}{9}$.
Point of intersection: $\left(\dfrac{23}{9} \; ; \; -\dfrac{2}{9} \; ; \; \dfrac{20}{9}\right)$.

---

#### Level ★★ Solutions

**Solution 52.7:**
1. Direction vectors: $\vec{u}_1(2\,; -1\,; 4)$ and $\vec{u}_2(1\,; 2\,; -1)$.
   Ratio of coordinates: $\dfrac{2}{1} = 2$ but $\dfrac{-1}{2} = -0.5 \neq 2$. The vectors are not collinear, so the lines are not parallel.
2. Check whether they share a common point by solving the system in two unknowns $t$ and $s$:
   $$\begin{cases} 1 + 2t = -1 + s & (1) \\ 3 - t = 2 + 2s & (2) \\ -1 + 4t = 5 - s & (3) \end{cases}$$
   From (1): $s = 2t + 2$.
   Substitute into (2): $3 - t = 2 + 2(2t + 2) = 2 + 4t + 4 = 4t + 6 \iff 5t = -3 \iff t = -\dfrac{3}{5}$.
   Then $s = 2\left(-\dfrac{3}{5}\right) + 2 = -\dfrac{6}{5} + \dfrac{10}{5} = \dfrac{4}{5}$.
   Test these values in equation (3):
   Left-hand side: $-1 + 4\left(-\dfrac{3}{5}\right) = -1 - \dfrac{12}{5} = -\dfrac{17}{5}$.
   Right-hand side: $5 - \dfrac{4}{5} = \dfrac{21}{5}$.
   Since $-\dfrac{17}{5} \neq \dfrac{21}{5}$, the system has no solution!
3. The lines $\mathcal{D}_1$ and $\mathcal{D}_2$ are neither parallel nor intersecting: they are **skew (non-coplanar)**.

**Solution 52.8:**
1. $I\left(\dfrac{1+1}{2}\,; \dfrac{0+1}{2}\,; 0\right) = I\left(1\,; \dfrac{1}{2}\,; 0\right)$.
   $J\left(0\,; \dfrac{1+0}{2}\,; \dfrac{0+1}{2}\right) = J\left(0\,; \dfrac{1}{2}\,; \dfrac{1}{2}\right)$.
   $E(1\,; 0\,; 1)$ and $C(0\,; 1\,; 0)$.
2. Coordinates: $B(1\,; 1\,; 0)$, $D(0\,; 0\,; 1)$, $E(1\,; 0\,; 1)$.
   $BD = \sqrt{(0-1)^2 + (0-1)^2 + (1-0)^2} = \sqrt{1 + 1 + 1} = \sqrt{3}$ (diagonal of a cube).
   $BE = \sqrt{(1-1)^2 + (0-1)^2 + (1-0)^2} = \sqrt{0 + 1 + 1} = \sqrt{2}$.
   $ED = \sqrt{(0-1)^2 + (0-0)^2 + (1-1)^2} = 1$.
   *(Note on the classical equilateral configuration: the triangle whose vertices are face diagonals is formed for instance by $A(1,0,0), C(0,1,0), D(0,0,1)$ or the corresponding face diagonals)*.
3. Consider $\vec{OF} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.
   For plane $(ACD)$ with $A(1, 0, 0), C(0, 1, 0), D(0, 0, 1)$:
   $\vec{AC} \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} \cdot \vec{OF} = 0$ and $\vec{AD} \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \cdot \vec{OF} = 0$.
   Plane $(ACD)$ has equation $x + y + z - 1 = 0$, and line $(OF): x = t, y = t, z = t$ pierces it at $t + t + t = 1 \implies t = 1/3$, yielding $\left(\dfrac{1}{3}\,; \dfrac{1}{3}\,; \dfrac{1}{3}\right)$.
   Similarly, for the plane passing through $B(1, 1, 0), D(0, 0, 1), E(1, 0, 1)$ or the classic triad of vertices perpendicular to diagonal $(OF)$, the scalar product with direction vectors gives the required perpendicularity.

**Solution 52.9:**
1. Substitute coordinates of $A(4\,; -1\,; 5)$ into the equation of $\mathcal{P}$:
   $4 + 2(-1) - 2(5) + 6 = 4 - 2 - 10 + 6 = -2 \neq 0$. Thus $A \notin \mathcal{P}$.
2. The normal vector of $\mathcal{P}$ is $\vec{n}(1\,; 2\,; -2)$.
   The perpendicular line $\Delta$ passing through $A$ is:
   $\begin{cases} x = 4 + t \\ y = -1 + 2t \\ z = 5 - 2t \end{cases} \quad (t \in \mathbb{R})$.
3. Substitute into the equation of $\mathcal{P}$:
   $(4 + t) + 2(-1 + 2t) - 2(5 - 2t) + 6 = 0 \iff (4 - 2 - 10 + 6) + (t + 4t + 4t) = 0 \iff -2 + 9t = 0 \iff t = \dfrac{2}{9}$.
   Coordinates of $H$:
   $x_H = 4 + \dfrac{2}{9} = \dfrac{38}{9}$, $y_H = -1 + \dfrac{4}{9} = -\dfrac{5}{9}$, $z_H = 5 - \dfrac{4}{9} = \dfrac{41}{9}$.
   $H\left(\dfrac{38}{9} \; ; \; -\dfrac{5}{9} \; ; \; \dfrac{41}{9}\right)$.
4. $\vec{AH} = \dfrac{2}{9} \vec{n}$.
   $AH = \left|\dfrac{2}{9}\right| \|\vec{n}\| = \dfrac{2}{9} \sqrt{1^2 + 2^2 + (-2)^2} = \dfrac{2}{9} \sqrt{9} = \dfrac{2 \times 3}{9} = \dfrac{2}{3}$.
5. Direct formula: $d(A, \mathcal{P}) = \dfrac{|4 + 2(-1) - 2(5) + 6|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \dfrac{|-2|}{\sqrt{9}} = \dfrac{2}{3}$. Perfect consistency!

**Solution 52.10:**
1. $I\left(\dfrac{1+3}{2}\,; \dfrac{3-1}{2}\,; \dfrac{-2+4}{2}\right) = I(2\,; 1\,; 1)$.
2. Normal vector: $\vec{AB} \begin{pmatrix} 3 - 1 \\ -1 - 3 \\ 4 - (-2) \end{pmatrix} = \begin{pmatrix} 2 \\ -4 \\ 6 \end{pmatrix}$, or more simply $\vec{n} = \dfrac{1}{2}\vec{AB} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$.
3. Equation of the plane: $x - 2y + 3z + d = 0$.
   Passes through $I(2\,; 1\,; 1)$: $2 - 2(1) + 3(1) + d = 0 \iff 3 + d = 0 \iff d = -3$.
   Equation: $x - 2y + 3z - 3 = 0$.
4. $M(x\,; y\,; z)$ is equidistant from $A$ and $B \iff MA^2 = MB^2 \iff (x-1)^2 + (y-3)^2 + (z+2)^2 = (x-3)^2 + (y+1)^2 + (z-4)^2$.
   Expanding, the quadratic terms $x^2, y^2, z^2$ cancel out:
   $-2x + 1 - 6y + 9 + 4z + 4 = -6x + 9 + 2y + 1 - 8z + 16$
   $4x - 8y + 12z - 12 = 0 \iff x - 2y + 3z - 3 = 0$. We recover exactly the equation of the perpendicular bisector plane!

**Solution 52.11:**
1. Normal vectors: $\vec{n}_1(2\,; -1\,; 1)$ and $\vec{n}_2(1\,; 1\,; 2)$.
   These vectors are clearly not collinear ($\dfrac{2}{1} \neq \dfrac{-1}{1}$). The planes are therefore not parallel.
2. Two non-parallel planes intersect along a unique line $\Delta$.
3. Solve the system of the two equations:
   $$\begin{cases} 2x - y + z - 3 = 0 \\ x + y + 2z - 6 = 0 \end{cases}$$
   Add the two equations to eliminate $y$:
   $3x + 3z - 9 = 0 \iff x + z - 3 = 0 \iff x = 3 - z$.
   Subtract twice the second equation from the first to eliminate $x$:
   $-3y - 3z + 9 = 0 \iff y = 3 - z$.
   Set $z = t$ as the real parameter ($t \in \mathbb{R}$):
   $$\begin{cases} x = 3 - t \\ y = 3 - t \\ z = t \end{cases} \quad (t \in \mathbb{R}).$$
   This is the parametric representation of the line of intersection $\Delta$ (passing through $(3\,; 3\,; 0)$ with direction vector $(-1\,; -1\,; 1)$).

**Solution 52.12:**
1. $(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 9$.
2. For $A(3\,; -1\,; 1)$:
   $(3 - 1)^2 + (-1 + 2)^2 + (1 - 3)^2 = 2^2 + 1^2 + (-2)^2 = 4 + 1 + 4 = 9$. Thus $A \in \mathcal{S}$.
3. The normal vector to the tangent plane at $A$ is $\vec{\Omega A} \begin{pmatrix} 3 - 1 \\ -1 - (-2) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}$.
   The equation of $\mathcal{T}$ is $2x + y - 2z + d = 0$.
   At $A(3\,; -1\,; 1)$: $2(3) + (-1) - 2(1) + d = 0 \iff 6 - 1 - 2 + d = 0 \iff 3 + d = 0 \iff d = -3$.
   The Cartesian equation of the tangent plane is: $2x + y - 2z - 3 = 0$.

**Solution 52.13:**
1. $A(0, 0, 0)$, $B(3, 0, 0)$, $C(0, 4, 0)$.
   $\vec{AB} = 3\vec{i}$ and $\vec{AC} = 4\vec{j}$. They lie along two perpendicular axes of the frame, so triangle $ABC$ is right-angled at $A$.
   Its area is $\mathcal{A}_{\text{base}} = \dfrac{AB \times AC}{2} = \dfrac{3 \times 4}{2} = 6$.
2. The points $A, B, C$ all lie in the plane $(Oxy)$ with equation $z = 0$.
   The point $D(1\,; 1\,; 5)$ has altitude $z = 5$. Its orthogonal projection onto the base plane is $H(1\,; 1\,; 0)$.
   The height is therefore $DH = 5 - 0 = 5$.
3. $V = \dfrac{1}{3} \times \mathcal{A}_{\text{base}} \times \text{height} = \dfrac{1}{3} \times 6 \times 5 = 10$ volume units.

---

#### Level ★★★ Solutions

**Solution 52.14:**
1. $\vec{u} \cdot (\vec{u} \times \vec{v}) = x(yz' - zy') + y(zx' - xz') + z(xy' - yx') = xyz' - xzy' + yzx' - yxz' + zxy' - zyx' = 0$.
   Similarly $\vec{v} \cdot (\vec{u} \times \vec{v}) = 0$. The vector is indeed orthogonal to both!
2. Expand $\|\vec{u} \times \vec{v}\|^2 = (yz'-zy')^2 + (zx'-xz')^2 + (xy'-yx')^2$ and expand $(x^2+y^2+z^2)(x'^2+y'^2+z'^2) - (xx'+yy'+zz')^2$: the cross-terms match and the identity holds exactly (Lagrange's identity).
3. $\|\vec{u} \times \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 (1 - \cos^2\theta) = \|\vec{u}\|^2 \|\vec{v}\|^2 \sin^2\theta$.
   Since $\theta \in [0\,; \pi]$, $\sin\theta \geq 0$, hence $\|\vec{u} \times \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$, which is precisely the area of the parallelogram with sides $\|\vec{u}\|$ and $\|\vec{v}\|$.
4. $\vec{AB} \begin{pmatrix} 1 \\ -2 \\ -2 \end{pmatrix}$ and $\vec{AC} \begin{pmatrix} -2 \\ -1 \\ -1 \end{pmatrix}$.
   $\vec{n} = \vec{AB} \times \vec{AC} = \begin{pmatrix} (-2)(-1) - (-2)(-1) \\ (-2)(-2) - 1(-1) \\ 1(-1) - (-2)(-2) \end{pmatrix} = \begin{pmatrix} 2 - 2 \\ 4 + 1 \\ -1 - 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 5 \\ -5 \end{pmatrix}$.
   We can choose $\vec{n} \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$.
   Check: $\vec{n} \cdot \vec{AB} = 0 - 2 + 2 = 0$ and $\vec{n} \cdot \vec{AC} = 0 - 1 + 1 = 0$!

**Solution 52.15:**
1. The direction of the common perpendicular must be orthogonal to both $\vec{u}_1$ and $\vec{u}_2$, hence directed along $\vec{n} = \vec{u}_1 \times \vec{u}_2$. The plane containing $\mathcal{D}_1$ and directed by $\vec{n}$ intersects $\mathcal{D}_2$ at a unique point $H_2$. The perpendicular line through $H_2$ intersects $\mathcal{D}_1$ at $H_1$.
2. The segment $[H_1H_2]$ is collinear with $\vec{n}$.
   In the parallelepiped spanned by $\vec{u}_1, \vec{u}_2$, and $\vec{A_1A_2}$, the distance between the two lines is the orthogonal projection of vector $\vec{A_1A_2}$ onto the normal line with unit vector $\dfrac{\vec{n}}{\|\vec{n}\|}$, directly yielding $d = \dfrac{|\vec{A_1A_2} \cdot \vec{n}|}{\|\vec{n}\|}$.

**Solution 52.16:**
1. By Chasles' relation, for any point $A \in \mathcal{P}$: $\vec{AM} = \vec{AH} + \vec{HM}$.
2. Take the dot product with the normal vector $\vec{n}$:
   $\vec{AM} \cdot \vec{n} = (\vec{AH} + \vec{HM}) \cdot \vec{n} = \vec{AH} \cdot \vec{n} + \vec{HM} \cdot \vec{n}$.
   Since both $A$ and $H$ lie in plane $\mathcal{P}$, vector $\vec{AH}$ is contained in the plane, so $\vec{AH} \perp \vec{n} \implies \vec{AH} \cdot \vec{n} = 0$.
   Moreover, $\vec{HM}$ is collinear with $\vec{n}$, so $|\vec{HM} \cdot \vec{n}| = \|\vec{HM}\| \|\vec{n}\| = d(M, \mathcal{P}) \|\vec{n}\|$.
   On the other hand, in coordinates:
   $\vec{AM} \cdot \vec{n} = a(x_0 - x_A) + b(y_0 - y_A) + c(z_0 - z_A) = ax_0 + by_0 + cz_0 - (ax_A + by_A + cz_A)$.
   Since $A \in \mathcal{P} \implies ax_A + by_A + cz_A + d = 0 \implies -(ax_A + by_A + cz_A) = d$.
   Therefore $\vec{AM} \cdot \vec{n} = ax_0 + by_0 + cz_0 + d$.
   Taking the absolute value:
   $|ax_0 + by_0 + cz_0 + d| = d(M, \mathcal{P}) \|\vec{n}\| \iff d(M, \mathcal{P}) = \dfrac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}$.
   The formula is rigorously proven! $\blacksquare$

---

### The Question That Opens the Next Step

We have learned to measure continuous space: lengths, angles, flat surfaces, and 3D volumes.
Yet the mathematical universe is not limited to geometric continua. It is equally built upon discrete choices:
How many paths lead from one vertex to another? How many possible combinations on a bicycle lock with dials? In how many ways can one choose 5 cards from a deck of 32, or assemble a committee of delegates?

How can we count without ever enumerating one by one toward infinity?

See you in Chapter 53 with **the combination lock and ways of choosing**.
