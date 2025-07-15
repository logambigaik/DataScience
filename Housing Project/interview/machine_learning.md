# 📘 Machine Learning Interview Questions

## ❓ What is the bias/variance trade-off?

The **bias/variance trade-off** explains the tension between two types of errors that affect model performance:

- **Bias**: Error from overly simplistic assumptions. High bias causes **underfitting**.
- **Variance**: Error from model complexity. High variance causes **overfitting**.

> The goal is to balance bias and variance to minimize total error and improve generalization to new data.

---

## 🤖 What are the different types of machine learning, with examples?

1. **Supervised Learning**
   - **Definition**: Learning from labeled data.
   - **Example**: Predicting house prices using **Linear Regression**.

2. **Unsupervised Learning**
   - **Definition**: Learning patterns from unlabeled data.
   - **Example**: Customer segmentation with **K-Means Clustering**.

3. **Semi-Supervised Learning**
   - **Definition**: Uses a small labeled dataset with a larger unlabeled dataset.
   - **Example**: Classifying text documents where only a portion is labeled.

4. **Reinforcement Learning**
   - **Definition**: Learning through trial and error to maximize rewards.
   - **Example**: Game playing agents using **Q-Learning** or **Deep Q-Networks (DQN)**.

---

## ⭐ What is your favorite algorithm and how does it work?

**Favorite Algorithm**: **Random Forest**

**Why?**  
- Versatile and performs well with little tuning.
- Handles both classification and regression tasks effectively.

**How it works**:
- It is an **ensemble method** combining multiple decision trees.
- Each tree is trained on a random subset of data and features (bagging).
- Final prediction is based on majority vote (classification) or average (regression).
- Reduces variance and prevents overfitting.

---

## 🧠 What is the difference between neural networks and other types of ML algorithms?

| Feature         | Neural Networks                            | Traditional ML Algorithms             |
|-----------------|---------------------------------------------|----------------------------------------|
| **Structure**   | Layers of interconnected neurons            | Often based on simple mathematical models |
| **Use Case**    | Image, audio, and text (unstructured data)  | Tabular data and simpler problems      |
| **Complexity**  | Can model complex nonlinear functions        | May require feature engineering        |
| **Training**    | Data and compute-intensive                  | Less resource-intensive                |
| **Examples**    | CNNs, RNNs, Transformers                     | SVM, Logistic Regression, Decision Trees |

---
