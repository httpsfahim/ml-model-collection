import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("student_data.csv")
df["final_score"] = df["final_score"].clip(1, 100)

X = df[["study_hours", "attendance", "sleep_hours", "previous_score"]]
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_pred = [max(1, min(100, pred)) for pred in y_pred]

results_df = pd.DataFrame({
    "actual_score": y_test.values,
    "predicted_score": [round(pred, 2) for pred in y_pred]
})

print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

last_five_students = df.tail(5).copy()
last_five_X = last_five_students[["study_hours", "attendance", "sleep_hours", "previous_score"]]
last_five_X_scaled = scaler.transform(last_five_X)

last_five_predictions = []

for i in range(len(last_five_students)):
    predicted_score = model.predict([last_five_X_scaled[i]])[0]
    predicted_score = max(1, min(100, predicted_score))

    student_result = {
        "study_hours": last_five_students.iloc[i]["study_hours"],
        "attendance": last_five_students.iloc[i]["attendance"],
        "sleep_hours": last_five_students.iloc[i]["sleep_hours"],
        "previous_score": last_five_students.iloc[i]["previous_score"],
        "actual_final_score": int(last_five_students.iloc[i]["final_score"]),
        "predicted_final_score": int(round(predicted_score))
    }

    last_five_predictions.append(student_result)

last_five_predictions_df = pd.DataFrame(last_five_predictions)

print("\nTest Results:")
print(results_df)

print("\nPredicted Final Scores for Last 5 Students:")
print(last_five_predictions_df.to_string(index=False))

study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance: "))
sleep_hours = float(input("Enter sleep hours: "))
previous_score = float(input("Enter previous score: "))

new_student = pd.DataFrame([[study_hours, attendance, sleep_hours, previous_score]], columns=[
    "study_hours", "attendance", "sleep_hours", "previous_score"
])

new_student_scaled = scaler.transform(new_student)
prediction = model.predict(new_student_scaled)[0]
prediction = max(1, min(100, prediction))

print("\nPredicted Final Score for New Student:", int(round(prediction)))