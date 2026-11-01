# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 26: Paper Folding and the Magic Mirror

> *“Observe a raindrop falling into a calm lake, the wings of a butterfly opening to the sun, or the face of a dear friend: nature never selects its shapes by accident. It builds in the mirror of symmetry, for that which is symmetrical distributes forces, balances masses, and endures against the tempest.”*

---

### What You Are About to Discover

- The secret of medieval master builders: why asymmetry tears down stone bridges, and how the **perpendicular bisector** and **angle bisector** produce geometric harmony.
- The grand family of plane geometric transformations:
  - **Axial reflection (line symmetry)**: paper folding and the mirror image.
  - **Point reflection (central symmetry)**: the perfect half-turn ($180^\circ$) around a pivot.
  - **Translation**: rectilinear sliding without the slightest rotation.
  - **Rotation**: controlled whirling through a given angle around a center.
  - **Dilation (homothety)**: the optical zoom lens shrinking or expanding space by a scale factor $k$.
- The properties these transformations **preserve**: lengths, angles, parallelism, and areas.
- The vital distinction between **congruent triangles** (identical clones) and **similar triangles** (identical silhouette at different scales).
- The enchanting art of **friezes and tessellations**: from the arabesques of the Alhambra in Granada to the impossible metamorphoses of Maurits Cornelis Escher.

---

### 1. The Problem: The Collapsing Bridge and the Well Dispute

In the 12th century, within a steep gorge of the Auvergne mountains, local villagers decided to construct a massive stone arch bridge across a roaring river. The master mason was in a hurry: he cut unequal voussoirs and erected an arch leaning noticeably to the right, much heavier on one flank than the other. The arch was picturesque, but dangerously unbalanced.

A few months later, the first heavy autumn flood arrived. The torrent surged, and howling winds rushed through the ravine. The heavier side pulled relentlessly upon the thinner side. A winding crack snaked across the vault... and with a deafening roar of crushed masonry, **the bridge collapsed into the abyss**!

```
             Leaning Arch (Unstable)                  Symmetric Arch (Eternal)
                     /\                                     /¯¯\
                    /  \___                                /    \
                   /       \                              /      \
               ───┴─────────┴───                      ───┴────────┴───
               Unbalanced forces                      Distributed forces
```

The master builder summoned his apprentices around his drafting table:
*“Carve this into your memories: stone forgives surface roughness, but it never forgives asymmetry. When an arch lacks its mirror axis, the weight of the heavens bears down on a single abutment, and ruin is certain.”*

A few leagues away, another dispute arose between two neighboring villages, Arras and Béthune, separated by six kilometers of open heath. The local count decided to sink a large stone well in the plain to water livestock and travelers.

Instantly, discord erupted:
*“Dig the well right near our church bell tower!”* demanded the villagers of Arras.
*“Out of the question!”* retorted the folk of Béthune. *“That would be blatant favoritism! We insist that the walking distance be strictly equal for both villages!”*

A child suggested: *“Let us dig the well right in the middle of the footpath connecting the two villages!”*
That was a sound idea: at 3 kilometers from Arras and 3 kilometers from Béthune, the location was fair.
Yet the commander's surveyor stepped forward and scored a deep trench across the soil with his spear:
*“There is not merely one possible location: there are infinitely many fair locations for the well!”*

```
                     Axis of the Perpendicular Bisector (d)
                                      ▲
                                      │  Potential Well 1 (Equidistant!)
                                      ●
                                    / │ \
                                  /   │   \
                                /     │     \
         Village A o───────────┼─────o─────┼───────────o Village B
         (Arras)               │  Midpoint │           (Béthune)
                               \     │     /
                                 \   │   /
                                   \ │ /
                                     ●  Potential Well 2 (Equidistant!)
                                     │
```

This perpendicular line cutting the path precisely at its midpoint possesses a magical geometric property: **every single point on this line is situated at the exact same distance from Village A and Village B**.
This line of absolute equity is called **the perpendicular bisector**.

To master architecture, art, and machinery, we must understand the fundamental laws governing plane motion: **geometric transformations**.

---

### 2. The Two Mirrors: Axial Reflection and Point Reflection

A **geometric transformation** is a rule that maps each point in the plane to a new position according to a strict geometric prescription. The original point is called the preimage $M$, and the resulting point is called its **image** $M'$.

#### 2.1 Axial Reflection: Paper Folding Along a Line

Take a sheet of paper, place a drop of wet ink on the left side, fold the sheet in half along a straight crease $(d)$, and press down firmly. When unfolded, the ink blot has imprinted itself on the other side.

> **📐 Definition — Axial Reflection (across line $(d)$).**
> - The image of a point $M$ lying off $(d)$ is the point $M'$ such that the line $(d)$ is the **perpendicular bisector** of the segment $[M M']$.
>   This means that $(d)$ is perpendicular to $[M M']$ and passes through its midpoint.
> - If a point $M$ lies directly on the axis $(d)$, its image is itself: $M' = M$ (such a point is called an **invariant point** or fixed point).

```
                      M ●
                         \
                          \  (d) Axis of Reflection
                           \  │
                            \ │
                             \┼─ Right angle
                              │\  Distance = Distance
                              │ \
                              │  \
                                  ● M'
```

*The Mirror Effect:* Axial reflection reverses orientation! Your right hand reflects as a left hand in a mirror. If the vertices of a triangle proceed clockwise ($A \to B \to C$), their reflected images will proceed counterclockwise.

#### 2.2 Point Reflection (Central Symmetry): The Half-Turn Around a Pivot

Now imagine placing a pushpin into your paper at point $O$, and rotating the tracing paper through an **exact half-turn ($180^\circ$)**.

> **📐 Definition — Point Reflection (Central Inversion across center $O$).**
> The image of a point $M$ under point reflection centered at $O$ is the point $M'$ such that **point $O$ is the midpoint of the segment $[M M']$**.

```
                M ●───────────────o───────────────● M'
                         OM   =   O   =   OM'
```

*Essential Property:*
A point reflection transforms any line $(d)$ into a line $(d')$ that is **strictly parallel** to it! It preserves orientation (a clockwise loop remains clockwise after a $180^\circ$ rotation).

---

### 3. The Two Rigid Motions: Translation and Rotation

#### 3.1 Translation: The Pure Slide

Picture opening a desk drawer, or a train speeding along straight tracks. Every point of the object glides by the exact same distance, along the same direction, and in the same sense.

> **📐 Definition — Translation.**
> A **translation** slides a geometric figure from point $A$ to point $B$.
> The image of any point $M$ is the point $M'$ such that:
> 1. The lines $(AB)$ and $(M M')$ are **parallel** (same direction).
> 2. Motion from $M$ to $M'$ has the **same sense** (orientation) as motion from $A$ to $B$.
> 3. The length $M M' = AB$ (same distance).
> 
> *In summary:* The quadrilateral $ABM'M$ is a **parallelogram** (possibly degenerate).

```
                 A ●────────────────────────────>● B
                          (Displacement Vector)
                 
                 M ●────────────────────────────>● M'
```

In a translation, the figure glides without rotating by a hair. It models footprints left in sequence across beach sand.

#### 3.2 Rotation: The Controlled Swirl

Think of the minute hand of a clock, the blades of a windmill, or the cabins on a Ferris wheel.

> **📐 Definition — Rotation.**
> A **rotation** is determined by three inseparable components:
> 1. A fixed point called the **center of rotation** $O$.
> 2. An **angle of rotation** $\alpha$ (in degrees).
> 3. A **direction of rotation**:
>    - either **clockwise**;
>    - or **counterclockwise** (standard mathematical / counterclockwise sense).
> 
> The image of a point $M$ under rotation centered at $O$ by angle $\alpha$ is the point $M'$ such that:
> - $OM = OM'$ (the point remains on a concentric circle of radius $OM$);
> - The angle $\widehat{MOM'} = \alpha$.

```
                              M' ●
                                /
                               /   Angle α
                              / ∡ 
                             /     \
                            /       \
                        O  ●─────────● M
                             OM = OM'
```

*Remarkable Insight:* A rotation of $180^\circ$ is identical to a **point reflection**!

---

### 4. The Optical Zoom: Dilation (Homothety)

All previous transformations (reflections, translations, rotations) moved shapes across the plane without ever changing their dimensions. They are called **isometries** (from Greek *isos*, equal, and *metron*, measure).

A **dilation** (homothety, from Greek *homoios*, similar, and *thesis*, arrangement) is fundamentally different: it is an **optical zoom**. It expands or shrinks a shape proportionally from a central projection point.

#### 4.1 Definition and Scale Factor $k$

> **📐 Definition — Dilation (Homothety).**
> A dilation is defined by:
> 1. A fixed point called the **center** $O$.
> 2. A non-zero real number called the **scale factor** $k$.
> 
> The image of a point $M$ is the point $M'$ on the line $(OM)$ such that:
> - The distance $OM' = |k| \times OM$.
> - **If $k > 0$:** point $M'$ lies on the ray $[OM)$ (on the same side of $O$ as $M$).
> - **If $k < 0$:** point $M'$ lies on the opposite ray from $O$. This combines an expansion/contraction with a half-turn!

```
     k > 0 (Zoom in k = 2):
     O ●──────────────● M ────────────────────────────● M'
            OM                     OM' = 2 × OM
     
     k < 0 (Inversion k = -1.5):
     M' ●─────────────────────────● O ──────────────● M
          OM' = 1.5 × OM
```

#### 4.2 Scaling Effects of Factor $k$
- If $|k| > 1$: the transformation is an **enlargement**.
- If $0 < |k| < 1$: the transformation is a **reduction**.
- If $k = 1$: the shape does not move (identity transformation).
- If $k = -1$: the dilation is identical to **point reflection across center $O$**!

#### 4.3 The Dramatic Effect on Areas and Volumes

This is one of the most classic pitfalls in middle and high school exams:
- Under a dilation of scale factor $k$, **all lengths are multiplied by $|k|$**.
- **The area of any surface is multiplied by $k^2$!**
- **The volume of any solid is multiplied by $|k|^3$!**

*Vivid Example:* If you scale up an architectural model by $k = 3$:
- Its height is multiplied by 3.
- The paint required for its facade is multiplied by $3^2 = 9$.
- Its total weight and volume are multiplied by $3^3 = 27$!

---

### 5. What Transformations Preserve: The Genetic Code of Shapes

| Transformation | Lengths | Angles | Parallelism | Collinearity | Areas | Orientation |
|---|---|---|---|---|---|---|
| **Axial Reflection** | Preserved | Preserved | Preserved | Preserved | Preserved | **Reversed** (Mirror) |
| **Point Reflection** | Preserved | Preserved | Preserved | Preserved | Preserved | Preserved |
| **Translation** | Preserved | Preserved | Preserved | Preserved | Preserved | Preserved |
| **Rotation** | Preserved | Preserved | Preserved | Preserved | Preserved | Preserved |
| **Dilation (Scale $k$)** | $\times |k|$ | **Preserved** | Preserved | Preserved | $\times k^2$ | Preserved if $k>0$ |

Remember this fundamental principle: **all standard transformations in middle school strictly preserve angle measures, parallelism, and point collinearity**.

---

### 6. Congruent Triangles and Similar Triangles

#### 6.1 Congruent Triangles (Isometries): Perfect Clones

Two triangles are **congruent** when they can be made to **coincide perfectly** through a rigid motion (translation, rotation, or reflection). Their corresponding sides have identical lengths and their corresponding angles have identical measures.

To prove that two triangles are congruent, you do not need to measure all 6 components (3 sides and 3 angles)! Three suffice, according to the **three congruence criteria**:

1. **SSS (Side-Side-Side):**
   The three sides of one triangle are respectively equal in length to the three sides of the other.
2. **SAS (Side-Angle-Side):**
   Two sides of one triangle are equal to two sides of the other, and **the angle enclosed between these two sides** has the same measure.
3. **ASA (Angle-Side-Angle):**
   One side of one triangle is equal to one side of the other, and **the two angles adjacent to that side** have the same measures.

```
       SAS Criterion:
             /|                                  /|
          b / |                               b / |
           /  | a                              /  | a
          /__θ|                               /__θ|
            c                                   c
```

#### 6.2 Similar Triangles: The Same Silhouette at Different Scales

Two triangles are called **similar** when they possess the **exact same shape**, though not necessarily the same size. One is an enlargement or reduction of the other.

> **📐 Definition — Similar Triangles.**
> Two triangles are similar if:
> - Their **corresponding angles are pairwise equal in measure**;
> - **OR** their corresponding side lengths are **pairwise proportional**:
>   $$\frac{A'B'}{AB} = \frac{B'C'}{BC} = \frac{A'C'}{AC} = k.$$

*The Efficiency Theorem:*
Since the sum of angles in any triangle always equals $180^\circ$ (Chapter 15), as soon as **two angles of one triangle equal two angles of another**, the third angle is automatically equal, and **the two triangles are immediately similar** (AA criterion)!

---

### 7. The Lines of Equity: Perpendicular Bisector and Angle Bisector

These two remarkable lines are rooted in axial symmetry:

#### 7.1 The Perpendicular Bisector of a Segment
- **Definition:** The line perpendicular to a line segment at its midpoint.
- **Equidistance Property:** A point lies on the perpendicular bisector of segment $[AB]$ if and only if it is equidistant from both endpoints:
  $$M \in \text{Perpendicular Bisector of } [AB] \iff MA = MB.$$
- **The Circumscribed Circle (Circumcircle):** The perpendicular bisectors of the three sides of a triangle intersect at a single point: the **circumcenter**, which is the center of the unique circle passing through all three vertices of the triangle.

#### 7.2 The Angle Bisector
- **Definition:** The ray that divides an angle into two adjacent angles of equal measure. It is the **axis of symmetry** of the angle.
- **Equidistance Property:** Every point on an angle bisector is equidistant from the two arms (sides) of the angle.
- **The Inscribed Circle (Incircle):** The angle bisectors of the three interior angles of a triangle meet at the **incenter**, which is the center of the circle tangent to all three sides inside the triangle.

---

### 8. The Art of Friezes, Tessellations, and the Genius of Escher

When the geometry of transformations meets artistic imagination, mathematics touches the sublime.

#### 8.1 What Is a Tessellation?
A **tessellation (tiling)** is a complete covering of the plane using interlocking geometric shapes, leaving no empty gaps and with no shapes overlapping.
- A **frieze (band ornament)** is a one-dimensional tessellation (a decorative border along a wall). It relies on periodic horizontal translations, sometimes combined with vertical reflections or half-turns.
- A **planar tessellation** extends infinitely across both dimensions.

#### 8.2 The Mosaics of the Alhambra in Granada
In the 14th century, Moorish artists decorating the Alhambra palace, bound by cultural restrictions against depicting living forms, explored the mathematics of symmetry with staggering brilliance.
Mathematicians proved centuries later that there are strictly **17 possible periodic planar symmetry groups** (the 17 wallpaper groups). The master craftsmen of Granada had **empirically discovered every single one of them** in the ceramic tilework (*azulejos*) of their palace!

#### 8.3 The Metamorphoses of M. C. Escher
In 1936, Dutch graphic artist M. C. Escher visited the Alhambra and was deeply captivated by these repeating patterns. He devoted his artistic life to replacing abstract polygons with interlocking living creatures: birds, fish, lizards, angels, and demons.

How did he design a lizard that interlocks seamlessly with identical copies of itself?
1. He began with a basic grid shape (such as a square or parallelogram) that naturally tiles the plane.
2. He sliced out a curved contour along the left boundary and **translated** it to the right boundary.
3. He sliced a contour from the bottom boundary and performed a **$90^\circ$ rotation** to form the upper paw.
Because every piece of area removed from one side is perfectly restored to another, the total area remains invariant, allowing the motifs to interlock into infinity!

```
              ┌───┐                  ┌───┐
      Cut out │   │  Translation     │   │ ───► Paste
      on left └───┘                  └───┘      on right
         \_____/                         \_____/
```

---

### 9. Step-by-Step Worked Examples

#### Example 1: Image under rotation
Let $ABC$ be an equilateral triangle oriented counterclockwise. Let $O$ denote the center of its circumscribed circle.
1. What is the image of vertex $A$ under a $120^\circ$ counterclockwise rotation centered at $O$?
2. What is the image of side $[AB]$ under this rotation?

**Detailed Solution:**
1. In an equilateral triangle, center $O$ divides the full $360^\circ$ turn into three equal central angles:
   $$\widehat{AOB} = \widehat{BOC} = \widehat{COA} = \frac{360^\circ}{3} = 120^\circ.$$
   Furthermore, by definition of the circumcircle, $OA = OB = OC$.
   A counterclockwise rotation of $120^\circ$ about $O$ sends $A$ directly to $B$, and $B$ directly to $C$.
   Thus, the image of $A$ is $B$.
2. Rotations preserve line segments. Because $A$ maps to $B$ and $B$ maps to $C$, the image of segment $[AB]$ is segment $[BC]$.

---

#### Example 2: Dilation calculations and area scaling
A trapezoid of area $12\text{ cm}^2$ undergoes a dilation with scale factor $k = -2.5$.
1. What geometric shape is the resulting image?
2. Is its orientation reversed?
3. What is the area of the scaled trapezoid?

**Detailed Solution:**
1. Dilations preserve geometric categories and parallelism: the image of a trapezoid is another **trapezoid**.
2. The scale factor $k = -2.5$ is negative: the figure experiences an inversion ($180^\circ$ half-turn) about the center of dilation, but preserves its intrinsic cyclic orientation (unlike an axial reflection).
3. Area scales by $k^2$:
   $$\text{Area}' = k^2 \times \text{Area} = (-2.5)^2 \times 12 = 6.25 \times 12 = 75\text{ cm}^2.$$
   The area of the dilated trapezoid is $75\text{ cm}^2$.

---

#### Example 3: Proving two triangles are similar
In a circle of center $O$, draw two distinct diameters $[AB]$ and $[CD]$.
Prove that triangles $AOC$ and $BOD$ are congruent, and subsequently prove that they are similar.

**Detailed Solution:**
1. Since $[AB]$ and $[CD]$ are diameters passing through center $O$, point $O$ is the common midpoint of $[AB]$ and $[CD]$.
2. Consequently:
   - Point reflection across $O$ maps $A$ to $B$ (since $O$ is the midpoint of $[AB]$).
   - Point reflection across $O$ maps $C$ to $D$ (since $O$ is the midpoint of $[CD]$).
3. The image of triangle $AOC$ under point reflection across $O$ is therefore triangle $BOD$.
4. Because point reflection is an isometry (strictly preserving all side lengths and angle measures), **triangles $AOC$ and $BOD$ are congruent**.
5. Congruent triangles have identical side lengths (scale factor $k = 1$), hence they are **similar** with ratio $1$.

---

#### Example 4: Using similar triangles to calculate an inaccessible height
Two vertical poles $[AB]$ and $[DE]$ stand upright on level ground.
Pole $[AB]$ is 2 meters tall. At a certain moment, its shadow on the ground measures 3.5 meters.
At that exact same instant, the shadow of the taller pole $[DE]$ measures 14 meters.
Calculate the height of the tall pole $[DE]$.

**Detailed Solution:**
1. Sunlight rays are parallel at any given instant, so the sun rays strike the horizontal ground at the same angle of elevation.
2. Both poles are vertical, forming $90^\circ$ right angles with the flat ground.
3. The right triangles formed by each pole and its shadow share two identical angle measures: they are **similar triangles** (by the AA criterion).
4. Corresponding side lengths are therefore proportional:
   $$\frac{\text{Height of tall pole } DE}{\text{Height of short pole } AB} = \frac{\text{Shadow of tall pole}}{\text{Shadow of short pole}}.$$
   $$\frac{DE}{2} = \frac{14}{3.5}.$$
5. Compute the scaling ratio:
   $$k = \frac{14}{3.5} = 4.$$
6. The height of pole $[DE]$ is:
   $$DE = 2 \times 4 = 8\text{ meters}.$$

---

#### Example 5: Compass-only construction of the perpendicular bisector
Explain and mathematically justify the classical compass-and-straightedge construction of the perpendicular bisector of segment $[AB]$.

**Detailed Solution:**
1. Open the compass to any radius $R$ strictly greater than half the length of $AB$ ($R > \frac{AB}{2}$).
2. Placing the compass tip at $A$, draw two arcs of radius $R$, one above and one below $[AB]$.
3. Without changing the compass radius, place the tip at $B$ and draw arcs intersecting the previous ones at points $P$ and $Q$.
4. Draw the straight line $(PQ)$ using a straightedge.
5. **Rigorous Justification:**
   - By construction, $PA = PB = R$: point $P$ is equidistant from $A$ and $B$, so $P$ lies on the perpendicular bisector of $[AB]$.
   - Likewise, $QA = QB = R$: point $Q$ is equidistant from $A$ and $B$, so $Q$ lies on the perpendicular bisector of $[AB]$.
   - Since two distinct points uniquely determine a straight line, the line $(PQ)$ is precisely the perpendicular bisector of $[AB]$.

---

### Key Takeaways

1. **The 5 Geometric Transformations:**
   - **Axial Reflection:** paper folding across an axis $(d)$ (perpendicular bisector). Reverses orientation.
   - **Point Reflection:** $180^\circ$ half-turn around a center $O$ (midpoint).
   - **Translation:** pure slide along a vector without turning (parallelogram).
   - **Rotation:** angular pivot of $\alpha^\circ$ about a center $O$ in a chosen direction.
   - **Dilation (Homothety):** scaling zoom by factor $k$ from center $O$ ($OM' = |k| \times OM$).
2. **Invariance and Scaling:**
   - All transformations preserve angles, collinearity, and parallelism.
   - The first four (isometries) preserve distances and areas.
   - A dilation multiplies lengths by $|k|$ and surface areas by $k^2$.
3. **Congruent Triangles:**
   Identical, superimposable triangles. Corresponding sides are equal and corresponding angles are equal (SSS, SAS, ASA criteria).
4. **Similar Triangles:**
   Triangles having the exact same shape: corresponding angles are equal and corresponding sides are proportional. Matching two pairs of angles guarantees similarity.
5. **Perpendicular Bisector and Angle Bisector:**
   - Perpendicular Bisector: perpendicular at the midpoint, locus of equidistant points from endpoints, circumcenter.
   - Angle Bisector: divides an angle in half, locus of equidistant points from arms, incenter.

---

### Exercises

#### Level ★: Direct Application

**Exercise 26.1** Identifying Transformations:
Match each real-world situation with the corresponding transformation:
1. A cabin on a moving Ferris wheel (staying upright).
2. The reflection of a tree in a still mountain lake.
3. A train traveling along straight tracks.
4. An image projected onto a movie theater screen from a film frame.
5. A playing card (the Queen of Hearts) with its inverted double on the table.

**Exercise 26.2** Properties of Axial Reflection:
Let segment $[AB]$ have length 6 cm and angle $\widehat{BAC} = 45^\circ$.
An axial reflection across line $(d)$ maps $A, B, C$ to $A', B', C'$.
1. What is the length of segment $[A'B']$? Justify.
2. What is the measure of angle $\widehat{B'A'C'}$? Justify.

**Exercise 26.3** Translation and Parallelograms:
Let $M'$ be the image of point $M$ under the translation mapping $A$ to $B$.
1. What is the geometric nature of quadrilateral $ABM'M$?
2. If $AB = 7\text{ cm}$, what is the distance $MM'$?

**Exercise 26.4** Dilation Calculations:
A triangle $ABC$ has perimeter 18 cm and area $14\text{ cm}^2$.
A dilation with scale factor $k = 3$ is applied.
1. What is the perimeter of the dilated triangle?
2. What is the area of the dilated triangle?

**Exercise 26.5** Recognizing Congruent Triangles:
In triangle $ABC$, $AB = 5\text{ cm}$, $AC = 7\text{ cm}$, and $\widehat{BAC} = 40^\circ$.
In triangle $DEF$, $DE = 5\text{ cm}$, $DF = 7\text{ cm}$, and $\widehat{EDF} = 40^\circ$.
Are triangles $ABC$ and $DEF$ congruent? What criterion justifies this?

---

#### Level ★★: Deeper Reflection and Multi-Step Problems

**Exercise 26.6** Composition of Reflections:
Let lines $(d_1)$ and $(d_2)$ be perpendicular, intersecting at point $O$.
Apply reflection across $(d_1)$ to a shape, then reflect the resulting image across $(d_2)$.
Prove that this sequence of two perpendicular reflections is equivalent to a single simple transformation.

**Exercise 26.7** Similar Triangles and Angle Calculation:
In triangle $ABC$, $\widehat{A} = 65^\circ$ and $\widehat{B} = 45^\circ$.
In triangle $RST$, $\widehat{R} = 65^\circ$ and $\widehat{T} = 70^\circ$.
Are triangles $ABC$ and $RST$ similar? Justify carefully.

**Exercise 26.8** The Tree and the Mirror Problem:
To measure an inaccessible tree, Arthur places a flat mirror horizontally on the ground at point $M$, 12 meters from the base of tree $P$.
He steps back 2 meters to point $A$, where he sees the top of tree $S$ reflected in the mirror.
Arthur's eyes are 1.60 meters above the ground.
By the optical law of reflection, angle of incidence equals angle of reflection: $\widehat{SMA} = \widehat{PMS}$.
1. Justify that the triangles formed by Arthur and the tree are similar.
2. Compute the height of the tree.

**Exercise 26.9** Negative Dilation:
On a number line, center of dilation $O$ has coordinate 0. Point $A$ has coordinate 3.
The dilation has scale factor $k = -2$.
1. What is the coordinate of image point $A'$?
2. Where is point $O$ located with respect to segment $[AA']$?

**Exercise 26.10** The Chord and the Bisector:
Let $O$ be the center of a circle and $[AB]$ a chord not passing through $O$.
1. Prove that point $O$ belongs to the perpendicular bisector of chord $[AB]$.
2. Deduce that any line passing through the center of a circle perpendicular to a chord bisects that chord.

**Exercise 26.11** Translating Friezes:
A decorative wall frieze is built from a repeating tile motif of width 4 cm.
The motif is repeatedly translated horizontally by 4 cm.
1. How many complete tiles compose a frieze 1.20 m in length?
2. If each motif has an area of $15\text{ cm}^2$, what is the total painted area?

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 26.12** Mathematical Billiards:
On a pocketless rectangular billiard table, white ball $A$ and red ball $B$ rest on the felt.
The player must strike ball $A$ so that it rebounds off top cushion $(d)$ before striking ball $B$.
1. Using reflection $B'$ of ball $B$ across cushion line $(d)$, find the exact target point $P$ on the cushion.
2. Prove that point $P$ minimizes the total path length $AP + PB$ (Fermat's principle of reflection).

**Exercise 26.13** Nested Similar Triangles in a Right Triangle:
Let $ABC$ be a right triangle at $A$. Let $H$ be the foot of the altitude from $A$ to hypotenuse $[BC]$.
1. Prove that triangles $ABC$, $HBA$, and $HAC$ are all pairwise similar.
2. By equating side ratios between $HBA$ and $HAC$, prove the famous altitude theorem:
   $$AH^2 = HB \times HC.$$
3. If $HB = 4\text{ cm}$ and $HC = 9\text{ cm}$, compute altitude $AH$.

**Exercise 26.14** The Ozanam Chessboard Paradox (Vanishing Area):
An $8 \times 8$ chessboard (area 64) is dissected into four pieces: two right triangles with legs 3 and 8, and two trapezoids with bases 5 and 3 and height 5.
When rearranged, they seemingly form a rectangle of $5 \times 13 = 65$!
Where did the extra square unit come from ($65 - 64 = 1$)?
*(Hint: compute the slopes of the hypotenuses using similar triangles).*

---

### Solutions

#### Level ★

**Solution 26.1**
1. Ferris wheel cabin: **Circular translation** (stays upright without spinning on its axis).
2. Reflection in water: **Axial reflection** (the water surface is the reflection axis).
3. Train on tracks: **Translation**.
4. Movie projector: **Dilation (Homothety)** (enlargement centered at the lens).
5. Queen of Hearts: **Point reflection** (half-turn about card center).

**Solution 26.2**
1. $A'B' = 6\text{ cm}$. Axial reflection is an isometry: it strictly preserves lengths.
2. $\widehat{B'A'C'} = 45^\circ$. Axial reflection strictly preserves angle measures.

**Solution 26.3**
1. Quadrilateral $ABM'M$ is a **parallelogram** by definition of translation.
2. Opposite sides of a parallelogram are equal: $MM' = AB = 7\text{ cm}$.

**Solution 26.4**
1. Lengths scale by $k = 3$: $\text{Perimeter}' = 3 \times 18 = 54\text{ cm}$.
2. Areas scale by $k^2 = 3^2 = 9$: $\text{Area}' = 9 \times 14 = 126\text{ cm}^2$.

**Solution 26.5**
Yes, triangles $ABC$ and $DEF$ are congruent by the **SAS (Side-Angle-Side)** criterion: two pairs of sides are equal in length ($5\text{ cm}$ and $7\text{ cm}$) and their included angles are equal ($40^\circ$).

---

#### Level ★★

**Solution 26.6**
Let $M$ be a point. Reflection across $(d_1)$ maps $M$ to $M_1$; reflection across $(d_2)$ maps $M_1$ to $M'$.
Since $(d_1) \perp (d_2)$, the coordinates show that $O$ is the midpoint of $[MM']$ and $\widehat{MOM'} = 180^\circ$.
Two perpendicular reflections compose into a **point reflection centered at $O$** (a $180^\circ$ rotation about $O$).

**Solution 26.7**
In $\triangle ABC$: $\widehat{C} = 180^\circ - (65^\circ + 45^\circ) = 70^\circ$. Angles are $65^\circ, 45^\circ, 70^\circ$.
In $\triangle RST$: $\widehat{R} = 65^\circ, \widehat{T} = 70^\circ \implies \widehat{S} = 180^\circ - (65^\circ + 70^\circ) = 45^\circ$.
All three pairs of angles match: the triangles are **similar** by AA.

**Solution 26.8**
1. Both triangles contain a vertical right angle ($90^\circ$) and an equal angle of incidence/reflection ($\widehat{SMA} = \widehat{PMS}$). By AA, they are **similar**.
2. Ratio:
   $$\frac{\text{Tree Height}}{\text{Arthur Eye Height}} = \frac{\text{Mirror to Tree}}{\text{Mirror to Arthur}} \implies \frac{h}{1.60} = \frac{12}{2} = 6.$$
   $$h = 1.60 \times 6 = 9.60\text{ meters}.$$

**Solution 26.9**
1. $x_{A'} = k \times x_A = (-2) \times 3 = -6$.
2. $OA = 3$ and $OA' = |-6| = 6$. Point $O$ lies between $A'$ and $A$, twice as far from $A'$ as from $A$.

**Solution 26.10**
1. Radii are equal: $OA = OB$. Point $O$ is equidistant from $A$ and $B$, so $O$ lies on the perpendicular bisector of chord $[AB]$.
2. The perpendicular bisector is the unique line perpendicular to $[AB]$ through its midpoint. Since $O$ lies on it, any line through $O$ perpendicular to $[AB]$ is the perpendicular bisector, necessarily bisecting $[AB]$.

**Solution 26.11**
1. Total length $1.20\text{ m} = 120\text{ cm}$. Tile count: $\frac{120}{4} = 30$ tiles.
2. Total area: $30 \times 15\text{ cm}^2 = 450\text{ cm}^2$.

---

#### Level ★★★

**Solution 26.12**
1. Reflect target ball $B$ across top rail $(d)$ to find point $B'$.
   For any point $M$ on rail $(d)$, $MB = MB'$. Thus path length $AM + MB = AM + MB'$.
   The shortest path between $A$ and $B'$ is the straight segment $[AB']$.
   Therefore, optimal impact point $P$ is the **intersection of segment $[AB']$ with cushion line $(d)$**.
2. By the triangle inequality, for any other point $M \neq P$, $AM + MB' > AB'$. The path via $P$ is strictly minimal.

**Solution 26.13**
1. In right triangle $ABC$, $\widehat{B} + \widehat{C} = 90^\circ$.
   In right triangle $HBA$, $\widehat{HAB} + \widehat{B} = 90^\circ \implies \widehat{HAB} = \widehat{C}$.
   All three triangles share angles ($90^\circ, \widehat{B}, \widehat{C}$): they are **similar**.
2. Comparing $HBA$ and $HAC$:
   $$\frac{AH}{HC} = \frac{HB}{AH} \implies AH^2 = HB \times HC.$$
3. With $HB = 4$ and $HC = 9$:
   $$AH^2 = 4 \times 9 = 36 \implies AH = \sqrt{36} = 6\text{ cm}.$$

**Solution 26.14**
The apparent paradox is a visual illusion!
For the $5 \times 13$ rectangle to be solid, the pieces' hypotenuses must form a single continuous straight diagonal.
Compare slopes:
- Triangle hypotenuse slope: $\frac{3}{8} = 0.375$.
- Trapezoid edge slope: $\frac{2}{5} = 0.400$.
Since $\frac{3}{8} \neq \frac{2}{5}$, the edges do not line up into a single straight line. They form a very thin, elongated parallelogram gap in the center whose hidden area equals exactly 1 square unit ($65 - 64 = 1$)!

---

### The Question Opening the Next Chapter

Look at the extraordinary journey we have accomplished: we know how to dissect shapes, compute areas, manipulate equations, inequalities, and functions. But what happens when we leave the flat sheet of paper and step into the three-dimensional depth of our physical universe? How do we measure the capacity of a conical amphora, a stone pyramid, or planet Earth itself?

That is the grand exploration of space, solids, and cross sections awaiting you in the next chapter: **Land Partitioning and the Potter's Box**.
