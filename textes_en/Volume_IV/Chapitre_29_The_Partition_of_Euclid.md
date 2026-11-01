# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 29: The Partition of Euclid

> *“A number is not a soft dough to be spread out at will: it is an edifice constructed from prime stones cut from diamond. Find the fundamental building blocks, and you will understand how to partition without shattering.”*

---

### What You Are About to Discover

- Why certain numbers refuse to be factored and constitute the **atoms of arithmetic**: prime numbers.
- How to factor any positive integer into a **unique product of prime factors** using factor trees and successive division ladders.
- What the **GCD (Greatest Common Divisor)** is, and three distinct methods to compute it.
- The dazzling insight conceived by **Euclid** over twenty-three centuries ago to uncover common divisors in a handful of division steps.
- How to reduce any fraction to **lowest terms (irreducible form)** in a single stroke.
- How to solve authentic real-life riddles: **tiling a hall without cutting a single slab**, and assembling **identical gift baskets** without leaving a single crumb.

---

### 1. The Problem: The Pharaoh's Mosaic and the Scribe's Baskets

Alexandria, around the year **300 BC**.
King Ptolemy I commissions a ceremonial hall in his royal palace. Two master craftsmen appear before the chief royal architect, their brows furrowed with concern.

* The first is the **master mosaicist**. The floor of the hall is a vast rectangle measuring **420 centimeters long by 132 centimeters wide**. The king has decreed:
  *“I want this floor paved entirely with square marble slabs, all strictly identical. I forbid cutting a single tile along the edges: every slab must be laid whole! And so that the floor appears magnificent, I demand that these slabs be **as large as possible**!”*
  The mosaicist groans: 1 cm tiles would work, of course, but it would take 55,440 of them and they would look tiny! Slabs of 2 cm would also work. But what is the largest possible square dimension?

* The second artisan is the **steward scribe** in charge of royal festivities. To honor visiting foreign dignitaries, he opens two chests of prized delicacies:
  - One chest holding **315 Egyptian pomegranates**;
  - One chest holding **180 honey confections**.
  The king demands identical ceremonial gift baskets for the guests:
  *“All baskets must be strictly identical: exactly the same count of pomegranates and the same count of honey confections in each basket. And I want nothing left over in the chests! Finally, I wish to host the **greatest possible number** of dignitaries!”*

```
   Problem 1: Tiling Without Waste          Problem 2: Gift Baskets Without Leftovers
   ┌───────────────────────────────┐
   │                               │         315 pomegranates    180 honey confections
   │   420 cm                      │           (to divide)            (to divide)
   │                               │                │                      │
   │ 132 cm                        │                ▼                      ▼
   │                               │         [ Basket 1 ]           [ Basket 2 ] ...
   └───────────────────────────────┘         Strictly identical contents!
   Maximal whole square slabs?               Maximal number of honored guests?
```

How can we resolve both dilemmas without spending three weeks testing random numbers?
In both cases, the underlying mathematical challenge is identical: we seek an integer that **evenly divides** two numbers simultaneously, and which is **as large as possible**.

To enlighten the artisans, a scholar steps into the palace courtyard carrying the papyrus rolls of his masterpiece, the *Elements*. His name is **Euclid**.

---

### 2. Multiples and Divisors: The Vocabulary of Precision

Before entering Euclid's workshop, we must master the precise vocabulary of arithmetic.

Let $a$ and $b$ be two positive integers (with $b \neq 0$).
If the division of $a$ by $b$ has a remainder of zero—that is, if $b$ divides evenly into $a$—we can write:
$$a = b \times k \quad (\text{where } k \text{ is an integer}).$$

We express this relationship using any of the following equivalent statements:
- **$a$ is a multiple of $b$** (e.g., 42 is a multiple of 6, since $42 = 6 \times 7$).
- **$b$ is a divisor of $a$** (e.g., 6 is a divisor of 42).
- **$b$ divides $a$** (often written in higher mathematics as $b \mid a$).
- **$a$ is divisible by $b$**.

> **⚠️ Watch Out! Pitfall — The Direction of Division!**
> Never confuse the divisor with the multiple:
> - Saying “6 divides 42” is **true**.
> - Saying “42 divides 6” is **completely false**! (42 does not fit inside 6).
> Rule of thumb: the **multiple** is always larger than or equal to the base; the **divisor** is always smaller than or equal to the dividend.

#### Quick Review: Divisibility Rules
To verify whether an integer divides another without executing long division:
- An integer is divisible by **2** if it is even (ends in 0, 2, 4, 6, 8).
- An integer is divisible by **3** if the sum of its digits is a multiple of 3 (e.g., $471 \implies 4+7+1 = 12$, divisible by 3).
- An integer is divisible by **4** if the number formed by its last two digits is divisible by 4 (e.g., $3,724 \implies 24 = 4 \times 6$, divisible by 4).
- An integer is divisible by **5** if its final digit is 0 or 5.
- An integer is divisible by **9** if the sum of its digits is a multiple of 9 (e.g., $855 \implies 8+5+5 = 18$, divisible by 9).
- An integer is divisible by **10** if it ends in 0.

---

### 3. Prime Numbers: The Atoms of the Mathematical Universe

Take the number 12. You can split it: $12 = 3 \times 4$. Then split 4 further: $4 = 2 \times 2$. Thus $12 = 2 \times 2 \times 3$.
Can you split 2 or 3 any further? No! Two and three are indivisible. They can only be divided by 1 and by themselves.

> **📐 Formal Definition — Prime Number.**
> A natural number is called **prime** if it possesses **exactly two distinct divisors**: 1 and itself.

Observe the direct consequences of this definition:
- **The number 0 is not prime**: it has infinitely many divisors (every non-zero number divides 0).
- **The number 1 is NOT prime**: it has only **one** divisor (itself). The definition strictly requires *two* distinct divisors. If 1 were classified as prime, the uniqueness of prime factorizations would break down ($6 = 2 \times 3 = 1 \times 2 \times 3 = 1 \times 1 \times 2 \times 3\dots$).
- **The number 2 is prime**: it is the **only even prime number** in the universe! Every other even number is divisible by 2, and therefore composite.

#### List of Prime Numbers Less Than 30
Memorize these as fundamental building blocks:
$$\mathbf{2, \quad 3, \quad 5, \quad 7, \quad 11, \quad 13, \quad 17, \quad 19, \quad 23, \quad 29}$$
*(Continuing to 100: 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97).*

> **💡 Did You Know?**
> In Book IX of the *Elements*, Euclid proved a breathtaking theorem: **there are infinitely many prime numbers**. Even if you journeyed for billions of years through unimaginably colossal numbers, you would never run out of newly emerging primes!

---

### 4. Prime Factorization

Here stands the single most important theorem in all of number theory. It is so foundational that it is termed the **Fundamental Theorem of Arithmetic**.

> **📐 Fundamental Theorem of Arithmetic —**
> Every integer greater than or equal to 2 can be written as a **product of prime numbers**.
> This factorization is **unique**, up to the order of the factors.

This is the “genetic fingerprint” of an integer. Two different numbers can never share the exact same prime factorization.

#### Two Practical Methods for Factoring Numbers

Let us factor the number **$360$**.

##### Method 1: The Factor Tree (Ideal for Mental Arithmetic)
Split the number into two convenient factors, then branch downward until every terminal leaf is a prime number:

```
                     360
                    /   \
                  36  ×  10
                 /  \    / \
                6 ×  6  2 × 5
               / \  / \
              2  3 2   3
```

Collect all prime leaves at the ends of the branches:
$$360 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 = \mathbf{2^3 \times 3^2 \times 5}$$

##### Method 2: The Division Ladder (The Algorithmic Method)
Draw a vertical bar. On the left, write the quotient; on the right, divide by successive primes in ascending order ($2, 3, 5, 7, 11\dots$):

```
     360 │ 2    (360 is even, divide by 2)
     180 │ 2    (180 is even, divide by 2)
      90 │ 2    (90 is even, divide by 2)
      45 │ 3    (45: 4+5=9, divisible by 3)
      15 │ 3    (15 is divisible by 3)
       5 │ 5    (5 is prime, divide by 5)
       1 │      (Division complete!)
```

The column on the right lists the prime factors directly:
$$360 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 = \mathbf{2^3 \times 3^2 \times 5}.$$

---

### 5. The GCD: Greatest Common Divisor

#### 5.1 Definition

When comparing two positive integers $a$ and $b$, certain integers divide both $a$ and $b$ simultaneously: these are their **common divisors**.
Because 1 divides every integer, there is always at least one common divisor: the number 1.

> **📐 Definition — GCD (Greatest Common Divisor).**
> Among all common divisors of two positive integers $a$ and $b$, the greatest of them is called the **Greatest Common Divisor**, denoted **$\gcd(a, b)$** or **$\text{GCD}(a, b)$**.

> **📐 Definition — Relatively Prime (Coprime) Numbers.**
> Two positive integers are said to be **relatively prime (coprime)** when their only common divisor is 1:
> $$\gcd(a, b) = 1$$
> *(Example: 8 and 15 are not prime numbers, but they are coprime because the divisors of 8 are $\{1, 2, 4, 8\}$ and those of 15 are $\{1, 3, 5, 15\}$; their sole common divisor is 1).*

#### 5.2 First Method: Using Prime Factorization

To find the GCD of two numbers from their prime factorizations:
1. Identify the **common prime factors** shared by both factorizations.
2. For each shared prime factor, select the **smallest exponent** with which it appears.
3. Multiply these shared powers together.

*Example:* Compute $\gcd(180, 315)$ (the banquet foods from our opening problem!):
- $180 = 2^2 \times 3^2 \times 5$
- $315 = 3^2 \times 5 \times 7$

Shared prime factors: 3 and 5.
- Lowest power of 3: $3^2$.
- Lowest power of 5: $5^1$.
$$\gcd(180, 315) = 3^2 \times 5 = 9 \times 5 = \mathbf{45}.$$
The royal scribe can prepare at most **45 identical gift baskets**!
Each basket will contain:
- $315 \div 45 = 7$ pomegranates;
- $180 \div 45 = 4$ honey confections.
Zero leftovers in the royal pantry!

---

### 6. The Two Historical Algorithms: Subtraction and Division

When dealing with large numbers, listing all divisors or finding complete prime factorizations can be labor-intensive. Ancient mathematicians devised fast, mechanical algorithms.

#### 6.1 The Repeated Subtraction Algorithm

This method rests on a straightforward arithmetic property:
> **📐 Property of Subtractions —**
> If an integer $d$ divides both $a$ and $b$ (with $a \ge b$), then $d$ also divides their difference $a - b$.
> Consequently: $\gcd(a, b) = \gcd(b, a - b)$.

**The Process:** Replace the larger number with the difference of the two numbers, and repeat until both numbers become equal. That shared final value is the GCD!

*Example:* Compute $\gcd(75, 45)$:
- $75 - 45 = 30 \implies \text{keep } 45 \text{ and } 30$
- $45 - 30 = 15 \implies \text{keep } 30 \text{ and } 15$
- $30 - 15 = 15 \implies \text{keep } 15 \text{ and } 15$
- $15 - 15 = 0$
The matching numbers reached are 15, so $\gcd(75, 45) = \mathbf{15}$.

> **⚠️ The Limitation of Subtraction:**
> If you needed to compute $\gcd(1,000,000, 2)$, you would have to subtract 2 five hundred thousand times! That is impractically slow. Fortunately, Euclid conceived a stroke of brilliance.

#### 6.2 The Euclidean Algorithm (Successive Divisions)

Instead of subtracting $b$ one step at a time, why not subtract all possible multiples of $b$ in a single stroke? That is precisely the principle of **Euclidean division** (integer division with remainder):
$$a = b \times q + r \quad (0 \le r < b)$$

> **📐 Euclid's Theorem —**
> If integer division of $a$ by $b$ yields remainder $r$, then:
> $$\gcd(a, b) = \gcd(b, r)$$

**The Euclidean Algorithm Procedure:**
1. Perform integer division of the larger number by the smaller number.
2. If the remainder is non-zero, divide the previous divisor by the remainder.
3. Repeat until the remainder becomes zero ($r = 0$).
4. **The GCD is the last NON-ZERO remainder.**

*Example: Solve the Alexandria mosaic tiling problem: $\gcd(420, 132)$.*

```
   Step 1:  420 = 132 × 3 + 24    (remainder r₁ = 24 ≠ 0)
   Step 2:  132 =  24 × 5 + 12    (remainder r₂ = 12 ≠ 0)
   Step 3:   24 =  12 × 2 +  0    (remainder r₃ = 0)
```

The final remainder before 0 is **12**.
Therefore:
$$\gcd(420, 132) = \mathbf{12}.$$

The master mosaicist has his solution:
- The largest possible uncut square slabs measure **$12\text{ cm} \times 12\text{ cm}$**.
- Along the length, he lays $420 \div 12 = 35$ slabs.
- Along the width, he lays $132 \div 12 = 11$ slabs.
- In total, he will install $35 \times 11 = \mathbf{385\text{ slabs}}$, fitting seamlessly without cutting a millimeter of marble!

---

### 7. The Crown Application: Simplifying Fractions to Lowest Terms

In middle school, you learned to simplify fractions by dividing numerator and denominator by common factors. But often students stop prematurely: dividing by 2, then by 3, uncertain whether further reduction is possible.

> **📐 Definition — Irreducible Fraction (Lowest Terms).**
> A fraction $\dfrac{a}{b}$ is said to be **irreducible** (in lowest terms) if its numerator $a$ and denominator $b$ are **relatively prime**, meaning $\gcd(a, b) = 1$. It cannot be simplified any further.

Using the GCD, any fraction can be simplified to lowest terms **in a single step**:

> **🧭 Method — One-Step Simplification.**
> To reduce $\dfrac{a}{b}$ to lowest terms, divide both numerator and denominator by their **GCD**:
> $$\frac{a}{b} = \frac{a \div \gcd(a, b)}{b \div \gcd(a, b)}$$

*Example:* Simplify the fraction $\dfrac{132}{420}$ to lowest terms.
We previously calculated $\gcd(420, 132) = 12$:
$$\frac{132}{420} = \frac{132 \div 12}{420 \div 12} = \mathbf{\frac{11}{35}}.$$
Since 11 and 35 share no common factors other than 1, the fraction is guaranteed to be in lowest terms!

---

### 8. Step-by-Step Worked Examples

#### Example 1: Factorization and divisibility
1. Factor the integer $540$ into a product of primes using the division ladder.
2. Write the result using exponent notation.
3. Is 540 divisible by 18? By 24? Justify without performing long division.

*Detailed Solution:*
1. Division ladder:
   - $540 \div 2 = 270$
   - $270 \div 2 = 135$
   - $135 \div 3 = 45$ (since $1+3+5 = 9$)
   - $45 \div 3 = 15$
   - $15 \div 3 = 5$
   - $5 \div 5 = 1$
2. Prime factorization: $540 = 2 \times 2 \times 3 \times 3 \times 3 \times 5 = \mathbf{2^2 \times 3^3 \times 5}$.
3. - For 18: $18 = 2 \times 3^2$. The prime factorization of 540 contains at least one factor of 2 (it has two) and at least two factors of 3 (it has three). Thus **540 is divisible by 18**.
   - For 24: $24 = 2^3 \times 3$. The factorization of 540 contains only $2^2$ (only two factors of 2). It lacks a third 2, so **540 is not divisible by 24**.

---

#### Example 2: The Euclidean algorithm on large numbers
Find the GCD of $1,575$ and $420$ using the Euclidean algorithm.

*Detailed Solution:*
Execute successive Euclidean divisions:
- $1,575 = 420 \times 3 + 315$  (remainder $315 \neq 0$)
- $420 = 315 \times 1 + 105$    (remainder $105 \neq 0$)
- $315 = 105 \times 3 + 0$      (remainder $0$)

The last non-zero remainder is **105**.
Conclusion: $\mathbf{\gcd(1,575, 420) = 105}$.

---

#### Example 3: Comparing subtractions versus divisions
Compute $\gcd(252, 105)$:
1. Using repeated subtractions.
2. Using the Euclidean algorithm.

*Detailed Solution:*
1. **Repeated subtractions:**
   - $252 - 105 = 147$
   - $147 - 105 = 42$
   - $105 - 42 = 63$
   - $63 - 42 = 21$
   - $42 - 21 = 21$
   - $21 - 21 = 0 \implies \mathbf{\gcd = 21}$ (5 subtraction steps).
2. **Euclidean algorithm:**
   - $252 = 105 \times 2 + 42$
   - $105 = 42 \times 2 + 21$
   - $42 = 21 \times 2 + 0 \implies \mathbf{\gcd = 21}$ (2 division steps).
Euclid's division approach is distinctly faster and cleaner!

---

#### Example 4: School fair party bags
For the school carnival, organizers have 280 glow bracelets and 448 collector stickers.
They wish to make identical surprise gift bags containing the exact same number of bracelets and stickers, using all supplies with no leftovers.
1. What is the maximum number of gift bags they can prepare?
2. What will be the contents of each gift bag?

*Detailed Solution:*
1. Let $N$ be the number of gift bags. For supplies to be distributed evenly without leftovers, $N$ must divide both 280 and 448. For $N$ to be maximal, $N = \gcd(448, 280)$.
   Euclidean algorithm:
   - $448 = 280 \times 1 + 168$
   - $280 = 168 \times 1 + 112$
   - $168 = 112 \times 1 + 56$
   - $112 = 56 \times 2 + 0$
   The last non-zero remainder is 56, so $\gcd(448, 280) = 56$.
   They can prepare at most **56 identical gift bags**.
2. Contents per bag:
   - Glow bracelets: $280 \div 56 = \mathbf{5\text{ bracelets}}$.
   - Collector stickers: $448 \div 56 = \mathbf{8\text{ stickers}}$.

---

#### Example 5: Lowest terms and addition of fractions
Consider the fraction $A = \dfrac{1,575}{420}$.
1. Reduce fraction $A$ to lowest terms.
2. Compute the sum $S = \dfrac{1,575}{420} + \dfrac{1}{4}$ as an irreducible fraction.

*Detailed Solution:*
1. From Example 2, $\gcd(1,575, 420) = 105$.
   Divide numerator and denominator by 105:
   $$A = \frac{1,575 \div 105}{420 \div 105} = \mathbf{\frac{15}{4}}.$$
2. Substitute the simplified fraction into the addition:
   $$S = \frac{15}{4} + \frac{1}{4} = \frac{15 + 1}{4} = \frac{16}{4} = \mathbf{4}.$$
   The calculation becomes instantaneous!

---

### Key Takeaways

1. **Foundational Vocabulary:**
   - $a = b \times k \iff a$ is a multiple of $b \iff b$ is a divisor of $a$.
   - **Prime Number**: an integer with exactly 2 distinct divisors (1 and itself). 0 and 1 are NOT prime. The only even prime is 2.

2. **Fundamental Theorem of Arithmetic:**
   - Every integer $\ge 2$ factors uniquely into a product of prime powers ($N = p_1^{\alpha_1} \times p_2^{\alpha_2} \times \dots$).

3. **GCD (Greatest Common Divisor):**
   - The largest integer that divides both numbers evenly.
   - Two numbers are **coprime** if $\gcd(a, b) = 1$.
   - **Prime Factorization Method**: product of all shared prime factors raised to their lowest powers.
   - **Euclidean Algorithm**: chain successive divisions $a = b \times q + r$. The GCD is the **last non-zero remainder**.

4. **Applications:**
   - **Fractions in Lowest Terms**: divide numerator and denominator by their GCD.
   - **Tiling and Equal Batches**: the GCD gives the maximal side length of unbroken square tiles or the maximal number of identical batches without leftovers.

---

### Exercises

#### Level ★: Direct Application

**Exercise 29.1**
From the following list, identify the prime numbers:
$$1 \quad ; \quad 2 \quad ; \quad 9 \quad ; \quad 13 \quad ; \quad 15 \quad ; \quad 21 \quad ; \quad 29 \quad ; \quad 31 \quad ; \quad 51 \quad ; \quad 91$$
For numbers that are not prime, justify by giving a divisor other than 1 and itself.

**Exercise 29.2**
Using divisibility rules, determine whether $3,420$ is divisible by 2, 3, 4, 5, 9, and 10. Justify each case.

**Exercise 29.3**
Find the prime factorizations of the following integers (using exponents where appropriate):
a) $84$
b) $126$
c) $200$
d) $525$

**Exercise 29.4**
Given $84 = 2^2 \times 3 \times 7$ and $126 = 2 \times 3^2 \times 7$:
1. What are the common prime factors of 84 and 126?
2. Compute $\gcd(84, 126)$.
3. Reduce $\dfrac{84}{126}$ to lowest terms.

**Exercise 29.5**
Use the repeated subtraction algorithm to determine $\gcd(65, 39)$.

---

#### Level ★★: Deeper Reflection and Practical Situations

**Exercise 29.6 (Euclidean Algorithm)**
1. Using the Euclidean algorithm, compute $\gcd(756, 441)$, clearly displaying each division step.
2. Are 756 and 441 coprime? Why or why not?
3. Reduce $\dfrac{441}{756}$ to lowest terms in a single step.

**Exercise 29.7 (Tiling the Patio)**
A builder must tile a rectangular patio measuring 5.40 m long by 3.00 m wide.
He wants to use the largest possible identical square slabs without cutting any tiles.
1. Convert the patio dimensions to centimeters.
2. What must be the side length of each tile?
3. How many tiles will be needed in total?

**Exercise 29.8 (The Fair Florist)**
A florist receives a delivery of 168 red roses and 216 white carnations.
She wants to arrange identical bouquets containing the same number of roses and carnations, using all flowers.
1. What is the maximum number of identical bouquets she can create?
2. How many roses and how many carnations will each bouquet contain?

**Exercise 29.9 (The Impostor Prime Trap)**
A student claims: *“All odd numbers greater than 1 are prime, except those ending in 5!”*
Prove that this claim is false by providing at least three distinct counterexamples less than 100.

**Exercise 29.10 (Track Race and Multiples)**
Two go-kart racers cross the starting line simultaneously on a closed circular track.
- The first racer completes a lap in 36 seconds.
- The second racer completes a lap in 48 seconds.
1. Factor 36 and 48 into prime factors.
2. After how much time will both racers cross the starting line together again for the first time?
3. How many laps will each racer have completed?

**Exercise 29.11 (Operations with Reduced Fractions)**
Consider the expression:
$$B = \frac{588}{882} - \frac{1}{6}$$
1. Compute $\gcd(882, 588)$ using the Euclidean algorithm.
2. Deduce the irreducible form of $\dfrac{588}{882}$.
3. Calculate expression $B$, giving the result as an irreducible fraction.

---

#### Level ★★★: Research Challenges and Olympiad-Style Riddles

**Exercise 29.12 (The Farmer's Boundary Fence)**
A farmer owns a triangular field whose three boundaries measure 120 meters, 144 meters, and 168 meters.
He wishes to plant fence posts at equal, regular intervals around the perimeter, with a post positioned at each vertex of the triangle.
To minimize expenses, he wants to use the **fewest possible fence posts**.
1. What must be the constant distance between consecutive posts?
2. How many posts must he plant in total around the fence?

**Exercise 29.13 (Euclid's Proof of the Infinitude of Primes)**
Euclid proved that the set of prime numbers is infinite using an elegant proof by contradiction.
Assume there are only finitely many primes: denote them all as $p_1, p_2, p_3, \dots, p_n$.
Consider the integer $N$ constructed by multiplying all these primes together and adding 1:
$$N = (p_1 \times p_2 \times p_3 \times \dots \times p_n) + 1$$
1. If you divide $N$ by any of the primes $p_1, p_2, \dots, p_n$, what is the remainder?
2. Can $N$ be divisible by any prime in the list?
3. Conclude: why does this produce a contradiction, and why must there be infinitely many prime numbers?

**Exercise 29.14 (Gear Meshing)**
Cogwheel $A$ with 54 teeth drives cogwheel $B$ with 42 teeth. Two designated teeth, one on each wheel, touch at the initial starting position.
1. Calculate $\gcd(54, 42)$.
2. After how many tooth contacts will these exact two teeth touch again for the first time?
3. How many complete revolutions will each wheel have made?

**Exercise 29.15 (Cube Packing in a 3D Rectangular Solid)**
A sculptor has a solid rectangular block of marble measuring 90 cm long, 75 cm wide, and 60 cm high.
He wants to slice this block into identical cubes of maximal size, without wasting any marble.
1. Factor 90, 75, and 60 into prime factors.
2. What is the Greatest Common Divisor of all three numbers?
3. What is the edge length of each cube?
4. How many cubes will the sculptor obtain?

---

### Solutions

#### Level ★

- **Solution 29.1:**
  - Primes: **2, 13, 29, 31**.
  - Non-primes:
    - 1 is not prime (only one divisor).
    - 9 is divisible by 3 ($9 = 3 \times 3$).
    - 15 is divisible by 3 and 5 ($15 = 3 \times 5$).
    - 21 is divisible by 3 and 7 ($21 = 3 \times 7$).
    - 51 is divisible by 3 ($5 + 1 = 6$; $51 = 3 \times 17$).
    - 91 is divisible by 7 ($91 = 7 \times 13$).
- **Solution 29.2:** For 3,420:
  - Divisible by 2: yes, ends in 0 (even).
  - Divisible by 3: yes, $3+4+2+0 = 9$, multiple of 3.
  - Divisible by 4: yes, last two digits 20 divisible by 4.
  - Divisible by 5: yes, ends in 0.
  - Divisible by 9: yes, digit sum 9 divisible by 9.
  - Divisible by 10: yes, ends in 0.
- **Solution 29.3:**
  a) $84 = 2^2 \times 3 \times 7$.
  b) $126 = 2 \times 3^2 \times 7$.
  c) $200 = 2^3 \times 5^2$.
  d) $525 = 3 \times 5^2 \times 7$.
- **Solution 29.4:**
  1. Shared prime factors: 2, 3, and 7.
  2. $\gcd(84, 126) = 2^1 \times 3^1 \times 7^1 = \mathbf{42}$.
  3. $\dfrac{84}{126} = \dfrac{84 \div 42}{126 \div 42} = \mathbf{\dfrac{2}{3}}$.
- **Solution 29.5:** Subtractions: $65 - 39 = 26 \implies 39 - 26 = 13 \implies 26 - 13 = 13 \implies 13 - 13 = 0$. Thus $\gcd(65, 39) = \mathbf{13}$.

---

#### Level ★★

- **Solution 29.6 (Euclidean Algorithm):**
  1. Divisions:
     - $756 = 441 \times 1 + 315$
     - $441 = 315 \times 1 + 126$
     - $315 = 126 \times 2 + 63$
     - $126 = 63 \times 2 + 0$
     Last non-zero remainder is 63, so $\mathbf{\gcd(756, 441) = 63}$.
  2. Not coprime because $\gcd = 63 \neq 1$.
  3. Reduced fraction: $\dfrac{441}{756} = \dfrac{441 \div 63}{756 \div 63} = \mathbf{\dfrac{7}{12}}$.

- **Solution 29.7 (Patio Tiling):**
  1. $L = 5.40\text{ m} = 540\text{ cm}$, $W = 3.00\text{ m} = 300\text{ cm}$.
  2. Tile side length is $\gcd(540, 300)$:
     - $540 = 300 \times 1 + 240$
     - $300 = 240 \times 1 + 60$
     - $240 = 60 \times 4 + 0$
     $\gcd = 60$. Tiles must measure **$60\text{ cm} \times 60\text{ cm}$**.
  3. Tile count:
     - Along length: $540 \div 60 = 9$ tiles.
     - Along width: $300 \div 60 = 5$ tiles.
     - Total: $9 \times 5 = \mathbf{45\text{ tiles}}$.

- **Solution 29.8 (Florist):**
  1. Maximum bouquets $= \gcd(216, 168)$:
     - $216 = 168 \times 1 + 48$
     - $168 = 48 \times 3 + 24$
     - $48 = 24 \times 2 + 0$
     $\gcd = 24$. She can assemble at most **24 bouquets**.
  2. Contents:
     - Roses: $168 \div 24 = \mathbf{7\text{ red roses}}$.
     - Carnations: $216 \div 24 = \mathbf{9\text{ white carnations}}$.

- **Solution 29.9 (Counterexamples):**
  - $9$ ($9 = 3 \times 3$, odd, not prime);
  - $21$ ($21 = 3 \times 7$);
  - $27$ ($27 = 3 \times 9$);
  - $91$ ($91 = 7 \times 13$, famous composite trap!).

- **Solution 29.10 (Track Race):**
  1. $36 = 2^2 \times 3^2$ and $48 = 2^4 \times 3$.
  2. First common meeting is the LCM (Least Common Multiple):
     $$\text{LCM}(36, 48) = 2^4 \times 3^2 = 16 \times 9 = \mathbf{144\text{ seconds}} = 2\text{ minutes and } 24\text{ seconds}.$$
  3. Laps:
     - Racer 1: $144 \div 36 = \mathbf{4\text{ laps}}$.
     - Racer 2: $144 \div 48 = \mathbf{3\text{ laps}}$.

- **Solution 29.11 (Fractions):**
  1. $\gcd(882, 588)$:
     - $882 = 588 \times 1 + 294$
     - $588 = 294 \times 2 + 0 \implies \gcd = \mathbf{294}$.
  2. Irreducible fraction: $\dfrac{588}{882} = \dfrac{588 \div 294}{882 \div 294} = \mathbf{\dfrac{2}{3}}$.
  3. $B = \frac{2}{3} - \frac{1}{6} = \frac{4}{6} - \frac{1}{6} = \frac{3}{6} = \mathbf{\frac{1}{2}}$.

---

#### Level ★★★

- **Solution 29.12 (Fence Posts):**
  1. Post interval $d$ must divide 120, 144, and 168. To minimize posts, $d = \gcd(120, 144, 168)$.
     - $\gcd(120, 144) = 24$.
     - Since $168 = 24 \times 7$, $\gcd(120, 144, 168) = \mathbf{24\text{ meters}}$.
  2. Perimeter $= 120 + 144 + 168 = 432\text{ meters}$.
     In a closed perimeter, total posts $= \frac{432}{24} = \mathbf{18\text{ posts}}$.

- **Solution 29.13 (Euclid's Infinitude of Primes):**
  1. $N = (p_1 \times p_2 \times \dots \times p_n) + 1$. The product is an exact multiple of any listed prime $p_k$. Thus dividing $N$ by $p_k$ leaves a remainder of **1**.
  2. Since the remainder is 1, $N$ is divisible by **none** of the primes in the list.
  3. By the Fundamental Theorem of Arithmetic, $N > 1$ must have at least one prime factor. That prime factor cannot be in the list, contradicting the assumption that the list contained all primes. Hence, there are infinitely many prime numbers.

- **Solution 29.14 (Gears):**
  1. $\gcd(54, 42) = \mathbf{6}$.
  2. Tooth contacts equal the LCM:
     $$\text{LCM}(54, 42) = \frac{54 \times 42}{\gcd(54, 42)} = \frac{2,268}{6} = \mathbf{378\text{ tooth contacts}}.$$
  3. Revolutions:
     - Wheel A: $378 \div 54 = \mathbf{7\text{ full turns}}$.
     - Wheel B: $378 \div 42 = \mathbf{9\text{ full turns}}$.

- **Solution 29.15 (3D Marble Cubes):**
  1. Factorizations:
     - $90 = 2 \times 3^2 \times 5$
     - $75 = 3 \times 5^2$
     - $60 = 2^2 \times 3 \times 5$
  2. Common prime factors: 3 and 5. $\gcd(90, 75, 60) = 3 \times 5 = \mathbf{15}$.
  3. Cube edge length is **$15\text{ cm}$**.
  4. Number of cubes:
     - Length: $90 \div 15 = 6$
     - Width: $75 \div 15 = 5$
     - Height: $60 \div 15 = 4$
     Total: $6 \times 5 \times 4 = \mathbf{120\text{ cubes}}$.

---

### The Question Opening the Next Chapter

Through Euclid's arithmetic, everything is governed with absolute certainty: every stone finds its place, every share divides evenly, every calculation is rock solid.
Yet our real world is not merely composed of sealed chests and square marble slabs.

What happens when the mist of the future rises, when dice roll across an innkeeper's table, or when a caravan master must choose between two perilous routes? Can one calculate rationally in the face of uncertainty?
Journey into the desert and the salons of 17th-century thinkers: we will learn to master the **roulette of fate** in Chapter 30: **The Roulette of Fate and the Hunter's Survival**.
