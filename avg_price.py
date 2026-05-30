import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="EVProject"
)

query = """
SELECT Brand, AVG(PriceEuro) AS AvgPrice
FROM ElectricCarData
GROUP BY Brand
ORDER BY AvgPrice DESC;
"""

df = pd.read_sql(query, conn)

df.to_csv("avg_price.csv", index=False)

print(df)

conn.close()