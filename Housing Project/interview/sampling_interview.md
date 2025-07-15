# 📊 Sampling Interview Questions & Answers

This document outlines answers to common conceptual and applied sampling questions, which may be encountered during data science or analytics interviews.

---

## 🧠 Conceptual Questions

### ❓ How do you decide which sampling technique to use and what do you take into account when deciding?

The choice of sampling technique depends on several key factors, including:

- **Population structure**: If the population is homogeneous, simple random sampling may suffice. If it's heterogeneous with identifiable subgroups, stratified or cluster sampling is more appropriate.
- **Research goals**: If specific subgroup insights are needed, stratified sampling helps ensure those groups are adequately represented.
- **Resources**: Time and budget constraints may make certain methods more feasible.
- **Sampling frame availability**: If a complete list of the population is available, simple or systematic random sampling can be used. Otherwise, alternative methods may be necessary.
- **Risk of bias**: Some methods (e.g., convenience sampling) introduce higher bias risk, so trade-offs must be evaluated.

---

### ❓ How do you typically create a representative sample?

To create a representative sample:

- **Understand the population demographics** (age, location, behavior, etc.).
- **Use stratified sampling** when important subgroups must be represented proportionally.
- **Randomize the selection process** to avoid selection bias.
- **Ensure sufficient sample size** so that the sample reflects the diversity in the population.
- **Avoid convenience sampling**, which may over-represent easily accessible individuals.

---

### ❓ What is selection bias and how do you account for it in your data?

**Selection bias** occurs when the sample collected is not representative of the population, usually due to non-random selection. This skews results and affects generalizability.

To account for it:

- Use **random sampling techniques**.
- Implement **stratified or quota sampling** to ensure underrepresented groups are included.
- **Compare sample characteristics** to known population benchmarks and apply **weighting adjustments** if needed.
- **Review sampling procedures** to identify and correct sources of bias.

---

### ❓ How do you determine sample size?

Sample size is determined by:

- **Desired confidence level** (commonly 95%)
- **Margin of error** (e.g., ±5%)
- **Population size**
- **Expected variability** in the data (standard deviation or proportion)
- Use of formulas or tools like:
  \[
  n = \frac{{Z^2 \cdot p(1 - p)}}{{E^2}}
  \]
  Where:
  - `Z` is the z-score for the confidence level
  - `p` is the estimated proportion
  - `E` is the margin of error

Power analysis can also be used when designing experiments.

---

## 🔧 Applied Questions

### 🏢 Publishing House Scenario

**Question**:  
We have 1 million users: 80% Freemium, 20% Paid. We want to understand customer interests to maximize revenue. Should we use random or stratified sampling? Focus on all customers or just the 20%?

**Answer**:  
I would recommend **stratified sampling** to ensure we capture insights from both Freemium and Paid users. Since their behaviors and motivations likely differ, it’s important to preserve these proportions or even **oversample the 20% Paid group** if they're the revenue focus.

Focusing only on the 20% paid users would give insights into current revenue drivers, but might miss opportunities in converting Freemium users. Therefore, a **balanced approach with stratification** helps maximize both insights and revenue potential.

---

### 🛒 Grocery Store Scenario

**Question**:  
200 customers enter daily. We want to track their movement through the store. How do you determine which customers to track?

**Answer**:  
Use **systematic sampling** — e.g., select every 5th customer who enters the store. This introduces randomness while being feasible for manual or sensor-based tracking.

Ensure the sampling period covers different times of day and days of the week to avoid time-based bias. Alternatively, use **stratified sampling by time blocks** (e.g., morning vs evening shoppers).

---

### 🏥 Healthcare Company Scenario

**Question**:  
We want to estimate how many people in a community have a respiratory illness. People come voluntarily to get tested for free. How do you handle the bias?

**Answer**:  
This setup introduces **self-selection bias** — those with symptoms are more likely to show up.

To address this:

- Set up **mobile testing units** in diverse neighborhoods.
- Provide **random invitations** or incentives to encourage asymptomatic participation.
- Apply **post-stratification weighting** based on demographic data.
- Combine this with **survey data** or electronic medical records to adjust estimates and improve representativeness.

---

## ✅ Summary


- How to choose and justify sampling methods.
- Creating representative samples using random and stratified techniques.
- Understanding and mitigating selection bias.
- Determining sample size based on statistical principles.

We also applied sampling to real-world scenarios across publishing, retail, and healthcare domains.

You're now equipped to showcase thoughtful, practical, and statistically sound sampling approaches in interviews and real projects!
