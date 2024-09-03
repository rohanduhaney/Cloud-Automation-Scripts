import pandas as pd

# Load the dataset
data = pd.read_csv('raw_data.csv')  # Replace with your actual dataset

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values with the mean
data.fillna(data.mean(), inplace=True)

# Remove any rows with NaN values
data.dropna(inplace=True)

# Convert categorical variables to numeric
data = pd.get_dummies(data)

# Save the cleaned data
data.to_csv('cleaned_data.csv', index=False)

print("Data cleaned and saved as 'cleaned_data.csv'")
