# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 44: The Runner Who Never Touches the Line

> *“Swift-footed Achilles will never overtake the tortoise, said Zeno. For to reach it, he must first cover half the distance, then half of the remainder, then half of what still remains. An infinity of steps cannot be completed in a finite time. Zeno’s mistake was not in his view of the world, but in his lack of a mathematical tool: the concept of a limit.”*

---

### What You Will Discover

- How the Greek paradox of **Zeno of Elea** challenged thinkers for more than two millennia, and how the modern notion of **limit** finally resolved it.
- The **formal definition** of a convergent sequence: the intuitive idea of a “tunnel” or an open interval that traps all terms beyond a certain rank, and the rigorous definition of divergence toward $\pm\infty$.
- The **comparison theorems** and the famous **squeeze theorem** (or squeeze theorem / sandwich theorem).
- The **monotone convergence theorem**: knowing that a sequence converges even before knowing its limit.
- The complete behavior of **geometric sequences** $q^n$, proven using Bernoulli’s inequality (a required proof for the Baccalaureate).
- The **threshold algorithm in Python** to find when a sequence crosses a given barrier.

---

### 1. The Problem: Achilles, the Tortoise, and the Infinite Stadium

#### 1.1 The Dichotomy Paradox

Five centuries before our era, in the Greek city of Elea in southern Italy, the philosopher **Zeno** proposed a series of troubling riddles designed to show that motion is an illusion of our senses.

Consider a runner setting off on a 100-meter track. Before crossing the finish line, he must imperatively reach the halfway mark: $50\text{ m}$.
Once at $50\text{ m}$, he still has $50\text{ m}$ left to run; he must first cover half of this remainder, which is $75\text{ m}$.
At $75\text{ m}$, he must cover half of the remaining quarter, reaching $87.5\text{ m}$...

```
Start                                                       Finish
[0] ───────────────┬───────────────┬───────┬───┬─┬[100]
                   50              75    87.5 93.75 ...
                  1/2             3/4     7/8 15/16
```

At each step $n$, the distance traveled as a fraction of the total track is:
$$u_n = 1 - \frac{1}{2^n}.$$

Zeno argues:
> *“The runner must perform an infinity of successive acts: traverse the 1st interval, then the 2nd, then the 3rd... But no one can accomplish an infinity of tasks in a finite time. Therefore, the runner will never reach the line. Worse: he cannot even start, because before traveling one meter, he must travel half a meter, and before that a quarter of a meter...”*

Yet in the real world, any child runs the 100 meters in a few seconds. Where does the flaw in Zeno's reasoning lie?

#### 1.2 The Sum of an Infinity of Pieces

Let us look at the total distance traveled as a sum of infinitely repeated slices:
$$S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \dots + \frac{1}{2^n} + \dots$$

Let us calculate the sum of the first $n$ terms (denoted $S_n$):
- $S_1 = \frac{1}{2} = 0.5$
- $S_2 = \frac{1}{2} + \frac{1}{4} = \frac{3}{4} = 0.75$
- $S_3 = \frac{3}{4} + \frac{1}{8} = \frac{7}{8} = 0.875$
- $S_n = 1 - \frac{1}{2^n}$.

As $n$ becomes larger and larger, the term $\frac{1}{2^n}$ becomes minuscule:
- for $n = 10$, $\frac{1}{2^{10}} = \frac{1}{1024} \approx 0.000976$;
- for $n = 30$, $\frac{1}{2^{30}} \approx 0.00000000093$.

The gap between the runner and the finish line ($100\text{ m}$) becomes smaller than the width of a hair, then smaller than a molecule, then smaller than an atomic nucleus.
Zeno's fallacy is to assume that a sum of an infinity of durations is necessarily infinite. But if the runner runs at a constant speed of $10\text{ m/s}$:
- the first half takes $5\text{ s}$;
- the next quarter takes $2.5\text{ s}$;
- the next eighth takes $1.25\text{ s}$...

The total elapsed time is also the sum:
$$T = 5 + 2.5 + 1.25 + 0.625 + \dots = 10\text{ seconds}.$$
An infinity of time intervals can perfectly sum to a finite duration!

To formalize this dizzying leap into the infinitely large without falling into metaphysical traps, nineteenth-century mathematicians (Cauchy, Weierstrass) forged a tool of surgical precision: **the limit of a sequence**.

---

### 2. Definitions: Taming Infinity

#### 2.1 The Notations Explained

- A real sequence is denoted $(u_n)_{n \in \mathbb{N}}$ or simply $(u_n)$. The letter $n$ represents a natural number ($n = 0, 1, 2, 3 \dots$) acting as a discrete time clock (the tick-tock of a clock). $u_n$ denotes the term of rank $n$.
- $\lim\limits_{n \to +\infty} u_n = L$ is read: “the limit of $u_n$ as $n$ tends to plus infinity is equal to $L$”. The abbreviation $\lim$ comes from the Latin *limes*, which referred to the fortified frontier of the Roman Empire.
- The arrow $\to$ is read “tends to” or “approaches”. One also sometimes writes $u_n \xrightarrow[n \to +\infty]{} L$.
- An open interval containing a real number $L$ is an interval of the form $]L - \varepsilon ; L + \varepsilon[$ (or $(L - \varepsilon, L + \varepsilon)$) with $\varepsilon > 0$ (the Greek letter $\varepsilon$, “epsilon”, traditionally denoting an error tolerance as tiny as one wishes).

```
                 L - ε         L         L + ε
───────(───────────[───────────●───────────]───────────)───────► Real axis
                 ◄─────── 2ε ───────►
```

#### 2.2 Convergent Sequence: The Official Definition

What exactly does it mean to say: “as $n$ becomes very large, the terms $u_n$ approach $L$”?
Saying merely “they approach” is insufficient. The sequence $1 + \frac{1}{n}$ approaches $-5$, but its limit is not $-5$! They must approach $L$ **as closely as one wishes**, and they must **stay there forever**.

> **📐 Definition — Finite limit (convergent sequence).**
> We say that a sequence $(u_n)$ has the real number $L$ as its limit when:
> **Every open interval containing $L$ contains all terms of the sequence from a certain rank onward.**
> We then write:
> $$\lim_{n \to +\infty} u_n = L.$$
> A sequence that has a finite real limit $L$ is said to be **convergent**. Otherwise, it is said to be **divergent**.

**Geometric and dynamic translation:**
Imagine a game between two players: a *Challenger* and a *Defender*.
1. The Challenger chooses an open interval $]a ; b[$ around $L$, as narrow and microscopic as desired (for example $]L - 0.001 \,;\, L + 0.001[$). This is the “target”.
2. The Defender must find an integer rank $N$ beyond which **all** subsequent terms $u_N, u_{N+1}, u_{N+2}, \dots$ fall within the target, never leaving it again.
If the Defender has a winning strategy regardless of the interval imposed at the start, then the sequence converges to $L$.

> **💡 Did you know?** In formalized symbols at the university level, this is written with the quantifiers $\forall$ (“for all”) and $\exists$ (“there exists”):
> $$\forall \varepsilon > 0, \;\exists N \in \mathbb{N}, \;\forall n \geq N, \; |u_n - L| < \varepsilon.$$
> In high school, the official curriculum uses the equivalent formulation with open intervals: *“for every open interval $I$ containing $L$, there exists an integer $N$ such that for all $n \geq N$, $u_n \in I$”*.

#### 2.3 Divergent Sequence toward $+\infty$ or $-\infty$

A sequence does not always converge to a number. It can explode toward infinity, or oscillate indefinitely without ever settling down.

> **📐 Definition — Infinite limit.**
> - We say that a sequence $(u_n)$ has limit $+\infty$ if every interval of the form $]A ; +\infty[$ (where $A$ is an arbitrary real number) contains all terms of the sequence from a certain rank onward:
>   $$\lim_{n \to +\infty} u_n = +\infty.$$
> - We say that a sequence $(u_n)$ has limit $-\infty$ if every interval of the form $]-\infty ; B[$ (where $B$ is an arbitrary real number) contains all terms of the sequence from a certain rank onward:
>   $$\lim_{n \to +\infty} u_n = -\infty.$$

**Concrete meaning:** Set a barrier $A$ as high as you want (a billion, ten billion...). From a certain rank $N$ onward, the sequence crosses above this barrier and never drops back below it.

> **⚠️ Caution, trap! — “Divergent” does not mean “tends to infinity”.**
> A divergent sequence is simply a sequence that **does not converge** to a finite real number.
> - The sequence $u_n = n^2$ diverges to $+\infty$.
> - The sequence $v_n = (-1)^n$ (which alternates $+1, -1, +1, -1 \dots$) is **divergent**, but it tends neither to $+\infty$ nor to $-\infty$! It remains bounded between $-1$ and $1$, but has no limit.

#### 2.4 Uniqueness of the Limit

> **📐 Fundamental Property — Uniqueness.**
> When a sequence $(u_n)$ admits a limit (finite or infinite), **this limit is unique**. A sequence cannot converge to two distinct numbers at the same time.

*Why?* If $u_n$ converged both to $L_1$ and $L_2$ with $L_1 \neq L_2$, we could surround $L_1$ and $L_2$ with two small disjoint intervals (not touching each other). Beyond a certain rank, the terms $u_n$ would have to lie simultaneously in both intervals: impossible!

---

### 3. Reference Sequences and Their Limits

The following table gathers the fundamental building blocks from which all other limits are constructed:

| Sequence $u_n$ ($n \geq 1$) | Limit at $+\infty$ | Intuitive Justification |
| :---: | :---: | :--- |
| $k$ (constant) | $k$ | All terms are already equal to $k$. |
| $\dfrac{1}{n}$ | $0$ | Sharing 1 cake among a billion guests leaves a crumb. |
| $\dfrac{1}{n^2}$, $\dfrac{1}{n^p}$ ($p \geq 1$) | $0$ | The denominator explodes even faster. |
| $\dfrac{1}{\sqrt{n}}$ | $0$ | $\sqrt{n}$ grows to $+\infty$, its reciprocal shrinks to $0$. |
| $n$, $n^2$, $n^p$ ($p \geq 1$) | $+\infty$ | Powers of integers exceed any bound. |
| $\sqrt{n}$ | $+\infty$ | Even though it slows down, it has no ceiling. |

---

### 4. Operations on Limits and Indeterminate Forms

When adding, multiplying, or dividing two sequences with known limits, mathematical common sense applies most of the time... except in four ambiguous situations called **Indeterminate Forms** (denoted I.F.).

#### 4.1 Direct Algebraic Rules

If $\lim u_n = L$ and $\lim v_n = L'$ (with $L, L' \in \mathbb{R}$):
- **Sum:** $\lim (u_n + v_n) = L + L'$
- **Product:** $\lim (u_n \times v_n) = L \times L'$
- **Quotient:** $\lim \left(\dfrac{u_n}{v_n}\right) = \dfrac{L}{L'}$ (provided that $L' \neq 0$).

With infinities:
- A finite number $+$ infinity yields infinity: $5 + (+\infty) = +\infty$.
- $(+\infty) + (+\infty) = +\infty$ and $(-\infty) + (-\infty) = -\infty$.
- Sign rule for products: $(+\infty) \times (-\infty) = -\infty$, $(-3) \times (-\infty) = +\infty$.
- A finite number divided by infinity yields $0$: $\dfrac{L}{\pm\infty} = 0$.
- A non-zero number divided by an infinitely small quantity yields infinity: if $u_n \to L > 0$ and $v_n \to 0$ with $v_n > 0$, then $\dfrac{u_n}{v_n} \to +\infty$.

#### 4.2 The Four Indeterminate Forms (I.F.)

A form is called “indeterminate” when **knowledge of the individual limits alone is insufficient to predict the overall outcome**. The result depends on which component is “stronger”:

1. **$\infty - \infty$** (sum of two infinities of opposite signs): who wins between the positive giant and the negative giant?
2. **$0 \times \infty$** (product of an infinitely small and an infinitely large quantity): crushing toward 0 or exploding toward infinity?
3. **$\dfrac{\infty}{\infty}$** (quotient of two infinities): does the numerator run faster than the denominator?
4. **$\dfrac{0}{0}$** (quotient of two infinitely small quantities).

> **⚠️ Caution, trap! — I.F. does not mean “no limit”.**
> “Indeterminate” does not mean the calculation is impossible or that the limit does not exist! It simply means: *“Stop, do not conclude immediately: transform the expression to resolve the ambiguity”*. The primary technique for polynomials and rational fractions is to **factor out the highest-degree term**.

---

### 5. Fundamental Theorems

#### 5.1 Comparison Theorems

> **📐 Comparison Theorem (toward infinity).**
> Let $(u_n)$ and $(v_n)$ be two sequences such that from a certain rank onward:
> $$u_n \geq v_n.$$
> 1. If $\lim\limits_{n \to +\infty} v_n = +\infty$, then $\lim\limits_{n \to +\infty} u_n = +\infty$.
> 2. If $\lim\limits_{n \to +\infty} u_n = -\infty$, then $\lim\limits_{n \to +\infty} v_n = -\infty$.

*Mental image:* If your friend $v_n$ climbs toward the sky without limit and you are constantly standing on their shoulders ($u_n \geq v_n$), you are inevitably propelled toward the sky alongside them.

#### 5.2 The Squeeze Theorem (Sandwich Theorem)

> **📐 Theorem — Squeeze Theorem (Theorem of the Gendarmes).**
> Let $(u_n)$, $(v_n)$, and $(w_n)$ be three real sequences.
> If there exists a rank $N$ from which:
> $$v_n \leq u_n \leq w_n$$
> and if $\lim\limits_{n \to +\infty} v_n = \lim\limits_{n \to +\infty} w_n = L \in \mathbb{R}$,
> then the sequence $(u_n)$ converges and its limit is:
> $$\lim\limits_{n \to +\infty} u_n = L.$$

```
 w_n (upper officer)    ╲
                          ╲
 u_n (trapped suspect)  ───*───────► converges to L
                          ╱
 v_n (lower officer)    ╱
```

*Origin of the French name (« Théorème des Gendarmes »):* If two police officers ($v_n$ and $w_n$) both converge toward the same police station $L$ while keeping the suspect ($u_n$) flanked between them, the suspect has no choice but to enter the police station $L$ as well.

> **✍️ Proof of the Squeeze Theorem.**
> Let $I$ be any open interval containing $L$. By definition of an open interval, there exists a real number $\varepsilon > 0$ such that $]L - \varepsilon \,;\, L + \varepsilon[ \subset I$.
> Since $\lim v_n = L$, there exists an integer $N_1$ such that for all $n \geq N_1$, $L - \varepsilon < v_n < L + \varepsilon$. In particular, $L - \varepsilon < v_n$.
> Since $\lim w_n = L$, there exists an integer $N_2$ such that for all $n \geq N_2$, $L - \varepsilon < w_n < L + \varepsilon$. In particular, $w_n < L + \varepsilon$.
> Moreover, by assumption, $v_n \leq u_n \leq w_n$ for all $n \geq N_0$.
> Now set $N = \max(N_0, N_1, N_2)$. For every integer $n \geq N$, the three conditions hold simultaneously:
> $$L - \varepsilon < v_n \leq u_n \leq w_n < L + \varepsilon \implies u_n \in ]L - \varepsilon \,;\, L + \varepsilon[ \subset I.$$
> Every open interval containing $L$ thus contains all terms $u_n$ from rank $N$ onward. The sequence $(u_n)$ indeed converges to $L$. $\blacksquare$

#### 5.3 Monotone Convergence Theorem

This is one of the most profound theorems in analysis: it allows one to establish that a sequence converges **without even calculating its limit**.

> **📐 Monotone Convergence Theorem.**
> 1. Every sequence that is **increasing and bounded above** converges to a real limit $L$.
> 2. Every sequence that is **decreasing and bounded below** converges to a real limit $L$.

```
 Ceiling (Upper bound M) ───────────────────────────────────
                           Lim L ---------------------------
                            u_n    .-'""'-.
                                 .'        '-.
                                /             '
 u_0 .-'
```

*Vocabulary review:*
- A sequence is **bounded above** by $M$ if for all $n$, $u_n \leq M$.
- A sequence is **bounded below** by $m$ if for all $n$, $u_n \geq m$.
- A sequence is **bounded** if it is both bounded above and bounded below ($m \leq u_n \leq M$).

> **⚠️ Caution, trap! — The upper bound is not necessarily the limit!**
> If an increasing sequence $(u_n)$ is bounded above by $10$, the theorem guarantees that it converges to a limit $L$, and that $L \leq 10$. But the limit $L$ is not necessarily $10$! It could converge to $2$, or to $\sqrt{3}$, because $10$ is merely one ceiling among others.
> Moreover, an increasing sequence that is not bounded above always diverges to $+\infty$.

---

### 6. The Limit of Geometric Sequences $q^n$

The fundamental geometric sequence is defined by $u_n = q^n$ where $q$ is a fixed real number called the common ratio. Its behavior depends on the position of $q$ relative to $-1$ and $1$.

> **📐 Theorem — Limit of $q^n$.**
> - If $q > 1$: $\lim\limits_{n \to +\infty} q^n = +\infty$.
> - If $q = 1$: the sequence is constantly equal to $1$, so $\lim\limits_{n \to +\infty} q^n = 1$.
> - If $-1 < q < 1$: $\lim\limits_{n \to +\infty} q^n = 0$.
> - If $q \leq -1$: the sequence has no limit (it oscillates, alternating signs).

#### Required Baccalaureate Proof (Case $q > 1$)

This proof relies directly on **Bernoulli’s inequality** established in Chapter 43: for any real number $a > 0$ and any integer $n \in \mathbb{N}$, $(1+a)^n \geq 1 + na$.

> **✍️ Proof (Required knowledge).**
> Let $q$ be a real number strictly greater than $1$.
> Set $a = q - 1$. Since $q > 1$, we have $a > 0$.
> We can therefore write: $q = 1 + a$.
> According to Bernoulli's inequality:
> $$q^n = (1 + a)^n \geq 1 + na.$$
> Now, since $a > 0$, the linear sequence $1 + na$ tends to $+\infty$:
> $$\lim_{n \to +\infty} (1 + na) = +\infty.$$
> By the comparison theorem (5.1), since $q^n \geq 1 + na$ for all $n$, we deduce immediately:
> $$\lim_{n \to +\infty} q^n = +\infty. \quad \blacksquare$$

*Consequences for the case $0 < q < 1$:*
If $0 < q < 1$, set $q' = \frac{1}{q} > 1$.
Then $q^n = \frac{1}{(q')^n}$. Since $(q')^n \to +\infty$, the quotient tends to $0$: $\lim q^n = 0$.
If $-1 < q < 0$, we have $|q^n| = |q|^n \to 0$ because $0 < |q| < 1$, whence $q^n \to 0$ by the squeeze theorem $-|q|^n \leq q^n \leq |q|^n$.

---

### 7. Threshold Algorithm in Python

When a sequence converges to a number or diverges to $+\infty$, a vital practical question arises for engineers, financial analysts, and scientists:
*“From what rank $n$ onward does the sequence cross a given threshold value?”*

Since the stopping rank is not known in advance, one uses an indefinite loop: the `while` loop.

#### Example: Engine Cooling
The temperature of an engine after $n$ minutes follows the decreasing geometric sequence:
$$T_n = 20 + 80 \times 0.9^n.$$
The engine is considered cold as soon as its temperature drops below $30^\circ\text{C}$.

```python
def engine_threshold(threshold):
    """Calculates the number of minutes required to fall below the threshold."""
    n = 0
    T = 100.0  # T_0 = 20 + 80 = 100 °C
    while T > threshold:
        n = n + 1
        T = 20 + 80 * (0.9 ** n)
    return n

# Test for a threshold of 30 °C
minutes = engine_threshold(30)
print(f"The engine drops below 30°C after {minutes} minutes.")
# Output: 20 minutes (since T_19 ≈ 30.8 °C and T_20 ≈ 29.7 °C)
```

> **🧭 Method — Standard structure of a threshold algorithm on the Bac:**
> 1. Initialize the rank counter: `n = 0`.
> 2. Initialize the sequence value: `u = u_0`.
> 3. Condition of the `while` loop: put the **opposite** condition of what is sought (continue *while* the threshold has not yet been crossed).
> 4. In the loop body: update the term `u` and increment `n = n + 1`.
> 5. Return `n` at the end.

---

### 8. Step-by-Step Worked Examples

#### Worked Example 1 — Using the Definition with an Interval

**Problem:** Consider the sequence $(u_n)_{n \geq 1}$ defined by $u_n = 3 + \dfrac{2}{n}$.
1. What is the conjectured limit $L$ of the sequence?
2. Determine a rank $N$ from which all terms $u_n$ belong to the open interval $]2.99 \,;\, 3.01[$.

**Solution:**
1. Since $\lim\limits_{n \to +\infty} \frac{1}{n} = 0$, we have $\lim\limits_{n \to +\infty} u_n = 3 + 2 \times 0 = 3$. The limit is $L = 3$.
2. The interval $]2.99 \,;\, 3.01[$ is written $]3 - 0.01 \,;\, 3 + 0.01[$.
We seek the values of $n$ for which $u_n \in ]2.99 \,;\, 3.01[$:
$$2.99 < 3 + \frac{2}{n} < 3.01.$$
Since $\frac{2}{n} > 0$ for all $n \geq 1$, the left inequality $2.99 < 3 + \frac{2}{n}$ is always true.
It remains to satisfy the right inequality:
$$3 + \frac{2}{n} < 3.01 \iff \frac{2}{n} < 0.01 \iff \frac{2}{n} < \frac{1}{100} \iff n > 200.$$
Since $n$ is an integer, starting from rank $N = 201$, all terms $u_n$ for $n \geq 201$ are guaranteed to lie within the interval $]2.99 \,;\, 3.01[$.

---

#### Worked Example 2 — Resolving a Rational Indeterminacy $\frac{\infty}{\infty}$

**Problem:** Determine the limit of the sequence $(u_n)$ defined for all $n \geq 1$ by:
$$u_n = \frac{5n^2 - 3n + 2}{2n^2 + 7}.$$

**Solution:**
- Numerator: $\lim (5n^2 - 3n + 2) = +\infty$.
- Denominator: $\lim (2n^2 + 7) = +\infty$.
This is an Indeterminate Form of the type “$\frac{\infty}{\infty}$”.
*Method: factor out the dominant term ($n^2$) from both numerator and denominator:*
$$u_n = \frac{n^2 \left(5 - \dfrac{3}{n} + \dfrac{2}{n^2}\right)}{n^2 \left(2 + \dfrac{7}{n^2}\right)}.$$
For $n \geq 1$, cancel out $n^2 \neq 0$:
$$u_n = \frac{5 - \dfrac{3}{n} + \dfrac{2}{n^2}}{2 + \dfrac{7}{n^2}}.$$
Now:
$\lim \dfrac{3}{n} = 0$, $\lim \dfrac{2}{n^2} = 0$, so $\lim \left(5 - \dfrac{3}{n} + \dfrac{2}{n^2}\right) = 5$.
$\lim \dfrac{7}{n^2} = 0$, so $\lim \left(2 + \dfrac{7}{n^2}\right) = 2$.
By the quotient rule for limits, we conclude irrefutably:
$$\lim_{n \to +\infty} u_n = \frac{5}{2}.$$

---

#### Worked Example 3 — Squeeze Theorem and Trigonometry

**Problem:** Determine the limit of the sequence $(v_n)_{n \geq 1}$ defined by:
$$v_n = \frac{3 + (-1)^n \cos(n)}{n + \sqrt{n}}.$$

**Solution:**
The functions $\cos(n)$ and $(-1)^n$ oscillate endlessly and have no limit as $n \to +\infty$. It is impossible to apply direct algebraic rules. We immediately turn to the **squeeze theorem**.
For any integer $n$, $-1 \leq \cos(n) \leq 1$ and $(-1)^n \in \{-1 ; 1\}$.
Thus, the product $(-1)^n \cos(n)$ remains bounded between $-1$ and $1$:
$$-1 \leq (-1)^n \cos(n) \leq 1.$$
Add 3 to each part:
$$3 - 1 \leq 3 + (-1)^n \cos(n) \leq 3 + 1 \iff 2 \leq 3 + (-1)^n \cos(n) \leq 4.$$
Since for all $n \geq 1$, the denominator $n + \sqrt{n}$ is strictly positive, we can divide without changing the direction of the inequalities:
$$\frac{2}{n + \sqrt{n}} \leq v_n \leq \frac{4}{n + \sqrt{n}}.$$
Examine the limits of both bounding sequences:
- $\lim (n + \sqrt{n}) = +\infty$, so $\lim\limits_{n \to +\infty} \dfrac{2}{n + \sqrt{n}} = 0$.
- Likewise, $\lim\limits_{n \to +\infty} \dfrac{4}{n + \sqrt{n}} = 0$.
Both bounding sequences converge to the same limit $0$.
By the **squeeze theorem**, the sequence $(v_n)$ converges and:
$$\lim_{n \to +\infty} v_n = 0.$$

---

#### Worked Example 4 — Geometric Sum and Convergence

**Problem:** Consider the sequence $(S_n)$ defined for any integer $n \geq 1$ by:
$$S_n = \sum_{k=1}^n \left(\frac{2}{3}\right)^k = \frac{2}{3} + \left(\frac{2}{3}\right)^2 + \dots + \left(\frac{2}{3}\right)^n.$$
1. Express $S_n$ in closed form without summation notation.
2. Determine the limit of $S_n$ as $n \to +\infty$.

**Solution:**
1. $S_n$ is the sum of the first $n$ consecutive terms of a geometric sequence with first term $a = \frac{2}{3}$ and common ratio $q = \frac{2}{3}$.
The geometric sum formula gives (with $q \neq 1$):
$$\text{Sum} = \text{First term} \times \frac{1 - q^{\text{number of terms}}}{1 - q}.$$
Here:
$$S_n = \frac{2}{3} \times \frac{1 - \left(\frac{2}{3}\right)^n}{1 - \frac{2}{3}} = \frac{2}{3} \times \frac{1 - \left(\frac{2}{3}\right)^n}{\frac{1}{3}} = \frac{2}{3} \times 3 \times \left(1 - \left(\frac{2}{3}\right)^n\right) = 2 \left(1 - \left(\frac{2}{3}\right)^n\right).$$
2. Since $-1 < \frac{2}{3} < 1$, according to the theorem on geometric sequences:
$$\lim_{n \to +\infty} \left(\frac{2}{3}\right)^n = 0.$$
By limit operations:
$$\lim_{n \to +\infty} S_n = 2(1 - 0) = 2.$$

---

#### Worked Example 5 — Comparison toward Infinity

**Problem:** Prove that the sequence $(w_n)$ defined for all $n \geq 1$ by $w_n = 2n^2 - 5\sin(n) + (-1)^n$ tends to $+\infty$.

**Solution:**
For any integer $n$, we have $-1 \leq \sin(n) \leq 1$, so $-5 \leq -5\sin(n) \leq 5$, and $(-1)^n \geq -1$.
Consequently:
$$w_n = 2n^2 - 5\sin(n) + (-1)^n \geq 2n^2 - 5 - 1 = 2n^2 - 6.$$
Now:
$$\lim_{n \to +\infty} (2n^2 - 6) = +\infty.$$
Since $w_n \geq 2n^2 - 6$ for all $n \geq 1$, by the **comparison theorem**, we conclude immediately:
$$\lim_{n \to +\infty} w_n = +\infty.$$

---

#### Worked Example 6 — Recurrence Sequence and Monotone Convergence

**Problem:** Let $(u_n)$ be the sequence defined by $u_0 = 0$ and for all $n \in \mathbb{N}$ by:
$$u_{n+1} = \frac{1}{2}u_n + 3.$$
1. Prove by induction that for all $n \in \mathbb{N}$, $u_n < 6$.
2. Prove that the sequence $(u_n)$ is strictly increasing.
3. Deduce that the sequence converges to a limit $L$ to be determined.

**Solution:**
1. **Proof by induction:**
For $n \in \mathbb{N}$, let $\mathcal{P}(n)$ be the statement: “$u_n < 6$”.
- *Base step:* $u_0 = 0 < 6$. Thus $\mathcal{P}(0)$ is true.
- *Inductive step:* Let $n \in \mathbb{N}$ be fixed. Assume $\mathcal{P}(n)$ is true, that is, $u_n < 6$.
Then:
$$\frac{1}{2}u_n < \frac{1}{2} \times 6 = 3 \implies \frac{1}{2}u_n + 3 < 3 + 3 = 6 \implies u_{n+1} < 6.$$
Thus $\mathcal{P}(n+1)$ is true.
- *Conclusion:* By induction, for all natural numbers $n$, $u_n < 6$. The sequence is **bounded above by 6**.

2. **Monotonicity:**
Compute the difference $u_{n+1} - u_n$:
$$u_{n+1} - u_n = \left(\frac{1}{2}u_n + 3\right) - u_n = -\frac{1}{2}u_n + 3 = \frac{1}{2}(6 - u_n).$$
From question 1, $u_n < 6$, hence $6 - u_n > 0$.
Consequently, $u_{n+1} - u_n > 0$, which proves that the sequence $(u_n)$ is **strictly increasing**.

3. **Convergence and calculation of the limit:**
Since the sequence $(u_n)$ is increasing and bounded above by 6, the **monotone convergence theorem** ensures that it converges to a finite real limit $L \leq 6$.
Let us determine $L$:
Since $\lim u_n = L$, we also have $\lim u_{n+1} = L$.
Taking the limit in the recurrence relation $u_{n+1} = \frac{1}{2}u_n + 3$, we obtain:
$$L = \frac{1}{2}L + 3 \iff L - \frac{1}{2}L = 3 \iff \frac{1}{2}L = 3 \iff L = 6.$$
The sequence $(u_n)$ converges to $6$.

---

### Key Takeaways

1. **Definition of convergence:** $\lim u_n = L$ means that every open interval containing $L$ contains all terms of the sequence from a rank $N$ onward.
2. **Divergence toward $+\infty$:** every interval $]A ; +\infty[$ contains all terms of the sequence from a certain rank onward.
3. **Indeterminate Forms:** $\infty - \infty$, $0 \times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$. For a quotient of polynomials in $n$, always factor out the highest-degree term in both the numerator and the denominator.
4. **Squeeze Theorem:** If $v_n \leq u_n \leq w_n$ and $\lim v_n = \lim w_n = L$, then $\lim u_n = L$.
5. **Comparison Theorem:** If $u_n \geq v_n$ and $\lim v_n = +\infty$, then $\lim u_n = +\infty$.
6. **Geometric Sequences $q^n$:**
   - If $q > 1$, $\lim q^n = +\infty$ (proven via Bernoulli's inequality $(1+a)^n \geq 1 + na$).
   - If $-1 < q < 1$, $\lim q^n = 0$.
   - If $q \leq -1$, no limit.
7. **Monotone Convergence:** Increasing $+$ bounded above $\implies$ convergent. Decreasing $+$ bounded below $\implies$ convergent.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 44.1.** Determine the limit of each of the following sequences as $n \to +\infty$:
1. $u_n = 4 - \dfrac{7}{n} + \dfrac{3}{n^2}$
2. $v_n = -3n^3 + 500$
3. $w_n = 5 \times 0.4^n$
4. $t_n = 2 \times 1.05^n$

**Exercise 44.2.** For each of the following geometric sequences, state whether it converges and, if so, give its limit:
1. $a_n = \left(-\dfrac{3}{4}\right)^n$
2. $b_n = \left(\dfrac{7}{5}\right)^n$
3. $c_n = (-1.2)^n$
4. $d_n = \dfrac{4^n}{3^n}$

**Exercise 44.3.** Calculate the limit of the following rational sequences:
1. $u_n = \dfrac{3n + 1}{5n - 2}$
2. $v_n = \dfrac{7n^2 - 4}{2n^3 + n}$
3. $w_n = \dfrac{n^4 - 1}{100n^3 + 5}$

**Exercise 44.4.** Let $u_n = 5 + \dfrac{1}{n}$. Find a rank $N$ from which $u_n \in ]4.999 \,;\, 5.001[$.

**Exercise 44.5.** Prove that for all $n \geq 1$, $\dfrac{-1}{n} \leq \dfrac{\sin(n)}{n} \leq \dfrac{1}{n}$. Deduce $\lim\limits_{n \to +\infty} \dfrac{\sin(n)}{n}$.

**Exercise 44.6.** A sequence $(u_n)$ satisfies for all $n \in \mathbb{N}$: $u_n \geq 3n^2 - 10n$. Determine its limit at $+\infty$.

**Exercise 44.7.** A bird population initially numbers 500 individuals and decreases by 5% per year.
1. Express the population $P_n$ after $n$ years.
2. What is the limit of $P_n$ as $n \to +\infty$?

**Exercise 44.8.** Write a Python function `geometric_threshold(q, A)` that takes as input a ratio $q > 1$ and a threshold $A > 0$, and returns the first rank $n$ such that $q^n > A$.

---

#### Level ★★ (Guided Reflection and Baccalaureate Style)

**Exercise 44.9 (Resolving Indeterminacy with Square Roots).**
Let $u_n = \sqrt{n+1} - \sqrt{n}$ for $n \geq 0$.
1. Show that this is an indeterminate form in its initial state.
2. By multiplying by the conjugate expression, show that $u_n = \dfrac{1}{\sqrt{n+1} + \sqrt{n}}$.
3. Deduce the limit of $(u_n)$.

**Exercise 44.10 (Baccalaureate Style: Complete Study of a Recurrence Sequence).**
Consider the sequence $(u_n)$ defined by $u_0 = 1$ and for all $n \in \mathbb{N}$:
$$u_{n+1} = \frac{2u_n + 3}{u_n + 2}.$$
1. Prove by induction that for all $n \in \mathbb{N}$, $1 \leq u_n \leq \sqrt{3}$.
2. Prove that for all $n \in \mathbb{N}$, $u_{n+1} - u_n = \dfrac{3 - u_n^2}{u_n + 2}$. Deduce the monotonicity of the sequence $(u_n)$.
3. Justify that the sequence $(u_n)$ converges and determine its exact limit.

**Exercise 44.11 (Arithmetico-Geometric Sequence and Bank Investment).**
A principal of €$10,000$ is invested at compound interest at an annual rate of 3%. Each year, the account holder deposits an additional €$500$ immediately after the interest is credited. Let $C_n$ be the capital after $n$ years ($C_0 = 10,000$).
1. Express $C_{n+1}$ in terms of $C_n$.
2. Set $v_n = C_n + \alpha$. Determine the real number $\alpha$ so that $(v_n)$ is a geometric sequence.
3. Deduce the explicit expression for $C_n$ in terms of $n$, then determine $\lim\limits_{n \to +\infty} C_n$.

**Exercise 44.12 (Squeeze Theorem and Finite Sum).**
Consider the sequence $(S_n)$ defined for any integer $n \geq 1$ by:
$$S_n = \sum_{k=1}^n \frac{n}{n^2 + k} = \frac{n}{n^2 + 1} + \frac{n}{n^2 + 2} + \dots + \frac{n}{n^2 + n}.$$
1. Show that for all $k \in \{1 ; 2 ; \dots ; n\}$, we have $\dfrac{n}{n^2 + n} \leq \dfrac{n}{n^2 + k} \leq \dfrac{n}{n^2 + 1}$.
2. Deduce that for all $n \geq 1$: $\dfrac{n^2}{n^2 + n} \leq S_n \leq \dfrac{n^2}{n^2 + 1}$.
3. Deduce the convergence of $(S_n)$ and its limit.

**Exercise 44.13 (True or False with Justifications).**
For each of the following statements, state whether it is true or false, providing a proof or a specific counterexample:
1. “If a sequence converges, then it is bounded.”
2. “If a sequence is bounded, then it converges.”
3. “If for all $n \in \mathbb{N}$, $u_n > 0$ and $(u_n)$ converges to $L$, then $L > 0$.”
4. “If $\lim\limits_{n \to +\infty} u_n^2 = 4$, then $\lim\limits_{n \to +\infty} u_n = 2$.”

**Exercise 44.14 (Geometric Sum and the Runner's Paradox).**
A runner covers successively $100\text{ m}$, then $50\text{ m}$, then $25\text{ m}$, and at each step half of the preceding step.
1. Calculate the total distance covered after $n$ steps.
2. Prove rigorously that the total distance will never exceed $200\text{ m}$, no matter how many steps are completed.

**Exercise 44.15 (Bernoulli's Inequality and Lower Bound).**
Consider the sequence $u_n = 1.01^n$.
1. Using Bernoulli's inequality, give a linear lower bound for $u_n$.
2. Deduce an integer $N$ such that for all $n \geq N$, $u_n \geq 1,000,000$.
3. Is this the smallest integer that satisfies the condition?

**Exercise 44.16 (Threshold Algorithm and Stopping Time).**
Consider the sequence $(u_n)$ defined by $u_0 = 2$ and $u_{n+1} = 0.8 u_n + 1$.
1. Conjecture the limit $L$ of $(u_n)$.
2. Write a Python script to find the smallest integer $n$ such that $|u_n - L| < 10^{-5}$.

**Exercise 44.17 (Study of an Auxiliary Geometric Sequence).**
Let $(u_n)$ be defined by $u_0 = 4$ and $u_{n+1} = \dfrac{u_n}{2u_n + 1}$.
1. Calculate $u_1$ and $u_2$.
2. Assume that $u_n > 0$ for all $n$. Set $v_n = \dfrac{1}{u_n}$. Show that $(v_n)$ is an arithmetic sequence.
3. Deduce the expression for $v_n$, then for $u_n$ in terms of $n$, and determine its limit.

---

#### Level ★★★ (Challenge and In-Depth Study)

**Exercise 44.18 (The Constant $e$ as the Limit of a Sequence).**
Consider the two sequences $(u_n)$ and $(v_n)$ defined for all $n \geq 1$ by:
$$u_n = \left(1 + \frac{1}{n}\right)^n \quad \text{and} \quad v_n = \left(1 + \frac{1}{n}\right)^{n+1}.$$
1. By computing the first few values with a calculator, conjecture the behavior of $(u_n)$ and $(v_n)$.
2. It is given that $(u_n)$ is strictly increasing and that $(v_n)$ is strictly decreasing with $u_n < v_n$. Prove that $\lim\limits_{n \to +\infty} (v_n - u_n) = 0$.
3. What can be deduced about the two sequences? (They converge to Euler's number $e \approx 2.71828$).

**Exercise 44.19 (Gauss's Arithmetico-Geometric Mean Sequence).**
Let $a_0 > 0$ and $b_0 > 0$ with $a_0 < b_0$. For all $n \in \mathbb{N}$, define:
$$a_{n+1} = \sqrt{a_n b_n} \quad \text{and} \quad b_{n+1} = \frac{a_n + b_n}{2}.$$
1. Recall why for any strictly positive real numbers $a$ and $b$, we have $\sqrt{ab} \leq \frac{a+b}{2}$.
2. Prove that for all $n \geq 1$, $a_n \leq b_n$.
3. Show that the sequence $(a_n)$ is increasing and that the sequence $(b_n)$ is decreasing.
4. Deduce that both sequences converge to a single common limit (the arithmetic-geometric mean of Gauss).

**Exercise 44.20 (The Koch Snowflake: Infinite Perimeter and Finite Area).**
The Koch snowflake is built in stages starting from an equilateral triangle of side length 1 and area $A_0 = \frac{\sqrt{3}}{4}$. At each stage, the central third of each side is replaced by an outward-pointing equilateral triangle.
1. The perimeter at stage $n$ is given by $P_n = 3 \times \left(\frac{4}{3}\right)^n$. What is the limit of $P_n$?
2. The area at stage $n$ satisfies $A_n = A_0 \left[1 + \frac{3}{5}\left(1 - \left(\frac{4}{9}\right)^n\right)\right]$. Calculate $\lim\limits_{n \to +\infty} A_n$.
3. Comment on the paradoxical geometric result (a figure with an infinite boundary enclosing a strictly bounded, finite area).

**Exercise 44.21 (Cesàro's Theorem — Beyond Syllabus / Olympiad).**
Let $(u_n)$ be a sequence converging to a finite limit $L$. Define the sequence of averages $(c_n)_{n \geq 1}$ by:
$$c_n = \frac{u_1 + u_2 + \dots + u_n}{n}.$$
1. Test this result on the sequence $u_n = 1 + \frac{1}{n}$.
2. Give an example showing that the converse is false (find a sequence $(u_n)$ that does not converge, but whose Cesàro mean $(c_n)$ converges).

**Exercise 44.22 (Fixed-Point Theorem for Sequences).**
Let $f$ be a continuous function on $[0 ; 1]$ such that for all $x \in [0 ; 1]$, $f(x) \in [0 ; 1]$.
Assume further that there exists a constant $k \in ]0 ; 1[$ such that for all $x, y \in [0 ; 1]$:
$$|f(x) - f(y)| \leq k |x - y|.$$
Let $u_0 \in [0 ; 1]$ and $u_{n+1} = f(u_n)$.
1. Show that for all $n \in \mathbb{N}$, $|u_{n+1} - u_n| \leq k^n |u_1 - u_0|$.
2. Prove that the sequence $(u_n)$ converges to the unique solution of $f(x) = x$ in $[0 ; 1]$.

---

### Solutions

#### Solutions for Level ★

- **44.1:**
  1. $\lim u_n = 4 - 0 + 0 = 4$.
  2. $\lim v_n = -\infty$ because $n^3 \to +\infty$ and $-3 < 0$.
  3. $0 < 0.4 < 1$, so $\lim 0.4^n = 0$, whence $\lim w_n = 0$.
  4. $1.05 > 1$, so $\lim 1.05^n = +\infty$, whence $\lim t_n = +\infty$.

- **44.2:**
  1. Converges to 0 because $|-3/4| = 3/4 < 1$.
  2. Diverges to $+\infty$ because $7/5 > 1$.
  3. Diverges without a limit because $-1.2 \leq -1$ (oscillates with increasing amplitude).
  4. $d_n = (4/3)^n$ with $4/3 > 1$, so it diverges to $+\infty$.

- **44.3:**
  1. Factoring: $u_n = \dfrac{n(3 + 1/n)}{n(5 - 2/n)} = \dfrac{3 + 1/n}{5 - 2/n} \to \dfrac{3}{5}$.
  2. $v_n = \dfrac{n^2(7 - 4/n^2)}{n^3(2 + 1/n^2)} = \dfrac{1}{n} \times \dfrac{7 - 4/n^2}{2 + 1/n^2} \to 0 \times \dfrac{7}{2} = 0$.
  3. $w_n = \dfrac{n^4(1 - 1/n^4)}{n^3(100 + 5/n^3)} = n \times \dfrac{1 - 1/n^4}{100 + 5/n^3} \to +\infty$.

- **44.4:** We require $4.999 < 5 + \dfrac{1}{n} < 5.001 \iff 0 < \dfrac{1}{n} < 0.001 = \dfrac{1}{1000} \iff n > 1000$. The minimal rank is $N = 1001$.

- **44.5:** For all $n \geq 1$, $-1 \leq \sin(n) \leq 1$. Dividing by $n > 0$ yields $\dfrac{-1}{n} \leq \dfrac{\sin(n)}{n} \leq \dfrac{1}{n}$. Since $\lim (-1/n) = \lim (1/n) = 0$, by the squeeze theorem, $\lim\limits_{n \to +\infty} \dfrac{\sin(n)}{n} = 0$.

- **44.6:** For $n \geq 4$, $3n^2 - 10n = n(3n - 10) \to +\infty$. Since $u_n \geq 3n^2 - 10n$, by comparison, $\lim u_n = +\infty$.

- **44.7:**
  1. A 5% decrease corresponds to multiplying by $1 - 0.05 = 0.95$. Thus $P_n = 500 \times 0.95^n$.
  2. Since $0 < 0.95 < 1$, $\lim 0.95^n = 0$, so $\lim P_n = 0$ (theoretical extinction of the population).

- **44.8:**
```python
def geometric_threshold(q, A):
    n = 0
    u = 1.0
    while u <= A:
        n += 1
        u = q ** n
    return n
```

---

#### Solutions for Level ★★

- **44.9:**
  1. $\lim \sqrt{n+1} = +\infty$ and $\lim \sqrt{n} = +\infty$, so this is an I.F. of type “$\infty - \infty$”.
  2. For $n \geq 0$:
     $$\sqrt{n+1} - \sqrt{n} = \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} = \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}}.$$
  3. The denominator tends to $+\infty$, so by the quotient rule, $\lim u_n = 0$.

- **44.10:**
  1. *Base step:* $n = 0$, $u_0 = 1 \in [1 ; \sqrt{3}]$ because $\sqrt{3} \approx 1.732$.
     *Inductive step:* Assume $1 \leq u_n \leq \sqrt{3}$.
     The function $f(x) = \frac{2x+3}{x+2} = 2 - \frac{1}{x+2}$ is strictly increasing on $[1 ; \sqrt{3}]$.
     Therefore $f(1) \leq f(u_n) \leq f(\sqrt{3})$.
     Now $f(1) = 5/3 \approx 1.67 \geq 1$.
     And $f(\sqrt{3}) = \frac{2\sqrt{3}+3}{\sqrt{3}+2} = \frac{\sqrt{3}(2+\sqrt{3})}{\sqrt{3}+2} = \sqrt{3}$.
     Thus $1 \leq u_{n+1} \leq \sqrt{3}$.
     *Conclusion:* For all $n \in \mathbb{N}$, $1 \leq u_n \leq \sqrt{3}$.
  2. $u_{n+1} - u_n = \frac{2u_n+3}{u_n+2} - u_n = \frac{2u_n+3 - u_n(u_n+2)}{u_n+2} = \frac{3 - u_n^2}{u_n+2}$.
     Since $u_n \leq \sqrt{3}$, we have $u_n^2 \leq 3$, so $3 - u_n^2 \geq 0$. Since $u_n \geq 1$, $u_n+2 > 0$.
     Therefore $u_{n+1} - u_n \geq 0$: the sequence is increasing.
  3. The sequence is increasing and bounded above by $\sqrt{3}$, so it converges to a limit $L \in [1 ; \sqrt{3}]$.
     Taking the limit: $L = \frac{2L+3}{L+2} \iff L(L+2) = 2L+3 \iff L^2 = 3$.
     Since $L \geq 1$, we have $L = \sqrt{3}$.

- **44.11:**
  1. Increasing by 3% and then adding 500 yields: $C_{n+1} = 1.03 C_n + 500$.
  2. $v_{n+1} = C_{n+1} + \alpha = 1.03 C_n + 500 + \alpha$. We want $v_{n+1} = 1.03 v_n = 1.03(C_n + \alpha) = 1.03 C_n + 1.03 \alpha$.
     Equating coefficients: $500 + \alpha = 1.03 \alpha \iff 0.03 \alpha = 500 \iff \alpha = \frac{500}{0.03} = \frac{50,000}{3}$.
  3. $(v_n)$ is a geometric sequence with ratio $q = 1.03$ and first term $v_0 = C_0 + \frac{50,000}{3} = 10,000 + \frac{50,000}{3} = \frac{80,000}{3}$.
     Hence $v_n = \frac{80,000}{3} \times 1.03^n$, whence $C_n = v_n - \alpha = \frac{80,000}{3} \times 1.03^n - \frac{50,000}{3}$.
     Since $1.03 > 1$, $\lim 1.03^n = +\infty$, so $\lim C_n = +\infty$.

- **44.12:**
  1. For $1 \leq k \leq n$, we have $n^2 + 1 \leq n^2 + k \leq n^2 + n$. Inverting strictly positive quantities: $\frac{1}{n^2 + n} \leq \frac{1}{n^2 + k} \leq \frac{1}{n^2 + 1}$. Multiplying by $n > 0$ yields the requested inequality.
  2. Summing these inequalities for $k$ from 1 to $n$, the sum contains $n$ terms:
     $n \times \frac{n}{n^2 + n} \leq S_n \leq n \times \frac{n}{n^2 + 1} \iff \frac{n^2}{n^2 + n} \leq S_n \leq \frac{n^2}{n^2 + 1}$.
  3. $\lim \frac{n^2}{n^2+n} = \lim \frac{n^2}{n^2(1+1/n)} = 1$ and $\lim \frac{n^2}{n^2+1} = 1$. By the squeeze theorem, $\lim S_n = 1$.

- **44.13:**
  1. **True.** If $u_n \to L$, then from a rank $N$ onward, all terms lie in $]L-1 ; L+1[$. The preceding terms $u_0, \dots, u_{N-1}$ are finite in number, so we take the minimum and maximum of the finite set $\{u_0, \dots, u_{N-1}, L-1, L+1\}$, which bounds the entire sequence.
  2. **False.** Counterexample: $u_n = (-1)^n$ is bounded between $-1$ and $1$, but does not converge.
  3. **False.** Counterexample: $u_n = \frac{1}{n+1} > 0$ for all $n \in \mathbb{N}$, but $\lim u_n = 0$ (which is not strictly positive). Taking the limit converts strict inequalities into non-strict inequalities.
  4. **False.** Counterexample: $u_n = 2 \times (-1)^n$. Then $u_n^2 = 4$ for all $n$, so $\lim u_n^2 = 4$, but $(u_n)$ oscillates between $2$ and $-2$ and has no limit.

- **44.14:**
  1. Distance at step $n$: $D_n = 100 \sum_{k=0}^{n-1} \left(\frac{1}{2}\right)^k = 100 \times \frac{1 - (1/2)^n}{1 - 1/2} = 200 \left(1 - \frac{1}{2^n}\right)$.
  2. For all $n \geq 1$, $\frac{1}{2^n} > 0$, so $1 - \frac{1}{2^n} < 1$, which implies $D_n < 200$. Moreover $\lim D_n = 200\text{ m}$. The distance tends toward $200\text{ m}$ without ever exceeding it for any finite $n$.

- **44.15:**
  1. With $a = 0.01$, Bernoulli gives: $1.01^n = (1 + 0.01)^n \geq 1 + 0.01n$.
  2. We seek $1 + 0.01n \geq 1,000,000 \iff 0.01n \geq 999,999 \iff n \geq 99,999,900$. The rank $N = 99,999,900$ works for sure.
  3. No, this is not the smallest: the exponential power grows far faster than the linear lower bound. The actual threshold (calculable using logarithms in Chapter 48) is $n = \lceil \frac{\ln(10^6)}{\ln(1.01)} \rceil = 1388$.

- **44.16:**
  1. If $u_n \to L$, then $L = 0.8 L + 1 \iff 0.2 L = 1 \iff L = 5$.
  2. Python script:
```python
n = 0
u = 2.0
while abs(u - 5.0) >= 1e-5:
    n += 1
    u = 0.8 * u + 1.0
print(f"Rank n found: {n}")
```

- **44.17:**
  1. $u_1 = \frac{4}{2(4)+1} = \frac{4}{9}$. $u_2 = \frac{4/9}{2(4/9)+1} = \frac{4/9}{17/9} = \frac{4}{17}$.
  2. $v_{n+1} = \frac{1}{u_{n+1}} = \frac{2u_n+1}{u_n} = 2 + \frac{1}{u_n} = v_n + 2$. $(v_n)$ is therefore an arithmetic sequence with common difference $r = 2$ and first term $v_0 = \frac{1}{u_0} = \frac{1}{4}$.
  3. $v_n = \frac{1}{4} + 2n = \frac{8n+1}{4}$. By inversion: $u_n = \frac{1}{v_n} = \frac{4}{8n+1}$.
     We immediately deduce: $\lim\limits_{n \to +\infty} u_n = 0$.

---

#### Solutions for Level ★★★

- **44.18:**
  1. For $n = 10$, $u_{10} \approx 2.5937$, $v_{10} \approx 2.8531$. For $n = 1000$, $u_{1000} \approx 2.7169$, $v_{1000} \approx 2.7196$. Both seem to tighten around $2.718...$
  2. $v_n - u_n = \left(1 + \frac{1}{n}\right)^n \left(1 + \frac{1}{n} - 1\right) = \frac{1}{n} u_n$. Since $u_n < v_n \leq v_1 = 4$, the sequence $(u_n)$ is bounded above by 4. Thus $0 < v_n - u_n \leq \frac{4}{n}$. By the squeeze theorem, $\lim (v_n - u_n) = 0$.
  3. One is increasing, the other decreasing, and their difference tends to 0: these are two **adjacent sequences**. They converge to a single common limit, which defines the number $e \approx 2.71828$.

- **44.19:**
  1. $(\sqrt{a} - \sqrt{b})^2 \geq 0 \iff a - 2\sqrt{ab} + b \geq 0 \iff \frac{a+b}{2} \geq \sqrt{ab}$ (arithmetic-mean-geometric-mean inequality).
  2. For $n \geq 0$, $b_{n+1} - a_{n+1} = \frac{a_n+b_n}{2} - \sqrt{a_n b_n} \geq 0$, so $a_{n+1} \leq b_{n+1}$ for all $n \geq 0$.
  3. $a_{n+1} - a_n = \sqrt{a_n b_n} - a_n = \sqrt{a_n}(\sqrt{b_n} - \sqrt{a_n}) \geq 0$ because $b_n \geq a_n$. Hence $(a_n)$ is increasing.
     Similarly, $b_{n+1} - b_n = \frac{a_n - b_n}{2} \leq 0$, so $(b_n)$ is decreasing.
  4. $(a_n)$ is increasing and bounded above by $b_0$, so it converges to $L_a$. $(b_n)$ is decreasing and bounded below by $a_0$, so it converges to $L_b$.
     Taking the limit in $b_{n+1} = \frac{a_n+b_n}{2}$, we have $L_b = \frac{L_a+L_b}{2} \iff L_a = L_b$. The two sequences converge to the same value, denoted $M(a_0, b_0)$.

- **44.20:**
  1. Since $\frac{4}{3} > 1$, $\lim\limits_{n \to +\infty} \left(\frac{4}{3}\right)^n = +\infty$, so the perimeter $P_n$ tends to $+\infty$.
  2. Since $0 < \frac{4}{9} < 1$, $\lim \left(\frac{4}{9}\right)^n = 0$.
     Therefore $\lim A_n = A_0 \left(1 + \frac{3}{5}(1 - 0)\right) = A_0 \left(1 + \frac{3}{5}\right) = \frac{8}{5} A_0 = \frac{8}{5} \times \frac{\sqrt{3}}{4} = \frac{2\sqrt{3}}{5}$.
  3. The Koch snowflake possesses an infinite perimeter while enclosing a strictly bounded, finite area. It shows that fractal geometry shatters our standard Euclidean intuition.

- **44.21:**
  1. $u_n \to 1$. $c_n = \frac{1}{n} \sum_{k=1}^n \left(1 + \frac{1}{k}\right) = 1 + \frac{1}{n}\sum_{k=1}^n \frac{1}{k}$. Now the harmonic sum $H_n = \sum_{k=1}^n \frac{1}{k}$ grows asymptotically as $\ln(n)$, so $\frac{H_n}{n} \to 0$. Thus $c_n \to 1$.
  2. Take $u_n = (-1)^n$. The sequence $(u_n)$ oscillates and diverges.
     However, $S_n = u_1 + \dots + u_n$ is equal to $-1$ if $n$ is odd and $0$ if $n$ is even.
     Hence $-\frac{1}{n} \leq c_n \leq 0$, which implies by the squeeze theorem that $\lim c_n = 0$. The Cesàro mean converges to 0 even though $(u_n)$ diverges!

- **44.22:**
  1. By induction: for $n = 0$, $|u_1 - u_0| \leq k^0 |u_1 - u_0|$ is trivially true.
     Assume $|u_{n+1} - u_n| \leq k^n |u_1 - u_0|$.
     Then $|u_{n+2} - u_{n+1}| = |f(u_{n+1}) - f(u_n)| \leq k |u_{n+1} - u_n| \leq k \times k^n |u_1 - u_0| = k^{n+1} |u_1 - u_0|$.
  2. Since $0 < k < 1$, $\lim k^n = 0$. The steps $|u_{n+1} - u_n|$ become infinitely small at a geometric rate. The sequence is a Cauchy sequence in a closed bounded interval, so it converges to a real number $L \in [0 ; 1]$. By continuity of $f$, $\lim f(u_n) = f(L)$, whence $L = f(L)$. Uniqueness follows from the fact that if $f(x)=x$ and $f(y)=y$, $|x - y| = |f(x) - f(y)| \leq k |x - y| \implies (1 - k)|x - y| \leq 0$, which requires $x = y$ since $1 - k > 0$.

---

### The Question That Opens What Follows

Until now, our counter $n$ was a natural number taking step-by-step jumps: $n = 0, 1, 2, 3...$
But what happens if the variable is no longer a runner with discrete steps, but a bird flying seamlessly through the sky, or a rocket accelerating at every microsecond?
How can we define the limit of a function $f(x)$ when the real variable $x$ glides continuously toward infinity, or worse, when it approaches a point where the function seems to tear apart or explode?

This is the mystery of function limits and the invisible lines that guide curves through space: **asymptotes**. See you in Chapter 45.
