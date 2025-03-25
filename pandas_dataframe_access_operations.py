# Q)32) Pandas DataFrame Access Operations

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 55000, 40000, 70000, 48000]
}

df = pd.DataFrame(data)

# Display the entire DataFrame
print("Complete DataFrame:")
print(df)


# Q)33) Accessing a Column from a DataFrame

# Access the 'Age' column
age_column = df['Age']
print("Age Column:")
print(age_column)


# Q)34) Accessing Rows by Index

# Access the row at index 1 (second row)
second_row = df.iloc[1]
print("Row at Index 1:")
print(second_row)


# Q)35) Accessing Multiple Rows or Columns

# Access the first three rows and the 'Name' and 'Age' columns
subset = df.loc[0:2, ['Name', 'Age']]
print("Subset of DataFrame:")
print(subset)


# Q)36) Accessing Rows Based on a Condition

# Access rows where 'Age' is greater than 25
filtered_data = df[df['Age'] > 25]
print("Rows where Age > 25:")
print(filtered_data)


# Q)37) Accessing Specific Cells with at and iat

# Access the 'Salary' of the row with label 2
salary_at_index_2 = df.at[2, 'Salary']
print("Salary at Index 2:", salary_at_index_2)