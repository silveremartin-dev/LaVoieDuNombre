# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 40: The Bacterial Colony

> *“In the inert world of stones, speed depends on an applied external force. In the ardent world of the living, force springs from number: each cell is its own engine. The larger the colony grows, the faster it explodes. Nature has chosen a single curve to sing the proliferation of life: the exponential function.”*

---

### What You Are About to Discover

- The biological secret of proliferation: why the growth rate of a population is proportional to its size.
- The birth of a revolutionary equation: $f' = f$ with $f(0) = 1$.
- **Euler's method**: how to trace the curve step-by-step along its own tangents, with an executable **Python** script.
- The grand curriculum proof: why $\exp(x)$ never vanishes and why this function is **unique**.
- The magical conversion of addition into multiplication: proving $\exp(x+y) = \exp(x)\exp(y)$.
- Euler's universal number: $e \approx 2.71828$, and the notation $e^x$.
- Complete study of the function: derivative, strict positivity, explosive growth, limits, and asymptotes.
- The chain rule for composite exponentials: $(e^{u(x)})' = u'(x)e^{u(x)}$.
- How to solve equations and inequalities involving $e^x$.

---

### 1. The Problem: The Petri Dish and the Biological Clock

Peer through the eyepiece of a microscope in a biology laboratory.
In a Petri dish filled with nutrient agar, a researcher deposits at noon ($t = 0$) a single bacterium of *Escherichia coli*.

This bacterium feeds. After twenty minutes, it elongates and splits into two: there are 2 bacteria.
Twenty minutes later, each divides in turn: there are 4 bacteria.
Then 8, then 16, 32, 64, 128, 256...

```
Time t (h) :  0      1      2      3       ...   10
Bacteria   :  1      8     64    512       ...   1 000 000 000
```

Observe closely what distinguishes this growth from every curve we have studied until now:

- For a car cruising on the highway at constant speed, distance increases by 100 km every hour, regardless of how far it has already traveled. The derivative is constant.
- For a stone falling freely under gravity, speed increases by $9.8\text{ m/s}$ each second: acceleration is constant, and distance follows a second-degree polynomial ($x^2$).
- But for the bacterial colony, **every newcomer is itself a future birth factory**!
  - When the colony counts 10 bacteria, there are 10 potential divisions per generation. The slope is modest.
  - When the colony counts one million individuals, there are **one million simultaneous cellular divisions**! The speed of proliferation becomes titanic.

Letting $N(t)$ denote the population size at time $t$, the instantaneous rate of growth (the derivative $N'(t)$) is not constant: it is **directly proportional to the number of individuals already present**:

$$N'(t) = k \cdot N(t).$$

By choosing the unit of time so that $k = 1$, and starting from a single individual at $t = 0$, we face the most fascinating challenge ever presented to differential calculus:

> **The Fundamental Enigma:**
> Does there exist a mathematical function $f$, defined and differentiable on $\mathbb{R}$, which is **strictly equal to its own derivative** at every moment, and equals 1 at the origin?
>
> $$\begin{cases} f'(x) = f(x) \quad \text{for all } x \in \mathbb{R} \\ f(0) = 1 \end{cases}$$

This is a function whose ski-slope beneath the boot at every point is equal to its instantaneous altitude! The higher it climbs, the steeper the slope; the steeper the slope, the faster it ascends into the sky.

---

### 2. Euler's Method: Building the Curve Step by Step

Before formally proving that such a function exists, how can we sketch its shape and compute its values?
In the 18th century, the Swiss genius **Leonhard Euler** conceived a revolutionary numerical method: stepping forward along the tangent line.

#### 2.1 The Geometric Principle

Recall from the previous chapter that near a point $x_0$, a smooth curve closely hugs its tangent line:
$$f(x_0 + h) \approx f(x_0) + h \cdot f'(x_0).$$

Here, our function has a magical property: **its derivative equals its own value** ($f'(x_0) = f(x_0)$)!
The linear approximation formula simplifies dramatically:

$$f(x_0 + h) \approx f(x_0) + h \cdot f(x_0) = (1 + h) \cdot f(x_0).$$

Each forward step of width $h$ simply means **multiplying the previous altitude by $(1 + h)$**!

```
    Altitude
        ▲                                     . - * M₂(2h ; (1+h)² f(0))
        │                               . - '   /
        │                         . - * M₁(h ; (1+h) f(0))
        │                   . - '   /
        │             . - * M₀(0 ; 1)
        │       . - '
      1 ┼──────*
        │
      0 └──────┴──────────┴──────────┴──────────► x
               0          h          2h
```

#### 2.2 Manual Calculation with Step Size $h = 0.2$
Starting from $x_0 = 0$ and $y_0 = 1$ with step size $h = 0.2$:
- At $x_1 = 0.2$: $y_1 = y_0 \times (1 + 0.2) = 1 \times 1.2 = 1.2$.
- At $x_2 = 0.4$: $y_2 = y_1 \times 1.2 = 1.2 \times 1.2 = 1.44$.
- At $x_3 = 0.6$: $y_3 = 1.44 \times 1.2 = 1.728$.
- At $x_4 = 0.8$: $y_4 = 1.728 \times 1.2 = 2.0736$.
- At $x_5 = 1.0$: $y_5 = 2.0736 \times 1.2 \approx 2.488$.

In 5 steps, we reach $x = 1$, and our approximation gives $f(1) \approx 2.488$.
If we take a step size ten times smaller ($h = 0.02$), performing 50 multiplications by $1.02$, we get $(1.02)^{50} \approx 2.691$.
With $h = 0.001$ (1000 steps), we obtain $(1.001)^{1000} \approx 2.7169$.
The curve is coming into sharp focus before our eyes!

#### 2.3 The Standard Python Algorithm

Here is the Python script to simulate Euler's method:

```python
def euler_method(n_steps):
    h = 1.0 / n_steps  # step size to travel from 0 to 1
    x = 0.0
    y = 1.0
    for _ in range(n_steps):
        y = y + h * y  # equivalent to y = y * (1 + h)
        x = x + h
    return y

# Testing with increasingly fine subdivisions:
for n in [10, 100, 1000, 10000]:
    print(f"For n = {n:5d} steps: f(1) ≈ {euler_method(n):.6f}")
```

Output:
```
For n =    10 steps: f(1) ≈ 2.593742
For n =   100 steps: f(1) ≈ 2.704814
For n =  1000 steps: f(1) ≈ 2.716924
For n = 10000 steps: f(1) ≈ 2.718146
```

The decimals steadily stabilize toward a mysterious number: **$2.71828\dots$**

---

### 3. Existence Theorem and Proof of Uniqueness

> **📐 Fundamental Theorem (Existence admitted, uniqueness proved)**
> There exists a **unique** function $f$ differentiable on $\mathbb{R}$ such that:
>
> $$\begin{cases} f'(x) = f(x) \quad \text{for all } x \in \mathbb{R} \\ f(0) = 1 \end{cases}$$
>
> This function is called the **exponential function**, denoted $\exp$.

The proof of uniqueness is a masterpiece of mathematical elegance. It hinges on a crucial lemma: the function can never vanish to zero.

#### 3.1 Lemma: The Function Never Vanishes

> **✍️ Proof — Non-vanishing of $f$**
> Let $f$ be a differentiable function on $\mathbb{R}$ satisfying $f' = f$ and $f(0) = 1$.
> Consider the auxiliary function $g$ defined on $\mathbb{R}$ by:
> $$g(x) = f(x) \times f(-x).$$
> Differentiate $g$ using the product rule $(uv)' = u'v + uv'$:
> The derivative of $f(-x)$ is $-f'(-x)$ (chain rule).
> $$g'(x) = f'(x) \cdot f(-x) + f(x) \cdot \big(-f'(-x)\big) = f'(x)f(-x) - f(x)f'(-x).$$
> But by hypothesis, $f' = f$ everywhere, so $f'(x) = f(x)$ and $f'(-x) = f(-x)$! Substituting:
> $$g'(x) = f(x)f(-x) - f(x)f(-x) = 0.$$
> The derivative of $g$ is **identically zero on $\mathbb{R}$**.
> A function whose derivative is zero everywhere is **constant**!
> Thus for all real numbers $x$:
> $$g(x) = g(0) = f(0) \times f(-0) = 1 \times 1 = 1.$$
> Hence, for all $x \in \mathbb{R}$:
> $$\boxed{f(x) \times f(-x) = 1}$$
>
> If the product of two real numbers is 1, neither of them can be zero!
> Consequently, **for all real $x$, $f(x) \neq 0$**. $\blacksquare$

#### 3.2 Proof of Uniqueness

> **✍️ Proof — Uniqueness of the Exponential Function**
> Suppose there exist two functions $f_1$ and $f_2$, both satisfying the conditions:
> $f'_1 = f_1$ with $f_1(0) = 1$, and $f'_2 = f_2$ with $f_2(0) = 1$.
> Since $f_1$ never vanishes on $\mathbb{R}$ by the lemma above, we have the complete mathematical right to define the quotient function:
> $$\phi(x) = \frac{f_2(x)}{f_1(x)}.$$
> Differentiating using the quotient rule $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
> $$\phi'(x) = \frac{f'_2(x)f_1(x) - f_2(x)f'_1(x)}{(f_1(x))^2}.$$
> Since $f'_2 = f_2$ and $f'_1 = f_1$:
> $$\phi'(x) = \frac{f_2(x)f_1(x) - f_2(x)f_1(x)}{(f_1(x))^2} = \frac{0}{(f_1(x))^2} = 0.$$
> The derivative of $\phi$ is identically zero on $\mathbb{R}$, so $\phi$ is a constant function.
> Evaluating at $x = 0$:
> $$\phi(0) = \frac{f_2(0)}{f_1(0)} = \frac{1}{1} = 1.$$
> Therefore, for all $x \in \mathbb{R}$, $\phi(x) = 1$, which means:
> $$f_2(x) = f_1(x).$$
> Thus there exists only one such function! $\blacksquare$

---

### 4. The Fundamental Property: Transforming Addition into Multiplication

This is the crowning property that makes the exponential the most powerful tool in all of mathematical science:

> **📐 Fundamental Theorem — Functional Equation**
> For all real numbers $x$ and $y$:
>
> $$\boxed{\exp(x + y) = \exp(x) \times \exp(y)}$$

> **✍️ Proof**
> Fix an arbitrary real number $y$, and consider the function of the single variable $x$:
> $$h(x) = \frac{\exp(x + y)}{\exp(x)}.$$
> (The quotient is valid because the denominator $\exp(x)$ never vanishes).
> Differentiate $h$ with respect to $x$:
> The numerator $u(x) = \exp(x + y)$ has derivative $u'(x) = 1 \cdot \exp'(x+y) = \exp(x+y)$.
> The denominator $v(x) = \exp(x)$ has derivative $v'(x) = \exp(x)$.
> Applying the quotient rule:
> $$h'(x) = \frac{\exp(x+y)\exp(x) - \exp(x+y)\exp(x)}{(\exp(x))^2} = 0.$$
> Thus $h$ is constant on $\mathbb{R}$.
> Its value for every $x$ equals its value at $x = 0$:
> $$h(0) = \frac{\exp(0 + y)}{\exp(0)} = \frac{\exp(y)}{1} = \exp(y).$$
> Therefore, for all $x \in \mathbb{R}$:
> $$\frac{\exp(x + y)}{\exp(x)} = \exp(y) \iff \exp(x + y) = \exp(x) \times \exp(y). \quad \blacksquare$$

#### 4.1 Algebraic Corollaries

From this core formula follow all the familiar laws of powers:

> **📐 Algebraic Properties** — For all real numbers $x, y$ and any integer $n$:
> 1. $\exp(-x) = \frac{1}{\exp(x)}$
> 2. $\exp(x - y) = \frac{\exp(x)}{\exp(y)}$
> 3. $\exp(n \cdot x) = \big(\exp(x)\big)^n$

> **✍️ Brief Proofs**
> 1. From the lemma: $\exp(x) \times \exp(-x) = \exp(x - x) = \exp(0) = 1 \implies \exp(-x) = \frac{1}{\exp(x)}$.
> 2. $\exp(x - y) = \exp(x + (-y)) = \exp(x) \times \exp(-y) = \exp(x) \times \frac{1}{\exp(y)} = \frac{\exp(x)}{\exp(y)}$.
> 3. By straightforward induction for $n \in \mathbb{N}$: $\exp(2x) = \exp(x+x) = (\exp(x))^2$, etc. $\blacksquare$

---

### 5. Euler's Notation and the Number $e$

Notice the stunning structural resemblance between the properties of $\exp$ and the laws of exponents:
- $a^{x+y} = a^x \times a^y$
- $a^{-x} = \frac{1}{a^x}$
- $a^{nx} = (a^x)^n$

This perfect correspondence prompted **Leonhard Euler** in 1728 to introduce an audacious notation.
Define the number $e$ as the value of the exponential function at 1:

$$e = \exp(1) \approx 2.718281828459\dots$$

Then, for every integer $n$, $\exp(n) = (\exp(1))^n = e^n$.
Euler boldly generalized this notation to all real numbers $x$:

> **📐 Euler's Notation**
> For every real number $x$, we write:
>
> $$\boxed{\exp(x) = e^x}$$
>
> We pronounce this interchangeably as “exponential of $x$” or “**e to the power x**”.
> The rules of manipulation mirror exponent laws exactly:
> $$e^0 = 1, \quad e^1 = e, \quad e^{x+y} = e^x \cdot e^y, \quad e^{-x} = \frac{1}{e^x}, \quad e^{x-y} = \frac{e^x}{e^y}, \quad (e^x)^n = e^{nx}.$$

---

### 6. Complete Study of the Exponential Function

#### 6.1 Sign and Strict Positivity
We have already proved that $e^x \neq 0$ for all $x$.
Furthermore, $e^x = e^{x/2 + x/2} = \left(e^{x/2}\right)^2$.
Any squared real number is non-negative. Because it cannot be zero, it must be **strictly positive**!

> **📐 Theorem — Strict Positivity**
> For every real number $x$:
>
> $$\boxed{e^x > 0}$$
>
> The graph of the exponential function lies **entirely above the horizontal axis**. It never touches or crosses the zero line.

#### 6.2 Monotonicity
The derivative of the exponential function is itself:
$$(e^x)' = e^x.$$
Since $e^x > 0$ for all $x \in \mathbb{R}$, **the derivative is strictly positive everywhere**.

> **📐 Theorem — Strict Growth**
> The exponential function is **strictly increasing** on all of $\mathbb{R}$.
> Consequently:
> - $e^a = e^b \iff a = b$
> - $e^a < e^b \iff a < b$

#### 6.3 Limits at Infinity and Asymptotes
- As $x \to +\infty$: $e^x$ explodes toward infinity with blistering speed:
  $$\lim_{x \to +\infty} e^x = +\infty.$$
- As $x \to -\infty$: set $X = -x$. As $x \to -\infty$, $X \to +\infty$.
  $$e^x = e^{-X} = \frac{1}{e^X} \xrightarrow[X \to +\infty]{} 0^+.$$
  $$\lim_{x \to -\infty} e^x = 0.$$

> **📐 Geometric Property — Horizontal Asymptote**
> The line $y = 0$ (the $x$-axis) is a **horizontal asymptote** to the graph of the exponential function at $-\infty$.

#### 6.4 Variation Table and Graph

| $x$ | $-\infty$ | | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $(e^x)' = e^x$ | | $+$ | $1$ | $+$ | $e$ | $+$ | |
| $e^x$ | $0$ | $\nearrow$ | $1$ | $\nearrow$ | $e \approx 2.718$ | $\nearrow$ | $+\infty$ |

Tangent line at $0$ ($a = 0$):
$y = e^0(x - 0) + e^0 \iff \boxed{y = x + 1}$.

```
      y
      ▲                                         /  e^x
   4  │                                       /
   3  │                                     .'  (1 ; e ≈ 2.72)
      │                                   .*
   2  │                             . - * │
   1  │                      . - *'       │
      │                . - *'│            │
   0  ┴─────────*──────┴─────┴────────────┴─────► x
     -3        -2     -1     0            1
   (Asymptote y = 0 at -∞)
```

The curve lies entirely above its tangent line at 0:
$$\text{For all } x \in \mathbb{R}, \quad \boxed{e^x \ge x + 1}$$

---

### 7. Derivative of the Composite Function $e^{u(x)}$

In physical applications (radioactivity, epidemics, RC circuits), the exponent is rarely a bare $x$, but a function of time: $e^{-3t}$, $e^{-x^2/2}$, and so on.

> **📐 Theorem — Derivative of $e^u$**
> If $u$ is a differentiable function on an interval $I$, then $f(x) = e^{u(x)}$ is differentiable on $I$, and:
>
> $$\boxed{\big(e^{u(x)}\big)' = u'(x) \cdot e^{u(x)}}$$

> **⚠️ Caution: Classic Trap! — Never Forget $u'(x)$**
> The derivative of $e^{5x}$ is not $e^{5x}$!
> Here $u(x) = 5x \implies u'(x) = 5$.
> Thus $(e^{5x})' = 5e^{5x}$.
> Similarly: $(e^{-x})' = -e^{-x}$, and $(e^{x^2})' = 2x e^{x^2}$.

---

### Step-by-Step Worked Examples

> **✅ Worked Example 1 — Simplifying Exponential Expressions**
> Simplify the following expressions completely:
> 1. $A = \frac{e^3 \times e^{-5}}{(e^2)^3}$
> 2. $B = \frac{e^{2x+1} \times e^{-x+3}}{e^{x-2}}$
> 3. $C = (e^x + e^{-x})^2 - (e^x - e^{-x})^2$
>
> **Detailed Solution:**
> 1. $A = \frac{e^{3 + (-5)}}{e^{2 \times 3}} = \frac{e^{-2}}{e^6} = e^{-2 - 6} = e^{-8} = \frac{1}{e^8}$.
> 2. $B = \frac{e^{(2x+1) + (-x+3)}}{e^{x-2}} = \frac{e^{x+4}}{e^{x-2}} = e^{(x+4) - (x-2)} = e^{x + 4 - x + 2} = e^6$.
> 3. Difference of squares identity $(u+v)^2 - (u-v)^2 = 4uv$:
>    $C = 4 \times e^x \times e^{-x} = 4 \times e^{x - x} = 4 \times e^0 = 4 \times 1 = 4$.

> **✅ Worked Example 2 — Solving Exponential Equations**
> Solve in $\mathbb{R}$:
> 1. $e^{3x - 1} = e^{x + 5}$
> 2. $e^{x^2 - 4} = 1$
> 3. $e^{2x} - 3e^x + 2 = 0$
>
> **Detailed Solution:**
> 1. By strict monotonicity: $e^a = e^b \iff a = b$.
>    $$3x - 1 = x + 5 \iff 2x = 6 \iff x = 3. \quad S = \{3\}.$$
> 2. Recall that $1 = e^0$:
>    $$e^{x^2 - 4} = e^0 \iff x^2 - 4 = 0 \iff (x - 2)(x + 2) = 0. \quad S = \{-2; 2\}.$$
> 3. Recognize that $e^{2x} = (e^x)^2$. Substitute $X = e^x$ (with $X > 0$).
>    The equation becomes:
>    $$X^2 - 3X + 2 = 0.$$
>    Roots are $X_1 = 1$ and $X_2 = 2$.
>    Returning to $x$:
>    - $e^x = 1 \iff x = 0$.
>    - $e^x = 2 \iff x = \ln(2)$ (the unique real number $\approx 0.693$).
>    $$S = \{0; \ln 2\}.$$

> **✅ Worked Example 3 — Solving Inequalities**
> Solve in $\mathbb{R}$:
> 1. $e^{4x - 7} \le 1$
> 2. $\frac{e^x - 3}{e^x + 2} > 0$
>
> **Detailed Solution:**
> 1. $e^{4x - 7} \le e^0 \iff 4x - 7 \le 0 \iff 4x \le 7 \iff x \le \frac{7}{4}$.
>    $$S = \left]-\infty; \frac{7}{4}\right].$$
> 2. For all real $x$, $e^x > 0$, so the denominator $e^x + 2 > 2 > 0$ is strictly positive!
>    The sign of the quotient is therefore determined entirely by the numerator:
>    $$e^x - 3 > 0 \iff e^x > 3 \iff x > \ln 3. \quad S = ]\ln 3; +\infty[.$$

> **✅ Worked Example 4 — Differentiating Composite Functions**
> Differentiate the following functions:
> 1. $f(x) = (2x - 3)e^{-x}$
> 2. $g(x) = e^{-x^2 + 4x}$
> 3. $h(x) = \frac{e^x}{x+1}$ for $x \neq -1$
>
> **Detailed Solution:**
> 1. Product form $u \cdot v$ with $u(x) = 2x - 3 \implies u'(x) = 2$, and $v(x) = e^{-x} \implies v'(x) = -e^{-x}$.
>    $$f'(x) = u'v + uv' = 2e^{-x} + (2x - 3)(-e^{-x}) = [2 - (2x - 3)]e^{-x} = (5 - 2x)e^{-x}.$$
> 2. Form $e^u$ with $u(x) = -x^2 + 4x \implies u'(x) = -2x + 4$.
>    $$g'(x) = u'(x)e^{u(x)} = (-2x + 4)e^{-x^2 + 4x}.$$
> 3. Quotient form $\frac{u}{v}$:
>    $$h'(x) = \frac{(e^x)'(x+1) - e^x(x+1)'}{(x+1)^2} = \frac{e^x(x+1) - e^x(1)}{(x+1)^2} = \frac{e^x(x + 1 - 1)}{(x+1)^2} = \frac{x e^x}{(x+1)^2}.$$

> **✅ Worked Example 5 — Complete Curve Study**
> Let $f(x) = (x - 1)e^x$ defined on $\mathbb{R}$.
> Construct its complete variation table and find the equation of its tangent line at 0.
>
> **Detailed Solution:**
> 1. Derivative: Product rule with $u(x) = x - 1 \implies u'(x) = 1$ and $v(x) = e^x \implies v'(x) = e^x$.
>    $$f'(x) = 1 \cdot e^x + (x - 1)e^x = (1 + x - 1)e^x = x e^x.$$
> 2. Sign of $f'(x)$:
>    Since $e^x > 0$ for all real $x$, the sign of $f'(x)$ is **identical to the sign of $x$**!
>    - $f'(x) < 0$ for $x < 0$;
>    - $f'(0) = 0$;
>    - $f'(x) > 0$ for $x > 0$.
> 3. Variations:
>    $f$ is strictly decreasing on $]-\infty; 0]$ and strictly increasing on $[0; +\infty[$.
>    It achieves an absolute minimum at $x = 0$, equal to $f(0) = (0 - 1)e^0 = -1$.
> 4. Tangent at 0:
>    $f(0) = -1$ and $f'(0) = 0 \cdot e^0 = 0$.
>    The tangent is horizontal with equation: $\boxed{y = -1}$.

> **✅ Worked Example 6 — Concrete Modeling: Capacitor Discharge**
> In an electrical circuit, the voltage across a discharging capacitor through a resistor is modeled by $U(t) = 12 e^{-0.5 t}$, where $t$ is time in seconds and $U$ is in volts.
> 1. What is the initial voltage at $t = 0$?
> 2. After how much time does the voltage drop to half its initial value?
> 3. Compute the initial rate of voltage drop at $t = 0$.
>
> **Detailed Solution:**
> 1. $U(0) = 12 e^0 = 12 \times 1 = 12$ V.
> 2. We seek $t$ such that $U(t) = 6$ V:
>    $$12 e^{-0.5 t} = 6 \iff e^{-0.5 t} = 0.5 = \frac{1}{2} \iff e^{0.5 t} = 2.$$
>    Since $0.5 t = \ln 2 \approx 0.693$, this gives $t \approx 2 \times 0.693 \approx 1.39$ seconds.
> 3. Rate of discharge: this is the derivative $U'(t)$.
>    $$U'(t) = 12 \times (-0.5) e^{-0.5 t} = -6 e^{-0.5 t}.$$
>    At $t = 0$, $U'(0) = -6 e^0 = -6\text{ V/s}$.
>    The voltage initially drops at a rate of 6 volts per second.

---

### What You Must Remember

1. **Definition of the Exponential:**
   - Unique function satisfying $f' = f$ and $f(0) = 1$.
   - Denoted $\exp(x)$ or $e^x$, with $e = \exp(1) \approx 2.71828$.

2. **Fundamental Property (Morphism: Addition $\to$ Multiplication):**
   - $e^{a+b} = e^a \cdot e^b$
   - $e^{-a} = \frac{1}{e^a}$
   - $e^{a-b} = \frac{e^a}{e^b}$
   - $(e^a)^n = e^{na}$

3. **Analytical Properties:**
   - Strictly positive: $e^x > 0$ on $\mathbb{R}$.
   - Strictly increasing on $\mathbb{R}$: $e^a < e^b \iff a < b$.
   - Limits: $\lim_{x \to -\infty} e^x = 0$ ($y = 0$ is a horizontal asymptote) and $\lim_{x \to +\infty} e^x = +\infty$.
   - Standard derivative: $(e^x)' = e^x$.
   - Composite derivative: $\big(e^{u(x)}\big)' = u'(x) e^{u(x)}$.
   - Tangent line at 0: $y = x + 1$, with $e^x \ge x + 1$ for all real $x$.

---

### Exercises

#### Level ★ (Expressions and Elementary Equations)

1. Write as a single power of $e$: $A = e^4 \times e^{-7}$, $B = \frac{e^8}{e^3}$, $C = (e^{-2})^5$.
2. Differentiate the function $f(x) = 3e^x - 4x + 1$.
3. Differentiate $g(x) = e^{4x - 1}$.
4. Differentiate $h(x) = e^{-3x}$.
5. Solve in $\mathbb{R}$ the equation $e^{2x - 3} = e^5$.
6. Solve in $\mathbb{R}$ the inequality $e^{3x+1} > e^{x-5}$.
7. Determine the equation of the tangent line to the curve of $f(x) = e^x$ at $a = 1$.
8. Compute $f'(x)$ for $f(x) = x^2 e^x$.

#### Level ★★ (Function Studies and Variations)

9. Solve in $\mathbb{R}$ the equation $e^{2x} - 4e^x + 3 = 0$ via a substitution.
10. Construct the complete variation table of $f(x) = (2x - 1)e^x$ on $\mathbb{R}$.
11. Consider the Gaussian bell curve function $f(x) = e^{-x^2}$.
    a) Compute $f'(x)$.
    b) Construct the variation table of $f$ and find its absolute maximum.
12. Solve the inequality $e^{2x} - e^x \le 0$.
13. Consider the function $f(x) = \frac{e^x - 1}{e^x + 1}$.
    a) Prove that $f$ is odd ($f(-x) = -f(x)$).
    b) Compute $f'(x)$ and prove that $f$ is strictly increasing on $\mathbb{R}$.
14. Consider the function $g(x) = e^{2x} - 2x$.
    a) Study the variations of $g$ on $\mathbb{R}$.
    b) Deduce that for all real $x$, $e^{2x} \ge 2x + 1 > 2x$.
15. Determine the coordinates of points on the curve of $f(x) = e^{x^2 - 3x}$ with a horizontal tangent.
16. A hot bowl of soup is set on a counter in a room at 20°C. Its temperature in degrees Celsius after $t$ minutes is modeled by $T(t) = 20 + 60e^{-0.05 t}$.
    a) What is the temperature of the soup when served ($t = 0$)?
    b) What will its temperature be after 20 minutes? (Given: $e^{-1} \approx 0.368$)
    c) What temperature does the soup approach as $t \to +\infty$?

#### Level ★★★ (Problems and Advanced Challenges)

17. **Proof of the Inequality $e^x \ge x + 1$:**
    Consider $\varphi(x) = e^x - x - 1$ defined on $\mathbb{R}$.
    a) Study the variations of $\varphi$ and construct its variation table.
    b) Deduce its minimum and conclude that the exponential curve lies entirely above its tangent line at 0.
18. **Curve Intersection and Orthogonality:**
    Consider $f(x) = e^x$ and $g(x) = e^{-x}$.
    a) Find the coordinates of their point of intersection.
    b) Show that their tangent lines at this point are perpendicular!
19. **The Catenary (Hyperbolic Cosine):**
    A power cable hanging between two utility poles assumes the shape of a curve called a catenary, with equation $f(x) = \frac{e^x + e^{-x}}{2}$.
    a) Show that $f$ is an even function.
    b) Compute $f'(x)$ and determine the monotonicity of $f$.
    c) Prove that for all real $x$, $(f(x))^2 - (f'(x))^2 = 1$.
20. **Euler Algorithm and Comparison:**
    Write a Python program that compares the approximation at $x = 1$ obtained by Euler's method with 100 steps to the exact value given by `math.exp(1)`. Compute the relative error as a percentage.
21. **Family of Functions and Invariant Slope:**
    For any real $k > 0$, define $f_k(x) = k e^{kx}$.
    Show that all curves $\mathcal{C}_k$ pass through an identifiable point under translation, and determine the coordinates of the point where the tangent to $\mathcal{C}_k$ has slope $k^2$.

---

### Solutions

**1.** $A = e^{4 - 7} = e^{-3} = \frac{1}{e^3}$. $B = e^{8 - 3} = e^5$. $C = e^{-2 \times 5} = e^{-10}$.

**2.** $f'(x) = 3e^x - 4$.

**3.** Form $e^u$ with $u = 4x-1 \implies u'=4$. $g'(x) = 4e^{4x-1}$.

**4.** Form $e^u$ with $u = -3x \implies u'=-3$. $h'(x) = -3e^{-3x}$.

**5.** $e^{2x-3} = e^5 \iff 2x - 3 = 5 \iff 2x = 8 \iff x = 4$. $S = \{4\}$.

**6.** $e^{3x+1} > e^{x-5} \iff 3x + 1 > x - 5 \iff 2x > -6 \iff x > -3$. $S = ]-3; +\infty[$.

**7.** At $a = 1$: $f(1) = e^1 = e$, $f'(1) = e$.
Tangent line: $y = f'(1)(x - 1) + f(1) = e(x - 1) + e = ex - e + e = ex$.
The tangent line at 1 passes directly through the origin: $y = ex$.

**8.** Product rule: $u = x^2 \implies u'=2x$; $v = e^x \implies v'=e^x$.
$f'(x) = 2x e^x + x^2 e^x = (x^2 + 2x)e^x = x(x+2)e^x$.

**9.** Substituting $X = e^x > 0$, the equation becomes $X^2 - 4X + 3 = 0$.
$\Delta = 16 - 12 = 4 = 2^2$.
$X_1 = \frac{4 - 2}{2} = 1$ and $X_2 = \frac{4 + 2}{2} = 3$.
- $e^x = 1 \iff x = 0$.
- $e^x = 3 \iff x = \ln 3 \approx 1.0986$.
$S = \{0; \ln 3\}$.

**10.** $f'(x) = 2e^x + (2x - 1)e^x = (2 + 2x - 1)e^x = (2x + 1)e^x$.
Since $e^x > 0$, the sign of $f'(x)$ matches $2x + 1$:
- $f'(x) < 0$ on $]-\infty; -0.5[$ ($f$ decreasing);
- $f'(-0.5) = 0$;
- $f'(x) > 0$ on $]-0.5; +\infty[$ ($f$ increasing).
Absolute minimum at $x = -0.5$: $f(-0.5) = (2(-0.5) - 1)e^{-0.5} = -2e^{-0.5} = -\frac{2}{\sqrt{e}} \approx -1.213$.

**11.**
a) $u(x) = -x^2 \implies u'(x) = -2x$. Thus $f'(x) = -2x e^{-x^2}$.
b) Since $e^{-x^2} > 0$, the sign of $f'(x)$ is opposite to the sign of $x$:
For $x < 0$, $f'(x) > 0$ (increasing); for $x > 0$, $f'(x) < 0$ (decreasing).
$f$ achieves an absolute maximum at $x = 0$, equal to $f(0) = e^0 = 1$.

**12.** Factor out $e^x$: $e^{2x} - e^x = e^x(e^x - 1) \le 0$.
Since $e^x > 0$ always, this is equivalent to $e^x - 1 \le 0 \iff e^x \le 1 = e^0 \iff x \le 0$.
$S = ]-\infty; 0]$.

**13.**
a) $f(-x) = \frac{e^{-x} - 1}{e^{-x} + 1} = \frac{\frac{1}{e^x} - 1}{\frac{1}{e^x} + 1} = \frac{\frac{1 - e^x}{e^x}}{\frac{1 + e^x}{e^x}} = \frac{-(e^x - 1)}{e^x + 1} = -f(x)$. The function is odd.
b) Quotient rule:
$f'(x) = \frac{e^x(e^x+1) - (e^x-1)e^x}{(e^x+1)^2} = \frac{e^{2x} + e^x - e^{2x} + e^x}{(e^x+1)^2} = \frac{2e^x}{(e^x+1)^2}$.
The numerator is strictly positive ($2e^x > 0$) and the denominator is a non-zero square ($> 0$).
Thus $f'(x) > 0$ on $\mathbb{R}$: $f$ is strictly increasing.

**14.**
a) $g'(x) = 2e^{2x} - 2 = 2(e^{2x} - 1)$.
$g'(x) > 0 \iff e^{2x} > 1 \iff 2x > 0 \iff x > 0$.
$g$ decreases on $]-\infty; 0]$ and increases on $[0; +\infty[$.
Absolute minimum at $0$: $g(0) = e^0 - 0 = 1$.
b) Because the minimum is 1, for all $x \in \mathbb{R}$: $g(x) \ge 1 \iff e^{2x} - 2x \ge 1 \iff e^{2x} \ge 2x + 1$.
Since $2x + 1 > 2x$, it follows immediately that $e^{2x} > 2x$.

**15.** $f'(x) = (2x - 3)e^{x^2 - 3x}$.
Horizontal tangent $\iff f'(x) = 0 \iff 2x - 3 = 0 \iff x = \frac{3}{2} = 1.5$.

**16.**
a) $T(0) = 20 + 60e^0 = 20 + 60 = 80^\circ$C.
b) $T(20) = 20 + 60e^{-0.05 \times 20} = 20 + 60e^{-1} \approx 20 + 60 \times 0.368 = 20 + 22.08 = 42.08^\circ$C.
c) As $t \to +\infty$, $-0.05t \to -\infty$, so $e^{-0.05t} \to 0$.
$\lim_{t \to +\infty} T(t) = 20 + 0 = 20^\circ$C (room temperature).

**17.**
a) $\varphi'(x) = e^x - 1$.
- $\varphi'(x) < 0$ for $x < 0$ ($\varphi$ decreasing);
- $\varphi'(0) = 0$;
- $\varphi'(x) > 0$ for $x > 0$ ($\varphi$ increasing).
b) $\varphi$ attains its absolute minimum at $x = 0$, equal to $\varphi(0) = e^0 - 0 - 1 = 1 - 1 = 0$.
Consequently, for all $x \in \mathbb{R}$, $\varphi(x) \ge 0 \iff e^x - x - 1 \ge 0 \iff e^x \ge x + 1$.
The exponential curve therefore lies above its tangent line at 0 for all $x$.

**18.**
a) $e^x = e^{-x} \iff e^x = \frac{1}{e^x} \iff (e^x)^2 = 1 \iff e^{2x} = 1 \iff 2x = 0 \iff x = 0$.
$y$-coordinate: $y = e^0 = 1$. The intersection point is $A(0; 1)$.
b) Tangent to $f$ at 0: slope $f'(0) = e^0 = 1$.
Tangent to $g$ at 0: $g'(x) = -e^{-x} \implies g'(0) = -e^0 = -1$.
The product of slopes is $m_1 \times m_2 = 1 \times (-1) = -1$.
By the perpendicularity criterion, the two tangent lines are strictly perpendicular!

**19.**
a) $f(-x) = \frac{e^{-x} + e^{-(-x)}}{2} = \frac{e^{-x} + e^x}{2} = f(x)$. The function is even.
b) $f'(x) = \frac{e^x - e^{-x}}{2}$.
$f'(x) > 0 \iff e^x - e^{-x} > 0 \iff e^x > e^{-x} \iff x > -x \iff 2x > 0 \iff x > 0$.
The function decreases on $]-\infty; 0]$ and increases on $[0; +\infty[$. Minimum at $0$ equal to $f(0) = 1$.
c) $(f(x))^2 - (f'(x))^2 = \left(\frac{e^x + e^{-x}}{2}\right)^2 - \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \frac{4}{4} = 1$.
(This is the hyperbolic counterpart of the Pythagorean trigonometric identity $\cos^2 x + \sin^2 x = 1$!).

**20.**
```python
import math

def euler_comparison(n=100):
    h = 1.0 / n
    y = 1.0
    for _ in range(n):
        y = y * (1 + h)
    exact = math.exp(1)
    error = abs(y - exact) / exact * 100
    print(f"Euler (n={n}): {y:.6f}")
    print(f"Exact: {exact:.6f}")
    print(f"Relative error: {error:.3f}%")

euler_comparison(100)
# Yields a relative error of only ~0.49%!
```

**21.** At $x = 0$, $f_k(0) = k e^0 = k$.
Derivative: $f'_k(x) = k \cdot (k e^{kx}) = k^2 e^{kx}$.
The slope equals $k^2$ if and only if $k^2 e^{kx} = k^2 \iff e^{kx} = 1 \iff kx = 0 \iff x = 0$ (since $k > 0$).
For all functions in this family, the tangent line has slope $k^2$ precisely at $x = 0$.

---

### The Question That Opens What Follows

The exponential function allowed us to model populations multiplying under pure and idealized mathematical laws.
Yet when a biologist counts bacteria under a microscope, or when an opinion pollster interviews a sample of one thousand citizens on the street, physical measurements never lie on an immaculate, deterministic curve: they scatter, deviate, and fluctuate randomly.
How do we summarize a scattered cloud of noisy data with two master numbers: the center of gravity (**the mean**) and the dispersion spread (**the standard deviation**)? That is what we are about to discover in the next chapter with **the pollster and standard deviation**.
