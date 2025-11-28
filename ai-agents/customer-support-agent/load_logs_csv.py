import pymysql
import pandas as pd

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="genforge_customer_support"
    )

def load_csv_to_logs(csv_path="../datasets/logs_bulk.csv"):
    df = pd.read_csv(csv_path)

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO logs (query, response) VALUES (%s, %s)",
            (row['query'], row['response'])
        )

    conn.commit()
    conn.close()
    print(f"✅ Loaded {len(df)} log records into genforge_customer_support.logs")

if __name__ == "__main__":
    load_csv_to_logs()
