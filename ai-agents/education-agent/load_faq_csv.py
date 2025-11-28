import pymysql
import pandas as pd

def get_connection():
    return pymysql.connect(host="localhost", user="root", password="", database="genforge_education")

def load_csv_to_db(csv_path="../datasets/education_faq.csv"):
    df = pd.read_csv(csv_path)
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO faq (question, answer) VALUES (%s, %s)", (row['question'], row['answer']))
    conn.commit()
    conn.close()
    print(f"✅ Loaded {len(df)} FAQ records into genforge_education.faq")

if __name__ == "__main__":
    load_csv_to_db()
