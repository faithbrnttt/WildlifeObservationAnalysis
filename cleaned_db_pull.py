import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="faith123",
    database="wildlife_conservation",
    autocommit=True,
    read_timeout=300,
    write_timeout=300
)

batch_size = 50000

with conn.cursor() as cursor:
    cursor.execute("SELECT MIN(id), MAX(id) FROM gbif_observations;")
    min_id, max_id = cursor.fetchone()

    start = min_id

    while start <= max_id:
        end = start + batch_size - 1

        sql = """
            INSERT INTO wildlife_observations_clean (
                raw_id,
                gbifID,
                species,
                event_date,
                observation_year,
                latitude,
                longitude,
                stateProvince,
                country,
                basisOfRecord
            )
            SELECT
                id,
                gbifID,
                species,

                CASE
                    WHEN eventDate REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}' 
                        THEN STR_TO_DATE(LEFT(eventDate, 10), '%%Y-%%m-%%d')
                    WHEN eventDate REGEXP '^[0-9]{4}-[0-9]{2}$'
                        THEN STR_TO_DATE(CONCAT(eventDate, '-01'), '%%Y-%%m-%%d')
                    WHEN eventDate REGEXP '^[0-9]{4}$'
                        THEN STR_TO_DATE(CONCAT(eventDate, '-01-01'), '%%Y-%%m-%%d')
                    ELSE NULL
                END AS event_date,

                CASE
                    WHEN eventDate REGEXP '^[0-9]{4}' 
                        THEN CAST(LEFT(eventDate, 4) AS UNSIGNED)
                    ELSE NULL
                END AS observation_year,

                CAST(decimalLatitude AS DECIMAL(10,6)),
                CAST(decimalLongitude AS DECIMAL(10,6)),
                stateProvince,
                country,
                basisOfRecord
            FROM gbif_observations
            WHERE id BETWEEN %s AND %s
            AND eventDate IS NOT NULL
            AND eventDate != ''
            AND decimalLatitude IS NOT NULL
            AND decimalLatitude != ''
            AND decimalLongitude IS NOT NULL
            AND decimalLongitude != '';
            """

        cursor.execute(sql, (start, end))
        print(f"Inserted raw IDs {start} - {end}")

        start = end + 1

conn.close()
print("Clean load complete.")