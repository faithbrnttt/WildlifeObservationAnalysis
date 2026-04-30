import pandas as pd
import os
from sqlalchemy import create_engine

chunk_folder = r"E:\Datasets\chunks"

user = "root"
password = "faith123"
host = "localhost"
database = "wildlife_conservation"

engine = create_engine (
    f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4"
)

needed_columns = [
    "gbifID",
    "species",
    "eventDate",
    "decimalLatitude",
    "decimalLongitude",
    "stateProvince",
    "country",
    "basisOfRecord"
]

for file in os.listdir(chunk_folder):
    if file.endswith(".csv"):
        path = os.path.join(chunk_folder, file)
        
        df = pd.read_csv(path, dtype=str, low_memory=False)
        
        existing_columns = [col for col in needed_columns if col in df.columns]
        
        df = df[existing_columns]
        
        df.to_sql(
            "gbif_observations",
            con=engine,
            if_exists="append",
            index=False,
            chunksize=5000,
            method="multi"
        )
        
        print(f"Loaded {file}: {len(df)} rows")

