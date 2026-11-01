# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)
## CHAPTER 56: Secret Messages and the Clock of Remainders

> *“On the face of a clock, after twelve o'clock does not come thirteen o'clock: the hand returns to one o'clock. This circular arithmetic, which every child practices without realizing it, is one of the deepest jewels of the human mind. It was by studying the remainders of divisions that Fermat unlocked the secret of powers, and that three centuries later, all of humanity learned to lock its digital secrets behind the indestructible padlock of prime numbers.”*

---

### What You Will Discover

- The rigorous structure of **divisibility in $\mathbb{Z}$** and **Euclidean division**.
- The fascinating world of **congruences modulo $n$**: circular arithmetic where numbers wind around a circle.
- The **extended Euclidean algorithm**, **Bézout's identity**, and the methodical resolution of **Diophantine equations** $ax + by = c$.
- **Gauss's lemma (theorem)**, a pillar of arithmetic, and its canonical proof.
- **Fermat's Little Theorem** and the method of **fast modular exponentiation**.
- The adventure of encryption: from the Caesar cipher and affine ciphers to the asymmetric **RSA** protocol, the shield of the modern Internet.

---

### 1. The Problem: Sending a Secret in Plain Sight

#### 1.1 Caesar's Courier and the Vulnerability of the Shared Key
Around 50 BCE, Julius Caesar sent military orders to his legions in Gaul. To prevent an intercepted courier from revealing his plans, he shifted each letter by 3 positions in the alphabet:
- A becomes D, B becomes E... X becomes A, Y becomes B, Z becomes C.
The recipient performs the inverse shift (-3).

This procedure has a glaring flaw: anyone who knows the rule can decipher all messages. Even when complicating the formula (affine cipher), frequency analysis of letters (with 'E' being the most common letter in French and English) breaks the code within minutes.

Yet the fundamental problem of classical cryptography is even more profound: **the key exchange problem**.
If Alice and Bob want to exchange secrets, they must first agree on a shared secret key. But how can they agree on this key without an eavesdropper sitting between them intercepting it?

#### 1.2 The Asymmetric Revolution (1977)
For two thousand years, monarchs and diplomats wrestled with this paradox.
Until 1977, when three researchers at MIT — **Ron Rivest, Adi Shamir, and Leonard Adleman** — pulled off a masterstroke: inventing a padlock with two distinct keys:
1. A **public key**, which anyone can inspect and use to lock the padlock (encrypt the message).
2. A **private key**, possessed solely by the recipient, indispensable for opening the padlock (decrypting the message).

The foundation of this unbreakable padlock relies on no mechanical apparatus: it rests on a theorem of arithmetic discovered by a Toulouse magistrate in **1640**, Pierre de Fermat, and on the theory of **congruences** developed by Carl Friedrich Gauss.

---

### 2. Divisibility and Euclidean Division in $\mathbb{Z}$

#### 2.1 Divisibility in the Set of Integers $\mathbb{Z}$

> **📐 Definition — Divisibility**
> Let $a \in \mathbb{Z}$ and $b \in \mathbb{Z}$.
> We say that **$a$ divides $b$** (or that $b$ is a **multiple** of $a$, or that $b$ is divisible by $a$), denoted by **$a \mid b$**, if there exists an integer $k \in \mathbb{Z}$ such that:
> $$b = k \cdot a$$

*Examples:*
- $7 \mid 42$ because $42 = 6 \times 7$.
- $-3 \mid 15$ because $15 = (-5) \times (-3)$.
- $5 \mid 0$ because $0 = 0 \times 5$ (every nonzero integer divides 0).
- 0 divides no nonzero number, because $0 \times k = 0 \neq b$.

> **📐 Fundamental Properties of Divisibility**
> 1. **Reflexivity:** For all $a \in \mathbb{Z}$, $a \mid a$.
> 2. **Transitivity:** If $a \mid b$ and $b \mid c$, then $a \mid c$.
> 3. **Linear combinations (essential!):**
>    If $a \mid b$ and $a \mid c$, then for all integers $u, v \in \mathbb{Z}$:
>    $$a \mid (u b + v c)$$

*Proof of linear combination:*
If $b = k_1 a$ and $c = k_2 a$, then $ub + vc = u(k_1 a) + v(k_2 a) = (u k_1 + v k_2) a$. Since $(u k_1 + v k_2) \in \mathbb{Z}$, $a$ indeed divides $ub + vc$.

#### 2.2 The Euclidean Division Theorem

> **📐 Fundamental Theorem — Euclidean Division in $\mathbb{Z}$**
> Let $a \in \mathbb{Z}$ and $b \in \mathbb{Z}^*$ (with $b > 0$).
> There exists a **unique** pair of integers $(q, r) \in \mathbb{Z} \times \mathbb{N}$ such that:
> $$a = b q + r \quad \text{with} \quad 0 \leq r < b$$
> - $a$ is the **dividend**.
> - $b$ is the **divisor**.
> - $q$ is the **quotient**.
> - $r$ is the **remainder**.

> **⚠️ Warning: Pitfall! — Division of a Negative Number**
> Let $a = -23$ and $b = 5$.
> A common mistake is writing $-23 = 5 \times (-4) - 3$.
> This is **strictly forbidden**! The remainder $r$ must imperatively be **non-negative** ($0 \leq r < 5$).
> The unique correct expression is:
> $$-23 = 5 \times (-5) + 2$$
> The quotient is $q = -5$ and the remainder is $r = 2$ (which strictly satisfies $0 \leq 2 < 5$).

---

### 3. Congruences and the Arithmetic of the Clock

In 1801, at the age of 24, **Carl Friedrich Gauss** published his *Disquisitiones Arithmeticae*. In it, he introduced a notation that revolutionized algebra: the concept of **congruence**.

#### 3.1 Definition and Circular Meaning

> **📐 Definition — Congruence Modulo $n$**
> Let $n$ be a positive integer ($n \geq 2$).
> Two integers $a$ and $b$ are said to be **congruent modulo $n$**, denoted by:
> $$a \equiv b \pmod n \quad \text{or} \quad a \equiv b \ [n]$$
> if and only if their difference $a - b$ is divisible by $n$:
> $$n \mid (a - b) \iff \exists k \in \mathbb{Z}, \ a - b = k n$$

*Characterization via remainders:*
Two integers $a$ and $b$ are congruent modulo $n$ if and only if **they have exactly the same remainder** in Euclidean division by $n$.

*Clock arithmetic:*
On a 12-hour clock, if it is 9 o'clock and we wait 7 hours, it will be 16 o'clock, which corresponds to 4 o'clock:
$$9 + 7 = 16 \equiv 4 \pmod{12}$$
The set of possible remainders modulo $n$ is finite: it is $\{0, 1, 2, \dots, n-1\}$.

```
              Modulo 12 (The clock face)
                           0 ≡ 12
                       11     1
                    10           2
                   9       o       3
                    8             4
                       7       5
                           6
```

#### 3.2 The Magical Compatibility with Operations

> **📐 Fundamental Theorem — Operational Properties of Congruences**
> If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then:
> 1. **Addition:** $a + c \equiv b + d \pmod n$
> 2. **Subtraction:** $a - c \equiv b - d \pmod n$
> 3. **Multiplication:** $a \times c \equiv b \times d \pmod n$
> 4. **Integer powers:** For any integer $k \in \mathbb{N}$, $a^k \equiv b^k \pmod n$

> **⚠️ Warning: Critical Pitfall! — Prohibition of Naive Division**
> In classical equality, $6x = 6y \implies x = y$.
> **In congruences, this is generally false!**
> Observe: $2 \times 1 = 2 \equiv 2 \pmod 4$ and $2 \times 3 = 6 \equiv 2 \pmod 4$.
> Thus $2 \times 1 \equiv 2 \times 3 \pmod 4$.
> Yet $1 \not\equiv 3 \pmod 4$! One cannot simply "divide by 2".
> One can divide by $c$ in $ac \equiv bc \pmod n$ only if **$c$ is coprime to $n$** ($\gcd(c, n) = 1$)!

---

### 4. GCD, Euclidean Algorithm, and Bézout's Identity

#### 4.1 The Euclidean Algorithm
The Greatest Common Divisor of two integers $a$ and $b$, not both zero, is denoted $\gcd(a, b)$ or $a \wedge b$.
Euclid (c. 300 BCE) established that if $a = bq + r$, then:
$$\gcd(a, b) = \gcd(b, r)$$
The GCD is the **last nonzero remainder** in the chain of successive Euclidean divisions.

*Example: Let us compute $\gcd(126, 48)$:*
1. $126 = 48 \times 2 + 30$
2. $48 = 30 \times 1 + 18$
3. $30 = 18 \times 1 + 12$
4. $18 = 12 \times 1 + 6$
5. $12 = 6 \times 2 + 0$
The last nonzero remainder is 6. Therefore, $\gcd(126, 48) = 6$.

#### 4.2 The Extended Euclidean Algorithm and Bézout Coefficients
By back-substituting through the steps of Euclid's algorithm in reverse order, we can always express the GCD as a **linear combination** of the two starting integers!
Let us revisit the example:
- Step 4: $6 = 18 - 12 \times 1$
- Step 3: but $12 = 30 - 18 \times 1$, hence:
  $$6 = 18 - (30 - 18 \times 1) = 2 \times 18 - 1 \times 30$$
- Step 2: but $18 = 48 - 30 \times 1$, hence:
  $$6 = 2 \times (48 - 30) - 1 \times 30 = 2 \times 48 - 3 \times 30$$
- Step 1: but $30 = 126 - 48 \times 2$, hence:
  $$6 = 2 \times 48 - 3 \times (126 - 48 \times 2) = 2 \times 48 - 3 \times 126 + 6 \times 48 = -3 \times 126 + 8 \times 48$$

We have found two integers $u = -3$ and $v = 8$ such that:
$$126 \times (-3) + 48 \times 8 = 6$$

#### 4.3 Bézout's Identity (Theorem)

> **📐 Fundamental Theorem — Bézout's Identity (1767)**
> Two nonzero integers $a$ and $b$ are **coprime** ($\gcd(a, b) = 1$) if and only if there exist two integers $u$ and $v$ such that:
>
> $$\mathbf{a u + b v = 1}$$

*Immediate converse direction:*
If $au + bv = 1$, every common divisor $d$ of $a$ and $b$ divides the linear combination $au + bv = 1$. Hence $d \mid 1$, which gives $d = \pm 1$. The GCD is therefore 1.

#### 4.4 Solving Diophantine Equations $ax + by = c$

A **Diophantine equation** (named in honor of Diophantus of Alexandria) is an equation whose solutions $(x, y)$ are sought strictly in the set of integer pairs $\mathbb{Z}^2$.

> **🧭 Method — Solving $ax + by = c$**
> 1. **Existence condition:** Let $d = \gcd(a, b)$.
>    The equation has integer solutions if and only if **$d$ divides $c$**.
> 2. **Simplification:** Divide the entire equation by $d$ to obtain $a'x + b'y = c'$ with $\gcd(a', b') = 1$.
> 3. **Particular solution:** Find a particular solution $(x_0, y_0)$ using the extended Euclidean algorithm.
> 4. **Term-by-term subtraction:**
>    $a'x + b'y = c'$ and $a'x_0 + b'y_0 = c'$.
>    Subtracting gives: $a'(x - x_0) = -b'(y - y_0) = b'(y_0 - y)$.
> 5. **Gauss's Lemma:** Since $a'$ divides $b'(y_0 - y)$ and $\gcd(a', b') = 1$, $a'$ divides $(y_0 - y)$.
>    From this, deduce the set of all solutions $(x, y)$ indexed by an integer $k \in \mathbb{Z}$.

---

### 5. Gauss's Lemma (Theorem)

> **📐 Fundamental Theorem — Gauss's Lemma**
> Let $a, b, c \in \mathbb{Z}$.
> If **$a$ divides the product $bc$** and if **$\gcd(a, b) = 1$**, then:
>
> $$\mathbf{a \text{ divides } c}$$

> **✍️ Required Proof — Gauss's Lemma**
> Assume that $a \mid bc$ and that $\gcd(a, b) = 1$.
> Since $a$ and $b$ are coprime, by Bézout's identity, there exist two integers $u, v \in \mathbb{Z}$ such that:
> $$a u + b v = 1$$
> Multiply both sides of this equality by the integer $c$:
> $$a c u + b c v = c$$
> Analyze the two terms on the left:
> - The first term $a c u$ is obviously a multiple of $a$ (it contains the factor $a$).
> - The second term contains $bc$. By hypothesis, $a \mid bc$, so there exists an integer $k$ such that $bc = ka$. The second term can thus be written $(ka)v = a(kv)$, which is also a multiple of $a$.
>
> We can therefore factor out $a$ on the left-hand side:
> $$a (cu + kv) = c$$
> Since $(cu + kv) \in \mathbb{Z}$, this equality rigorously proves that $a$ divides $c$.

*Corollary (Uniqueness of prime factorization):*
If a prime number $p$ divides a product $x_1 x_2 \dots x_m$, then $p$ must divide at least one of the factors $x_i$.

---

### 6. Fermat's Little Theorem and Fast Exponentiation

#### 6.1 Fermat's Little Theorem (1640)

> **📐 Theorem — Fermat's Little Theorem**
> Let $p$ be a prime number.
> 1. For any integer $a$ not divisible by $p$ ($\gcd(a, p) = 1$):
>    $$\mathbf{a^{p-1} \equiv 1 \pmod p}$$
> 2. For any integer $a \in \mathbb{Z}$ (without any restriction):
>    $$\mathbf{a^p \equiv a \pmod p}$$

> **✍️ Classical Proof via Remainders**
> Let $p$ be a prime and $a$ an integer not divisible by $p$.
> Consider the $p-1$ successive multiples: $a, 2a, 3a, \dots, (p-1)a$.
> Let us show that their remainders modulo $p$ are all distinct and nonzero:
> If $k_1 a \equiv k_2 a \pmod p$ with $1 \leq k_2 \leq k_1 \leq p-1$, then $p \mid (k_1 - k_2)a$.
> Since $\gcd(a, p) = 1$, by Gauss's lemma, $p \mid (k_1 - k_2)$.
> But $0 \leq k_1 - k_2 < p$, which forces $k_1 - k_2 = 0 \iff k_1 = k_2$.
> Thus, the remainders of the numbers $\{a, 2a, \dots, (p-1)a\}$ modulo $p$ are precisely the integers $\{1, 2, \dots, p-1\}$ in some permuted order!
> Multiply these $p-1$ congruences together:
> $$a \times 2a \times 3a \times \dots \times (p-1)a \equiv 1 \times 2 \times \dots \times (p-1) \pmod p$$
> Factoring out $a$ from each term:
> $$a^{p-1} \times (p-1)! \equiv (p-1)! \pmod p$$
> Since $p$ is prime, none of the factors of $(p-1)!$ is divisible by $p$, so $\gcd((p-1)!, p) = 1$.
> By Gauss's lemma (or by multiplying by the modular inverse of $(p-1)!$), we can simplify by $(p-1)!$:
> $$a^{p-1} \equiv 1 \pmod p$$

#### 6.2 The Fast Modular Exponentiation Algorithm
How do we calculate an astronomical power such as $7^{100} \pmod{13}$ without computing an 85-digit number?
We use the binary decomposition of the exponent (the *Square-and-Multiply* method):
The exponent $100$ is written in binary: $100 = 64 + 32 + 4$.
We compute the successive squares modulo 13:
- $7^1 \equiv 7 \pmod{13}$
- $7^2 = 49 = 3 \times 13 + 10 \equiv -3 \pmod{13}$
- $7^4 \equiv (-3)^2 = 9 \equiv -4 \pmod{13}$
- $7^8 \equiv (-4)^2 = 16 \equiv 3 \pmod{13}$
- $7^{16} \equiv 3^2 = 9 \equiv -4 \pmod{13}$
- $7^{32} \equiv (-4)^2 = 16 \equiv 3 \pmod{13}$
- $7^{64} \equiv 3^2 = 9 \equiv -4 \pmod{13}$

All that remains is to multiply the relevant powers:
$$7^{100} = 7^{64} \times 7^{32} \times 7^4 \equiv (-4) \times 3 \times (-4) = 48 \equiv 9 \pmod{13}.$$
The calculation required just 7 simple multiplications of numbers less than 50 instead of 99 giant multiplications!

---

### 7. Applications to Cryptography: From Caesar to RSA

#### 7.1 Affine Ciphers
We associate each letter of the alphabet with a number from 0 to 25 (A=0, B=1, ..., Z=25).
The encryption function is:
$$y \equiv a x + b \pmod{26}$$

For this cipher to be **uniquely decryptable**, distinct letters must produce distinct codes:
$$a x_1 + b \equiv a x_2 + b \pmod{26} \iff a(x_1 - x_2) \equiv 0 \pmod{26}$$
This enforces $x_1 = x_2$ only if **$a$ is coprime to 26**: $\gcd(a, 26) = 1$.
Since $26 = 2 \times 13$, $a$ must be divisible by neither 2 nor 13.
To decrypt, one looks for the **modular inverse** of $a$ modulo 26, that is, the integer $a'$ such that $a a' \equiv 1 \pmod{26}$ (provided by Bézout's algorithm).
The decryption function is then:
$$x \equiv a'(y - b) \pmod{26}$$

#### 7.2 The Principle of Asymmetric RSA Encryption

Here is the crowning jewel of modern computer security:

```
 Alice (Sender)                                       Bob (Recipient)
 ──────────────                                       ───────────────
                                                      Chooses two large prime
                                                      numbers p and q (secret).
                                                      Computes n = p × q.
                                                      Computes φ(n) = (p-1)(q-1).
                                                      Chooses e coprime to φ(n).
                                                      Computes d = e⁻¹ mod φ(n) (secret).
                                                            │
   Receives Public Key (n, e) ◄─────────────────────────────┘
   Holds message M (integer < n)
   Computes ciphertext:
   C ≡ Mᵉ (mod n)
         │
         └────────────────────────► Receives ciphertext C
                                    Applies Private Key (d):
                                    M' ≡ Cᵈ (mod n)
                                    Mathematical result: M' = M !
```

> **✍️ Mathematical Proof — Why RSA Always Decrypts Exactly**
> By construction, $d$ is the inverse of $e$ modulo $\varphi(n) = (p-1)(q-1)$.
> Hence there exists an integer $k \in \mathbb{Z}$ such that:
> $$e \cdot d = 1 + k(p-1)(q-1)$$
> Bob computes $C^d \pmod n$. Since $C \equiv M^e \pmod n$, we have:
> $$C^d \equiv (M^e)^d = M^{ed} = M^{1 + k(p-1)(q-1)} \pmod n$$
> Let us show that this quantity is congruent to $M$ modulo $p$ and modulo $q$:
> - **Modulo $p$:**
>   - If $p$ divides $M$, then $M \equiv 0 \pmod p$, hence $M^{ed} \equiv 0 \equiv M \pmod p$.
>   - If $p$ does not divide $M$, by Fermat's Little Theorem, $M^{p-1} \equiv 1 \pmod p$.
>     Then:
>     $$M^{ed} = M \times \left(M^{p-1}\right)^{k(q-1)} \equiv M \times 1^{k(q-1)} = M \pmod p$$
>   In both cases, $M^{ed} \equiv M \pmod p \iff p \mid (M^{ed} - M)$.
> - **Modulo $q$:**
>   By a strictly symmetric argument, $q \mid (M^{ed} - M)$.
>
> Since $p$ and $q$ are distinct prime numbers, they are coprime.
> By Gauss's lemma (or by product of distinct prime divisors), their product $n = pq$ divides $(M^{ed} - M)$:
> $$M^{ed} \equiv M \pmod n$$
> The original message reappears intact!

*Why is it impossible to cheat?*
To find the private key $d$, an eavesdropper must compute the inverse of $e$ modulo $(p-1)(q-1)$.
To do this, they imperatively need to know $p$ and $q$.
Yet the eavesdropper knows only the public modulus $n = p \times q$.
If $p$ and $q$ each have 300 decimal digits, the product $n$ has 600 digits. Factoring such a number into prime factors would require billions of years of computation for all the supercomputers on Earth combined!

---

### 8. Step-by-Step Solved Examples

#### Example 1: Solving a Linear Congruence
Solve in $\mathbb{Z}$ the congruence:
$$5x \equiv 3 \pmod{14}$$

**Detailed Solution:**
To solve this equation, we must find an inverse of 5 modulo 14.
Let us seek a Bézout relation between 5 and 14:
$$14 = 5 \times 2 + 4 \implies 4 = 14 - 5 \times 2$$
$$5 = 4 \times 1 + 1 \implies 1 = 5 - 4 \times 1 = 5 - (14 - 5 \times 2) = 5 \times 3 - 14 \times 1$$
We thus have $5 \times 3 - 14 \times 1 = 1$, which means:
$$5 \times 3 \equiv 1 \pmod{14}$$
The inverse of 5 modulo 14 is therefore **3**.
Multiply both sides of the original congruence by 3:
$$3 \times (5x) \equiv 3 \times 3 \pmod{14}$$
$$(3 \times 5) x \equiv 9 \pmod{14}$$
$$1 \cdot x \equiv 9 \pmod{14} \iff x \equiv 9 \pmod{14}$$
The set of solutions is the set of integers of the form:
$$x = 14k + 9 \quad (k \in \mathbb{Z})$$
*(Verification: for $x = 9$, $5 \times 9 = 45 = 14 \times 3 + 3 \equiv 3 \pmod{14}$).*

#### Example 2: Solving a Diophantine Equation
Solve in $\mathbb{Z}^2$ the equation:
$$47x + 29y = 1$$

**Detailed Solution:**
1. **Euclidean algorithm for 47 and 29:**
   - $47 = 29 \times 1 + 18$
   - $29 = 18 \times 1 + 11$
   - $18 = 11 \times 1 + 7$
   - $11 = 7 \times 1 + 4$
   - $7 = 4 \times 1 + 3$
   - $4 = 3 \times 1 + 1$
   - $3 = 1 \times 3 + 0$
   The last nonzero remainder is 1, so $\gcd(47, 29) = 1$. The equation has solutions.
2. **Back-substitution through the algorithm:**
   - $1 = 4 - 3 \times 1$
   - $1 = 4 - (7 - 4) = 2 \times 4 - 7$
   - $1 = 2 \times (11 - 7) - 7 = 2 \times 11 - 3 \times 7$
   - $1 = 2 \times 11 - 3 \times (18 - 11) = 5 \times 11 - 3 \times 18$
   - $1 = 5 \times (29 - 18) - 3 \times 18 = 5 \times 29 - 8 \times 18$
   - $1 = 5 \times 29 - 8 \times (47 - 29) = 13 \times 29 - 8 \times 47 = 47 \times (-8) + 29 \times 13$
   A particular solution is therefore $(x_0, y_0) = (-8, 13)$.
3. **General solution:**
   $$47x + 29y = 1 \quad \text{and} \quad 47(-8) + 29(13) = 1$$
   Subtracting gives:
   $$47(x - (-8)) + 29(y - 13) = 0 \iff 47(x + 8) = 29(13 - y)$$
   Since 47 divides $29(13 - y)$ and $\gcd(47, 29) = 1$, by Gauss's lemma, 47 divides $(13 - y)$.
   There exists an integer $k \in \mathbb{Z}$ such that:
   $$13 - y = 47k \iff y = 13 - 47k$$
   Substituting back into the equality:
   $$47(x + 8) = 29(47k) \iff x + 8 = 29k \iff x = -8 + 29k$$
   The solution set in $\mathbb{Z}^2$ is:
   $$S = \{(-8 + 29k \ ;\  13 - 47k) \mid k \in \mathbb{Z}\}$$

#### Example 3: Decrypting an Affine Cipher
A message was encrypted using the affine cipher $y \equiv 7x + 5 \pmod{26}$.
The ciphertext letter **V** (corresponding to position 21) is intercepted.
Recover the original letter $x$.

**Detailed Solution:**
1. The equation to solve is $7x + 5 \equiv 21 \pmod{26} \iff 7x \equiv 16 \pmod{26}$.
2. Let us find the inverse of 7 modulo 26:
   $26 = 7 \times 3 + 5$
   $7 = 5 \times 1 + 2$
   $5 = 2 \times 2 + 1 \implies 1 = 5 - 2 \times 2 = 5 - 2(7 - 5) = 3 \times 5 - 2 \times 7 = 3(26 - 7 \times 3) - 2 \times 7 = 3 \times 26 - 11 \times 7$.
   Thus $-11 \times 7 \equiv 1 \pmod{26}$.
   Now $-11 \equiv 26 - 11 = 15 \pmod{26}$.
   Check: $7 \times 15 = 105 = 4 \times 26 + 1 \equiv 1 \pmod{26}$.
   The inverse of 7 modulo 26 is therefore **15**.
3. Multiply the equation $7x \equiv 16 \pmod{26}$ by 15:
   $$x \equiv 15 \times 16 \pmod{26}$$
   $15 \times 16 = 240$.
   Perform Euclidean division of 240 by 26:
   $240 = 26 \times 9 + 6$.
   Thus $x \equiv 6 \pmod{26}$.
4. Position 6 corresponds to the letter:
   $0 \to A, 1 \to B, 2 \to C, 3 \to D, 4 \to E, 5 \to F, 6 \to \mathbf{G}$.
   The original letter was **G**.

#### Example 4: Remainder Calculation with Fermat's Little Theorem
Determine the remainder of the Euclidean division of $3^{2026}$ by 17.

**Detailed Solution:**
1. The divisor is $p = 17$, which is prime.
2. The integer $a = 3$ is not divisible by 17 ($\gcd(3, 17) = 1$).
3. By Fermat's Little Theorem:
   $$3^{17-1} = 3^{16} \equiv 1 \pmod{17}$$
4. Perform Euclidean division of the exponent 2026 by 16:
   $$2026 = 16 \times 126 + 10$$
5. Decompose the power:
   $$3^{2026} = 3^{16 \times 126 + 10} = (3^{16})^{126} \times 3^{10} \equiv 1^{126} \times 3^{10} \equiv 3^{10} \pmod{17}$$
6. Compute $3^{10} \pmod{17}$ by successive squares:
   - $3^2 = 9$
   - $3^4 = 9^2 = 81 = 17 \times 4 + 13 \equiv -4 \pmod{17}$
   - $3^8 \equiv (-4)^2 = 16 \equiv -1 \pmod{17}$
   - $3^{10} = 3^8 \times 3^2 \equiv (-1) \times 9 = -9 \equiv 17 - 9 = 8 \pmod{17}$.
The remainder of the division of $3^{2026}$ by 17 is therefore **8**.

#### Example 5: A Complete Miniature RSA Example
Bob prepares his RSA keys:
1. He chooses $p = 5$ and $q = 11$.
2. Calculate the modulus $n$ and the totient value $\varphi(n)$.
3. Bob chooses the public exponent $e = 3$. Verify that this choice is valid.
4. Calculate the secret private key $d$.
5. Alice wants to send the secret message $M = 9$. Encrypt this message to obtain $C$.
6. Show how Bob decrypts $C$ to recover $M$.

**Detailed Solution:**
1. $n = p \times q = 5 \times 11 = 55$.
2. $\varphi(n) = (p-1)(q-1) = 4 \times 10 = 40$.
3. $e = 3$. Since $40 = 3 \times 13 + 1$, $\gcd(3, 40) = 1$. The choice $e = 3$ is completely valid.
4. We seek $d$ such that $3d \equiv 1 \pmod{40}$.
   Notice that $3 \times 13 = 39 = 40 - 1 \equiv -1 \pmod{40}$, so $3 \times (-13) \equiv 1 \pmod{40}$.
   Since $-13 \equiv 40 - 13 = 27 \pmod{40}$, we have $d = 27$.
   *(Check: $3 \times 27 = 81 = 2 \times 40 + 1 \equiv 1$).*
   Bob's private key is **$d = 27$**.
5. **Encryption by Alice:**
   $C \equiv M^e \pmod n \iff C \equiv 9^3 \pmod{55}$.
   $9^3 = 729$.
   Division of 729 by 55: $729 = 55 \times 13 + 14$.
   The ciphertext sent across the network is **$C = 14$**.
6. **Decryption by Bob:**
   Bob computes $M \equiv C^d = 14^{27} \pmod{55}$.
   Decompose the exponent 27 in binary: $27 = 16 + 8 + 2 + 1$.
   Compute powers of 14 modulo 55:
   - $14^1 \equiv 14$
   - $14^2 = 196 = 55 \times 3 + 31 \equiv 31 \equiv -24 \pmod{55}$
   - $14^4 \equiv (-24)^2 = 576 = 55 \times 10 + 26 \equiv 26 \pmod{55}$
   - $14^8 \equiv 26^2 = 676 = 55 \times 12 + 16 \equiv 16 \pmod{55}$
   - $14^{16} \equiv 16^2 = 256 = 55 \times 4 + 36 \equiv 36 \equiv -19 \pmod{55}$
   Multiply:
   $14^{27} = 14^{16} \times 14^8 \times 14^2 \times 14 \equiv (-19) \times 16 \times 31 \times 14 \pmod{55}$.
   - $(-19) \times 16 = -304 = 55 \times (-6) + 26 \equiv 26$
   - $31 \times 14 = 434 = 55 \times 7 + 49 \equiv -6$
   - $26 \times (-6) = -156 = 55 \times (-3) + 9 \equiv 9 \pmod{55}$.
   Bob recovers exactly **$M = 9$**!

#### Example 6: Divisibility Criteria via Congruences
Prove using congruences that an integer is divisible by 9 if and only if the sum of its digits is divisible by 9.

**Detailed Solution:**
Let $N$ be a natural number whose decimal expansion is $a_k a_{k-1} \dots a_1 a_0$:
$$N = \sum_{j=0}^k a_j 10^j = a_0 + a_1 10 + a_2 10^2 + \dots + a_k 10^k$$
Notice that:
$$10 = 9 + 1 \equiv 1 \pmod 9$$
By the compatibility of congruences with powers:
For any integer $j \geq 0$, $10^j \equiv 1^j \equiv 1 \pmod 9$.
Multiplying by each digit $a_j$ and summing:
$$N = \sum_{j=0}^k a_j 10^j \equiv \sum_{j=0}^k a_j (1) \equiv \sum_{j=0}^k a_j \pmod 9$$
The number $N$ and the sum of its digits have exactly the same remainder modulo 9.
Consequently, $9 \mid N$ if and only if 9 divides the sum of its decimal digits.

---

### Key Takeaways

1. **Divisibility and Division:**
   - $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$.
   - Linear combinations: if $a \mid b$ and $a \mid c$, then $a \mid (ub + vc)$.
   - Euclidean division: $a = bq + r$ with $0 \leq r < b$.

2. **Congruences:**
   - $a \equiv b \pmod n \iff n \mid (a - b)$ (same remainder modulo $n$).
   - Compatible with addition, subtraction, multiplication, and powers.
   - One may simplify $ac \equiv bc \pmod n$ by $c$ only if $\gcd(c, n) = 1$.

3. **Bézout and Gauss:**
   - $\gcd(a, b) = 1 \iff \exists u, v \in \mathbb{Z}, au + bv = 1$ (Bézout).
   - If $a \mid bc$ and $\gcd(a, b) = 1$, then $a \mid c$ (Gauss).

4. **Fermat and RSA:**
   - Fermat's Little Theorem: if $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.
   - RSA: public key $(n, e)$ with $n = pq$, private key $d \equiv e^{-1} \pmod{(p-1)(q-1)}$.
   - $C \equiv M^e \pmod n \implies M \equiv C^d \pmod n$.

---

### Exercises

#### Level ★ (Direct Applications)

**Exercise 1.** Perform Euclidean division in $\mathbb{Z}$:
1. Of $157$ by $11$.
2. Of $-75$ by $8$.
3. Of $-140$ by $12$.

**Exercise 2.** True or False? Justify.
1. If $a \equiv 3 \pmod 5$, then $a^2 \equiv 4 \pmod 5$.
2. If $a \equiv 2 \pmod 6$, then $a$ is an even number.
3. If $3x \equiv 3y \pmod 7$, then $x \equiv y \pmod 7$.

**Exercise 3.** Compute $\gcd(323, 187)$ using the Euclidean algorithm. Are these numbers coprime?

**Exercise 4.** Find a pair of integers $(u, v)$ satisfying Bézout's identity:
$$17 u + 11 v = 1$$

**Exercise 5.** Compute the remainder of the Euclidean division of $2^{100}$ by 7.

**Exercise 6.** A 12-hour clock indicates 8 o'clock. What time will it indicate in 1,500 hours?

**Exercise 7.** Solve in $\mathbb{Z}$ the equation $3x \equiv 1 \pmod{10}$.

#### Level ★★ (Analytical Thinking & Exam Problems)

**Exercise 8.** Solve in $\mathbb{Z}^2$ the Diophantine equation:
$$13x - 7y = 1$$
Deduce all solutions satisfying $0 \leq x \leq 50$.

**Exercise 9.** Affine cipher.
We use the cipher $y \equiv 5x + 7 \pmod{26}$.
1. Verify that this encryption is reversible.
2. Encrypt the word **BAC**.
3. Find the decryption function and decode the letter **R** (position 17).

**Exercise 10.** Determine the units digit of $7^{2025}$ in its standard decimal representation.
*(Hint: find the remainder modulo 10).*

**Exercise 11.** Prove that for all $n \in \mathbb{N}$, the integer $A_n = 3^{2n+1} + 2^{n+2}$ is divisible by 7.

**Exercise 12.** Let $n \in \mathbb{N}$. Prove that the fraction $\frac{2n+1}{3n+1}$ is irreducible for every integer $n$.

**Exercise 13.** The Coconut Thieves.
Three castaways gather a pile of coconuts. During the night, the first wakes up, divides the pile into 3 equal shares, finds that 1 coconut remains, gives it to a monkey, and hides his share. The second and third castaways do successively the same.
Translate this problem into a system of congruences and find the minimal initial number of coconuts.

**Exercise 14.** Chinese Remainder Theorem (Special Case).
Solve in $\mathbb{Z}$ the system of congruences:
$$\begin{cases} x \equiv 2 \pmod 5 \\ x \equiv 3 \pmod 7 \end{cases}$$

**Exercise 15.** Mersenne Numbers and Fermat.
Let $p$ be an odd prime. Consider the Mersenne number $M_p = 2^p - 1$.
Let $q$ be a prime divisor of $M_p$. Prove that $q \equiv 1 \pmod{2p}$.

#### Level ★★★ (Advanced Explorations & Competition Problems)

**Exercise 16.** Proof of Wilson's Theorem.
Prove that an integer $p \geq 2$ is prime if and only if:
$$(p-1)! \equiv -1 \pmod p$$
*(Hint: pair each element of $\{2, \dots, p-2\}$ with its distinct modular inverse).*

**Exercise 17.** Euler's Totient Function $\varphi(n)$.
1. For $p$ prime, justify that $\varphi(p) = p - 1$ and $\varphi(p^k) = p^k - p^{k-1}$.
2. Prove Euler's theorem generalizing Fermat: if $\gcd(a, n) = 1$, then $a^{\varphi(n)} \equiv 1 \pmod n$.

**Exercise 18.** The Miller-Rabin Primality Test.
Explain the principle of the Miller-Rabin probabilistic test based on Fermat's theorem and the square roots of 1 modulo $p$. Why does it allow testing 500-digit numbers in a fraction of a second?

**Exercise 19.** Wiener's Attack on the RSA Cryptosystem.
Show that if the secret exponent $d$ is chosen too small ($d < \frac{1}{3} n^{1/4}$), the private key can be recovered quickly from the public key $(n, e)$ using the continued fraction expansion of $\frac{e}{n}$.

**Exercise 20.** Order of an Element in $\mathbb{Z}/p\mathbb{Z}$.
Let $p$ be a prime number and $a$ an integer not divisible by $p$.
The order of $a$ modulo $p$ is defined as the smallest positive integer $k$ such that $a^k \equiv 1 \pmod p$.
Prove that $k$ necessarily divides $p - 1$.

**Exercise 21.** Quadratic Residues and the Legendre Symbol.
Let $p$ be an odd prime. An integer $a$ not a multiple of $p$ is a quadratic residue (square) modulo $p$ if there exists $x$ such that $x^2 \equiv a \pmod p$.
Prove Euler's criterion:
$$a^{\frac{p-1}{2}} \equiv \begin{cases} +1 \pmod p & \text{if } a \text{ is a square} \\ -1 \pmod p & \text{if } a \text{ is not a square} \end{cases}$$

**Exercise 22.** The Discrete Logarithm Problem and Diffie-Hellman Key Exchange.
Explain the Diffie-Hellman key exchange protocol based on the modular power function $g^a \pmod p$. Why is it easy to compute $g^a \pmod p$ but computationally infeasible to recover $a$ knowing $g^a$?

---

### Solutions

**Solution 1.**
1. $157 = 11 \times 14 + 3$ ($q = 14, r = 3$).
2. $-75 = 8 \times (-10) + 5$ ($q = -10, r = 5$).
3. $-140 = 12 \times (-12) + 4$ ($q = -12, r = 4$).

**Solution 2.**
1. **True.** $a \equiv 3 \pmod 5 \implies a^2 \equiv 3^2 = 9 \equiv 4 \pmod 5$.
2. **True.** $a = 6k + 2 = 2(3k + 1)$, which is divisible by 2.
3. **True.** Since $\gcd(3, 7) = 1$, we can divide by 3 by Gauss's lemma.

**Solution 3.**
$323 = 187 \times 1 + 136$.
$187 = 136 \times 1 + 51$.
$136 = 51 \times 2 + 34$.
$51 = 34 \times 1 + 17$.
$34 = 17 \times 2 + 0$.
$\gcd(323, 187) = 17 \neq 1$. They are not coprime.

**Solution 4.**
$17 = 11 \times 1 + 6 \implies 6 = 17 - 11$.
$11 = 6 \times 1 + 5 \implies 5 = 11 - 6 = 11 - (17 - 11) = 2 \times 11 - 17$.
$6 = 5 \times 1 + 1 \implies 1 = 6 - 5 = (17 - 11) - (2 \times 11 - 17) = 2 \times 17 - 3 \times 11$.
A solution pair is $(u, v) = (2, -3)$.

**Solution 5.**
Modulo 7, $2^3 = 8 \equiv 1 \pmod 7$.
Division of 100 by 3: $100 = 3 \times 33 + 1$.
$2^{100} = (2^3)^{33} \times 2^1 \equiv 1^{33} \times 2 = 2 \pmod 7$. The remainder is 2.

**Solution 6.**
We seek $8 + 1500 \pmod{12}$.
$1500 = 12 \times 125 + 0 \equiv 0 \pmod{12}$.
The clock will therefore indicate **8 o'clock** sharp again.

**Solution 7.**
We seek the inverse of 3 modulo 10. Since $3 \times 7 = 21 \equiv 1 \pmod{10}$, the inverse is 7.
$3x \equiv 1 \implies 7 \times 3x \equiv 7 \times 1 \implies x \equiv 7 \pmod{10}$.
$S = \{10k + 7 \mid k \in \mathbb{Z}\}$.

**Solution 8.**
$13(1) - 7(2) = 13 - 14 = -1 \implies 13(-1) - 7(-2) = 1$. Particular solution: $(-1, -2)$.
$13(x + 1) = 7(y + 2)$. Since $\gcd(13, 7) = 1$, by Gauss: $x + 1 = 7k \implies x = 7k - 1$ and $y = 13k - 2$.
For $0 \leq x \leq 50$: $0 \leq 7k - 1 \leq 50 \implies 1 \leq 7k \leq 51 \implies k \in \{1, 2, 3, 4, 5, 6, 7\}$.
There are 7 solution pairs.

**Solution 9.**
1. $\gcd(5, 26) = 1$ because $26 = 2 \times 13$, hence the encryption is bijective.
2. B(1): $5(1) + 7 = 12 \to$ M.
   A(0): $5(0) + 7 = 7 \to$ H.
   C(2): $5(2) + 7 = 17 \to$ R. BAC becomes **MHR**.
3. Inverse of 5 modulo 26: $5 \times 21 = 105 = 4 \times 26 + 1$, hence $5^{-1} \equiv 21$.
   $x \equiv 21(y - 7) \pmod{26}$.
   For R ($y = 17$): $x \equiv 21(17 - 7) = 210 = 26 \times 8 + 2 \equiv 2 \pmod{26}$. Position 2 corresponds to **C**.

**Solution 10.**
We seek $7^{2025} \pmod{10}$.
$7^1 \equiv 7$, $7^2 = 49 \equiv 9 \equiv -1$, $7^4 \equiv 1 \pmod{10}$.
$2025 = 4 \times 506 + 1$.
$7^{2025} = (7^4)^{506} \times 7^1 \equiv 1 \times 7 = 7 \pmod{10}$.
The units digit is **7**.

**Solution 11.**
$3^{2n+1} = 3 \times (3^2)^n = 3 \times 9^n \equiv 3 \times 2^n \pmod 7$ (since $9 \equiv 2$).
$2^{n+2} = 2^2 \times 2^n = 4 \times 2^n \pmod 7$.
Sum: $A_n \equiv 3 \times 2^n + 4 \times 2^n = 7 \times 2^n \equiv 0 \pmod 7$. Hence $7 \mid A_n$.

**Solution 12.**
Let $d$ be a common divisor of the numerator and denominator.
$d \mid (2n + 1)$ and $d \mid (3n + 1)$.
Then $d$ divides the linear combination $3(2n + 1) - 2(3n + 1) = 6n + 3 - 6n - 2 = 1$.
Since $d \mid 1$, we must have $d = 1$. The two integers are always coprime; the fraction is irreducible.

**Solution 13.**
Let $N$ be the number of coconuts.
Each step removes 1 coconut and takes one-third, leaving $\frac{2}{3}(N-1)$.
After 3 steps, the successive divisions lead to the congruence $8N \equiv 17 \pmod{27} \implies N \equiv 25 \pmod{27}$.
The smallest positive nonzero number possible is $N = 25$ (or 79 if the final morning sharing is non-empty).

**Solution 14.**
$x = 5k + 2$. Substituting into the second congruence: $5k + 2 \equiv 3 \pmod 7 \iff 5k \equiv 1 \pmod 7$.
The inverse of 5 modulo 7 is 3 ($5 \times 3 = 15 \equiv 1$).
Thus $k \equiv 3 \pmod 7 \implies k = 7m + 3$.
Hence $x = 5(7m + 3) + 2 = 35m + 17$. The solutions are $x \equiv 17 \pmod{35}$.

**Solution 15.**
If $q \mid (2^p - 1)$, then $2^p \equiv 1 \pmod q$. The order of 2 modulo $q$ divides the prime $p$, so the order is $p$.
By Fermat, $2^{q-1} \equiv 1 \pmod q$, so the order $p$ divides $q - 1$, meaning $q - 1 = kp \implies q \equiv 1 \pmod p$.
Since $q$ is odd ($M_p$ being odd), $q - 1$ is even, so $k$ is even ($k = 2m$).
Hence $q = 2mp + 1 \equiv 1 \pmod{2p}$.

**Solution 16.**
If $p$ is prime, every element $x \in \{2, \dots, p-2\}$ possesses a unique modular inverse distinct from itself (since $x^2 \equiv 1 \implies x = \pm 1$). All these terms cancel in pairs in the product $(p-1)!$, leaving only $1 \times (p-1) \equiv -1 \pmod p$. The converse follows from the fact that if $p$ is composite, a proper divisor $d < p$ would divide $(p-1)!$ and could not divide $(p-1)! + 1$.

**Solution 17.**
1. For $p^k$, the integers not coprime to $p^k$ are multiples of $p$, of which there are $p^{k-1}$. Hence $\varphi(p^k) = p^k - p^{k-1}$.
2. Considering the integers coprime to $n$ and multiplying by $a$, the product of elements is preserved by bijectivity of multiplication in the group of units $(\mathbb{Z}/n\mathbb{Z})^\times$, yielding $a^{\varphi(n)} \equiv 1 \pmod n$.

**Solution 18.**
If $n$ is prime, for $n-1 = 2^s d$, the sequence of repeated squarings starting from $a^d$ must terminate in 1, and the last value different from 1 must be $-1$. If any other value appears, $n$ is definitely composite. This fast polynomial-time test is the keystone of large prime generation for cryptography.

**Solution 19.**
If $ed - k\varphi(n) = 1$, then $\left|\frac{e}{n} - \frac{k}{d}\right| \leq \frac{1}{2d^2}$. By Legendre's theorem on continued fractions, $\frac{k}{d}$ must be one of the convergents of the continued fraction expansion of $\frac{e}{n}$, enabling an attacker to compute $d$ almost instantaneously.

**Solution 20.**
Let $k$ be the order of $a$. Perform Euclidean division of $p-1$ by $k$: $p-1 = kq + r$ with $0 \leq r < k$.
Then $a^{p-1} = (a^k)^q \times a^r \equiv 1^q \times a^r \equiv a^r \pmod p$.
By Fermat, $a^{p-1} \equiv 1 \pmod p$, hence $a^r \equiv 1 \pmod p$.
Since $k$ is the smallest positive integer with this property and $r < k$, we must have $r = 0$. Hence $k$ divides $p - 1$.

**Solution 21.**
By Fermat, $(a^{\frac{p-1}{2}})^2 = a^{p-1} \equiv 1 \pmod p$. Thus $a^{\frac{p-1}{2}}$ solves $X^2 \equiv 1 \pmod p$, so $a^{\frac{p-1}{2}} \equiv \pm 1 \pmod p$. If $a = x^2$, then $a^{\frac{p-1}{2}} = x^{p-1} \equiv 1$. The polynomial $X^{\frac{p-1}{2}} - 1$ of degree $\frac{p-1}{2}$ has at most $\frac{p-1}{2}$ roots, so the quadratic residues are its only roots.

**Solution 22.**
Alice chooses secret $a$, sends $A = g^a \pmod p$. Bob chooses secret $b$, sends $B = g^b \pmod p$. The shared key is $K = B^a = A^b = g^{ab} \pmod p$. An eavesdropper intercepting $g^a$ and $g^b$ cannot compute $g^{ab}$ without solving the discrete logarithm problem, believed to be intractable for large prime moduli.

---

### The Question That Opens the Future

We have just seen how arithmetic equations allow us to encrypt information flows and link integer variables.
But what happens when the flows to be transformed are no longer isolated numbers, but entire tables of data, interconnected networks, and probabilistic states in perpetual transition?
How do we model the evolution of a population, the ranking of web pages by Google, or the states of a Turing machine?
To orchestrate these multidimensional flows, mathematicians forged a spectacular tool: matrices and graphs. Turn the page to discover **Chapter 57 and The Jacquard Loom Revisited: Matrices and Graphs**.
