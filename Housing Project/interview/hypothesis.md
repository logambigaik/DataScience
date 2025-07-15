
# Hypothesis Testing Interview Questions

## Introduction
As you know, my team is in need of someone who can help us answer our data questions. We have a lot of data, I’d say maybe too much for one person to handle. I’m looking for a candidate who can work with samples and draw conclusions with a certain level of confidence.

As with any candidate, I am also looking for a problem solver who can clearly communicate their thinking and knowledge, someone who is curious about our data and has ideas on how to solve our specific business problems.

---

## Conceptual Questions

### What is the difference between type I and type II errors? Which one is worse? Why? Can you give me an example of each?

**Answer:**  
A **Type I error** occurs when the null hypothesis is true, but we reject it (false positive).  
A **Type II error** occurs when the null hypothesis is false, but we fail to reject it (false negative).  

Which is worse depends on context:  
- In medical testing, Type I error could mean a false alarm for a disease, while Type II could mean missing a real diagnosis. The latter may be worse due to health risks.  
- In judicial systems, a Type I error could convict an innocent person; this is often considered more severe.  

**Example Type I**: Declaring a new drug effective when it isn’t.  
**Example Type II**: Failing to detect a real effect of a new treatment.

---

### What is a p-value and what does it tell you?

**Answer:**  
A **p-value** is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is true.  

A small p-value (typically < 0.05) indicates strong evidence against the null hypothesis, so we reject it. A high p-value means the observed result is likely under the null hypothesis, so we fail to reject it.

---

### What is the Central Limit Theorem and why does it matter?

**Answer:**  
The **Central Limit Theorem (CLT)** states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the population's distribution.

It matters because it justifies the use of normal probability models in hypothesis testing and confidence intervals even when the population distribution is not normal.

---

## Applied Questions

### Finance company:
We assume that the average rate of return of a mutual fund is 9%. Talk through the steps of how you would validate if this is true. State any assumptions you would need to make and the data that you would need to validate your results.

**Answer:**  
1. Define hypotheses:  
   - Null (H₀): μ = 9%  
   - Alternative (H₁): μ ≠ 9%  

2. Collect a representative sample of mutual fund returns.  
3. Calculate the sample mean and standard deviation.  
4. Use a t-test to compare the sample mean to 9%.  
5. Check the p-value:  
   - If p < 0.05, reject H₀.  
   - If p ≥ 0.05, fail to reject H₀.  

**Assumptions:**  
- Returns are independent and identically distributed.  
- Data is approximately normally distributed or sample size is large.

---

### Mortgage Lender:
We think that first-time homebuyers take out smaller loans than other borrowers. What information do you need to assess this and what would you do?

**Answer:**  
1. Data needed:  
   - Loan amounts  
   - Buyer status (first-time vs. others)  

2. Define hypotheses:  
   - H₀: μ₁ = μ₂  
   - H₁: μ₁ < μ₂ (μ₁ = mean loan for first-time buyers; μ₂ = others)  

3. Perform an independent two-sample t-test.  
4. If p < 0.05, conclude first-time buyers take smaller loans.

---

### A marketing company:
We think that at least 60% of American households have an iPad. Our research team surveyed 200 households and found that 123 of them had iPads. Can we be sure that 60% is accurate? Why or why not?

**Answer:**  
1. Sample proportion: 123 / 200 = 0.615  
2. Define hypotheses:  
   - H₀: p = 0.60  
   - H₁: p ≠ 0.60  

3. Perform a one-proportion z-test:  
   - z = (0.615 - 0.60) / √[(0.6)(0.4)/200]  
   - Calculate z and find the p-value.

4. If p < 0.05, reject the null hypothesis.  
   - This would suggest the true proportion might differ from 60%.  
   - Otherwise, we don’t have enough evidence to reject the claim.

---

## Review



- Step-by-step process for conducting hypothesis tests.  
- The importance of representative samples when performing hypothesis tests.  
- Code that can be used to calculate the confidence interval of a sample.  
- The theory behind the central limit theorem and a clear example.  
- How vital the p-value is to any hypothesis test.

You are ready to talk about hypothesis testing in a real interview setting!
