import pandas as pd
import mysql.connector

# EXTRACT
df = pd.read_csv("students.csv")

print("Original rows:", len(df))

# TRANSFORM
df["marks"] = df["marks"].fillna(df["marks"].mean())
df = df.drop_duplicates(subset=["name"])

print("Cleaned rows:", len(df))

# LOAD: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="etl_project_db"
)

cursor = connection.cursor()

# Prevent duplicate rows when you run the program again
cursor.execute("DELETE FROM students")

# Insert cleaned data
sql = """
INSERT INTO students
(student_id, name, department, marks, city)
VALUES (%s, %s, %s, %s, %s)
"""

for row in df.itertuples(index=False, name=None):
    cursor.execute(sql, row)

connection.commit()

print("Data loaded successfully!")

cursor.close()
connection.close()