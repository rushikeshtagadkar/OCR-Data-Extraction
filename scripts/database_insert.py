import psycopg2
import json

def insert_into_db(json_file):
    """Insert JSON data into PostgreSQL"""
    conn = psycopg2.connect("dbname=patients user=postgres password=root")
    cur = conn.cursor()
    
    with open(json_file, "r") as f:
        data = json.load(f)
    
    cur.execute("INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id;",
                (data["patient_name"], data["dob"]))
    patient_id = cur.fetchone()[0]
    
    cur.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
                (patient_id, json.dumps(data)))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data Inserted Successfully!")

if __name__ == "__main__":
    insert_into_db("extracted_data.json")