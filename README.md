🏦 AutoML Cash Flow Optimization for Insurance Companies
📌 Project Overview

Insurance companies rely heavily on accurate forecasting of medical expenses to manage cash flow, pricing, underwriting, and risk segmentation.
This project builds an AutoML-powered medical cost prediction pipeline and visualizes the results in an interactive Power BI dashboard.

Using patient demographics and health risk factors such as age, BMI, smoking status, gender, region, and dependents, the system predicts future medical insurance charges and highlights key cost drivers.

<img width="1084" height="614" alt="Screenshot 2026-01-20 165605" src="https://github.com/user-attachments/assets/540f7d58-4033-47bc-8f44-9da6a80bddf6" />


The solution combines:

Python (scikit-learn AutoML-style model comparison)

Feature engineering

Explainable predictions

Power BI analytics & visualization

🎯 Business Objective

Improve cash flow forecasting accuracy

Identify high-risk / high-cost customer segments

Support data-driven pricing and underwriting decisions

Enable executive-level visibility through dashboards

🧠 Machine Learning Approach
🔹 Dataset

Medical Cost Personal Dataset

Source: Kaggle
https://www.kaggle.com/datasets/mirichoi0218/insurance

🔹 Features Used

Age

Sex

BMI

Number of Children

Smoking Status

Region

🔹 Engineered Features

Age Group: Young, Adult, Middle Aged, Senior

BMI Category: Underweight, Normal, Overweight, Obese

🔹 Models Evaluated (AutoML-style)

Linear Regression

Ridge Regression

Random Forest Regressor

Gradient Boosting Regressor

🔹 Model Selection Metric

RMSE (Root Mean Squared Error) via cross-validation

The model with the lowest RMSE is automatically selected and used for final predictions.

⚙️ Technology Stack
Layer	Tools
Data Processing	Python, Pandas, NumPy
Machine Learning	scikit-learn (pipelines, preprocessing, CV)
Feature Engineering	pandas, sklearn transformers
Visualization	Power BI Desktop
Export Format	Excel (.xlsx)
Environment	Python 3.12, uv
🗂️ Project Structure
📁 AutoML-Cashflow-Insurance
│
├── main.py                         # End-to-end ML pipeline
├── insurance.xlsx                  # Raw dataset
├── insurance_predictions_powerbi.xlsx  # Model output for Power BI
├── Cash Flow.pbix                  # Power BI dashboard file
├── README.md                       # Project documentation

🧪 Machine Learning Pipeline (Python)

Load and clean dataset

Engineer age and BMI categories

Build preprocessing pipeline

StandardScaler for numeric features

OneHotEncoder for categorical features

Compare multiple regression models using cross-validation

Select best model automatically

Train final model

Generate predictions and error metrics

Export results for Power BI visualization

📊 Power BI Dashboard Overview
🔹 Dashboard Title

AutoML Cash Flow & Medical Cost Forecast Dashboard

🔹 KPIs

Total Actual Charges

Total Predicted Charges

Average Prediction Error

Prediction Accuracy %

🔹 Visuals

Bar Charts

Predicted Charges by Age Group

Predicted Charges by BMI Category

Bubble Chart

BMI vs Predicted Charges

Bubble size = cost

Color = smoker / non-smoker

Validation Table

Actual vs Predicted charges

Conditional formatting to highlight outliers

Slicers

Region

Gender

Smoking status

Age group

BMI category

Numeric sliders for Age & BMI

🎨 Dashboard Design Principles

Clear Actual vs Predicted color separation

Red–green gradients to instantly highlight risk and errors

Executive-friendly layout:
Summary → Drivers → Interaction → Validation

📈 Key Insights Enabled

Smokers and obese patients show significantly higher predicted costs

Age and BMI are strong cost drivers

Model enables early detection of high-cash-outflow segments

Improves transparency and explainability of predictions

🚀 How to Run the Project
1️⃣ Run Python Model
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

Data science portfolio project

🏁 Conclusion

This project demonstrates how AutoML-style model selection, combined with Power BI storytelling, can transform raw healthcare data into actionable financial intelligence for insurance companies.
