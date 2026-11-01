# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 33: The Line of Sight

> *“A straight line is not merely an ink trace drawn with a ruler: it is an infinite laser beam traversing the universe, a line of sight swept by a watchman's gaze. To confine this infinity of points into an algebraic formula, two numbers suffice: an anchor along the vertical axis and a climbing slope. Then, the crossing of two paths becomes the unfolding of an equation.”*

---

### What You Are About to Discover

- How a line is born from an anchor point and a **direction vector** that sets its heading.
- The general **Cartesian equation** $ax + by + c = 0$, and why the vector $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ serves as its compass needle.
- The **slope-intercept form** (or reduced equation) $y = mx + p$: the physical meaning of the **slope** $m$ (gradient) and the **$y$-intercept** $p$.
- The special case of vertical lines with equation $x = k$.
- The three possible fates of two meeting lines: intersecting at a unique point, strictly parallel, or coincident.
- Solving **systems of two linear equations in two variables** algebraically and graphically via substitution and linear combination (elimination).

---

### 1. The Problem: The Watchtower and the Ship in the Fog

A solitary watchtower stands atop a craggy cliff overlooking the ocean. Night has fallen, thick fog shrouds the bay, and two ships navigate blindly.

The lighthouse keeper monitors a Cartesian radar screen:
- The merchant vessel *L'Espérance* is presently located at coordinates $A(2\,; 3)$ and maintains a steady heading guided by velocity vector $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
- A rescue frigate *La Vigilante* is reported at point $B(-1\,; 8)$, steaming in a straight path along vector $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

```
                 y ▲
                   │           La Vigilante B(-1, 8)
                 8 ┼           o
                   │            \   v(1, -1)
                   │             ▼\
                   │               \
                   │                 \   Intersection point?
                 3 ┼               o───►o──────────────────►
                   │            A(2,3)   \ u(2, 1)
                   │                      \   L'Espérance
                 O ┼───────┼───────┼───────┼────────► x
                  -1       0       2
```

The port commander poses two urgent questions:
1. *Do these two vessels risk collision—meaning, do their paths cross at a specific point on the water?*
2. *If so, what are the exact coordinates of the intersection point?*

To answer, drawing on graph paper is unreliable: a blunt pencil lead or a slightly warped scale could be off by hundreds of meters. We need an infallible algebraic method capable of translating an infinite line into an equation solvable with absolute precision.

---

### 2. Heading and Path: The Direction Vector

#### 2.1 Setting the Direction of a Line

A line in the plane is entirely determined by:
- either **two distinct points** $A$ and $B$ (through two points passes a unique straight line);
- or **one anchor point** $A$ and **one non-zero vector** prescribing its direction.

> **📐 Definition — Direction Vector.**
> Let $\mathcal{D}$ be a line in the plane. Any non-zero vector $\vec{u}$ having the same direction as line $\mathcal{D}$ is called a **direction vector** of $\mathcal{D}$.
> If $A$ and $B$ are two distinct points on $\mathcal{D}$, then the vector $\vec{AB}$ is a direction vector of $\mathcal{D}$.

```
                             D
                           /
                         /  u (direction vector)
                       /──►
                     /
                   o A
                 /
               /
```

> **💡 Did You Know? A line possesses infinitely many direction vectors!**
> If $\vec{u}$ is a direction vector of line $\mathcal{D}$, then for any non-zero real number $k$, the vector $k\vec{u}$ shares the same direction: it is therefore also a direction vector of $\mathcal{D}$. Twice as long, one third the length, or pointing in reverse, it still lies along the very same line.

#### 2.2 Vector Characterization of a Line

A point $M(x\,; y)$ belongs to the line $\mathcal{D}$ passing through $A(x_A\,; y_A)$ with direction vector $\vec{u}$ if and only if the displacement from $A$ to $M$ follows this exact same heading:
$$M \in \mathcal{D} \iff \vec{AM} \text{ and } \vec{u} \text{ are collinear}.$$

From the preceding chapter, two vectors are collinear if and only if their determinant vanishes:
$$M \in \mathcal{D} \iff \det(\vec{AM}, \vec{u}) = 0.$$

This single, elegant condition generates all linear equations!

---

### 3. The Cartesian Equation of a Line

#### 3.1 The General Form $ax + by + c = 0$

> **📐 Fundamental Theorem — Cartesian Equation.**
> 1. Every straight line $\mathcal{D}$ in the plane admits an equation of the form:
>    $$ax + by + c = 0$$
>    where $a, b, c$ are real numbers with $(a, b) \neq (0, 0)$ (that is, $a$ and $b$ are not both zero).
> 2. Conversely, every equation of the form $ax + by + c = 0$ with $(a, b) \neq (0, 0)$ represents a straight line.
> 3. The vector $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ is a **direction vector** of this line.

> **✍️ Proof (Core Curriculum) — From Collinearity to the Cartesian Equation.**
> Let $\mathcal{D}$ be the line passing through $A(x_A\,; y_A)$ with non-zero direction vector $\vec{u}\begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$.
> Let $M(x\,; y)$ be an arbitrary point in the plane.
> Vector $\vec{AM}$ has coordinates:
> $$\vec{AM}\begin{pmatrix} x - x_A \\ y - y_A \end{pmatrix}.$$
> Point $M$ belongs to $\mathcal{D}$ if and only if $\vec{AM}$ and $\vec{u}$ are collinear:
> $$\det(\vec{AM}, \vec{u}) = 0 \iff (x - x_A)u_2 - (y - y_A)u_1 = 0.$$
> Expanding:
> $$u_2 x - u_1 y + (-u_2 x_A + u_1 y_A) = 0.$$
> Let us set:
> $$a = u_2, \quad b = -u_1, \quad c = -u_2 x_A + u_1 y_A.$$
> Since $\vec{u} \neq \vec{0}$, the pair $(u_1, u_2) \neq (0, 0)$, hence $(a, b) \neq (0, 0)$.
> The identity becomes:
> $$ax + by + c = 0.$$
> Furthermore, vector $\vec{u}$ has coordinates $\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} -b \\ a \end{pmatrix}$. This is indeed a direction vector of the line. $\blacksquare$

> **⚠️ Pitfall Warning! Cartesian equations are not unique.**
> If $2x - 3y + 5 = 0$ is the equation of a line, then multiplying each term by $2$ gives $4x - 6y + 10 = 0$, which describes **the exact same line**!
> Two equations $ax + by + c = 0$ and $a'x + b'y + c' = 0$ represent the same line if and only if their coefficients are proportional: there exists a non-zero real scalar $k$ such that $a' = ka$, $b' = kb$, and $c' = kc$.

---

### 4. Slope-Intercept Form: The Gradient and the $y$-Intercept

While the general form $ax + by + c = 0$ is universally applicable, for graphing and physical intuition mathematicians often prefer expressing $y$ explicitly in terms of $x$.

#### 4.1 Two Categories of Lines

Isolate the $y$-term in the Cartesian equation:
$$by = -ax - c.$$

Two cases arise:

##### Case 1: $b \neq 0$ (the line is non-vertical)
We can divide through by $b$:
$$y = -\frac{a}{b}x - \frac{c}{b}.$$
Setting $m = -\frac{a}{b}$ and $p = -\frac{c}{b}$, the equation takes the canonical form:
$$\boxed{y = mx + p}$$
This is the **slope-intercept form** (or reduced equation) of the line.

- **$m$ is the slope** (gradient, or *coefficient directeur*).
- **$p$ is the $y$-intercept** (ordonnée à l'origine): it is the vertical coordinate where the line crosses the $y$-axis $(Oy)$ (setting $x = 0$ yields $y = m(0) + p = p$). The point $(0\,; p)$ lies on the line.

```
                    y ▲
                      │            /
                      │          /
                      │        /
                    p ┼──────o             Run = 1
                      │     /│             Rise = m
                      │    / │ m
                      │   /  │
                      │  o───┴──
                      │  │ 1
                    O ┼──┴────────────► x
```

##### Case 2: $b = 0$ (the line is vertical)
The equation reduces to $ax + c = 0$. Since $(a, b) \neq (0, 0)$ and $b = 0$, we must have $a \neq 0$.
We deduce:
$$x = -\frac{c}{a} = k.$$
Every point on the line shares the **same $x$-coordinate** $k$. The line is parallel to the $y$-axis $(Oy)$. Its slope is undefined (“infinite”), and it cannot be written in the form $y = mx + p$. Its direction vector is strictly vertical, such as $\vec{j}\begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

#### 4.2 The Geometric Meaning of Slope $m$

> **📐 Fundamental Property — Calculating the Slope.**
> Let $A(x_A\,; y_A)$ and $B(x_B\,; y_B)$ be two distinct points on a non-vertical line ($x_A \neq x_B$).
> The slope $m$ is given by:
> $$m = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x} = \frac{\text{rise}}{\text{run}}.$$

**Physical Intuition:**
$\Delta y$ represents vertical elevation change and $\Delta x$ represents horizontal advance.
- If $m > 0$: the line “climbs” from left to right. The associated affine function is strictly increasing.
- If $m < 0$: the line “descends” from left to right. The associated affine function is strictly decreasing.
- If $m = 0$: the equation becomes $y = p$. The line is perfectly **horizontal**, parallel to the $x$-axis.
- An immediate direction vector for a line with equation $y = mx + p$ is $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$. Advancing by $1$ unit horizontally produces a vertical change of $m$ units.

---

### 5. Standard Techniques: Construction and Identification

#### 5.1 Graphing a Line Accurately

Two reliable methods:
1. **The Two-Point Method:** Choose two simple values for $x$ (frequently $x = 0$ and $x = 1$ or $x = 2$), compute the corresponding $y$-values, plot both points, and connect them with a straightedge.
2. **The Slope-Intercept Method:** Plot the intercept $(0\,; p)$ on the vertical axis. From there, move $1$ unit to the right, then move vertically by $m$ units (upward if $m > 0$, downward if $m < 0$). Mark the second point and draw the line.

#### 5.2 Finding the Equation of a Line

- **Case A: Given two points $A(x_A\,; y_A)$ and $B(x_B\,; y_B)$ with $x_A \neq x_B$.**
  1. Compute the slope: $m = \frac{y_B - y_A}{x_B - x_A}$.
  2. The equation is $y = mx + p$. To find $p$, use the condition that $A \in \mathcal{D}$:
     $$y_A = m x_A + p \implies p = y_A - m x_A.$$

- **Case B: Given a point $A(x_A\,; y_A)$ and a direction vector $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$.**
  1. Write down the general Cartesian template: $ax + by + c = 0$.
  2. Substitute the coordinates of $A$ into the equation to determine constant $c$:
     $$a x_A + b y_A + c = 0 \implies c = -a x_A - b y_A.$$

---

### 6. Relative Positions of Two Lines and Linear Systems

Consider two lines in the plane: $\mathcal{D} : ax + by + c = 0$ and $\mathcal{D}' : a'x + b'y + c' = 0$, with direction vectors $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$ and $\vec{u}'\begin{pmatrix} -b' \\ a' \end{pmatrix}$ respectively.

#### 6.1 The Three Configurations

```
   Intersecting Lines          Strictly Parallel Lines            Coincident Lines
          /  /                            /     /                        ///////
         /  /                            /     /                        ///////
        /  X  (one point)               /     /   (no point)           /////// (infinitely many)
       /  /  \                         /     /                        ///////
```

1. **Intersecting Lines:** Their direction vectors are not collinear:
   $$\det(\vec{u}, \vec{u}') \neq 0 \iff (-b)(a') - (a)(-b') \neq 0 \iff ab' - a'b \neq 0.$$
   For non-vertical lines: $m \neq m'$.
   They meet at a **single, unique point**.

2. **Strictly Parallel Lines:** Their direction vectors are collinear ($ab' - a'b = 0$, so $m = m'$), but their intercepts differ ($p \neq p'$).
   Their intersection is empty: $\mathcal{D} \cap \mathcal{D}' = \varnothing$.

3. **Coincident (Identical) Lines:** Their direction vectors are collinear and they share at least one point (hence $m = m'$ and $p = p'$). Every point is shared: $\mathcal{D} = \mathcal{D}'$.

#### 6.2 Solving a System of Two Linear Equations in Two Variables

Finding where two lines intersect is equivalent to finding the pair $(x\,; y)$ satisfying both equations simultaneously:
$$\begin{cases} ax + by = e \\ cx + dy = f \end{cases}$$

Two primary algebraic techniques exist:

##### Method 1: Substitution
Isolate one unknown (the one with the simplest coefficient, preferably $1$ or $-1$) in one equation, then substitute its expression into the second equation. This reduces the problem to a single linear equation in one unknown.

##### Method 2: Elimination (Linear Combination)
Multiply one or both equations by suitable non-zero constants so that the coefficients of one variable (say $x$) become exact opposites. Adding the two resulting equations cancels $x$ completely!

---

### 7. Detailed Worked Examples

> **Worked Example 1 — Readdressing the Port Problem: Ship Collision.**
> Recap of the data:
> - *L'Espérance* departs $A(2\,; 3)$ along $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
> - *La Vigilante* departs $B(-1\,; 8)$ along $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
> 1. Determine a Cartesian equation of trajectory $\mathcal{D}_1$ of *L'Espérance*.
> 2. Determine a Cartesian equation of trajectory $\mathcal{D}_2$ of *La Vigilante*.
> 3. Determine whether their paths intersect and calculate intersection coordinates $I$.
>
> **Solution:**
> 1. For $\mathcal{D}_1$, $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ is a direction vector. Since $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$, we choose $a = 1$ and $b = -2$.
>    The equation has template $1x - 2y + c = 0$.
>    $A(2\,; 3) \in \mathcal{D}_1 \implies 2 - 2(3) + c = 0 \implies 2 - 6 + c = 0 \implies c = 4$.
>    Thus $\mathcal{D}_1 : x - 2y + 4 = 0$ (or in slope-intercept form: $y = \frac{1}{2}x + 2$).
>
> 2. For $\mathcal{D}_2$, $\vec{v}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ is a direction vector. We can choose $a = 1, b = 1$ (since $\begin{pmatrix} -1 \\ 1 \end{pmatrix} = -\vec{v}$).
>    The equation has template $x + y + c' = 0$.
>    $B(-1\,; 8) \in \mathcal{D}_2 \implies -1 + 8 + c' = 0 \implies 7 + c' = 0 \implies c' = -7$.
>    Thus $\mathcal{D}_2 : x + y - 7 = 0$ (or in slope-intercept form: $y = -x + 7$).
>
> 3. Compare slopes: $m_1 = \frac{1}{2}$ and $m_2 = -1$.
>    Since $m_1 \neq m_2$, the lines intersect at a unique point $I$.
>    Solve the system:
>    $$\begin{cases} y = \frac{1}{2}x + 2 \\ y = -x + 7 \end{cases}$$
>    Equating both expressions for $y$:
>    $$\frac{1}{2}x + 2 = -x + 7 \iff \frac{1}{2}x + x = 7 - 2 \iff \frac{3}{2}x = 5 \iff x = \frac{10}{3}.$$
>    Calculate $y$:
>    $$y = -\frac{10}{3} + 7 = -\frac{10}{3} + \frac{21}{3} = \frac{11}{3}.$$
>    The trajectories intersect at coordinates $I\left(\frac{10}{3} \,;\, \frac{11}{3}\right)$.

> **Worked Example 2 — Equation of a Line Through Two Points.**
> Given $E(-3\,; 5)$ and $F(1\,; -3)$.
> Find the slope-intercept equation of line $(EF)$.
>
> **Solution:**
> Check if vertical: $x_E = -3$ and $x_F = 1$. Since $x_E \neq x_F$, it is non-vertical.
> 1. Calculate slope $m$:
>    $$m = \frac{y_F - y_E}{x_F - x_E} = \frac{-3 - 5}{1 - (-3)} = \frac{-8}{4} = -2.$$
> 2. Calculate intercept $p$:
>    The equation is $y = -2x + p$.
>    Since $F(1\,; -3)$ lies on the line:
>    $$-3 = -2(1) + p \implies -3 = -2 + p \implies p = -1.$$
> The slope-intercept equation is $\boxed{y = -2x - 1}$.
> *(Verification with $E$: $-2(-3) - 1 = 6 - 1 = 5 = y_E$. Matches!)*

> **Worked Example 3 — Solving a System via Elimination.**
> Solve in $\mathbb{R}^2$ the system:
> $$\begin{cases} 3x + 4y = 11 \quad (L_1) \\ 5x - 2y = 40 \quad (L_2) \end{cases}$$
>
> **Solution:**
> Observe the $y$-coefficients: $+4$ in $L_1$ and $-2$ in $L_2$.
> Multiplying $L_2$ by $2$ produces $-4$, the exact opposite of $+4$!
> Multiply $L_2$ by $2$:
> $$2 \times (5x - 2y) = 2 \times 40 \iff 10x - 4y = 80 \quad (L'_2).$$
> Add $L_1$ and $L'_2$ term by term:
> $$(3x + 4y) + (10x - 4y) = 11 + 80 \iff 13x = 91 \iff x = \frac{91}{13} = 7.$$
> Substitute $x = 7$ into $L_1$:
> $$3(7) + 4y = 11 \iff 21 + 4y = 11 \iff 4y = 11 - 21 = -10 \iff y = -\frac{10}{4} = -2.5.$$
> The unique solution pair is $(7\,; -2.5)$.
> Solution set: $S = \{(7\,; -2.5)\}$.

> **Worked Example 4 — Inconsistent and Dependent Systems.**
> Examine geometrically the following two systems:
> a) $\begin{cases} 2x - 3y = 7 \\ -4x + 6y = 5 \end{cases}$ \quad b) $\begin{cases} x - 2y = 3 \\ 3x - 6y = 9 \end{cases}$
>
> **Solution:**
> a) Multiply the first equation by $2$:
> $$4x - 6y = 14.$$
> Add to the second:
> $$(4x - 6y) + (-4x + 6y) = 14 + 5 \iff 0 = 19.$$
> This is a contradiction! Geometrically, the two lines have collinear direction vectors ($\frac{-4}{2} = \frac{6}{-3} = -2$), so they are strictly parallel and never cross. The system has **no solution**: $S = \varnothing$.
>
> b) Multiply the first equation by $3$:
> $$3x - 6y = 9.$$
> This is identical to the second equation! Both equations describe the **same line**.
> Every point on this line is a solution. The system has **infinitely many solutions**: all pairs of the form $(2y + 3 \,;\, y)$ for $y \in \mathbb{R}$.

> **Worked Example 5 — Equation of the Perpendicular Bisector.**
> Let $A(1\,; 2)$ and $B(5\,; 4)$.
> Find the equation of the perpendicular bisector $\Delta$ of segment $[AB]$.
>
> **Solution:**
> Recall: the perpendicular bisector is the locus of points equidistant from $A$ and $B$, passing through the midpoint $I$ of $[AB]$.
> 1. Midpoint $I$ of $[AB]$:
>    $$x_I = \frac{1 + 5}{2} = 3, \quad y_I = \frac{2 + 4}{2} = 3 \implies I(3\,; 3).$$
> 2. Geometric condition: $M(x\,; y) \in \Delta \iff MA^2 = MB^2$.
>    $$MA^2 = (x - 1)^2 + (y - 2)^2 = x^2 - 2x + 1 + y^2 - 4y + 4 = x^2 + y^2 - 2x - 4y + 5.$$
>    $$MB^2 = (x - 5)^2 + (y - 4)^2 = x^2 - 10x + 25 + y^2 - 8y + 16 = x^2 + y^2 - 10x - 8y + 41.$$
>    Equating $MA^2 = MB^2$:
>    $$x^2 + y^2 - 2x - 4y + 5 = x^2 + y^2 - 10x - 8y + 41.$$
>    The quadratic terms $x^2$ and $y^2$ cancel:
>    $$-2x - 4y + 5 = -10x - 8y + 41 \iff 8x + 4y - 36 = 0.$$
>    Dividing through by $4$:
>    $$\boxed{2x + y - 9 = 0} \quad \text{or in slope-intercept form} \quad \boxed{y = -2x + 9}.$$

> **Worked Example 6 — Pencil of Lines Depending on a Parameter.**
> For any real parameter $m$, consider line $\mathcal{D}_m$ defined by:
> $$(m - 1)x + (2m + 1)y - 5m + 2 = 0.$$
> Prove that all lines $\mathcal{D}_m$ pass through a fixed point $K$, and find its coordinates.
>
> **Solution:**
> Regroup terms by powers of parameter $m$:
> $$mx - x + 2my + y - 5m + 2 = 0 \iff m(x + 2y - 5) + (-x + y + 2) = 0.$$
> For this equation to hold true **for all values of $m$**, both the coefficient of $m$ and the constant term must vanish simultaneously:
> $$\begin{cases} x + 2y - 5 = 0 \\ -x + y + 2 = 0 \end{cases}$$
> Add both equations:
> $$(x + 2y - 5) + (-x + y + 2) = 0 \iff 3y - 3 = 0 \iff y = 1.$$
> Substitute into the second equation:
> $$-x + 1 + 2 = 0 \iff x = 3.$$
> Every line in the family passes through the fixed pivot point $K(3\,; 1)$!

---

### 8. In Computer Science: Solving a $2 \times 2$ System in Python

Here is a Python script that takes Cartesian coefficients for two lines and determines their intersection point:

```python
def solve_system(a1, b1, c1, a2, b2, c2):
    """
    Solves the linear system:
    a1*x + b1*y + c1 = 0
    a2*x + b2*y + c2 = 0
    """
    # Main determinant (a1*b2 - a2*b1)
    det = a1 * b2 - a2 * b1
    
    if abs(det) < 1e-12:
        # Lines are parallel or coincident
        # Test proportionality with constants
        if abs(a1 * c2 - a2 * c1) < 1e-12 and abs(b1 * c2 - b2 * c1) < 1e-12:
            return "Infinitely many solutions (coincident lines)"
        else:
            return "No solution (strictly parallel lines)"
    else:
        # Cramer's rule to find x and y
        # Rewrite in form: a*x + b*y = -c
        e1, e2 = -c1, -c2
        x = (e1 * b2 - e2 * b1) / det
        y = (a1 * e2 - a2 * e1) / det
        return (x, y)

# Test using system from Worked Example 1:
# x - 2y + 4 = 0  and  x + y - 7 = 0
solution = solve_system(1, -2, 4, 1, 1, -7)
print("Intersection point:", solution)  # Outputs (3.3333333333333335, 3.6666666666666665)
```

---

### Key Takeaways

1. **Direction Vector:** any non-zero vector $\vec{u}$ parallel to the line. If $A, B \in \mathcal{D}$, then $\vec{AB}$ is a direction vector.
2. **Cartesian Equation:** $ax + by + c = 0$ with $(a, b) \neq (0, 0)$.
   - Canonical direction vector: $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$.
3. **Slope-Intercept Form:**
   - If the line is non-vertical ($b \neq 0$): $y = mx + p$.
     - $m = -\frac{a}{b} = \frac{y_B - y_A}{x_B - x_A}$ is the **slope** (gradient).
     - $p$ is the **$y$-intercept** (point $(0\,; p)$).
     - Direction vector: $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$.
   - If the line is vertical ($b = 0$): $x = k$. No slope is defined.
4. **Relative Positions:**
   - Parallel $\iff m = m'$ (or $ab' - a'b = 0$).
   - Intersecting $\iff m \neq m'$ (or $ab' - a'b \neq 0$). Unique intersection via system solving.
5. **Methods for Solving Systems:**
   - *Substitution*: isolate one variable and substitute into the second equation.
   - *Elimination*: scale equations so one variable cancels upon addition.

---

### Exercises

#### Direct Application Exercises (★)

1. State a direction vector for the line with equation $3x - 5y + 7 = 0$.
2. State a direction vector for the line with equation $y = -4x + 3$.
3. Determine the slope and $y$-intercept of the line $2x + 4y - 8 = 0$.
4. Write the slope-intercept equation of the line passing through point $P(0\,; -5)$ with slope $m = 3$.
5. Does the line $x = 4$ have a slope? Explain why or why not.
6. Are the lines $y = 3x - 2$ and $6x - 2y + 5 = 0$ parallel?
7. Does the point $A(3\,; -1)$ lie on the line $2x - 5y - 11 = 0$?
8. Find the $x$-coordinate of the point on the line $y = 2x - 6$ whose $y$-coordinate is $4$.
9. Solve the system by substitution: $\begin{cases} y = 2x - 1 \\ 3x + y = 9 \end{cases}$.
10. Solve the system by elimination: $\begin{cases} x + y = 10 \\ x - y = 4 \end{cases}$.

#### Practice and Reasoning Exercises (★★)

11. Determine the Cartesian equation of the line passing through $A(2\,; -3)$ with direction vector $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix}$.
12. Determine the slope-intercept equation of the line passing through points $M(-2\,; 7)$ and $N(4\,; 1)$.
13. Given points $A(-1\,; 2)$, $B(3\,; 4)$, and $C(2\,; -1)$.
    Determine an equation of line $\mathcal{D}$ passing through $C$ parallel to $(AB)$.
14. Solve in $\mathbb{R}^2$ the system: $\begin{cases} 4x + 3y = 1 \\ 2x - 5y = 7 \end{cases}$.
15. Find the coordinates of the intersection point of lines $\mathcal{D}_1 : 3x - 2y + 6 = 0$ and $\mathcal{D}_2 : x + 2y - 2 = 0$.
16. For what value of $k \in \mathbb{R}$ is the line $kx + 2y - 5 = 0$ parallel to the line passing through $A(1\,; 1)$ and $B(3\,; 7)$?
17. Let triangle $ABC$ have vertices $A(0\,; 4)$, $B(-2\,; 0)$, and $C(4\,; 0)$.
    Determine the equation of the median passing through $A$.
18. Find the real parameter $m$ such that the system $\begin{cases} mx + 2y = 4 \\ 3x + (m - 1)y = 2 \end{cases}$ fails to have a unique solution.

#### Advanced Problems and Challenges (★★★)

19. **Concurrency of Altitudes (The Orthocenter).**
    In an orthonormal coordinate frame, let $A(0\,; 3)$, $B(-2\,; 0)$, and $C(4\,; 0)$.
    a) Determine an equation of the altitude from $A$.
    b) Using the property that the altitude from $B$ is perpendicular to $(AC)$, determine its equation.
    c) Compute the coordinates of the orthocenter $H$ of the triangle.
20. **Orthogonal Projection of a Point onto a Line.**
    Consider the line $\mathcal{D} : 2x - y + 1 = 0$ and point $A(4\,; 4)$.
    a) Determine the equation of line $\Delta$ perpendicular to $\mathcal{D}$ passing through $A$.
    b) Determine the coordinates of intersection point $H$ of $\mathcal{D}$ and $\Delta$.
    c) Calculate the distance $AH$. (This is the minimum distance from point $A$ to line $\mathcal{D}$).
21. **Concurrency of Three Lines.**
    Consider the three lines:
    $\mathcal{D}_1 : 2x - y - 1 = 0$, $\mathcal{D}_2 : x + y - 5 = 0$, and $\mathcal{D}_3 : 3x + ky - 7 = 0$.
    Determine the value of $k \in \mathbb{R}$ such that all three lines are concurrent at a single point.
22. **Economic Equilibrium: Supply and Demand.**
    In a commodities market, quantity supplied $q_S$ and quantity demanded $q_D$ (in tonnes) depend on unit price $p$ (in euros per kg) according to the following linear laws:
    - Supply: $q_S = 2p - 4$ (producers supply more as price rises).
    - Demand: $q_D = -3p + 21$ (buyers demand less as price rises).
    a) Plot both lines in a coordinate system $(p\,; q)$.
    b) Calculate the equilibrium price $p_E$ where supply equals demand.
    c) What is the market transaction quantity at equilibrium?

---

### Solutions

1. For $ax + by + c = 0$, a direction vector is $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix}$. Here $a = 3, b = -5 \implies \vec{u}\begin{pmatrix} 5 \\ 3 \end{pmatrix}$.
2. For $y = mx + p$, a direction vector is $\vec{u}\begin{pmatrix} 1 \\ m \end{pmatrix}$. Here $m = -4 \implies \vec{u}\begin{pmatrix} 1 \\ -4 \end{pmatrix}$.
3. $4y = -2x + 8 \iff y = -\frac{2}{4}x + \frac{8}{4} = -\frac{1}{2}x + 2$.
   Slope $m = -\frac{1}{2}$, $y$-intercept $p = 2$.
4. $y = 3x - 5$.
5. No, the line $x = 4$ is vertical. Its slope is undefined (run $\Delta x = 0$).
6. Line 1: $m_1 = 3$. Line 2: $-2y = -6x - 5 \iff y = 3x + 2.5 \implies m_2 = 3$.
   Since $m_1 = m_2 = 3$ and intercepts differ ($-2 \neq 2.5$), the lines are strictly parallel.
7. Substitute $x = 3$ and $y = -1$: $2(3) - 5(-1) - 11 = 6 + 5 - 11 = 0$. Yes, $A \in \mathcal{D}$.
8. $4 = 2x - 6 \iff 2x = 10 \iff x = 5$.
9. Substitute $y$ into the second equation: $3x + (2x - 1) = 9 \iff 5x - 1 = 9 \iff 5x = 10 \iff x = 2$.
   Then $y = 2(2) - 1 = 3$. Solution: $(2\,; 3)$.
10. Add equations: $(x + y) + (x - y) = 10 + 4 \iff 2x = 14 \iff x = 7$.
    Then $7 + y = 10 \iff y = 3$. Solution: $(7\,; 3)$.
11. $\vec{u}\begin{pmatrix} -3 \\ 4 \end{pmatrix} = \begin{pmatrix} -b \\ a \end{pmatrix} \implies a = 4$ and $b = 3$.
    Equation: $4x + 3y + c = 0$.
    $A(2\,; -3) \in \mathcal{D} \implies 4(2) + 3(-3) + c = 0 \iff 8 - 9 + c = 0 \iff c = 1$.
    Equation: $4x + 3y + 1 = 0$.
12. $m = \frac{1 - 7}{4 - (-2)} = \frac{-6}{6} = -1$.
    $y = -x + p$. Using $N(4\,; 1)$: $1 = -4 + p \implies p = 5$.
    Slope-intercept equation: $y = -x + 5$.
13. Vector $\vec{AB}\begin{pmatrix} 3 - (-1) \\ 4 - 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$ or scaled $\vec{u}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
    $\vec{u}\begin{pmatrix} -b \\ a \end{pmatrix} \implies a = 1, b = -2$.
    Equation: $x - 2y + c = 0$.
    $C(2\,; -1) \in \mathcal{D} \implies 2 - 2(-1) + c = 0 \iff 2 + 2 + c = 0 \iff c = -4$.
    Equation: $x - 2y - 4 = 0$ (or $y = \frac{1}{2}x - 2$).
14. Multiply the second row by $-2$:
    $-2(2x - 5y) = -2(7) \iff -4x + 10y = -14$.
    Add to the first: $(4x + 3y) + (-4x + 10y) = 1 - 14 \iff 13y = -13 \iff y = -1$.
    Substitute back: $2x - 5(-1) = 7 \iff 2x + 5 = 7 \iff 2x = 2 \iff x = 1$.
    Solution: $(1\,; -1)$.
15. Add $\mathcal{D}_1$ and $\mathcal{D}_2$:
    $(3x - 2y + 6) + (x + 2y - 2) = 0 \iff 4x + 4 = 0 \iff x = -1$.
    Substitute into $\mathcal{D}_2$: $-1 + 2y - 2 = 0 \iff 2y = 3 \iff y = 1.5$.
    Intersection: $I(-1\,; 1.5)$.
16. Slope of $(AB)$: $m = \frac{7 - 1}{3 - 1} = \frac{6}{2} = 3$.
    Line $kx + 2y - 5 = 0 \iff 2y = -kx + 5 \iff y = -\frac{k}{2}x + \frac{5}{2}$.
    Its slope is $-\frac{k}{2}$.
    Parallelism $\iff -\frac{k}{2} = 3 \iff k = -6$.
17. The median from $A$ connects $A(0\,; 4)$ and midpoint $A'$ of $[BC]$.
    $x_{A'} = \frac{-2 + 4}{2} = 1$ and $y_{A'} = \frac{0 + 0}{2} = 0$, so $A'(1\,; 0)$.
    Slope $m = \frac{0 - 4}{1 - 0} = -4$. Intercept from $A(0\,; 4)$: $p = 4$.
    Equation: $y = -4x + 4$.
18. No unique solution when determinant vanishes:
    $m(m - 1) - 2 \times 3 = 0 \iff m^2 - m - 6 = 0$.
    Factoring: $(m - 3)(m + 2) = 0 \implies m = 3$ or $m = -2$.
19. a) Side $[BC]$ lies on the $x$-axis ($y = 0$). The altitude from $A$ is therefore perpendicular to the $x$-axis: it is a vertical line through $A(0\,; 3)$, equation $x = 0$.
    b) Vector $\vec{AC}\begin{pmatrix} 4 - 0 \\ 0 - 3 \end{pmatrix} = \begin{pmatrix} 4 \\ -3 \end{pmatrix}$.
    A line perpendicular to $(AC)$ has normal vector $\vec{AC}$, meaning its direction vector is $\vec{u}\begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
    Slope of this altitude: $m = \frac{4}{3}$.
    Passing through $B(-2\,; 0)$: $y - 0 = \frac{4}{3}(x - (-2)) \implies y = \frac{4}{3}x + \frac{8}{3}$.
    c) Orthocenter $H$ is the intersection of both altitudes.
    Since the first altitude is $x = 0$, substitute $x = 0$ into the second: $y = \frac{8}{3}$.
    Thus $H\left(0\,; \frac{8}{3}\right)$.
20. a) Direction vector of $\mathcal{D} : 2x - y + 1 = 0$ is $\vec{u}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ (slope $m = 2$).
    Perpendicular line $\Delta$ has slope $m' = -\frac{1}{m} = -\frac{1}{2}$.
    Equation: $y - 4 = -\frac{1}{2}(x - 4) \iff y = -\frac{1}{2}x + 2 + 4 = -\frac{1}{2}x + 6 \iff x + 2y - 12 = 0$.
    b) Intersection of $\mathcal{D}$ and $\Delta$:
    From $\mathcal{D}$, $y = 2x + 1$. In $\Delta$: $x + 2(2x + 1) - 12 = 0 \iff 5x - 10 = 0 \iff x = 2$.
    Then $y = 2(2) + 1 = 5$. Projected point is $H(2\,; 5)$.
    c) $AH = \sqrt{(2 - 4)^2 + (5 - 4)^2} = \sqrt{(-2)^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}$.
21. Find intersection $K$ of $\mathcal{D}_1$ and $\mathcal{D}_2$:
    $\begin{cases} 2x - y = 1 \\ x + y = 5 \end{cases}$
    Sum: $3x = 6 \implies x = 2$. Then $y = 5 - 2 = 3$. Thus $K(2\,; 3)$.
    For $\mathcal{D}_3$ to pass through $K$:
    $3(2) + k(3) - 7 = 0 \iff 6 + 3k - 7 = 0 \iff 3k = 1 \iff k = \frac{1}{3}$.
22. a) Supply line has positive slope $2$; demand line has negative slope $-3$.
    b) At equilibrium, $q_S = q_D \iff 2p - 4 = -3p + 21 \iff 5p = 25 \iff p_E = 5\text{ €/kg}$.
    c) Equilibrium quantity: $q_E = 2(5) - 4 = 10 - 4 = 6\text{ tonnes}$ (or $q_E = -3(5) + 21 = 6\text{ tonnes}$).

---

### The Question That Opens the Future

A straight line represents mathematics in its most well-behaved and predictable form: a relationship where every step forward produces the exact same steady return. This is the domain of affine functions $x \mapsto mx + p$.

Yet what happens when the inner rule of the machine becomes more intricate? When the machine squares numbers, reciprocates them, or extracts square roots? How do we map the curves, crests, and valleys of non-linear graphs? That is what we are about to explore in **The Jacquard Loom and the Function Box**.
