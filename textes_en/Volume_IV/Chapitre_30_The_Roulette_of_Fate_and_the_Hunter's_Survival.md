# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)
## CHAPTER 30: The Roulette of Fate and the Hunter's Survival

> *“The ignorant man blames bad luck, consults fortune-tellers, or trembles before the thunderstorm when danger approaches. The mathematician surveys the paths of the future, calculates the fraction of chance, and makes the decision that saves his caravan. Chance is no blind monster: it is a tree whose branches can be counted.”*

---

### What You Are About to Discover

- How to transform the fog of uncertainty into a **precise number between 0 and 1** (the probability).
- The formal vocabulary that structures chance: **random experiment**, **outcome**, **event**, **certain, impossible, and complementary events**.
- Why the formula $P(E) = \dfrac{\text{number of favorable outcomes}}{\text{number of possible outcomes}}$ only works under **equiprobability**, and the monumental pitfall of the two dice.
- How to explore the two-stage future using a **probability tree diagram** and a **two-way table**.
- The crucial difference between sampling **with replacement** and sampling **without replacement**.
- How real-world chance obeys the law of large numbers: the **stabilization of relative frequencies** and computer simulation.

---

### 1. The Problem: The Caravan and the Forest of Two Paths

Dusk is falling over the Silk Road. A caravan of ten camels loaded with bales of precious spices and fine silks halts at the edge of an immense, dark, and misty forest.
To reach the oasis where the grand annual market is being held, the caravan master must choose between two routes:

```
                                  ┌─── Marsh Trail (A) ──────────┐
                                  │    1 caravan in 10 lost      │
          Caravan Departure ──────┤                              ├─── Jade Oasis
                                  │    Gorge Trail (B)           │
                                  └─── 4 caravans in 10 lost ────┘
```

* **The Marsh Trail (Path A):**
  It is a flat track, easy on the animals' feet. But the region is riddled with treacherous mud pits. Merchant records show that out of 100 caravans that took this trail this year, **10 became bogged down and lost everything**, while 90 arrived safe and sound.
* **The Gorge Trail (Path B):**
  It is a steep, rocky defile, twice as short and much faster. But armed bandits lurk in the caves: out of 100 caravans, **40 were ambushed and plundered**, while 60 managed to cross unscathed.

The young camel driver exclaims:
*“Let us take the gorge trail! We will arrive tomorrow at dawn to sell at the best price! With a bit of luck, the bandits will be asleep!”*

The old leader shakes his head:
*“Luck is not a prayer one casts into the sky. Luck is a fraction of reality. He who cannot weigh risk walks blindfolded toward the abyss!”*

For the first time in the history of mathematics, we are no longer merely measuring what lies before our eyes (a length, a weight, a count of tiles), but **what has not yet happened**!
We enter the realm of **Probability**.

---

### 2. The Formal Vocabulary of Probability

To speak of chance with the rigor of a geometer, mathematicians forged a very precise vocabulary. Each word carries a strict definition that must be mastered.

#### 2.1 Random Experiment and Outcome
> **📐 Definition — Random Experiment.**
> An experiment is said to be **random** if:
> 1. All possible results are known in advance;
> 2. The final result depends solely on chance and is **impossible to predict with certainty**.

*Examples:*
- Tossing a balanced coin and observing the upper face is a random experiment.
- Dropping an apple to see if it falls toward the ground is **not** a random experiment (gravity guarantees that it will always fall).

> **📐 Definition — Outcome.**
> An **outcome** (or elementary event) is one of the possible results of a random experiment. The set of all possible outcomes is called the **sample space** (often denoted by the Greek letter $\Omega$, “omega”).

*Example with a 6-sided die:* The possible outcomes are 1, 2, 3, 4, 5, and 6. The sample space is $\{1, 2, 3, 4, 5, 6\}$.

#### 2.2 Events: Impossible, Certain, Complementary
> **📐 Definition — Event.**
> An **event** is a set consisting of zero, one, or several outcomes. An event is said to **occur** (or be realized) if the outcome obtained during the experiment belongs to that event.

Consider the roll of an ordinary six-sided die:
- Event $A$: “Roll an even number” consists of the outcomes $\{2, 4, 6\}$. If the die lands on 4, event $A$ has occurred.
- **Impossible event:** an event that contains no outcomes and can never happen. Its probability is equal to **0**.
  *Example:* “Roll a 7” with a 6-sided die.
- **Certain event:** an event that contains all possible outcomes and always happens. Its probability is equal to **1** (or $100\%$)!
  *Example:* “Roll a number less than or equal to 6”.
- **Complementary event:** the complementary event of an event $A$, denoted **$\bar{A}$** (read **“A bar”** or “not $A$”), is the event that occurs **precisely when $A$ does not occur**.

```
                   ┌───────────────────────────────────┐
                   │ Complete Sample Space Ω (Total=1) │
                   │  ┌───────────────┐                │
                   │  │ Event A       │  Complement Ā  │
                   │  │ (Success)     │  (Failures)    │
                   │  └───────────────┘                │
                   └───────────────────────────────────┘
```

> **📐 Fundamental Property of Complementary Events —**
> For any event $A$:
> $$P(\bar{A}) = 1 - P(A) \qquad\text{or equivalently}\qquad P(A) + P(\bar{A}) = 1$$

*Example:* If the probability of rain tomorrow is $P(\text{Rain}) = 0.3$ (or $30\%$), then the probability of no rain is:
$$P(\text{No Rain}) = 1 - 0.3 = 0.7 \quad (\text{or } 70\%).$$

---

### 3. Calculating Probability under Equiprobability

#### 3.1 What is Equiprobability?

A situation is one of **equiprobability** (equally likely outcomes) when **every possible outcome has exactly the same chance of occurring**.
In problems, this condition is indicated by standard key phrases:
- “A **fair** (or balanced, unbiased) six-sided die”;
- “A **fair** coin”;
- “Marbles **indistinguishable by touch**” in an urn;
- “A card drawn **at random** from a well-shuffled deck”.

#### 3.2 Laplace's Formula

> **📐 Laplace's Rule — Probability under Equiprobability.**
> In a situation with equally likely outcomes, the probability of an event $E$ is equal to the number of favorable outcomes divided by the total number of possible outcomes:
> $$P(E) = \frac{\text{Number of outcomes favorable to } E}{\text{Total number of possible outcomes}}$$

#### 3.3 The Three Guises of a Probability
A probability is always a real number between 0 and 1:
$$0 \le P(E) \le 1$$
It can be written in three equivalent forms:
1. As a **fraction** (exact value): $\dfrac{1}{4}$
2. As a **decimal number**: $0.25$
3. As a **percentage**: $25\%$

> **⚠️ Warning, Trap!** A probability can **NEVER** be negative, nor greater than 1 (or $100\%$)! If you calculate $P = 1.25$ or $P = -0.3$, there is inevitably an error in your work. Furthermore, the sum of the probabilities of all elementary outcomes is **always equal to 1**.

Returning to our caravan:
- For the Marsh Trail: $P(\text{Peril}) = \dfrac{10}{100} = \dfrac{1}{10} = 0.10 = \mathbf{10\%}$.
- For the Gorge Trail: $P(\text{Peril}) = \dfrac{40}{100} = \dfrac{4}{10} = 0.40 = \mathbf{40\%}$.
The danger in the gorge is **four times higher**! The wise master chooses the marsh, and the caravan reaches its destination unharmed.

---

### 4. Two-Stage Experiments: Trees and Tables

When a random experiment unfolds across several successive stages (for instance: tossing two coins in a row, rolling two dice, or drawing two marbles from a bag), keeping track of all outcomes mentally becomes treacherous. Two visual tools make everything transparent.

#### 4.1 Tool #1: The Two-Way Table (The Classic Two-Dice Example)

If you roll two 6-sided dice and compute the sum of the two numbers, how many possible outcomes are there?
The sums range from $1+1 = 2$ up to $6+6 = 12$. That makes 11 different possible sums.
Some students leap to the conclusion: *“The probability of getting a sum of 7 is 1 in 11!”*
**This is a monumental blunder!** Because the sums are not equally likely!

Let us construct the table of all possible pairs ($6 \times 6 = \mathbf{36\text{ equally likely outcomes}}$):

| Die 1 \ Die 2 | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 2 | 3 | 4 | 5 | 6 | **[7]** |
| **2** | 3 | 4 | 5 | 6 | **[7]** | 8 |
| **3** | 4 | 5 | 6 | **[7]** | 8 | 9 |
| **4** | 5 | 6 | **[7]** | 8 | 9 | 10 |
| **5** | 6 | **[7]** | 8 | 9 | 10 | 11 |
| **6** | **[7]** | 8 | 9 | 10 | 11 | 12 |

Look at the long diagonal of **7s**:
- To obtain a sum of **2**, there is only a single cell: $(1 ; 1) \implies P(2) = \dfrac{1}{36}$.
- To obtain a sum of **12**, only one cell: $(6 ; 6) \implies P(12) = \dfrac{1}{36}$.
- But to obtain a sum of **7**, there are **6 different cells**: $(1;6), (2;5), (3;4), (4;3), (5;2), (6;1)$!
$$P(\text{Sum} = 7) = \frac{6}{36} = \frac{1}{6} \approx \mathbf{16.7\%}$$
A sum of 7 is **six times more likely** than a sum of 2! It is the king of the dice table.

```
       Distribution of the sum of two dice:
       Probability
          ▲
     6/36 ┤                     ██ (7)
     5/36 ┤                  ██ ██ ██ (6, 7, 8)
     4/36 ┤               ██ ██ ██ ██ ██
     3/36 ┤            ██ ██ ██ ██ ██ ██ ██
     2/36 ┤         ██ ██ ██ ██ ██ ██ ██ ██ ██
     1/36 ┤      ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██
          └──────┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──►
                 2  3  4  5  6  7  8  9 10 11 12   Sum
```

#### 4.2 Tool #2: The Weighted Probability Tree Diagram

The tree diagram is the Swiss Army knife of probability. Each fork represents a trial.

> **📐 The Three Sacred Laws of the Probability Tree —**
> 1. **The sum of the probabilities** on all branches issuing from any single node is **always equal to 1**.
> 2. **Along any path**, you **multiply** the branch probabilities to find the probability of the final compound outcome (multiplication rule).
> 3. **The probability of an event** composed of several distinct paths is the **sum** of the probabilities of those paths.

```
                        1st Trial                2nd Trial             Full Path Outcome
                                           1/2
                                      ┌────────── Heads ===> (Heads ; Heads) : 1/2 × 1/2 = 1/4
                                  1/2 │
                        ┌─────────────┤    1/2
                        │    Heads    └────────── Tails ===> (Heads ; Tails) : 1/2 × 1/2 = 1/4
                        │
        Start ──────────┤
                        │    Tails    ┌────────── Heads ===> (Tails ; Heads) : 1/2 × 1/2 = 1/4
                        └─────────────┤    1/2
                                  1/2 │
                                      └────────── Tails ===> (Tails ; Tails) : 1/2 × 1/2 = 1/4
                                           1/2
```

---

### 5. Sampling With Replacement vs. Sampling Without Replacement

This is one of the most vital distinctions in introductory probability.
Imagine a box containing **3 red marbles (R)** and **2 green marbles (G)** (making 5 marbles in total).
We draw two marbles successively at random.

#### Case 1: Sampling WITH Replacement
After recording the color of the first marble, we **place it back into the box** and mix before drawing the second marble.
- On the first draw: $P(R) = \dfrac{3}{5}$ and $P(G) = \dfrac{2}{5}$.
- On the second draw: the box is once again **strictly identical**!
  The probabilities do not change: $P(R) = \dfrac{3}{5}$ and $P(G) = \dfrac{2}{5}$.
- The probability of drawing two reds $(R ; R)$ is:
  $$P(R ; R) = \frac{3}{5} \times \frac{3}{5} = \frac{9}{25} = 0.36 = \mathbf{36\%}.$$

#### Case 2: Sampling WITHOUT Replacement
After the first draw, we keep the marble in hand: **we do not return it**!
- On the first draw: $P(R) = \dfrac{3}{5}$.
- For the second draw, only **4 marbles in total remain** in the box!
  - If the first marble was red, only 2 red marbles remain out of 4: $P(\text{2nd } R) = \dfrac{2}{4}$.
  - The probability of drawing two reds $(R ; R)$ is:
    $$P(R ; R) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10} = 0.30 = \mathbf{30\%}.$$

> **⚠️ Warning, Trap!** In sampling without replacement, **the denominator decreases by 1** on the second draw, and the numerator corresponding to the drawn color also decreases by 1!

---

### 6. From Theoretical Chance to the Real World: The Law of Large Numbers

When you flip a fair coin, the theoretical probability of landing Heads is $p = 0.5$.
Does this mean that if you flip the coin 10 times, you will obtain **exactly** 5 Heads and 5 Tails?
No! You could very easily get 7 Heads and 3 Tails (an observed relative frequency of $70\%$ Heads).

What happens, however, if you flip the coin 100 times, 1,000 times, 100,000 times?
Let us calculate the **observed relative frequency**:
$$f = \frac{\text{Number of observed Heads}}{\text{Total number of flips } N}$$

> **📐 Phenomenon of Frequency Stabilization (Law of Large Numbers) —**
> When a random experiment is repeated an **independently large number of times**, the observed relative frequency of an event approaches and stabilizes around its **theoretical probability**.

```
   Relative Frequency f
      ▲
  1.0 ┼──o
      │   \
  0.7 ┼────o
      │     \
  0.5 ┼──────\───o──────o───o──────────────── Theoretical Probability = 0.5
      │       \ / \    / \ / \
  0.3 ┼────────o   \  /   o   \
      │             o          \
  0.0 ┴──┼──────┼───────┼───────┼─────────────►
         10    100    1,000   10,000   Number of trials N
```

This very principle allows insurance companies to set policy premiums fairly, meteorologists to predict storm patterns, and casinos to guarantee they never operate at a net loss over the course of a full year!

> **🔍 True History — The Letters of Pascal and Fermat (1654)**
> In 1654, a Parisian gambler, the **Chevalier de Méré**, presented **Blaise Pascal** with an enigma that set tavern arguments ablaze: “the problem of points” (*le problème des partis*). Two players are tossing a coin for a prize purse of 64 gold pistoles. The first player to reach 3 wins takes everything. But the game is abruptly interrupted by a fire when Player A is leading 2 to 1! How should the purse be divided in fairness?
> Pascal began exchanging letters with the brilliant magistrate of Toulouse, **Pierre de Fermat**. Rather than dwelling on the past, they mapped the tree of all possible futures: across the 4 possible game completions, Player A would win in 3 of them, and Player B in only 1. Natural justice therefore demanded giving $\frac{3}{4}$ of the pot to Player A (48 pistoles) and $\frac{1}{4}$ to Player B (16 pistoles). Modern probability theory was born!

---

### 7. Step-by-Step Worked Examples

#### Worked Example 1 — Drawing from a Deck of Cards (Equiprobability and Complementary Events)
A card is drawn at random from a well-shuffled 32-card deck (consisting of 4 suits: Hearts, Diamonds, Clubs, Spades, each with 8 cards: 7, 8, 9, 10, Jack, Queen, King, Ace).
1. What is the probability of drawing an Ace?
2. What is the probability of drawing a red card (Heart or Diamond)?
3. What is the probability of drawing a card that is **not** a Club?

*Step-by-Step Solution:*
Because the deck is thoroughly shuffled, every card is equally likely to be drawn.
1. The deck contains 4 Aces (one of each suit).
   $$P(\text{Ace}) = \frac{4}{32} = \frac{1}{8} = \mathbf{0.125} \quad (12.5\%).$$
2. There are 8 hearts and 8 diamonds, totaling $8 + 8 = 16$ red cards out of 32.
   $$P(\text{Red}) = \frac{16}{32} = \frac{1}{2} = \mathbf{0.5} \quad (50\%).$$
3. *Method using the complementary event:*
   Let event $C$ be “Drawing a Club”. There are 8 clubs, so $P(C) = \frac{8}{32} = \frac{1}{4}$.
   The event “Not drawing a Club” is the complementary event $\bar{C}$:
   $$P(\bar{C}) = 1 - P(C) = 1 - \frac{1}{4} = \mathbf{\frac{3}{4}} = \mathbf{0.75} \quad (75\%).$$

---

#### Worked Example 2 — Two-Stage Sequential Experiment (The Keychain)
A keychain holds 4 keys that look identical, but **only one** opens the garage door.
A hurried driver tries the keys at random in the dark. Whenever a key does not work, he sets it aside so as not to retest it (sampling without replacement).
What is the probability that he opens the door on exactly his second attempt?

*Step-by-Step Solution:*
To succeed on the second attempt, two consecutive events must occur:
- Failure on the 1st attempt ($F_1$);
- Success on the 2nd attempt ($S_2$).

Let us examine the corresponding branches:
1. On the 1st attempt: there are 3 wrong keys out of 4 keys in total:
   $$P(F_1) = \frac{3}{4}$$
2. On the 2nd attempt: the wrong key has been removed. Only 3 keys remain, of which exactly 1 is the right key:
   $$P(S_2 \text{ given } F_1) = \frac{1}{3}$$
3. By the multiplication rule along a path:
   $$P(\text{Success on 2nd attempt}) = P(F_1) \times P(S_2) = \frac{3}{4} \times \frac{1}{3} = \frac{3}{12} = \mathbf{\frac{1}{4}} = \mathbf{0.25}.$$
Each attempt has strictly a $\frac{1}{4}$ chance of being the successful one!

---

#### Worked Example 3 — Drawing Marbles With and Without Replacement
A bag contains 2 blue marbles and 3 yellow marbles. Two marbles are drawn successively at random.
What is the probability of drawing **two marbles of different colors**:
1. When sampling **with replacement**?
2. When sampling **without replacement**?

*Step-by-Step Solution:*
Drawing two marbles of different colors corresponds to two disjoint paths: $(B ; Y)$ or $(Y ; B)$.
1. **With replacement:**
   - $P(B ; Y) = \frac{2}{5} \times \frac{3}{5} = \frac{6}{25}$.
   - $P(Y ; B) = \frac{3}{5} \times \frac{2}{5} = \frac{6}{25}$.
   Adding the two mutually exclusive paths:
   $$P(\text{Different colors}) = \frac{6}{25} + \frac{6}{25} = \frac{12}{25} = \mathbf{0.48} \quad (48\%).$$

2. **Without replacement:**
   - For $(B ; Y)$: first blue ($2/5$), then 4 marbles remain including 3 yellow ($3/4$):
     $$P(B ; Y) = \frac{2}{5} \times \frac{3}{4} = \frac{6}{20} = \frac{3}{10}.$$
   - For $(Y ; B)$: first yellow ($3/5$), then 4 marbles remain including 2 blue ($2/4$):
     $$P(Y ; B) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}.$$
   Adding the two paths:
   $$P(\text{Different colors}) = \frac{3}{10} + \frac{3}{10} = \frac{6}{10} = \mathbf{0.60} \quad (60\%).$$
*Notice: the probability shifts significantly depending on whether the item is replaced or not!*

---

#### Worked Example 4 — The Magic Trick of “At Least One”
A fair coin is tossed three times in succession.
What is the probability of getting **at least one Head**?

*Step-by-Step Solution:*
“Getting at least one Head” means obtaining 1 Head, 2 Heads, or 3 Heads. Calculating all these cases individually would be tedious.
Let us examine the **complementary event**:
The opposite of “getting at least one Head” is **“getting NO Heads at all”**, which means obtaining three consecutive Tails $(T ; T ; T)$.
- The probability of Tails on any single toss is $\frac{1}{2}$.
- Since the three tosses are independent:
  $$P(\text{No Heads}) = P(T ; T ; T) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}.$$
- By the complementary event formula:
  $$P(\text{At least one Head}) = 1 - P(\text{No Heads}) = 1 - \frac{1}{8} = \mathbf{\frac{7}{8}} = \mathbf{0.875} \quad (87.5\%).$$
By passing through the complement, the calculation took a single line!

---

#### Worked Example 5 — Two-Color Die and the Fairground Game
A carnival booth invites players to roll a special 6-sided die: 4 faces are painted Green and 2 faces are painted Red.
To play, the participant pays $2.
- If the die lands on Red, the player wins $5 (a net profit of +$3).
- If the die lands on Green, the player wins nothing (a net loss of -$2).
The booth owner claims: *“Step right up and test your luck! You can win more than double your stake!”*
Is this game favorable to the player?

*Step-by-Step Solution:*
Let us calculate the probabilities:
- $P(\text{Red}) = \frac{2}{6} = \frac{1}{3} \approx 33.3\%$.
- $P(\text{Green}) = \frac{4}{6} = \frac{2}{3} \approx 66.7\%$.

Imagine playing 300 rounds:
- The die lands on Red approximately $300 \times \frac{1}{3} = 100$ times, yielding $100 \times (+\$3) = +\$300$.
- The die lands on Green approximately $300 \times \frac{2}{3} = 200$ times, costing $200 \times (-\$2) = -\$400$.
Overall balance for 300 rounds: $300 - 400 = -\$100$!
On average per round, the player loses approximately $\dfrac{-100}{300} \approx -\$0.33$.
**The game is strictly unfavorable to the player** (and reliably profitable for the booth operator).

---

### What You Must Remember

1. **Vocabulary:**
   - **Random experiment**: an outcome driven by chance, not predictable with certainty.
   - **Outcomes**: individual elementary results.
   - **Impossible event** ($P = 0$); **Certain event** ($P = 1$).
   - **Complementary event $\bar{A}$**: $P(\bar{A}) = 1 - P(A)$. The magic shortcut for “at least one”: $P(\text{at least one}) = 1 - P(\text{none})$.

2. **Equiprobability:**
   $$P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$
   Always verify: $0 \le P(E) \le 1$. The sum of probabilities over all elementary outcomes equals $1$.

3. **Two-Stage Experiments:**
   - **Two-way table**: ideal for 2 dice, 2 spinners (total cells = product of outcomes).
   - **Probability tree diagram**:
     - Sum of branches issuing from a single node = 1.
     - **Multiply** probabilities along a path.
     - **Add** probabilities of disjoint paths that achieve the event.
   - **With replacement**: probabilities remain constant.
   - **Without replacement**: sample size decreases by 1 on each draw.

4. **Law of Large Numbers:**
   - The observed **relative frequency** over a large number of repetitions converges and stabilizes around the **theoretical probability**.

---

### Exercises

#### Level ★: Direct Application

**Exercise 1.**
An opaque urn contains 4 red marbles, 3 green marbles, and 5 blue marbles, all indistinguishable by touch. A marble is drawn at random.
1. How many possible outcomes are there? Are they equally likely?
2. Calculate the probability of drawing a red marble as an irreducible fraction.
3. Calculate the probability of drawing a marble that is not green.

**Exercise 2.**
A fair 6-sided die numbered 1 to 6 is rolled. Calculate the probability of the following events:
- $A$: “Roll an odd number”.
- $B$: “Roll a multiple of 3”.
- $C$: “Roll a number strictly greater than 4”.
- $D$: “Roll a prime number”.

**Exercise 3.**
A lottery wheel divided into 8 equal sectors is spun: 3 sectors are painted blue, 4 yellow, and 1 red.
1. What is the probability of landing on red?
2. What is the probability of not landing on blue?
3. Express these probabilities as percentages.

**Exercise 4.**
A fair coin is tossed twice in succession.
1. Draw the tree of possibilities showing probabilities on each branch.
2. What is the probability of getting Tails twice?
3. What is the probability of getting exactly one Head and one Tail?

**Exercise 5.**
In a middle school, $55\%$ of students eat lunch at the cafeteria and the rest are day-pupils (eating at home). A student is chosen at random.
What is the probability that this student eats at home?

---

#### Level ★★: Deeper Reflection and Combined Situations

**Exercise 6 (Rolling Two Dice and Multiplying).**
Two fair 6-sided dice are rolled, and the two numbers obtained are **multiplied**.
1. Using a $6 \times 6$ two-way table, determine all possible product outcomes.
2. What is the probability that the product equals 12?
3. What is the probability that the product is an even number?

**Exercise 7 (Socks in the Drawer in the Dark).**
In a drawer, 6 black socks and 4 blue socks are mixed together, completely indistinguishable by touch.
In the morning, before sunrise, Lucas picks two socks successively at random **without replacing them**.
1. Construct the weighted tree diagram representing this random experiment.
2. What is the probability that Lucas picks two black socks?
3. What is the probability that Lucas picks two socks of the same color (so that they match)?

**Exercise 8 (The Word “PROBABILITÉ”).**
Each of the 11 letters of the word “P R O B A B I L I T É” is written on an identical card, and the 11 cards are placed in a bag. A card is drawn at random.
1. What is the probability of drawing the letter “B”?
2. What is the probability of drawing a vowel (O, A, I, I, É)?
3. What is the probability of drawing a consonant?

**Exercise 9 (Factory Quality Control).**
A factory manufactures electronic components. On a production line, $3\%$ of the components have a soldering defect.
A technician selects two components in succession at random (this selection is treated as sampling with replacement due to the very large volume of parts produced).
1. What is the probability that both components are defective?
2. What is the probability that neither component is defective?
3. What is the probability that at least one of the two components has a defect?

**Exercise 10 (The Gambler's Fallacy at the Casino).**
A player stands at a roulette wheel. The ball has landed on a Black pocket on the last 6 consecutive spins.
The player exclaims: *“Red hasn't appeared for 6 spins, it has a massive chance of landing now, I am betting everything on Red!”*
1. What do you think of this player's reasoning?
2. What is the actual probability that the ball lands on Red on the 7th spin (on a European roulette wheel with 18 red pockets, 18 black pockets, and 1 green zero pocket)?

**Exercise 11 (The Archery Target).**
A square target with side length 40 cm has a red disk of radius 10 cm at its center.
A novice archer fires an arrow that is certain to hit the square target, but at a completely random point (probability proportional to area).
1. Calculate the total area of the square target.
2. Calculate the exact area of the central red disk.
3. What is the probability that the arrow hits the red disk? (Round to the nearest hundredth).

---

#### Level ★★★: Challenges and Further Exploration

**Exercise 12 (The Historical Problem of the Chevalier de Méré).**
In the 17th century, the Chevalier de Méré noticed that he consistently made money betting that at least one 6 would appear when rolling a fair 6-sided die 4 times in a row.
1. What is the probability of NOT rolling a 6 on a single roll of the die?
2. What is the probability of rolling no 6s in 4 independent rolls?
3. Deduce the probability of rolling at least one 6 in 4 rolls. Was the Chevalier right to place this bet?

**Exercise 13 (Computer Simulation of the Law of Large Numbers).**
A Python program simulates 10,000 rolls of a balanced 6-sided die.
Here is the script used:
```python
import random

rolls = 10000
sixes = 0

for i in range(rolls):
  die = random.randint(1, 6)
  if die == 6:
    sixes += 1

frequency = sixes / rolls
print("Frequency of 6:", frequency)
```
1. What is the theoretical probability of obtaining a 6 on a single roll? Give its value as a fraction and as a decimal rounded to 0.001.
2. What approximate value will the program display for `frequency`?
3. Why will the displayed value generally not be exactly equal to $1/6$? What is this phenomenon called?

**Exercise 14 (The Birthday Paradox in the Classroom).**
In a 9th-grade class of 25 students, the teacher asserts: *“There is a greater than 50% chance that two students in this classroom share the same birthday!”* (Assume a non-leap year of 365 days, and all birth dates equally likely).
To test the assertion, we investigate the complementary event: “All 25 students have pairwise distinct birthdays.”
1. The first student can have a birthday on any day (probability $365/365$). What is the probability that the second student is born on a different day from the first?
2. What is the probability that the 3rd student is born on a day different from the first two?
3. The product of the 25 probabilities is approximately $0.43$. Calculate the probability that at least two students share the same birthday. Was the teacher correct?

**Exercise 15 (The Problem of Points Revisited: Pascal and Fermat).**
Two players $A$ and $B$ each bet 50 pistoles into a pot (total: 100 pistoles). The first to win 3 rounds takes the entire pot.
The current score is 2 to 0 in favor of Player $A$. The game is abruptly interrupted.
1. At most, how many additional rounds would have been necessary to complete the game?
2. Draw the tree of remaining rounds assuming each round is equally likely ($P = 1/2$).
3. What is the probability that Player $B$ stages a comeback and wins the game?
4. How should the 100 pistoles be fairly divided between $A$ and $B$?

---

### Solutions

#### Solutions to Level ★ Exercises

- **Exercise 1:** 
  1. Total number of outcomes: $4 + 3 + 5 = 12$ marbles. Since they are indistinguishable by touch, they are equally likely.
  2. $P(\text{Red}) = \frac{4}{12} = \mathbf{\frac{1}{3}}$.
  3. There are $4 + 5 = 9$ non-green marbles, or $1 - \frac{3}{12} = \frac{9}{12} = \mathbf{\frac{3}{4}}$.
- **Exercise 2:** 
  - $P(A) = \frac{3}{6} = \mathbf{\frac{1}{2}}$ (outcomes: 1, 3, 5).
  - $P(B) = \frac{2}{6} = \mathbf{\frac{1}{3}}$ (outcomes: 3, 6).
  - $P(C) = \frac{2}{6} = \mathbf{\frac{1}{3}}$ (outcomes: 5, 6).
  - $P(D) = \frac{3}{6} = \mathbf{\frac{1}{2}}$ (prime outcomes: 2, 3, 5; remember: 1 is not prime!).
- **Exercise 3:** 
  1. $P(\text{Red}) = \frac{1}{8} = \mathbf{0.125} = \mathbf{12.5\%}$.
  2. $P(\text{Not Blue}) = 1 - \frac{3}{8} = \frac{5}{8} = \mathbf{0.625} = \mathbf{62.5\%}$.
- **Exercise 4:** 
  1. The tree has 4 terminal branches: $(H;H), (H;T), (T;H), (T;T)$, each with probability $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
  2. $P(T ; T) = \mathbf{\frac{1}{4}} = 0.25$.
  3. Favorable paths: $(H;T)$ and $(T;H) \implies \frac{1}{4} + \frac{1}{4} = \mathbf{\frac{1}{2}} = 0.5$.
- **Exercise 5:** $P(\text{Day-pupil}) = 1 - 0.55 = \mathbf{0.45} = \mathbf{45\%}$.

---

#### Detailed Solutions to Level ★★ Exercises

- **Exercise 6 (Product of Two Dice):**
  1. Product table ($6 \times 6 = 36$ cells):
     - Row 1: 1, 2, 3, 4, 5, 6
     - Row 2: 2, 4, 6, 8, 10, 12
     - Row 3: 3, 6, 9, 12, 15, 18
     - Row 4: 4, 8, 12, 16, 20, 24
     - Row 5: 5, 10, 15, 20, 25, 30
     - Row 6: 6, 12, 18, 24, 30, 36
  2. The cells giving 12 are: $(2;6), (3;4), (4;3), (6;2)$, totaling 4 cells.
     $$P(\text{Product} = 12) = \frac{4}{36} = \mathbf{\frac{1}{9}} \approx 0.111.$$
  3. The product is odd only if BOTH dice show odd numbers (3 choices $\times$ 3 choices = 9 cells).
     All other cells yield even products: $36 - 9 = 27$ even cells.
     $$P(\text{Even Product}) = \frac{27}{36} = \mathbf{\frac{3}{4}} = \mathbf{0.75}.$$

- **Exercise 7 (Socks Without Replacement):**
  Initial total: $6 + 4 = 10$ socks.
  1. Tree diagram:
     - 1st draw: Black ($6/10$), Blue ($4/10$).
     - 2nd draw after Black: Black ($5/9$), Blue ($4/9$).
     - 2nd draw after Blue: Black ($6/9$), Blue ($3/9$).
  2. Two black socks: $P(B ; B) = \frac{6}{10} \times \frac{5}{9} = \frac{30}{90} = \mathbf{\frac{1}{3}} \approx 0.333$.
  3. Same color: two black or two blue.
     $P(\text{Blue} ; \text{Blue}) = \frac{4}{10} \times \frac{3}{9} = \frac{12}{90}$.
     $$P(\text{Same Color}) = \frac{30}{90} + \frac{12}{90} = \frac{42}{90} = \mathbf{\frac{7}{15}} \approx \mathbf{0.467} \quad (46.7\%).$$

- **Exercise 8 (The Word PROBABILITÉ):**
  The word contains 11 letters: P (1), R (1), O (1), B (2), A (1), I (2), L (1), T (1), É (1).
  1. $P(\text{B}) = \mathbf{\frac{2}{11}}$.
  2. Vowels: O, A, I, I, É $\implies 5$ vowels. $P(\text{Vowel}) = \mathbf{\frac{5}{11}}$.
  3. Consonants: complementary event $\implies 1 - \frac{5}{11} = \mathbf{\frac{6}{11}}$.

- **Exercise 9 (Quality Control):**
  Let $D$ be the event “defective component”, $P(D) = 0.03$, and $P(\bar{D}) = 0.97$.
  1. Both defective: $P(D ; D) = 0.03 \times 0.03 = \mathbf{0.0009}$ (or $0.09\%$, less than one in a thousand).
  2. Neither defective: $P(\bar{D} ; \bar{D}) = 0.97 \times 0.97 = \mathbf{0.9409} \approx \mathbf{94.1\%}$.
  3. At least one defective: complement of neither defective:
     $$P = 1 - 0.9409 = \mathbf{0.0591} \approx \mathbf{5.91\%}.$$

- **Exercise 10 (The Gambler's Fallacy):**
  1. The gambler's reasoning is a **classic illusion** (known as the “gambler's fallacy”). The roulette wheel has no memory: every spin is entirely independent of previous spins. Past results have zero influence on the ball's next resting place.
  2. On a European roulette wheel with 37 pockets (18 red, 18 black, 1 green zero):
     $$P(\text{Red}) = \frac{18}{37} \approx \mathbf{0.4865} \quad (48.65\%).$$
     The probability is strictly the same as on the very first spin!

- **Exercise 11 (The Archery Target):**
  1. Area of the square target: $\mathcal{A}_{\text{square}} = 40 \times 40 = \mathbf{1{,}600\text{ cm}^2}$.
  2. Area of the red disk: $\mathcal{A}_{\text{disk}} = \pi \times R^2 = \pi \times 10^2 = \mathbf{100\pi\text{ cm}^2} \approx 314.16\text{ cm}^2$.
  3. Probability:
     $$P = \frac{\mathcal{A}_{\text{disk}}}{\mathcal{A}_{\text{square}}} = \frac{100\pi}{1{,}600} = \frac{\pi}{16} \approx \mathbf{0.20} \quad (20\%).$$

---

#### Detailed Solutions to Level ★★★ Exercises

- **Exercise 12 (The Chevalier de Méré):**
  1. Probability of not rolling a 6: $P(\text{not 6}) = \frac{5}{6}$.
  2. Over 4 independent rolls, probability of rolling no 6s:
     $$P(\text{no 6s}) = \left(\frac{5}{6}\right)^4 = \frac{625}{1{,}296} \approx 0.4823.$$
  3. Probability of getting at least one 6:
     $$P(\text{at least one 6}) = 1 - 0.4823 = \mathbf{0.5177} \approx \mathbf{51.8\%}.$$
     Since $51.8\% > 50\%$, the probability is strictly greater than one half: the Chevalier de Méré was right, in the long run he was guaranteed a profit!

- **Exercise 13 (Python Simulation):**
  1. Theoretical probability: $p = \frac{1}{6} \approx \mathbf{0.167}$.
  2. The program will display a value very close to $0.167$ (for example $0.1658$ or $0.1682$).
  3. Due to **sampling variability (fluctuation)**, chance produces minor variations around the theoretical mean. Only at infinity would the equality become exact.

- **Exercise 14 (The Birthday Paradox):**
  1. For the 2nd student to have a different birthday from the 1st: $\frac{364}{365}$.
  2. For the 3rd student: $\frac{363}{365}$.
  3. The probability that all 25 students have distinct birthdays is the product of these 25 fractions: $P(\text{all distinct}) \approx 0.43$.
     Therefore, the probability that at least two students share the same birthday is:
     $$P(\text{at least two identical}) = 1 - 0.43 = \mathbf{0.57} \quad (\mathbf{57\%}).$$
     Since $57\% > 50\%$, the teacher was completely right: there is more than a 1 in 2 chance!

- **Exercise 15 (Pascal and Fermat Leading 2 to 0):**
  1. Player A needs only 1 more win (leading 2-0). Player B must win 3 consecutive rounds to win 3-2. At most **3 additional rounds** are required.
  2. Tree of remaining rounds:
     - Round 1: either A wins ($1/2$) $\implies$ A wins match (3-0).
     - Or B wins ($1/2$):
       - Round 2: either A wins ($1/4$) $\implies$ A wins match (3-1).
       - Or B wins ($1/4$):
         - Round 3: either A wins ($1/8$) $\implies$ A wins match (3-2).
         - Or B wins ($1/8$) $\implies$ B wins match (3-3 final).
  3. Player B wins in only one scenario: winning all 3 consecutive rounds, with probability:
     $$P(\text{B wins}) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \mathbf{\frac{1}{8}} = \mathbf{12.5\%}.$$
     Player A therefore has $P(\text{A wins}) = 1 - \frac{1}{8} = \mathbf{\frac{7}{8}} = \mathbf{87.5\%}$.
  4. Fair division of the 100 pistoles:
     - For A: $\frac{7}{8} \times 100 = \mathbf{87.5\text{ pistoles}}$.
     - For B: $\frac{1}{8} \times 100 = \mathbf{12.5\text{ pistoles}}$.

---

### The Question That Opens the Future

Here ends our grand journey through Middle School (*Collège*).
You began with the mystery of Al-Khwarizmi's letters, balanced scale pans, conquered the Pythagorean Theorem, measured the Earth with Eratosthenes, unlocked the secrets of Euclid, and learned to tame uncertainty with Pascal and Fermat.

Yet an immense frontier now stands before you. Until now, our numbers were either discrete counters on fingers or static lengths locked within stationary figures.
What happens when the wind blows, when a sailboat battles the crosscurrent in the heart of a storm? How can we represent a force that pulls in a specific direction with a precise magnitude?
Welcome to High School (*Lycée*): in Volume V, numbers will take flight, grow arrows, soar into the sky, and become **vectors**.
