# 🐾 Wildlife Observation Trend Analysis

## 📌 Overview

This project analyzes wildlife observation data from the Global Biodiversity Information Facility to identify temporal and geographic patterns in species sightings.

The analysis focuses on three North American species:

* Gray Wolf (*Canis lupus*)
* American Black Bear (*Ursus americanus*)
* Bald Eagle (*Haliaeetus leucocephalus*)

The goal is to explore **how observation patterns change over time and across regions**, while accounting for the limitations of observation-based datasets.

---

## 🎯 Objectives

* Ingest and process large-scale biodiversity data (~750MB)
* Clean and standardize inconsistent real-world data
* Store and query data using MySQL
* Analyze trends in wildlife observations over time
* Identify geographic hotspots for species observations
* Interpret results with awareness of data limitations

---

## 🧱 Tech Stack

* **Python** (Pandas, PyMySQL)
* **MySQL** (data storage, indexing, querying)
* **SQL** (aggregation, normalization, analysis)
* **Matplotlib** (visualization)

---

## 📥 Data Source

* Global Biodiversity Information Facility

GBIF provides **occurrence (observation) data**, which represents recorded sightings or evidence of species at a specific place and time.

> ⚠️ Important: This dataset reflects **observation activity**, not actual population size.

---

## ⚙️ Data Pipeline

### 1. Data Extraction

* Downloaded GBIF occurrence data for selected species
* File size: ~750MB

### 2. Data Processing

* Split large dataset into manageable chunks
* Loaded chunks into MySQL (`gbif_observations` table)

### 3. Data Cleaning

* Standardized inconsistent date formats
* Converted coordinates to numeric values
* Filtered out invalid or incomplete records
* Created cleaned table: `wildlife_observations_clean`

### 4. Database Optimization

* Indexed key fields:

  * `species`
  * `observation_year`
  * `stateProvince`

---

## 📊 Analysis

### Temporal Trends

```sql
SELECT
    species,
    observation_year,
    COUNT(*) AS observations
FROM wildlife_observations_clean
WHERE observation_year BETWEEN 2000 AND 2024
GROUP BY species, observation_year
ORDER BY species, observation_year;
```

### Geographic Distribution

```sql
SELECT
    species,
    stateProvince,
    COUNT(*) AS observations
FROM wildlife_observations_clean
GROUP BY species, stateProvince
ORDER BY observations DESC;
```

---

## 📈 Key Insights

* **Bald Eagles** show strong growth in recorded observations over time, consistent with known conservation recovery trends.
* **Gray Wolves** exhibit fluctuating observation patterns, likely influenced by regional policy and habitat factors.
* **Black Bears** show relatively stable observation patterns across years.

---

## ⚠️ Data Limitations

* GBIF data represents **observations**, not actual population counts.
* Trends may be influenced by:

  * Changes in observation effort
  * Reporting behavior
  * Data availability by year
* Recent-year data (e.g., 2025) may be incomplete and was excluded from analysis.

---

## 🧠 Key Takeaway

This project demonstrates how to work with **large, real-world datasets** and extract meaningful insights while properly accounting for data limitations.

> “Observation trends do not directly represent population changes but can provide valuable signals when interpreted carefully.”

---

## 🚀 Future Improvements

* Integrate conservation status from the IUCN Red List
* Build an interactive dashboard for visualization
* Add geospatial mapping of observation data
* Incorporate additional environmental or population datasets

---

## 📂 Project Structure

```
WildlifePopulationAnalysis/
│
├── data/
│   ├── raw/
│   └── chunks/
│
├── scripts/
│   ├── chunk_splitter.py
│   ├── mysql_db.py
│   └── analysis.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── README.md
└── requirements.txt
```

---

## 💼 Portfolio Value

This project highlights:

* Large-scale data handling
* Data cleaning and transformation
* SQL-based analysis
* Understanding of real-world data limitations
* Ability to communicate insights clearly

---

## 📬 Contact

Feel free to connect or reach out for collaboration or questions.
