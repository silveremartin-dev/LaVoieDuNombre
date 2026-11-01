# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 54: The Thousand Coin Tosses

> *“If you toss a coin ten times, chance may play the prank of giving you ten Heads in a row. But toss it a million times: disorder cancels out, caprice fades away, and out of the anarchy of individual tosses emerges a crystalline regularity. The law of large numbers is not some magical constraint imposed upon the coin: it is the inevitable mathematical victory of the multitude over the singular.”*

---

### What You Are About to Discover

- How to model the repetition of identical and independent random trials via the **Bernoulli scheme**.
- The rigorous construction of the **binomial distribution $\mathcal{B}(n, p)$** and the combinatorial rationale behind the formula $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
- The required examination proofs of the **expected value** $E(X) = np$ and the **variance** $V(X) = np(1-p)$ via decomposition into sums of independent Bernoulli random variables.
- **Markov's inequality** and the **Bienaymé-Chebyshev inequality**, bounding the dispersion of any random variable.
- The **concentration inequality** and the proof of the **Weak Law of Large Numbers**: why observed frequency inexorably converges to theoretical probability.
- A complete **Python** simulation script of 10,000 coin tosses to observe firsthand the sharpening around the mean.

---

### 1. The Problem: The Casino, the Pollster, and the Insurer

#### 1.1 The Gambler's Coin
Imagine playing Heads or Tails with a stranger on a train. You bet 1 euro on Tails.
On the first toss: Heads. You lose €1.
On the second toss: Heads. You lose €2.
On the third: Heads. Doubt begins to creep in.
On the tenth consecutive toss, the coin lands on Heads yet again!
The stranger smiles at you and says: *“That's just random chance, my friend. On the next toss, Tails is actually more likely to come up to balance things out!”*
Two fatal errors hide behind that casual sentence:
1. **The Gambler's Fallacy:** The coin possesses no memory of its past outcomes. On every single toss, the probability of obtaining Tails remains strictly equal to $\frac{1}{2}$.
2. **Legitimate Suspicion:** Obtaining 10 consecutive Heads with a fair coin has probability $\left(\frac{1}{2}\right)^{10} = \frac{1}{1024} \approx 0.00098$, or less than one chance in a thousand. The coin is overwhelmingly likely to be loaded!

#### 1.2 The Pollster and the Insurer
How can a polling institute determine the political leanings of 45 million citizens by surveying a mere 1,000 respondents, achieving a margin of error under 3%?
How can an insurance company guarantee reimbursement for fire damages when it has no way of predicting which specific houses will burn down this year?
Their secret is identical: **individually, the outcome of a single trial is unpredictable; collectively, the average of a large number of trials behaves with near-absolute certainty.**

To transition from the erratic caprice of a single trial to the certainty of large aggregates, mathematicians forged two monumental instruments: the **binomial distribution** and the **law of large numbers**.

---

### 2. From the Bernoulli Trial to the Binomial Distribution

#### 2.1 The Bernoulli Trial
The Swiss mathematician and physicist **Jacob Bernoulli** (1655–1705) studied the most elementary random experiment imaginable: one admitting only **two possible outcomes**.

> **📐 Definition — Bernoulli Trial**
> A **Bernoulli trial** with parameter $p \in (0, 1)$ is a random experiment that admits only two complementary outcomes:
> - One conventionally designated **Success** (denoted $S$), with probability $P(S) = p$.
> - The other conventionally designated **Failure** (denoted $F$ or $\overline{S}$), with probability $P(F) = 1 - p$ (often denoted $q$).
>
> The associated indicator random variable $X$ that equals $1$ on success and $0$ on failure follows a **Bernoulli distribution** with parameter $p$, denoted $X \sim \mathcal{B}(p)$.

*Bernoulli Probability Mass Function Table:*
| $k$ | 0 | 1 |
|---|---|---|
| $P(X = k)$ | $1 - p$ | $p$ |

Let us immediately compute its parameters:
- **Expected Value (Mean):**
  $$E(X) = 0 \times P(X=0) + 1 \times P(X=1) = 0 \times (1-p) + 1 \times p = p$$
- **Variance:**
  By the Koenig-Huygens formula ($V(X) = E(X^2) - (E(X))^2$):
  Since $X$ only takes values 0 and 1, we have $X^2 = X$, and thus $E(X^2) = E(X) = p$.
  $$V(X) = p - p^2 = p(1 - p)$$
- **Standard Deviation:**
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{p(1-p)}$$

#### 2.2 The Bernoulli Scheme

> **📐 Definition — Bernoulli Scheme**
> A **Bernoulli scheme** with parameters $n$ and $p$ is the sequence of $n$ identical and **mutually independent** Bernoulli trials, each having the same success probability $p$.

*What does independence mean?*
The outcome of any trial in no way affects the probabilities of subsequent trials. Examples include consecutive coin tosses, or draws from an urn **with replacement**. If draws are made *without replacement*, trials are not independent: this would not constitute a Bernoulli scheme!

#### 2.3 The Probability Tree and the Binomial Distribution
Let us represent a Bernoulli scheme of $n = 3$ trials on a probability tree:

![Probability tree of a Bernoulli scheme with 3 independent trials](figures/vol_6/fig_54_arbre_bernoulli.svg)

Consider the random variable $X$ that counts the **total number of successes** obtained across the $n$ trials.
- $X$ can take any integer value between $0$ and $n$.
- What is the probability of obtaining exactly 2 successes when $n = 3$?
  Let us trace the paths yielding 2 successes:
  - $S-S-F$: probability $p \times p \times (1-p) = p^2(1-p)$
  - $S-F-S$: probability $p \times (1-p) \times p = p^2(1-p)$
  - $F-S-S$: probability $(1-p) \times p \times p = p^2(1-p)$
  Every path comprising 2 successes and 1 failure has the exact same probability $p^2(1-p)$.
  How many such paths exist? Exactly 3 paths.
  Hence $P(X = 2) = 3 \times p^2(1-p)$.
  And what is this number 3? It is the number of ways to choose the positions of the 2 successes among the 3 trials, which is $\binom{3}{2} = 3$!

> **📐 Fundamental Theorem — The Binomial Distribution**
> Let $X$ be the random variable equal to the number of successes in a Bernoulli scheme of $n$ independent trials with parameter $p$.
> We say that $X$ follows the **binomial distribution with parameters $n$ and $p$**, denoted:
> $$X \sim \mathcal{B}(n, p)$$
> For every integer $k \in \{0, 1, 2, \dots, n\}$, the probability of obtaining exactly $k$ successes is:
>
> $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}$$

*Consistency Check:*
The sum of all probabilities must equal 1:
$$\sum_{k=0}^n P(X = k) = \sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1^n = 1.$$
This is none other than Newton's binomial expansion from Chapter 53! That algebraic connection is precisely why this law is named the **binomial distribution**.

---

### 3. Expected Value and Variance: Core Derivations

#### 3.1 Sum of Independent Random Variables
Let $X_1, X_2, \dots, X_n$ be the $n$ Bernoulli indicator variables associated with the $n$ trials:
$$X_i = \begin{cases} 1 & \text{if the } i\text{-th trial is a success} \\ 0 & \text{if it is a failure} \end{cases}$$
The total number of successes $X$ is simply the sum of these indicators:
$$X = X_1 + X_2 + \dots + X_n = \sum_{i=1}^n X_i$$

Recall two fundamental properties of random variables:
1. **Linearity of Expectation:** For any random variables $X$ and $Y$ (independent or not) and any constant $a \in \mathbb{R}$:
   $$E(X + Y) = E(X) + E(Y) \quad \text{and} \quad E(aX) = a E(X)$$
2. **Additivity of Variance for Independent Variables:**
   If $X$ and $Y$ are **independent** random variables:
   $$V(X + Y) = V(X) + V(Y)$$
   *(Note: for a scalar constant $a$, $V(aX) = a^2 V(X)$).*

#### 3.2 Derivation of Expected Value for the Binomial Distribution

> **✍️ Required Proof — Expected Value of the Binomial Distribution**
> Let $X \sim \mathcal{B}(n, p)$. We decompose $X$ as $X = \sum_{i=1}^n X_i$, where the $X_i$ are $n$ identical Bernoulli variables with parameter $p$.
> For each $i \in \{1, \dots, n\}$, we have $E(X_i) = p$.
> By linearity of expectation:
> $$E(X) = E\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n E(X_i) = \underbrace{p + p + \dots + p}_{n \text{ terms}} = np$$
>
> $$\mathbf{E(X) = n p}$$

*Intuitive Meaning:* If you toss a fair coin ($p = 0.5$) 100 times, you expect on average to obtain $100 \times 0.5 = 50$ Heads. If you roll a die 60 times and win on a 6 ($p = 1/6$), you expect on average to win $60 \times \frac{1}{6} = 10$ times.

#### 3.3 Derivation of Variance and Standard Deviation

> **✍️ Required Proof — Variance of the Binomial Distribution**
> Since the trials are mutually independent in a Bernoulli scheme, the random variables $X_1, X_2, \dots, X_n$ are independent.
> By additivity of variance for independent variables:
> $$V(X) = V\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n V(X_i)$$
> For each Bernoulli variable $X_i$, we previously established that $V(X_i) = p(1 - p)$.
> Hence:
> $$V(X) = \sum_{i=1}^n p(1 - p) = \underbrace{p(1-p) + \dots + p(1-p)}_{n \text{ terms}} = np(1 - p)$$
>
> $$\mathbf{V(X) = n p (1 - p)}$$
>
> The standard deviation is consequently:
>
> $$\mathbf{\sigma(X) = \sqrt{n p (1 - p)}}$$

*Crucial Remark on Scaling:*
- The expectation $E(X)$ scales linearly with $n$ (order of magnitude $n$).
- The standard deviation $\sigma(X)$ scales only as $\sqrt{n}$.
This asymmetry between $n$ and $\sqrt{n}$ holds the key to the entire phenomenon of statistical stabilization!

---

### 4. Dispersion and Concentration: From Markov to Bienaymé-Chebyshev

How can we bound the probability that a random variable deviates substantially from its mean?

#### 4.1 Markov's Inequality
The Russian mathematician **Andrey Markov** (1856–1922) established a universal bound for non-negative random variables.

> **📐 Theorem — Markov's Inequality**
> Let $Y$ be a non-negative random variable ($Y \geq 0$).
> For any strictly positive real number $a > 0$:
> $$P(Y \geq a) \leq \frac{E(Y)}{a}$$

> **✍️ Curriculum Proof — Markov's Inequality**
> Let $Y$ be a discrete random variable taking non-negative values $y_1, y_2, \dots, y_m \geq 0$.
> The expected value is given by:
> $$E(Y) = \sum_{i=1}^m y_i P(Y = y_i)$$
> Split this sum into two parts: outcomes strictly less than $a$, and outcomes greater than or equal to $a$:
> $$E(Y) = \sum_{y_i < a} y_i P(Y = y_i) + \sum_{y_i \geq a} y_i P(Y = y_i)$$
> Since all values $y_i$ and probabilities are non-negative, the first sum is $\geq 0$. Thus:
> $$E(Y) \geq \sum_{y_i \geq a} y_i P(Y = y_i)$$
> In this second sum, each value satisfies $y_i \geq a$. We can therefore replace each $y_i$ by its lower bound $a$:
> $$E(Y) \geq \sum_{y_i \geq a} a P(Y = y_i) = a \sum_{y_i \geq a} P(Y = y_i) = a P(Y \geq a)$$
> Because $a > 0$, dividing by $a$ immediately yields:
> $$P(Y \geq a) \leq \frac{E(Y)}{a}$$

*Striking Example:* If the average monthly income in a country is €2,000, what fraction of the population could earn at least €10,000?
Here $Y \geq 0$, $E(Y) = 2\,000$, and $a = 10\,000$.
$P(Y \geq 10\,000) \leq \frac{2\,000}{10\,000} = \frac{1}{5} = 20\%$.
It is mathematically impossible for more than 20% of citizens to earn more than 5 times the national average!

#### 4.2 The Bienaymé-Chebyshev Inequality
The French mathematician **Irénée-Jules Bienaymé** (1853) and his Russian peer **Pafnuty Chebyshev** (1867) had the brilliant insight to apply Markov's inequality to the squared deviation from the mean: $Y = (X - E(X))^2$.

> **📐 Fundamental Theorem — Bienaymé-Chebyshev Inequality**
> Let $X$ be a random variable admitting expectation $E(X)$ and variance $V(X)$.
> For any real number $\varepsilon > 0$ (epsilon):
> $$P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$$

> **✍️ Required Proof — Bienaymé-Chebyshev**
> Let $\varepsilon > 0$. Note the fundamental equivalence between events:
> $$|X - E(X)| \geq \varepsilon \iff (X - E(X))^2 \geq \varepsilon^2$$
> Define the auxiliary random variable $Y = (X - E(X))^2$.
> - $Y$ is non-negative ($Y \geq 0$).
> - Its expectation is, by definition, the variance of $X$: $E(Y) = E\left((X - E(X))^2\right) = V(X)$.
>
> Apply Markov's inequality to the non-negative variable $Y$ with threshold $a = \varepsilon^2 > 0$:
> $$P(Y \geq \varepsilon^2) \leq \frac{E(Y)}{\varepsilon^2}$$
> Replacing $Y$ by its definition and $E(Y)$ by $V(X)$:
> $$P\left((X - E(X))^2 \geq \varepsilon^2\right) \leq \frac{V(X)}{\varepsilon^2}$$
> Which translates precisely to:
> $$P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$$

*Significance:*
The probability that a random variable $X$ strays from its mean by at least $\varepsilon$ is strictly bounded by a term proportional to its variance, decaying rapidly with the inverse square of the distance $\varepsilon^2$.

---

### 5. The Weak Law of Large Numbers

#### 5.1 The Sample Mean of an Empirical Sample
Consider $n$ independent random variables $X_1, X_2, \dots, X_n$ that are **identically distributed**, sharing the same mean $\mu = E(X_1)$ and the same variance $\sigma^2 = V(X_1)$.
We define the **sample mean** (or empirical average) as the random variable:
$$M_n = \frac{X_1 + X_2 + \dots + X_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i$$

Let us compute the mean and variance of this sample mean:
- **Expectation of $M_n$:**
  $$E(M_n) = E\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n} \sum_{i=1}^n E(X_i) = \frac{1}{n} \times n\mu = \mu$$
  The sample mean is **unbiased**: on average, it hits the theoretical value $\mu$ exactly.
- **Variance of $M_n$:**
  By independence of the variables $X_i$, pulling out the factor $\frac{1}{n}$ squared:
  $$V(M_n) = V\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n V(X_i) = \frac{1}{n^2} \times n\sigma^2 = \frac{\sigma^2}{n}$$

Look closely at this ratio:
$$V(M_n) = \frac{V(X_1)}{n}$$
As the sample size $n$ grows indefinitely, **the variance of the sample mean vanishes toward zero**!

#### 5.2 The Concentration Inequality

> **📐 Theorem — Concentration Inequality**
> For every real number $\varepsilon > 0$:
> $$P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$$

*Proof:*
Simply apply the Bienaymé-Chebyshev inequality to the random variable $M_n$:
$$P(|M_n - E(M_n)| \geq \varepsilon) \leq \frac{V(M_n)}{\varepsilon^2}$$
Substituting $E(M_n) = \mu$ and $V(M_n) = \frac{V(X_1)}{n}$ gives the result directly.

#### 5.3 Proof of the Weak Law of Large Numbers

> **✍️ Required Proof — Weak Law of Large Numbers**
> Let $\varepsilon > 0$ be an arbitrarily small positive tolerance (for instance, $\varepsilon = 0.001$).
> The concentration inequality guarantees that:
> $$0 \leq P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$$
> As $n \to +\infty$, the numerator $V(X_1)$ and $\varepsilon^2$ remain fixed constants.
> Hence:
> $$\lim_{n \to +\infty} \frac{V(X_1)}{n \varepsilon^2} = 0$$
> By the Squeeze Theorem (Sandwich Rule):
>
> $$\mathbf{\lim_{n \to +\infty} P(|M_n - \mu| \geq \varepsilon) = 0}$$
>
> Equivalently, passing to the complementary event:
>
> $$\mathbf{\lim_{n \to +\infty} P(|M_n - \mu| < \varepsilon) = 1}$$

*Philosophical and Practical Meaning:*
No matter how tiny the error margin $\varepsilon > 0$ might be, provided the sample size $n$ is sufficiently large, the probability that the sample average lands within the interval $(\mu - \varepsilon, \mu + \varepsilon)$ approaches 100%.
In the specific case of coin tosses where $X_i \sim \mathcal{B}(p)$, $M_n = \frac{X}{n} = F_n$ is the **observed frequency** of successes.
The observed frequency of an event thus converges mathematically to its theoretical probability $p$!

---

### 6. Python Simulation: 10,000 Tosses Before Your Eyes

To verify this theorem experimentally, let us run a Python simulation of $N = 10\,000$ tosses of a fair coin ($p = 0.5$) tracking the evolution of the relative frequency of Heads:

```python
import random

def simulate_tosses(n):
    successes = 0
    frequency_history = []
    
    for i in range(1, n + 1):
        # 1 = Heads (success), 0 = Tails (failure)
        draw = random.choice([0, 1])
        successes += draw
        frequency = successes / i
        frequency_history.append((i, frequency))
        
    return frequency_history

# Run the simulation
results = simulate_tosses(10000)

# Display key milestones
milestones = [10, 50, 100, 500, 1000, 5000, 10000]
print(f"{'Tosses (n)':<12} | {'Heads Frequency':<17} | {'Deviation from 0.5':<18}")
print("-" * 50)
for m in milestones:
    freq = results[m - 1][1]
    deviation = abs(freq - 0.5)
    print(f"{m:<12} | {freq:<17.4f} | {deviation:<18.4f}")
```

*Typical Console Output:*
```
Tosses (n)   | Heads Frequency   | Deviation from 0.5
--------------------------------------------------
10           | 0.7000            | 0.2000            
50           | 0.4400            | 0.0600            
100          | 0.5300            | 0.0300            
500          | 0.4880            | 0.0120            
1000         | 0.5040            | 0.0040            
5000         | 0.4982            | 0.0018            
10000        | 0.5007            | 0.0007            
```

At first (10 tosses), the frequency fluctuates erratically (anywhere from 0.30 to 0.70).
By 1,000 tosses, it is locked within 1% of 0.5.
At 10,000 tosses, precision reaches parts per thousand! The chaotic storm of chance has crystallized into stable order.

> **🔍 True History — The Galton Board and the Bell Curve**
> In 1877, British polymath Francis Galton conceived a physical apparatus to visualize the convergence of the binomial distribution: **the quincunx** (or **Galton board**). Steel ball bearings drop one by one through a triangular array of pegs. At each peg encountered, the ball has an equal probability of bouncing right ($S$) or left ($F$). At the bottom, the balls accumulate into vertical columns: the central pile rises majestically while the extremities taper off, carving out the bell curve of Gauss with astonishing mechanical regularity.

![The Galton Board: physical manifestation of the convergence of Pascal's triangle to the Gaussian bell curve](figures/histoire/ch_54_galton_box.png)

---

### 7. Step-by-Step Worked Examples

#### Example 1: Industrial Quality Control
A factory manufactures LED bulbs. The probability that any single bulb is defective is $p = 0.02$. A sample of $n = 100$ bulbs is selected at random. Production volume is sufficiently large that this selection can be modeled as sampling with replacement.
Let $X$ denote the number of defective bulbs in the batch.
1. State the probability distribution of $X$ and its parameters.
2. Calculate the mean and standard deviation of $X$.
3. Calculate the probability of finding exactly 2 defective bulbs.
4. Calculate the probability of finding at least one defective bulb.

**Detailed Solution:**
1. The experiment consists of repeating $n = 100$ identical trials (testing a bulb) with two outcomes:
   - Success $S$: “the bulb is defective”, with probability $p = 0.02$.
   - Failure $\overline{S}$: “the bulb works properly”, with probability $1 - p = 0.98$.
   Because sampling is treated as independent with replacement, trials are independent.
   The variable $X$ counts the total number of successes.
   Therefore, $X$ follows the **binomial distribution** with parameters $n = 100$ and $p = 0.02$: $X \sim \mathcal{B}(100, 0.02)$.
2. - Expected value: $E(X) = np = 100 \times 0.02 = 2$.
     On average, a batch of 100 bulbs contains 2 defective units.
   - Variance: $V(X) = np(1-p) = 100 \times 0.02 \times 0.98 = 1.96$.
   - Standard deviation: $\sigma(X) = \sqrt{1.96} = 1.4$.
3. Probability of exactly 2 defectives:
   $$P(X = 2) = \binom{100}{2} (0.02)^2 (0.98)^{98}$$
   Here $\binom{100}{2} = \frac{100 \times 99}{2} = 4\,950$.
   $(0.02)^2 = 0.0004$.
   $(0.98)^{98} \approx 0.1380$.
   $$P(X = 2) = 4\,950 \times 0.0004 \times 0.1380 \approx 0.2734 \quad (\approx 27.3\%).$$
4. “At least one defective” corresponds to $X \geq 1$.
   The complementary event is “zero defectives”, $X = 0$.
   $$P(X = 0) = \binom{100}{0} (0.02)^0 (0.98)^{100} = 1 \times 1 \times (0.98)^{100} \approx 0.1326.$$
   Hence:
   $$P(X \geq 1) = 1 - P(X = 0) = 1 - (0.98)^{100} \approx 1 - 0.1326 = 0.8674 \quad (\approx 86.7\%).$$

#### Example 2: Guessing on a Multiple-Choice Exam
A candidate takes a test unprepared. The test consists of 10 independent multiple-choice questions. For each question, 4 choices are offered, of which exactly one is correct. The candidate guesses randomly on every question.
Passing requires at least 6 correct answers.
What is the probability that the candidate passes?

**Detailed Solution:**
Let $X$ be the number of correct answers. The 10 questions are independent with success probability $p = \frac{1}{4} = 0.25$.
Thus $X \sim \mathcal{B}(10, 0.25)$.
The candidate passes if $X \geq 6$.
$$P(X \geq 6) = P(X = 6) + P(X = 7) + P(X = 8) + P(X = 9) + P(X = 10)$$
Compute each term:
- $P(X = 6) = \binom{10}{6} (0.25)^6 (0.75)^4 = 210 \times \frac{1}{4096} \times \frac{81}{256} = \frac{17\,010}{1\,048\,576} \approx 0.01622$
- $P(X = 7) = \binom{10}{7} (0.25)^7 (0.75)^3 = 120 \times \frac{1}{16384} \times \frac{27}{64} = \frac{3\,240}{1\,048\,576} \approx 0.00309$
- $P(X = 8) = \binom{10}{8} (0.25)^8 (0.75)^2 = 45 \times \frac{1}{65536} \times \frac{9}{16} = \frac{405}{1\,048\,576} \approx 0.000386$
- $P(X = 9) = \binom{10}{9} (0.25)^9 (0.75)^1 = 10 \times \frac{3}{1\,048\,576} \approx 0.000029$
- $P(X = 10) = \binom{10}{10} (0.25)^{10} (0.75)^0 = \frac{1}{1\,048\,576} \approx 0.000001$

Summing these probabilities:
$$P(X \geq 6) \approx 0.01622 + 0.00309 + 0.00039 + 0.00003 + 0.000001 = 0.01973 \approx 1.97\%.$$
The candidate has less than a $2\%$ chance of passing purely by luck.

#### Example 3: Airline Overbooking
An airliner has 200 seats. The airline knows from historical data that 5% of ticket holders do not show up for boarding ($p_{\text{show}} = 0.95$).
The airline sells $n = 205$ tickets.
1. What is the probability that all passengers who show up receive a seat?
2. What is the probability that the airline faces an overbooking crisis (at least one passenger bumped without a seat)?

**Detailed Solution:**
1. Let $Y$ be the number of passengers arriving for boarding among the 205 ticket holders. Assuming passenger decisions are independent, $Y \sim \mathcal{B}(205, 0.95)$.
   Every arriving passenger receives a seat if and only if $Y \leq 200$.
   The complementary event is $P(Y > 200) = P(Y = 201) + P(Y = 202) + P(Y = 203) + P(Y = 204) + P(Y = 205)$.
   Calculate these 5 terms:
   - $P(Y = 205) = (0.95)^{205} \approx 0.000025$
   - $P(Y = 204) = 205 \times (0.95)^{204} \times 0.05 \approx 0.000270$
   - $P(Y = 203) = \binom{205}{2} (0.95)^{203} (0.05)^2 = 20\,910 \times (0.95)^{203} \times 0.0025 \approx 0.00144$
   - $P(Y = 202) = \binom{205}{3} (0.95)^{202} (0.05)^3 \approx 0.0051$
   - $P(Y = 201) = \binom{205}{4} (0.95)^{201} (0.05)^4 \approx 0.0133$
   Sum of crisis probabilities:
   $$P(Y > 200) \approx 0.0133 + 0.0051 + 0.0014 + 0.0003 + 0.0000 = 0.0201 \approx 2.01\%.$$
2. The probability of an overbooking conflict is approximately $2.0\%$.
   The probability that boarding proceeds without incident is $1 - 0.0201 = 0.9799$, or nearly $98\%$.

#### Example 4: Sample Sizing via Bienaymé-Chebyshev
A fair coin is tossed ($p = 0.5$). Let $F_n = \frac{X}{n}$ be the observed frequency of Heads over $n$ tosses.
We require that the probability of the frequency deviating from 0.5 by more than 0.02 be strictly less than 0.05 (at most a 5% risk of error exceeding 2 hundredths).
Determine, using the concentration inequality, a sample size $n$ that guarantees this level of precision.

**Detailed Solution:**
Here $X_1 \sim \mathcal{B}(0.5)$, so $\mu = 0.5$ and $V(X_1) = p(1-p) = 0.5 \times 0.5 = 0.25$.
The tolerated margin of error is $\varepsilon = 0.02$.
By the concentration inequality applied to $M_n = F_n$:
$$P(|F_n - 0.5| \geq 0.02) \leq \frac{V(X_1)}{n \varepsilon^2} = \frac{0.25}{n \times (0.02)^2} = \frac{0.25}{n \times 0.0004} = \frac{625}{n}$$
We want this upper bound to be at most $0.05 = \frac{1}{20}$:
$$\frac{625}{n} \leq 0.05 \iff n \geq \frac{625}{0.05} = 12\,500.$$
It is therefore sufficient to perform $12\,500$ tosses to ensure, without any further distributional assumptions, that the risk of a deviation greater than 0.02 does not exceed 5%.
*(Note: Because Bienaymé-Chebyshev is universal, this bound is conservative. Using the Central Limit Theorem and the normal distribution, about 2,500 tosses would suffice).*

#### Example 5: Medical Screening Test in a Healthy Population
A rapid screening test has a false-positive rate of $1\%$ ($p = 0.01$).
A cohort of 500 healthy patients is tested. Let $X$ be the number of false positives observed.
1. Determine $E(X)$ and $V(X)$.
2. Give an upper bound for $P(|X - 5| \geq 4)$ using Bienaymé-Chebyshev.

**Detailed Solution:**
1. $X \sim \mathcal{B}(500, 0.01)$.
   - $E(X) = np = 500 \times 0.01 = 5$.
   - $V(X) = np(1-p) = 500 \times 0.01 \times 0.99 = 4.95$.
2. With expectation $E(X) = 5$, the condition $|X - 5| \geq 4$ corresponds to $\varepsilon = 4$.
   By the Bienaymé-Chebyshev inequality:
   $$P(|X - 5| \geq 4) \leq \frac{V(X)}{4^2} = \frac{4.95}{16} \approx 0.3094.$$
   The probability of observing fewer than 1 or at least 9 false positives is guaranteed to be below $31\%$.

#### Example 6: Sum of Two Independent Binomial Random Variables
Two independent production lines A and B produce machine parts.
- Line A produces 50 parts per hour, with a defect rate of $0.03$. Let $X_A$ be the number of defective parts from Line A: $X_A \sim \mathcal{B}(50, 0.03)$.
- Line B produces 70 parts per hour, with a defect rate of $0.03$. Let $X_B$ be the number of defective parts from Line B: $X_B \sim \mathcal{B}(70, 0.03)$.
Let $S = X_A + X_B$ be the total number of defective parts produced in one hour.
1. Determine the distribution of $S$.
2. Calculate $E(S)$ and $V(S)$.

**Detailed Solution:**
1. Each part from Line A undergoes a Bernoulli trial with parameter $p = 0.03$. There are 50 independent trials.
   Each part from Line B undergoes the same Bernoulli trial with parameter $p = 0.03$. There are 70 independent trials.
   Because both lines operate independently and **share the same parameter $p$**, the sum $S = X_A + X_B$ represents the total number of successes across $50 + 70 = 120$ independent Bernoulli trials with parameter $0.03$.
   Therefore:
   $$S \sim \mathcal{B}(120, 0.03)$$
   *(Crucial warning: This additivity property holds only when both distributions share the exact same success parameter $p$!)*
2. - $E(S) = np = 120 \times 0.03 = 3.6$.
   - $V(S) = np(1-p) = 120 \times 0.03 \times 0.97 = 3.492$.

---

### Key Takeaways

1. **Bernoulli Distribution $\mathcal{B}(p)$:**
   - 2 outcomes: Success ($X=1$, probability $p$), Failure ($X=0$, probability $1-p$).
   - $E(X) = p$ and $V(X) = p(1-p)$.

2. **Binomial Distribution $\mathcal{B}(n, p)$:**
   - Repetition of $n$ identical and independent Bernoulli trials.
   - Formula: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.
   - Expected Value: $E(X) = np$.
   - Variance: $V(X) = np(1-p)$; Standard Deviation: $\sigma(X) = \sqrt{np(1-p)}$.

3. **Universal Inequalities:**
   - **Markov:** If $Y \geq 0$ and $a > 0$, then $P(Y \geq a) \leq \frac{E(Y)}{a}$.
   - **Bienaymé-Chebyshev:** For any $\varepsilon > 0$, $P(|X - E(X)| \geq \varepsilon) \leq \frac{V(X)}{\varepsilon^2}$.
   - **Concentration:** For the sample mean $M_n$, $P(|M_n - \mu| \geq \varepsilon) \leq \frac{V(X_1)}{n \varepsilon^2}$.

4. **Weak Law of Large Numbers:**
   - $\lim_{n \to +\infty} P(|M_n - \mu| \geq \varepsilon) = 0$.
   - The empirical frequency converges in probability to the theoretical parameter as the number of trials tends to infinity.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 1.** Let $X \sim \mathcal{B}(6, 0.3)$.
1. Calculate $E(X)$ and $V(X)$.
2. Calculate the exact probability $P(X = 2)$.
3. Express $P(X \geq 1)$ and round its value to $10^{-4}$.
**Exercise 2.** A fair coin is tossed 8 consecutive times. Let $X$ be the number of Heads obtained.
1. What distribution does $X$ follow?
2. Calculate $P(X = 4)$.
**Exercise 3.** An archer shoots 5 arrows at a target. On each shot, the probability of hitting the bullseye is $p = 0.7$. Shots are assumed independent.
Calculate the probability that the archer hits the bullseye:
1. Exactly 5 times.
2. At least once.
**Exercise 4.** A non-negative random variable $Y \geq 0$ has $E(Y) = 12$.
Using Markov's inequality, find an upper bound for $P(Y \geq 60)$.
**Exercise 5.** A random variable $X$ has mean $E(X) = 50$ and variance $V(X) = 8$.
Using the Bienaymé-Chebyshev inequality, find an upper bound for $P(|X - 50| \geq 6)$.
**Exercise 6.** True or False? Justify your answers.
1. Tossing a coin 100 times, the probability of getting exactly 50 Heads is 0.5.
2. If $X \sim \mathcal{B}(10, 0.4)$, then $P(X \leq 9) = 1 - (0.4)^{10}$.
3. For any random variable, $P(|X - E(X)| \geq 3\sigma) \leq \frac{1}{9}$.
**Exercise 7.** An urn contains 3 white balls and 7 black balls. Four successive draws are conducted **with replacement**. Let $X$ be the number of white balls drawn.
State the distribution of $X$, its expectation, and the probability of obtaining exactly 1 white ball.

#### Level ★★ (Exploration and Examination Classics)

**Exercise 8.** A medical treatment cures a condition in $80\%$ of cases. The treatment is administered to a group of 20 independent patients. Let $X$ be the number of cured patients.
1. Calculate the probability that exactly 16 patients are cured.
2. Calculate the probability that at least 18 patients are cured.
**Exercise 9.** A fair 6-sided die is rolled $n$ times. Let $A$ be the event: “obtain at least one 6”.
What is the minimum number of rolls required so that the probability of obtaining at least one 6 is at least 0.99?
**Exercise 10.** Concentration inequality for a survey poll.
$n$ randomly selected individuals are polled to estimate the proportion $p$ in favor of a project. Let $F_n$ be the observed sample frequency.
1. Recall why $V(X_1) = p(1-p) \leq \frac{1}{4}$ for all $p \in [0, 1]$.
2. Deduce that $P(|F_n - p| \geq 0.05) \leq \frac{100}{n}$.
3. What sample size $n$ guarantees that the observed frequency does not differ from the true proportion by more than 0.05 with a risk under 1%?
**Exercise 11.** Mode of the binomial distribution.
Let $X \sim \mathcal{B}(n, p)$.
1. Show that the ratio $\frac{P(X = k+1)}{P(X = k)}$ equals $\frac{n - k}{k + 1} \frac{p}{1 - p}$.
2. Deduce the value(s) of $k$ for which $P(X = k)$ is maximized.
**Exercise 12.** A web server handles 1,000 requests per minute. The processing time for each request is an independent random variable with mean $\mu = 40\text{ ms}$ and standard deviation $\sigma = 15\text{ ms}$.
Find an upper bound for the probability that the average duration of the 1,000 requests deviates from 40 ms by more than 2 ms.
**Exercise 13.** Two independent random variables satisfy $X_1 \sim \mathcal{B}(n_1, p)$ and $X_2 \sim \mathcal{B}(n_2, p)$.
Prove algebraically, using Vandermonde's convolution formula from Chapter 53, that $X_1 + X_2 \sim \mathcal{B}(n_1 + n_2, p)$.
**Exercise 14.** Truncated geometric distribution (time to first success).
Repeated independent Bernoulli trials with parameter $p$ are conducted. Let $T$ be the index of the first success.
1. For every integer $k \geq 1$, find $P(T = k)$.
2. Calculate $P(T > k)$ directly and combinatorially.
3. Verify that $\sum_{k=1}^{+\infty} P(T = k) = 1$.
**Exercise 15.** Fluctuation of absolute deviations.
Let $X \sim \mathcal{B}(n, 0.5)$.
Prove that $P(|X - 0.5n| \geq a\sqrt{n}) \leq \frac{1}{4a^2}$. Deduce the characteristic scale of fluctuations around the mean.

#### Level ★★★ (Deepening and Advanced Competitions)

**Exercise 16.** Direct expectation derivation without indicator decomposition.
Derive the formula $E(X) = np$ for $X \sim \mathcal{B}(n, p)$ by directly evaluating the sum:
$$E(X) = \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k}$$
*(Hint: use the identity $k\binom{n}{k} = n\binom{n-1}{k-1}$ from Chapter 53).*
**Exercise 17.** Direct variance derivation via sum evaluation.
1. Evaluate the quantity $E(X(X-1)) = \sum_{k=0}^n k(k-1) \binom{n}{k} p^k (1-p)^{n-k}$.
2. Deduce $E(X^2)$, and recover $V(X) = np(1-p)$.
**Exercise 18.** Laplace's Rule of Succession.
$n$ draws with replacement from an urn have yielded $k$ successes. What is the probability that the next draw yields a success if the initial composition of the urn was completely unknown?
Show that a uniform Bayesian prior leads to Laplace's rule:
$$P(S_{n+1}) = \frac{k + 1}{n + 2}$$
Compare with the naive estimate $\frac{k}{n}$ for $k = 0$ and $k = n$.
**Exercise 19.** Cantelli's Inequality (One-sided Chebyshev).
Let $X$ be a random variable with mean 0 and variance $\sigma^2$.
Prove that for any real number $a > 0$:
$$P(X \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$$
*(Hint: for any $t > 0$, consider the variable $(X + t)^2$ and optimize over $t$).*
**Exercise 20.** Buffon's Needle and Monte Carlo Estimation.
A plane is ruled with parallel lines spaced at distance $D$. A needle of length $L \leq D$ is dropped at random onto the plane.
1. Given that the probability of crossing a line is $p = \frac{2L}{\pi D}$, explain how to estimate the mathematical constant $\pi$ by simulation.
2. If $n$ independent drops are performed, determine via the concentration inequality the number of trials needed to guarantee an accuracy of 0.01 on $\pi$ with a specified confidence level.
**Exercise 21.** Condorcet's Jury Theorem.
A jury of $n$ independent jurors ($n$ odd, $n = 2m+1$) decides guilt by majority vote. Each juror has an individual probability $p > 0.5$ of reaching the correct decision.
1. Express the probability $P_n$ that the majority of the jury reaches the correct decision.
2. Prove that $P_n > p$ and that $\lim_{n \to +\infty} P_n = 1$.
Interpret this result for democratic decision-making and trial juries.
**Exercise 22.** Almost Sure Convergence and the Strong Law of Large Numbers (Overview).
Explain the conceptual difference between the Weak Law of Large Numbers (convergence in probability: $\lim P(|M_n - \mu| \geq \varepsilon) = 0$) and the Strong Law of Émile Borel and Andrey Kolmogorov (stating that the sample path of averages converges to $\mu$ with probability 1).

---

### Solutions

**Solution 1:**
1. $E(X) = np = 6 \times 0.3 = 1.8$.
   $V(X) = np(1-p) = 6 \times 0.3 \times 0.7 = 1.26$.
2. $P(X = 2) = \binom{6}{2} (0.3)^2 (0.7)^4 = 15 \times 0.09 \times 0.2401 = 0.3241$.
3. $P(X \geq 1) = 1 - P(X = 0) = 1 - \binom{6}{0} (0.3)^0 (0.7)^6 = 1 - (0.7)^6 = 1 - 0.117649 = 0.8824$.

**Solution 2:**
1. Repetition of 8 independent Bernoulli trials with $p = 0.5$. Hence $X \sim \mathcal{B}(8, 0.5)$.
2. $P(X = 4) = \binom{8}{4} (0.5)^4 (0.5)^4 = 70 \times (0.5)^8 = \frac{70}{256} = \frac{35}{128} \approx 0.2734$.

**Solution 3:**
$X \sim \mathcal{B}(5, 0.7)$.
1. $P(X = 5) = (0.7)^5 = 0.16807$.
2. $P(X \geq 1) = 1 - P(X = 0) = 1 - (0.3)^5 = 1 - 0.00243 = 0.99757$.

**Solution 4:**
By Markov's inequality: $P(Y \geq 60) \leq \frac{E(Y)}{60} = \frac{12}{60} = \frac{1}{5} = 0.20$.

**Solution 5:**
By the Bienaymé-Chebyshev inequality: $P(|X - 50| \geq 6) \leq \frac{V(X)}{6^2} = \frac{8}{36} = \frac{2}{9} \approx 0.222$.

**Solution 6:**
1. **False.** For $n = 100$ and $p = 0.5$, $P(X = 50) = \binom{100}{50} (0.5)^{100} \approx 0.0796$ (around 8%). The mean is 50, but the probability distribution is spread over neighboring integers.
2. **True.** $P(X \leq 9) = 1 - P(X = 10) = 1 - \binom{10}{10} (0.4)^{10} (0.6)^0 = 1 - (0.4)^{10}$. The statement is therefore **True**.
3. **True.** Setting $\varepsilon = 3\sigma$, $P(|X - E(X)| \geq 3\sigma) \leq \frac{\sigma^2}{(3\sigma)^2} = \frac{1}{9}$.

**Solution 7:**
Draws with replacement: $p = \frac{3}{10} = 0.3$. $n = 4$ independent trials.
$X \sim \mathcal{B}(4, 0.3)$.
$E(X) = 4 \times 0.3 = 1.2$.
$P(X = 1) = \binom{4}{1} (0.3)^1 (0.7)^3 = 4 \times 0.3 \times 0.343 = 0.4116$.

**Solution 8:**
$X \sim \mathcal{B}(20, 0.8)$.
1. $P(X = 16) = \binom{20}{16} (0.8)^{16} (0.2)^4 = 4\,845 \times (0.8)^{16} \times (0.2)^4 \approx 0.2182$.
2. $P(X \geq 18) = P(X = 18) + P(X = 19) + P(X = 20)$.
   - $P(X = 18) = \binom{20}{18} (0.8)^{18} (0.2)^2 = 190 \times (0.8)^{18} \times 0.04 \approx 0.1369$
   - $P(X = 19) = 20 \times (0.8)^{19} \times 0.2 \approx 0.0576$
   - $P(X = 20) = (0.8)^{20} \approx 0.0115$
   Total: $P(X \geq 18) \approx 0.1369 + 0.0576 + 0.0115 = 0.2060 \quad (\approx 20.6\%)$.

**Solution 9:**
The probability of obtaining no 6s in $n$ rolls is $(5/6)^n$.
We require $P(A) = 1 - (5/6)^n \geq 0.99 \iff (5/6)^n \leq 0.01$.
Taking natural logarithms (noting $\ln(5/6) < 0$, which flips the inequality):
$n \ln(5/6) \leq \ln(0.01) \iff n \geq \frac{\ln(0.01)}{\ln(5/6)} \approx \frac{-4.60517}{-0.18232} \approx 25.26$.
A minimum of **26 rolls** is required.

**Solution 10:**
1. For $f(p) = p(1-p) = p - p^2$, the derivative $f'(p) = 1 - 2p$ vanishes at $p = 0.5$, attaining its maximum $f(0.5) = 0.25 = \frac{1}{4}$.
2. By the concentration inequality with $\varepsilon = 0.05$:
   $P(|F_n - p| \geq 0.05) \leq \frac{V(X_1)}{n (0.05)^2} \leq \frac{0.25}{n \times 0.0025} = \frac{100}{n}$.
3. We require $\frac{100}{n} \leq 0.01 \iff n \geq \frac{100}{0.01} = 10\,000$. A sample size of 10,000 individuals guarantees this result.

**Solution 11:**
1. $\frac{P(X = k+1)}{P(X = k)} = \frac{\frac{n!}{(k+1)!(n-k-1)!} p^{k+1} (1-p)^{n-k-1}}{\frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}} = \frac{n-k}{k+1} \frac{p}{1-p}$.
2. This ratio is $\geq 1$ as long as $(n-k)p \geq (k+1)(1-p) \iff np - kp \geq k - kp + 1 - p \iff np + p - 1 \geq k \iff k \leq (n+1)p - 1$.
   The sequence of probabilities is initially increasing, then decreasing. The maximum (mode) is achieved at integer $k = \lfloor (n+1)p \rfloor$.

**Solution 12:**
For $n = 1000$ requests, the sample mean duration $M_n$ has mean $\mu = 40$ and variance $V(M_n) = \frac{\sigma^2}{n} = \frac{15^2}{1000} = \frac{225}{1000} = 0.225$.
By Bienaymé-Chebyshev with $\varepsilon = 2$:
$P(|M_n - 40| \geq 2) \leq \frac{V(M_n)}{2^2} = \frac{0.225}{4} = 0.05625$ (less than $5.6\%$).

**Solution 13:**
For any $k \in \{0, \dots, n_1+n_2\}$, the event $(X_1 + X_2 = k)$ is the disjoint union of events $(X_1 = j \text{ and } X_2 = k-j)$ for $j \in \{0, \dots, k\}$.
By independence:
$$P(X_1+X_2=k) = \sum_{j=0}^k \binom{n_1}{j} p^j (1-p)^{n_1-j} \binom{n_2}{k-j} p^{k-j} (1-p)^{n_2-(k-j)} = p^k (1-p)^{n_1+n_2-k} \sum_{j=0}^k \binom{n_1}{j}\binom{n_2}{k-j}$$
By Vandermonde's identity, the sum equals $\binom{n_1+n_2}{k}$.
We recognize the formula for $\mathcal{B}(n_1+n_2, p)$.

**Solution 14:**
1. $T = k$ means $k-1$ consecutive failures followed by a success: $P(T = k) = (1-p)^{k-1} p$.
2. $T > k$ means that the first $k$ trials were all failures: $P(T > k) = (1-p)^k$.
3. $\sum_{k=1}^{+\infty} p (1-p)^{k-1} = p \sum_{j=0}^{+\infty} (1-p)^j = p \frac{1}{1 - (1-p)} = \frac{p}{p} = 1$.

**Solution 15:**
For $X \sim \mathcal{B}(n, 0.5)$, $E(X) = 0.5n$ and $V(X) = 0.25n$.
Apply Bienaymé-Chebyshev with $\varepsilon = a\sqrt{n}$:
$P(|X - 0.5n| \geq a\sqrt{n}) \leq \frac{V(X)}{(a\sqrt{n})^2} = \frac{0.25n}{a^2 n} = \frac{1}{4a^2}$.
The characteristic scale of deviations between the number of successes and the expected value is thus of order $\sqrt{n}$.

**Solution 16:**
$E(X) = \sum_{k=1}^n k \binom{n}{k} p^k (1-p)^{n-k}$.
Using $k\binom{n}{k} = n\binom{n-1}{k-1}$:
$$E(X) = \sum_{k=1}^n n \binom{n-1}{k-1} p \cdot p^{k-1} (1-p)^{(n-1)-(k-1)} = np \sum_{j=0}^{n-1} \binom{n-1}{j} p^j (1-p)^{n-1-j} = np (p + (1-p))^{n-1} = np.$$

**Solution 17:**
1. $k(k-1)\binom{n}{k} = k(k-1)\frac{n!}{k!(n-k)!} = \frac{n!}{(k-2)!(n-k)!} = n(n-1)\binom{n-2}{k-2}$.
   Summing for $k \geq 2$:
   $E(X(X-1)) = n(n-1)p^2 \sum_{j=0}^{n-2} \binom{n-2}{j} p^j (1-p)^{n-2-j} = n(n-1)p^2$.
2. $E(X^2) = E(X(X-1)) + E(X) = n(n-1)p^2 + np = n^2 p^2 - np^2 + np$.
   $V(X) = E(X^2) - (E(X))^2 = (n^2 p^2 - np^2 + np) - (np)^2 = np(1-p)$.

**Solution 18:**
Under a uniform prior distribution on the unknown parameter $p \in [0, 1]$, the posterior conditional probability is given via the Beta function:
$P(S_{n+1} \mid k \text{ successes out of } n) = \frac{\int_0^1 p \cdot p^k (1-p)^{n-k} dp}{\int_0^1 p^k (1-p)^{n-k} dp} = \frac{B(k+2, n-k+1)}{B(k+1, n-k+1)} = \frac{k+1}{n+2}$.
For $k = 0$ (zero successes in 10 trials), the naive frequency estimate is 0, whereas Laplace gives $\frac{1}{12} \approx 8.3\%$, avoiding the pitfall of declaring an unobserved event impossible.

**Solution 19:**
For any $t > 0$, the event $X \geq a$ is equivalent to $X + t \geq a + t$, which implies $(X + t)^2 \geq (a + t)^2$.
Applying Markov's inequality to $(X+t)^2 \geq 0$:
$P(X \geq a) \leq \frac{E((X+t)^2)}{(a+t)^2} = \frac{E(X^2) + 2tE(X) + t^2}{(a+t)^2} = \frac{\sigma^2 + t^2}{(a+t)^2}$.
Minimizing this function with respect to $t > 0$, setting the derivative to zero yields $t = \frac{\sigma^2}{a}$.
Substituting this optimal choice produces $P(X \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$.

**Solution 20:**
1. Dropping $n$ needles and recording $X$ intersections, the frequency $F_n = \frac{X}{n}$ converges to $p = \frac{2L}{\pi D}$. An estimator for $\pi$ is therefore $\hat{\pi}_n = \frac{2L}{D \cdot F_n}$.
2. By the concentration inequality, since $V(X_1) \leq 1/4$, the variance of the frequency is bounded by $\frac{1}{4n}$. To achieve a given precision on $p$, solving $\frac{1}{4n\varepsilon^2} \leq \alpha$ yields the required finite number of drops $n$.

**Solution 21:**
1. A majority is achieved when $k \geq m+1 = \frac{n+1}{2}$. Thus $P_n = \sum_{k=m+1}^n \binom{n}{k} p^k (1-p)^{n-k}$.
2. By the Law of Large Numbers, as $n \to +\infty$, the fraction of correct votes converges to $p > 0.5$. The probability of a correct majority vote approaches 1. This theorem provides a mathematical foundation for collective decision-making: a large assembly of fallible yet moderately enlightened voters ($p > 0.5$) reaches an optimal verdict by majority rule.

**Solution 22:**
The Weak Law asserts that for a fixed arbitrarily large sample size $n$, the probability of a deviation is vanishingly small. The Strong Law guarantees an infinitely stronger statement: with probability 1, the entire infinite trajectory of averages $(M_n)_{n \geq 1}$ converges to $\mu$, ruling out any infinite recurrence of rogue deviations.

---

### The Question That Opens the Next Step

We have seen how statistical laws govern the empirical reality of coin tosses and sample surveys.
What happens when algebra itself hits an impenetrable wall?
Recall the equation $x^2 = -1$: no real number, no tally of pebbles, no probability can possess a negative square.
Yet in 16th-century Italy, while seeking formulas to solve ordinary cubic equations with obvious integer roots, algebraists were compelled to imagine a ghostly phantom number. A number capable of pivoting the coordinate plane by a ninety-degree right angle.
Welcome to the fascinating world of complex numbers: turn the page to discover **Chapter 55 and The Right-Angled Whirlwind**.
