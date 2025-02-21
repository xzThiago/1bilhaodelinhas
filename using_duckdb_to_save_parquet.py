import duckdb
import time

def create_duckdb():
    result = duckdb.sql("""
                        SELECT 
                            station,
                            MIN(temperature) AS min_temperature,
                            AVG(temperature) AS mean_temperature,
                            MAX(temperature) AS max_temperature
                        FROM read_csv("data/measurements10M.txt", AUTO_DETECT=FALSE, sep=';', columns={'station': 'VARCHAR', 'temperature': 'DECIMAL(3,1)'}, encoding='utf-8')
                        GROUP BY station
                        ORDER BY station
                    """)
    
    result.show()

    # save the result to a Parquet file
    result.write_parquet('data/measurements_summary.parquet')


if __name__ == "__main__":
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")