# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 36: The Staircase Steps and the Usurer's Loan

> *“A continuous curve flows like the water of a river, without ever lifting the pen from the parchment. But the time of human affairs moves in discrete strides: heartbeats, clock ticks, the stone steps of a staircase, and interest payments falling due at month’s end. A numerical sequence is a voyage where each step rests upon the previous one to spring forward toward infinity.”*

---

### What You Are About to Discover

- The fundamental difference between a continuous quantity and a **numerical sequence** indexed by natural numbers $n \in \mathbb{N}$.
- The two primary ways of generating a sequence: the **explicit formula** $u_n = f(n)$ and the **recurrence relation** $u_{n+1} = g(u_n)$.
- **Arithmetic sequences**: the steady staircase where one always adds the same common difference $r$, and the legendary trick of young **Carl Friedrich Gauss** to sum consecutive integers.
- **Geometric sequences**: chained multiplication by the common ratio $q$, the dizzying growth of compound interest, and the trap of Sissa's chessboard.
- How to determine the **direction of variation** (monotonicity) of a sequence and intuitively grasp its **limit** at infinity.
- Programming a **threshold algorithm** in Python to determine when a quantity surpasses a given ceiling.

---

### 1. The Problem: The Two Bankers of Florence

In Renaissance Florence, two cloth merchants, Matteo and Cosimo, seek financing to charter a caravel bound for the Levant. Each needs to borrow $1\,000$ gold florins for a term of 10 years.

They approach two moneylenders on the Ponte Vecchio:

```
       MATTEO'S CONTRACT (Arithmetic Loan)          COSIMO'S CONTRACT (Geometric Loan)
   Each year, Matteo repays                     Each year, Cosimo's debt
   a FIXED penalty of 100 florins.              increases by 10% (compound rate).
   
   Year 0 : 1,000 florins                       Year 0 : 1,000 florins
   Year 1 : 1,100 florins                       Year 1 : 1,100 florins
   Year 2 : 1,200 florins                       Year 2 : 1,210 florins
   Year 3 : 1,300 florins                       Year 3 : 1,331 florins
   ...                                          ...
   Year 10: 2,000 florins                       Year 10: 2,593.74 florins!
```

Look closely at what occurred:
- For Matteo, each year adds **the same fixed amount**: $+100$ florins. It is an even staircase. Over 10 years, he pays $1\,000 + 10 \times 100 = 2\,000$ florins.
- For Cosimo, the first year appears identical ($+100$ florins). But in the second year, the $10\%$ applies to the $1\,100$ florins already owed: the debt expands by $110$ florins! In the third year, the $10\%$ applies to $1\,210$ florins ($+121$ florins). Interest begets interest, which in turn breeds more interest: this is the inexorable engine of **compound interest**. In 10 years, Cosimo owes nearly $2\,594$ florins—almost $60\%$ more than Matteo!

These two contracts embody the two royal families of discrete sequences:
- **Arithmetic sequences**, governed by **repeated addition**.
- **Geometric sequences**, propelled by **repeated multiplication**.

---

### 2. What Is a Numerical Sequence?

#### 2.1 Definition and Notations

A familiar function $f(x)$ accepts any real number: $x = 0$, $x = 1.5$, $x = \sqrt{2}$, $x = \pi$…
A **sequence** is far more restrained: it accepts only **non-negative integer indices**: $0, 1, 2, 3, 4\dots$

> **📐 Definition — Numerical Sequence.**
> A **numerical sequence** is a function whose domain is the set of natural numbers $\mathbb{N}$ (or a subset of $\mathbb{N}$ starting from a certain index $n_0$).
> For any natural number $n$, the image of $n$ is written as a **subscript**:
> $$u_n \quad \text{(instead of } u(n)\text{)}.$$
> We read it aloud: “$u$ sub $n$” (or “$u$ index $n$”).
> - $n$ is the **index** (or rank).
> - $u_n$ is the **term of index $n$** (or general term).
> - The entire sequence is denoted in parentheses: $(u_n)$ or $(u_n)_{n \in \mathbb{N}}$.

> **⚠️ Beware: Common Pitfall! Never confuse $u_n$ and $(u_n)$!**
> - $u_n$ is an **isolated real number** (for instance, $u_3 = 8$).
> - $(u_n)$ with parentheses denotes **the entire sequence**, the infinite machine producing the ordered list $\{u_0, u_1, u_2, u_3, \dots\}$.

#### 2.2 The Two Modes of Generation

##### Mode 1: Explicit Definition ($u_n = f(n)$)
The term $u_n$ is expressed directly as a function of the integer $n$.
*Example:* $u_n = 3n^2 - 1$.
- To calculate $u_0$, substitute $n = 0$: $u_0 = 3(0)^2 - 1 = -1$.
- To calculate $u_{100}$, there is no need to compute the 99 previous terms: $u_{100} = 3(100)^2 - 1 = 30\,000 - 1 = 29\,999$.

##### Mode 2: Recursive Definition ($u_{n+1} = g(u_n)$)
We specify:
1. The **initial term** that anchors the sequence (for example, $u_0 = 2$).
2. A **transition rule** that explains how to construct the next term from the current one: $u_{n+1} = g(u_n)$.
*Example:* $u_0 = 2$ and $u_{n+1} = 3u_n - 4$.
- $u_1 = 3u_0 - 4 = 3(2) - 4 = 2$.
- $u_2 = 3u_1 - 4 = 3(2) - 4 = 2$.
*(Here the sequence remains constant!)*

> **⚠️ Beware: Common Pitfall! In a recursive sequence, you advance step by step.**
> To compute $u_{10}$ using a recurrence relation, you are obliged to first compute $u_1, u_2, u_3\dots$ all the way to $u_9$. It operates like falling dominoes: each domino topples the next.

#### 2.3 Graphical Representation of a Sequence

Because the index $n$ takes only whole integer values ($0, 1, 2, 3\dots$), the graph of a sequence is a **cloud of isolated points** with coordinates $(n, u_n)$.
You must **never connect these points with a continuous solid line**, because intermediate non-integer values (such as $n = 1.5$) have no meaning for a sequence!

```
         un ▲
            │                     o (3, u3)
            │           o (2, u2)
            │
            │  o (1, u1)
            │
          o ┼ (0, u0)
            │
          O ┼───┼───────┼───────┼───────► n
            0   1       2       3
```

---

### 3. Arithmetic Sequences: The Regular Staircase

#### 3.1 Definition and General Term

> **📐 Definition — Arithmetic Sequence.**
> A sequence $(u_n)$ is called **arithmetic** if there exists a fixed real number $r$, called the **common difference**, such that for every natural number $n$:
> $$\boxed{u_{n+1} = u_n + r}$$

To climb from one step to the next, we always add the same number $r$:
- $u_1 = u_0 + r$
- $u_2 = u_1 + r = (u_0 + r) + r = u_0 + 2r$
- $u_3 = u_2 + r = (u_0 + 2r) + r = u_0 + 3r$

Continuing in this fashion up to index $n$:

> **📐 Theorem — Explicit Formula for the General Term.**
> If $(u_n)$ is an arithmetic sequence with initial term $u_0$ and common difference $r$, then for all $n \in \mathbb{N}$:
> $$\boxed{u_n = u_0 + nr}$$
> If the initial term is given at index $p$ as $u_p$, the formula becomes:
> $$u_n = u_p + (n - p)r.$$

**Remark:**
The points representing an arithmetic sequence all lie on the straight line with equation $y = rx + u_0$. The common difference $r$ plays exactly the role of the slope (rate of change)!
- If $r > 0$: the sequence is **strictly increasing**.
- If $r < 0$: the sequence is **strictly decreasing**.
- If $r = 0$: the sequence is **constant**.

#### 3.2 Gauss's Staircase: Sum of Consecutive Integers

In 1784, in a schoolhouse in Brunswick, Germany, an exhausted schoolmaster ordered his seven-year-old pupils to add all the numbers from $1$ to $100$:
$$S = 1 + 2 + 3 + 4 + \dots + 99 + 100.$$
The teacher hoped for an hour of quiet. But after just a few seconds, a young boy set his slate on the master's desk, saying: *“Ligget se!”* (“There it lies!”). The result written on the slate was $5\,050$, perfectly exact.

That child was **Carl Friedrich Gauss**.

```
    1   +   2   +   3   + ... +  98  +  99  + 100
  100   +  99   +  98   + ... +   3  +   2  +   1
  ────────────────────────────────────────────────
  101   + 101   + 101   + ... + 101  + 101  + 101   (100 times the sum 101!)
```

> **✍️ Proof (Required knowledge) — Sum of the First $n$ Positive Integers.**
> For any natural number $n \ge 1$:
> $$\boxed{1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}}$$
> 
> *Proof:*
> Write the sum $S_n$ in ascending order, and directly beneath it in descending order:
> $$S_n = 1 + 2 + 3 + \dots + (n-1) + n$$
> $$S_n = n + (n-1) + (n-2) + \dots + 2 + 1$$
> Add the two equations column by column:
> $$2S_n = (1 + n) + (2 + n - 1) + (3 + n - 2) + \dots + (n + 1).$$
> Each bracketed pair sums to exactly $n + 1$.
> How many columns are there? There are precisely $n$ columns.
> Therefore:
> $$2S_n = n \times (n + 1) \implies S_n = \frac{n(n + 1)}{2}. \quad \blacksquare$$

For $n = 100$: $S_{100} = \frac{100 \times 101}{2} = 50 \times 101 = 5\,050$.

#### 3.3 Sum of Consecutive Terms of an Arithmetic Sequence

> **📐 General Theorem — Arithmetic Sum.**
> For any arithmetic sequence:
> $$\boxed{S = \sum_{k=p}^n u_k = u_p + u_{p+1} + \dots + u_n = (\text{number of terms}) \times \frac{\text{first term} + \text{last term}}{2}}$$
> where the number of terms is given by: $\text{last index} - \text{first index} + 1 = n - p + 1$.

---

### 4. Geometric Sequences: The Vertigo of Multiplication

#### 4.1 Definition and General Term

> **📐 Definition — Geometric Sequence.**
> A sequence $(u_n)$ is called **geometric** if there exists a fixed real number $q$, called the **common ratio**, such that for every natural number $n$:
> $$\boxed{u_{n+1} = q \times u_n}$$

To move from one term to the next, we always multiply by the same number $q$:
- $u_1 = q \times u_0$
- $u_2 = q \times u_1 = q \times (q u_0) = u_0 \times q^2$
- $u_3 = q \times u_2 = u_0 \times q^3$

> **📐 Theorem — Explicit Formula for the General Term.**
> If $(u_n)$ is a geometric sequence with initial term $u_0$ and common ratio $q$, then for all $n \in \mathbb{N}$:
> $$\boxed{u_n = u_0 \times q^n}$$
> If the initial term is given at index $p$ as $u_p$, the formula becomes:
> $$u_n = u_p \times q^{n-p}.$$

#### 4.2 Sissa's Chessboard and Exponential Explosion

The Indian sage Sissa invented the game of chess to entertain his king. Delighted, the monarch offered him any reward he desired. Sissa replied modestly:
> “Sire, place a single grain of wheat on the first square, two on the second, four on the third, eight on the fourth, doubling on each subsequent square up to the 64th square of the board.”

The king smiled at what seemed a trifling request. But his treasurers returned as pale as death:
- Square 1: $u_0 = 1 = 2^0$
- Square 2: $u_1 = 2 = 2^1$
- Square 3: $u_2 = 4 = 2^2$
- Square 64: $u_{63} = 2^{63} \approx 9.22 \times 10^{18}$ grains!

The total number of grains across the entire board equals:
$$S = 1 + 2 + 4 + \dots + 2^{63} = 2^{64} - 1 \approx 18.4 \times 10^{18}\text{ grains}.$$
This represents more than $1\,200$ billion metric tons of wheat—equivalent to the modern world's wheat harvest for more than two millennia! The king could never honor his promise.

#### 4.3 Sum of Consecutive Powers of a Number $q$

> **✍️ Proof (Required knowledge) — Sum of Powers of $q$.**
> For any real $q \neq 1$ and any integer $n \ge 0$:
> $$\boxed{1 + q + q^2 + q^3 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}}$$
> 
> *Proof (by the telescoping method):*
> Let $S_n = 1 + q + q^2 + \dots + q^n$.
> Multiply both sides by $q$:
> $$q S_n = q(1 + q + q^2 + \dots + q^n) = q + q^2 + q^3 + \dots + q^{n+1}.$$
> Now subtract this equation from the original equation ($S_n - qS_n$):
> $$S_n - qS_n = (1 + q + q^2 + \dots + q^n) - (q + q^2 + q^3 + \dots + q^{n+1}).$$
> Observe the striking cancellation: all intermediate terms eliminate each other diagonally in pairs!
> Only the very first term ($1$) and the very last term ($-q^{n+1}$) survive:
> $$S_n(1 - q) = 1 - q^{n+1}.$$
> Since $q \neq 1$, we can divide by $1 - q$:
> $$S_n = \frac{1 - q^{n+1}}{1 - q}. \quad \blacksquare$$

> **📐 General Theorem — Geometric Sum.**
> For any geometric sequence with common ratio $q \neq 1$:
> $$\boxed{S = (\text{first term}) \times \frac{1 - q^{\text{number of terms}}}{1 - q}}$$

---

### 5. Variations and Intuition of the Limit

#### 5.1 The Three Methods for Studying the Monotonicity of a Sequence

To determine whether a sequence climbs ($u_{n+1} \ge u_n$) or descends ($u_{n+1} \le u_n$):

1. **Method 1: Study the sign of the difference $u_{n+1} - u_n$ (Universal method).**
   - If for all $n$, $u_{n+1} - u_n > 0$, the sequence $(u_n)$ is strictly increasing.
   - If for all $n$, $u_{n+1} - u_n < 0$, the sequence $(u_n)$ is strictly decreasing.

2. **Method 2: Compare the quotient $\frac{u_{n+1}}{u_n}$ with $1$ (valid ONLY when all terms are strictly positive!).**
   - If $\frac{u_{n+1}}{u_n} > 1$, the sequence is strictly increasing.
   - If $\frac{u_{n+1}}{u_n} < 1$, the sequence is strictly decreasing.

3. **Method 3: Leverage the associated function if $u_n = f(n)$.**
   If the function $f$ is increasing on $[0, +\infty[$, then the sequence $u_n = f(n)$ is increasing.

#### 5.2 Limit of a Geometric Sequence According to Ratio $q$

What happens to $q^n$ as $n$ grows indefinitely large ($n \to +\infty$)?

- **If $q > 1$:** The sequence explodes toward infinity: $\lim_{n \to +\infty} q^n = +\infty$. (Example: $2^n$).
- **If $q = 1$:** The sequence is constant and equal to 1.
- **If $-1 < q < 1$:** The sequence shrinks toward zero: $\lim_{n \to +\infty} q^n = 0$. (Example: $\left(\frac{1}{2}\right)^n \to 0$).
- **If $q \le -1$:** The sequence oscillates without admitting any limit (Example: $(-1)^n = 1, -1, 1, -1\dots$).

---

### 6. In Computer Science: The Threshold Algorithm in Python

A fundamental problem in finance, biology, and physics is determining **at which index $n$** a sequence crosses a given critical boundary (the threshold). We use a `while` loop for this purpose:

```python
def growth_threshold(initial_value, rate, threshold):
    """
    Computes the number of periods needed to exceed a given threshold.
    Example: an initial capital of €1,000 invested at 5% per year (ratio q = 1.05)
    must exceed €2,000 (double).
    """
    n = 0
    u = initial_value
    
    while u < threshold:
        u = u * (1 + rate)  # Apply annual growth rate
        n += 1              # Step to the next year
        
    return n, round(u, 2)

years, final_amount = growth_threshold(1000, 0.05, 2000)
print(f"The capital will double after {years} years, reaching €{final_amount}.")
# Prints: The capital will double after 15 years, reaching €2078.93.
```

---

### 7. Detailed Worked Examples

> **Worked Example 1 — Reconstructing an Arithmetic Sequence.**
> Let $(u_n)$ be an arithmetic sequence such that $u_4 = 17$ and $u_9 = 37$.
> 1. Determine the common difference $r$ and the initial term $u_0$.
> 2. Express $u_n$ in terms of $n$.
> 3. Calculate the value of $u_{50}$.
>
> **Solution:**
> 1. According to the general term formula: $u_9 = u_4 + (9 - 4)r$.
>    $$37 = 17 + 5r \iff 5r = 37 - 17 = 20 \iff r = \frac{20}{5} = 4.$$
>    To find $u_0$, use $u_4 = u_0 + 4r$:
>    $$17 = u_0 + 4(4) \iff 17 = u_0 + 16 \iff u_0 = 1.$$
> 2. The general term is therefore: $\boxed{u_n = 1 + 4n}$.
> 3. For $n = 50$: $u_{50} = 1 + 4(50) = 1 + 200 = 201$.

> **Worked Example 2 — Computing an Arithmetic Sum of Terms.**
> Compute the sum:
> $$S = 7 + 11 + 15 + 19 + \dots + 123.$$
>
> **Solution:**
> The terms increase by $+4$ each step: this is an arithmetic sequence with common difference $r = 4$ and initial term $u_0 = 7$.
> The general term is $u_n = 7 + 4n$.
> Let us find the index of the last term $123$:
> $$7 + 4n = 123 \iff 4n = 116 \iff n = 29.$$
> The terms run from $u_0$ to $u_{29}$: there are therefore $29 - 0 + 1 = 30\text{ terms}$.
> Apply the formula for the sum of an arithmetic sequence:
> $$S = (\text{number of terms}) \times \frac{\text{first} + \text{last}}{2} = 30 \times \frac{7 + 123}{2} = 30 \times \frac{130}{2} = 30 \times 65 = 1\,950.$$

> **Worked Example 3 — Geometric Sequence and Sum of Powers.**
> Let $(v_n)$ be the geometric sequence with initial term $v_0 = 5$ and common ratio $q = 3$.
> 1. Compute $v_1, v_2$, and $v_6$.
> 2. Compute the sum $S = v_0 + v_1 + v_2 + \dots + v_6$.
>
> **Solution:**
> 1. $v_1 = 5 \times 3 = 15$.
>    $v_2 = 15 \times 3 = 45$.
>    General formula: $v_n = 5 \times 3^n$.
>    For $n = 6$: $v_6 = 5 \times 3^6 = 5 \times 729 = 3\,645$.
> 2. Number of terms from $v_0$ to $v_6$: $6 - 0 + 1 = 7\text{ terms}$.
>    $$S = v_0 \times \frac{1 - q^7}{1 - q} = 5 \times \frac{1 - 3^7}{1 - 3} = 5 \times \frac{1 - 2\,187}{-2} = 5 \times \frac{-2\,186}{-2} = 5 \times 1\,093 = 5\,465.$$

> **Worked Example 4 — Studying the Monotonicity of a Sequence.**
> Determine the direction of variation of the following sequences:
> a) $u_n = \frac{n}{n + 1}$ for $n \in \mathbb{N}$ \quad b) $v_n = \frac{3^n}{n!}$ for $n \ge 1$
>
> **Solution:**
> a) Study the sign of the difference $u_{n+1} - u_n$:
>    $$u_{n+1} - u_n = \frac{n + 1}{(n + 1) + 1} - \frac{n}{n + 1} = \frac{n + 1}{n + 2} - \frac{n}{n + 1}.$$
>    Find a common denominator $(n + 2)(n + 1) > 0$:
>    $$u_{n+1} - u_n = \frac{(n + 1)^2 - n(n + 2)}{(n + 2)(n + 1)} = \frac{n^2 + 2n + 1 - (n^2 + 2n)}{(n + 2)(n + 1)} = \frac{1}{(n + 2)(n + 1)}.$$
>    The numerator is $1 > 0$ and the denominator is strictly positive for all $n \in \mathbb{N}$.
>    Hence $u_{n+1} - u_n > 0$ for all $n$: the sequence $(u_n)$ is **strictly increasing**.
>
> b) All terms of $v_n$ are strictly positive. Compare the ratio $\frac{v_{n+1}}{v_n}$ to 1:
>    $$\frac{v_{n+1}}{v_n} = \frac{\frac{3^{n+1}}{(n+1)!}}{\frac{3^n}{n!}} = \frac{3^{n+1}}{3^n} \times \frac{n!}{(n+1)!} = 3 \times \frac{n!}{(n+1)n!} = \frac{3}{n + 1}.$$
>    - If $n = 1$: $\frac{v_2}{v_1} = \frac{3}{2} > 1$ (the sequence initially increases: $v_1 = 3, v_2 = 4.5$).
>    - If $n = 2$: $\frac{v_3}{v_2} = \frac{3}{3} = 1$ ($v_3 = v_2 = 4.5$).
>    - For all $n \ge 3$: $n + 1 \ge 4$, so $\frac{3}{n+1} < 1$, which implies $v_{n+1} < v_n$.
>    The sequence $(v_n)$ is **strictly decreasing starting from index $n = 2$**.

> **Worked Example 5 — Arithmetico-Geometric Sequence.**
> An animal shelter has $200$ animals on January 1, 2025. Each year, $20\%$ of the animals are adopted and leave the shelter, while $50$ newly abandoned animals are taken in.
> Let $u_n$ denote the number of animals after $n$ years.
> 1. Establish the recurrence relation linking $u_{n+1}$ and $u_n$.
> 2. Define $v_n = u_n - 250$. Prove that $(v_n)$ is a geometric sequence.
> 3. Deduce the explicit formula for $u_n$ in terms of $n$, and find the limit of $u_n$ as $n \to +\infty$.
>
> **Solution:**
> 1. If $20\%$ of the animals leave, $80\%$ remain, which corresponds to multiplying by $0.8$. Adding the 50 new arrivals:
>    $$u_0 = 200 \quad \text{and} \quad u_{n+1} = 0.8u_n + 50.$$
> 2. Express $v_{n+1}$ in terms of $v_n$:
>    $$v_{n+1} = u_{n+1} - 250 = (0.8u_n + 50) - 250 = 0.8u_n - 200.$$
>    Factor out $0.8$:
>    $$v_{n+1} = 0.8(u_n - 250) = 0.8 v_n.$$
>    The sequence $(v_n)$ is a **geometric sequence with common ratio $q = 0.8$** and initial term:
>    $$v_0 = u_0 - 250 = 200 - 250 = -50.$$
> 3. By the geometric formula: $v_n = v_0 \times q^n = -50 \times (0.8)^n$.
>    Since $u_n = v_n + 250$, we deduce:
>    $$\boxed{u_n = 250 - 50 \times (0.8)^n}.$$
>    Since $-1 < 0.8 < 1$, we have $\lim_{n \to +\infty} (0.8)^n = 0$.
>    Consequently:
>    $$\lim_{n \to +\infty} u_n = 250 - 50 \times 0 = 250.$$
>    In the long term, the shelter population stabilizes around $250$ animals.

> **Worked Example 6 — Cobweb Plot (Web Diagram) of a Recurrence Sequence.**
> Consider the recursive sequence defined by $u_0 = 0$ and $u_{n+1} = \frac{1}{2}u_n + 1$.
> Graphically represent the first four terms on a coordinate plane using the line $y = x$.
>
> **Solution and Method:**
> Draw the line $y = x$ (the main diagonal) and the line representing the function $g(x) = \frac{1}{2}x + 1$ in the coordinate plane.
> 1. Start from $u_0 = 0$ on the horizontal axis.
> 2. Move vertically up to the line $y = g(x)$: the point reached has $y$-coordinate $g(u_0) = u_1 = 1$.
> 3. Move horizontally to the diagonal line $y = x$: this transfers the value $u_1 = 1$ onto the horizontal axis without recalculation!
> 4. Move vertically to the line $y = g(x)$ again to find $u_2 = g(1) = 1.5$.
> 5. Move horizontally to $y = x$, then vertically back to the function line to find $u_3 = g(1.5) = 1.75$.
> The successive segments form a “staircase” (or cobweb) that converges toward the intersection point of the two lines:
> $$x = \frac{1}{2}x + 1 \iff \frac{1}{2}x = 1 \iff x = 2.$$
> The sequence $(u_n)$ increases, approaching its limit $L = 2$.

---

### Key Takeaways

1. **Sequence:** A function indexed by whole numbers $n \in \mathbb{N}$. Term $u_n$, sequence $(u_n)$.
2. **Explicit vs Recursive Definition:**
   - Explicit: $u_n = f(n)$ (direct calculation).
   - Recursive: $u_0$ and $u_{n+1} = g(u_n)$ (step-by-step propagation).
3. **Arithmetic Sequences:**
   - Definition: $u_{n+1} = u_n + r$.
   - General term: $u_n = u_0 + nr$ (or $u_n = u_p + (n-p)r$).
   - Gauss sum: $1 + 2 + \dots + n = \frac{n(n+1)}{2}$.
   - General sum: $(\text{number of terms}) \times \frac{\text{first} + \text{last}}{2}$.
4. **Geometric Sequences:**
   - Definition: $u_{n+1} = q \times u_n$.
   - General term: $u_n = u_0 \times q^n$ (or $u_n = u_p \times q^{n-p}$).
   - Sum of powers: $1 + q + q^2 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$).
   - General sum: $(\text{first}) \times \frac{1 - q^{\text{number of terms}}}{1 - q}$.
5. **Variations:** Sign of $u_{n+1} - u_n$ or quotient $\frac{u_{n+1}}{u_n}$ compared to 1.
6. **Geometric Limit:** If $|q| < 1$, then $q^n \to 0$. If $q > 1$, then $q^n \to +\infty$.

---

### Exercises

#### Direct Application Exercises (★)

1. Given the explicit sequence $u_n = 2n^2 - 3$. Compute $u_0, u_1, u_2$, and $u_{10}$.
2. Given the recursive sequence $v_0 = 4$ and $v_{n+1} = 2v_n - 3$. Compute $v_1, v_2$, and $v_3$.
3. An arithmetic sequence has initial term $u_0 = 5$ and common difference $r = 3$. Give the expression for $u_n$, then calculate $u_{20}$.
4. A geometric sequence has initial term $v_0 = 3$ and common ratio $q = 2$. Give the expression for $v_n$, then calculate $v_8$.
5. Compute the sum of integers from $1$ to $50$: $S = 1 + 2 + 3 + \dots + 50$.
6. Compute the geometric sum: $S = 1 + 2 + 4 + 8 + \dots + 2^{10}$.
7. Is the sequence $u_n = 5 - 4n$ arithmetic? State its common difference and its direction of variation.
8. Is the sequence $v_n = 7 \times 0.6^n$ geometric? State its common ratio and its limit as $n \to +\infty$.
9. Determine the direction of variation of the sequence $u_n = 3n + 7$.
10. Given an arithmetic sequence such that $u_3 = 10$ and $u_5 = 16$. Find the common difference $r$.

#### Practice and Reasoning Exercises (★★)

11. Consider the arithmetic sequence $(u_n)$ such that $u_2 = 11$ and $u_7 = 36$.
    a) Compute the common difference $r$ and the initial term $u_0$.
    b) Starting from which index $n$ do we have $u_n > 1\,000$?
12. Compute the sum: $S = 12 + 15 + 18 + 21 + \dots + 150$.
13. A capital sum of $€5\,000$ is deposited into an account earning compound interest at an annual rate of $4\%$.
    Let $C_n$ denote the value of the capital after $n$ years.
    a) Express $C_{n+1}$ in terms of $C_n$, then $C_n$ in terms of $n$.
    b) What will be the available capital after 10 years?
    c) Write a Python script to determine after how many years the capital will exceed $€8\,000$.
14. Determine the direction of variation of the sequence $u_n = \frac{2^n}{n}$ for $n \ge 1$.
15. Determine the direction of variation of the sequence $w_n = n^2 - 10n + 3$ for $n \in \mathbb{N}$.
16. Compute the sum of powers of 3: $S = 1 + 3 + 9 + 27 + \dots + 3^7$.
17. Consider the recursive sequence defined by $u_0 = 1$ and $u_{n+1} = \sqrt{u_n + 2}$.
    a) Compute $u_1$ and $u_2$ in exact and approximate decimal form.
    b) Determine graphically the value toward which this sequence appears to converge by finding the fixed point of $f(x) = \sqrt{x + 2}$.
18. Let $(u_n)$ be a positive geometric sequence such that $u_1 = 6$ and $u_3 = 24$.
    Determine the common ratio $q$, the initial term $u_0$, and compute the sum $u_0 + u_1 + \dots + u_8$.

#### Deepening Exercises and Challenges (★★★)

19. **The Paradox of the Koch Snowflake.**
    The Koch snowflake is a fractal generated starting from an equilateral triangle of side length 1 (stage 0). At each stage, the central third of each side is replaced by an outward-pointing equilateral triangle.
    - Stage 0: number of sides $N_0 = 3$, length of each side $\ell_0 = 1$.
    - At stage $n+1$, each segment is replaced by 4 segments, each 3 times shorter.
    a) Express the number of sides $N_n$ in terms of $n$.
    b) Express the length $\ell_n$ of a side in terms of $n$.
    c) Deduce the perimeter $P_n = N_n \times \ell_n$ of the snowflake at stage $n$.
    d) What is the limit of the perimeter as $n \to +\infty$?
20. **Sum of Squares of Consecutive Integers.**
    We wish to prove that:
    $$1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}.$$
    a) Verify this formula for $n = 1, 2, 3$.
    b) Expanding $(k + 1)^3 - k^3 = 3k^2 + 3k + 1$, sum this identity for $k$ ranging from $1$ to $n$ and deduce the formula.
21. **Achilles and the Tortoise Revisited.**
    The tortoise starts with a $100\text{ meter}$ head start over Achilles. Achilles runs at $10\text{ m/s}$ and the tortoise crawls at $1\text{ m/s}$.
    - To cover the initial $100\text{ m}$, Achilles takes $t_0 = 10\text{ s}$. During this time, the tortoise has moved $10\text{ m}$.
    - To cover those $10\text{ m}$, Achilles takes $t_1 = 1\text{ s}$. The tortoise has moved $1\text{ m}$.
    - To cover that meter, Achilles takes $t_2 = 0.1\text{ s}$, and so on.
    a) Express the time $t_n$ of the $n$-th stage. What type of sequence is $(t_n)$?
    b) Compute the total elapsed time $T_n = t_0 + t_1 + \dots + t_n$ after $n$ stages.
    c) What is the limit of $T_n$ as $n \to +\infty$? Does Achilles overtake the tortoise?
22. **The Fibonacci Sequence and the Golden Ratio.**
    The famous Fibonacci sequence is defined by $F_0 = 0, F_1 = 1$ and for all $n \in \mathbb{N}$:
    $$F_{n+2} = F_{n+1} + F_n.$$
    a) Compute the first ten terms $F_0, F_1, F_2, \dots, F_9$.
    b) Consider the ratio $r_n = \frac{F_{n+1}}{F_n}$ for $n \ge 1$. Compute $r_1, r_2, r_3, r_4, r_5$.
    c) Toward what remarkable value does this ratio appear to converge?

---

### Solutions

1. $u_0 = -3$. $u_1 = 2(1) - 3 = -1$. $u_2 = 2(4) - 3 = 5$. $u_{10} = 2(100) - 3 = 197$.
2. $v_1 = 2(4) - 3 = 5$. $v_2 = 2(5) - 3 = 7$. $v_3 = 2(7) - 3 = 11$.
3. $u_n = 5 + 3n$. $u_{20} = 5 + 3(20) = 65$.
4. $v_n = 3 \times 2^n$. $v_8 = 3 \times 256 = 768$.
5. $S = \frac{50 \times 51}{2} = 25 \times 51 = 1\,275$.
6. $S = \frac{1 - 2^{11}}{1 - 2} = \frac{1 - 2\,048}{-1} = 2\,047$.
7. $u_{n+1} - u_n = [5 - 4(n+1)] - [5 - 4n] = -4$. This is an arithmetic sequence with common difference $r = -4$. Since $r < 0$, it is strictly decreasing.
8. $v_{n+1} = 7 \times 0.6^{n+1} = 0.6 \times (7 \times 0.6^n) = 0.6 v_n$. Geometric sequence with common ratio $q = 0.6$. Since $|0.6| < 1$, $\lim_{n \to +\infty} v_n = 0$.
9. $u_{n+1} - u_n = [3(n+1) + 7] - [3n + 7] = 3 > 0$. Strictly increasing.
10. $u_5 = u_3 + 2r \iff 16 = 10 + 2r \iff 2r = 6 \iff r = 3$.
11. a) $u_7 = u_2 + 5r \iff 36 = 11 + 5r \iff 5r = 25 \iff r = 5$.
       $u_2 = u_0 + 2r \iff 11 = u_0 + 10 \iff u_0 = 1$. General term: $u_n = 1 + 5n$.
    b) $1 + 5n > 1\,000 \iff 5n > 999 \iff n > 199.8$. Starting from index $n = 200$.
12. Arithmetic sequence with common difference $r = 3$. $u_0 = 12$, $u_n = 12 + 3n = 150 \iff 3n = 138 \iff n = 46$.
    Number of terms: $46 - 0 + 1 = 47\text{ terms}$.
    $S = 47 \times \frac{12 + 150}{2} = 47 \times 81 = 3\,807$.
13. a) Increasing by $4\%$ corresponds to multiplying by $1.04$. $C_{n+1} = 1.04 C_n$.
       $C_n = 5\,000 \times (1.04)^n$.
    b) $C_{10} = 5\,000 \times (1.04)^{10} \approx 5\,000 \times 1.48024 \approx €7\,401.22$.
    c) Python script:
       ```python
       n, c = 0, 5000
       while c <= 8000:
           c *= 1.04
           n += 1
       print(n)  # Prints 12 years (c ≈ 8005.16 €)
       ```
14. $u_n > 0$ for all $n \ge 1$.
    $\frac{u_{n+1}}{u_n} = \frac{2^{n+1}}{n+1} \times \frac{n}{2^n} = 2 \times \frac{n}{n+1} = \frac{2n}{n+1}$.
    Compare to 1: $\frac{2n}{n+1} > 1 \iff 2n > n + 1 \iff n > 1$.
    For $n = 1$: $u_1 = 2, u_2 = 2 \implies u_1 = u_2$.
    For all $n \ge 2$, $\frac{u_{n+1}}{u_n} > 1$, so the sequence $(u_n)$ is strictly increasing starting from $n = 2$.
15. $w_{n+1} - w_n = [(n+1)^2 - 10(n+1) + 3] - [n^2 - 10n + 3] = n^2 + 2n + 1 - 10n - 10 + 3 - n^2 + 10n - 3 = 2n - 9$.
    - If $n \le 4$: $2n - 9 < 0$, the sequence decreases ($w_0 = 3, w_1 = -6, w_2 = -13, w_3 = -18, w_4 = -21, w_5 = -22$).
    - If $n \ge 5$: $2n - 9 > 0$, the sequence is strictly increasing.
16. $S = \frac{1 - 3^8}{1 - 3} = \frac{1 - 6\,561}{-2} = \frac{-6\,560}{-2} = 3\,280$.
17. a) $u_1 = \sqrt{1 + 2} = \sqrt{3} \approx 1.732$. $u_2 = \sqrt{\sqrt{3} + 2} \approx \sqrt{3.732} \approx 1.932$.
    b) Fixed point: $x = \sqrt{x + 2} \implies x^2 = x + 2 \iff x^2 - x - 2 = 0 \iff (x - 2)(x + 1) = 0$.
       Since $x \ge 0$, the solution is $x = 2$. The sequence converges toward $2$.
18. $u_3 = u_1 \times q^2 \iff 24 = 6q^2 \iff q^2 = 4 \implies q = 2$ (since the sequence is positive).
    $u_1 = u_0 \times q \iff 6 = 2u_0 \iff u_0 = 3$.
    Number of terms from $u_0$ to $u_8$: 9 terms.
    $S = 3 \times \frac{1 - 2^9}{1 - 2} = 3 \times \frac{1 - 512}{-1} = 3 \times 511 = 1\,533$.
19. a) At each stage, each segment is replaced by 4 segments: $N_n = 3 \times 4^n$.
    b) The length of each segment is divided by 3: $\ell_n = \left(\frac{1}{3}\right)^n$.
    c) Perimeter: $P_n = N_n \times \ell_n = 3 \times 4^n \times \frac{1}{3^n} = 3 \times \left(\frac{4}{3}\right)^n$.
    d) Since $\frac{4}{3} > 1$, $\lim_{n \to +\infty} \left(\frac{4}{3}\right)^n = +\infty$, hence $\lim_{n \to +\infty} P_n = +\infty$.
    The Koch snowflake encloses a finite area within an infinitely long perimeter!
20. a) For $n = 1$: $1^2 = 1$ and $\frac{1 \times 2 \times 3}{6} = 1$.
       For $n = 2$: $1 + 4 = 5$ and $\frac{2 \times 3 \times 5}{6} = 5$.
       For $n = 3$: $1 + 4 + 9 = 14$ and $\frac{3 \times 4 \times 7}{6} = 14$.
    b) Summing $(k+1)^3 - k^3$ from $k=1$ to $n$, the left side telescopes to $(n+1)^3 - 1$.
       On the other hand, the sum equals $3\sum k^2 + 3\sum k + \sum 1 = 3\sum k^2 + 3\frac{n(n+1)}{2} + n$.
       Isolating $\sum k^2$:
       $3\sum k^2 = (n+1)^3 - 1 - \frac{3n(n+1)}{2} - n = (n+1)[(n+1)^2 - 1] - \frac{3n(n+1)}{2} = (n+1)n(n+2) - \frac{3n(n+1)}{2} = n(n+1)\left(n + 2 - \frac{3}{2}\right) = n(n+1)\left(\frac{2n+1}{2}\right)$.
       Dividing by 3: $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.
21. a) $t_n = 10 \times (0.1)^n$. This is a geometric sequence with initial term $t_0 = 10$ and common ratio $q = 0.1$.
    b) $T_n = 10 \times \frac{1 - (0.1)^{n+1}}{1 - 0.1} = 10 \times \frac{1 - (0.1)^{n+1}}{0.9} = \frac{100}{9}\left[1 - (0.1)^{n+1}\right]$.
    c) Since $|0.1| < 1$, $(0.1)^{n+1} \to 0$.
       $\lim_{n \to +\infty} T_n = \frac{100}{9} \approx 11.11\text{ seconds}$.
       Zeno's paradox is resolved: an infinite sum of time intervals can sum to a finite total duration! After $11.11\text{ s}$, Achilles overtakes the tortoise.
22. a) $F_0 = 0, F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, F_6 = 8, F_7 = 13, F_8 = 21, F_9 = 34$.
    b) $r_1 = \frac{1}{1} = 1$; $r_2 = \frac{2}{1} = 2$; $r_3 = \frac{3}{2} = 1.5$; $r_4 = \frac{5}{3} \approx 1.667$; $r_5 = \frac{8}{5} = 1.6$.
    c) The ratio oscillates and converges toward the **golden ratio** $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887\dots$

---

### The Question Opening the Next Stage

In this chapter, we explored sequences advancing by discrete strides, and we computed quantities that cycle or oscillate. But now imagine a fairground Ferris wheel spinning endlessly, or an ocean wave rising and falling with rhythmic perfection.

How can we measure angles not in rigid degrees, but by unwinding a flexible ribbon around a circle of radius 1? How do cosine and sine, first discovered in middle school right-angled triangles, become the undulations of waves describing sound, light, and alternating electric current? This is what we will discover in **The Ferris Wheel and the Winding Circle**.
