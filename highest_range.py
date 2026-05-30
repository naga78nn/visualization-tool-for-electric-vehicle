import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="EVProject"
)

query = """
SELECT Brand, Model, Range_Km
FROM ElectricCarData
ORDER BY Range_Km DESC;
"""

df = pd.read_sql(query, conn)

df.to_csv("highest_range.csv", index=False)

print(df)

conn.close()