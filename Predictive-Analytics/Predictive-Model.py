import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('data.csv')  # Replace with your actual dataset

# Prepare the data
X = data[['feature1', 'feature2', 'feature3']]  # Replace with your actual features
y = data['target']  # Replace with your actual target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Save the model
import joblib
joblib.dump(model, 'predictive_model.pkl')

print("Predictive model saved as 'predictive_model.pkl'")
