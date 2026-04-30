import pandas as pd
import os
import csv

csv.field_size_limit(10_000_000)

input_file = r"E:\Datasets\GW_BB_BE_PopData.csv"
output_dir = r"E:\Datasets\chunks"
chunk_size = 25000

os.makedirs(output_dir, exist_ok=True)

# GBIF Simple is commonly TSV, not comma CSV
separator = "\t"

total_rows = 0
expected_columns = None

try:
    reader = pd.read_csv(
        input_file,
        sep=separator,
        chunksize=chunk_size,
        dtype=str,
        low_memory=False,
        quoting=csv.QUOTE_MINIMAL,
        quotechar='"',
        doublequote=True,
        encoding="utf-8",
        on_bad_lines="error"   # do NOT silently skip
    )

    for i, chunk in enumerate(reader, start=1):

        # Capture expected header from first chunk
        if expected_columns is None:
            expected_columns = list(chunk.columns)
            print(f"Detected {len(expected_columns)} columns:")
            print(expected_columns)

        # Validate headers
        if list(chunk.columns) != expected_columns:
            raise ValueError(f"Header mismatch in chunk {i}")

        chunk_file = os.path.join(output_dir, f"chunk_{i:04d}.csv")

        chunk.to_csv(
            chunk_file,
            index=False,
            header=True,
            encoding="utf-8"
        )

        total_rows += len(chunk)
        print(f"Processed chunk {i}: {len(chunk)} rows | Total: {total_rows}")

except Exception as e:
    print(f"Error: {e}")
    print(f"Total rows processed before error: {total_rows}")