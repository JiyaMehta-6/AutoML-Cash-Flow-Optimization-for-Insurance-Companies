<h1 align="center">🏦 AutoML Cash Flow Optimization for Insurance Companies</h1>

<p align="center">
  <b>Predicting medical insurance costs using machine learning & Power BI</b><br>
  <sub>From raw healthcare data → financial intelligence for decision-makers</sub> 
</p>

<img width="1081" height="608" alt="Screenshot 2026-01-20 170547" src="https://github.com/user-attachments/assets/1e138343-ca48-42a2-9ae1-5e9f8475972f" />

---

## 📌 Overview

> **Insurance is a cash-flow problem disguised as a healthcare problem.**

Insurance companies operate on thin margins where forecasting accuracy matters more than raw scale. Even small prediction errors—when multiplied across millions of policyholders—can translate into massive unexpected payouts.

This project builds an **AutoML-style machine learning pipeline** to predict medical insurance charges using demographic and health risk factors, then translates those predictions into **executive-ready insights** via an interactive **Power BI dashboard**.

### 🔍 What this enables
- 📈 More accurate forecasting of future liabilities  
- 🚨 Early identification of high-risk, high-cost customers  
- 💼 Data-driven pricing, underwriting, and risk segmentation  
- 📊 Business-friendly ML outputs for non-technical stakeholders  

---

## 🎯 Business Objectives

✔ Improve cash flow forecasting accuracy  
✔ Detect high-risk / high-cost policyholders  
✔ Enable data-driven pricing and underwriting  
✔ Deliver executive-ready visual insights  

---

## 🧠 Machine Learning Strategy

### 📂 Dataset
**Medical Cost Personal Dataset**  
Source: Kaggle  
🔗 https://www.kaggle.com/datasets/mirichoi0218/insurance

---

### 🔍 Features Used
- **Age**
- **Sex**
- **BMI**
- **Number of Children**
- **Smoking Status**
- **Region**

---

### 🧩 Feature Engineering

To improve **interpretability** and **model performance**, raw variables are transformed into business-friendly categories:

- **Age Group** → Young | Adult | Middle-Aged | Senior  
- **BMI Category** → Underweight | Normal | Overweight | Obese  

These groupings allow stakeholders to reason about risk **without reading coefficients**.

---

## 🤖 AutoML-Style Model Selection

Rather than committing to a single model upfront, the pipeline evaluates multiple regression models automatically using cross-validation:

- Linear Regression  
- Ridge Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  

**Model selection criterion**  
> 📉 **Root Mean Squared Error (RMSE)**

The model with the **lowest RMSE** is selected and trained as the final predictor.

---

## ⚙️ Technology Stack

| Layer | Tools |
|------|------|
| 🧹 Data Processing | Python, Pandas, NumPy |
| 🤖 Machine Learning | scikit-learn (pipelines, preprocessing, CV) |
| 🧠 Feature Engineering | pandas, sklearn transformers |
| 📊 Visualization | Power BI Desktop |
| 📦 Output | Excel (.xlsx) |
| 🐍 Environment | Python 3.12, `uv` |

---

## 🧪 Machine Learning Pipeline

Raw Data
↓
Feature Engineering
↓
Preprocessing Pipeline
↓
Model Comparison (CV)
↓
Best Model Selection
↓
Final Training
↓
Predictions + Metrics
↓
Power BI Dashboard


**Key components**
- `StandardScaler` for numeric variables  
- `OneHotEncoder` for categorical variables  
- Cross-validation for fair model comparison  

---

## 📊 Power BI Dashboard

### 🏷 Dashboard Title
**AutoML Cash Flow & Medical Cost Forecast Dashboard**

---

### 📌 Executive KPIs
- **Total Actual Charges**
- **Total Predicted Charges**
- **Average Prediction Error**
- **Prediction Accuracy (%)**

---

### 📈 Visual Analytics

**Cost Drivers**
- Predicted Charges by **Age Group**
- Predicted Charges by **BMI Category**

**Risk Interaction**
- **BMI vs Predicted Charges** (Bubble Chart)  
  - Bubble size → cost magnitude  
  - Color → smoker vs non-smoker  

**Model Validation**
- Actual vs Predicted Charges  
- Conditional formatting to highlight outliers  

---

### 🎛 Interactive Controls
- Region  
- Gender  
- Smoking Status  
- Age Group  
- BMI Category  
- Numeric sliders for Age and BMI  

---

### 🎨 Design Principles
- Clear separation of **Actual vs Predicted** values  
- Red–green gradients for instant risk detection  
- Executive storytelling flow:  
  **Summary → Cost Drivers → Risk Interaction → Validation**

---

## 📈 Key Insights

> **The model doesn’t just predict costs — it explains where risk comes from.**

- 🚬 Smokers show significantly higher predicted medical costs  
- ⚖ Obesity is a dominant cost driver across all age groups  
- ⏳ Age and BMI strongly influence long-term insurance liabilities  
- 💸 High cash-outflow segments can be identified *before* losses occur  

---

## 🧾 Use Cases

- **Insurance Underwriting**  
  Risk-based evaluation of policyholders using predicted medical costs.

- **Premium Pricing Optimization**  
  Data-driven premium adjustments aligned with customer risk profiles.

- **Financial Forecasting**  
  Improved cash flow and liability forecasting at scale.

- **Healthcare Risk Analytics**  
  Identification of cost drivers across demographic and health dimensions.

- **Data Science / Analytics Portfolio**  
  End-to-end example of machine learning translated into business impact.

---

## 🏁 Conclusion

This project demonstrates how **AutoML-style model selection**, paired with **Power BI storytelling**, can turn healthcare data into **clear financial intelligence**.

It bridges the gap between machine learning and business strategy—making predictive analytics **understandable**, **explainable**, and **actionable** for decision-makers.

> *The universe may be stochastic. Cash flow doesn’t have to be.* 💸📊



