# VOLUME II — THE SECRET OF SHARING AND THE MAGNITUDES OF THE WORLD (Ages 8–11 / Grades 3–5)
## CHAPTER 8: The Rebel Stones and the Lonely Numbers

> *“There are numbers that willingly accept being folded, organized into battalions, and sliced into rectangles. And there are rebel numbers, wild and untamed, that refuse to bend and stand like solitary stones in the desert. These wild stones are the atoms of all numbers.”*

---

### What You Are About to Discover

- What **multiples** of a number are (the numbers you land on when always leaping by the same length).
- What **divisors** of a number are (row lengths that divide evenly with nothing left over).
- **Detective tricks** to know, without calculating long divisions, whether a number divides evenly by 2, 3, 5, 9, or 10.
- **Prime numbers**, those numbers that refuse to form rectangles, and why they are the bricks of all other numbers.
- The **Sieve of Eratosthenes**, a number-sorting machine invented more than 2,000 years ago.

---

### 1. The Problem: The Market Guards' Parade

You are now eight years old. The tent campsite has grown into a small town on the banks of a great river. Every morning, merchants arrive from distant oases with camels laden with spices, pottery, and woven wool.

To ensure no one steals from the market stalls, the governor has recruited a small troop of guards. Today is the great harvest festival: the guards must march in parade across the grand central square.

The captain commands **12 soldiers**. He shouts:  
*“Form a rectangle! I want perfect rows, without a single soldier sticking out!”*

The 12 soldiers obey with a smile:

- they form **2 rows of 6**: $2 \times 6 = 12$;
- then **3 rows of 4**: $3 \times 4 = 12$;
- and to pass through the city's narrow gate, a single **file of 12**: $1 \times 12 = 12$.

```
   Formation 2 × 6:              Formation 3 × 4:
   o o o o o o                    o o o o
   o o o o o o                    o o o o
                                  o o o o
```

Everyone applauds: 12 is a **docile** number. It loves forming rectangles.

Suddenly, a messenger arrives at a full gallop: one of the soldiers must leave immediately to deliver an urgent message to the king. Only **11 soldiers** remain. The captain blows his whistle:  
*“Reform a rectangle!”*

- In rows of 2: five in front, five behind… and the eleventh finds himself **all alone** at the end!
- In rows of 3: three rows of three make 9… and **2 soldiers** are left stranded outside.
- In rows of 4: $4 + 4 = 8$, leaving **3** soldiers stranded.
- In rows of 5: $5 + 5 = 10$, leaving **1** soldier sticking out.

```
   o o o o o
   o o o o o  o   <--- the soldier sticking out!
```

The captain sweats under his bronze helmet. No matter how hard he tries: **with 11 soldiers, no solid rectangle is possible**, except for the long single line of 1 by 11.

It is neither the soldiers' fault nor the captain's. It is the number 11 itself that **refuses** to be broken into rows. Why are some numbers so flexible, while others are so stubborn? To understand this mystery, we must learn two crucial words: **multiple** and **divisor**.

> **🖐️ Your Turn —** Take 12 small objects (buttons, beans, or coins). Form every possible rectangle. Then remove one object and try again with 11. Feel the difference with your own fingers!

---

### 2. Multiples: Always Leaping by the Same Length

Imagine a frog hopping along a long number line. It starts at 0 and always makes jumps of **3 steps**.

```
  0     3     6     9     12    15    18    21
  |--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|--.--.--|
  ^        ^        ^        ^        ^        ^        ^        ^
  start   1 jump   2 jumps  3 jumps  4 jumps  ...
```

The points where its feet land are: $0, 3, 6, 9, 12, 15, 18, 21, \dots$  
These are exactly the products of the **times-3 table**: $3 \times 0$, $3 \times 1$, $3 \times 2$, $3 \times 3$, and so on.

> **📐 Definition — Multiple**  
> A number is a **multiple of 3** if it belongs to the 3-times table, which means it can be written as $3 \times (\text{a whole number})$.  
> More generally, a number is a **multiple of $b$** if it can be written as $b \times (\text{a whole number})$.

The three small dots “$\dots$” written at the end of a list read as “**and so on**”. They mean: the list continues in exactly the same way, **never stopping**. For the frog can keep jumping as long as it likes: there are **infinitely many** multiples of 3!

> **Worked Example 1 — Is it a multiple?**  
> *Question:* Is 42 a multiple of 6? What about 45?  
> *Looking into the 6-times table:* $6 \times 7 = 42$. Yes, 42 is a multiple of 6.  
> *For 45:* $6 \times 7 = 42$ and $6 \times 8 = 48$. 45 falls **between** the two; it is not in the table. 45 is **not** a multiple of 6. (The frog jumping by 6 leaps right over 45 without landing on it.)

> **Worked Example 2 — Common Multiples**  
> *Question:* Which numbers up to 40 are multiples of both 4 and 6?  
> Multiples of 4: 0, 4, 8, **12**, 16, 20, **24**, 28, 32, **36**, 40.  
> Multiples of 6: 0, 6, **12**, 18, **24**, 30, **36**.  
> The numbers present in both lists: **0, 12, 24, 36**. Two frogs, one jumping by 4s and the other by 6s, meet on these exact stepping stones!

---

### 3. Divisors: Row Lengths that Divide Evenly

Let us return to our soldiers. With 12 soldiers, we could form rows of 1, 2, 3, 4, 6, and 12 (since $4 \times 3$ and $6 \times 2$ also work by simply turning the rectangle). With 11, only rows of 1 and 11 worked.

> **📐 Definition — Divisor**  
> A number $b$ is a **divisor** of $a$ if we can arrange $a$ objects into rows of $b$ **without a single object left over**.  
> In other words: $a$ is in the times table of $b$.  
> We also say: “**$a$ is divisible by $b$**” or “**$b$ divides $a$**”.

Notice how these two concepts go hand in hand, like two faces of the same coin:

$$12 = 3 \times 4 \quad \Longrightarrow \quad \begin{cases} 12 \text{ is a multiple of } 3 \\ 3 \text{ is a divisor of } 12 \end{cases}$$

The heavy arrow “$\Longrightarrow$” reads as “**therefore**” or “**implies that**”.

> **💡 Did You Know?** Later, in middle and high school, mathematicians will write “$3 \mid 12$” (a small vertical bar) to say “3 divides 12”. Do not confuse this with a fraction bar, which is horizontal or slanted!

#### The Pair Method for Finding ALL Divisors

Every rectangle reveals **two** divisors at once: its width and its length. To make sure nothing is forgotten, we look for pairs systematically, starting with 1.

> **Worked Example 3 — All Divisors of 24**  
> - $1 \times 24 = 24 \implies$ divisors 1 and 24  
> - $2 \times 12 = 24 \implies$ divisors 2 and 12  
> - $3 \times 8 = 24 \implies$ divisors 3 and 8  
> - 4? $4 \times 6 = 24 \implies$ divisors 4 and 6  
> - 5? $5 \times 4 = 20$, $5 \times 5 = 25$: no.  
> - 6? Already found with 4! The pairs begin to repeat in reverse: **we can stop here**.  
>  
> The divisors of 24 are: **1, 2, 3, 4, 6, 8, 12, 24**. There are 8 of them, forming 4 distinct rectangles.

```
     1 ───────────────────────── 24
        2 ─────────────── 12
            3 ─────── 8
               4 ─ 6          <- the pairs meet in the middle
```

> **Worked Example 4 — Divisors of 36 (A Square Number)**  
> $1 \times 36$, $2 \times 18$, $3 \times 12$, $4 \times 9$, $6 \times 6$.  
> Divisors: **1, 2, 3, 4, 6, 9, 12, 18, 36**. There are 9 divisors: an **odd** number of divisors! Why? Because the rectangle $6 \times 6$ is a **square**: the 6 serves as both width and length, so it is counted only once.

> **⚠️ Pitfall Warning — Peculiar Cases**  
> - **1 is a divisor of every whole number**: we can always form a single file ($1 \times 12$, $1 \times 11$, etc.).  
> - **Every number is a divisor of itself** and a multiple of itself: $12 = 12 \times 1$.  
> - **0 is a multiple of every number**: $0 = 3 \times 0 = 7 \times 0$. Before jumping, the frog is already standing on 0!  
> - **Never divide by 0**: arrange 12 soldiers into rows of 0 soldiers? You could make empty rows for a thousand years without ever placing a single person. It is completely meaningless.  
> - Do not mix up the words: “3 is a **divisor** of 12”, but “12 is a **multiple** of 3”. The **smaller** divides, the **larger** is a multiple.

---

### 4. Detective Tricks: Divisibility Rules

At the market, a merchant has 3,471 dates. Can he divide them into bags of 3 without any leftover? Carrying out long division by hand would be tedious. Fortunately, mathematicians have discovered **divisibility rules**: clever clues that let you answer in the blink of an eye.

#### Rules for the Last Digit: 2, 5, and 10

Remember: a number like 3,471 consists of thousands, hundreds, tens, and units. But **a ten (10) can always be divided evenly by 2, 5, and 10**: $10 = 2 \times 5 = 5 \times 2 = 10 \times 1$. And hundreds and thousands are simply bundles of tens! Therefore, everything in the tens, hundreds, and thousands columns divides evenly without remainder. **Only the single units digit can cause a leftover.** That is why you only need to inspect the **last digit**.

> **📐 Divisibility Rules for 2, 5, and 10**  
> - A number is divisible by **2** if its units digit is **0, 2, 4, 6, or 8**. We say it is **even**. Otherwise, it is **odd**.  
> - A number is divisible by **5** if its units digit is **0 or 5**.  
> - A number is divisible by **10** if its units digit is **0**.

> **Worked Example 5 — The Last Digit Speaks**  
> - 3,476: ends in 6 $\implies$ divisible by 2; not by 5; not by 10.  
> - 985: ends in 5 $\implies$ divisible by 5; odd, so not by 2; not by 10.  
> - 7,230: ends in 0 $\implies$ divisible by 2, by 5, **and** by 10.

#### The Magic Rules of Summing the Digits: 3 and 9

For 3 and 9, inspecting the last digit does not work at all! (13 ends in 3, but $13 = 3 \times 4 + 1$ is not divisible by 3.) We need a sharper insight.

Look closely:
$$10 = 9 + 1 \qquad 100 = 99 + 1 \qquad 1\,000 = 999 + 1$$

Now, $9$, $99$, and $999$ divide perfectly into groups of 9 (and thus into groups of 3 as well, since $9 = 3 \times 3$). Each ten, each hundred, and each thousand therefore leaves **exactly 1 stray unit sticking out**.

Take 234: this is 2 hundreds, 3 tens, and 4 units.  
- The 2 hundreds leave **2** stray units (1 each).  
- The 3 tens leave **3** stray units.  
- The 4 units are **4** stray units.  

In total, the leftover stray pieces equal $2 + 3 + 4 = 9$ units: **the sum of the digits**! And 9 divides evenly by both 9 and 3. Therefore, 234 is divisible by both 9 and 3. (Check: $234 = 9 \times 26$.)

> **📐 Divisibility Rules for 3 and 9**  
> - A number is divisible by **3** if the **sum of its digits** is a multiple of 3.  
> - A number is divisible by **9** if the **sum of its digits** is a multiple of 9.

> **Worked Example 6 — The Merchant's Dates**  
> 3,471: $3 + 4 + 7 + 1 = 15$. 15 is in the 3-times table ($3 \times 5$), so **3,471 is divisible by 3**: the merchant can pack his bags without any leftovers! ($3\,471 = 3 \times 1\,157$.)  
> However, 15 is not in the 9-times table: 3,471 is **not** divisible by 9.

> **Worked Example 7 — When the Sum Is Still Large**  
> 98,769: $9 + 8 + 7 + 6 + 9 = 39$. Is 39 a multiple of 3? Repeat the trick: $3 + 9 = 12$, and $12 = 3 \times 4$. Yes! Therefore 98,769 is divisible by 3. By 9? 39 is not in the 9-times table ($9 \times 4 = 36$, $9 \times 5 = 45$): no.

> **⚠️ Pitfall Warning**  
> - For 3 and 9, **never look only at the last digit**: 23 ends in 3 but is not divisible by 3 ($2 + 3 = 5$). 27 ends in 7 and is divisible by 3 ($2 + 7 = 9$).  
> - **Divisible by 9 $\implies$ divisible by 3**, because $9 = 3 \times 3$. But the **reverse is false**: 12 is divisible by 3, but not by 9.  
> - **Divisible by 2 and by 5 $\implies$ divisible by 10** (the last digit must be even AND be 0 or 5: it must be 0).  
> - An **odd** number is never divisible by 10, nor by 4, nor by 6 (because all these divisors are even).

> **🖐️ Your Turn — The Detective Game**  
> One player calls out a large number. The other player must announce as fast as possible which numbers among 2, 3, 5, 9, and 10 divide it evenly. Each correct answer scores one point; a mistake loses a point.

---

### 5. Prime Numbers: The Atoms of Numbers

Let us return to our stubborn troop of soldiers. The number 11 has only **two** divisors: 1 and 11. It cannot form any true rectangle.

> **📐 Definition — Prime Number**  
> A **prime number** is a whole number greater than or equal to 2 that has **exactly two distinct divisors**: 1 and itself.  
> A whole number (greater than 1) that has more than two divisors is called **composite**: it can be composed into a rectangle.

The word “prime” comes from the Latin *primus*: “first, original, that which comes before all else”. These are numbers that exist **before** all others, because every other number is built from them, as you will see.

Let us inspect the first few whole numbers:

| Number | Possible Rectangles | Divisors | Prime? |
|:---:|:---|:---|:---:|
| 1 | 1 × 1 | 1 | **No** (only one divisor) |
| 2 | 1 × 2 | 1, 2 | Yes |
| 3 | 1 × 3 | 1, 3 | Yes |
| 4 | 1 × 4, 2 × 2 | 1, 2, 4 | No |
| 5 | 1 × 5 | 1, 5 | Yes |
| 6 | 1 × 6, 2 × 3 | 1, 2, 3, 6 | No |
| 7 | 1 × 7 | 1, 7 | Yes |
| 8 | 1 × 8, 2 × 4 | 1, 2, 4, 8 | No |
| 9 | 1 × 9, 3 × 3 | 1, 3, 9 | No |
| 10 | 1 × 10, 2 × 5 | 1, 2, 5, 10 | No |
| 11 | 1 × 11 | 1, 11 | Yes |

> **⚠️ Pitfall Warning — The Special Cases of 1 and 2**  
> - **1 is not prime.** It has only **one** divisor (itself), whereas the definition strictly demands exactly two. Mathematicians deliberately excluded 1: otherwise, the fundamental law “every number breaks down in a unique way into prime numbers” would collapse (one could multiply by 1 as many times as desired without changing the value).  
> - **2 is the only even prime number.** Every other even number is divisible by 2, meaning it has at least three divisors: 1, 2, and itself.  
> - **Odd does not mean prime!** 9, 15, 21, 25, 27 are odd… and composite ($9 = 3 \times 3$, $15 = 3 \times 5$, $21 = 3 \times 7$, etc.). Beware especially of **51** ($= 3 \times 17$) and **91** ($= 7 \times 13$): they look prime at first glance, but they are impostors!

#### Breaking a Number Down to Its Atoms: The Factor Tree

Take any composite number, for example **60**. Break it into two factors, then break down each factor as long as possible:

```
              60
            /    \
           6      10
          / \    /  \
         2   3  2    5        <- cannot be broken further: these are primes!
```

$$60 = 2 \times 2 \times 3 \times 5$$

The numbers multiplied together are called **factors**. Here, all factors are prime numbers: we say we have **factored 60 into a product of prime factors**.

> **Worked Example 8 — Another Path for 60**  
> What if we had started with $60 = 4 \times 15$?  
> $4 = 2 \times 2$ and $15 = 3 \times 5$. We still obtain $60 = 2 \times 2 \times 3 \times 5$!  
> No matter which path you take, **you always arrive at the exact same prime atoms** (only the order of factors might change). This is a profound law of arithmetic, already known to the ancient Greek mathematician **Euclid**, which you will prove formally in high school.

This is why prime numbers are called **the atoms of numbers**: just as all physical objects are built of atoms, **every whole number greater than 1 is uniquely built of prime numbers multiplied together**.
