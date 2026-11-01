# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 31: The Court of Logic

> *“In the courtroom of mathematics, no eloquence can save the accused. Verdicts are not reached on the sincere expression of the witness, nor on the number of those who believe him: judgement is passed strictly on proof. A single counterexample suffices to condemn a statement, but a thousand examples will never suffice to clear it.”*

---

### What You Are About to Discover

- The great **number families** ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{D}$, $\mathbb{Q}$, $\mathbb{R}$), nested like Russian dolls, and why each of them had to be invented.
- The language of **sets** and **intervals**: $\in$, $\subset$, $\cup$, $\cap$, $[a\,;b[$, $+\infty$… and how to read them aloud.
- The **absolute value**, which measures distance without caring about direction.
- The rules of the **court**: implication, converse, contrapositive, equivalence, and the quantifiers “for all” and “there exists.”
- The four great **weapons of proof**: direct proof, counterexample, contraposition, and proof by contradiction—with the core demonstrations required in Grade 10 ($\frac13$ is not decimal, $\sqrt2$ is irrational, the square of an odd integer is odd…).

---

### 1. The Problem: The Formula That Lied Forty Times in a Row

Imagine a courtroom. In the dock sits not a man, but a **sentence**. It has been brought forward by an enthusiastic student, who defends it with fiery passion:

> “For every natural number $n$, the number $n^2 + n + 41$ is prime.”

The defense attorney calls witnesses to the stand, one by one.

| $n$ | $n^2+n+41$ | Prime? |
|---|---|---|
| 0 | 41 | yes |
| 1 | 43 | yes |
| 2 | 47 | yes |
| 3 | 53 | yes |
| 4 | 61 | yes |
| 5 | 71 | yes |
| 10 | 151 | yes |
| 20 | 461 | yes |
| 30 | 971 | yes |
| 39 | 1601 | yes |

Forty witnesses ($n = 0, 1, 2, \dots, 39$) step up to the stand, and **every single one** confirms: the resulting number is prime. The courtroom audience is convinced. The jury prepares to acquit.

Then the prosecutor stands up, completely calm, and calls a single witness: $n = 40$.

$$40^2 + 40 + 41 = 1600 + 40 + 41 = 1681 = 41 \times 41.$$

$1681$ is **not** prime. The statement is **false**. The gavel strikes; the verdict is final and unappealable.

> **💡 Did You Know?** This polynomial was observed by **Leonhard Euler** in 1772. It produces prime numbers for $n$ from $0$ up to $39$—an astounding streak—but it fails at $n = 40$. One can even see this without calculating: for $n = 41$, $41^2 + 41 + 41 = 41 \times 43$, which is obviously divisible by $41$.

This story encapsulates the entire spirit of this chapter:

1. **Checking cases, even dozens of them, proves nothing** for a statement that speaks of *all* integers.
2. **A single counterexample is enough** to shatter a universal assertion.
3. To *establish* a general truth, an entirely different tool is required: **proof**.

In middle school, you often “saw” that a property worked on examples. Starting in tenth grade (Seconde), you step into the court of law. You need precise language (which numbers are we talking about? what does “if… then” mean?) and reliable methods of proof. This is what we will construct together.

> **🔍 The True Story —** Around 350 BCE, **Aristotle** laid the foundations of logic by studying the *syllogism*: “All men are mortal; Socrates is a man; therefore Socrates is mortal.” More than two thousand years later, in 1847 and 1854, the Englishman **George Boole**, a cobbler's son and largely self-taught, transformed logic into an *algebra*: truth became $1$, falsehood $0$, and “and” became multiplication. Without knowing it, he had just penned the grammar for all twentieth-century computers.

---

### 2. The Number Families: A History of Crises

Every family of numbers was born out of an **impossible operation**. When existing tools no longer sufficed, humanity had to expand the universe of numbers.

#### 2.1 The Natural Numbers $\mathbb{N}$: Counting Pebbles

The very first numbers are those of the shepherd counting his sheep: $0, 1, 2, 3, \dots$

> **📐 Definition —** The set of **natural numbers** is
> $$\mathbb{N} = \{0\,;1\,;2\,;3\,;\dots\}.$$

**Notation Explained.**
- The **curly braces** $\{\ \}$ are used to write a set by listing its elements. We read this as “the set of elements $0, 1, 2\dots$”. In French and continental European tradition, elements are often separated by semicolons to avoid confusion with the decimal comma.
- The letter $\mathbb{N}$ comes from *naturale* (Italian): it was introduced by **Giuseppe Peano** in 1889. The “double-struck” style (known as *blackboard bold*) was born at the blackboard: chalk cannot easily produce boldface type, so mathematicians doubled a stroke. It became standard in printed textbooks during the mid-twentieth century.
- We simply read “$\mathbb{N}$” as “the set of natural numbers” or “N”.

In $\mathbb{N}$, we can always add and multiply. But **subtraction** causes trouble: $3 - 5$ has no answer in $\mathbb{N}$.

#### 2.2 The Integers $\mathbb{Z}$: The Merchant’s Debts

Recall the merchant’s slate (Chapter 14): to record a debt, negative numbers become indispensable.

> **📐 Definition —** The set of **integers** (or relative integers) is
> $$\mathbb{Z} = \{\dots\,;-3\,;-2\,;-1\,;0\,;1\,;2\,;3\,;\dots\}.$$

The letter $\mathbb{Z}$ comes from the German ***Zahlen*** (“numbers”), widely adopted by Richard Dedekind and German mathematicians in the nineteenth century. In $\mathbb{Z}$, subtraction is always possible. But **division** is not: $7 \div 2$ is not an integer.

#### 2.3 The Decimals $\mathbb{D}$: Stevin’s Tenths

A merchant weighing spices needs $2.35\text{ kg}$. Simon Stevin (Chapter 11) popularized decimal numbers.

> **📐 Definition —** A number is **decimal** if it can be written in the form
> $$\frac{a}{10^n} \quad \text{with } a \in \mathbb{Z} \text{ and } n \in \mathbb{N}.$$
> The set of decimal numbers is denoted $\mathbb{D}$.

In other words: a decimal number is one that can be written with a **finite** number of digits after the decimal point. Examples: $2.35 = \frac{235}{10^2}$; $-0.007 = \frac{-7}{10^3}$; $12 = \frac{12}{10^0}$ (every integer is a decimal number).

The symbol $\in$ is read “**belongs to**” or “**is an element of**”. “$a \in \mathbb{Z}$” means “$a$ is an element of $\mathbb{Z}$”, that is, “$a$ is an integer.” This symbol is a stylized version of the Greek letter epsilon $\varepsilon$, the initial of ἐστί (*esti*, “is”): introduced once again by **Peano** in 1889. Its negation, $\notin$, is read “does not belong to.”

Everything seems in order… until the day we divide a loaf of bread into **three**.

#### 2.4 The Rational Numbers $\mathbb{Q}$: Dividing into Three

> **📐 Definition —** A number is **rational** if it can be written in the form
> $$\frac{p}{q} \quad \text{with } p \in \mathbb{Z} \text{ and } q \in \mathbb{N},\ q \neq 0.$$
> The set of rational numbers is denoted $\mathbb{Q}$ (from the initial of *quotient*, proposed by Peano in 1895).

The word “rational” comes from the Latin *ratio*, meaning “ratio” or “proportion”: a rational number is a **ratio** of two integers. It has nothing to do with being “sensible” or “reasonable”… even though mathematical history often plays on this double meaning.

The natural question arises: $\frac13$ is rational, but is it decimal? Your calculator displays $0.333333333$, which *looks* like a decimal. But its screen is too small to tell the whole truth. Here is the first trial of the chapter.

> **✍️ Proof (Core Curriculum) — $\frac13$ is not a decimal number.**
>
> Let us reason **by contradiction** (*reductio ad absurdum*): suppose that $\frac13$ were a decimal number. There would then exist an integer $a$ and a natural number $n$ such that
> $$\frac13 = \frac{a}{10^n}.$$
> Multiplying both sides by $3 \times 10^n$, we obtain:
> $$10^n = 3a.$$
> Thus $10^n$ would be a multiple of $3$. However, the sum of the digits of $10^n$ (a single “1” followed by $n$ zeros) is $1$, which is not divisible by $3$; by the standard divisibility rule for $3$, $10^n$ is **not** a multiple of $3$.
>
> (Alternative argument: $10^n = 2^n \times 5^n$; its prime factorization contains only $2$s and $5$s, and never any factor $3$.)
>
> We have reached a contradiction. The initial assumption must therefore be false: $\frac13 \notin \mathbb{D}$. $\blacksquare$

The small filled black square $\blacksquare$ (or Halmos symbol) marks the end of a proof. The Ancients used to write “**QED**”: *quod erat demonstrandum* (“which was to be demonstrated”).

> **💡 Did You Know?** An irreducible fraction $\frac{p}{q}$ is decimal if and only if its denominator $q$ contains only the prime factors $2$ and $5$. Thus $\frac{7}{40} = \frac{7}{2^3 \times 5} = 0.175$ is decimal, but $\frac{1}{6} = \frac{1}{2 \times 3}$ is not. Every rational number has a decimal representation that is either **terminating** (finite) or **eventually periodic**: for example, $\frac{1}{7} = 0.\overline{142857}$ (where the overline indicates the repeating period).

#### 2.5 The Real Numbers $\mathbb{R}$: The Diagonal That Broke the Brotherhood

You have already encountered this drama (Chapter 19, *The Forbidden Secret of the Pythagoreans*). The diagonal of a square with unit side length measures $\sqrt2$, according to the Pythagorean theorem: $d^2 = 1^2 + 1^2 = 2$. The Pythagoreans believed that “all is number,” meaning every length in the cosmos is a ratio of integers. The diagonal betrayed them. We will now write out the proof with full high-school rigor. First, we need a small lemma (a *lemma* is an auxiliary stepping stone towards a main theorem).

> **✍️ Proof (Core Curriculum) — The square of an odd integer is odd.**
>
> Let $n$ be an odd integer. By definition, there exists an integer $k$ such that $n = 2k + 1$. Then:
> $$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.$$
> Since $2k^2 + 2k$ is an integer (let us call it $k'$), we have $n^2 = 2k' + 1$: therefore $n^2$ is odd. $\blacksquare$

Similarly, the square of an even integer $n = 2k$ is $n^2 = 4k^2 = 2(2k^2)$, which is even.

> **📐 Consequence (by Contraposition) —** If $n^2$ is even, then $n$ is even.
>
> Indeed, if $n$ were not even, it would be odd, and its square would be odd by the lemma above. We will revisit this mode of reasoning (contraposition) in detail in Section 6.

> **✍️ Proof (Core Curriculum) — $\sqrt2$ is irrational.**
>
> Let us reason by contradiction. Suppose that $\sqrt2$ were rational. Then it could be written as an **irreducible fraction**:
> $$\sqrt2 = \frac{p}{q}, \quad p \in \mathbb{N},\ q \in \mathbb{N}^*,\ \text{where $p$ and $q$ share no common factor other than 1.}$$
> Squaring both sides: $2 = \dfrac{p^2}{q^2}$, hence:
> $$p^2 = 2q^2.$$
> 1. Therefore $p^2$ is even. By the consequence above, $p$ is even: there exists an integer $k$ such that $p = 2k$.
> 2. Substituting this back: $(2k)^2 = 2q^2$, which gives $4k^2 = 2q^2$, or $q^2 = 2k^2$. Hence $q^2$ is even, which implies that $q$ is also even.
> 3. Consequently, $p$ and $q$ are both even: they share $2$ as a common factor. This **contradicts** the fact that the fraction $\frac{p}{q}$ is in lowest terms (irreducible).
>
> The assumption “$\sqrt2$ is rational” leads to an absurdity: it must be false. Therefore $\sqrt2 \notin \mathbb{Q}$. $\blacksquare$

The notation $\mathbb{N}^*$ denotes $\mathbb{N}$ excluding $0$. Likewise, $\mathbb{R}^*$ denotes the non-zero real numbers.

> **📐 Definition —** The set of **real numbers**, denoted $\mathbb{R}$, is the set of all coordinates of points along a graduated number line. A real number that is not rational is called **irrational**.

Examples of irrationals: $\sqrt2$, $\sqrt3$, $\pi$ (proved irrational by Lambert in 1761), $\sqrt2 + 1$ (see Exercise 11).

#### 2.6 The Russian Dolls: Inclusion $\subset$

Every natural number is an integer; every integer is a decimal; every decimal is rational ($\frac{a}{10^n}$ is a quotient of integers); every rational is real.

> **📐 Definition —** A set $A$ is said to be **included** in (or a **subset** of) a set $B$, written $A \subset B$, if every element of $A$ is also an element of $B$. We read this as “$A$ is included in $B$” or “$A$ is a subset of $B$.”

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R}$$

```
 ┌──────────────────────────────────────────────────────────┐
 │ R                                    √2     π    -√3     │
 │   ┌───────────────────────────────────────────┐          │
 │   │ Q                       1/3     -2/7      │          │
 │   │   ┌──────────────────────────────┐        │          │
 │   │   │ D            0.25    -1.7    │        │          │
 │   │   │   ┌──────────────────┐       │        │          │
 │   │   │   │ Z        -3  -1  │       │        │          │
 │   │   │   │   ┌──────────┐   │       │        │          │
 │   │   │   │   │ N  0 1 7 │   │       │        │          │
 │   │   │   │   └──────────┘   │       │        │          │
 │   │   │   └──────────────────┘       │        │          │
 │   │   └──────────────────────────────┘        │          │
 │   └───────────────────────────────────────────┘          │
 └──────────────────────────────────────────────────────────┘
```

Each inclusion is **strict**: $-1 \in \mathbb{Z}$ but $-1 \notin \mathbb{N}$; $0.5 \in \mathbb{D}$ but $0.5 \notin \mathbb{Z}$; $\frac13 \in \mathbb{Q}$ but $\frac13 \notin \mathbb{D}$; $\sqrt2 \in \mathbb{R}$ but $\sqrt2 \notin \mathbb{Q}$.

> **⚠️ Pitfall Warning!** Do not confuse $\in$ and $\subset$.
> - $\in$ connects an **element** to a **set**: $3 \in \mathbb{N}$.
> - $\subset$ connects **two sets**: $\{3\} \subset \mathbb{N}$, $\mathbb{N} \subset \mathbb{Z}$.
>
> Writing “$3 \subset \mathbb{N}$” or “$\mathbb{N} \in \mathbb{Z}$” is a violation of mathematical grammar.

> **⚠️ Pitfall Warning!** A number can wear many disguises. $\frac{12}{4}$ looks like a fraction, but it simplifies to $3$, a natural number. $\sqrt{9} = 3 \in \mathbb{N}$, $\sqrt{\frac{4}{9}} = \frac23 \in \mathbb{Q}$, $\frac{21}{75} = \frac{7}{25} = 0.28 \in \mathbb{D}$. Always **simplify** before passing judgement.

> **Worked Example 1 — Classifying Numbers.**
> For each number, determine the smallest set among $\mathbb{N}, \mathbb{Z}, \mathbb{D}, \mathbb{Q}, \mathbb{R}$ that contains it:
> $$a = -\frac{18}{6},\quad b = \frac{3}{8},\quad c = \frac{5}{12},\quad d = \sqrt{16} - \sqrt{2},\quad e = (\sqrt{5})^2,\quad f = \frac{\pi}{2\pi}.$$
>
> - $a = -3$: $a \in \mathbb{Z}$, and $a \notin \mathbb{N}$. Smallest set: $\mathbb{Z}$.
> - $b = \frac{3}{8} = \frac{3}{2^3}$: denominator contains only factors of 2, hence decimal: $b = \frac{375}{1000} = 0.375$. Smallest set: $\mathbb{D}$.
> - $c = \frac{5}{12} = \frac{5}{2^2 \times 3}$, irreducible with a factor of 3 in the denominator: $c \in \mathbb{Q}$, $c \notin \mathbb{D}$. (Verification: $c = 0.41666\dots$)
> - $d = 4 - \sqrt2$. If $d$ were rational, then $\sqrt2 = 4 - d$ would be rational (the difference of two rationals), which is false. Thus $d \in \mathbb{R}$, irrational.
> - $e = 5$: $\mathbb{N}$.
> - $f = \frac12 = 0.5$: $\mathbb{D}$. The $\pi$ cancels out: do not let outward appearances mislead you!

---

### 3. The Language of Sets and Intervals

#### 3.1 Describing a Set

There are two primary ways to describe a set:
- **By extension (roster method)**: listing all its elements, $A = \{1\,;3\,;5\,;7\}$;
- **By comprehension (set-builder notation)**: stating a characteristic property, $A = \{x \in \mathbb{N} \mid x \text{ is odd and } x < 8\}$.

The vertical bar $\mid$ (or colon “:”) is read “**such that**”. The statement is read: “the set of all $x$ belonging to $\mathbb{N}$ such that $x$ is odd and strictly less than $8$.”

The **empty set**, which contains no elements at all, is denoted $\varnothing$. This symbol was introduced by **André Weil** (of the Bourbaki group) around 1939, inspired by the Scandinavian letter Ø. Warning: $\varnothing$ is not the same as $\{0\}$! The set $\{0\}$ contains one element, namely zero; $\varnothing$ contains nothing. An empty box is not a box containing a zero.

#### 3.2 Union, Intersection, and Complement

Let $A$ and $B$ be two subsets of a universal set $E$.

> **📐 Definitions —**
> - The **intersection** $A \cap B$ (read “$A$ intersect $B$”) is the set of elements belonging to both $A$ **and** $B$.
> - The **union** $A \cup B$ (read “$A$ union $B$”) is the set of elements belonging to $A$ **or** $B$ (or both).
> - The **complement** of $A$ in $E$, denoted $\overline{A}$ or $E \setminus A$, is the set of elements in $E$ that **do not belong** to $A$. The symbol $\setminus$ is read “minus” or “excluding.”
> - $A$ and $B$ are **disjoint** if $A \cap B = \varnothing$.

A mnemonic trick: $\cap$ resembles a narrow tunnel or arch through which only those holding both tickets may pass; $\cup$ resembles a wide cup or bowl, a **U** for **U**nion, gathering everything together.

```
        A ∩ B                        A ∪ B
     ┌───────┐                    ┌───────┐
     │ A  ┌──┼────┐               │███████│████┐
     │    │██│    │               │███┌───┼────┤
     └────┼──┘  B │               └───┼███████B│
          └───────┘                   └────────┘
   (only the shared region)       (all shaded areas combined)
```

> **Worked Example 2 — Operations on Finite Sets.**
> Let $E = \{1\,;2\,;\dots\,;12\}$, $A$ = the set of multiples of 2 in $E$, and $B$ = the set of multiples of 3 in $E$.
> - $A = \{2\,;4\,;6\,;8\,;10\,;12\}$, $B = \{3\,;6\,;9\,;12\}$.
> - $A \cap B = \{6\,;12\}$: these are the multiples of $6$.
> - $A \cup B = \{2\,;3\,;4\,;6\,;8\,;9\,;10\,;12\}$ (6 and 12 are not duplicated).
> - $\overline{A \cup B} = \{1\,;5\,;7\,;11\}$: numbers in $E$ divisible by neither 2 nor 3.
> - Checking cardinalities: $\text{card}(A \cup B) = \text{card}(A) + \text{card}(B) - \text{card}(A \cap B) = 6 + 4 - 2 = 8$. (The *cardinality*, written $\text{card}$, denotes the number of elements.)

#### 3.3 Intervals of $\mathbb{R}$

On the real number line, the most useful subsets are **unbroken line segments without holes**: intervals.

> **📐 Definition —** Let $a$ and $b$ be two real numbers with $a < b$.
>
> | Notation | Set of reals $x$ such that | Verbal Description | Visual Representation |
> |---|---|---|---|
> | $[a\,;b]$ | $a \le x \le b$ | closed interval $a$ to $b$ | `[■■■■■■]` |
> | $]a\,;b[$ or $(a, b)$ | $a < x < b$ | open interval $a$ to $b$ | `]■■■■■■[` |
> | $[a\,;b[$ or $[a, b)$ | $a \le x < b$ | half-open: closed at $a$, open at $b$ | `[■■■■■■[` |
> | $]a\,;b]$ or $(a, b]$ | $a < x \le b$ | half-open: open at $a$, closed at $b$ | `]■■■■■■]` |
> | $[a\,;+\infty[$ or $[a, +\infty)$ | $x \ge a$ | from $a$ inclusive to plus infinity | `[■■■■■■→` |
> | $]a\,;+\infty[$ or $(a, +\infty)$ | $x > a$ | from $a$ exclusive to plus infinity | `]■■■■■■→` |
> | $]-\infty\,;b]$ or $(-\infty, b]$ | $x \le b$ | from minus infinity to $b$ inclusive | `←■■■■■■]` |
> | $]-\infty\,;b[$ or $(-\infty, b)$ | $x < b$ | from minus infinity to $b$ exclusive | `←■■■■■■[` |
>
> We also write $\mathbb{R} = ]-\infty\,;+\infty[ = (-\infty, +\infty)$. The real numbers $a$ and $b$ are the **endpoints** (or bounds) of the interval; $b - a$ is its **length** (or width).

**Why these brackets?** The French and ISO convention is visual: an **inward-facing bracket** $[$ or $]$ “captures” the endpoint (it is included); an **outward-facing bracket** $]$ or $[$ “pushes it away” (it is excluded). In many English-speaking traditions, parentheses $(a, b)$ are used for open bounds. A **semicolon** is used between endpoints to avoid confusion with decimal commas or periods: $[1.5\,;2]$.

**The symbol $\infty$** (“infinity”) was introduced by the Englishman **John Wallis** in 1655. It is **not a number**: it is a way to express “without bound in this direction.” This is why brackets are **always open** adjacent to $+\infty$ or $-\infty$: one can never “reach” infinity, and so it can never be included.

> **⚠️ Pitfall Warning!**
> - $[3\,;+\infty]$ is **incorrect**: the bracket must be open at $+\infty$.
> - $[5\,;2]$ makes no sense: the smaller endpoint must always be written on the left.
> - $]2\,;2[ = \varnothing$, but $[2\,;2] = \{2\}$ (a single point).
> - The interval $[1\,;3]$ contains an **infinite** number of real values ($1.5$, $\sqrt2$, $2.999\dots$), not just the integers $1, 2, 3$! Do not confuse it with the discrete set of integers $\{1\,;2\,;3\}$.

**Useful Notations:** $\mathbb{R}_+ = [0\,;+\infty[$ (non-negative real numbers), $\mathbb{R}_- = ]-\infty\,;0]$ (non-positive reals), $\mathbb{R}^*_+ = ]0\,;+\infty[$ (strictly positive reals), $\mathbb{R}^* = \mathbb{R} \setminus \{0\} = ]-\infty\,;0[ \cup ]0\,;+\infty[$.

> **Worked Example 3 — Intersection and Union of Intervals.**
> Let $I = [-2\,;5[$ and $J = ]1\,;+\infty[$. Find $I \cap J$ and $I \cup J$.
>
> Let us draw both intervals aligned on a line:
> ```
>          -2        1         5
>   I :     [■■■■■■■■■■■■■■■■■■[
>   J :               ]■■■■■■■■■■■■■■■■■■■■■→
>   I∩J:              ]■■■■■■■■[
>   I∪J:    [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■→
> ```
> - $I \cap J$: a number must satisfy both $\ge -2$, $< 5$, and $> 1$. The most restrictive lower bound is $x > 1$, and upper bound $x < 5$. Therefore $I \cap J = ]1\,;5[$.
> - $I \cup J$: belonging to at least one suffices. This spans everything from $-2$ (included) onwards to $+\infty$. Hence $I \cup J = [-2\,;+\infty[$.

> **Worked Example 4 — Translating an Inequality into an Interval.**
> Solve in $\mathbb{R}$: $-3 < 2x + 1 \le 7$, and express the solution set as an interval.
>
> Subtract $1$ across all three parts: $-4 < 2x \le 6$. Divide by $2$, which is **positive** (preserving inequality direction): $-2 < x \le 3$.
> The solution set is $S = ]-2\,;3]$.

> **Worked Example 5 — A Union That Cannot Be Simplified.**
> Solve $x^2 > 9$ in $\mathbb{R}$.
>
> $x^2 > 9 \iff x^2 - 9 > 0 \iff (x-3)(x+3) > 0$. A product of two factors is strictly positive when both factors share the same sign. Sign table:
>
> | $x$ | $-\infty$ | | $-3$ | | $3$ | | $+\infty$ |
> |---|---|---|---|---|---|---|---|
> | $x+3$ | | $-$ | $0$ | $+$ | | $+$ | |
> | $x-3$ | | $-$ | | $-$ | $0$ | $+$ | |
> | Product | | $+$ | $0$ | $-$ | $0$ | $+$ | |
>
> Thus $S = ]-\infty\,;-3[ \cup ]3\,;+\infty[$. This union of two disjoint intervals **is not** an interval: there is a “gap” between $-3$ and $3$.
>
> ⚠️ The classic mistake “$x^2 > 9 \iff x > 3$” completely ignores the negative branch: $x = -4$ indeed satisfies $(-4)^2 = 16 > 9$.
