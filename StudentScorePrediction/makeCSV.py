import pandas as pd
import random

data = []

for _ in range(100):
    study = random.randint(1, 10)
    attendance = random.randint(45, 100)
    sleep = random.randint(4, 10)
    prev = random.randint(33, 100)

    final_score = int(
        (study * 3) +
        (attendance * 0.2) +
        (sleep * 1.5) +
        (prev * 0.4) +
        random.randint(-5, 5)
    )

    final_score = max(1, min(100, final_score))

    data.append([study, attendance, sleep, prev, final_score])

df = pd.DataFrame(data, columns=[
    "study_hours",
    "attendance",
    "sleep_hours",
    "previous_score",
    "final_score"
])

df.to_csv("student_data.csv", index=False)

print("CSV file created successfully as student_data.csv")
print(df.head())
print(df.shape)