import pandas as pd
import mysql.connector

# Define your MySQL database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "test"
}

# Read the CSV file into a pandas DataFrame
csv_file = "XSMB.csv"
df = pd.read_csv(csv_file)
print(df)

dataType = df.dtypes
print(dataType)

values = (int(df['Ket Qua'][0]),)

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Specify the table name where you want to insert the data
table_name = "ketquaxoso"

# Insert data into the MySQL table
# This assumes the columns in the CSV match the columns in the MySQL table
for index, row in df.iterrows():
    values = (int(row['Ket Qua']),)  # Convert "Ket Qua" data to int and keep it as a tuple
    insert_query = f"INSERT INTO {table_name} (`Ket_Qua`) VALUES (%s)"
    cursor.execute(insert_query, values)


# Close the database connection
conn.commit()
conn.close()

print("Data inserted successfully.")