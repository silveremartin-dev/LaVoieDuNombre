# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 25: The Doubling Machine and the Tariff Line

> *“An equation is a snapshot: it freezes the balance in search of a motionless treasure. A function is the entire motion picture: it captures the unfolding of the world, where every cause produces an effect, and where every forward step lifts the traveler to a new altitude.”*

---

### What You Are About to Discover

- What a **function** truly is: the marvelous “magic box” that ingests a number and outputs another according to an unchanging rule.
- Official mathematical vocabulary demystified: distinguishing the **input (preimage)** from the **output (image)**, and why we write $f(x)$ or $x \mapsto f(x)$.
- The three reflections of a function: its **formula**, its **table of values**, and its **graph**.
- The **linear function** $f(x) = ax$: the geometric embodiment of pure proportionality, the faithful straight line that never departs from the origin $(0, 0)$.
- The **affine function** $f(x) = ax + b$: the straight line of real-world subscription plans, its **slope (rate of change)** $a$, and its **$y$-intercept** $b$ (the starting entry fee).
- How to graph and read these lines at a single glance: “run 1 to the right, rise by $a$.”
- Thrilling real-life applications: cell phone plans, taxi meters, speeds, and the famous conversion between degrees Celsius and Fahrenheit.

---

### 1. The Problem: The Magic Forge and the Boat Rental Meter

Imagine visiting a village perched on the shore of a grand alpine lake.
At the far end of the pier, two craftsmen offer their services to travelers.

The first is an elderly clockmaker and inventor. In his workshop, he built a steel box equipped with a slot on top and a sliding drawer at the bottom. He calls it his **“Transforming Machine.”**
- If you slip the number **3** into the slot, gears whirl, and the drawer ejects the number **11**.
- If you slip **5** in, the machine ejects **17**.
- If you slip **0** in, it ejects **2**.
- If you slip **$-4$** in, it ejects **$-10$**.

```
                         [ Input : x ]
                                │
                                ▼
                       ┌─────────────────┐
                       │    MACHINE f    │
                       │   “Multiply     │
                       │    by 3 and     │
                       │    add 2”       │
                       └─────────────────┘
                                │
                                ▼
                         [ Output : f(x) ]
```

The village children gather around: *“What secret rule is hidden inside the cogs of the box?”*
Look closely:
- $3 \times 3 + 2 = 9 + 2 = 11$.
- $5 \times 3 + 2 = 15 + 2 = 17$.
- $0 \times 3 + 2 = 2$.
- $(-4) \times 3 + 2 = -12 + 2 = -10$.

The universal rule is unmasked: whatever number $x$ is dropped into the box, the mechanism computes $3x + 2$.

Right beside the workshop, the **boat rental owner** posts his prices for rowing across the lake:
*“To step aboard, each passenger pays a fixed boarding fee of €10 (life vest and insurance). Thereafter, each hour spent on the water costs €15.”*

How much will a family pay to rent a boat for 1 hour? 2 hours? 4 hours?
- For 1 h: $10 + 15 \times 1 = 25$ €.
- For 2 h: $10 + 15 \times 2 = 40$ €.
- For 4 h: $10 + 15 \times 4 = 70$ €.
- For $x$ hours: the total price is $T(x) = 15x + 10$.

Neither of these situations is an equation where we hunt for a single unknown $x$. They are **living rules of correspondence**, continuous bonds of dependence between two dynamic quantities. This is the very soul of the concept of a **function**, the backbone of modern mathematics and all natural sciences.

---

### 2. The Concept of a Function and Its Vocabulary

#### 2.1 What Is a Function?

> **📐 Definition — Function.**
> A **function** is a mathematical process that takes an initial input value (the variable) and assigns to it **one, and only one**, output value (the result).

We typically designate a function by a letter: a lowercase letter such as $f$, $g$, or $h$ (standing for “function”), or an evocative uppercase letter like $T$ (for “Tariff”) or $V$ (for “Volume”).

#### 2.2 Input (Preimage) and Output (Image): Never Confuse Them!

This is the standard terminology you will encounter through senior high school and university. To keep them straight, remember the metaphor of a camera or portrait studio:

```
       BEFORE (Starting Subject)  ──────>  AFTER (Visible Result)
            x : PREIMAGE / INPUT               f(x) : IMAGE / OUTPUT
        “The person posing                 “The photograph printed
         before the lens”                    by the machine”
```

- **The input (preimage / argument)**: the value fed **into** the machine. This is $x$.
- **The output (image / value)**: the computed result that emerges **out** of the machine. This is $f(x)$.

> **⚠️ Critical Warning!**
> - Every input produces **one and only one output** (the machine cannot produce two contradictory results when a single button is pressed).
> - However, a single output may have **multiple different inputs**!
>   *Example:* If the machine squares numbers ($f(x) = x^2$), the output $9$ possesses **two distinct inputs**: $3$ (since $3^2 = 9$) and $-3$ (since $(-3)^2 = 9$).

#### 2.3 Notations: How to Write and Read Functions

| Written Notation | Spoken Phrasing | Exact Meaning |
|---|---|---|
| $f$ | “the function $f$” | The name of the entire machine (the mapping). |
| $f(x)$ | “$f$ of $x$” | The **output value** produced for the input $x$. |
| $x \mapsto f(x)$ | “$x$ maps to $f$ of $x$” | The process arrow (note the bar at the base of the arrow $\mapsto$). |

*Concrete Example:*
Consider the function $g(x) = 2x - 5$.
- Compute the image (output) of $4$:
  Substitute $x = 4$: $g(4) = 2 \times 4 - 5 = 8 - 5 = 3$.
  We say: “The image of $4$ under $g$ is $3$”, or “$4$ is a preimage of $3$ under $g$.”
- Find the preimage (input) of $11$:
  Find the value of $x$ such that $g(x) = 11$. That is an equation!
  $$2x - 5 = 11 \implies 2x = 16 \implies x = 8.$$
  The input that yields $11$ under $g$ is $8$.

---

### 3. The Three Faces of a Single Function

A function is an abstract mathematical object. To visualize and work with it, mathematicians rely on three complementary representations:

```
             ┌───────────────────────────────┐
             │ 1. Algebraic Formula          │
             │    (The Exact Rule)           │
             │    f(x) = 2x + 1              │
             └──────────────┬────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
 ┌──────────────────────┐        ┌──────────────────────┐
 │ 2. Table of Values   │        │ 3. Graph of Function │
 │ (Discrete Samples)   │        │ (Continuous Geometric│
 │                      │        │     Trajectory)      │
 └──────────────────────┘        └──────────────────────┘
```

#### 3.1 The Table of Values
Choose a few values for $x$ on the top row, and calculate their outputs $f(x)$ on the bottom row:

| $x$ (inputs) | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|
| $f(x) = 2x + 1$ (outputs) | $-3$ | $-1$ | $1$ | $3$ | $5$ | $7$ |

Each column provides the coordinates of a point: $(-2, -3)$, $(-1, -1)$, $(0, 1)$, $(1, 3)$, etc.

#### 3.2 The Graph in a Coordinate Plane
Plot these coordinate pairs in a Cartesian plane:
- The horizontal axis ($x$-axis) displays the **inputs $x$**.
- The vertical axis ($y$-axis) displays the **outputs $y = f(x)$**.

> **📐 Definition — Graph of a Function.**
> The graph of a function $f$ (often denoted $\mathcal{C}_f$) is the collection of all points in the plane having coordinates $(x, f(x))$.

---

### 4. The Linear Function: Pure Proportionality $f(x) = ax$

#### 4.1 Definition and Physical Meaning

A **linear function** is the simplest and purest of all functions: it is the algebraic translation of a **perfectly proportional relationship** (as studied in Chapter 13).

> **📐 Definition — Linear Function.**
> A linear function is a function defined by a formula of the form:
> $$f(x) = ax$$
> where $a$ is a fixed real constant, known as the **constant of proportionality** or the **slope**.

*Examples:*
- Buying cherries at €4 per kg: $P(x) = 4x$ ($a = 4$).
- Cycling at a constant speed of 20 km/h: distance $d(t) = 20t$ ($a = 20$).
- A 30% discount: the discounted price is $N(x) = (1 - 0.30)x = 0.7x$ ($a = 0.7$).

#### 4.2 Graphical Representation: The Line Passing Through the Origin

If you plot points belonging to a linear function in a coordinate plane, a geometric wonder appears: **all points align in a straight line passing through the origin $O(0, 0)$**!

Why? Because if you purchase nothing ($x = 0$), you pay nothing ($f(0) = a \times 0 = 0$).

```
             y ▲                    f(x) = 2x
               │                   /
             4 ┼                  /
               │                 /|
             2 ┼                * |
               │               /| |
             0 ┼──────────────*─┼─┼───────> x
                              0 1 2
                   Passes through the origin O(0,0)!
```

> **📐 Graphical Theorem —**
> The graph of a linear function $f(x) = ax$ is **a straight line passing through the origin $O(0, 0)$**.
> Conversely, any non-vertical line passing through the origin represents a linear function.

To plot the graph of a linear function, it suffices to calculate **a single additional point** alongside the origin $(0, 0)$!

---

### 5. The Affine Function: The General Tariff Line $f(x) = ax + b$

#### 5.1 Definition: Proportionality with a Base Fee

What happens when a real-world scenario involves an initial fixed charge (a subscription fee, an opening meter charge, a deposit) to which a proportional rate is added? It is no longer pure proportionality, but an **affine function** (commonly called a linear function with non-zero intercept in English curricula).

> **📐 Definition — Affine Function.**
> An affine function is a function defined for all real numbers $x$ by:
> $$f(x) = ax + b$$
> where $a$ and $b$ are fixed real constants.
> - The constant $a$ is the **slope** (rate of change / directional coefficient).
> - The constant $b$ is the **$y$-intercept** (the initial value at $x = 0$).

#### 5.2 Why This Terminology?
1. **The $y$-intercept ($b$):**
   Evaluate the function at $0$:
   $$f(0) = a \times 0 + b = 0 + b = b.$$
   The point on the line corresponding to $x = 0$ has coordinates $(0, b)$. That is precisely where the line **crosses the vertical $y$-axis**!
2. **The slope ($a$):**
   It governs the tilt and steepness of the line:
   - If $a > 0$, the function is **increasing** (the line rises from left to right).
   - If $a < 0$, the function is **decreasing** (the line falls from left to right).
   - The larger $|a|$, the steeper the line. The closer $|a|$ is to 0, the flatter the line.

```
       y ▲               (a > 0 : Rising)       y ▲
         │                 /                     │ \
         │                /                      │  \
       b ┼───────────────*                     b ┼───*──────────── (a < 0 : Falling)
         │              /                        │    \
         │             /                         │     \
       0 ┼────────────┼──────────> x           0 ┼──────┼─────────> x
                      0                                 0
```

#### 5.3 Special Cases
- If $b = 0$, the formula becomes $f(x) = ax$: a linear function is simply an **affine function that starts at the origin $b = 0$**.
- If $a = 0$, the formula becomes $f(x) = b$: this is a **constant function**. The output is always $b$, regardless of $x$. Its graph is a **horizontal straight line**.

---

### 6. The Art of Graphing and Reading Lines

#### 6.1 The Magic Staircase: “Run 1, Rise $a$”

To draw the line $y = ax + b$ without building a lengthy table of values, use the staircase rule (rise over run):

1. Plot the initial starting anchor on the vertical $y$-axis: the point $(0, b)$.
2. From this point, **step horizontally 1 unit to the right** (Run $+1$).
3. Then:
   - If $a$ is positive: **climb vertically by $a$ units** (Rise $+a$).
   - If $a$ is negative: **drop vertically by $|a|$ units** (Rise $-|a|$).
4. Mark this second point. Place your straightedge through both points: your line is complete!

```
              y ▲
                │
              4 ┼                 ● New point (1, 4)
                │                 ▲
                │                 │ Rise by a = 2
              2 ┼────●────────────┤
                │  (0, b)     Run 1
                │  (b = 2)
              0 ┼─────────────────┼───────> x
                0                 1
```

#### 6.2 Computing the Slope $a$ from Two Given Points

If a line passes through two known points $A(x_A, y_A)$ and $B(x_B, y_B)$ (with $x_A \neq x_B$), its slope is calculated using the fundamental ratio:

$$a = \frac{\text{Vertical change}}{\text{Horizontal change}} = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x} = \frac{\text{Rise}}{\text{Run}}.$$

The symbol $\Delta$ (the uppercase Greek letter Delta) signifies “change” or “difference.”
This formula expresses that the slope measures how many vertical units the line climbs for each unit traveled toward the right.

---

### 7. True History: The Thermometer of Fahrenheit and Celsius

In the 18th century, European scientists sought reliable means to measure temperature.
In 1724, German physicist Daniel Gabriel Fahrenheit constructed the first dependable mercury thermometer. He established:
- $0^\circ\text{F}$: the coldest temperature he could achieve in his laboratory using a mixture of water, ice, and ammonium chloride.
- $96^\circ\text{F}$: the body temperature of a healthy human being (later calibrated to $98.6^\circ\text{F}$).
On his scale, pure water freezes at $32^\circ\text{F}$ and boils at $212^\circ\text{F}$.

In 1742, Swedish astronomer Anders Celsius devised a decimal scale grounded in the fundamental states of pure water:
- $0^\circ\text{C}$ for the freezing point of water.
- $100^\circ\text{C}$ for the boiling point of water.

How do we convert Celsius temperature ($x$) into Fahrenheit temperature ($f(x)$)?
The mapping is precisely an **affine function**!
- The freezing point yields point $A(0, 32)$.
- The boiling point yields point $B(100, 212)$.

Let us compute the slope $a$ and the $y$-intercept $b$:
1. Since $x = 0$ yields $y = 32$, the $y$-intercept is immediately:
   $$b = 32.$$
2. The slope is:
   $$a = \frac{y_B - y_A}{x_B - x_A} = \frac{212 - 32}{100 - 0} = \frac{180}{100} = \frac{9}{5} = 1.8.$$

The universal formula connecting both worlds is:
$$f(x) = 1.8x + 32 \quad \text{or} \quad T_{\text{Fahrenheit}} = \frac{9}{5} T_{\text{Celsius}} + 32.$$

When your bedroom temperature reads $20^\circ\text{C}$, an American reading a Fahrenheit thermometer sees:
$$f(20) = 1.8 \times 20 + 32 = 36 + 32 = 68^\circ\text{F}!$$

---

### 8. Step-by-Step Worked Examples

#### Example 1: Evaluating images and preimages
Consider the affine function $f$ defined by:
$$f(x) = -3x + 7.$$
1. Calculate the image of $4$ and the image of $-2$.
2. Determine the preimage of $-11$.
3. Determine the preimage of $0$.

**Detailed Solution:**
1. To calculate an image, substitute the given value for $x$:
   - $f(4) = -3 \times 4 + 7 = -12 + 7 = -5$. The image of $4$ is $-5$.
   - $f(-2) = -3 \times (-2) + 7 = +6 + 7 = 13$. The image of $-2$ is $13$.
2. Finding the preimage of $-11$ means solving $f(x) = -11$:
   $$-3x + 7 = -11$$
   $$-3x = -11 - 7 = -18$$
   $$x = \frac{-18}{-3} = 6.$$
   The preimage of $-11$ under $f$ is $6$.
3. Finding the preimage of $0$:
   $$-3x + 7 = 0 \implies -3x = -7 \implies x = \frac{-7}{-3} = \frac{7}{3}.$$
   The preimage of $0$ is the irreducible fraction $\frac{7}{3}$.

---

#### Example 2: Determining an affine function from two points
A straight line passes through points $A(2, 5)$ and $B(6, 17)$.
Determine the formula of the affine function $f(x) = ax + b$ whose graph is this line.

**Detailed Solution:**
1. **Compute the slope $a$:**
   $$a = \frac{y_B - y_A}{x_B - x_A} = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3.$$
   The function is now known to be of the form $f(x) = 3x + b$.
2. **Compute the $y$-intercept $b$:**
   Since $A(2, 5)$ lies on the line, $f(2) = 5$:
   $$3 \times 2 + b = 5$$
   $$6 + b = 5 \implies b = 5 - 6 = -1.$$
3. **Conclusion:**
   The desired affine function is:
   $$f(x) = 3x - 1.$$
   *(Quick check with point $B$: $f(6) = 3 \times 6 - 1 = 18 - 1 = 17$. Exact!)*

---

#### Example 3: Finding $a$ and $b$ by graphical inspection
On a given coordinate grid, a straight line $(d)$ crosses the vertical axis at $-3$.
Stepping $2$ grid units to the right requires climbing $5$ units vertically to return to the line.
1. State the $y$-intercept $b$.
2. Calculate the slope $a$.
3. Deduce the formula of the corresponding function.

**Detailed Solution:**
1. The line intersects the vertical axis at $-3$, so:
   $$b = -3.$$
2. Running 2 units right and rising 5 units means:
   $$\Delta x = +2 \quad \text{and} \quad \Delta y = +5.$$
   The slope is:
   $$a = \frac{\Delta y}{\Delta x} = \frac{5}{2} = 2.5.$$
3. The function formula is:
   $$f(x) = 2.5x - 3 \quad \left(\text{or } f(x) = \frac{5}{2}x - 3\right).$$

---

#### Example 4: Mobile phone plan comparison
A telecommunications provider offers two mobile subscriptions:
- **Eco Plan:** €0.10 per call minute, with no monthly base fee.
- **Serenity Plan:** A fixed monthly fee of €12, plus €0.02 per call minute.
1. Write formulas for $E(x)$ and $S(x)$ giving the monthly cost for $x$ call minutes.
2. Identify the mathematical type of each function.
3. Compute the monthly bill for 60 minutes of calls under each plan.
4. Beyond how many minutes per month does the Serenity Plan become cheaper than the Eco Plan?

**Detailed Solution:**
1. For $x$ minutes:
   - $E(x) = 0.10x$.
   - $S(x) = 0.02x + 12$.
2. $E$ is a **linear function** (pure proportionality, passing through the origin).
   $S$ is an **affine function** (with non-zero base intercept $b = 12$).
3. For 60 minutes:
   - $E(60) = 0.10 \times 60 = 6$ €.
   - $S(60) = 0.02 \times 60 + 12 = 1.20 + 12 = 13.20$ €.
4. Serenity is cheaper when its cost is strictly less than Eco:
   $$S(x) < E(x) \iff 0.02x + 12 < 0.10x$$
   $$12 < 0.10x - 0.02x \implies 12 < 0.08x \implies x > \frac{12}{0.08} = 150.$$
   Conclusion: The Serenity Plan becomes more economical whenever calling exceeds **150 minutes (2 hours 30 minutes) per month**.

---

#### Example 5: Speed, distance, and affine functions
A water cistern contains 800 liters. At 8:00 AM, a drain valve is opened: water empties at a steady, constant rate of 25 liters per minute.
1. Express the remaining volume $V(t)$ (in liters) in terms of elapsed time $t$ (in minutes).
2. What is the nature of function $V$? What is the sign of its slope?
3. How much water remains after 12 minutes?
4. How long until the cistern is completely dry?

**Detailed Solution:**
1. At time $t = 0$, there are 800 L. Every minute, 25 L drain out:
   $$V(t) = 800 - 25t = -25t + 800.$$
2. $V$ is an **affine function** with slope $a = -25$ and $y$-intercept $b = 800$.
   Its slope is **negative** ($a = -25 < 0$), so the function is **decreasing** (volume decreases over time).
3. At $t = 12$ min:
   $$V(12) = -25 \times 12 + 800 = -300 + 800 = 500\text{ liters}.$$
4. The cistern is empty when $V(t) = 0$:
   $$V(t) = 0 \iff -25t + 800 = 0 \iff 25t = 800 \iff t = \frac{800}{25} = 32\text{ minutes}.$$
   The tank will be completely empty at 8:32 AM.

---

### Key Takeaways

1. **Core Vocabulary:**
   - $x$ is the **input / preimage** (the starting value).
   - $f(x)$ is the **output / image** of $x$ under $f$ (the computed result).
   - The mapping notation $f : x \mapsto f(x)$ reads: “the function $f$ that maps $x$ to $f(x)$.”
2. **Linear Function: $f(x) = ax$**
   - Represents pure **proportionality**.
   - Its graph is **a straight line strictly passing through the origin $O(0, 0)$**.
3. **Affine Function: $f(x) = ax + b$**
   - Its graph is **a straight line** intersecting the vertical $y$-axis at $(0, b)$.
   - $b$ is the **$y$-intercept**: $f(0) = b$.
   - $a$ is the **slope (rate of change)**:
     $$a = \frac{y_B - y_A}{x_B - x_A} = \frac{\Delta y}{\Delta x}.$$
     If $a > 0$, the line rises. If $a < 0$, the line falls. If $a = 0$, the line is horizontal (constant function).
4. **Graphical Reading:**
   - To find an output given an input: start at $x$ on the horizontal axis, move vertically to meet the line, then read $y$ on the vertical axis.
   - To find an input given an output: start at $y$ on the vertical axis, move horizontally to meet the line, then read $x$ on the horizontal axis.

---

### Exercises

#### Level ★: Direct Application

**Exercise 25.1** Vocabulary and Notations:
Let $h$ be a function such that $h(3) = 7$.
1. What is the image of 3 under $h$?
2. What is a preimage of 7 under $h$?
3. Translate into an equation of the form $f(a) = b$ the statement: “The image of $-5$ under the function $f$ is $12$.”
4. Translate into an equation the statement: “$-2$ is a preimage of $9$ under the function $g$.”

**Exercise 25.2** Evaluating Images:
Consider the affine function $f(x) = 4x - 5$.
Calculate:
1. $f(0)$
2. $f(3)$
3. $f(-2)$
4. $f\left(\frac{1}{2}\right)$

**Exercise 25.3** Finding Preimages:
Using the same function $f(x) = 4x - 5$, determine the preimage of:
1. $15$
2. $-5$
3. $0$
4. $-13$

**Exercise 25.4** Classifying Functions:
State whether each function is linear, affine (non-linear), or neither:
1. $f(x) = 5x$
2. $g(x) = 3x - 8$
3. $h(x) = x^2 + 1$
4. $k(x) = 7$
5. $m(x) = \frac{4}{x}$
6. $p(x) = \frac{x}{5} + 2$

**Exercise 25.5** Graphing Lines:
In a Cartesian coordinate plane, plot the graphs of:
1. $d_1 : f(x) = 2x$
2. $d_2 : g(x) = -x$
3. $d_3 : h(x) = 2x - 3$
4. $d_4 : k(x) = -0.5x + 2$

---

#### Level ★★: Deeper Reflection and Multi-Step Problems

**Exercise 25.6** Deriving Formulas from Points:
1. A linear function $g$ satisfies $g(4) = 14$. Determine the formula for $g(x)$.
2. An affine function $f$ passes through $A(1, 4)$ and $B(3, 10)$. Compute its slope $a$, its $y$-intercept $b$, and write down $f(x)$.

**Exercise 25.7** Reverse Graphical Reading:
A straight line representing an affine function $f$ intersects the vertical axis at $(0, 4)$ and passes through $(4, 0)$.
1. State the value of $b$.
2. Calculate the slope $a$.
3. Write the formula for $f(x)$.
4. Is $f$ increasing or decreasing?

**Exercise 25.8** The Night Taxi:
A taxi driver applies the following rate schedule:
- Base flag drop fee upon starting the meter: €4.20.
- Per-kilometer rate: €1.60.
1. Write an expression for the total fare $C(x)$ for a trip of $x$ kilometers.
2. How much does a 15 km ride cost?
3. A passenger has a €25 note. What maximum distance can they travel?

**Exercise 25.9** Point Membership on a Line:
Let $f(x) = -2x + 7$.
1. Does point $M(3, 1)$ lie on the graph of $f$?
2. Does point $N(-4, 15)$ lie on this line?
3. Find the $x$-coordinate of the point $P$ on the line having $y$-coordinate $-9$.

**Exercise 25.10** Intersection of Two Affine Functions:
Consider $f(x) = 2x - 1$ and $g(x) = -x + 5$.
1. Graph both lines on the same axes.
2. Read the coordinates of their intersection point $I$ from the graph.
3. Verify these coordinates algebraically by solving $f(x) = g(x)$.

**Exercise 25.11** The Burning Candle:
A candle is 24 cm tall. When lit, its height decreases at a steady rate of 1.5 cm per hour.
1. Express the candle's height $h(t)$ in centimeters after $t$ hours.
2. What is the height after 6 hours?
3. How many hours until the candle is completely burned down?

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 25.12** Collinearity of Three Points:
Consider three points in a coordinate plane: $A(-2, -7)$, $B(2, 5)$, and $C(5, 14)$.
1. Determine the affine function $f$ whose line passes through $A$ and $B$.
2. Is point $C$ collinear with $A$ and $B$? (Hint: test whether $f(5) = 14$).

**Exercise 25.13** Parallelism and Lines:
Line $(d_1)$ represents the function $f(x) = 3x - 4$.
We seek a line $(d_2)$ that is **parallel** to $(d_1)$ and passes through point $E(2, 9)$.
1. What must be true about the slope of $(d_2)$ compared to $(d_1)$?
2. Deduce the formula of the affine function $g$ associated with $(d_2)$.

**Exercise 25.14** The Double-Hop Box Mystery:
An unknown affine function $f(x) = ax + b$ possesses this remarkable property:
When applied twice in succession—that is, computing $f(f(x))$—it always yields $4x + 9$!
1. Expand the algebraic expression $f(f(x)) = a(ax + b) + b$.
2. By equating coefficients with $4x + 9$, find the two possible values for $a$.
3. Deduce the two affine functions that solve this riddle.

---

### Solutions

#### Level ★

**Solution 25.1**
1. The image of 3 is 7.
2. A preimage of 7 is 3.
3. $f(-5) = 12$.
4. $g(-2) = 9$.

**Solution 25.2**
1. $f(0) = 4(0) - 5 = -5$.
2. $f(3) = 4(3) - 5 = 12 - 5 = 7$.
3. $f(-2) = 4(-2) - 5 = -8 - 5 = -13$.
4. $f\left(\frac{1}{2}\right) = 4 \times \frac{1}{2} - 5 = 2 - 5 = -3$.

**Solution 25.3**
1. $4x - 5 = 15 \implies 4x = 20 \implies x = 5$.
2. $4x - 5 = -5 \implies 4x = 0 \implies x = 0$.
3. $4x - 5 = 0 \implies 4x = 5 \implies x = \frac{5}{4} = 1.25$.
4. $4x - 5 = -13 \implies 4x = -8 \implies x = -2$.

**Solution 25.4**
1. $f(x) = 5x$: linear (and affine with $b = 0$).
2. $g(x) = 3x - 8$: affine non-linear ($a = 3, b = -8$).
3. $h(x) = x^2 + 1$: neither (quadratic term, not affine).
4. $k(x) = 7$: constant (affine with $a = 0, b = 7$).
5. $m(x) = \frac{4}{x}$: neither (inverse variation, $x$ in denominator).
6. $p(x) = \frac{1}{5}x + 2$: affine ($a = 0.2, b = 2$).

**Solution 25.5**
1. $d_1$ passes through $(0, 0)$ and $(1, 2)$.
2. $d_2$ passes through $(0, 0)$ and $(1, -1)$.
3. $d_3$ passes through $(0, -3)$ and $(1, -1)$ (or $(2, 1)$).
4. $d_4$ passes through $(0, 2)$ and $(2, 1)$ (or $(4, 0)$).

---

#### Level ★★

**Solution 25.6**
1. $g(x) = ax$. Since $g(4) = 14$, $4a = 14 \implies a = \frac{14}{4} = 3.5$. Thus $g(x) = 3.5x$.
2. $a = \frac{y_B - y_A}{x_B - x_A} = \frac{10 - 4}{3 - 1} = \frac{6}{2} = 3$.
   So $f(x) = 3x + b$.
   Using $A(1, 4)$: $3(1) + b = 4 \implies b = 1$.
   Thus $f(x) = 3x + 1$.

**Solution 25.7**
1. Line meets $y$-axis at $(0, 4)$, so $b = 4$.
2. Passes through $(4, 0)$, so $a = \frac{0 - 4}{4 - 0} = \frac{-4}{4} = -1$.
3. $f(x) = -x + 4$.
4. Since $a = -1 < 0$, the function is **strictly decreasing** (line slopes downward).

**Solution 25.8**
1. $C(x) = 1.60x + 4.20$.
2. For 15 km: $C(15) = 1.60 \times 15 + 4.20 = 24 + 4.20 = 28.20$ €.
3. With €25: $1.60x + 4.20 \le 25 \implies 1.60x \le 20.80 \implies x \le \frac{20.80}{1.60} = 13$ km.
   The maximum distance is 13 km.

**Solution 25.9**
1. Check $f(3)$: $f(3) = -2(3) + 7 = -6 + 7 = 1$. Matches the $y$-coordinate, so $M(3, 1)$ lies on the line.
2. Check $f(-4)$: $f(-4) = -2(-4) + 7 = 8 + 7 = 15$. Yes, $N(-4, 15)$ also lies on the line.
3. Solve $f(x) = -9$: $-2x + 7 = -9 \implies -2x = -16 \implies x = 8$. The $x$-coordinate of $P$ is 8.

**Solution 25.10**
1. Plot lines: $f$ crosses $(0, -1)$ and $(2, 3)$; $g$ crosses $(0, 5)$ and $(2, 3)$.
2. Graphically, the intersection point is $I(2, 3)$.
3. Algebraically:
   $$f(x) = g(x) \iff 2x - 1 = -x + 5 \iff 3x = 6 \iff x = 2.$$
   Then $f(2) = 2(2) - 1 = 3$. The point is confirmed: $I(2, 3)$.

**Solution 25.11**
1. $h(t) = -1.5t + 24$.
2. After 6 hours: $h(6) = -1.5 \times 6 + 24 = -9 + 24 = 15\text{ cm}$.
3. Burned out when $h(t) = 0$:
   $$-1.5t + 24 = 0 \iff 1.5t = 24 \iff t = \frac{24}{1.5} = 16\text{ hours}.$$

---

#### Level ★★★

**Solution 25.12**
1. Find line through $A(-2, -7)$ and $B(2, 5)$:
   $a = \frac{5 - (-7)}{2 - (-2)} = \frac{12}{4} = 3$.
   $f(x) = 3x + b$. With $B(2, 5)$: $3(2) + b = 5 \implies b = -1$.
   So $f(x) = 3x - 1$.
2. Test $C(5, 14)$:
   $f(5) = 3(5) - 1 = 15 - 1 = 14$.
   The equality is verified: point $C$ is **collinear** with $A$ and $B$!

**Solution 25.13**
1. Two lines are parallel if and only if they have the **exact same slope**. Thus $(d_2)$ has slope $a = 3$.
2. $g(x) = 3x + b$. Since it passes through $E(2, 9)$:
   $$3(2) + b = 9 \implies 6 + b = 9 \implies b = 3.$$
   Formula: $g(x) = 3x + 3$.

**Solution 25.14**
1. Apply $f$ to $f(x) = ax + b$:
   $$f(f(x)) = a(ax + b) + b = a^2x + ab + b = a^2x + b(a + 1).$$
2. Equate to $4x + 9$ for all $x$:
   - For the $x$ coefficient: $a^2 = 4 \implies a = 2$ or $a = -2$.
   - For the constant term: $b(a + 1) = 9$.
3. Two cases arise:
   - Case 1: if $a = 2$, then $b(2 + 1) = 9 \implies 3b = 9 \implies b = 3$.
     First function: $f_1(x) = 2x + 3$.
     *(Check: $f_1(f_1(x)) = 2(2x + 3) + 3 = 4x + 6 + 3 = 4x + 9$!)*
   - Case 2: if $a = -2$, then $b(-2 + 1) = 9 \implies b(-1) = 9 \implies b = -9$.
     Second function: $f_2(x) = -2x - 9$.
     *(Check: $f_2(f_2(x)) = -2(-2x - 9) - 9 = 4x + 18 - 9 = 4x + 9$!)*

---

### The Question Opening the Next Chapter

Thus far, numbers have served to calculate weights, prices, areas, and linear trajectories. But look around you: a repeating fabric pattern, roof tiles, a six-petaled flower, the infinite mosaics of the Alhambra in Granada, or the dizzying art of M. C. Escher.

How can a single triangle or shape **slide**, **rotate**, **reflect across a mirror**, or **expand under a magnifying glass** while preserving its exact proportions? That is the enchanting realm of plane transformations that we will explore in Chapter 26: **Paper Folding and the Magic Mirror**.
