from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
X = [
    ['Young', 'High', 'No'],
    ['Young', 'High', 'No'],
    ['Middle', 'High', 'No'],
    ['Senior', 'Medium', 'No'],
    ['Senior', 'Low', 'Yes'],
    ['Middle', 'Low', 'Yes']
]

y = ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes']

# Separate columns
ages = [row[0] for row in X]
income = [row[1] for row in X]
student = [row[2] for row in X]

# Create encoders
le_age = LabelEncoder()
le_income = LabelEncoder()
le_student = LabelEncoder()
le_buy = LabelEncoder()

# Fit encoders ONCE on full data
ages_enc = le_age.fit_transform(ages)
income_enc = le_income.fit_transform(income)
student_enc = le_student.fit_transform(student)

# Combine encoded features
X_encoded = list(zip(ages_enc, income_enc, student_enc))
y_encoded = le_buy.fit_transform(y)

# Train Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X_encoded, y_encoded)

# Test data
test = ['Young', 'Medium', 'Yes']
test_encoded = [[
    le_age.transform([test[0]])[0],
    le_income.transform([test[1]])[0],
    le_student.transform([test[2]])[0]
]]

# Prediction
prediction = model.predict(test_encoded)

print("Test Data :", test)
print("Prediction:", "Yes" if prediction[0] == 1 else "No")
