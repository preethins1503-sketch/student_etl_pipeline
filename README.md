# Student Data ETL Pipeline

## Project Overview
This beginner-friendly Data Engineering project demonstrates the ETL process using student data stored in a CSV file.

## ETL Process

### 1. Extract
Read student data from `students.csv` using Python and Pandas.

### 2. Transform
- Handle missing marks by replacing them with the average marks.
- Remove duplicate student names for this practice dataset.

### 3. Load
Load the transformed data into a MySQL database using Python.

## Technologies Used
- Python
- Pandas
- MySQL
- MySQL Connector
- Git and GitHub

## Project Files
- `etl.py` — ETL pipeline code
- `students.csv` — Input dataset

## What I Learned
- Reading CSV files using Pandas
- Handling missing values
- Removing duplicate records
- Connecting Python to MySQL
- Uploading a project to GitHub using Git

## How to Run
1. Install Python.
2. Install the required packages:
   `pip install pandas mysql-connector-python`
3. Configure your MySQL database and credentials.
4. Run `python etl.py`.

**Note:** This project is for learning and practicing the fundamentals of ETL.
