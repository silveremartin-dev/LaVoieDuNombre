# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 22: The Mystery Bag on Al-Khwarizmi's Scale

> *“The ignorant man forces the lock and tears open the bag to see what is hidden inside. The mathematician observes the two arms of the scale, removes a weight on the left, a weight on the right, and the unknown reveals itself in the clear light of reason.”*

---

### What You Are About to Discover

- Why we suddenly begin to **calculate with letters**, and what “$3x$”, “$x^2$”, or “$a(b+c)$” truly mean.
- How to **simplify and combine like terms** (sorting apples with apples) and how to **expand** using the **distributive property**, proved with a simple rectangle.
- How to **test an equality**: true for one value, true for all, or false—and the power of a single **counterexample**.
- How to solve any **first-degree equation** using the two fundamental gestures of the balance scale.
- How to **set up an equation from a word problem**: ages, perimeters, computational algorithms, and even the riddle of Diophantus's epitaph.
- The classic **pitfalls**: $2x + 3 \neq 5x$, $x \times x \neq 2x$, the minus sign “$-$” before parentheses, and equations that have… no solution, or infinitely many.

---

### 1. The Problem: The Grand Bazaar of Baghdad and the Bag of Gold

You are now twelve or thirteen years old. Let us leave the plains of Egypt behind, cross the desert sands, and enter the most fabulous metropolis of the medieval world: **Baghdad**, the “City of Peace,” around the year **820**.

At the heart of the city stands the *House of Wisdom* (*Bayt al-Hikma*), an immense library where scholars from Persia, India, and Greece translate the world's manuscripts into Arabic: Euclid, Ptolemy, Indian astronomers… But today, a lively crowd gathers in the great goldsmiths' bazaar.

At the center of a circle of curious merchants, a man draped in a green brocade cloak has set upon a table a magnificent **brass balance scale with two pans**.

* On the left pan, he places **a brown canvas bag, tightly stitched**, sealed with a stamp of red wax. No one knows what is inside! Beside the bag, he places **3 copper ingots**, each weighing one kilogram.
* On the right pan, he places **11 copper ingots** of one kilogram each.

The beam of the scale rocks slowly… and comes to rest, **perfectly horizontal**.

```
             [ Bag ] + 3 kg                     11 kg
                 o─────o                        o─────o
                 \     /                        \     /
                  \   /                          \   /
         ───────────[■]────────────────────────────[■]───────────
                                    ▲
                              Scale Fulcrum
```

*“This bag contains pure gold dust. Whoever tells me its exact weight without breaking the seal will leave with all the gold! But whoever is off by a single gram must surrender his mount to me!”*

No one dares risk their horse. Then, a Persian astronomer steps forward with a calm stride: **Muhammad ibn Musa al-Khwarizmi**.

*“The truth is already before your eyes. The two pans are in balance. If I remove the exact same amount from both sides at the same time, will the scale remain level?”* — *“Of course!”* replies the crowd.

With his left hand, he removes the **3 ingots** from the left pan: the pan lightens and rises. But instantly, with his right hand, he removes **3 ingots** from the right pan. The beam settles back down and rests once more, **level and still**.

```
                 [ Bag ]                          8 kg
                 o─────o                        o─────o
                 \     /                        \     /
                  \   /                          \   /
         ───────────[■]────────────────────────────[■]───────────
                                    ▲
```

On the left: the bag, all alone. On the right: $11 - 3 = 8$ ingots. *“The bag weighs eight kilograms.”* The merchant pales, breaks the seal, and weighs the bag alone: **precisely eight kilograms**.

So far, nothing you could not already do in your head. But the next day, the merchant returns, stung in his pride, with increasingly cunning riddles: two identical bags and 5 kg balancing 17 kg; three bags and 2 kg balancing one bag and 10 kg; then bags from which a portion of the contents has been removed… After a few puzzles, mental arithmetic is no longer enough. We need **a language** to write down these balance states, and **rules** to manipulate them without error. That language is **algebraic notation**. Those rules are the laws of **algebra**.

---

### 2. Calculating with Letters: Why and How

#### 2.1 The Letter Is a Hidden Number

In mathematics, a letter is **not** a word or an abbreviation for a unit. It is **a number** whose value is not (yet) known, or whose value can vary.

- When the letter represents a specific but **unknown** number (the weight of the bag), we call it an **unknown**.
- When the letter can take on **any value whatsoever** (the side length of an arbitrary square), we call it a **variable**.

You already know formulas with letters: the perimeter of a square of side length $c$ is $4 \times c$; the area of a rectangle is $L \times \ell$. These formulas say something that is true **for all squares**, for **all rectangles**, all at once. That is the great power of letters: **a single statement for an infinity of cases**.

> **📐 Definition — Algebraic Expression.** An *algebraic expression* is a sequence of operations in which certain numbers are replaced by letters. Examples: $3x + 5$; $\; 2(a - 4)$; $\; x^2 - 7x + 1$.

#### 2.2 Notational Conventions (and How to Read Them)

To work faster, mathematicians have agreed on a few shorthand conventions. Each has a spoken form:

| Written Form | Meaning | Read Aloud |
|---|---|---|
| $3x$ | $3 \times x$ | “three $x$” |
| $ab$ | $a \times b$ | “$a$ times $b$” or “$a$ $b$” |
| $4(x+1)$ | $4 \times (x + 1)$ | “four times the quantity $x$ plus one” |
| $x^2$ | $x \times x$ | “$x$ squared” |
| $x^3$ | $x \times x \times x$ | “$x$ cubed” |
| $1x$ | written simply as $x$ | “$x$” |
| $-1x$ | written simply as $-x$ | “negative $x$” or “minus $x$” |
| $0x$ | equals $0$ | — |

Safety rules:
- **Never omit** the $\times$ sign between **two numbers**: $3 \times 5$ must never be written as $35$!
- By convention, we write the **number before the letter**: $x \times 3$ is written $3x$ (and not $x3$).
- The order of operations from Chapter 18 still holds: exponents first, then multiplications and divisions, then additions and subtractions. Thus $3x^2$ means $3 \times (x \times x)$ and **not** $(3x) \times (3x)$.

> **🔍 True History — Who Invented Letters in Math?** Al-Khwarizmi himself wrote **no symbols at all**! Everything was written out in words: “a square and ten roots equal thirty-nine dirhams” (which we write $x^2 + 10x = 39$). He called the unknown *shay'* (“the thing”). Around 250 AD, the Greek mathematician **Diophantus** was already using abbreviations. In 1591, the Frenchman **François Viète**, advisor to King Henry IV and a master codebreaker, had the decisive insight: designate unknowns by vowels and known numbers by consonants. Finally, in 1637, **René Descartes**, in *La Géométrie*, took the last letters of the alphabet $x, y, z$ for unknowns and the first letters $a, b, c$ for known quantities: this is our modern convention. A popular tale claims that $x$ comes from the Arabic word *shay'* transcribed into Spanish as *xei*; it is a charming story, but no historical document confirms it.

> **💡 Did You Know?** The symbols $+$ and $-$ first appeared in print in 1489 in a commercial arithmetic book by the German Johannes Widmann. The equals sign $=$ was invented in 1557 by the Welsh mathematician **Robert Recorde**, who grew tired of writing “is equal to”: he chose two parallel line segments of identical length, “bicause noe 2 thynges can be moare equalle.”

#### 2.3 Evaluating an Expression (Substitution)

*Substitution* means replacing the letter with a specific number. The process is straightforward, but it requires two safeguards: **reinsert the multiplication signs $\times$** and **put negative numbers in parentheses**.

> **✏️ Worked Example 1 — Evaluating an expression for several values.**
> Let $A = 3x^2 - 5x + 2$. Evaluate $A$ for $x = 4$, then for $x = -2$.
>
> For $x = 4$: $A = 3 \times 4^2 - 5 \times 4 + 2 = 3 \times 16 - 20 + 2 = 48 - 20 + 2 = 30$.
>
> For $x = -2$: $A = 3 \times (-2)^2 - 5 \times (-2) + 2 = 3 \times 4 + 10 + 2 = 24$.
>
> Note: $(-2)^2 = (-2) \times (-2) = 4$ (the rule of signs from Chapter 20), and $-5 \times (-2) = +10$.

> **⚠️ Watch Out! Common Pitfall — Squaring and the Minus Sign.**
> - $-x^2$ means “the opposite of $x^2$”. For $x = 3$: $-x^2 = -9$.
> - $(-x)^2$ means “the square of the opposite of $x$”. For $x = 3$: $(-3)^2 = 9$.
> - For $x = -2$, $3x^2 = 3 \times 4 = 12$, but $(3x)^2 = (-6)^2 = 36$. The exponent applies **only to what immediately precedes it**.
> - And $x \times x = x^2$, **not** $2x$! For $x = 5$: $x^2 = 25$ whereas $2x = 10$.

---

### 3. Simplifying: Sorting Apples with Apples

Imagine a bazaar stall: “5 melons, 3 dates, 2 melons, 7 dates”. Any merchant will immediately say: “7 melons and 10 dates”. He **groups items of the same kind together**. But he would never say “17 melon-dates”!

In algebraic manipulation, it is the exact same. $5x + 3 + 2x + 7$ is grouped into $7x + 10$. The “$x$” terms go with the “$x$” terms, and the standalone constants with standalone constants. But $7x + 10$ cannot become $17x$: they are not objects of the same nature.

> **📐 Definition — Like Terms, Combining Like Terms.**
> - In a sum, each piece separated by $+$ or $-$ is a **term**. In $5x^2 - 3x + 8$, the terms are $5x^2$, $-3x$, and $8$.
> - The number placed in front of the variable part is called the **coefficient**: in $-3x$, the coefficient is $-3$.
> - Two terms are **like terms** if they have **the exact same variable part**: $4x$ and $-7x$ are like terms; $3x^2$ and $x^2$ are like terms; but $3x$ and $3x^2$ **are not like terms**.
> - **Simplifying (combining like terms)** an expression means grouping like terms by adding their coefficients, until the expression is written in its shortest possible form.

Why are we allowed to write $5x + 2x = 7x$? Because $5x + 2x$ is “5 bags plus 2 bags,” hence 7 bags. We will prove this rigorously in a moment using the distributive property.

> **✏️ Worked Example 2 — Combining like terms.**
> a) $B = 5x + 3 - 2x + 7$. We group: $(5x - 2x) + (3 + 7) = 3x + 10$.
>
> b) $C = 4x^2 - 3x + x^2 + 7x - 1$. The $x^2$ terms: $4x^2 + x^2 = 5x^2$. The $x$ terms: $-3x + 7x = 4x$. The constants: $-1$. Thus $C = 5x^2 + 4x - 1$.
>
> c) $D = 2a \times 3a$. Here it is a **product**: we multiply the numbers together and the letters together: $2 \times 3 \times a \times a = 6a^2$.
>
> d) $E = 2a + 3a = 5a$ (sum), whereas $2a \times 3a = 6a^2$ (product). Never confuse the two!

> **⚠️ Watch Out! Common Pitfall — What Cannot Be Combined.**
> - $2x + 3$ **does not equal** $5x$. Test: for $x = 10$, $2x + 3 = 23$, but $5x = 50$.
> - $x^2 + x$ **does not equal** $x^3$ nor $2x^2$. Test: for $x = 2$, $x^2 + x = 6$, $x^3 = 8$, $2x^2 = 8$.
> - $3x^2 + 2x^2 = 5x^2$, **and not** $5x^4$: we are adding “packets of $x^2$”, we are not multiplying.

---

### 4. Distributivity: A Rectangle That Does Not Lie

#### 4.1 The Intuition

A jeweler sells necklaces. Each necklace contains $a$ gold beads and $b$ silver beads. A customer orders 3 necklaces. How many beads are there in total? We can count necklace by necklace: $3 \times (a + b)$. Or we can count all the gold beads, then all the silver beads: $3a + 3b$. The total number of beads is identical! Therefore, $3(a + b) = 3a + 3b$.

#### 4.2 Proof by the Area of a Rectangle

Draw a rectangle of height $k$ and width $a + b$, partitioned into two parts:

```
            a              b
     ┌──────────────┬──────────┐
     │              │          │
  k  │   area k×a   │ area k×b │
     │              │          │
     └──────────────┴──────────┘
     ◄────────── a + b ─────────►
```

The area of the large rectangle is $k \times (a + b)$. But it is also the sum of the areas of the two smaller rectangles: $k \times a + k \times b$. **One and the same surface, two ways to calculate its area**: they must be equal.

> **📐 Property — The Distributive Property.** For any real numbers $k$, $a$, $b$:
> $$k(a + b) = ka + kb \qquad\text{and}\qquad k(a - b) = ka - kb.$$
> Read from left to right, we **expand** (converting a product into a sum). Read from right to left, we **factor** (converting a sum into a product, factoring out the **greatest common factor** $k$).

The word “distributivity” comes from the image of the multiplier $k$ being **distributed** to each term inside the parentheses, just as a mail carrier delivers a letter to every mailbox on the street.

And here is the promised proof of $5x + 2x = 7x$: it is simply the distributive property read in reverse: $5x + 2x = (5 + 2)x = 7x$.

> **✏️ Worked Example 3 — Expanding and simplifying.**
> a) $3(2x - 5) = 3 \times 2x - 3 \times 5 = 6x - 15$.
>
> b) $-2(x - 4) = (-2) \times x - (-2) \times 4 = -2x + 8$. (Watch the signs carefully: $-2 \times (-4) = +8$.)
>
> c) $x(x + 3) = x \times x + x \times 3 = x^2 + 3x$.
>
> d) $F = 4(x + 2) - 3(2x - 1) = 4x + 8 - 6x + 3 = -2x + 11$.

#### 4.3 The Minus Sign in Front of Parentheses

Parentheses preceded by a minus sign secretly conceal a factor of $-1$: $-(a + b) = (-1) \times (a + b) = -a - b$. Consequently:

> **📐 Rule — Removing Parentheses.**
> - Preceded by $+$: remove the parentheses **without changing anything**. $\; 7 + (3x - 2) = 7 + 3x - 2$.
> - Preceded by $-$: remove the parentheses **by reversing the sign of every term** inside. $\; 7 - (3x - 2) = 7 - 3x + 2 = 9 - 3x$.

> **⚠️ Watch Out! Common Pitfall.** The most frequent error in middle school: writing $7 - (3x - 2) = 7 - 3x - 2$. The student forgot to flip the sign of the **second** term! Test with $x = 0$: $7 - (0 - 2) = 9$, but $7 - 0 - 2 = 5$. The test exposes the blunder in two seconds.

#### 4.4 Factoring: The Return Journey

> **✏️ Worked Example 4 — Factoring out a common factor.**
> a) $6x + 9$: $6x = 3 \times 2x$ and $9 = 3 \times 3$. Common factor $3$: $6x + 9 = 3(2x + 3)$.
>
> b) $5x^2 - 10x$: $5x^2 = 5x \times x$ and $10x = 5x \times 2$. Common factor $5x$: $5x^2 - 10x = 5x(x - 2)$.
>
> c) $7a + 7 = 7 \times a + 7 \times 1 = 7(a + 1)$. Do not forget the “$1$”!
>
> **Systematic Verification**: expand back out. $5x(x - 2) = 5x^2 - 10x$ ✓.

Why factor? Because a **product** is often far easier to study than a sum. You will see in the next chapter that factoring allows us to solve equations that no physical scale could ever untangle.

---
