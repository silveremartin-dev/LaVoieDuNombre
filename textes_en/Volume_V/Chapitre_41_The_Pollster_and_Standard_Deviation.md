# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)
## CHAPTER 41: The Pollster and Standard Deviation

> *“If you put your head in a burning oven and your feet in a block of ice, an incautious statistician will tell you that, ‘on average,’ your body temperature is ideal. The mean is a lighthouse illuminating the center while plunging the peripheral storms into deep shadow. To understand the real world, one must measure the dispersion.”*

---

### What You Are About to Discover

- The fatal trap of the arithmetic mean: why two factories, two classes, or two medical treatments sharing the exact same mean can be diametrically opposed.
- Position indicators: the **weighted mean** ($\bar{x}$) versus the **median** ($M_e$), and why the median cannot be fooled by billionaires.
- Sentinels of the quarter: the **quartiles** $Q_1$ and $Q_3$, and the **interquartile range** ($IQR$).
- The art of visual summarization: John Tukey’s **box-and-whisker plot** (*boxplot*).
- The mystery of the square: why the sum of deviations from the mean always vanishes ($\sum (x_i - \bar{x}) = 0$), and why we had to invent the **variance** and **standard deviation** $\sigma$.
- The **König-Huygens formula**: the lightning-fast shortcut for computing variance.
- The law of sampling: how a pollster can predict the vote of 45 million citizens by interviewing a mere 1,000 individuals, using the **sampling fluctuation interval**.
- Sampling simulations programmed in **Python**.

---

### 1. The Problem: The Two Drive-Shaft Factories

We find ourselves inside a cutting-edge aerospace manufacturing facility near Toulouse.
The plant produces titanium drive shafts destined for commercial jet turbine engines. The engineers' technical specifications are absolute: to fit within a thousandth of a millimeter into the turbine’s precision ball bearings, the nominal diameter of a shaft must measure exactly **$50.00$ millimeters**. A shaft measuring $50.10$ mm will jam the engine; a shaft measuring $49.90$ mm will introduce destructive mechanical play at 10,000 rpm.

Two subcontracting suppliers, Workshop **Alpha** and Workshop **Beta**, each deliver a batch of 1,000 machined shafts.
The quality control director measures the samples:

- In Workshop **Alpha**, the mean diameter is exactly **$50.00$ mm**.
- In Workshop **Beta**, the mean diameter is likewise exactly **$50.00$ mm**.

A naive purchasing agent might declare: *“Both suppliers produce identical results, let’s buy the cheaper one!”*
However, the chief technical director inspects the pieces under an electronic microscope:

```
Workshop Alpha:
   Every single shaft measures between 49.98 mm and 50.02 mm.
   They are virtually immaculate, tightly clustered like a dense swarm around 50.00 mm.

                                 |
                               |||||
                              |||||||
                         ────┼┼┼┼┼┼┼┼┼────
                            49.99  50  50.01

Workshop Beta:
   One shaft measures 46.00 mm, another 54.00 mm, another 48.20 mm...
   The pieces are scattered across a frightening expanse of chaotic variation!

             |         |         |         |         |
             |    |    |    |    |    |    |    |    |
        ─────┼────┼────┼────┼────┼────┼────┼────┼────┼────
            46   47   48   49   50   51   52   53   54
```

In Workshop Beta, **virtually no part can safely be fitted into an aircraft**! Some are wildly oversized, others dangerously thin, even though by sheer symmetrical coincidence their arithmetic average hits 50 mm on the dot. Installing Beta’s parts would lead directly to engine failure.

This is the intellectual crisis that birthed modern statistics:
**A measure of central tendency (the mean) is useless unless accompanied by a measure of dispersion (the standard deviation).**

---

### 2. Measures of Central Tendency: Mean vs. Median

Consider a discrete quantitative dataset where the variable takes sorted values $x_1 < x_2 < \dots < x_p$, associated with frequencies (counts) $n_1, n_2, \dots, n_p$.
The total sample size is $N = \sum_{i=1}^p n_i$.

#### 2.1 The Weighted Mean ($\bar{x}$)

The mean is the center of gravity of the distribution: it is the fair share each individual would receive if all values were pooled and redistributed equally.

> **📐 Definition — Weighted Mean**
> The **weighted mean** of a dataset, denoted $\bar{x}$ (read “**x bar**”), is given by:
>
> $$\boxed{\bar{x} = \frac{\sum_{i=1}^p n_i x_i}{N} = \sum_{i=1}^p f_i x_i}$$
>
> where $f_i = \frac{n_i}{N}$ denotes the relative frequency of the value $x_i$.

**Linearity Property:**
If every value is multiplied by a constant $a$ and shifted by a constant $b$ (affine transformation $y_i = a x_i + b$), the new mean is simply:
$$\bar{y} = a \bar{x} + b.$$

#### 2.2 The Median ($M_e$): The Justice of Rank

The median ignores the sum total and focuses entirely on **position in line**.

> **📐 Definition — Median**
> The **median** of a sorted statistical dataset, denoted $M_e$, is a value that splits the population into two halves of equal size:
> - At least 50% of the individuals have a value less than or equal to $M_e$;
> - At least 50% of the individuals have a value greater than or equal to $M_e$.

**Practical Computation Method:**
1. If the total count $N$ is **odd**: $N = 2k + 1$.
   The median is the value of the individual at rank $k+1$.
   *(Example: for $N = 9$, $\frac{9+1}{2} = 5$: the median is the 5th value).*
2. If the total count $N$ is **even**: $N = 2k$.
   The median is conventionally taken as the midpoint between the values at ranks $k$ and $k+1$.
   *(Example: for $N = 10$, take the average of the 5th and 6th values).*

> **🔍 True Story — Bill Gates Walks into a Bar**
> Imagine a neighborhood café where ten factory workers and clerks sit at the counter. Each earns \$2,000 per month.
> The mean wage is \$2,000, and the median wage is \$2,000.
> Suddenly, billionaire **Bill Gates** opens the door and takes a seat at the bar. His monthly income is around \$10,000,000.
> Let us recalculate the statistics of the patrons:
> - The **mean income** skyrockets: $\frac{10 \times 2,000 + 10,000,000}{11} \approx \mathbf{\$910,900\text{ per month}}$!
>   A foolish statistician might announce: “In this diner, the average customer is nearly a millionaire!” Which is absurd.
> - The **median income**, however, lines up the 11 patrons in ascending order. The 6th person in line still earns exactly **\$2,000**!
> The median did not budge by a single penny: it is **robust** against extreme outliers, whereas the mean is hyper-sensitive.

---

### 3. Quartiles and the Box-and-Whisker Plot

To analyze the spread more deeply, we partition the ordered dataset into **four equal quarters** of 25% each.

#### 3.1 Formal Definitions of Quartiles

> **📐 Definition — Quartiles**
> In a sorted dataset of size $N$:
> - The **first quartile**, denoted $Q_1$, is the smallest value in the dataset such that at least **25%** of observations are less than or equal to $Q_1$. Its rank is the smallest integer greater than or equal to $\frac{N}{4}$ (denoted $\lceil N/4 \rceil$).
> - The **third quartile**, denoted $Q_3$, is the smallest value such that at least **75%** of observations are less than or equal to $Q_3$. Its rank is the smallest integer greater than or equal to $\frac{3N}{4}$ (denoted $\lceil 3N/4 \rceil$).
> - The second quartile $Q_2$ is none other than the median $M_e$.

> **📐 Definition — Interquartile Range**
> The difference between the third and first quartiles is called the **interquartile range** ($IQR$):
>
> $$\boxed{IQR = Q_3 - Q_1}$$
>
> It measures the width of the interval housing the **central 50%** of the population. Like the median, this measure of spread is entirely impervious to extreme outliers.

#### 3.2 John Tukey’s Boxplot (1977)

Pioneered by the American statistician **John Tukey**, the box-and-whisker plot summarizes an entire distribution at a single glance:

```
                  Central Box (50% of data)
                ┌───────────────────┬──────────────┐
     ├──────────┤                   │              ├──────────┤
     │          │                   │              │          │
    Min         Q₁               Median           Q₃         Max
     |◄──25%───►|◄──────25%────────►|◄────25%─────►|◄──25%───►|
```

- The **box** spans from $Q_1$ to $Q_3$. Its width is the interquartile range.
- The vertical line inside marks the **median**. An off-center median reveals skewness.
- The two **whiskers** extend outward to the minimum and maximum non-outlier observations.

---

### 4. The Mystery of the Square: Variance and Standard Deviation

Let us return to our aerospace shafts. How do we mathematically capture the average distance of the observations from the target mean $\bar{x}$?

#### 4.1 The First Naive Idea: Average of Deviations

The most instinctive attempt would be to compute the raw difference $(x_i - \bar{x})$ for each individual, then take their average.
Test this on three simple test scores: $8, 12, 16$.
The mean is $\bar{x} = \frac{8 + 12 + 16}{3} = 12$.
The individual deviations from the mean are:
- For 8: $8 - 12 = -4$
- For 12: $12 - 12 = 0$
- For 16: $16 - 12 = +4$

Add them up: $(-4) + 0 + (+4) = \mathbf{0}$!
The positive deviations were completely cancelled out by the negative ones!

> **📐 Theorem — The Sum of Deviations is Always Zero**
> For any dataset:
>
> $$\sum_{i=1}^p n_i (x_i - \bar{x}) = 0$$

> **✍️ Proof**
> Expand the summation:
> $$\sum_{i=1}^p n_i (x_i - \bar{x}) = \sum_{i=1}^p n_i x_i - \sum_{i=1}^p n_i \bar{x} = \sum_{i=1}^p n_i x_i - \bar{x} \sum_{i=1}^p n_i = N \bar{x} - \bar{x} N = 0. \quad \blacksquare$$

The average of raw deviations is **identically zero**, no matter how dispersed the data is! It is entirely useless as a measure of spread.

#### 4.2 The Square Trick: Variance

To prevent negative deviations from neutralizing positive ones, mathematicians square each deviation: $(-4)^2 = +16$! A squared real number is always non-negative.

> **📐 Definition — Variance**
> The **variance** of a dataset, denoted $V$, is the mean of the squared deviations from the mean:
>
> $$\boxed{V = \frac{1}{N} \sum_{i=1}^p n_i (x_i - \bar{x})^2 = \sum_{i=1}^p f_i (x_i - \bar{x})^2}$$

#### 4.3 Standard Deviation ($\sigma$): Restoring the Physical Unit

Variance overcomes the sign problem, but introduces a dimensional absurdity:
If we measure heights in **meters** (m), the deviations are in meters, but their squared deviations are in **square meters** ($\text{m}^2$)! Expressing the spread of human heights in square meters makes no physical sense.
To restore the original unit of measurement (meters, euros, millimeters), we take the **square root**:

> **📐 Definition — Standard Deviation**
> The **standard deviation**, denoted $\sigma$ (lowercase Greek letter **sigma**), is the square root of the variance:
>
> $$\boxed{\sigma = \sqrt{V} = \sqrt{\frac{1}{N} \sum_{i=1}^p n_i (x_i - \bar{x})^2}}$$

**Intuitive Meaning:**
The standard deviation measures the *typical* distance by which an individual data point deviates from the group mean.
- Workshop Alpha: $\bar{x} = 50.00$ mm and $\sigma = \mathbf{0.01\text{ mm}}$ (negligible spread).
- Workshop Beta: $\bar{x} = 50.00$ mm and $\sigma = \mathbf{2.45\text{ mm}}$ (catastrophic spread).
Thanks to $\sigma$, the aerospace engineer instantly identifies the defective workshop!

---

### 5. The König-Huygens Formula: The Computational Shortcut

Computing every $(x_i - \bar{x})^2$ by hand becomes tedious as soon as $\bar{x}$ involves decimals. Fortunately, 17th-century mathematicians **Samuel König** and **Christiaan Huygens** established an ingenious computational identity:

> **📐 Theorem — König-Huygens Formula**
> The variance equals **the mean of the squares minus the square of the mean**:
>
> $$\boxed{V = \overline{x^2} - (\bar{x})^2}$$
>
> where $\overline{x^2} = \frac{1}{N} \sum_{i=1}^p n_i x_i^2$ denotes the mean of the squared values.

> **✍️ Proof**
> Expand the square inside the variance definition:
> $$V = \frac{1}{N} \sum_{i=1}^p n_i \big(x_i^2 - 2x_i\bar{x} + \bar{x}^2\big).$$
> Distribute the summation:
> $$V = \frac{1}{N}\sum n_i x_i^2 - \frac{2\bar{x}}{N}\sum n_i x_i + \frac{\bar{x}^2}{N}\sum n_i.$$
> Since $\frac{1}{N}\sum n_i x_i^2 = \overline{x^2}$, $\frac{1}{N}\sum n_i x_i = \bar{x}$, and $\sum n_i = N$, this simplifies to:
> $$V = \overline{x^2} - 2\bar{x}(\bar{x}) + \frac{\bar{x}^2}{N}(N) = \overline{x^2} - 2(\bar{x})^2 + (\bar{x})^2 = \overline{x^2} - (\bar{x})^2. \quad \blacksquare$$

> **💡 Affine Transformation Property —**
> If $y_i = a x_i + b$, then:
> $$V(aX + b) = a^2 V(X) \quad \text{and} \quad \boxed{\sigma(aX + b) = |a| \cdot \sigma(X)}$$
> Note: Adding a constant $b$ (e.g., granting a 2-point bonus to the entire class) shifts all scores without altering their spread: the standard deviation remains unchanged!

---

### 6. Sampling, Fluctuation, and Python Simulation

How can a polling institute accurately gauge the outcome of a national presidential election by calling only 1,000 citizens?
This is the mathematical magic of **sampling fluctuation**.

#### 6.1 The Principle of Fluctuation

Suppose an actual proportion $p$ of all citizens in the nation supports a given policy.
If we draw a random sample of size $n$, the observed proportion $f$ in that sample will almost never equal $p$ exactly: it fluctuates around $p$.
However, for a sufficiently large sample ($n \ge 30$, $np \ge 5$, $n(1-p) \ge 5$), probability theory guarantees that in **at least 95% of random samples**, the observed frequency $f$ falls within a well-defined interval:

> **📐 Definition — 95% Fluctuation Interval**
> - Introductory approximation:
>   $$I = \left[ p - \frac{1}{\sqrt{n}} \ ; \ p + \frac{1}{\sqrt{n}} \right]$$
> - Asymptotic formula (derived from the Normal distribution):
>   $$\boxed{I_{0.95} = \left[ p - 1.96 \sqrt{\frac{p(1-p)}{n}} \ ; \ p + 1.96 \sqrt{\frac{p(1-p)}{n}} \right]}$$

#### 6.2 Sampling Simulation in Python

To verify this experimentally, let us simulate 1,000 independent polls of size $n = 100$ drawn from a population where the true proportion is $p = 0.40$ (40%):

```python
import random

def simulate_sample(n, p):
    """Simulates drawing a sample of size n and returns observed frequency f."""
    successes = sum(1 for _ in range(n) if random.random() < p)
    return successes / n

def fluctuation_study(num_samples=1000, n=100, p=0.40):
    lower_bound = p - 1.96 * (p * (1 - p) / n) ** 0.5
    upper_bound = p + 1.96 * (p * (1 - p) / n) ** 0.5

    inside_interval = 0
    for _ in range(num_samples):
        f = simulate_sample(n, p)
        if lower_bound <= f <= upper_bound:
            inside_interval += 1

    percentage = (inside_interval / num_samples) * 100
    print(f"Theoretical 95% interval: [{lower_bound:.4f} ; {upper_bound:.4f}]")
    print(f"Percentage of samples inside interval: {percentage:.1f}%")

fluctuation_study()
```

Output:
```
Theoretical 95% interval: [0.3040 ; 0.4960]
Percentage of samples inside interval: 95.3%
```
Precisely as predicted: over 95% of random polls hit the theoretical bullseye!

---

### Step-by-Step Worked Examples

> **✅ Worked Example 1 — Computing Mean and Standard Deviation**
> The grades of 20 students on an examination are distributed as follows:
>
> | Grade $x_i$ | 6 | 8 | 10 | 12 | 15 | 18 |
> |---|---|---|---|---|---|---|
> | Count $n_i$ | 2 | 4 | 6 | 5 | 2 | 1 |
>
> Calculate the mean $\bar{x}$, variance $V$, and standard deviation $\sigma$.
>
> **Detailed Solution:**
> Total count: $N = 2 + 4 + 6 + 5 + 2 + 1 = 20$.
> 1. Mean:
>    $$\sum n_i x_i = (2 \times 6) + (4 \times 8) + (6 \times 10) + (5 \times 12) + (2 \times 15) + (1 \times 18)$$
>    $$= 12 + 32 + 60 + 60 + 30 + 18 = 212.$$
>    $$\bar{x} = \frac{212}{20} = 10.6.$$
>
> 2. König-Huygens formula for variance:
>    Compute $\sum n_i x_i^2$:
>    $$2(36) + 4(64) + 6(100) + 5(144) + 2(225) + 1(324)$$
>    $$= 72 + 256 + 600 + 720 + 450 + 324 = 2422.$$
>    $$\overline{x^2} = \frac{2422}{20} = 121.1.$$
>    $$V = \overline{x^2} - (\bar{x})^2 = 121.1 - (10.6)^2 = 121.1 - 112.36 = 8.74.$$
>
> 3. Standard deviation:
>    $$\sigma = \sqrt{V} = \sqrt{8.74} \approx 2.96.$$
>    The class average is $10.6$ with a standard deviation of nearly $3$ points.

> **✅ Worked Example 2 — Determining Median and Quartiles**
> Find $M_e$, $Q_1$, $Q_3$, and the $IQR$ for the dataset in Example 1.
>
> **Detailed Solution:**
> Construct the cumulative frequency table:
>
> | Grade $x_i$ | 6 | 8 | 10 | 12 | 15 | 18 |
> |---|---|---|---|---|---|---|
> | Count $n_i$ | 2 | 4 | 6 | 5 | 2 | 1 |
> | Cumulative | 2 | 6 | 12 | 17 | 19 | 20 |
>
> - **Median:** $N = 20$ (even). $\frac{N}{2} = 10$.
>   Take the average of the 10th and 11th values.
>   From cumulative counts, both the 10th and 11th values are 10.
>   Thus $\boxed{M_e = 10}$.
> - **First Quartile $Q_1$:** $\frac{N}{4} = \frac{20}{4} = 5$.
>   $Q_1$ is the 5th value in the sorted list.
>   Ranks 3 through 6 are 8.
>   Thus $\boxed{Q_1 = 8}$.
> - **Third Quartile $Q_3$:** $\frac{3N}{4} = \frac{60}{4} = 15$.
>   $Q_3$ is the 15th value. Ranks 13 through 17 are 12.
>   Thus $\boxed{Q_3 = 12}$.
> - **Interquartile Range:** $IQR = Q_3 - Q_1 = 12 - 8 = 4$.
>   The middle 50% of the class earned grades between 8 and 12.

> **✅ Worked Example 3 — Boxplot Comparison of Two Archery Competitors**
> Two archers $A$ and $B$ shoot 50 arrows each. Their five-number summaries are:
> - Archer $A$: $\text{Min} = 5$, $Q_1 = 8$, $M_e = 9$, $Q_3 = 10$, $\text{Max} = 10$.
> - Archer $B$: $\text{Min} = 2$, $Q_1 = 6$, $M_e = 9$, $Q_3 = 9$, $\text{Max} = 10$.
> Compare their performance profiles.
>
> **Detailed Solution:**
> - Both archers share the exact same median ($M_e = 9$): at least half their arrows hit a 9 or 10.
> - Contrast their dispersion:
>   - Archer $A$: $IQR = 10 - 8 = 2$, total range is $10 - 5 = 5$. Fully 75% of shots scored 8 or higher.
>   - Archer $B$: $IQR = 9 - 6 = 3$, total range is $10 - 2 = 8$. One quarter of shots scored 6 or worse, including an erratic wild shot of 2.
> - **Conclusion:** Archer $A$ is far more **consistent and reliable**, despite their identical median scores.

> **✅ Worked Example 4 — Linear Transformation of Mean and Standard Deviation**
> A teacher administers a challenging test: the mean is $\bar{x} = 8$ and standard deviation is $\sigma = 3$.
> To rescale the grades, she applies the formula:
> $$y = 1.2 x + 2.$$
> Find the new mean $\bar{y}$ and new standard deviation $\sigma_y$.
>
> **Detailed Solution:**
> - By linearity of the mean:
>   $$\bar{y} = 1.2 \bar{x} + 2 = 1.2(8) + 2 = 9.6 + 2 = 11.6.$$
> - By properties of standard deviation: $\sigma(aX + b) = |a| \sigma(X)$.
>   $$\sigma_y = |1.2| \times \sigma = 1.2 \times 3 = 3.6.$$
> The mean rises by $3.6$ points, but the standard deviation also expands: individual score gaps widen slightly.

> **✅ Worked Example 5 — Hypothesis Testing on a Quality Sample**
> A bakery claims that only 2% of its packaged cookies have baking defects ($p = 0.02$).
> A consumer watchdog inspects a sample of $n = 500$ cookies and finds 18 defective ones.
> Should the manufacturer’s claim be rejected at the 95% confidence level?
>
> **Detailed Solution:**
> 1. Check validity conditions:
>    $n = 500 \ge 30$, $np = 500 \times 0.02 = 10 \ge 5$, $n(1-p) = 500 \times 0.98 = 490 \ge 5$.
>    Conditions are satisfied.
> 2. Theoretical 95% fluctuation interval:
>    $$I_{0.95} = \left[ 0.02 - 1.96 \sqrt{\frac{0.02 \times 0.98}{500}} \ ; \ 0.02 + 1.96 \sqrt{\frac{0.02 \times 0.98}{500}} \right].$$
>    $$\sqrt{\frac{0.0196}{500}} = \sqrt{0.0000392} \approx 0.00626.$$
>    Margin of error: $1.96 \times 0.00626 \approx 0.0123$.
>    $$I_{0.95} = [0.02 - 0.0123 \ ; \ 0.02 + 0.0123] = [0.0077 \ ; \ 0.0323].$$
>    In percentage terms: between $0.77\%$ and $3.23\%$.
> 3. Observed sample frequency:
>    $$f = \frac{18}{500} = 0.036 = 3.6\%.$$
> 4. Decision:
>    The observed frequency $f = 0.036 \notin I_{0.95}$ (it exceeds the upper bound of $0.0323$).
>    **Conclusion:** At the 95% confidence level, the manufacturer’s claim is **rejected**. The defect rate is abnormally high.

> **✅ Worked Example 6 — Detecting Statistical Outliers**
> Tukey established a standard rule for identifying outliers: any value strictly outside the fences:
> $$[Q_1 - 1.5 \times IQR \ ; \ Q_3 + 1.5 \times IQR].$$
> In a company, salaries have $Q_1 = \$1,800$ and $Q_3 = \$2,600$.
> Is an executive salary of \$4,000 considered an outlier?
>
> **Detailed Solution:**
> - Interquartile range: $IQR = 2600 - 1800 = \$800$.
> - Upper fence:
>   $Q_3 + 1.5 \times IQR = 2600 + 1.5(800) = 2600 + 1200 = \$3,800$.
> - Since $\$4,000 > \$3,800$, this salary exceeds the upper threshold: it is formally classified as an **outlier**.

---

### What You Must Remember

1. **Measures of Central Tendency:**
   - Mean: $\bar{x} = \frac{1}{N} \sum n_i x_i = \sum f_i x_i$. Highly sensitive to extreme values.
   - Median $M_e$: middle value (50% above, 50% below). Robust against outliers.
   - Quartiles: $Q_1$ (at least 25%) and $Q_3$ (at least 75%).

2. **Measures of Dispersion:**
   - Interquartile range: $IQR = Q_3 - Q_1$.
   - Variance: $V = \frac{1}{N} \sum n_i (x_i - \bar{x})^2$.
   - König-Huygens formula: $\boxed{V = \overline{x^2} - (\bar{x})^2}$.
   - Standard deviation: $\boxed{\sigma = \sqrt{V}}$ (shares original units of the data).

3. **Affine Transformations ($y = ax + b$):**
   - $\bar{y} = a\bar{x} + b$
   - $V(aX + b) = a^2 V(X)$
   - $\sigma(aX + b) = |a|\sigma(X)$

4. **Sampling and Fluctuation (at 95% Confidence):**
   - $I_{0.95} = \left[ p - 1.96 \sqrt{\frac{p(1-p)}{n}} \ ; \ p + 1.96 \sqrt{\frac{p(1-p)}{n}} \right]$ (for $n \ge 30$, $np \ge 5$, $n(1-p) \ge 5$).
   - If observed sample frequency $f \notin I_{0.95}$, reject hypothesis $p$.

---

### Exercises

#### Level ★ (Direct Computation of Statistics)

1. Compute the mean and median of the dataset: $4, 7, 9, 11, 14$.
2. Compute the mean and median of the dataset: $3, 5, 8, 12, 16, 20$.
3. A set of 5 values has a mean of 10. Four of the values are $6, 8, 11, 13$. Find the fifth value.
4. Compute the variance and standard deviation of the dataset $2, 4, 6, 8, 10$.
5. Given $\overline{x^2} = 53$ and $\bar{x} = 7$, find the variance $V$ and standard deviation $\sigma$.
6. If company salaries have a standard deviation $\sigma = \$250$, what is the new standard deviation if every employee receives an across-the-board raise of \$100?
7. What is the new standard deviation if every salary is increased by 5% (multiplied by 1.05)?
8. Determine $Q_1$, $M_e$, and $Q_3$ for the ordered dataset of 12 values:
   $1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 18, 20$.

#### Level ★★ (Comparative Analysis and Properties)

9. Consider the following dataset:
   | Value $x_i$ | 10 | 20 | 30 | 40 |
   |---|---|---|---|---|
   | Count $n_i$ | 3 | 5 | 8 | 4 |
   a) Compute $\bar{x}$.
   b) Use the König-Huygens formula to find $V$ and $\sigma$.
10. Prove that for two real numbers $a$ and $b$, the variance of $\{a, b\}$ equals $\left(\frac{a - b}{2}\right)^2$.
11. An assessment is taken by two groups:
    - Group 1 (15 students): mean $\bar{x}_1 = 12$.
    - Group 2 (25 students): mean $\bar{x}_2 = 10$.
    Calculate the combined mean of all 40 students.
12. In a class, test scores have a mean of 11 and a standard deviation of 2.5. The teacher wishes to scale the grades so that the mean becomes 12 and the standard deviation becomes 3.
    What affine transformation $y = ax + b$ should be applied?
13. A random sample of 400 voters reveals that 228 intend to vote for candidate $C$.
    Calculate the 95% fluctuation interval under the hypothesis that the electorate is evenly split ($p = 0.50$). Can we conclude that candidate $C$ has a statistically significant lead?
14. Daily high temperatures recorded in July at two weather stations show:
    - Station A: $\bar{x} = 28^\circ\text{C}$, $\sigma = 1.5^\circ\text{C}$.
    - Station B: $\bar{x} = 28^\circ\text{C}$, $\sigma = 6.2^\circ\text{C}$.
    Contrast the climate characteristics of the two locations.
15. Write a Python function `statistics(data)` that takes a list of numbers and returns its size, mean, variance, and standard deviation without importing external libraries.

#### Level ★★★ (Theoretical Challenges and Modeling)

16. **Variance of the Union of Two Datasets:**
    Let two datasets have sizes $N_1, N_2$, means $\bar{x}_1, \bar{x}_2$, and variances $V_1, V_2$.
    Prove that the variance $V$ of the pooled dataset of size $N = N_1 + N_2$ satisfies:
    $$V = \frac{N_1 V_1 + N_2 V_2}{N} + \frac{N_1 N_2}{N^2}(\bar{x}_1 - \bar{x}_2)^2.$$
    Interpret both terms (within-group variance and between-group variance).
17. **Bienaymé-Chebyshev Inequality (Discovery):**
    For any dataset with mean $\bar{x}$ and standard deviation $\sigma$, prove that the proportion of data points located at a distance of $2\sigma$ or more from the mean can never exceed $\frac{1}{4} = 25\%$, regardless of the distribution's shape!
18. **Polling Sample Size and Margin of Error:**
    A political poll interviews $n$ voters to decide an election between two neck-and-neck candidates ($p \approx 0.50$).
    What is the minimum sample size $n$ needed to ensure that the 95% margin of error ($1.96 \sqrt{\frac{p(1-p)}{n}}$) is strictly under 1% (i.e., $0.01$)?
19. **Variance of Consecutive Integers:**
    Consider the first $n$ positive integers: $1, 2, 3, \dots, n$.
    a) Find the mean $\bar{x}$ in terms of $n$.
    b) Using $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$, prove that the variance is $V = \frac{n^2 - 1}{12}$.
20. **Outlier Detection in Python:**
    Write a Python function that accepts a list of raw numbers, computes $Q_1$, $Q_3$, Tukey’s fences, and extracts all outliers.

---

### Solutions

**1.** Mean: $\bar{x} = \frac{4 + 7 + 9 + 11 + 14}{5} = \frac{45}{5} = 9$.
Median: 3rd value out of 5, so $M_e = 9$.

**2.** Mean: $\bar{x} = \frac{3 + 5 + 8 + 12 + 16 + 20}{6} = \frac{64}{6} \approx 10.67$.
Median: average of 3rd and 4th values: $M_e = \frac{8 + 12}{2} = 10$.

**3.** Total sum = $5 \times 10 = 50$.
Sum of given four values = $6 + 8 + 11 + 13 = 38$.
Fifth value: $50 - 38 = 12$.

**4.** $\bar{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = 6$.
Deviations from mean: $-4, -2, 0, 2, 4$.
Squared deviations: $16, 4, 0, 4, 16$.
Variance: $V = \frac{16 + 4 + 0 + 4 + 16}{5} = \frac{40}{5} = 8$.
Standard deviation: $\sigma = \sqrt{8} = 2\sqrt{2} \approx 2.83$.

**5.** $V = \overline{x^2} - (\bar{x})^2 = 53 - 7^2 = 53 - 49 = 4$.
$\sigma = \sqrt{4} = 2$.

**6.** Standard deviation is invariant under addition: new standard deviation is still $\sigma = \$250$.

**7.** $y = 1.05 x \implies \sigma_y = 1.05 \times \sigma = 1.05 \times 250 = \$262.50$.

**8.** $N = 12$.
- $Q_1$: rank $\frac{12}{4} = 3 \implies$ 3rd value, so $Q_1 = 4$.
- Median: average of 6th and 7th values $\implies M_e = \frac{9 + 10}{2} = 9.5$.
- $Q_3$: rank $\frac{3 \times 12}{4} = 9 \implies$ 9th value, so $Q_3 = 13$.

**9.**
a) $N = 3 + 5 + 8 + 4 = 20$.
$\sum n_i x_i = 3(10) + 5(20) + 8(30) + 4(40) = 30 + 100 + 240 + 160 = 530$.
$\bar{x} = \frac{530}{20} = 26.5$.
b) $\sum n_i x_i^2 = 3(100) + 5(400) + 8(900) + 4(1600) = 300 + 2000 + 7200 + 6400 = 15900$.
$\overline{x^2} = \frac{15900}{20} = 795$.
$V = \overline{x^2} - (\bar{x})^2 = 795 - (26.5)^2 = 795 - 702.25 = 92.75$.
$\sigma = \sqrt{92.75} \approx 9.63$.

**10.** Mean: $\bar{x} = \frac{a+b}{2}$.
Deviations: $a - \frac{a+b}{2} = \frac{a-b}{2}$, and $b - \frac{a+b}{2} = \frac{b-a}{2} = -\frac{a-b}{2}$.
The mean of the squared deviations is:
$V = \frac{1}{2}\left[\left(\frac{a-b}{2}\right)^2 + \left(-\frac{a-b}{2}\right)^2\right] = \left(\frac{a-b}{2}\right)^2$.

**11.** Pooled weighted mean:
$\bar{x} = \frac{N_1 \bar{x}_1 + N_2 \bar{x}_2}{N_1 + N_2} = \frac{15 \times 12 + 25 \times 10}{40} = \frac{180 + 250}{40} = \frac{430}{40} = 10.75$.

**12.** Require $\sigma_y = |a|\sigma \iff 3 = a \times 2.5 \iff a = \frac{3}{2.5} = 1.2$.
Then require $\bar{y} = a\bar{x} + b \iff 12 = 1.2(11) + b \iff 12 = 13.2 + b \iff b = -1.2$.
The transformation is $y = 1.2 x - 1.2$.

**13.** Sample frequency: $f = \frac{228}{400} = 0.57$.
Under $p = 0.50$, the 95% fluctuation interval is:
$I = \left[ 0.50 - 1.96\sqrt{\frac{0.25}{400}} \ ; \ 0.50 + 1.96\sqrt{\frac{0.25}{400}} \right] = [0.50 - 1.96 \times 0.025 \ ; \ 0.50 + 1.96 \times 0.025] = [0.451 \ ; \ 0.549]$.
Since $f = 0.57 > 0.549$, the observed frequency falls above the interval: Candidate $C$ has a statistically significant lead over an even split.

**14.** Both stations share the same average temperature ($28^\circ$C).
Station A exhibits very low standard deviation ($1.5^\circ$C): maritime/oceanic stability.
Station B shows high standard deviation ($6.2^\circ$C): continental weather with sharp temperature swings.

**15.**
```python
def statistics(data):
    N = len(data)
    mean_val = sum(data) / N
    variance_val = sum((x - mean_val) ** 2 for x in data) / N
    std_val = variance_val ** 0.5
    return {"size": N, "mean": mean_val, "std_dev": std_val}
```

**16.** Let $S_1 = \sum_{x \in G_1} x^2$ and $S_2 = \sum_{x \in G_2} x^2$.
By König-Huygens in each group: $S_1 = N_1 (V_1 + \bar{x}_1^2)$ and $S_2 = N_2 (V_2 + \bar{x}_2^2)$.
In the pooled group: $\bar{x} = \frac{N_1 \bar{x}_1 + N_2 \bar{x}_2}{N}$, and $V = \frac{S_1 + S_2}{N} - \bar{x}^2$.
Expanding and regrouping terms yields:
$V = \frac{N_1 V_1 + N_2 V_2}{N} + \frac{N_1 N_2}{N^2}(\bar{x}_1 - \bar{x}_2)^2$.
- The first term represents **within-group variance** (weighted average of group variances).
- The second term represents **between-group variance** (the separation between group means).

**17.** Let $E$ be the set of observations satisfying $|x_i - \bar{x}| \ge 2\sigma$, with count $N_E$.
For every $x_i \in E$, $(x_i - \bar{x})^2 \ge 4\sigma^2$.
The total sum of squared deviations satisfies:
$N V = \sum_{i=1}^N (x_i - \bar{x})^2 \ge \sum_{i \in E} (x_i - \bar{x})^2 \ge N_E \times 4\sigma^2$.
Since $V = \sigma^2$, we have $N \sigma^2 \ge 4 N_E \sigma^2$.
Dividing by $4 N \sigma^2$ yields $\frac{N_E}{N} \le \frac{1}{4} = 25\%$.

**18.** Margin of error: $1.96 \sqrt{\frac{0.5 \times 0.5}{n}} = 1.96 \times \frac{0.5}{\sqrt{n}} = \frac{0.98}{\sqrt{n}}$.
Set $\frac{0.98}{\sqrt{n}} < 0.01 \iff \sqrt{n} > \frac{0.98}{0.01} = 98 \iff n > 98^2 = 9,604$.
At least **9,605 people** must be polled to achieve a margin of error under 1%.

**19.**
a) $\bar{x} = \frac{1}{n} \sum_{k=1}^n k = \frac{1}{n} \times \frac{n(n+1)}{2} = \frac{n+1}{2}$.
b) $\overline{x^2} = \frac{1}{n} \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6}$.
By König-Huygens:
$V = \overline{x^2} - (\bar{x})^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4} = (n+1)\left[ \frac{2(2n+1) - 3(n+1)}{12} \right] = (n+1)\frac{4n+2-3n-3}{12} = \frac{(n+1)(n-1)}{12} = \frac{n^2 - 1}{12}$.

**20.**
```python
import math

def detect_outliers(data):
    s = sorted(data)
    N = len(s)
    q1 = s[math.ceil(N / 4) - 1]
    q3 = s[math.ceil(3 * N / 4) - 1]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return {"Q1": q1, "Q3": q3, "IQR": iqr, "outliers": outliers}
```

---

### The Question That Opens What Follows

We now know how to describe and summarize empirical data collected from past trials.
Yet how do we advance from describing observed facts to **predicting the future**?
How do we determine the true probability that a patient is genuinely ill when a medical diagnostic test with 99% accuracy lights up positive? Why does our natural intuition about chance deceive us so consistently?
That is the great crossroads of **conditional probability** and **Bayes' formula**, in the next chapter.
