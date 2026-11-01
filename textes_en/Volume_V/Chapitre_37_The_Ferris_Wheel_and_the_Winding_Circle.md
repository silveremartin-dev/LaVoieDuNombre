# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 37: The Ferris Wheel and the Winding Circle

> *“The degree is an invention of Babylonian merchants who were fond of the number 60. The radian, on the other hand, is an invention of the wheel itself: it is the circle measuring itself with its own radius.”*

---

### What You Are About to Discover

- Why the **degree** is no longer sufficient when we want to describe motion that turns endlessly (wheels, planets, waves, motors).
- A new unit of angle, born from the circle itself: the **radian**.
- How to **wind the real number line** around a circle of radius 1, and thereby give meaning to $\cos(100)$, to $\sin(-7)$, or to $\cos\left(\frac{37\pi}{4}\right)$.
- The **special values** ($\frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}$) proved with a square and an equilateral triangle.
- The **associated angles**: how the symmetries of the circle allow everything to be brought back to the first quadrant.
- How to **solve** the equations $\cos x = a$ and $\sin x = a$, and sketch the undulating curves of the cosine and sine functions.

---

### 1. The Problem: The Fairground Gondola Turning Endlessly

You have boarded the giant Ferris wheel at the fairground. It has a radius of $20\text{ m}$, its central axle is $22\text{ m}$ above the ground, and your gondola departs from the lowest point, just $2\text{ m}$ off the ground. The wheel turns slowly, steadily, in a counterclockwise direction when viewed from the parking lot.

Your little brother, watching from below, asks you a simple question:

*“When your gondola has traveled 50 meters along the circle, how high will you be? And after 300 meters? And after 1 kilometer?”*

You pull out your middle-school trigonometry (Chapter 28): in a right-angled triangle, $\cos \widehat{A} = \frac{\text{adjacent}}{\text{hypotenuse}}$. But very quickly, three major obstacles arise.

```
                     peak (42 m)
                        .-*-.
                    .-'   |   '-.
                  .'      |      '.
                 /        |        \
                |         O---------|   axle at 22 m
                 \        |  20 m  /
                  '.      |      .'
                    '-.   |   .-'
                        '-*-'   ← gondola boarding (2 m)
           ═══════════════════════════════  ground
```

**Obstacle 1 — Middle-school angles stop at 90°.** A right-angled triangle cannot have an acute angle of $120^\circ$, much less $400^\circ$. Yet your gondola keeps turning: after a turn and a half, it has “turned through $540^\circ$”.

**Obstacle 2 — The degree has no natural connection to distance traveled.** Your brother speaks in **meters traveled along the circle**. To convert meters to degrees, you must each time perform a rule of three with the circumference $2\pi \times 20$. This is clumsy: the unit “degree” is foreign to the circle.

**Obstacle 3 — Direction matters.** If the wheel turns backward (to let passengers off), we must account for **negative** angles.

We therefore need:
1. a **natural** unit of angle, directly tied to arc length;
2. a definition of cosine and sine valid for **any real number**, positive or negative, small or vast.

This is precisely what mathematicians constructed between the seventeenth and eighteenth centuries, and what you will now reconstruct with a simple piece of string.

> **🔍 The True History — The Sine Is a Pocket!**
> Around 150 BC, the Greek astronomer **Hipparchus** compiled the first table of “chords” to calculate the positions of celestial bodies; **Ptolemy** refined it in the *Almagest* (2nd century AD). In India, around 499, **Aryabhata** preferred to work with the **half-chord**, which he termed *ardha-jyā* (“half-bowstring”), abbreviated to *jyā* and then *jīva*. Arab scholars transcribed this word phonetically as *jība*, which, written without vowels, resembled *jayb*, meaning “pocket” or “fold of a garment”. In the twelfth century, while translating these texts in Toledo, **Gerard of Cremona** rendered it literally into Latin as *sinus*, meaning “fold, pocket, bay”. That is why the most famous wave function in mathematics bears the name of a fold in a tunic!

---

### 2. The Radian: Measuring an Angle with the Radius

#### 2.1 The String Experiment

> **🖐️ Your Turn to Try —** Take a round tin can, a piece of string, and a marker. Cut a piece of string whose length is exactly equal to the **radius** of the can. Place one end on the rim, then press the string flush along the circular rim. Draw the two radii connecting the center of the can to both ends of the string.

The angle you have just traced—the angle that subtends an arc **whose length is equal to the radius**—is the natural unit of the circle: it is **one radian**.

```
                    . - ~ ~ ~ - .
                .'      arc = R     '.
              /         ______*        \
             |     R  /       |         |
             |      /  1 rad  |         |
             |    O-----------*         |
             |          R               |
              \                        /
                '.                  .'
                    ' - . _ _ . - '
```

How many such “radius” strings can be laid end-to-end around the circle? The circumference is $2\pi R$, so we can lay $\frac{2\pi R}{R} = 2\pi \approx 6.28$ strings. A complete revolution thus measures $2\pi$ radians. With $6$ strings, a small gap remains ($0.28$ of a string) to close the full loop.

> **📐 Definition — The Radian**
> In a circle of radius $R$, a central angle measures **$1$ radian** (symbol: **rad**) when it subtends an arc of length $R$.
> A full turn measures $2\pi\text{ rad}$, therefore:
> $$\boxed{\pi \text{ rad} = 180^\circ}$$

The word “radian” naturally derives from “radius” (*radius* in Latin). The idea of measuring angles by arc length dates back to the English mathematician **Roger Cotes** (1714); the name *radian* appeared in print for the first time in **1873**, in examination papers set by **James Thomson** (brother of Lord Kelvin) in Belfast.

> **💡 Did You Know?** The radian is dimensionless: it is a ratio of two lengths ($\frac{\text{arc}}{\text{radius}}$, meters divided by meters). That is why we often omit the unit: we write “the angle $\frac{\pi}{3}$” rather than “$\frac{\pi}{3}\text{ rad}$”. When no unit is specified, **it is always radians**.

#### 2.2 Conversions

The proportionality $\pi \text{ rad} \leftrightarrow 180^\circ$ gives:

$$\text{measure in rad} = \text{measure in degrees} \times \frac{\pi}{180} \qquad ; \qquad \text{measure in degrees} = \text{measure in rad} \times \frac{180}{\pi}.$$

| Degrees | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Radians | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |

And $1 \text{ rad} = \frac{180}{\pi}{}^\circ \approx 57.3^\circ$.

> **✅ Worked Example 1 — Conversions**
> a) Convert $75^\circ$ to radians. b) Convert $\frac{7\pi}{9}\text{ rad}$ to degrees. c) Convert $2.5\text{ rad}$ to degrees.
>
> a) $75 \times \frac{\pi}{180} = \frac{75\pi}{180} = \frac{5\pi}{12}$ (dividing numerator and denominator by $15$).
> b) $\frac{7\pi}{9} \times \frac{180}{\pi} = \frac{7 \times 180}{9} = 7 \times 20 = 140^\circ$.
> c) $2.5 \times \frac{180}{\pi} = \frac{450}{\pi} \approx 143.2^\circ$.

#### 2.3 Arc Length and Sector Area

Because the radian is defined by “$\text{arc} = \text{radius}$ for 1 rad”, the arc length is directly proportional to the angle: $1\text{ rad} \leftrightarrow R$, hence $\theta\text{ rad} \leftrightarrow R\theta$.

> **📐 Property — Arc Length, Sector Area**
> In a circle of radius $R$, a central angle of $\theta$ **radians** subtends:
> - an arc of length $\boxed{\ell = R\,\theta}$;
> - an angular sector (a “slice of pie”) of area $\boxed{\mathcal{A} = \frac{1}{2}R^2\theta}$.

*Justification of the area:* The full disk (angle $2\pi$) has area $\pi R^2$; by proportionality, an angle $\theta$ yields an area of $\pi R^2 \times \frac{\theta}{2\pi} = \frac{1}{2}R^2\theta$.

Notice how remarkably simple these formulas are **in radians**. In degrees, one would have to write $\ell = \frac{\pi R \alpha}{180}$: the nuisance factor $\frac{\pi}{180}$ appears everywhere. This is the first great virtue of the radian: **it eliminates parasitic constants**. You will see a second, even more spectacular reason in Grade 12: the derivative of $\sin x$ is $\cos x$ **only when $x$ is in radians**.

> **✅ Worked Example 2 — The Ferris Wheel Gondola**
> The wheel has a radius of $20\text{ m}$. The gondola has traveled $50\text{ m}$ along the circumference. Through what angle has the wheel turned? And how many full turns after $1\text{ km}$?
>
> $\theta = \frac{\ell}{R} = \frac{50}{20} = 2.5\text{ rad}$, which is approximately $143.2^\circ$ (Example 1c).
> For $1000\text{ m}$: $\theta = \frac{1000}{20} = 50\text{ rad}$. One full revolution is $2\pi \approx 6.283\text{ rad}$, and $\frac{50}{2\pi} \approx 7.96$: the wheel has completed $7$ full revolutions and almost an eighth turn (falling short by about $0.04$ of a turn).

> **✅ Worked Example 3 — A Slice of Pizza**
> A pizza with a diameter of $30\text{ cm}$ is sliced into sectors of angle $\frac{\pi}{5}$. What is the crust length and the area of one slice? How many slices are there?
>
> $R = 15\text{ cm}$. Crust: $\ell = 15 \times \frac{\pi}{5} = 3\pi \approx 9.42\text{ cm}$. Area: $\frac{1}{2} \times 15^2 \times \frac{\pi}{5} = \frac{225\pi}{10} = 22.5\pi \approx 70.7\text{ cm}^2$. Number of slices: $\frac{2\pi}{\pi/5} = 10$.

> **⚠️ Beware: Common Pitfall! — Calculator Angle Mode**
> Calculators have a **DEG** mode and a **RAD** mode. If you enter `cos(60)` in RAD mode, you obtain $\cos(60\text{ rad}) \approx -0.952$, rather than $0.5$! Conversely, `cos(π/3)` in DEG mode yields $\cos(1.047^\circ) \approx 0.9998$. Before every exam or calculation, verify the mode. In Python, `math.cos` **always** expects radians; to convert degrees, use `math.radians(60)`.

> **⚠️ Beware: Common Pitfall! — Arc Formulas with Degrees**
> $\ell = R\theta$ is **false** if $\theta$ is in degrees: with $R = 1$ and $\theta = 90$, one would obtain an arc of 90 meters on a circle whose total circumference is only $6.28\text{ m}$! Always convert to radians first.

---

### 3. The Unit Circle and Winding the Real Line

#### 3.1 The Oriented Unit Circle

We work in an orthonormal Cartesian coordinate system $(O ; \vec{\imath}, \vec{\jmath})$—recall: “orthonormal” means both axes are perpendicular and have the same unit length. Let $I(1; 0)$ and $J(0; 1)$.

> **📐 Definition — Unit Circle (Trigonometric Circle)**
> The **unit circle** (or trigonometric circle) is the circle $\mathcal{C}$ centered at the origin $O$ with radius $1$, **oriented**: we choose as the **positive direction** (or direct, counterclockwise, or **trigonometric** direction) the direction opposite to the hands of a clock.

Why this direction? Because it is the direction that leads from $I$ (on the horizontal axis) to $J$ (on the vertical axis) via the shortest path, just as one moves from $\vec{\imath}$ to $\vec{\jmath}$. It is a **convention**—clocks happen to turn in the opposite, clockwise (or indirect) direction.

On this circle of radius $1$, the formula $\ell = R\theta$ becomes $\ell = \theta$: **the radian measure of an angle is precisely the length of the subtended arc**. Here lies the immense power of radius $1$.

#### 3.2 Winding: Every Real Number Becomes a Point

Now picture the real number line as an infinitely long, calibrated **measuring tape**. Place it vertically, tangent to the circle at point $I$, with the zero mark of the line resting on $I$. Then **wind** it:
- the positive half-line wraps around the circle in the **counterclockwise (positive) direction**;
- the negative half-line wraps around in the **clockwise (negative) direction**.

```
                 real number line (tape)
                          ↑  2
                  J       |
               .-*-.      ↑  1
             .'     '.    |
            |    O    *---0   ← the 0 mark is placed at I
             '.     .'    |
               '-*-'      ↓ -1
                          |
                          ↓ -2
      The upper tape wraps toward J (positive direction),
      the lower tape wraps downward (negative direction).
```

Each real number $x$ on the tape comes to rest on a specific point on the circle: we call it the **image point** of $x$, denoted $M(x)$.

- $x = \frac{\pi}{2}$: we have wound one quarter of the circumference ($\frac{2\pi}{4}$): we arrive at $J(0; 1)$.
- $x = \pi$: a half-turn: point $I'(-1; 0)$.
- $x = -\frac{\pi}{2}$: a quarter-turn in the negative direction: point $J'(0; -1)$.
- $x = 2\pi$: a complete turn: back at $I(1; 0)$.

> **📐 Definition — Image Point of a Real Number**
> To every real number $x$, the winding process associates a unique point $M$ on the unit circle, called the **image of $x$**. We also say that $x$ is **a radian measure** of the directed angle $(\vec{OI}, \vec{OM})$.

#### 3.3 One Point, Infinitely Many Reals: “Modulo $2\pi$”

The tape is infinite, but the circle is finite: after one full lap, we pass through the same points again. The real numbers $\frac{\pi}{3}$, $\frac{\pi}{3} + 2\pi = \frac{7\pi}{3}$, $\frac{\pi}{3} + 4\pi = \frac{13\pi}{3}$, $\frac{\pi}{3} - 2\pi = -\frac{5\pi}{3}$… all share **the exact same image point**.

> **📐 Property — Real Numbers Sharing the Same Image**
> Two real numbers $x$ and $y$ have the same image on the circle if and only if their difference is an integer multiple of $2\pi$:
> $$y = x + 2k\pi \quad \text{with } k \in \mathbb{Z}.$$
> We write $y \equiv x \ [2\pi]$, read as “$y$ is congruent to $x$ **modulo** $2\pi$”.

*Reading the notations:* $k \in \mathbb{Z}$ means “$k$ belongs to $\mathbb{Z}$”, i.e., “$k$ is an integer” ($\dots, -2, -1, 0, 1, 2, \dots$); $\mathbb{Z}$ comes from the German *Zahlen*, “numbers” (Chapter 31). The word *modulo* (“according to the measure of”) was introduced by **Gauss** in 1801 for modular arithmetic; here it means “up to an integer number of full revolutions”.

> **📐 Definition — Principal Measure**
> Among all the real numbers sharing the same image point $M$, there exists **exactly one** in the half-open interval $]-\pi, \pi]$. It is called the **principal measure** of the angle.

(Recall of interval notation: $]-\pi, \pi]$ denotes the set of real numbers $x$ such that $-\pi < x \leqslant \pi$; the bracket pointing outward at $-\pi$ means $-\pi$ is **excluded**, while the bracket pointing inward at $\pi$ means $\pi$ is **included**. We exclude $-\pi$ because it represents the same image point as $\pi$: otherwise, point $I'$ would have two principal measures.)

> **🧭 Method — Finding the Principal Measure of $\frac{p\pi}{q}$**
> 1. Look at $\frac{p}{q}$ and seek the nearest **even** multiple: we want $\frac{p\pi}{q} = \alpha + 2k\pi$ with $-\pi < \alpha \leqslant \pi$.
> 2. In practice: divide $p$ by $2q$ to determine how many full revolutions ($2\pi = \frac{2q\pi}{q}$) to subtract or add.
> 3. Adjust by one turn if the remaining value falls outside $]-\pi, \pi]$.

> **✅ Worked Example 4 — Principal Measures**
> Determine the principal measure of: a) $\frac{37\pi}{4}$; b) $-\frac{17\pi}{3}$; c) $\frac{2023\pi}{6}$.
>
> a) One full turn is $\frac{8\pi}{4}$. We write $37 = 8 \times 4 + 5$, so $\frac{37\pi}{4} = \frac{5\pi}{4} + 4 \times 2\pi$. But $\frac{5\pi}{4} > \pi$: we subtract one more full turn: $\frac{5\pi}{4} - 2\pi = -\frac{3\pi}{4}$. The principal measure is $\boxed{-\frac{3\pi}{4}}$.
> *Verification:* $-\frac{3\pi}{4} + 10\pi = -\frac{3\pi}{4} + \frac{40\pi}{4} = \frac{37\pi}{4}$ ✓.
>
> b) One full turn is $\frac{6\pi}{3}$. $-\frac{17\pi}{3} = -\frac{18\pi}{3} + \frac{\pi}{3} = -6\pi + \frac{\pi}{3}$. Since $-6\pi = -3 \times 2\pi$, the principal measure is $\boxed{\frac{\pi}{3}}$.
>
> c) One full turn is $\frac{12\pi}{6}$. $2023 = 12 \times 168 + 7$ (since $12 \times 168 = 2016$). Thus $\frac{2023\pi}{6} = \frac{7\pi}{6} + 168 \times 2\pi$. Since $\frac{7\pi}{6} > \pi$, subtract one turn: $\frac{7\pi}{6} - 2\pi = -\frac{5\pi}{6}$. The principal measure is $\boxed{-\frac{5\pi}{6}}$.

> **⚠️ Beware: Common Pitfall! — Principal Measure and Interval**
> The principal measure lies in $]-\pi, \pi]$, **not** in $[0, 2\pi[$. For $\frac{37\pi}{4}$, answering $\frac{5\pi}{4}$ is incorrect as the “principal measure” (even though $\frac{5\pi}{4}$ has the exact same image point).

#### 3.4 Marking Special Points

By dividing the circle into $4$, $8$, and $12$ equal parts, we locate the images of multiples of $\frac{\pi}{2}$, $\frac{\pi}{4}$, $\frac{\pi}{6}$, and $\frac{\pi}{3}$:

<div align="center">
<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="10"/>
  
  <!-- Coordinate Axes -->
  <line x1="30" y1="200" x2="370" y2="200" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="370,196 378,200 370,204" fill="#0f172a"/>
  <text x="365" y="190" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8">cosine x</text>
  
  <line x1="200" y1="370" x2="200" y2="30" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="196,30 200,22 204,30" fill="#0f172a"/>
  <text x="210" y="32" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b91c1c">sine x</text>
  
  <!-- Unit Circle R = 140 -->
  <circle cx="200" cy="200" r="140" fill="none" stroke="#64748b" stroke-width="2"/>
  
  <!-- Direction arrow -->
  <path d="M 310 140 A 130 130 0 0 0 250 80" fill="none" stroke="#15803d" stroke-width="2.5" stroke-dasharray="4,2"/>
  <polygon points="245,75 258,82 250,90" fill="#15803d"/>
  <text x="300" y="105" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d">Positive (+)</text>

  <!-- Special points and radii (using r=140) -->
  <!-- 0 rad -->
  <circle cx="340" cy="200" r="4" fill="#1d4ed8"/>
  <text x="350" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">0 (2π)</text>

  <!-- pi/6 (30 deg: dx = 140*cos(30) = 121, dy = -140*sin(30) = -70) -> (321, 130) -->
  <line x1="200" y1="200" x2="321" y2="130" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="321" cy="130" r="4" fill="#d97706"/>
  <text x="330" y="130" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/6 (30°)</text>

  <!-- pi/4 (45 deg: dx = 99, dy = -99) -> (299, 101) -->
  <line x1="200" y1="200" x2="299" y2="101" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="299" cy="101" r="4" fill="#d97706"/>
  <text x="308" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/4 (45°)</text>

  <!-- pi/3 (60 deg: dx = 70, dy = -121) -> (270, 79) -->
  <line x1="200" y1="200" x2="270" y2="79" stroke="#cbd5e1" stroke-dasharray="3,3"/>
  <circle cx="270" cy="79" r="4" fill="#d97706"/>
  <text x="275" y="70" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">π/3 (60°)</text>

  <!-- pi/2 (90 deg) -> (200, 60) -->
  <circle cx="200" cy="60" r="4" fill="#b91c1c"/>
  <text x="200" y="52" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">π/2 (90°)</text>

  <!-- pi (180 deg) -> (60, 200) -->
  <circle cx="60" cy="200" r="4" fill="#1d4ed8"/>
  <text x="45" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">π (180°)</text>

  <!-- 3pi/2 (270 deg) -> (200, 340) -->
  <circle cx="200" cy="340" r="4" fill="#b91c1c"/>
  <text x="200" y="360" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">-π/2 (or 3π/2)</text>

  <!-- Origin O -->
  <circle cx="200" cy="200" r="3" fill="#0f172a"/>
  <text x="188" y="215" font-family="sans-serif" font-size="11" fill="#64748b">O</text>
</svg>
</div>

```
                          π/2
                  2π/3     J      π/3
             3π/4    *     *     *    π/4
          5π/6  *                   *  π/6
                                           
         π  I' *          O          * I   0
                                           
         -5π/6  *                   *  -π/6
            -3π/4    *     *     *    -π/4
                  -2π/3     J'    -π/3
                          -π/2
```

> **🧭 Method — Locating $\frac{k\pi}{n}$ Quickly**
> Count in “slices of $\frac{\pi}{n}$”: the upper half-turn ($0$ to $\pi$) contains $n$ such slices. For $\frac{5\pi}{6}$, advance $5$ slices out of $6$ in the upper semicircle: you are almost at $I'$, just above it. For $-\frac{2\pi}{3}$, step downward (negative direction) by $2$ slices out of $3$ in the lower semicircle.

---

### 4. Cosine and Sine of a Real Number

#### 4.1 The Definition

The image point $M(x)$ has two coordinates in the Cartesian system $(O; \vec{\imath}, \vec{\jmath})$. We give them precise names:

> **📐 Definition — Cosine and Sine of a Real Number**
> Let $x$ be a real number and $M$ its image point on the unit circle. We call:
> - the **cosine of $x$**, written $\cos x$ or $\cos(x)$, the **$x$-coordinate (abscissa)** of $M$;
> - the **sine of $x$**, written $\sin x$ or $\sin(x)$, the **$y$-coordinate (ordinate)** of $M$.
> $$M(x) = \big(\cos x \ ; \ \sin x\big).$$

```
                  y
                  ▲
               1  |    . - * M(x)
                  |  .'   /|
                  | /    / |
                  |/  1 /  | sin x
                  |    /   |
           -------O---/----+---------*---> x
                  | x ⌒     cos x    I (1;0)
                  |
                  |
```

Reading: $\cos x$ is pronounced “cosine of $x$”. The abbreviation *cos* originates from *complementi sinus*, “sine of the complement” (we shall see below that $\cos x = \sin(\frac{\pi}{2} - x)$). The notations *sin* and *cos* took hold in the seventeenth century, notably through the English mathematician **William Oughtred**; it was **Euler** who, in the eighteenth century, treated them firmly as **functions** of a real variable.

> **⚠️ Beware: Common Pitfall! — It Is Not a Product**
> $\cos x$ is not “$\cos \times x$”: “cos” by itself is meaningless. Thus $\cos(2x) \neq 2\cos x$, and $\cos(a+b) \neq \cos a + \cos b$ (for instance, $\cos\left(\frac{\pi}{2} + \frac{\pi}{2}\right) = \cos\pi = -1$ whereas $\cos\frac{\pi}{2} + \cos\frac{\pi}{2} = 0$).
> Standard notation: $\cos^2 x$ means $(\cos x)^2$, the square of the cosine—not to be confused with $\cos(x^2)$.

#### 4.2 Return to the Ferris Wheel

Let us place the origin at the center of the wheel, with unit $1 = 20\text{ m}$. Measuring angles from the conventional horizontal line: the position of the gondola at angle $x$ is $(20\cos x, 20\sin x)$ relative to the central axle. Since the gondola starts at the **bottom**, which corresponds to $x = -\frac{\pi}{2}$, after turning through an angle $\theta$ it is at angle $x = \theta - \frac{\pi}{2}$. Its height above the ground is:

$$h(\theta) = 22 + 20\sin\left(\theta - \frac{\pi}{2}\right).$$

Using the identity $\sin\left(\theta - \frac{\pi}{2}\right) = -\cos\theta$, we obtain the elegant formula $h(\theta) = 22 - 20\cos\theta$. Let us check: $\theta = 0$ gives $22 - 20 = 2\text{ m}$ (boarding at bottom) ✓; $\theta = \pi$ gives $22 + 20 = 42\text{ m}$ (summit) ✓.

Answer to your brother: After $50\text{ m}$, $\theta = 2.5\text{ rad}$ and $h = 22 - 20\cos(2.5) \approx 22 - 20 \times (-0.8011) \approx 38.0\text{ m}$. After $1\text{ km}$, $\theta = 50\text{ rad}$ and $h = 22 - 20\cos 50 \approx 22 - 20 \times 0.9650 \approx 2.7\text{ m}$: nearly back at the lowest point, as anticipated (7.96 revolutions).

#### 4.3 First Properties

> **📐 Fundamental Properties** — For every real number $x$ and every integer $k$:
> 1. $-1 \leqslant \cos x \leqslant 1$ and $-1 \leqslant \sin x \leqslant 1$;
> 2. $\cos(x + 2k\pi) = \cos x$ and $\sin(x + 2k\pi) = \sin x$;
> 3. $\boxed{\cos^2 x + \sin^2 x = 1}$.

> **✍️ Proof**
> 1. Point $M$ lies on the circle centered at $O$ with radius $1$, so its coordinates are bounded between $-1$ and $1$.
> 2. $x$ and $x + 2k\pi$ share the same image point (§3.3), and hence have the exact same coordinates.
> 3. $OM = 1$. The distance formula in an orthonormal frame (Chapter 20, a consequence of the Pythagorean Theorem) gives $OM^2 = (\cos x - 0)^2 + (\sin x - 0)^2$, hence $\cos^2 x + \sin^2 x = 1$. $\blacksquare$

#### 4.4 Consistency with Middle School

Does this new definition contradict the middle-school triangle definition? Not at all.

> **📐 Property — Connection to the Right-Angled Triangle**
> If $0 < x < \frac{\pi}{2}$, then $\cos x$ and $\sin x$ coincide with the cosine and sine of the acute angle of measure $x$ in a right-angled triangle.

> **✍️ Proof**
> Let $M(x)$ with $0 < x < \frac{\pi}{2}$: $M$ lies in the upper-right quadrant. Let $H$ be the orthogonal projection of $M$ onto the horizontal axis. The triangle $OHM$ is right-angled at $H$, with hypotenuse $OM = 1$, and the angle $\widehat{HOM}$ measures $x\text{ rad}$. In the sense of middle school:
> $\cos \widehat{HOM} = \frac{OH}{OM} = \frac{OH}{1} = OH$, and $OH$ is precisely the positive $x$-coordinate of $M$. Similarly, $\sin\widehat{HOM} = \frac{HM}{OM} = HM$, which is the $y$-coordinate of $M$. $\blacksquare$

#### 4.5 Signs According to Quadrants

```
                     y
             sin > 0 | sin > 0
             cos < 0 | cos > 0
               (II)  |  (I)
           -----------O-----------> x
              (III)  |  (IV)
             sin < 0 | sin < 0
             cos < 0 | cos > 0
```

> **✅ Worked Example 5 — Using $\cos^2 + \sin^2 = 1$**
> Suppose that $x \in \left]\frac{\pi}{2}, \pi\right[$ and $\sin x = \frac{3}{5}$. Compute $\cos x$.
>
> $\cos^2 x = 1 - \sin^2 x = 1 - \frac{9}{25} = \frac{16}{25}$, so $\cos x = \frac{4}{5}$ or $\cos x = -\frac{4}{5}$.
> However, $x$ lies in Quadrant II, where the cosine is strictly negative. Therefore, $\boxed{\cos x = -\frac{4}{5}}$.

> **⚠️ Beware: Common Pitfall! — Never Forget the Sign**
> $\cos^2 x = \frac{16}{25}$ does not automatically imply $\cos x = \frac{4}{5}$. The quadratic equation $X^2 = a$ (with $a > 0$) has **two** solutions, $\sqrt{a}$ and $-\sqrt{a}$ (Chapter 23). It is the **geometric location of the point** on the circle that decides between them.
