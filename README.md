🏦 AutoML Cash Flow Optimization for Insurance Companies

Predicting medical insurance costs using machine learning & Power BI

📌 Overview

Insurance companies operate on thin margins where accurate cash flow forecasting is critical. Small prediction errors at scale can translate into millions in unexpected payouts.

This project builds an AutoML-style machine learning pipeline to predict medical insurance charges using patient demographics and health risk factors, and presents the results through an interactive Power BI dashboard designed for business decision-makers.

The solution enables insurers to:

Forecast future liabilities more accurately

Identify high-risk, high-cost customer segments

Support pricing, underwriting, and risk segmentation decisions

<p align="center"> <img width="1084" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/540f7d58-4033-47bc-8f44-9da6a80bddf6" /> </p>
🎯 Business Objectives

Improve cash flow forecasting accuracy

Detect high-risk / high-cost policyholders

Enable data-driven pricing and underwriting

Provide executive-ready visual insights

🧠 Machine Learning Strategy
📂 Dataset

Medical Cost Personal Dataset

Source: Kaggle
https://www.kaggle.com/datasets/mirichoi0218/insurance

🔍 Features Used

Age

Sex

BMI

Number of Children

Smoking Status

Region

🧩 Feature Engineering

To improve interpretability and model performance:

Age Group: Young, Adult, Middle Aged, Senior

BMI Category: Underweight, Normal, Overweight, Obese

🤖 AutoML-Style Model Comparison

Multiple regression models are evaluated automatically using cross-validation:

Linear Regression

Ridge Regression

Random Forest Regressor

Gradient Boosting Regressor

Model selection criterion:

Root Mean Squared Error (RMSE)

The model with the lowest RMSE is selected and trained as the final predictor.

⚙️ Technology Stack
Layer	Tools
Data Processing	Python, Pandas, NumPy
Machine Learning	scikit-learn (pipelines, preprocessing, CV)
Feature Engineering	pandas, sklearn transformers
Visualization	Power BI Desktop
Output Format	Excel (.xlsx)
Environment	Python 3.12, uv
🧪 Machine Learning Pipeline

Load and clean raw insurance data

Engineer age and BMI categories

Build preprocessing pipeline

StandardScaler for numeric variables

OneHotEncoder for categorical variables

Compare multiple regression models using cross-validation

Automatically select best-performing model

Train final model on full dataset

Generate predictions and error metrics

Export results for Power BI visualization

📊 Power BI Dashboard
🏷️ Dashboard Title

AutoML Cash Flow & Medical Cost Forecast Dashboard

📌 Key Performance Indicators

Total Actual Charges

Total Predicted Charges

Average Prediction Error

Prediction Accuracy (%)

📈 Visual Analytics

Bar Charts

Predicted Charges by Age Group

Predicted Charges by BMI Category

Bubble Chart

BMI vs Predicted Charges

Bubble size represents cost magnitude

Color differentiates smoker vs non-smoker

Validation Table

Actual vs Predicted Charges

Conditional formatting to highlight outliers

Interactive Slicers

Region

Gender

Smoking Status

Age Group

BMI Category

Numeric sliders for Age and BMI

🎨 Design Principles

Clear visual separation of Actual vs Predicted values

Red–green gradients to instantly highlight risk and error

Executive-friendly flow:
Summary → Cost Drivers → Risk Interaction → Model Validation

📈 Key Insights

Smokers consistently exhibit significantly higher predicted medical costs

Obesity is a major cost driver across all age groups

Age and BMI strongly influence insurance liabilities

The model enables early identification of high cash-outflow segments

🚀 How to Run the Project
1️⃣ Run the Machine Learning Pipeline
uv run main.py


This generates:

insurance_predictions_powerbi.xlsx

2️⃣ Open Power BI

Load the generated Excel file

Open Cash Flow.pbix

Refresh data

Explore interactive insights

🧾 Use Cases

Insurance underwriting

Premium pricing optimization

Financial forecasting

Healthcare risk analytics

Data science / analytics portfolio project

🏁 Conclusion

This project demonstrates how AutoML-style model selection, combined with Power BI storytelling, can transform raw healthcare data into actionable financial intelligence for insurance companies.

It bridges the gap between machine learning outputs and business decision-making, making predictive analytics accessible to non-technical stakeholders.
