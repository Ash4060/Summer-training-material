import  pandas as pd
import numpy as np

# 1.Create a DataFrame of 5 students with columns: name, age, marks and print it.
data = {
    'name': ['Arsh', 'Rahul', 'Preeti', 'Aman', 'Neha'],
    'age': [20, 21, 19, 22, 20],
    'marks': [85, 67, 92, 45, 78]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2.Load a CSV file using Pandas and display the first 5 rows.
df = pd.read_csv("Netflix Dataset.csv")
print(df.head())

# 3.Display only the name and marks columns from the DataFrame.
df = pd.DataFrame(data)
print(df[['name', 'marks']])

# 4. Find students whose marks are greater than 70.
print(df[df['marks'] > 70])

# 5. Sort the DataFrame by marks in descending order.
print(df.sort_values(by='marks', ascending=False))

# 6. Add a new column result where marks ≥ 40 is &quot;Pass&quot; else &quot;Fail&quot;.
df['result'] = df['marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(df)

# 7. Find the average marks of all students.
avg_marks = df['marks'].mean()
print("Average Marks:", avg_marks)

# 8. Find the student with highest marks.
highest = df.loc[df['marks'].idxmax()]
print(highest)

# 9. Count how many students passed the exam.
count_pass = (df['marks'] >= 40).sum()
print("Number of Passed Students:", count_pass)

# 10. Change the index of the DataFrame to the name column.
df.set_index('name', inplace=True)
print(df)

# 11. Read an Excel file and print its column names.
df = pd.read_excel("students.xlsx")
print(df.columns)

# 12. Replace missing values (NaN) in marks with 0.
df['marks'].fillna(0, inplace=True)
print(df)

# 13. Rename column marks to score.
df.rename(columns={'marks': 'score'}, inplace=True)
print(df)

# 14. Delete the age column from the DataFrame.
df.drop('age', axis=1, inplace=True)
print(df)

# 15. Save the updated DataFrame to a new CSV file.
df.to_csv("updated_students.csv", index=False)
print("File saved successfully!")