
# 🎲 Probability Interview Questions & Answers

This document contains answers and explanations to conceptual, coding, and applied probability questions commonly asked during data science interviews.

---

## 🧠 Conceptual Questions

### ❓ On any given day, there is a 10% chance you will see a friend on the subway. Assuming you ride the subway 5 days a week, what is the probability that you will see a friend at least once?

**Answer**:  
This is a classic example of a **complementary probability** problem.

- Probability of **not** seeing a friend on one day = 0.90  
- Probability of not seeing a friend all 5 days = \( 0.9^5 pprox 0.59049 \)  
- Therefore, the probability of seeing a friend **at least once** in 5 days is:  
  \[
  1 - 0.9^5 pprox 1 - 0.59049 = 0.40951
  \]

**Final Answer**: ~**40.95%**

---

### ❓ A couple has 2 children. At least 1 is a girl. What is the likelihood that both are girls?

**Answer**:  
List the possible combinations of two children:

- BB  
- BG  
- GB  
- GG  

Given that **at least one is a girl**, we eliminate the **BB** case. That leaves:

- BG  
- GB  
- GG  

Out of these 3 possibilities, only **GG** has both girls.

**Final Answer**: \( rac{1}{3} \)

---

### ❓ A fair six-sided die is rolled twice. What is the probability of getting 1 on the first roll and not getting 6 on the second roll?

**Answer**:

- Probability of getting 1 on the first roll = \( rac{1}{6} \)
- Probability of not getting 6 on the second roll = \( rac{5}{6} \)
- These are **independent events**, so multiply the probabilities:

\[
rac{1}{6} 	imes rac{5}{6} = rac{5}{36}
\]

**Final Answer**: \( rac{5}{36} \)

---

## 🧪 Coding Challenges

### ❓ How would you simulate the behavior of a fair coin?

```python
import random

def flip_fair_coin():
    return 'Heads' if random.random() < 0.5 else 'Tails'
```

---

### ❓ How would you simulate the behavior of an unfair coin?

```python
import random

def flip_unfair_coin(prob_heads=0.7):
    return 'Heads' if random.random() < prob_heads else 'Tails'
```

You can adjust `prob_heads` to simulate coins with any given bias.

---

## 🌐 Applied Questions

### 🧵 Facebook Ad Question

**Scenario**:  
We have two ad-serving strategies:
- **Option 1**: 1 ad per 25 stories  
- **Option 2**: 4% chance per story  

**Expected number of ads in 100 stories**:
- Option 1: \( 100 / 25 = 4 \)
- Option 2: \( 100 	imes 0.04 = 4 \)

**Probability of exactly 1 ad using Option 2 (Binomial)**:
- \( P(X = 1) = inom{100}{1} 	imes (0.04)^1 	imes (0.96)^{99} pprox 100 	imes 0.04 	imes (0.96)^{99} \)

**Probability of no ads using Option 2**:
- \( P(X = 0) = (0.96)^{100} pprox 0.016 \)

**Summary**:
- Expected number of ads is the same for both.
- Option 2 introduces **variability** (user may see no ads or several), whereas Option 1 ensures **consistency**.

---

### 🚗 Uber vs. Lyft Arrival Order

**Scenario**:  
You call 2 UberX’s and 3 Lyfts. Arrival times are i.i.d.

**Total ways to arrange 5 arrivals** = \( 5! = 120 \)

**Probability all Lyfts arrive first** = Probability Lyfts take first 3 spots:  
\[
= rac{3! \cdot 2!}{5!} = rac{6 \cdot 2}{120} = rac{1}{10}
\]

**Probability all Ubers arrive first**:  
Same logic — Ubers need first 2 spots:  
\[
= rac{2! \cdot 3!}{5!} = rac{2 \cdot 6}{120} = rac{1}{10}
\]

**Final Answer**:  
- Lyfts first: **10%**  
- Ubers first: **10%**

---

### 🌧️ It’s Raining in London

**Scenario**:  
Three friends say it’s raining. Each has a 1/3 chance of lying.

**Probability all are lying** = \( \left(rac{1}{3}
ight)^3 = rac{1}{27} \)

**Probability that at least one is telling the truth** =  
\[
1 - rac{1}{27} = rac{26}{27}
\]

So the chance that it's **actually raining** is **26/27** (~**96.3%**).

---

## ✅ Summary


- **Complementary and conditional probabilities**
- **Independence** and **combinatorics**
- **Simulations with code**
- **Applied real-world reasoning**

These skills are essential in interpreting uncertainty, designing experiments, and evaluating outcomes in data-driven environments. You're now well-prepared to tackle probability problems in a professional setting!
