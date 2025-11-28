import pymysql
import pandas as pd

# Database connection (XAMPP, root / no password)
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="genforge_customer_support"
    )

def load_csv_to_db(csv_path="../datasets/faq_bulk.csv"):
    # Read CSV
    df = pd.read_csv(csv_path)

    conn = get_connection()
    cursor = conn.cursor()

    # Insert each row into FAQ table
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO faq (question, answer) VALUES (%s, %s)",
            (row['question'], row['answer'])
        )

    conn.commit()
    conn.close()
    print(f"✅ Loaded {len(df)} FAQ records into genforge_customer_support.faq")

if __name__ == "__main__":
    load_csv_to_db()
