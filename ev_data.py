import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="EVProject"
)

query = "SELECT * FROM ElectricCarData"

df = pd.read_sql(query, conn)

df.to_csv("ev_data.csv", index=False)

print(df)

conn.close()