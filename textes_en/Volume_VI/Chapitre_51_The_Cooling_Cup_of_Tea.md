# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 51: The Cooling Cup of Tea

> *“Nature does not hand us trajectories pre-drawn; she gives us only local laws connecting the present state to the rate of its change. Everything else is a differential equation.”*
> — Henri Poincaré

---

### What You Are About to Discover

- Why most fundamental laws in physics, biology, and economics do not directly specify the formula for what happens, but rather **the relationship between a quantity and its instantaneous rate of change**.
- Newton's phenomenological **Law of Cooling** (1701): why your hot coffee cools very rapidly at first, then progressively more slowly.
- The homogeneous linear differential equation **$y' = ay$**: its rigorous proof and general solutions $y(t) = C e^{at}$.
- The non-homogeneous linear differential equation with constant forcing **$y' = ay + b$**: decomposing into *general solution of the homogeneous equation + constant particular solution*: $y(t) = C e^{at} - \dfrac{b}{a}$.
- The Cauchy initial value problem and how the **initial condition** $y(t_0) = y_0$ guarantees uniqueness of the trajectory.
- Foundational real-world models: radioactive decay, electronic RC circuits, terminal velocity of a skydiver, and population dynamics.
- Step-by-step **Euler's method**: how computers numerically simulate any differential equation with a clean **Python** script.

---

### 1. The Problem: The Steaming Cup of Tea on the Table

#### 1.1 Isaac Newton's Observation (1701)

Imagine a freshly poured cup of tea, scalding at $90^\circ\text{C}$, resting on a table in a kitchen where the ambient air temperature is $20^\circ\text{C}$.
After one minute, the temperature drops by $10^\circ\text{C}$: it reads $80^\circ\text{C}$.
After two minutes, will it read $70^\circ\text{C}$? After nine minutes, will it reach $0^\circ\text{C}$? And after a quarter of an hour, will the tea freeze solid into an ice cube?

Certainly not! Daily experience teaches us that:
- When tea is piping hot, steam billows off and it cools down rapidly;
- When tea is lukewarm (say $25^\circ\text{C}$), it loses only a tiny fraction of a degree per minute;
- It will never drop below the ambient temperature of the room: its temperature asymptotically approaches the surrounding $20^\circ\text{C}$ without ever falling below it.

In **1701**, **Isaac Newton** published an anonymous paper in the *Philosophical Transactions of the Royal Society* entitled *Scala graduum caloris* (“Scale of the Degrees of Heat”). In it, he formulated a universal empirical principle:

> **Newton's Law of Cooling —**
> The rate at which a hot body loses heat to its surroundings is **proportional to the temperature difference** between the body and the ambient environment.

```
       Temperature T(t)
            ▲
      90°C  ┼ *
            │   \   Steep slope: rapid initial cooling
            │     \
      50°C  ┼       '--.
            │           '--.   Gentle slope: slow cooling
      20°C  ┼ - - - - - - - - - - - - - - - - -  Ambient temperature Text
            │                                  (Horizontal asymptote)
         0  └──────────────────────────────────────► Time t
```

#### 1.2 Translation into a Mathematical Equation

Let $T(t)$ represent the temperature of the tea at time $t$.
The “rate at which temperature changes” at each instant is precisely the instantaneous rate of change—that is, **the derivative $T'(t)$**.
The difference between the tea's temperature and the surrounding ambient temperature $T_{\text{ext}}$ is $T(t) - T_{\text{ext}}$.
Newton's law can therefore be stated in a single line:
$$T'(t) = -k \big(T(t) - T_{\text{ext}}\big)$$
where $k > 0$ is a positive physical constant that depends on the geometry of the cup, its material (porcelain, glass, metal), and airflow in the room. The negative sign reflects cooling ($T'(t) < 0$ whenever $T(t) > T_{\text{ext}}$).

Expanding this expression gives:
$$T'(t) = -k T(t) + k T_{\text{ext}}.$$

This is a **differential equation**: the unknown is not an isolated number $x$, but an **entire function $t \mapsto T(t)$**, and the equation links this unknown function directly to its own derivative!

---

### 2. The Homogeneous Differential Equation: $y' = ay$

#### 2.1 Definition and Intuition

> **📐 Definition —**
> Let $a$ be a fixed real number. The differential equation:
> $$(E_0) : \quad y' = ay$$
> is called a **first-order homogeneous linear differential equation with constant coefficients**.
> A solution of $(E_0)$ on an interval $I$ is any function $f$ differentiable on $I$ such that for all $t \in I$:
> $$f'(t) = a f(t).$$

**What this means:** We seek a function whose derivative is directly proportional to itself.
Do you know a function that is its own derivative? Yes! The exponential function: $(e^t)' = e^t$.
And if we consider $y(t) = e^{at}$, the chain rule gives $(e^{at})' = a e^{at} = a y(t)$!
Furthermore, multiplying by any arbitrary real constant $C$, the linearity of differentiation confirms that $(C e^{at})' = C (a e^{at}) = a (C e^{at})$.
All functions of the form $t \mapsto C e^{at}$ are therefore solutions. Are there any others? The answer is no.

#### 2.2 Fundamental Theorem and Rigorous Proof

> **📐 Theorem (Required Curriculum Proof) —**
> Let $a \in \mathbb{R}$.
> The solutions on $\mathbb{R}$ to the differential equation $y' = ay$ are precisely the functions of the form:
> $$y(t) = C e^{at}$$
> where $C$ is an arbitrary real constant.

> **✍️ Rigorous Proof —**
> The proof proceeds in two stages: verification (existence) and uniqueness.
> 1. **Verification:** Let $C \in \mathbb{R}$ and define $f(t) = C e^{at}$.
>    The function $f$ is differentiable on $\mathbb{R}$, and for all $t \in \mathbb{R}$:
>    $$f'(t) = C \times (a e^{at}) = a (C e^{at}) = a f(t).$$
>    Thus, every function of the form $C e^{at}$ is indeed a solution to $(E_0)$.
>
> 2. **Uniqueness:** Let $g$ be an arbitrary solution to $y' = ay$ on $\mathbb{R}$.
>    By definition, for all $t \in \mathbb{R}$, $g'(t) = a g(t)$.
>    Define the auxiliary function $\varphi$ on $\mathbb{R}$ by:
>    $$\varphi(t) = g(t) e^{-at}.$$
>    The function $\varphi$ is differentiable on $\mathbb{R}$ as a product of differentiable functions. Using the product rule $(uv)' = u'v + uv'$:
>    $$\varphi'(t) = g'(t) e^{-at} + g(t) (-a e^{-at}) = \big(g'(t) - a g(t)\big) e^{-at}.$$
>    Since $g$ satisfies $y' = ay$, we know that $g'(t) - a g(t) = 0$ for all $t \in \mathbb{R}$!
>    Consequently:
>    $$\varphi'(t) = 0 \times e^{-at} = 0.$$
>    The derivative of $\varphi$ is **identically zero across the entire real line $\mathbb{R}$**.
>    Therefore, $\varphi$ is a **constant function** on $\mathbb{R}$: there exists a real constant $C$ such that for all $t \in \mathbb{R}$:
>    $$\varphi(t) = C \iff g(t) e^{-at} = C.$$
>    Multiplying both sides by $e^{at}$ (which is nowhere zero):
>    $$g(t) = C e^{at}.$$
>    Every solution must be of the form $C e^{at}$. $\blacksquare$

#### 2.3 Uniqueness Under Initial Conditions: The Cauchy Problem

The equation $y' = ay$ admits an infinite family of solutions (one for each real value of $C$). Graphically, this corresponds to an entire family of non-intersecting trajectories:

```
       y ▲                     C = 2
         │                    /
         │      C = 1       /
         │        /       /
       1 ┼ - - - * - - - /
         │     /       /
       0 ┼───/───────/────────► t
         │  /
      -1 ┼ * C = -1
         │  \
```

To determine $C$ and fix the unique physical trajectory followed by the system, one must specify an **initial condition** at some reference time $t_0$.

> **📐 Existence and Uniqueness Theorem (Cauchy Initial Value Problem) —**
> For any real numbers $t_0$ and $y_0$, the differential equation $y' = ay$ has **a unique solution** $f$ satisfying the initial condition:
> $$f(t_0) = y_0.$$
> This solution is given for all $t \in \mathbb{R}$ by:
> $$f(t) = y_0 \, e^{a(t - t_0)}.$$

> **✍️ Proof —**
> The general solutions have the form $f(t) = C e^{at}$.
> The initial condition requires:
> $$f(t_0) = y_0 \iff C e^{a t_0} = y_0 \iff C = y_0 e^{-a t_0}.$$
> Substituting $C$ back into the function:
> $$f(t) = (y_0 e^{-a t_0}) e^{at} = y_0 \, e^{a(t - t_0)}.$$
> Because $C$ is uniquely determined, the solution is unique. $\blacksquare$

> **Worked Example 1 — Radioactive Decay.**
> A sample of Iodine-131 initially contains $N_0 = 10^8$ radioactive nuclei at $t = 0$.
> The number of remaining undecayed nuclei $N(t)$ satisfies the differential equation $N'(t) = -0.0866 N(t)$ (with time $t$ measured in days).
> 1. Determine the explicit formula for $N(t)$.
> 2. Calculate the number of nuclei remaining after 8 days.
>
> *Solution:*
> 1. This is the equation $y' = ay$ with $a = -0.0866$.
>    The general solutions are $N(t) = C e^{-0.0866 t}$.
>    Applying the initial condition: $N(0) = C e^0 = C = 10^8$.
>    Thus, $N(t) = 10^8 e^{-0.0866 t}$.
> 2. At $t = 8$ days:
>    $N(8) = 10^8 e^{-0.0866 \times 8} = 10^8 e^{-0.6928} \approx 10^8 \times 0.50017 \approx 5 \times 10^7 \text{ nuclei}$.
>    (Approximately half of the sample has decayed: the half-life of Iodine-131 is roughly 8 days!).

---

### 3. The Non-Homogeneous Differential Equation: $y' = ay + b$

In many real-world systems, quantities do not decay to zero: our hot tea does not drop to absolute zero ($0\text{ K}$), but levels off at room temperature ($20^\circ\text{C}$); a capacitor in a charging circuit does not charge without bound, but approaches the source voltage $E$.
The differential equation includes a constant forcing term:
$$(E) : \quad y' = ay + b \quad (a \neq 0).$$

#### 3.1 Finding a Constant Particular Solution

Let us determine whether there exists a constant solution $y(t) = k$ (where $k \in \mathbb{R}$) to this equation.
If $y$ is constant, its derivative is identically zero: $y'(t) = 0$.
Substituting into $(E)$:
$$0 = ak + b \iff ak = -b \iff k = -\dfrac{b}{a}.$$

> **The constant particular solution of $y' = ay + b$ is:**
> $$y_p(t) = -\dfrac{b}{a}.$$
> In physical modeling, this value represents the **steady-state equilibrium** of the system.

#### 3.2 Solution Structure Theorem

> **📐 Theorem (General Solution of $y' = ay + b$) —**
> Let $a \neq 0$ and $b$ be real numbers.
> The solutions on $\mathbb{R}$ to the differential equation $y' = ay + b$ are precisely the functions:
> $$y(t) = C e^{at} - \dfrac{b}{a}$$
> where $C$ is an arbitrary real constant.

> **✍️ Proof (Required Curriculum Proof) —**
> Let $(E) : y' = ay + b$ and let $(E_0) : y' = ay$ be its associated homogeneous equation.
> Define $y_p(t) = -\dfrac{b}{a}$. We have $y'_p = 0 = a y_p + b$, so $y_p$ is a particular solution of $(E)$.
>
> Let $f$ be any differentiable function on $\mathbb{R}$.
> We claim:
> $$f \text{ is a solution of } (E) \iff f - y_p \text{ is a solution of } (E_0).$$
>
> Indeed:
> - $(f - y_p)' = f' - y'_p = f' - 0 = f'$.
> - Meanwhile, $a(f - y_p) = af - ay_p = af - a\left(-\dfrac{b}{a}\right) = af + b$.
>
> Therefore:
> $$(f - y_p)' = a(f - y_p) \iff f' = af + b.$$
>
> This demonstrates that the difference $f - y_p$ satisfies the homogeneous equation $y' = ay$.
> From Theorem 2.2, there exists a constant $C \in \mathbb{R}$ such that:
> $$(f - y_p)(t) = C e^{at} \iff f(t) = C e^{at} + y_p(t) \iff f(t) = C e^{at} - \dfrac{b}{a}. \quad \blacksquare$$

> **🧭 The Principle of Superposition:**
> $$\text{General Solution of } (E) = \underbrace{C e^{at}}_{\text{General solution of homogeneous equation}} + \underbrace{\left(-\dfrac{b}{a}\right)}_{\text{Constant particular solution}}$$

#### 3.3 Initial Condition for $y' = ay + b$

To determine $C$ from an initial condition $y(t_0) = y_0$:
$$y(t_0) = y_0 \iff C e^{a t_0} - \dfrac{b}{a} = y_0 \iff C e^{a t_0} = y_0 + \dfrac{b}{a} \iff C = \left(y_0 + \dfrac{b}{a}\right) e^{-a t_0}.$$
Substituting back:
$$y(t) = \left(y_0 + \dfrac{b}{a}\right) e^{a(t - t_0)} - \dfrac{b}{a}.$$

> **Worked Example 2 — The Cooling Tea Solved.**
> Revisit our cup of tea cooling from $90^\circ\text{C}$ in a room at $20^\circ\text{C}$.
> The equation is $T'(t) = -0.1 T(t) + 2$ (with $t$ in minutes).
> 1. Determine the general solution of the differential equation.
> 2. Find the unique solution satisfying $T(0) = 90$.
> 3. What will the temperature be after 20 minutes?
> 4. When will the tea reach a comfortable drinking temperature of $45^\circ\text{C}$?
>
> *Step-by-step Solution:*
> 1. This is $y' = ay + b$ with $a = -0.1$ and $b = 2$.
>    The equilibrium constant is $-\dfrac{b}{a} = -\dfrac{2}{-0.1} = 20$.
>    The general solution is:
>    $$T(t) = C e^{-0.1 t} + 20.$$
> 2. Initial condition $T(0) = 90$:
>    $$T(0) = C e^0 + 20 = 90 \iff C + 20 = 90 \iff C = 70.$$
>    The temperature profile is:
>    $$T(t) = 70 e^{-0.1 t} + 20.$$
> 3. At $t = 20$ minutes:
>    $$T(20) = 70 e^{-0.1 \times 20} + 20 = 70 e^{-2} + 20 \approx 70 \times 0.1353 + 20 \approx 9.47 + 20 = 29.5^\circ\text{C}.$$
> 4. Set $T(t) = 45$:
>    $$70 e^{-0.1 t} + 20 = 45 \iff 70 e^{-0.1 t} = 25 \iff e^{-0.1 t} = \dfrac{25}{70} = \dfrac{5}{14}.$$
>    Applying the natural logarithm (Chapter 48):
>    $$-0.1 t = \ln\left(\dfrac{5}{14}\right) = -\ln\left(\dfrac{14}{5}\right) \iff t = 10 \ln(2.8) \approx 10 \times 1.0296 \approx 10.3\text{ minutes}.$$
>    The tea will be drinkable after approximately 10 minutes and 18 seconds.

---

### 4. Foundational Real-World Models

#### 4.1 Charging a Capacitor (RC Circuit)

In an electrical circuit comprising a DC voltage source $E$, a resistor $R$, and a capacitor $C$ in series, Kirchhoff's voltage law yields:
$$u_R(t) + u_C(t) = E.$$
Ohm's law gives $u_R = R i(t)$, while the current through the capacitor is $i(t) = C \dfrac{du_C}{dt}$.
This yields the differential equation:
$$R C \dfrac{du_C}{dt} + u_C(t) = E \iff u'_C(t) = -\dfrac{1}{RC} u_C(t) + \dfrac{E}{RC}.$$

Defining the **time constant** $\tau = RC$ (measured in seconds), the equation becomes:
$$u'_C(t) = -\dfrac{1}{\tau} u_C(t) + \dfrac{E}{\tau}.$$
With the initial condition of an initially uncharged capacitor ($u_C(0) = 0$), the unique solution is:
$$u_C(t) = E \left(1 - e^{-t/\tau}\right).$$

```
       u_C(t) ▲
            E ┼ - - - - - - - - - - - - - - - - - -  Maximum voltage E
              │                      ..-------''
              │                 _--''
        0.63E ┼ - - - - - - - *
              │           _--'¦
              │        .-'    ¦
            0 └───────*───────┴────────────────────► Time t
                      0       τ
```

> **Notable Properties of Time Constant $\tau$:**
> At $t = \tau$, the voltage reaches $u_C(\tau) = E(1 - e^{-1}) \approx E(1 - 0.368) = 0.632 E$.
> The capacitor is charged to **$63.2\%$** of its capacity.
> At $t = 3\tau$, it reaches $95\%$. At $t = 5\tau$, it reaches $99.3\%$ (effectively full charge).

#### 4.2 Terminal Velocity with Linear Drag

A skydiver of mass $m$ falls under the influence of gravity ($P = mg$, downward) and linear aerodynamic air drag ($F = -k v$, upward).
Newton's second law ($m a = \sum F$) gives:
$$m v'(t) = mg - k v(t) \iff v'(t) = -\dfrac{k}{m} v(t) + g.$$

This is of the form $y' = ay + b$ with $a = -\dfrac{k}{m}$ and $b = g$.
The steady-state equilibrium velocity is the **terminal velocity** $v_{\text{lim}}$:
$$v_{\text{lim}} = -\dfrac{b}{a} = -\dfrac{g}{-k/m} = \dfrac{mg}{k}.$$
If the skydiver drops from rest ($v(0) = 0$), the velocity over time is:
$$v(t) = \dfrac{mg}{k} \left(1 - e^{-\frac{k}{m}t}\right).$$
The skydiver accelerates initially at $g$, but as speed rises, drag increases until it balances weight, causing velocity to level off at $v_{\text{lim}}$.

---

### 5. Euler's Method: Solving When Integration Fails

In advanced science, many differential equations are non-linear (such as $y' = y^2 - t$ or $y' = \sin(yt)$) and possess no closed-form solutions in terms of elementary functions!
How do NASA trajectory designers and climate modelers solve them?
They use a simple geometric approximation introduced by **Leonhard Euler** in 1768: **approximate the unknown curve with a sequence of short tangent line segments**.

#### 5.1 The Geometric Concept

Consider the differential equation $y' = f(t, y)$ with initial condition $y(t_0) = y_0$.
Choose a small step size $h > 0$.
1. **At the starting point $(t_0\,; y_0)$:**
   The slope of the tangent line is given directly by the differential equation:
   $$\text{Slope} = y'(t_0) = f(t_0, y_0).$$
2. **Advancing by step $h$:**
   Follow this tangent line forward for a duration $h$. The new time coordinate is $t_1 = t_0 + h$.
   The approximated ordinate $y_1$ is obtained from the local affine approximation:
   $$y_1 = y_0 + h \times y'(t_0) = y_0 + h \times f(t_0, y_0).$$
3. **Iterate from $(t_1\,; y_1)$:**
   Compute the updated slope $f(t_1, y_1)$ and advance by another step $h$:
   $$y_{n+1} = y_n + h \times f(t_n, y_n) \quad \text{with} \quad t_{n+1} = t_n + h.$$

```
       y ▲                                           True curve y(t)
         │                                       ..---*---..
         │                                 _--''     /
         │                           *---''         /
         │                     *---''              /
         │               *---''                   /  Euler line segments (step h)
       y₀┼─────────*---''
         │         │
       0 └─────────┴───────┴───────┴───────┴───────► t
                   t₀      t₁      t₂      t₃
                   |<- h ->|
```

The smaller the step size $h$ ($h = 0.01$, $h = 0.001$), the closer the polygonal approximation hugs the true trajectory!

#### 5.2 Python Implementation of Euler's Method

Here is the Python script implementing Euler's method for $y' = -2y$ with $y(0) = 1$ on $[0\,; 2]$, comparing the numerical simulation against the exact analytical solution $y(t) = e^{-2t}$:

```python
import math

def euler_method(a, b, y0, n):
    """
    Numerically solves y' = -2y on [a, b] with y(a) = y0 using n steps.
    """
    h = (b - a) / n
    t = a
    y = y0
    results = [(t, y, math.exp(-2 * t))]
    
    for _ in range(n):
        # Slope from differential equation y' = -2y
        slope = -2 * y
        y = y + h * slope
        t = t + h
        y_exact = math.exp(-2 * t)
        results.append((round(t, 4), round(y, 4), round(y_exact, 4)))
    
    return results

# Run with 10 steps of h = 0.2
points = euler_method(0, 2, 1.0, 10)
print(f"{'t':<6} | {'y_Euler':<10} | {'y_Exact':<10} | {'Error':<10}")
print("-" * 42)
for t_val, y_e, y_ex in points:
    err = abs(y_e - y_ex)
    print(f"{t_val:<6} | {y_e:<10} | {y_ex:<10} | {err:<10.4f}")
```

---

### Key Takeaways

#### 1. The Linear Differential Equation $y' = ay$
- The general solution on $\mathbb{R}$ is:
  $$y(t) = C e^{at} \quad (C \in \mathbb{R}).$$
- If $a > 0$, solutions explode toward $\pm\infty$ as $t \to +\infty$ (exponential growth).
- If $a < 0$, solutions decay toward $0$ as $t \to +\infty$ (exponential decay toward equilibrium).
- Initial condition: for $y(t_0) = y_0$, the unique solution is $y(t) = y_0 e^{a(t - t_0)}$.

#### 2. The Non-Homogeneous Equation $y' = ay + b$ ($a \neq 0$)
- General solution:
  $$y(t) = C e^{at} - \dfrac{b}{a}.$$
- The term $-\dfrac{b}{a}$ is the **constant particular solution**, representing the steady-state equilibrium value (a horizontal asymptote when $a < 0$).

#### 3. Equations with Variable Forcing $y' = ay + f(t)$
- To solve $y' = ay + f(t)$, find a particular solution $y_p(t)$ matching the functional form of $f$ (a polynomial if $f$ is a polynomial; an exponential if $f$ is an exponential), then form the general solution $y(t) = C e^{at} + y_p(t)$.

#### 4. Euler's Method
- Iterative algorithm with step size $h$:
  $$t_{n+1} = t_n + h \quad \text{and} \quad y_{n+1} = y_n + h \times y'(t_n).$$

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 51.1 —** Elementary Homogeneous Equations.
Solve on $\mathbb{R}$:
1. $y' = 3y$
2. $y' = -5y$
3. $2y' + 6y = 0$
4. $4y' - y = 0$

**Exercise 51.2 —** Initial Value Problems for $y' = ay$.
Find the unique solution satisfying the given initial condition:
1. $y' = 2y$ with $y(0) = 7$
2. $y' = -3y$ with $y(0) = -4$
3. $y' = 0.5y$ with $y(2) = 10$
4. $y' = -y$ with $y(1) = e$

**Exercise 51.3 —** Non-Homogeneous Equations with Constant Forcing $y' = ay + b$.
Solve on $\mathbb{R}$:
1. $y' = -2y + 6$
2. $y' = 4y - 8$
3. $3y' + 9y = 18$
4. $y' = -0.2y + 5$

**Exercise 51.4 —** Initial Conditions for $y' = ay + b$.
1. Solve $y' = -y + 3$ with $y(0) = 1$.
2. Solve $y' = 2y - 10$ with $y(0) = 5$.
3. Solve $2y' + y = 4$ with $y(0) = 0$.

**Exercise 51.5 —** Determining Asymptotes.
Let $f$ be a solution to $y' = -3y + 12$.
1. Determine the general expression for $f(t)$.
2. What is the limit of $f(t)$ as $t \to +\infty$?
3. Deduce the horizontal asymptote common to all solution curves.

**Exercise 51.6 —** Steps in Euler's Method.
Consider $y' = 2t + y$ with $y(0) = 1$.
Using Euler's method with step size $h = 0.1$, compute the approximations $y_1 \approx y(0.1)$ and $y_2 \approx y(0.2)$.

---

#### Level ★★ (Exploration and Exam Preparation)

**Exercise 51.7 —** The Detective's Coffee Cup (Crime Scene Investigation).
A deceased body is discovered in a climate-controlled room held at a steady $20^\circ\text{C}$.
At 2:00 PM, the forensic pathologist measures the body temperature: it reads $30^\circ\text{C}$.
At 3:00 PM, the pathologist measures it again: it has fallen to $28^\circ\text{C}$.
Assume cooling satisfies Newton's law: $T'(t) = -k(T(t) - 20)$, and that normal body temperature is $37^\circ\text{C}$.
1. Taking $t = 0$ at 2:00 PM, express temperature $T(t)$ in terms of $t$ and $k$.
2. Using the measurement taken at 3:00 PM ($t = 1$), determine the exact and numerical value of $k$.
3. Determine the estimated time of death.

**Exercise 51.8 —** Discharging a Capacitor Through a Resistor.
A capacitor of capacitance $C = 50\,\mu\text{F}$ charged to $U_0 = 12\text{ V}$ is discharged through a resistor of resistance $R = 20\,\text{k}\Omega$.
1. Establish the differential equation satisfied by the capacitor voltage $u(t)$.
2. Calculate the time constant $\tau = RC$.
3. Solve the equation and give the expression for $u(t)$.
4. After how much time does the voltage drop below $1\text{ V}$?

**Exercise 51.9 —** Intravenous Drug Infusion (Exam Style).
An antibiotic is administered intravenously at a continuous constant rate.
The quantity of drug $q(t)$ present in the bloodstream (in milligrams) at time $t$ (in hours) satisfies:
$$q'(t) = -0.15 q(t) + 30.$$
At the start of infusion ($t = 0$), no drug is present: $q(0) = 0$.
1. Solve this differential equation to determine $q(t)$.
2. Determine the monotonicity of $q$ on $[0\,; +\infty[$.
3. Determine $\lim\limits_{t \to +\infty} q(t)$. What is the maximum plateau level reached?
4. The drug is therapeutically effective only when the blood concentration exceeds $150\text{ mg}$. When is this threshold reached?

**Exercise 51.10 —** Equation with Affine Forcing $y' = ay + f(t)$.
Consider the differential equation:
$$(E) : \quad y' - 2y = 4x - 6.$$
1. Find constants $m$ and $p$ such that the affine function $y_p(x) = mx + p$ is a particular solution to $(E)$.
2. Solve the associated homogeneous equation $(E_0) : y' - 2y = 0$.
3. Deduce the general solution of $(E)$.
4. Find the unique solution $f$ satisfying $f(0) = 1$.

**Exercise 51.11 —** Equation with Trigonometric Forcing.
Consider $(E) : y' + y = \cos x + \sin x$.
1. Show that $g(x) = \sin x$ is a particular solution to $(E)$.
2. Deduce the general solution of $(E)$.
3. Determine the solution satisfying $y(0) = 2$.

**Exercise 51.12 —** Terminal Velocity of a Raindrop.
A raindrop of mass $m = 4 \times 10^{-5}\text{ kg}$ falls from rest from a cloud. It experiences gravity ($g = 9.81\text{ m}\cdot\text{s}^{-2}$) and air drag $F = -k v$ with $k = 5 \times 10^{-5}\text{ kg}\cdot\text{s}^{-1}$.
1. Formulate the differential equation for velocity $v(t)$.
2. Determine the terminal velocity $v_{\text{lim}}$.
3. Solve the differential equation for $v(t)$.
4. Calculate the time required for the drop to reach $99\%$ of its terminal velocity.

**Exercise 51.13 —** Tangent Condition.
Consider $y' = -2y + 4$.
1. Solve this equation.
2. Does there exist a solution curve whose tangent line at $x = 0$ passes through $A(1\,; 0)$? If so, identify it.

---

#### Level ★★★ (In-Depth Challenges)

**Exercise 51.14 —** Verhulst's Logistic Population Model.
The Malthusian model $y' = ay$ predicts unbounded population growth.
In 1838, **Pierre-François Verhulst** proposed the logistic differential equation:
$$(E_L) : \quad y' = a y \left(1 - \dfrac{y}{K}\right)$$
where $K > 0$ is the carrying capacity of the environment, and $a > 0$ is the intrinsic growth rate.
Let $y$ be a positive solution bounded by $0 < y < K$. Define $z(t) = \dfrac{1}{y(t)}$.
1. Compute the derivative $z'(t)$ in terms of $y(t)$ and $y'(t)$.
2. Substituting $y'(t)$ from $(E_L)$, show that $z$ satisfies the linear differential equation:
   $$z' + az = \dfrac{a}{K}.$$
3. Solve this equation for $z(t)$.
4. Deduce the explicit formula for the population $y(t)$ in terms of initial population $y_0 = y(0)$.
5. Analyze the limits of $y(t)$ as $t \to -\infty$ and $t \to +\infty$. What shape does the curve have?

**Exercise 51.15 —** Second-Order Differential Equation $y'' + \omega^2 y = 0$.
Let $\omega > 0$. We seek all twice-differentiable functions on $\mathbb{R}$ satisfying:
$$(H) : \quad y'' + \omega^2 y = 0.$$
1. Verify that for any constants $A, B \in \mathbb{R}$, $y(t) = A \cos(\omega t) + B \sin(\omega t)$ is a solution.
2. Let $f$ be an arbitrary solution of $(H)$.
   Define $u(t) = \omega f(t) \sin(\omega t) + f'(t) \cos(\omega t)$ and $v(t) = \omega f(t) \cos(\omega t) - f'(t) \sin(\omega t)$.
   Compute the derivatives $u'(t)$ and $v'(t)$.
3. Deduce that $u$ and $v$ are constant functions, and thereby prove that **all** solutions to $(H)$ must be of the form $A\cos(\omega t) + B\sin(\omega t)$.

**Exercise 51.16 —** Error Analysis of Euler's Method.
Consider $y' = y$ with $y(0) = 1$ on $[0\,; 1]$. The exact analytical solution is $y(t) = e^t$, so $y(1) = e$.
Apply Euler's method with $n$ subdivisions of step size $h = \dfrac{1}{n}$.
1. Write the recurrence relation expressing $y_{k+1}$ in terms of $y_k$.
2. Deduce an explicit expression for $y_n$ in terms of $n$.
3. Use this to recover Euler's celebrated classical limit: $\lim\limits_{n \to +\infty} \left(1 + \dfrac{1}{n}\right)^n = e$.

---

### Solutions

#### Level ★ Solutions

**Solution 51.1:**
1. $y' = 3y \implies y(t) = C e^{3t}$ with $C \in \mathbb{R}$.
2. $y' = -5y \implies y(t) = C e^{-5t}$ with $C \in \mathbb{R}$.
3. $2y' + 6y = 0 \iff y' = -3y \implies y(t) = C e^{-3t}$.
4. $4y' - y = 0 \iff y' = \dfrac{1}{4}y \implies y(t) = C e^{t/4}$.

**Solution 51.2:**
1. $y(t) = C e^{2t}$. Condition: $y(0) = C = 7 \implies y(t) = 7 e^{2t}$.
2. $y(t) = C e^{-3t}$. Condition: $y(0) = C = -4 \implies y(t) = -4 e^{-3t}$.
3. $y(t) = C e^{0.5t}$. Condition: $y(2) = C e^1 = 10 \iff C = 10 e^{-1}$. Solution: $y(t) = 10 e^{0.5t - 1}$.
4. $y(t) = C e^{-t}$. Condition: $y(1) = C e^{-1} = e \iff C = e^2$. Solution: $y(t) = e^{2-t}$.

**Solution 51.3:**
General formula for $y' = ay + b$: $y(t) = C e^{at} - \dfrac{b}{a}$.
1. $a = -2, b = 6 \implies -\dfrac{b}{a} = 3$. Solution: $y(t) = C e^{-2t} + 3$.
2. $a = 4, b = -8 \implies -\dfrac{b}{a} = 2$. Solution: $y(t) = C e^{4t} + 2$.
3. $y' = -3y + 6 \implies -\dfrac{b}{a} = 2$. Solution: $y(t) = C e^{-3t} + 2$.
4. $a = -0.2, b = 5 \implies -\dfrac{b}{a} = 25$. Solution: $y(t) = C e^{-0.2t} + 25$.

**Solution 51.4:**
1. $y(t) = C e^{-t} + 3$. Condition $y(0) = C + 3 = 1 \iff C = -2$. Solution: $y(t) = -2e^{-t} + 3$.
2. $y(t) = C e^{2t} + 5$. Condition $y(0) = C + 5 = 5 \iff C = 0$. Constant solution: $y(t) = 5$.
3. $y' = -0.5y + 2$. General solution: $y(t) = C e^{-0.5t} + 4$. Condition $y(0) = C + 4 = 0 \iff C = -4$. Solution: $y(t) = 4(1 - e^{-0.5t})$.

**Solution 51.5:**
1. $a = -3, b = 12 \implies -\dfrac{b}{a} = 4$. Solution: $f(t) = C e^{-3t} + 4$.
2. Since $-3 < 0$, $\lim\limits_{t \to +\infty} e^{-3t} = 0$, so $\lim\limits_{t \to +\infty} f(t) = 4$.
3. The horizontal line $y = 4$ is the common horizontal asymptote as $t \to +\infty$.

**Solution 51.6:**
- At $t_0 = 0$, $y_0 = 1$. Slope is $y'(0) = 2(0) + 1 = 1$.
  $y_1 = y_0 + h \times y'(0) = 1 + 0.1(1) = 1.1$ at $t_1 = 0.1$.
- At $t_1 = 0.1$, $y_1 = 1.1$. Estimated slope is $y'(0.1) \approx 2(0.1) + 1.1 = 1.3$.
  $y_2 = y_1 + h \times y'(t_1) = 1.1 + 0.1(1.3) = 1.23$ at $t_2 = 0.2$.

---

#### Level ★★ Solutions

**Solution 51.7:**
1. The equation is $T'(t) = -k T(t) + 20k$.
   The general solution is $T(t) = C e^{-kt} + 20$.
   At 2:00 PM ($t = 0$), $T(0) = 30 \implies C + 20 = 30 \iff C = 10$.
   Thus $T(t) = 10 e^{-kt} + 20$.
2. At 3:00 PM ($t = 1$), $T(1) = 28$:
   $10 e^{-k} + 20 = 28 \iff 10 e^{-k} = 8 \iff e^{-k} = 0.8 \iff k = -\ln(0.8) = \ln(1.25) \approx 0.22314\text{ h}^{-1}$.
3. Let $t_d$ be the time of death, when body temperature was $37^\circ\text{C}$:
   $10 e^{-k t_d} + 20 = 37 \iff 10 e^{-k t_d} = 17 \iff e^{-k t_d} = 1.7$.
   Taking logarithms:
   $$-k t_d = \ln(1.7) \iff t_d = -\dfrac{\ln(1.7)}{k} \approx -\dfrac{0.53063}{0.22314} \approx -2.378\text{ hours}.$$
   Converting $0.378\text{ h}$ to minutes: $0.378 \times 60 \approx 23\text{ minutes}$.
   Death occurred $2\text{ hours and } 23\text{ minutes}$ prior to 2:00 PM, at **11:37 AM**.

**Solution 51.8:**
1. During discharge, $u_R + u_C = 0 \iff R C u'(t) + u(t) = 0 \iff u'(t) = -\dfrac{1}{RC} u(t)$.
2. $\tau = RC = 20 \times 10^3 \times 50 \times 10^{-6} = 1.0\text{ second}$.
3. $u'(t) = -u(t)$. With $u(0) = 12\text{ V}$, $u(t) = 12 e^{-t}$.
4. $u(t) < 1 \iff 12 e^{-t} < 1 \iff e^{-t} < \dfrac{1}{12} \iff t > \ln 12 \approx 2.48\text{ seconds}$.

**Solution 51.9:**
1. Equation $y' = ay + b$ with $a = -0.15$ and $b = 30$.
   Equilibrium value: $-\dfrac{b}{a} = 200$.
   General solution: $q(t) = C e^{-0.15t} + 200$.
   With $q(0) = 0 \implies C = -200$, we have $q(t) = 200(1 - e^{-0.15t})$.
2. $q'(t) = 30 e^{-0.15t} > 0$. The drug quantity is strictly increasing on $[0\,; +\infty[$.
3. Since $-0.15 < 0$, $\lim\limits_{t \to +\infty} q(t) = 200\text{ mg}$. The bloodstream level never exceeds $200\text{ mg}$.
4. $q(t) \geq 150 \iff 200(1 - e^{-0.15t}) \geq 150 \iff e^{-0.15t} \leq 0.25$.
   Taking $\ln$: $-0.15t \leq -\ln 4 \iff t \geq \dfrac{\ln 4}{0.15} \approx 9.24\text{ hours}$ (approx. 9 hours and 14 minutes).

**Solution 51.10:**
1. $y_p(x) = mx + p \implies y'_p(x) = m$.
   Substitute into $(E)$: $m - 2(mx + p) = 4x - 6 \iff -2mx + (m - 2p) = 4x - 6$.
   Equating coefficients: $-2m = 4 \implies m = -2$, and $m - 2p = -6 \implies -2 - 2p = -6 \implies p = 2$.
   Particular solution: $y_p(x) = -2x + 2$.
2. Homogeneous equation: $y' - 2y = 0 \implies y(x) = C e^{2x}$.
3. General solution: $y(x) = C e^{2x} - 2x + 2$ with $C \in \mathbb{R}$.
4. Condition $f(0) = 1 \implies C + 2 = 1 \iff C = -1$.
   Unique solution: $f(x) = -e^{2x} - 2x + 2$.

**Solution 51.11:**
1. $g(x) = \sin x \implies g'(x) = \cos x$.
   $g'(x) + g(x) = \cos x + \sin x$. The equation is satisfied.
2. Homogeneous equation $y' + y = 0 \implies y(x) = C e^{-x}$.
   General solution: $y(x) = C e^{-x} + \sin x$.
3. $y(0) = C e^0 + \sin 0 = C = 2$. Solution: $y(x) = 2e^{-x} + \sin x$.

**Solution 51.12:**
1. $v'(t) = -\dfrac{k}{m}v(t) + g$.
   Here $\dfrac{k}{m} = \dfrac{5 \times 10^{-5}}{4 \times 10^{-5}} = 1.25\text{ s}^{-1}$.
   The equation is $v'(t) = -1.25 v(t) + 9.81$.
2. $v_{\text{lim}} = \dfrac{9.81}{1.25} = 7.848\text{ m}\cdot\text{s}^{-1}$ ($28.3\text{ km/h}$).
3. General solution: $v(t) = C e^{-1.25t} + 7.848$.
   Initial condition $v(0) = 0 \implies C = -7.848$.
   $v(t) = 7.848(1 - e^{-1.25t})$.
4. $v(t) = 0.99 v_{\text{lim}} \iff 1 - e^{-1.25t} = 0.99 \iff e^{-1.25t} = 0.01$.
   $t = \dfrac{\ln 100}{1.25} \approx \dfrac{4.605}{1.25} \approx 3.68\text{ seconds}$.

**Solution 51.13:**
1. $y' = -2y + 4 \implies y(x) = C e^{-2x} + 2$.
2. The tangent line at $x = 0$ is $y = y'(0)x + y(0)$.
   Here $y(0) = C + 2$ and $y'(0) = -2(C+2) + 4 = -2C$.
   Tangent equation: $y = -2C x + (C + 2)$.
   Passing through $(1\,; 0)$ requires $0 = -2C(1) + C + 2 \iff -C + 2 = 0 \iff C = 2$.
   Unique solution: $y(x) = 2e^{-2x} + 2$.

---

#### Level ★★★ Solutions

**Solution 51.14:**
1. $z(t) = \dfrac{1}{y(t)} \implies z'(t) = -\dfrac{y'(t)}{(y(t))^2}$.
2. From $(E_L)$, $y'(t) = a y(t) - \dfrac{a}{K}(y(t))^2$.
   Then:
   $z'(t) = -\dfrac{a y(t) - \frac{a}{K}(y(t))^2}{(y(t))^2} = -\dfrac{a}{y(t)} + \dfrac{a}{K} = -a z(t) + \dfrac{a}{K}$.
   Rearranging gives the linear equation $z' + az = \dfrac{a}{K}$.
3. The equilibrium solution of $z' = -az + \dfrac{a}{K}$ is $\dfrac{a/K}{a} = \dfrac{1}{K}$.
   Thus $z(t) = B e^{-at} + \dfrac{1}{K}$ with $B \in \mathbb{R}$.
4. At $t = 0$, $z(0) = \dfrac{1}{y_0} = B + \dfrac{1}{K} \implies B = \dfrac{K - y_0}{K y_0}$.
   Then $z(t) = \dfrac{1}{K}\left(1 + \dfrac{K - y_0}{y_0} e^{-at}\right)$.
   Inverting $z(t)$:
   $$y(t) = \dfrac{K}{1 + \left(\dfrac{K - y_0}{y_0}\right) e^{-at}}.$$
5. As $t \to +\infty$, $e^{-at} \to 0$ (since $a > 0$), so $\lim\limits_{t \to +\infty} y(t) = K$.
   The resulting trajectory is an **S-shaped logistic curve** (sigmoid) that saturates smoothly at carrying capacity $K$.

**Solution 51.15:**
1. For $y(t) = A\cos(\omega t) + B\sin(\omega t)$:
   $y'(t) = -A\omega\sin(\omega t) + B\omega\cos(\omega t)$.
   $y''(t) = -A\omega^2\cos(\omega t) - B\omega^2\sin(\omega t) = -\omega^2 y(t)$.
   Hence $y'' + \omega^2 y = 0$.
2. Differentiate $u(t) = \omega f(t)\sin(\omega t) + f'(t)\cos(\omega t)$:
   $u'(t) = \omega f'(t)\sin(\omega t) + \omega^2 f(t)\cos(\omega t) + f''(t)\cos(\omega t) - \omega f'(t)\sin(\omega t) = \big(f''(t) + \omega^2 f(t)\big)\cos(\omega t) = 0$.
   Similarly, $v'(t) = -\big(f''(t) + \omega^2 f(t)\big)\sin(\omega t) = 0$.
3. Since $u'$ and $v'$ are identically zero on $\mathbb{R}$, $u$ and $v$ are constant: $u(t) = B\omega$ and $v(t) = A\omega$.
   Computing $\dfrac{u(t)\sin(\omega t) + v(t)\cos(\omega t)}{\omega}$ yields:
   $f(t)(\sin^2(\omega t) + \cos^2(\omega t)) = f(t) = A\cos(\omega t) + B\sin(\omega t)$.
   Every solution must be of this form!

**Solution 51.16:**
1. $y' = y \implies y_{k+1} = y_k + h y_k = (1 + h) y_k$.
2. With $y_0 = 1$ and $h = \dfrac{1}{n}$, $(y_k)$ is geometric with common ratio $\left(1 + \dfrac{1}{n}\right)$.
   After $n$ steps (reaching $t = n h = 1$):
   $y_n = \left(1 + \dfrac{1}{n}\right)^n$.
3. Since Euler's method converges to the exact solution $y(1) = e^1 = e$ as $n \to +\infty$, we immediately recover:
   $$\lim_{n \to +\infty} \left(1 + \dfrac{1}{n}\right)^n = e.$$

---

### The Question that Opens What Follows

Until now, we have described movement and physical change along a single line (time $t$) or across a two-dimensional flat plane (a sheet of paper with coordinates $x$ and $y$).
Yet our physical universe is not flat: the Earth floats in three-dimensional space, medieval cathedrals loft their vaults into the sky, satellites traverse inclined orbital planes, and aircraft navigate using latitude, longitude, and altitude.

How do we pinpoint a position, trace a line, and establish the algebraic equation of a tilted plane in three-dimensional space? How do we calculate the shortest distance from an airborne drone to the wall of a cathedral?

Join us in Chapter 52 with **The Cathedral in Space** and vector geometry in three dimensions.
