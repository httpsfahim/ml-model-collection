import pandas as pd
import random
data = []

for i in range(100):
    study = random.randint(1, 10)
    attendance = random.randint(1,100)
    sleep = random.randint(2,10)
    prev = random.randint(1,100)
    assignment = random.randint(1,100)

    final = (study * 0.4) + (attendance * 0.2) + (sleep * 0.1) + (prev * 0.2) + (assignment * 0.1)
    final = int(max(0,min(100, final)))
    data.append([study, attendance, sleep, prev, assignment, final])


dataframe = pd.DataFrame(data, columns=['Study Hours', 'Attendance', 'Sleep Hours', 'Previous Scores', 'Assignment Scores', 'Final Score'])


dataframe.to_csv('student_performance.csv', index=False)