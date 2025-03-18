# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.impute import SimpleImputer  # For handling missing values
import kagglehub
import os
import joblib 

# Download the dataset from Kaggle using KaggleHub
path = kagglehub.dataset_download("ruchi798/housing-prices-in-metropolitan-areas-of-india")
print("Path to dataset files:", path)

# Load the dataset
# Assuming the dataset contains a single CSV file named 'Bangalore.csv'
csv_file_path = os.path.join(path, 'Bangalore.csv')  # Update 'data.csv' if the filename is different
data = pd.read_csv(csv_file_path)

# Display basic information about the dataset
print(data.info())
print(data.head())

datacols = pd.read_csv(csv_file_path)
column_names = list(datacols.columns)

# Вывод списка
print(column_names)

new_list = [column_names[i] for i in range(4,8)]

# Data Preprocessing
# Handle missing values marked as '9'
for col in data.columns:
    if data[col].dtype == 'int64' or data[col].dtype == 'float64':
        data[col] = data[col].replace(9, np.nan)

# Drop rows with missing target values
data = data.dropna(subset=['Price'])

# Separate features and target variable
X = data.drop(columns= new_list)  # Features
print(X)
y = data['Price']  # Target variable

# Encode categorical variables
label_encoders = {}
for col in X.columns:
    if X[col].dtype == 'object':
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        label_encoders[col] = le

# Handle missing values in features using SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')  # Replace NaN with the mean of each column
X_imputed = imputer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Feature scaling (optional for tree-based models but useful for logistic regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Baseline Model: Predict the Mean of the Target Variable
baseline_pred = np.full_like(y_test, fill_value=y_train.mean())  # Predict the mean of y_train
baseline_mse = mean_squared_error(y_test, baseline_pred)
baseline_mae = mean_absolute_error(y_test, baseline_pred)
baseline_r2 = r2_score(y_test, baseline_pred)

print(f"Baseline Model - MSE: {baseline_mse:.2f}, MAE: {baseline_mae:.2f}, R2: {baseline_r2:.2f}")

# Model Training
models = {
    "Random Forest": RandomForestRegressor(random_state=42),
    "CatBoost": CatBoostRegressor(verbose=0, random_state=42),
    "XGBoost": XGBRegressor(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000)
}

# Train and evaluate each model
results = {}
for name, model in models.items():
    print(f"Training {name}...")
    
    # Train the model
    if name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)  # Use scaled data for Logistic Regression
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)  # Use imputed data for other models
        y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'MSE': mse, 'MAE': mae, 'R2': r2}
    print(f"{name} - MSE: {mse:.2f}, MAE: {mae:.2f}, R2: {r2:.2f}")

# Display results
print("\nModel Performance:")
print(f"Baseline Model: MSE = {baseline_mse:.2f}, MAE = {baseline_mae:.2f}, R2 = {baseline_r2:.2f}")
for model_name, metrics in results.items():
    print(f"{model_name}: MSE = {metrics['MSE']:.2f}, MAE = {metrics['MAE']:.2f}, R2 = {metrics['R2']:.2f}")
best_model_name = max(results, key=lambda k: results[k]['R2'])
best_model = models[best_model_name]
print(f"\nBest Model: {best_model_name}")

model_filename = "best_model.pkl"
joblib.dump(best_model, model_filename)
print(f"Best model saved as '{model_filename}'")

label_encoders_filename = "label_encoders.pkl"
joblib.dump(label_encoders, label_encoders_filename)
print(f"LabelEncoders saved as '{label_encoders_filename}'")

# Сохранение Imputer
imputer_filename = "imputer.pkl"
joblib.dump(imputer, imputer_filename)
print(f"Imputer saved as '{imputer_filename}'")

# Сохранение Scaler
scaler_filename = "scaler.pkl"
joblib.dump(scaler, scaler_filename)
print(f"Scaler saved as '{scaler_filename}'")

# Сохранение списка столбцов
original_columns = list(X.columns)  # Список всех признаков
original_columns_filename = "original_columns.pkl"
joblib.dump(original_columns, original_columns_filename)
print(f"Original columns saved as '{original_columns_filename}'")