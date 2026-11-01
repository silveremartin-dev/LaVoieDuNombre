# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 53: The Combination Lock and Ways of Choosing

> *“Nothing is more deceptive than our intuition regarding the number of possibilities: the human mind goes astray as soon as choices multiply. Yet the moment reason structures the spectrum—ordering or mingling, repeating or excluding—the boundless maze becomes a crystal edifice governed by humble factorials.”*

---

### What You Are About to Discover

- How to count without ever enumerating millions of objects one by one, using two foundational laws: the **addition principle** and the **multiplication principle**.
- The crucial distinction governing all combinatorics: **does order matter?** and **can elements be repeated?**
- **$k$-tuples**, **permutations**, and **arrangements (partial permutations)**, articulated around the spectacular factorial function $n!$.
- **Combinations** $\binom{n}{k}$ (“$n$ choose $k$”), **Pascal's triangle**, and their properties of symmetry and recurrence.
- The power of **Newton's binomial theorem**, expanding instantly any power of a binomial sum $(a+b)^n$.
- Classic overcounting pitfalls and the strategy of taking the **complementary event**.

---

### 1. The Problem: Counting the Invisible

#### 1.1 The Locker Padlock
Imagine a 4-dial bicycle padlock, each dial carrying digits from 0 to 9. You have forgotten the combination. How many attempts would you need, in the worst case, to be certain of opening it?
For the first digit, 10 choices. For the second, 10 choices. For the third, 10 choices. For the fourth, 10 choices.
The total number of possible codes is:
$$10 \times 10 \times 10 \times 10 = 10^4 = 10\,000.$$
At a rate of one attempt every 3 seconds without pause, it would take you more than 8 hours to test every code.

Now let us change a single rule: the manufacturer guarantees that **all 4 digits of a code are distinct** (no digit is repeated). How many codes remain?
- First digit: 10 possible choices.
- Second digit: only 9 choices (the one already used is forbidden).
- Third digit: 8 choices.
- Fourth digit: 7 choices.
The total drops to:
$$10 \times 9 \times 8 \times 7 = 5\,040 \text{ codes}.$$
Nearly half of the combinations vanished by the simple prohibition of repetition!

#### 1.2 The Bistro Menu
A bistro offers a lunch special: a choice of 3 appetizers, 4 main courses, and 3 desserts. How many different three-course meals (appetizer + main + dessert) can a customer compose?
Here, choosing an appetizer does not restrict in any way the choice of main course or dessert. The choices unfold independently:
$$3 \times 4 \times 3 = 36 \text{ different meals}.$$
If you had lunch there every weekday from Monday through Friday, it would take you over 7 weeks to exhaust every combination without ever eating the exact same meal twice!

#### 1.3 The Hand of Cards and the Sports Team
Now consider a different situation: a coach must select 3 runners among 10 available athletes to form a relay patrol.
Is selecting Alice, Bob, and Chloe different from selecting Chloe, Bob, and Alice?
**No.** The team is identical. The order in which the coach calls their names has no significance: they stand together on the track.

If we counted as we did for the lock without repetition ($10 \times 9 \times 8 = 720$), we would make a massive blunder: the trio {Alice, Bob, Chloe} would be counted multiple times:
- Alice, Bob, Chloe
- Alice, Chloe, Bob
- Bob, Alice, Chloe
- Bob, Chloe, Alice
- Chloe, Alice, Bob
- Chloe, Bob, Alice

Exactly 6 times the same team! The true number of possible teams is therefore not 720, but:
$$\frac{720}{6} = 120.$$

#### 1.4 The Combinatorial Challenge
These three scenarios lay the groundwork for a rigorous science: **combinatorics** (or the art of counting).
As soon as collections grow, it becomes physically impossible to draw up an exhaustive inventory of possibilities. If an urn holds 50 numbered balls and 5 are drawn, the number of possible draws exceeds two million.
The mathematician does not list: he **structures**, **categorizes**, and **calculates**.

---

### 2. Foundations: Finite Sets, Addition Principle, and Multiplication Principle

#### 2.1 Finite Sets and Cardinality
Let $E$ be a set. We say that $E$ is a **finite set** if it contains a finite integer number of elements.

> **📐 Definition — Cardinality of a Finite Set**
> The number of elements of a finite set $E$ is called the **cardinality** of $E$.
> It is denoted by $\text{Card}(E)$ or, more commonly in upper secondary and higher mathematics, $|E|$ or $\#E$.
> If $E = \emptyset$ (the empty set), then $|E| = 0$.

*Etymology and Notation:* The word *cardinal* comes from the Latin *cardo*, meaning “hinge, pivot”: it is the fundamental number on which the size of a collection pivots. The notation $|E|$ echoes the absolute value (which measures magnitude or distance).

#### 2.2 The Addition Principle: Partitions and Disjoint Sets

> **📐 Fundamental Property — Addition Principle**
> Let $A$ and $B$ be two finite subsets of a set $E$.
> If $A$ and $B$ are **disjoint** (meaning they share no common element: $A \cap B = \emptyset$), then:
> $$|A \cup B| = |A| + |B|$$
> More generally, if $A_1, A_2, \dots, A_m$ form a **partition** of $E$ (they are pairwise disjoint and their union equals all of $E$), then:
> $$|E| = |A_1| + |A_2| + \dots + |A_m| = \sum_{i=1}^m |A_i|$$

```
   Set E
 ┌──────────────────────────┐
 │  ┌────────┐  ┌────────┐  │
 │  │   A    │  │   B    │  │   A ∩ B = ∅
 │  │ 5 elem │  │ 7 elem │  │   |A ∪ B| = 5 + 7 = 12
 │  └────────┘  └────────┘  │
 └──────────────────────────┘
```

What if the two sets overlap?
This gives the celebrated Principle of Inclusion-Exclusion (for 2 sets):

> **📐 Theorem — Two-Set Inclusion-Exclusion Formula**
> For any finite sets $A$ and $B$:
> $$|A \cup B| = |A| + |B| - |A \cap B|$$

*Visual proof:* In adding $|A|$ and $|B|$, elements belonging to the intersection $A \cap B$ were counted twice. We must therefore subtract $|A \cap B|$ once to restore the exact tally.

> **🧭 Method — The Complement Principle**
> If $A$ is a subset of a finite universal set $E$, its complement $\overline{A}$ (or $E \setminus A$) satisfies:
> $$|A| + |\overline{A}| = |E| \iff |A| = |E| - |\overline{A}|$$
> **Golden Rule:** Whenever a problem contains the phrasing *“at least one…”*, it is almost always ten times faster to count the opposite (*“none at all…”*) and subtract from the total!

#### 2.3 The Multiplication Principle and the Cartesian Product

> **📐 Definition — Cartesian Product**
> Let $A$ and $B$ be two sets. The Cartesian product $A \times B$ is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$:
> $$A \times B = \{ (a, b) \mid a \in A, b \in B \}$$

> **📐 Theorem — Multiplication Principle**
> If $A$ and $B$ are two finite sets, then:
> $$|A \times B| = |A| \times |B|$$
> Generally, for $k$ finite sets $A_1, A_2, \dots, A_k$:
> $$|A_1 \times A_2 \times \dots \times A_k| = |A_1| \times |A_2| \times \dots \times |A_k| = \prod_{i=1}^k |A_i|$$

*The Tree of Choices:*
Each successive choice corresponds to a branching point. If the first stage offers $n_1$ branches, and from each branch sprout $n_2$ sub-branches, the total number of leaves at the end of the tree is $n_1 \times n_2$.

---

### 3. Order Matters: $k$-tuples, Permutations, and Factorials

#### 3.1 $k$-tuples (With Replacement / Repetition Allowed)
We draw $k$ objects from $n$, **one after the other**, replacing the drawn object back into the bag at each step (or reusing the same symbol, as on a combination dial).

> **📐 Theorem — Number of $k$-tuples**
> Let $E$ be a set of $n$ elements. A **$k$-tuple** (or list / sequence of length $k$) of elements of $E$ is an element of the Cartesian product $E^k = \underbrace{E \times E \times \dots \times E}_{k \text{ factors}}$.
> The number of $k$-tuples from a set of $n$ elements is:
> $$|E^k| = n^k$$

*Concrete Examples:*
- Number of possible bytes (8-bit binary words made of 0s and 1s): $2^8 = 256$.
- Number of 4-digit bank PIN codes: $10^4 = 10\,000$.
- Number of possible outcomes when tossing a coin 5 times (Heads or Tails): $2^5 = 32$.

#### 3.2 Arrangements / Partial Permutations ($k$-tuples of Distinct Elements, Without Repetition)
This time, we select $k$ elements from $n$ **one after the other**, but **without replacement**: each element can be chosen at most once.

> **📐 Definition & Theorem — Arrangements ($k$-permutations)**
> Let $E$ be a set of $n$ elements and $k$ an integer such that $0 \leq k \leq n$.
> An **arrangement** of $k$ elements from $E$ (or $k$-tuple of distinct elements) is an ordered list $(x_1, x_2, \dots, x_k)$ of pairwise distinct elements of $E$.
> The number of such arrangements is denoted by $A_n^k$ (or $P(n, k)$) and equals:
> $$A_n^k = n \times (n-1) \times (n-2) \times \dots \times (n - k + 1)$$

*Proof:*
For the 1st position, we have $n$ available candidates.
For the 2nd position, there remain $n - 1$ candidates.
For the 3rd position, there remain $n - 2$ candidates.
...
For the $k$-th position, there remain $n - (k - 1) = n - k + 1$ candidates.
By the multiplication principle, we multiply these integers together.

#### 3.3 Permutations and the Factorial Function $n!$
What happens when we take all elements, that is, when $k = n$?
We arrange all $n$ elements in order: this is a **permutation**.

> **📐 Definition & Theorem — Permutations and Factorial**
> A **permutation** of a set $E$ of $n$ elements is an arrangement of all elements of $E$ (an $n$-tuple of distinct elements of $E$).
> The number of permutations of an $n$-element set is denoted by $n!$ (read **“$n$ factorial”**):
> $$n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1$$
> By fundamental convention:
> $$0! = 1$$

*Notation Explained:*
The exclamation mark was introduced in 1808 by French mathematician **Christian Kramp** of Strasbourg, simply to abbreviate cumbersome typographic products.
Why is $0! = 1$?
1. **Combinatorial interpretation:** In how many ways can one order zero objects? Exactly one way: the empty sequence!
2. **Algebraic consistency:** For every $n \geq 1$, we have $n! = n \times (n-1)!$. Applying this formula for $n = 1$ gives $1! = 1 \times 0!$. Since $1! = 1$, we must set $0! = 1$ to preserve the integrity of arithmetic.

*Compact Expression for $A_n^k$:*
Notice that we can complete the product of $A_n^k$ down to 1:
$$A_n^k = \frac{n \times (n-1) \times \dots \times (n-k+1) \times (n-k) \times \dots \times 1}{(n-k) \times \dots \times 1} = \frac{n!}{(n-k)!}$$

> **💡 Did You Know? Factorial Explosion**
> The factorial grows with astonishing rapidity:
> - $3! = 6$
> - $5! = 120$
> - $10! = 3\,628\,800$
> - $52! \approx 8.06 \times 10^{67}$
> When you shuffle a deck of 52 cards thoroughly, the resulting order has almost certainly **never existed** in the entire history of humanity, and will likely never appear again before the Sun burns out!

---

### 4. Order Does Not Matter: Combinations $\binom{n}{k}$

#### 4.1 Handshakes and Subsets
In many practical situations, the order of presentation is meaningless:
- Drawing a 5-card poker hand (whether you receive the Ace of Spades first or last, you hold the Ace of Spades).
- Choosing 3 class representatives from a group of 30 students.
- Selecting 6 numbers out of 49 on a lottery ticket.

In these cases, the outcome is not a $k$-tuple (an ordered list in parentheses), but a **subset** of size $k$ (enclosed in curly braces $\{x_1, \dots, x_k\}$).

> **📐 Definition — Combinations**
> Let $E$ be a set with $n$ elements and $k$ an integer such that $0 \leq k \leq n$.
> A **combination** of $k$ elements from $n$ is a subset of $E$ having exactly $k$ elements.
> The number of such combinations is denoted by $\binom{n}{k}$ (read **“$n$ choose $k$”**).
> *(Older notation: $C_n^k$ or $C(n,k)$).*

#### 4.2 The Master Formula

> **✍️ Required Proof — Formula for $\binom{n}{k}$**
> Let us count the number of arrangements $A_n^k$ in two different ways:
> 1. On one hand, we know that the number of arrangements is $A_n^k = \frac{n!}{(n-k)!}$.
> 2. On the other hand, to construct an arrangement of $k$ elements (an ordered list), we can proceed in two stages:
>    - **Stage 1:** Choose the $k$ elements without regard to order. By definition, there are $\binom{n}{k}$ ways to do this.
>    - **Stage 2:** Order these $k$ chosen elements into a list. By Section 3.3, there are $k!$ ways to permute these $k$ elements.
>
> By the multiplication principle:
> $$A_n^k = \binom{n}{k} \times k!$$
> Isolating $\binom{n}{k}$ yields the fundamental theorem:
>
> $$\binom{n}{k} = \frac{A_n^k}{k!} = \frac{n!}{k!(n-k)!}$$

*Immediate Example:*
The number of 3-card hands from a deck of 10 cards:
$$\binom{10}{3} = \frac{10!}{3! \times 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120.$$
We recover our intuitive calculation from the locker room!

#### 4.3 Fundamental Properties of Combinations

1. **Notable Values:**
   $$\binom{n}{0} = 1 \quad \text{(a single empty set)}, \quad \binom{n}{1} = n, \quad \binom{n}{n} = 1$$

2. **Symmetry of Choices:**
   $$\binom{n}{k} = \binom{n}{n-k}$$

> **✍️ Proof — Symmetry**
> - **By algebraic computation:**
>   $$\binom{n}{n-k} = \frac{n!}{(n-k)!(n - (n-k))!} = \frac{n!}{(n-k)!k!} = \binom{n}{k}$$
> - **By combinatorial reasoning (pure elegance!):**
>   Choosing $k$ people out of $n$ to board a boat is exactly equivalent to designating the $n-k$ people who stay on the dock! To every group of $k$ chosen individuals corresponds a unique group of $n-k$ excluded individuals. There must be exactly as many ways to do one as the other.

#### 4.4 Pascal's Recurrence Relation

> **📐 Theorem — Pascal's Identity**
> For all integers $n \geq 1$ and $1 \leq k \leq n$:
> $$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

> **✍️ Required Combinatorial Proof — The Designated Witness Method**
> Let $E$ be a set with $n$ elements. Single out one particular individual in $E$, and call her **Alice**.
> We wish to choose a subset of $k$ members from these $n$ people. There are $\binom{n}{k}$ total ways.
> Partition these subsets into two mutually exclusive categories:
> - **Category 1: Committees that include Alice.**
>   Since Alice is already selected by decree, we only need to pick $k-1$ companions from the remaining $n-1$ people. There are $\binom{n-1}{k-1}$ ways to do this.
> - **Category 2: Committees that do not include Alice.**
>   Alice is excluded. We must choose all $k$ committee members entirely from the remaining $n-1$ people. There are $\binom{n-1}{k}$ ways.
>
> These two categories form a partition of all possible committees. By the addition principle:
> $$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$
> The formula is established without writing down a single algebraic fraction!

---

### 5. Pascal's Triangle and Newton's Binomial Theorem

#### 5.1 Construction of the Triangle
Pascal's identity $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ states that each entry is the sum of two numbers in the row immediately above: the one directly above, and the one directly above to the left.

```
 n \ k │  0    1    2    3    4    5    6    Row Sum
───────┼───────────────────────────────────  ───────
 n = 0 │  1                                    1 = 2⁰
 n = 1 │  1    1                               2 = 2¹
 n = 2 │  1    2    1                          4 = 2²
 n = 3 │  1    3    3    1                     8 = 2³
 n = 4 │  1    4    6    4    1               16 = 2⁴
 n = 5 │  1    5   10   10    5    1          32 = 2⁵
 n = 6 │  1    6   15   20   15    6    1     64 = 2⁶
```
Notice the rightmost column: the sum of all coefficients in row $n$ is always $2^n$!
Why?
Summing all $\binom{n}{k}$ for $k$ ranging from 0 to $n$ counts all possible subsets of an $n$-element set (subsets of size 0, size 1, size 2... up to size $n$).
For each element of a set, there are 2 choices: either it belongs to the subset, or it does not.
For $n$ elements, this yields $2 \times 2 \times \dots \times 2 = 2^n$ subsets (the power set $\mathcal{P}(E)$).

$$\sum_{k=0}^n \binom{n}{k} = 2^n$$

#### 5.2 Newton's Binomial Theorem

Recall the elementary polynomial expansions:
- $(a+b)^1 = a + b$
- $(a+b)^2 = a^2 + 2ab + b^2$
- $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$

Observe the coefficients:
- Row 1: $1, 1$
- Row 2: $1, 2, 1$
- Row 3: $1, 3, 3, 1$
These are precisely the rows of Pascal's triangle!

> **📐 Fundamental Theorem — Newton's Binomial Formula**
> For all real or complex numbers $a$ and $b$, and for every non-negative integer $n \in \mathbb{N}$:
> $$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$
> Written out in full:
> $$(a+b)^n = \binom{n}{0} a^n + \binom{n}{1} a^{n-1}b + \binom{n}{2} a^{n-2}b^2 + \dots + \binom{n}{n} b^n$$

> **✍️ Combinatorial Proof — Why the Formula is Self-Evident**
> Expand the product of $n$ identical binomial factors:
> $$(a+b)^n = \underbrace{(a+b)(a+b)\dots(a+b)}_{n \text{ factors}}$$
> Under complete distributivity, to form each term in the expansion, we must choose **either the letter $a$ or the letter $b$** from each of the $n$ factors.
> If we choose the letter $b$ from $k$ factors, we must necessarily choose the letter $a$ from the remaining $n-k$ factors. The resulting monomial is:
> $$a^{n-k} b^k$$
> How many times does this term $a^{n-k} b^k$ appear in the expansion?
> Exactly as many times as there are ways to select the $k$ factors providing the letter $b$ out of the $n$ factors available!
> This is the very definition of **“$n$ choose $k$”**, namely $\binom{n}{k}$.
> The formula is thus proved with total transparency.

---

### 6. Toolbox and Classical Traps

#### 6.1 The Decision Flowchart
When confronted with a combinatorial counting problem, **always** ask these two questions in sequence:

```
                   DOES ORDER MATTER?
                       /         \
                     YES          NO
                    /               \
         IS REPETITION ALLOWED?   IS REPETITION ALLOWED?
            /          \                    \
          YES           NO                   NO
          /              \                    \
      k-tuples      Arrangements         Combinations
        n^k            A_n^k             (n choose k)
                    = n!/(n-k)!        = n! / (k!(n-k)!)
                   (if k=n : n!)
```

#### 6.2 Fatal Pitfalls
> **⚠️ Warning, Trap! — Overcounting via False Decomposition**
> *Example:* In a class of 10 boys and 12 girls, we wish to form a group of 4 students containing **at least one girl**.
> - *Tempting False Reasoning:* “I choose 1 girl among 12 (12 ways), then choose the remaining 3 students from the 21 remaining students ($\binom{21}{3}$ ways). Total: $12 \times \binom{21}{3}$.”
> **This is wrong!** You have overcounted groups that contain more than one girl. For example, selecting Clara as the designated girl, then Sophie among the other 3, produces the exact same group as selecting Sophie first and Clara among the other 3.
> - *The Correct Method (Complementary Event):*
>   Count all possible groups of 4 without restriction: $\binom{22}{4}$.
>   Subtract groups containing **no girls at all** (i.e., 4 boys): $\binom{10}{4}$.
>   Exact count: $\binom{22}{4} - \binom{10}{4} = 7\,315 - 210 = 7\,105$.

> **🔍 True History — The Dice of Chevalier de Méré (1654)**
> Antoine Gombaud, known as the Chevalier de Méré—a nobleman and avid gambler—brought a puzzle to Blaise Pascal:
> *“Rolling a fair 6-sided die 4 times, I have better than an even chance of getting at least one 6. But rolling a pair of dice 24 times, I seem to have less than an even chance of getting a double 6. Yet $4/6 = 24/36$! Can mathematics be inconsistent?”*
> Pascal wrote to Pierre de Fermat. Through their historic correspondence, they analyzed the problem using the complement:
> 1. With 1 die in 4 rolls: probability of no 6s = $(5/6)^4 \approx 0.482$. Hence the probability of at least one 6 = $1 - 0.482 = 0.518 > 1/2$. (Favorable bet!)
> 2. With 2 dice in 24 rolls: probability of no double 6s = $(35/36)^{24} \approx 0.509$. Hence at least one double 6 = $1 - 0.509 = 0.491 < 1/2$. (Unfavorable bet!)
> The Chevalier was losing his money because of a naive ratio. Modern probability and combinatorics were born!

---

### 7. Step-by-Step Worked Examples

#### Example 1: Building Door Code
An apartment building keypad has keys 0 through 9, as well as letters A, B, C (13 keys in total). An entry code consists of 1 letter followed by 3 digits.
1. How many total codes can be formed?
2. How many codes if the 3 digits must all be distinct?
3. How many codes if the code begins with A and contains no even digits?

**Detailed Solution:**
1. A code is a 4-tuple $(L, d_1, d_2, d_3)$ belonging to $\{A,B,C\} \times \{0..9\}^3$.
   By the multiplication principle: $3 \times 10 \times 10 \times 10 = 3 \times 10^3 = 3\,000$ codes.
2. For the letter: 3 choices. For distinct digits, this is an arrangement of 3 digits chosen from 10: $A_{10}^3 = 10 \times 9 \times 8 = 720$.
   Total: $3 \times 720 = 2\,160$ codes.
3. The letter is fixed (A: 1 choice).
   Odd digits are $\{1, 3, 5, 7, 9\}$, giving 5 available digits.
   Since repetition is allowed, each digit position has 5 possibilities:
   Total: $1 \times 5^3 = 125$ codes.

#### Example 2: Examination Jury Composition
In a school, 15 science teachers and 12 humanities teachers volunteer to form an oral examination panel consisting of 4 examiners.
1. How many different panels can be constituted?
2. How many panels contain exactly 2 science teachers and 2 humanities teachers?
3. How many panels contain at least one teacher from each subject area?

**Detailed Solution:**
1. A panel is an unordered subset of 4 individuals chosen from the $15 + 12 = 27$ teachers. Order does not matter:
   $$\binom{27}{4} = \frac{27 \times 26 \times 25 \times 24}{4 \times 3 \times 2 \times 1} = 17\,550 \text{ panels}.$$
2. We independently choose 2 science teachers from 15, AND 2 humanities teachers from 12:
   $$\binom{15}{2} \times \binom{12}{2} = \frac{15 \times 14}{2} \times \frac{12 \times 11}{2} = 105 \times 66 = 6\,930 \text{ panels}.$$
3. The opposite of “at least one from each discipline” is “all science OR all humanities”.
   - Panels with science teachers only: $\binom{15}{4} = \frac{15 \times 14 \times 13 \times 12}{24} = 1\,365$.
   - Panels with humanities teachers only: $\binom{12}{4} = \frac{12 \times 11 \times 10 \times 9}{24} = 495$.
   These two cases are mutually exclusive, so the total non-mixed panels count is $1\,365 + 495 = 1\,860$.
   Subtracting from the overall total:
   $$17\,550 - 1\,860 = 15\,690 \text{ mixed panels}.$$

#### Example 3: Poker Hands
In a standard 52-card deck (4 suits: Spades, Hearts, Diamonds, Clubs; 13 ranks from Ace to King), a “hand” is a combination of 5 cards. The total number of hands is $\binom{52}{5} = 2\,598\,960$.
1. Count the number of “Four of a Kind” hands (4 cards of the same rank + 1 fifth card).
2. Count the number of “Full House” hands (3 cards of one rank + 2 cards of another rank).

**Detailed Solution:**
1. **Four of a Kind:**
   - Step 1: Choose the rank of the four cards among 13 possibilities: 13 choices.
   - Step 2: Take all 4 cards of that rank: $\binom{4}{4} = 1$ way.
   - Step 3: Choose the 5th card from the 48 remaining cards of different ranks: 48 choices.
   Total: $13 \times 1 \times 48 = 624$ possible Four of a Kind hands.
2. **Full House:**
   - Step 1: Choose the rank of the three-of-a-kind from the 13 ranks: 13 choices.
   - Step 2: Choose 3 suits out of 4 for this rank: $\binom{4}{3} = 4$ ways.
   - Step 3: Choose the rank of the pair from the remaining 12 ranks: 12 choices.
   - Step 4: Choose 2 suits out of 4 for this pair: $\binom{4}{2} = 6$ ways.
   Total: $13 \times 4 \times 12 \times 6 = 3\,744$ possible Full House hands.

#### Example 4: Anagrams with Repeated Letters
How many distinct anagrams (words, whether meaningful or not) can be formed with the letters of the word **PARALLELE**?

**Detailed Solution:**
The word contains 9 letters in total:
- P: 1 occurrence
- A: 2 occurrences
- R: 1 occurrence
- L: 3 occurrences
- E: 2 occurrences
Sum verification: $1 + 2 + 1 + 3 + 2 = 9$.
If all letters were distinct (e.g., $A_1, A_2, L_1, L_2, L_3$), there would be $9! = 362\,880$ permutations.
However, swapping the two A's among themselves does not change the word ($2!$ neutral permutations for A).
Similarly, permuting the three L's produces $3!$ identical arrangements, and the two E's produce $2!$.
By the formula for permutations with repetition:
$$\text{Number of anagrams} = \frac{9!}{1! \times 2! \times 1! \times 3! \times 2!} = \frac{362\,880}{1 \times 2 \times 1 \times 6 \times 2} = \frac{362\,880}{24} = 15\,120.$$
*(Equivalent viewpoint: choose the 3 positions for L out of 9 ($\binom{9}{3}$), then the 2 positions for A out of the 6 remaining ($\binom{6}{2}$), then the 2 positions for E out of 4 remaining ($\binom{4}{2}$), etc. The product gives exactly 15,120).*

#### Example 5: Grid Walks
In a square grid street layout, a pedestrian starts at $A(0,0)$ and heads to $B(5,3)$. At every intersection, he can only move East ($E$, one unit right) or North ($N$, one unit up).
How many minimal paths lead from $A$ to $B$?

```
 B(5,3)  ┌───┬───┬───┬───┬───┐
         │   │   │   │   │   │
         ├───┼───┼───┼───┼───┤
         │   │   │   │   │   │
         ├───┼───┼───┼───┼───┤
 A(0,0)  └───┴───┴───┴───┴───┘
```

**Detailed Solution:**
To travel from $(0,0)$ to $(5,3)$, any minimal path must consist of exactly 5 steps East ($E$) and 3 steps North ($N$).
The total length of each path is $5 + 3 = 8$ steps.
A path is uniquely determined by an 8-letter sequence containing five $E$'s and three $N$'s (for example: $E-E-N-E-N-E-E-N$).
It suffices to choose the positions of the 3 North steps among the 8 steps of the route:
$$\text{Number of paths} = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56.$$
*(Equivalently, choosing the 5 East positions: $\binom{8}{5} = \binom{8}{3} = 56$).*

#### Example 6: Finding a Term in a Binomial Expansion
In the expansion of $\left(2x^2 - \frac{1}{x}\right)^9$, determine the term independent of $x$ (the constant term).

**Detailed Solution:**
By Newton's binomial formula with $a = 2x^2$ and $b = -\frac{1}{x} = -x^{-1}$:
$$\left(2x^2 - \frac{1}{x}\right)^9 = \sum_{k=0}^9 \binom{9}{k} (2x^2)^{9-k} \left(-\frac{1}{x}\right)^k$$
Isolate powers of $x$ in the general term:
$$T_k = \binom{9}{k} 2^{9-k} (x^2)^{9-k} (-1)^k x^{-k} = \binom{9}{k} 2^{9-k} (-1)^k \cdot x^{18 - 2k - k} = \binom{9}{k} 2^{9-k} (-1)^k \cdot x^{18 - 3k}$$
The term is independent of $x$ when the exponent of $x$ is 0:
$$18 - 3k = 0 \iff 3k = 18 \iff k = 6.$$
Since $k = 6$ is an integer in the range $0 \le k \le 9$, this term exists. Its value is:
$$T_6 = \binom{9}{6} 2^{9-6} (-1)^6 = \binom{9}{3} \times 2^3 \times 1 = \frac{9 \times 8 \times 7}{6} \times 8 = 84 \times 8 = 672.$$
The constant term is **672**.

---

### Key Takeaways

1. **Basic Principles:**
   - Disjoint sets union: $|A \cup B| = |A| + |B|$.
   - Complement: $|A| = |E| - |\overline{A}|$ (always consider the opposite case for *“at least one”*).
   - Cartesian product: $|A \times B| = |A| \times |B|$.

2. **Counting with Order:**
   - With repetition ($k$-tuple): $n^k$.
   - Without repetition ($k$-permutations / arrangements): $A_n^k = \frac{n!}{(n-k)!} = n(n-1)\dots(n-k+1)$.
   - Permutation of $n$ elements: $n! = n \times (n-1) \times \dots \times 1$, with $0! = 1$.

3. **Counting without Order:**
   - Combinations of $k$ from $n$: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.
   - Symmetry: $\binom{n}{k} = \binom{n}{n-k}$.
   - Pascal's identity: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

4. **Sums and Powers:**
   - Row sum of Pascal's triangle: $\sum_{k=0}^n \binom{n}{k} = 2^n$.
   - Binomial theorem: $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 1.** Compute by hand: $5!$, $\frac{8!}{6!}$, $\binom{7}{2}$, $\binom{9}{9}$, and $\binom{10}{7}$.
**Exercise 2.** A computer password must consist of 8 characters selected from the 26 lowercase letters of the alphabet.
1. How many passwords can be formed if repetition is allowed?
2. How many if all letters must be distinct?
**Exercise 3.** A horse race starts with 12 horses. How many trifectas (podium predictions) are possible:
1. In exact finishing order?
2. Regardless of order (any 3 horses finishing in the top three)?
**Exercise 4.** Prove by direct calculation that $\binom{n}{2} = \frac{n(n-1)}{2}$. What does this quantity represent if $n$ people all shake hands with each other once?
**Exercise 5.** Expand using the binomial theorem:
1. $(x + 2)^4$
2. $(2x - 1)^3$
**Exercise 6.** How many anagrams can be formed with the letters of the word **MATHS**? What about the word **LIVRE**?
**Exercise 7.** An urn contains 6 red, 4 green, and 2 yellow balls. Three balls are drawn simultaneously. How many total draws are possible?

#### Level ★★ (Exploration and Standard Methods)

**Exercise 8.** Five fair 6-sided dice are rolled simultaneously (as in Yahtzee).
1. How many total distinct outcomes are possible?
2. How many outcomes contain no 6?
3. Deduce the number of outcomes containing at least one 6.
**Exercise 9.** How many 4-digit integers between 1000 and 9999 (inclusive):
1. Have all digits distinct?
2. Are even integers with all digits distinct?
**Exercise 10.** A chess club has 14 members: 8 adults and 6 juniors. A 5-player team must be chosen.
1. In how many ways can this team be formed?
2. How many teams contain exactly 3 adults and 2 juniors?
3. How many teams contain at least one adult and at least one junior?
**Exercise 11.** Anagrams with repeated letters:
How many distinct anagrams can be formed from the letters of **ANANAS**?
**Exercise 12.** A convex polygon has $n$ vertices ($n \geq 4$).
How many diagonals does this polygon possess? *(Hint: a diagonal is a line segment connecting two non-consecutive vertices).*
**Exercise 13.** Determine the coefficient of $x^5$ in the expansion of $(3x - 2)^8$.
**Exercise 14.** Prove that for every integer $n \geq 1$:
$$\sum_{k=0}^n (-1)^k \binom{n}{k} = \binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \dots + (-1)^n \binom{n}{n} = 0$$
*(Hint: apply Newton's binomial theorem to $(1 - 1)^n$).*
**Exercise 15.** The Birthday Problem.
In a class of 30 students, assume each student's birthday is independently and uniformly distributed across the 365 days of a non-leap year.
1. How many birthday profiles are possible for the 30 students?
2. How many profiles have all 30 students with pairwise distinct birthdays?
3. Deduce the formula for the probability that at least two students share a birthday.

#### Level ★★★ (Deepening and Challenges)

**Exercise 16.** The Committee-Chair identity:
1. Prove algebraically that for all integers $1 \leq k \leq n$:
   $$k \binom{n}{k} = n \binom{n-1}{k-1}$$
2. Provide an elegant combinatorial interpretation by considering the selection of a committee of $k$ people from $n$ along with the designation of a chairperson within that committee.
**Exercise 17.** Compute the sum:
$$S = \sum_{k=1}^n k \binom{n}{k} = 1\binom{n}{1} + 2\binom{n}{2} + 3\binom{n}{3} + \dots + n\binom{n}{n}$$
*(Hint: use the result of Exercise 16 or differentiate the function $f(x) = (1+x)^n$).*
**Exercise 18.** Stars and Bars principle.
We wish to distribute 10 identical candies among 3 children (Alice, Bob, and Chloe).
1. How many distributions are possible if each child may receive 0, 1, or more candies?
2. How many distributions if each child must receive at least 1 candy?
**Exercise 19.** Vandermonde's Convolution Identity.
By expanding the polynomial identity $(1+x)^{m+n} = (1+x)^m (1+x)^n$ in two ways, prove the relation:
$$\sum_{k=0}^p \binom{m}{k}\binom{n}{p-k} = \binom{m+n}{p}$$
Give also a combinatorial interpretation of this identity.
**Exercise 20.** Sum of squares of binomial coefficients.
Using Vandermonde's identity with $m = n$ and $p = n$, prove that:
$$\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$$
**Exercise 21.** Derangements (The Hat-Check Problem).
$n$ guests leave their coats in a cloakroom. Upon exiting, coats are returned at random.
A derangement is a permutation where nobody receives their own coat.
Show using the Principle of Inclusion-Exclusion that the number of derangements $D_n$ satisfies:
$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$
**Exercise 22.** Dyck Paths and Catalan Numbers.
Consider lattice paths from $(0,0)$ to $(n,n)$ made of steps $(+1, 0)$ and $(0, +1)$, that never cross above the diagonal $y = x$ (i.e., remaining always in the half-plane $y \leq x$).
Show by Désiré André's Reflection Principle that the number of such paths is given by the Catalan number:
$$C_n = \frac{1}{n+1} \binom{2n}{n}$$

---

### Solutions

**Solution 1:**
- $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.
- $\frac{8!}{6!} = 8 \times 7 = 56$.
- $\binom{7}{2} = \frac{7 \times 6}{2 \times 1} = 21$.
- $\binom{9}{9} = 1$.
- $\binom{10}{7} = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.

**Solution 2:**
1. $26^8 = 208\,827\,064\,576$.
2. $A_{26}^8 = 26 \times 25 \times 24 \times 23 \times 22 \times 21 \times 20 \times 19 = 62\,990\,928\,000$.

**Solution 3:**
1. Trifecta in exact order: $A_{12}^3 = 12 \times 11 \times 10 = 1\,320$.
2. Trifecta regardless of order: $\binom{12}{3} = \frac{1\,320}{6} = 220$.

**Solution 4:**
$\binom{n}{2} = \frac{n!}{2!(n-2)!} = \frac{n(n-1)(n-2)!}{2(n-2)!} = \frac{n(n-1)}{2}$.
A handshake involves 2 distinct people without order. Between $n$ people, there are therefore $\binom{n}{2} = \frac{n(n-1)}{2}$ mutual handshakes.

**Solution 5:**
1. $(x+2)^4 = \binom{4}{0}x^4 + \binom{4}{1}x^3(2) + \binom{4}{2}x^2(2^2) + \binom{4}{3}x(2^3) + \binom{4}{4}(2^4) = x^4 + 8x^3 + 24x^2 + 32x + 16$.
2. $(2x-1)^3 = (2x)^3 - 3(2x)^2(1) + 3(2x)(1^2) - 1^3 = 8x^3 - 12x^2 + 6x - 1$.

**Solution 6:**
- MATHS: 5 distinct letters, so $5! = 120$ anagrams.
- LIVRE: 5 distinct letters, so $5! = 120$ anagrams.

**Solution 7:**
Total balls: $6 + 4 + 2 = 12$. Simultaneous draw of 3 balls: $\binom{12}{3} = \frac{12 \times 11 \times 10}{6} = 220$ possible draws.

**Solution 8:**
1. $6^5 = 7\,776$ possible outcomes.
2. For each die, 5 outcomes excluding 6: $5^5 = 3\,125$ outcomes.
3. Taking the complement: $7\,776 - 3\,125 = 4\,651$ outcomes contain at least one 6.

**Solution 9:**
A 4-digit number is written $d_1 d_2 d_3 d_4$ with $d_1 \in \{1..9\}$ (9 choices) and $d_2, d_3, d_4 \in \{0..9\}$.
1. Distinct digits:
   - For $d_1$: 9 choices (from 1 to 9).
   - For $d_2$: 9 choices (from 0 to 9 except $d_1$).
   - For $d_3$: 8 choices.
   - For $d_4$: 7 choices.
   Total: $9 \times 9 \times 8 \times 7 = 4\,536$ numbers.
2. Even numbers with distinct digits ($d_4 \in \{0, 2, 4, 6, 8\}$):
   - Case 1: $d_4 = 0$ (1 choice). Then $d_1$ has 9 choices (from 1 to 9), $d_2$ has 8 choices, $d_3$ has 7 choices. Total: $1 \times 9 \times 8 \times 7 = 504$ numbers.
   - Case 2: $d_4 \in \{2, 4, 6, 8\}$ (4 choices). Then $d_1$ can be neither 0 nor $d_4$, so it has $10 - 2 = 8$ choices. Then $d_2$ has 8 choices (including 0), and $d_3$ has 7 choices. Total: $4 \times 8 \times 8 \times 7 = 1\,792$ numbers.
   Grand total: $504 + 1\,792 = 2\,296$ even numbers.

**Solution 10:**
1. Teams without restriction: $\binom{14}{5} = \frac{14 \times 13 \times 12 \times 11 \times 10}{120} = 2\,002$.
2. 3 adults and 2 juniors: $\binom{8}{3} \times \binom{6}{2} = 56 \times 15 = 840$.
3. Complementary cases: all-adult team ($\binom{8}{5} = 56$) or all-junior team ($\binom{6}{5} = 6$).
   Mixed teams: $2\,002 - (56 + 6) = 1\,940$ teams.

**Solution 11:**
The word ANANAS has 6 letters: 3 A's, 2 N's, and 1 S.
Number of anagrams = $\frac{6!}{3! \times 2! \times 1!} = \frac{720}{6 \times 2} = 60$.

**Solution 12:**
There are $\binom{n}{2}$ segments connecting any pair of vertices. Among these, $n$ form the boundary edges of the polygon. The number of diagonals is:
$$\binom{n}{2} - n = \frac{n(n-1)}{2} - n = \frac{n^2 - 3n}{2} = \frac{n(n-3)}{2}.$$

**Solution 13:**
In $(3x - 2)^8 = \sum_{k=0}^8 \binom{8}{k} (3x)^k (-2)^{8-k}$, the term with $x^5$ corresponds to $k=5$:
$\binom{8}{5} (3x)^5 (-2)^3 = 56 \times 243 x^5 \times (-8) = -108\,864 x^5$. The coefficient is **$-108\,864$**.

**Solution 14:**
By Newton's binomial theorem, $(1 + x)^n = \sum_{k=0}^n \binom{n}{k} x^k$.
For $x = -1$ with $n \geq 1$:
$$(1 + (-1))^n = 0^n = 0 = \sum_{k=0}^n \binom{n}{k} (-1)^k$$

**Solution 15:**
1. For each student, 365 possible birthdates: $365^{30}$.
2. If all birthdates are distinct: arrangement $A_{365}^{30} = 365 \times 364 \times \dots \times 336$.
3. Probability that at least two students share a birthday:
   $$P = 1 - \frac{A_{365}^{30}}{365^{30}} \approx 1 - 0.2937 = 0.7063 \quad (\approx 70.6\,\%!).$$
   Starting with just 23 people, this probability already exceeds 50%!

**Solution 16:**
1. Algebraically:
   $$k \binom{n}{k} = k \frac{n!}{k!(n-k)!} = \frac{n!}{(k-1)!(n-k)!} = n \frac{(n-1)!}{(k-1)!((n-1)-(k-1))!} = n \binom{n-1}{k-1}.$$
2. Combinatorial interpretation: We wish to select a committee of $k$ people from $n$ along with a chair.
   - Method A: First choose the $k$ members of the committee ($\binom{n}{k}$ ways), then choose the chair from among those $k$ members ($k$ ways). Total: $k \binom{n}{k}$.
   - Method B: First choose the chair from the $n$ candidates ($n$ ways), then choose the remaining $k-1$ committee members from the remaining $n-1$ people ($\binom{n-1}{k-1}$ ways). Total: $n \binom{n-1}{k-1}$.
   Since both methods enumerate the exact same set of outcomes, equality holds.

**Solution 17:**
Using the identity $k\binom{n}{k} = n\binom{n-1}{k-1}$:
$$S = \sum_{k=1}^n n \binom{n-1}{k-1} = n \sum_{j=0}^{n-1} \binom{n-1}{j} = n \cdot 2^{n-1}.$$

**Solution 18:**
1. Distributing 10 identical candies to 3 children is equivalent to placing 10 stars and 2 divider bars among $10 + 2 = 12$ positions:
   Number of ways = $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$.
2. If each child must receive at least 1 candy, give 1 candy to each first (leaving 7 candies). Distribute the 7 remaining candies to the 3 children with no restriction:
   $\binom{7+3-1}{2} = \binom{9}{2} = 36$.

**Solution 19:**
In the product $(1+x)^m (1+x)^n = (1+x)^{m+n}$, the coefficient of $x^p$ on the right side is $\binom{m+n}{p}$.
On the left side, a term in $x^p$ comes from multiplying a term $\binom{m}{k} x^k$ from the first factor with a term $\binom{n}{p-k} x^{p-k}$ from the second factor, for $k$ ranging from 0 to $p$. The sum of these products gives $\sum_{k=0}^p \binom{m}{k}\binom{n}{p-k}$.
*Combinatorial justification:* To choose $p$ individuals from a group of $m$ men and $n$ women, one can select $k$ men and $p-k$ women, for all $k \in \{0, \dots, p\}$.

**Solution 20:**
In Vandermonde's identity with $m = n$ and $p = n$:
$$\sum_{k=0}^n \binom{n}{k}\binom{n}{n-k} = \binom{2n}{n}$$
By symmetry, $\binom{n}{n-k} = \binom{n}{k}$. Thus:
$$\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}.$$

**Solution 21:**
Let $A_i$ be the set of permutations leaving the $i$-th person with their own coat.
We seek $D_n = n! - |\bigcup_{i=1}^n A_i|$.
By the Principle of Inclusion-Exclusion:
$$|\bigcup_{i=1}^n A_i| = \sum_{i} |A_i| - \sum_{i<j} |A_i \cap A_j| + \dots + (-1)^{n-1} |A_1 \cap \dots \cap A_n|$$
The intersection of $k$ sets $A_i$ corresponds to permutations fixing at least $k$ designated elements, leaving $(n-k)!$ permutations. There are $\binom{n}{k}$ such intersections.
The $k$-th order term is thus $\binom{n}{k} (n-k)! = \frac{n!}{k!}$.
Hence $D_n = n! - \sum_{k=1}^n (-1)^{k-1} \frac{n!}{k!} = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$.
*(Remark: as $n \to \infty$, $D_n / n! \to e^{-1} \approx 36.8\%$).*

**Solution 22:**
The total number of lattice paths from $(0,0)$ to $(n,n)$ is $\binom{2n}{n}$.
Any path that crosses the diagonal $y = x$ must touch the line $y = x + 1$ at least once.
Consider the first point of contact $P$ with this line. Reflecting the entire remaining portion of the path after $P$ across the line $y = x + 1$ maps the destination $(n, n)$ to $(n-1, n+1)$.
This reflection gives a bijection between paths that cross the diagonal and all paths from $(0,0)$ to $(n-1, n+1)$.
The number of forbidden paths is therefore $\binom{2n}{n-1}$.
The number of Dyck paths is consequently:
$$C_n = \binom{2n}{n} - \binom{2n}{n-1} = \binom{2n}{n} - \frac{n}{n+1}\binom{2n}{n} = \frac{1}{n+1}\binom{2n}{n}.$$

---

### The Question That Opens the Next Step

We have learned to count the number of ways to choose $k$ successes out of $n$ trials: that is the binomial coefficient $\binom{n}{k}$.
What happens when each individual trial is governed by chance, with a probability $p$ of success and $1-p$ of failure?
If we toss a coin a thousand times, how often will "Heads" turn up? Can we be certain that the observed frequency will stabilize around $50\%$?
This is the breathtaking leap from discrete combinatorics to the binomial distribution and the great limit theorems: welcome to **Chapter 54 and The Thousand Coin Tosses**.
