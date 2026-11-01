# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)
## CHAPTER 16: The Potter's Wheel and Archimedes' Secret

> *“Every polygon built of right angles readily submits to a grid. But the gentle curve of the circle slips through the surveyor's fingers. To measure the perfect ring, one had to unroll the circumference upon the earth and discover that mysterious, unending number without repetition that the sages of Syracuse hunted down between two vast armies of polygons.”*

---

### What You Are About to Discover

- The essential distinction between the **circle** (the boundary line) and the **disc** (the solid interior surface).
- The complete vocabulary of roundness: **center**, **radius**, **diameter**, **chord**, and **arc**.
- The rolling wheel experiment and the magic constant: why the ratio of perimeter to diameter always yields the same number $\pi \approx 3.14159\dots$
- The astonishing intellectual feat of **Archimedes of Syracuse** and his 96-sided polygon method.
- The two indispensable formulas: the circumference of the circle ($C = 2\pi r$) and the area of the disc ($A = \pi r^2$), proved visually by unrolling a disc into a near-rectangle!
- 🛠️ The Boundary Case Laboratory: extreme limits of circles, concentric rings, and the Earth-rope paradox.

---

### 1. The Problem: The Chariot Wheel and the Clay Pot

You are eleven years old. After exploring the straight lines and right angles of the Egyptian surveyors in the previous chapter, let us step into the workshop of an ancient artisan.

In a sunlit corner of the potter's studio, a heavy wooden turntable spins smoothly upon an iron pivot. It is the **potter's wheel**. The craftsman drops a lump of wet grey clay onto the exact center of the spinning disc. His wet palms cup the earth. Under his thumbs, as if by enchantment, the shapeless lump blossoms into an exquisitely symmetrical bowl.

```
                  Potter's wheel in rotation
                         ___________
                     .-'     O     '-.
                   .'   . - ' ' - .   '.
                  /   /      r      \   \
                 |   |       ●───────|---|  <- Potter's hand
                  \   \             /   /
                   '.   ' - . . - '   .'
                     '-.___________.-'
                             |
                             | pivot
```

Every single point along the outer rim of the bowl spins at the exact same distance from the central pivot. If one side were even a fraction of an inch further from the center than another, the whirling vessel would wobble violently and collapse in an instant.

The next day, in the neighboring village, the blacksmith faces a far more punishing challenge. He must forge an **iron tire** to encase the heavy wooden wheel of a war chariot. This iron band must be forged straight on the anvil, heated white-hot, bent into a ring, and fitted around the wooden wheel with millimeter precision.
- If the blacksmith cuts the iron band two centimeters too short, it will never fit over the wooden rim.
- If he cuts it two centimeters too long, the iron hoop will rattle loosely against the wood, and the wheel will shatter against the very first rock on the road.

The smith measures the width of the wooden wheel: it measures exactly **1 meter straight across**, passing through the center.  
What exact length of straight iron must he cut from his stock?

He tries wrapping a thin cord around the curved rim of the wheel, but the cord sags, slips, and stretches. The frustrated craftsman grumbles:  
*“Why is it so easy to measure a square or a triangle with a rigid ruler, and so treacherous to measure the curved rim of a round wheel?”*

To answer this question, we must do what the ancient geometers did: unroll the circle upon the ground.

---

### 2. The Vocabulary of the Circle and the Disc

Before unrolling our wheel, let us establish precise terms. Mathematical language is rigorous; confusing these terms is the most frequent beginner trap.

#### 2.1 Circle vs. Disc

> **📐 Definition — Circle and Disc**  
> - The **circle** of center $O$ and radius $r$ is the collection of all points in the plane located at the exact same distance $r$ from center $O$. The circle is **a closed curved line**—it is the hollow boundary (like a wedding ring, a hoop, or an iron tire).  
> - The **disc** of center $O$ and radius $r$ is the collection of all points in the plane located at a distance less than or equal to $r$ from center $O$. The disc is **a solid filled surface** (like a coin, a dinner plate, or a pancake).

```
          THE CIRCLE (the boundary line)        THE DISC (the solid surface)
                 .-""""-.                              .######.
               .'        '.                          .##########.
              /            \                        /############\
             |      O       |                      |###### O #####|
              \            /                        \############/
               '.        .'                          '##########'
                 '-....-'                              '######'
            (Perimeter / Boundary)                   (Area and Perimeter)
```

#### 2.2 Remarkable Segments and Curves

Mark a point $O$ on a sheet of paper:

```
                             B
                            /
                           /   Radius r
                          /
               A ────────●──────── B'
                 |       O       |
                 |<── Diameter d ─►|
                        /
                       / Arc CD
                      C ─────── D
                         Chord
```

- The **center**: the fixed point $O$ located at the exact midpoint of the figure.
- The **radius** ($r$): both the straight line segment $[OB]$ joining the center to any point on the circle, and the **numerical length** $r = OB$. All radii of the same circle have identical lengths.
- The **diameter** ($d$): a straight line segment $[AB']$ passing through center $O$ and connecting two opposite points on the circle. Its length is denoted $d$. Since it consists of two radii placed end-to-end ($[AO]$ and $[OB']$), we have the fundamental relationship:
  $$d = 2 \times r \quad \Longleftrightarrow \quad r = \frac{d}{2}$$
- A **chord**: a line segment $[CD]$ connecting any two points on the circle without necessarily passing through the center. The diameter is simply the longest possible chord of the circle.
- An **arc**: a continuous portion of the curved circle between two points, denoted $\wideparen{CD}$.

> **💡 Did You Know?** The word *radius* comes from the Latin word for the spoke of a chariot wheel or a weaver's rod. The word *diameter* comes from the ancient Greek *dia* (“across, through”) and *metron* (“measure”): it is the measure that cuts straight through the figure from one side to the other.

---

### 3. The Rolling Experiment and the Magic Constant

Let us return to the blacksmith and his chariot wheel. Consider an experiment you can easily perform at home using a coin, a roll of masking tape, or a circular tin can:

1. Take a felt-tip pen and draw a tiny red mark on the bottom rim of your circular tin can.
2. Place the can on a long sheet of blank paper taped to the floor, aligning the red mark with the $0\text{ cm}$ mark on your ruler.
3. Roll the can along the ruler in a straight line without slipping, until the red mark touches the ground again after completing **exactly one full revolution**.
4. Measure the distance traveled along the ruler: this represents the length of one full turn of the rim—the **perimeter** of the circle, historically known as the **circumference**.

```
   Start (0 cm)                                      End (1 full turn)
        |                                                        |
      ( O ● )                                                  ( O ● )
     ═══╧════════════════════════════════════════════════════════╧═════════
     0 cm                                                    Perimeter P
```

Let us record careful measurements for round objects of widely varying sizes:

| Object Measured | Diameter $d$ | Measured Perimeter $P$ | Ratio $\frac{P}{d}$ (division) |
|---|---|---|---|
| 2-Euro coin | $2.57\text{ cm}$ | $8.07\text{ cm}$ | $\frac{8.07}{2.57} \approx 3.140$ |
| Roll of tape | $8.00\text{ cm}$ | $25.13\text{ cm}$ | $\frac{25.13}{8.00} \approx 3.141$ |
| Dinner plate | $22.00\text{ cm}$ | $69.10\text{ cm}$ | $\frac{69.10}{22.00} \approx 3.141$ |
| Bicycle wheel | $68.00\text{ cm}$ | $213.60\text{ cm}$ | $\frac{213.60}{68.00} \approx 3.141$ |

Look closely at the final column: **the division $\frac{P}{d}$ always yields the exact same number: approximately $3.14$!**  
Whether the object is as minuscule as the head of a pin or as colossal as the orbit of the Moon around the Earth, **the circumference of any circle is always just a little more than three times its diameter.**

This constant ratio does not depend on the size of the object: it is a universal mathematical constant of Euclidean geometry. Mathematicians denote it with the Greek letter **$\pi$** (pronounced *“pie”*).

> **📐 The Universal Constant $\pi$ —**  
> For every circle of circumference $P$ and diameter $d$:
> $$\frac{P}{d} = \pi \approx 3.1415926535\dots$$

Multiplying both sides by diameter $d$ yields the famous formula for the **circumference of a circle**:
$$P = \pi \times d = 2 \times \pi \times r$$

Generations of students remember it by its rhythmic cadence: **“Two $\pi$ $r$”**.

> **🔍 Historical Note — Where Did the Letter $\pi$ Come From?**  
> The letter $\pi$ is the first letter of the Greek word *periphereia* (which gave us “periphery,” meaning outer boundary). The Welsh mathematician William Jones was the first to use $\pi$ to represent this ratio in 1706 in an educational textbook. However, it was the Swiss mathematical titan **Leonhard Euler** who popularized it worldwide starting in 1737 by adopting it in all his master treatises.

---

### 4. Archimedes' Secret: Taming the Circle with Polygons

Ancient Babylonians and Egyptians already knew that the circumference was roughly three times the diameter. Egyptian scribes used an approximation near $\left(\frac{16}{9}\right)^2 \approx 3.16$, and the Old Testament (1 Kings 7:23) describes a great circular bronze basin measuring 10 cubits across and 30 cubits around ($\pi \approx 3$).

Yet no one knew how to calculate the true value of this number with mathematical certainty. Enter the greatest scientific mind of Antiquity: **Archimedes of Syracuse** (c. 287 – 212 BC).

#### 4.1 The Stroke of Genius: The Polygon Vise

Archimedes reasoned: *“I cannot measure a curved line directly. However, I know how to calculate the perimeter of straight-sided figures: regular polygons!”*

Archimedes trapped the circle between two regular polygons like a vise:
1. An **inscribed polygon** (lying entirely **inside** the circle, whose vertices touch the circle).
2. A **circumscribed polygon** (lying entirely **outside** the circle, whose straight sides touch the circle).

```
         Inscribed Polygon (Inside)         Circumscribed Polygon (Outside)
                  .---.                             .-------.
                /   |   \                          / |     | \
               /    |    \                        /  |     |  \
              |─────●─────|                      |───●─────●───|
               \    |    /                        \  |     |  /
                \   |   /                          \ |     | /
                  '---'                             '-------'
         Inner Perimeter < Circle Perimeter < Outer Perimeter
```

Physical reality is undeniable:
- The path along the inner polygon is strictly shorter than the curve of the circle.
- The path along the outer polygon is strictly longer than the curve of the circle.

Therefore:
$$\text{Perimeter of Inscribed Polygon} < P_{\text{circle}} < \text{Perimeter of Circumscribed Polygon}$$

Dividing each term by diameter $d$, Archimedes trapped $\pi$ within an unbreakable arithmetic interval!

#### 4.2 The Climb to 96 Sides

Archimedes began with regular hexagons (6 sides), computing their perimeters using the Pythagorean theorem.  
Then, through a brilliant geometric formula of his own invention, he systematically **doubled** the number of sides:
- 12-sided polygons (dodecagons);
- 24-sided polygons;
- 48-sided polygons;
- And finally, polygons of **96 sides**!

Imagine the immense labor: at 96 sides, the inner and outer polygons hug the circular line so tightly that the human eye cannot distinguish the broken straight edges from the smooth curve.

After heroic manual computations involving square roots and fractions, Archimedes proved his historic inequality:
$$\frac{223}{71} < \pi < \frac{22}{7}$$

In decimal form:
$$3.140845\dots < \pi < 3.142857\dots$$

Thanks to Archimedes, humanity knew beyond doubt that $\pi$ begins with **$3.14$**.  
Archimedes' upper fraction, **$\frac{22}{7}$**, is so remarkably accurate (error under $0.04\%$) that master builders and engineers used it for mental calculations for over two thousand years!

---

### 5. The Area of the Disc: Turning a Circle into a Rectangle

We now know how to measure the outer boundary cord ($P = 2\pi r$). But what is the **surface area** of the disc? How many square meters of paint are required to coat a round tabletop?

The answer is given by a celebrated formula:
$$A = \pi \times r^2$$

Where does this formula come from? Why does the square of the radius ($r^2$) appear, multiplied by the exact same constant $\pi$?  
Here is a breathtaking visual demonstration, attributed to Leonardo da Vinci and anticipated by ancient Greek thinkers.

#### The Apple Pie Metaphor

Imagine a large circular disc of pastry of radius $r$:
1. Slice this disc into a large number of identical, razor-thin wedge-shaped slices (say 16 slices, like narrow arrowheads).
2. Separate the 16 slices and interlock them alternately, one pointing up, one pointing down:

```
          Disc sliced into wedges                Wedges interlocked alternating
                 .-""""-.                              /\/\/\/\/\/\/\/\
               .'  \  /  '.                           |                |  Height ≈ r
              /  \  \/  /  \                           \/\/\/\/\/\/\/\/
             |----\----/---|                           |◄──────────────►|
              \  /  /\  \  /                             Base ≈ 1/2 P
               '.  /  \  .'
                 '-....-'
```

Look at the reassembled figure: it astonishingly resembles a **rectangle** (or a near-perfect parallelogram)!
- What is the **height** of this rectangle? It is the length of one pastry wedge, which is the **radius $r$** of the circle.
- What is the **base** of this rectangle? The upper scalloped rim consists of half the wedges, and the bottom rim consists of the other half. The base is therefore **half the circumference of the circle**:
  $$\text{Base} = \frac{1}{2} \times P = \frac{1}{2} \times (2 \pi r) = \pi r$$

What is the area of this rectangle?
$$\text{Area} = \text{base} \times \text{height} = (\pi r) \times r = \pi r^2$$

If instead of 16 wedges, we slice the disc into 100, 1,000, or 1,000,000 infinitely thin slices, the tiny curved scallops flatten completely into straight lines: the shape becomes an exact mathematical rectangle of area $\pi r^2$.

> **📐 Theorem — Area of a Disc**  
> The area $A$ of a disc of radius $r$ (and diameter $d = 2r$) equals:
> $$A = \pi \times r^2 = \pi \times r \times r$$
> Expressed in terms of diameter $d$: $A = \pi \times \left(\frac{d}{2}\right)^2 = \frac{\pi d^2}{4}$.

---

### 6. Beware of Pitfalls!

> **⚠️ Warning: Deadly Traps!**  
> 1. **Never confuse radius and diameter!** In any word problem, highlight immediately whether you are given the radius or the diameter. If a wheel has a diameter of $10\text{ cm}$, its radius is $5\text{ cm}$. If you blindly write $A = \pi \times 10^2$, your result will be four times too large!  
> 2. **Never confuse perimeter and area!**  
>    - Perimeter is a **length** (in $\text{m}$, $\text{cm}$, $\text{mm}$): $P = 2\pi r$. The radius has power 1.  
>    - Area is a **surface** (in $\text{m}^2$, $\text{cm}^2$, $\text{mm}^2$): $A = \pi r^2$. The radius is squared.  
> 3. **The Semicircle Perimeter Trap:** The perimeter of a closed semicircle is NOT simply half of $2\pi r$. You must add the straight flat edge that closes the shape—the diameter!  
>    $$P_{\text{semicircle}} = \pi r + 2r$$  
> 4. **$\pi$ is neither $3.14$ nor $\frac{22}{7}$!** These are merely practical approximations. The decimal expansion of $\pi$ continues infinitely without any repeating periodic pattern: $\pi = 3.141592653589793\dots$ ($\pi$ is an irrational number). When a problem asks for the “exact value,” you must leave the symbol $\pi$ in your final answer (e.g., $16\pi\text{ cm}^2$).

---

### 7. Solved Examples

#### Solved Example 1 — Iron Hooping of a Wine Barrel
A cooper wishes to encase a round wooden barrel with an iron hoop. The barrel has a diameter of $80\text{ cm}$.  
What minimum length of iron strap must he cut? (Use $\pi \approx 3.14$).

*Solution:*  
- We are looking for a perimeter. Given diameter $d = 80\text{ cm}$.  
- Formula: $P = \pi \times d$.  
- Calculation: $P \approx 3.14 \times 80 = 251.2\text{ cm}$.  
He must cut an iron band of at least $251.2\text{ cm}$ (about $2.51\text{ meters}$). ✔

#### Solved Example 2 — The Bicycle Odometer
A mountain bike tire has a radius of $r = 35\text{ cm}$.  
1. How far does the bicycle travel when the wheel completes exactly one full revolution?  
2. How many full turns does the wheel make over a journey of $1.1\text{ km}$?

*Solution:*  
1. One revolution equals the wheel's circumference:  
   $$P = 2 \times \pi \times r = 2 \times \pi \times 35 = 70\pi \approx 219.91\text{ cm} \approx 2.20\text{ m}$$  
2. Convert total distance into meters: $1.1\text{ km} = 1,100\text{ m}$.  
   $$\text{Number of turns} = \frac{\text{Total distance}}{\text{Circumference}} = \frac{1,100}{2.20} = 500\text{ turns}$$  
The wheel makes exactly 500 full rotations. ✔

#### Solved Example 3 — The Pizza Dilemma: A Feast of Geometry!
At a pizzeria, you face a hungry choice for the exact same price of \$16:  
- One **large pizza** with a diameter of $40\text{ cm}$.  
- Two **small pizzas** with a diameter of $28\text{ cm}$ each.  
Which choice gives you more pizza to eat?

*Solution:*  
Calculate the edible surface area in both cases (watch the radii!):  
- For the large pizza: diameter is $40\text{ cm}$, so radius $r_1 = 20\text{ cm}$.  
  $$A_1 = \pi \times r_1^2 = \pi \times 20^2 = 400\pi \approx 1,256.6\text{ cm}^2$$  
- For the two small pizzas: diameter is $28\text{ cm}$, so radius $r_2 = 14\text{ cm}$.  
  Area of one small pizza: $A_{\text{small}} = \pi \times 14^2 = 196\pi \approx 615.75\text{ cm}^2$.  
  For two small pizzas:  
  $$A_2 = 2 \times 196\pi = 392\pi \approx 1,231.5\text{ cm}^2$$  
*Conclusion:* $400\pi > 392\pi$. The single large pizza provides more food than both small pizzas combined! The single large pizza is the smarter choice. ✔

#### Solved Example 4 — Finding the Radius from Perimeter or Area
1. A venerable oak tree has a trunk circumference measured at $314\text{ cm}$. What is its diameter?  
2. A circular plaza has an area of $706.5\text{ m}^2$. What is its radius? (Use $\pi \approx 3.14$).

*Solution:*  
1. Since $P = \pi \times d$:  
   $$d = \frac{P}{\pi} \approx \frac{314}{3.14} = 100\text{ cm} = 1\text{ meter}$$  
2. Since $A = \pi \times r^2$:  
   $$r^2 = \frac{A}{\pi} \approx \frac{706.5}{3.14} = 225$$  
   What positive number squared equals $225$? We find the square root: $15 \times 15 = 225$, so $r = 15\text{ meters}$. ✔

#### Solved Example 5 — The Running Track and Circular Ring (Annulus)
A training stadium features a central circular grass lawn of radius $R_1 = 30\text{ m}$, surrounded by a tartan running track of uniform width $4\text{ m}$.  
What is the area of the tartan running track?

```
                   Running Track (width 4 m)
                     . - - - - - .
                  .'     .---.     '.
                 /     /   R1  \     \
                |     |    ●────|─────|
                 \     \       /     /
                  '.     '---'     .'
                     ' - - - - - '
                         R2 = R1 + 4 m
```

*Solution:*  
The track forms an **annulus** (a circular ring): the difference between the large outer disc and the small inner lawn disc.  
- Inner radius: $R_1 = 30\text{ m}$.  
- Outer radius: $R_2 = 30 + 4 = 34\text{ m}$.  
- Large disc area: $A_{\text{large}} = \pi \times R_2^2 = \pi \times 34^2 = 1,156\pi\text{ m}^2$.  
- Small disc area: $A_{\text{small}} = \pi \times R_1^2 = \pi \times 30^2 = 900\pi\text{ m}^2$.  
- Area of the ring:  
  $$A_{\text{track}} = A_{\text{large}} - A_{\text{small}} = 1,156\pi - 900\pi = 256\pi \approx 256 \times 3.1416 \approx 804.25\text{ m}^2$$  
The track covers approximately $804.25\text{ m}^2$. ✔

---

### What You Must Remember

1. **Circle vs. Disc:**  
   - The circle is the boundary line (length / perimeter).  
   - The disc is the solid interior surface (area).
2. **Radius and Diameter:**  
   - Diameter is twice the radius: $d = 2r \Longleftrightarrow r = \frac{d}{2}$.
3. **The Constant $\pi$:**  
   - It is the invariant ratio of perimeter to diameter: $\pi = \frac{P}{d} \approx 3.14159\dots$  
   - Archimedes bounded it with 96-sided polygons: $\frac{223}{71} < \pi < \frac{22}{7}$.
4. **Fundamental Formulas:**  
   - **Circumference:** $P = 2 \pi r = \pi d$.  
   - **Area of a Disc:** $A = \pi r^2 = \frac{\pi d^2}{4}$.
5. **Exact vs. Rounded Values:**  
   - Keep the symbol $\pi$ for exact mathematical values (e.g., $25\pi\text{ cm}^2$).  
   - Replace $\pi$ with $3.14$ or calculator $\pi$ for decimal approximations.

---

### Exercises

#### Level ★ (Direct Application)

**Exercise 1.** Complete the table below for different circles (use $\pi \approx 3.14$):  
| Circle | Radius $r$ | Diameter $d$ | Circumference $P$ |
|---|---|---|---|
| A | $6\text{ cm}$ | ? | ? |
| B | ? | $18\text{ m}$ | ? |
| C | ? | ? | $31.4\text{ dm}$ |

**Exercise 2.** Calculate the exact area (leaving $\pi$), then round to the nearest tenth:  
1. A disc of radius $4\text{ cm}$.  
2. A disc of diameter $14\text{ m}$.

**Exercise 3.** A gardener installs wooden edging around a circular flowerbed of radius $3\text{ m}$. What length of edging must he purchase?

**Exercise 4.** A dinner plate has a diameter of $24\text{ cm}$. Calculate its area to the nearest $\text{cm}^2$.

**Exercise 5.** Give the exact perimeter of a closed semicircle of radius $5\text{ cm}$, including its straight baseline.

#### Level ★★ (Reasoning and Geometry)

**Exercise 6.** A round dining table has a perimeter of $376.8\text{ cm}$.  
1. What is its radius?  
2. What is its area in $\text{m}^2$?

**Exercise 7.** A goat is tethered to a stake in the middle of an open flat meadow by a rope $6\text{ meters}$ long.  
1. What geometric shape can the goat graze?  
2. Calculate the exact area of this grazing zone.

**Exercise 8.** The radius of a disc is doubled (from $r$ to $2r$).  
1. By what factor is its perimeter multiplied?  
2. By what factor is its area multiplied? Justify using algebraic formulas.

**Exercise 9.** A sports field has the shape of a rectangle $100\text{ m}$ long and $60\text{ m}$ wide, capped at both ends by semicircular regions of diameter $60\text{ m}$.  
1. Calculate the total outer track perimeter.  
2. Calculate the total surface area of the sports complex.

**Exercise 10.** A truck tire has an outer diameter of $90\text{ cm}$. At cruising speed, the wheel rotates at $10\text{ revolutions per second}$.  
How far does the truck travel in one minute? State the answer in meters, then convert to kilometers per hour ($\text{km/h}$).

**Exercise 11.** An audio CD has an outer diameter of $12\text{ cm}$ and a center spindle hole of diameter $1.5\text{ cm}$.  
What surface area is available for recorded musical data?

#### Level ★★★ (Challenges and In-Depth Investigations)

**Exercise 12. Inscribed Square and Circle.**  
From a square sheet of copper $20\text{ cm}$ on each side, a metalsmith cuts out the largest possible circular disc.  
1. What is the diameter of this disc?  
2. What area of copper is discarded as scrap from the four corners?  
3. What percentage of the initial metal plate was wasted?

**Exercise 13. The Lunes of Hippocrates of Chios.**  
Let $ABC$ be a right triangle at vertex $A$, with $AB = 4\text{ cm}$ and $AC = 3\text{ cm}$. The hypotenuse is $BC = 5\text{ cm}$.  
On each of the three sides taken as diameters, draw a semicircle outward.  
The two crescent shapes formed above the hypotenuse are called *lunes*.  
Prove that the combined area of these two curved lunes is strictly equal to the area of the flat right triangle $ABC$!

**Exercise 14. The Rope Around the Earth.**  
Imagine a snug rope wrapped tightly around the equator of the Earth (assume Earth is a perfect sphere of circumference $C_1 = 40,000\text{ km}$).  
We now add **just 1 meter** to the length of this rope ($C_2 = 40,000\text{ km} + 1\text{ m}$), and prop it up uniformly all around the globe so it forms a concentric circle.  
Can a mouse crawl under the elevated rope without ducking? A cat? A human being?  
*(Hint: calculate the clearance height $h = r_2 - r_1$. The result will astonish you!)*

**Exercise 15. Archimedes' Hexagon Method.**  
Consider a circle of radius $R = 1$.  
1. Inscribe a regular hexagon inside this circle. How long are its 6 sides? Deduce the perimeter of this hexagon and the elementary lower bound for $\pi$.  
2. Calculate the perimeter of a square circumscribed outside this circle. What upper bound for $\pi$ does this produce? Between which two whole integers is $\pi$ thus proven to lie?

---

### Solutions

**Exercise 1.**  
- Circle A: $d = 2 \times 6 = 12\text{ cm}$; $P = \pi \times 12 \approx 3.14 \times 12 = 37.68\text{ cm}$.  
- Circle B: $r = 18 / 2 = 9\text{ m}$; $P = \pi \times 18 \approx 3.14 \times 18 = 56.52\text{ m}$.  
- Circle C: $d = P / \pi \approx 31.4 / 3.14 = 10\text{ dm}$; $r = 10 / 2 = 5\text{ dm}$.

**Exercise 2.**  
1. $r = 4\text{ cm}$: Exact Area $A = \pi \times 4^2 = 16\pi\text{ cm}^2 \approx 50.3\text{ cm}^2$.  
2. $d = 14\text{ m} \implies r = 7\text{ m}$: Exact Area $A = \pi \times 7^2 = 49\pi\text{ m}^2 \approx 153.9\text{ m}^2$.

**Exercise 3.**  
$P = 2\pi r = 2 \times \pi \times 3 = 6\pi \approx 18.85\text{ m}$. He should buy about $18.9\text{ m}$ of edging.

**Exercise 4.**  
$d = 24\text{ cm} \implies r = 12\text{ cm}$.  
$A = \pi \times 12^2 = 144\pi \approx 452.39\text{ cm}^2 \approx 452\text{ cm}^2$.

**Exercise 5.**  
The semicircle consists of the curved arc of length $\frac{1}{2}(2\pi r) = \pi r = 5\pi\text{ cm}$, plus the straight baseline diameter $d = 2 \times 5 = 10\text{ cm}$.  
Exact perimeter: $P = (5\pi + 10)\text{ cm} \approx 25.71\text{ cm}$.

**Exercise 6.**  
1. $P = 2\pi r \implies r = \frac{P}{2\pi} \approx \frac{376.8}{2 \times 3.14} = \frac{376.8}{6.28} = 60\text{ cm}$.  
2. $A = \pi r^2 = \pi \times 60^2 = 3,600\pi \approx 11,304\text{ cm}^2 = 1.1304\text{ m}^2$.

**Exercise 7.**  
1. The accessible area is a solid disc centered at the stake with radius $6\text{ m}$.  
2. Exact area: $A = \pi \times 6^2 = 36\pi\text{ m}^2 \approx 113.10\text{ m}^2$.

**Exercise 8.**  
1. New perimeter: $P' = 2\pi(2r) = 2(2\pi r) = 2P$. Perimeter is **multiplied by 2**.  
2. New area: $A' = \pi(2r)^2 = \pi \times 4r^2 = 4(\pi r^2) = 4A$. Area is **multiplied by 4** ($2^2$)!

**Exercise 9.**  
1. The perimeter consists of two straight lengths of $100\text{ m}$ plus two semicircular arcs of diameter $60\text{ m}$ (which form one complete circle of diameter $60\text{ m}$):  
   $P_{\text{total}} = 2 \times 100 + \pi \times 60 = 200 + 60\pi \approx 200 + 188.5 = 388.5\text{ m}$.  
2. Total area is the central rectangle ($100 \times 60 = 6,000\text{ m}^2$) plus the complete disc formed by the two semicircles ($r = 30\text{ m}$):  
   $A_{\text{disc}} = \pi \times 30^2 = 900\pi \approx 2,827.4\text{ m}^2$.  
   $A_{\text{total}} = 6,000 + 900\pi \approx 8,827.4\text{ m}^2$.

**Exercise 10.**  
Distance per turn: $P = \pi \times 0.90\text{ m} \approx 2.8274\text{ m}$.  
In one second (10 turns): $10 \times 2.8274 = 28.274\text{ m/s}$.  
In one minute ($60\text{ s}$):  
$D = 28.274 \times 60 \approx 1,696.46\text{ m} \approx 1.70\text{ km}$.  
Speed in $\text{km/h}$: $28.274 \times 3.6 \approx 101.8\text{ km/h}$.

**Exercise 11.**  
Outer radius $R = 6\text{ cm}$, inner hole radius $r = 0.75\text{ cm}$.  
$A = \pi R^2 - \pi r^2 = \pi(6^2 - 0.75^2) = \pi(36 - 0.5625) = 35.4375\pi \approx 111.33\text{ cm}^2$.

**Exercise 12.**  
1. The largest disc has a diameter equal to the width of the square: $d = 20\text{ cm} \implies r = 10\text{ cm}$.  
2. Area of square: $A_{\text{square}} = 20 \times 20 = 400\text{ cm}^2$.  
   Area of disc: $A_{\text{disc}} = \pi \times 10^2 = 100\pi \approx 314.16\text{ cm}^2$.  
   Scrap area: $400 - 100\pi \approx 85.84\text{ cm}^2$.  
3. Waste percentage: $\frac{85.84}{400} \approx 0.2146 = 21.46\%$. More than 21% of the raw material is lost!

**Exercise 13.**  
Triangle $ABC$ is right-angled at $A$; its area is $\frac{3 \times 4}{2} = 6\text{ cm}^2$.  
The semicircles on the legs have radii $r_1 = 2$ and $r_2 = 1.5$.  
Their areas are $\frac{1}{2}\pi(2^2) = 2\pi$ and $\frac{1}{2}\pi(1.5^2) = 1.125\pi$.  
The large semicircle on hypotenuse $BC$ has radius $R = 2.5$ and area $\frac{1}{2}\pi(2.5^2) = 3.125\pi$.  
Notice: $2\pi + 1.125\pi = 3.125\pi$! The sum of the two smaller semicircles equals the large semicircle.  
The total figure area is (Triangle + 2 small semicircles).  
Subtracting the large semicircle leaves the lunes:  
$\text{Area of lunes} = (\text{Area of triangle} + 3.125\pi) - 3.125\pi = \text{Area of triangle} = 6\text{ cm}^2$.  
A curved shape whose area is strictly equal to a straight polygon!

**Exercise 14.**  
Let $R_E$ be Earth's radius and $R_2$ the radius of the lengthened rope.  
Initial circumference: $C_1 = 2\pi R_E$.  
Lengthened circumference: $C_2 = 2\pi R_2 = C_1 + 1\text{ meter}$.  
Subtract: $2\pi R_2 - 2\pi R_E = 1 \implies 2\pi(R_2 - R_E) = 1$.  
The clearance height $h = R_2 - R_E$ is:  
$$h = \frac{1}{2\pi} \approx \frac{1}{6.283} \approx 0.159\text{ m} \approx 16\text{ cm}!$$  
This clearance is entirely independent of the size of the sphere! Whether wrapped around the Earth, the Sun, or a baseball, adding 1 meter to the circumference lifts the rope by nearly $16\text{ cm}$ everywhere. A mouse, and even a large cat, can slip underneath with ease!

**Exercise 15.**  
1. An inscribed regular hexagon splits into 6 equilateral triangles of side length equal to radius $R = 1$.  
   Each side measures $1$; perimeter is $6 \times 1 = 6$.  
   Since diameter is $2$, the ratio gives $\pi > \frac{6}{2} = 3$.  
2. The circumscribed square has sides equal to the diameter, $2$.  
   Its perimeter is $4 \times 2 = 8$.  
   The outer ratio gives $\pi < \frac{8}{2} = 4$.  
   We obtain the clean integer bracket: $3 < \pi < 4$.

---

### The Question That Opens What Follows

We now know how to measure round, curving shapes upon the ground. But what can we do when the object to be measured is neither a small wheel before our eyes nor a cord we can lay across the sand, but a towering mountain of stone: the **Great Pyramid of Giza**?

How did a Greek philosopher named **Thales**, armed with nothing more than a simple wooden stick planted in the scorching desert sand, deduce the exact height of the greatest tomb on Earth without ever climbing a single step? That is the secret of **geometric proportions and similar triangles**, which we shall master in the next chapter.
