# Interview Answers – Data Visualization & EDA

---

## ✅ What makes a good visualization?

A good visualization is **clear, accurate, and purpose-driven**. It should:
- Communicate insights **quickly and intuitively**.
- Avoid clutter and chartjunk—only show what's needed.
- Use color and scale appropriately (e.g., avoid misleading axes).
- Be **tailored to the audience**—technical for analysts, simplified for business stakeholders.
- Highlight patterns, trends, and outliers that support a **narrative or decision**.

I focus on visualizations that **answer a question**, not just display data.

---

## ✅ What types of charts do you gravitate towards and why?

It depends on the data and context, but generally:

- **Bar charts**: For comparing categories clearly.
- **Line charts**: For trends over time.
- **Box plots**: For distribution and spotting outliers.
- **Heatmaps**: For correlation matrices or density.
- **Scatter plots**: For relationships between numeric variables.

These are effective, minimal, and flexible for most data storytelling needs. I choose charts that **balance simplicity with impact**.

---

## ✅ How would you represent six variables of a dataset?

There are a few strategies, depending on variable types:

1. **Faceting** (e.g., `seaborn.FacetGrid`, `plotly.subplots`): Split into small multiples.
2. **Color, size, shape**: Encode additional variables in a scatter plot.
3. **Interactive dashboards**: Tools like Plotly, Tableau, or Dash let users explore all six dimensions.
4. **Pair plots**: Useful when exploring multiple numeric variables together.
5. **Parallel coordinates plot**: For comparing multivariate patterns.

Ultimately, I'd **prioritize the story** I'm trying to tell and reduce dimensionality (via PCA or clustering) if needed.

---

## ✅ Which tools do you use for EDA and communication?

- **EDA Tools**:
  - `Pandas` and `NumPy` for data manipulation.
  - `Seaborn`, `Matplotlib`, and `Plotly` for visualization.
  - `Sweetviz` and `Pandas-Profiling` for automated EDA.
  - `Scikit-learn` for stats and modeling.

- **Communication Tools**:
  - **Jupyter Notebooks**: Great for combining code, visuals, and narrative.
  - **PowerPoint / Google Slides**: For executive summaries.
  - **Tableau / Power BI**: For interactive, shareable dashboards.
  - **Markdown or PDFs**: For structured written reports.

