# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 48: Napier's Logarithm and the Navigator's Tables

> *“By shortening the labours, the invention of logarithms doubled the life of astronomers.”*
> — Pierre-Simon de Laplace

---

### What You Are About to Discover

- Why, around 1600, navigators and astronomers were suffocating under **multiplications**, and how a Scottish baron invented a machine to transform multiplications into **additions**.
- The **natural logarithm function** $\ln$, defined as the machine that **undoes** the exponential: $y = e^x \iff x = \ln y$.
- Its **algebraic properties** ($\ln(ab) = \ln a + \ln b$, etc.) and their complete **proofs**.
- A **comprehensive analysis** of the function: derivative $\frac{1}{x}$, monotonicity, limits, indeterminate forms, asymptotic growth rates, and concavity.
- Rigorous methods to solve **equations and inequalities** involving $\ln$ and $e$, and how to determine **thresholds** in geometric sequences.
- Real-world **logarithmic scales**: pH, decibels, earthquake magnitudes, and carbon-14 radiometric dating.

---

### 1. The Problem: The Sea, the Stars, and Endless Multiplications

#### 1.1 The Lost Navigator

Imagine yourself in the year **1600**, standing on the deck of a galleon crossing the Atlantic. There is no GPS, no radio, no reliable marine chronometer. To determine the ship's coordinates, the navigator uses a **quadrant** to measure the angular elevation of the Sun or a guide star above the horizon, and must then solve a **spherical triangle**: a triangle inscribed on the celestial sphere.

The formulas of spherical trigonometry look like this:
$$\cos a = \cos b \cos c + \sin b \sin c \cos A.$$

Sines and cosines are read from printed **tables**, computed to seven or eight decimal places for navigational accuracy. The navigator must therefore multiply, entirely by hand, numbers such as:
$$0.8746197 \times 0.4848096.$$

Such long multiplication involves dozens of intermediate products and additions, with carries at every step. A single calculation error, and the vessel believes itself to be a hundred kilometers from its actual position—heading straight for submerged reefs. Astronomers, too, such as **Tycho Brahe** and **Johannes Kepler**, spent whole **decades** of their lives grinding through tedious multiplications to determine planetary orbits.

> **💡 Did you know?** Before logarithms, mathematicians used a computational shortcut known as **prosthaphaeresis** (from the Greek for “addition and subtraction”), which exploited the product-to-sum trigonometric identity $\cos a \cos b = \frac{1}{2}\left[\cos(a+b) + \cos(a-b)\right]$ to convert products into sums… but it was cumbersome, error-prone, and restricted to numbers between $-1$ and $1$.

#### 1.2 The Dream: Replacing × with +

Addition is straightforward: one aligns the digits and adds. Multiplication is laborious and prone to error. Hence the great dream of Renaissance computers:

> *To find a “dictionary” that pairs every positive number with another number in such a way that the translation of a product is simply the sum of the translations.*

The German monk **Michael Stifel** caught a glimpse of this dream in 1544 by tabulating two sequences, one beneath the other:

```
 Arithmetic progression :   0    1    2    3    4     5     6      7      8
 Geometric progression  :   1    2    4    8   16    32    64    128    256
```

To multiply $8 \times 32$, look above: $8$ corresponds to $3$, and $32$ corresponds to $5$. Add them: $3 + 5 = 8$. Look back down: under $8$ sits $256$. And indeed, $8 \times 32 = 256$! **The top row converts multiplications of the bottom row into simple additions.**

This is simply the rule of exponents you have known since middle school:
$$2^3 \times 2^5 = 2^{3+5}.$$

Yet there was a critical flaw: between $8$ and $16$, there are vast gaps. How could one multiply $11 \times 13$? One would need a geometric progression **with steps so densely packed** that virtually every real number is represented. One had to **fill the gaps**.

#### 1.3 Twenty Years of Calculation: The Baron of Merchiston

This monumental feat was accomplished by **John Napier** (1550–1617), 8th Laird of Merchiston in Scotland. He chose a geometric progression whose common ratio was exceedingly close to $1$, namely $1 - 10^{-7} = 0.9999999$, so that consecutive terms barely differed: the gaps shrank to microscopic proportions. For **twenty years**, by hand, he computed his tables. In **1614**, he published *Mirifici Logarithmorum Canonis Descriptio* (“Description of the Wonderful Rule of Logarithms”).

The word **logarithm**, which he coined, derives from the Greek *logos* (ratio, proportion) and *arithmos* (number): “the number that measures ratios”. The logarithm of a number is, in essence, **the number of steps** one must take along the geometric progression to reach it.

> **🔍 True History —** The English mathematician **Henry Briggs**, reading Napier's work, was so astonished that he journeyed from London to Scotland in 1615 to meet him. It is said that when they met, the two men stood looking at one another in speechless admiration for a quarter of an hour before uttering a word. Together, they agreed that logarithms should be recast in “base 10” (where $\log 10 = 1$), which was far more practical for decimal notation: these became the **common (or decimal) logarithms**. Kepler, who received Napier's tables in 1617, immediately used them to complete his monumental *Rudolphine Tables* of planetary motions and dedicated one of his works to Napier… unaware that Napier had passed away in the interim.

For more than **three centuries**, logarithmic tables and **slide rules** (pairs of logarithmic scales sliding against each other to add lengths mechanically) accompanied engineers, sailors, architects, and scientists—all the way to NASA engineers working on the Apollo moon landings in the 1960s!

#### 1.4 The Same Problem, Seen from the Laboratory

Recall the bacterial colony from Chapter 40. A population governed by the law $N(t) = N_0 \, e^{kt}$ grows exponentially. The biologist faces the **inverse** question:

> *“The population has grown by a factor of 1000. How long ago did the infection begin?”*

This requires solving $e^{kt} = 1000$—that is, finding the **exponent** that produces a desired result. The exponential function maps the exponent to the output; we need the reciprocal machine that maps the **output back to the exponent**. That machine is the **natural logarithm**. The two narratives—that of navigators at sea and that of biologists in the laboratory—converge at the exact same concept.

---

### 2. Definition: The Machine that Inverts the Exponential

#### 2.1 What We Already Know About the Exponential

Let us summarize what Chapters 40 and 46 established regarding the function $\exp : x \mapsto e^x$:

- It is defined, continuous, and differentiable on $\mathbb{R}$, with $(e^x)' = e^x$;
- It is **strictly positive**: $e^x > 0$ for all real numbers $x$;
- It is therefore **strictly increasing** on $\mathbb{R}$;
- $\lim\limits_{x \to -\infty} e^x = 0$ and $\lim\limits_{x \to +\infty} e^x = +\infty$.

The **corollary to the Intermediate Value Theorem** (the Bijective Theorem, Chapter 46) then guarantees: a function that is continuous and strictly monotonic on an interval defines a **bijection** from that interval onto its image. Here:

> **For every real number $a > 0$, the equation $e^x = a$ has a unique real solution.**

Visually: the exponential curve intersects every horizontal line $y = a$ (with $a > 0$) **at exactly one point**. And it never intersects the lines $y = a$ with $a \leq 0$, because the curve lies entirely above the horizontal axis.

```
       y
       ▲                         /  y = e^x
       │                       /
     a ┼ - - - - - - - - - - *      ← single point of intersection
       │                  /  ¦
       │              _-'    ¦
     1 ┼ _ _ _ _ _ _-*       ¦
       │      __--'  ¦       ¦
 ──────┼--''─────────┼───────┼────────► x
       │             0     ln a
   -2 ┼ - - - - - - - - - - - - - - -   ← never reached: no solution
```

#### 2.2 The Definition

> **📐 Definition —** For every strictly positive real number $a$, the **natural logarithm** of $a$, denoted by $\ln a$ (or $\ln(a)$), is the **unique** real number $x$ such that $e^x = a$.
> The function $\ln : \; ]0\,;+\infty[ \; \to \mathbb{R}, \; x \mapsto \ln x$ is the **natural logarithm function**. It is the **inverse function** of the exponential function.
> $$\text{For } a > 0 \text{ and } x \in \mathbb{R} : \qquad e^x = a \iff x = \ln a.$$

**Notation.** The symbol $\ln$ abbreviates *logarithmus naturalis* (Latin for “natural logarithm”). It is read “the natural logarithm of $x$”, or informally “el-en of $x$”. Parentheses are optional when there is no ambiguity: $\ln 2$, $\ln x$; but one writes $\ln(x+1)$, and never $\ln x + 1$, which represents $(\ln x) + 1$.

> **💡 Did you know?** Napier did not use the symbol $\ln$, nor did he view it as the inverse of $e^x$: the base $e$ had not yet been identified or named! It was **Grégoire de Saint-Vincent** and **Alphonse Antonio de Sarasa** (around 1647–1649) who discovered that the area under the hyperbola $y = \frac{1}{x}$ exhibits logarithmic behavior (as we will explore in Chapter 50), and **Leonhard Euler**, in 1748, who systematically established the exponential and logarithm as mutual inverse operations. Napier's original tables corresponded closely to the function $x \mapsto 10^7 \ln\left(\frac{10^7}{x}\right)$.

#### 2.3 Immediate Consequences

From this definition follow directly:

| Property | Reason |
|---|---|
| $\ln 1 = 0$ | because $e^0 = 1$ |
| $\ln e = 1$ | because $e^1 = e$ |
| $e^{\ln a} = a$ for all $a > 0$ | $\ln a$ is *by definition* the exponent that yields $a$ |
| $\ln(e^x) = x$ for all $x \in \mathbb{R}$ | the unique exponent producing $e^x$ is $x$ |

The last two rows express cancellation: **applying “$\exp$” then “$\ln$”, or “$\ln$” then “$\exp$”, returns you to your starting value.** It is like opening a drawer and then closing it.

> **⚠️ Common Pitfall!** $e^{\ln a} = a$ holds only if $a > 0$. For instance, $e^{\ln(-3)}$ is **meaningless**, because $\ln(-3)$ does not exist in the real numbers. In contrast, $\ln(e^x) = x$ is valid for **every** real number $x$, even negative numbers: $\ln(e^{-5}) = -5$.

#### 2.4 The Curve: A Mirror Reflection of the Exponential

In a Cartesian coordinate system, if the point $M(a\,;b)$ lies on the graph of $\exp$ (so that $b = e^a$), then $a = \ln b$, which means the point $M'(b\,;a)$ lies on the graph of $\ln$. The point $M'$ is the **geometric reflection** of $M$ across the line $\Delta$ of equation $y = x$ (interchanging abscissa and ordinate).

> **The curves of $\exp$ and $\ln$ are reflections of each other across the first bisector line $y = x$.**

```
        y
        ▲            exp          y = x
        │             /          /
        │            /         /
        │           /        /
        │          /       /          ___---- ln
      e ┼         /      /     __---''
        │        /     /  _--''
      1 ┼ _ _ _ * _  /_-*'                 (e ; 1)
        │    _-'   /-'  ¦
        │_--'   _/'¦    ¦
   ─────┼─────/────*────┼──────────────────► x
        │   /      1    e
        │  /
        │ /   ← ln plunges toward -∞ as x → 0⁺
        │/
```

If you fold the coordinate plane along the diagonal line $y = x$, the exponential curve lands precisely on top of the logarithmic curve. The point $(0\,;1)$ of $\exp$ becomes $(1\,;0)$ on $\ln$; the horizontal asymptote $y = 0$ of $\exp$ (as $x \to -\infty$) transforms into the **vertical asymptote** $x = 0$ of $\ln$ (as $x \to 0^+$).

#### 2.5 Worked Examples

> **Worked Example 1 — Solve $e^x = 5$.**
> Since $5 > 0$, the equation has a unique solution: $x = \ln 5 \approx 1.609$.
> Verification: $e^{1.609} \approx 4.998$. ✔

> **Worked Example 2 — Solve $e^{2x-1} = 3$.**
> Since $3 > 0$, we have $e^{2x-1} = 3 \iff 2x - 1 = \ln 3 \iff x = \dfrac{1 + \ln 3}{2}$.
> Solution set: $\mathcal{S} = \left\{ \dfrac{1+\ln 3}{2} \right\} \approx 1.049$.

> **Worked Example 3 — Solve $\ln x = 2$.**
> The equation is defined only for $x > 0$. Then $\ln x = 2 \iff x = e^2$. Since $e^2 > 0$, the solution is valid: $\mathcal{S} = \{e^2\}$, where $e^2 \approx 7.389$.

> **Worked Example 4 — Solve $e^{x} = -4$ and $3e^{x} + 6 = 0$.**
> The exponential is strictly positive for all real inputs: $e^x = -4$ has **no solution**, so $\mathcal{S} = \varnothing$.
> Similarly, $3e^x + 6 = 0 \iff e^x = -2$: $\mathcal{S} = \varnothing$. Writing “$x = \ln(-2)$” is a fatal conceptual error.

> **Worked Example 5 — Simplify $A = e^{\ln 7}$, $B = \ln(e^{-3})$, $C = e^{-\ln 2}$, $D = \ln\left(\sqrt{e}\right)$.**
> - $A = 7$;
> - $B = -3$;
> - $C = \dfrac{1}{e^{\ln 2}} = \dfrac{1}{2}$;
> - $D = \ln\left(e^{1/2}\right) = \dfrac{1}{2}$.

> **⚠️ Common Pitfall! — Domain Boundaries.**
> - $\ln 0$ **does not exist**: no real power of $e$ equals $0$ (the exponential approaches $0$ asymptotically but never reaches it).
> - The logarithm of a negative number **does not exist** within the real numbers $\mathbb{R}$.
> - Before solving any equation involving $\ln(\dots)$, you must **always** begin by determining the domain of definition—the set of all $x$ for which every argument inside a logarithm is **strictly positive**.

---

### 3. Algebraic Properties: Napier's Dream Realized

#### 3.1 The Fundamental Identity

> **📐 Fundamental Theorem —** For all real numbers $a > 0$ and $b > 0$:
> $$\ln(ab) = \ln a + \ln b.$$

**In words:** the logarithm **converts products into sums**. This is precisely Stifel's top row, freed from all gaps: every positive real number participates.

> **✍️ Proof (Required Curriculum Proof) —** Let $a > 0$ and $b > 0$. Then $ab > 0$, so $\ln(ab)$ is defined.
> On the one hand, $e^{\ln(ab)} = ab$ by definition of the logarithm.
> On the other hand, applying the fundamental exponent rule $e^{x+y} = e^x e^y$:
> $$e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = a \times b.$$
> Consequently:
> $$e^{\ln(ab)} = e^{\ln a + \ln b}.$$
> Because the exponential function is strictly increasing, it is **injective** (distinct inputs yield distinct outputs). Thus, their exponents must be equal:
> $$\ln(ab) = \ln a + \ln b. \quad \blacksquare$$

The entire mystery is revealed: **the fundamental additive identity of the logarithm is the exact mirror image of the multiplicative identity $e^{x+y} = e^x e^y$ of the exponential**, reflected across the diagonal line $y = x$.

#### 3.2 Derived Algebraic Identities

> **📐 Properties —** For all real numbers $a > 0$, $b > 0$, and every integer $n \in \mathbb{Z}$:
> 1. $\ln\left(\dfrac{1}{a}\right) = -\ln a$
> 2. $\ln\left(\dfrac{a}{b}\right) = \ln a - \ln b$
> 3. $\ln(a^n) = n \ln a$
> 4. $\ln\left(\sqrt{a}\right) = \dfrac{1}{2} \ln a$

> **✍️ Proofs —**
> 1. Since $a \times \dfrac{1}{a} = 1$, we have $\ln a + \ln\left(\dfrac{1}{a}\right) = \ln 1 = 0$, which yields $\ln\left(\dfrac1a\right) = -\ln a$.
> 2. Using identity 1: $\ln\left(\dfrac ab\right) = \ln\left(a \times \dfrac1b\right) = \ln a + \ln\left(\dfrac1b\right) = \ln a - \ln b$.
> 3. For $n \in \mathbb{N}$, we proceed **by induction** (Chapter 43). Let $P(n)$ be the statement: “$\ln(a^n) = n\ln a$”.
>    - *Base step:* For $n = 0$, $\ln(a^0) = \ln 1 = 0 = 0 \times \ln a$. Thus $P(0)$ is true.
>    - *Inductive step:* Assume $P(n)$ holds for some integer $n \geq 0$. Then:
>      $$\ln(a^{n+1}) = \ln(a^n \times a) = \ln(a^n) + \ln a = n\ln a + \ln a = (n+1)\ln a.$$
>      Hence $P(n+1)$ is true.
>    - *Conclusion:* $P(n)$ holds for all $n \in \mathbb{N}$.
>
>    For negative integers $n < 0$, let $n = -m$ where $m \in \mathbb{N}$:
>    $$\ln(a^{-m}) = \ln\left(\dfrac{1}{a^m}\right) = -\ln(a^m) = -m \ln a = n \ln a.$$
> 4. Since $\left(\sqrt a\right)^2 = a$, applying property 3 gives $2 \ln\left(\sqrt a\right) = \ln a$, whence $\ln(\sqrt a) = \frac{1}{2}\ln a$. $\blacksquare$

> **💡 Did you know?** More generally, for $a > 0$ and any real number $r$, we **define** general powers by $a^r = e^{r \ln a}$, which immediately entails $\ln(a^r) = r \ln a$. This is how a digital computer evaluates $2^{\sqrt{2}}$ or $10^{0.3}$. In particular, $2^x = e^{x \ln 2}$: **all** constant-rate exponential growth is nothing more than base-$e$ exponential growth in disguise.

#### 3.3 Worked Examples

> **Worked Example 6 — Express in terms of $\ln 2$ and $\ln 3$:**
> $A = \ln 12$, $\quad B = \ln\left(\dfrac{9}{16}\right)$, $\quad C = \ln\sqrt{72}$, $\quad D = 3\ln 4 - 2\ln 6$.
> - $12 = 2^2 \times 3$, so $A = 2\ln 2 + \ln 3$.
> - $B = \ln(3^2) - \ln(2^4) = 2\ln 3 - 4 \ln 2$.
> - $72 = 2^3 \times 3^2$, so $C = \dfrac12 (3 \ln 2 + 2 \ln 3) = \dfrac32 \ln 2 + \ln 3$.
> - $D = 3 \times 2\ln 2 - 2(\ln 2 + \ln 3) = 6\ln 2 - 2\ln 2 - 2\ln 3 = 4\ln 2 - 2\ln 3$.

> **Worked Example 7 — Simplify $E = \ln(e^3) + \ln\left(\dfrac{1}{e}\right) - \ln\left(e\sqrt{e}\right)$.**
> We have $\ln(e^3) = 3$, $\ln\left(\frac1e\right) = -1$, and $\ln\left(e \sqrt e\right) = \ln\left(e^{3/2}\right) = \frac32$.
> Thus $E = 3 - 1 - \dfrac32 = \dfrac12$.

> **Worked Example 8 — Multiplying like a Navigator in 1620.**
> Suppose we need to compute $2.37 \times 5.81$ using a table of **common logarithms** ($\log_{10} x = \dfrac{\ln x}{\ln 10}$, which satisfies $\log(ab) = \log a + \log b$ and $\log 10 = 1$).
> The table provides: $\log 2.37 \approx 0.37475$ and $\log 5.81 \approx 0.76418$.
> We **add** them: $0.37475 + 0.76418 = 1.13893$.
> We search the table for the antilogarithm: the number whose mantissa is $0.13893$ is approximately $1.37697$.
> Adjusting for the characteristic $1$: the answer is $10^1 \times 1.37697 \approx 13.770$.
> Exact direct calculation: $2.37 \times 5.81 = 13.7697$. ✔ One addition and two table lookups completely replace long multiplication!

#### 3.4 Crucial Pitfalls to Avoid

> **⚠️ Common Pitfall! — Erroneous Identities.**
> - In general, $\ln(a + b) \neq \ln a + \ln b$. Counterexample: $\ln(1+1) = \ln 2 \approx 0.69$, whereas $\ln 1 + \ln 1 = 0$. The logarithm transforms **products**, never sums.
> - $\ln a \times \ln b \neq \ln(ab)$. Counterexample: $\ln e \times \ln e = 1 \times 1 = 1$, yet $\ln(e \cdot e) = \ln(e^2) = 2$.
> - $\dfrac{\ln a}{\ln b} \neq \ln\left(\dfrac ab\right)$ and $\neq \ln a - \ln b$.
> - $(\ln a)^2 \neq \ln(a^2)$. For instance, with $a = e^3$: $(\ln a)^2 = 3^2 = 9$, whereas $\ln(a^2) = \ln(e^6) = 6$. To avoid ambiguity, write $(\ln x)^2$ or $\ln^2 x$, never $\ln x^2$ when you mean the square of the logarithm.

> **⚠️ Common Pitfall! — Hidden Signs.**
> The formula $\ln(ab) = \ln a + \ln b$ strictly requires $a > 0$ **and** $b > 0$. However, the product $ab$ can be positive when both $a < 0$ and $b < 0$! For instance, $\ln\big((-2)(-3)\big) = \ln 6$ is well-defined, but $\ln(-2) + \ln(-3)$ is completely undefined in $\mathbb{R}$. The general identity, valid whenever $ab > 0$, is:
> $$\ln(ab) = \ln|a| + \ln|b|.$$
> Likewise, for any non-zero real number $x \neq 0$: $\ln(x^2) = 2 \ln|x|$ (and not $2\ln x$, which is defined only for $x > 0$).
> Practical consequence: the functions $x \mapsto \ln(x^2)$ and $x \mapsto 2\ln x$ **are not identical**: the former is defined on $\mathbb{R}^*$, while the latter is defined only on $]0\,;+\infty[$.

---

### 4. Comprehensive Analysis of the Natural Logarithm Function

#### 4.1 Differentiability and the Derivative

> **📐 Theorem —** The natural logarithm function $\ln$ is differentiable on $]0\,;+\infty[$, and for every real number $x > 0$:
> $$\ln'(x) = \dfrac{1}{x}.$$

> **✍️ Proof (Required Curriculum Proof) —**
> For every real number $x > 0$, we have the identity:
> $$e^{\ln x} = x.$$
> The function $\ln$ is differentiable on $]0\,;+\infty[$ because it is the inverse of the exponential function $\exp$, which is differentiable on $\mathbb{R}$ with a strictly positive derivative $\exp' = \exp > 0$.
> Differentiating both sides of the identity $e^{\ln x} = x$ with respect to $x$ via the chain rule $(e^{u(x)})' = u'(x)\, e^{u(x)}$ with $u(x) = \ln x$:
> $$(\ln)'(x) \times e^{\ln x} = 1.$$
> Since $e^{\ln x} = x$, this simplifies to:
> $$(\ln)'(x) \times x = 1 \iff \ln'(x) = \dfrac{1}{x}. \quad \blacksquare$$

> **💡 Alternative Proof via the Difference Quotient —**
> Let $x > 0$ be fixed and let $h \neq 0$ be such that $x + h > 0$. The difference quotient of $\ln$ at $x$ is:
> $$\tau(h) = \dfrac{\ln(x+h) - \ln x}{h} = \dfrac{1}{h} \ln\left(1 + \dfrac{h}{x}\right).$$
> Let $u = \ln\left(1 + \dfrac{h}{x}\right)$. Then $e^u = 1 + \dfrac{h}{x}$, which gives $h = x(e^u - 1)$.
> As $h \to 0$, $1 + \dfrac{h}{x} \to 1$, so $u \to \ln 1 = 0$ by the continuity of $\ln$.
> The difference quotient becomes:
> $$\tau(h) = \dfrac{u}{x(e^u - 1)} = \dfrac{1}{x} \times \dfrac{1}{\dfrac{e^u - 1}{u}}.$$
> By definition of the derivative of the exponential function at $0$, $\lim\limits_{u \to 0} \dfrac{e^u - 1}{u} = \exp'(0) = e^0 = 1$.
> Hence, taking the limit:
> $$\lim_{h \to 0} \tau(h) = \dfrac{1}{x} \times \dfrac{1}{1} = \dfrac{1}{x}. \quad \blacksquare$$

#### 4.2 Derivative of $\ln(u)$ and $\ln|u|$

When the argument of the logarithm is a differentiable function $u$, the chain rule $(f \circ u)' = u' \times (f' \circ u)$ immediately provides:

> **📐 Chain Rule for Logarithms —**
> Let $u$ be a differentiable, **strictly positive** function on an interval $I$. Then $f = \ln \circ u$, defined by $f(x) = \ln(u(x))$, is differentiable on $I$, and:
> $$(\ln(u))' = \dfrac{u'}{u}.$$
> More generally, if $u$ is differentiable and **nowhere zero** on $I$, then $x \mapsto \ln|u(x)|$ is differentiable on $I$, and:
> $$(\ln|u|)' = \dfrac{u'}{u}.$$

> **✍️ Proof for $\ln|u|$ when $u(x) < 0$ —**
> If $u(x) < 0$, then $|u(x)| = -u(x) > 0$. Hence $\ln|u(x)| = \ln(-u(x))$.
> Differentiating via the chain rule: $\big(\ln(-u)\big)' = \dfrac{(-u)'}{-u} = \dfrac{-u'}{-u} = \dfrac{u'}{u}$.
> The resulting derivative is identical regardless of the sign of $u(x)$! $\blacksquare$

> **🧭 Method — Differentiating an Expression Involving $\ln(u)$:**
> 1. Determine the domain where the argument $u(x)$ is strictly positive (or non-zero for $\ln|u|$).
> 2. Differentiate the inside function to find $u'(x)$.
> 3. Form the quotient $\dfrac{u'(x)}{u(x)}$ and simplify algebraically.

#### 4.3 Monotonicity and Sign of the Logarithm

For every $x \in \; ]0\,;+\infty[$, we have $x > 0$, and therefore $\ln'(x) = \dfrac{1}{x} > 0$.
The derivative is **strictly positive** across its entire domain.

> **Property —** The natural logarithm function is **strictly increasing** on $]0\,;+\infty[$.
> For all positive real numbers $a, b \in \; ]0\,;+\infty[$:
> - $\ln a = \ln b \iff a = b$ (injectivity);
> - $\ln a < \ln b \iff a < b$ (strict monotonicity).

Since $\ln 1 = 0$, strict monotonicity immediately establishes the **sign of $\ln x$**:
- If $0 < x < 1$, then $\ln x < \ln 1$, meaning **$\ln x < 0$**;
- If $x = 1$, then **$\ln 1 = 0$**;
- If $x > 1$, then $\ln x > \ln 1$, meaning **$\ln x > 0$**.

```
    x    │ 0         1         +∞
─────────┼────────────────────────
  ln'(x) │     +     │    +
─────────┼────────────────────────
  ln(x)  │     -     0    +
```

#### 4.4 Boundary Limits

> **📐 Boundary Limits Theorem —**
> 1. $\lim\limits_{x \to +\infty} \ln x = +\infty$
> 2. $\lim\limits_{x \to 0^+} \ln x = -\infty$
>
> The vertical axis $x = 0$ (the $y$-axis) is therefore a **vertical asymptote** to the graph of $\ln$.

> **✍️ Proofs (Required Curriculum Proofs) —**
> 1. **Limit at $+\infty$:**
>    For every natural number $n$, we have $\ln(2^n) = n \ln 2$.
>    Since $2 > 1$, $\ln 2 > 0$.
>    Consequently, $\lim\limits_{n \to +\infty} \ln(2^n) = \lim\limits_{n \to +\infty} (n \ln 2) = +\infty$.
>    Now choose an arbitrarily large real threshold $M > 0$. Since $n \ln 2 \to +\infty$, there exists an integer $N$ such that $N \ln 2 > M$.
>    For every real number $x \geq 2^N$, the strict monotonicity of $\ln$ implies:
>    $$\ln x \geq \ln(2^N) = N \ln 2 > M.$$
>    Hence, any interval $]M\,;+\infty[$ contains all values of $\ln x$ for all sufficiently large $x$. Therefore, $\lim\limits_{x \to +\infty} \ln x = +\infty$. $\blacksquare$
>
> 2. **Limit at $0^+$:**
>    Substitute $X = \dfrac{1}{x}$.
>    As $x \to 0^+$, we have $X \to +\infty$.
>    Then $\ln x = \ln\left(\dfrac{1}{X}\right) = -\ln X$.
>    Since $\lim\limits_{X \to +\infty} \ln X = +\infty$, composite limit rules yield:
>    $$\lim_{x \to 0^+} \ln x = \lim_{X \to +\infty} (-\ln X) = -\infty. \quad \blacksquare$$

#### 4.5 Variation Table and Graphic Profile

Assembling these results into a complete table of variations:

```
    x    │ 0                        1                        +∞
─────────┼─────────────────────────────────────────────────────
  ln'(x) │ ║           +                         +
─────────┼─╫───────────────────────────────────────────────────
         │ ║                                                +∞
  ln(x)  │ ║                                  ↗
         │ ║                     0       ↗
         │ ║               ↗
         │ ║ -∞
```

**Notable Tangent at $x = 1$:**
At $x = 1$, the slope is $\ln'(1) = \dfrac{1}{1} = 1$, and the point is $(1\,;0)$.
The equation of the tangent line $T_1$ at $(1\,;0)$ is:
$$y = \ln'(1)(x - 1) + \ln 1 = 1 \times (x - 1) + 0 \iff y = x - 1.$$

#### 4.6 Concavity and the Second Derivative

Differentiating once more to find the second derivative:
$$(\ln)''(x) = \left(\dfrac{1}{x}\right)' = -\dfrac{1}{x^2}.$$
For every $x \in \; ]0\,;+\infty[$, $x^2 > 0$, so $(\ln)''(x) < 0$.

> **Fundamental Concavity Property —**
> The natural logarithm function is **strictly concave** on $]0\,;+\infty[$.
> Consequently:
> 1. The graph of $\ln$ lies **strictly below every one of its tangent lines** (except at the point of tangency).
> 2. In particular, comparing it to its tangent at $x = 1$ ($y = x - 1$), we have for all $x > 0$:
>    $$\ln x \leq x - 1.$$
>    Equality holds if and only if $x = 1$.

Setting $x = 1 + h$ with $h > -1$, this fundamental inequality is equivalently written as:
$$\ln(1 + h) \leq h.$$

```
        y
        ▲                           y = x - 1 (tangent at x = 1)
        │                          /
        │                         /
        │                        /  . y = ln(x)
      1 ┼                       /.-'
        │                     .-'
        │                 _.-' /
      0 ┼───────────────*─────/────────► x
        │              / 1   / 2
     -1 ┼             /     /
        │            /
        │    :      /
        │    :  ln(x) ≤ x - 1
```

#### 4.7 Asymptotic Growth Rates (Comparative Growth)

Although $\lim\limits_{x \to +\infty} \ln x = +\infty$, this growth is **exceptionally sluggish**, slower than any positive power of $x$, no matter how small the exponent.
For example:
- $\ln(10) \approx 2.3$;
- $\ln(10^6) \approx 13.8$;
- $\ln(10^{12}) \approx 27.6$.
For $\ln x$ to reach a modest value of $100$, one requires $x = e^{100} \approx 2.68 \times 10^{43}$—a quantity far exceeding the number of grains of sand on the entire planet Earth!

This extreme slowness gives rise to the classic **comparative growth theorems**.

> **📐 Comparative Growth Theorems (Required Curriculum Proofs) —**
> For every positive integer $n \geq 1$:
> 1. $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0$
> 2. $\lim\limits_{x \to 0^+} x^n \ln x = 0$
> 3. $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1 \quad \text{or equivalently} \quad \lim\limits_{x \to 1} \dfrac{\ln x}{x-1} = 1$.

> **✍️ Proof of $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$ (Required Curriculum Proof) —**
> Recall the comparative growth limit of the exponential function (established in Chapter 45):
> $$\lim_{t \to +\infty} \dfrac{e^t}{t} = +\infty.$$
> Perform the change of variable $t = \ln x$, so that $x = e^t$.
> As $x \to +\infty$, we have $t \to +\infty$.
> The quotient $\dfrac{\ln x}{x}$ becomes:
> $$\dfrac{\ln x}{x} = \dfrac{t}{e^t} = \dfrac{1}{\dfrac{e^t}{t}}.$$
> Taking the limit as $t \to +\infty$:
> $$\lim_{x \to +\infty} \dfrac{\ln x}{x} = \lim_{t \to +\infty} \dfrac{1}{\dfrac{e^t}{t}} = \dfrac{1}{+\infty} = 0. \quad \blacksquare$$

> **✍️ Proof of $\lim\limits_{x \to 0^+} x \ln x = 0$ (Required Curriculum Proof) —**
> Perform the substitution $X = \dfrac{1}{x}$.
> As $x \to 0^+$, we have $X \to +\infty$.
> Thus:
> $$x \ln x = \dfrac{1}{X} \ln\left(\dfrac{1}{X}\right) = \dfrac{-\ln X}{X} = -\dfrac{\ln X}{X}.$$
> By the preceding result, $\lim\limits_{X \to +\infty} \dfrac{\ln X}{X} = 0$.
> Therefore:
> $$\lim_{x \to 0^+} x \ln x = 0. \quad \blacksquare$$

> **✍️ Proof of $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1$ —**
> This expression is simply the difference quotient of the function $\ln$ evaluated at $x_0 = 1$:
> $$\lim_{h \to 0} \dfrac{\ln(1+h) - \ln 1}{h} = \ln'(1) = \dfrac{1}{1} = 1. \quad \blacksquare$$

---

### 5. Methods: Equations, Inequalities, and Geometric Thresholds

#### 5.1 Solving Equations with $\ln$

> **🧭 Method — Standard Protocol for Logarithmic Equations:**
> 1. **Validity Domain:** Find the domain $D$ where all arguments inside logarithms are **strictly positive**.
> 2. **Consolidation:** Use algebraic identities to consolidate the expression into one of the standard forms:
>    - $\ln(A(x)) = \ln(B(x)) \iff A(x) = B(x)$;
>    - or $\ln(A(x)) = k \iff A(x) = e^k$.
> 3. **Algebraic Resolution:** Solve the resulting polynomial, rational, or linear equation.
> 4. **Domain Verification:** Check which solutions lie within the validity domain $D$; discard any extraneous solutions.

> **Worked Example 9 — Equation with Two Logarithms.**
> Solve $\ln(2x - 3) = \ln(x + 5)$.
> - *Step 1: Domain.*
>   We need $2x - 3 > 0 \iff x > \dfrac{3}{2}$ and $x + 5 > 0 \iff x > -5$.
>   Intersecting gives $D = \left]\dfrac{3}{2}\,;+\infty\right[$.
> - *Steps 2 & 3: Solving.*
>   For $x \in D$:
>   $$\ln(2x - 3) = \ln(x + 5) \iff 2x - 3 = x + 5 \iff x = 8.$$
> - *Step 4: Conclusion.*
>   $8 \in D$ (since $8 > 1.5$). The solution set is $\mathcal{S} = \{8\}$.

> **Worked Example 10 — Sum of Logarithms and Extraneous Solutions.**
> Solve $\ln(x) + \ln(x - 2) = \ln 3$.
> - *Step 1: Domain.*
>   We require $x > 0$ and $x - 2 > 0 \iff x > 2$.
>   Hence the validity domain is $D = \; ]2\,;+\infty[$.
> - *Step 2: Consolidation.*
>   For all $x \in D$, $\ln(x) + \ln(x - 2) = \ln(x(x - 2))$. The equation becomes:
>   $$\ln(x^2 - 2x) = \ln 3 \iff x^2 - 2x = 3 \iff x^2 - 2x - 3 = 0.$$
> - *Step 3: Quadratic Roots.*
>   $\Delta = (-2)^2 - 4(1)(-3) = 4 + 12 = 16 = 4^2$.
>   The roots are $x_1 = \dfrac{2 - 4}{2} = -1$ and $x_2 = \dfrac{2 + 4}{2} = 3$.
> - *Step 4: Domain Check.*
>   $x_1 = -1 \notin D$: for this value, $\ln(-1)$ is undefined! It is an extraneous root arising from $(-1) \times (-3) = 3$.
>   $x_2 = 3 \in D$ since $3 > 2$.
>   The unique valid solution is $\mathcal{S} = \{3\}$.

#### 5.2 Equations Involving Change of Variables

When the unknown appears as powers of $\ln x$, substitute a new variable.

> **Worked Example 11 — Quadratic Equation in $\ln x$.**
> Solve $2(\ln x)^2 - 5\ln x + 2 = 0$ on $]0\,;+\infty[$.
> Set $X = \ln x$. The equation transforms into:
> $$2X^2 - 5X + 2 = 0.$$
> The discriminant is $\Delta = (-5)^2 - 4(2)(2) = 25 - 16 = 9 = 3^2$.
> The solutions for $X$ are:
> $$X_1 = \dfrac{5 - 3}{4} = \dfrac{1}{2} \quad \text{and} \quad X_2 = \dfrac{5 + 3}{4} = 2.$$
> Converting back to $x$:
> - $\ln x = \dfrac{1}{2} \iff x = e^{1/2} = \sqrt{e}$;
> - $\ln x = 2 \iff x = e^2$.
> Both values are strictly positive. The solution set is $\mathcal{S} = \{\sqrt{e}\,; e^2\}$.

#### 5.3 Solving Inequalities with $\ln$

Because the logarithm is strictly increasing, it preserves inequalities:

$$\text{For all } A > 0 \text{ and } B > 0 : \quad \ln A < \ln B \iff A < B.$$

> **Worked Example 12 — Simple Inequality.**
> Solve $\ln(3x - 1) \leq 2$.
> 1. *Domain:* $3x - 1 > 0 \iff x > \dfrac{1}{3}$. Thus $D = \left]\dfrac{1}{3}\,;+\infty\right[$.
> 2. *Solving:* Express $2$ as $\ln(e^2)$:
>    $$\ln(3x - 1) \leq \ln(e^2) \iff 3x - 1 \leq e^2 \iff 3x \leq e^2 + 1 \iff x \leq \dfrac{e^2 + 1}{3}.$$
> 3. *Intersection with $D$:*
>    Since $\dfrac{e^2 + 1}{3} \approx \dfrac{7.389 + 1}{3} \approx 2.796 > \dfrac{1}{3}$, the solution set is:
>    $$\mathcal{S} = \left] \dfrac{1}{3} \; ; \; \dfrac{e^2 + 1}{3} \right].$$

#### 5.4 Finding Thresholds for Geometric Sequences

This is one of the most frequent exam applications: determining the smallest index $n$ at which a geometric sequence surpasses or falls below a prescribed value.

> **🧭 Method — Solving $q^n < S$ or $q^n > S$:**
> 1. Isolate the power $q^n$ on one side of the inequality.
> 2. Apply $\ln$ to both sides (valid because $q > 0$ and $S > 0$).
> 3. Apply the exponent identity $\ln(q^n) = n \ln q$.
> 4. **Divide by $\ln q$, paying extreme attention to the sign of $\ln q$:**
>    - If $q > 1$, then $\ln q > 0$: the inequality direction is **preserved**;
>    - If $0 < q < 1$, then $\ln q < 0$: the inequality direction is **reversed** ($\leq$ becomes $\geq$)!

> **Worked Example 13 — Depreciation Threshold (Inequality Reversal).**
> A new piece of industrial machinery costs $\$20,000$. Each year, its value depreciates by $15\%$.
> After how many years will its book value fall below $\$5,000$?
> 
> *Modeling:* The value after $n$ years is $V_n = 20\,000 \times (1 - 0.15)^n = 20\,000 \times 0.85^n$.
> We seek the smallest non-negative integer $n$ such that:
> $$20\,000 \times 0.85^n < 5\,000 \iff 0.85^n < \dfrac{5\,000}{20\,000} \iff 0.85^n < 0.25.$$
> Applying $\ln$:
> $$\ln(0.85^n) < \ln(0.25) \iff n \ln(0.85) < \ln(0.25).$$
> Since $0 < 0.85 < 1$, we have $\ln(0.85) \approx -0.1625 < 0$.
> Dividing by this **negative** quantity reverses the inequality:
> $$n > \dfrac{\ln(0.25)}{\ln(0.85)}.$$
> Calculating: $\dfrac{\ln(0.25)}{\ln(0.85)} \approx \dfrac{-1.38629}{-0.16252} \approx 8.53$.
> Since $n$ must be an integer number of years, the minimum integer satisfying this is **$n = 9$**.
> After 9 years, the machine will be worth less than $\$5,000$.

> **💻 Associated Python Script — Threshold Search:**
> ```python
> def threshold_decay(initial_value, rate, target):
>     n = 0
>     v = initial_value
>     while v >= target:
>         v = v * (1 - rate)
>         n += 1
>     return n
>
> print("Years required:", threshold_decay(20000, 0.15, 5000))
> # Output: Years required: 9
> ```

---

### 6. Real-World Logarithmic Scales

Why are logarithms ubiquitous throughout all experimental sciences?
Because both nature and human perception frequently operate not by **additive differences**, but by **multiplicative ratios** (the Weber-Fechner psycho-physical law). When our ears perceive a sound as twice as loud, the underlying acoustic power has not increased by a few milliwatts: it has increased tenfold!

#### 6.1 Acidity and pH in Chemistry

In aqueous chemistry, the oxonium ion concentration $[H_3O^+]$ ranges from $1\,\text{mol}\cdot\text{L}^{-1}$ (concentrated hydrochloric acid) down to $10^{-14}\,\text{mol}\cdot\text{L}^{-1}$ (concentrated sodium hydroxide). This spans a dynamic ratio of $10^{14}$—one hundred trillion!
To compress this enormous span into convenient numbers between 0 and 14, the Danish chemist **Søren Sørensen** introduced the **pH** (potential of hydrogen) in 1909 using the common logarithm $\log_{10}(x) = \dfrac{\ln x}{\ln 10}$:

> **📐 Definition of pH —**
> $$\text{pH} = -\log_{10}\left(\dfrac{[H_3O^+]}{c_0}\right) = -\dfrac{\ln([H_3O^+]/c_0)}{\ln 10}$$
> where $c_0 = 1\,\text{mol}\cdot\text{L}^{-1}$ is the standard reference concentration.
> Inversely: $[H_3O^+] = 10^{-\text{pH}}\,\text{mol}\cdot\text{L}^{-1}$.

> **Direct Consequence:**
> When the pH drops by a single unit (for instance from 7 to 6), the concentration of $[H_3O^+]$ ions **multiplies by 10**. If the pH drops from 7 to 4, it multiplies by $10^3 = 1\,000$!

#### 6.2 Acoustics and Decibels

The human ear detects acoustic intensities spanning from the faintest threshold of hearing ($I_0 = 10^{-12}\,\text{W}\cdot\text{m}^{-2}$) to the roar of a rocket launch ($100\,\text{W}\cdot\text{m}^{-2}$)—a dynamic range of $10^{14}$.
The **sound intensity level** $L$, measured in **decibels (dB)**, is defined as:

> **📐 Sound Level in Decibels —**
> $$L = 10 \log_{10}\left(\dfrac{I}{I_0}\right) = 10 \dfrac{\ln(I / I_0)}{\ln 10}.$$

> **Worked Example 14 — Do Two Vacuum Cleaners Make Twice the Noise?**
> Suppose a vacuum cleaner emits an acoustic intensity $I_1$ resulting in a sound level of $L_1 = 70\,\text{dB}$.
> Two identical vacuum cleaners operating simultaneously produce double the acoustic intensity: $I_2 = 2 I_1$.
> What is the resulting sound level $L_2$?
> $$L_2 = 10 \log_{10}\left(\dfrac{2 I_1}{I_0}\right) = 10\left[\log_{10}(2) + \log_{10}\left(\dfrac{I_1}{I_0}\right)\right] = 10 \log_{10}(2) + L_1.$$
> Since $10 \log_{10}(2) \approx 10 \times 0.30103 \approx 3\,\text{dB}$, we have:
> $$L_2 \approx 70 + 3 = 73\,\text{dB}!$$
> **Doubling the physical acoustic power increases the perceived sound level by only 3 decibels!**

#### 6.3 Earthquakes and the Richter Magnitude Scale

The Richter scale relates the seismic energy $E$ released at an earthquake's epicenter via a formula of the form:
$$M = \dfrac{2}{3} \log_{10}\left(\dfrac{E}{E_0}\right).$$
If the magnitude increases by 1 unit, we have $\Delta M = 1 = \dfrac{2}{3} \log_{10}\left(\dfrac{E'}{E}\right)$, whence:
$$\log_{10}\left(\dfrac{E'}{E}\right) = \dfrac{3}{2} = 1.5 \iff \dfrac{E'}{E} = 10^{1.5} = 10 \sqrt{10} \approx 31.6.$$
A magnitude 7 earthquake releases **31.6 times more energy** than a magnitude 6 earthquake, and $(31.6)^2 \approx 1\,000$ times more energy than a magnitude 5 earthquake!

#### 6.4 Radiocarbon Dating and Half-Life

In any living organism, the ratio of radioactive carbon-14 to stable carbon-12 remains constant. Upon death, metabolic intake ceases and carbon-14 decays exponentially according to:
$$N(t) = N_0 \, e^{-\lambda t},$$
where $\lambda > 0$ is the radioactive decay constant of the isotope.

The **half-life** $t_{1/2}$ is the duration after which half of the original radioactive nuclei have decayed:
$$N(t_{1/2}) = \dfrac{N_0}{2} \iff N_0 e^{-\lambda t_{1/2}} = \dfrac{N_0}{2} \iff e^{-\lambda t_{1/2}} = \dfrac{1}{2}.$$
Applying the natural logarithm:
$$-\lambda t_{1/2} = \ln\left(\dfrac{1}{2}\right) = -\ln 2 \iff t_{1/2} = \dfrac{\ln 2}{\lambda}.$$
For carbon-14, $t_{1/2} \approx 5\,730$ years.
If a sample of charcoal recovered from a prehistoric cave retains $30\%$ of its original carbon-14 activity, its age $t$ is obtained by solving:
$$\dfrac{N(t)}{N_0} = 0.30 \iff e^{-\lambda t} = 0.30 \iff -\lambda t = \ln(0.30) \iff t = -\dfrac{\ln(0.30)}{\lambda} = -5\,730 \times \dfrac{\ln(0.30)}{\ln 2} \approx 9\,950 \text{ years}.$$

---

### Key Takeaways

#### 1. Definition and Fundamental Link with the Exponential
- For all $a > 0$ and $x \in \mathbb{R}$: $e^x = a \iff x = \ln a$.
- The function $\ln$ is defined, continuous, and differentiable on $]0\,;+\infty[$.
- Inversion identities: $e^{\ln a} = a$ (for all $a > 0$) and $\ln(e^x) = x$ (for all $x \in \mathbb{R}$).
- $\ln 1 = 0$ and $\ln e = 1$.
- The graphs of $\exp$ and $\ln$ are reflections across the first bisector line $y = x$.

#### 2. Algebraic Identities (for all $a > 0, b > 0$)
- Fundamental relation: $\ln(ab) = \ln a + \ln b$.
- Reciprocals and quotients: $\ln\left(\dfrac{1}{a}\right) = -\ln a$ and $\ln\left(\dfrac{a}{b}\right) = \ln a - \ln b$.
- Powers and roots: $\ln(a^n) = n\ln a$ ($n \in \mathbb{Z}$) and $\ln\left(\sqrt{a}\right) = \dfrac{1}{2}\ln a$.

#### 3. Calculus of the Logarithm Function
- Derivative: $(\ln x)' = \dfrac{1}{x} > 0$ on $]0\,;+\infty[$.
- Chain rule: $\big(\ln(u)\big)' = \dfrac{u'}{u}$ (for $u > 0$).
- Strictly increasing on $]0\,;+\infty[$: $\ln a < \ln b \iff a < b$.
- Sign: $\ln x < 0$ on $]0\,;1[$, $\ln 1 = 0$, and $\ln x > 0$ on $]1\,;+\infty[$.
- Limits: $\lim\limits_{x \to 0^+} \ln x = -\infty$ (vertical asymptote $x = 0$) and $\lim\limits_{x \to +\infty} \ln x = +\infty$.
- Concavity: $(\ln)''(x) = -\dfrac{1}{x^2} < 0$. The function is strictly concave, leading to $\ln x \leq x - 1$ for all $x > 0$.

#### 4. Essential Comparative Growth Limits
- $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0 \quad (n \geq 1)$.
- $\lim\limits_{x \to 0^+} x^n \ln x = 0 \quad (n \geq 1)$.
- $\lim\limits_{h \to 0} \dfrac{\ln(1+h)}{h} = 1$.

#### 5. Solving Equations and Thresholds
- Always begin by determining the validity domain $D$ ($u(x) > 0$).
- For $q^n < S$ with $0 < q < 1$: $n > \dfrac{\ln S}{\ln q}$ (because $\ln q < 0$ reverses the inequality symbol).

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 48.1 —** Mental Arithmetic and Simplifications.
Compute the exact values of the following numbers without a calculator:
1. $A = \ln(e^5)$
2. $B = e^{\ln 11}$
3. $C = \ln\left(\dfrac{1}{e^4}\right)$
4. $D = \ln\left(\sqrt[3]{e}\right)$ (recall: $\sqrt[3]{e} = e^{1/3}$)
5. $E = e^{-\ln 3}$
6. $F = \ln(e \sqrt{e})$

**Exercise 48.2 —** Prime Factor Decomposition.
Setting $a = \ln 2$ and $b = \ln 5$, express in terms of $a$ and $b$:
1. $\ln 10$
2. $\ln 20$
3. $\ln 50$
4. $\ln(0.04)$
5. $\ln\left(\dfrac{\sqrt{2}}{25}\right)$

**Exercise 48.3 —** Domains of Definition.
Determine the domain of definition of each of the following functions:
1. $f_1(x) = \ln(3x - 12)$
2. $f_2(x) = \ln(x^2 - 9)$
3. $f_3(x) = \ln\left(\dfrac{x+1}{2-x}\right)$
4. $f_4(x) = \ln(x^2 + 1)$
5. $f_5(x) = \dfrac{1}{\ln x}$

**Exercise 48.4 —** Simple Derivatives.
Calculate the derivative of the following functions on their domain of differentiability:
1. $g_1(x) = \ln(4x + 7)$
2. $g_2(x) = \ln(x^2 + 3)$
3. $g_3(x) = x^2 \ln x$
4. $g_4(x) = \dfrac{\ln x}{x}$
5. $g_5(x) = (\ln x)^3$

**Exercise 48.5 —** Elementary Equations.
Solve in $\mathbb{R}$:
1. $\ln x = 4$
2. $\ln(2x - 1) = 0$
3. $e^x = 9$
4. $e^{3x-2} = 5$
5. $\ln(x^2) = 6$

**Exercise 48.6 —** Elementary Inequalities.
Solve in $\mathbb{R}$:
1. $\ln x > -2$
2. $\ln(3 - x) \leq 1$
3. $e^{2x} \geq 7$
4. $2\ln x + 3 < 0$

**Exercise 48.7 —** Direct Limits.
Determine the following limits:
1. $\lim\limits_{x \to +\infty} (\ln x + 2x)$
2. $\lim\limits_{x \to 0^+} (x^2 - \ln x)$
3. $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^2}$
4. $\lim\limits_{x \to 0^+} x^3 \ln x$

---

#### Level ★★ (Exploration and Exam Preparation)

**Exercise 48.8 —** Quadratic Equation in Logarithms.
Solve in $\mathbb{R}$ the equation:
$$(\ln x)^2 - 3\ln x - 10 = 0.$$

**Exercise 48.9 —** Equation with a Sum of Logarithms.
Solve in $\mathbb{R}$ the equation:
$$\ln(x + 2) + \ln(x - 1) = \ln(4x + 8).$$

**Exercise 48.10 —** System of Non-Linear Equations.
Solve in $\mathbb{R}^2$ the system:
$$\begin{cases} x + y = 30 \\ \ln x + \ln y = 3\ln 2 + \ln 27 \end{cases}$$

**Exercise 48.11 —** Study of a Classic Logarithmic Function.
Let $f$ be the function defined on $]0\,;+\infty[$ by:
$$f(x) = x - 2 - \ln x.$$
1. Determine the limits of $f$ at $0$ and at $+\infty$.
2. Compute $f'(x)$ and determine its sign.
3. Draw up the complete variation table of $f$.
4. Deduce the number of real roots of $f(x) = 0$ on $]0\,;+\infty[$.

**Exercise 48.12 —** Tangent Passing Through the Origin.
Does there exist a tangent line to the graph of $\ln$ that passes through the origin $(0\,;0)$? If so, find the coordinates of the point of tangency and the equation of this tangent line.

**Exercise 48.13 —** Resolving Indeterminate Forms.
Evaluate the following limits, justifying your reasoning carefully:
1. $\lim\limits_{x \to +\infty} (x - \ln x)$
2. $\lim\limits_{x \to +\infty} \dfrac{\ln(x^2 + 1)}{x}$
3. $\lim\limits_{x \to 0^+} x \ln\left(1 + \dfrac{1}{x}\right)$
4. $\lim\limits_{x \to 1} \dfrac{\ln x}{x^2 - 1}$

**Exercise 48.14 —** Investment Doubling Threshold.
A capital sum of $\$10,000$ is invested at an annual compound interest rate of $3.5\%$.
1. Express the accumulated capital $C_n$ after $n$ years.
2. Determine by exact calculation (using logarithms) the number of years required for the initial investment to double.
3. Compare this with the famous “Rule of 70” used in finance: the doubling time at an interest rate of $t\%$ per annum is approximately $70 / t$. Prove why this rule works using the first-order affine approximation of $\ln(1+u)$ near $0$.

**Exercise 48.15 —** Study of a Rational Logarithmic Function and Concavity.
Let $f$ be defined on $]0\,;+\infty[$ by $f(x) = \dfrac{\ln x}{x}$.
1. Determine the limits of $f$ at $0$ and at $+\infty$. Give the graphical interpretations.
2. Calculate $f'(x)$ and establish the complete table of variations of $f$.
3. Identify the global maximum of $f$.
4. Without a calculator, compare the numbers $e^{\pi}$ and $\pi^e$ using the monotonicity of $f$.
5. Compute $f''(x)$ and study the convexity of $f$. Identify the inflection point.

**Exercise 48.16 —** Convexity Inequality.
1. Prove that for all $x > 0$, $\ln x \leq x - 1$.
2. Deduce that for all $t > -1$, $\ln(1+t) \leq t$.
3. Applying this inequality with $t = -\dfrac{1}{n+1}$, show that for all integers $n \geq 1$:
   $$\left(1 + \dfrac{1}{n}\right)^n \leq e \leq \left(1 + \dfrac{1}{n}\right)^{n+1}.$$

**Exercise 48.17 —** Dating the Chauvet Cave.
Prehistoric rock paintings were discovered in a cave. Charcoal fragments collected near the paintings exhibit an activity of $2.4$ disintegrations per minute per gram of carbon, whereas fresh modern wood exhibits $15.3$ disintegrations per minute per gram.
Given that the half-life of carbon-14 is $T = 5\,730$ years, estimate the age of the cave paintings.

**Exercise 48.18 —** Threshold and Arithmetico-Geometric Sequence (Exam Style).
Let $(u_n)$ be the sequence defined by $u_0 = 10$ and for all $n \in \mathbb{N}$, $u_{n+1} = 0.6 u_n + 2$.
1. Prove that the sequence $(v_n)$ defined by $v_n = u_n - 5$ is a geometric sequence whose common ratio and first term you will determine.
2. Express $v_n$, and then $u_n$, as a function of $n$.
3. Determine algebraically the smallest integer $n$ such that $|u_n - 5| < 10^{-4}$.

---

#### Level ★★★ (In-Depth Challenges)

**Exercise 48.19 —** The Harmonic Sum and Euler's Constant.
Let $H_n = \sum\limits_{k=1}^n \dfrac{1}{k} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}$.
1. Using the inequality $\ln(1+x) \leq x$ for $x > 0$, show that for every integer $k \geq 1$:
   $$\ln(k+1) - \ln k \leq \dfrac{1}{k}.$$
2. Using the inequality $\ln(1-x) \leq -x$ for $x \in \; ]0\,;1[$, show that for every integer $k \geq 2$:
   $$\dfrac{1}{k} \leq \ln k - \ln(k-1).$$
3. Summing these inequalities from $k = 1$ to $n$, establish the bounding:
   $$\ln(n+1) \leq H_n \leq 1 + \ln n.$$
4. Deduce the limit of $(H_n)_{n \geq 1}$. What does this say about the harmonic series?
5. Determine the limit of $\dfrac{H_n}{\ln n}$ as $n \to +\infty$.

**Exercise 48.20 —** Stirling's Formula (First Approach via Logarithms).
We wish to estimate $n! = 1 \times 2 \times 3 \times \dots \times n$.
1. Express $\ln(n!)$ as a summation.
2. Using the bounding strategy of the previous exercise, obtain an estimate for $\ln(n!)$ in terms of the integral of $\ln x$.

**Exercise 48.21 —** The Transcendental Equation $x^a = a^x$.
Let $a > 0$ be a fixed real parameter. We seek positive real solutions to $x^a = a^x$.
1. Show that for all $x > 0$, the equation is equivalent to $\dfrac{\ln x}{x} = \dfrac{\ln a}{a}$.
2. Using the study of $f(x) = \dfrac{\ln x}{x}$ from Exercise 48.15, discuss the number of solutions depending on the value of $a$.
3. Find the unique pair of distinct positive integers $(x\,;y)$ with $x < y$ satisfying $x^y = y^x$.

**Exercise 48.22 —** Logarithmic Differentiation of Products.
Let $f$ be the product of $n$ differentiable, strictly positive functions: $f(x) = u_1(x) u_2(x) \dots u_n(x)$.
1. Show that $\dfrac{f'(x)}{f(x)} = \sum\limits_{k=1}^n \dfrac{u'_k(x)}{u_k(x)}$.
2. Application: Rapidly compute the derivative of $g(x) = (x+1)^3 (2x-1)^4 (x^2+5)^2$.

---

### Solutions

#### Level ★ Solutions

**Solution 48.1:**
1. $A = \ln(e^5) = 5$.
2. $B = e^{\ln 11} = 11$.
3. $C = \ln(e^{-4}) = -4$.
4. $D = \ln(e^{1/3}) = \dfrac{1}{3}$.
5. $E = e^{-\ln 3} = e^{\ln(1/3)} = \dfrac{1}{3}$.
6. $F = \ln(e^1 \times e^{1/2}) = \ln(e^{3/2}) = \dfrac{3}{2}$.

**Solution 48.2:**
1. $\ln 10 = \ln(2 \times 5) = \ln 2 + \ln 5 = a + b$.
2. $\ln 20 = \ln(2^2 \times 5) = 2\ln 2 + \ln 5 = 2a + b$.
3. $\ln 50 = \ln(2 \times 5^2) = \ln 2 + 2\ln 5 = a + 2b$.
4. $\ln(0.04) = \ln\left(\dfrac{4}{100}\right) = \ln\left(\dfrac{1}{25}\right) = -\ln(5^2) = -2b$.
5. $\ln\left(\dfrac{\sqrt{2}}{25}\right) = \ln(\sqrt 2) - \ln(5^2) = \dfrac{1}{2}a - 2b$.

**Solution 48.3:**
1. $3x - 12 > 0 \iff 3x > 12 \iff x > 4$. Domain: $D_1 = \; ]4\,;+\infty[$.
2. $x^2 - 9 > 0 \iff (x-3)(x+3) > 0$. The roots are $-3$ and $3$; the quadratic is positive outside the roots. Domain: $D_2 = \; ]-\infty\,;-3[\; \cup \; ]3\,;+\infty[$.
3. $\dfrac{x+1}{2-x} > 0$. By a sign table, the quotient is positive strictly between $-1$ and $2$. Domain: $D_3 = \; ]-1\,;2[$.
4. For all real $x$, $x^2 \geq 0 \implies x^2 + 1 \geq 1 > 0$. Domain: $D_4 = \mathbb{R}$.
5. We require $x > 0$ (for $\ln x$ to exist) and $\ln x \neq 0 \iff x \neq 1$. Domain: $D_5 = \; ]0\,;1[\; \cup \; ]1\,;+\infty[$.

**Solution 48.4:**
1. Using $(\ln u)' = \dfrac{u'}{u}$ with $u(x) = 4x + 7$ and $u'(x) = 4$: $g'_1(x) = \dfrac{4}{4x+7}$.
2. With $u(x) = x^2 + 3$, $u'(x) = 2x$: $g'_2(x) = \dfrac{2x}{x^2+3}$.
3. Product rule $(uv)' = u'v + uv'$: $g'_3(x) = 2x \ln x + x^2 \times \dfrac{1}{x} = 2x \ln x + x = x(2\ln x + 1)$.
4. Quotient rule: $g'_4(x) = \dfrac{\frac{1}{x} \times x - \ln x \times 1}{x^2} = \dfrac{1 - \ln x}{x^2}$.
5. Power rule $(u^3)' = 3u^2 u'$: $g'_5(x) = 3(\ln x)^2 \times \dfrac{1}{x} = \dfrac{3(\ln x)^2}{x}$.

**Solution 48.5:**
1. $\ln x = 4 \iff x = e^4$. $\mathcal{S} = \{e^4\}$.
2. Domain $x > 1/2$. $\ln(2x - 1) = 0 = \ln 1 \iff 2x - 1 = 1 \iff 2x = 2 \iff x = 1 \in D$. $\mathcal{S} = \{1\}$.
3. $e^x = 9 \iff x = \ln 9 = 2\ln 3$. $\mathcal{S} = \{2\ln 3\}$.
4. $e^{3x-2} = 5 \iff 3x - 2 = \ln 5 \iff 3x = 2 + \ln 5 \iff x = \dfrac{2 + \ln 5}{3}$. $\mathcal{S} = \left\{\dfrac{2+\ln 5}{3}\right\}$.
5. Domain: $x \neq 0$. $\ln(x^2) = 6 \iff x^2 = e^6 \iff x = e^3$ or $x = -e^3$. $\mathcal{S} = \{-e^3\,; e^3\}$.

**Solution 48.6:**
1. $\ln x > -2 \iff x > e^{-2} = \dfrac{1}{e^2}$. $\mathcal{S} = \left]\dfrac{1}{e^2}\,;+\infty\right[$.
2. Domain: $3 - x > 0 \iff x < 3$. $\ln(3 - x) \leq 1 = \ln e \iff 3 - x \leq e \iff x \geq 3 - e$. Intersecting with the domain: $\mathcal{S} = [3 - e\,;3[$.
3. $e^{2x} \geq 7 \iff 2x \geq \ln 7 \iff x \geq \dfrac{\ln 7}{2}$. $\mathcal{S} = \left[\dfrac{\ln 7}{2}\,;+\infty\right[$.
4. Domain $x > 0$. $2\ln x < -3 \iff \ln x < -\dfrac{3}{2} \iff 0 < x < e^{-3/2} = \dfrac{1}{e\sqrt{e}}$. $\mathcal{S} = \left]0\,; e^{-3/2}\right[$.

**Solution 48.7:**
1. Sum of limits: $\lim\limits_{x \to +\infty} \ln x = +\infty$ and $\lim\limits_{x \to +\infty} 2x = +\infty$, so the limit is $+\infty$.
2. Difference of limits: $\lim\limits_{x \to 0^+} x^2 = 0$ and $\lim\limits_{x \to 0^+} \ln x = -\infty$, so $\lim\limits_{x \to 0^+} (x^2 - \ln x) = 0 - (-\infty) = +\infty$.
3. Comparative growth: $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^2} = 0$.
4. Comparative growth: $\lim\limits_{x \to 0^+} x^3 \ln x = 0$.

---

#### Level ★★ Solutions

**Solution 48.8:**
The equation is defined on $]0\,;+\infty[$.
Set $X = \ln x$. The equation becomes $X^2 - 3X - 10 = 0$.
Discriminant: $\Delta = (-3)^2 - 4(1)(-10) = 9 + 40 = 49 = 7^2$.
Roots: $X_1 = \dfrac{3 - 7}{2} = -2$ and $X_2 = \dfrac{3 + 7}{2} = 5$.
Back-substituting to $x$:
- $\ln x = -2 \iff x = e^{-2}$;
- $\ln x = 5 \iff x = e^5$.
Both values are strictly positive. Thus $\mathcal{S} = \{e^{-2}\,; e^5\}$.

**Solution 48.9:**
Validity domain:
We require $x + 2 > 0 \iff x > -2$, $x - 1 > 0 \iff x > 1$, and $4x + 8 > 0 \iff x > -2$.
Their intersection is $D = \; ]1\,;+\infty[$.
For $x \in D$, $\ln(x+2) + \ln(x-1) = \ln\big((x+2)(x-1)\big) = \ln(x^2 + x - 2)$.
The equation becomes:
$$x^2 + x - 2 = 4x + 8 \iff x^2 - 3x - 10 = 0.$$
The algebraic roots are $-2$ and $5$.
Now $-2 \notin D$ because $-2$ is not strictly greater than $1$ (at $-2$, $\ln(x-1) = \ln(-3)$ is undefined).
Only the root $5 \in D$ is valid. Therefore $\mathcal{S} = \{5\}$.

**Solution 48.10:**
The system is defined for $x > 0$ and $y > 0$.
The second equation gives: $\ln(xy) = \ln(2^3 \times 27) = \ln(8 \times 27) = \ln(216) \iff xy = 216$.
We seek two real numbers given their sum $S = 30$ and product $P = 216$.
They are the roots of $t^2 - 30t + 216 = 0$.
$\Delta = (-30)^2 - 4(216) = 900 - 864 = 36 = 6^2$.
$t_1 = \dfrac{30 - 6}{2} = 12$ and $t_2 = \dfrac{30 + 6}{2} = 18$.
Both roots are strictly positive, yielding two solution pairs:
$$\mathcal{S} = \{(12\,;18)\,;\, (18\,;12)\}.$$

**Solution 48.11:**
1. At $0^+$: $\lim\limits_{x \to 0^+} (x - 2) = -2$ and $\lim\limits_{x \to 0^+} \ln x = -\infty$, so $\lim\limits_{x \to 0^+} f(x) = -2 - (-\infty) = +\infty$.
   At $+\infty$: Indeterminate form $\infty - \infty$. Factor out $x$: $f(x) = x\left(1 - \dfrac{2}{x} - \dfrac{\ln x}{x}\right)$.
   Since $\lim\limits_{x \to +\infty} \dfrac{2}{x} = 0$ and by comparative growth $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$, the factor inside parentheses approaches $1$.
   By product: $\lim\limits_{x \to +\infty} f(x) = +\infty$.
2. $f'(x) = 1 - 0 - \dfrac{1}{x} = \dfrac{x-1}{x}$.
   For $x > 0$, the denominator $x$ is strictly positive, so $f'(x)$ shares the sign of $x - 1$:
   - $f'(x) < 0$ on $]0\,;1[$;
   - $f'(1) = 0$;
   - $f'(x) > 0$ on $]1\,;+\infty[$.
3. Variations: $f$ is strictly decreasing on $]0\,;1]$ and strictly increasing on $[1\,;+\infty[$.
   The minimum occurs at $x = 1$, where $f(1) = 1 - 2 - \ln 1 = -1$.
4. On $]0\,;1]$, $f$ is continuous and strictly decreasing, mapping $]0\,;1]$ onto $[-1\,;+\infty[$. Since $0 \in [-1\,;+\infty[$, the IVT corollary guarantees a unique root $\alpha_1 \in \; ]0\,;1]$.
   On $[1\,;+\infty[$, $f$ is continuous and strictly increasing, mapping $[1\,;+\infty[$ onto $[-1\,;+\infty[$. Likewise, $0 \in [-1\,;+\infty[$, guaranteeing a unique root $\alpha_2 \in [1\,;+\infty[$.
   The equation $f(x) = 0$ has exactly **two real solutions** on $]0\,;+\infty[$ ($\alpha_1 \approx 0.158$ and $\alpha_2 \approx 3.146$).

**Solution 48.12:**
Let $a > 0$. The tangent line to the graph of $\ln$ at abscissa $a$ has equation:
$$y = \ln'(a)(x - a) + \ln a \iff y = \dfrac{1}{a}(x - a) + \ln a \iff y = \dfrac{1}{a}x - 1 + \ln a.$$
This line passes through the origin $(0\,;0)$ if and only if its $y$-intercept is zero:
$$-1 + \ln a = 0 \iff \ln a = 1 \iff a = e.$$
There exists an **unique tangent line** passing through the origin. The point of tangency is $A(e\,;1)$ and the tangent equation is:
$$y = \dfrac{1}{e}x.$$

**Solution 48.13:**
1. $\lim\limits_{x \to +\infty} (x - \ln x)$: Indeterminate form $\infty - \infty$. Factor out $x$: $x - \ln x = x\left(1 - \dfrac{\ln x}{x}\right)$.
   Since $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$, the term in parentheses tends to $1$. Thus the product tends to $+\infty$.
2. $\lim\limits_{x \to +\infty} \dfrac{\ln(x^2+1)}{x}$: For $x > 0$, $\ln(x^2+1) = \ln\left[x^2\left(1 + \dfrac{1}{x^2}\right)\right] = 2\ln x + \ln\left(1 + \dfrac{1}{x^2}\right)$.
   The quotient becomes: $\dfrac{\ln(x^2+1)}{x} = 2 \dfrac{\ln x}{x} + \dfrac{\ln(1 + 1/x^2)}{x}$.
   As $x \to +\infty$, $\dfrac{\ln x}{x} \to 0$ and $\dfrac{\ln(1 + 1/x^2)}{x} \to \dfrac{0}{+\infty} = 0$. The limit is $0$.
3. $\lim\limits_{x \to 0^+} x \ln\left(1 + \dfrac{1}{x}\right)$: Substitute $u = \dfrac{1}{x} \to +\infty$.
   The expression becomes $\dfrac{\ln(1+u)}{u} = \dfrac{\ln u + \ln(1 + 1/u)}{u} = \dfrac{\ln u}{u} + \dfrac{\ln(1 + 1/u)}{u} \to 0 + 0 = 0$.
4. $\lim\limits_{x \to 1} \dfrac{\ln x}{x^2-1}$: Form $\frac{0}{0}$. Factor the denominator: $\dfrac{\ln x}{(x-1)(x+1)} = \dfrac{\ln x - \ln 1}{x - 1} \times \dfrac{1}{x+1}$.
   Since $\lim\limits_{x \to 1} \dfrac{\ln x - \ln 1}{x - 1} = \ln'(1) = 1$ and $\lim\limits_{x \to 1} \dfrac{1}{x+1} = \dfrac{1}{2}$, the product limit is $\dfrac{1}{2}$.

**Solution 48.14:**
1. With an annual interest rate of $3.5\%$, the capital multiplies each year by $1 + 0.035 = 1.035$.
   Thus $C_n = 10\,000 \times 1.035^n$.
2. Doubling occurs when $C_n \geq 20\,000 \iff 1.035^n \geq 2$.
   Applying $\ln$: $n \ln(1.035) \geq \ln 2 \iff n \geq \dfrac{\ln 2}{\ln(1.035)}$ (since $\ln(1.035) > 0$).
   $\dfrac{\ln 2}{\ln(1.035)} \approx \dfrac{0.69315}{0.03440} \approx 20.15$.
   It takes $21$ full years for the capital to double.
3. Rule of 70: For an annual rate of $t\%$, the multiplier is $1 + \dfrac{t}{100}$.
   The doubling time satisfies $n = \dfrac{\ln 2}{\ln(1 + t/100)}$.
   For small $t/100$, the first-order approximation gives $\ln(1+u) \approx u$, hence $\ln(1 + t/100) \approx \dfrac{t}{100}$.
   Moreover, $\ln 2 \approx 0.693 \approx 0.70$.
   Thus: $n \approx \dfrac{0.693}{t / 100} = \dfrac{69.3}{t} \approx \dfrac{70}{t}$.
   For $t = 3.5$, this yields $\dfrac{70}{3.5} = 20$ years, remarkably close to the exact $20.15$ years!

**Solution 48.15:**
1. As $x \to 0^+$, $\ln x \to -\infty$ and $\dfrac{1}{x} \to +\infty$, so by product $\lim\limits_{x \to 0^+} \dfrac{\ln x}{x} = -\infty$. The line $x = 0$ is a vertical asymptote.
   By comparative growth, $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$. The line $y = 0$ is a horizontal asymptote as $x \to +\infty$.
2. $f$ is differentiable on $]0\,;+\infty[$ as a quotient of differentiable functions:
   $f'(x) = \dfrac{\frac{1}{x} \times x - \ln x \times 1}{x^2} = \dfrac{1 - \ln x}{x^2}$.
   The denominator $x^2 > 0$. The sign of $f'(x)$ is that of $1 - \ln x$:
   - $1 - \ln x > 0 \iff \ln x < 1 \iff 0 < x < e$: $f$ is strictly increasing;
   - $1 - \ln x = 0 \iff x = e$;
   - $1 - \ln x < 0 \iff x > e$: $f$ is strictly decreasing.
3. The global maximum of $f$ on $]0\,;+\infty[$ is attained at $x = e$ and equals $f(e) = \dfrac{\ln e}{e} = \dfrac{1}{e}$.
4. Comparing $e^{\pi}$ and $\pi^e$:
   Since $e \approx 2.718 < \pi \approx 3.14$, and $f$ is strictly decreasing on $[e\,;+\infty[$:
   $$f(e) > f(\pi) \iff \dfrac{\ln e}{e} > \dfrac{\ln \pi}{\pi}.$$
   Multiplying by $e\pi > 0$:
   $$\pi \ln e > e \ln \pi \iff \ln(e^\pi) > \ln(\pi^e).$$
   Since the natural logarithm is strictly increasing:
   $$e^\pi > \pi^e.$$
   (Numerical check: $e^\pi \approx 23.14$ and $\pi^e \approx 22.46$).
5. Second derivative:
   $$f''(x) = \dfrac{\left(-\frac{1}{x}\right) x^2 - (1 - \ln x)(2x)}{x^4} = \dfrac{-x - 2x + 2x\ln x}{x^4} = \dfrac{2\ln x - 3}{x^3}.$$
   The sign depends solely on $2\ln x - 3$:
   - $2\ln x - 3 < 0 \iff \ln x < \dfrac{3}{2} \iff 0 < x < e^{3/2} = e\sqrt{e}$: $f''(x) < 0$, $f$ is **concave**.
   - $2\ln x - 3 > 0 \iff x > e^{3/2}$: $f''(x) > 0$, $f$ is **convex**.
   The second derivative changes sign at $x_0 = e^{3/2}$. The curve has an **inflection point** at $I\left(e^{3/2}\,; \dfrac{3}{2e^{3/2}}\right)$.

**Solution 48.16:**
1. Let $\varphi(x) = \ln x - (x - 1)$ on $]0\,;+\infty[$. Then $\varphi'(x) = \dfrac{1}{x} - 1 = \dfrac{1-x}{x}$.
   $\varphi'$ is positive on $]0\,;1[$, zero at $1$, and negative on $]1\,;+\infty[$.
   The maximum of $\varphi$ is $\varphi(1) = 0$. Thus $\varphi(x) \leq 0 \iff \ln x \leq x - 1$ for all $x > 0$.
2. Substituting $x = 1 + t$ with $1 + t > 0 \iff t > -1$ yields $\ln(1+t) \leq (1+t) - 1 = t$.
3. - Apply $\ln(1+t) \leq t$ with $t = \dfrac{1}{n} > 0$: $\ln\left(1 + \dfrac{1}{n}\right) \leq \dfrac{1}{n} \iff n \ln\left(1 + \dfrac{1}{n}\right) \leq 1$.
     Applying the increasing exponential function: $\left(1 + \dfrac{1}{n}\right)^n \leq e$.
   - Apply $\ln(1+t) \leq t$ with $t = -\dfrac{1}{n+1} > -1$:
     $$\ln\left(1 - \dfrac{1}{n+1}\right) \leq -\dfrac{1}{n+1} \iff \ln\left(\dfrac{n}{n+1}\right) \leq -\dfrac{1}{n+1} \iff -\ln\left(\dfrac{n+1}{n}\right) \leq -\dfrac{1}{n+1}.$$
     Multiplying by $-(n+1) < 0$:
     $$(n+1)\ln\left(1 + \dfrac{1}{n}\right) \geq 1.$$
     Applying the exponential function: $\left(1 + \dfrac{1}{n}\right)^{n+1} \geq e$.
   Combining both yields the celebrated bounds: $\left(1 + \dfrac{1}{n}\right)^n \leq e \leq \left(1 + \dfrac{1}{n}\right)^{n+1}$.

**Solution 48.17:**
The activity follows $A(t) = A_0 e^{-\lambda t}$, where $\lambda = \dfrac{\ln 2}{T} = \dfrac{\ln 2}{5\,730}$.
Here $\dfrac{A(t)}{A_0} = \dfrac{2.4}{15.3} \approx 0.15686$.
$e^{-\lambda t} = \dfrac{2.4}{15.3} \iff -\lambda t = \ln\left(\dfrac{2.4}{15.3}\right) \iff t = -5\,730 \times \dfrac{\ln(2.4 / 15.3)}{\ln 2}$.
Computing numerically:
$\ln\left(\dfrac{2.4}{15.3}\right) \approx -1.8524$.
$t \approx -5\,730 \times \dfrac{-1.8524}{0.69315} \approx 5\,730 \times 2.672 \approx 15\,310 \text{ years}$.
The paintings are approximately $15,300$ years old (dating from the Upper Paleolithic / Magdalenian period).

**Solution 48.18:**
1. For all $n \in \mathbb{N}$:
   $v_{n+1} = u_{n+1} - 5 = (0.6 u_n + 2) - 5 = 0.6 u_n - 3 = 0.6(u_n - 5) = 0.6 v_n$.
   Hence $(v_n)$ is a geometric sequence with common ratio $q = 0.6$ and first term $v_0 = u_0 - 5 = 10 - 5 = 5$.
2. Thus $v_n = 5 \times 0.6^n$, and $u_n = 5 + 5 \times 0.6^n$.
3. $|u_n - 5| < 10^{-4} \iff 5 \times 0.6^n < 10^{-4} \iff 0.6^n < \dfrac{10^{-4}}{5} = 2 \times 10^{-5}$.
   Taking logarithms: $n \ln(0.6) < \ln(2 \times 10^{-5})$.
   Since $0.6 < 1$, $\ln(0.6) \approx -0.5108 < 0$, which reverses the inequality:
   $$n > \dfrac{\ln(2 \times 10^{-5})}{\ln(0.6)} \approx \dfrac{-10.8198}{-0.5108} \approx 21.18.$$
   The smallest integer satisfying this condition is **$n = 22$**.

---

#### Level ★★★ Solutions

**Solution 48.19:**
1. For all $x > 0$, $\ln(1+x) \leq x$. Setting $x = \dfrac{1}{k}$ for $k \geq 1$:
   $$\ln\left(1 + \dfrac{1}{k}\right) \leq \dfrac{1}{k} \iff \ln\left(\dfrac{k+1}{k}\right) \leq \dfrac{1}{k} \iff \ln(k+1) - \ln k \leq \dfrac{1}{k}.$$
2. For all $x \in \; ]0\,;1[$, $\ln(1-x) \leq -x \iff -\ln(1-x) \geq x$.
   Setting $x = \dfrac{1}{k}$ for $k \geq 2$:
   $$\dfrac{1}{k} \leq -\ln\left(1 - \dfrac{1}{k}\right) = -\ln\left(\dfrac{k-1}{k}\right) = \ln k - \ln(k-1).$$
3. - Summing inequality 1 for $k = 1$ to $n$:
     $$\sum_{k=1}^n (\ln(k+1) - \ln k) \leq \sum_{k=1}^n \dfrac{1}{k} = H_n.$$
     The left sum telescopes: $(\ln 2 - \ln 1) + (\ln 3 - \ln 2) + \dots + (\ln(n+1) - \ln n) = \ln(n+1)$.
     Thus $\ln(n+1) \leq H_n$.
   - Summing inequality 2 for $k = 2$ to $n$:
     $$\sum_{k=2}^n \dfrac{1}{k} \leq \sum_{k=2}^n (\ln k - \ln(k-1)) = \ln n - \ln 1 = \ln n.$$
     Since $H_n = 1 + \sum_{k=2}^n \dfrac{1}{k}$, we obtain $H_n - 1 \leq \ln n \iff H_n \leq 1 + \ln n$.
   We have established the bounds: $\ln(n+1) \leq H_n \leq 1 + \ln n$.
4. Since $\lim\limits_{n \to +\infty} \ln(n+1) = +\infty$, the comparison theorem immediately implies $\lim\limits_{n \to +\infty} H_n = +\infty$.
   The harmonic series diverges, even though its individual terms $\frac{1}{n}$ tend to zero!
5. Divide the bounds by $\ln n$ (which is strictly positive for $n \geq 2$):
   $$\dfrac{\ln(n+1)}{\ln n} \leq \dfrac{H_n}{\ln n} \leq \dfrac{1}{\ln n} + 1.$$
   Since $\dfrac{\ln(n+1)}{\ln n} = 1 + \dfrac{\ln(1+1/n)}{\ln n} \to 1$ and $\dfrac{1}{\ln n} + 1 \to 1$, the Squeeze Theorem gives:
   $$\lim_{n \to +\infty} \dfrac{H_n}{\ln n} = 1.$$
   (The difference $H_n - \ln n$ converges to the celebrated **Euler-Mascheroni constant** $\gamma \approx 0.577215$).

**Solution 48.20:**
1. $\ln(n!) = \ln(1 \times 2 \times \dots \times n) = \sum\limits_{k=1}^n \ln k$.
2. For $k \geq 2$, the monotonicity of $\ln$ gives for $t \in [k-1\,; k]$: $\ln(k-1) \leq \ln t \leq \ln k$.
   Integrating (to be formalized in Chapter 50) yields $\int_1^n \ln t \, dt \leq \ln(n!) \leq \int_1^{n+1} \ln t \, dt$.
   Since an antiderivative of $\ln t$ is $t \ln t - t$, we obtain $\ln(n!) \approx n\ln n - n$, which leads to Stirling's asymptotic formula $n! \sim \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n$.

**Solution 48.21:**
1. For $x > 0$ and $a > 0$: $x^a = a^x \iff e^{a\ln x} = e^{x\ln a} \iff a\ln x = x\ln a \iff \dfrac{\ln x}{x} = \dfrac{\ln a}{a}$.
2. From Exercise 48.15, $f(x) = \dfrac{\ln x}{x}$ increases from $-\infty$ to $\dfrac{1}{e}$ on $]0\,;e]$, then decreases from $\dfrac{1}{e}$ to $0$ on $[e\,;+\infty[$.
   - If $a = e$: $f(a) = \dfrac{1}{e}$ is the absolute maximum; the equation has the unique solution $x = e$.
   - If $a > 1$ and $a \neq e$: the value $f(a) \in \left]0\,; \dfrac{1}{e}\right[$ is attained at exactly two points: one in $]1\,;e[$ and one in $]e\,;+\infty[$. One solution is $x = a$, and the other is a distinct real number.
   - If $0 < a \leq 1$: $f(a) \leq 0$. Since $f$ is strictly increasing on $]0\,;1]$ and positive on $]1\,;+\infty[$, there is only the trivial solution $x = a$.
3. We seek distinct positive integers $1 \leq x < y$ such that $x^y = y^x$.
   One integer must lie strictly below $e \approx 2.718$ and the other strictly above $e$.
   The only integer strictly between 1 and $e$ is $x = 2$.
   Testing $x = 2$: the equation is $2^y = y^2$.
   - For $y = 3$: $2^3 = 8 \neq 9$.
   - For $y = 4$: $2^4 = 16 = 4^2$. It matches!
   Since $f$ is strictly decreasing for $y > e$, no other integer solutions exist.
   The unique pair of distinct positive integers is **$(2\,;4)$**.

**Solution 48.22:**
1. Take the natural logarithm of both sides: $\ln f(x) = \ln(u_1(x) u_2(x) \dots u_n(x)) = \sum\limits_{k=1}^n \ln(u_k(x))$.
   Differentiating both sides with respect to $x$:
   $$\dfrac{f'(x)}{f(x)} = \sum_{k=1}^n \dfrac{u'_k(x)}{u_k(x)}.$$
2. For $g(x) = (x+1)^3 (2x-1)^4 (x^2+5)^2$:
   $$\dfrac{g'(x)}{g(x)} = \dfrac{3}{x+1} + \dfrac{4 \times 2}{2x-1} + \dfrac{2 \times 2x}{x^2+5} = \dfrac{3}{x+1} + \dfrac{8}{2x-1} + \dfrac{4x}{x^2+5}.$$
   Multiplying this sum by $g(x)$ gives $g'(x)$ immediately without an unwieldy generalized product rule!

---

### The Question that Opens What Follows

The logarithm and exponential functions allow us to master growth that explodes without bound and decay that fades toward zero. But in the physical universe, not everything grows or vanishes indefinitely: the seasons repeat, the heart beats, planets orbit, guitar strings vibrate, and a child's swing rocks back and forth.

How do mathematics describe phenomena that **return endlessly to their starting point**? How do we calculate the instantaneous velocity of a pendulum at the exact instant it swings through its lowest point?

Welcome to the world of oscillations, waves, and the geometry of the circle: join us in Chapter 49 with **The Swing and Oscillating Functions**.
