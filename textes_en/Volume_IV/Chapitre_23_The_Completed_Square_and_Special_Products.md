# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 23: The Completed Square and Special Products

> *“Do not recite an algebraic formula like a magical incantation. Close your eyes and look at the tiled floor: cut a rectangle, shift a corner, complete the missing square. Letters are nothing other than the sides of geometric shapes fitting together under your fingers.”*

---

### What You Are About to Discover

- How the **double distributive property** is explained by slicing a rectangle into four plots of land: $(a+b)(c+d) = ac + ad + bc + bd$.
- The **three special products (algebraic identities)**, demonstrated before your eyes through pure geometric dissections of squares and rectangles.
- The art of **lightning-fast mental math**: calculating $101^2$, $99^2$, or $48 \times 52$ in two seconds without a calculator.
- **Factoring**: the reverse journey, transforming a sum into a product by unearthing the hidden common factor or the footprint of a special product.
- The **zero-product equation**: the master key to solving quadratic equations without panic.
- The complete resolution of the equation $x^2 = a$ depending on the sign of $a$, and why a real square can never equal a negative number.
- The grand historical stroke of genius by **Al-Khwarizmi**: “completing the square,” which laid the foundations of global algebra twelve centuries ago.

---

### 1. The Problem: The Caliph's Garden and the Missing Corner

In the spring of the year 825, in the hanging gardens of the caliphal palace in Baghdad, the head gardener faced an infuriating dilemma. The Caliph desired to enlarge his square orchard.

The current orchard was a square of unknown side length $x$ meters. The Caliph decreed:
*“Extend two opposite sides by 5 meters to the north, and extend the other two sides by 5 meters to the east!”*

The gardener drafted the plan. The new garden had side length $(x + 5)$ meters. But the Grand Steward of the Treasury demanded the exact formula for the total area to order the bags of grass seed:
*“If the initial side length was $x$, the new area is obviously $x^2 + 5^2 = x^2 + 25$!”* proclaimed the vizier without a second thought.

Al-Khwarizmi, present during the audience, smiled quietly and sketched a figure in the fine sand with the tip of his reed cane:

```
             x             5
      ┌──────────────┬───────────┐
      │              │           │
    x │   x × x      │   5 × x   │
      │   = x²       │   = 5x    │
      │              │           │
      ├──────────────┼───────────┤
    5 │   x × 5      │   5 × 5   │
      │   = 5x       │   = 25    │
      └──────────────┴───────────┘
```

*“Look closely, noble vizier,”* said Al-Khwarizmi. *“Your calculation forgets two immense strips of land! You indeed have the old square of $x^2$, and you indeed have the small corner square of $25 \text{ m}^2$. But where have you accounted for the plot of $5x$ in the upper right, and the other plot of $5x$ in the lower left?”*

The true area of the expanded garden is not $x^2 + 25$, but:
$$(x + 5)^2 = x^2 + 5x + 5x + 25 = x^2 + 10x + 25.$$

The vizier had “forgotten” $10x$ square meters of lawn—enough to leave half the garden completely bare!

This blunder is the most notorious mistake in the entire history of school mathematics. Millions of students commit it every year by inadvertently writing $(a+b)^2 = a^2 + b^2$.

In this chapter, we will etch into your mind, through geometry and pure reasoning, why those two middle pieces always emerge, how to navigate effortlessly between expanding and factoring, and how this geometry unlocks second-degree equations.

---

### 2. Double Distributivity: Four Plots in a Rectangle

In Chapter 22, you encountered **single distributivity**: multiplying a number by a sum inside parentheses distributes the factor to each term:
$$k(a + b) = ka + kb.$$
This represented the area of a rectangle partitioned into two vertical strips.

What happens if both sides of the rectangle are themselves split into two segments?

#### 2.1 Proof by the Area of a Rectangle

Let us draw a rectangle whose total length is $(a + b)$ and whose total width is $(c + d)$.

```
               a                 b
        ┌───────────────┬────────────────┐
        │               │                │
      c │    a × c      │     b × c      │
        │    = ac       │     = bc       │
        │               │                │
        ├───────────────┼────────────────┤
      d │    a × d      │     b × d      │
        │    = ad       │     = bd       │
        └───────────────┴────────────────┘
```

The total area of the large rectangle can be evaluated in two equivalent ways:
1. **All at once:** Length $\times$ Width, which is $(a + b)(c + d)$.
2. **Piece by piece:** The sum of the areas of the 4 interior plots:
   $$ac + ad + bc + bd.$$

Since both calculations measure the exact same surface, they are strictly equal.

> **📐 Fundamental Property — The Double Distributive Property.** For any real numbers $a, b, c, d$:
> $$(a + b)(c + d) = ac + ad + bc + bd.$$
> Every term in the first pair of parentheses is multiplied by every term in the second pair of parentheses. This produces 4 pairwise multiplications.

#### 2.2 The Arrow Rule and Managing Signs

To ensure nothing is forgotten in a written calculation, one can mentally trace four arrows (often known in English as the **FOIL method**: First, Outer, Inner, Last):

```
         ┌───── 1 ─────┐
         │   ┌── 2 ────┼───┐
         ▼   ▼         ▼   ▼
       ( a + b )  ×  ( c + d )
             ▲   ▲
             │   └─── 4 ───┘
             └─────── 3 ───┘
```

1. **First:** $a \times c = ac$
2. **Outer:** $a \times d = ad$
3. **Inner:** $b \times c = bc$
4. **Last:** $b \times d = bd$

> **⚠️ Watch Out! Pitfall — The Sign Belongs to the Term Following It!**
> When a factor contains a subtraction, such as $(2x - 3)(x + 4)$, view the first factor as consisting of the terms $(+2x)$ and $(-3)$.
> Then apply the sign rules rigorously (Chapter 20):
> * $(+2x) \times (+x) = +2x^2$
> * $(+2x) \times (+4) = +8x$
> * $(-3) \times (+x) = -3x$
> * $(-3) \times (+4) = -12$
> Then **simplify** by combining like terms:
> $$(2x - 3)(x + 4) = 2x^2 + 8x - 3x - 12 = 2x^2 + 5x - 12.$$

---

### 3. The Three Special Products (Algebraic Identities)

Certain algebraic products occur so frequently across science and mathematics that they are termed **remarkable** or **special products**. They deserve to be mastered as instantaneous reflexes. But before memorizing them by heart, let us observe them living before our eyes.

#### 3.1 First Identity: The Square of a Sum $(a+b)^2$

Consider a square of side length $(a + b)$.

<div align="center">
<svg width="340" height="340" viewBox="0 0 340 340" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="340" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="10"/>
  
  <g transform="translate(45, 45)">
    <!-- Square a^2 (Byrne Blue) -->
    <rect x="0" y="0" width="160" height="160" fill="#1d4ed8" fill-opacity="0.85" stroke="#1e3a8a" stroke-width="2"/>
    <text x="80" y="88" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="bold" text-anchor="middle">a²</text>
    
    <!-- Rectangle a x b upper-right (Byrne Amber/Yellow) -->
    <rect x="160" y="0" width="80" height="160" fill="#d97706" fill-opacity="0.85" stroke="#b45309" stroke-width="2"/>
    <text x="200" y="88" fill="#ffffff" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">ab</text>
    
    <!-- Rectangle a x b lower-left (Byrne Amber/Yellow) -->
    <rect x="0" y="160" width="160" height="80" fill="#d97706" fill-opacity="0.85" stroke="#b45309" stroke-width="2"/>
    <text x="80" y="208" fill="#ffffff" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">ab</text>
    
    <!-- Small square b^2 (Byrne Red) -->
    <rect x="160" y="160" width="80" height="80" fill="#b91c1c" fill-opacity="0.85" stroke="#7f1d1d" stroke-width="2"/>
    <text x="200" y="208" fill="#ffffff" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">b²</text>
    
    <!-- Top labels -->
    <text x="80" y="-12" fill="#1d4ed8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">a</text>
    <text x="200" y="-12" fill="#b91c1c" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">b</text>
    
    <!-- Left labels -->
    <text x="-15" y="88" fill="#1d4ed8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">a</text>
    <text x="-15" y="208" fill="#b91c1c" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">b</text>
  </g>
  <text x="170" y="320" fill="#0f172a" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">(a + b)² = a² (blue) + 2ab (yellow) + b² (red)</text>
</svg>
</div>

```
             a             b
      ┌──────────────┬───────────┐
      │              │           │
    a │      a²      │    ab     │
      │              │           │
      ├──────────────┼───────────┤
    b │      ab      │    b²     │
      └──────────────┴───────────┘
```

The total area is the square of its side length: $(a + b)^2$.
This area naturally divides into four components:
- a large square of area $a^2$;
- a small square of area $b^2$;
- two identical rectangles of area $a \times b = ab$.

Adding these components together gives:
$$(a + b)^2 = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2.$$

The middle term $2ab$ is known as the **cross product** or **double product**.

> **📐 First Special Product — Square of a Sum.** For any real numbers $a$ and $b$:
> $$(a + b)^2 = a^2 + 2ab + b^2.$$
> *In plain words:* “The square of a sum equals the square of the first term, plus twice the product of the terms, plus the square of the second term.”

#### 3.2 Second Identity: The Square of a Difference $(a-b)^2$

Now imagine a large square of side length $a$, with total area $a^2$. We want to determine the area of a smaller square nestled in the top-left corner, of side length $(a - b)$. Its area is $(a - b)^2$.

```
               a - b            b
        ┌──────────────────┬─────────┐
        │                  │/////////│
  a - b │    (a - b)²      │/////////│
        │     SOUGHT       │/////////│
        ├──────────────────┼─────────┤
      b │//////////////////│xxxxxxxxx│
        │//////////////////│xxxxxxxxx│
        └──────────────────┴─────────┘
```

How can we obtain the area of this white square $(a-b)^2$ from the large square $a^2$?
1. Remove the bottom horizontal strip, of length $a$ and width $b$: its area is $a \times b = ab$.
2. Remove the right vertical strip, of length $a$ and width $b$: its area is $a \times b = ab$.
3. **Caution!** The small bottom-right corner square (marked with `xxxx`), of side length $b$ and area $b^2$, belonged simultaneously to both the horizontal strip and the vertical strip! In subtracting both strips, we removed it **twice**.
4. To restore exact balance, we must **add back once** that small corner $b^2$.

The remaining area is therefore:
$$(a - b)^2 = a^2 - ab - ab + b^2 = a^2 - 2ab + b^2.$$

Algebraically, we find this exact result by applying double distributivity to $(a - b)(a - b)$:
$$(a - b)(a - b) = a \times a - a \times b - b \times a + (-b) \times (-b) = a^2 - 2ab + b^2.$$

> **📐 Second Special Product — Square of a Difference.** For any real numbers $a$ and $b$:
> $$(a - b)^2 = a^2 - 2ab + b^2.$$
> *In plain words:* “The square of a difference equals the square of the first term, minus twice the product of the terms, plus the square of the second term.”

> **⚠️ Watch Out! Pitfall.** In $(a - b)^2 = a^2 - 2ab + b^2$, the final term is **always preceded by a plus sign $+$**! Indeed, $(-b) \times (-b) = +b^2$. Only the double product carries the minus sign.

#### 3.3 Third Identity: The Product of a Sum and a Difference $(a+b)(a-b)$

Start with a square of side length $a$ (area $a^2$), from which we cut out a smaller square of side length $b$ situated at a corner (area $b^2$).
The remaining surface has area $a^2 - b^2$. It is an L-shaped region.

```
           a - b            b
      ┌──────────────┬───────────┐
      │              │           │
a - b │      I       │    II     │
      │              │           │
      ├──────────────┴───────────┤
    b │           III            │  (Cut out!)
      └──────────────────────────┘
```

Let us slice this L-shaped region and rearrange it into a single large rectangle of length $(a + b)$ and width $(a - b)$:

```
          ┌───────────────────────────┬─────────────┐
    a - b │             a             │      b      │
          └───────────────────────────┴─────────────┘
          <───────────────── a + b ─────────────────>
```

The area of this new rectangle is $\text{Length} \times \text{Width} = (a + b)(a - b)$.
Since this rectangle was formed by rearranging the large square $a^2$ stripped of the small square $b^2$, the two areas are strictly equal!

Algebraically, via double distributivity:
$$(a + b)(a - b) = a \times a - a \times b + b \times a - b \times b = a^2 - ab + ba - b^2.$$
The two middle terms cancel because $-ab + ba = 0$. What remains is:
$$(a + b)(a - b) = a^2 - b^2.$$

> **📐 Third Special Product — Difference of Two Squares.** For any real numbers $a$ and $b$:
> $$(a + b)(a - b) = a^2 - b^2.$$
> This identity is universally celebrated as the **difference of squares**.

#### 3.4 Summary Table of Special Products

| Factored Form (Product) | | Expanded Form (Sum) | Name |
|---|---|---|---|
| $(a + b)^2$ | $\Longleftrightarrow$ | $a^2 + 2ab + b^2$ | Square of a sum |
| $(a - b)^2$ | $\Longleftrightarrow$ | $a^2 - 2ab + b^2$ | Square of a difference |
| $(a + b)(a - b)$ | $\Longleftrightarrow$ | $a^2 - b^2$ | Difference of two squares |

- Moving from left to right ($\longrightarrow$): this is **expanding** (writing as a sum/difference of terms).
- Moving from right to left ($\longleftarrow$): this is **factoring** (writing as a product of factors).

#### 3.5 Lightning-Fast Mental Math Using Identities

Special products are not merely tools for manipulating abstract symbols; they enable staggering arithmetic calculations entirely in your head without scrap paper or calculators!

- **Calculating $101^2$:**
  $$101^2 = (100 + 1)^2 = 100^2 + 2 \times 100 \times 1 + 1^2 = 10\,000 + 200 + 1 = 10\,201.$$
- **Calculating $99^2$:**
  $$99^2 = (100 - 1)^2 = 100^2 - 2 \times 100 \times 1 + 1^2 = 10\,000 - 200 + 1 = 9\,801.$$
- **Calculating $52 \times 48$:**
  Notice that $52 = 50 + 2$ and $48 = 50 - 2$!
  $$52 \times 48 = (50 + 2)(50 - 2) = 50^2 - 2^2 = 2\,500 - 4 = 2\,496.$$
- **Calculating $105 \times 95$:**
  $$105 \times 95 = (100 + 5)(100 - 5) = 100^2 - 5^2 = 10\,000 - 25 = 9\,975.$$

> **💡 Did You Know?** In Antiquity, the Babylonians possessed no multiplication tables for all numbers. However, they possessed engraved clay tables of squares ($1^2, 2^2, 3^2, \dots$). To multiply any two arbitrary numbers $x$ and $y$, they utilized the formula:
> $$x \times y = \frac{(x + y)^2 - (x - y)^2}{4}.$$
> By calculating the sum, the difference, and looking up their squares in their tables, they found the product instantaneously!

---

### 4. Factoring: Recovering the Elementary Building Blocks

Expanding is mechanical: simply distribute arrows without losing track of signs. **Factoring** is the exact reverse: it is detective work. One is given an unraveled sum of scattered terms and must uncover how it was assembled from a pristine product.

Why go to such lengths to factor? Because a product is infinitely easier to examine and manage than a sum:
- A product allows us to simplify algebraic fractions.
- A product enables us to solve complex equations using the zero-product property.

In middle school algebra, there are two primary factoring techniques:

#### 4.1 First Technique: Factoring Out a Common Factor

Search for a number, a variable, or a bracketed expression that multiplies **every single term** in the sum.

**Case 1: An Obvious Common Factor (a number or a single variable)**
- In $6x + 15$: notice that $6 = 3 \times 2$ and $15 = 3 \times 5$. The common factor is $3$.
  $$6x + 15 = 3 \times 2x + 3 \times 5 = 3(2x + 5).$$
- In $x^2 - 7x$: notice that $x^2 = x \times x$ and $7x = 7 \times x$. The common factor is $x$.
  $$x^2 - 7x = x \times x - x \times 7 = x(x - 7).$$

**Case 2: An Entire Binomial as a Common Factor**
Consider the expression:
$$A = (3x + 2)(x - 5) + (3x + 2)(2x + 1).$$
The expression is a sum of two composite terms. The block $(3x + 2)$ is present in both terms: it is our **common factor**.

Underline it, factor it out in front, and open a set of brackets to collect everything that remains:
$$A = \underline{(3x + 2)}(x - 5) + \underline{(3x + 2)}(2x + 1)$$
$$A = \underline{(3x + 2)} \left[ (x - 5) + (2x + 1) \right]$$
$$A = (3x + 2) [ x - 5 + 2x + 1 ]$$
$$A = (3x + 2)(3x - 4).$$

> **⚠️ Watch Out! Pitfall — When the Common Factor Stands “All Alone”!**
> Consider the expression $B = (2x + 1)^2 - (2x + 1)$.
> Remember that $(2x + 1)^2 = (2x + 1)(2x + 1)$ and $(2x + 1) = (2x + 1) \times 1$.
> When factoring out $(2x + 1)$, the second term does not vanish into thin air; it leaves behind the number $1$:
> $$B = \underline{(2x + 1)}(2x + 1) - \underline{(2x + 1)} \times 1 = \underline{(2x + 1)} \left[ (2x + 1) - 1 \right] = (2x + 1)(2x) = 2x(2x + 1).$$
> Writing $B = (2x+1)(2x+1) = (2x+1)^2$ is a disastrous error!

#### 4.2 Second Technique: Recognizing a Special Product

When no common factor is shared across all terms, inspect the overall architecture of the expression:

1. **Three terms: two positive perfect squares with a plus sign in the middle:**
   $$x^2 + 6x + 9 = x^2 + 2 \times x \times 3 + 3^2 = (x + 3)^2.$$
2. **Three terms: two positive perfect squares with a minus sign in the middle:**
   $$4x^2 - 20x + 25 = (2x)^2 - 2 \times (2x) \times 5 + 5^2 = (2x - 5)^2.$$
3. **Two terms only, separated by a minus sign: it is the difference of two squares!**
   $$x^2 - 49 = x^2 - 7^2 = (x + 7)(x - 7).$$
   $$9x^2 - 16 = (3x)^2 - 4^2 = (3x + 4)(3x - 4).$$

---

### 5. The Zero-Product Equation: The Key to Higher Degrees

In Chapter 22, we learned how to solve first-degree (linear) equations, such as $3x + 5 = 14$.
But how can we solve an equation involving $x^2$, such as:
$$(2x - 6)(3x + 9) = 0 \quad \text{or} \quad x^2 - 25 = 0\text{ ?}$$

#### 5.1 The Fundamental Property of Zero

Ask yourself this question of childlike simplicity:
*If I multiply two secret numbers $A$ and $B$, and the result equals zero ($A \times B = 0$), what can you assert with absolute certainty?*

If you choose $A = 4$, for the product to be $0$, $B$ must **unconditionally** equal $0$.
If neither of the two numbers is zero (for instance $2 \times 3 = 6$ or $(-5) \times 0.1 = -0.5$), their product can **never** equal zero!

> **📐 Theorem — Zero-Product Property.**
> A product of factors equals zero **if and only if** at least one of its factors equals zero:
> $$A \times B = 0 \quad \Longleftrightarrow \quad A = 0 \quad \text{or} \quad B = 0.$$

This theorem is momentous: it shatters a difficult second-degree equation into **two straightforward first-degree equations**!

#### 5.2 Step-by-Step Method of Presentation

> **🧭 Method — Solving a Zero-Product Equation.**
> Let us solve the equation $(3x - 12)(2x + 8) = 0$.
> 
> 1. **Introductory statement:** “A product of factors is zero if and only if at least one of the factors is zero.”
> 2. **Split into two branches:**
>    $$3x - 12 = 0 \quad \text{or} \quad 2x + 8 = 0$$
> 3. **Solve each branch independently:**
>    - First branch: $3x = 12 \implies x = \frac{12}{3} = 4$.
>    - Second branch: $2x = -8 \implies x = \frac{-8}{2} = -4$.
> 4. **Conclusion:** The equation has two solutions: $-4$ and $4$. We denote the solution set by $S = \{-4, 4\}$.

> **⚠️ Watch Out! Pitfall — Never Divide by $x$!**
> Faced with an equation like $x^2 = 5x$, a tempting but disastrous mistake is to divide both sides by $x$ to conclude $x = 5$.
> In doing so, **you murder the solution $x = 0$**! (Because division by zero is strictly forbidden).
> **The correct method:** move everything to the left to produce a zero on the right, then factor:
> $$x^2 - 5x = 0 \iff x(x - 5) = 0 \iff x = 0 \quad \text{or} \quad x - 5 = 0 \iff x = 0 \quad \text{or} \quad x = 5.$$
> There are genuinely two solutions: $0$ and $5$.

---

### 6. Equations of the Form $x^2 = a$

The equation $x^2 = a$ is the purest of second-degree equations: what number, multiplied by itself, yields $a$?

The answer depends entirely on the **sign of $a$**.

#### 6.1 The Three Possible Cases

1. **If $a > 0$ ($a$ is strictly positive):**
   There exist **two opposite solutions**: $\sqrt{a}$ and $-\sqrt{a}$.
   *Rigorous proof by factoring:*
   $$x^2 = a \iff x^2 - a = 0.$$
   Since $a > 0$, we can express $a$ as $(\sqrt{a})^2$.
   The equation becomes:
   $$x^2 - (\sqrt{a})^2 = 0.$$
   This is the third special product $A^2 - B^2 = (A-B)(A+B)$!
   $$(x - \sqrt{a})(x + \sqrt{a}) = 0.$$
   By the zero-product property:
   $$x - \sqrt{a} = 0 \implies x = \sqrt{a} \quad \text{or} \quad x + \sqrt{a} = 0 \implies x = -\sqrt{a}.$$
   *Example:* The equation $x^2 = 9$ has solutions $\sqrt{9} = 3$ and $-\sqrt{9} = -3$.
   Indeed, $3 \times 3 = 9$ and $(-3) \times (-3) = 9$.

2. **If $a = 0$:**
   The equation $x^2 = 0$ has **a single unique solution**: $x = 0$.

3. **If $a < 0$ ($a$ is strictly negative):**
   The equation $x^2 = a$ has **no real solutions**.
   *Why?* The square of any real number is always non-negative:
   $(+5)^2 = +25$ and $(-5)^2 = +25$. It is physically and mathematically impossible for a real number squared to yield a negative value like $-16$.
   *Example:* $x^2 = -4$ has no real solution. We write $S = \emptyset$ (the empty set).

```
                            Equation: x² = a
                                    │
           ┌────────────────────────┼────────────────────────┐
           ▼                        ▼                        ▼
         a > 0                    a = 0                    a < 0
     Two solutions:          One solution:           No real solution:
    x = √a  or  x = -√a           x = 0                 Impossible!
```

---

### 7. True History: Al-Khwarizmi's Masterpiece and “Completing the Square”

How did Al-Khwarizmi solve an equation in 820 AD that entwined squares and linear terms, such as:
$$x^2 + 10x = 39\text{ ?}$$

In that era, algebraic formulas with $\Delta = b^2 - 4ac$ did not yet exist. Al-Khwarizmi conceived an entirely visual geometric technique known as **completing the square** (*al-jabr wa'l-muqabala*).

1. He draws a square of side length $x$, having area $x^2$.
2. He must add $10x$ to it. He takes two rectangles of side lengths $x$ and $5$ (whose combined area is $5x + 5x = 10x$) and pastes them along two adjacent sides of the central square:

```
             x             5
      ┌──────────────┬───────────┐
      │              │           │
    x │      x²      │    5x     │
      │              │           │
      ├──────────────┼ - - - - - ┤
    5 │      5x      │  MISSING  │
      └──────────────┴ - - - - - ┘
```

The area of this L-shaped region is $x^2 + 5x + 5x = x^2 + 10x$. And we know this total area must equal $39$.

3. Al-Khwarizmi observes: *“This shape is almost a complete large square of side length $(x + 5)$! It lacks only the tiny corner in the lower right.”*
4. What is the area of this missing corner?
   It is a square of $5 \times 5 = 25$!
5. Al-Khwarizmi resolves to **complete the square** by adding $25$ to both pans of the scale:
   $$(x^2 + 10x) + 25 = 39 + 25.$$
   The geometric figure becomes a perfect large square of side length $(x+5)$:
   $$(x + 5)^2 = 64.$$
6. It now suffices to take the square root:
   $$x + 5 = \sqrt{64} = 8.$$
7. Subtracting 5:
   $$x = 8 - 5 = 3.$$

Let us verify: for $x = 3$, we have $3^2 + 10 \times 3 = 9 + 30 = 39$. It is completely exact!
Every formula for quadratic equations taught in high school (in Chapter 35) directly descends from this geometric stroke of Al-Khwarizmi adding the missing corner.

---

### 8. Step-by-Step Worked Examples

#### Example 1: Expanding and simplifying with double distributivity and negative parentheses
Expand and simplify the expression:
$$C = (3x - 2)(4x + 5) - (2x - 1)(x - 3).$$

**Detailed Solution:**
Beware of the minus sign “$-$” between the two products! To prevent sign errors, keep the entire second expansion inside large square brackets:

1. First product:
   $$(3x - 2)(4x + 5) = 3x \times 4x + 3x \times 5 - 2 \times 4x - 2 \times 5 = 12x^2 + 15x - 8x - 10 = 12x^2 + 7x - 10.$$
2. Second product (inside brackets):
   $$(2x - 1)(x - 3) = 2x \times x + 2x \times (-3) - 1 \times x - 1 \times (-3) = 2x^2 - 6x - x + 3 = 2x^2 - 7x + 3.$$
3. Assemble:
   $$C = (12x^2 + 7x - 10) - [2x^2 - 7x + 3].$$
4. Remove brackets by reversing every interior sign:
   $$C = 12x^2 + 7x - 10 - 2x^2 + 7x - 3.$$
5. Group like terms:
   $$C = (12x^2 - 2x^2) + (7x + 7x) + (-10 - 3) = 10x^2 + 14x - 13.$$

---

#### Example 2: Expanding with special products
Expand the following expressions:
1. $D = (3x + 4)^2$
2. $E = (5x - 2)^2$
3. $F = (7x + 3)(7x - 3)$

**Detailed Solution:**
1. $D$ is of the form $(a + b)^2$ with $a = 3x$ and $b = 4$:
   $$D = (3x)^2 + 2 \times (3x) \times 4 + 4^2 = 9x^2 + 24x + 16.$$
   *(Pitfall avoided: $(3x)^2 = 9x^2$, not $3x^2$!)*
2. $E$ is of the form $(a - b)^2$ with $a = 5x$ and $b = 2$:
   $$E = (5x)^2 - 2 \times (5x) \times 2 + 2^2 = 25x^2 - 20x + 4.$$
3. $F$ is of the form $(a + b)(a - b)$ with $a = 7x$ and $b = 3$:
   $$F = (7x)^2 - 3^2 = 49x^2 - 9.$$

---

#### Example 3: Factoring with a common binomial factor
Factor the expression:
$$G = (2x - 5)(x + 4) - (2x - 5)(3x - 1).$$

**Detailed Solution:**
1. Identify the common binomial factor present in both terms: $(2x - 5)$.
2. Factor it out in front of large brackets:
   $$G = \underline{(2x - 5)} \left[ (x + 4) - (3x - 1) \right].$$
3. Simplify inside the brackets, taking extreme care with the minus sign before the second binomial:
   $$G = (2x - 5) [ x + 4 - 3x + 1 ].$$
4. Combine like terms:
   $$G = (2x - 5)(-2x + 5).$$

---

#### Example 4: Factoring a complex difference of two squares
Factor the expression:
$$H = (2x + 3)^2 - 36.$$

**Detailed Solution:**
1. Notice that $36 = 6^2$.
2. The expression is of the form $A^2 - B^2$ with $A = (2x + 3)$ and $B = 6$.
3. Apply the identity $A^2 - B^2 = (A + B)(A - B)$:
   $$H = \left[ (2x + 3) + 6 \right] \times \left[ (2x + 3) - 6 \right].$$
4. Simplify within each set of parentheses:
   $$H = (2x + 9)(2x - 3).$$

---

#### Example 5: Solving a complex equation reducible to a zero product
Solve in the real numbers the equation:
$$(3x + 1)^2 = (x - 4)^2.$$

**Detailed Solution:**
*Forbidden temptation:* Taking the square root directly on both sides without care, or expanding everything (which produces quadratic terms that are tricky to handle).
*The correct method:* Move everything to the left to yield “$= 0$” and factor as a difference of two squares:
$$(3x + 1)^2 - (x - 4)^2 = 0.$$
This is of the form $A^2 - B^2 = 0$ with $A = (3x + 1)$ and $B = (x - 4)$.
$$[(3x + 1) + (x - 4)] \times [(3x + 1) - (x - 4)] = 0$$
$$[3x + 1 + x - 4] \times [3x + 1 - x + 4] = 0$$
$$(4x - 3)(2x + 5) = 0.$$

This is a **zero-product equation**!
A product of factors equals zero if and only if at least one factor equals zero:
$$4x - 3 = 0 \quad \text{or} \quad 2x + 5 = 0$$
$$4x = 3 \implies x = \frac{3}{4} = 0.75$$
$$2x = -5 \implies x = -\frac{5}{2} = -2.5.$$
Conclusion: The equation has two solutions: $S = \left\{ -\frac{5}{2}, \frac{3}{4} \right\}$.

---

### Key Takeaways

1. **Double Distributivity:**
   $$(a + b)(c + d) = ac + ad + bc + bd.$$
2. **The 3 Special Products (know them forward and backward):**
   - Square of a sum: $(a + b)^2 = a^2 + 2ab + b^2$
   - Square of a difference: $(a - b)^2 = a^2 - 2ab + b^2$
   - Difference of two squares: $(a + b)(a - b) = a^2 - b^2$
3. **Fatal Errors to Avoid:**
   - $(a + b)^2 \neq a^2 + b^2$ (the double product $2ab$ is missing!)
   - $(3x)^2 = 9x^2 \neq 3x^2$ (the square applies to the coefficient 3 as well)
4. **Factoring Strategy:**
   - First look for a common factor (a number, $x$, or a binomial in parentheses).
   - If no common factor exists, identify a special product ($a^2-b^2$, $a^2+2ab+b^2$, or $a^2-2ab+b^2$).
5. **Zero-Product Equation:**
   $$A \times B = 0 \iff A = 0 \quad \text{or} \quad B = 0.$$
6. **Equations of the Form $x^2 = a$:**
   - If $a > 0$: two solutions $x = \sqrt{a}$ and $x = -\sqrt{a}$.
   - If $a = 0$: one solution $x = 0$.
   - If $a < 0$: no real solution ($S = \emptyset$).

---

### Exercises

#### Level ★: Direct Application

**Exercise 23.1** Expand and simplify the following expressions:
1. $A = (x + 3)(x + 7)$
2. $B = (2x + 1)(x - 4)$
3. $C = (x - 5)(3x - 2)$

**Exercise 23.2** Use special products to expand:
1. $D = (x + 6)^2$
2. $E = (x - 5)^2$
3. $F = (x + 8)(x - 8)$
4. $G = (2x + 3)^2$
5. $H = (4x - 1)^2$
6. $I = (5x + 2)(5x - 2)$

**Exercise 23.3** Compute cleverly without a calculator using a special product:
1. $102^2$
2. $49^2$
3. $61 \times 59$
4. $1003 \times 997$

**Exercise 23.4** Factor by identifying an obvious common factor:
1. $J = 5x + 35$
2. $K = x^2 + 8x$
3. $L = 7x^2 - 14x$

**Exercise 23.5** Factor using special products:
1. $M = x^2 - 81$
2. $N = x^2 + 10x + 25$
3. $P = x^2 - 12x + 36$
4. $Q = 4x^2 - 9$

**Exercise 23.6** Solve the following zero-product equations:
1. $(x - 7)(x + 2) = 0$
2. $(2x - 10)(3x + 15) = 0$
3. $x(4x - 9) = 0$

**Exercise 23.7** Solve the equations $x^2 = a$:
1. $x^2 = 49$
2. $x^2 = 17$
3. $x^2 = -9$
4. $x^2 = 0$

---

#### Level ★★: Deeper Reflection and Multi-Step Problems

**Exercise 23.8** Expand and simplify the complex expressions:
1. $R = (3x - 2)^2 - (x + 4)(x - 4)$
2. $S = (2x + 1)^2 - (3x - 2)^2$

**Exercise 23.9** Factor by identifying a common binomial block:
1. $T = (x - 3)(2x + 5) + (x - 3)(x - 1)$
2. $U = (3x + 2)(5x - 1) - (3x + 2)(2x + 7)$
3. $V = (4x - 3)^2 + (4x - 3)(x + 2)$

**Exercise 23.10** Factor the composite differences of squares:
1. $W = (x + 2)^2 - 25$
2. $Z = 49 - (2x - 1)^2$
3. $Y = (3x - 5)^2 - (x + 1)^2$

**Exercise 23.11** Solve the equations by reducing them to a zero-product equation:
1. $x^2 - 36 = 0$
2. $(2x + 3)(x - 1) = (2x + 3)(3x - 7)$
3. $9x^2 - 25 = 0$
4. $x^2 = 6x$

**Exercise 23.12** Computational Algorithm and Mystery:
Consider the following computational algorithm:
- Choose an integer.
- Add 1 to it.
- Square the result.
- Subtract the square of the starting number from the result.
- Subtract 1.
1. Test this algorithm with 3, 5, and 10. What pattern emerges?
2. Prove this conjecture for any starting number using algebra.

**Exercise 23.13** The Magic Trick for Squaring Numbers Ending in 5:
To mentally compute the square of a number ending in 5 (such as $35^2$), the trick is to multiply the tens digit ($3$) by the next consecutive integer ($4$), yielding $3 \times 4 = 12$, and append $25$ to the end: you get $1225$!
A number ending in 5 can be written algebraically as $10d + 5$, where $d$ is the number of tens.
Expand $(10d + 5)^2$ and prove why this trick works every single time!

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 23.14** Solving in the Manner of Al-Khwarizmi (Completing the Square):
Solve the equation $x^2 + 6x = 16$ following Al-Khwarizmi's geometric method step by step:
1. Express $x^2 + 6x$ in the form $(x + \dots)^2 - \dots$
2. Deduce an equation of the form $(x + 3)^2 = \text{number}$.
3. Find the positive value of $x$.

**Exercise 23.15** The Grand Challenge of Pythagoras and Algebra:
A right triangle has a hypotenuse measuring $(x + 8)$ cm. Its two legs measure $x$ cm and $(x + 7)$ cm respectively.
1. Using the Pythagorean theorem, write an equation satisfied by $x$.
2. Expand and simplify this equation to bring it into the form $x^2 - 2x - 15 = 0$.
3. Verify that $x^2 - 2x - 15 = (x - 5)(x + 3)$.
4. Deduce the value of $x$ and the lengths of the three sides of the triangle.

**Exercise 23.16** The Difference of Two Cubes (For the Inquisitive Mind):
1. Expand the expression $(a - b)(a^2 + ab + b^2)$.
2. What do you notice?
3. Deduce a factorization of $x^3 - 8$ (noting that $8 = 2^3$).

---

### Solutions

#### Level ★

**Solution 23.1**
1. $A = x^2 + 7x + 3x + 21 = x^2 + 10x + 21$.
2. $B = 2x^2 - 8x + x - 4 = 2x^2 - 7x - 4$.
3. $C = 3x^2 - 2x - 15x + 10 = 3x^2 - 17x + 10$.

**Solution 23.2**
1. $D = x^2 + 2 \times x \times 6 + 6^2 = x^2 + 12x + 36$.
2. $E = x^2 - 2 \times x \times 5 + 5^2 = x^2 - 10x + 25$.
3. $F = x^2 - 8^2 = x^2 - 64$.
4. $G = (2x)^2 + 2 \times 2x \times 3 + 3^2 = 4x^2 + 12x + 9$.
5. $H = (4x)^2 - 2 \times 4x \times 1 + 1^2 = 16x^2 - 8x + 1$.
6. $I = (5x)^2 - 2^2 = 25x^2 - 4$.

**Solution 23.3**
1. $102^2 = (100 + 2)^2 = 100^2 + 2 \times 100 \times 2 + 2^2 = 10\,000 + 400 + 4 = 10\,404$.
2. $49^2 = (50 - 1)^2 = 50^2 - 2 \times 50 \times 1 + 1^2 = 2\,500 - 100 + 1 = 2\,401$.
3. $61 \times 59 = (60 + 1)(60 - 1) = 60^2 - 1^2 = 3\,600 - 1 = 3\,599$.
4. $1003 \times 997 = (1000 + 3)(1000 - 3) = 1000^2 - 3^2 = 1\,000\,000 - 9 = 999\,991$.

**Solution 23.4**
1. $J = 5(x + 7)$.
2. $K = x(x + 8)$.
3. $L = 7x(x - 2)$.

**Solution 23.5**
1. $M = x^2 - 9^2 = (x + 9)(x - 9)$.
2. $N = x^2 + 2 \times x \times 5 + 5^2 = (x + 5)^2$.
3. $P = x^2 - 2 \times x \times 6 + 6^2 = (x - 6)^2$.
4. $Q = (2x)^2 - 3^2 = (2x + 3)(2x - 3)$.

**Solution 23.6**
1. $x - 7 = 0$ or $x + 2 = 0 \implies x = 7$ or $x = -2$. $S = \{-2, 7\}$.
2. $2x - 10 = 0 \implies 2x = 10 \implies x = 5$ or $3x + 15 = 0 \implies 3x = -15 \implies x = -5$. $S = \{-5, 5\}$.
3. $x = 0$ or $4x - 9 = 0 \implies 4x = 9 \implies x = \frac{9}{4} = 2.25$. $S = \{0, 2.25\}$.

**Solution 23.7**
1. $x = \sqrt{49} = 7$ or $x = -\sqrt{49} = -7$. $S = \{-7, 7\}$.
2. $x = \sqrt{17}$ or $x = -\sqrt{17}$. $S = \{-\sqrt{17}, \sqrt{17}\}$.
3. No real square is negative. No real solutions: $S = \emptyset$.
4. $x = 0$. Exactly one solution: $S = \{0\}$.

---

#### Niveau ★★

**Solution 23.8**
1. $R = (9x^2 - 12x + 4) - (x^2 - 16) = 9x^2 - 12x + 4 - x^2 + 16 = 8x^2 - 12x + 20$.
2. $S = (4x^2 + 4x + 1) - (9x^2 - 12x + 4) = 4x^2 + 4x + 1 - 9x^2 + 12x - 4 = -5x^2 + 16x - 3$.

**Solution 23.9**
1. $T = (x - 3)[(2x + 5) + (x - 1)] = (x - 3)(3x + 4)$.
2. $U = (3x + 2)[(5x - 1) - (2x + 7)] = (3x + 2)[5x - 1 - 2x - 7] = (3x + 2)(3x - 8)$.
3. $V = (4x - 3)[(4x - 3) + (x + 2)] = (4x - 3)(5x - 1)$.

**Solution 23.10**
1. $W = (x + 2)^2 - 5^2 = [(x + 2) + 5][(x + 2) - 5] = (x + 7)(x - 3)$.
2. $Z = 7^2 - (2x - 1)^2 = [7 + (2x - 1)][7 - (2x - 1)] = [7 + 2x - 1][7 - 2x + 1] = (2x + 6)(-2x + 8)$. (Factoring out 2 from each factor gives: $Z = 4(x + 3)(-x + 4)$).
3. $Y = [(3x - 5) + (x + 1)][(3x - 5) - (x + 1)] = [4x - 4][2x - 6] = 4(x - 1) \times 2(x - 3) = 8(x - 1)(x - 3)$.

**Solution 23.11**
1. $x^2 - 36 = 0 \iff (x - 6)(x + 6) = 0 \iff x = 6$ or $x = -6$. $S = \{-6, 6\}$.
2. Move everything to the left: $(2x + 3)(x - 1) - (2x + 3)(3x - 7) = 0$.
   Common factor $(2x + 3)$: $(2x + 3)[(x - 1) - (3x - 7)] = 0 \iff (2x + 3)(-2x + 6) = 0$.
   Branches: $2x + 3 = 0 \implies x = -\frac{3}{2}$ or $-2x + 6 = 0 \implies x = 3$. $S = \{-\frac{3}{2}, 3\}$.
3. $(3x)^2 - 5^2 = 0 \iff (3x - 5)(3x + 5) = 0 \implies x = \frac{5}{3}$ or $x = -\frac{5}{3}$. $S = \{-\frac{5}{3}, \frac{5}{3}\}$.
4. $x^2 - 6x = 0 \iff x(x - 6) = 0 \implies x = 0$ or $x = 6$. $S = \{0, 6\}$.

**Solution 23.12**
1. For 3: $3 + 1 = 4 \to 4^2 = 16 \to 16 - 3^2 = 16 - 9 = 7 \to 7 - 1 = 6$ (twice 3).
   For 5: $5 + 1 = 6 \to 6^2 = 36 \to 36 - 25 = 11 \to 11 - 1 = 10$ (twice 5).
   For 10: $10 + 1 = 11 \to 11^2 = 121 \to 121 - 100 = 21 \to 21 - 1 = 20$ (twice 10).
   Conjecture: the algorithm always yields double the chosen number ($2n$).
2. Let $n$ be the starting number.
   The algorithm computes: $(n + 1)^2 - n^2 - 1$.
   Expanding: $(n^2 + 2n + 1) - n^2 - 1 = n^2 + 2n + 1 - n^2 - 1 = 2n$.
   The conjecture is rigorously proved for any integer $n$.

**Solution 23.13**
Expand $(10d + 5)^2$ with the square of a sum identity:
$$(10d + 5)^2 = (10d)^2 + 2 \times (10d) \times 5 + 5^2 = 100d^2 + 100d + 25.$$
Factor out $100d$ from the first two terms:
$$100d(d + 1) + 25 = [d \times (d + 1)] \times 100 + 25.$$
Multiplying $d \times (d + 1)$ by 100 exactly shifts the result two places to the left (into the hundreds place), and adding 25 places “25” directly in the tens and units places! The trick is mathematically infallible.

---

#### Level ★★★

**Solution 23.14**
1. We know that $(x + 3)^2 = x^2 + 6x + 9$. Therefore $x^2 + 6x = (x + 3)^2 - 9$.
2. The equation $x^2 + 6x = 16$ becomes:
   $$(x + 3)^2 - 9 = 16 \iff (x + 3)^2 = 16 + 9 = 25.$$
3. Since $25 = 5^2$, we have $x + 3 = 5$ (for the positive solution sought by Al-Khwarizmi), yielding $x = 5 - 3 = 2$.
   (The modern second algebraic solution is $x + 3 = -5 \implies x = -8$).

**Solution 23.15**
1. By the Pythagorean theorem:
   $$x^2 + (x + 7)^2 = (x + 8)^2.$$
2. Expand both sides:
   $$x^2 + (x^2 + 14x + 49) = x^2 + 16x + 64$$
   $$2x^2 + 14x + 49 = x^2 + 16x + 64.$$
   Move everything to the left:
   $$(2x^2 - x^2) + (14x - 16x) + (49 - 64) = 0 \iff x^2 - 2x - 15 = 0.$$
3. Expand $(x - 5)(x + 3)$:
   $$(x - 5)(x + 3) = x^2 + 3x - 5x - 15 = x^2 - 2x - 15.$$
   The identity is verified!
4. The equation becomes $(x - 5)(x + 3) = 0$.
   The solutions are $x = 5$ or $x = -3$.
   Since a physical length cannot be negative, we retain only $x = 5$.
   The three sides of the triangle measure:
   - First leg: $x = 5 \text{ cm}$
   - Second leg: $x + 7 = 5 + 7 = 12 \text{ cm}$
   - Hypotenuse: $x + 8 = 5 + 8 = 13 \text{ cm}$.
   Check: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$. It is a perfect Pythagorean triple!

**Solution 23.16**
1. Expand by distributive properties:
   $$(a - b)(a^2 + ab + b^2) = a \times a^2 + a \times ab + a \times b^2 - b \times a^2 - b \times ab - b \times b^2$$
   $$= a^3 + a^2b + ab^2 - a^2b - ab^2 - b^3.$$
   All intermediate terms cancel pairwise!
   $$= a^3 - b^3.$$
2. We observe that the difference of two cubes factors according to the remarkable formula:
   $$a^3 - b^3 = (a - b)(a^2 + ab + b^2).$$
3. For $x^3 - 8 = x^3 - 2^3$, apply with $a = x$ and $b = 2$:
   $$x^3 - 8 = (x - 2)(x^2 + 2x + 2^2) = (x - 2)(x^2 + 2x + 4).$$

---

### The Question Opening the Next Chapter

Thanks to special products and the zero-product property, you now know how to master perfect equalities and strict balance. But in real life and commerce, scale pans rarely rest at the exact same level: one is often heavier than the other, a subscription price becomes more advantageous than another beyond a certain threshold, and two merchants compete for customers.

What happens when the scale tilts? How can we manipulate an **inequality** without turning the world upside down, and how do we determine the intersection of two merchant destinies? That is the mystery we will unravel in the next chapter: **The Two Merchants and Inequalities**.
