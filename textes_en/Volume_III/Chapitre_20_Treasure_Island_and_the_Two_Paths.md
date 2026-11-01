# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)
## CHAPTER 20: Treasure Island and the Two Paths

> *“A single number can only measure linear distance along a solitary trail. But to locate a buried chest across an open plain, guide a galleon through thick sea mist, or map every star in the night sky, one must open the universe in two dimensions and marry algebra to geometry.”*

---

### What You Are About to Discover

- The mystery of the pirate's map and the legendary fly on the ceiling of **René Descartes**.
- The **Cartesian coordinate plane**: the horizontal **$x$-axis** of abscissas, the vertical **$y$-axis** of ordinates, and the **four quadrants**.
- How to plot and read the **coordinates** of a point $(x\,;\,y)$ without ever reversing them.
- The formula for the **midpoint of a segment**: the simple arithmetic average of coordinates.
- Calculating the exact **distance between two points** in a coordinate plane via the Pythagorean Theorem: $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.
- **Multiplication and division of signed (relative) numbers**: why “negative times negative equals positive,” proved through time-reversed motion and algebraic distributivity!
- 🛠️ The Boundary Case Laboratory: points on the axes, reflections across the origin, and irrational coordinates in Euclidean space.

---

### 1. The Problem: The Treasure Map and the Anxiety of the Circle

Imagine that you have just rowed ashore onto an uninhabited tropical island in the Indian Ocean.  
Clutched in your trembling hand is the brittle, yellowed parchment of a buccaneer. The ink has faded from sea salt and humidity, but you manage to decipher these few quill-drawn words:  
*“The brass-bound chest of gold coins lies buried at exactly 50 meters from the solitary black standing stone that towers above the beach.”*

Your heart pounds. You dash toward the black standing stone.  
You plant your heels against the volcanic rock, face the palm grove, pace out 50 meters, plunge your shovel into the sand, and begin digging feverishly.  
You dig for an hour under a blistering sun. Nothing! Not a single coin, only crushed coral.

You stop, drenched in sweat, as the chilling mathematical truth dawns on you:  
The pirate wrote: *“at 50 meters from the standing stone.”*  
But in which direction?
- 50 meters to the North?
- 50 meters to the East, into the crashing ocean surf?
- 50 meters to the West, beneath the tangled roots of a giant banyan tree?

```
                             50 m North
                                 ●
                               /   \
                             /       \
       50 m West ● ──── [ Standing Stone ] ──── ● 50 m East
                             \       /
                               \   /
                                 ●
                             50 m South
```

As we proved in Chapter 16, all the points located at 50 meters from the central stone form an **immense circle surrounding the marker**!  
If you must excavate every trench along that circular perimeter, you will have to dig a ditch over 314 meters long. By the time you finish, you will be an old hermit with a long white beard!

A single number is insufficient to pinpoint a unique position across a two-dimensional surface.  
To locate any object without hesitation, one requires **two independent pieces of information**.

---

### 2. The Fly on the Ceiling of René Descartes

To solve this riddle, let us leave our tropical island and travel through time to the bitter winter of **1637** in France.

Inside a bedroom of a venerable stone house, a forty-year-old gentleman rests beneath heavy feather quilts well past mid-morning. His name is **René Descartes**.  
Descartes had suffered from frail health since boyhood, and his Jesuit tutors had granted him the lifetime habit of lingering in bed each morning to let his mind meditate in quiet stillness.

As he gazes upward, a small black housefly lands upon the white plaster ceiling.  
The fly crawls a few inches, pauses, buzzes into the air, and settles on a new spot.  
Descartes asks himself a deceptively simple question that no human mind had ever formulated with such precision:  
*“How could I describe the exact, instantaneous position of that fly to a friend across the room without needing to climb a ladder and point my finger at it?”*

```
     Far Wall (Vertical y-axis)
          ▲
          |
        4 |            ● Fly M (3 ; 4)
        3 |            :
        2 |            :
        1 |            :
          +------------+------------► Right Wall (Horizontal x-axis)
          O   1   2    3    4    5
        Room Corner
```

Descartes looks at the two perpendicular walls meeting in the corner of his bedroom:
1. He measures the horizontal distance from the fly to the **left wall**: say, **3 meters**.
2. He measures the vertical distance from the fly to the **far wall**: say, **4 meters**.

*“It is luminous!”* Descartes realizes. The ordered pair of numbers $(3\,;\,4)$ uniquely fixes the position of the fly upon the flat ceiling without the slightest ambiguity!  
Two numbers to identify any point in a two-dimensional world: Descartes had just invented the **Cartesian coordinate system**.

---

### 3. The Coordinate Plane and the Four Quadrants

#### 3.1 Anatomy of the Cartesian System

Upon grid paper, we construct two perpendicular number lines intersecting at their common zero:

```
                                  Vertical y-axis (Ordinates)
                                            ▲
                                          3 |       Quadrant II         Quadrant I
                                          2 |         (- , +)             (+ , +)
                                          1 |
      Horizontal ◄───┼────┼────┼────┼────┼─────┼─────┼────┼────┼────┼────┼───► x-axis (Abscissas)
      Number line   -5   -4   -3   -2   -1    O|    1    2    3    4    5
                                         -1 |
                                         -2 |       Quadrant III        Quadrant IV
                                         -3 |         (- , -)             (+ , -)
                                            ▼
```

> **📐 Foundational Definitions — Official Terminology**  
> - The intersection of the two perpendicular axes is the **origin**, denoted $O$. Its coordinates are $(0\,;\,0)$.  
> - The horizontal axis is the **$x$-axis** (axis of abscissas). The $x$-coordinate measures displacement **left / right**.  
> - The vertical axis is the **$y$-axis** (axis of ordinates). The $y$-coordinate measures displacement **down / up**.  
> - A coordinate system is **orthogonal** if its axes are strictly perpendicular. It is **orthonormal** (or Cartesian) if both axes share the identical unit scale (e.g., $1\text{ grid unit} = 1\text{ cm}$ on both axes).

#### 3.2 Coordinate Notation

For any point $M$, we write its ordered pair:
$$M(x_M\,;\,y_M)$$
- $x_M$ is the **abscissa** ($x$-coordinate).  
- $y_M$ is the **ordinate** ($y$-coordinate).

> **🧭 Mnemonic Rules — Never Confuse $x$ and $y$**  
> 1. **Alphabetical Order:** In the alphabet, **A**bscissa precedes **O**rdinate, just as **$x$** precedes **$y$**. The $x$-coordinate is ALWAYS written first!  
> 2. **The Apartment Elevator:** To visit a friend in an apartment building, you must first walk down the street to the entrance of their building hallway (**horizontal $x$**), and only then take the elevator up to their floor (**vertical $y$**). You cannot ride the elevator before you enter the lobby!

#### 3.3 The Four Quadrants

The intersecting axes partition the infinite plane into four quadrants, numbered counterclockwise starting from the top right:
- **Quadrant I (top-right):** $x > 0$ and $y > 0$ $(+, +)$.
- **Quadrant II (top-left):** $x < 0$ and $y > 0$ $(-, +)$.
- **Quadrant III (bottom-left):** $x < 0$ and $y < 0$ $(-, -)$.
- **Quadrant IV (bottom-right):** $x > 0$ and $y < 0$ $(+, -)$.

---

### 4. Two Magic Formulas of the Coordinate Plane

Once geometric points are encoded as numerical pairs, we no longer need to draw physical figures to solve geometric problems: algebraic calculation solves everything!

#### 4.1 The Midpoint of a Segment

Given two points $A(x_A\,;\,y_A)$ and $B(x_B\,;\,y_B)$:  
Where is the exact midpoint $I$ of segment $[AB]$?  
It lies exactly halfway horizontally, and halfway vertically. It is simply the **arithmetic mean (average)** of their coordinates!

> **📐 Property — Midpoint Coordinates**  
> The coordinates of midpoint $I$ of segment $[AB]$ are:
> $$x_I = \frac{x_A + x_B}{2} \quad \text{and} \quad y_I = \frac{y_A + y_B}{2}$$

#### 4.2 Distance Between Two Points: Pythagoras on the Grid

How can we calculate the exact straight-line distance $AB$ between any two points in the plane?  
Observe the diagram:

```
          yB |                     ● B(xB ; yB)
             |                   / |
             |                 /   |  Δy = yB - yA (vertical leg)
          yA |     A(xA ; yA)●─────● C(xB ; yA)
             |                 Δx = xB - xA (horizontal leg)
             +───────────────┼─────┼────────► x
                            xA    xB
```

Draw a horizontal line through $A$, and a vertical line through $B$. They intersect at point $C(x_B\,;\,y_A)$, forming a **right triangle $ABC$**!
- The horizontal base length is: $AC = |x_B - x_A|$.
- The vertical altitude length is: $BC = |y_B - y_A|$.
- The hypotenuse is the segment $[AB]$!

Applying the Pythagorean Theorem in right triangle $ABC$:
$$AB^2 = AC^2 + BC^2 = (x_B - x_A)^2 + (y_B - y_A)^2$$

Taking the square root delivers the universal Cartesian distance formula:

> **📐 Theorem — Cartesian Distance Formula**  
> In an orthonormal coordinate plane, the distance between points $A(x_A\,;\,y_A)$ and $B(x_B\,;\,y_B)$ is:
> $$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

---

### 5. Multiplying Signed Numbers: Why Minus Times Minus Equals Plus

Navigating all four quadrants with positive and negative coordinates brings us face-to-face with a fundamental arithmetic challenge: how do we **multiply** signed numbers?

While addition and subtraction of negative numbers are intuitive (winning or losing money, climbing or descending into a basement), the multiplication of two negative numbers seems at first glance like an impenetrable paradox. Why should $(-3) \times (-4) = +12$?

Here are two irrefutable demonstrations: one cinematic and visual, the other purely algebraic.

#### 5.1 The Movie Reel Proof: The Walking Actor and Rewind

Imagine an actor walking along a straight road marked with meter posts, recorded on video:
- His **velocity**:
  - Walking forward to the right (positive direction): velocity $+2\text{ m/s}$.
  - Walking backward to the left: velocity $-2\text{ m/s}$.
- The **time** on the video player:
  - Playing the film forward into the future: time $+3\text{ seconds}$.
  - Rewinding the film into the past: time $-3\text{ seconds}$.

Where does the actor appear on the screen relative to the starting line?

1. **$(+2) \times (+3) = +6$:**  
   He walks forward at $2\text{ m/s}$, watched 3 seconds into the future $\implies$ he is at **$+6\text{ meters}$** to the right.
2. **$(-2) \times (+3) = -6$:**  
   He walks backward at $-2\text{ m/s}$, watched 3 seconds into the future $\implies$ he is at **$-6\text{ meters}$** to the left.
3. **$(+2) \times (-3) = -6$:**  
   He walks forward to the right, but we rewind the video 3 seconds into the past $\implies$ he was at **$-6\text{ meters}$** to the left!
4. **$(-2) \times (-3) = +6$:**  
   He was walking backward to the left, and we rewind the video into the past! What do your eyes see on the screen? **An actor advancing forward to the right!** He was at **$+6\text{ meters}$**!  
   *Rewinding a film of someone walking backward shows them moving forward!*

#### 5.2 The Algebraic Proof via Distributivity

Mathematicians require a proof independent of physical metaphors. Here it is: we demand that the foundational law of distributivity, $k \times (a + b) = k \times a + k \times b$, remains universally true for all real numbers.

Let us evaluate the following expression in two different ways:
$$E = (-3) \times [4 + (-4)]$$

- **Method 1 (inside brackets first):**  
  $4 + (-4) = 0$. Therefore:  
  $$E = (-3) \times 0 = \mathbf{0}$$

- **Method 2 (expanding via distributivity):**  
  $$E = (-3) \times 4 + (-3) \times (-4)$$  
  We already know that $(-3) \times 4 = -12$ (since 4 debts of \$3 equal a debt of \$12).  
  Our equation becomes:  
  $$0 = -12 + [(-3) \times (-4)]$$

Ask yourself: what unique number must be added to $-12$ to yield zero?  
The one and only number in the mathematical universe is **$+12$**!  
Therefore, with absolute logical necessity:
$$(-3) \times (-4) = \mathbf{+12}$$

If negative times negative did not equal positive, the entire framework of algebra would collapse into contradiction!

> **📐 The Rule of Signs — Multiplication and Division**  
> - The product (or quotient) of two numbers with the **same sign** is **POSITIVE**:  
>   $$(+) \times (+) = (+) \quad \text{and} \quad (-) \times (-) = (+)$$  
> - The product (or quotient) of two numbers with **different signs** is **NEGATIVE**:  
>   $$(+) \times (-) = (-) \quad \text{and} \quad (-) \times (+) = (-)$$  
>  
> For a product of multiple non-zero factors:  
> - An **even number** of negative factors yields a **positive** product.  
> - An **odd number** of negative factors yields a **negative** product.

---

### 6. Beware of Pitfalls!

> **⚠️ Warning: Never Confuse Addition and Multiplication!**  
> 1. **The Deadly Sign Confusion:**  
>    $$-3 - 5 = \mathbf{-8} \quad (\text{losing 3, then losing 5: this is addition/subtraction!})$$  
>    $$(-3) \times (-5) = \mathbf{+15} \quad (\text{this is multiplication!})$$  
>    Never chant “two minuses make a plus” without emphasizing that this applies ONLY to multiplication and division!  
> 2. **Reversing Abscissa and Ordinate:**  
>    Point $A(2\,;\,5)$ is located 2 units right, 5 units up.  
>    Point $B(5\,;\,2)$ is located 5 units right, 2 units up.  
>    These are two completely different locations!  
> 3. **The Minus Sign Trap in Distance Computations:**  
>    If $x_A = -3$ and $x_B = 4$, the horizontal leg length is:  
>    $$x_B - x_A = 4 - (-3) = 4 + 3 = \mathbf{7}$$  
>    Watch out for the double negative turning into addition!

---

### 7. Solved Examples

#### Solved Example 1 — Plotting and Identifying Coordinates
In an orthonormal grid where 1 grid square = 1 unit:
1. Plot the points: $A(3\,;\,2)$, $B(-4\,;\,3)$, $C(-2\,;\,-3)$, $D(5\,;\,-1)$, $E(0\,;\,4)$, $F(-3\,;\,0)$.  
2. State the quadrant or axis for each point.

*Solution:*  
- $A(3\,;\,2)$: 3 units right, 2 units up $\to$ **Quadrant I**.  
- $B(-4\,;\,3)$: 4 units left, 3 units up $\to$ **Quadrant II**.  
- $C(-2\,;\,-3)$: 2 units left, 3 units down $\to$ **Quadrant III**.  
- $D(5\,;\,-1)$: 5 units right, 1 unit down $\to$ **Quadrant IV**.  
- $E(0\,;\,4)$: zero abscissa $\to$ lies directly on the **$y$-axis**.  
- $F(-3\,;\,0)$: zero ordinate $\to$ lies directly on the **$x$-axis**. ✔

#### Solved Example 2 — Calculating Segment Midpoint
Given points $M(-5\,;\,7)$ and $N(3\,;\,-1)$. Calculate the coordinates of midpoint $K$ of segment $[MN]$.

*Solution:*  
Apply the midpoint formulas:
$$x_K = \frac{x_M + x_N}{2} = \frac{-5 + 3}{2} = \frac{-2}{2} = -1$$
$$y_K = \frac{y_M + y_N}{2} = \frac{7 + (-1)}{2} = \frac{6}{2} = 3$$
The midpoint is $K(-1\,;\,3)$. ✔

#### Solved Example 3 — Calculating Distance Between Two Points
Given $A(-2\,;\,1)$ and $B(4\,;\,9)$ in an orthonormal centimeter grid.  
Calculate the exact length of segment $[AB]$.

*Solution:*  
Apply the distance formula:
$$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$
Compute the directional spans:
$$x_B - x_A = 4 - (-2) = 4 + 2 = 6$$
$$y_B - y_A = 9 - 1 = 8$$
Square and sum:
$$AB^2 = 6^2 + 8^2 = 36 + 64 = 100$$
Take the square root:
$$AB = \sqrt{100} = 10\text{ cm}$$
Segment $[AB]$ measures exactly $10\text{ cm}$. ✔

#### Solved Example 4 — Signed Number Arithmetic
Evaluate:  
1. $P_1 = (-4) \times (+7)$  
2. $P_2 = (-6) \times (-8)$  
3. $Q_1 = \frac{-45}{9}$  
4. $Q_2 = \frac{-56}{-7}$  
5. $P_3 = (-2) \times (-3) \times (-1) \times (+4) \times (-5)$

*Solution:*  
1. Opposite signs $\implies$ negative: $P_1 = -28$.  
2. Same sign (both negative) $\implies$ positive: $P_2 = +48$.  
3. Opposite signs $\implies$ negative: $Q_1 = -5$.  
4. Same sign $\implies$ positive: $Q_2 = +8$.  
5. Count negative factors in $P_3$: there are 4 negative factors ($(-2), (-3), (-1), (-5)$).  
   4 is even $\implies$ product is **positive**.  
   Magnitude: $2 \times 3 \times 1 \times 4 \times 5 = 120$.  
   Therefore, $P_3 = +120$. ✔

#### Solved Example 5 — Determining Triangle Classification via Coordinates
Given $A(1\,;\,2)$, $B(4\,;\,6)$, and $C(-3\,;\,5)$ in an orthonormal plane.  
Prove that triangle $ABC$ is an isosceles right-angled triangle.

*Solution:*  
Calculate the squared side lengths:
- For $AB$:  
  $$AB^2 = (4 - 1)^2 + (6 - 2)^2 = 3^2 + 4^2 = 9 + 16 = 25 \implies AB = 5$$  
- For $AC$:  
  $$AC^2 = (-3 - 1)^2 + (5 - 2)^2 = (-4)^2 + 3^2 = 16 + 9 = 25 \implies AC = 5$$  
- For $BC$:  
  $$BC^2 = (-3 - 4)^2 + (5 - 6)^2 = (-7)^2 + (-1)^2 = 49 + 1 = 50$$

Geometric analysis:
1. $AB = AC = 5$: triangle $ABC$ has two sides of equal length, so it is **isosceles at vertex $A$**.  
2. Compare squares:  
   $$AB^2 + AC^2 = 25 + 25 = 50 = BC^2$$  
   By the **Converse of the Pythagorean Theorem**, triangle $ABC$ is **right-angled at vertex $A$**.  
Conclusion: $ABC$ is an **isosceles right-angled triangle at $A$**. ✔

---

### What You Must Remember

1. **Cartesian Coordinate Plane:**  
   - Horizontal $(Ox)$: **abscissas** ($x$).  
   - Vertical $(Oy)$: **ordinates** ($y$).  
   - Coordinates: $M(x\,;\,y)$ ($x$ first, $y$ second).
2. **Segment Midpoint $[AB]$:**  
   $$x_I = \frac{x_A + x_B}{2} \quad \text{and} \quad y_I = \frac{y_A + y_B}{2}$$
3. **Cartesian Distance Formula:**  
   $$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$
4. **Rule of Signs:**  
   - Same signs $\implies$ **positive** ($+ \times + = +$ and $- \times - = +$).  
   - Opposite signs $\implies$ **negative** ($+ \times - = -$ and $- \times + = -$).  
   - Products of multiple factors: count the minus signs (even $\implies +$; odd $\implies -$).

---

### Exercises

#### Level ★ (Direct Application)

**Exercise 1.** State the coordinates of the vertices of rectangle $ABCD$:  
$A$ is 3 units left and 2 up; $B$ is 4 units right and 2 up; $C$ is 4 units right and 1 down; $D$ is 3 units left and 1 down.

**Exercise 2.** Compute without a calculator:  
1. $(-7) \times (-6)$  
2. $(-8) \times (+9)$  
3. $(+12) \times (-5)$  
4. $\frac{-72}{-8}$  
5. $\frac{-42}{+7}$

**Exercise 3.** State the sign of each product without evaluating its numerical value:  
1. $(-3) \times (-5) \times (+2) \times (-7)$  
2. $(-1) \times (-2) \times (-3) \times (-4) \times (-5) \times (-6)$  
3. The product of 15 negative numbers and 28 positive numbers.

**Exercise 4.** Given $A(2\,;\,4)$ and $B(8\,;\,10)$. Calculate the coordinates of midpoint $I$ of segment $[AB]$.

**Exercise 5.** Calculate the exact distance $AB$ between $A(1\,;\,2)$ and $B(4\,;\,6)$.

#### Level ★★ (Reasoning and Geometric Calculations)

**Exercise 6. Combined Operations with Signed Numbers.**  
Evaluate respecting operational precedence:  
1. $E = (-3) \times (-4) + (-5) \times (+2)$  
2. $F = 15 - (-2) \times (-6)$  
3. $G = \frac{(-4) \times (-9)}{-3 - 3}$  
4. $H = (-2)^4 - (-3)^3$

**Exercise 7. Finding an Unknown Segment Endpoint.**  
Given $A(-3\,;\,5)$ and midpoint $I(1\,;\,2)$ of segment $[AB]$. Find the coordinates of endpoint $B$.

**Exercise 8. Parallelogram Verification via Diagonals.**  
Given four points: $A(-2\,;\,1)$, $B(3\,;\,4)$, $C(5\,;\,1)$, and $D(0\,;\,-2)$.  
1. Compute the midpoint of diagonal $[AC]$.  
2. Compute the midpoint of diagonal $[BD]$.  
3. What can you deduce about the geometric nature of quadrilateral $ABCD$?

**Exercise 9. The Circumscribed Circle.**  
In an orthonormal plane, consider $E(-4\,;\,0)$ and $F(2\,;\,8)$.  
1. Calculate the coordinates of center $O'$ of the circle with diameter $[EF]$.  
2. Calculate the length of diameter $EF$, then radius $R$.  
3. Does point $G(2\,;\,0)$ lie on this circle?

**Exercise 10. Triangle Classification.**  
Given $K(-1\,;\,2)$, $L(3\,;\,5)$, and $M(3\,;\,-1)$.  
1. Calculate the exact side lengths $KL$, $LM$, and $KM$.  
2. Is triangle $KLM$ isosceles? Is it right-angled?

**Exercise 11. Squares and Powers of Negative Numbers.**  
Insert $<$ or $>$:  
1. $(-5)^2 \dots 0$  
2. $-5^2 \dots 0$  
3. $(-2)^3 \dots (-2)^2$  
4. $(-1)^{100} \dots (-1)^{101}$

#### Level ★★★ (Challenges and Analytic Geometry)

**Exercise 12. Pirate Treasure Hunt.**  
On a map where origin $O(0\,;\,0)$ is the old island lighthouse, a treasure chest is buried at point $T$.  
The pirate log reads:  
- Start from cove $A(-6\,;\,-4)$.  
- The treasure $T$ lies along the straight line toward cave $B(6\,;\,4)$, three-quarters of the way from $A$ to $B$.  
1. What are the coordinates of treasure $T$?  
2. What distance in meters separates the lighthouse from treasure $T$ ($1\text{ grid unit} = 10\text{ meters}$)?

**Exercise 13. Point Reflection Across a Center.**  
Let $A(2\,;\,-3)$ and center of symmetry $S(-1\,;\,1)$. Point $A'$ is the reflection of $A$ across $S$.  
1. What does point $S$ represent for segment $[AA']$?  
2. Determine algebraically the coordinates of point $A'$.

**Exercise 14. Sign Rule via Arithmetic Sequences.**  
Construct a multiplication table with $-3, -2, -1, 0, 1, 2, 3$ along both row and column headers. Fill the positive products first, then extend each row and column using constant step intervals. Explain why cell $(-3) \times (-3)$ must equal $+9$.

**Exercise 15. Equilateral Triangle in a Coordinate Grid.**  
Place $A(0\,;\,0)$ and $B(4\,;\,0)$ on the $x$-axis.  
1. What must be the coordinates of point $C$ (with positive $y$-coordinate) such that triangle $ABC$ is equilateral?  
2. Are the coordinates of $C$ rational or irrational? Justify.

---

### Solutions

**Exercise 1.**  
$A(-3\,;\,2)$; $B(4\,;\,2)$; $C(4\,;\,-1)$; $D(-3\,;\,-1)$.

**Exercise 2.**  
1. $(-7) \times (-6) = +42$.  
2. $(-8) \times (+9) = -72$.  
3. $(+12) \times (-5) = -60$.  
4. $\frac{-72}{-8} = +9$.  
5. $\frac{-42}{+7} = -6$.

**Exercise 3.**  
1. 3 negative factors (odd) $\implies$ **negative**.  
2. 6 negative factors (even) $\implies$ **positive**.  
3. 15 negative factors (odd) $\implies$ **negative** (positive factors do not alter the sign).

**Exercise 4.**  
$x_I = \frac{2 + 8}{2} = 5$; $y_I = \frac{4 + 10}{2} = 7 \implies I(5\,;\,7)$.

**Exercise 5.**  
$AB = \sqrt{(4 - 1)^2 + (6 - 2)^2} = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.

**Exercise 6.**  
1. $E = (+12) + (-10) = 2$.  
2. $F = 15 - (+12) = 3$.  
3. $G = \frac{+36}{-6} = -6$.  
4. $H = (+16) - (-27) = 16 + 27 = 43$.

**Exercise 7.**  
$1 = \frac{-3 + x_B}{2} \implies 2 = -3 + x_B \implies x_B = 5$.  
$2 = \frac{5 + y_B}{2} \implies 4 = 5 + y_B \implies y_B = -1$.  
Endpoint is $B(5\,;\,-1)$.

**Exercise 8.**  
1. Midpoint of $[AC]$: $(\frac{-2 + 5}{2}\,;\,\frac{1 + 1}{2}) = (1.5\,;\,1)$.  
2. Midpoint of $[BD]$: $(\frac{3 + 0}{2}\,;\,\frac{4 + (-2)}{2}) = (1.5\,;\,1)$.  
3. Both diagonals share the identical midpoint. A quadrilateral whose diagonals bisect each other is a **parallelogram**. Thus $ABCD$ is a parallelogram.

**Exercise 9.**  
1. Center $O'$: $(\frac{-4 + 2}{2}\,;\,\frac{0 + 8}{2}) = (-1\,;\,4)$.  
2. Diameter: $EF = \sqrt{(2 - (-4))^2 + (8 - 0)^2} = \sqrt{6^2 + 8^2} = 10 \implies R = 5$.  
3. Distance $O'G = \sqrt{(2 - (-1))^2 + (0 - 4)^2} = \sqrt{3^2 + (-4)^2} = 5$.  
   Since $O'G = R = 5$, point $G$ lies on the circle.

**Exercise 10.**  
1. $KL = \sqrt{4^2 + 3^2} = 5$; $LM = \sqrt{0^2 + (-6)^2} = 6$; $KM = \sqrt{4^2 + (-3)^2} = 5$.  
2. $KL = KM = 5 \implies$ triangle $KLM$ is **isosceles at vertex $K$**.  
   Pythagoras test: $LM^2 = 36 \neq 5^2 + 5^2 = 50$, so it is not right-angled.

**Exercise 11.**  
1. $(-5)^2 = 25 > 0$.  
2. $-5^2 = -25 < 0$.  
3. $(-2)^3 = -8 < 4 = (-2)^2$.  
4. $(-1)^{100} = +1 > -1 = (-1)^{101}$.

**Exercise 12.**  
1. Vector displacement from $A$ to $B$: horizontal $\Delta x = 12$, vertical $\Delta y = 8$.  
   Three-quarters displacement: $\Delta x' = 9$, $\Delta y' = 6$.  
   $x_T = -6 + 9 = 3$ and $y_T = -4 + 6 = 2 \implies T(3\,;\,2)$.  
2. Distance $OT = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3.6055\text{ units}$.  
   In meters: $3.6055 \times 10\text{ m} \approx 36.1\text{ meters}$.

**Exercise 13.**  
1. Point $S$ is the midpoint of segment $[AA']$.  
2. $-1 = \frac{2 + x_{A'}}{2} \implies x_{A'} = -4$; $1 = \frac{-3 + y_{A'}}{2} \implies y_{A'} = 5$.  
   $A'(-4\,;\,5)$.

**Exercise 14.**  
Along row $-3$: $(-3) \times 3 = -9$, $(-3) \times 2 = -6$, $(-3) \times 1 = -3$, $(-3) \times 0 = 0$. Moving left steps up by $+3$. Continuing the sequence: $(-3) \times (-1) = 3$, $(-3) \times (-2) = 6$, $(-3) \times (-3) = 9$. The cell must equal $+9$.

**Exercise 15.**  
1. Base $AB = 4$, midpoint at $x = 2$. Apex $C$ has $x_C = 2$.  
   Altitude $h = \sqrt{4^2 - 2^2} = \sqrt{12} = 2\sqrt{3}$. Thus $C(2\,;\,2\sqrt{3})$.  
2. Abscissa $2$ is rational ($\mathbb{Q}$), but ordinate $2\sqrt{3}$ is an **irrational number** because $\sqrt{3}$ is irrational.

---

### The Question That Opens What Follows

With Cartesian coordinates, we can locate any individual point or buried chest across space.  
Yet what happens when a tax collector must levy fair contributions from hundreds of merchants of wildly differing wealth, or when a school must summarize the test scores of an entire class in a single representative figure?

How do we compare portions fairly when group totals are never the same? That is the power of **percentages**, and the birth of **statistics**—with means, medians, and frequency diagrams—in our final chapter!
