import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# Load the dataset
data = pd.read_csv("Train.csv")
data.rename(columns={'Reached.on.Time_Y.N': 'Reached_on_Time_Y_N'}, inplace=True)


# Data Preprocessing
# Handling missing values, encoding categorical variables, and scaling if necessary
data = data.dropna()  # Remove rows with missing values

# Example encoding categorical features
data['Warehouse_block'] = data['Warehouse_block'].astype('category').cat.codes
data['Mode_of_Shipment'] = data['Mode_of_Shipment'].astype('category').cat.codes
data['Product_importance'] = data['Product_importance'].astype('category').cat.codes
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

# Define features (X) and target variable (y)
X = data.drop('Reached_on_Time_Y_N', axis=1)
y = data['Reached_on_Time_Y_N']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
