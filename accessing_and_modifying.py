# Q)27) Accessing and Modifying the Index of a Series

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 55000, 40000, 70000, 48000]
}

df = pd.DataFrame(data)
print("Accessing the Index:")
print(df.index)  # Accessing the index


# Q)28) Setting a Custom Index

# Set 'Name' column as the index
df_with_index = df.set_index('Name')
print("DataFrame with Custom Index:")
print(df_with_index)


# Q)29) Resetting the Index

# Reset the index back to the default integer index
df_reset = df_with_index.reset_index()
print("DataFrame after Resetting Index:")
print(df_reset)


# Q)30) Index with loc

# Using loc to access a row
row = df_with_index.loc['Alice']
print("Row with index 'Alice':")
print(row)


# Q)31) Changing the Index

# Set 'Age' as the new index
df_with_new_index = df.set_index('Age')
print("DataFrame with 'Age' as Index:")
print(df_with_new_index)