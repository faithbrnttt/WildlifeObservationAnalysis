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
SELECT stateProvince, COUNT(*) AS observations
FROM wildlife_observations_clean
WHERE species = 'Canis lupus'
AND basisOfRecord IN ('HUMAN_OBSERVATION', 'OBSERVATION')
AND observation_year >= 2015
GROUP BY stateProvince
ORDER BY observations;
"""

df = pd.read_sql(query, conn)

# Clean state names and observations
df = df.dropna(subset=["stateProvince"])
df["stateProvince"] = df["stateProvince"].astype(str)
df["observations"] = pd.to_numeric(df["observations"], errors="coerce")
df = df.dropna(subset=["observations"])

# Optional: remove blank-looking state values
df = df[df["stateProvince"].str.strip() != ""]

# Sort for nicer bar chart
df = df.sort_values("observations", ascending=True)

plt.figure(figsize=(10, 12))
plt.barh(df["stateProvince"], df["observations"])

plt.xlabel("Observations")
plt.ylabel("State")
plt.title("Gray Wolf Observations by State")
plt.tight_layout()

plt.show()