from flask import Flask
import psycopg2
import os 

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = "devops_db"
DB_USER = "dbuser"
DB_PASS = "mypassword123"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, time timestamp DEFAULT CURRENT_TIMESTAMP);')
    cur.execute('INSERT INTO visits DEFAULT VALUES;')
    cur.execute('SELECT COUNT(*) FROM visits;')
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return f"<h1>Hello DevOps Pro!</h1><p>This page has been visited {count} times.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)