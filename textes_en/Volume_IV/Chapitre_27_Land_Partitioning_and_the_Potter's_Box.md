# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 27: Land Partitioning and the Potter's Box

> *“A formula memorized by heart without ever being seen is like a sterile seed. But take a pair of scissors, cut out a triangle, paste the pieces on the other side: the rectangle appears, and the formula becomes self-evident.”*

---

### What You Are About to Discover

- Why **every triangle is half of a rectangle**, and how a pair of scissors suffices to rediscover the formulas for the area of a parallelogram, a trapezoid, and even a circle.
- How to transition from the **flat** (areas, in $\text{m}^2$) to the **solid** (volumes, in $\text{m}^3$), and why we multiply by 100 in one case and by 1,000 in the other.
- The mystery of the **“divided by 3”** in pyramids and cones, and the crowning achievement Archimedes was most proud of: the volume of the **sphere**.
- What appears when you **slice** a solid with a flat blade: geometric **cross sections**.
- The classic pitfalls that cost points on exams: radius or diameter? vertical height or slanted side? $\text{cm}^3$ or liters?

---

### 1. The Problem: The Feud of Two Farmers and the Potter's Order

In the Meuse valley during the 13th century, the count's chief steward compiles the land registry to levy the fair share of harvested wheat. Two neighboring farmers step forward before him.

* Farmer **Martin** owns a **rectangular** field measuring 20 meters wide by 30 meters long. The steward computes without hesitation:
  $$20 \times 30 = 600 \text{ square meters.}$$
  It is a grid of 600 small one-meter-by-one-meter plots of land (remember the brick wall from Chapter 5?).
* But farmer **Thomas** owns an **elongated, sharply pointed triangular** field. The side running along the stream measures 40 meters, and the perpendicular distance from the stream to the farthest tip of the meadow is 30 meters.

The surveyors argue: *“How can we count whole squares in a pointed field? The slanted boundaries slice the grid squares into irregular fragments impossible to measure!”*

A young journeyman mason steps up holding a sheet of parchment and a pair of scissors: *“Put away your measuring cords, gentlemen. There is no need to chop blades of grass into crumbs: we merely need to invite a twin brother to the table.”*

That very afternoon, at the opposite end of the village, the **potter** receives a curious commission: the miller requests three vessels holding **the exact same capacity of grain**—a cylindrical jar, a conical funnel, and a hemispherical bowl. The potter knows how to measure length with a cord and area with tiles… but how do we measure **what fits inside**?

These two challenges—measuring an irregular surface and measuring interior capacity—will guide us through this chapter. You will discover that both rest upon one and the same foundational principle: **cut, rearrange, and reassemble**, without losing or adding a single grain.

---

### 2. What Is an Area? Units and Conversions

#### 2.1 The Intuitive Idea

The **area** of a planar shape is the quantity of “paint” required to coat it, or the number of unit squares needed to tile it completely. Two shapes with completely different outlines can have the exact same area: it suffices that one can be dissected and reassembled to form the other.

> **📐 Definition —** We choose a unit of area: for example, the **square of side length 1 cm**. The **area** of a figure is the number of these unit squares (and fractions of squares) required to tile it exactly, without gaps or overlaps.

**The notation $\text{cm}^2$.** We write $1\text{ cm}^2$ and pronounce it “one **square centimeter**.” The small superscript 2 is not decorative: it records that we multiplied **two** lengths (a width in cm and a length in cm). It is the exact same exponent seen in $5^2 = 5 \times 5$ (Chapter 18). Indeed, the area of a square of side length $c$ is $c^2$: that is precisely why we say “$c$ **squared**”!

**Perimeter versus Area:** The **perimeter** is the length of the fence (walking around the boundary, in cm); the **area** is the surface of the lawn (filling the interior, in $\text{cm}^2$). A rectangle of $1 \times 9$ and a square of $3 \times 3$ share the same area ($9\text{ cm}^2$) but have very different perimeters ($20\text{ cm}$ versus $12\text{ cm}$).

#### 2.2 Area Conversions: The Pitfall of “Times 100”

One meter is 10 decimeters. But how many square decimeters are in one **square meter**? Sketch it: a square of side length 1 m is a square of side length 10 dm, so it contains $10 \times 10 = 100$ small squares of 1 dm on each side.

```
  1 m = 10 dm
  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤      10 rows of 10 squares
  │  ...  100 squares of 1 dm²  │      = 100 dm²
  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
  └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
```

$$1\text{ m}^2 = 100\text{ dm}^2 = 10,000\text{ cm}^2 = 1,000,000\text{ mm}^2.$$

In an area conversion table, **every metric unit spans two columns**:

| $\text{km}^2$ | | $\text{hm}^2$ (ha) | | $\text{dam}^2$ (a) | | $\text{m}^2$ | | $\text{dm}^2$ | | $\text{cm}^2$ | | $\text{mm}^2$ | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | 3 | 5 | 0 | 0 | 0 | | |

Here we read: $3.5\text{ m}^2 = 350\text{ dm}^2 = 35,000\text{ cm}^2$.

> **💡 Did You Know?** Farmers traditionally use the **are** (a), which equals $1\text{ dam}^2 = 100\text{ m}^2$ (a square of 10 m by 10 m), and the **hectare** (ha), which equals $1\text{ hm}^2 = 10,000\text{ m}^2$ (a square of 100 m by 100 m, roughly the size of one and a half soccer fields). The word “are” comes from the Latin *area*, meaning “open space,” which also gave rise to the English word “area”!

> **⚠️ Watch Out! Pitfall.** $1\text{ m}^2 \neq 100\text{ cm}^2$. Because $1\text{ m} = 100\text{ cm}$, we have $1\text{ m}^2 = 100\text{ cm} \times 100\text{ cm} = 10,000\text{ cm}^2$. When converting units of area, you multiply or divide by 100 **at each step**, not by 10.

---

### 3. The Scissors Stroke: Every Triangle Is Half a Rectangle

#### 3.1 Base and Height: Precise Definitions

Before cutting, we must establish exact terms.

> **📐 Definition —** In any triangle, we choose one side to call the **base**. The **altitude (height) relative to that base** is the line segment dropped from the opposite vertex **perpendicular** to the line containing the base. Its length is also termed the “height.”

```
              C
             /|\
            / | \
           /  |h \
          /   |   \
         /____|____\
        A     H     B
        <---- b ---->
   [CH] is the altitude to base [AB]; (CH) ⊥ (AB)
```

The symbol $\perp$ reads “is perpendicular to.” The small square drawn at the foot $H$ of the altitude indicates the right angle.

A triangle has **three** sides, hence **three** altitudes—one for each possible base. You may select whichever is most convenient, provided you pair a base **with its own corresponding height**.

#### 3.2 The Twin Brother Proof

Let us return to Thomas's pointed field: base $b = 40$ m, height $h = 30$ m.

1. Cut out a **second identical twin triangle** in another color.
2. Rotate this twin through a **half-turn ($180^\circ$)** (a point reflection through the midpoint of a side, as in Chapter 26).
3. Glue it alongside the first: together, they form a **parallelogram** of base $b$ and height $h$.
4. And as we will prove momentarily, a parallelogram has the exact same area as a **rectangle** of dimensions $b \times h$.

Even simpler, when the foot $H$ of the altitude falls inside the base: the altitude splits the triangle into two right triangles. Each is half of a small rectangle (halved along its diagonal). The two small rectangles together form the large rectangle $b \times h$, and the triangle occupies precisely half of it.

```
   ┌─────────┬─────────┐
   │ ╲  (1') │ (2')  ╱ │      Pieces (1) and (2) form the triangle.
   │   ╲     │     ╱   │      Pieces (1') and (2') are their twin mirrors.
   │ (1) ╲   │   ╱ (2) │      (1) = (1') and (2) = (2')
   │       ╲ │ ╱       │      therefore triangle = half the rectangle.
   └─────────┴─────────┘
   A         H         B
```

> **📐 Formula — Area of a Triangle**
> $$\mathcal{A}_{\text{triangle}} = \frac{\text{base} \times \text{height}}{2} = \frac{b \times h}{2}$$

We frequently write $\mathcal{A}$ in calligraphy script to avoid confusion with vertex point $A$.

For Thomas's field: $\mathcal{A} = \dfrac{40 \times 30}{2} = \dfrac{1200}{2} = 600\text{ m}^2$. Both farmers, despite their drastically different field shapes, hold **the exact same surface area** of farmland: they will owe the identical tax, down to the single grain of wheat.

#### 3.3 Boundary Cases: When the Altitude Falls Outside

> **⚠️ Watch Out! Pitfall.** In an **obtuse** triangle (having an angle greater than $90^\circ$), the altitude to certain sides falls **outside** the triangle, landing on the **extended line** of the base. The formula remains unconditionally true, but the proof requires care!

```
                          C
                        / |
                      /   |
                    /     | h
                  /    .  |
                /   .     |
              / .         |
             A--------B . . H
             <--- b -->
```

> **✍️ Proof —** Foot $H$ lies on the line extension of $[AB]$, beyond vertex $B$. The large right triangle $AHC$ contains our target triangle $ABC$ **plus** the small right triangle $BHC$. Therefore:
> $$\mathcal{A}_{ABC} = \mathcal{A}_{AHC} - \mathcal{A}_{BHC} = \frac{AH \times h}{2} - \frac{BH \times h}{2} = \frac{(AH - BH) \times h}{2} = \frac{AB \times h}{2}.$$
> The formula “$\text{base} \times \text{height} \div 2$” is universally valid for **all** triangles.

> **💡 Did You Know?** Any triangle sharing base $[AB]$ whose third vertex $C$ slides along a line parallel to $(AB)$ possesses **the exact same area**, because its perpendicular height never varies! Even if the triangle becomes extremely flattened and skewed. This is Euclid's famous “shearing triangle” theorem (Book I of the *Elements*, Proposition 37).

---

### 4. Parallelograms and Trapezoids Unveiled

#### 4.1 The Parallelogram: The Tilted Field

Take a cardboard rectangle and push its top edge sideways: it tilts into a parallelogram. Has it lost any material? Cut off the small protruding triangle on one side and glue it into the recess on the opposite side: **the rectangle reappears**, with identical base and height.

```
        ________________                 ________________
       /|              /                |              |
      / |             /      ════>      |              | h
     /  | h          /                  |              |
    /___|___________/                   |______________|
    <------ b ----->                    <------ b ----->
    Cut the left triangle and paste it onto the right side.
```

> **📐 Formula — Area of a Parallelogram**
> $$\mathcal{A}_{\text{parallelogram}} = b \times h$$
> where $h$ is the distance between the two parallel sides of length $b$ (measured **perpendicularly**).

> **⚠️ Watch Out! Pitfall.** **Never** multiply the base by the slanted side! A parallelogram with sides 10 cm and 6 cm can have an area of $60\text{ cm}^2$ (if upright, forming a rectangle), $30\text{ cm}^2$ (if tilted), or nearly 0 if squashed flat. The slanted edge length does not change, but the height certainly does.

#### 4.2 The Trapezoid: The Flared Skirt

A **trapezoid (trapezium)** is a quadrilateral with two parallel sides called **bases**: the major base $B$ and the minor base $b$. The **height** $h$ is the perpendicular distance between them.

Take two twin trapezoids. Invert one upside down and place it next to the other: together they form a **parallelogram** whose base equals $B + b$ and whose height is $h$.

```
      b                B                   B + b
   ______  _________________       ________________________
  /      \ \               /      /      /                /
 /        \ \             /  ═>  /      /                / h
/__________\ \___________/      /______/________________/
      B             b               B + b
```

> **📐 Formula — Area of a Trapezoid**
> $$\mathcal{A}_{\text{trapezoid}} = \frac{(B + b) \times h}{2}$$

This can also be understood as $\dfrac{B+b}{2} \times h$: it equals the area of a rectangle whose width is the **average** of the two bases.

> **💡 Did You Know?** Checking extreme boundary cases is reassuring. If $b = B$, the trapezoid becomes a parallelogram, recovering $\dfrac{2B \times h}{2} = B \times h$. If $b = 0$, the minor base collapses to a point, turning the trapezoid into a triangle, recovering $\dfrac{B \times h}{2}$. A sound mathematical formula always holds true at its extreme limits!

---

### 5. Archimedes' Pizza: The Area of a Disk

You met the number $\pi$ in Chapter 16: it is the ratio of a circle's circumference to its diameter, $\pi \approx 3.14159$. The circumference of a circle of radius $R$ is $2\pi R$. But what about the **surface area** of the interior disk?

In the 3rd century BC, **Archimedes of Syracuse** envisioned slicing the disk like a pizza into a large number of slender triangular wedges radiating from the center. Each wedge has length equal to radius $R$. He arranged these slices **head-to-tail**, alternating one pointing up and one pointing down:

```
    ____  ____  ____  ____  ____  ____  ____  ____
    \  /\ \  /\ \  /\ \  /\ \  /\ \  /\ \  /\ \  /\
     \/  \ \/  \ \/  \ \/  \ \/  \ \/  \ \/  \ \/  \   height ≈ R
          ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾
    |<--------- half-circumference = π R --------->|
```

The resulting shape resembles an **undulating rectangle**:
* its height is radius $R$;
* its length is **half the circumference** of the pizza (the other half of the crust forms the bottom edge), which is $\dfrac{2\pi R}{2} = \pi R$.

As the slices become infinitely slender, the ripples vanish: in the limit, it becomes a true rectangle.

> **📐 Formula — Area of a Disk of Radius $R$**
> $$\mathcal{A}_{\text{disk}} = \pi R \times R = \pi R^2$$
> Pronounced “pi R squared.” Note: this is $\pi \times (R \times R)$; the exponent applies only to $R$.

> **⚠️ Watch Out! Pitfall.** Two classical mistakes:
> 1. Using the **diameter** instead of the radius. For a disk of diameter 10 cm, $R = 5$ cm and $\mathcal{A} = 25\pi \approx 78.5\text{ cm}^2$, and definitely not $100\pi$!
> 2. Confusing $2\pi R$ (the **circumference**, a 1D length in cm) with $\pi R^2$ (the **area**, a 2D surface in $\text{cm}^2$). Memory aid: area contains a square exponent, matching its unit $\text{cm}^2$.

> **🔍 True History —** Archimedes did not possess the decimal digits of $\pi$ (no one can write them all down, as they are endless and non-repeating!). He proved that the area of a circle equals that of a right triangle whose legs are the radius and the circle's circumference: $\dfrac{2\pi R \times R}{2} = \pi R^2$. Furthermore, by inscribing and circumscribing 96-sided regular polygons around a circle, he bounded $\pi$ strictly between $3\frac{10}{71}$ and $3\frac{1}{7}$.

---

### 6. Worked Examples on Area

**Worked Example 1 — The Trapezoidal Garden.**
A garden has the shape of a trapezoid: the back fence measures 16 m, the front fence measures 10 m, and the two parallel fences are separated by 8 m. What is its area? How many bags of grass seed are needed if one bag covers $25\text{ m}^2$?

*Solution.* $\mathcal{A} = \dfrac{(16 + 10) \times 8}{2} = \dfrac{26 \times 8}{2} = \dfrac{208}{2} = 104\text{ m}^2$.
$104 \div 25 = 4.16$: 4 bags are not enough, so **5 bags** are required. (Always round **up** when purchasing coverage materials!)

**Worked Example 2 — The Hidden Altitude of a Right Triangle.**
A triangle $ABC$ is right-angled at $A$ with $AB = 6$ cm, $AC = 8$ cm, and hypotenuse $BC = 10$ cm. Calculate the length of the altitude drawn from vertex $A$ to hypotenuse $[BC]$.

*Solution.* In a right triangle, the two perpendicular legs act as **base and altitude to each other**. Using base $[AB]$ and altitude $[AC]$:
$$\mathcal{A} = \frac{6 \times 8}{2} = 24\text{ cm}^2.$$
Alternatively, we can express the area using hypotenuse $[BC]$ as the base and unknown altitude $h$ dropped from $A$: $\mathcal{A} = \dfrac{10 \times h}{2} = 5h$.
Both calculations describe the exact same area, so $5h = 24 \implies h = 4.8\text{ cm}$. We found an unknown length purely through area equivalence!

**Worked Example 3 — Composite Figure.**
A church window has the shape of a rectangle 120 cm wide and 150 cm tall, topped by a semicircle of diameter 120 cm. What is the area of the stained glass window, rounded to the nearest $\text{cm}^2$?

*Solution.* Dissect the figure into basic components:
* Rectangle: $120 \times 150 = 18,000\text{ cm}^2$.
* Semicircle: radius $R = 60$ cm, area $\dfrac{\pi \times 60^2}{2} = \dfrac{3600\pi}{2} = 1800\pi \approx 5654.87\text{ cm}^2$.
* Total: $18,000 + 1800\pi \approx 23,655\text{ cm}^2$, or approximately $2.37\text{ m}^2$.

**Worked Example 4 — The Annulus (Circular Ring).**
A circular pond of radius 6 m is surrounded by a walking path 2 m wide. What is the area of the path?

*Solution.* The path is an **annulus**: the large disk (radius $6 + 2 = 8$ m) minus the small inner pond (radius 6 m).
$$\mathcal{A} = \pi \times 8^2 - \pi \times 6^2 = 64\pi - 36\pi = 28\pi \approx 87.96\text{ m}^2.$$

> **⚠️ Watch Out! Pitfall.** You cannot subtract radii before squaring: $\pi \times (8 - 6)^2 = 4\pi$ is completely wrong! One subtracts the **areas**, not the linear radii.

**Worked Example 5 — Notary Land Conversions.**
A rectangular parcel of farmland measures 85 m by 64 m. Express its area in $\text{m}^2$, in ares, and in hectares.

*Solution.* $85 \times 64 = 5,440\text{ m}^2$. Since $1\text{ a} = 100\text{ m}^2$: $5,440\text{ m}^2 = 54.4$ a. Since $1\text{ ha} = 100$ a: $54.4\text{ a} = 0.544$ ha.

---
