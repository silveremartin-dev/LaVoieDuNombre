# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 42: The Physician, the Test and the Tree of Possibilities

> *“Common sense in the presence of randomness is a blind traveler stumbling in the dark. When a medical test advertised as 99% reliable declares you diseased, panic shrieks that you are 99% doomed. The mathematician breathes calmly, draws a tree in the space of possibilities, narrows the sample space, and reveals that you have a nine-in-ten chance of being perfectly healthy.”*

---

### What You Are About to Discover

- The medical test paradox: how a nearly infallible test can yield a vast majority of false positives for a rare disease.
- The revolutionary concept of **conditional probability**: how new information **narrows the universe of possibilities**.
- The laws of the **probability tree**: the product rule along branches and the sum of paths.
- The **law of total probability**: partitioning sample space into mutually exclusive slices to determine the unknown.
- The celebrated theorem of Reverend **Thomas Bayes** for reasoning backward from effects to causes.
- The vital distinction between **independent** events and **mutually exclusive** (disjoint) events.
- **Discrete random variables**: assigning a numeric payout or score to each random outcome.
- **Expected value** $E(X)$: long-run average gain and the fair price of a lottery ticket.
- **Variance** $V(X)$, **standard deviation** $\sigma(X)$, and the **linearity of expectation**: $E(aX + b) = aE(X) + b$.

---

### 1. The Problem: Thomas's Nightmare in the Doctor's Office

Thomas is seventeen years old. To compete in high school athletics, his physician administers a routine blood screening test for a rare but dangerous congenital heart condition that affects **1 in 1,000 individuals** across the general population.

Three days later, the phone rings. The doctor’s tone is heavy:
*“Thomas, your blood test came back positive.”*

Thomas feels the floor give way beneath him. With a trembling voice, he asks:
*“Doctor, how reliable is this test?”*
The physician consults the laboratory specification sheet:
*“The test boasts an exceptional reliability rating of **99%**:*
- *If a person has the condition, the test registers positive 99% of the time (sensitivity).*
- *If a person is healthy, the test registers negative 99% of the time (specificity).”*

Thomas slumps into his chair, overwhelmed:
*“The test is 99% accurate. My test came back positive. Therefore, I have a 99% chance of having this heart defect!”*

Is Thomas right to panic?
The verdict of mathematics is clear, dramatic, and will upend your intuition:
**NO! Thomas actually faces less than a 10% chance of having the disease!**
He has more than a **90% chance of being in perfect health**!

How can this be? How can a medical diagnostic tool with 99% laboratory precision be wrong nine times out of ten when it announces a disease?

---

### 2. Narrowing the Universe: Conditional Probability

To see through this paradox without dense symbolism, consider a concrete, representative cohort of **100,000 individuals**:

```
                                 TOTAL POPULATION
                                100,000 individuals
                                  /              \
                                 /                \
                     1 in 1,000 /                  \  999 in 1,000
                               /                    \
                         DISEASED                  HEALTHY
                      100 individuals          99,900 individuals
                       /          \               /          \
               99%    /            \ 1%    1%    /            \ 99%
                     /              \           /              \
                 POSITIVE       NEGATIVE    POSITIVE       NEGATIVE
                99 diseased    1 diseased  999 healthy  98,901 healthy
```

Trace the arithmetic carefully:
1. Among 100,000 people, because the condition strikes 1 in 1,000, there are **100 diseased individuals** and **99,900 healthy individuals**.
2. Among the 100 diseased patients: the test detects 99% of them: there are **99 positive tests** (and 1 false negative).
3. Now inspect the **99,900 healthy individuals**:
   The test is 99% specific, which means it misclassifies 1% of them.
   1% of 99,900 yields exactly **999 healthy individuals falsely flagged as positive** (false positives)!

Now step into Thomas's shoes:
The physician informed him that his test is positive. Thomas’s relevant reference frame has suddenly **shrunk**: Thomas is no longer an arbitrary member of the 100,000 general public; he belongs exclusively to the select club of individuals who received a **positive test result**!

How many total positive individuals exist in the clinic's waiting room?
$$\text{Total Positives} = 99 \text{ (diseased)} + 999 \text{ (healthy)} = \mathbf{1,098 \text{ people}}.$$

And among these 1,098 individuals testing positive, how many actually carry the disease?
Only **99 individuals**!

The probability that Thomas is genuinely ill given that his test is positive is therefore:

$$P(\text{Diseased} \mid \text{Positive}) = \frac{99}{1,098} \approx \mathbf{0.0902} = \mathbf{9.02\%}.$$

More than **91% of those who test positive are completely disease-free**!
Why? Because the disease is so exceedingly rare that the tiny 1% false-positive rate applied to the massive ocean of healthy people creates ten times more false alarms than genuine cases!

---

### 3. The Formal Theory: Conditional Probability

#### 3.1 Formal Definition

Let $\Omega$ be a sample space endowed with a probability measure $P$. Let $A$ and $B$ be two events.

> **📐 Definition — Conditional Probability**
> Let $A$ be an event with non-zero probability ($P(A) > 0$).
> The **conditional probability of $B$ given $A$**, denoted $P_A(B)$ or $P(B \mid A)$, is defined by:
>
> $$\boxed{P(B \mid A) = \frac{P(A \cap B)}{P(A)}}$$
>
> Read aloud as: “**probability of B given A**”.

**Geometric Interpretation:**
We replace the universal reference sample space $\Omega$ (which had total probability 1) with the restricted subspace $A$. The event $A$ becomes the new universe. The fraction of $B$ that survives inside this restricted frame is the intersection $A \cap B$, normalized by the measure of $A$.

```
     ┌───────────────────────────────────┐
     │  Sample Space Ω                   │
     │        ┌──────────────┐           │
     │        │ A            │           │
     │        │     ┌────────┼──────┐    │
     │        │     │ A ∩ B  │  B   │    │
     │        │     └────────┼──────┘    │
     │        └──────────────┘           │
     └───────────────────────────────────┘
     The universe is restricted to bubble A: P(B|A) = Area(A ∩ B) / Area(A)
```

#### 3.2 The Multiplication Rule

Multiplying by $P(A)$ yields the fundamental product identity:

> **📐 Theorem — Multiplication Rule**
> For any events $A$ and $B$ with $P(A) > 0$:
>
> $$\boxed{P(A \cap B) = P(A) \times P(B \mid A)}$$

---

### 4. Probability Trees and the Law of Total Probability

#### 4.1 The Golden Rules of Tree Diagrams

A probability tree organizes successive sequential stages of a random experiment with clarity.

```
                  P(B|A)
               .────────► B     ──► Path A ∩ B: P(A ∩ B) = P(A) × P(B|A)
         P(A) /
        .─────► A
       /      \
      /        '────────► B̄     ──► Path A ∩ B̄: P(A ∩ B̄) = P(A) × P(B̄|A)
     o        P(B̄|A)
      \
       \      .────────► B     ──► Path Ā ∩ B: P(Ā ∩ B) = P(Ā) × P(B|Ā)
        '─────► Ā
         P(Ā) \
               '────────► B̄     ──► Path Ā ∩ B̄: P(Ā ∩ B̄) = P(Ā) × P(B̄|Ā)
                  P(B̄|Ā)
```

> **📐 Rules of Probability Trees**
> 1. **Node Rule:** The sum of probabilities on all branches emanating from any single node **always equals 1**.
>    $$P(A) + P(\overline{A}) = 1, \qquad P(B \mid A) + P(\overline{B} \mid A) = 1.$$
> 2. **Path Rule (Multiplication):** The probability of any complete path from root to leaf is the **product** of the probabilities along its branches.
> 3. **Leaf Rule (Addition):** The total probability of an outcome is the **sum** of the path probabilities that terminate at that outcome.

#### 4.2 The Law of Total Probability

> **📐 Definition — Partition of a Sample Space**
> A family of events $A_1, A_2, \dots, A_n$ forms a **partition** of $\Omega$ if:
> - They are pairwise disjoint ($A_i \cap A_j = \varnothing$ for $i \neq j$);
> - Their union covers the entire sample space ($A_1 \cup A_2 \cup \dots \cup A_n = \Omega$);
> - None of them is impossible ($P(A_i) > 0$).
>
> The most frequent partition is the elementary binary partition $\{A, \overline{A}\}$.

> **📐 Theorem — Law of Total Probability**
> If $A_1, A_2, \dots, A_n$ form a partition of $\Omega$, then for any event $B$:
>
> $$\boxed{P(B) = \sum_{i=1}^n P(B \cap A_i) = \sum_{i=1}^n P(A_i) \times P(B \mid A_i)}$$
>
> In the two-event case $\{A, \overline{A}\}$:
> $$\boxed{P(B) = P(A) \times P(B \mid A) + P(\overline{A}) \times P(B \mid \overline{A})}$$

---

### 5. Bayes' Theorem: Reasoning Backward from Effects to Causes

In 1763, the British Presbyterian minister and mathematician **Thomas Bayes** published a posthumous essay that reshaped the philosophy of knowledge. He asked: *“Given that an observed effect has occurred (the test is positive), what is the probability that a specific underlying cause generated it (the patient is truly diseased)?”*

> **📐 Theorem — Bayes' Theorem**
> Let $\{A, \overline{A}\}$ partition the sample space and let $B$ have non-zero probability.
>
> $$\boxed{P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \times P(B \mid A)}{P(A) \times P(B \mid A) + P(\overline{A}) \times P(B \mid \overline{A})}}$$

Applying Bayes' formula to Thomas's scenario:
- Underlying cause $M$: “has the condition”, $P(M) = 0.001 \implies P(\overline{M}) = 0.999$.
- Observed effect $T$: “positive test result”.
  - Sensitivity: $P(T \mid M) = 0.99$.
  - False positive rate: $P(T \mid \overline{M}) = 1 - 0.99 = 0.01$.
- Total probability of testing positive:
  $$P(T) = P(M)P(T \mid M) + P(\overline{M})P(T \mid \overline{M}) = (0.001 \times 0.99) + (0.999 \times 0.01)$$
  $$= 0.00099 + 0.00999 = 0.01098.$$
- Posterior probability of disease given a positive test:
  $$P(M \mid T) = \frac{P(M \cap T)}{P(T)} = \frac{0.00099}{0.01098} = \frac{99}{1098} \approx \mathbf{9.02\%}.$$
The algebraic formula matches our tabular calculation point for point!

---

### 6. Independence: Randomness Without Memory

When two events exert no causal or probabilistic influence on one another, learning that one has occurred provides zero information about the likelihood of the other.

> **📐 Definition — Independent Events**
> Two events $A$ and $B$ are **independent** if and only if:
>
> $$\boxed{P(A \cap B) = P(A) \times P(B)}$$
>
> If $P(A) > 0$, this is equivalent to:
> $$P(B \mid A) = P(B).$$

> **⚠️ Caution: The Ultimate Trap! — Never Conflate “Independent” and “Disjoint”**
> This is the single most common conceptual error in probability!
> - Two events are **disjoint** (mutually exclusive) if they cannot happen at the same time: $A \cap B = \varnothing$, so $P(A \cap B) = 0$.
> - Two events are **independent** if the occurrence of one does not alter the likelihood of the other: $P(A \cap B) = P(A) \times P(B)$.
>
> Two non-impossible events that are disjoint are **NEVER independent**! On the contrary, they are maximally dependent: if $A$ occurs, you know with 100% certainty that $B$ did not occur ($P(B \mid A) = 0 \neq P(B)$)!

---

### 7. Discrete Random Variables

Until now, random outcomes were qualitative categories: “heads”, “tails”, “sick”, “red card”.
A **random variable** bridges probability to arithmetic: it attaches a **real number** (a monetary gain, an arrival count, a waiting time) to every elementary outcome.

> **📐 Definition — Discrete Random Variable**
> A **discrete random variable** $X$ defined on a sample space $\Omega$ is a function that maps every elementary outcome $\omega \in \Omega$ to a real number $x_i \in \mathbb{R}$.
> We write $X(\Omega) = \{x_1, x_2, \dots, x_k\}$ for the set of values $X$ can take.

#### 7.1 Probability Distribution

Specifying the **probability distribution** of $X$ means determining the probability $P(X = x_i)$ for each possible value $x_i$, presented as a distribution table:

| $x_i$ | $x_1$ | $x_2$ | $\dots$ | $x_k$ | **Total** |
|---|---|---|---|---|---|
| $P(X = x_i)$ | $p_1$ | $p_2$ | $\dots$ | $p_k$ | **1** |

The sum of all probabilities must strictly equal 1: $\sum_{i=1}^k p_i = 1$.

#### 7.2 Expected Value: The Fair Price of a Game

Imagine a carnival lottery: what can you expect to win on average per ticket if you play millions of games?

> **📐 Definition — Expected Value**
> The **expected value** (or expectation) of a discrete random variable $X$, denoted $E(X)$, is the weighted average of the values taken by $X$:
>
> $$\boxed{E(X) = \sum_{i=1}^k x_i \cdot P(X = x_i)}$$

- If $X$ represents a player's net profit (payout minus ticket cost):
  - $E(X) > 0$: the game is **in the player's favor**.
  - $E(X) < 0$: the game is **unfavorable to the player** (the mathematical reality of all commercial casinos and state lotteries!).
  - $E(X) = 0$: the game is **fair**.

#### 7.3 Variance and Standard Deviation of a Random Variable

Just as in Chapter 41 for descriptive statistics, we measure uncertainty and dispersion around the mean:

> **📐 Definition — Variance and Standard Deviation**
> - The **variance** of $X$ is:
>   $$\boxed{V(X) = E\big((X - E(X))^2\big) = \sum_{i=1}^k (x_i - E(X))^2 P(X = x_i)}$$
> - Probabilistic König-Huygens identity:
>   $$\boxed{V(X) = E(X^2) - \big(E(X)\big)^2}$$
> - The **standard deviation** is:
>   $$\boxed{\sigma(X) = \sqrt{V(X)}}$$

#### 7.4 Linearity of Expectation

> **📐 Theorem — Affine Transformation of a Random Variable**
> For all real numbers $a$ and $b$:
>
> 1. $\boxed{E(aX + b) = aE(X) + b}$  (Linearity of Expectation)
> 2. $\boxed{V(aX + b) = a^2 V(X)}$
> 3. $\boxed{\sigma(aX + b) = |a|\sigma(X)}$

> **✍️ Proof of Linearity**
> $$E(aX + b) = \sum_{i=1}^k (a x_i + b) p_i = \sum_{i=1}^k a x_i p_i + \sum_{i=1}^k b p_i = a \sum_{i=1}^k x_i p_i + b \sum_{i=1}^k p_i.$$
> Since $\sum x_i p_i = E(X)$ and $\sum p_i = 1$:
> $$E(aX + b) = aE(X) + b(1) = aE(X) + b. \quad \blacksquare$$

---

### Step-by-Step Worked Examples

> **✅ Worked Example 1 — Direct Conditional Probability**
> In a class of 32 students, 18 study Spanish, 10 study German, and 6 study both languages.
> A student is chosen at random.
> 1. What is the probability that the student studies German?
> 2. Given that the chosen student studies Spanish, what is the probability that they also study German?
>
> **Detailed Solution:**
> Let $S$ denote “studies Spanish” and $G$ denote “studies German”.
> $P(S) = \frac{18}{32}$, $P(G) = \frac{10}{32}$, and $P(S \cap G) = \frac{6}{32}$.
> 1. $P(G) = \frac{10}{32} = \frac{5}{16} = 0.3125$.
> 2. We seek $P(G \mid S)$ (sample space restricted to Spanish students):
>    $$P(G \mid S) = \frac{P(S \cap G)}{P(S)} = \frac{6/32}{18/32} = \frac{6}{18} = \frac{1}{3} \approx 0.333.$$

> **✅ Worked Example 2 — Tree Diagram and Law of Total Probability**
> A company sources microchips from two suppliers:
> - Supplier $A$ provides 70% of the inventory, with a 2% defect rate.
> - Supplier $B$ provides the remaining 30%, with a 5% defect rate.
> A chip is chosen at random from inventory.
> 1. Construct the tree diagram.
> 2. Find the probability that the chip is defective.
> 3. If a selected chip is found to be defective, what is the probability it came from Supplier $B$?
>
> **Detailed Solution:**
> 1. Data: $P(A) = 0.70$, $P(B) = 0.30$.
>    $P(D \mid A) = 0.02$, $P(D \mid B) = 0.05$.
> 2. By the law of total probability with partition $\{A, B\}$:
>    $$P(D) = P(A \cap D) + P(B \cap D) = P(A)P(D \mid A) + P(B)P(D \mid B)$$
>    $$P(D) = (0.70 \times 0.02) + (0.30 \times 0.05) = 0.014 + 0.015 = 0.029 = 2.9\%.$$
> 3. By Bayes' theorem, find $P(B \mid D)$:
>    $$P(B \mid D) = \frac{P(B \cap D)}{P(D)} = \frac{0.015}{0.029} = \frac{15}{29} \approx 0.5172 = 51.7\%.$$
>    Even though Supplier $B$ delivers only 30% of total volume, it accounts for more than half of all defective parts!

> **✅ Worked Example 3 — Testing for Independence**
> Two standard fair 6-sided dice are rolled, one red and one blue.
> Let $A$ be: “the red die shows 4” and $B$ be: “the sum of the two dice is 7”.
> Are events $A$ and $B$ independent?
>
> **Detailed Solution:**
> There are $6 \times 6 = 36$ equally likely outcomes.
> - For $A$: 6 outcomes $(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)$, so $P(A) = \frac{6}{36} = \frac{1}{6}$.
> - For $B$: sums of 7 are $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$, giving 6 outcomes. Thus $P(B) = \frac{6}{36} = \frac{1}{6}$.
> - For $A \cap B$: only one outcome has red die 4 and sum 7: namely $(4, 3)$.
>   Thus $P(A \cap B) = \frac{1}{36}$.
> - Compare with the product:
>   $P(A) \times P(B) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.
> - Since $P(A \cap B) = P(A) \times P(B)$, **events $A$ and $B$ are strictly independent**!
>   Knowing that the red die rolled a 4 provides zero information regarding whether the sum will equal 7.

> **✅ Worked Example 4 — Random Variable and Game Expectation**
> A carnival stall offers the following game for an entry stake of \$5:
> A fair 6-sided die is rolled:
> - Roll a 6: receive \$20 (net profit: +\$15).
> - Roll a 4 or 5: receive \$6 (net profit: +\$1).
> - Roll a 1, 2, or 3: receive \$0 (net loss: -\$5).
> 1. Define the random variable $X$ representing the player's net gain and specify its probability distribution.
> 2. Compute the expected value. Who has the mathematical edge?
>
> **Detailed Solution:**
> 1. Values taken by $X$: $X(\Omega) = \{-5, 1, 15\}$.
>    - $P(X = 15) = P(\{6\}) = \frac{1}{6}$
>    - $P(X = 1) = P(\{4, 5\}) = \frac{2}{6} = \frac{1}{3}$
>    - $P(X = -5) = P(\{1, 2, 3\}) = \frac{3}{6} = \frac{1}{2}$
>    Check: $\frac{1}{6} + \frac{2}{6} + \frac{3}{6} = 1$.
>
> 2. Expected value:
>    $$E(X) = \left(-5 \times \frac{3}{6}\right) + \left(1 \times \frac{2}{6}\right) + \left(15 \times \frac{1}{6}\right) = \frac{-15 + 2 + 15}{6} = \frac{2}{6} = +\frac{1}{3} \approx +\$0.33.$$
>    Since $E(X) > 0$, the game is **favorable to the player**! On average, players win 33 cents per round. The stall operator will soon face bankruptcy unless the rules are revised!

> **✅ Worked Example 5 — Variance and Standard Deviation of a Random Variable**
> Compute the variance $V(X)$ and standard deviation $\sigma(X)$ for the game in Example 4.
>
> **Detailed Solution:**
> 1. Compute $E(X^2)$:
>    $$E(X^2) = (-5)^2 \times \frac{3}{6} + (1)^2 \times \frac{2}{6} + (15)^2 \times \frac{1}{6}$$
>    $$= 25 \times \frac{3}{6} + 1 \times \frac{2}{6} + 225 \times \frac{1}{6} = \frac{75 + 2 + 225}{6} = \frac{302}{6} = \frac{151}{3} \approx 50.33.$$
> 2. König-Huygens identity:
>    $$V(X) = E(X^2) - (E(X))^2 = \frac{151}{3} - \left(\frac{1}{3}\right)^2 = \frac{453}{9} - \frac{1}{9} = \frac{452}{9} \approx 50.22.$$
> 3. Standard deviation:
>    $$\sigma(X) = \sqrt{\frac{452}{9}} = \frac{\sqrt{452}}{3} \approx \$7.09.$$
>    The standard deviation is high: earnings fluctuate substantially around the mean.

> **✅ Worked Example 6 — Linearity of Expectation**
> An insurance provider insures a citywide fleet of shared bicycles. The daily number of bicycle accidents $X$ has expected value $E(X) = 4$ and standard deviation $\sigma(X) = 1.5$.
> Each accident costs \$50 in repairs, plus a fixed daily maintenance overhead of \$100.
> The total daily cost is therefore $Y = 50X + 100$.
> Determine the expected value and standard deviation of the daily cost.
>
> **Detailed Solution:**
> - Expectation: by linearity:
>   $$E(Y) = E(50X + 100) = 50E(X) + 100 = 50(4) + 100 = 200 + 100 = \$300.$$
> - Standard deviation:
>   $$\sigma(Y) = \sigma(50X + 100) = |50| \times \sigma(X) = 50 \times 1.5 = \$75.$$
> The insurer must budget an average of \$300 per day, with typical day-to-day fluctuations of \$75.

---

### What You Must Remember

1. **Conditional Probability:**
   - $P(B \mid A) = \frac{P(A \cap B)}{P(A)}$ (sample space restricted to $A$).
   - Product rule: $P(A \cap B) = P(A) \times P(B \mid A)$.

2. **Probability Trees and Law of Total Probability:**
   - Sum of branches leaving any node equals 1.
   - Path probability = product along branches.
   - Law of total probability: $P(B) = P(A)P(B \mid A) + P(\overline{A})P(B \mid \overline{A})$.

3. **Bayes' Theorem (Inverting Conditions):**
   - $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)P(B \mid A)}{P(A)P(B \mid A) + P(\overline{A})P(B \mid \overline{A})}$.

4. **Independence:**
   - $A$ and $B$ are independent $\iff P(A \cap B) = P(A) \times P(B) \iff P(B \mid A) = P(B)$.
   - Mutually exclusive (disjoint) non-null events are never independent.

5. **Random Variables:**
   - Expected value: $E(X) = \sum x_i p_i$. Linearity: $E(aX+b) = aE(X)+b$.
   - Variance: $V(X) = E(X^2) - (E(X))^2$. Scaling: $V(aX+b) = a^2 V(X)$.
   - Standard deviation: $\sigma(X) = \sqrt{V(X)}$. Scaling: $\sigma(aX+b) = |a|\sigma(X)$.

---

### Exercises

#### Level ★ (Direct Applications, Basic Trees)

1. Given $P(A) = 0.4$, $P(B) = 0.5$, and $P(A \cap B) = 0.2$.
   Compute $P(B \mid A)$ and $P(A \mid B)$. Are $A$ and $B$ independent?
2. Given $P(A) = 0.6$ and $P(B \mid A) = 0.3$. Compute $P(A \cap B)$.
3. In a tree diagram, a branch leading to $A$ has probability $0.7$. From $A$, two branches lead to $B$ and $\overline{B}$. Given $P(B \mid A) = 0.4$, determine $P(\overline{B} \mid A)$.
4. A card is drawn at random from a standard 32-card deck. Let $K$ be “the card is a King” and $H$ be “the card is a Heart”. Are $K$ and $H$ independent?
5. A random variable $X$ has distribution:
   | $x_i$ | -2 | 0 | 3 |
   |---|---|---|---|
   | $P(X=x_i)$ | 0.3 | 0.5 | $p$ |
   Determine $p$, then calculate $E(X)$.
6. Given $E(X) = 5$ and $V(X) = 4$. Let $Y = 3X - 2$. Find $E(Y)$, $V(Y)$, and $\sigma(Y)$.
7. A bag holds 3 white balls and 2 black balls. Two balls are drawn successively without replacement. Find the probability of drawing two white balls.
8. A multiple-choice question offers 4 options with only one correct answer. A student guesses randomly. What is the probability of answering correctly given that they have already eliminated two incorrect choices?

#### Level ★★ (Complete Trees, Bayes, and Random Variables)

9. In a textile factory, three machines $M_1, M_2, M_3$ produce 50%, 30%, and 20% of the garments, respectively.
   Defect rates are 3% for $M_1$, 4% for $M_2$, and 5% for $M_3$.
   a) Calculate the probability that a randomly chosen garment is defective.
   b) Given that a garment is defective, what is the probability it was produced by machine $M_1$?
10. Prove that if $A$ and $B$ are independent events, then $A$ and $\overline{B}$ are also independent.
11. A fair coin is tossed 3 times. Let $X$ denote the number of Heads obtained.
    a) Determine the support of $X$ and tabulate its probability distribution.
    b) Compute $E(X)$ and $V(X)$.
12. A carnival game costs \$2 to play. A fair 6-sided die is rolled:
    - Even outcome: win \$3 (net profit: +\$1).
    - Outcome 5: win \$6 (net profit: +\$4).
    - Otherwise: win nothing (net profit: -\$2).
    Is the game fair?
13. Two dice are rolled. Let $A$ be: “the first die is even” and $B$ be: “the sum of the two dice is odd”.
    Show that $A$ and $B$ are independent.
14. In a population, 60% are vaccinated against the flu. The vaccine has an 80% efficacy rate (vaccinated individuals are five times less likely to contract the flu). The infection rate among the unvaccinated is 25%.
    a) Compute the overall infection rate in the general population.
    b) Given that an individual contracts the flu, what is the probability that they were vaccinated?
15. A random variable $X$ satisfies $E(X) = 10$ and $E(X^2) = 116$.
    Compute $V(X)$ and $\sigma(X)$.
16. Python Simulation: Write a script to simulate 10,000 rounds of the game in Exercise 12, computing the empirical mean payoff to corroborate the theoretical expected value.

#### Level ★★★ (Challenges and Open Problems)

17. **The Two-Child Paradox (Lewis Carroll / Martin Gardner):**
    A family has two children. Assume each child is independently equally likely to be a boy or a girl.
    a) Given that the elder child is a girl, what is the probability that both children are girls?
    b) Given that at least one of the children is a girl, what is the probability that both children are girls? Explain the apparent paradox.
18. **The Monty Hall Problem (The Three Doors Game Show):**
    On a game show, three closed doors $A, B, C$ stand before you. Behind one is a sports car; behind the other two, goats.
    1. You choose Door $A$.
    2. The host, who knows what is behind each door, opens one of the remaining doors (say Door $B$), revealing a goat.
    3. He offers: *“Do you wish to stick with Door $A$, or switch to Door $C$?”*
    Using conditional probabilities, rigorously demonstrate why switching doors doubles your chance of winning!
19. **Gambler's Ruin:**
    A player begins with \$2 and plays coin tosses against the house using a fair coin. Each round, he wins \$1 with probability 0.5 or loses \$1 with probability 0.5. The game halts if he reaches \$4 (victory) or \$0 (ruin).
    Find the probability of ruin by formulating a system of recurrence equations on conditional probabilities.
20. **Truncated Geometric Distribution:**
    A fair 6-sided die is rolled until a 6 appears, with a maximum cap of 4 rolls. Let $X$ be the number of rolls performed.
    a) Give the probability distribution of $X$.
    b) Compute the expected value $E(X)$.

---

### Solutions

**1.** $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{0.2}{0.4} = 0.5$.
$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.2}{0.5} = 0.4$.
$P(A) \times P(B) = 0.4 \times 0.5 = 0.2 = P(A \cap B)$. Yes, the events are independent!

**2.** $P(A \cap B) = P(A) \times P(B \mid A) = 0.6 \times 0.3 = 0.18$.

**3.** Branches leaving a node sum to 1: $P(\overline{B} \mid A) = 1 - P(B \mid A) = 1 - 0.4 = 0.6$.

**4.** $P(K) = \frac{4}{32} = \frac{1}{8}$. $P(H) = \frac{8}{32} = \frac{1}{4}$.
$K \cap H$ is the King of Hearts: $P(K \cap H) = \frac{1}{32}$.
Since $P(K) \times P(H) = \frac{1}{8} \times \frac{1}{4} = \frac{1}{32} = P(K \cap H)$, the events are independent.

**5.** Sum of probabilities = 1: $0.3 + 0.5 + p = 1 \implies p = 0.2$.
$E(X) = (-2 \times 0.3) + (0 \times 0.5) + (3 \times 0.2) = -0.6 + 0 + 0.6 = 0$.

**6.** $E(Y) = 3E(X) - 2 = 3(5) - 2 = 13$.
$V(Y) = 3^2 V(X) = 9 \times 4 = 36$.
$\sigma(Y) = \sqrt{36} = 6$ (or $|3| \times \sqrt{4} = 3 \times 2 = 6$).

**7.** $P(W_1) = \frac{3}{5}$. After drawing one white ball, 2 white balls remain among 4 total: $P(W_2 \mid W_1) = \frac{2}{4} = \frac{1}{2}$.
$P(W_1 \cap W_2) = \frac{3}{5} \times \frac{1}{2} = \frac{3}{10} = 0.30$.

**8.** The sample space is reduced to the two remaining choices, exactly one of which is correct: $P = \frac{1}{2} = 50\%$.

**9.**
a) Total probability:
$P(D) = P(M_1)P(D \mid M_1) + P(M_2)P(D \mid M_2) + P(M_3)P(D \mid M_3)$
$P(D) = (0.50 \times 0.03) + (0.30 \times 0.04) + (0.20 \times 0.05) = 0.015 + 0.012 + 0.010 = 0.037 = 3.7\%$.
b) Bayes: $P(M_1 \mid D) = \frac{P(M_1 \cap D)}{P(D)} = \frac{0.015}{0.037} = \frac{15}{37} \approx 0.4054 = 40.54\%$.

**10.** By the law of total probability: $P(A) = P(A \cap B) + P(A \cap \overline{B})$.
Thus $P(A \cap \overline{B}) = P(A) - P(A \cap B)$.
Since $A$ and $B$ are independent, $P(A \cap B) = P(A)P(B)$.
Substitute: $P(A \cap \overline{B}) = P(A) - P(A)P(B) = P(A)(1 - P(B)) = P(A)P(\overline{B})$.
This proves independence of $A$ and $\overline{B}$.

**11.**
a) $X \in \{0, 1, 2, 3\}$. There are $2^3 = 8$ equally likely outcomes.
- $P(X=0) = P(\{TTT\}) = \frac{1}{8}$
- $P(X=1) = P(\{HTT, THT, TTH\}) = \frac{3}{8}$
- $P(X=2) = P(\{HHT, HTH, THH\}) = \frac{3}{8}$
- $P(X=3) = P(\{HHH\}) = \frac{1}{8}$
b) $E(X) = 0(\frac{1}{8}) + 1(\frac{3}{8}) + 2(\frac{3}{8}) + 3(\frac{1}{8}) = \frac{0 + 3 + 6 + 3}{8} = \frac{12}{8} = 1.5$.
$E(X^2) = 0^2(\frac{1}{8}) + 1^2(\frac{3}{8}) + 2^2(\frac{3}{8}) + 3^2(\frac{1}{8}) = \frac{0 + 3 + 12 + 9}{8} = \frac{24}{8} = 3$.
$V(X) = E(X^2) - (E(X))^2 = 3 - (1.5)^2 = 3 - 2.25 = 0.75 = \frac{3}{4}$.

**12.** Let $G$ be net gain: $G \in \{+1, +4, -2\}$.
- Even outcomes $\{2, 4, 6\} \implies P(G = 1) = \frac{3}{6} = \frac{1}{2}$.
- Outcome 5 $\{5\} \implies P(G = 4) = \frac{1}{6}$.
- Other outcomes $\{1, 3\} \implies P(G = -2) = \frac{2}{6} = \frac{1}{3}$.
Expectation:
$E(G) = \left(1 \times \frac{3}{6}\right) + \left(4 \times \frac{1}{6}\right) + \left(-2 \times \frac{2}{6}\right) = \frac{3 + 4 - 4}{6} = \frac{3}{6} = +\$0.50$.
The game is not fair ($E(G) \neq 0$): it favors the player, who averages 50 cents profit per game.

**13.** $P(A) = \frac{3}{6} = \frac{1}{2}$.
An odd sum requires one even and one odd die. There are 18 such outcomes out of 36, so $P(B) = \frac{18}{36} = \frac{1}{2}$.
$A \cap B$: first die is even AND sum is odd $\iff$ first die even AND second die odd.
There are $3 \times 3 = 9$ outcomes out of 36. Thus $P(A \cap B) = \frac{9}{36} = \frac{1}{4}$.
Since $P(A) \times P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = P(A \cap B)$, the events are independent.

**14.**
a) $P(V) = 0.60$ and $P(\overline{V}) = 0.40$.
Rate in unvaccinated: $P(I \mid \overline{V}) = 0.25$.
Rate in vaccinated: 5 times lower $\implies P(I \mid V) = \frac{0.25}{5} = 0.05$.
$P(I) = P(V)P(I \mid V) + P(\overline{V})P(I \mid \overline{V}) = (0.60 \times 0.05) + (0.40 \times 0.25) = 0.03 + 0.10 = 0.13 = 13\%$.
b) Bayes: $P(V \mid I) = \frac{P(V \cap I)}{P(I)} = \frac{0.03}{0.13} = \frac{3}{13} \approx 23.08\%$.
(Nearly 77% of infected individuals are unvaccinated).

**15.** $V(X) = E(X^2) - (E(X))^2 = 116 - 10^2 = 116 - 100 = 16$.
$\sigma(X) = \sqrt{16} = 4$.

**16.**
```python
import random

def simulate_game(num_plays=10000):
    payouts = []
    for _ in range(num_plays):
        roll = random.randint(1, 6)
        if roll in [2, 4, 6]:
            gain = 1  # 3 - 2
        elif roll == 5:
            gain = 4  # 6 - 2
        else:
            gain = -2  # 0 - 2
        payouts.append(gain)
    sim_mean = sum(payouts) / num_plays
    print(f"Simulated mean: {sim_mean:.4f} € (Theoretical: 0.5000 €)")

simulate_game()
```

**17.**
The sample space of two-child families is $\Omega = \{(B, B), (B, G), (G, B), (G, G)\}$, with 4 equally likely outcomes (first child, second child).
a) The condition “elder child is a girl” gives $A = \{(G, B), (G, G)\}$.
In this 2-element space, the probability that both are girls is $\frac{1}{2} = 50\%$.
b) The condition “at least one child is a girl” gives $B = \{(B, G), (G, B), (G, G)\}$.
This reduced space has **3 elements**. Only one corresponds to two girls: $(G, G)$.
The probability is thus $\frac{1}{3} \approx 33.3\%$!
The paradox arises because “at least one girl” provides strictly less information than identifying which specific child is a girl.

**18.**
- When you pick Door $A$ initially, $P(\text{Car behind } A) = \frac{1}{3}$.
  The probability the car is behind $\{B, C\}$ is $\frac{2}{3}$.
- The host deliberately eliminates a goat among $\{B, C\}$. This is not a random action: he acts with full knowledge of the car's location.
- The entire $\frac{2}{3}$ probability mass originally residing on the block $\{B, C\}$ now concentrates **entirely onto the sole remaining door $C$**!
- If you keep Door $A$, your winning probability remains $\frac{1}{3}$.
- If you switch to Door $C$, your winning probability rises to $\frac{2}{3}$.
Switching doors strictly doubles your likelihood of winning!

**19.** Let $p_k$ denote the probability of ruin starting with fortune $k$ dollars ($k \in \{0, 1, 2, 3, 4\}$).
Boundary conditions: $p_0 = 1$ (already ruined) and $p_4 = 0$ (target reached).
For $k \in \{1, 2, 3\}$, after one toss:
$p_k = 0.5 p_{k+1} + 0.5 p_{k-1} \iff 2p_k = p_{k+1} + p_{k-1} \iff p_{k+1} - p_k = p_k - p_{k-1}$.
The sequence $(p_k)$ is arithmetic!
Since $p_0 = 1$ and $p_4 = 0$, the common difference is $r = \frac{0 - 1}{4} = -0.25$.
Thus $p_1 = 0.75$, $p_2 = 0.50$, $p_3 = 0.25$.
Starting with \$2, the probability of ruin is exactly $p_2 = 0.50 = 50\%$.

**20.**
a) Success (rolling 6) has probability $p = \frac{1}{6}$, failure $q = \frac{5}{6}$.
- $P(X=1) = \frac{1}{6}$.
- $P(X=2) = \frac{5}{6} \times \frac{1}{6} = \frac{5}{36}$.
- $P(X=3) = \left(\frac{5}{6}\right)^2 \times \frac{1}{6} = \frac{25}{216}$.
- $P(X=4)$: stop on the 4th roll whether a 6 is rolled or not, which corresponds to failing the first 3 rolls: $P(X=4) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}$.
Check: $\frac{36 + 30 + 25 + 125}{216} = \frac{216}{216} = 1$.
b) $E(X) = 1\left(\frac{36}{216}\right) + 2\left(\frac{30}{216}\right) + 3\left(\frac{25}{216}\right) + 4\left(\frac{125}{216}\right) = \frac{36 + 60 + 75 + 500}{216} = \frac{671}{216} \approx 3.106$ rolls.

---

### The Question That Opens What Follows

We have reached the culmination of Volume V.
From towing ropes and vectors to the medical clinic, we have mastered directional forces, instantaneous rates of change via derivatives, explosive exponential growth, and probabilistic reasoning.
Yet behold the road leading up to the final summit: what happens when a random experiment is repeated not 4 times, but indefinitely? How do we prove mathematical truths across all infinite integers simultaneously via **mathematical induction**? How do we calculate the exact area under a curved surface by stacking infinitely many infinitesimal slices?
That is the crowning domain of **Volume VI: The Age of Flow and Velocity**, awaiting you in the next chapter!
