import pandas as pd
import matplotlib.pyplot as plt
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="faith123",
    database="wildlife_conservation"
)

query = """
SELECT species, observation_year, COUNT(*) as observations
FROM wildlife_observations_clean
WHERE observation_year BETWEEN 2000 AND 2024
GROUP BY species, observation_year
ORDER BY species, observation_year;
"""

df = pd.read_sql(query, conn)

pivot = df.pivot(index="observation_year", columns="species", values="observations")

pivot.plot(figsize=(10,6))
plt.title("Wildlife Observation Trends (2000–2024)")
plt.ylabel("Observation Count")
plt.xlabel("Year")
plt.show()