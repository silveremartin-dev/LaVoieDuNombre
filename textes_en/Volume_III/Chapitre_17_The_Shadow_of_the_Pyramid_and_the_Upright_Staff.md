# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)
## CHAPTER 17: The Shadow of the Pyramid and the Upright Staff

> *“Why risk one's life attempting to scale a mountain of stone? When the sun illuminates the world, every creature casts upon the earth a faithful mirror of its own height. One must simply learn to read the shadow.”*

---

### What You Are About to Discover

- The historic challenge of **Thales of Miletus** at the foot of the Great Pyramid of Giza.
- What an **enlargement** or **reduction** by scale factor $k$ truly means.
- The astonishing geometric effect of factor $k$ on our physical universe: why lengths scale by $k$, surface areas by $k^2$, and volumes by $k^3$.
- **Thales' Theorem** in its two classic configurations: nested triangles and the hourglass (butterfly).
- The equality of the three side ratios and the foolproof technique of cross-multiplication.
- The **Converse of Thales' Theorem** to prove beyond doubt that two lines are parallel.
- 🛠️ The Boundary Case Laboratory: extreme scaling limits, Galileo's giant bone paradox, and the pinhole camera (*camera obscura*).

---

### 1. The Problem: The Pharaoh's Insolent Challenge

The desert wind whips up golden dust swirls across the Giza plateau in Egypt, twenty-six hundred years ago. Before you looms the Great Pyramid of Pharaoh Khufu: an artificial mountain of solid limestone soaring to a dizzying height.

Pharaoh Amasis gathers his high priests, court architects, and surveyors at the foot of the stone giant:  
*“Who among you is wise enough to determine the exact vertical height of this sacred tomb, from the bedrock of the earth to the gilded peak that touches the sky?”*

The master builders lower their eyes in embarrassment:  
*“Your Majesty, the four faces are polished smooth as glass and slope steeply toward the heavens. No man can climb with a surveyor's measuring chain without slipping and falling one hundred and forty meters to his death!”*

A foreign traveler, hailing from the Greek city of Miletus and cloaked in a simple woolen mantle, steps calmly forward. His name is **Thales**.  
Thales gazes up at the stone colossus, observes the blazing sun in the azure sky, and smiles:  
*“Your Majesty, I have no need to climb your pyramid. Hand me a simple wooden walking staff, and before sunset, I shall give you the exact height of the monument without ever lifting my feet from the ground!”*

The Egyptian courtiers scoff. How could an itinerant Greek merchant measure a stone mountain with a common piece of wood?

```
      Sunlight Ray
            \
             \
              \      Pyramid Summit (Unknown Height H)
               \     ▲
                \   / \
                 \ /   \
                  /     \
                 /       \           Staff Top (Height h = 2 m)
                /         \             |
    ───────────●───────────●────────────●─────────► Ground
               |◄─── Shadow L ──►|      |◄─ l ─►| (Staff shadow)
```

---

### 2. From the Magic Instant to Universal Proportions

#### 2.1 The First Insight: The Magic Hour

Thales sits in the warm sand and carefully observes the path of the sun.
- Early in the morning, the sun sits low on the horizon: shadows stretch out enormously across the plain.
- At noon, the sun reaches its zenith overhead: shadows shrink to tiny pools huddled under one's feet.
- Through the afternoon, the sun descends again, and the shadows begin to lengthen once more.

Thales drives his wooden staff vertically into the sand. The staff stands exactly **2 meters tall**.  
He marks a tick mark in the sand and tracks the tip of the staff's shadow:
- At 2:00 PM, the shadow measures $1.20\text{ m}$ (shorter than the staff).
- At 3:00 PM, it measures $1.60\text{ m}$.
- Suddenly, at **3:45 PM**, Thales measures the shadow again: **it measures precisely 2 meters!**

At that singular instant, a geometric miracle occurs:
$$\text{Length of Staff's Shadow} = \text{Actual Height of Staff} = 2\text{ meters}$$

The sunlight strikes the ground at an angle of exactly $45^\circ$, forming an **isosceles right-angled triangle** with the upright staff and the horizontal ground.  
Thales shouts to the servants: *“Measure the shadow of the pyramid right now!”*  
At that exact second, the length of the pyramid's shadow (measured from the vertical line below its apex to the far tip of its shadow) is **strictly equal to its true vertical height**!

> **💡 Did You Know?** According to the Greek historian Plutarch, Pharaoh Amasis was so utterly astonished to see Thales determine the monument's height in just a few paces that he showered the philosopher with gifts and revered him as the wisest living mortal.

#### 2.2 What If the Sun Won't Wait? The Power of Proportion

The “magic hour” technique is brilliant, but it has one glaring limitation: one must wait for the exact moment when the solar angle reaches $45^\circ$. What if a storm cloud hides the sun at 3:45 PM? What if you must measure a tall tree at 10:00 AM?

Thales realized a far deeper truth: **sunlight rays, arriving from an astronomical body 150 million kilometers away, reach the surface of the Earth along lines that are virtually parallel to one another.**

Therefore, at **any hour of the day**, the pyramid and its shadow form a triangle that has the **exact same geometric shape** as the triangle formed by the staff and its shadow! One triangle is simply an **enlargement** of the other.

```
       Pyramid Triangle                         Staff Triangle
                 S                                    A
                /|                                   /|
               / |                                  / |
              /  |                                 /  |
             /   | Height H                       /   | Height h
            /    |                               /    |
           /     |                              /     |
          /______|                             /______|
         O       H'                           B       C
          Shadow L                             Shadow l
```

The ratio between vertical height and cast shadow is **identical for all vertical objects standing under the sun at that same moment**:
$$\frac{\text{Pyramid Height}}{\text{Pyramid Shadow}} = \frac{\text{Staff Height}}{\text{Staff Shadow}} \iff \frac{H}{L} = \frac{h}{l}$$

Hence, the formula that delivers the height at any time without waiting:
$$H = L \times \frac{h}{l}$$

---

### 3. Enlargement, Reduction, and the Dimensional Trap

Before stating the theorem in its full mathematical generality, let us pause to examine what it truly means to “enlarge” or “reduce” a geometric shape. This is an area where human intuition is easily deceived!

#### 3.1 The Scale Factor $k$

> **📐 Definition — Enlargement and Reduction**  
> - Transforming a figure by multiplying **all its linear dimensions** by the same strictly positive number $k$ is called:
>   - An **enlargement** (or dilation) if $k > 1$.
>   - A **reduction** (or contraction) if $0 < k < 1$.
> - The constant multiplier $k$ is called the **scale factor** (or scale ratio).
> - In an enlargement or reduction, **the overall shape is strictly preserved**: angles remain completely unchanged, and parallel lines remain parallel.

#### 3.2 The Effect on Lengths, Areas, and Volumes

Here is the golden rule that governs the geometry of our three-dimensional physical universe:

> **📐 Fundamental Scaling Theorem — The Powers of Factor $k$**  
> When all linear dimensions of a figure or solid are multiplied by a scale factor $k$ ($k > 0$):
> - **Lengths** are multiplied by $k$.
> - **Surface areas** are multiplied by $k^2$ ($k \times k$).
> - **Volumes** are multiplied by $k^3$ ($k \times k \times k$).

#### Why Squares and Cubes? The Visual Proof with Blocks

Take a small modeling-clay cube measuring $1\text{ cm}$ along each edge:
- Its edge length is $1\text{ cm}$.
- The surface area of one square face is $1 \times 1 = 1\text{ cm}^2$.
- Its solid volume is $1 \times 1 \times 1 = 1\text{ cm}^3$.

Now perform an enlargement with scale factor **$k = 2$** (doubling all linear dimensions: edge $= 2\text{ cm}$):

```
        Initial Cube (k = 1)           Enlarged Cube (k = 2)
             ┌─┐                            ┌───┬───┐
             │ │                            │   │   │  4 small cubes in front
             └─┘                            ├───┼───┤
          Edge = 1 cm                       │   │   │
          Face area = 1 cm²                 └───┴───┘
          Volume = 1 cm³                + 4 small cubes in back!
                                        Total = 8 cubes = 2³
```

Look closely:
1. The edge length was multiplied by **$2$** ($2\text{ cm}$).
2. The area of a square face: it now contains $2 \times 2 = 4$ unit squares. It was multiplied by $2^2 = \mathbf{4}$!
3. The solid volume: to build the new cube of edge $2\text{ cm}$, you need 4 unit cubes on the bottom tier and 4 unit cubes on the top tier, totaling $2 \times 2 \times 2 = 8$ unit cubes. The volume was multiplied by $2^3 = \mathbf{8}$!

If we tripled all linear dimensions ($k = 3$):
- Lengths would scale by $\times 3$.
- Surface areas would scale by $\times 3^2 = \mathbf{9}$.
- Volumes would scale by $\times 3^3 = \mathbf{27}$!

> **💡 Did You Know? — Why Giant Movie Monsters Cannot Exist**  
> Galileo Galilei was the first to demonstrate this mathematical reality: if a human being were enlarged to 10 times his normal height ($k = 10$), he would be 10 times taller, but his body weight (which depends on volume) would multiply by $10^3 = \mathbf{1,000}$!  
> However, the mechanical strength of his leg bones (which depends on their cross-sectional area) would only multiply by $10^2 = \mathbf{100}$. His bones would experience 10 times the normal stress: they would snap under his own weight at his very first step!

---

### 4. Thales' Theorem in Triangles

Let us formulate this foundational theorem as it appears in standard Euclidean geometry.

#### 4.1 The Two Canonical Configurations

Thales' Theorem applies whenever a straight line intersects two sides of a triangle while being strictly **parallel** to the third side. There are two geometric arrangements:

```
    Configuration 1: Nested Triangles              Configuration 2: Hourglass (Butterfly)
                     A                                            M       N
                    / \                                            \     /
                   /   \                                            \   /
                  M─────N   (MN) // (BC)                             \ /
                 /       \                                            A
                /         \                                          / \
               B───────────C                                        /   \
                                                                   B─────C   (MN) // (BC)
```

In both configurations:
- Lines $(MB)$ and $(NC)$ are secant lines intersecting at point $A$.
- Lines $(MN)$ and $(BC)$ are **strictly parallel**.

Triangle $AMN$ is a scaled replica of triangle $ABC$: it represents a reduction (or enlargement) by some factor $k$. Their corresponding angles are equal, and all pairs of corresponding sides are proportional.

#### 4.2 Formal Statement of Thales' Theorem

> **📐 Thales' Theorem (Intercept Theorem) —**  
> Let $(d)$ and $(d')$ be two straight lines intersecting at point $A$.  
> Let $B$ and $M$ be two points on $(d)$, distinct from $A$.  
> Let $C$ and $N$ be two points on $(d')$, distinct from $A$.  
> If the lines $(MN)$ and $(BC)$ are parallel, then:  
> $$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$$

Each fraction compares a side of the smaller triangle to the corresponding side of the larger triangle:
$$\frac{\text{side of } AMN}{\text{side of } ABC} = \text{scale factor } k$$

> **🧭 Method — Writing the Equal Ratios Without Error**  
> 1. Identify the **shared intersection vertex** (the point where the two secant lines cross, here $A$).  
> 2. Write the first two ratios radiating outward from this shared vertex:  
>    $\frac{A\dots}{A\dots} = \frac{A\dots}{A\dots}$ (e.g., $\frac{AM}{AB} = \frac{AN}{AC}$).  
> 3. For the third ratio, “ignore” vertex $A$ and take the two remaining letters from the numerators, then denominators: $\frac{MN}{BC}$.  
> 4. Check that all side lengths of the upper triangle ($AM, AN, MN$) reside exclusively in the **numerators**, and all side lengths of the lower triangle ($AB, AC, BC$) reside in the **denominators** (or vice versa—never mix them up!).

---

### 5. The Converse of Thales' Theorem: Proving Parallelism

Thales' Theorem asserts:
$$\text{If lines are parallel} \Longrightarrow \text{corresponding ratios are equal.}$$

What if we wish to travel in the opposite direction? Suppose we are on a construction site or surveying land, measure lengths on the ground, and need to prove with absolute certainty that two beams or property lines are **parallel**.  
That is the purpose of the **Converse of Thales' Theorem**.

> **📐 Converse of Thales' Theorem —**  
> Let $(AB)$ and $(AC)$ be two lines intersecting at $A$.  
> Let $M$ be a point on line $(AB)$ and $N$ a point on line $(AC)$.  
> If:  
> 1. The points $A, M, B$ and $A, N, C$ are aligned **in the exact same order**,  
> 2. And $\frac{AM}{AB} = \frac{AN}{AC}$,  
>  
> then the lines $(MN)$ and $(BC)$ are **parallel**.

#### The Contrapositive: Proving Lines Are NOT Parallel

If after computing the two quotients, you find that they are not equal ($\frac{AM}{AB} \neq \frac{AN}{AC}$), you can immediately conclude via the **contrapositive of Thales' Theorem** that **the lines $(MN)$ and $(BC)$ are not parallel**.

---

### 6. Beware of Pitfalls!

> **⚠️ Warning: Classic Exam Traps!**  
> 1. **Inverting Numerator and Denominator:** Writing $\frac{AM}{AB} = \frac{AC}{AN}$ is a fatal error. You have placed “small over large” on the left, and “large over small” on the right. Any cross-multiplication will be completely wrong.  
> 2. **Using the Intermediate Segment Instead of the Full Triangle Side:** In the nested configuration, the side of the larger triangle is $AB$. Some students mistakenly plug in the length $MB$. But $MB$ is not the side of any triangle! Remember: $AB = AM + MB$.  
> 3. **Omitting the Alignment Order Condition:** To apply the converse rigorously, you **must explicitly state**: *“Points $A, M, B$ on one hand, and $A, N, C$ on the other, lie in the same order along their respective lines.”*  
> 4. **Multiplying Areas by $k$ Instead of $k^2$:** If a scale model is built at scale $\frac{1}{100}$, lengths are divided by $100$, but the area of a surface on the model is divided by $100^2 = 10,000$!

---

### 7. Solved Examples

#### Solved Example 1 — Measuring the Pyramid with Historical Data
Let us compute the height of the Great Pyramid using authentic measurements:
- The staff has height $h = 2\text{ m}$. Its shadow measures $l = 3\text{ m}$.
- The pyramid has a square base measuring $230\text{ m}$ on each side.
- The shadow cast by the pyramid's apex extends $74\text{ m}$ beyond the exterior edge of its base.  
What is the vertical height $H$ of the pyramid?

```
          Summit
            ▲\
            │ \
            │  \ Slanted face
            │   \
            │    \
     ───────┼─────┴───────────●  (Tip of shadow)
            │      │◄── 74 m ──►│
            │◄ Half-base ►│
                115 m
```

*Solution:*  
1. Find total shadow length $L$, measured from directly below the summit (the center of the square base):  
   $$L = \text{half-base} + \text{exterior shadow} = \frac{230}{2} + 74 = 115 + 74 = 189\text{ m}$$  
2. Because the sun's rays are parallel, we set up Thales' proportion:  
   $$\frac{H}{h} = \frac{L}{l} \implies \frac{H}{2} = \frac{189}{3}$$  
3. Solve for $H$ using cross-multiplication:  
   $$H = \frac{2 \times 189}{3} = 2 \times 63 = 126\text{ meters}$$  
The Great Pyramid stood at approximately $126$ meters on that day (accounting for summit erosion). ✔

#### Solved Example 2 — Computing Unknown Side Lengths (Nested Configuration)
Lines $(AB)$ and $(AC)$ intersect at $A$.  
Given: $AM = 3\text{ cm}$, $AB = 7.5\text{ cm}$, $AC = 10\text{ cm}$, and $BC = 12\text{ cm}$.  
Lines $(MN)$ and $(BC)$ are parallel. Calculate lengths $AN$ and $MN$.

*Solution:*  
- Standard formal presentation:  
  In triangle $ABC$, point $M$ lies on $[AB]$ and point $N$ lies on $[AC]$.  
  Since lines $(MN)$ and $(BC)$ are parallel, by **Thales' Theorem**:  
  $$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$$  
- Substitute known numerical values:  
  $$\frac{3}{7.5} = \frac{AN}{10} = \frac{MN}{12}$$  
- Solve for $AN$:  
  $$AN = \frac{3 \times 10}{7.5} = \frac{30}{7.5} = 4\text{ cm}$$  
- Solve for $MN$:  
  $$MN = \frac{3 \times 12}{7.5} = \frac{36}{7.5} = 4.8\text{ cm}$$  
The requested lengths are $AN = 4\text{ cm}$ and $MN = 4.8\text{ cm}$. ✔

#### Solved Example 3 — The Impassable River (Hourglass Configuration)
A surveyor needs to determine the width $AB$ of a rushing river without swimming across.  
Lines $(AD)$ and $(BC)$ cross at point $O$, with $(AB) \parallel (CD)$.  
Measurements on the accessible bank yield: $OB = 12\text{ m}$, $OC = 30\text{ m}$, and $CD = 45\text{ m}$.  
Calculate distance $AB$.

```
         Tree A (Far bank)
            ●
             \
  ~~~~~~~~~~~~\~~~~~~~~~~~~~~~~~~~ River
               \
                ● B (Near bank)
                 \
                  \
                   ● O
                  / \
                 /   \
             C  ●─────● D   (Baseline CD on dry land)
```

*Solution:*  
- Lines $(AD)$ and $(BC)$ intersect at $O$, with $(AB) \parallel (CD)$.  
- By **Thales' Theorem** in the hourglass configuration:  
  $$\frac{OA}{OD} = \frac{OB}{OC} = \frac{AB}{CD}$$  
- Using the known ratio:  
  $$\frac{12}{30} = \frac{AB}{45}$$  
- Cross-multiplication:  
  $$AB = \frac{12 \times 45}{30} = \frac{540}{30} = 18\text{ meters}$$  
The distance across the river is $18\text{ meters}$. ✔

#### Solved Example 4 — Proving Parallelism with the Converse
Consider triangle $ABC$ with $AB = 6\text{ cm}$ and $AC = 8\text{ cm}$.  
On ray $[AB)$, mark point $E$ such that $AE = 15\text{ cm}$.  
On ray $[AC)$, mark point $F$ such that $AF = 20\text{ cm}$.  
Are lines $(BC)$ and $(EF)$ parallel?

*Solution:*  
- Compute both ratios separately:  
  $$\frac{AB}{AE} = \frac{6}{15} = \frac{2}{5} = 0.4$$  
  $$\frac{AC}{AF} = \frac{8}{20} = \frac{2}{5} = 0.4$$  
- We observe that:  
  $$\frac{AB}{AE} = \frac{AC}{AF}$$  
- Formal conclusion:  
  Points $A, B, E$ on one hand, and $A, C, F$ on the other, lie in the same order along their lines.  
  Furthermore, $\frac{AB}{AE} = \frac{AC}{AF}$.  
  Therefore, by the **Converse of Thales' Theorem**, lines $(BC)$ and $(EF)$ are strictly parallel. ✔

#### Solved Example 5 — The Skyscraper Architectural Model
An architecture firm builds a scale model of a planned glass skyscraper at scale $\frac{1}{200}$.  
1. The model stands $1.40\text{ m}$ tall. What will be the actual height of the skyscraper?  
2. The model uses $0.35\text{ m}^2$ of glass siding. What total area of glass will the actual tower require?  
3. The interior volume of the model is $0.05\text{ m}^3$. What will be the actual building volume?

*Solution:*  
Moving from the model to the real structure represents an enlargement by factor $K = 200$.  
1. **Lengths ($K = 200$):**  
   $$\text{Actual Height} = 1.40 \times 200 = 280\text{ meters}$$  
2. **Areas ($K^2 = 200^2 = 40,000$):**  
   $$\text{Actual Glass Area} = 0.35 \times 40,000 = 14,000\text{ m}^2$$  
3. **Volumes ($K^3 = 200^3 = 8,000,000$):**  
   $$\text{Actual Volume} = 0.05 \times 8,000,000 = 400,000\text{ m}^3$$  
Notice the dimensional explosion: the real volume is eight million times greater than the model's! ✔

---

### What You Must Remember

1. **Enlargement and Reduction:**  
   - Scale factor $k > 1$ represents an enlargement; $0 < k < 1$ represents a reduction.  
   - Dimensional consequences:  
     - Lengths scale by $k$  
     - Surface areas scale by $k^2$  
     - Volumes scale by $k^3$  
2. **Thales' Theorem (Length Calculations):**  
   - **Hypothesis:** Two lines intersecting at $A$, cut by parallel lines $(MN)$ and $(BC)$.  
   - **Conclusion:** $\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$.  
3. **Converse of Thales (Proof of Parallelism):**  
   - **Hypothesis:** Points aligned in the same order on two intersecting lines, AND $\frac{AM}{AB} = \frac{AN}{AC}$.  
   - **Conclusion:** Lines $(MN)$ and $(BC)$ are parallel.  
   - If the ratios differ, the **contrapositive** proves the lines are not parallel.

---

### Exercises

#### Level ★ (Direct Application)

**Exercise 1.** Apply an enlargement of scale factor $k = 3$ to a triangle whose sides measure $4\text{ cm}$, $5\text{ cm}$, and $6\text{ cm}$. What are the side lengths of the enlarged triangle?

**Exercise 2.** A square has an area of $25\text{ cm}^2$. We reduce its side lengths by scale factor $k = 0.4$.  
1. What is the side length of the original square?  
2. What is the side length of the reduced square?  
3. What is the area of the reduced square? Verify that $\text{Area}' = k^2 \times \text{Area}$.

**Exercise 3.** In triangle $ABC$, point $M \in [AB]$ and point $N \in [AC]$ with $(MN) \parallel (BC)$.  
Given $AM = 2\text{ cm}$, $AB = 6\text{ cm}$, and $AN = 3\text{ cm}$. Calculate length $AC$.

**Exercise 4.** Hourglass configuration: lines $(AB)$ and $(CD)$ intersect at $O$, with $(AC) \parallel (BD)$.  
Given $OA = 5\text{ cm}$, $OB = 15\text{ cm}$, and $AC = 4\text{ cm}$. Calculate length $BD$.

**Exercise 5.** On line $(d)$, $AM = 4\text{ cm}$ and $AB = 10\text{ cm}$. On intersecting line $(d')$, $AN = 6\text{ cm}$ and $AC = 15\text{ cm}$. Are the ratios $\frac{AM}{AB}$ and $\frac{AN}{AC}$ equal?

#### Level ★★ (Reasoning and Geometric Deductions)

**Exercise 6. The Height of the Church Belfry.**  
One sunny afternoon, a pedestrian $1.80\text{ m}$ tall casts a shadow of $2.40\text{ m}$ across a stone courtyard.  
At the exact same instant, the shadow cast by the church belfry measures $36\text{ meters}$.  
What is the vertical height of the belfry?

**Exercise 7. The Mid-Segment Trap!**  
In triangle $ABC$, $AB = 12\text{ cm}$ and $AC = 16\text{ cm}$. Point $M$ lies on $[AB]$ such that $MB = 3\text{ cm}$. The parallel to $(BC)$ through $M$ intersects $[AC]$ at $N$.  
1. Calculate length $AM$.  
2. Calculate length $AN$, then length $NC$.

**Exercise 8. The Wall Shelves.**  
A carpenter mounts two horizontal wooden shelves $[MN]$ and $[BC]$ between two sloping struts that meet at apex $A$.  
Given: $AM = 45\text{ cm}$, $MB = 30\text{ cm}$, and shelf $MN = 60\text{ cm}$.  
Since both shelves are horizontal, $(MN) \parallel (BC)$. Calculate the length of the lower shelf $[BC]$.

**Exercise 9. Parallelism Check.**  
In triangle $RST$, $RS = 7\text{ cm}$ and $RT = 9\text{ cm}$.  
Point $P$ is placed on $[RS]$ such that $RP = 2.8\text{ cm}$, and point $Q$ on $[RT]$ such that $RQ = 3.6\text{ cm}$.  
Are lines $(PQ)$ and $(ST)$ parallel? Write out your proof carefully.

**Exercise 10. The Non-Parallel Counterexample.**  
In triangle $ABC$, $AB = 5\text{ cm}$ and $AC = 8\text{ cm}$. Point $D$ lies on $[AB]$ with $AD = 2\text{ cm}$, and point $E$ on $[AC]$ with $AE = 3\text{ cm}$.  
Are lines $(DE)$ and $(BC)$ parallel? Justify your answer.

**Exercise 11. Painting a Billboard: The $k^2$ Factor.**  
A commercial painter takes 2 hours and uses a 5-liter can of paint to cover a square billboard measuring $3\text{ meters}$ on each side.  
How many cans of paint and how many hours of labor will he require to paint a giant billboard of the same shape measuring $9\text{ meters}$ on each side (assuming he works at the same pace)?

#### Level ★★★ (Challenges and Modeling)

**Exercise 12. Surveying Across a Marsh.**  
To measure the distance between two survey beacons $A$ and $B$ separated by a deep swamp, a surveyor selects an observation station $S$ on dry ground from which both $A$ and $B$ are visible.  
He measures on dry land: $SA = 120\text{ m}$ and $SB = 150\text{ m}$.  
He extends sightlines straight past $S$:  
On the ray opposite to $[SA)$, he marks point $A'$ with $SA' = 40\text{ m}$.  
On the ray opposite to $[SB)$, he marks point $B'$ with $SB' = 50\text{ m}$.  
He measures the distance between the pegs directly on the meadow: $A'B' = 36\text{ m}$.  
1. Prove that line $(A'B')$ is parallel to line $(AB)$.  
2. Determine the inaccessible distance $AB$ across the swamp.

**Exercise 13. Slicing the Cake into Equal Areas.**  
A baker bakes a triangular pastry $ABC$ of vertical height $18\text{ cm}$.  
He wishes to divide it into three portions of equal surface area using two horizontal cuts parallel to base $[BC]$, located at heights $h_1$ and $h_2$ below apex $A$.  
1. By what scale factor is the surface area multiplied when moving from the small top triangle to the middle triangle? And to the full pastry?  
2. At what exact vertical distances $h_1$ and $h_2$ from vertex $A$ must the cuts be made?

**Exercise 14. The Frustum of the Pyramid.**  
Consider a regular square pyramid of base side $10\text{ m}$ and height $12\text{ m}$.  
Its total volume is $V = \frac{1}{3} \times \text{Base} \times \text{Height} = \frac{1}{3} \times 100 \times 12 = 400\text{ m}^3$.  
The pyramid is sliced horizontally at mid-height ($6\text{ m}$ from the summit) by a plane parallel to the base.  
1. What is the reduction scale factor $k$ of the smaller upper pyramid?  
2. What is the volume of the small removed pyramid?  
3. What is the volume of the remaining lower “frustum”? What fraction of the total volume does it represent?

**Exercise 15. Thales in Optics: The Pinhole Camera (*Camera Obscura*).**  
The earliest camera is a lightproof box with a tiny pinhole $O$ in its front face.  
A tree $15\text{ meters}$ tall stands $30\text{ meters}$ in front of the pinhole.  
The depth of the camera box from the pinhole to the rear photographic plate is $20\text{ centimeters}$.  
1. Sketch a ray diagram showing light rays crossing at pinhole $O$. Is the projected image upright or upside-down?  
2. What will be the vertical height of the tree's image formed on the photographic plate?

---

### Solutions

**Exercise 1.**  
Each side is multiplied by $3$: $12\text{ cm}$, $15\text{ cm}$, and $18\text{ cm}$.

**Exercise 2.**  
1. Side of original square: $\sqrt{25} = 5\text{ cm}$.  
2. Side of reduced square: $5 \times 0.4 = 2\text{ cm}$.  
3. Area of reduced square: $2 \times 2 = 4\text{ cm}^2$.  
   Check: $k^2 \times \text{Area} = 0.4^2 \times 25 = 0.16 \times 25 = 4\text{ cm}^2$. Exact!

**Exercise 3.**  
By Thales' Theorem: $\frac{AM}{AB} = \frac{AN}{AC} \implies \frac{2}{6} = \frac{3}{AC} \implies AC = \frac{6 \times 3}{2} = 9\text{ cm}$.

**Exercise 4.**  
Hourglass configuration: $\frac{OA}{OB} = \frac{AC}{BD} \implies \frac{5}{15} = \frac{4}{BD} \implies BD = \frac{15 \times 4}{5} = 12\text{ cm}$.

**Exercise 5.**  
$\frac{AM}{AB} = \frac{4}{10} = 0.4$ and $\frac{AN}{AC} = \frac{6}{15} = 0.4$. Yes, both ratios are equal.

**Exercise 6.**  
Sunlight parallelism: $\frac{H_{\text{belfry}}}{h_{\text{man}}} = \frac{L_{\text{belfry}}}{l_{\text{man}}} \implies \frac{H}{1.80} = \frac{36}{2.40} \implies H = \frac{1.80 \times 36}{2.40} = 27\text{ meters}$.

**Exercise 7.**  
1. $AM = AB - MB = 12 - 3 = 9\text{ cm}$.  
2. Thales: $\frac{AM}{AB} = \frac{AN}{AC} \implies \frac{9}{12} = \frac{AN}{16} \implies AN = \frac{9 \times 16}{12} = 12\text{ cm}$.  
   $NC = AC - AN = 16 - 12 = 4\text{ cm}$.

**Exercise 8.**  
Total leg $AB = AM + MB = 45 + 30 = 75\text{ cm}$.  
Thales: $\frac{AM}{AB} = \frac{MN}{BC} \implies \frac{45}{75} = \frac{60}{BC} \implies BC = \frac{75 \times 60}{45} = 100\text{ cm} = 1\text{ meter}$.

**Exercise 9.**  
Compute separately: $\frac{RP}{RS} = \frac{2.8}{7} = 0.4$ and $\frac{RQ}{RT} = \frac{3.6}{9} = 0.4$.  
Points $R, P, S$ and $R, Q, T$ lie in the same order. Since $\frac{RP}{RS} = \frac{RQ}{RT}$, by the Converse of Thales' Theorem, lines $(PQ)$ and $(ST)$ are parallel.

**Exercise 10.**  
$\frac{AD}{AB} = \frac{2}{5} = 0.40$ while $\frac{AE}{AC} = \frac{3}{8} = 0.375$.  
Since $\frac{AD}{AB} \neq \frac{AE}{AC}$, by the contrapositive of Thales' Theorem, lines $(DE)$ and $(BC)$ are not parallel.

**Exercise 11.**  
Linear dimension scales by $k = \frac{9}{3} = 3$.  
Surface area scales by $k^2 = 3^2 = 9$.  
- Paint: $5\text{ L} \times 9 = 45\text{ liters}$ (9 cans).  
- Time: $2\text{ h} \times 9 = 18\text{ hours}$ of labor.

**Exercise 12.**  
1. Points $A', S, A$ and $B', S, B$ are aligned in order.  
   Ratios: $\frac{SA'}{SA} = \frac{40}{120} = \frac{1}{3}$ and $\frac{SB'}{SB} = \frac{50}{150} = \frac{1}{3}$.  
   By the Converse of Thales' Theorem, $(A'B') \parallel (AB)$.  
2. By Thales: $\frac{A'B'}{AB} = \frac{1}{3} \implies AB = 3 \times 36 = 108\text{ meters}$.

**Exercise 13.**  
1. Let $A$ be total area. Top portion $= \frac{1}{3}A$, middle triangle $= \frac{2}{3}A$. Area scale factors are $\frac{1}{3}$ and $\frac{2}{3}$. Linear scale factors are square roots of area ratios: $k_1 = \sqrt{1/3}$ and $k_2 = \sqrt{2/3}$.  
2. $h_1 = 18 \times \frac{1}{\sqrt{3}} = 6\sqrt{3} \approx 10.39\text{ cm}$.  
   $h_2 = 18 \times \sqrt{\frac{2}{3}} = 6\sqrt{6} \approx 14.70\text{ cm}$.

**Exercise 14.**  
1. Cut at half-height ($6\text{ m}$ of $12\text{ m}$): $k = \frac{6}{12} = \frac{1}{2} = 0.5$.  
2. Volume scales by $k^3 = (1/2)^3 = 1/8$. $V_{\text{small}} = \frac{1}{8} \times 400 = 50\text{ m}^3$.  
3. Volume of frustum: $V_{\text{frustum}} = 400 - 50 = 350\text{ m}^3$.  
   It accounts for $\frac{350}{400} = \frac{7}{8}$ (87.5%) of the pyramid's entire volume!

**Exercise 15.**  
1. Light rays travel in straight lines through pinhole $O$: the ray from the treetop hits the bottom of the plate, and the ray from the base hits the top. The image is formed **upside-down (inverted)**.  
2. Hourglass configuration: Object distance $D = 30\text{ m} = 3,000\text{ cm}$; Camera depth $d = 20\text{ cm}$; Tree height $H = 15\text{ m} = 1,500\text{ cm}$.  
   $\frac{h}{H} = \frac{d}{D} \implies \frac{h}{1,500} = \frac{20}{3,000} = \frac{1}{150} \implies h = \frac{1,500}{150} = 10\text{ cm}$.  
The tree projects an inverted miniature image $10\text{ cm}$ tall.

---

### The Question That Opens What Follows

When we scale a 3D pyramid or cube, its volume multiplies by $k^3$: it explodes upward at tremendous speed. But what happens when we do not merely triple a dimension once, but repeat a multiplication dozens of times in succession?

It is the legend of an Eastern king who thought he was granting a humble handful of rice to the inventor of chess, only to discover his entire empire buried beneath a mountain of grain. Welcome to the dizzying universe of **exponents, order of operations, and scientific notation**!
