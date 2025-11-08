import sqlite3
import pandas as pd

#connect to databese(if not exist, will be create)
connection = sqlite3.connect("sales.db")
#for executing SQL commands
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")
#commit changes in database
connection.commit()

#read CSV file and save data to database
df = pd.read_csv('sales.csv')
df.to_sql('Sales', connection, if_exists='replace', index=False)

#display all records from database
all_records = pd.read_sql_query('SELECT * FROM SALES', connection)
print(all_records)
print('\n')

#update record 
record = pd.read_sql_query("SELECT * FROM Sales WHERE name = 'Smartphone Case'", connection)
print(record)
cursor.execute("UPDATE Sales SET price = price * 0.5 WHERE name = 'Smartphone Case'")
connection.commit()
record = pd.read_sql_query("SELECT * FROM Sales WHERE name = 'Smartphone Case'", connection)
print(record)
print('\n')

#remove record
cursor.execute("DELETE FROM Sales WHERE name = 'LED Desk Lamp'")
connection.commit()

record = pd.read_sql_query("SELECT * FROM Sales WHERE name = 'LED Desk Lamp'", connection)
if record.empty:
    print('Brak rekordu')
else:
    print(record)

connection.close()