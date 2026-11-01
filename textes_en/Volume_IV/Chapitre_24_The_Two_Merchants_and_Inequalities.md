# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 24: The Two Merchants and Inequalities

> *“As long as both pans remain level, the world sleeps in motionless peace. But the moment one pan plunges, motion is born. Inequality is not a defect of justice: it is the driving engine of commerce, the breakeven threshold, the exact frontier where one decision becomes superior to another.”*

---

### What You Are About to Discover

- How to reason about an **unbalanced scale** without tipping it over.
- The notations $\le, \ge, <, >$: what they mean and how to read them without hesitation.
- The golden rule of inequalities: why adding or subtracting preserves order, why multiplying by a positive number changes nothing…
- … and why **multiplying or dividing by a negative number REVERSES the direction** of the inequality (the mystery of the mirror and the thermometer).
- How to solve a **first-degree inequality** and plot its solutions on a **number line** using oriented brackets.
- How to unravel the secret of two unknowns at once using **systems of linear equations**: the **substitution method** and the **elimination (linear combination) method**.
- The luminous geometric interpretation: a system is nothing other than the **point of intersection of two lines**.
- Exciting real-world applications: comparing merchant pricing schemes, calculating breakeven points, and formulating perfect mixtures.

---

### 1. The Problem: The Spice Fair of Venice and the Merchant's Dilemma

The year is **1340**, upon the Rialto quayside in **Venice**. The galleys have returned from the Levant, their holds heavy with cinnamon, black pepper, and saffron. Two Venetian merchants, Giovanni and Marco, have set up their stalls facing each other in the bustling marketplace. Both sell the exact same first-press olive oil from Crete.

Yet each offers a different pricing scheme to entice tavern keepers and ship captains:

* **Merchant Giovanni** announces:
  *“Free entry! No membership fee! I sell every liter of olive oil at the fixed price of 6 ducats per liter.”*
* **Merchant Marco**, more cunning, proposes:
  *“Purchase a seasonal patron card for 30 ducats, and I will deliver every liter of oil to you for only 4 ducats per liter!”*

```
     Giovanni's Tariff:  Total Price = 6 × Number of liters
     Marco's Tariff   :  Total Price = 30 + 4 × Number of liters
```

A tavern keeper stops, hesitating, clutching the purse at his belt. He asks his young apprentice:
*“From whom should we buy our oil this season?”*

The apprentice replies with common sense:
*“That depends on our consumption, master! If we only purchase 2 liters for the week, Giovanni costs us $2 \times 6 = 12$ ducats, whereas with Marco we would pay $30 + 4 \times 2 = 38$ ducats: Giovanni is far cheaper.
But if we run a large tavern and purchase 50 liters, Giovanni would cost us $50 \times 6 = 300$ ducats, while Marco would charge us only $30 + 4 \times 50 = 230$ ducats: Marco becomes significantly less expensive!”*

The master tavern keeper knits his brow:
*“Very well. But at **exactly how many liters** does Marco's price become more advantageous than Giovanni's?”*

This is no longer an equality to be solved, but an **inequality**:
$$30 + 4x < 6x.$$
We seek the region where the total expenditure with Marco is *strictly less than* that with Giovanni.

And that is not all. The next morning, Giovanni and Marco partner together to sell a lot of 100 amphorae containing a total of 380 liters of oil. Some amphorae hold 3 liters, while others hold 5 liters. How many amphorae of each kind are there? This is a problem with **two unknowns**, where two conditions must be satisfied simultaneously.

To answer the tavern keeper and pierce the secrets of the market, we must forge two new mathematical tools: **inequalities** and **linear systems**.

---

### 2. The Language of Inequalities: Comparing Quantities

#### 2.1 Symbols and Reading Direction

In mathematics, an equality ($=$) asserts that two quantities have the exact same value. An **inequality** captures an imbalance: one quantity is greater or smaller than another.

| Symbol | Meaning | Read Aloud | Example |
|---|---|---|---|
| $<$ | Strictly less than | “is strictly less than” | $3 < 7$ |
| $>$ | Strictly greater than | “is strictly greater than” | $8 > 2$ |
| $\le$ or $\leqslant$ | Less than or equal to | “is less than or equal to” (at most) | $x \le 10$ ($x$ is 10 or less) |
| $\ge$ or $\geqslant$ | Greater than or equal to | “is greater than or equal to” (at least) | $x \ge 18$ ($x$ is 18 or more) |

> **💡 The Arrowhead Visual Rule —** The symbol always opens wide toward the larger number and points its sharp tip toward the smaller number:
> $$\text{BIG} > \text{small} \qquad \text{small} < \text{BIG}.$$

- **Strict inequality ($<$ or $>$) :** Equality is strictly excluded. If age $a > 12$, being exactly 12 years old does not qualify.
- **Non-strict (weak) inequality ($\le$ or $\ge$) :** Equality is accepted. If test score $s \ge 10$, scoring exactly 10 is sufficient to pass.

---

### 3. The Rules of the Tilted Scale

Let us return to Al-Khwarizmi's two-pan scale, but this time, **the beam tilts**. The left pan sits higher than the right pan: the left side is lighter than the right side ($A < B$).

```
                A (Lighter)
                o─────o
                \     /
                 \   /                           B (Heavier)
        ───────────[■]────────                  o─────o
                              \                 \     /
                               \                 \   /
                                ───────────[■]────────
                                     ▲
```

What occurs if we perform identical operations on both pans simultaneously?

#### 3.1 Rule 1: Adding or Subtracting the Same Number

If you place 2 kg of lead on the left pan AND 2 kg of lead on the right pan, the right pan remains heavier. The direction of the tilt does not budge by a millimeter.
Likewise, if you remove 3 kg from both sides, the scale preserves its exact tilt.

> **📐 Fundamental Rule 1 — Addition and Subtraction.**
> The direction of an inequality does not change if you **add** or **subtract** the same number from both sides:
> $$\text{If } a < b, \text{ then } a + c < b + c \quad \text{and} \quad a - c < b - c.$$

*Numerical Example:*
We know that $3 < 8$.
- Add $5$: $3 + 5 < 8 + 5 \implies 8 < 13$ (true).
- Subtract $10$: $3 - 10 < 8 - 10 \implies -7 < -2$ (true, $-7^\circ\text{C}$ is colder than $-2^\circ\text{C}$).

#### 3.2 Rule 2: Multiplying or Dividing by a POSITIVE Number

If you triple the contents of the left pan and triple the contents of the right pan, the heavier side becomes three times heavier, and the lighter side three times lighter. The direction of imbalance remains unchanged.

> **📐 Fundamental Rule 2 — Multiplying and Dividing by a POSITIVE Number ($c > 0$).**
> The direction of an inequality does not change if you **multiply** or **divide** both sides by the same **strictly positive** number:
> $$\text{If } a < b \text{ and } c > 0, \text{ then } a \times c < b \times c \quad \text{and} \quad \frac{a}{c} < \frac{b}{c}.$$

*Numerical Example:*
We have $-4 < 6$. Multiply by $3$:
$$-4 \times 3 < 6 \times 3 \implies -12 < 18 \quad \text{(still true)}.$$

#### 3.3 Rule 3: The Great Reversal! Multiplying or Dividing by a NEGATIVE Number

Here unfolds the most surprising phenomenon in algebra, the one that trips up countless students.

Take two self-evident numbers:
$$2 < 5.$$
Multiply both sides by $-1$. What do they become?
- On the left: $2 \times (-1) = -2$.
- On the right: $5 \times (-1) = -5$.

Now compare $-2$ and $-5$. Which number is greater?
On a thermometer, $-2^\circ\text{C}$ is warmer than $-5^\circ\text{C}$.
On the number line, $-2$ is located **to the right** of $-5$:
$$-2 > -5\text{ !}$$

**The inequality has flipped!** The sign $<$ became $>$.

```
     ───|──────|──────|──────|──────|──────|──────|──────|──────|──────|───>
       -5     -4     -3     -2     -1      0      1      2      3      5
        ▲                    ▲                    ▲                    ▲
        └────── < ───────────┘                    └──────── < ─────────┘
            -5 is LESS than -2                        2 is LESS than 5
```

> **📐 Fundamental Rule 3 — Multiplying and Dividing by a NEGATIVE Number ($c < 0$).**
> **Whenever you multiply or divide both sides of an inequality by a STRICTLY NEGATIVE number, YOU MUST REVERSE THE DIRECTION OF THE INEQUALITY SYMBOL!**
> $$\text{If } a < b \text{ and } c < 0, \text{ then } a \times c \mathbf{ > } b \times c \quad \text{and} \quad \frac{a}{c} \mathbf{ > } \frac{b}{c}.$$

**Why this reversal? Two concrete insights:**
1. **The Mirror Reflection:** Multiplying by $-1$ rotates the number line through a half-turn around zero. Whatever lay farthest to the right in the positive realm ($+5$) is hurled farthest to the left in the negative realm ($-5$). The champion of greatness becomes the champion of smallness!
2. **The Debt Analogy:** Is having \$200 in your account better than having \$500? No, $200 < 500$. But having a **debt** of \$200 ($-200$) is vastly preferable to having a debt of \$500 ($-500$)! Therefore, $-200 > -500$.

---

### 4. Solving Inequalities and Graphical Representation

#### 4.1 What Is an Inequality?

A first-degree inequality is an inequality involving an unknown $x$.
Unlike a standard linear equation which typically yields a single isolated solution ($x = 3$), an inequality generally possesses **infinitely many solutions**: an entire continuum of numbers forming an interval.

#### 4.2 Step-by-Step Solution Example

Let us solve the inequality from our merchants' pricing problem:
$$30 + 4x < 6x.$$

1. **Group the variable terms:**
   Subtract $4x$ from both sides (Rule 1: subtraction preserves direction):
   $$30 + 4x - 4x < 6x - 4x$$
   $$30 < 2x.$$
2. **Isolate $x$:**
   Divide both sides by $+2$ (Rule 2: division by a positive number preserves direction):
   $$\frac{30}{2} < \frac{2x}{2} \implies 15 < x \quad \text{which means} \quad x > 15.$$
3. **Conclusion for the Merchants:**
   As soon as the tavern keeper purchases **strictly more than 15 liters of oil**, Marco's pricing becomes the more economical choice! At exactly 15 liters, both merchants charge the identical sum ($15 \times 6 = 90$ ducats and $30 + 4 \times 15 = 90$ ducats).

#### 4.3 An Example Involving Symbol Reversal

Solve the inequality:
$$-3x + 7 \le 22.$$

1. Subtract $7$ from both sides:
   $$-3x \le 22 - 7 \implies -3x \le 15.$$
2. Divide by the coefficient of $x$, which is **$-3$ (negative)**.
   **Red alert: immediately flip the inequality sign!**
   $$\frac{-3x}{-3} \ge \frac{15}{-3}$$
   $$x \ge -5.$$
The solutions are all real numbers greater than or equal to $-5$.

#### 4.4 Graphing Solutions on the Number Line

Because there are infinitely many solutions, we depict them visually by shading the corresponding ray on the number line.

How do we indicate whether the boundary number itself is included or excluded? **Through the orientation of brackets!**

- **The bracket faces TOWARD the shaded solution set:** the boundary value is **included** ($\le$ or $\ge$).
  Example for $x \ge -5$:
  ```
  ──────────┼──────────[████████████████████████████████>
           -5          -5 is included (bracket opens rightward)
  ```
- **The bracket turns its BACK to the shaded solution set:** the boundary value is **excluded** ($<$ or $>$).
  Example for $x > 15$:
  ```
  ──────────┼──────────]████████████████████████████████>
            0          15 is excluded (bracket faces away from shaded zone)
  ```

> **🧭 Method — Writing Solutions in Interval Notation.**
> In standard mathematics, the solution set $S$ is written using intervals:
> - For $x \ge -5$: $S = [-5, +\infty[$ (or $[-5, +\infty)$, read as “the half-open interval from $-5$ inclusive to positive infinity”).
> - For $x < 3$: $S = ]-\infty, 3[$ (or $(-\infty, 3)$, read as “from negative infinity to 3 exclusive”).
> The symbol $\infty$ (“infinity”) **always** receives an open bracket, because infinity is a boundless direction, not a reachable number that can be closed in.

---

### 5. Systems of Two Linear Equations in Two Variables

Let us revisit the second riddle from Venice:
*A merchant sells a lot of 100 amphorae of oil. There are small amphorae holding 3 liters and large amphorae holding 5 liters. The total volume of oil is 380 liters. How many amphorae of each kind are there?*

Here, there are **two unknown quantities**:
- Let $x$ be the number of small amphorae (3 L).
- Let $y$ be the number of large amphorae (5 L).

Each sentence in the problem provides an equation:
1. *“100 amphorae in total”* $\implies x + y = 100$.
2. *“380 liters in total”* $\implies 3x + 5y = 380$.

These two equations constitute a **system of two linear equations in two variables**. We bind them together with a curly brace:
$$\begin{cases} x + y = 100 & (L_1) \\ 3x + 5y = 380 & (L_2) \end{cases}$$

Solving this system means determining the unique pair $(x, y)$ that makes both equations simultaneously true. Two universal methods accomplish this.

---

#### 5.1 Method 1: The Substitution Method (The Infiltrated Agent)

The principle is straightforward: use one equation to isolate one variable in terms of the other, then “inject” that expression into the second equation.

1. **Isolate an easy variable:**
   From the first equation $x + y = 100$, isolate $x$:
   $$x = 100 - y.$$
2. **Substitute into the other equation:**
   In the second equation $3x + 5y = 380$, replace the symbol $x$ with $(100 - y)$:
   $$3(100 - y) + 5y = 380.$$
   Magic: the variable $x$ has vanished! We now have a standard equation in the single variable $y$!
3. **Solve for $y$:**
   $$300 - 3y + 5y = 380$$
   $$300 + 2y = 380$$
   $$2y = 380 - 300 = 80$$
   $$y = \frac{80}{2} = 40.$$
4. **Compute the first unknown $x$:**
   Since $x = 100 - y$:
   $$x = 100 - 40 = 60.$$
5. **Conclusion and Verification:**
   The merchant sold $60$ small amphorae and $40$ large amphorae.
   Verification:
   - Total amphorae: $60 + 40 = 100$ (exact).
   - Total liters: $60 \times 3 + 40 \times 5 = 180 + 200 = 380$ liters (exact!).
   The solution pair is written: $(x, y) = (60, 40)$.

*When to use substitution?* Whenever one of the variables has a coefficient of $1$ or $-1$ (such as $x$ or $y$ in $x + y = 100$), because it can be isolated instantly without introducing messy fractions.

---

#### 5.2 Method 2: The Linear Combination / Elimination Method (The Elimination Duel)

What should we do when every variable is saddled with an awkward coefficient, such as:
$$\begin{cases} 2x + 3y = 19 & (L_1) \\ 5x - 2y = 19 & (L_2) \end{cases}$$
Isolating $x$ in the first equation would produce $x = \frac{19 - 3y}{2}$, cluttering the calculation with cumbersome fractions.

The **elimination method** (also known as addition or Gaussian elimination) multiplies the equations by strategically chosen numbers so that the coefficients of one variable become **exact opposites** (for instance, $+6y$ and $-6y$). By adding the two equations side by side, that variable is liquidated instantly!

Let us solve this system step by step:

1. **Choose the variable to eliminate:** Let us eliminate $y$.
   The coefficient of $y$ is $+3$ in $(L_1)$ and $-2$ in $(L_2)$.
   The least common multiple of 3 and 2 is 6.
2. **Multiply the equations:**
   - Multiply the entire equation $(L_1)$ by $2$:
     $$2 \times (2x + 3y) = 2 \times 19 \implies 4x + 6y = 38.$$
   - Multiply the entire equation $(L_2)$ by $3$:
     $$3 \times (5x - 2y) = 3 \times 19 \implies 15x - 6y = 57.$$
3. **Add the two equations vertically:**
   ```
        4x  +  6y  =  38
   +   15x  -  6y  =  57
   ─────────────────────
       19x  +   0  =  95
   ```
   The $y$ terms have cancelled out entirely!
4. **Solve for $x$:**
   $$19x = 95 \implies x = \frac{95}{19} = 5.$$
5. **Solve for $y$:**
   Substitute $x = 5$ into either original equation, for instance $(L_1)$:
   $$2(5) + 3y = 19 \implies 10 + 3y = 19 \implies 3y = 9 \implies y = 3.$$
6. **Conclusion:**
   The unique solution to the system is the pair $(x, y) = (5, 3)$.

---

### 6. The Geometric Interpretation: Two Intersecting Lines

Every first-degree equation in two variables, such as $2x + 3y = 19$, corresponds graphically to a **straight line** in the Cartesian plane (Chapter 20).
Every point $(x, y)$ lying on the line represents a valid solution to that equation.

Solving the system means finding a point $(x, y)$ that lies **simultaneously on line $(d_1)$ and on line $(d_2)$**.

```
          y ▲                     (d1)
            │                    /
            │                   /     (d2)
            │                  /     /
          3 ┼─────────────────*─────/──
            │                /│    /
            │               / │   /
            │              /  │  /
          ──┼─────────────┼───┼─┼────────> x
            0             2   5
                         Intersection Point: (5, 3)
```

Three geometric configurations can occur:

1. **The lines intersect (cross at a single unique point):**
   This is the standard case. The system has **one unique solution** $(x_0, y_0)$.
2. **The lines are strictly parallel (they never meet):**
   The system has **no solution** ($S = \emptyset$).
   *Example:* $\begin{cases} x + y = 4 \\ x + y = 10 \end{cases}$ (the sum of two numbers cannot equal 4 and 10 at the same time!).
3. **The lines are coincident (they lie right on top of each other):**
   Both equations are merely different algebraic representations of the exact same line (e.g., $x + y = 2$ and $2x + 2y = 4$).
   The system possesses **infinitely many solutions**.

---

### 7. True History: The Secret Counting Rods of the Nine Chapters

Two centuries before our era, during the Han Dynasty in China, imperial mathematicians were already solving systems of linear equations to manage grain harvests, labor levies, and imperial taxes.

In the crowning jewel of Chinese mathematics, *The Nine Chapters on the Mathematical Art* (*Jiuzhang Suanshu*), Chapter 8 is entitled *Fangcheng* (“Rectangular Arrays”).

Chinese scholars arranged red bamboo rods (for positive numbers) and black rods (for negative numbers) on a felt counting board. Each column represented an equation and each row represented a different grade of grain (top-grade millet, medium-grade millet, low-grade millet):

```
   [ 3 bundles top millet ] + [ 2 bundles medium millet ] + [ 1 bundle low millet ] = 39 measures
   [ 2 bundles top millet ] + [ 3 bundles medium millet ] + [ 1 bundle low millet ] = 34 measures
   [ 1 bundle top millet ] + [ 2 bundles medium millet ] + [ 3 bundles low millet ] = 26 measures
```

By sliding rods across columns, multiplying a column and subtracting it from another, they systematically cleared entries to produce zeroes. This 2,200-year-old Chinese algorithm is identical to **Gaussian elimination**, taught today in universities worldwide and programmed into modern supercomputing linear algebra libraries!

---

### 8. Step-by-Step Worked Examples

#### Example 1: Solving an inequality with parentheses and basic terms
Solve the following inequality over the real numbers and sketch the solution set:
$$4(2x - 3) - 5x \ge 7x - 24.$$

**Detailed Solution:**
1. Expand the left-hand side:
   $$8x - 12 - 5x \ge 7x - 24 \implies 3x - 12 \ge 7x - 24.$$
2. Group the $x$ terms on the left by subtracting $7x$:
   $$3x - 7x - 12 \ge -24 \implies -4x - 12 \ge -24.$$
3. Add $12$ to both sides:
   $$-4x \ge -24 + 12 \implies -4x \ge -12.$$
4. Divide by the coefficient of $x$, which is **$-4$ (negative)**.
   **Reverse the inequality symbol ($\ge$ becomes $\le$):**
   $$x \le \frac{-12}{-4} \implies x \le 3.$$
5. Graphical representation:
   The solutions are all real numbers less than or equal to 3.
   The bracket is closed at 3 and oriented leftward toward the shaded region:
   ```
   <████████████████████████████]──────────┼───────>
                                3          0
   ```
   Solution set: $S = ]-\infty, 3]$ (or $(-\infty, 3]$).

---

#### Example 2: Inequality with a denominator and strict sign control
Solve the inequality:
$$\frac{2 - 5x}{3} > 4.$$

**Detailed Solution:**
1. Multiply both sides by $3$. Since $3 > 0$, the inequality direction is preserved:
   $$2 - 5x > 4 \times 3 \implies 2 - 5x > 12.$$
2. Subtract 2:
   $$-5x > 12 - 2 \implies -5x > 10.$$
3. Divide by **$-5$ (negative)**, which flips the inequality symbol ($>$ becomes $<$):
   $$x < \frac{10}{-5} \implies x < -2.$$
Conclusion: $S = ]-\infty, -2[$ (or $(-\infty, -2)$). The bracket at $-2$ turns its back on the solutions since $-2$ is excluded.

---

#### Example 3: System solved by substitution
Solve the system:
$$\begin{cases} 3x - y = 7 & (L_1) \\ 2x + 4y = 42 & (L_2) \end{cases}$$

**Detailed Solution:**
1. In $(L_1)$, the variable $y$ has a coefficient of $-1$, allowing quick isolation:
   $$-y = 7 - 3x \implies y = 3x - 7.$$
2. Substitute $y$ by $(3x - 7)$ in equation $(L_2)$:
   $$2x + 4(3x - 7) = 42$$
   $$2x + 12x - 28 = 42$$
   $$14x - 28 = 42$$
   $$14x = 42 + 28 = 70 \implies x = \frac{70}{14} = 5.$$
3. Compute $y$ using the formula from step 1:
   $$y = 3(5) - 7 = 15 - 7 = 8.$$
4. Check in both original equations:
   - $(L_1)$: $3(5) - 8 = 15 - 8 = 7$ (true).
   - $(L_2)$: $2(5) + 4(8) = 10 + 32 = 42$ (true).
Conclusion: The unique solution pair is $(x, y) = (5, 8)$.

---

#### Example 4: System solved by linear combination (elimination)
Solve the system:
$$\begin{cases} 4x + 3y = 1 & (L_1) \\ 6x - 5y = 20 & (L_2) \end{cases}$$

**Detailed Solution:**
Let us eliminate $y$. The coefficients of $y$ are $+3$ and $-5$.
Their least common multiple is 15.
1. Multiply $(L_1)$ by $5$:
   $$5 \times (4x + 3y) = 5 \times 1 \implies 20x + 15y = 5.$$
2. Multiply $(L_2)$ by $3$:
   $$3 \times (6x - 5y) = 3 \times 20 \implies 18x - 15y = 60.$$
3. Add the two new equations term by term:
   $$(20x + 18x) + (15y - 15y) = 5 + 60$$
   $$38x = 65 \implies x = \frac{65}{38}.$$
   *Alternatively:* Eliminate $x$ by multiplying $(L_1)$ by $3$ and $(L_2)$ by $-2$:
   - $3 \times (L_1) \implies 12x + 9y = 3$
   - $-2 \times (L_2) \implies -12x + 10y = -40$
   Adding gives: $19y = -37 \implies y = -\frac{37}{19} = -\frac{74}{38}$.
Conclusion: The solution pair is $\left( \frac{65}{38}, -\frac{37}{19} \right)$.

---

#### Example 5: Real-world ticketing problem (Setting up a linear system)
To finance their end-of-year class trip, 9th-grade students organize a theater evening.
- Adult tickets cost €8.
- Child tickets cost €4.50.
At the end of the evening, the ticket booth reports 240 attendees and total receipts of €1,570.
How many adults and how many children attended the play?

**Detailed Solution:**
1. **Choose variables:**
   - Let $a$ be the number of adults.
   - Let $c$ be the number of children.
2. **Set up equations:**
   - Total attendees: $a + c = 240$.
   - Total receipts in euros: $8a + 4.5c = 1570$.
3. **Solve by substitution:**
   From the first equation, $c = 240 - a$.
   Substitute into the second:
   $$8a + 4.5(240 - a) = 1570$$
   $$8a + 1080 - 4.5a = 1570$$
   $$3.5a + 1080 = 1570$$
   $$3.5a = 1570 - 1080 = 490$$
   $$a = \frac{490}{3.5} = \frac{4900}{35} = 140.$$
4. **Compute the second variable:**
   $$c = 240 - 140 = 100.$$
5. **Conclusion:**
   There were 140 adults and 100 children in the audience.
   Verification: $140 \times 8 + 100 \times 4.5 = 1120 + 450 = 1570$ €. Everything matches!

---

### Key Takeaways

1. **Golden Rules of Inequalities:**
   - Adding or subtracting the same number **never** alters the inequality direction.
   - Multiplying or dividing by a **positive** number **preserves** the direction.
   - Multiplying or dividing by a **negative** number **MUST REVERSE THE DIRECTION** ($<$ becomes $>$, $\le$ becomes $\ge$).
2. **Number Line Representation:**
   - Closed bracket $[\text{ or }]$ toward solutions if the value is **included** ($\le, \ge$).
   - Open bracket $]\text{ or }[$ turning away from solutions if the value is **excluded** ($<, >$).
3. **System of Two Linear Equations in Two Variables:**
   $$\begin{cases} ax + by = c \\ a'x + b'y = c' \end{cases}$$
   - **Substitution Method:** isolate one variable in one equation and substitute it into the other (best when a coefficient is 1 or $-1$).
   - **Elimination Method:** multiply equations to create opposite coefficients for one variable, then add equations vertically (universal).
4. **Geometric Vision:** The solution to a system represents the $(x, y)$ coordinates of the point of intersection of the two associated lines.

---

### Exercises

#### Level ★: Direct Application

**Exercise 24.1** Fill in the appropriate inequality symbol ($<$ or $>$):
1. Given $x < 5$, compare $x + 4$ and $9$.
2. Given $y \ge -2$, compare $y - 3$ and $-5$.
3. Given $a < b$, compare $3a$ and $3b$.
4. Given $u < v$, compare $-4u$ and $-4v$.

**Exercise 24.2** Solve the basic first-degree inequalities:
1. $x + 7 < 15$
2. $x - 9 \ge 3$
3. $4x \le 28$
4. $-5x < 35$
5. $-2x \ge -18$
6. $\frac{x}{3} > -4$

**Exercise 24.3** Plot the following solution sets on a number line:
1. $x > 4$
2. $x \le -1$
3. $x \ge 2.5$
4. $x < 0$

**Exercise 24.4** Test whether the pair $(x = 3, y = 2)$ is a solution to the following systems:
1. $\begin{cases} 2x + y = 8 \\ x - y = 1 \end{cases}$
2. $\begin{cases} 3x - 4y = 1 \\ 5x + 2y = 20 \end{cases}$

**Exercise 24.5** Solve using the substitution method:
1. $\begin{cases} y = 2x - 1 \\ 3x + y = 14 \end{cases}$
2. $\begin{cases} x + 2y = 8 \\ 3x - 4y = 4 \end{cases}$

**Exercise 24.6** Solve using the elimination method:
1. $\begin{cases} 2x + y = 11 \\ 3x - y = 9 \end{cases}$
2. $\begin{cases} 3x + 2y = 12 \\ 5x - 2y = 20 \end{cases}$

---

#### Level ★★: Deeper Reflection and Multi-Step Problems

**Exercise 24.7** Solve and state the solution set in interval notation:
1. $5x - 8 < 2x + 7$
2. $3(x - 2) - 4(2x + 1) \ge 5$
3. $\frac{3x - 1}{4} \le \frac{x + 2}{2}$

**Exercise 24.8** Compound Inequalities (Double Bounds):
Find all real numbers $x$ satisfying simultaneously:
$$-3 \le 2x + 1 < 9.$$
*(Hint: subtract 1 from all three parts, then divide by 2).*

**Exercise 24.9** Solve the linear systems:
1. $\begin{cases} 4x + 3y = 25 \\ 2x - 5y = -7 \end{cases}$
2. $\begin{cases} 5x + 2y = 1 \\ 3x - 4y = 11 \end{cases}$
3. $\begin{cases} 2x - 3y = 7 \\ 4x - 6y = 10 \end{cases}$ (What is happening geometrically?)

**Exercise 24.10** The Amusement Park Problem:
An amusement park offers two pricing plans:
- **Plan A:** €25 general admission providing unlimited access to all rides.
- **Plan B:** €9 basic admission, plus €2 per individual ride.
1. Write down the cost of each plan for taking $x$ rides.
2. Set up and solve an inequality to determine at how many rides Plan A becomes more economical than Plan B.

**Exercise 24.11** The Silver Alloy Problem:
A jeweler has two silver ingots:
- The first ingot contains $80\%$ pure silver.
- The second ingot contains $60\%$ pure silver.
He wishes to melt these two ingots together to obtain exactly 500 grams of a new alloy containing $75\%$ pure silver.
What mass of each ingot must he melt?

**Exercise 24.12** Geometry and Perimeter:
A rectangle has a length that exceeds its width by 4 cm. Its perimeter is strictly less than 36 cm.
What values can the width of this rectangle take?

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 24.13** Graphical Intersection of Two Rate Lines:
In a Cartesian coordinate system, consider the two lines:
$(d_1) : y = 2x + 1 \quad \text{and} \quad (d_2) : y = -x + 7.$
1. Find algebraically the coordinates of their intersection point $K$.
2. Solve graphically and algebraically the inequality $2x + 1 \le -x + 7$.
3. Interpret the result: which line lies below the other?

**Exercise 24.14** The Chinese Age Puzzle:
A father says to his son:
*“Today, I am four times as old as you. But in 20 years, I will be only twice as old as you.”*
What are the current ages of the father and the son?

**Exercise 24.15** Parametric System (For Future Scientists):
Consider the system:
$$\begin{cases} ax + 2y = 4 \\ 3x + y = 2 \end{cases}$$
For what value of parameter $a$ does this system fail to have a unique solution pair?
What can be said about the two associated lines for this value of $a$?

---

### Solutions

#### Level ★

**Solution 24.1**
1. $x + 4 < 9$ (added 4 to both sides).
2. $y - 3 \ge -5$ (subtracted 3 from both sides).
3. $3a < 3b$ (multiplied by $3 > 0$).
4. $-4u > -4v$ (multiplied by $-4 < 0$, the inequality sign flips!).

**Solution 24.2**
1. $x < 15 - 7 \implies x < 8$.
2. $x \ge 3 + 9 \implies x \ge 12$.
3. $x \le \frac{28}{4} \implies x \le 7$.
4. Division by $-5 < 0$: $x > \frac{35}{-5} \implies x > -7$.
5. Division by $-2 < 0$: $x \le \frac{-18}{-2} \implies x \le 9$.
6. Multiplication by $3 > 0$: $x > -12$.

**Solution 24.3**
1. Shaded region to the right of 4, open bracket facing left: $]4, +\infty[$ (or $(4, +\infty)$).
2. Shaded region to the left of $-1$, closed bracket facing left: $]-\infty, -1]$ (or $(-\infty, -1]$).
3. Shaded region to the right of $2.5$, closed bracket facing right: $[2.5, +\infty[$ (or $[2.5, +\infty)$).
4. Shaded region to the left of 0, open bracket facing right: $]-\infty, 0[$ (or $(-\infty, 0)$).

**Solution 24.4**
1. $2(3) + 2 = 6 + 2 = 8$ (true) and $3 - 2 = 1$ (true). The pair $(3, 2)$ is indeed a solution to the first system.
2. $3(3) - 4(2) = 9 - 8 = 1$ (true). But $5(3) + 2(2) = 15 + 4 = 19 \neq 20$ (false!). The pair is not a solution to the second system.

**Solution 24.5**
1. Substitute $y = 2x - 1$ into the second equation:
   $3x + (2x - 1) = 14 \implies 5x - 1 = 14 \implies 5x = 15 \implies x = 3$.
   Then $y = 2(3) - 1 = 5$. Solution: $(3, 5)$.
2. From the first equation: $x = 8 - 2y$.
   Second equation: $3(8 - 2y) - 4y = 4 \implies 24 - 6y - 4y = 4 \implies -10y = -20 \implies y = 2$.
   Then $x = 8 - 2(2) = 4$. Solution: $(4, 2)$.

**Solution 24.6**
1. Add both equations directly ($+y$ and $-y$ cancel):
   $(2x + 3x) + (y - y) = 11 + 9 \implies 5x = 20 \implies x = 4$.
   Then $2(4) + y = 11 \implies 8 + y = 11 \implies y = 3$. Solution: $(4, 3)$.
2. Add both equations directly ($+2y$ and $-2y$ cancel):
   $8x = 32 \implies x = 4$.
   Then $3(4) + 2y = 12 \implies 12 + 2y = 12 \implies 2y = 0 \implies y = 0$. Solution: $(4, 0)$.

---

#### Level ★★

**Solution 24.7**
1. $5x - 2x < 7 + 8 \implies 3x < 15 \implies x < 5$. Solution: $S = ]-\infty, 5[$.
2. $3x - 6 - 8x - 4 \ge 5 \implies -5x - 10 \ge 5 \implies -5x \ge 15 \implies x \le -3$ (reversal). Solution: $S = ]-\infty, -3]$.
3. Multiply by 4 (positive): $3x - 1 \le 2(x + 2) \implies 3x - 1 \le 2x + 4 \implies x \le 5$. Solution: $S = ]-\infty, 5]$.

**Solution 24.8**
Subtract 1 from all three parts:
$$-3 - 1 \le 2x < 9 - 1 \implies -4 \le 2x < 8.$$
Divide all parts by $2 > 0$:
$$-2 \le x < 4.$$
The solutions are all real numbers between $-2$ (included) and $4$ (excluded). $S = [-2, 4[$.

**Solution 24.9**
1. Multiply the 2nd equation by $-2$: $-4x + 10y = 14$.
   Add to the 1st ($4x + 3y = 25$): $13y = 39 \implies y = 3$.
   Then $2x - 5(3) = -7 \implies 2x - 15 = -7 \implies 2x = 8 \implies x = 4$. Solution: $(4, 3)$.
2. Multiply the 1st equation by 2: $10x + 4y = 2$.
   Add to the 2nd ($3x - 4y = 11$): $13x = 13 \implies x = 1$.
   Then $5(1) + 2y = 1 \implies 2y = -4 \implies y = -2$. Solution: $(1, -2)$.
3. Multiply the 1st equation by 2: $4x - 6y = 14$.
   The 2nd equation is $4x - 6y = 10$.
   Subtracting the two equations gives: $(4x - 4x) - (6y - 6y) = 14 - 10 \implies 0 = 4$, which is **impossible**!
   Geometrically, both lines share the same slope: they are **strictly parallel**. There is no intersection point, hence no solution ($S = \emptyset$).

**Solution 24.10**
1. For $x$ rides: Cost of Plan A $= 25$ €; Cost of Plan B $= 9 + 2x$ €.
2. Plan A is more economical if:
   $$25 < 9 + 2x \iff 25 - 9 < 2x \iff 16 < 2x \iff 8 < x \iff x > 8.$$
   Since the number of rides is an integer, Plan A becomes more advantageous starting from **9 rides**.

**Solution 24.11**
Let $x$ be the mass (in grams) of the first ingot (80%) and $y$ the mass of the second (60%).
1. Total mass: $x + y = 500$.
2. Pure silver mass: $0.80x + 0.60y = 0.75 \times 500 = 375$.
From the 1st equation: $y = 500 - x$.
Substitute into the 2nd:
$0.8x + 0.6(500 - x) = 375 \implies 0.8x + 300 - 0.6x = 375 \implies 0.2x = 75 \implies x = \frac{75}{0.2} = 375\text{ g}$.
Then $y = 500 - 375 = 125\text{ g}$.
The jeweler must melt 375 g of the first ingot and 125 g of the second.

**Solution 24.12**
Let $w$ be the width in cm. The length is $L = w + 4$.
The perimeter is $P = 2(w + L) = 2(w + w + 4) = 2(2w + 4) = 4w + 8$.
The problem states that $P < 36$, so:
$$4w + 8 < 36 \implies 4w < 28 \implies w < 7.$$
Furthermore, a geometric width must be strictly positive ($w > 0$).
Thus, the width $w$ can take any value strictly between 0 and 7 cm: $w \in ]0, 7[$ (or $(0, 7)$).

---

#### Level ★★★

**Solution 24.13**
1. At the intersection point, the $y$-values are equal:
   $$2x + 1 = -x + 7 \implies 3x = 6 \implies x = 2.$$
   Then $y = 2(2) + 1 = 5$. The intersection point is $K(2, 5)$.
2. Solve $2x + 1 \le -x + 7$:
   $$3x \le 6 \implies x \le 2.$$
   The solution set is $S = ]-\infty, 2]$ (or $(-\infty, 2]$).
3. Interpretation: for all $x \le 2$, line $(d_1)$ lies **below** (or intersects) line $(d_2)$. Beyond $x = 2$, line $(d_1)$ rises above line $(d_2)$.

**Solution 24.14**
Let $f$ be the father's current age and $s$ the son's current age.
1. “Today, I am 4 times your age”: $f = 4s$.
2. “In 20 years, father will be $f + 20$ and son will be $s + 20$”:
   $$f + 20 = 2(s + 20).$$
Substitute $f = 4s$ into the second equation:
$$4s + 20 = 2s + 40 \implies 2s = 20 \implies s = 10.$$
Then $f = 4 \times 10 = 40$.
The father is currently 40 years old and the son is 10 years old.
Check in 20 years: father will be 60, son will be 30, and 60 is indeed twice 30!

**Solution 24.15**
Isolate $y$ in the second equation: $y = 2 - 3x$.
Substitute into the first equation:
$$ax + 2(2 - 3x) = 4 \implies ax + 4 - 6x = 4 \implies (a - 6)x = 0.$$
- If $a \neq 6$, then $a - 6 \neq 0$, yielding a unique solution $x = 0$ (and $y = 2$).
- If $a = 6$, the equation becomes $0 \times x = 0$, which holds true for **all real numbers $x$**! In this case, both equations are equivalent ($6x + 2y = 4 \iff 3x + y = 2$). The two lines are **coincident**, yielding infinitely many solutions.
To get strictly parallel lines (no solution), the constant term would have had to differ (e.g. $6x + 2y = 5$).
Conclusion: the critical value is **$a = 6$**. For this value, the determinant vanishes ($a \times 1 - 2 \times 3 = a - 6 = 0$), and the system loses its unique solution.

---

### The Question Opening the Next Chapter

Look at what we have just accomplished: to every number of liters of oil $x$, we assigned a total cost $P(x) = 6x$ or $P(x) = 30 + 4x$. To every number of amusement park rides, we mapped a total expenditure.

This powerful mathematical mechanism, where an input number generates a unique output number, is called a **function**. Why not look this machine directly in the face? What geometric trajectory is traced by a proportional relationship or by a fixed subscription tariff? That is the grand journey awaiting us in Chapter 25: **The Doubling Machine and the Tariff Line**.
