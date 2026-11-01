# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 28: Eratosthenes and the Circumference of the Earth

> *“Do not say that the Earth is too vast to be measured by a mortal. Grant me a simple staff planted upright in the soil, a ray of sunlight, and a right triangle: I will tell you the circumference of the world before the sun sets.”*

---

### What You Are About to Discover

- How **Eratosthenes**, more than 2,200 years ago, calculated the circumference of the Earth using a staff, a well, and a camel caravan.
- How a right triangle constructs three indestructible bridges between **angles** and **lengths**: the **cosine**, the **sine**, and the **tangent**.
- The universal mnemonic **SOH-CAH-TOA** (or **CAH-SOH-TOA**) so you never hesitate again.
- Why the cosine and sine are **strictly bounded between 0 and 1** inside any right triangle.
- How to determine the **inaccessible height of a sea cliff**, the **width of a roaring river**, or the path of a ship without taking a single step across.
- Pythagoras's magical identity in disguise: $\cos^2(x) + \sin^2(x) = 1$.

---

### 1. The Problem: Midday on the Summer Solstice in Alexandria

The date is **June 21**, around the year **240 BC**, beneath the luminous skies of Egypt.
In the coastal city of Alexandria, the polymath **Eratosthenes** presides over the most prestigious library of the ancient world: the Great Library. Hundreds of thousands of papyrus scrolls line cedar shelves.

Eratosthenes reads an astonishing dispatch arriving from the southern frontier town of **Syene** (modern-day Aswan), roughly 800 kilometers up the Nile River:
> *“On the day of the summer solstice, at the stroke of noon, the sun shines straight down to illuminate the water at the bottom of the deepest vertical wells without casting the faintest shadow on their walls. The stone columns of temples cast no shadow on the pavement. The solar rays strike the earth perpendicularly.”*

Eratosthenes waits for that exact day, at that exact hour, in **Alexandria**.
He plants a **gnomon**—a perfectly vertical wooden staff—into level ground, and watches closely.
To his wonder: in Alexandria, at the exact same moment, **the staff casts a clear shadow**!

```
             Solar rays (parallel)
                │ │ │ │ │ │ │ │ │
                ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼

     Alexandria:                           Syene:
       Vertical staff                        Vertical staff
          │                                     │
          │                                     │
       ───┴───────                           ───┴───────
          ▲                                     ▲
        Cast shadow!                         No shadow!
   (The sun strikes at an angle)         (The sun is at the zenith)
```

How is this possible? If the Earth were a flat disk, as ancient poets once imagined, the Sun—situated at a tremendous cosmic distance and showering down parallel light rays—would strike Alexandria at the exact same angle as Syene. There would either be no shadows anywhere, or identical shadows everywhere!

If the staff in Alexandria casts a shadow while the staff in Syene casts none, it can mean only one thing: **the surface of the Earth is curved**!

Eratosthenes measures the height of his staff and the length of its shadow upon the ground. These two segments form a **right triangle**. Comparing these two lengths, he determines that the solar rays deviate from the vertical by an angle of approximately **$7.2^\circ$**.

```
                           Tip of the staff
                                  ● S
                                 /│
                                / │
                               /  │  Vertical staff (height h)
                 Sunbeam      /   │
                             / α  │
                            /     │
                           ●──────■ P (Base of staff)
                           O      Right angle
                           <-- l ->
                         Shadow on ground
```

Now, by the geometric theorem of alternate interior angles (studied in Chapter 15), this $7.2^\circ$ angle at the tip of the staff is **strictly equal to the subtended central angle at the center of the Earth** separating Alexandria from Syene!

```
                                 Alexandria
                                    /
                                   /  Angle α = 7.2°
                                  /
                                 ●─────── Syene
                                /
                               /
                              /
                             ● Center of the Earth
```

Eratosthenes then sets up a luminous proportion:
* A complete circle spans $360^\circ$.
* But $7.2^\circ$ is exactly $\dfrac{7.2}{360} = \dfrac{1}{50}$ of a full circle!
* Therefore, the overland distance between Alexandria and Syene represents **one-fiftieth of the entire circumference of the Earth**.

Royal surveyors and camel caravans estimate this travel distance at approximately **5,000 stadia** (about 800 km).
Eratosthenes multiplies:
$$\text{Earth's Circumference} = 50 \times 5,000 = \mathbf{250,000\text{ stadia}} \approx \mathbf{40,000\text{ kilometers}}!$$

An estimate of staggering precision for antiquity: modern satellite geodesy measures the equatorial circumference at 40,075 km!

Admire the core genius of this feat: to uncover the celestial angle of $7.2^\circ$, Eratosthenes did not ascend into the heavens with a giant protractor. He measured **two linear lengths on the ground** (the height of the staff and the length of its shadow) and deduced **an angle**.

This science connecting the side lengths and angles of a triangle is called **trigonometry** (from Greek *trigōnon*, triangle, and *metron*, measure).

---

### 2. The Right Triangle: Naming the Three Sides

To practice trigonometry without confusion, one must learn to view a right triangle through the eyes of a **specific acute angle**.

Consider triangle $ABC$, right-angled at $B$.
Its two acute angles are $\widehat{A}$ and $\widehat{C}$. Let us choose to view the triangle from acute angle $\widehat{A}$.

```
                 C
                 ▲
                 │ \
                 │  \
  OPPOSITE side  │   \   HYPOTENUSE
  to angle A     │    \  (the longest side,
                 │     \  facing the right angle)
                 │      \
                 ■───────● A
                 B   ^
                 ADJACENT side to angle A
```

Observe the three sides from vertex $A$:
1. **The hypotenuse:** the side directly opposite the $90^\circ$ right angle. It is always the longest side of the right triangle. Here, it is segment $[AC]$. Its identity never depends on which acute angle you select: it is the master side of the right triangle.
2. **The side adjacent to angle $\widehat{A}$:** the word *adjacent* comes from Latin *ad-jacere*, meaning “lying next to.” It is the leg of the right angle that touches angle $\widehat{A}$. Here, it is segment $[AB]$.
3. **The side opposite to angle $\widehat{A}$:** it is the leg of the right angle facing directly across from angle $\widehat{A}$. Here, it is segment $[BC]$.

> **⚠️ Watch Out! Pitfall — Roles Reverse When You Switch Angles!**
> If you shift your perspective to vertex $C$:
> - The hypotenuse remains $[AC]$.
> - The side **adjacent** to $\widehat{C}$ becomes $[BC]$!
> - The side **opposite** to $\widehat{C}$ becomes $[AB]$!
> A side is never “opposite” or “adjacent” in the absolute: it is so **strictly relative to the chosen acute angle**.

---

### 3. The Three Ratios: Cosine, Sine, Tangent

Imagine drawing a right triangle with an acute angle of $30^\circ$.
Whether you draw it in your notebook (hypotenuse 10 cm), on the classroom blackboard (hypotenuse 1 meter), or across the courtyard pavement (hypotenuse 10 meters), these three triangles are exact **dilations** of one another (similar triangles, Chapter 17).

Because their shapes are geometrically identical, **the ratios of their side lengths depend solely on the angle**, and not at all on the physical size of the drawing!

For any given acute angle $x$, these ratios carry three universal names:

> **📐 Fundamental Definitions —** In any right triangle:
>
> 1. The **cosine** of an acute angle is the ratio of the adjacent side to the hypotenuse:
>    $$\cos(x) = \frac{\text{length of adjacent side}}{\text{length of hypotenuse}}$$
>
> 2. The **sine** of an acute angle is the ratio of the opposite side to the hypotenuse:
>    $$\sin(x) = \frac{\text{length of opposite side}}{\text{length of hypotenuse}}$$
>
> 3. The **tangent** of an acute angle is the ratio of the opposite side to the adjacent side:
>    $$\tan(x) = \frac{\text{length of opposite side}}{\text{length of adjacent side}}$$

#### How to Pronounce and Write These Notations
- $\cos(x)$ is written “cos” and read aloud as **“cosine of $x$.”**
- $\sin(x)$ is written “sin” and read aloud as **“sine of $x$.”**
- $\tan(x)$ is written “tan” and read aloud as **“tangent of $x$.”**

#### The Universal Mnemonic: SOH-CAH-TOA
To recall these definitions instantaneously, students across the world chant this phrase like a warrior's banner:

$$\mathbf{S}\text{O}\text{H} \quad-\quad \mathbf{C}\text{A}\text{H} \quad-\quad \mathbf{T}\text{O}\text{A}$$

- **S**ine = **O**pposite / **H**ypotenuse
- **C**osine = **A**djacent / **H**ypotenuse
- **T**angent = **O**pposite / **A**djacent

Some European curricula memorize it in the order **CAH-SOH-TOA**. Both are identical; choose whichever resonates best in your memory!

---

### 4. Two Essential Properties to Master

#### 4.1 Why Cosine and Sine Always Lie Between 0 and 1

In any right triangle, the hypotenuse is strictly the **longest side**.
Consequently, the adjacent leg is strictly shorter than the hypotenuse, and the opposite leg is likewise strictly shorter than the hypotenuse.

Since the numerator is strictly smaller than the denominator (and all lengths are positive):
$$\frac{\text{adjacent}}{\text{hypotenuse}} < 1 \qquad\text{and}\qquad \frac{\text{opposite}}{\text{hypotenuse}} < 1$$

> **📐 Property — Bounds on Cosine and Sine.**
> For any acute angle $x$ in a right triangle ($0^\circ < x < 90^\circ$):
> $$0 < \cos(x) < 1 \qquad\text{and}\qquad 0 < \sin(x) < 1$$

> **⚠️ Watch Out! Pitfall.**
> If on a test you calculate $\cos(x) = 1.45$ or $\sin(x) = 2.3$, **stop immediately**: that is mathematically impossible! You almost certainly inverted the numerator and denominator.
> By contrast, the **tangent** $\tan(x) = \frac{\text{opposite}}{\text{adjacent}}$ can equal any positive real number: it can be $0.5$, $1$, $10$, or even $1,000$ if the triangle is extremely tall and narrow!

#### 4.2 The Fundamental Pythagorean Trigonometric Identity

What happens if we sum the squares of the cosine and sine of the same angle $x$?
Consider our right triangle with adjacent side $a$, opposite side $b$, and hypotenuse $c$.
By the Pythagorean theorem (Chapter 19):
$$a^2 + b^2 = c^2$$

Now compute:
$$\cos^2(x) + \sin^2(x) = \left(\frac{a}{c}\right)^2 + \left(\frac{b}{c}\right)^2 = \frac{a^2}{c^2} + \frac{b^2}{c^2} = \frac{a^2 + b^2}{c^2}$$
Since $a^2 + b^2 = c^2$, we have:
$$\frac{a^2 + b^2}{c^2} = \frac{c^2}{c^2} = 1$$

> **📐 Fundamental Theorem of Trigonometry —**
> For any angle $x$:
> $$\cos^2(x) + \sin^2(x) = 1$$
> *(Note on notation: $\cos^2(x)$ denotes $(\cos(x))^2$, meaning the cosine multiplied by itself).*

Furthermore, dividing sine by cosine yields:
$$\frac{\sin(x)}{\cos(x)} = \frac{\frac{\text{opposite}}{\text{hypotenuse}}}{\frac{\text{adjacent}}{\text{hypotenuse}}} = \frac{\text{opposite}}{\text{adjacent}} = \tan(x)$$

> **📐 Quotient Identity —**
> $$\tan(x) = \frac{\sin(x)}{\cos(x)}$$

These two identities allow you to determine the sine and tangent of an angle the instant its cosine is known, without even determining the angle itself!

> **💡 Did You Know? Where Do These Strange Words Come From?**
> The word **sine** traveled through one of the most famous linguistic misadventures in history. Fifth-century Indian astronomers termed this half-chord *jya-ardha*, shortened to *jiva*. When Arab scholars translated these texts in the 8th century, they transliterated the sound as *jiba*, written *jb* without vowels. In 12th-century Toledo, Spain, the translator Gerard of Cremona mistook this word for the Arabic word *jayb*, which means “crease of a robe, pocket, or bay.” He translated it into Latin as **sinus**, meaning “fold, curve, or gulf” (which also gives us the word “sinuous”)!
> As for **cosine**, it is an abbreviation of *complementi sinus*: the sine of the complementary angle!

---

### 5. Using the Calculator: Two Essential Modes

To carry out trigonometric calculations, you will use the scientific calculator keys: `cos`, `sin`, `tan`.

> **⚠️ Critical Warning! Calculator Angle Mode!**
> A scientific calculator can measure angles in Degrees (DEG), Radians (RAD), or Gradians (GRA). In middle school, **all angles are given in degrees**.
> Always ensure that a small letter **D** or **DEG** appears at the top of your display screen. If you see an **R** or **RAD**, all your calculations will be wrong! To switch to degrees, navigate to the `Setup` or `Mode` menu.

#### Case 1: The Angle Is Known, Find the Ratio
Press the key directly:
- $\cos(60^\circ) = 0.5$ exactly.
- $\sin(30^\circ) = 0.5$ exactly.
- $\tan(45^\circ) = 1$ exactly (because in a half-square, opposite leg = adjacent leg!).
- $\cos(48^\circ) \approx 0.6691...$

#### Case 2: The Ratio Is Known, Find the Angle (Inverse Keys)
If you know that $\cos(x) = 0.8$, what is the angle $x$?
Use the inverse key, labeled **$\arccos$** or **$\cos^{-1}$** (typically accessed by pressing `2nd` or `Shift` followed by `cos`):
- If $\cos(x) = 0.8$, then $x = \arccos(0.8) \approx 36.87^\circ$.
- If $\sin(x) = 0.5$, then $x = \arcsin(0.5) = 30^\circ$.
- If $\tan(x) = 1$, then $x = \arctan(1) = 45^\circ$.

---

### 6. The Two Primary Problems in Middle School Trigonometry

Every middle school trigonometry problem boils down to one of two quests:
1. **Calculate an unknown length** when given an angle and another side length.
2. **Calculate an unknown angle** when given two side lengths.

Here is the 4-step method:

```
                  ┌───────────────────────────────────────────────┐
                  │ 1. Sketch a diagram and identify the right   │
                  │    angle and the target acute angle.          │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 2. Label the three sides:                     │
                  │    Hypotenuse / Adjacent / Opposite.          │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 3. Select the correct formula:                │
                  │    - Adjacent and Hypotenuse? => CAH          │
                  │    - Opposite and Hypotenuse? => SOH          │
                  │    - Opposite and Adjacent?   => TOA          │
                  └───────────────────────┬───────────────────────┘
                                          │
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │ 4. Write the equation, isolate the unknown    │
                  │    (cross-multiply), and evaluate.            │
                  └───────────────────────────────────────────────┘
```

---

### 7. Step-by-Step Worked Examples

#### Example 1: Calculating a length in the numerator
In triangle $KLM$, right-angled at $L$, we are given $KM = 8\text{ cm}$ and $\widehat{K} = 35^\circ$.
Calculate the length of side $[LM]$, rounded to the nearest millimeter.

```
                     M
                     ▲
                     │ \
                     │  \
           LM = ?    │   \  KM = 8 cm
                     │    \
                     │ 35° \
                     ■──────● K
                     L
```

*Detailed Solution:*
1. **Triangle type:** Triangle $KLM$ is right-angled at $L$.
2. **Identify sides relative to angle $\widehat{K} = 35^\circ$:**
   - $[KM]$ is the hypotenuse (known: 8 cm).
   - $[LM]$ is the side **opposite** to $\widehat{K}$ (unknown sought).
3. **Select formula:** Opposite and hypotenuse $\implies$ use **sine** (SOH):
   $$\sin(\widehat{K}) = \frac{LM}{KM}$$
4. **Compute:**
   $$\sin(35^\circ) = \frac{LM}{8}$$
   Multiplying both sides by 8 (or cross-multiplying with $\frac{\sin(35^\circ)}{1} = \frac{LM}{8}$):
   $$LM = 8 \times \sin(35^\circ) \approx 8 \times 0.573576 \approx 4.588\text{ cm}$$
   The length $LM$ is approximately **$4.6\text{ cm}$** (to the nearest millimeter).

---

#### Example 2: Calculating a length in the denominator (The Classic Pitfall)
In triangle $RST$, right-angled at $S$, we know $RS = 5\text{ cm}$ and $\widehat{R} = 40^\circ$.
Calculate the length of hypotenuse $[RT]$, rounded to the nearest millimeter.

```
                     T
                     ▲
                     │ \
                     │  \  RT = ? (Hypotenuse)
                     │   \
                     │ 40°\
                     ■─────● R
                     S  5 cm
```

*Detailed Solution:*
1. Triangle $RST$ is right-angled at $S$.
2. Relative to angle $\widehat{R} = 40^\circ$:
   - $[RS]$ is the **adjacent** side ($RS = 5\text{ cm}$).
   - $[RT]$ is the **hypotenuse** (unknown).
3. Adjacent and hypotenuse $\implies$ use **cosine** (CAH):
   $$\cos(\widehat{R}) = \frac{RS}{RT}$$
4. Substitute values:
   $$\cos(40^\circ) = \frac{5}{RT}$$
   To solve for $RT$ in the denominator, cross-multiply using $\frac{\cos(40^\circ)}{1} = \frac{5}{RT}$:
   $$RT \times \cos(40^\circ) = 5 \times 1 \implies RT = \frac{5}{\cos(40^\circ)}$$
   On the calculator:
   $$RT = \frac{5}{\cos(40^\circ)} \approx \frac{5}{0.766044} \approx 6.527\text{ cm}$$
   The hypotenuse $[RT]$ measures approximately **$6.5\text{ cm}$**.
   *(Sanity check: the hypotenuse is 6.5 cm, strictly longer than the adjacent leg of 5 cm. This is entirely consistent!)*

---

#### Example 3: Calculating an acute angle given two sides
A sailboat approaches a lighthouse erected on a rocky cliff. The top of the cliff rises 42 meters above sea level. The boat is positioned 110 meters horizontally from the base of the cliff.
Under what angle of elevation does the sailor see the top of the cliff? (Round to the nearest tenth of a degree).

```
               Cliff summit F
                     ●
                     │\
                     │ \
             42 m    │  \
                     │   \
                     ■────● Boat B
                     P   ^ Angle α = ?
                       110 m
```

*Detailed Solution:*
1. Triangle $FPB$ formed by the vertical cliff, horizontal water, and line of sight is right-angled at $P$.
2. Relative to angle $\widehat{B}$:
   - The opposite side is the cliff height: $FP = 42\text{ m}$.
   - The adjacent side is the horizontal distance: $PB = 110\text{ m}$.
3. Opposite and adjacent $\implies$ use **tangent** (TOA):
   $$\tan(\widehat{B}) = \frac{FP}{PB} = \frac{42}{110}$$
4. Use the inverse key $\arctan$ (or $\tan^{-1}$) on the calculator:
   $$\widehat{B} = \arctan\left(\frac{42}{110}\right) \approx \arctan(0.3818) \approx 20.899^\circ$$
   The sailor views the cliff top at an angle of elevation of approximately **$20.9^\circ$**.

---

#### Example 4: Fully Solving a Right Triangle
Let $ABC$ be a right triangle at $A$ with $BC = 13\text{ cm}$ and $AB = 5\text{ cm}$.
1. Calculate the exact length of side $AC$.
2. Determine the exact value of $\cos(\widehat{B})$, then the measure of angle $\widehat{B}$ rounded to the nearest degree.
3. Deduce the measure of angle $\widehat{C}$ without using trigonometric functions.

*Detailed Solution:*
1. By the Pythagorean theorem in triangle $ABC$ right-angled at $A$:
   $$BC^2 = AB^2 + AC^2 \implies 13^2 = 5^2 + AC^2 \implies 169 = 25 + AC^2$$
   $$AC^2 = 169 - 25 = 144 \implies AC = \sqrt{144} = 12\text{ cm}.$$
2. In the right triangle, relative to angle $\widehat{B}$:
   $$\cos(\widehat{B}) = \frac{AB}{BC} = \frac{5}{13}$$
   Using the calculator: $\widehat{B} = \arccos\left(\frac{5}{13}\right) \approx 67.38^\circ$, which is **$67^\circ$** to the nearest degree.
3. In a right triangle, the two acute angles are complementary ($\widehat{B} + \widehat{C} = 90^\circ$):
   $$\widehat{C} = 90^\circ - \widehat{B} \approx 90^\circ - 67.38^\circ \approx 22.62^\circ \approx \mathbf{23^\circ}.$$

---

#### Example 5: Finding sine from cosine without finding the angle
An acute angle $x$ satisfies $\cos(x) = \dfrac{3}{5} = 0.6$.
Compute the exact values of $\sin(x)$ and $\tan(x)$ without using the $\arccos$ key on your calculator.

*Detailed Solution:*
1. Apply the fundamental identity $\cos^2(x) + \sin^2(x) = 1$:
   $$\left(\frac{3}{5}\right)^2 + \sin^2(x) = 1 \implies \frac{9}{25} + \sin^2(x) = 1$$
   $$\sin^2(x) = 1 - \frac{9}{25} = \frac{25 - 9}{25} = \frac{16}{25}$$
   Since $x$ is acute, its sine is positive:
   $$\sin(x) = \sqrt{\frac{16}{25}} = \frac{4}{5} = \mathbf{0.8}.$$
2. Apply the quotient identity $\tan(x) = \frac{\sin(x)}{\cos(x)}$:
   $$\tan(x) = \frac{\frac{4}{5}}{\frac{3}{5}} = \frac{4}{5} \times \frac{5}{3} = \frac{4}{3} \approx \mathbf{1.333...}$$
This is the classic 3-4-5 Egyptian right triangle!

---

### Key Takeaways

1. **Right Triangle Vocabulary:**
   - **Hypotenuse**: side facing the right angle, strictly the longest side.
   - **Adjacent side** to an acute angle: the leg of the right angle that touches that angle.
   - **Opposite side** to an acute angle: the leg of the right angle facing that angle.

2. **The Magic Formulas (SOH-CAH-TOA):**
   $$\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}} \qquad \cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}} \qquad \tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}$$

3. **Core Properties:**
   - For any acute angle in a right triangle: $0 < \cos(x) < 1$ and $0 < \sin(x) < 1$.
   - Pythagorean identity: $\cos^2(x) + \sin^2(x) = 1$.
   - Quotient identity: $\tan(x) = \frac{\sin(x)}{\cos(x)}$.
   - Complementary angles: if $\alpha + \beta = 90^\circ$, then $\cos(\alpha) = \sin(\beta)$ and $\sin(\alpha) = \cos(\beta)$.

4. **Calculator Guidelines:**
   - Always ensure the calculator is in **Degree mode (DEG)**.
   - To find a side length: use `sin`, `cos`, or `tan`.
   - To find an angle: use `arcsin` ($\sin^{-1}$), `arccos` ($\cos^{-1}$), or `arctan` ($\tan^{-1}$).

---

### Exercises

#### Level ★: Direct Application

**Exercise 28.1**
In a triangle $DEF$ right-angled at $D$, identify:
1. The hypotenuse.
2. The side adjacent to angle $\widehat{E}$.
3. The side opposite to angle $\widehat{E}$.
4. Write down the ratios $\cos(\widehat{E})$, $\sin(\widehat{E})$, and $\tan(\widehat{E})$ using vertex letters.

**Exercise 28.2**
Using a calculator in Degree mode, provide the rounded value to the nearest thousandth of:
a) $\cos(25^\circ)$
b) $\sin(70^\circ)$
c) $\tan(12^\circ)$
d) $\tan(85^\circ)$

**Exercise 28.3**
Find the measure of acute angle $x$ rounded to the nearest tenth of a degree, given:
a) $\cos(x) = 0.72$
b) $\sin(x) = 0.35$
c) $\tan(x) = 1.8$
d) $\cos(x) = \frac{\sqrt{2}}{2}$

**Exercise 28.4**
Let $ABC$ be a right triangle at $B$ such that $AB = 6\text{ cm}$ and $AC = 10\text{ cm}$.
Calculate the exact value of $\cos(\widehat{A})$, then deduce the measure of angle $\widehat{A}$ rounded to the nearest degree.

**Exercise 28.5**
In triangle $MNO$ right-angled at $N$, $MO = 12\text{ cm}$ and $\widehat{M} = 30^\circ$.
Calculate the exact length of $[NO]$.

---

#### Level ★★: Deeper Reflection and Practical Situations

**Exercise 28.6 (Wheelchair Access Ramp)**
Accessibility regulations mandate that public wheelchair ramps must not form an incline angle greater than $5^\circ$ with the horizontal.
A ramp is 4 meters long and ascends to a porch 40 cm high.
Does this ramp comply with regulations? Justify with calculation.

**Exercise 28.7 (Tree Struck by Lightning)**
During a storm, a 15-meter vertical tree was snapped in two by lightning. The upper portion bent over without detaching from the trunk: its crown touches the ground, forming an angle of $28^\circ$ with the horizontal ground.
At what height did the trunk snap? (Round to the nearest centimeter).

**Exercise 28.8 (Crossing the River)**
A surveyor stands on a riverbank at point $A$, directly facing a landmark tree $C$ on the opposite bank (segment $[AC]$ is perpendicular to the parallel riverbanks).
He walks 50 meters along the bank in a straight line to point $B$. From point $B$, he sights tree $C$ through a theodolite and measures an angle $\widehat{ABC} = 38^\circ$.
What is the width of the river, rounded to the nearest meter?

**Exercise 28.9 (The Rhombus and Its Diagonals)**
A rhombus $ABCD$ has side lengths of 8 cm. One of its interior angles measures $50^\circ$.
Recall the properties of a rhombus's diagonals, then compute the exact length of each diagonal (rounded to the nearest millimeter).

**Exercise 28.10 (Airplane on Descent)**
An airliner flies at an altitude of 9,000 meters at a constant speed of 720 km/h. It begins its descent toward the runway at a constant glide slope of $3^\circ$ below the horizontal.
1. What total flight distance (along its slanted descent path) must it travel before touching down?
2. How long does this descent take, in minutes and seconds?

**Exercise 28.11 (Trigonometric Identities)**
An acute angle $\alpha$ satisfies $\sin(\alpha) = \dfrac{5}{13}$.
1. Without calculating the measure of angle $\alpha$, use the fundamental identity to find the exact value of $\cos(\alpha)$ as an irreducible fraction.
2. Determine the exact value of $\tan(\alpha)$.
3. Verify your results using a calculator.

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 28.12 (Measuring the Inaccessible Tower)**
To measure the height of a medieval fortress tower encircled by a deep moat, a surveyor stands at point $A$ and measures a sight angle of $32^\circ$ to the tower summit.
He then walks straight backward 25 meters across level ground to point $B$, where the sight angle to the summit is $24^\circ$.
Let $h$ be the height of the tower and $x$ the distance from the base of the tower to point $A$.
1. Express $x$ in terms of $h$ and $\tan(32^\circ)$.
2. Express $x + 25$ in terms of $h$ and $\tan(24^\circ)$.
3. Formulate an equation in $h$, and compute the tower height to the nearest decimeter.

**Exercise 28.13 (Eratosthenes' Gnomon Shadow)**
In Alexandria, Eratosthenes planted a vertical gnomon 1 meter in height. The ground shadow measured approximately 12.6 cm.
1. Compute the angle formed by the sunbeams with the vertical staff.
2. Does this recover the historical value of $7.2^\circ$?

**Exercise 28.14 (General Triangle Area Formula)**
Let $ABC$ be an arbitrary triangle where two side lengths $AB = c$ and $AC = b$ are known, along with the acute enclosed angle $\widehat{A}$.
Let $H$ be the foot of the altitude from $C$.
1. In right triangle $ACH$, express altitude $CH$ in terms of $b$ and $\sin(\widehat{A})$.
2. Prove the famous area formula:
   $$\text{Area}(ABC) = \frac{1}{2} b c \sin(\widehat{A})$$
3. Compute the area of a triangle having sides 7 cm and 10 cm enclosing an angle of $40^\circ$.

**Exercise 28.15 (The Isosceles Right Triangle and Exact Values)**
Consider a square $ABCD$ of side length 1. Draw diagonal $[AC]$.
1. What is the nature of triangle $ABC$? What are the measures of its acute angles?
2. Compute the exact length of diagonal $[AC]$ using the Pythagorean theorem.
3. Deduce the exact values of $\cos(45^\circ)$, $\sin(45^\circ)$, and $\tan(45^\circ)$.

---

### Solutions

#### Level ★

- **Solution 28.1:** 1. Hypotenuse: $[EF]$. 2. Adjacent side to $\widehat{E}$: $[DE]$. 3. Opposite side to $\widehat{E}$: $[DF]$. 4. $\cos(\widehat{E}) = \frac{DE}{EF}$, $\sin(\widehat{E}) = \frac{DF}{EF}$, $\tan(\widehat{E}) = \frac{DF}{DE}$.
- **Solution 28.2:** a) $\approx 0.906$; b) $\approx 0.940$; c) $\approx 0.213$; d) $\approx 11.430$.
- **Solution 28.3:** a) $x = \arccos(0.72) \approx 43.9^\circ$; b) $x = \arcsin(0.35) \approx 20.5^\circ$; c) $x = \arctan(1.8) \approx 60.9^\circ$; d) $x = 45^\circ$ because $\cos(45^\circ) = \frac{\sqrt{2}}{2}$.
- **Solution 28.4:** $\cos(\widehat{A}) = \frac{AB}{AC} = \frac{6}{10} = 0.6$. On the calculator, $\widehat{A} = \arccos(0.6) \approx 53^\circ$.
- **Solution 28.5:** In $MNO$ right-angled at $N$, $\sin(\widehat{M}) = \frac{NO}{MO} \implies \sin(30^\circ) = \frac{NO}{12}$. Since $\sin(30^\circ) = 0.5$, $NO = 12 \times 0.5 = 6\text{ cm}$.

---

#### Level ★★

- **Solution 28.6 (Access Ramp):**
  Let $\alpha$ be the ramp's incline angle. The ramp forms the hypotenuse ($4\text{ m} = 400\text{ cm}$) and the rise forms the opposite leg ($40\text{ cm}$).
  $$\sin(\alpha) = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{40}{400} = 0.1$$
  $\alpha = \arcsin(0.1) \approx 5.74^\circ$.
  Since $5.74^\circ > 5^\circ$, the slope is too steep: **the ramp does not comply**.

- **Solution 28.7 (Broken Tree):**
  Let $h$ be the standing trunk height (opposite leg to $28^\circ$).
  The bent upper portion forms the hypotenuse of length $L$.
  Total height is $h + L = 15 \implies L = 15 - h$.
  $$\sin(28^\circ) = \frac{h}{L} = \frac{h}{15 - h}$$
  $$(15 - h)\sin(28^\circ) = h \implies 15\sin(28^\circ) = h(1 + \sin(28^\circ)) \implies h = \frac{15\sin(28^\circ)}{1 + \sin(28^\circ)}$$
  Since $\sin(28^\circ) \approx 0.46947$:
  $$h \approx \frac{15 \times 0.46947}{1 + 0.46947} = \frac{7.042}{1.46947} \approx 4.79\text{ m}.$$
  The tree snapped at approximately **4.79 meters** above ground.

- **Solution 28.8 (River Crossing):**
  Triangle $ABC$ is right-angled at $A$. Relative to $\widehat{B} = 38^\circ$, $[AC]$ is the opposite side (river width) and $[AB] = 50\text{ m}$ is the adjacent leg.
  $$\tan(38^\circ) = \frac{AC}{50} \implies AC = 50 \times \tan(38^\circ) \approx 50 \times 0.781286 \approx 39.06\text{ m}.$$
  The river is approximately **39 meters** wide.

- **Solution 28.9 (Rhombus):**
  Diagonals of a rhombus are perpendicular bisectors of each other and bisect interior angles.
  Let $O$ be the center. $\triangle AOB$ is right-angled at $O$ with hypotenuse $AB = 8\text{ cm}$ and $\widehat{OAB} = 25^\circ$.
  - Half-diagonal $OA$: $\cos(25^\circ) = \frac{OA}{8} \implies OA = 8\cos(25^\circ) \approx 7.2505\text{ cm}$. Long diagonal $AC = 2 \times OA \approx \mathbf{14.5\text{ cm}}$.
  - Half-diagonal $OB$: $\sin(25^\circ) = \frac{OB}{8} \implies OB = 8\sin(25^\circ) \approx 3.3809\text{ cm}$. Short diagonal $BD = 2 \times OB \approx \mathbf{6.8\text{ cm}}$.

- **Solution 28.10 (Airplane Descent):**
  1. Altitude is the opposite leg ($9,000\text{ m}$), flight path is hypotenuse $D$:
     $$\sin(3^\circ) = \frac{9,000}{D} \implies D = \frac{9,000}{\sin(3^\circ)} \approx \frac{9,000}{0.052336} \approx 171,966\text{ m} \approx \mathbf{172\text{ km}}.$$
  2. Velocity is $720\text{ km/h} = \frac{720,000}{3,600} = 200\text{ m/s}$.
     Time $t = \frac{171,966}{200} \approx 859.8\text{ seconds} \approx \mathbf{14\text{ minutes and } 20\text{ seconds}}$.

- **Solution 28.11 (Identities):**
  1. $\cos^2(\alpha) = 1 - \sin^2(\alpha) = 1 - \frac{25}{169} = \frac{144}{169} \implies \cos(\alpha) = \mathbf{\frac{12}{13}}$.
  2. $\tan(\alpha) = \frac{5/13}{12/13} = \mathbf{\frac{5}{12}}$.
  3. $\arcsin(5/13) \approx 22.62^\circ$, $\cos(22.62^\circ) \approx 0.923 \approx 12/13$. Verified.

---

#### Level ★★★

- **Solution 28.12 (Inaccessible Tower):**
  1. $\tan(32^\circ) = \frac{h}{x} \implies x = \frac{h}{\tan(32^\circ)}$.
  2. $\tan(24^\circ) = \frac{h}{x + 25} \implies x + 25 = \frac{h}{\tan(24^\circ)}$.
  3. Subtracting:
     $$25 = h\left(\frac{1}{\tan(24^\circ)} - \frac{1}{\tan(32^\circ)}\right)$$
     $\frac{1}{\tan(24^\circ)} \approx 2.2460$, $\frac{1}{\tan(32^\circ)} \approx 1.6003 \implies \text{Difference} = 0.6457$.
     $$h = \frac{25}{0.6457} \approx \mathbf{38.7\text{ meters}}.$$

- **Solution 28.13 (Eratosthenes' Gnomon):**
  1. Staff height $100\text{ cm}$ (adjacent), shadow $12.6\text{ cm}$ (opposite):
     $$\tan(\alpha) = \frac{12.6}{100} = 0.126 \implies \alpha = \arctan(0.126) \approx 7.18^\circ.$$
  2. Rounded to the nearest tenth, this yields **$7.2^\circ$**, exactly matching Eratosthenes' measurement!

- **Solution 28.14 (General Triangle Area):**
  1. In right triangle $ACH$, $\sin(\widehat{A}) = \frac{CH}{AC} = \frac{CH}{b} \implies CH = b\sin(\widehat{A})$.
  2. $\text{Area} = \frac{1}{2} \times AB \times CH = \frac{1}{2} c b \sin(\widehat{A}) = \frac{1}{2} b c \sin(\widehat{A})$.
  3. For $b = 7$, $c = 10$, $\widehat{A} = 40^\circ$:
     $$\text{Area} = \frac{1}{2} \times 7 \times 10 \times \sin(40^\circ) = 35\sin(40^\circ) \approx 35 \times 0.64279 \approx \mathbf{22.5\text{ cm}^2}.$$

- **Solution 28.15 (45° Angle):**
  1. Triangle $ABC$ has $AB = BC = 1$ and a right angle at $B$: it is an **isosceles right triangle**. Acute angles are $(180^\circ - 90^\circ) / 2 = \mathbf{45^\circ}$.
  2. $AC^2 = 1^2 + 1^2 = 2 \implies AC = \mathbf{\sqrt{2}}$.
  3. Values:
     - $\cos(45^\circ) = \frac{1}{\sqrt{2}} = \mathbf{\frac{\sqrt{2}}{2}} \approx 0.707$.
     - $\sin(45^\circ) = \frac{1}{\sqrt{2}} = \mathbf{\frac{\sqrt{2}}{2}} \approx 0.707$.
     - $\tan(45^\circ) = \frac{1}{1} = \mathbf{1}$.

---

### The Question Opening the Next Chapter

Through trigonometry, we learned to survey continuous space, celestial angles, and vast terrestrial distances. But what happens if we step away from smoothly stretching lengths and return to the realm of **discrete, indivisible integers**?

How can we tile a rectangular hall with square marble slabs without cutting a single tile? How can treasures be divided into strictly equal shares without breaking a single coin?
In Alexandria, a century before Eratosthenes, another intellectual giant established the eternal laws of integer division. Prepare to discover the secrets of divisors and the immortal Euclidean algorithm in Chapter 29: **The Partition of Euclid**.
