# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 43: The Endless Staircase and the Dominoes

> *“To climb an infinite staircase, it is not necessary to see the top step. It suffices to be certain of two things: that one can set foot upon the first, and that from any step one always knows how to climb to the next.”*

---

### What You Are About to Discover

- Why **verifying** a property on 10, 100, or even a billion examples **proves** nothing, and how seemingly “obvious” conjectures have collapsed.
- **Proof by mathematical induction**: a three-stage logical engine (**initialization / base step**, **inductive step / heredity**, **conclusion**) that allows demonstrating an infinity of statements in a finite number of lines.
- How to **write** an impeccable induction proof, exactly as expected on the Baccalauréat and advanced examinations.
- The celebrated **Bernoulli's inequality** $(1+a)^n \geq 1 + na$, the first required core proof of the year, which will prove essential starting in the very next chapter.
- Common **pitfalls**: induction without a base step, heredity that breaks at a single link (the "all horses are the same color" paradox), induction that "won't go through," and how to strengthen the induction hypothesis.

---

### 1. The Problem: The Trap of Examples

#### 1.1 Odd Numbers and Squares

Take a handful of pebbles and arrange them in nested squares, just as the Pythagoreans did in the sand:

```
  ●        ● ○        ● ○ ●        ● ○ ● ○
           ○ ○        ○ ○ ●        ○ ○ ● ○
                      ● ● ●        ● ● ● ○
                                   ○ ○ ○ ○
  1      1 + 3      1 + 3 + 5    1 + 3 + 5 + 7
  = 1     = 4         = 9          = 16
```

Each new L-shaped angle of pebbles (known as a **gnomon**) adds the next odd number, and the square grows by one row and one column. We conjecture:

$$1 + 3 + 5 + \dots + (2n - 1) = n^2.$$

We verify for $n = 1, 2, 3, 4, 5$... it always works. But **is it true for every $n$**? For $n = 10^{100}$? No human will ever carry out the full tally. The drawing convinces our eyes, but a visual diagram only demonstrates a handful of cases.

#### 1.2 Euler's Prime-Generating Polynomial

In 1772, Leonhard Euler noted the polynomial $p(n) = n^2 + n + 41$. Let us compute:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 10 | 20 | 39 |
|---|---|---|---|---|---|---|---|---|---|
| $p(n)$ | 41 | 43 | 47 | 53 | 61 | 71 | 151 | 461 | 1601 |

Every single one of these numbers is **prime**! We can check all 40 values from $n = 0$ to $n = 39$: not a single exception. Forty successes in a row... A hasty thinker would conclude: “$n^2 + n + 41$ is always prime.” And yet:

$$p(40) = 40^2 + 40 + 41 = 1600 + 81 = 1681 = 41 \times 41.$$

It fails. And $p(41) = 41^2 + 41 + 41 = 41 \times 43$ is not prime either.

#### 1.3 Circles and Regions

Place $n$ points on the boundary of a circle, connect every pair of points with a straight chord (choosing points in general position so that no three chords intersect at the same interior point), and count the number of disjoint regions carved out inside the disk:

| Number of points $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Number of regions | 1 | 2 | 4 | 8 | 16 | **31** |

Almost everyone wagers on 32 for $n = 6$: the progression of powers of 2 seems inescapable ($1, 2, 4, 8, 16\dots$). Yet drawing it with scrupulous precision reveals only **31** regions! The true formula is $\binom{n}{4} + \binom{n}{2} + 1$, which has nothing to do with $2^{n-1}$ for $n \geq 6$.

#### 1.4 The Crisis

These three examples reveal a profound epistemological problem. In mathematics, we seek statements that hold **for all natural numbers $n$**: an infinite collection of cases. However:

- Checking cases, even by millions, proves nothing (Euler, circle regions);
- A convincing diagram remains an illustration of a few particular cases (the gnomons).

We require an intellectual tool that **captures the entirety of the infinite sequence of integers in a single stroke**. That tool is mathematical induction.

> **💡 Did You Know?** Some conjectures hold out far longer. The Pólya conjecture (1919), which asserted that “most” integers up to any bound have an odd number of prime factors, was verified up to hundreds of millions before a counterexample was found in 1958; the smallest counterexample is $906\,150\,257$. No computer search could ever have “proven” this conjecture by finite verification—and fortunately so, since it was false.

---

### 2. The Core Idea: Dominoes and the Staircase

#### 2.1 The Dynamic Gesture

Imagine an endless row of dominoes stood upright on end. What do you need to be absolutely certain that they will **all** fall?

1. **That the first one falls**: you knock it over with your fingertip.
2. **That every domino, if it falls, causes the next one to fall**: they are spaced closely enough together.

Note carefully: condition 2 does **not** assert that the dominoes are falling. It merely says: “*if* this one falls, *then* the next one will fall as well.” It is an **implication**, a guarantee of transmission.

```
   Push!
     ↓
    ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ...      Base step (initialization): the first one falls.
    ╲ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ▌ ...      Inductive step (heredity): each fall triggers the next.
    ╲ ╲ ╲ ╲ ╲ ▌ ▌ ▌ ▌ ...      Conclusion: they all fall.
```

If either condition is missing, the entire guarantee collapses:
- Without the initial push, dominoes may stand at perfect intervals forever; not one moves.
- If a single gap is too wide (say, between the 40th and the 41st), the wave of falling tiles grinds to an abrupt halt.

The endless staircase presents the exact same intuition: to climb **every** step of an infinite stairway, it suffices to be capable of stepping onto the very first step, and to know how to step from any arbitrary step up to the next.

#### 2.2 Mathematical Notation

Before formally stating the principle, let us sharpen our vocabulary.

- $\mathbb{N}$ (read “the natural numbers”) $= \{0, 1, 2, 3, \dots\}$. The blackboard bold font was popularized in the 20th century by the Nicolas Bourbaki collective; the letter N stands for *natural*.
- We denote by $\mathcal{P}(n)$ (read “P of n”) a **predicate or statement** that depends on the integer $n$: it is a mathematical **assertion** that is either true or false depending on the value of $n$. For example, $\mathcal{P}(n)$: “$1 + 3 + \dots + (2n-1) = n^2$”. Warning: $\mathcal{P}(n)$ is **not a number**; it is a logical proposition. You do not add it or multiply it: you declare it to be true or false.
- The symbol $\Rightarrow$ (read “implies”): $A \Rightarrow B$ means “if $A$ is true, then $B$ is necessarily true.”
- $n_0$ denotes the **starting rank (base index)**, typically $0$ or $1$, but occasionally larger.
- The universal quantifier $\forall$ (read “for all” or “for every”) is an inverted letter A (for the German *alle* or English *all*); it was introduced by Gerhard Gentzen in 1935.

#### 2.3 The Principle of Mathematical Induction

> **📐 Definition — Principle of Mathematical Induction.** Let $\mathcal{P}(n)$ be a mathematical proposition depending on a natural number $n$, and let $n_0$ be a fixed integer. If:
> 1. **Initialization (Base Step)**: $\mathcal{P}(n_0)$ is true;
> 2. **Heredity (Inductive Step)**: for every integer $n \geq n_0$, if $\mathcal{P}(n)$ is true, then $\mathcal{P}(n+1)$ is true;
>
> then **(Conclusion)** $\mathcal{P}(n)$ is true for all integers $n \geq n_0$.

The assumption “$\mathcal{P}(n)$ is true”, invoked during the inductive step, is termed the **induction hypothesis** (frequently abbreviated as **IH**).

**Why is this principle true?** It can be viewed as a foundational axiom of the natural numbers: every natural number is generated by starting from $0$ and repeatedly adding $1$. If a property is inherited from each integer to the next, and is present at the starting point, no integer can escape its grasp. 

Alternatively, one may reason by contradiction via the **well-ordering principle** (every non-empty subset of natural numbers contains a least element): suppose there existed integers $n \geq n_0$ for which $\mathcal{P}(n)$ is false. Let $m$ be the **smallest** such counterexample. By the base step, $m \neq n_0$, so $m > n_0$, which means $m - 1 \geq n_0$. Because $m$ is the smallest counterexample, $\mathcal{P}(m-1)$ must be true. But then the inductive step dictates that $\mathcal{P}\big((m-1)+1\big) = \mathcal{P}(m)$ is true: a contradiction. In 1889, Giuseppe Peano formalized this principle as one of the foundational **Peano Axioms** defining arithmetic.

> **🔍 Historical Note —** Early manifestations of inductive reasoning appear in the work of the Persian mathematician **Al-Karaji** (around 1000 CE), who applied it to the binomial theorem and sums of cubes, and later **Francesco Maurolico**, who in 1575 proved that the sum of the first $n$ odd integers equals $n^2$—our exact Pythagorean gnomon problem! However, **Blaise Pascal**, in his *Treatise on the Arithmetical Triangle* (1654), was the first to give an explicit two-step formulation: proving a property “for the first base,” and then demonstrating that “if it holds in any arbitrary base, it will necessarily hold in the following one.” Augustus De Morgan coined the term “mathematical induction” in 1838.

> **⚠️ Pitfall Alert! —** In the inductive step, you do **not** assume that $\mathcal{P}(n)$ is true for all $n$ (that would be assuming the very thing you set out to prove!). Rather, you **fix** an arbitrary integer $n \geq n_0$, **assume** that $\mathcal{P}(n)$ holds for that single, specific rank, and **deduce** that $\mathcal{P}(n+1)$ must consequently hold. You are proving an implication, not asserting unconditional truth.

---

### 3. Method: Writing an Impeccable Induction Proof

> **🧭 Method — Standard Structure for Written Examinations.**
>
> *For every integer $n \geq n_0$, let $\mathcal{P}(n)$ denote the statement: “[...]”.*
>
> **Base Step (Initialization).** For $n = n_0$: evaluate the left-hand and right-hand sides independently and confirm that $\mathcal{P}(n_0)$ is true.
>
> **Inductive Step (Heredity).** Let $n \geq n_0$ be a fixed integer. Assume that $\mathcal{P}(n)$ is true (Induction Hypothesis). We wish to show that $\mathcal{P}(n+1)$ is true, that is: “[...]” (explicitly write out the target statement at rank $n+1$: this is **the goal**).
> [Perform algebraic calculations starting from rank $n+1$, strategically injecting the Induction Hypothesis and explicitly stating where it is used.]
> Therefore, $\mathcal{P}(n+1)$ is true.
>
> **Conclusion.** The property is true for $n = n_0$ and is inherited from rank $n$ to $n+1$ for all $n \geq n_0$; by the principle of mathematical induction, $\mathcal{P}(n)$ is true for every integer $n \geq n_0$.

Three golden rules from exam graders:
1. **Always write down the goal** (the statement at rank $n+1$) before computing: know exactly where you are heading.
2. **Start with the expression at rank $n+1$** and factor out or isolate the component corresponding to rank $n$, so you can cleanly apply the induction hypothesis.
3. **Explicitly cite the induction hypothesis** (“by the induction hypothesis, we have...”): this is the first thing a grader scans for. An inductive step that never uses the induction hypothesis is almost certainly invalid or circular.

---

### 4. Worked Examples

#### Worked Example 1 — The Pythagorean Gnomons

**Statement.** Prove that for all integers $n \geq 1$: $1 + 3 + 5 + \dots + (2n-1) = n^2$.

**Notation.** We also write this sum as $\displaystyle\sum_{k=1}^{n} (2k-1)$. The symbol $\sum$ (capital Greek letter **sigma**, corresponding to S for “sum”) was introduced by Euler in 1755. It reads: “the sum from $k = 1$ to $n$ of $2k - 1$”. The index $k$ is a **dummy variable**: it traverses $1, 2, \dots, n$ and disappears from the final result.

**Solution.** For $n \geq 1$, let $\mathcal{P}(n)$ be the proposition: “$\displaystyle\sum_{k=1}^{n}(2k-1) = n^2$”.

*Base Step.* For $n = 1$: the sum contains a single term, $2(1) - 1 = 1$, and the right side gives $1^2 = 1$. Hence $\mathcal{P}(1)$ is true.

*Inductive Step.* Let $n \geq 1$ be fixed; assume $\mathcal{P}(n)$ is true.  
**Goal:** Prove that $\displaystyle\sum_{k=1}^{n+1}(2k-1) = (n+1)^2$.  
Decomposing the sum:
$$\sum_{k=1}^{n+1}(2k-1) = \underbrace{\sum_{k=1}^{n}(2k-1)}_{= n^2 \text{ by IH}} + \big(2(n+1) - 1\big) = n^2 + 2n + 1 = (n+1)^2.$$
Thus $\mathcal{P}(n+1)$ is true.

*Conclusion.* By mathematical induction, $\mathcal{P}(n)$ is true for all integers $n \geq 1$. $\blacksquare$

Remark: The inductive step mirrors **exactly** the geometric gnomon: adding an L-shaped band of $2n+1$ pebbles transforms an $n \times n$ square into an $(n+1)\times(n+1)$ square. Induction is the algebraic rigor of the visual proof.

#### Worked Example 2 — Gauss’s Sum

**Statement.** Prove that for all $n \geq 1$: $1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$.

**Solution.** Let $\mathcal{P}(n)$ be: “$\displaystyle\sum_{k=1}^n k = \frac{n(n+1)}{2}$”.

*Base Step.* For $n = 1$: left-hand side $= 1$; right-hand side $= \frac{1(2)}{2} = 1$. True.

*Inductive Step.* Assume $\mathcal{P}(n)$ holds for a fixed $n \geq 1$.  
**Goal:** $\displaystyle\sum_{k=1}^{n+1} k = \frac{(n+1)(n+2)}{2}$.  
$$\sum_{k=1}^{n+1} k = \sum_{k=1}^n k + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2}.$$
We factored out $(n+1)$, instantly yielding the required form. Thus $\mathcal{P}(n+1)$ is true.

*Conclusion.* $\mathcal{P}(n)$ holds for all $n \geq 1$. $\blacksquare$

> **💡 Did You Know?** The young Carl Friedrich Gauss famously evaluated this sum for $n = 100$ in school by pairing terms: $(1 + 100) + (2 + 99) + \dots$, giving 50 pairs of 101, or 5050. Gauss's insight **discovers** the formula; mathematical induction **verifies** it. The two approaches are complementary: induction is formidable at proving a formula once known, but it cannot invent it out of thin air.

#### Worked Example 3 — Sum of Squares

**Statement.** Prove that for all $n \geq 1$: $\displaystyle\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.

**Solution.**  
*Base Step.* For $n = 1$: $1^2 = 1$ and $\frac{1(2)(3)}{6} = 1$. True.

*Inductive Step.* Assume the formula holds at rank $n$.  
**Goal:** $\displaystyle\sum_{k=1}^{n+1} k^2 = \frac{(n+1)(n+2)(2n+3)}{6}$.  
$$\sum_{k=1}^{n+1} k^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)\big[n(2n+1) + 6(n+1)\big]}{6} = \frac{(n+1)(2n^2 + 7n + 6)}{6}.$$
Expanding the target bracket: $(n+2)(2n+3) = 2n^2 + 7n + 6$.  
Hence the sum is indeed $\frac{(n+1)(n+2)(2n+3)}{6}$. Therefore $\mathcal{P}(n+1)$ is true.

*Conclusion.* The formula holds for all $n \geq 1$. $\blacksquare$

**Numerical sanity check**: for $n = 3$, $1 + 4 + 9 = 14$, and $\frac{3(4)(7)}{6} = 14$. ✓

#### Worked Example 4 — A Sequence Defined by Recurrence

**Statement.** Let $(u_n)$ be the sequence defined by $u_0 = 1$ and, for all $n \in \mathbb{N}$, $u_{n+1} = 2u_n + 3$. Compute the first few terms, conjecture an explicit closed formula, and prove it by induction.

**Notation Reminder:** $(u_n)$ denotes the entire sequence, while $u_n$ is the $n$-th term. The relation $u_{n+1} = 2u_n + 3$ is a **recurrence relation**: each term is generated from the preceding one.

**Investigation.** $u_0 = 1$, $u_1 = 5$, $u_2 = 13$, $u_3 = 29$, $u_4 = 61$. Notice that $u_n + 3$ yields $4, 8, 16, 32, 64$, which are powers of 2: $4 \times 2^n$.  
Conjecture: $u_n = 4 \times 2^n - 3 = 2^{n+2} - 3$.

**Proof.** Let $\mathcal{P}(n)$ be: “$u_n = 2^{n+2} - 3$”.

*Base Step.* $n = 0$: $2^{0+2} - 3 = 4 - 3 = 1 = u_0$. True.

*Inductive Step.* Assume $u_n = 2^{n+2} - 3$ for a fixed $n \geq 0$.  
**Goal:** $u_{n+1} = 2^{n+3} - 3$.  
$$u_{n+1} = 2u_n + 3 = 2\left(2^{n+2} - 3\right) + 3 = 2^{n+3} - 6 + 3 = 2^{n+3} - 3.$$
Thus $\mathcal{P}(n+1)$ is true.

*Conclusion.* For all $n \in \mathbb{N}$, $u_n = 2^{n+2} - 3$. $\blacksquare$

#### Worked Example 5 — Divisibility

**Statement.** Prove that for all $n \in \mathbb{N}$, $4^n - 1$ is divisible by 3.

**Definition Reminder.** “$a$ is divisible by 3” means there exists an integer $k \in \mathbb{Z}$ such that $a = 3k$.

**Solution.** Let $\mathcal{P}(n)$ be: “$\exists k \in \mathbb{Z}, \, 4^n - 1 = 3k$”.

*Base Step.* For $n = 0$: $4^0 - 1 = 1 - 1 = 0 = 3 \times 0$. True with $k = 0$.

*Inductive Step.* Assume there exists an integer $k$ such that $4^n - 1 = 3k$, so $4^n = 3k + 1$.  
**Goal:** Prove that $4^{n+1} - 1$ is a multiple of 3.  
$$4^{n+1} - 1 = 4 \times 4^n - 1 = 4(3k + 1) - 1 = 12k + 3 = 3(4k + 1).$$
Since $k$ is an integer, $4k + 1$ is an integer. Thus $4^{n+1} - 1$ is divisible by 3. $\mathcal{P}(n+1)$ is true.

*Conclusion.* For all $n \in \mathbb{N}$, $3$ divides $4^n - 1$. $\blacksquare$

The key technique is to **rephrase the induction hypothesis as an equality** ($4^n = 3k + 1$) so that it can be directly substituted into the expression at rank $n+1$.

#### Worked Example 6 — Bernoulli's Inequality (Core Curriculum Proof)

> **📐 Theorem — Bernoulli's Inequality.** For every real number $a > -1$ (and in particular for all $a > 0$) and for every natural number $n \in \mathbb{N}$:
> $$(1 + a)^n \geq 1 + na.$$

**Concrete Intuition.** Invest a capital at a compound interest rate $a$ per year (e.g., $a = 0.05$ for $5\%$): after $n$ years, the capital has multiplied by $(1+a)^n$. With simple interest, it would multiply by $1 + na$. Bernoulli's inequality asserts that **compound interest always earns at least as much as simple interest**—which is intuitive, because you earn interest on top of accumulated interest.

> **✍️ Proof.** Let $a > -1$ be a fixed real number. For $n \in \mathbb{N}$, let $\mathcal{P}(n)$ be: “$(1+a)^n \geq 1 + na$”.
>
> *Base Step.* For $n = 0$: $(1+a)^0 = 1$ and $1 + 0 \times a = 1$. Since $1 \geq 1$, $\mathcal{P}(0)$ is true.
>
> *Inductive Step.* Let $n \in \mathbb{N}$ be fixed; assume $(1+a)^n \geq 1 + na$.  
> **Goal:** $(1+a)^{n+1} \geq 1 + (n+1)a$.  
> We multiply both sides of the induction hypothesis by $1 + a$. Since $a > -1$, we have $1 + a > 0$, so the inequality direction is **preserved**:
> $$(1+a)^{n+1} = (1+a)^n (1+a) \geq (1+na)(1+a) = 1 + a + na + na^2 = 1 + (n+1)a + na^2.$$
> Since $n \geq 0$ and $a^2 \geq 0$, the quantity $na^2$ is non-negative: $na^2 \geq 0$.  
> Therefore, $1 + (n+1)a + na^2 \geq 1 + (n+1)a$.  
> By transitivity, $(1+a)^{n+1} \geq 1 + (n+1)a$.  
> Hence $\mathcal{P}(n+1)$ is true.
>
> *Conclusion.* For all $n \in \mathbb{N}$, $(1+a)^n \geq 1 + na$. $\blacksquare$

The little black square $\blacksquare$ (or Q.E.D., *quod erat demonstrandum*, “which was to be demonstrated”) marks the conclusion of a proof; it is often called the Halmos tombstone after Paul Halmos.

**Where did we use the hypothesis $a > -1$?** Exactly in one crucial step: multiplying an inequality by $1+a$ without flipping its direction. If $1 + a$ were negative, the inequality sign would reverse and the argument would collapse. For instance, with $a = -3$ and $n = 5$: $(1-3)^5 = (-2)^5 = -32$, whereas $1 + 5(-3) = -14$; here $-32 < -14$, so the inequality is blatantly **false**. In mathematics, conditions in a theorem are never merely decorative.

**Why is this inequality indispensable?** Because it bounds an exponential growth $(1+a)^n$ from below by an easily managed **affine linear** function $1 + na$. In Chapter 44, it will allow us to prove that if $q > 1$, then $q^n \to +\infty$: setting $q = 1 + a$ with $a > 0$, we have $q^n \geq 1 + na$, which outgrows any chosen bound.

#### Worked Example 7 — An Inequality Starting at a Higher Rank

**Statement.** Prove that for all integers $n \geq 4$: $2^n \geq n^2$.

**Exploration.**

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $2^n$ | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
| $n^2$ | 0 | 1 | 4 | **9** | 16 | 25 | 36 |

The inequality holds for $n = 0, 1, 2$, but **fails at $n = 3$** ($8 < 9$). It then holds for all $n \geq 4$. The starting rank $n_0 = 4$ is strictly necessary!

**Solution.**  
*Base Step.* For $n = 4$: $2^4 = 16 \geq 4^2 = 16$. True.

*Inductive Step.* Let $n \geq 4$; assume $2^n \geq n^2$.  
**Goal:** $2^{n+1} \geq (n+1)^2$.  
By the induction hypothesis, $2^{n+1} = 2 \times 2^n \geq 2n^2$.  
It now suffices to prove that $2n^2 \geq (n+1)^2$.  
Let us examine the difference:
$$2n^2 - (n+1)^2 = 2n^2 - (n^2 + 2n + 1) = n^2 - 2n - 1 = (n-1)^2 - 2.$$
Since $n \geq 4$, we have $n - 1 \geq 3$, so $(n-1)^2 \geq 9$.  
Therefore $(n-1)^2 - 2 \geq 9 - 2 = 7 > 0$.  
Hence $2n^2 \geq (n+1)^2$, which gives $2^{n+1} \geq 2n^2 \geq (n+1)^2$.  
Thus $\mathcal{P}(n+1)$ is true.

*Conclusion.* For all $n \geq 4$, $2^n \geq n^2$. $\blacksquare$

#### Worked Example 8 — A Monotone and Bounded Sequence

**Statement.** Let $(u_n)$ be defined by $u_0 = 1$ and $u_{n+1} = \sqrt{2 + u_n}$. Prove that for all $n \in \mathbb{N}$: $0 \leq u_n \leq u_{n+1} \leq 2$.

**Strategy.** Define $f(x) = \sqrt{2 + x}$ on $[-2, +\infty[$, so that $u_{n+1} = f(u_n)$. The function $f$ is strictly **increasing** (as the composite of two increasing functions: $x \mapsto 2 + x$ and the square root). An increasing function **preserves inequalities**: if $a \leq b$, then $f(a) \leq f(b)$. This is the decisive tool.

**Solution.** Let $\mathcal{P}(n)$ be: “$0 \leq u_n \leq u_{n+1} \leq 2$”.

*Base Step.* For $n = 0$: $u_0 = 1$ and $u_1 = \sqrt{2+1} = \sqrt{3} \approx 1.732$. We clearly have $0 \leq 1 \leq \sqrt{3} \leq 2$. True.

*Inductive Step.* Assume $0 \leq u_n \leq u_{n+1} \leq 2$.  
Since $f$ is increasing on $[0, 2]$, applying $f$ across the inequalities preserves their order:
$$f(0) \leq f(u_n) \leq f(u_{n+1}) \leq f(2) \iff \sqrt{2} \leq u_{n+1} \leq u_{n+2} \leq \sqrt{4} = 2.$$
Since $0 \leq \sqrt{2}$, we obtain $0 \leq u_{n+1} \leq u_{n+2} \leq 2$, which is precisely $\mathcal{P}(n+1)$.

*Conclusion.* For all $n \in \mathbb{N}$, $0 \leq u_n \leq u_{n+1} \leq 2$. The sequence $(u_n)$ is therefore **increasing** and **bounded above by 2**. $\blacksquare$

This technique—applying an increasing function to an entire chained inequality—is one of the most effective and elegant methods tested at the Grade 12 level.

#### Worked Example 9 — Higher-Order Derivatives

**Statement.** Let $f(x) = x e^x$ on $\mathbb{R}$. We denote by $f^{(n)}$ the **$n$-th derivative** of $f$ ($f^{(0)} = f$, $f^{(1)} = f'$, $f^{(2)} = f''$). Prove that for all $n \in \mathbb{N}$: $f^{(n)}(x) = (x + n)e^x$.

**Notation Note:** Parentheses in $f^{(n)}$ are vital to distinguish the $n$-th derivative from the $n$-th algebraic power $f(x)^n$.

**Solution.**  
*Base Step.* For $n = 0$: $f^{(0)}(x) = f(x) = x e^x = (x + 0)e^x$. True.

*Inductive Step.* Assume $f^{(n)}(x) = (x + n)e^x$ for all $x \in \mathbb{R}$.  
The $(n+1)$-th derivative is the derivative of the $n$-th: $f^{(n+1)} = (f^{(n)})'$.  
Applying the product rule $(uv)' = u'v + uv'$ with $u(x) = x + n$ and $v(x) = e^x$:
$$f^{(n+1)}(x) = 1 \cdot e^x + (x + n)e^x = (x + n + 1)e^x.$$
Thus $\mathcal{P}(n+1)$ is true.

*Conclusion.* For all $n \in \mathbb{N}$, $f^{(n)}(x) = (x + n)e^x$. $\blacksquare$

---
