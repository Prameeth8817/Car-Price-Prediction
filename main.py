# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv('data/quikr_car.csv')

# Data Preprocessing
data['Year'] = data['Year'].astype(int)
data = data[data['Price'] != 'Ask for Price']
data['Price'] = data['Price'].str.replace(',', '').astype(int)
data['Kms_Driven'] = data['Kms_Driven'].str.split(' ').str[0].str.replace(',', '').astype(int)
data['Fuel_Type'].fillna('Petrol', inplace=True)

# Remove outliers
data = data[data['Price'] < data['Price'].quantile(0.95)]

# Data visualization
plt.figure(figsize=(10, 5))
sns.barplot(x='Company', y='Price', data=data)
plt.xticks(rotation=90)
plt.title('Car Company vs Price')
plt.savefig('visualizations/company_vs_price.png')
plt.show()

# Feature selection and model training
X = data[['Year', 'Kms_Driven', 'Fuel_Type']]
y = data['Price']

# One-hot encoding for categorical data
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X[['Fuel_Type']]).toarray()

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X[['Year', 'Kms_Driven']], y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
r2 = r2_score(y_test, y_pred)
print(f'R-squared Score: {r2}')

# Example prediction
example = pd.DataFrame({'Year': [2006], 'Kms_Driven': [5100], 'Fuel_Type': ['Petrol']})
predicted_price = model.predict(example[['Year', 'Kms_Driven']])
print(f'Predicted price for Toyota Corolla 2006: {predicted_price}')
