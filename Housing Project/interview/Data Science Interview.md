# Data Science Interview Responses

---

## ✅ What is lifetime value and how can you measure it?

**Customer Lifetime Value (CLV or LTV)** is the **total revenue** or **profit a company expects to earn from a customer over the entire duration of their relationship**.

### How to measure it:
- **Simple formula (historical):**  
  LTV = Average Order Value × Purchase Frequency × Customer Lifespan

- **Predictive LTV (more advanced):**
  - Use cohort analysis and regression models (e.g., BG/NBD model).
  - Include features like user behavior, purchase history, and engagement.
  - Optionally discount future value using NPV (Net Present Value).

LTV is crucial for optimizing acquisition cost, retention strategies, and overall marketing ROI.

---

## ✅ Reducing churn by 10%: How would you model susceptibility to churn?

To build a churn prediction model:

1. **Define churn clearly** (e.g., no login/purchase in 30+ days).
2. **Collect features**:
   - Behavioral: session frequency, recency, time on platform.
   - Transactional: purchase volume, frequency.
   - Support interactions, cancellations, NPS.
3. **Feature engineering**:
   - Metrics like days since last login, usage decay, avg session length.
4. **Label users** as churned or not.
5. **Modeling**:
   - Classification algorithms (Logistic Regression, Random Forest, XGBoost).
   - Use SHAP values for interpretability.
6. **Validation**:
   - Use AUC, Precision-Recall, and Confusion Matrix.
   - Backtest on historical data for robustness.

Deploy the model to trigger proactive re-engagement campaigns.

---

## ✅ Measuring the effectiveness of a search feature on an e-commerce site

1. **Define success metrics**:
   - Conversion rate from search.
   - Search Exit Rate.
   - Search Refinement Rate.
   - Time to find product or CTR.
   - Revenue per search.

2. **Compare against benchmarks**:
   - Historical trends or browse-based purchases.

3. **Segment analysis**:
   - Device type, user segment (new vs. returning), query complexity.

4. **Qualitative insights**:
   - Heatmaps, session recordings, surveys.

If redesigning, consider synthetic or sandbox A/B testing.

---

## ✅ Measuring the performance of a song recommendation model

### Key Metrics:
- **Precision@K / Recall@K**
- **MRR / NDCG** for rank-aware accuracy.
- **Coverage**: Catalog variety.
- **Diversity & Novelty**: Exposure to new content.
- **User engagement**: Skips, likes, replays, playlist adds.

### Online metrics:
- Click-through, listen-through, retention after recommendation.
- A/B tests when possible.

Success = Relevance + Satisfaction + Business Value.

---

## ✅ Evaluating the success of a playlist feature (no A/B test)

1. **Metrics**:
   - % of users using playlists.
   - Avg playlist size.
   - Repeat visits/session time after creation.
   - Consumption rate of playlist items.
   - Retention lift among playlist users.

2. **Causal inference**:
   - Propensity score matching.
   - Difference-in-differences analysis.

3. **Cohort analysis**:
   - Track outcomes by playlist adoption date.

4. **Qualitative insights**:
   - Feedback, NPS, adoption funnels.

Combining quantitative and qualitative analysis allows for robust impact evaluation.
