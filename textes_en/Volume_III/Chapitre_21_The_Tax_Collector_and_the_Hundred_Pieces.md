# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)
## CHAPTER 21: The Tax Collector and the Hundred Pieces

> *“How can one compare the contribution of a poor woodcutter who surrenders three silver coins out of ten to that of an opulent merchant who yields thirty out of one hundred and fifty? To render justice blind and compare the incomparable, the human mind forged a magic mirror where every crowd is reduced to an ideal assembly of one hundred citizens.”*

---

### What You Are About to Discover

- Why a **percentage** is simply a fraction in disguise with a denominator of one hundred ($\% = \frac{\dots}{100}$).
- The two essential gestures: **applying** a percentage (taking $p\%$ of a quantity) and **calculating** a percentage rate ($\frac{\text{part}}{\text{total}} \times 100$).
- The master secret of **multiplier coefficients** for percentage increases ($1 + \frac{t}{100}$) and decreases ($1 - \frac{t}{100}$).
- The foundational vocabulary of statistics: **population**, **individual**, **variable**, **frequencies**, and **counts**.
- Standard graphic representations: **bar charts**, **histograms**, and **pie charts**.
- The three key summary indicators of statistical data: the **mean**, the **median**, and the **range**.
- 🛠️ The Boundary Case Laboratory: successive percentage changes, Simpson's Paradox, and why the mean can disguise reality.

---

### 1. The Problem: The Medieval Trade Fair and the Quarrel of Merchants

We are in the 13th century, in the heart of Champagne, during the great Trade Fair of Troyes. Merchants from Venice, Flanders, and Castile have raised hundreds of striped canvas stalls overflowing with fragrant spices, silk bolts, fine wools, and embossed leathers.

At the end of the week, the **Count’s chief tax collector** sits behind a heavy oak table with his iron-bound chest and leather ledger. Two fabric merchants present themselves before his quill to settle the tax on their earnings.

- Merchant **Geoffroy** achieved a modest profit of **150 silver ecus**. The collector levies a tax of **30 ecus**.
- Merchant **Barthélemy**, a wealthy Flemish draper, amassed an opulent profit of **400 silver ecus**. The collector levies a tax of **72 ecus**.

Barthélemy slams his fist onto the oak table in indignation:  
*“This is an outrageous injustice! You take 72 ecus from me while demanding a mere 30 from Geoffroy! I am paying more than double what he pays!”*

Geoffroy shoots back indignantly:  
*“Come now, Barthélemy! You earned an enormous fortune compared to my humble shop! My 30 ecus represent a painful butchery of my meager earnings, while your 72 ecus are a mere drop in your golden vaults!”*

```
         Geoffroy (Small merchant)                 Barthélemy (Wealthy merchant)
     ┌────────────────────────┐ (150 ecus)     ┌────────────────────────────────────────┐ (400 ecus)
     │ Tax: 30 ecus  │        │                │ Tax: 72 ecus   │                       │
     └────────────────────────┘                └────────────────────────────────────────┘
          Part = 30 / 150                           Part = 72 / 400
```

The provost of the fair is summoned to judge the dispute. Who is truly taxed more heavily?

To answer with true mathematical justice, one cannot merely compare the raw number of coins surrendered (72 versus 30). One must compare the **proportional share** surrendered relative to total profits earned:
- For Geoffroy: $\frac{30}{150} = \frac{3}{15} = \frac{1}{5} = 0.20$.
- For Barthélemy: $\frac{72}{400} = \frac{18}{100} = 0.18$.

Imagine that each merchant had earned a standardized benchmark purse of **100 ecus**:
- Geoffroy would have surrendered **20 ecus per hundred ecus earned**.
- Barthélemy would have surrendered only **18 ecus per hundred ecus earned**!

It is Geoffroy who bears the heavier burden!  
To compare parts originating from groups of completely different sizes, humanity invented a universal standard benchmark denominator: **the number one hundred**. This is the birth of the **percentage**.

---

### 2. The Percentage: A Fraction over One Hundred

#### 2.1 Notation and Meaning

> **📐 Definition — Percentage**  
> A **percentage** is a standardized way of writing a fraction whose **denominator is equal to 100**:
> $$t\% = \frac{t}{100}$$
> The symbol **$\%$** reads aloud as **“percent”** (literally *“per hundred”*).

- $50\% = \frac{50}{100} = \frac{1}{2} = 0.5$ (one half).
- $25\% = \frac{25}{100} = \frac{1}{4} = 0.25$ (one quarter).
- $75\% = \frac{75}{100} = \frac{3}{4} = 0.75$ (three quarters).
- $10\% = \frac{10}{100} = \frac{1}{10} = 0.1$ (one tenth).
- $100\% = \frac{100}{100} = 1$ (the entirety, the whole).

> **💡 Where Did the Symbol $\%$ Come From?**  
> In 15th-century Italy, merchant scribes abbreviated the phrase *per cento* as *p. 100* or *p. c.*. Over centuries of rapid quill-work, the letter *p* vanished, the horizontal fraction stroke tilted into a forward slash, and the two zeros of 100 perched above and below the bar, giving birth to our modern $\%$ sign.

#### 2.2 The Two Foundational Computations

| Question Asked | What We Seek | Standard Formula |
|---|---|---|
| **Applying a percentage:**<br>“What is $p\%$ of quantity $Q$?” | A **concrete amount** (in \$, in kg, in students…) | $\text{Result} = Q \times \frac{p}{100}$ |
| **Finding a percentage rate:**<br>“What proportion does part $A$ represent within total $T$?” | A **rate in $\%$** | $\text{Rate } t\% = \frac{A}{T} \times 100$ |

---

### 3. Percentage Changes and Multiplier Coefficients

In everyday commerce (store sales, price inflation, tax levies), quantities do not remain static: they **increase** or **decrease** by a certain percentage.

#### 3.1 The Traditional Two-Step Method
A winter jacket costs $\$80$. The store advertises a $30\%$ discount.
1. Calculate the dollar discount:
   $$\text{Discount} = 80 \times \frac{30}{100} = \$24$$
2. Subtract discount from the original price:
   $$\text{New Price} = 80 - 24 = \$56$$

#### 3.2 The Master Tool: The Multiplier Coefficient
Notice that we can factor this calculation into a single, lightning-fast multiplication:
$$\text{New Price} = 80 - 80 \times \frac{30}{100} = 80 \times \left(1 - \frac{30}{100}\right) = 80 \times 0.70 = \$56$$

Paying with a $30\%$ discount is mathematically identical to paying **$70\%$ of the original price**!

> **📐 Theorem — Multiplier Coefficients**  
> - To **increase** a quantity by $t\%$, multiply it by:
>   $$C = 1 + \frac{t}{100}$$
>   *(Example: a $20\%$ increase $\implies \times 1.20$; a $5\%$ increase $\implies \times 1.05$)*  
>  
> - To **decrease** a quantity by $t\%$, multiply it by:
>   $$C = 1 - \frac{t}{100}$$
>   *(Example: a $15\%$ discount $\implies \times 0.85$; a $40\%$ discount $\implies \times 0.60$)*

---

### 4. Statistics: Making Numbers Speak

When a city, a medical center, or a school gathers thousands of individual data points (student heights, employee salaries, exam test scores), the human brain cannot extract meaningful wisdom from an unorganized list of raw numbers.  
**Statistics** is the mathematical discipline that organizes, summarizes, and illuminates large bodies of information.

#### 4.1 Statistical Vocabulary
- The **population**: the entire collection of individuals or objects under study (e.g., *all students in 7th Grade*).
- An **individual**: a single member of that population (e.g., *student Thomas*).
- The **variable** (or characteristic): the specific property observed for each individual (e.g., *score on the math exam out of 20*).
- The **frequency count** (or absolute frequency) of a value: the number of times that specific value occurs.
- The **total sample size** ($N$): the total number of individuals in the population.
- The **relative frequency** of a value: the proportion of individuals possessing that value:
  $$f = \frac{\text{count}}{\text{total sample size } N}$$
  Relative frequency is expressed as a decimal between 0 and 1, or as a percentage ($f \times 100$).  
  **The sum of all relative frequencies across a population is always strictly equal to 1 ($100\%$).**

#### 4.2 Three Standard Graphic Displays

```
   1. BAR CHART                   2. HISTOGRAM (grouped bins)     3. PIE CHART
        Count                          Count
        ▲                              ▲                                   .---.
      6 |    |                       6 |    ┌───┐                        .'     '.
      4 |    |   |                   4 | ┌──┤   ├───┐                   / 40% \ 25%/
      2 |  | | | |                   2 | │  │   │   │                  |-------●---|
      0 └──┴─┴─┴─┴─►                 0 └─┴──┴───┴───┴─►                 \  35% /   /
          8 10 12 15                     [0;5) [5;10) [10;15)            '.     .'
             Scores                          Intervals                     '---'
```

In a **pie chart**, the surface area and central angle of each slice are strictly proportional to its frequency:
$$\text{Central Angle in Degrees} = \text{Relative Frequency } f \times 360^\circ$$

---

### 5. The Three Guardians of Data: Mean, Median, and Range

To summarize an entire statistical distribution in a few representative numbers, statisticians rely on three major indicators:

#### 5.1 The Arithmetic Mean ($\bar{x}$)
The **mean** (commonly called the average) is the fair-share value each individual would receive if all values were pooled together and redistributed equally.
- **Simple Mean:**
  $$\bar{x} = \frac{\text{sum of all data values}}{\text{total number of values } N}$$
- **Weighted Mean (with frequencies or course credits):**
  $$\bar{x} = \frac{(n_1 \times x_1) + (n_2 \times x_2) + \dots + (n_k \times x_k)}{N}$$

#### 5.2 The Median ($Me$): The Justice of the Midpoint
The **median** is the exact central value that partitions an ordered data set into two groups of identical size:
- At least $50\%$ of individuals have a value less than or equal to the median.
- At least $50\%$ of individuals have a value greater than or equal to the median.

> **🧭 Method — Finding the Median of a Data Set**  
> 1. You **must first sort** all data values in ascending order (from smallest to largest).  
> 2. Determine half the sample size: $\frac{N}{2}$.  
>    - **Case 1: $N$ is odd ($N = 2k + 1$):**  
>      The median is the unique value located at rank $k + 1$.  
>      *(Example: $N = 7 \implies \frac{7}{2} = 3.5$. The median is the 4th value).*  
>    - **Case 2: $N$ is even ($N = 2k$):**  
>      The median is the average of the $k$-th and $(k+1)$-th values.  
>      *(Example: $N = 8 \implies \frac{8}{2} = 4$. Median $= \frac{\text{4th value} + \text{5th value}}{2}$).*

#### 5.3 The Range ($R$): Measuring Dispersion
The **range** measures the overall spread or dispersion of the data set:
$$R = \text{Maximum Value} - \text{Minimum Value}$$
A small range indicates that values are clustered tightly together (homogeneous group). A large range indicates substantial disparity.

---

### 6. Beware of Pitfalls!

> **⚠️ Warning: Statistical Illusions!**  
> 1. **The Consecutive Increase and Decrease Trap:**  
>    *“If an item rises in price by $20\%$ and subsequently drops by $20\%$, does it return to its original price?”*  
>    **ABSOLUTELY NOT, NEVER!**  
>    Test with an initial price of $\$100$:  
>    - $20\%$ increase $\implies 100 \times 1.20 = \$120$.  
>    - $20\%$ decrease on $\$120 \implies 120 \times (1 - 0.20) = 120 \times 0.80 = \mathbf{\$96}$!  
>    You lost $\$4$, because the $20\%$ drop was calculated on a larger base amount!  
> 2. **Adding Percentages from Different Groups:**  
>    If Class A has 20 students with $50\%$ girls, and Class B has 30 students with $40\%$ girls, the combined proportion of girls is NOT $50\% + 40\% = 90\%$, nor is it $\frac{50+40}{2} = 45\%$!  
>    You must count actual human beings: $10 + 12 = 22$ girls out of $50$ students total, which is $\frac{22}{50} = 44\%$.  
> 3. **Confusing Mean and Median:**  
>    In a small workshop of 5 people, 4 workers earn $\$1,500$ per month, while the owner earns $\$21,000$.  
>    - Mean salary: $\frac{4 \times 1,500 + 21,000}{5} = \frac{27,000}{5} = \mathbf{\$5,400}$!  
>    - Median salary: the 3rd person earns **$\$1,500$**.  
>    The mean gives the deceptive impression that everyone is well-off. The median reflects the true economic reality of the majority!

---

### 7. Solved Examples

#### Solved Example 1 — Applying a Percentage in a Bakery Recipe
To make $1.2\text{ kg}$ of brioche dough, a baker uses $55\%$ flour, $20\%$ butter, $15\%$ eggs, and $10\%$ sugar and yeast.  
What mass of butter (in grams) must the baker weigh?

*Solution:*  
- Convert total mass to grams: $1.2\text{ kg} = 1,200\text{ g}$.  
- Butter share: $20\%$.  
- Calculation:  
  $$\text{Mass of butter} = 1,200 \times \frac{20}{100} = 1,200 \times 0.20 = 240\text{ grams}$$  
The baker must weigh $240\text{ g}$ of butter. ✔

#### Solved Example 2 — Calculating an Exam Pass Rate
In a middle school, 138 eighth-grade students sat for the national diploma exam.  
124 of them passed successfully.  
What was the pass rate for this school? Round to the nearest tenth of a percent.

*Solution:*  
- Successful candidates (part): $A = 124$.  
- Total cohort (whole): $T = 138$.  
- Rate:  
  $$t = \frac{A}{T} \times 100 = \frac{124}{138} \times 100 \approx 0.89855 \times 100 \approx 89.9\%$$  
The diploma pass rate was $89.9\%$. ✔

#### Solved Example 3 — Winter Sales and Multiplier Coefficients
A sporting goods store applies a $40\%$ discount to running shoes originally priced at $\$115$.  
What is the discounted price?

*Solution:*  
- Multiplier coefficient for a $40\%$ decrease:  
  $$C = 1 - \frac{40}{100} = 1 - 0.40 = 0.60$$  
- Discounted price:  
  $$\text{Sale Price} = 115 \times 0.60 = \$69$$  
The shoes now cost $\$69$. ✔

#### Solved Example 4 — Full Statistical Analysis of an Exam
Here are the scores out of 20 earned by 25 students on a mathematics exam:

| Score ($x_i$) | 8 | 10 | 12 | 14 | 16 | 18 | Total |
|---|---|---|---|---|---|---|---|
| Count ($n_i$) | 3 | 5 | 7 | 6 | 3 | 1 | 25 |
| Frequency $\%$ | ? | ? | ? | ? | ? | ? | $100\%$ |
| Central Angle | ? | ? | ? | ? | ? | ? | $360^\circ$ |

1. Complete the frequencies and angles for a pie chart.  
2. Calculate the class mean score.  
3. Determine the median score and the score range.

*Solution:*  
1. For each score, relative frequency is $\frac{n_i}{25} \times 100\%$ and angle is $\frac{n_i}{25} \times 360^\circ$:  
   - Score 8: Frequency $= \frac{3}{25} = 12\%$; Angle $= 0.12 \times 360^\circ = 43.2^\circ$.  
   - Score 10: Frequency $= \frac{5}{25} = 20\%$; Angle $= 0.20 \times 360^\circ = 72^\circ$.  
   - Score 12: Frequency $= \frac{7}{25} = 28\%$; Angle $= 0.28 \times 360^\circ = 100.8^\circ$.  
   - Score 14: Frequency $= \frac{6}{25} = 24\%$; Angle $= 0.24 \times 360^\circ = 86.4^\circ$.  
   - Score 16: Frequency $= \frac{3}{25} = 12\%$; Angle $= 0.12 \times 360^\circ = 43.2^\circ$.  
   - Score 18: Frequency $= \frac{1}{25} = 4\%$; Angle $= 0.04 \times 360^\circ = 14.4^\circ$.  
2. **Weighted Mean:**  
   $$\bar{x} = \frac{3 \times 8 + 5 \times 10 + 7 \times 12 + 6 \times 14 + 3 \times 16 + 1 \times 18}{25}$$  
   $$\bar{x} = \frac{24 + 50 + 84 + 84 + 48 + 18}{25} = \frac{308}{25} = 12.32$$  
   The class mean is $12.32 / 20$.  
3. **Median and Range:**  
   - Total sample size $N = 25$ (odd).  
   - $\frac{25 + 1}{2} = 13$. The median is the **13th score** in ascending order.  
   - Cumulative counts:  
     - Scores up to 8: 3 students.  
     - Scores up to 10: $3 + 5 = 8$ students.  
     - Scores up to 12: $8 + 7 = 15$ students.  
     The 13th score lies in the score 12 group! Thus, median $Me = \mathbf{12}$.  
   - **Range:** $R = 18 - 8 = \mathbf{10}$ points. ✔

#### Solved Example 5 — Successive Percentage Increases
The price of gasoline rises by $10\%$ in January, then rises by an additional $10\%$ in February.  
1. What is the total percentage increase over the two-month period?  
2. What is the new price of a liter originally costing $\$1.50$?

*Solution:*  
1. Multiply the respective multiplier coefficients:  
   $$C_1 = 1 + 0.10 = 1.10$$  
   $$C_2 = 1 + 0.10 = 1.10$$  
   $$C_{\text{overall}} = 1.10 \times 1.10 = 1.21$$  
   Since $1.21 = 1 + \frac{21}{100}$, the overall increase is **$21\%$** (not $20\%$)!  
2. Final price per liter:  
   $$P_{\text{final}} = 1.50 \times 1.21 = \$1.815 \approx \$1.82$$  
The liter of fuel now costs $\$1.815$. ✔

---

### What You Must Remember

1. **Percentage Concepts:**  
   - $t\% = \frac{t}{100}$.  
   - Calculate $p\%$ of $Q$: $Q \times \frac{p}{100}$.  
   - Find percentage rate: $\frac{\text{Part}}{\text{Total}} \times 100$.
2. **Multiplier Coefficients:**  
   - Increase of $t\%$: multiply by $\left(1 + \frac{t}{100}\right)$.  
   - Decrease of $t\%$: multiply by $\left(1 - \frac{t}{100}\right)$.  
   - Consecutive changes: **multiply** coefficients ($C_{\text{total}} = C_1 \times C_2$).
3. **Statistical Indicators:**  
   - **Relative Frequency:** $f = \frac{\text{count}}{N}$.  
   - **Pie Chart Angle:** $\text{Angle} = f \times 360^\circ$.  
   - **Mean ($\bar{x}$):** sum of all values divided by total count $N$.  
   - **Median ($Me$):** the midpoint value dividing sorted data into equal $50\% / 50\%$ halves.  
   - **Range ($R$):** $\text{maximum value} - \text{minimum value}$.

---

### Exercises

#### Level ★ (Direct Application)

**Exercise 1.** Express each percentage as a simplified fraction, then as a decimal:  
$10\%$; $20\%$; $25\%$; $50\%$; $75\%$; $5\%$.

**Exercise 2.** Compute mentally:  
1. $50\%$ of $\$84$  
2. $25\%$ of $120\text{ kg}$  
3. $10\%$ of $350\text{ m}$  
4. $1\%$ of $2,500\text{ citizens}$

**Exercise 3.** State the multiplier coefficient associated with:  
1. A price increase of $12\%$  
2. A discount of $25\%$  
3. A tax increase of $3.5\%$  
4. A clearance markdown of $50\%$

**Exercise 4.** In a box of 40 gourmet chocolates, 14 are dark chocolate. What percentage of the box is dark chocolate?

**Exercise 5.** Calculate the simple arithmetic mean of the five test scores: $11$, $14$, $9$, $17$, $14$.

#### Level ★★ (Reasoning and Statistical Problems)

**Exercise 6. Discounted Smartphone.**  
A smartphone retails for $\$340$. During a seasonal promotion, its price is marked down by $15\%$.  
1. What is the cash savings in dollars?  
2. What is the new promotional price?

**Exercise 7. Electricity Bill and Sales Tax.**  
On an electricity bill of $\$150$ before tax, the state levies a sales tax (VAT) of $20\%$.  
What is the total amount paid by the customer?

**Exercise 8. The Deceptive Reversal.**  
A train ticket increases in price by $25\%$. A few months later, the railway company offers a “$25\%$ immediate discount” promotion.  
A traveler believes the ticket has returned to its initial price. Is he correct? Justify with an exact calculation starting from a $\$100$ ticket.

**Exercise 9. Finding Medians (Odd vs. Even Sample Sizes).**  
Find the median and range for each of the two weekly noon temperature records:  
- Week A: $14^\circ\text{C}$, $17^\circ\text{C}$, $12^\circ\text{C}$, $19^\circ\text{C}$, $21^\circ\text{C}$, $15^\circ\text{C}$, $18^\circ\text{C}$.  
- Week B: $13^\circ\text{C}$, $16^\circ\text{C}$, $11^\circ\text{C}$, $20^\circ\text{C}$, $14^\circ\text{C}$, $18^\circ\text{C}$.

**Exercise 10. Neighborhood Pet Survey Pie Chart.**  
A survey of 180 neighborhood households records pet ownership:  
- 72 households own a dog.  
- 54 households own a cat.  
- 36 households own rodents or birds.  
- 18 households own no pets.  
1. Calculate the percentage frequency for each category.  
2. Calculate the central angle in degrees for each category to construct a pie chart.

**Exercise 11. Weighted Academic Average.**  
A middle school student earns the following grades in mathematics:  
- Two short quizzes (weight 1 each): $12$ and $15$.  
- Two major exams (weight 3 each): $14$ and $10$.  
What is her weighted quarterly grade point average?

#### Level ★★★ (Challenges and Critical Thinking)

**Exercise 12. The Factory Salary Paradox.**  
A small manufacturing plant employs 20 individuals:  
- 1 CEO earning $\$10,000$ per month.  
- 3 senior engineers earning $\$4,000$ per month each.  
- 16 assembly workers earning $\$1,500$ per month each.  
1. Calculate the mean monthly salary across the company.  
2. Calculate the median monthly salary.  
3. Why would management and a labor union choose different statistical indicators during wage negotiations? Explain the manipulative power of the arithmetic mean.

**Exercise 13. Reverse Percentage (Finding the Original Price).**  
After receiving a $20\%$ discount during a sale, a winter coat costs $\$120$.  
What was its original price before the sale?  
*(Warning: do NOT compute $\$120 + 20\%$ of $\$120$! Use the multiplier coefficient).*

**Exercise 14. Consecutive Percentage Changes.**  
The price of a gaming console increases by $5\%$ in 2024, then rises by an additional $8\%$ in 2025.  
1. What is the overall percentage increase over the two-year period?  
2. If the price then drops by $12\%$ in 2026, is the console ultimately more expensive or less expensive than at the start of 2024?

**Exercise 15. Simpson's Paradox in Surgery.**  
In a major hospital, two surgeons (Dr. Martin and Dr. Dupont) perform two types of procedures: low-risk routine surgeries and high-risk complex surgeries.  
- Low-risk surgeries:  
  - Dr. Martin succeeds in 95 out of 100 cases ($95\%$).  
  - Dr. Dupont succeeds in 19 out of 20 cases ($95\%$).  
- High-risk surgeries:  
  - Dr. Martin succeeds in 10 out of 20 cases ($50\%$).  
  - Dr. Dupont succeeds in 45 out of 100 cases ($45\%$).  
1. For high-risk surgeries alone, which surgeon has the superior success rate?  
2. Calculate the overall success rate for each surgeon combining all procedures.  
3. Which surgeon has the higher overall success rate? What astonishing contradiction do you notice? Explain this statistical paradox.

---

### Solutions

**Exercise 1.**  
- $10\% = \frac{1}{10} = 0.10$  
- $20\% = \frac{1}{5} = 0.20$  
- $25\% = \frac{1}{4} = 0.25$  
- $50\% = \frac{1}{2} = 0.50$  
- $75\% = \frac{3}{4} = 0.75$  
- $5\% = \frac{1}{20} = 0.05$

**Exercise 2.**  
1. $84 / 2 = \$42$.  
2. $120 / 4 = 30\text{ kg}$.  
3. $350 / 10 = 35\text{ m}$.  
4. $2,500 / 100 = 25\text{ citizens}$.

**Exercise 3.**  
1. $1 + 0.12 = 1.12$.  
2. $1 - 0.25 = 0.75$.  
3. $1 + 0.035 = 1.035$.  
4. $1 - 0.50 = 0.50$.

**Exercise 4.**  
Rate $= \frac{14}{40} \times 100 = \frac{7}{20} \times 100 = 35\%$.

**Exercise 5.**  
Sum $= 11 + 14 + 9 + 17 + 14 = 65$.  
Mean $= \frac{65}{5} = 13 / 20$.

**Exercise 6.**  
1. Savings: $340 \times 0.15 = \$51$.  
2. New price: $340 - 51 = \$289$ (or $340 \times 0.85 = \$289$).

**Exercise 7.**  
Total bill $= 150 \times (1 + 0.20) = 150 \times 1.20 = \$180$.

**Exercise 8.**  
Initial price: $\$100$.  
After $25\%$ increase: $100 \times 1.25 = \$125$.  
After $25\%$ decrease: $125 \times 0.75 = \$93.75$.  
The traveler is mistaken: the ticket costs $\$93.75$, which is $\$6.25$ cheaper than the original price!

**Exercise 9.**  
- **Week A (7 values):** Sorted: $12, 14, 15, \mathbf{17}, 18, 19, 21$.  
  Median $= \mathbf{17^\circ\text{C}}$ (the 4th value).  
  Range $= 21 - 12 = 9^\circ\text{C}$.  
- **Week B (6 values):** Sorted: $11, 13, \mathbf{14}, \mathbf{16}, 18, 20$.  
  Median $= \frac{14 + 16}{2} = \mathbf{15^\circ\text{C}}$.  
  Range $= 20 - 11 = 9^\circ\text{C}$.

**Exercise 10.**  
Total $N = 180$.  
1. Frequencies:  
   - Dogs: $\frac{72}{180} = 40\%$.  
   - Cats: $\frac{54}{180} = 30\%$.  
   - Rodents/birds: $\frac{36}{180} = 20\%$.  
   - None: $\frac{18}{180} = 10\%$.  
2. Central Angles:  
   - Dogs: $0.40 \times 360^\circ = 144^\circ$.  
   - Cats: $0.30 \times 360^\circ = 108^\circ$.  
   - Rodents/birds: $0.20 \times 360^\circ = 72^\circ$.  
   - None: $0.10 \times 360^\circ = 36^\circ$.

**Exercise 11.**  
Sum of weights: $1 + 1 + 3 + 3 = 8$.  
Mean $= \frac{1 \times 12 + 1 \times 15 + 3 \times 14 + 3 \times 10}{8} = \frac{12 + 15 + 42 + 30}{8} = \frac{99}{8} = 12.375 / 20$.

**Exercise 12.**  
1. Total payroll: $1 \times 10,000 + 3 \times 4,000 + 16 \times 1,500 = 10,000 + 12,000 + 24,000 = \$46,000$.  
   Mean salary: $\frac{46,000}{20} = \mathbf{\$2,300}$.  
2. Sorted salaries: the bottom 16 employees earn $\$1,500$. The 10th and 11th values are both $\$1,500$.  
   Median salary: $\mathbf{\$1,500}$.  
3. The director will highlight the mean ($\$2,300$) to claim: *“Our workers earn generous wages on average,”* even though $80\%$ earn only $\$1,500$! The union will point to the median ($\$1,500$) to demonstrate that at least half the workforce earns only base pay.

**Exercise 13.**  
Let $P_0$ be the initial price. A $20\%$ discount corresponds to multiplier $1 - 0.20 = 0.80$.  
$P_0 \times 0.80 = 120 \implies P_0 = \frac{120}{0.80} = \$150$.  
The original price was $\$150$! (Check: $\$150 - 20\% \text{ of } 150 = 150 - 30 = \$120$).

**Exercise 14.**  
1. $C_{\text{overall}} = (1 + 0.05) \times (1 + 0.08) = 1.05 \times 1.08 = 1.134$.  
   Overall increase: $1.134 - 1 = 0.134 = \mathbf{+13.4\%}$ (not $13\%$).  
2. With the $12\%$ discount ($C_3 = 0.88$):  
   $C_{\text{final}} = 1.134 \times 0.88 = 0.99792$.  
   Since $0.99792 < 1$, the console is ultimately **slightly less expensive** than at the start of 2024 (a net decrease of $0.208\%$).

**Exercise 15.**  
1. High-risk surgeries: Dr. Martin has $50\%$, Dr. Dupont has $45\%$. **Dr. Martin** has the higher success rate.  
2. Combined rates:  
   - Dr. Martin: successes $= 95 + 10 = 105$ out of $100 + 20 = 120$ operations.  
     Overall rate $= \frac{105}{120} = 0.875 = \mathbf{87.5\%}$.  
   - Dr. Dupont: successes $= 19 + 45 = 64$ out of $20 + 100 = 120$ operations.  
     Overall rate $= \frac{64}{120} \approx 0.533 = \mathbf{53.3\%}$.  
3. Dr. Martin has an overall success rate of $87.5\%$ versus $53.3\%$ for Dr. Dupont!  
   The paradox: for routine cases, both surgeons have identical success rates ($95\%$). For high-risk cases, Dr. Martin is superior ($50\%$ vs. $45\%$). And overall, Dr. Martin dramatically outperforms Dr. Dupont!  
   Explanation: Dr. Martin performed $83\%$ of his surgeries on easy, low-risk patients, whereas Dr. Dupont took on $83\%$ high-risk, dangerous operations. This famous statistical phenomenon is known as **Simpson's Paradox**: an unobserved confounding variable (the underlying severity of cases) distorts the aggregate comparison!

---

### The Question That Opens What Follows

We have arrived at the conclusion of Volume III. We now know how to measure the earth, lay out right angles with compass and rope, compute inaccessible heights with Thales and Pythagoras, navigate Cartesian planes with signed coordinates, and synthesize crowds of data with percentages and statistics.

Yet up to this point, all our numbers were known, or uncovered through direct arithmetic.  
What happens when a problem hides a secret unknown quantity inside a sealed velvet bag resting upon a balance scale, tangled in a web of additions and multiplications?

How do we forge a new mathematical language where unknown numbers are represented by letters like $x$, and where the scales of justice transform into algebraic equations?  
That is the great threshold into the adolescence of mathematics: **Volume IV and the Mystery Bag on the Balance of Al-Khwarizmi**!
