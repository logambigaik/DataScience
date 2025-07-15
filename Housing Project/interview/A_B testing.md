# A/B Testing - Interview Responses

---

## ✅ What is the goal of A/B Testing, and why is it important?

The goal of A/B Testing is to compare two or more variations (e.g., control vs. treatment) to determine which performs better on a defined success metric (e.g., click-through rate, conversion, engagement). 

It’s important because:
- It provides **data-driven evidence** for decision-making.
- Helps avoid reliance on intuition or assumptions.
- Quantifies impact of changes before full rollout.
- Reduces risk of deploying ineffective or harmful features.

---

## ✅ What considerations do you need to make when determining the number of participants needed for an A/B Test?

Key considerations:
- **Minimum detectable effect (MDE):** Small changes require larger samples.
- **Statistical power (commonly 80%)**: Likelihood of detecting a true effect.
- **Significance level (alpha, usually 0.05):** Controls false positives.
- **Baseline conversion rate:** Affects variance and sample size.
- **Test duration and traffic volume:** Ensures feasibility within business constraints.

Tools like power calculators or platforms like Optimizely or Statsmodels in Python can help compute sample sizes.

---

## ✅ If you had to stop an A/B Test early, what considerations would you make?

Stopping early requires caution:

- **Statistical validity**: Has the test reached the required sample size and power?
- **Interim p-values** can be misleading due to peeking.
- Use **sequential testing** or **Bayesian methods** if early stopping is planned.
- **Business urgency**: Consider cost/risk of continuing vs. stopping.
- **Direction of effect**: Is the result strong and consistent enough to justify action?

If stopped early, always **document reasoning and limitations** clearly.

---

## ✅ Applied Question: Social networking app — Saved Comments Feature

To determine whether to implement the "Saved Comments" feature:

1. **Define success metrics**:
   - Engagement with saved comments (views, re-visits).
   - Session duration, retention, satisfaction (survey/NPS).
   - Messaging frequency before and after.

2. **Design an A/B Test**:
   - Randomly assign users to control (no feature) and treatment (with feature).
   - Run for enough time to gather statistical power.

3. **Qualitative feedback**:
   - Conduct surveys or usability tests.

4. **Cost vs benefit**:
   - Measure dev cost and complexity against engagement uplift.

---

## ✅ Applied Question: News site — Prioritizing Features for A/B Testing

Prioritize based on:
1. **Expected business impact**:
   - Signup page changes may affect acquisition (high impact).
2. **Ease of implementation**:
   - Header and home button may be simpler and low-risk.
3. **User journey priority**:
   - Signup > Newsfeed layout > Header > Home button.

Start with high-impact, low-effort changes and proceed iteratively.

---

## ✅ Four variations, one p-value < 0.05 — Should we make the change?

Not immediately.

- You’re performing **multiple comparisons**, which increases the false positive rate.
- Apply corrections (e.g., **Bonferroni**, **Holm**, **False Discovery Rate**) before trusting significance.
- Confirm effect size and reproducibility.
- Consider re-running with the top two variants in a focused A/B test.

---

## ✅ Applied Question: Food delivery — Managing spillover between groups

To manage spillover:

1. **User-level randomization**: Avoid household or network contamination.
2. **Geographical or network clustering**: Assign entire areas or communities to treatment/control to prevent cross-exposure.
3. **Track sharing behavior**:
   - Log who shares and who redeems.
   - Analyze indirect treatment effects (network diffusion).
4. **Instrumental variable analysis**:
   - Adjust for endogenous sharing using advanced causal inference.

Document potential spillover in your interpretation to avoid biased results.

---
