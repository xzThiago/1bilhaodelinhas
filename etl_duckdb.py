import duckdb
import time

def create_duckdb():
    duckdb.sql("""
    SELECT 
        cidade,
        min(temperatura) as temperatura_minima,
        avg(temperatura) as temperatura_media,
        max(temperatura) as temperatura_maxima
    FROM read_csv("data/measurements10M.txt", AUTO_DETECT=FALSE, sep=';', columns={'cidade':VARCHAR, 'temperatura': 'DECIMAL(3,1)'}) 
    GROUP BY cidade
    ORDER BY cidade
    """).show()

if __name__ == "__main__":
    import time
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")
