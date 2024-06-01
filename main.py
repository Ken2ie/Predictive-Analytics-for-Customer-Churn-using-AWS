# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
data = pd.read_csv('customer_churn_dataset.csv')

# Data preprocessing
# One-hot encode categorical variables
data_encoded = pd.get_dummies(data)

# Split data into features and target variable
X = data_encoded.drop('churn_Yes', axis=1)  # Adjusted column name to 'churn_Yes'
y = data_encoded['churn_Yes']  # Adjusted column name to 'churn_Yes'

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
