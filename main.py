import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the dataset
df = pd.read_csv('heart_disease_data.csv')

# Define the target variable and features
X = df.drop('target', axis=1)  # Features
y = df['target']                # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Function to make predictions
def predict_health():
    try:
        # Get input values from the user
        inputs = [
            int(age_entry.get()),
            int(sex_entry.get()),
            int(cp_entry.get()),
            int(trestbps_entry.get()),
            int(chol_entry.get()),
            int(fbs_entry.get()),
            int(restecg_entry.get()),
            int(thalach_entry.get()),
            int(exang_entry.get()),
            float(oldpeak_entry.get()),
            int(slope_entry.get()),
            int(ca_entry.get()),
            int(thal_entry.get())
        ]
        
        # Convert inputs to numpy array
        new_data = np.array([inputs])
        
        # Make prediction
        prediction = model.predict(new_data)
        
        # Display result
        if prediction[0] == 0:
            messagebox.showinfo("Prediction Result", "The person is healthy.")
        else:
            messagebox.showwarning("Prediction Result", "The person is not healthy. Consult your doctor.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input values.")

# Create the main window
root = tk.Tk()
root.title("Heart Disease Prediction")

# Create input fields
tk.Label(root, text="Age:").grid(row=0, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1)

tk.Label(root, text="Sex (1=male, 0=female):").grid(row=1, column=0)
sex_entry = tk.Entry(root)
sex_entry.grid(row=1, column=1)

tk.Label(root, text="Chest Pain Type (0-3):").grid(row=2, column=0)
cp_entry = tk.Entry(root)
cp_entry.grid(row=2, column=1)

tk.Label(root, text="Resting Blood Pressure:").grid(row=3, column=0)
trestbps_entry = tk.Entry(root)
trestbps_entry.grid(row=3, column=1)

tk.Label(root, text="Cholesterol:").grid(row=4, column=0)
chol_entry = tk.Entry(root)
chol_entry.grid(row=4, column=1)

tk.Label(root, text="Fasting Blood Sugar > 120 mg/dl (1=True, 0=False):").grid(row=5, column=0)
fbs_entry = tk.Entry(root)
fbs_entry.grid(row=5, column=1)

tk.Label(root, text="Resting Electrocardiographic Results (0-2):").grid(row=6, column=0)
restecg_entry = tk.Entry(root)
restecg_entry.grid(row=6, column=1)

tk.Label(root, text="Maximum Heart Rate Achieved:").grid(row=7, column=0)
thalach_entry = tk.Entry(root)
thalach_entry.grid(row=7, column=1)

tk.Label(root, text="Exercise Induced Angina (1=True, 0=False):").grid(row=8, column=0)
exang_entry = tk.Entry(root)
exang_entry.grid(row=8, column=1)

tk.Label(root, text="Oldpeak:").grid(row=9, column=0)
oldpeak_entry = tk.Entry(root)
oldpeak_entry.grid(row=9, column=1)

tk.Label(root, text="Slope (0-2):").grid(row=10, column=0)
slope_entry = tk.Entry(root)
slope_entry.grid(row=10, column=1)

tk.Label(root, text="Number of Major Vessels (0-3):").grid(row=11, column=0)
ca_entry = tk.Entry(root)
ca_entry.grid(row=11, column=1)

tk.Label(root, text="Thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect):").grid(row=12, column=0)
thal_entry = tk.Entry(root)
thal_entry.grid(row=12, column=1)

# Create a button to make the prediction
predict_button = tk.Button(root, text="Predict Health Status", command=predict_health)
predict_button.grid(row=13, columnspan=2)

# Start the GUI event loop
root.mainloop()