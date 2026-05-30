import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="EVProject"
)

query = """
SELECT Brand, AVG(Efficiency_WhKm) AS AvgEfficiency
FROM ElectricCarData
GROUP BY Brand
ORDER BY AvgEfficiency ASC;
"""

df = pd.read_sql(query, conn)

print(df)

# Save CSV
df.to_csv("top_efficiency.csv", index=False)

print("CSV File Created")

conn.close()