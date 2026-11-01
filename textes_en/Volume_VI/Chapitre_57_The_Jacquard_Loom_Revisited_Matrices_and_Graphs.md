# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 57: The Jacquard Loom Revisited: Matrices and Graphs

> *“In 1801 in Lyon, Joseph Marie Jacquard punched holes into cards to guide the silk threads of his loom: a grid of perforations orchestrated the rising and falling of shuttles to weave patterns of boundless complexity. Matrices are the Jacquard punched cards of modern algebra: grids of numbers capable of distorting space, enumerating the paths of a network, and predicting the future equilibrium of the world's flows.”*

---

### What You Will Discover

- How a **matrix** encapsulates a table of operations and transforms vectors via the row $\times$ column product.
- Why matrix multiplication is associative but **non-commutative** ($AB \neq BA$), and how the identity matrix $I_n$ functions.
- Computing the **inverse of a $2 \times 2$ matrix** using the determinant and instantly solving linear systems $AX = B$.
- Modeling networks using **graphs** and the **adjacency matrix**.
- The fundamental theorem proving why the $k$-th power of an adjacency matrix $M^k$ counts precisely the **number of paths of length $k$**.
- **Markov chains** and probabilistic graphs: calculating the **steady state** and the foundations of Google's PageRank algorithm.

---

### 1. The Problem: World Networks and Control Arrays

#### 1.1 Airline Flight Routes
Consider a small airline operating across four cities: Paris (P), London (L), Madrid (M), and Rome (R).
The daily nonstop flights are as follows:
- From Paris to London, Madrid, and Rome.
- From London to Paris and Madrid.
- From Madrid to Paris and Rome.
- From Rome to Paris only.

If a passenger wishes to travel from London to Rome, there is no direct flight. But can they make the trip with **exactly one layover** (a two-flight itinerary)? What about two layovers?
How many possible routes exist?

Searching by hand quickly becomes confusing as the branching tree grows. But if we record these connections in a **binary grid** (1 if there is a flight, 0 otherwise), and multiply this grid by itself, a miracle occurs: **matrix algebra instantly counts the set of all possible paths on any network!**

#### 1.2 Weather and Long-Term Forecasts
In a coastal region, we observe the weather day after day:
- If it is sunny today, there is an 80% chance it will be sunny tomorrow, and a 20% chance of rain.
- If it rains today, there is a 40% chance it will be sunny tomorrow, and a 60% chance of rain.

What will the weather be like in one week? In one year?
Does there exist an average long-term equilibrium climate (for instance, 65% sunny days and 35% rainy days) toward which the system inevitably converges, regardless of today's weather?
To answer this question, we must merge probability theory with matrix algebra: this is the theory of **Markov chains**.

---

### 2. The Matrix Object and Its Operations

#### 2.1 Definition of a Matrix

> **📐 Definition — Matrix**
> Let $n$ and $p$ be positive integers.
> A **matrix** of dimension (or size) $n \times p$ (read “$n$ rows, $p$ columns”) with real coefficients is a rectangular array of numbers arranged in $n$ rows and $p$ columns:
>
> $$A = \begin{pmatrix}
> a_{1,1} & a_{1,2} & \dots & a_{1,p} \\
> a_{2,1} & a_{2,2} & \dots & a_{2,p} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n,1} & a_{n,2} & \dots & a_{n,p}
> \end{pmatrix} = (a_{i,j})_{\substack{1 \leq i \leq n \\ 1 \leq j \leq p}}$$
>
> The entry $a_{i,j}$ is located at the intersection of the $i$-th row and the $j$-th column.
> The set of $n \times p$ matrices with real coefficients is denoted by $\mathcal{M}_{n,p}(\mathbb{R})$.

*Terminology:*
- If $n = p$, the matrix is called **square** of order $n$. The set is denoted $\mathcal{M}_n(\mathbb{R})$.
- If $n = 1$, it is a **row matrix**: $(x_1 \ x_2 \ \dots \ x_p)$.
- If $p = 1$, it is a **column matrix**: $\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$.
- The **zero matrix** (denoted $0_{n,p}$) has all its entries equal to zero.

#### 2.2 Addition and Scalar Multiplication
- **Addition:** If $A$ and $B$ have the **same dimensions** $n \times p$, the sum $A + B$ is obtained by adding corresponding entries:
  $$(A + B)_{i,j} = a_{i,j} + b_{i,j}$$
- **Scalar multiplication by $\lambda \in \mathbb{R}$:** Multiply every entry by $\lambda$:
  $$(\lambda A)_{i,j} = \lambda a_{i,j}$$

#### 2.3 Matrix Multiplication: Row by Column
Multiplication of two matrices is **not** element-wise! It captures the composition of linear maps.

> **📐 Definition — Matrix Product**
> Let $A$ be a matrix of size $n \times \mathbf{k}$ and $B$ a matrix of size $\mathbf{k} \times p$.
> *(The number of columns of $A$ must strictly equal the number of rows of $B$!)*
> The product $C = A \times B$ is an $n \times p$ matrix whose general entry $c_{i,j}$ is the dot product of the **$i$-th row of $A$** with the **$j$-th column of $B$**:
>
> $$c_{i,j} = \sum_{m=1}^k a_{i,m} \cdot b_{m,j} = a_{i,1}b_{1,j} + a_{i,2}b_{2,j} + \dots + a_{i,k}b_{k,j}$$

```
                Row i of A : ( a_i,1   a_i,2  ...  a_i,k )
                                       │
                                       ▼
                Column j of B : ┌ b_1,j ┐
                                │ b_2,j │
                                │  ...  │
                                └ b_k,j ┘
                                       │
                                       ▼
  c_i,j = a_i,1 · b_1,j + a_i,2 · b_2,j + ... + a_i,k · b_k,j
```

*Fundamental $2 \times 2$ example:*
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x & y \\ z & t \end{pmatrix} = \begin{pmatrix} ax + bz & ay + bt \\ cx + dz & cy + dt \end{pmatrix}$$

#### 2.4 Properties and Pitfalls of Matrix Multiplication

> **⚠️ Warning: Pitfall! — Non-Commutativity in General**
> For two square matrices $A$ and $B$, in general:
> $$\mathbf{A B \neq B A}$$
> *Example:*
> $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
> $AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ whereas $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$!
> They do not commute. Consequently, standard algebraic identities like $(A+B)^2 = A^2 + 2AB + B^2$ are **false** for matrices (the correct expansion is $(A+B)^2 = A^2 + AB + BA + B^2$).

> **⚠️ Second Pitfall — Zero Divisors**
> For real numbers, $ab = 0 \implies a = 0 \text{ or } b = 0$.
> **This fails for matrices!**
> Take $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$:
> $$A^2 = A \times A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0_2$$
> The product of two nonzero matrices can be the zero matrix!

#### 2.5 Identity Matrix and Powers
The **identity matrix** of order $n$, denoted $I_n$, has 1s on its main diagonal and 0s elsewhere:
$$I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
For any square matrix $A \in \mathcal{M}_n(\mathbb{R})$:
$$A \times I_n = I_n \times A = A$$
For any integer $k \in \mathbb{N}$, the power $A^k$ is defined by $A^0 = I_n$ and $A^k = \underbrace{A \times A \times \dots \times A}_{k \text{ factors}}$.

---

### 3. Matrix Inversion and Linear Systems

#### 3.1 Definition of Invertibility

> **📐 Definition — Invertible Matrix**
> A square matrix $A \in \mathcal{M}_n(\mathbb{R})$ is called **invertible** if there exists a square matrix $B \in \mathcal{M}_n(\mathbb{R})$ such that:
> $$A B = B A = I_n$$
> If such a matrix exists, it is unique. It is called the **inverse matrix** of $A$ and is denoted **$A^{-1}$**.

*(⚠️ There is no matrix “division” $\frac{B}{A}$! One multiplies by the inverse $A^{-1}$, carefully respecting left-multiplication versus right-multiplication).*

#### 3.2 Inversion of $2 \times 2$ Matrices

> **📐 Theorem — Inverse of a $2 \times 2$ Matrix**
> Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
> The **determinant** of $A$ is the real number:
> $$\det(A) = ad - bc$$
> 1. The matrix $A$ is **invertible if and only if $\det(A) \neq 0$**.
> 2. If $\det(A) \neq 0$, its inverse is given by the formula:
>
> $$\mathbf{A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}}$$

*Direct proof by verification:*
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \begin{pmatrix} ad - bc & 0 \\ 0 & ad - bc \end{pmatrix} = (ad - bc) I_2$$
Dividing by the nonzero real number $ad - bc$ yields $I_2$ rigorously.

#### 3.3 Solving Linear Systems via Matrix Inversion
Consider a system of two equations in two variables:
$$\begin{cases} ax + by = \alpha \\ cx + dy = \beta \end{cases}$$
This system can be written as a single matrix equation:
$$A X = B \quad \text{with } A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \ X = \begin{pmatrix} x \\ y \end{pmatrix}, \ B = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$$

If $\det(A) = ad - bc \neq 0$, the matrix $A$ is invertible.
Multiplying **on the left by $A^{-1}$**:
$$A^{-1} (A X) = A^{-1} B \iff (A^{-1} A) X = A^{-1} B \iff I_2 X = A^{-1} B$$
From which we obtain the unique solution:
$$\mathbf{X = A^{-1} B}$$

---

### 4. Graphs and Adjacency Matrices

#### 4.1 Graph Terminology
A **graph** $G = (V, E)$ consists of:
- A set of **vertices** (or nodes) denoted $\{1, 2, \dots, n\}$.
- A set of **edges** (bidirectional links in an undirected graph) or **arcs** (directed arrows from one vertex to another in a directed graph).
- The **degree** of a vertex is the number of edges connected to it.
- A **walk** (or path) of length $k$ is a sequence of $k$ consecutive edges connecting an initial vertex to a destination vertex.

#### 4.2 The Adjacency Matrix

> **📐 Definition — Adjacency Matrix**
> Let $G$ be a graph of order $n$ whose vertices are labeled from 1 to $n$.
> The **adjacency matrix** of $G$ is the square matrix $M \in \mathcal{M}_n(\mathbb{R})$ whose entry in row $i$ and column $j$ is:
> $$m_{i,j} = \text{number of edges (or arcs) going from vertex } i \text{ to vertex } j$$
> *(In a simple undirected graph, $m_{i,j} \in \{0, 1\}$ and $M$ is symmetric: $m_{i,j} = m_{j,i}$).*

```
       3-Vertex Graph                     Adjacency Matrix M
             (1)
            /   ▲                          To 1    To 2    To 3
           /     \                       ┌                       ┐
          ▼       \               From 1 │   0       1       0   │
         (2) ───► (3)             From 2 │   0       0       1   │
                                  From 3 │   1       0       0   │
                                         └                       ┘
```

#### 4.3 The Fundamental Theorem of Paths of Length $k$

> **📐 Fundamental Theorem — Powers of the Adjacency Matrix**
> Let $M$ be the adjacency matrix of a graph with $n$ vertices.
> For every positive integer $k \geq 1$, the entry in the $i$-th row and $j$-th column of the matrix **$M^k$** equals the **number of paths of length $k$ from vertex $i$ to vertex $j$**.

> **✍️ Required Proof by Induction**
> Let $c_{i,j}^{(k)}$ denote the $(i, j)$ entry of the matrix $M^k$, and $N_{i,j}^{(k)}$ denote the number of paths of length $k$ from $i$ to $j$.
> Let us prove by mathematical induction on $k \geq 1$ the property $\mathcal{P}(k): \text{“For all } i, j, \ c_{i,j}^{(k)} = N_{i,j}^{(k)}\text{”}$.
>
> - **Base case ($k = 1$):**
>   $M^1 = M$. By definition of the adjacency matrix, $c_{i,j}^{(1)} = m_{i,j}$ is exactly the number of direct edges from $i$ to $j$, which is the number of paths of length 1. Thus $\mathcal{P}(1)$ holds.
>
> - **Inductive step:**
>   Assume the property holds for some $k \geq 1$: for all vertices $i$ and $m$, $c_{i,m}^{(k)} = N_{i,m}^{(k)}$.
>   Consider a path of length $k+1$ from $i$ to $j$.
>   Such a path consists of a path of length $k$ from $i$ to some intermediate vertex $m$, followed by a direct edge from $m$ to $j$ (of length 1).
>   By the addition and multiplication counting principles (Chapter 53), the total number of such paths is the sum over all possible intermediate vertices $m \in \{1, \dots, n\}$:
>   $$N_{i,j}^{(k+1)} = \sum_{m=1}^n N_{i,m}^{(k)} \times m_{m,j}$$
>   By the induction hypothesis, $N_{i,m}^{(k)} = c_{i,m}^{(k)}$. Hence:
>   $$N_{i,j}^{(k+1)} = \sum_{m=1}^n c_{i,m}^{(k)} \cdot m_{m,j}$$
>   This sum is precisely the formula for the matrix product of row $i$ of $M^k$ with column $j$ of $M$!
>   It is exactly the entry $(i, j)$ of the matrix $M^k \times M = M^{k+1}$.
>   Therefore $N_{i,j}^{(k+1)} = c_{i,j}^{(k+1)}$, proving the inductive step.
>
> - **Conclusion:** By induction, the property holds for all $k \geq 1$.

---

### 5. Markov Chains and Probabilistic Graphs

#### 5.1 Probabilistic Graphs and Transition Matrices
A random system evolves over discrete time steps among $k$ possible states (for example: States $E_1, E_2, \dots, E_k$).
At each unit of time (step $n$), the system transitions from one state to another according to fixed probabilities.

> **📐 Definition — Transition Matrix**
> The **transition matrix** $T$ of a probabilistic graph with $k$ states is the $k \times k$ square matrix whose entry $t_{i,j}$ is the conditional probability of moving to state $j$ given that the system is currently in state $i$:
> $$t_{i,j} = P_{(E_i)}(E_j)$$
> **Stochastic property:** Along each row of $T$, the sum of entries equals 1:
> $$\sum_{j=1}^k t_{i,j} = 1 \quad (\text{since the sum of outgoing transition probabilities from any vertex equals 1})$$

#### 5.2 Evolution of the Probability Distribution
Let $P_n$ denote the **row vector** of state probabilities at step $n$:
$$P_n = \begin{pmatrix} p_n^{(1)} & p_n^{(2)} & \dots & p_n^{(k)} \end{pmatrix} \quad \text{with } \sum_{i=1}^k p_n^{(i)} = 1$$

> **📐 Theorem — Matrix Recurrence Formula**
> By the law of total probability:
> $$\mathbf{P_{n+1} = P_n \times T}$$
> By immediate induction, for any integer $n \in \mathbb{N}$:
> $$\mathbf{P_n = P_0 \times T^n}$$

```
                2-State Probabilistic Graph
                      0.8
                    ┌─────┐
                    ▼     │
                   ( A ) ─┼─────── 0.2 ──────► ( B ) ◄───┐
                          │                              │ 0.6
                          └─────── 0.4 ─────── (   ) ────┘
                                                 ▲
```
For this graph, the transition matrix is:
$$T = \begin{pmatrix} 0.8 & 0.2 \\ 0.4 & 0.6 \end{pmatrix}$$
*(Row checks: $0.8 + 0.2 = 1$ and $0.4 + 0.6 = 1$).*

#### 5.3 The Steady State (Stationary Distribution)

What happens to $P_n$ when the number of steps $n$ becomes very large?

> **📐 Definition & Theorem — Steady State**
> A probability row vector $P = \begin{pmatrix} x & y \end{pmatrix}$ (or $\begin{pmatrix} x & y & z \end{pmatrix}$) is called a **steady state** (or stationary distribution) of the Markov chain if it satisfies:
>
> $$\mathbf{P = P \times T} \quad \text{with} \quad \sum x_i = 1 \text{ and } x_i \geq 0$$
>
> If all entries of the transition matrix $T$ (or one of its powers) are strictly positive (the graph is connected and aperiodic), then:
> Regardless of the initial state $P_0$, the sequence of distributions $(P_n)$ converges toward this unique steady state:
> $$\mathbf{\lim_{n \to +\infty} P_n = P}$$

*Calculation method for 2 states:*
Let $P = \begin{pmatrix} x & y \end{pmatrix}$ with $x + y = 1 \implies y = 1 - x$.
The equation $P = PT$ gives:
$$\begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 0.8 & 0.2 \\ 0.4 & 0.6 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}$$
This is equivalent to the system:
$$\begin{cases} 0.8x + 0.4y = x \\ 0.2x + 0.6y = y \end{cases} \iff -0.2x + 0.4y = 0 \iff 0.4y = 0.2x \iff x = 2y$$
Since $x + y = 1$:
$$2y + y = 1 \iff 3y = 1 \iff y = \frac{1}{3} \quad \text{and} \quad x = \frac{2}{3}$$
The steady state is therefore $P = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} \end{pmatrix}$.
In the long run, the weather will be sunny two-thirds of the time ($\approx 66.7\%$) and rainy one-third of the time ($\approx 33.3\%$), regardless of today's weather!

---

### 6. Google's PageRank: A Giant Matrix Network

In 1998, two Stanford doctoral students, **Larry Page and Sergey Brin**, founded the search engine **Google**.
Their stroke of genius was dubbed **PageRank**.
The World Wide Web is modeled as a massive directed graph where each web page is a vertex and each hyperlink is an arc.
A virtual surfer traverses the Web at random:
- From a page with $k$ outgoing links, the surfer chooses one with probability $\frac{1}{k}$.
- With a small damping probability $\alpha \approx 0.15$, the surfer gets bored and jumps to a completely random page anywhere on the Web.

This random walk is a Markov chain on a matrix measuring billions by billions!
The steady state of this matrix assigns an occupancy probability to each webpage: **the most important pages are those whose component in the steady state is the largest**.
A simple equation $P = PT$ laid the foundation for the most powerful technological empire of the 21st century!

---

### 7. Step-by-Step Solved Examples

#### Example 1: Matrix Multiplication and Non-Commutativity
Let $A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 0 \\ -1 & 4 \end{pmatrix}$.
1. Compute $A \times B$.
2. Compute $B \times A$.
3. What can be concluded?

**Detailed Solution:**
1. Computing $A \times B$:
   - Row 1, Col 1: $1 \times 2 + 2 \times (-1) = 2 - 2 = 0$
   - Row 1, Col 2: $1 \times 0 + 2 \times 4 = 8$
   - Row 2, Col 1: $3 \times 2 + (-1) \times (-1) = 6 + 1 = 7$
   - Row 2, Col 2: $3 \times 0 + (-1) \times 4 = -4$
   $$A B = \begin{pmatrix} 0 & 8 \\ 7 & -4 \end{pmatrix}$$
2. Computing $B \times A$:
   - Row 1, Col 1: $2 \times 1 + 0 \times 3 = 2$
   - Row 1, Col 2: $2 \times 2 + 0 \times (-1) = 4$
   - Row 2, Col 1: $(-1) \times 1 + 4 \times 3 = -1 + 12 = 11$
   - Row 2, Col 2: $(-1) \times 2 + 4 \times (-1) = -2 - 4 = -6$
   $$B A = \begin{pmatrix} 2 & 4 \\ 11 & -6 \end{pmatrix}$$
3. We observe that $A B \neq B A$. Matrix multiplication is not commutative.

#### Example 2: Inversion and System Solving
Consider the system:
$$\begin{cases} 3x + 5y = 11 \\ 2x + 4y = 8 \end{cases}$$
1. Write the system in matrix form $A X = B$.
2. Compute $\det(A)$ and deduce $A^{-1}$.
3. Solve the system via the calculation $X = A^{-1} B$.

**Detailed Solution:**
1. Matrix form:
   $$\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 11 \\ 8 \end{pmatrix}$$
   with $A = \begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 11 \\ 8 \end{pmatrix}$.
2. Computing the determinant:
   $$\det(A) = 3 \times 4 - 5 \times 2 = 12 - 10 = 2 \neq 0$$
   Since $\det(A) \neq 0$, $A$ is invertible.
   Using the inverse formula:
   $$A^{-1} = \frac{1}{2} \begin{pmatrix} 4 & -5 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -2.5 \\ -1 & 1.5 \end{pmatrix}$$
3. Solving:
   $$X = A^{-1} B = \frac{1}{2} \begin{pmatrix} 4 & -5 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 11 \\ 8 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 4 \times 11 + (-5) \times 8 \\ (-2) \times 11 + 3 \times 8 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 44 - 40 \\ -22 + 24 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
   The unique solution is **$x = 2$ and $y = 1$**.
   *(Verification: $3(2) + 5(1) = 6 + 5 = 11$ and $2(2) + 4(1) = 4 + 4 = 8$).*

#### Example 3: Counting Paths in a Graph
Let $G$ be a 3-vertex graph with vertices $S_1, S_2, S_3$ whose adjacency matrix is:
$$M = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$
*(This is the complete triangle $K_3$ where every vertex is linked to every other).*
1. Compute $M^2$.
2. Deduce the number of paths of length 2 connecting $S_1$ to itself, and connecting $S_1$ to $S_2$.
3. Compute $M^3$ and determine the number of paths of length 3 connecting $S_1$ to $S_2$.

**Detailed Solution:**
1. Computing $M^2$:
   $$M^2 = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0+1+1 & 0+0+1 & 0+1+0 \\ 0+0+1 & 1+0+1 & 1+0+0 \\ 0+1+0 & 1+0+0 & 1+1+0 \end{pmatrix} = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$
2. - Entry $(1, 1)$ of $M^2$ equals 2: there are **2 paths of length 2** from $S_1$ to $S_1$ (the round-trips $S_1 \to S_2 \to S_1$ and $S_1 \to S_3 \to S_1$).
   - Entry $(1, 2)$ of $M^2$ equals 1: there is **1 path of length 2** from $S_1$ to $S_2$ ($S_1 \to S_3 \to S_2$).
3. Computing $M^3 = M^2 \times M$:
   $$M^3 = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0+1+1 & 2+0+1 & 2+1+0 \\ 0+2+1 & 1+0+1 & 1+2+0 \\ 0+1+2 & 1+0+2 & 1+1+0 \end{pmatrix} = \begin{pmatrix} 2 & 3 & 3 \\ 3 & 2 & 3 \\ 3 & 3 & 2 \end{pmatrix}$$
   Entry $(1, 2)$ of $M^3$ equals **3**: there are exactly 3 paths of length 3 from $S_1$ to $S_2$ ($S_1 \to S_2 \to S_1 \to S_2$, $S_1 \to S_2 \to S_3 \to S_2$, and $S_1 \to S_3 \to S_1 \to S_2$).

#### Example 4: 3-State Markov Chain (Phone Subscriptions)
Three mobile operators A, B, and C share a market. Each year:
- Operator A retains 70% of its customers, losing 20% to B and 10% to C.
- Operator B retains 60% of its customers, losing 20% to A and 20% to C.
- Operator C retains 80% of its customers, losing 10% to A and 10% to B.
1. Write the transition matrix $T$.
2. If the initial market shares are $P_0 = \begin{pmatrix} 0.5 & 0.3 & 0.2 \end{pmatrix}$, compute the shares after one year $P_1$.
3. Determine the market's steady state $P = \begin{pmatrix} x & y & z \end{pmatrix}$.

**Detailed Solution:**
1. Transition matrix:
   $$T = \begin{pmatrix} 0.7 & 0.2 & 0.1 \\ 0.2 & 0.6 & 0.2 \\ 0.1 & 0.1 & 0.8 \end{pmatrix}$$
   *(Each row sums to 1).*
2. Shares after one year:
   $$P_1 = P_0 \times T = \begin{pmatrix} 0.5 & 0.3 & 0.2 \end{pmatrix} \begin{pmatrix} 0.7 & 0.2 & 0.1 \\ 0.2 & 0.6 & 0.2 \\ 0.1 & 0.1 & 0.8 \end{pmatrix}$$
   - For A: $0.5 \times 0.7 + 0.3 \times 0.2 + 0.2 \times 0.1 = 0.35 + 0.06 + 0.02 = 0.43$ ($43\%$)
   - For B: $0.5 \times 0.2 + 0.3 \times 0.6 + 0.2 \times 0.1 = 0.10 + 0.18 + 0.02 = 0.30$ ($30\%$)
   - For C: $0.5 \times 0.1 + 0.3 \times 0.2 + 0.2 \times 0.8 = 0.05 + 0.06 + 0.16 = 0.27$ ($27\%$)
   $$P_1 = \begin{pmatrix} 0.43 & 0.30 & 0.27 \end{pmatrix}$$
3. The steady state satisfies $P = PT$ and $x + y + z = 1$:
   $$\begin{cases}
   0.7x + 0.2y + 0.1z = x \iff -0.3x + 0.2y + 0.1z = 0 \quad (L_1) \\
   0.2x + 0.6y + 0.1z = y \iff 0.2x - 0.4y + 0.1z = 0 \quad (L_2) \\
   x + y + z = 1 \quad (L_3)
   \end{cases}$$
   Subtract $(L_2)$ from $(L_1)$:
   $$(-0.3x - 0.2x) + (0.2y - (-0.4y)) + (0.1z - 0.1z) = 0 \iff -0.5x + 0.6y = 0 \iff x = \frac{6}{5}y = 1.2y$$
   Substitute $x$ into $(L_1)$ to express $z$:
   $$-0.3(1.2y) + 0.2y + 0.1z = 0 \iff -0.36y + 0.2y + 0.1z = 0 \iff 0.1z = 0.16y \iff z = 1.6y$$
   Use the normalization condition $x + y + z = 1$:
   $$1.2y + y + 1.6y = 1 \iff 3.8y = 1 \iff y = \frac{1}{3.8} = \frac{10}{38} = \frac{5}{19} \approx 0.2632$$
   Then:
   - $x = 1.2 \times \frac{5}{19} = \frac{6}{19} \approx 0.3158$
   - $z = 1.6 \times \frac{5}{19} = \frac{8}{19} \approx 0.4211$
   The steady state is:
   $$P = \begin{pmatrix} \frac{6}{19} & \frac{5}{19} & \frac{8}{19} \end{pmatrix} \approx \begin{pmatrix} 31.6\% & 26.3\% & 42.1\% \end{pmatrix}$$
   In the long run, operator C will dominate the market with over 42% of customer share.

#### Example 5: $n$-th Power via Diagonalization (Simple Case)
Let $A = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$.
Given $P = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and its inverse $P^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
1. Compute the matrix $D = P^{-1} A P$ and verify that it is diagonal.
2. For all $n \in \mathbb{N}$, express $D^n$.
3. Deduce an explicit expression for $A^n$ in terms of $n$.

**Detailed Solution:**
1. First compute $A P$:
   $$A P = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 8-2 & 4-2 \\ 2+1 & 1+1 \end{pmatrix} = \begin{pmatrix} 6 & 2 \\ 3 & 2 \end{pmatrix}$$
   Compute $D = P^{-1} (A P)$:
   $$D = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 6 & 2 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 6-3 & 2-2 \\ -6+6 & -2+4 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$$
   $D$ is indeed a diagonal matrix.
2. For a diagonal matrix, powers apply directly to diagonal elements:
   $$D^n = \begin{pmatrix} 3^n & 0 \\ 0 & 2^n \end{pmatrix}$$
3. Since $D = P^{-1} A P$, multiplying by $P$ on the left and $P^{-1}$ on the right gives $A = P D P^{-1}$.
   By telescoping: $A^n = (P D P^{-1})(P D P^{-1})\dots(P D P^{-1}) = P D^n P^{-1}$.
   Compute the product:
   $$P D^n = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 3^n & 0 \\ 0 & 2^n \end{pmatrix} = \begin{pmatrix} 2 \cdot 3^n & 2^n \\ 3^n & 2^n \end{pmatrix}$$
   Then $(P D^n) P^{-1}$:
   $$A^n = \begin{pmatrix} 2 \cdot 3^n & 2^n \\ 3^n & 2^n \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 \cdot 3^n - 2^n & -2 \cdot 3^n + 2 \cdot 2^n \\ 3^n - 2^n & -3^n + 2 \cdot 2^n \end{pmatrix}$$
   *(Verification for $n = 1$: $A^1 = \begin{pmatrix} 6 - 2 & -6 + 4 \\ 3 - 2 & -3 + 4 \end{pmatrix} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix} = A$). Exact formula for all $n$!*

#### Example 6: Random Walk on a Triangle
A flea randomly hops among the vertices of a triangle $A, B, C$.
At each jump, it leaves its current vertex and chooses one of the other two vertices with equal probability ($p = 0.5$).
If the flea starts at vertex $A$ at time $n = 0$, what is the probability that it is back at $A$ after $n$ jumps?

**Detailed Solution:**
The transition matrix is:
$$T = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.5 & 0 & 0.5 \\ 0.5 & 0.5 & 0 \end{pmatrix}$$
Let $a_n$ be the probability of being at $A$ at step $n$. By obvious symmetry between $B$ and $C$, the probability of being at $B$ equals that of being at $C$, so $b_n = c_n$.
Since $a_n + b_n + c_n = 1$, we have $a_n + 2b_n = 1 \implies b_n = \frac{1 - a_n}{2}$.
From the first column of the transition matrix:
$$a_{n+1} = 0 \cdot a_n + 0.5 b_n + 0.5 c_n = 0.5(b_n + c_n) = 0.5(2b_n) = b_n = \frac{1 - a_n}{2} = -\frac{1}{2}a_n + \frac{1}{2}$$
This is an arithmetico-geometric sequence!
Finding the fixed point: $\ell = -\frac{1}{2}\ell + \frac{1}{2} \iff \frac{3}{2}\ell = \frac{1}{2} \iff \ell = \frac{1}{3}$.
Let $u_n = a_n - \frac{1}{3}$. Then $u_{n+1} = -\frac{1}{2} u_n$.
The sequence $(u_n)$ is geometric with common ratio $-\frac{1}{2}$ and first term $u_0 = a_0 - \frac{1}{3} = 1 - \frac{1}{3} = \frac{2}{3}$ (since the flea begins at $A$, $a_0 = 1$).
Hence:
$$u_n = \frac{2}{3} \left(-\frac{1}{2}\right)^n \implies a_n = \frac{1}{3} + \frac{2}{3} \left(-\frac{1}{2}\right)^n$$
- For $n = 0$: $a_0 = \frac{1}{3} + \frac{2}{3} = 1$.
- For $n = 1$: $a_1 = \frac{1}{3} - \frac{1}{3} = 0$ (it jumped to $B$ or $C$).
- For $n = 2$: $a_2 = \frac{1}{3} + \frac{2}{3} \times \frac{1}{4} = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$.
- As $n \to +\infty$: $\left(-\frac{1}{2}\right)^n \to 0$, so $a_n \to \frac{1}{3}$. The flea spends one-third of its time at each vertex.

---

### Key Takeaways

1. **Matrix Algebra:**
   - Product $A \times B$: dimension $(n \times k) \times (k \times p) \to (n \times p)$. Row by column.
   - Non-commutative in general: $AB \neq BA$.
   - Zero divisors: $AB = 0$ does not imply $A = 0$ or $B = 0$.

2. **Inversion and Systems:**
   - $2 \times 2$ Matrix: $\det(A) = ad - bc \neq 0 \iff A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
   - System solving: $AX = B \iff X = A^{-1} B$.

3. **Graphs and Adjacency Matrices:**
   - Adjacency matrix $M$: $m_{i,j}$ = number of edges connecting $i$ to $j$.
   - **Path Counting Theorem:** Entry $(i, j)$ of $M^k$ is the exact number of paths of length $k$ from $i$ to $j$.

4. **Markov Chains:**
   - Transition matrix $T$: each row sums to 1.
   - Evolution: $P_{n+1} = P_n \times T$ and $P_n = P_0 \times T^n$.
   - Steady state: unique vector satisfying $P = P \times T$ with $\sum p_i = 1$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 1.** Let $A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 5 \\ 1 & -2 \end{pmatrix}$.
Compute $2A - 3B$, $A \times B$, and $B \times A$.

**Exercise 2.** Compute the determinant and inverse (if it exists) of the following matrices:
$M_1 = \begin{pmatrix} 5 & 2 \\ 2 & 1 \end{pmatrix}$, $M_2 = \begin{pmatrix} 3 & -6 \\ -2 & 4 \end{pmatrix}$, $M_3 = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

**Exercise 3.** Solve the system in matrix form:
$$\begin{cases} 4x + 3y = 25 \\ 2x + 5y = 23 \end{cases}$$

**Exercise 4.** Consider an undirected graph with 4 vertices $\{A, B, C, D\}$ whose edges are $[A, B], [A, C], [B, C], [C, D]$.
1. Draw the graph.
2. Write its adjacency matrix $M$.
3. What is the degree of vertex $C$?

**Exercise 5.** A transition matrix is given by $T = \begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix}$.
If $P_0 = \begin{pmatrix} 0.6 & 0.4 \end{pmatrix}$, compute $P_1$ and $P_2$.

**Exercise 6.** Determine the steady state $P = \begin{pmatrix} x & y \end{pmatrix}$ associated with the transition matrix $T = \begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix}$ from Exercise 5.

**Exercise 7.** Compute $A^2$ and $A^3$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Conjecture $A^n$.

#### Level ★★ (Analytical Thinking & Probabilistic Graphs)

**Exercise 8.** Powers of a Nilpotent Matrix.
Let $N = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$.
1. Compute $N^2$ and $N^3$.
2. Deduce $N^k$ for all $k \geq 3$.
3. Let $A = I_3 + N$. Using the binomial theorem (justify its applicability), compute $A^n$ for all integers $n \geq 2$.

**Exercise 9.** Graph Connectedness.
Let $G$ be a graph of order 4 with adjacency matrix $M$.
We compute $S = M + M^2 + M^3$.
Prove that the graph is connected if and only if all off-diagonal entries of $S$ are strictly positive.

**Exercise 10.** Leslie Matrix Population Model.
A bird population is divided into two age classes: juveniles $J_n$ and adults $A_n$.
Each year:
- Adults give birth on average to 2 juveniles.
- 30% of juveniles survive and become adults the following year.
- 50% of adults survive.
1. Write the dynamical system in matrix form $\begin{pmatrix} J_{n+1} \\ A_{n+1} \end{pmatrix} = L \begin{pmatrix} J_n \\ A_n \end{pmatrix}$.
2. If the initial population consists of 100 juveniles and 50 adults, compute the population at $n = 1$ and $n = 2$.

**Exercise 11.** Matrix Equation $A^2 - 4A + 3I = 0$.
Let $A$ be a square matrix satisfying $A^2 - 4A + 3I = 0$.
1. Prove that $A$ is invertible and express $A^{-1}$ in terms of $A$ and $I$.
2. Show that for every $n \in \mathbb{N}$, there exist real numbers $a_n$ and $b_n$ such that $A^n = a_n A + b_n I$.

**Exercise 12.** 3-State Markov Chain: Rumor Propagation.
In a village, an individual learns a piece of news. At each step, they may share it with their neighbor.
The states are: $E_1$ (Ignorant), $E_2$ (Believer), $E_3$ (Skeptic/Immune).
Transition matrix:
$$T = \begin{pmatrix} 0.5 & 0.4 & 0.1 \\ 0 & 0.6 & 0.4 \\ 0 & 0 & 1 \end{pmatrix}$$
1. What is the status of state $E_3$ (absorbing state)?
2. Compute $T^2$ and $T^3$.
3. What happens to the population in the long run?

**Exercise 13.** Stochastic Matrix and Eigenvalue 1.
Let $T$ be an $n \times n$ stochastic matrix (row sums equal to 1).
Let $U$ be the column vector with all entries equal to 1.
1. Compute the matrix product $T \times U$.
2. What can be deduced about the system $(T - I_n) X = 0$?
3. Why does this prove that there always exists at least one nonzero steady state?

**Exercise 14.** Inverse of a $3 \times 3$ Matrix via Gauss-Jordan Elimination.
Invert the matrix $A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{pmatrix}$ by solving the system $AX = Y$.

**Exercise 15.** Number of Spanning Trees (Kirchhoff's Matrix Tree Theorem, Overview).
For a simple graph, define the Laplacian matrix $L = D - M$, where $D$ is the diagonal degree matrix and $M$ is the adjacency matrix.
Compute $L$ for a triangle $K_3$ and compute one of its cofactors. Compare with the number of possible spanning trees.

#### Level ★★★ (Advanced Explorations & Competition Problems)

**Exercise 16.** Cayley-Hamilton Theorem in Dimension 2.
Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
Define its trace $\text{Tr}(A) = a + d$ and its determinant $\det(A) = ad - bc$.
Prove by direct computation the fundamental Cayley-Hamilton identity:
$$A^2 - \text{Tr}(A) \cdot A + \det(A) \cdot I_2 = 0_2$$

**Exercise 17.** Second-Order Recurrence Relations and Matrix Powers (Fibonacci).
Let the Fibonacci sequence be defined by $F_0 = 0$, $F_1 = 1$, and $F_{n+2} = F_{n+1} + F_n$.
1. Determine a square matrix $A \in \mathcal{M}_2(\mathbb{R})$ such that $\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = A \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}$.
2. Prove by induction that for all $n \geq 1$:
   $$A^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$
3. By computing $\det(A^n)$ in two different ways, prove the famous **Cassini's identity**:
   $$F_{n+1} F_{n-1} - F_n^2 = (-1)^n$$

**Exercise 18.** Convergence of Transition Matrices and Spectral Projectors.
Let $T = \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}$ with $a, b \in (0, 1)$.
1. Show that $T$ has eigenvalues $\lambda_1 = 1$ and $\lambda_2 = 1 - a - b$.
2. Prove that $T^n = \frac{1}{a+b} \begin{pmatrix} b & a \\ b & a \end{pmatrix} + \frac{(1-a-b)^n}{a+b} \begin{pmatrix} a & -a \\ -b & b \end{pmatrix}$.
3. Deduce $\lim_{n \to +\infty} T^n$ and recover the steady state for any initial distribution.

**Exercise 19.** Perron-Frobenius Theorem (Statement and Geometric Meaning).
For a matrix with strictly positive entries, explain the significance of the Perron-Frobenius theorem: existence of a strictly positive dominant real eigenvalue and uniqueness of the associated positive eigenvector (the steady state).

**Exercise 20.** PageRank Algorithm with Damping Factor.
Write the Google matrix for a mini-web of 3 pages where page 1 links to 2 and 3, page 2 links to 3, and page 3 links to 1.
Incorporate the teleportation factor $\alpha = 0.85$ and compute the PageRank ranking of the 3 pages.

**Exercise 21.** Hadamard Matrices and Error-Correcting Codes.
A Hadamard matrix $H_n$ is an $n \times n$ matrix with entries in $\{-1, +1\}$ such that $H_n H_n^T = n I_n$.
Construct $H_2$ and $H_4$ via the Kronecker product and explain their role in signal transmission for the Mariner and Voyager deep space probes.

**Exercise 22.** Eulerian and Hamiltonian Graphs.
Prove Euler's theorem: a connected graph possesses an Eulerian circuit (a closed trail visiting every edge exactly once) if and only if every vertex has even degree.

---

### Solutions

**Solution 1.**
$2A - 3B = \begin{pmatrix} 4 & -2 \\ 6 & 8 \end{pmatrix} - \begin{pmatrix} 0 & 15 \\ 3 & -6 \end{pmatrix} = \begin{pmatrix} 4 & -17 \\ 3 & 14 \end{pmatrix}$.
$A \times B = \begin{pmatrix} 2(0)-1(1) & 2(5)-1(-2) \\ 3(0)+4(1) & 3(5)+4(-2) \end{pmatrix} = \begin{pmatrix} -1 & 12 \\ 4 & 7 \end{pmatrix}$.
$B \times A = \begin{pmatrix} 0(2)+5(3) & 0(-1)+5(4) \\ 1(2)-2(3) & 1(-1)-2(4) \end{pmatrix} = \begin{pmatrix} 15 & 20 \\ -4 & -9 \end{pmatrix}$.

**Solution 2.**
- $\det(M_1) = 5(1) - 2(2) = 1 \neq 0 \implies M_1^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -2 \\ -2 & 5 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -2 & 5 \end{pmatrix}$.
- $\det(M_2) = 3(4) - (-6)(-2) = 12 - 12 = 0$. $M_2$ is not invertible.
- $\det(M_3) = \cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1 \neq 0$.
  $M_3^{-1} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} = M_3(-\theta)$ (the inverse rotation!).

**Solution 3.**
$A = \begin{pmatrix} 4 & 3 \\ 2 & 5 \end{pmatrix}$, $\det(A) = 20 - 6 = 14 \neq 0$.
$A^{-1} = \frac{1}{14}\begin{pmatrix} 5 & -3 \\ -2 & 4 \end{pmatrix}$.
$X = A^{-1} B = \frac{1}{14}\begin{pmatrix} 5 & -3 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 25 \\ 23 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 125 - 69 \\ -50 + 92 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 56 \\ 42 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$.
Solution: $x = 4$ and $y = 3$.

**Solution 4.**
1. Diamond-shaped graph with an edge trailing to $D$.
2. Vertex ordering A, B, C, D:
   $$M = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
3. The degree of $C$ is the sum of row 3: $1 + 1 + 0 + 1 = 3$.

**Solution 5.**
$P_1 = P_0 T = \begin{pmatrix} 0.6 & 0.4 \end{pmatrix}\begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix} = \begin{pmatrix} 0.54+0.12 & 0.06+0.28 \end{pmatrix} = \begin{pmatrix} 0.66 & 0.34 \end{pmatrix}$.
$P_2 = P_1 T = \begin{pmatrix} 0.66 & 0.34 \end{pmatrix}\begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix} = \begin{pmatrix} 0.594+0.102 & 0.066+0.238 \end{pmatrix} = \begin{pmatrix} 0.696 & 0.304 \end{pmatrix}$.

**Solution 6.**
$P = PT \iff \begin{pmatrix} x & y \end{pmatrix}\begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}$ with $x + y = 1$.
$0.9x + 0.3y = x \iff 0.3y = 0.1x \iff x = 3y$.
$3y + y = 1 \iff 4y = 1 \iff y = 0.25$ and $x = 0.75$.
Steady state: $P = \begin{pmatrix} 0.75 & 0.25 \end{pmatrix}$.

**Solution 7.**
$A^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
$A^3 = A^2 A = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$.
By immediate induction: $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$.

**Solution 8.**
1. $N^2 = \begin{pmatrix} 0 & 0 & 6 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $N^3 = 0_3$.
2. For $k \geq 3$, $N^k = 0_3$.
3. Since $I_3$ and $N$ commute ($I_3 N = N I_3 = N$), the binomial theorem applies:
   $A^n = (I_3 + N)^n = \sum_{k=0}^n \binom{n}{k} I_3^{n-k} N^k = \binom{n}{0}I_3 + \binom{n}{1}N + \binom{n}{2}N^2 + 0 = I_3 + n N + \frac{n(n-1)}{2}N^2$.
   $A^n = \begin{pmatrix} 1 & 2n & n + 3n(n-1) \\ 0 & 1 & 3n \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2n & 3n^2 - 2n \\ 0 & 1 & 3n \\ 0 & 0 & 1 \end{pmatrix}$.

**Solution 9.**
In a graph with 4 vertices, if two distinct vertices $i$ and $j$ are connected, they can be reached via a path of length 1, 2, or at most 3 (without loops). The $(i, j)$ entry of $S = M + M^2 + M^3$ is the total count of paths of length 1, 2, and 3 connecting $i$ to $j$. It is strictly positive for every pair $(i, j)$ with $i \neq j$ if and only if every vertex can reach every other vertex, which is the very definition of connectedness.

**Solution 10.**
1. $\begin{cases} J_{n+1} = 2 A_n \\ A_{n+1} = 0.3 J_n + 0.5 A_n \end{cases} \iff \begin{pmatrix} J_{n+1} \\ A_{n+1} \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0.3 & 0.5 \end{pmatrix} \begin{pmatrix} J_n \\ A_n \end{pmatrix}$.
2. For $n = 0$, $X_0 = \begin{pmatrix} 100 \\ 50 \end{pmatrix}$.
   $X_1 = \begin{pmatrix} 0 & 2 \\ 0.3 & 0.5 \end{pmatrix}\begin{pmatrix} 100 \\ 50 \end{pmatrix} = \begin{pmatrix} 100 \\ 55 \end{pmatrix}$.
   $X_2 = \begin{pmatrix} 0 & 2 \\ 0.3 & 0.5 \end{pmatrix}\begin{pmatrix} 100 \\ 55 \end{pmatrix} = \begin{pmatrix} 110 \\ 57.5 \end{pmatrix}$.

**Solution 11.**
1. $A^2 - 4A = -3I \iff A(A - 4I) = -3I \iff A \times \left[-\frac{1}{3}(A - 4I)\right] = I$.
   Thus $A$ is invertible and $A^{-1} = -\frac{1}{3}A + \frac{4}{3}I$.
2. By polynomial Euclidean division of $X^n$ by $X^2 - 4X + 3 = (X-1)(X-3)$:
   $X^n = (X^2 - 4X + 3)Q(X) + a_n X + b_n$.
   Evaluating at $A$ yields $A^n = a_n A + b_n I$.

**Solution 12.**
1. Row 3 is $(0 \ 0 \ 1)$: once in state $E_3$ (skeptic), the probability of remaining there is 1. It is a permanent absorbing state.
2. By computing powers, the first two rows have transition probabilities toward $E_3$ that strictly increase at each step.
3. In the long run, $\lim_{n \to +\infty} T^n = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$. The entire population ends up in the skeptic/immune state $E_3$.

**Solution 13.**
1. Entry $i$ of $T \times U$ is the sum of entries along row $i$ of $T$, which equals 1 by definition of a stochastic matrix. Hence $T \times U = U = 1 \cdot U$.
2. This implies $(T - I_n)U = 0$. The homogeneous system admits a nontrivial solution ($U \neq 0$), so $\det(T - I_n) = 0$.
3. Since $\det(T^T - I_n) = \det(T - I_n) = 0$, there also exists a nonzero row vector $P$ such that $P(T - I_n) = 0 \iff PT = P$. Normalizing so that $\sum p_i = 1$ yields a steady state.

**Solution 14.**
Solving $\begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$.
By row elimination: $L_2 \leftarrow L_2 - 2L_1$ and $L_3 \leftarrow L_3 - 4L_1$, we find $z = a + b - \frac{1}{2}(c - 4a - \dots)$.
Inverting gives $A^{-1} = \begin{pmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{pmatrix}$.

**Solution 15.**
For the triangle $K_3$, each vertex has degree 2: $D = 2I_3$.
$L = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix}$.
The cofactor obtained by deleting row 1 and column 1 is $\det\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = 4 - 1 = 3$.
By Kirchhoff's theorem, there are exactly 3 spanning trees (the 3 ways of removing one edge to form a tree), matching perfectly.

**Solution 16.**
$\text{Tr}(A) = a+d$ and $\det(A) = ad - bc$.
$A^2 = \begin{pmatrix} a^2+bc & ab+bd \\ ca+dc & cb+d^2 \end{pmatrix}$.
$(a+d)A = \begin{pmatrix} a^2+ad & ab+bd \\ ca+cd & ad+d^2 \end{pmatrix}$.
$A^2 - (a+d)A = \begin{pmatrix} bc-ad & 0 \\ 0 & bc-ad \end{pmatrix} = -(ad-bc)I_2 = -\det(A)I_2$.
Hence $A^2 - \text{Tr}(A)A + \det(A)I_2 = 0_2$.

**Solution 17.**
1. Since $F_{n+1} = 1 \cdot F_n + 1 \cdot F_{n-1}$ and $F_n = 1 \cdot F_n + 0 \cdot F_{n-1}$, the matrix is $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
2. For $n = 1$: $A^1 = \begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
   The inductive step follows immediately by multiplying by $A$ and applying the Fibonacci recurrence.
3. $\det(A) = 1(0) - 1(1) = -1$.
   Thus $\det(A^n) = (\det A)^n = (-1)^n$.
   On the other hand, $\det(A^n) = F_{n+1}F_{n-1} - F_n^2$. Equating the two yields Cassini's identity.

**Solution 18.**
1. Characteristic polynomial $\det(T - \lambda I) = (\lambda - 1)(\lambda - (1 - a - b))$. The roots are 1 and $1 - a - b$.
2. Diagonalizing $T = P D P^{-1}$ with $D = \begin{pmatrix} 1 & 0 \\ 0 & 1-a-b \end{pmatrix}$, computing $P D^n P^{-1}$ gives exactly the stated decomposition.
3. Since $|1 - a - b| < 1$, $(1-a-b)^n \to 0$.
   The limit is $\frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix}$.
   For any $P_0 = (x \ 1-x)$, $P_0 \lim T^n = \begin{pmatrix} \frac{b}{a+b} & \frac{a}{a+b} \end{pmatrix}$, which is the universal steady state.

**Solution 19.**
The Perron-Frobenius theorem guarantees that for any matrix with strictly positive entries, the eigenvalue of largest magnitude is real, strictly positive, simple, and its corresponding eigenvector can be chosen with strictly positive entries. This ensures that no oscillating chaotic phenomena can disrupt convergence: the system always attains a stable and predictable global equilibrium.

**Solution 20.**
Raw link matrix: $H = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$.
Google matrix: $G = 0.85 H + 0.15 \times \frac{1}{3} J$, where $J$ is the all-ones matrix.
Solving $P = PG$ yields the relative importance of each page, with page 3 being the most heavily cited and receiving the highest rank.

**Solution 21.**
$H_2 = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
$H_4 = \begin{pmatrix} H_2 & H_2 \\ H_2 & -H_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{pmatrix}$.
These orthogonal matrices allow transmitting codes with maximum Hamming separation: even under heavy deep-space noise, the terrestrial receiver recovers the original signal through simple matrix correlation.

**Solution 22.**
At each visit to a vertex, a cycle uses one incoming edge and one outgoing edge, consuming 2 incident edges. Every vertex must therefore have an even degree. The converse follows by Fleury's algorithm or decomposition into edge-disjoint cycles.

---

### The Question That Opens the Future

We have reached the culmination of structures in our journey.
From the very first pebble you picked up from the ground at age six to learn how to count, to the transition matrices ordering billions of pages across global cyberspace, what an extraordinary path you have traveled!
Why do these symbols created by the human mind align with such flawless precision to the fabric of physical reality?
How do all branches of mathematics — arithmetic, geometry, analysis, probability — converge into one and the same mighty river?
It is time to gaze upon the panorama in all its grandeur: turn the final page and enter **Chapter 58 and The End of the Voyage**.
