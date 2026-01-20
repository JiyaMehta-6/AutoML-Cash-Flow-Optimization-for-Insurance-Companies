# -----------------------------------------------
# Insurance Cost Prediction – AutoML Style
# Python 3.12 + scikit-learn
# -----------------------------------------------

import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_excel("insurance.xlsx")
df.columns = df.columns.str.lower().str.strip()  # clean column names

# -----------------------------
# 2. Feature engineering
# -----------------------------
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 25, 40, 60, 100],
    labels=['Young', 'Adult', 'Middle Aged', 'Senior']
)

df['bmi_category'] = pd.cut(
    df['bmi'],
    bins=[0, 18.5, 25, 30, 100],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)

df = df.dropna().reset_index(drop=True)

# Features & target
X = df.drop(columns=['charges'])
y = df['charges']

# -----------------------------
# 3. Preprocessing
# -----------------------------
numeric_features = ['age', 'bmi', 'children']
categorical_features = ['sex', 'smoker', 'region', 'age_group', 'bmi_category']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# -----------------------------
# 4. Models to compare
# -----------------------------
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=200, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42)
}

results = {}

# -----------------------------
# 5. AutoML loop
# -----------------------------
for name, model in models.items():
    pipeline = Pipeline([
        ('preprocess', preprocessor),
        ('model', model)
    ])

    rmse = -cross_val_score(
        pipeline, X, y, cv=5, scoring='neg_root_mean_squared_error'
    ).mean()

    results[name] = rmse
    print(f"{name}: RMSE = {rmse:.2f}")

# -----------------------------
# 6. Select best model
# -----------------------------
best_model_name = min(results, key=results.get)
best_model = models[best_model_name]
print(f"\n🏆 Best Model: {best_model_name}")

# -----------------------------
# 7. Train final model
# -----------------------------
final_pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('model', best_model)
])

final_pipeline.fit(X, y)

# -----------------------------
# 8. Predictions
# -----------------------------
df['Predicted_Charges'] = final_pipeline.predict(X)
df['Prediction_Error'] = abs(df['charges'] - df['Predicted_Charges'])
df['Prediction_Accuracy_%'] = 1 - (df['Prediction_Error'] / df['charges'])

# -----------------------------
# 9. Export predictions to Excel
# -----------------------------
output_file = "insurance_predictions_powerbi.xlsx"
df.to_excel(output_file, index=False)
print(f"\n✅ Exported: {output_file}")

# -----------------------------
# 10. Optional: Feature Importance for Tree Models
# -----------------------------
if hasattr(best_model, "feature_importances_"):
    # Extract feature names from preprocessing
    feature_names = final_pipeline.named_steps['preprocess'].get_feature_names_out()
    importances = best_model.feature_importances_

    fi = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    fi_file = "feature_importance.xlsx"
    fi.to_excel(fi_file, index=False)
    print(f"✅ Feature importance exported: {fi_file}")
