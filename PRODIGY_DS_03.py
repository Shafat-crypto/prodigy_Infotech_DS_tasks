# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Creating the dataset
data = {
    'Age': [35, 45, 28, 55, 40, 30],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Income': [50000, 75000, 30000, 90000, 60000, 40000],
    'Education': ['Bachelor', 'Master', 'High School', 'PhD', 'Bachelor', 'High School'],
    'Marital_Status': ['Single', 'Married', 'Single', 'Married', 'Divorced', 'Married'],
    'Purchase': ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Encoding categorical variables
df_encoded = pd.get_dummies(df, columns=['Gender', 'Education', 'Marital_Status'], drop_first=True)

# Splitting features and target variable
X = df_encoded.drop('Purchase', axis=1)
y = df_encoded['Purchase']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Making predictions
y_pred = clf.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
