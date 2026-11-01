# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)
## CHAPTER 18: The Grain of Rice on the Chessboard

> *“Addition is the slow step of the walker advancing stone by stone. Multiplication is the gallop of the horseman. But exponentiation is the dazzling ascent of the rocket: in a few beats of its wings, it outstrips the comprehension of kings and fills the entire cosmos.”*

---

### What You Are About to Discover

- The ancient Indian legend of sage **Sissa** and the unstoppable avalanche of rice grains across the chessboard.
- The universal **order of operations** (PEMDAS): why without strict rules of the road, no two mathematicians would ever agree on a calculation.
- **Exponential notation**: how to compress giant repeated multiplications into a tiny raised exponent ($a^n$).
- The secrets of **powers of 10** and **negative exponents** ($10^{-n} = \frac{1}{10^n}$).
- The four golden rules for multiplying, dividing, and raising powers without ever getting tangled.
- **Scientific notation** and the exploration of scales, from the subatomic nucleus to the edge of the observable universe.
- 🛠️ The Boundary Case Laboratory: exponents of zero ($a^0 = 1$), the indeterminate mystery of $0^0$, and Kasner's Googolplex.

---

### 1. The Problem: The Reckless Promise of King Belkib

More than fifteen hundred years ago, in a magnificent palace in northern India, lived a powerful king named Belkib (or Shirham). Despite all his riches, armies, and palaces, the monarch suffered from profound boredom. No banquet, no dance performance, and no cavalry tournament could dispel his heavy melancholy.

One afternoon, a wise court scholar named **Sissa** appeared before the throne carrying a carved ebony box. From it, he drew a game board of 64 alternating black and white squares, accompanied by two armies of carved wooden figurines: kings, horses, towers, and foot soldiers. It was the game of chess (then called *Chaturanga*).

The king was instantly mesmerized. For weeks on end, he studied strategies, shielded his king, and sacrificed pawns. Cured of his sorrow, he summoned Sissa before the entire assembled court:  
*“Sissa, your invention is sublime! Name any reward you desire, be it half the gold in my royal treasuries or my grandest marble palace, and it shall be yours!”*

Sissa bowed with humble grace:  
*“Great King, I am merely a modest scholar. I seek neither gold coins nor glittering jewels. Place your chessboard before you:*
- *Place **1 grain of rice** upon the first square.*
- *Place **2 grains of rice** upon the second square.*
- *Place **4 grains of rice** upon the third square.*
- *And double the number of grains on each subsequent square until the sixty-fourth square is reached.*  
*Grant me simply these few grains of rice, and my heart will be content.”*

```
     1st square     2nd square     3rd square     4th square     ...        64th square
        ┌───┐          ┌───┐          ┌───┐          ┌───┐                     ┌───┐
        │ • │          │•• │          │••••│         │••••│                    │ ? │
        └───┘          └───┘          └───┘          │••••│                    └───┘
       1 grain        2 grains       4 grains       8 grains                 2⁶³ grains!
```

The king burst into hearty laughter:  
*“What foolish modesty! You could have asked for a royal fortune, and you ask for bird food! Fetch a sack of rice from the royal granaries and pay this humble man at once!”*

Yet that evening, the king's chief royal treasurer returned pale, trembling, and bowing to the marble floor:  
*“Your Majesty… we have emptied every granary in the palace, every silo in the imperial city, and we could not even cover the thirtieth square! To fulfill Sissa's request, every harvest produced across the entire Earth for over two thousand years would not suffice!”*

How could the simple act of doubling a quantity 63 times in succession produce a mountain of grain larger than planet Earth itself? That is the staggering power of **exponential growth and powers**.

---

### 2. The Order of Operations: Who Takes Command in a Calculation?

Before handling colossal powers, we need an unambiguous navigational compass. Consider this disarmingly simple arithmetic expression:

$$2 + 3 \times 5$$

If you pose this question to random people on the street:
- The first computes strictly from left to right: $2 + 3 = 5$, followed by $5 \times 5 = \mathbf{25}$.
- The second performs the multiplication first: $3 \times 5 = 15$, followed by $2 + 15 = \mathbf{17}$.

Who is correct? $25$ or $17$?

In nature and physical life, this is not a matter of subjective opinion! Imagine visiting the market: you purchase 1 apple for \$2, and 3 bags of sweets for \$5 each. How much do you owe?  
You pay $2 + 15 = \$17$, not \$25! Multiplication binds objects into indivisible packets.

To ensure that every engineer, scientist, and computer program across the globe computes the exact same value without ambiguity, mathematicians established an international code of the road: the **order of operations**.

#### 2.1 The PEMDAS Hierarchy

Mathematicians memorize this operational hierarchy using the mnemonic **PEMDAS**:

```
                  ┌──────────────────────────────────────────┐
                  │ 1. P : PARENTHESES (innermost first)     │
                  ├──────────────────────────────────────────┤
                  │ 2. E : EXPONENTS (Powers & Roots)        │
                  ├──────────────────────────────────────────┤
                  │ 3. M / D : MULTIPLICATION & DIVISION     │
                  │    (tied in rank, evaluated left to right│
                  ├──────────────────────────────────────────┤
                  │ 4. A / S : ADDITION & SUBTRACTION        │
                  │    (tied in rank, evaluated left to right│
                  └──────────────────────────────────────────┘
```

> **📐 Official Rule — Operational Precedence**  
> 1. Always evaluate expressions inside **parentheses** first, working from the innermost brackets outward.  
> 2. Evaluate all **exponents** (powers).  
> 3. Perform all **multiplications and divisions** in order from left to right.  
> 4. Perform all **additions and subtractions** in order from left to right.

#### 2.2 The Role of the Horizontal Fraction Bar

A horizontal fraction bar acts as an invisible set of parentheses enclosing everything above it (the numerator) and everything below it (the denominator):
$$\frac{8 + 12}{2 + 3} = \frac{(8 + 12)}{(2 + 3)} = \frac{20}{5} = 4$$

---

### 3. Exponential Notation: Compressing Multiplication

Let us revisit Sissa's chessboard:
- Square 1: $1$
- Square 2: $2$
- Square 3: $2 \times 2 = 4$
- Square 4: $2 \times 2 \times 2 = 8$
- Square 5: $2 \times 2 \times 2 \times 2 = 16$

For the 10th square, we must write the digit 2 multiplied by itself ten times. For the 64th square, we would have to write a line of sixty-three consecutive 2's! That is painfully tedious and unreadable.

In the 17th century, the French philosopher and mathematician **René Descartes** introduced a brilliant typographic invention: writing the number of repeated factors in tiny script perched high to the upper right of the number.

> **📐 Definition — Power of a Number**  
> For any real number $a$ and any positive integer $n \ge 1$:
> $$a^n = \underbrace{a \times a \times a \times \dots \times a}_{n \text{ factors}}$$
> - $a$ is called the **base**.  
> - $n$ is called the **exponent** (or power).  
> - The notation $a^n$ reads aloud as **“$a$ to the power of $n$”** or **“$a$ raised to the $n$-th power”**.

#### Special Terminology for Powers of 2 and 3
- $a^2$ reads as **“$a$ squared”** (representing the geometric area of a square of side $a$).
- $a^3$ reads as **“$a$ cubed”** (representing the geometric volume of a cube of edge $a$).

#### Vital Special Cases: Exponent 1 and Exponent 0
- **Exponent 1:** $a^1 = a$ (a single factor).
- **Exponent 0:** For any non-zero base $a \neq 0$:
  $$a^0 = 1$$

*Why is $a^0 = 1$?* Observe the clean pattern of descending division by 2 at each step:
$$2^3 = 8 \xrightarrow{\div 2} 2^2 = 4 \xrightarrow{\div 2} 2^1 = 2 \xrightarrow{\div 2} 2^0 = \mathbf{1}$$
Defining $a^0 = 1$ is the only logically coherent way to preserve the rules of arithmetic!

#### How Many Grains on the Entire Chessboard?
On the 64th square alone, there sit:
$$2^{63} \approx 9.22 \times 10^{18} \text{ grains}$$
And the grand total across all 64 squares equals:
$$2^0 + 2^1 + 2^2 + \dots + 2^{63} = 2^{64} - 1 = \mathbf{18,446,744,073,709,551,615} \text{ grains!}$$
That is over **18 quintillion grains of rice**! If spread evenly across the entire surface of France, the country would be buried beneath a mountain of rice over one meter deep.

---

### 4. Powers of 10 and Negative Exponents

The number $10$ is the sovereign ruler of our decimal system (inherited from our ten human fingers). Powers of 10 are the supreme engine of modern scientific calculation.

#### 4.1 Positive Powers of 10: The March of Zeros

> **📐 Rule — Positive Powers of 10**  
> For any positive integer $n$:
> $$10^n = 1\underbrace{000\dots0}_{n \text{ zeros}}$$
> The exponent indicates **the exact number of zeros** following the leading digit 1!

- $10^1 = 10$ (ten)
- $10^2 = 100$ (one hundred)
- $10^3 = 1,000$ (one thousand, metric prefix *kilo-*)
- $10^6 = 1,000,000$ (one million, metric prefix *mega-*)
- $10^9 = 1,000,000,000$ (one billion, metric prefix *giga-*)
- $10^{12} = 1,000,000,000,000$ (one trillion, metric prefix *tera-*)

#### 4.2 Negative Exponents: Journey into the Infinitesimal

Let us continue stepping down our arithmetic ladder by dividing by 10 at each successive step:

$$\begin{aligned}
10^3 &= 1,000 \\
10^2 &= 100 \\
10^1 &= 10 \\
10^0 &= 1 \\
10^{-1} &= \frac{1}{10} = 0.1 \\
10^{-2} &= \frac{1}{10^2} = \frac{1}{100} = 0.01 \\
10^{-3} &= \frac{1}{10^3} = \frac{1}{1,000} = 0.001
\end{aligned}$$

> **📐 Definition — Negative Exponents**  
> For any non-zero base $a \neq 0$ and any integer $n$:
> $$a^{-n} = \frac{1}{a^n}$$
> Specifically for powers of 10:
> $$10^{-n} = \frac{1}{10^n} = \underbrace{0.00\dots0}_{n \text{ total zeros}}1$$
> A negative exponent designates the **reciprocal** of the power. In $10^{-n}$, there are **$n$ zeros in total**, including the leading zero before the decimal point!

- $10^{-1} = 0.1$ (one tenth, prefix *deci-*)
- $10^{-2} = 0.01$ (one hundredth, prefix *centi-*)
- $10^{-3} = 0.001$ (one thousandth, prefix *milli-*)
- $10^{-6} = 0.000001$ (one millionth, prefix *micro-*)
- $10^{-9} = 0.000000001$ (one billionth, prefix *nano-*)

---

### 5. The Golden Rules of Exponent Arithmetic

When manipulating powers with the same base, computation transforms magically: **multiplication of powers becomes simple addition of exponents!**

> **📐 Fundamental Exponent Laws**  
> For all integers $m$ and $n$, and non-zero bases $a$ and $b$:
>  
> 1. **Product of Powers with Same Base:**  
>    $$a^m \times a^n = a^{m+n}$$  
>    *(Example: $10^3 \times 10^4 = 10^{3+4} = 10^7$)*  
>  
> 2. **Quotient of Powers with Same Base:**  
>    $$\frac{a^m}{a^n} = a^{m-n}$$  
>    *(Example: $\frac{10^7}{10^2} = 10^{7-2} = 10^5$; $\frac{10^3}{10^8} = 10^{3-8} = 10^{-5}$)*  
>  
> 3. **Power of a Power:**  
>    $$(a^m)^n = a^{m \times n}$$  
>    *(Example: $(10^3)^4 = 10^{3 \times 4} = 10^{12}$)*  
>  
> 4. **Power of a Product:**  
>    $$(a \times b)^n = a^n \times b^n$$  
>    *(Example: $(2 \times 5)^3 = 2^3 \times 5^3 = 8 \times 125 = 1,000 = 10^3$)*

---

### 6. Scientific Notation: Writing the Universe

How can one compare the mass of a single hydrogen atom ($0.00000000000000000000000000167\text{ kg}$) to the mass of planet Earth ($5,972,000,000,000,000,000,000,000\text{ kg}$)?  
With standard digits, human eyes lose count of the zeros instantly!  
Scientists therefore established an international standard format: **scientific notation**.

> **📐 Definition — Scientific Notation**  
> A number is written in **scientific notation** when formatted strictly as:
> $$a \times 10^n$$
> where:
> - $a$ is a decimal number with **exactly one non-zero digit before the decimal point** ($1 \le a < 10$ or $-10 < a \le -1$).  
> - $n$ is an integer (positive, zero, or negative).

#### Rapid Conversion Technique
- For large numbers ($> 10$): shift the decimal point $n$ places to the **left** $\implies 10^{+n}$.  
  $$149,600,000\text{ km} = 1.496 \times 10^8\text{ km} \quad (\text{Earth-Sun distance})$$
- For small numbers ($< 1$): shift the decimal point $n$ places to the **right** $\implies 10^{-n}$.  
  $$0.00000012\text{ m} = 1.2 \times 10^{-7}\text{ m} \quad (\text{size of a virus})$$

```
       Scale of Magnitudes Across the Universe (in meters)
    10⁻¹⁵ m      10⁻¹⁰ m       1 m        10⁶ m       10¹¹ m        10²¹ m
       |────────────|───────────|───────────|───────────|─────────────|
     Atomic       Atom        Human       Earth       Solar        Milky Way
     nucleus                                         system         Galaxy
```

---

### 7. Beware of Pitfalls!

> **⚠️ Warning: Monumental Exponent Blunders!**  
> 1. **The Phantom Exponent Addition Trap:**  
>    $$10^2 + 10^3 \neq 10^5 \quad !$$  
>    Powers can NEVER be added by adding their exponents!  
>    $10^2 + 10^3 = 100 + 1,000 = 1,100$, whereas $10^5 = 100,000$.  
> 2. **The Minus Sign and Parentheses Trap:**  
>    $$-3^2 = -(3 \times 3) = \mathbf{-9}$$  
>    $$(-3)^2 = (-3) \times (-3) = \mathbf{+9}$$  
>    Without grouping parentheses, the exponent applies ONLY to the base number 3, not to the preceding minus sign!  
> 3. **Non-Standard Scientific Format:**  
>    - $35 \times 10^4$ is **not** in scientific notation because $35 \ge 10$ (must be written $3.5 \times 10^5$).  
>    - $0.7 \times 10^{-3}$ is **not** in scientific notation because $0.7 < 1$ (must be written $7 \times 10^{-4}$).  
> 4. **Multiplying Bases Instead of Adding Exponents:**  
>    $$2^3 \times 2^4 \neq 4^7 \quad \text{correct is} \quad 2^{3+4} = 2^7 = 128$$

---

### 8. Solved Examples

#### Solved Example 1 — Evaluating with Order of Operations
Calculate the exact value of the following expression, detailing every intermediate step:
$$A = 5 + 3 \times (4^2 - 6) - \frac{24}{2^3}$$

*Solution:*  
Apply PEMDAS rigorously:
1. Inside parentheses:
   - Exponent first: $4^2 = 16$.
   - Subtraction: $16 - 6 = 10$.  
   Expression becomes: $A = 5 + 3 \times 10 - \frac{24}{2^3}$.
2. Exponent in denominator:
   - $2^3 = 2 \times 2 \times 2 = 8$.  
   Expression becomes: $A = 5 + 3 \times 10 - \frac{24}{8}$.
3. Multiplications and divisions:
   - $3 \times 10 = 30$.
   - $\frac{24}{8} = 3$.  
   Expression becomes: $A = 5 + 30 - 3$.
4. Additions and subtractions from left to right:
   - $5 + 30 = 35$, then $35 - 3 = 32$.  
Conclusion: $A = 32$. ✔

#### Solved Example 2 — Simplifying Powers of 10
Write as a single power of 10:
$$B = \frac{10^5 \times (10^{-2})^3}{10^{-4}}$$

*Solution:*  
1. Power of a power in numerator:  
   $$(10^{-2})^3 = 10^{-2 \times 3} = 10^{-6}$$
2. Product in numerator (add exponents):  
   $$10^5 \times 10^{-6} = 10^{5 + (-6)} = 10^{-1}$$
3. Division (subtract denominator exponent):  
   $$B = \frac{10^{-1}}{10^{-4}} = 10^{-1 - (-4)} = 10^{-1 + 4} = 10^3$$  
Conclusion: $B = 10^3 = 1,000$. ✔

#### Solved Example 3 — Converting to Scientific Notation
Write in standard scientific notation:
1. $C = 548,000,000$ (continental population)  
2. $D = 0.000037\text{ m}$ (microscopic fiber diameter)  
3. $E = 485 \times 10^6$  
4. $F = 0.029 \times 10^{-4}$

*Solution:*  
1. Move decimal 8 places left: $C = 5.48 \times 10^8$.  
2. Move decimal 5 places right: $D = 3.7 \times 10^{-5}\text{ m}$.  
3. $E = (4.85 \times 10^2) \times 10^6 = 4.85 \times 10^{2+6} = 4.85 \times 10^8$.  
4. $F = (2.9 \times 10^{-2}) \times 10^{-4} = 2.9 \times 10^{-2 + (-4)} = 2.9 \times 10^{-6}$. ✔

#### Solved Example 4 — Astrophysical Travel Time
Light travels through vacuum at speed $v = 3 \times 10^8\text{ m/s}$.  
Mean Earth-Sun distance is $d = 1.5 \times 10^{11}\text{ meters}$.  
How long does a photon take to travel from Sun to Earth?

*Solution:*  
Using $t = \frac{d}{v}$:
$$t = \frac{1.5 \times 10^{11}}{3 \times 10^8} = \left(\frac{1.5}{3}\right) \times 10^{11-8} = 0.5 \times 10^3\text{ seconds}$$
Convert to standard decimal:
$$t = 0.5 \times 1,000 = 500\text{ seconds}$$
In minutes and seconds ($1\text{ min} = 60\text{ s}$):
$$500 = 8 \times 60 + 20$$
Sunlight takes **8 minutes and 20 seconds** to reach Earth! ✔

#### Solved Example 5 — The Folded Sheet of Paper
A sheet of notebook paper has thickness $t = 0.1\text{ mm} = 10^{-4}\text{ m}$.  
Each fold doubles its thickness.  
1. What is its thickness after 10 folds?  
2. What would its thickness be after 42 folds?

*Solution:*  
1. After 10 folds: thickness scales by $2^{10} = 1,024 \approx 10^3$.  
   $$\text{Thickness} = 0.1\text{ mm} \times 1,024 = 102.4\text{ mm} \approx 10.24\text{ cm}$$  
2. After 42 folds:  
   $$\text{Thickness} = 10^{-4}\text{ m} \times 2^{42}$$  
   $2^{42} = (2^{10})^4 \times 2^2 \approx (1,000)^4 \times 4 = 4 \times 10^{12}$.  
   $$\text{Thickness} \approx 10^{-4}\text{ m} \times (4.398 \times 10^{12}) \approx 4.4 \times 10^8\text{ m} = 440,000\text{ km}!$$  
The mean distance from Earth to the Moon is $384,400\text{ km}$.  
A piece of paper folded 42 times reaches past the Moon! ✔

---

### What You Must Remember

1. **Order of Operations (PEMDAS):**  
   Parentheses $\to$ Exponents $\to$ Multiplication & Division (left to right) $\to$ Addition & Subtraction (left to right).
2. **Definition of Powers:**  
   $a^n = \underbrace{a \times a \times \dots \times a}_{n \text{ times}}$; $a^1 = a$; $a^0 = 1$ ($a \neq 0$).
3. **Negative Exponents:**  
   $a^{-n} = \frac{1}{a^n}$; $10^{-n} = \frac{1}{10^n} = 0.00\dots01$ ($n$ total zeros).
4. **Exponent Calculation Rules:**  
   - $a^m \times a^n = a^{m+n}$  
   - $\frac{a^m}{a^n} = a^{m-n}$  
   - $(a^m)^n = a^{m \times n}$  
   - $(a \times b)^n = a^n \times b^n$
5. **Scientific Notation:**  
   Standard format: $a \times 10^n$ with $1 \le a < 10$ (exactly one non-zero digit before the decimal point).

---

### Exercises

#### Level ★ (Direct Application)

**Exercise 1.** Evaluate numerical expressions:  
1. $A = 7 + 3 \times 4$  
2. $B = (7 + 3) \times 4$  
3. $C = 20 - 4 \times 2 + 1$  
4. $D = 30 / 5 \times 2$

**Exercise 2.** Compute without a calculator:  
$2^4$; $3^3$; $5^2$; $10^5$; $7^0$; $(-2)^3$; $(-2)^4$; $-5^2$.

**Exercise 3.** Write in decimal notation:  
$10^3$; $10^{-2}$; $10^{-5}$; $4.2 \times 10^3$; $7 \times 10^{-4}$.

**Exercise 4.** Express as a single power of 10:  
1. $10^4 \times 10^7$  
2. $\frac{10^9}{10^3}$  
3. $(10^5)^2$  
4. $10^{-3} \times 10^{-5}$  
5. $\frac{10^2}{10^{-4}}$

**Exercise 5.** Which of the following numbers are written in valid scientific notation?  
a) $3.45 \times 10^7$; b) $0.4 \times 10^{-3}$; c) $12 \times 10^5$; d) $9.99 \times 10^{-1}$; e) $1 \times 10^0$.

#### Level ★★ (Reasoning and Rules)

**Exercise 6.** Compute following strict operational precedence:  
1. $G = 3 \times 2^3 - 4 \times (5 - 2^2)$  
2. $H = \frac{5^2 - 3^2}{2^4 - 2 \times 4}$

**Exercise 7.** Express in the form $a^n$ ($a$ integer, $n$ relative integer):  
1. $2^5 \times 2^3 \times 2^{-4}$  
2. $\frac{3^8}{(3^2)^3}$  
3. $\frac{7^3 \times 7^{-5}}{7^{-4}}$  
4. $8 \times 2^5$ *(Hint: rewrite 8 as a power of 2)*.

**Exercise 8.** Express in scientific notation:  
1. Red blood cell diameter: $0.000007\text{ m}$.  
2. Speed of light: $300,000,000\text{ m/s}$.  
3. Human world population: $8,100,000,000\text{ people}$.  
4. Mass of a single water droplet: $0.00005\text{ kg}$.

**Exercise 9.** Compute and give final answers in scientific notation:  
1. $K = (3 \times 10^4) \times (5 \times 10^7)$  
2. $L = \frac{8 \times 10^{-3}}{4 \times 10^5}$  
3. $M = \frac{1.2 \times 10^5 \times 7 \times 10^{-2}}{2.4 \times 10^{-6}}$

**Exercise 10. Bacterial Explosion.**  
A culture of bacteria is placed in a warm nutrient dish.  
At noon ($t = 0$), there are $1,000$ bacteria ($10^3$).  
The colony doubles every 20 minutes.  
1. How many bacteria exist at 1:00 PM?  
2. How many bacteria exist at 4:00 PM? Express in scientific notation.

**Exercise 11. Sorting Without Calculating.**  
Order from least to greatest without full decimal expansion:  
$$A = 4.5 \times 10^6 \quad ; \quad B = 8.2 \times 10^5 \quad ; \quad C = 1.1 \times 10^7 \quad ; \quad D = 9.9 \times 10^5$$

#### Level ★★★ (Challenges and Astronomical Scales)

**Exercise 12. The Googol and the Googolplex.**  
In 1920, American mathematician Edward Kasner asked his 9-year-old nephew Milton Sirotta to invent a name for 1 followed by 100 zeros. The boy replied: “A GOOGOL!” (which later inspired the name of the search engine *Google*).  
1. Write a googol as a power of 10.  
2. The total number of subatomic particles in the observable universe is estimated at $10^{80}$. How many times larger is a googol than the particle count of the cosmos?  
3. Kasner then defined a *Googolplex*: 1 followed by a googol of zeros! Write a Googolplex using powers of 10. Why is it physically impossible to write this number down in our universe?

**Exercise 13. Voyager 1 Interstellar Mission.**  
Spacecraft *Voyager 1* speeds through deep space at $17\text{ km/s}$ ($\approx 6.12 \times 10^4\text{ km/h}$).  
It heads toward Proxima Centauri, located $4.24\text{ light-years}$ away.  
One light-year is approximately $9.46 \times 10^{12}\text{ km}$.  
1. Compute the distance to Proxima Centauri in kilometers in scientific notation.  
2. How many hours, then years, will the probe take to cover this distance?

**Exercise 14. Algebraic Exponent Simplification.**  
For non-zero real numbers $x$ and $y$, simplify:  
$$Z = \frac{(x^2 y^{-3})^4 \times (x^{-1} y)^2}{x^5 y^{-8}}$$

**Exercise 15. The Geometric Series of Halves.**  
Compute the exact fraction:  
$$S = \frac{1}{2^1} + \frac{1}{2^2} + \frac{1}{2^3} + \frac{1}{2^4} + \frac{1}{2^5} + \frac{1}{2^6}$$  
What do you observe about its relation to the number 1? What would the sum equal if continued infinitely?

---

### Solutions

**Exercise 1.**  
1. $A = 7 + 12 = 19$.  
2. $B = 10 \times 4 = 40$.  
3. $C = 20 - 8 + 1 = 13$.  
4. $D = (30 / 5) \times 2 = 6 \times 2 = 12$.

**Exercise 2.**  
$2^4 = 16$; $3^3 = 27$; $5^2 = 25$; $10^5 = 100,000$; $7^0 = 1$.  
$(-2)^3 = -8$; $(-2)^4 = +16$; $-5^2 = -(5 \times 5) = -25$.

**Exercise 3.**  
$10^3 = 1,000$; $10^{-2} = 0.01$; $10^{-5} = 0.00001$;  
$4.2 \times 10^3 = 4,200$; $7 \times 10^{-4} = 0.0007$.

**Exercise 4.**  
1. $10^4 \times 10^7 = 10^{11}$.  
2. $\frac{10^9}{10^3} = 10^6$.  
3. $(10^5)^2 = 10^{10}$.  
4. $10^{-3} \times 10^{-5} = 10^{-8}$.  
5. $\frac{10^2}{10^{-4}} = 10^{2 - (-4)} = 10^6$.

**Exercise 5.**  
- a) Yes ($1 \le 3.45 < 10$).  
- b) No ($0.4 < 1$).  
- c) No ($12 \ge 10$).  
- d) Yes ($1 \le 9.99 < 10$).  
- e) Yes ($1 \le 1 < 10$).

**Exercise 6.**  
1. $G = 3 \times 8 - 4 \times (5 - 4) = 24 - 4 \times 1 = 20$.  
2. $H = \frac{25 - 9}{16 - 8} = \frac{16}{8} = 2$.

**Exercise 7.**  
1. $2^{5 + 3 - 4} = 2^4$.  
2. $\frac{3^8}{3^6} = 3^{8-6} = 3^2$.  
3. $\frac{7^{-2}}{7^{-4}} = 7^{-2 - (-4)} = 7^2$.  
4. $8 = 2^3 \implies 2^3 \times 2^5 = 2^8$.

**Exercise 8.**  
1. $7 \times 10^{-6}\text{ m}$.  
2. $3 \times 10^8\text{ m/s}$.  
3. $8.1 \times 10^9\text{ people}$.  
4. $5 \times 10^{-5}\text{ kg}$.

**Exercise 9.**  
1. $K = 15 \times 10^{11} = 1.5 \times 10^{12}$.  
2. $L = 2 \times 10^{-3-5} = 2 \times 10^{-8}$.  
3. $M = \left(\frac{8.4}{2.4}\right) \times 10^{3 - (-6)} = 3.5 \times 10^9$.

**Exercise 10.**  
1. In 1 hour (3 periods of 20 min): $N_1 = 1,000 \times 2^3 = 8,000\text{ bacteria}$.  
2. In 4 hours (12 periods of 20 min): $N_2 = 10^3 \times 2^{12} = 10^3 \times 4,096 = 4.096 \times 10^6\text{ bacteria}$.

**Exercise 11.**  
Exponent 5: $B = 8.2 \times 10^5$ and $D = 9.9 \times 10^5 \implies B < D$.  
Exponent 6: $A = 4.5 \times 10^6$.  
Exponent 7: $C = 1.1 \times 10^7$.  
Ascending order: $B < D < A < C$.

**Exercise 12.**  
1. $1\text{ googol} = 10^{100}$.  
2. $\frac{10^{100}}{10^{80}} = 10^{20}$. A googol is **one hundred quintillion times larger** than the particle count of the entire cosmos!  
3. $1\text{ googolplex} = 10^{\text{googol}} = 10^{10^{100}}$. Writing it out would require $10^{100}$ zeros—vastly more than all atoms in the universe ($10^{80}$).

**Exercise 13.**  
1. $D = 4.24 \times (9.46 \times 10^{12}) \approx 4.011 \times 10^{13}\text{ km}$.  
2. In hours: $t = \frac{4.011 \times 10^{13}}{6.12 \times 10^4} \approx 6.554 \times 10^8\text{ hours}$.  
   In years ($8,766\text{ h/year}$): $T \approx 74,766\text{ years}$!

**Exercise 14.**  
Numerator: $(x^8 y^{-12}) \times (x^{-2} y^2) = x^6 y^{-10}$.  
Dividing: $Z = \frac{x^6 y^{-10}}{x^5 y^{-8}} = x^{6-5} y^{-10 - (-8)} = x^1 y^{-2} = \frac{x}{y^2}$.

**Exercise 15.**  
$S = \frac{32 + 16 + 8 + 4 + 2 + 1}{64} = \frac{63}{64} = 0.984375$.  
The sum approaches 1 asymptotically; an infinite sum of these halves equals exactly 1!

---

### The Question That Opens What Follows

We now know that $a^2$ represents the square of a number: $3^2 = 9$, $4^2 = 16$.  
But what happens when we attempt the reverse operation? What number multiplied by itself yields exactly $2$?

This innocent question shattered the most secret philosophical brotherhood of ancient Greece, sparked death sentences on the open sea, and revealed a terrifying breed of numbers that no fraction can tame: **irrational numbers**. Step into the mystic sanctuary of Croton with **The Pythagorean Theorem**!
